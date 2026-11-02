"""Fail-closed block comparison for Football C selection research.

The engine remains authoritative. This contract forces multi-candidate blocks to
show the football comparison that produced their grades. A declared comparison
cannot override the deterministic engine; disagreement means the factual grades
must be rechecked/reconciled before the block is considered complete.
"""
from __future__ import annotations

from datetime import datetime
from typing import Any

POLICY = "BLOCK_DISCRIMINATION_V2"
REQUIRED_BASES = (
    "g3_strength_basis",
    "g4_strength_basis",
    "carrier_self_funding_basis",
    "reply_dependence_basis",
    "endpoint_exposure_basis",
    "continuation_basis",
    "tournament_incentive_basis",
    "supported_burden_basis",
    "beats_next_basis",
)
THIN = frozenset({
    "CHECKED", "OK", "YES", "NO", "MEDIUM", "HIGH", "LOW", "UNKNOWN",
    "TBD", "N/A", "NA", "SAME", "UNCHANGED",
})


def _kickoff(row: dict[str, Any]) -> datetime:
    value = row.get("kickoff_ict")
    if not isinstance(value, str):
        raise ValueError("kickoff_ict required")
    parsed = datetime.fromisoformat(value)
    if parsed.tzinfo is None:
        raise ValueError("kickoff_ict must be timezone-aware")
    return parsed


def comparison_blocks(
    raw_rows: list[dict[str, Any]],
    compiled_rows: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Build deterministic credible blocks: <=60m adjacent, <=90m total span."""

    compiled = {
        str(row.get("match_id")): row
        for row in compiled_rows if isinstance(row, dict)
    }
    credible = []
    for raw in raw_rows:
        mid = str(raw.get("match_id"))
        out = compiled.get(mid)
        if not isinstance(out, dict):
            continue
        if out.get("board_state") not in {"FOCUS", "WATCH"}:
            continue
        if out.get("operational_viability_grade") != "A":
            continue
        credible.append((raw, out, _kickoff(raw)))

    credible.sort(key=lambda item: (item[2], str(item[0].get("match_id"))))
    groups: list[list[tuple[dict[str, Any], dict[str, Any], datetime]]] = []
    current = []
    for item in credible:
        if not current:
            current = [item]
            continue
        start = current[0][2]
        prev = current[-1][2]
        now = item[2]
        if (now - prev).total_seconds() <= 3600 and (now - start).total_seconds() <= 5400:
            current.append(item)
        else:
            groups.append(current)
            current = [item]
    if current:
        groups.append(current)

    blocks = []
    for group in groups:
        if len(group) < 2:
            continue
        if not any(out.get("board_state") == "FOCUS" for _, out, _ in group):
            continue
        ids = [str(raw.get("match_id")) for raw, _, _ in group]
        blocks.append({
            "block_id": (
                group[0][2].isoformat(timespec="minutes")
                + "__"
                + group[-1][2].isoformat(timespec="minutes")
            ),
            "candidate_match_ids": ids,
            "rows": group,
        })
    return blocks


def review_block(block: dict[str, Any]) -> dict[str, Any]:
    ids = list(block["candidate_match_ids"])
    missing_by_id: dict[str, list[str]] = {}
    declared_ranks: dict[str, int] = {}
    engine_ranks: dict[str, int] = {}

    for raw, compiled, _ in block["rows"]:
        mid = str(raw.get("match_id"))
        engine_ranks[mid] = int(compiled.get("rank"))
        proof = raw.get("block_comparison")
        missing: list[str] = []
        if not isinstance(proof, dict):
            missing.append("block_comparison")
            proof = {}
        if proof.get("contract") != POLICY:
            missing.append("contract")
        if proof.get("completed") is not True:
            missing.append("completed")
        if proof.get("market_independent") is not True:
            missing.append("market_independent")
        if proof.get("block_id") != block["block_id"]:
            missing.append("block_id")
        declared_ids = proof.get("candidate_match_ids")
        if not isinstance(declared_ids, list) or declared_ids != ids:
            missing.append("candidate_match_ids")
        if proof.get("same_depth_completed") is not True:
            missing.append("same_depth_completed")

        rank = proof.get("block_rank")
        if not isinstance(rank, int) or rank < 1 or rank > len(ids):
            missing.append("block_rank")
        else:
            declared_ranks[mid] = rank

        refs = proof.get("evidence_refs")
        if (
            not isinstance(refs, list)
            or len({str(x).strip() for x in refs if isinstance(x, str) and x.strip()}) < 2
        ):
            missing.append("evidence_refs")

        for key in REQUIRED_BASES:
            value = proof.get(key)
            if not isinstance(value, str):
                missing.append(key)
                continue
            normalized = value.strip()
            token = normalized.upper().replace("-", "_").replace(" ", "_")
            if len(normalized) < 24 or token in THIN:
                missing.append(key)

        if missing:
            missing_by_id[mid] = sorted(set(missing))

    ranks_complete = (
        len(declared_ranks) == len(ids)
        and sorted(declared_ranks.values()) == list(range(1, len(ids) + 1))
    )
    if not ranks_complete:
        for mid in ids:
            missing_by_id.setdefault(mid, []).append("unique_block_rank_1_to_n")

    # Compare relative order, not global rank values.
    declared_order = [
        mid for mid, _ in sorted(declared_ranks.items(), key=lambda kv: (kv[1], kv[0]))
    ] if ranks_complete else []
    engine_order = [
        mid for mid, _ in sorted(engine_ranks.items(), key=lambda kv: (kv[1], kv[0]))
    ]
    reconciled = bool(declared_order) and declared_order == engine_order
    if ranks_complete and not reconciled:
        for mid in ids:
            missing_by_id.setdefault(mid, []).append(
                "declared_block_order_must_reconcile_with_engine_inputs"
            )

    return {
        "policy": POLICY,
        "block_id": block["block_id"],
        "candidate_match_ids": ids,
        "status": "COMPLETE" if not missing_by_id and reconciled else "PENDING",
        "missing_by_match_id": {
            mid: sorted(set(fields)) for mid, fields in missing_by_id.items()
        },
        "declared_order": declared_order,
        "engine_order": engine_order,
        "engine_reconciled": reconciled,
        "no_override_authority": True,
        "outcome_fields_read": False,
    }
