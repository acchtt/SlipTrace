"""Source-anchored V4 routine /xi authorization. No Airtable or network I/O.

The caller MUST independently refetch Airtable and run stage.py verify
first. This validator separately checks frozen V4 source/rank hashes,
official C and shadow C2 board contents and the readback receipt;
the old V1-V3 packaged work_ready workflow is not an accepted substitute.
"""
from __future__ import annotations

import hashlib
import json
import re
from typing import Any


_SHA256 = re.compile(r"^[a-f0-9]{64}$")


class V4XIQueueError(ValueError):
    pass


def _digest(obj: dict[str, Any]) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True,
                 ensure_ascii=True, separators=(",", ":")).encode("utf-8")).hexdigest()


def _sealed(obj: Any, label: str, status: str) -> None:
    if not isinstance(obj, dict) or obj.get("schema_version") != "football-stages-v4" or obj.get("status") != status:
        raise V4XIQueueError(f"{label}: original {status} required")
    expected = obj.get("integrity_sha256")
    if not isinstance(expected, str) or expected != _digest({k:v for k,v in obj.items() if k != "integrity_sha256"}):
        raise V4XIQueueError(f"{label}: V4 frozen SHA256 integrity mismatch")


def validate_v4_queue_authority(data: dict[str, Any], board: list[dict[str, Any]]) -> dict[str, Any]:
    source, ranked, readback = (data.get(name) for name in (
        "v4_sweep_receipt", "v4_rank_receipt", "v4_persistence_receipt"))
    original_source = data.get("v4_original_source")
    status_refresh = data.get("v4_status_refresh")
    _sealed(source, "sweep", "V4_SWEEP_READY")
    _sealed(ranked, "rank", "V4_RANK_EXECUTED_AWAITING_AIRTABLE_READBACK")
    if not isinstance(readback, dict) or readback.get("schema_version") != "football-stages-v4" or readback.get("status") != "V4_RANK_PERSISTENCE_VERIFIED":
        raise V4XIQueueError("V4: real independently refetched Airtable rank verification required")
    run_id = source["run_id"]
    if not isinstance(run_id, str) or not run_id.startswith("V4-") or (
        ranked.get("run_id") != run_id or readback.get("run_id") != run_id):
        raise V4XIQueueError("V4: source, rank and persistence run IDs differ")
    if ranked.get("sweep_integrity_sha256") != source["integrity_sha256"] or readback.get("rank_sha256") != ranked["integrity_sha256"]:
        raise V4XIQueueError("V4: source/rank/persistence chain broken")
    if readback.get("ranked_count") != ranked.get("ranked_count") or readback.get("c2_shadow_only") is not True:
        raise V4XIQueueError("V4: persisted cohort or C2-shadow authority invalid")
    if ranked.get("source_replayed") is not True or ranked.get("current_fixture_status_checked") is not True:
        raise V4XIQueueError("V4: rank lacks mandatory original-source replay/current-status proof")
    if readback.get("source_replayed") is not True or readback.get("current_fixture_status_checked") is not True:
        raise V4XIQueueError("V4: persistence receipt did not preserve rank provenance proof")
    for field in ("original_source_sha256", "status_refresh_sha256"):
        value = ranked.get(field)
        if not isinstance(value, str) or not _SHA256.fullmatch(value):
            raise V4XIQueueError(f"V4: rank {field} missing/invalid")
        if readback.get(field) != value:
            raise V4XIQueueError(f"V4: persistence {field} differs from verified rank")
    if not isinstance(original_source, dict) or _digest(original_source) != ranked["original_source_sha256"]:
        raise V4XIQueueError("V4: unchanged original source payload/hash required for routine XI")
    if not isinstance(status_refresh, dict) or _digest(status_refresh) != ranked["status_refresh_sha256"]:
        raise V4XIQueueError("V4: exact rank status-refresh payload/hash required for routine XI")
    if (status_refresh.get("schema_version") != "football-v4-rank-status-refresh-v1"
            or status_refresh.get("run_id") != run_id
            or status_refresh.get("sweep_integrity_sha256") != source["integrity_sha256"]):
        raise V4XIQueueError("V4: status-refresh source/run binding invalid")
    status_rows = status_refresh.get("matches")
    original_ids = {m.get("match_id") for m in source.get("eligible_queue", []) if isinstance(m, dict)}
    if not isinstance(status_rows, list) or len(status_rows) != len(original_ids):
        raise V4XIQueueError("V4: status-refresh must cover the full frozen eligible cohort")
    status_by_id = {m.get("match_id"): m.get("fixture_status") for m in status_rows if isinstance(m, dict)}
    if set(status_by_id) != original_ids or any(v != "PREMATCH_CONFIRMED" for v in status_by_id.values()):
        raise V4XIQueueError("V4: routine XI requires the exact prematch status-refresh cohort used by rank")
    pair = ranked.get("board_pair")
    if not isinstance(pair, dict) or pair.get("board_engine_execution_status") != "EXECUTED_C_C2_BOARDS" or pair.get("common_evidence_reconciled") is not True:
        raise V4XIQueueError("V4: real reconciled C+C2 paired rank execution missing")
    results = pair.get("results", {})
    if not isinstance(results, dict) or not all(m in results for m in ("c","c2")):
        raise V4XIQueueError("V4: C official and C2 shadow model outputs required")
    c = results["c"].get("matches", [])
    c2 = results["c2"].get("matches", [])
    if not isinstance(c,list) or not isinstance(c2,list):
        raise V4XIQueueError("V4: paired ranked rows missing")
    cmap, c2map = ({m.get("match_id"):m for m in rows if isinstance(m,dict)}
                    for rows in (c,c2))
    if len(cmap) != len(c) or len(c2map) != len(c2) or set(cmap) != set(c2map) or len(c) != ranked.get("ranked_count"):
        raise V4XIQueueError("V4: C/C2 ranked cohorts mismatch")
    original = {m.get("match_id"):m for m in source.get("eligible_queue", []) if isinstance(m,dict)}
    if set(cmap) - set(original):
        raise V4XIQueueError("V4: out-of-sweep ranked match")
    if len(board) != len(cmap) or {b.get("match_id") for b in board if isinstance(b,dict)} != set(cmap):
        raise V4XIQueueError("V4: the complete verified ranked board is required")
    if len({b.get("match_id") for b in board}) != len(board):
        raise V4XIQueueError("V4: duplicate fixture in board")
    for b in board:
        mid = b["match_id"]
        cr, sh = cmap[mid], c2map[mid]
        if b.get("official_follow_lane") != cr.get("follow_lane"):
            raise V4XIQueueError(f"V4: {mid} C official follow lane differs from engine")
        if b.get("c_board_state") != "C-"+str(cr.get("board_state")):
            raise V4XIQueueError(f"V4: {mid} C board state differs")
        if b.get("c2_shadow_state") != "C2-"+str(sh.get("board_state")):
            raise V4XIQueueError(f"V4: {mid} C2 shadow state differs")
        if b.get("c_supported_line") != cr.get("supported_line") or b.get("c2_supported_line") != sh.get("supported_line"):
            raise V4XIQueueError(f"V4: {mid} supported burdens do not match frozen C/C2 rank")
        if b.get("kickoff_utc") != original[mid].get("kickoff_utc"):
            raise V4XIQueueError(f"V4: {mid} kickoff does not match original source")
        if b.get("coverage_id") != f"{run_id}|{mid}":
            raise V4XIQueueError(f"V4: {mid} immutable Airtable coverage identity invalid")
    return {"source_run_id":run_id,
            "board_snapshot_id":ranked["integrity_sha256"],
            "v4_verified":True,
            "v4_provenance_chain_verified":True,
            "v4_original_source_sha256":ranked["original_source_sha256"],
            "v4_status_refresh_sha256":ranked["status_refresh_sha256"],
            "v4_rank_sha256":ranked["integrity_sha256"]}
