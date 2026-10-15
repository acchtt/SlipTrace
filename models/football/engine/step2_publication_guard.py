#!/usr/bin/env python3
"""Final publication/readback gate for one strict Football C priced decision.

The deterministic C decision has already executed before this gate. This verifier
therefore does not execute the model again and does not run a second session
reconciliation layer. It checks only what can change after execution:
- exact Google Sheets Decision State readback,
- evidence/source revision continuity,
- quote and fixture still executable,
- duplicate publication prevention.

Observed/screenshot quote comparisons never enter this gate.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


_SHA = re.compile(r"^[a-f0-9]{40}$")


class PublicationBlocked(ValueError):
    pass


def _text(row: dict[str, Any], key: str) -> str:
    value = row.get(key)
    if not isinstance(value, str) or not value.strip():
        raise PublicationBlocked(f"{key} must be a nonempty string")
    return value.strip()


def _json(value: Any, key: str) -> dict[str, Any]:
    if isinstance(value, str):
        try:
            value = json.loads(value)
        except json.JSONDecodeError as exc:
            raise PublicationBlocked(f"{key} invalid JSON") from exc
    if not isinstance(value, dict):
        raise PublicationBlocked(f"{key} must be an object")
    return value


def _expected_action(engine_action: str) -> str:
    if engine_action not in {"BET", "WAIT", "PASS"}:
        raise PublicationBlocked("C: invalid engine action")
    return f"C-{engine_action}"


def check_publication(data: dict[str, Any]) -> dict[str, Any]:
    if (
        not isinstance(data, dict)
        or data.get("schema_version") != "football-step2-publication-v3"
    ):
        raise PublicationBlocked(
            "schema_version must be football-step2-publication-v3"
        )

    receipt = data.get("decision_receipt")
    stored = data.get("decision_state_snapshot")
    if not isinstance(receipt, dict) or not isinstance(stored, dict):
        raise PublicationBlocked(
            "strict C decision receipt and independent Decision State readback required"
        )
    if (
        receipt.get("engine_execution_status") != "EXECUTED_C_DECISION"
        or receipt.get("model") != "c"
        or not isinstance(receipt.get("result"), dict)
    ):
        raise PublicationBlocked("strict Football C decision receipt invalid")

    match_id = _text(stored, "match_id")
    row_key = _text(stored, "row_key")
    assessment_id = _text(stored, "assessment_id")
    if row_key != assessment_id:
        raise PublicationBlocked("Decision State row key must equal Assessment ID")

    active_epoch = _text(data, "active_evidence_epoch_id")
    if _text(stored, "evidence_epoch_id") != active_epoch:
        raise PublicationBlocked("stored evidence epoch stale")
    if _text(data, "latest_evidence_epoch_id") != active_epoch:
        raise PublicationBlocked("newer evidence epoch exists — reassess")

    source = _text(data, "active_engine_source_revision")
    if not _SHA.fullmatch(source):
        raise PublicationBlocked("active_engine_source_revision invalid")
    if _text(stored, "engine_source_revision") != source:
        raise PublicationBlocked("stored engine source revision stale")

    if data.get("quote_still_executable") is not True:
        raise PublicationBlocked("executable quote not confirmed at publication")
    if data.get("fixture_status_still_valid") is not True:
        raise PublicationBlocked("fixture status invalidated — reassess")

    result = receipt["result"]
    if result.get("match_id") != match_id:
        raise PublicationBlocked("C decision fixture differs from readback")
    if _json(stored.get("engine_c_result"), "engine_c_result") != result:
        raise PublicationBlocked("engine_c_result differs from strict C result")
    expected = _expected_action(result.get("action"))
    observed_action = _text(stored, "c_action").upper()
    if observed_action != expected:
        raise PublicationBlocked("c_action differs from strict C result")

    key = match_id + ":" + active_epoch
    published = data.get("previously_published_keys")
    if not isinstance(published, list) or any(
        not isinstance(item, str) for item in published
    ):
        raise PublicationBlocked(
            "previously_published_keys must be an explicit array"
        )
    if key in published:
        raise PublicationBlocked("duplicate assessment epoch — do not republish")

    return {
        "status": "STEP2_PUBLICATION_ELIGIBLE",
        "publication_key": key,
        "match_id": match_id,
        "row_key": row_key,
        "assessment_id": assessment_id,
        "engine_source_revision": source,
        "evidence_epoch_id": active_epoch,
        "c_action": _text(stored, "c_action"),
        "readback_verified": True,
        "quote_still_executable": True,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify strict priced Football C publication readback"
    )
    parser.add_argument("--input", required=True)
    args = parser.parse_args()
    try:
        result = check_publication(
            json.loads(Path(args.input).read_text(encoding="utf-8"))
        )
        print(json.dumps({"ok": True, **result}, indent=2, sort_keys=True))
        return 0
    except (OSError, ValueError) as exc:
        print(json.dumps({
            "ok": False,
            "status": "STEP2 PUBLICATION BLOCKED",
            "reason": str(exc),
        }, indent=2, sort_keys=True), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
