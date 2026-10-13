"""V4 source-backed goal-history screen for all competitive fixtures.

This module is deliberately small and V4-local. It validates two recent-result
histories, derives an evidence-only goal priority score, and returns a research
qualification. It is not a C/C2 prediction and has no bookmaker input.

The former dependency on engine/goal_route_prescreen.py is retired.
"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
import hashlib
import json
from typing import Any
from urllib.parse import urlsplit


MIN_RESULTS_PER_TEAM = 4
MAX_RESULTS_PER_TEAM = 10
MAX_SOURCE_AGE_HOURS = 168
MAX_MATCH_AGE_DAYS = 120
RESULT_FINISH_BUFFER_MINUTES = 120

MIN_PRIORITY_SCORE = 60
MIN_MEAN_OVER_TWO_RATE = 0.55
MAX_MEAN_LOW_DRAW_TRAP_RATE = 0.35


class GoalHistoryError(ValueError):
    pass


def _time(value: Any, field: str) -> datetime:
    if not isinstance(value, str):
        raise GoalHistoryError(f"{field}: timezone-aware timestamp required")
    try:
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise GoalHistoryError(f"{field}: invalid timestamp") from exc
    if result.utcoffset() is None:
        raise GoalHistoryError(f"{field}: timezone required")
    return result.astimezone(timezone.utc)


def _url(value: Any, field: str) -> None:
    if not isinstance(value, str):
        raise GoalHistoryError(f"{field}: HTTPS source required")
    parsed = urlsplit(value)
    if (
        parsed.scheme != "https"
        or not parsed.hostname
        or "." not in parsed.hostname
        or parsed.username
        or parsed.password
    ):
        raise GoalHistoryError(f"{field}: public HTTPS source required")


def _goals(value: Any, field: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value <= 20:
        raise GoalHistoryError(f"{field}: actual integer goals 0..20 required")
    return value


def _team_evidence(data: Any, now: datetime, field: str) -> dict[str, float] | None:
    if data is None:
        return None
    if not isinstance(data, dict):
        raise GoalHistoryError(f"{field}: object required")
    recent = data.get("recent")
    if recent is None:
        return None
    if not isinstance(recent, list):
        raise GoalHistoryError(f"{field}.recent: list required")
    if len(recent) < MIN_RESULTS_PER_TEAM:
        return None
    if len(recent) > MAX_RESULTS_PER_TEAM:
        raise GoalHistoryError(f"{field}: at most {MAX_RESULTS_PER_TEAM} results")
    _url(data.get("source_url"), f"{field}.source_url")
    observed = _time(data.get("observed_at_utc"), f"{field}.observed_at_utc")
    if not now - timedelta(hours=MAX_SOURCE_AGE_HOURS) <= observed <= now:
        raise GoalHistoryError(f"{field}: source stale or future")

    seen: set[datetime] = set()
    total_for = total_against = over2 = over3 = stalls = traps = 0
    for index, game in enumerate(recent):
        if not isinstance(game, dict):
            raise GoalHistoryError(f"{field}.recent[{index}]: object required")
        kickoff = _time(
            game.get("kickoff_utc"), f"{field}.recent[{index}].kickoff_utc"
        )
        if kickoff in seen:
            raise GoalHistoryError(f"{field}: duplicate historical kickoff")
        seen.add(kickoff)
        if kickoff > now - timedelta(minutes=RESULT_FINISH_BUFFER_MINUTES):
            raise GoalHistoryError(f"{field}: result not provably final")
        if kickoff < now - timedelta(days=MAX_MATCH_AGE_DAYS):
            raise GoalHistoryError(f"{field}: result outside lookback")
        gf = _goals(game.get("goals_for"), f"{field}.recent[{index}].goals_for")
        ga = _goals(
            game.get("goals_against"), f"{field}.recent[{index}].goals_against"
        )
        total_for += gf
        total_against += ga
        over2 += int(gf + ga >= 3)
        over3 += int(gf + ga >= 4)
        stalls += int(gf + ga <= 2)
        traps += int((gf, ga) in {(0, 0), (1, 1)})

    n = len(recent)
    return {
        "gf": total_for / n,
        "ga": total_against / n,
        "over2": over2 / n,
        "over3": over3 / n,
        "stall": stalls / n,
        "draw_trap": traps / n,
        "n": n,
    }


def _priority_score(home: dict[str, float], away: dict[str, float]) -> int:
    """Evidence-only research score; league identity never adds points."""

    home_route = (home["gf"] + away["ga"]) / 2
    away_route = (away["gf"] + home["ga"]) / 2
    carrier = max(home_route, away_route)
    second_route = min(home_route, away_route)
    over2 = (home["over2"] + away["over2"]) / 2
    stall = (home["stall"] + away["stall"]) / 2
    return max(
        0,
        min(
            100,
            round(15 * carrier + 14 * second_route + 22 * over2 - 12 * stall),
        ),
    )


def screen_discovery(
    *,
    run_id: str,
    source_payload_hash: str,
    at_utc: str,
    fixture: dict[str, Any],
) -> dict[str, Any]:
    """Return a traceable research eligibility decision, never a model PASS."""

    base = {
        "policy": "V4_EQUAL_SOURCE_BACKED_GOAL_HISTORY_V2",
        "is_model_prediction": False,
        "bookmaker_quote_required": False,
    }
    evidence = fixture.get("football_evidence")
    if not isinstance(evidence, dict):
        return {
            **base,
            "status": "PENDING_GOAL_HISTORY",
            "reason": "FOUR_VERIFIED_RESULTS_PER_TEAM_NOT_YET_COLLECTED",
        }

    try:
        now = _time(at_utc, "at_utc")
        home = _team_evidence(evidence.get("home"), now, "goal_history.home")
        away = _team_evidence(evidence.get("away"), now, "goal_history.away")
        if home is None or away is None:
            return {
                **base,
                "status": "PENDING_GOAL_HISTORY",
                "reason": "FOUR_VERIFIED_RESULTS_PER_TEAM_NOT_YET_COLLECTED",
            }
    except GoalHistoryError as exc:
        return {
            **base,
            "status": "PENDING_SOURCE_SCORING_EVIDENCE",
            "reason": str(exc),
        }

    over_two = round((home["over2"] + away["over2"]) / 2, 4)
    low_draw_trap = round((home["draw_trap"] + away["draw_trap"]) / 2, 4)
    over_three = round((home["over3"] + away["over3"]) / 2, 4)
    priority = _priority_score(home, away)
    qualifies = (
        priority >= MIN_PRIORITY_SCORE
        and over_two >= MIN_MEAN_OVER_TWO_RATE
        and low_draw_trap <= MAX_MEAN_LOW_DRAW_TRAP_RATE
    )
    fingerprint_payload = {
        "run_id": run_id,
        "source_payload_hash": source_payload_hash,
        "match_id": fixture.get("match_id"),
        "at_utc": at_utc,
        "priority_score": priority,
        "home_sample_n": home["n"],
        "away_sample_n": away["n"],
        "mean_over_two_rate": over_two,
        "mean_over_three_rate": over_three,
        "mean_0_0_or_1_1_rate": low_draw_trap,
    }
    fingerprint = hashlib.sha256(
        json.dumps(
            fingerprint_payload,
            sort_keys=True,
            ensure_ascii=True,
            separators=(",", ":"),
        ).encode("utf-8")
    ).hexdigest()

    return {
        **base,
        "status": (
            "DISCOVERY_GOAL_QUALIFIED"
            if qualifies
            else "WATCH_GOAL_SIGNAL"
        ),
        "reason": (
            "SOURCE_BACKED_HIGH_SCORING_RESEARCH"
            if qualifies
            else "GOAL_ROUTE_OR_LOW_DRAW_TRAP_SCREEN_NOT_YET_PERSUASIVE"
        ),
        "priority_score": priority,
        "home_sample_n": home["n"],
        "away_sample_n": away["n"],
        "mean_over_two_rate": over_two,
        "mean_over_three_rate": over_three,
        "mean_0_0_or_1_1_rate": low_draw_trap,
        "thresholds": {
            "minimum_priority_score": MIN_PRIORITY_SCORE,
            "minimum_mean_over_two_rate": MIN_MEAN_OVER_TWO_RATE,
            "maximum_mean_0_0_or_1_1_rate": MAX_MEAN_LOW_DRAW_TRAP_RATE,
        },
        "source_screen_fingerprint": fingerprint,
    }
