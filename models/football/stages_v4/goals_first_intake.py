"""V4 source-backed goals-first qualification for every researched league.

A league registration is NOT goals evidence. All non-excluded competitive
fixtures enter an acquisition/research pool, but only source-quantified
goal-positive fixtures enter the official rank-eligible shortlist.
Evidence-limited or weak-goal matches remain visible and researchable,
never labelled a C/C2 PASS or assumed to be a profitable Over.
"""
from __future__ import annotations

from typing import Any
from discovery_goal_gate import screen_discovery

CANDIDATE_LANES = frozenset({"ROUTINE","CONDITIONAL","PILOT","DISCOVERY"})
ADMITTED_LANES = CANDIDATE_LANES
PENDING_LANES = frozenset({"PENDING_DISCOVERY","PENDING_RESEARCHABILITY"})


def _research_order(row: dict[str, Any]) -> tuple[Any, ...]:
    screen = row["goal_screen"]
    status = screen["status"]
    # Pursue strong verified goals form FIRST, whether or not registered.
    # Then recover missing form, before expending effort on negative
    # goal signals. Urgency matters within each football-evidence class.
    if status == "DISCOVERY_GOAL_QUALIFIED":
        tier = 0
    elif status in {"PENDING_GOAL_HISTORY","PENDING_SOURCE_SCORING_EVIDENCE"}:
        tier = 1
    else:
        tier = 2
    priority = screen.get("priority_score")
    return (
        tier,
        -(priority if isinstance(priority, (float, int)) else 0),
        row["kickoff_utc"],
        row["match_id"],
    )


def select(
    *, run_id: str, at_utc: str, source_hash: str,
    source_rows: list[dict[str, Any]],
    ledger: list[dict[str, Any]],
    provisional_queue: list[dict[str, Any]],
) -> dict[str, Any]:
    indexed = {
        raw["match_id"]: raw for raw in source_rows
        if isinstance(raw, dict) and isinstance(raw.get("match_id"), str)
    }
    queue_map = {item["match_id"]: item for item in provisional_queue}
    selected, research = [], []
    for item in ledger:
        if (item.get("registry_lane") not in CANDIDATE_LANES
                or item.get("intake_lane") not in ADMITTED_LANES | PENDING_LANES):
            continue
        mid = item["match_id"]
        source = indexed[mid]
        screen = item.get("discovery_screen")
        if screen is None:
            screen = screen_discovery(
                run_id=run_id, source_payload_hash=source_hash,
                at_utc=at_utc, fixture=source,
            )
        item["goal_screen"] = screen
        old_lane = item["intake_lane"]
        if old_lane in ADMITTED_LANES:
            if screen["status"] == "DISCOVERY_GOAL_QUALIFIED":
                # Treat ROUTINE, PILOT, CONDITIONAL and DISCOVERY identically.
                item["intake_lane"] = "GOAL_PRIORITY"
                item["reason"] = "SOURCE_BACKED_GOAL_SIGNAL_QUALIFIED"
                q = queue_map[mid]
                q["intake_lane"] = item["intake_lane"]
                q["reason"] = item["reason"]
                q["goal_screen"] = screen
                selected.append(q)
            else:
                item["intake_lane"] = "PENDING_GOAL_RESEARCH"
                item["reason"] = screen["reason"]
        if item["intake_lane"] != "GOAL_PRIORITY":
            research.append({
                "match_id": mid, "country": item["country"],
                "competition": item["competition"],
                "home": item["home"], "away": item["away"],
                "kickoff_utc": item["kickoff_utc"],
                "registry_lane": item["registry_lane"],
                "intake_lane": item["intake_lane"],
                "reason": item["reason"], "goal_screen": screen,
                "source_url": item["source_url"],
            })
    research.sort(key=_research_order)
    return {
        "eligible_queue": selected,
        "goal_research_queue": research,
        "goal_research_order": [r["match_id"] for r in research],
        "pending_goal_research_count": sum(
            r["intake_lane"] == "PENDING_GOAL_RESEARCH" for r in research
        ),
        "low_goal_signal_count": sum(
            r["goal_screen"]["status"] == "WATCH_GOAL_SIGNAL" for r in research
        ),
        "unresearched_goal_history_count": sum(
            r["goal_screen"]["status"] in {
                "PENDING_GOAL_HISTORY", "PENDING_SOURCE_SCORING_EVIDENCE"
            } for r in research
        ),
        "verified_goal_qualified_count": len(selected),
    }
