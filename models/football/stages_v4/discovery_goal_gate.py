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

# Borderline safety lane. This is deliberately looser than the strong gate but
# still requires complete source-backed histories and a non-trap profile.
# It exists only to prevent sweep threshold cliffs from hiding a fixture before
# Football C can research it. GOAL_REVIEW is not a certificate or prediction.
REVIEW_MIN_PRIORITY_SCORE = 50
REVIEW_MIN_MEAN_OVER_TWO_RATE = 0.50
REVIEW_MAX_MEAN_LOW_DRAW_TRAP_RATE = 0.35

# Alternate evidence path for a fixture whose route-composite score is below
# 60 but whose finished-match goal distribution is independently persuasive.
# This remains a research-admission signal only; it never creates a C/C2
# certificate or betting action.
ALT_MIN_MEAN_OVER_TWO_RATE = 0.65
ALT_MIN_MEAN_OVER_THREE_RATE = 0.45
ALT_MAX_MEAN_LOW_DRAW_TRAP_RATE = 0.20

# G3-oriented research paths. These deliberately stop at research admission:
# they do not create a Football C goal certificate or supported burden.
G3_DIST_MIN_PRIORITY_SCORE = 50
G3_DIST_MIN_MEAN_OVER_TWO_RATE = 0.67
G3_DIST_MAX_MEAN_LOW_DRAW_TRAP_RATE = 0.25

CARRIER_MIN_PRIORITY_SCORE = 50
CARRIER_MIN_ROUTE = 1.75
CARRIER_MIN_MEAN_OVER_TWO_RATE = 0.60
CARRIER_MIN_MEAN_OVER_THREE_RATE = 0.30
CARRIER_MAX_MEAN_LOW_DRAW_TRAP_RATE = 0.25


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


def _route_shape(
    home: dict[str, float], away: dict[str, float]
) -> tuple[float, float]:
    home_route = (home["gf"] + away["ga"]) / 2
    away_route = (away["gf"] + home["ga"]) / 2
    return max(home_route, away_route), min(home_route, away_route)


def _priority_score(home: dict[str, float], away: dict[str, float]) -> int:
    """Evidence-only research score; league identity never adds points."""

    carrier, second_route = _route_shape(home, away)
    over2 = (home["over2"] + away["over2"]) / 2
    stall = (home["stall"] + away["stall"]) / 2
    return max(
        0,
        min(
            100,
            round(15 * carrier + 14 * second_route + 22 * over2 - 12 * stall),
        ),
    )


def _goal_research_path(
    priority: int,
    over_two: float,
    over_three: float,
    low_draw_trap: float,
    *,
    carrier_route: float = 0.0,
) -> str | None:
    """Return the league-neutral evidence path that permits deeper research.

    The two G3-oriented paths prevent the intake layer from demanding G4-like
    evidence before Football C has even researched whether a G3 certificate
    exists. They are admission-only and never manufacture a certificate.
    """

    route_score_path = (
        priority >= MIN_PRIORITY_SCORE
        and over_two >= MIN_MEAN_OVER_TWO_RATE
        and low_draw_trap <= MAX_MEAN_LOW_DRAW_TRAP_RATE
    )
    if route_score_path:
        return "ROUTE_SCORE"

    high_rate_path = (
        over_two >= ALT_MIN_MEAN_OVER_TWO_RATE
        and over_three >= ALT_MIN_MEAN_OVER_THREE_RATE
        and low_draw_trap <= ALT_MAX_MEAN_LOW_DRAW_TRAP_RATE
    )
    if high_rate_path:
        return "HIGH_RATE_3PLUS_4PLUS"

    g3_distribution_path = (
        priority >= G3_DIST_MIN_PRIORITY_SCORE
        and over_two >= G3_DIST_MIN_MEAN_OVER_TWO_RATE
        and low_draw_trap <= G3_DIST_MAX_MEAN_LOW_DRAW_TRAP_RATE
    )
    if g3_distribution_path:
        return "G3_DISTRIBUTION"

    carrier_leakage_path = (
        priority >= CARRIER_MIN_PRIORITY_SCORE
        and carrier_route >= CARRIER_MIN_ROUTE
        and over_two >= CARRIER_MIN_MEAN_OVER_TWO_RATE
        and over_three >= CARRIER_MIN_MEAN_OVER_THREE_RATE
        and low_draw_trap <= CARRIER_MAX_MEAN_LOW_DRAW_TRAP_RATE
    )
    if carrier_leakage_path:
        return "CARRIER_LEAKAGE_G3"

    return None


def _borderline_goal_review(
    priority: int,
    over_two: float,
    low_draw_trap: float,
) -> bool:
    """Narrow safety-net admission for complete but near-threshold histories."""

    return (
        priority >= REVIEW_MIN_PRIORITY_SCORE
        and over_two >= REVIEW_MIN_MEAN_OVER_TWO_RATE
        and low_draw_trap <= REVIEW_MAX_MEAN_LOW_DRAW_TRAP_RATE
    )


def _qualifies_goal_research(
    priority: int,
    over_two: float,
    over_three: float,
    low_draw_trap: float,
    *,
    carrier_route: float = 0.0,
) -> bool:
    return _goal_research_path(
        priority,
        over_two,
        over_three,
        low_draw_trap,
        carrier_route=carrier_route,
    ) is not None


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
    carrier_route, second_route = _route_shape(home, away)
    carrier_route = round(carrier_route, 4)
    second_route = round(second_route, 4)
    priority = _priority_score(home, away)
    qualification_path = _goal_research_path(
        priority,
        over_two,
        over_three,
        low_draw_trap,
        carrier_route=carrier_route,
    )
    qualifies = qualification_path is not None
    review = (
        not qualifies
        and _borderline_goal_review(priority, over_two, low_draw_trap)
    )
    if review:
        qualification_path = "BORDERLINE_GOAL_REVIEW"
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
        "carrier_route": carrier_route,
        "second_route": second_route,
        "qualification_path": qualification_path,
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
            else "DISCOVERY_GOAL_REVIEW"
            if review
            else "WATCH_GOAL_SIGNAL"
        ),
        "reason": (
            "SOURCE_BACKED_HIGH_SCORING_RESEARCH"
            if qualifies
            else "SOURCE_BACKED_BORDERLINE_GOAL_REVIEW"
            if review
            else "GOAL_ROUTE_OR_LOW_DRAW_TRAP_SCREEN_NOT_YET_PERSUASIVE"
        ),
        "priority_score": priority,
        "home_sample_n": home["n"],
        "away_sample_n": away["n"],
        "mean_over_two_rate": over_two,
        "mean_over_three_rate": over_three,
        "mean_0_0_or_1_1_rate": low_draw_trap,
        "carrier_route": carrier_route,
        "second_route": second_route,
        "qualification_path": qualification_path,
        "thresholds": {
            "minimum_priority_score": MIN_PRIORITY_SCORE,
            "minimum_mean_over_two_rate": MIN_MEAN_OVER_TWO_RATE,
            "maximum_mean_0_0_or_1_1_rate": MAX_MEAN_LOW_DRAW_TRAP_RATE,
            "review_minimum_priority_score": REVIEW_MIN_PRIORITY_SCORE,
            "review_minimum_mean_over_two_rate": REVIEW_MIN_MEAN_OVER_TWO_RATE,
            "review_maximum_mean_0_0_or_1_1_rate": REVIEW_MAX_MEAN_LOW_DRAW_TRAP_RATE,
            "alternate_minimum_mean_over_two_rate": ALT_MIN_MEAN_OVER_TWO_RATE,
            "alternate_minimum_mean_over_three_rate": ALT_MIN_MEAN_OVER_THREE_RATE,
            "alternate_maximum_mean_0_0_or_1_1_rate": ALT_MAX_MEAN_LOW_DRAW_TRAP_RATE,
            "g3_distribution_minimum_priority_score": G3_DIST_MIN_PRIORITY_SCORE,
            "g3_distribution_minimum_mean_over_two_rate": G3_DIST_MIN_MEAN_OVER_TWO_RATE,
            "g3_distribution_maximum_mean_0_0_or_1_1_rate": G3_DIST_MAX_MEAN_LOW_DRAW_TRAP_RATE,
            "carrier_minimum_priority_score": CARRIER_MIN_PRIORITY_SCORE,
            "carrier_minimum_route": CARRIER_MIN_ROUTE,
            "carrier_minimum_mean_over_two_rate": CARRIER_MIN_MEAN_OVER_TWO_RATE,
            "carrier_minimum_mean_over_three_rate": CARRIER_MIN_MEAN_OVER_THREE_RATE,
            "carrier_maximum_mean_0_0_or_1_1_rate": CARRIER_MAX_MEAN_LOW_DRAW_TRAP_RATE,
        },
        "source_screen_fingerprint": fingerprint,
    }
