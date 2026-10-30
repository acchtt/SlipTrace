#!/usr/bin/env python3
"""Create a transport-safe Football C rank authority package.

The verified rank artifact persisted to Library can be tens of megabytes and may
be serialized as a single JSON line. Text-oriented chat/file transports can
therefore fail before /xi reaches the deterministic runtime. This utility reads
the exact raw artifact bytes, verifies the persisted rank certificate, and emits
only the ranked board rows plus their matching frozen model-input rows.

It never reconstructs Football C from the ledger and never changes rank state,
certified burden, evidence, or policy metadata.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

VERIFIED_RANK_STATUSES = {
    "V4_RANK_PERSISTENCE_VERIFIED",
    "V4_RANK_PARTIAL_PERSISTENCE_VERIFIED",
}
CAPSULE_SCHEMA = "football-c-rank-authority-capsule-v1"
VERIFIED_ARTIFACT_SCHEMA = "football-c-verified-rank-artifact-v1"


class RankTransportError(ValueError):
    pass


def _require_dict(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise RankTransportError(f"{label} must be an object")
    return value


def _require_rows(value: Any, label: str) -> list[dict[str, Any]]:
    if not isinstance(value, list) or any(not isinstance(x, dict) for x in value):
        raise RankTransportError(f"{label} must be an object array")
    return value


def _sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def build_capsule(raw: bytes, *, match_id: str | None = None) -> dict[str, Any]:
    try:
        artifact = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise RankTransportError("verified rank artifact is not valid JSON") from exc
    artifact = _require_dict(artifact, "artifact")
    if artifact.get("schema_version") != VERIFIED_ARTIFACT_SCHEMA:
        raise RankTransportError(
            f"artifact schema must be {VERIFIED_ARTIFACT_SCHEMA}"
        )

    artifacts = _require_dict(artifact.get("artifacts"), "artifact.artifacts")
    verified = _require_dict(artifacts.get("verified.json"), "verified.json")
    rank = _require_dict(artifacts.get("rank.json"), "rank.json")

    status = verified.get("status")
    if status not in VERIFIED_RANK_STATUSES:
        raise RankTransportError(f"rank persistence status is not verified: {status}")
    if verified.get("persistence_verified") is not True:
        raise RankTransportError(
            "verified.json does not assert persistence_verified=true"
        )

    run_id = str(rank.get("run_id") or "")
    if not run_id or run_id != str(artifact.get("run_id") or ""):
        raise RankTransportError("artifact/rank run_id mismatch")
    if str(verified.get("run_id") or "") != run_id:
        raise RankTransportError("verified/rank run_id mismatch")

    rank_sha = str(rank.get("integrity_sha256") or "")
    if not rank_sha or str(verified.get("rank_sha256") or "") != rank_sha:
        raise RankTransportError("verified rank hash does not match rank receipt")

    policy_lock = rank.get("engine_policy_lock")
    policy_fingerprint = rank.get("engine_policy_fingerprint")
    if verified.get("engine_policy_lock") != policy_lock:
        raise RankTransportError("verified/rank engine policy lock mismatch")
    if verified.get("engine_policy_fingerprint") != policy_fingerprint:
        raise RankTransportError(
            "verified/rank engine policy fingerprint mismatch"
        )

    board = _require_dict(rank.get("board"), "rank.board")
    board_rows = _require_rows(board.get("matches"), "rank.board.matches")
    frozen = _require_dict(rank.get("frozen_model_input"), "rank.frozen_model_input")
    frozen_rows = _require_rows(
        frozen.get("matches"), "rank.frozen_model_input.matches"
    )
    frozen_by_id = {str(row.get("match_id")): row for row in frozen_rows}

    selected_board: list[dict[str, Any]] = []
    selected_frozen: list[dict[str, Any]] = []
    wanted = str(match_id) if match_id is not None else None
    for row in board_rows:
        mid = str(row.get("match_id") or "")
        if wanted is not None and mid != wanted:
            continue
        frozen_row = frozen_by_id.get(mid)
        if not isinstance(frozen_row, dict):
            raise RankTransportError(
                f"ranked match {mid} lacks frozen model input"
            )
        selected_board.append(row)
        selected_frozen.append(frozen_row)

    if wanted is not None and not selected_board:
        raise RankTransportError(
            f"match_id {wanted} is not on the sealed rank board"
        )
    if not selected_board:
        raise RankTransportError("sealed rank board is empty")

    return {
        "schema_version": CAPSULE_SCHEMA,
        "status": status,
        "source_artifact_schema": artifact.get("schema_version"),
        "source_artifact_run_id": artifact.get("run_id"),
        "source_artifact_sha256": _sha256(raw),
        "rank_sha256": rank_sha,
        "engine_policy_lock": policy_lock,
        "engine_policy_fingerprint": policy_fingerprint,
        "rank_receipt": {
            "schema_version": rank.get("schema_version"),
            "run_id": run_id,
            "integrity_sha256": rank_sha,
            "engine_source_revision": rank.get("engine_source_revision"),
            "engine_policy_lock": policy_lock,
            "engine_policy_fingerprint": policy_fingerprint,
            "context_contract_version": rank.get("context_contract_version"),
            "rank_at_utc": rank.get("rank_at_utc"),
            "slate_window_class": rank.get("slate_window_class"),
            "slate_window_start_ict": rank.get("slate_window_start_ict"),
            "slate_window_end_ict": rank.get("slate_window_end_ict"),
            "active_model": rank.get("active_model"),
            "retired_models": rank.get("retired_models"),
            "board": {"matches": selected_board},
            "frozen_model_input": {"matches": selected_frozen},
        },
    }


def run(
    input_path: Path,
    output_path: Path,
    *,
    match_id: str | None = None,
) -> int:
    raw = input_path.read_bytes()
    capsule = build_capsule(raw, match_id=match_id)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(capsule, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--match-id")
    args = parser.parse_args()
    return run(args.input, args.output, match_id=args.match_id)


if __name__ == "__main__":
    raise SystemExit(main())
