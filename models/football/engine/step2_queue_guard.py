#!/usr/bin/env python3
"""Small Step-2 authorization guard for active V4 Football C+C2.

Step 1 already replays the original source, refreshes fixture status, executes
C/C2 and independently verifies Airtable persistence. Step 2 therefore verifies
that one sealed rank+persistence chain and the board rows it is about to use;
it does NOT replay source acquisition a second time.

Active modes:
- V4_ROUTINE: verified ranked board; FOLLOW is routine, RESERVE needs activation.
- EXCEPTION_ONLY: explicit user-requested fixture, no imported board authority.

Retired V1-V3 packaging/terminal routes are intentionally unsupported.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import re
import sys
from typing import Any


VERSION = "football-step2-queue-v2"
LANES = {"FOLLOW", "RESERVE", "STOP"}
ISO_ICT = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+07:00$")


class Step2QueueError(ValueError):
    pass


def _digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(
            value, sort_keys=True, ensure_ascii=True, separators=(",", ":")
        ).encode("utf-8")
    ).hexdigest()


def _text(row: dict[str, Any], key: str) -> str:
    value = row.get(key)
    if not isinstance(value, str) or not value.strip():
        raise Step2QueueError(f"{key} must be non-empty")
    return value.strip()


def _quarter(value: object, key: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise Step2QueueError(f"{key} must be a numeric supported quarter line")
    line = float(value)
    if not math.isfinite(line) or line < 0 or abs(line * 4 - round(line * 4)) > 1e-8:
        raise Step2QueueError(f"{key} must be a supported quarter line")
    return line


def _list(row: dict[str, Any], key: str) -> list:
    value = row.get(key)
    if not isinstance(value, list):
        raise Step2QueueError(f"{key} must be an array")
    return value


def _sealed_rank_chain(data: dict[str, Any], board: list[dict[str, Any]]) -> dict[str, str]:
    rank = data.get("v4_rank_receipt")
    persisted = data.get("v4_persistence_receipt")
    if not isinstance(rank, dict) or not isinstance(persisted, dict):
        raise Step2QueueError(
            "V4 routine requires sealed rank and persistence receipts"
        )
    if (
        rank.get("schema_version") != "football-stages-v4"
        or rank.get("status") != "V4_RANK_EXECUTED_AWAITING_AIRTABLE_READBACK"
    ):
        raise Step2QueueError("V4 rank receipt invalid")
    rank_hash = rank.get("integrity_sha256")
    expected_rank_hash = _digest({
        key: value for key, value in rank.items() if key != "integrity_sha256"
    })
    if rank_hash != expected_rank_hash:
        raise Step2QueueError("V4 rank receipt integrity mismatch")

    if (
        persisted.get("schema_version") != "football-stages-v4"
        or persisted.get("status") != "V4_RANK_PERSISTENCE_VERIFIED"
        or persisted.get("run_id") != rank.get("run_id")
        or persisted.get("rank_sha256") != rank_hash
        or persisted.get("ranked_count") != rank.get("ranked_count")
        or persisted.get("c2_shadow_only") is not True
        or persisted.get("model_evidence_readback_verified") is not True
    ):
        raise Step2QueueError("V4 rank persistence chain invalid")

    if (
        rank.get("source_replayed") is not True
        or rank.get("current_fixture_status_checked") is not True
        or persisted.get("source_replayed") is not True
        or persisted.get("current_fixture_status_checked") is not True
    ):
        raise Step2QueueError("V4 Step1 source/status verification missing")

    pair = rank.get("board_pair")
    if (
        not isinstance(pair, dict)
        or pair.get("board_engine_execution_status") != "EXECUTED_C_C2_BOARDS"
        or pair.get("common_evidence_reconciled") is not True
    ):
        raise Step2QueueError("V4 C/C2 board pair missing")
    results = pair.get("results")
    if not isinstance(results, dict) or set(results) != {"c", "c2"}:
        raise Step2QueueError("V4 C/C2 board results incomplete")
    evidence_hash = _digest(results)
    if persisted.get("model_evidence_sha256") != evidence_hash:
        raise Step2QueueError("V4 persisted C/C2 model evidence differs")

    c_rows = results["c"].get("matches")
    c2_rows = results["c2"].get("matches")
    if not isinstance(c_rows, list) or not isinstance(c2_rows, list):
        raise Step2QueueError("V4 board rows missing")
    c = {row.get("match_id"): row for row in c_rows if isinstance(row, dict)}
    c2 = {row.get("match_id"): row for row in c2_rows if isinstance(row, dict)}
    if len(c) != len(c_rows) or len(c2) != len(c2_rows) or set(c) != set(c2):
        raise Step2QueueError("V4 C/C2 ranked cohorts mismatch")
    if len(board) != len(c) or {row.get("match_id") for row in board} != set(c):
        raise Step2QueueError("complete verified V4 board required")

    for row in board:
        mid = _text(row, "match_id")
        if row.get("official_follow_lane") != c[mid].get("follow_lane"):
            raise Step2QueueError(f"{mid}: C lane differs from verified rank")
        if row.get("c_board_state") != "C-" + str(c[mid].get("board_state")):
            raise Step2QueueError(f"{mid}: C board state differs from verified rank")
        if row.get("c2_shadow_state") != "C2-" + str(c2[mid].get("board_state")):
            raise Step2QueueError(f"{mid}: C2 state differs from verified rank")
        if row.get("c_supported_line") != c[mid].get("supported_line"):
            raise Step2QueueError(f"{mid}: C supported line differs from verified rank")
        if row.get("c2_supported_line") != c2[mid].get("supported_line"):
            raise Step2QueueError(f"{mid}: C2 supported line differs from verified rank")

    return {
        "source_run_id": rank["run_id"],
        "board_snapshot_id": rank_hash,
        "model_evidence_sha256": evidence_hash,
    }


def freeze_queue(data: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(data, dict) or data.get("schema_version") != VERSION:
        raise Step2QueueError(f"schema_version must be {VERSION}")
    session_id = _text(data, "session_id")
    mode = _text(data, "mode").upper()
    if mode not in {"V4_ROUTINE", "EXCEPTION_ONLY"}:
        raise Step2QueueError("mode must be V4_ROUTINE or EXCEPTION_ONLY")

    board = _list(data, "board")
    exceptions = _list(data, "user_exceptions")
    activated = _list(data, "activated_reserves")
    authority = None

    if mode == "V4_ROUTINE":
        if not board:
            raise Step2QueueError("V4 routine board is empty")
        authority = _sealed_rank_chain(data, board)
    else:
        if board or activated:
            raise Step2QueueError(
                "EXCEPTION_ONLY cannot import board or reserve authority"
            )
        if not exceptions:
            raise Step2QueueError("EXCEPTION_ONLY requires explicit user exception")

    board_by_id: dict[str, dict[str, Any]] = {}
    for row in board:
        if not isinstance(row, dict):
            raise Step2QueueError("board entries must be objects")
        mid = _text(row, "match_id")
        if mid in board_by_id:
            raise Step2QueueError(f"DUPLICATE BOARD FIXTURE: {mid}")
        kickoff = _text(row, "kickoff_ict")
        if not ISO_ICT.fullmatch(kickoff):
            raise Step2QueueError(f"KICKOFF NOT FROZEN: {mid}")
        lane = _text(row, "official_follow_lane").upper()
        if lane not in LANES:
            raise Step2QueueError(f"INVALID OFFICIAL LANE: {mid}")
        if row.get("xi_window_open") not in (True, False):
            raise Step2QueueError(f"XI WINDOW NOT DOCUMENTED: {mid}")
        if lane in {"FOLLOW", "RESERVE"}:
            _quarter(row.get("c_supported_line"), "c_supported_line")
            _quarter(row.get("c2_supported_line"), "c2_supported_line")
        board_by_id[mid] = row

    activated_by_id: dict[str, str] = {}
    for row in activated:
        if not isinstance(row, dict):
            raise Step2QueueError("activated reserve entries must be objects")
        mid = _text(row, "match_id")
        if (
            mid not in board_by_id
            or board_by_id[mid]["official_follow_lane"] != "RESERVE"
        ):
            raise Step2QueueError(f"UNAUTHORIZED RESERVE ACTIVATION: {mid}")
        activated_by_id[mid] = _text(row, "activation_reference")

    exception_by_id: dict[str, str] = {}
    for row in exceptions:
        if not isinstance(row, dict):
            raise Step2QueueError("user exception entries must be objects")
        mid = _text(row, "match_id")
        if mid in exception_by_id:
            raise Step2QueueError(f"DUPLICATE USER EXCEPTION: {mid}")
        exception_by_id[mid] = _text(row, "user_authorization_reference")

    due: list[dict[str, Any]] = []
    not_due: list[dict[str, Any]] = []
    for mid, row in board_by_id.items():
        lane = row["official_follow_lane"]
        if mid in exception_by_id:
            auth = "USER_EXCEPTION"
            reference = exception_by_id[mid]
        elif lane == "FOLLOW" and row["xi_window_open"]:
            auth = "ROUTINE_FOLLOW"
            reference = "VERIFIED_V4_FOLLOW"
        elif lane == "RESERVE" and mid in activated_by_id:
            auth = "RESERVE_ACTIVATED"
            reference = activated_by_id[mid]
        else:
            not_due.append({
                "match_id": mid,
                "reason": (
                    "XI_WINDOW_CLOSED"
                    if lane in {"FOLLOW", "RESERVE"} and not row["xi_window_open"]
                    else "RESERVE_NOT_ACTIVATED"
                    if lane == "RESERVE"
                    else "STOP_NOT_AUTHORIZED"
                    if lane == "STOP"
                    else "NOT_DUE"
                ),
            })
            continue
        due.append({
            "match_id": mid,
            "official_follow_lane": lane,
            "step2_authorization": auth,
            "authorization_reference": reference,
        })

    for mid, reference in exception_by_id.items():
        if mid not in board_by_id:
            due.append({
                "match_id": mid,
                "official_follow_lane": "STOP",
                "step2_authorization": "USER_EXCEPTION",
                "authorization_reference": reference,
            })

    due.sort(key=lambda row: row["match_id"])
    not_due.sort(key=lambda row: row["match_id"])
    return {
        "schema_version": VERSION,
        "session_id": session_id,
        "mode": mode,
        "source_run_id": authority["source_run_id"] if authority else None,
        "board_snapshot_id": authority["board_snapshot_id"] if authority else None,
        "model_evidence_sha256": (
            authority["model_evidence_sha256"] if authority else None
        ),
        "due": due,
        "not_due": not_due,
        "due_count": len(due),
        "board_fixture_count": len(board),
        "user_exception_count": len(exception_by_id),
        "activated_reserve_count": len(activated_by_id),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Freeze active V4 Step-2 due queue")
    parser.add_argument("--input", required=True)
    args = parser.parse_args()
    try:
        receipt = freeze_queue(json.loads(Path(args.input).read_text(encoding="utf-8")))
        print(json.dumps({"ok": True, **receipt}, indent=2, sort_keys=True))
        return 0
    except (OSError, ValueError) as exc:
        print(json.dumps({
            "ok": False,
            "status": "STEP2 QUEUE BLOCKED",
            "reason": str(exc),
        }, indent=2, sort_keys=True), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
