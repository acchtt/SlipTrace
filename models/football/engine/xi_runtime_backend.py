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
from xi_authority import RankAuthorityError, authorize_c_football


REQUEST_SCHEMA = "football-c-xi-runtime-request-v2"
RESULT_SCHEMA = "football-c-xi-runtime-result-v1"


def _authorized_c_football(request: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    return authorize_c_football(
        request.get("c_football"),
        request.get("authority"),
    )


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
