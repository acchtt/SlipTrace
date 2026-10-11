"""Source-backed goal-potential discovery for competitive unregistered leagues.

This is a *research admission* heuristic, not a C/C2 model result, goal
prediction or betting selection. Unknown country/competition combinations
are never silently dropped for being outside the researched registry.
An actual senior match must have canonical fixture identity, current
researchability proof and two independently verifiable team result histories
before it can enter the official C/C2 football research queue.
"""
from __future__ import annotations

from datetime import datetime
from typing import Any

from goal_route_prescreen import (
    GoalPrescreenError, _team_evidence, run_prescreen,
)

MIN_PRIORITY_SCORE = 60
MIN_MEAN_OVER_TWO_RATE = 0.55
MAX_MEAN_LOW_DRAW_TRAP_RATE = 0.35


def screen_discovery(
    *,
    run_id: str,
    source_payload_hash: str,
    at_utc: str,
    fixture: dict[str, Any],
) -> dict[str, Any]:
    """Return a traceable research eligibility decision, never a model PASS."""
    base = {
        "policy": "UNREGISTERED_SOURCE_BACKED_GOAL_DISCOVERY_V1",
        "is_model_prediction": False,
        "bookmaker_quote_required": False,
    }
    evidence = fixture.get("football_evidence")
    if not isinstance(evidence, dict):
        return {
            **base, "status": "PENDING_GOAL_HISTORY",
            "reason": "FOUR_VERIFIED_RESULTS_PER_TEAM_NOT_YET_COLLECTED",
        }
    candidate = {
        "match_id": fixture["match_id"],
        "queue_rank": 1,
        "operational_grade": "B",
        "fixture_status": fixture["fixture_status"],
        "kickoff_utc": fixture["kickoff_utc"],
        "country": fixture["country"],
        "competition_name": fixture["competition"],
        "football_evidence": evidence,
    }
    payload = {
        "schema_version": "football-goal-route-prescreen-v1",
        "run_id": run_id,
        "source_payload_hash": source_payload_hash,
        "screen_at_utc": at_utc,
        "candidates": [candidate],
    }
    try:
        result = run_prescreen(payload)
        row = result["manifest"]["original_rows"][0]
        if row["screen_status"] != "QUANTIFIED":
            return {
                **base, "status": "PENDING_GOAL_HISTORY",
                "reason": row.get("evidence_limit_reason") or "INSUFFICIENT_TEAM_RESULTS",
            }
        now = datetime.fromisoformat(at_utc.replace("Z", "+00:00"))
        home = _team_evidence(evidence.get("home"), now, "discovery.home")
        away = _team_evidence(evidence.get("away"), now, "discovery.away")
        if home is None or away is None:
            return {
                **base, "status": "PENDING_GOAL_HISTORY",
                "reason": "FOUR_VERIFIED_RESULTS_PER_TEAM_NOT_YET_COLLECTED",
            }
    except (GoalPrescreenError, KeyError, TypeError, ValueError) as exc:
        return {
            **base, "status": "PENDING_SOURCE_SCORING_EVIDENCE",
            "reason": str(exc),
        }
    over_two = round((home["over2"] + away["over2"]) / 2, 4)
    low_draw_trap = round((home["draw_trap"] + away["draw_trap"]) / 2, 4)
    over_three = round((home["over3"] + away["over3"]) / 2, 4)
    priority = row["priority_score"]
    qualifies = (
        priority is not None
        and priority >= MIN_PRIORITY_SCORE
        and over_two >= MIN_MEAN_OVER_TWO_RATE
        and low_draw_trap <= MAX_MEAN_LOW_DRAW_TRAP_RATE
    )
    return {
        **base,
        "status": "DISCOVERY_GOAL_QUALIFIED" if qualifies else "WATCH_GOAL_SIGNAL",
        "reason": "SOURCE_BACKED_HIGH_SCORING_RESEARCH" if qualifies else
                  "GOAL_ROUTE_OR_LOW_DRAW_TRAP_SCREEN_NOT_YET_PERSUASIVE",
        "priority_score": priority,
        "home_sample_n": row["home_sample_n"],
        "away_sample_n": row["away_sample_n"],
        "mean_over_two_rate": over_two,
        "mean_over_three_rate": over_three,
        "mean_0_0_or_1_1_rate": low_draw_trap,
        "thresholds": {
            "minimum_priority_score": MIN_PRIORITY_SCORE,
            "minimum_mean_over_two_rate": MIN_MEAN_OVER_TWO_RATE,
            "maximum_mean_0_0_or_1_1_rate": MAX_MEAN_LOW_DRAW_TRAP_RATE,
        },
        "source_screen_fingerprint": result["manifest"]["screen_fingerprint"],
    }
