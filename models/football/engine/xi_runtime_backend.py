#!/usr/bin/env python3
"""On-demand deterministic Football C /xi backend for normal chat.

The normal-chat interface submits the already-researched Football C payload and
the exact user screenshot quote. This module executes the same xi_portable
runtime used locally and emits one durable result envelope. It does not fetch
odds or perform free-form football research.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
from typing import Any

ENGINE = Path(__file__).resolve().parent
sys.path.insert(0, str(ENGINE))

import xi_portable


REQUEST_SCHEMA = "football-c-xi-runtime-request-v2"
RESULT_SCHEMA = "football-c-xi-runtime-result-v1"


class RankAuthorityError(ValueError):
    pass


def _canonical(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, ensure_ascii=True, separators=(",", ":")
    ).encode("utf-8")


def _load_request(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("request must be a JSON object")
    if value.get("schema_version") != REQUEST_SCHEMA:
        raise ValueError(f"schema_version must be {REQUEST_SCHEMA}")
    request_id = value.get("request_id")
    if not isinstance(request_id, str) or not request_id.strip():
        raise ValueError("request_id required")
    if path.stem != request_id:
        raise ValueError("request_id must equal request filename stem")
    c_football = value.get("c_football")
    if not isinstance(c_football, dict):
        raise ValueError("c_football object required")
    screenshot = value.get("screenshot_quote")
    strict = value.get("strict_price_c")
    if screenshot is not None and not isinstance(screenshot, dict):
        raise ValueError("screenshot_quote must be an object")
    if strict is not None and not isinstance(strict, dict):
        raise ValueError("strict_price_c must be an object")
    if screenshot is not None and strict is not None:
        raise ValueError("choose screenshot_quote or strict_price_c, not both")
    authority = value.get("authority")
    if not isinstance(authority, dict) or authority.get("mode") not in {
        "RANKED", "EXCEPTION"
    }:
        raise RankAuthorityError(
            "RANK_RECEIPT_REQUIRED: authority.mode must be RANKED or EXCEPTION"
        )
    return value


def _rank_payload(package: dict[str, Any]) -> dict[str, Any]:
    for key in ("native_rank", "rank_receipt"):
        candidate = package.get(key)
        if isinstance(candidate, dict) and isinstance(candidate.get("board"), dict):
            return candidate
    if isinstance(package.get("board"), dict):
        return package
    raise RankAuthorityError("RANK_RECEIPT_REQUIRED: sealed rank board missing")


def _authorized_c_football(request: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    authority = request.get("authority")
    if not isinstance(authority, dict):
        raise RankAuthorityError("RANK_RECEIPT_REQUIRED: explicit authority missing")
    mode = authority.get("mode")
    supplied = request.get("c_football")
    if not isinstance(supplied, dict):
        raise ValueError("c_football object required")
    if mode == "EXCEPTION":
        reference = authority.get("exception_reference")
        if not isinstance(reference, str) or not reference.strip():
            raise RankAuthorityError(
                "RANK_RECEIPT_REQUIRED: exception authority must be explicitly tagged"
            )
        return supplied, {"mode": "EXCEPTION", "reference": reference}
    if mode != "RANKED":
        raise RankAuthorityError("RANK_RECEIPT_REQUIRED: ranked or exception authority required")

    package = authority.get("verified_rank_package")
    if not isinstance(package, dict) or package.get("status") not in {
        "V4_RANK_PERSISTENCE_VERIFIED", "V4_RANK_PARTIAL_PERSISTENCE_VERIFIED"
    }:
        raise RankAuthorityError("RANK_RECEIPT_REQUIRED: verified rank package missing")
    rank = _rank_payload(package)
    board = rank.get("board") or {}
    rows = board.get("matches")
    frozen = rank.get("frozen_model_input") or {}
    frozen_rows = frozen.get("matches") if isinstance(frozen, dict) else None
    if not isinstance(rows, list) or not isinstance(frozen_rows, list):
        raise RankAuthorityError("RANK_RECEIPT_REQUIRED: frozen rank evidence missing")
    match = supplied.get("match") or {}
    mid = str(authority.get("match_id") or match.get("match_id") or "")
    board_row = next((row for row in rows if str(row.get("match_id")) == mid), None)
    frozen_row = next((row for row in frozen_rows if str(row.get("match_id")) == mid), None)
    if not isinstance(board_row, dict) or not isinstance(frozen_row, dict):
        raise RankAuthorityError("RANK_RECEIPT_REQUIRED: exact ranked match row missing")

    declared = authority.get("material_evidence_updates") or []
    if not isinstance(declared, list) or any(not isinstance(x, str) for x in declared):
        raise RankAuthorityError("material_evidence_updates must be a field-name array")
    declared_set = set(declared)
    for key, frozen_value in frozen_row.items():
        if key in match and match[key] != frozen_value and key not in declared_set:
            raise RankAuthorityError(
                f"RANK_RECEIPT_REQUIRED: undeclared override of frozen field {key}"
            )
    inherited = dict(frozen_row)
    for key in declared_set:
        if key not in match:
            raise RankAuthorityError(f"declared material update absent from match: {key}")
        inherited[key] = match[key]
    inherited["match_id"] = mid
    c_football = dict(supplied)
    c_football["match"] = inherited
    return c_football, {
        "mode": "RANKED", "match_id": mid, "rank_run_id": rank.get("run_id"),
        "rank_integrity_sha256": rank.get("integrity_sha256"),
        "frozen_board_state": board_row.get("board_state"),
        "frozen_supported_line": board_row.get("supported_line"),
        "material_evidence_updates": sorted(declared_set),
    }


def execute(request: dict[str, Any]) -> dict[str, Any]:
    try:
        c_football, authority_trace = _authorized_c_football(request)
        if c_football.get("stage") == "decision":
            if request.get("screenshot_quote") is not None or request.get("strict_price_c") is not None:
                raise ValueError("decision-stage request cannot include a second price source")
            runtime = xi_portable._decision_receipt(c_football)
            runtime = {**runtime, "xi_mode": "STRICT_EXECUTABLE_PRICE_C"}
        else:
            if c_football.get("stage") != "football_assessment":
                raise ValueError("c_football.stage must be football_assessment or decision")
            runtime = xi_portable._football_and_optional_price(
                c_football,
                price_c=request.get("strict_price_c"),
                screenshot=request.get("screenshot_quote"),
            )
        return {
            "schema_version": RESULT_SCHEMA,
            "request_id": request["request_id"],
            "ok": True,
            "runtime_commit": os.environ.get("GITHUB_SHA"),
            "input_sha256": hashlib.sha256(_canonical(request)).hexdigest(),
            "authority": authority_trace,
            "runtime": runtime,
        }
    except Exception as exc:
        return {
            "schema_version": RESULT_SCHEMA,
            "request_id": request.get("request_id"),
            "ok": False,
            "runtime_commit": os.environ.get("GITHUB_SHA"),
            "input_sha256": hashlib.sha256(_canonical(request)).hexdigest(),
            "status": (
                "RANK_RECEIPT_REQUIRED"
                if isinstance(exc, RankAuthorityError)
                else "XI ENGINE CONTRACT REJECTED"
                if isinstance(exc, (xi_portable.ContractError, ValueError, KeyError))
                else "XI RUNTIME: EXECUTION FAILED"
            ),
            "failure_class": (
                "PAYLOAD_OR_MODEL_CONTRACT"
                if isinstance(exc, (xi_portable.ContractError, ValueError, KeyError))
                else "PYTHON_OR_RUNTIME"
            ),
            "error_type": type(exc).__name__,
            "error": str(exc),
        }


def run(request_path: Path, output_path: Path) -> int:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        request = _load_request(request_path)
        result = execute(request)
    except Exception as exc:
        # A malformed outer request is still persisted as a concrete backend
        # error instead of becoming an ambiguous ANALYSIS_ONLY fallback.
        result = {
            "schema_version": RESULT_SCHEMA,
            "request_id": request_path.stem,
            "ok": False,
            "runtime_commit": os.environ.get("GITHUB_SHA"),
            "status": "XI BACKEND REQUEST REJECTED",
            "failure_class": "REQUEST_ENVELOPE",
            "error_type": type(exc).__name__,
            "error": str(exc),
        }
    output_path.write_text(
        json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return 0


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--request", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    return run(args.request, args.output)


if __name__ == "__main__":
    raise SystemExit(main())
