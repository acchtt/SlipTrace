#!/usr/bin/env python3
"""Same-information replay of the frozen recent 44 through current Football C.

The audit deliberately does not use outcomes, bookmaker results, or post-match
facts. Historical research payloads are parsed directly through the current C
core so legacy G4 declarations cannot abort the entire cohort before selection
discrimination is measured. Any declaration that now contradicts deterministic
G4 funding is recorded as contract drift and treated as non-finalizable.
"""
from __future__ import annotations

from collections import Counter, defaultdict
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

from adapter import parse_assessment  # noqa: E402
from core import (  # noqa: E402
    compile_c_board_state,
    funded_goal_certificate_depth,
    ranking_key,
)
from selection_discrimination import review_borderline_recheck  # noqa: E402
from block_discrimination import comparison_blocks, review_block  # noqa: E402

INPUT = ROOT / "models" / "football" / "qa" / "replays" / "2026-11-02_recent_44_frozen_assessments.json"


def compile_rows(raw_rows: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    parsed = []
    parsed_by_id = {}
    raw_by_id = {}
    for raw in raw_rows:
        a = parse_assessment(raw, require_c_completion=True)
        mid = str(a.match_id)
        parsed.append(a)
        parsed_by_id[mid] = a
        raw_by_id[mid] = raw

    ordered = sorted(
        parsed,
        key=lambda a: (compile_c_board_state(a), ranking_key(a), str(a.match_id)),
        reverse=True,
    )
    compiled = []
    for rank, a in enumerate(ordered, 1):
        mid = str(a.match_id)
        raw = raw_by_id[mid]
        depth = funded_goal_certificate_depth(a, "c")
        compiled.append({
            "match_id": mid,
            "board_state": compile_c_board_state(a).name,
            "rank": rank,
            "operational_viability_grade": str(raw.get("operational_viability_grade") or ""),
            "goal3_funded": depth >= 3,
            "goal4_funded": depth >= 4,
            "funded_depth": depth,
            "kickoff_ict": raw.get("kickoff_ict"),
        })
    return compiled, parsed_by_id


def g4_contract_drift(raw: dict[str, Any], compiled: dict[str, Any]) -> str | None:
    status = raw.get("g4_research_status")
    goal3 = bool(compiled["goal3_funded"])
    goal4 = bool(compiled["goal4_funded"])
    if status is None:
        return None
    normalized = "G4_RESEARCH_COMPLETE_REJECTED" if status == "G4_RESEARCH_COMPLETE_MIXED" else status
    if normalized == "G4_NOT_APPLICABLE" and goal3:
        return "G4_NOT_APPLICABLE_BUT_G3_FUNDED"
    if normalized != "G4_NOT_APPLICABLE" and not goal3:
        return "G4_STATUS_REQUIRES_G3_BUT_G3_NOT_FUNDED"
    if normalized == "G4_RESEARCH_COMPLETE_FUNDED" and not goal4:
        return "DECLARED_G4_FUNDED_BUT_CURRENT_CORE_NOT_FUNDED"
    if normalized in {
        "G4_RESEARCH_INCOMPLETE",
        "G4_RESEARCH_COMPLETE_REJECTED",
        "G4_RESEARCH_EVIDENCE_LIMITED",
    } and goal4:
        return "DECLARED_G4_NOT_FUNDED_BUT_CURRENT_CORE_FUNDED"
    return None


def replay() -> dict[str, Any]:
    src = json.loads(INPUT.read_text(encoding="utf-8"))
    fixtures = src["fixtures"]
    assert len(fixtures) == 44, len(fixtures)
    assert src.get("outcome_fields_included") is False

    raws = [copy.deepcopy(f["match"]) for f in fixtures]
    raw_by_id = {str(r["match_id"]): r for r in raws}
    names = {
        str(f["match_id"]): f'{f["match"].get("home")}–{f["match"].get("away")}'
        for f in fixtures
    }
    original_state = {
        str(f["match_id"]): str(f["original_board_state"])
        for f in fixtures
    }

    compiled, _parsed = compile_rows(raws)
    compiled_by_id = {str(r["match_id"]): r for r in compiled}

    current_state_dist = Counter(str(r["board_state"]) for r in compiled)
    state_changes = []
    for mid in sorted(compiled_by_id):
        new = str(compiled_by_id[mid]["board_state"])
        old = original_state[mid]
        if new != old:
            state_changes.append({
                "match_id": mid,
                "fixture": names[mid],
                "original_state": old,
                "current_compiled_state": new,
            })

    # Record legacy metadata that current production adapter would reject before
    # selection finalization.
    drift = []
    for mid in sorted(raw_by_id):
        reason = g4_contract_drift(raw_by_id[mid], compiled_by_id[mid])
        if reason:
            drift.append({
                "match_id": mid,
                "fixture": names[mid],
                "reason": reason,
                "declared_g4_research_status": raw_by_id[mid].get("g4_research_status"),
                "current_funded_depth": compiled_by_id[mid]["funded_depth"],
            })
    drift_ids = {r["match_id"] for r in drift}

    # Current G3 borderline gate.
    selection_reviews = {}
    selection_pending = []
    for raw in raws:
        mid = str(raw["match_id"])
        review = review_borderline_recheck(raw, compiled_by_id[mid])
        selection_reviews[mid] = review
        if review.get("required") is True and review.get("status") != "COMPLETE":
            selection_pending.append(mid)

    selection_pending_set = set(selection_pending)

    # Production sequence removes borderline-pending rows before block
    # discrimination. Contract-drift rows are also non-finalizable under current
    # adapter, so exclude them from the block-finalization set while preserving
    # their current-core state in the audit above.
    remaining_raws = [
        raw for raw in raws
        if str(raw["match_id"]) not in selection_pending_set
        and str(raw["match_id"]) not in drift_ids
    ]
    remaining_compiled, _ = compile_rows(remaining_raws) if remaining_raws else ([], {})

    block_reviews = []
    block_pending_ids: set[str] = set()
    for block in comparison_blocks(remaining_raws, remaining_compiled):
        review = review_block(block)
        block_reviews.append(review)
        if review.get("status") != "COMPLETE":
            block_pending_ids.update(str(mid) for mid in review["candidate_match_ids"])

    finalizable_ids = [
        str(r["match_id"]) for r in remaining_compiled
        if str(r["match_id"]) not in block_pending_ids
    ]
    finalizable = [r for r in remaining_compiled if str(r["match_id"]) in set(finalizable_ids)]

    # Preserve original assessment-batch boundaries and report the current
    # core's top-ranked row in each historical batch.
    batches: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for f in fixtures:
        batches[str(f["assessment_at_utc"])].append(copy.deepcopy(f["match"]))
    batch_top = []
    for batch_id, batch_raws in sorted(batches.items()):
        batch_compiled, _ = compile_rows(batch_raws)
        if batch_compiled:
            top = batch_compiled[0]
            batch_top.append({
                "assessment_batch": batch_id,
                "fixture_count": len(batch_compiled),
                "top_match_id": str(top["match_id"]),
                "top_fixture": names[str(top["match_id"])],
                "top_state": top["board_state"],
                "top_funded_depth": top["funded_depth"],
            })

    selection_detail = []
    for mid in selection_pending:
        review = selection_reviews[mid]
        selection_detail.append({
            "match_id": mid,
            "fixture": names[mid],
            "compiled_state": compiled_by_id[mid]["board_state"],
            "operational_grade": compiled_by_id[mid]["operational_viability_grade"],
            "funded_depth": compiled_by_id[mid]["funded_depth"],
            "missing_fields": review.get("missing_fields", []),
        })

    block_detail = []
    for review in block_reviews:
        ids = [str(x) for x in review["candidate_match_ids"]]
        block_detail.append({
            "block_id": review["block_id"],
            "status": review["status"],
            "candidate_match_ids": ids,
            "fixtures": [names[mid] for mid in ids],
            "engine_order": review.get("engine_order", []),
            "declared_order": review.get("declared_order", []),
            "missing_by_match_id": review.get("missing_by_match_id", {}),
        })

    final_state_dist = Counter(str(r["board_state"]) for r in finalizable)
    all_checkpointed = set(selection_pending) | drift_ids | block_pending_ids

    return {
        "schema_version": "football-c-recent-44-current-repair-replay-v2",
        "same_information_replay": True,
        "outcome_fields_read": False,
        "source_fixture_count": 44,
        "assessment_batch_count": len(batches),
        "original_state_distribution": dict(sorted(Counter(original_state.values()).items())),
        "current_core_state_distribution": dict(sorted(current_state_dist.items())),
        "current_core_state_change_count": len(state_changes),
        "current_core_state_changes": state_changes,
        "g4_contract_drift_count": len(drift),
        "g4_contract_drift": drift,
        "g3_borderline_pending_count": len(selection_pending),
        "g3_borderline_pending_ids": selection_pending,
        "g3_borderline_pending": selection_detail,
        "block_comparison_review_count": len(block_reviews),
        "block_comparison_pending_block_count": sum(
            1 for r in block_reviews if r.get("status") != "COMPLETE"
        ),
        "block_comparison_pending_match_count": len(block_pending_ids),
        "block_comparison_pending_ids": sorted(block_pending_ids),
        "block_comparison_reviews": block_detail,
        "total_checkpointed_unique_count": len(all_checkpointed),
        "total_checkpointed_unique_ids": sorted(all_checkpointed),
        "finalizable_without_new_research_count": len(finalizable_ids),
        "finalizable_without_new_research_ids": finalizable_ids,
        "finalizable_state_distribution": dict(sorted(final_state_dist.items())),
        "historical_batch_top": batch_top,
    }


def main() -> int:
    result = replay()
    print("RECENT44_CURRENT_REPAIR_REPLAY=" + json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
