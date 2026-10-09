#!/usr/bin/env python3
"""Create a STEP0 Work ZIP *only* after final source-ledger read-back and validation.

A provisional artifact is NOT a rankable handoff, even if it has 8 fixtures.
The run-proof JSON is supplied by independent Airtable read-back; this local
command cannot itself confirm remote source freshness.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import tempfile
import zipfile
from pathlib import Path

from step0_handoff_cli import Step0HandoffError, validate_step0_handoff


def validate_run_proof(handoff: dict, run: dict) -> None:
    if not isinstance(run, dict):
        raise Step0HandoffError("PACKAGE BLOCKED — missing independent Sweep Runs read-back")
    run_id = handoff.get("run_id")
    if not isinstance(run_id, str) or not run_id.startswith("SWEEP-"):
        raise Step0HandoffError("PACKAGE BLOCKED — handoff run_id missing")
    if run.get("run_id") != run_id:
        raise Step0HandoffError("PACKAGE BLOCKED — Sweep Runs identity mismatch")
    if run.get("run_status") != "RUNNING" or run.get("phase") != "PACKAGING":
        raise Step0HandoffError("PACKAGE BLOCKED — source run must be RUNNING/PACKAGING")
    if run.get("reconciliation_complete") is not True:
        raise Step0HandoffError("PACKAGE BLOCKED — Step 0 reconciliation not complete")
    if run.get("capacity_queue_frozen") is not True:
        raise Step0HandoffError("PACKAGE BLOCKED — capacity queue not frozen")
    if run.get("required_competition_blocks_complete") is not True:
        raise Step0HandoffError("PACKAGE BLOCKED — required-competition coverage not complete")
    if run.get("pending_verification_blocks") != 0 or run.get("unresolved_count") != 0:
        raise Step0HandoffError("PACKAGE BLOCKED — unresolved/pending source evidence")
    if run.get("source_payload_hash") != handoff.get("source_payload_hash"):
        raise Step0HandoffError("PACKAGE BLOCKED — source epoch hash mismatch")
    if run.get("admitted_count") != len(handoff.get("admitted_fixtures", [])):
        raise Step0HandoffError("PACKAGE BLOCKED — Airtable admitted count mismatch")
    if run.get("production_universe_count") != handoff.get("production_universe_count"):
        raise Step0HandoffError("PACKAGE BLOCKED — source coverage count mismatch")
    if handoff.get("verification_policy") == "FAST_FINISH_V1":
        from coverage_manifest import REQUIRED_BLOCKS
        ledger = run.get("required_competition_source_fixture_ids")
        if not isinstance(ledger, dict):
            raise Step0HandoffError("PACKAGE BLOCKED — required fixture source ledger missing")
        for block in REQUIRED_BLOCKS:
            if ledger.get(block) != handoff.get("required_competition_source_fixture_ids", {}).get(block):
                raise Step0HandoffError("PACKAGE BLOCKED — source ledger / handoff identity disagreement")
        # A proposed Work queue is not frozen merely because eight B grades
        # exist. Every admitted row needs a matching finalized Airtable state.
        persisted = run.get("admitted_dispositions")
        if not isinstance(persisted, dict):
            raise Step0HandoffError("PACKAGE BLOCKED — persisted Work admissions missing")
        admitted_ids = {x.get("match_id") for x in handoff["admitted_fixtures"]}
        if admitted_ids != set(persisted) or any(
            persisted[mid] != "ADMITTED_TO_C" for mid in admitted_ids
        ):
            raise Step0HandoffError("PACKAGE BLOCKED — admitted fixture rows still provisional")


def package(handoff_path: Path, note_path: Path, proof_path: Path, output: Path) -> dict:
    handoff = json.loads(handoff_path.read_text(encoding="utf-8"))
    proof = json.loads(proof_path.read_text(encoding="utf-8"))
    result = validate_step0_handoff(handoff, consumer="export")
    validate_run_proof(handoff, proof)
    if result["step0_handoff_validation_status"] != "PASS":
        raise Step0HandoffError("PACKAGE BLOCKED — handoff validator did not pass")
    # Do not hide model/scoring work inside a provisional text file.
    text = note_path.read_text(encoding="utf-8")
    if not text.strip():
        raise Step0HandoffError("PACKAGE BLOCKED — human-readable handoff empty")
    if "PROVISIONAL" in text.upper() or "WORK_READY=FALSE" in text.upper():
        raise Step0HandoffError("PACKAGE BLOCKED — provisional handoff text")
    if not output.name.startswith("AISCORE_FIXTURES_") or output.suffix.lower() != ".zip":
        raise Step0HandoffError("PACKAGE BLOCKED — invalid canonical ZIP filename")
    if not note_path.name.startswith("AISCORE_FIXTURES_") or note_path.suffix.lower() != ".txt":
        raise Step0HandoffError("PACKAGE BLOCKED — invalid canonical text filename")
    if output.exists():
        raise Step0HandoffError("PACKAGE BLOCKED — output exists; no silent overwrite")
    output.parent.mkdir(parents=True, exist_ok=True)
    fd, tmpname = tempfile.mkstemp(prefix=".step0-validating-", suffix=".zip", dir=output.parent)
    os.close(fd)
    try:
        with zipfile.ZipFile(tmpname, "w", compression=zipfile.ZIP_DEFLATED) as z:
            z.write(handoff_path, arcname="STEP0_HANDOFF.json")
            z.write(note_path, arcname=note_path.name)
        with zipfile.ZipFile(tmpname) as z:
            if z.testzip() is not None:
                raise Step0HandoffError("PACKAGE BLOCKED — zip integrity error")
        os.replace(tmpname, output)
    finally:
        if os.path.exists(tmpname):
            os.unlink(tmpname)
    return {
        "status": "STEP0 WORK ZIP VALIDATED",
        "output": str(output),
        "run_id": handoff["run_id"],
        "sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
        "admitted": len(handoff["admitted_fixtures"]),
        "required_competition_blocks_complete": True,
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True, help="STEP0_HANDOFF.json")
    p.add_argument("--text", required=True, help="AISCORE_FIXTURES_*.txt")
    p.add_argument("--run-proof", required=True, help="independent current Airtable Sweep Runs read-back")
    p.add_argument("--output", required=True, help="AISCORE_FIXTURES_*.zip")
    args = p.parse_args()
    try:
        print(json.dumps(package(Path(args.input), Path(args.text), Path(args.run_proof), Path(args.output)), indent=2))
        return 0
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(f"STEP0 WORK ZIP BLOCKED — {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
