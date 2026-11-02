#!/usr/bin/env python3
"""Replay the frozen recent 44 cohort through the current Football C repair.

This is a same-information audit. It reads no result/outcome fields and does not
invent the new research objects required by G3_BORDERLINE_DISCRIMINATION_V2 or
BLOCK_DISCRIMINATION_V2. Instead it runs the current deterministic compiler and
then applies the production fail-closed checkpoint sequence to show exactly
which historical rows the new repair would stop for bounded re-research.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from datetime import datetime, timezone
import copy
import json
from pathlib import Path
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
ENGINE = ROOT / "models" / "football" / "engine"
STAGES = ROOT / "models" / "football" / "stages_v4"
sys.path.insert(0, str(ENGINE))
sys.path.insert(0, str(STAGES))

from adapter import run_board  # noqa: E402
from stage import (  # noqa: E402
    _checkpoint_incomplete_selection_discrimination,
    _checkpoint_incomplete_g4_focus,
    _checkpoint_incomplete_block_discrimination,
)

INPUT = ROOT / "models" / "football" / "qa" / "replays" / "2026-11-02_recent_44_frozen_assessments.json"
AT = datetime(2026, 11, 2, 6, 30, tzinfo=timezone.utc)


def payload(rows: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "schema_version": "football-engine-v1",
        "stage": "board",
        "model": "c",
        "matches": copy.deepcopy(rows),
    }


def board(rows: list[dict[str, Any]]) -> dict[str, Any]:
    if not rows:
        return {"model": "c", "stage": "board_result", "matches": []}
    return run_board(payload(rows))


def replay() -> dict[str, Any]:
    src = json.loads(INPUT.read_text(encoding="utf-8"))
    fixtures = src["fixtures"]
    assert len(fixtures) == 44, len(fixtures)
    assert src.get("outcome_fields_included") is False

    names = {
        str(f["match_id"]): f'{f["match"].get("home")}–{f["match"].get("away")}'
        for f in fixtures
    }
    original_state = {
        str(f["match_id"]): str(f["original_board_state"])
        for f in fixtures
    }
    rows = [copy.deepcopy(f["match"]) for f in fixtures]

    # Current compiler before the new research-completeness checkpoints.
    base = board(rows)
    base_by_id = {str(r["match_id"]): r for r in base["matches"]}
    base_state = Counter(str(r["board_state"]) for r in base["matches"])

    # Preserve original assessment-batch boundaries for a direct ordering audit.
    batches: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for f in fixtures:
        batches[str(f["assessment_at_utc"])].append(copy.deepcopy(f["match"]))
    batch_top = []
    for batch_id, batch_rows in sorted(batches.items()):
        b = board(batch_rows)
        ordered = sorted(
            b["matches"],
            key=lambda r: (int(r.get("rank") or 10**9), str(r.get("match_id"))),
        )
        if ordered:
            top = ordered[0]
            batch_top.append({
                "assessment_batch": batch_id,
                "fixture_count": len(ordered),
                "top_match_id": str(top["match_id"]),
                "top_fixture": names[str(top["match_id"])],
                "top_state": top["board_state"],
                "top_rank": top.get("rank"),
            })

    # Production checkpoint order introduced by the current repair.
    c0 = payload(rows)
    reasons0: dict[str, Any] = {}

    c1, reasons1, selection_pending, selection_reviews = (
        _checkpoint_incomplete_selection_discrimination(
            c0, base, reasons0, at=AT
        )
    )
    after_selection = board(c1["matches"])

    c2, reasons2, g4_pending, _g4_snapshots = _checkpoint_incomplete_g4_focus(
        c1, after_selection, reasons1
    )
    after_g4 = board(c2["matches"])

    c3, reasons3, block_pending, block_reviews = (
        _checkpoint_incomplete_block_discrimination(
            c2, after_g4, reasons2, at=AT
        )
    )
    final_board = board(c3["matches"])

    state_changes = []
    for mid, compiled in sorted(base_by_id.items()):
        old = original_state[mid]
        new = str(compiled["board_state"])
        if old != new:
            state_changes.append({
                "match_id": mid,
                "fixture": names[mid],
                "original_state": old,
                "current_compiled_state": new,
            })

    selection_details = []
    for mid in selection_pending:
        review = selection_reviews[mid]
        selection_details.append({
            "match_id": mid,
            "fixture": names[mid],
            "compiled_state": base_by_id[mid]["board_state"],
            "operational_grade": base_by_id[mid].get("operational_viability_grade"),
            "missing_fields": review.get("missing_fields", []),
        })

    block_details = []
    for review in block_reviews:
        ids = [str(x) for x in review["candidate_match_ids"]]
        block_details.append({
            "block_id": review["block_id"],
            "status": review["status"],
            "candidate_match_ids": ids,
            "fixtures": [names[mid] for mid in ids],
            "engine_order": review.get("engine_order", []),
            "declared_order": review.get("declared_order", []),
            "missing_by_match_id": review.get("missing_by_match_id", {}),
        })

    final_state = Counter(str(r["board_state"]) for r in final_board["matches"])
    all_pending = list(dict.fromkeys(selection_pending + g4_pending + block_pending))

    return {
        "schema_version": "football-c-recent-44-current-repair-replay-v1",
        "base_revision_expected": "cd2d51bcf2fa426d6af8eb9797f40502e2cd02dc",
        "same_information_replay": True,
        "outcome_fields_read": False,
        "source_fixture_count": 44,
        "assessment_batch_count": len(batches),
        "original_state_distribution": dict(sorted(Counter(original_state.values()).items())),
        "current_preflight_state_distribution": dict(sorted(base_state.items())),
        "current_preflight_state_change_count": len(state_changes),
        "current_preflight_state_changes": state_changes,
        "g3_borderline_pending_count": len(selection_pending),
        "g3_borderline_pending_ids": selection_pending,
        "g3_borderline_pending": selection_details,
        "g4_pending_after_borderline_count": len(g4_pending),
        "g4_pending_after_borderline_ids": g4_pending,
        "block_comparison_review_count": len(block_reviews),
        "block_comparison_pending_block_count": sum(
            1 for r in block_reviews if r.get("status") != "COMPLETE"
        ),
        "block_comparison_pending_match_count": len(block_pending),
        "block_comparison_pending_ids": block_pending,
        "block_comparison_reviews": block_details,
        "total_checkpointed_unique_count": len(set(all_pending)),
        "total_checkpointed_unique_ids": sorted(set(all_pending)),
        "finalizable_count_without_new_research": len(c3["matches"]),
        "finalizable_state_distribution": dict(sorted(final_state.items())),
        "finalizable_match_ids": [str(r["match_id"]) for r in final_board["matches"]],
        "reasons_count": len(reasons3),
        "batch_top": batch_top,
    }


def main() -> int:
    result = replay()
    print("RECENT44_CURRENT_REPAIR_REPLAY=" + json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
