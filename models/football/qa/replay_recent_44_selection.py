#!/usr/bin/env python3
"""Same-information replay of the 44 recent assessed fixtures.

The cohort is frozen from Decision States. This replay deliberately reads no
final scores and no bookmaker data. It compares the pre-repair 31 Oct
depth/history-first ordering with the current execution-first ranking and the
REVIEW_PARETO_DOMINANCE_GUARD_V1 selection guard.

Fixtures are replayed only against other fixtures assessed in the same frozen
assessment batch, so later matches cannot retrospectively challenge earlier
selection capacity.
"""
from __future__ import annotations

from collections import Counter, defaultdict
import json
from pathlib import Path
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
ENGINE = ROOT / "models" / "football" / "engine"
sys.path.insert(0, str(ENGINE))

from adapter import parse_assessment  # noqa: E402
from core import (  # noqa: E402
    BoardState,
    _c_endpoint_control_key,
    _goal_signal_rank_key,
    _goal_tail_rank_key,
    c_effective_incentive_grades,
    c_g3_endpoint_control_pressure,
    c_goal3_execution_floor_authorized,
    c_goal3_mechanism_class,
    c_goal3_mechanism_rank,
    c_upper_tail_transferable,
    certificate_robustness,
    compile_c_board_state,
    follow_priority_profile,
    funded_goal_certificate_depth,
    ranking_key,
    tournament_incentive_rank_score,
)

INPUT = ROOT / "models" / "football" / "qa" / "replays" / "2026-11-02_recent_44_frozen_assessments.json"


def old_depth_first_key(a) -> tuple[int, ...]:
    """Exact 31 Oct ordering that was removed by the 2 Nov repair."""

    effective_continuation, _ = c_effective_incentive_grades(a)
    endpoint = _c_endpoint_control_key(a)
    tail_signal = _goal_tail_rank_key(a)
    goal_signal = _goal_signal_rank_key(a)
    upper_tail_self_fund = int(a.carrier_self_fund and c_upper_tail_transferable(a))
    profile = follow_priority_profile(a)
    return (
        int(c_goal3_execution_floor_authorized(a)),
        funded_goal_certificate_depth(a, "c"),
        *tail_signal,
        c_goal3_mechanism_rank(a),
        int(profile["follow_clearability_score"]),
        certificate_robustness(a, "c"),
        *endpoint,
        int(effective_continuation),
        int(a.burden_completion_quality),
        *goal_signal,
        int(a.route_reliability),
        int(a.independent_route_quality),
        int(a.chance_quality),
        int(a.carrier),
        int(a.failure_resistance),
        int(a.evidence_confidence),
        int(a.burden_protection),
        int(a.opponent_leakage),
        upper_tail_self_fund,
        int(a.xi_robustness),
        tournament_incentive_rank_score(a),
    )


def dominates(review: dict[str, Any], focus: dict[str, Any]) -> bool:
    if review["new_state"] != "WATCH" or focus["new_state"] != "FOCUS":
        return False
    if review["operational_grade"] != "A":
        return False
    if review["g3_endpoint_control_pressure"] == "HIGH":
        return False
    if review["material_suppression"] or review["failure_attacks_route"]:
        return False
    return (
        review["clearability"] >= focus["clearability"]
        and review["ceiling"] >= focus["ceiling"]
        and (
            review["clearability"] > focus["clearability"]
            or review["ceiling"] > focus["ceiling"]
        )
    )


def replay() -> dict[str, Any]:
    src = json.loads(INPUT.read_text(encoding="utf-8"))
    fixtures = src["fixtures"]
    if len(fixtures) != 44:
        raise AssertionError(f"expected 44 fixtures, got {len(fixtures)}")
    if src.get("outcome_fields_included") is not False:
        raise AssertionError("replay input must not contain outcome fields")

    batches: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for fixture in fixtures:
        batches[str(fixture["assessment_at_utc"])].append(fixture)

    replay_rows: list[dict[str, Any]] = []
    batch_summaries: list[dict[str, Any]] = []

    for batch_id, batch in sorted(batches.items()):
        parsed = []
        by_id = {}
        for fixture in batch:
            a = parse_assessment(fixture["match"], require_c_completion=True)
            parsed.append(a)
            by_id[a.match_id] = fixture

        old_order = sorted(
            parsed,
            key=lambda a: (compile_c_board_state(a), old_depth_first_key(a), a.match_id),
            reverse=True,
        )
        new_order = sorted(
            parsed,
            key=lambda a: (compile_c_board_state(a), ranking_key(a), a.match_id),
            reverse=True,
        )
        old_rank = {a.match_id: i for i, a in enumerate(old_order, 1)}
        new_rank = {a.match_id: i for i, a in enumerate(new_order, 1)}

        derived: dict[str, dict[str, Any]] = {}
        for a in parsed:
            raw = by_id[a.match_id]["match"]
            profile = follow_priority_profile(a)
            state = compile_c_board_state(a).name
            derived[a.match_id] = {
                "match_id": a.match_id,
                "new_state": state,
                "operational_grade": str(raw.get("operational_viability_grade") or ""),
                "clearability": int(profile["follow_clearability_score"]),
                "ceiling": int(profile["follow_ceiling_score"]),
                "balanced": int(profile["follow_balanced_score"]),
                "mechanism": c_goal3_mechanism_class(a),
                "certificate_depth": funded_goal_certificate_depth(a, "c"),
                "robustness": certificate_robustness(a, "c"),
                "g3_endpoint_control_pressure": c_g3_endpoint_control_pressure(a),
                "material_suppression": bool(a.material_suppression),
                "failure_attacks_route": bool(a.failure_attacks_route),
            }

        focus_pool = [
            derived[a.match_id] for a in new_order
            if derived[a.match_id]["new_state"] == "FOCUS"
            and derived[a.match_id]["operational_grade"] == "A"
        ]
        review_pool = [
            derived[a.match_id] for a in new_order
            if derived[a.match_id]["new_state"] == "WATCH"
            and derived[a.match_id]["operational_grade"] == "A"
        ]
        dominated: dict[str, list[str]] = {}
        challengers: dict[str, list[str]] = defaultdict(list)
        for focus in focus_pool:
            ids = [r["match_id"] for r in review_pool if dominates(r, focus)]
            if ids:
                dominated[focus["match_id"]] = ids
                for mid in ids:
                    challengers[mid].append(focus["match_id"])

        selected = [
            row for row in focus_pool
            if row["match_id"] not in dominated
        ][:8]
        selected_ids = {row["match_id"] for row in selected}

        for a in new_order:
            fixture = by_id[a.match_id]
            d = derived[a.match_id]
            if a.match_id in selected_ids:
                new_lane = "FOLLOW"
            elif d["new_state"] == "FOCUS":
                new_lane = "RESERVE"
            elif a.match_id in challengers:
                new_lane = "REVIEW_CHALLENGER"
            elif d["new_state"] == "WATCH":
                new_lane = "REVIEW_ONLY"
            else:
                new_lane = "PASS"
            replay_rows.append({
                "assessment_batch": batch_id,
                "match_id": a.match_id,
                "home": fixture["match"].get("home"),
                "away": fixture["match"].get("away"),
                "kickoff_ict": fixture["match"].get("kickoff_ict"),
                "original_board_state": fixture["original_board_state"],
                "original_action": fixture["original_action"],
                "new_compiled_state": d["new_state"],
                "old_depth_first_rank_in_batch": old_rank[a.match_id],
                "new_execution_first_rank_in_batch": new_rank[a.match_id],
                "rank_delta_old_minus_new": old_rank[a.match_id] - new_rank[a.match_id],
                "new_lane": new_lane,
                "mechanism": d["mechanism"],
                "certificate_depth": d["certificate_depth"],
                "robustness": d["robustness"],
                "clearability": d["clearability"],
                "ceiling": d["ceiling"],
                "balanced": d["balanced"],
                "g3_endpoint_control_pressure": d["g3_endpoint_control_pressure"],
                "dominated_by_review_ids": dominated.get(a.match_id, []),
                "review_challenges_focus_ids": challengers.get(a.match_id, []),
            })

        batch_summaries.append({
            "assessment_batch": batch_id,
            "fixture_count": len(batch),
            "selected_follow_ids": [row["match_id"] for row in selected],
            "review_challenger_ids": sorted(challengers),
            "dominated_focus_ids": sorted(dominated),
        })

    rows_by_id = {row["match_id"]: row for row in replay_rows}
    original_dist = Counter(str(f["original_board_state"]) for f in fixtures)
    new_dist = Counter(row["new_compiled_state"] for row in replay_rows)
    lane_dist = Counter(row["new_lane"] for row in replay_rows)
    moved = [row for row in replay_rows if row["old_depth_first_rank_in_batch"] != row["new_execution_first_rank_in_batch"]]
    state_changed = [
        row for row in replay_rows
        if row["original_board_state"] != row["new_compiled_state"]
    ]
    challengers = [row for row in replay_rows if row["new_lane"] == "REVIEW_CHALLENGER"]
    dominated = [row for row in replay_rows if row["dominated_by_review_ids"]]

    return {
        "schema_version": "football-c-recent-44-selection-replay-v1",
        "same_information_replay": True,
        "outcome_fields_read": False,
        "source_fixture_count": 44,
        "assessment_batch_count": len(batches),
        "original_state_distribution": dict(sorted(original_dist.items())),
        "new_compiled_state_distribution": dict(sorted(new_dist.items())),
        "new_lane_distribution": dict(sorted(lane_dist.items())),
        "state_change_count": len(state_changed),
        "rank_movement_count": len(moved),
        "review_challenger_count": len(challengers),
        "dominated_focus_count": len(dominated),
        "state_changes": state_changed,
        "rank_movements": moved,
        "review_challengers": challengers,
        "dominated_focus": dominated,
        "batches": batch_summaries,
        "fixtures": sorted(
            replay_rows,
            key=lambda row: (str(row["kickoff_ict"]), row["match_id"]),
        ),
    }


def main() -> int:
    result = replay()
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
