#!/usr/bin/env python3
"""Advisory, football-first Step-1 goal burden forecast.

No sportsbook probability, xG model, C/C2 betting action or Step-0 ranking
is computed here. The forecast is frozen from source-backed football evidence
BEFORE market comparison. A limited forecast never becomes an execution veto.
"""
from __future__ import annotations

import argparse
import json
import math
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit


class GoalForecastError(ValueError):
    pass


def _text(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise GoalForecastError(f"{field} missing")
    return value.strip()


def _date(value: Any, field: str) -> datetime:
    from datetime import timezone
    try:
        val = datetime.fromisoformat(_text(value, field).replace("Z", "+00:00"))
    except ValueError as exc:
        raise GoalForecastError(f"{field} invalid ISO timestamp") from exc
    if val.utcoffset() is None:
        raise GoalForecastError(f"{field} requires timezone")
    return val.astimezone(timezone.utc)


def _number(value: Any, field: str, upper: float) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise GoalForecastError(f"{field} must be numeric")
    x = float(value)
    if not math.isfinite(x) or x < 0 or x > upper:
        raise GoalForecastError(f"{field} outside finite 0..{upper}")
    return x


def _provider(url: str, field: str) -> str:
    source = _text(url, field)
    parsed = urlsplit(source)
    if parsed.scheme != "https" or not parsed.hostname or "." not in parsed.hostname:
        raise GoalForecastError(f"{field} must be an https source URL")
    if parsed.username or parsed.password:
        raise GoalForecastError(f"{field} must not contain credentials")
    return source


def _team(value: Any, name: str, *, quantified: bool) -> dict:
    if not isinstance(value, dict):
        raise GoalForecastError(f"{name} team forecast missing")
    basis = _text(value.get("basis"), f"{name}.basis")
    if len(basis) < 20:
        raise GoalForecastError(f"{name}.basis needs a concrete football explanation")
    sources = value.get("evidence_urls")
    if not isinstance(sources, list) or not sources:
        raise GoalForecastError(f"{name}.evidence_urls missing")
    urls = [_provider(v, f"{name}.evidence_urls") for v in sources]
    result = {"basis": basis, "evidence_urls": urls}
    if not quantified:
        if any(k in value for k in ("central", "low", "high")):
            raise GoalForecastError("EVIDENCE_LIMITED cannot imply numerical goals")
        return result
    numbers = {k: _number(value.get(k), f"{name}.{k}", 8.0) for k in ("low", "central", "high")}
    if not numbers["low"] <= numbers["central"] <= numbers["high"]:
        raise GoalForecastError(f"{name} expected goals must satisfy low <= central <= high")
    result.update(numbers)
    return result


def validate_forecast(payload: dict[str, Any]) -> dict:
    if not isinstance(payload, dict) or payload.get("schema_version") != "football-step1-goal-burden-v1":
        raise GoalForecastError("schema_version invalid")
    match_id = _text(payload.get("match_id"), "match_id")
    epoch = _text(payload.get("evidence_epoch_id"), "evidence_epoch_id")
    freeze = _date(payload.get("forecast_frozen_at_utc"), "forecast_frozen_at_utc")
    kickoff = _date(payload.get("kickoff_utc"), "kickoff_utc")
    if freeze >= kickoff:
        raise GoalForecastError("forecast must be prospective before kickoff")
    if payload.get("market_independent_forecast") is not True:
        raise GoalForecastError("football forecast must be attested independent of odds")
    status = payload.get("forecast_status")
    if status not in ("QUANTIFIED", "EVIDENCE_LIMITED"):
        raise GoalForecastError("forecast_status must be QUANTIFIED or EVIDENCE_LIMITED")
    quantified = status == "QUANTIFIED"
    home = _team(payload.get("home"), "home", quantified=quantified)
    away = _team(payload.get("away"), "away", quantified=quantified)
    for field in ("goal_three_mechanism", "goal_four_mechanism", "failure_scenario"):
        if len(_text(payload.get(field), field)) < 12:
            raise GoalForecastError(f"{field} needs football reasoning")
    if not quantified:
        _text(payload.get("limitation_reason"), "limitation_reason")
    centre = round(home["central"] + away["central"], 3) if quantified else None
    if quantified and "declared_total" in payload:
        value = _number(payload["declared_total"], "declared_total", 16.0)
        if abs(value - centre) > 0.001:
            raise GoalForecastError("declared_total != sum(home.central, away.central)")
    market = payload.get("market")
    comparison: dict = {"status": "NOT_OBSERVED", "market_gap": None, "conflict": False}
    if market is not None:
        if not isinstance(market, dict):
            raise GoalForecastError("market must be an object")
        center = _number(market.get("center"), "market.center", 12.0)
        _provider(market.get("source_url"), "market.source_url")
        _date(market.get("observed_at_utc"), "market.observed_at_utc")
        gap = round(centre - center, 3) if quantified else None
        conflict = gap is not None and abs(gap) >= 0.75
        note = market.get("conflict_recheck_note")
        comparison = {
            "status": "RECHECK_REQUIRED" if conflict and not isinstance(note, str) or conflict and not note.strip() else "COMPARE_ONLY",
            "market_gap": gap,
            "conflict": conflict,
            "meaning": "football expectation minus bookmaker market centre; not an edge probability",
        }
    return {
        "ok": True,
        "match_id": match_id,
        "evidence_epoch_id": epoch,
        "forecast_status": status,
        "home_expected_goals": home.get("central"),
        "away_expected_goals": away.get("central"),
        "expected_total": centre,
        "total_low": round(home["low"] + away["low"], 3) if quantified else None,
        "total_high": round(home["high"] + away["high"], 3) if quantified else None,
        "market_comparison": comparison,
        "advisory_only": True,
        "modifies_production_thresholds": False,
    }


def main() -> int:
    import sys
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    args = parser.parse_args()
    try:
        data = json.loads(Path(args.input).read_text(encoding="utf-8"))
        result = validate_forecast(data)
    except (OSError, ValueError, TypeError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}), file=sys.stderr)
        return 2
    print(json.dumps(result, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
