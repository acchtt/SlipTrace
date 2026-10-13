#!/usr/bin/env python3
"""Final publication/readback gate for a strict C+C2 priced decision.

The deterministic pair has already executed before this gate. This verifier
therefore does not execute the models again and does not run a second session
reconciliation layer. It checks only what can change after execution:
- exact Decision State readback,
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
_RECORD = re.compile(r"^rec[A-Za-z0-9]{14}$")


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


def _expected_action(model: str, engine_action: str) -> str:
    if engine_action not in {"BET", "WAIT", "PASS"}:
        raise PublicationBlocked(f"{model}: invalid engine action")
    return (
        f"C-{engine_action}"
        if model == "c"
        else f"C2-{engine_action}"
    )


def check_publication(data: dict[str, Any]) -> dict[str, Any]:
    if (
        not isinstance(data, dict)
        or data.get("schema_version") != "football-step2-publication-v2"
    ):
        raise PublicationBlocked(
            "schema_version must be football-step2-publication-v2"
        )

    receipt = data.get("pair_receipt")
    stored = data.get("decision_state_snapshot")
    if not isinstance(receipt, dict) or not isinstance(stored, dict):
        raise PublicationBlocked(
            "strict pair receipt and independent Decision State readback required"
        )
    if (
        receipt.get("engine_execution_status") != "EXECUTED_C_C2_PAIR"
        or receipt.get("models_executed") != ["c", "c2"]
        or not isinstance(receipt.get("results"), dict)
        or set(receipt["results"]) != {"c", "c2"}
    ):
        raise PublicationBlocked("strict C+C2 pair receipt invalid")

    match_id = _text(stored, "match_id")
    record_id = _text(stored, "record_id")
    if not _RECORD.fullmatch(record_id):
        raise PublicationBlocked("Decision State record ID invalid")

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

    for model, stored_key, action_key in (
        ("c", "engine_c_result", "c_action"),
        ("c2", "engine_c2_result", "c2_shadow_action"),
    ):
        result = receipt["results"][model]
        if result.get("match_id") != match_id:
            raise PublicationBlocked(f"{model}: pair fixture differs from readback")
        if _json(stored.get(stored_key), stored_key) != result:
            raise PublicationBlocked(f"{stored_key} differs from strict pair result")
        expected = _expected_action(model, result.get("action"))
        observed_action = _text(stored, action_key).upper()
        if model == "c2":
            observed_action = observed_action.split(" —", 1)[0]
        if observed_action != expected:
            raise PublicationBlocked(f"{action_key} differs from strict pair result")

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
        "record_id": record_id,
        "engine_source_revision": source,
        "evidence_epoch_id": active_epoch,
        "c_action": _text(stored, "c_action"),
        "c2_shadow_action": _text(stored, "c2_shadow_action"),
        "readback_verified": True,
        "quote_still_executable": True,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify strict priced C+C2 publication readback"
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
