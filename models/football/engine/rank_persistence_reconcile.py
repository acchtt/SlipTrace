#!/usr/bin/env python3
"""Independent Step1 persistence readback guard, no model or market decisions.

The caller must fetch active Airtable records again by immutable match ID.
A saved notebook or pre-write payload is NOT independent readback.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

ACTIVE_BASE = "appbzxqXYf0lKfD4P"
SCHEMA = "football-step1-readback-v1"
UNRANKED_REASONS = {
    "RESEARCH_BUDGET_EXHAUSTED",
    "PREMATCH_WINDOW_CLOSED",
    "MISSING_FOOTBALL_EVIDENCE",
    "SOURCE_IDENTITY_UNRESOLVED",
    "NOT_SELECTED_BY_GOAL_SCREEN",
}


class RankReadbackError(ValueError):
    pass


def _rows(records: Any, label: str) -> dict[str, dict[str, Any]]:
    if not isinstance(records, list):
        raise RankReadbackError(f"{label}: rows must be a list")
    indexed: dict[str, dict[str, Any]] = {}
    for row in records:
        if not isinstance(row, dict) or not isinstance(row.get("match_id"), str):
            raise RankReadbackError(f"{label}: match_id missing")
        mid = row["match_id"].strip()
        if not mid or mid in indexed or mid.upper().startswith("DISCOVERY-"):
            raise RankReadbackError(f"{label}: duplicate/provisional match_id: {mid}")
        indexed[mid] = row
    return indexed


def _ranks(rows: dict[str, dict[str, Any]], key: str, label: str) -> None:
    ranks = [r.get(key) for r in rows.values()]
    if any(type(rank) is not int for rank in ranks) or sorted(ranks) != list(range(1, len(rows) + 1)):
        raise RankReadbackError(f"{label}: noncontiguous/duplicate {key}")


def validate_rank_readback(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict) or payload.get("schema_version") != SCHEMA:
        raise RankReadbackError("readback schema_version invalid")
    run_id, source_hash = payload.get("run_id"), payload.get("source_payload_hash")
    if not isinstance(run_id, str) or not run_id.startswith("SWEEP-"):
        raise RankReadbackError("frozen run_id missing")
    if not isinstance(source_hash, str) or len(source_hash) < 8:
        raise RankReadbackError("frozen source hash missing")
    if payload.get("active_base_id") != ACTIVE_BASE or payload.get("readback_method") != "INDEPENDENT_AIRTABLE_REFETCH":
        raise RankReadbackError("active Airtable independent readback not attested")
    at = payload.get("readback_at_utc")
    try:
        stamp = datetime.fromisoformat(at.replace("Z", "+00:00"))
        if stamp.tzinfo is None:
            raise ValueError("missing timezone")
    except (ValueError, AttributeError):
        raise RankReadbackError("readback UTC timestamp invalid") from None
    queue = _rows(payload.get("frozen_ab_queue"), "frozen queue")
    _ranks(queue, "step0_capacity_queue_rank", "frozen queue")
    pair = payload.get("board_pair")
    if not isinstance(pair, dict) or pair.get("board_engine_execution_status") != "EXECUTED_C_C2_BOARDS" or pair.get("common_evidence_reconciled") is not True:
        raise RankReadbackError("C+C2 paired engine not verified")
    results = pair.get("results")
    if not isinstance(results, dict) or set(results) != {"c", "c2"}:
        raise RankReadbackError("C+C2 independent results required")
    c = _rows(results["c"].get("matches"), "C engine")
    c2 = _rows(results["c2"].get("matches"), "C2 engine")
    if set(c) != set(c2) or not set(c).issubset(queue):
        raise RankReadbackError("ranked C/C2 fixture universe diverges from frozen A/B queue")
    _ranks(c, "rank", "C engine")
    _ranks(c2, "rank", "C2 engine")
    persisted = _rows(payload.get("readback_rows"), "Airtable readback")
    if set(persisted) != set(c):
        raise RankReadbackError("Airtable rank readback missing/extra fixture IDs")
    fields = {
        "c": ("c_rank", "c_board_state", "c_supported_line"),
        "c2": ("c2_rank", "c2_board_state", "c2_supported_line"),
    }
    for mid, stored in persisted.items():
        if stored.get("run_id") != run_id or stored.get("source_payload_hash") != source_hash:
            raise RankReadbackError(f"{mid}: source epoch/readback provenance mismatch")
        if stored.get("step0_capacity_queue_rank") != queue[mid]["step0_capacity_queue_rank"]:
            raise RankReadbackError(f"{mid}: immutable Step0 rank altered")
        for model, engine_rows in (("c", c), ("c2", c2)):
            r = engine_rows[mid]
            for local, remote in zip(("rank", "board_state", "supported_line"), fields[model]):
                if r.get(local) != stored.get(remote):
                    raise RankReadbackError(f"{mid}: {model} {local} differs from Airtable")
        if c[mid].get("follow_lane") != stored.get("follow_lane"):
            raise RankReadbackError(f"{mid}: C FOLLOW/RESERVE/STOP differs from Airtable")
    reasons = payload.get("unranked_reasons")
    if not isinstance(reasons, dict) or set(reasons) != set(queue) - set(c):
        raise RankReadbackError("missing/extra reasons for unranked frozen candidates")
    if any(reason not in UNRANKED_REASONS for reason in reasons.values()):
        raise RankReadbackError("unknown unranked reason (do not invent C PASS)")
    terminal = payload.get("terminal_status")
    if not isinstance(terminal, dict) or terminal.get("complete") is not True or terminal.get("blocked") is not False:
        raise RankReadbackError("rank terminal status not complete")
    if terminal.get("ranked_eligible_count") != len(c):
        raise RankReadbackError("rank terminal count differs from paired engine")
    if terminal.get("follow_count") != sum(r.get("follow_lane") == "FOLLOW" for r in c.values()):
        raise RankReadbackError("FOLLOW count differs from paired engine")
    if terminal.get("reserve_count") != sum(r.get("follow_lane") == "RESERVE" for r in c.values()):
        raise RankReadbackError("RESERVE count differs from paired engine")
    if terminal.get("stop_count") != sum(r.get("follow_lane") == "STOP" for r in c.values()):
        raise RankReadbackError("STOP count differs from paired engine")
    return {
        "status": "STEP1_PERSISTENCE_READBACK_VERIFIED",
        "run_id": run_id,
        "source_payload_hash": source_hash,
        "active_base_id": ACTIVE_BASE,
        "ranked_count": len(c),
        "unranked_count": len(reasons),
        "verified_match_ids": sorted(c),
        "unranked_reasons": reasons,
        "readback_at_utc": stamp.isoformat(),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify persisted Step1 C+C2 against fresh Airtable readback")
    parser.add_argument("--input", required=True)
    args = parser.parse_args()
    try:
        receipt = validate_rank_readback(json.loads(Path(args.input).read_text(encoding="utf-8")))
        print(json.dumps(receipt, indent=2, sort_keys=True))
        return 0
    except (RankReadbackError, OSError, ValueError, TypeError, KeyError) as exc:
        print(json.dumps({"status": "STEP1_PERSISTENCE_READBACK_FAILED", "error": str(exc)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
