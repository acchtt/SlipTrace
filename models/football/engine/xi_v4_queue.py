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
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

STAGE_DIR = Path(__file__).resolve().parents[1] / "stages_v4"
if str(STAGE_DIR) not in sys.path:
    sys.path.insert(0, str(STAGE_DIR))
from stage import StageError as V4StageError, verify_rank_source_and_status


_SHA256 = re.compile(r"^[a-f0-9]{64}$")


class V4XIQueueError(ValueError):
    pass


def _digest(obj: dict[str, Any]) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True,
                 ensure_ascii=True, separators=(",", ":")).encode("utf-8")).hexdigest()


def _instant(value: Any, label: str) -> datetime:
    if not isinstance(value, str):
        raise V4XIQueueError(f"{label}: timezone-aware timestamp required")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise V4XIQueueError(f"{label}: invalid timestamp") from exc
    if parsed.tzinfo is None:
        raise V4XIQueueError(f"{label}: timezone-aware timestamp required")
    return parsed


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
    rank_time = ranked.get("rank_at_utc")
    if not isinstance(rank_time, str):
        raise V4XIQueueError("V4: native rank rank_at_utc required")
    try:
        native_proof = verify_rank_source_and_status(
            source, original_source, status_refresh, now=rank_time
        )
    except (V4StageError, ValueError, KeyError, TypeError) as exc:
        raise V4XIQueueError(f"V4: native rank provenance replay failed: {exc}") from exc
    for field in ("original_source_sha256", "status_refresh_sha256"):
        if native_proof.get(field) != ranked.get(field):
            raise V4XIQueueError(f"V4: native provenance {field} differs from rank")
    status_by_id = native_proof["status_by_match"]
    pair = ranked.get("board_pair")
    if not isinstance(pair, dict) or pair.get("board_engine_execution_status") != "EXECUTED_C_C2_BOARDS" or pair.get("common_evidence_reconciled") is not True:
        raise V4XIQueueError("V4: real reconciled C+C2 paired rank execution missing")
    results = pair.get("results", {})
    if not isinstance(results, dict) or not all(m in results for m in ("c","c2")):
        raise V4XIQueueError("V4: C official and C2 shadow model outputs required")
    expected_model_evidence_sha256 = _digest(results)
    if (readback.get("model_evidence_readback_verified") is not True
            or readback.get("model_evidence_sha256") != expected_model_evidence_sha256):
        raise V4XIQueueError(
            "V4: exact persisted C/C2 Step1 model evidence was not independently verified"
        )
    c = results["c"].get("matches", [])
    c2 = results["c2"].get("matches", [])
    if not isinstance(c,list) or not isinstance(c2,list):
        raise V4XIQueueError("V4: paired ranked rows missing")
    cmap, c2map = ({m.get("match_id"):m for m in rows if isinstance(m,dict)}
                    for rows in (c,c2))
    if len(cmap) != len(c) or len(c2map) != len(c2) or set(cmap) != set(c2map) or len(c) != ranked.get("ranked_count"):
        raise V4XIQueueError("V4: C/C2 ranked cohorts mismatch")
    if any(status_by_id.get(mid) != "PREMATCH_CONFIRMED" for mid in cmap):
        raise V4XIQueueError("V4: ranked XI cohort was not prematch-confirmed in exact rank status refresh")
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
        if _instant(b.get("kickoff_utc"), f"{mid}.board_kickoff") != _instant(
                original[mid].get("kickoff_utc"), f"{mid}.source_kickoff"):
            raise V4XIQueueError(f"V4: {mid} kickoff does not match original source")
        if b.get("coverage_id") != f"{run_id}|{mid}":
            raise V4XIQueueError(f"V4: {mid} immutable Airtable coverage identity invalid")
    return {"source_run_id":run_id,
            "board_snapshot_id":ranked["integrity_sha256"],
            "v4_verified":True,
            "v4_provenance_chain_verified":True,
            "v4_original_source_sha256":ranked["original_source_sha256"],
            "v4_status_refresh_sha256":ranked["status_refresh_sha256"],
            "v4_rank_sha256":ranked["integrity_sha256"],
            "v4_model_evidence_sha256":expected_model_evidence_sha256}
