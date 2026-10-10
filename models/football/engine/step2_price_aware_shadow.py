#!/usr/bin/env python3
"""Prospective price-aware C/C2 gate calibration -- shadow only.

This compares *actual, fresh, independently sourced* Asian Over quotes with
each model's frozen support and alternative goal-burden hypotheses. It never
returns BET/WAIT authority, changes core thresholds, or infers EV from the
uncalibrated researcher goal forecast.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

from core import (
    CarrierStrength, CompletionMode, Grade, RouteStrength, SelectionFloor,
    c2_clearing_goal_funded, c2_selection_floor, clearing_goal_funded, settle_over,
)
from goal_gate_shadow_audit import _snapshot

SCHEMA = "football-step2-price-calibration-shadow-v1"
FRESH_SECONDS = 120
QUOTE_MIN_ODDS = 1.65


class PriceShadowError(ValueError):
    pass


def _time(value: Any, field: str) -> datetime:
    if not isinstance(value, str):
        raise PriceShadowError(f"{field} requires timezone-aware timestamp")
    try:
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise PriceShadowError(f"{field} invalid timestamp") from exc
    if result.utcoffset() is None:
        raise PriceShadowError(f"{field} timezone missing")
    return result.astimezone(timezone.utc)


def _source(value: Any, field: str) -> str:
    if not isinstance(value, str):
        raise PriceShadowError(f"{field} requires HTTPS source")
    p = urlsplit(value)
    if p.scheme != "https" or not p.hostname or "." not in p.hostname or p.username or p.password:
        raise PriceShadowError(f"{field} requires HTTPS source")
    return value


def _number(value: Any, field: str, low: float, high: float) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise PriceShadowError(f"{field} must be numeric")
    x = float(value)
    if not math.isfinite(x) or not low <= x <= high:
        raise PriceShadowError(f"{field} outside valid range")
    return x


def _line(value: Any, field: str) -> float:
    result = _number(value, field, 0, 12)
    if abs(result * 4 - round(result * 4)) > 1e-9:
        raise PriceShadowError(f"{field} requires 0.25 increments")
    return result


def _sha(value: dict) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()).hexdigest()


def _same_epoch_quote(raw: dict, start: datetime, assessment: datetime, ko: datetime) -> dict:
    if not isinstance(raw, dict):
        raise PriceShadowError("quote must be object")
    if raw.get("market_phase") != "PREMATCH":
        raise PriceShadowError("only prematch fresh quotes are supported; run /live for started fixtures")
    line = _line(raw.get("line"), "quote.line")
    odds = _number(raw.get("decimal_odds"), "quote.decimal_odds", 1.001, 1000)
    src = _source(raw.get("source_url"), "quote.source_url")
    captured = _time(raw.get("observed_at_utc"), "quote.observed_at_utc")
    if not start <= captured <= assessment < ko:
        raise PriceShadowError("quote must be observed after independent model freeze and before kickoff")
    if (assessment - captured).total_seconds() > FRESH_SECONDS:
        raise PriceShadowError("stale quote: cannot infer executable market")
    return {"line": line, "decimal_odds": odds, "source_url": src,
            "observed_at_utc": captured.isoformat(), "market_phase": "PREMATCH"}


def _c_shadow_route(a, burden: float) -> bool:
    # Diagnostic-only hypothesis: MEDIUM continuation with strong, sourced
    # two-route shape may deserve market-calibrated study, not a BET.
    if a.material_suppression or a.failure_attacks_route:
        return False
    if a.burden_stall_risk == Grade.HIGH or a.burden_completion_quality != Grade.HIGH:
        return False
    if a.continuation_quality < Grade.MEDIUM or not a.independent_upper_tail:
        return False
    if a.carrier != CarrierStrength.STRONG or a.route_reliability < Grade.MEDIUM:
        return False
    if a.chance_quality < Grade.MEDIUM or a.failure_resistance < Grade.MEDIUM:
        return False
    two = (
        a.home_route >= RouteStrength.USABLE
        and a.away_route >= RouteStrength.USABLE
        and max(a.home_route, a.away_route) == RouteStrength.STRONG
        and a.opponent_leakage >= Grade.MEDIUM
    )
    if burden < 3:
        return two or a.carrier_self_fund
    # At O3.0+ require two genuinely STRONG routes or carrier self-funding.
    return a.carrier_self_fund or (
        two and a.home_route == RouteStrength.STRONG
        and a.away_route == RouteStrength.STRONG
    )


def _c2_shadow_route(a, burden: float) -> bool:
    floor, _ = c2_selection_floor(a)
    if floor != SelectionFloor.CLEAR or a.material_suppression or a.failure_attacks_route:
        return False
    if a.route_reliability != Grade.HIGH or a.chance_quality < Grade.MEDIUM:
        return False
    if a.failure_resistance < Grade.MEDIUM or not a.independent_upper_tail:
        return False
    two = (a.home_route >= RouteStrength.USABLE
           and a.away_route >= RouteStrength.USABLE
           and max(a.home_route, a.away_route) == RouteStrength.STRONG
           and a.independent_route_quality == Grade.HIGH)
    if burden < 3:
        return two or (a.carrier == CarrierStrength.STRONG and a.carrier_self_fund)
    # Fourth-goal sensitivity: would MEDIUM (rather than HIGH) failure
    # resistance be sufficient with independently HIGH route quality?
    return two and a.carrier == CarrierStrength.STRONG


def _payoff(line: float, odds: float) -> dict:
    # No assumed total-goal distribution! Exact settlement table only.
    ret = []
    for goals in range(0, 10):
        outcome, profit = settle_over(line, goals, odds)
        ret.append({"goals": goals, "settlement": outcome.value,
                    "hypothetical_profit_per_1u": round(profit, 4)})
    full_win = next((r["goals"] for r in ret if r["settlement"] == "WIN"), None)
    return {"full_win_from_total_goals": full_win,
            "at_2_goals": ret[2], "at_3_goals": ret[3],
            "at_4_goals": ret[4], "at_5_goals": ret[5],
            "assumed_probabilities": None, "computed_expected_value": None}


def _model(model: str, raw: Any, match: dict, quotes: list[dict]) -> dict:
    if not isinstance(raw, dict):
        raise PriceShadowError(f"{model} independently frozen snapshot required")
    if raw.get("board_state") not in ("FOCUS", "WATCH", "PASS"):
        raise PriceShadowError(f"{model} board state invalid")
    support = _line(raw.get("supported_line"), f"{model}.supported_line")
    frozen = _time(raw.get("frozen_at_utc"), f"{model}.frozen_at_utc")
    if frozen >= match["assessment"] or frozen >= match["kickoff"]:
        raise PriceShadowError(f"{model} must be frozen before quote assessment and kickoff")
    facts = raw.get("frozen_factors")
    try:
        a = _snapshot(facts, model)
        production = (clearing_goal_funded(a, support) if model == "c"
                      else c2_clearing_goal_funded(a, support))
        trial = (_c_shadow_route(a, support) if model == "c"
                 else _c2_shadow_route(a, support))
    except (KeyError, TypeError, ValueError) as exc:
        raise PriceShadowError(f"{model} model-specific frozen factor evidence invalid: {exc}") from exc
    if raw["board_state"] != "FOCUS":
        trial = False
    rows = []
    for q in quotes:
        quoted_support = q["line"] <= support + 1e-9
        at_quote = (clearing_goal_funded(a, min(q["line"], support)) if model == "c"
                    else c2_clearing_goal_funded(a, min(q["line"], support)))
        trial_at_quote = (_c_shadow_route(a, q["line"]) if model == "c"
                          else _c2_shadow_route(a, q["line"]))
        sufficient_price = q["decimal_odds"] >= QUOTE_MIN_ODDS
        candidate = (raw["board_state"] == "FOCUS" and quoted_support
                     and not at_quote and trial_at_quote and sufficient_price
                     and match["integrity_ready"])
        if not quoted_support:
            code = "MARKET_ABOVE_FROZEN_SUPPORT_RECHECK_NO_INFERRED_WAIT"
        elif not match["integrity_ready"]:
            code = "XI_OR_PRIMARY_THESIS_RECHECK_REQUIRED"
        elif not sufficient_price:
            code = "QUOTE_BELOW_COMPARISON_PRICE_FLOOR"
        elif at_quote:
            code = "ALREADY_FUNDED_BY_CURRENT_PRODUCTION_GATE"
        elif trial_at_quote and raw["board_state"] == "FOCUS":
            code = "SHADOW_PRICE_AWARE_ELIGIBILITY_ONLY"
        else:
            code = "BOTH_FUNDING_HYPOTHESES_FAIL"
        rows.append({
            "line": q["line"], "decimal_odds": q["decimal_odds"],
            "observed_at_utc": q["observed_at_utc"],
            "quote_source_url": q["source_url"],
            "line_at_or_below_frozen_support": quoted_support,
            "production_funded_at_effective_burden": at_quote,
            "alternative_shadow_funded_at_quote": trial_at_quote,
            "price_above_1_65_screening_floor": sufficient_price,
            "research_priority_code": code,
            "shadow_price_candidate_for_backtest": candidate,
            "payoff_scenarios": _payoff(q["line"], q["decimal_odds"]),
            "value_established": False,
            "authorised_bet": False,
            "official_or_shadow_action": "UNMODIFIED",
        })
    return {
        "board_state": raw["board_state"], "supported_line": support,
        "funded_at_own_supported_line": production,
        "alternative_shadow_funded_at_own_support": trial,
        "trial_disagrees_with_production": bool(trial and not production),
        "quotes_evaluated": rows,
        "has_current_quoted_shadow_candidate": any(r["shadow_price_candidate_for_backtest"] for r in rows),
        "bet_authorized": False,
        "model_accounting": "NONE",
    }


def compare(payload: dict) -> dict:
    if not isinstance(payload, dict) or payload.get("schema_version") != SCHEMA:
        raise PriceShadowError(f"schema_version must be {SCHEMA}")
    if payload.get("mode") != "PROSPECTIVE_PREMATCH_SHADOW":
        raise PriceShadowError("mode must be PROSPECTIVE_PREMATCH_SHADOW")
    f = payload.get("fixture")
    if not isinstance(f, dict) or not isinstance(f.get("match_id"), str) or not f["match_id"].strip():
        raise PriceShadowError("fixture.match_id missing")
    epoch = f.get("evidence_epoch_id")
    if not isinstance(epoch, str) or not epoch.strip():
        raise PriceShadowError("fixture.evidence_epoch_id missing")
    if f.get("fixture_status") != "PREMATCH_CONFIRMED":
        raise PriceShadowError("not confirmed prematch; use current live route instead")
    ko = _time(f.get("kickoff_utc"), "fixture.kickoff_utc")
    now = _time(f.get("assessment_at_utc"), "fixture.assessment_at_utc")
    if now >= ko:
        raise PriceShadowError("postkickoff assessments must use /live; never backfill")
    integrity = (f.get("xi_status") in ("CONFIRMED", "RELIABLE")
                 and f.get("thesis_state") == "PRESERVED"
                 and f.get("primary_mechanism_intact") is True
                 and f.get("material_veto") is False)
    for key in ("primary_mechanism_intact", "material_veto"):
        if type(f.get(key)) is not bool:
            raise PriceShadowError(f"{key} must be attested true/false")
    forecast = payload.get("forecast_total")
    if forecast is not None:
        forecast = _number(forecast, "forecast_total", 0, 16)
        if not isinstance(payload.get("forecast_frozen_at_utc"), str):
            raise PriceShadowError("forecast freeze required")
        if _time(payload["forecast_frozen_at_utc"], "forecast_frozen_at_utc") >= now:
            raise PriceShadowError("forecast must predate this pricing check")
        if payload.get("market_independent_forecast") is not True:
            raise PriceShadowError("forecast independence missing")
    quotes = payload.get("quotes")
    if not isinstance(quotes, list) or len(quotes) > 30:
        raise PriceShadowError("quotes must be 0..30 actual observed offers")
    models = payload.get("models")
    if not isinstance(models, dict) or set(models) != {"c", "c2"}:
        raise PriceShadowError("both independent C and C2 inputs required")
    for illegal in ("final_score", "ft_total", "actual_bet", "pnl", "outcome"):
        if illegal in payload or illegal in f:
            raise PriceShadowError("future result/actual exposure fields forbidden")
    model_freezes = [_time(models[m].get("frozen_at_utc"), m+".frozen_at_utc")
                     for m in ("c", "c2")]
    start = max(model_freezes)
    quote_rows = [_same_epoch_quote(q, start, now, ko) for q in quotes]
    qkeys = [(q["line"], q["source_url"], q["observed_at_utc"]) for q in quote_rows]
    if len(qkeys) != len(set(qkeys)):
        raise PriceShadowError("duplicate line/source/quote epoch")
    match = {"assessment": now, "kickoff": ko, "integrity_ready": integrity}
    result = {m: _model(m, models[m], match, quote_rows) for m in ("c", "c2")}
    reason = ("NO_VALIDATED_EXECUTABLE_OFFERS_TO_COMPARE" if not quote_rows else
              "PROSPECTIVE_SHADOW_PRICE_REVIEW_ONLY")
    return {
        "schema_version": SCHEMA, "match_id": f["match_id"],
        "evidence_epoch_id": epoch, "assessment_at_utc": now.isoformat(),
        "input_sha256": _sha(payload), "status": reason,
        "forecast_total_advisory": forecast,
        "quote_count": len(quote_rows),
        "c_official_production_unchanged": result["c"],
        "c2_independent_shadow": result["c2"],
        "shadow_evaluation_only": True,
        "actual_user_bet": None, "official_c_exposure": None,
        "calibrated_goal_probability": None, "expected_value": None,
        "go_no_go_for_production": "NO_POLICY_CHANGE_WITHOUT_PRICE_AWARE_PROSPECTIVE_VALIDATION",
        "interpretation": (
            "True quote-level comparison of existing and independently hypothesized funding "
            "rules. Even SHADOW_PRICE_AWARE_ELIGIBILITY_ONLY is not positive-EV proof, "
            "a current C BET, a C2 bet, a feasible WAIT, or permission to chase a goal. "
            "Asia quarter-line payoff scenarios are exact conditional accounting, not "
            "forecast probabilities. Frozen research evidence must be attested independently."
        ),
    }


def main() -> int:
    p = argparse.ArgumentParser(description="Prospective C/C2 price-aware goal-funding shadow")
    p.add_argument("--input", required=True)
    p.add_argument("--output")
    args = p.parse_args()
    try:
        result = compare(json.loads(Path(args.input).read_text(encoding="utf-8")))
        rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
        if args.output:
            Path(args.output).write_text(rendered, encoding="utf-8")
        else:
            print(rendered)
        return 0
    except (ValueError, TypeError, OSError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
