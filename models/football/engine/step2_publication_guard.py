#!/usr/bin/env python3
"""Fail-closed PRE-PUBLICATION gate for Football C official / C2 shadow Step-2.

Run after independent Decision State read-back and immediately before exposing
an action to the user / Website Picks. Does not publish or contact Airtable.
The caller must supply live truth for the current evidence/quote epoch.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from decision_pair_cli import run_pair
from step2_reconcile import _check_persisted_decision, Step2ReconciliationError

_SHA = re.compile(r"^[a-f0-9]{40}$")


class PublicationBlocked(ValueError):
    pass


def _text(row: dict, key: str) -> str:
    value = row.get(key)
    if not isinstance(value, str) or not value.strip():
        raise PublicationBlocked(f"{key} must be a nonempty string")
    return value.strip()


def check_publication(data: dict) -> dict:
    if not isinstance(data, dict) or data.get("schema_version") != "football-step2-publication-v1":
        raise PublicationBlocked("schema_version must be football-step2-publication-v1")
    c = data.get("c_input")
    c2 = data.get("c2_input")
    receipt = data.get("pair_receipt")
    stored = data.get("decision_state_snapshot")
    if not all(isinstance(x, dict) for x in (c, c2, receipt, stored)):
        raise PublicationBlocked("C/C2 inputs, pair receipt and independent read-back required")
    active_epoch = _text(data, "active_evidence_epoch_id")
    for label, payload in (("C", c), ("C2", c2)):
        match = payload.get("match")
        context = payload.get("context")
        if not isinstance(match, dict) or not isinstance(context, dict):
            raise PublicationBlocked(f"{label} match/context missing")
        if _text(context, "evidence_epoch_id") != active_epoch:
            raise PublicationBlocked(f"{label} STALE EVIDENCE EPOCH")
        if _text(match, "match_id") != _text(stored, "match_id"):
            raise PublicationBlocked(f"{label} FIXTURE IDENTITY MISMATCH")
        if context.get("quote_revalidated") is not True:
            raise PublicationBlocked(f"{label} QUOTE NOT REVALIDATED")

    if _text(stored, "evidence_epoch_id") != active_epoch:
        raise PublicationBlocked("STORED EVIDENCE EPOCH STALE")
    if _text(data, "latest_evidence_epoch_id") != active_epoch:
        raise PublicationBlocked("NEWER EVIDENCE EPOCH EXISTS — REASSESS")
    if data.get("quote_still_executable") is not True:
        raise PublicationBlocked("EXECUTABLE QUOTE NOT CONFIRMED AT PUBLICATION")
    if data.get("fixture_status_still_valid") is not True:
        raise PublicationBlocked("FIXTURE STATUS INVALIDATED — REROUTE")
    source = _text(data, "active_engine_source_revision")
    if not _SHA.fullmatch(source):
        raise PublicationBlocked("active_engine_source_revision invalid")
    if _text(stored, "engine_source_revision") != source:
        raise PublicationBlocked("STALE ENGINE SOURCE REVISION")

    # Execute from frozen inputs again; a copied/ad-hoc pair receipt cannot
    # authorize publication. Engines must agree on the common evidence epoch.
    computed = run_pair(c, c2)
    if receipt != computed:
        raise PublicationBlocked("PAIR RECEIPT DOES NOT MATCH DETERMINISTIC EXECUTION")

    try:
        _check_persisted_decision(_text(stored, "match_id"), {
            "decision_state_snapshot": stored,
        })
    except Step2ReconciliationError as exc:
        raise PublicationBlocked(f"READ-BACK INVALID: {exc}") from exc

    for model, key in (("c", "engine_c_result"), ("c2", "engine_c2_result")):
        actual = stored.get(key)
        if isinstance(actual, str):
            try:
                actual = json.loads(actual)
            except json.JSONDecodeError as exc:
                raise PublicationBlocked(f"{key} invalid JSON") from exc
        # The engine returns its action but keeps the supported burden in
        # the input assessment. The persisted Step-2 contract requires
        # a normalized result containing that exact frozen supported_line.
        model_payload = c if model == "c" else c2
        expected = {**computed["results"][model],
                    "supported_line": model_payload["match"]["supported_line"]}
        if actual != expected:
            raise PublicationBlocked(f"{key} NOT THE CURRENT PAIR RESULT")

    key = _text(stored, "match_id") + ":" + active_epoch
    published = data.get("previously_published_keys")
    if not isinstance(published, list) or any(not isinstance(x, str) for x in published):
        raise PublicationBlocked("previously_published_keys must be an explicit array")
    if key in published:
        raise PublicationBlocked("DUPLICATE ASSESSMENT EPOCH — DO NOT REPUBLISH")

    # This certifies only internal consistency of supplied inputs and
    # attestations. External quote freshness/read-back still requires a
    # real connector fetch by the caller; this tool cannot attest its own source.
    return {
        "status": "STEP2 PUBLICATION ELIGIBLE",
        "publication_key": key,
        "match_id": _text(stored, "match_id"),
        "record_id": _text(stored, "record_id"),
        "engine_source_revision": source,
        "evidence_epoch_id": active_epoch,
        "c_action": _text(stored, "c_action"),
        "c2_shadow_action": _text(stored, "c2_shadow_action"),
        "external_freshness_attested_by_caller": True,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Check C+C2 Step-2 prepublication integrity")
    parser.add_argument("--input", required=True)
    args = parser.parse_args()
    try:
        data = json.loads(Path(args.input).read_text(encoding="utf-8"))
        print(json.dumps({"ok": True, **check_publication(data)}, indent=2, sort_keys=True))
        return 0
    except (OSError, ValueError, KeyError) as exc:
        print(json.dumps({"ok": False, "status": "STEP2 PUBLICATION BLOCKED", "reason": str(exc)}, indent=2), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
