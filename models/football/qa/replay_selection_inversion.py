#!/usr/bin/env python3
"""Frozen same-information replay for the selection-inversion repair.

This tool reads sealed rank packages, never final scores. It compares the old
declared-state champion, repaired compiled-state champion, and clearability
challenger. Outcome separation is reported only when an explicit settlement
map is supplied by a separate audit process.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys
from typing import Any

ENGINE = Path(__file__).resolve().parents[1] / "engine"
sys.path.insert(0, str(ENGINE))

from adapter import parse_assessment  # noqa: E402
from core import (  # noqa: E402
    BoardState,
    c_direct_act_ceiling,
    c_g3_endpoint_control_pressure,
    c_upper_tail_control_pressure,
    certificate_robustness,
    compile_c_board_state,
    follow_priority_profile,
    funded_goal_certificate_depth,
    ranking_key,
    ranking_key_clearability_challenger,
)


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _declared(raw: dict[str, Any]) -> BoardState:
    value = str(raw.get("board_state", "WATCH")).replace("-", "_")
    value = value.removeprefix("C_")
    return BoardState[value]


def _distribution(states: list[BoardState]) -> dict[str, int]:
    counts = Counter(state.name for state in states)
    return {name: counts.get(name, 0) for name in ("FOCUS", "WATCH", "PASS")}


def _avg(values: list[int]) -> float | None:
    return round(sum(values) / len(values), 3) if values else None


def replay(paths: list[Path]) -> dict[str, Any]:
    boards = []
    total_rows = 0
    old_states: list[BoardState] = []
    repaired_states: list[BoardState] = []
    mismatches = 0
    movements = []
    strong_tail_demotions = []
    old_act_capable = repaired_act_capable = 0

    for path in sorted(paths):
        package = json.loads(path.read_text(encoding="utf-8"))
        native = package.get("native_rank", package)
        payload = native.get("frozen_model_input") or package.get("frozen_c_evidence")
        if not isinstance(payload, dict) or not isinstance(payload.get("matches"), list):
            raise ValueError(f"{path}: frozen Football C input missing")
        raw_rows = payload["matches"]
        parsed = [parse_assessment(raw, require_c_completion=True) for raw in raw_rows]
        raw_by_id = {raw["match_id"]: raw for raw in raw_rows}
        old = sorted(
            parsed,
            key=lambda item: (
                _declared(raw_by_id[item.match_id]), ranking_key(item), item.match_id
            ),
            reverse=True,
        )
        repaired = sorted(
            parsed,
            key=lambda item: (
                compile_c_board_state(item), ranking_key(item), item.match_id
            ),
            reverse=True,
        )
        challenger = sorted(
            parsed,
            key=lambda item: (
                compile_c_board_state(item),
                ranking_key_clearability_challenger(item),
                item.match_id,
            ),
            reverse=True,
        )
        old_rank = {item.match_id: i for i, item in enumerate(old, 1)}
        repaired_rank = {item.match_id: i for i, item in enumerate(repaired, 1)}
        challenger_rank = {item.match_id: i for i, item in enumerate(challenger, 1)}
        states_old = [_declared(raw_by_id[item.match_id]) for item in parsed]
        states_new = [compile_c_board_state(item) for item in parsed]
        old_states.extend(states_old)
        repaired_states.extend(states_new)
        mismatches += sum(a != b for a, b in zip(states_old, states_new))
        total_rows += len(parsed)

        focus = [item for item in parsed if compile_c_board_state(item) == BoardState.FOCUS]
        old_act_capable += sum(
            _declared(raw_by_id[item.match_id]) == BoardState.FOCUS
            and c_direct_act_ceiling(item) is not None
            for item in parsed
        )
        repaired_act_capable += sum(c_direct_act_ceiling(item) is not None for item in focus)
        for item in parsed:
            delta = repaired_rank[item.match_id] - challenger_rank[item.match_id]
            movements.append(abs(delta))
            if funded_goal_certificate_depth(item, "c") >= 4 and delta < 0:
                strong_tail_demotions.append({
                    "run_id": package.get("run_id") or native.get("run_id"),
                    "match_id": item.match_id,
                    "champion_rank": repaired_rank[item.match_id],
                    "challenger_rank": challenger_rank[item.match_id],
                    "certificate_depth": funded_goal_certificate_depth(item, "c"),
                    "robustness": certificate_robustness(item, "c"),
                })

        def top_summary(order: list[Any], n: int) -> dict[str, Any]:
            rows = [
                item for item in order
                if compile_c_board_state(item) == BoardState.FOCUS
            ][:n]
            return {
                "count": len(rows),
                "mean_clearability_score": _avg([
                    int(follow_priority_profile(item)["follow_clearability_score"])
                    for item in rows
                ]),
                "act_capable": sum(c_direct_act_ceiling(item) is not None for item in rows),
                "g4_plus_funded": sum(
                    funded_goal_certificate_depth(item, "c") >= 4 for item in rows
                ),
            }

        boards.append({
            "file": path.name,
            "sha256": _sha(path),
            "run_id": package.get("run_id") or native.get("run_id"),
            "row_count": len(parsed),
            "old_distribution": _distribution(states_old),
            "repaired_distribution": _distribution(states_new),
            "state_mismatches": sum(a != b for a, b in zip(states_old, states_new)),
            "champion_top3": top_summary(repaired, 3),
            "challenger_top3": top_summary(challenger, 3),
            "champion_top5": top_summary(repaired, 5),
            "challenger_top5": top_summary(challenger, 5),
            "rank_movements": [
                {
                    "match_id": item.match_id,
                    "old_declared_state_rank": old_rank[item.match_id],
                    "repaired_champion_rank": repaired_rank[item.match_id],
                    "challenger_rank": challenger_rank[item.match_id],
                }
                for item in parsed
                if old_rank[item.match_id] != repaired_rank[item.match_id]
                or repaired_rank[item.match_id] != challenger_rank[item.match_id]
            ],
            "split_pressure_distribution": {
                "g3": dict(Counter(c_g3_endpoint_control_pressure(item) for item in parsed)),
                "upper_tail": dict(Counter(c_upper_tail_control_pressure(item) for item in parsed)),
            },
        })

    return {
        "schema_version": "football-c-selection-inversion-replay-v1",
        "same_information_replay": True,
        "outcome_fields_read": False,
        "board_count": len(boards),
        "fixture_epoch_count": total_rows,
        "old_declared_distribution": _distribution(old_states),
        "repaired_compiled_distribution": _distribution(repaired_states),
        "declared_compiled_mismatch_count": mismatches,
        "old_declared_focus_act_capable_count": old_act_capable,
        "repaired_compiled_focus_act_capable_count": repaired_act_capable,
        "rank_movement": {
            "moved_count": sum(value > 0 for value in movements),
            "mean_absolute_places": _avg(movements),
            "maximum_places": max(movements, default=0),
        },
        "strong_upper_tail_challenger_demotions": strong_tail_demotions,
        "outcome_separation": {
            "status": "NOT_COMPUTED_NO_PER_FIXTURE_SETTLEMENT_MAP",
            "reason": (
                "sealed rank packages contain prospective evidence only; final "
                "scores were not reconstructed or inferred"
            ),
        },
        "promotion_gate": (
            "CHALLENGER_NOT_PROMOTED_UNTIL_SETTLED_UNIVERSAL_LEDGER_PROVES_"
            "SEPARATION_WITHOUT_COVERAGE_COLLAPSE"
        ),
        "boards": boards,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("inputs", nargs="+", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = replay(args.inputs)
    content = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(content, encoding="utf-8")
    else:
        print(content, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
