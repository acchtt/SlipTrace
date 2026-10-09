#!/usr/bin/env python3
"""Freeze the authorized Football C Step-2 due universe before any XI execution.

Pure pre-execution audit: no network, predictions, odds changes or Airtable writes.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import re
import sys

VERSION = "football-step2-queue-v1"
LANES = {"FOLLOW", "RESERVE", "STOP"}
ISO_ICT = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+07:00$")


class Step2QueueError(ValueError):
    pass


def _text(row: dict, key: str) -> str:
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


def _list(row: dict, key: str) -> list:
    value = row.get(key)
    if not isinstance(value, list):
        raise Step2QueueError(f"{key} must be an array")
    return value


def freeze_queue(data: dict) -> dict:
    if not isinstance(data, dict) or data.get("schema_version") != VERSION:
        raise Step2QueueError(f"schema_version must be {VERSION}")
    session_id = _text(data, "session_id")
    mode = _text(data, "mode").upper()
    if mode not in {"ROUTINE", "EXCEPTION_ONLY"}:
        raise Step2QueueError("mode must be ROUTINE or EXCEPTION_ONLY")
    board = _list(data, "board")
    exceptions = _list(data, "user_exceptions")
    activated = _list(data, "activated_reserves")

    if mode == "ROUTINE":
        source = data.get("source_run")
        rank = data.get("rank")
        if not isinstance(source, dict) or not isinstance(rank, dict):
            raise Step2QueueError("QUEUE NOT FROZEN — source_run and rank attestations required")
        _text(source, "run_id")
        _text(source, "source_snapshot_id")
        if source.get("status") != "COMPLETE" or source.get("packaging_complete") is not True:
            raise Step2QueueError("QUEUE NOT FROZEN — SWEEP INCOMPLETE")
        if source.get("work_ready") is not True:
            raise Step2QueueError("QUEUE NOT FROZEN — STEP0 NOT WORK-READY")
        if rank.get("status") != "TERMINAL_COMPLETE":
            raise Step2QueueError("QUEUE NOT FROZEN — RANK NOT TERMINAL")
        if rank.get("board_pair_execution_status") != "EXECUTED_C_C2_BOARDS" or rank.get("common_evidence_reconciled") is not True:
            raise Step2QueueError("QUEUE NOT FROZEN — C/C2 BOARD PAIR MISSING")
        _text(rank, "board_snapshot_id")
        if not board:
            raise Step2QueueError("QUEUE NOT FROZEN — board is empty")
    else:
        if board or activated:
            raise Step2QueueError("EXCEPTION_ONLY cannot import unverified board or reserves")
        if not exceptions:
            raise Step2QueueError("EXCEPTION_ONLY requires explicit user exceptions")

    board_by_id: dict[str, dict] = {}
    for row in board:
        if not isinstance(row, dict):
            raise Step2QueueError("board entries must be objects")
        identity = _text(row, "match_id")
        if identity in board_by_id:
            raise Step2QueueError(f"DUPLICATE BOARD FIXTURE: {identity}")
        kickoff = _text(row, "kickoff_ict")
        if not ISO_ICT.fullmatch(kickoff):
            raise Step2QueueError(f"KICKOFF NOT FROZEN: {identity}")
        lane = _text(row, "official_follow_lane").upper()
        if str(row.get("eligibility", "ELIGIBLE")).upper() == "EXCLUDED":
            raise Step2QueueError(f"EXCLUDED FIXTURE IN RANKED BOARD: {identity}")
        if lane not in LANES:
            raise Step2QueueError(f"INVALID OFFICIAL LANE: {identity}")
        if row.get("xi_window_open") not in (True, False):
            raise Step2QueueError(f"XI WINDOW NOT DOCUMENTED: {identity}")
        _text(row, "xi_window_basis")
        _text(row, "c_board_state")
        _text(row, "c2_shadow_state")
        if lane == "FOLLOW" and row["c_board_state"] != "C-FOCUS":
            raise Step2QueueError(f"FOLLOW REQUIRES C-FOCUS: {identity}")
        if lane in {"FOLLOW", "RESERVE"}:
            _quarter(row.get("c_supported_line"), "c_supported_line")
            _quarter(row.get("c2_supported_line"), "c2_supported_line")
            _text(row, "c2_supported_line_basis")
        board_by_id[identity] = row

    activated_by_id: dict[str, str] = {}
    for row in activated:
        if not isinstance(row, dict):
            raise Step2QueueError("activated reserve entries must be objects")
        identity = _text(row, "match_id")
        if identity in activated_by_id:
            raise Step2QueueError(f"DUPLICATE RESERVE ACTIVATION: {identity}")
        if identity not in board_by_id or board_by_id[identity]["official_follow_lane"] != "RESERVE":
            raise Step2QueueError(f"UNAUTHORIZED RESERVE ACTIVATION: {identity}")
        activated_by_id[identity] = _text(row, "activation_reference")

    exception_by_id: dict[str, str] = {}
    for row in exceptions:
        if not isinstance(row, dict):
            raise Step2QueueError("user exception entries must be objects")
        identity = _text(row, "match_id")
        if identity in exception_by_id:
            raise Step2QueueError(f"DUPLICATE USER EXCEPTION: {identity}")
        exception_by_id[identity] = _text(row, "user_authorization_reference")

    due: list[dict] = []
    not_due: list[dict] = []
    for identity, row in board_by_id.items():
        lane = row["official_follow_lane"]
        if identity in exception_by_id:
            auth = "USER_EXCEPTION"
        elif lane == "FOLLOW" and row["xi_window_open"]:
            auth = "ROUTINE_FOLLOW"
        elif lane == "RESERVE" and identity in activated_by_id:
            auth = "RESERVE_ACTIVATED"
        else:
            not_due.append({
                "match_id": identity,
                "reason": "XI_WINDOW_CLOSED" if lane in {"FOLLOW", "RESERVE"} and not row["xi_window_open"] else (
                    "RESERVE_NOT_ACTIVATED" if lane == "RESERVE" else "STOP_NOT_AUTHORIZED" if lane == "STOP" else "NOT_YET_DUE"
                ),
            })
            continue
        due.append({
            "match_id": identity,
            "official_follow_lane": lane,
            "step2_authorization": auth,
            "authorization_reference": exception_by_id.get(identity) if auth == "USER_EXCEPTION" else activated_by_id.get(identity) if auth == "RESERVE_ACTIVATED" else "FROZEN_C_FOLLOW",
        })

    for identity, reference in exception_by_id.items():
        if identity not in board_by_id:
            due.append({
                "match_id": identity,
                "official_follow_lane": "STOP",
                "step2_authorization": "USER_EXCEPTION",
                "authorization_reference": reference,
            })
    due.sort(key=lambda x: x["match_id"])
    not_due.sort(key=lambda x: x["match_id"])
    return {
        "schema_version": VERSION,
        "session_id": session_id,
        "mode": mode,
        "source_run_id": data.get("source_run", {}).get("run_id") if mode == "ROUTINE" else None,
        "board_snapshot_id": data.get("rank", {}).get("board_snapshot_id") if mode == "ROUTINE" else None,
        "due": due,
        "not_due": not_due,
        "due_count": len(due),
        "board_fixture_count": len(board),
        "user_exception_count": len(exception_by_id),
        "activated_reserve_count": len(activated_by_id),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Freeze official C Step-2 due queue")
    parser.add_argument("--input", required=True)
    args = parser.parse_args()
    try:
        receipt = freeze_queue(json.loads(Path(args.input).read_text(encoding="utf-8")))
        print(json.dumps({"ok": True, **receipt}, indent=2, sort_keys=True))
        return 0
    except (OSError, ValueError) as exc:
        print(json.dumps({"ok": False, "status": "STEP2 QUEUE BLOCKED", "reason": str(exc)}, indent=2, sort_keys=True), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
