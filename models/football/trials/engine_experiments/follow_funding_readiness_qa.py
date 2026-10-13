#!/usr/bin/env python3
"""Non-blocking QA: can frozen FOLLOW/FOCUS supported totals fund their clearing goals?

This is a *readiness diagnostic*, not a goal forecast, a trading strategy, a
reason to demote FOCUS, an exposure receipt, or authorization to change C/C2.
Both models use the exact frozen gate implementations from core.py, through
the existing goal_gate_shadow_audit._gate adapter.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from goal_gate_shadow_audit import GateAuditError, _gate, _timestamp

SCHEMA = "football-follow-funding-readiness-v1"


class FollowFundingQAError(ValueError):
    pass


def _text(obj: dict, key: str) -> str:
    value = obj.get(key)
    if not isinstance(value, str) or not value.strip():
        raise FollowFundingQAError(f"{key} missing")
    return value


def _model(row: dict, name: str, shared: dict) -> dict:
    side = row.get(name)
    if not isinstance(side, dict):
        raise FollowFundingQAError(f"{name} independent frozen model snapshot missing")
    state = side.get("board_state")
    if state not in ("FOCUS", "WATCH", "PASS"):
        raise FollowFundingQAError(f"{name} board_state invalid")
    line = side.get("supported_line")
    if isinstance(line, bool) or not isinstance(line, (int, float)):
        raise FollowFundingQAError(f"{name} supported_line invalid")
    factors = side.get("frozen_factors")
    if not isinstance(factors, dict):
        raise FollowFundingQAError(f"{name} independent frozen_factors required")
    own_freeze = side.get("frozen_at_utc")
    if _timestamp(own_freeze) >= _timestamp(shared["kickoff_utc"]):
        raise FollowFundingQAError(f"{name} factors not frozen before kickoff")
    if _timestamp(own_freeze) > _timestamp(shared["assessment_at_utc"]):
        raise FollowFundingQAError(f"{name} frozen factors from the future")
    try:
        gate = _gate({
            "match_id": shared["match_id"],
            "evidence_epoch_id": shared["evidence_epoch_id"],
            "model": name,
            "freeze_status": "PROSPECTIVE_VERIFIED",
            "frozen_at_utc": own_freeze,
            "kickoff_utc": shared["kickoff_utc"],
            "selected_line": line,
            "frozen_factors": factors,
        })
    except GateAuditError as exc:
        raise FollowFundingQAError(f"{name} goal-funding evidence invalid: {exc}") from exc
    return {
        "board_state": state,
        "supported_line": gate["line"],
        "funded_at_own_supported_line": gate["production_goal_gate"],
        "less_restrictive_gate_pass": gate["less_restrictive_comparator_gate"],
        "additional_goal_gate_blocks": gate["gate_disagreement"],
        "bet_authorized": False,
        "action": "NOT_ASSESSED",
    }


def analyze(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict) or payload.get("schema_version") != SCHEMA:
        raise FollowFundingQAError(f"schema_version must be {SCHEMA}")
    board_id = _text(payload, "board_id")
    revision = _text(payload, "source_revision")
    fixtures = payload.get("fixtures")
    if not isinstance(fixtures, list) or not fixtures:
        raise FollowFundingQAError("complete board fixtures required")
    results, seen = [], set()
    for row in fixtures:
        if not isinstance(row, dict):
            raise FollowFundingQAError("fixture must be object")
        forbidden = {
            "final_score", "live_score", "ft_goals", "ft_result", "pnl",
            "actual_bet", "executed_quote", "settlement", "observed_ft_total_goals",
        }
        if forbidden.intersection(row):
            raise FollowFundingQAError("future outcomes/prices forbidden in funding-readiness QA")
        mid = _text(row, "match_id")
        epoch = _text(row, "evidence_epoch_id")
        key = (mid, epoch)
        if key in seen:
            raise FollowFundingQAError("duplicate fixture/epoch")
        seen.add(key)
        ko = _text(row, "kickoff_utc")
        observed = _text(row, "assessment_at_utc")
        if _timestamp(observed) >= _timestamp(ko):
            raise FollowFundingQAError("QA epoch must precede kickoff")
        lane = row.get("official_c_follow_lane")
        if lane not in ("FOLLOW", "RESERVE", "STOP"):
            raise FollowFundingQAError("official C lane invalid")
        shared = {
            "match_id": mid, "evidence_epoch_id": epoch,
            "kickoff_utc": ko, "assessment_at_utc": observed,
        }
        c = _model(row, "c", shared)
        c2 = _model(row, "c2", shared)
        if lane == "FOLLOW" and c["board_state"] != "FOCUS":
            raise FollowFundingQAError("FOLLOW without C FOCUS contradicts frozen board")
        if c["board_state"] == "PASS" and lane != "STOP":
            raise FollowFundingQAError("C PASS cannot receive routine FOLLOW/RESERVE")
        forecast = row.get("forecast_total")
        center = row.get("market_center")
        for k, val in (("forecast_total", forecast), ("market_center", center)):
            if val is not None and (
                isinstance(val, bool) or not isinstance(val, (int, float))
                or not 0 <= val <= 20
            ):
                raise FollowFundingQAError(f"{k} invalid")
        issues = []
        if lane == "FOLLOW" and not c["funded_at_own_supported_line"]:
            issues.append("C_FOLLOW_SUPPORTED_BURDEN_UNFUNDED")
        if c2["board_state"] == "FOCUS" and not c2["funded_at_own_supported_line"]:
            issues.append("C2_FOCUS_SUPPORTED_BURDEN_UNFUNDED")
        results.append({
            "match_id": mid, "evidence_epoch_id": epoch,
            "official_c_follow_lane": lane,
            "c": c, "c2": c2,
            "forecast_total": forecast, "market_center": center,
            "forecast_market_gap": round(forecast - center, 3) if (
                forecast is not None and center is not None
            ) else None,
            "issues": issues,
            "model_bet_exposure": None,
            "user_bet_exposure": None,
        })
    follows = [x for x in results if x["official_c_follow_lane"] == "FOLLOW"]
    c2focus = [x for x in results if x["c2"]["board_state"] == "FOCUS"]
    c_ready = sum(x["c"]["funded_at_own_supported_line"] for x in follows)
    c2_ready = sum(x["c2"]["funded_at_own_supported_line"] for x in c2focus)
    warnings = []
    if follows and c_ready == 0:
        warnings.append("CRITICAL_ALL_FOLLOW_SUPPORTED_BURDENS_UNFUNDED")
    if c2focus and c2_ready == 0:
        warnings.append("C2_SHADOW_ALL_FOCUS_SUPPORTED_BURDENS_UNFUNDED")
    return {
        "schema_version": SCHEMA,
        "board_id": board_id, "source_revision": revision,
        "qa_status": "WARN_REVIEW_FUNDING_ALIGNMENT" if warnings else "REVIEWED",
        "warning_codes": warnings, "fixtures_checked": len(results),
        "official_c_follow": len(follows),
        "official_c_follow_funded_at_supported": c_ready,
        "c2_shadow_focus": len(c2focus),
        "c2_shadow_focus_funded_at_supported": c2_ready,
        "fixtures": results,
        "advisory_only": True, "thresholds_changed": False,
        "no_official_or_shadow_bets_created": True,
        "interpretation": (
            "A failed funding gate at a supported total is a forecast/execution "
            "alignment warning, not proof that an offered market Over has value. "
            "C and C2 need separate current XI/quote authorization; this QA "
            "must neither demote FOCUS nor synthesize exposure or returns."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Football C/C2 frozen funding alignment QA")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output")
    args = parser.parse_args()
    try:
        result = analyze(json.loads(Path(args.input).read_text(encoding="utf-8")))
        text = json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
        if args.output:
            Path(args.output).write_text(text, encoding="utf-8")
        else:
            print(text)
        return 0
    except (OSError, ValueError, TypeError, GateAuditError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
