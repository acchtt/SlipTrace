#!/usr/bin/env python3
"""Recover an authentic V4 stage receipt from saved, exact source evidence.

Crucially: a self-hashed, derived V4_SWEEP_DERIVED_UNATTESTED JSON is NOT a
V4_SWEEP_READY receipt. The only legal promotion path is to rerun the
production stage.sweep() on the *original unchanged source snapshot*
at the original observed assessment time, compare EVERY deterministic
business field, and emit the genuine production result.

Historical replay does not verify today's current kickoff or odds and
NEVER authorizes retroactive prematch assessment or an Airtable write.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import timedelta
from pathlib import Path
from typing import Any

from stage import SCHEMA, StageError, _hash, _time, sweep

STATUS = "V4_SWEEP_DERIVED_UNATTESTED"
# Research-order manifest is non-authoritative scheduling metadata. Historical
# attestation must still match the source ledger, intake lanes, eligible queue,
# counts and every other business field exactly, but a V2 refactor may replace
# the old manifest implementation without changing historical eligibility.
IGNORABLE = {
    "status",
    "integrity_sha256",
    "implementation_note",
    "goal_screen_manifest",
    # Added prospectively in the 2026-10-24 window-completeness repair.
    # Historical derived receipts predate these deterministic summary fields;
    # the underlying source ledger/intake lanes still have to match exactly.
    "window_status",
    "whole_requested_surface_complete",
    "upstream_remaining_fixture_count",
    "upstream_resume_fixtures",
}


def replay(source: dict[str, Any], derived: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(source, dict) or source.get("schema_version") != SCHEMA:
        raise StageError("original V4 source.json required; cannot reconstruct from Airtable rows")
    if not isinstance(derived, dict) or derived.get("status") != STATUS or derived.get("schema_version") != SCHEMA:
        raise StageError("explicitly un-attested original V4 intake JSON required")
    if source.get("run_id") != derived.get("run_id"):
        raise StageError("original source and derived intake run IDs disagree")
    digest = derived.get("integrity_sha256")
    if digest != _hash({k: v for k, v in derived.items() if k != "integrity_sha256"}):
        raise StageError("derived intake integrity digest does not match original bytes")
    created = _time(derived.get("created_at_utc"), "created_at_utc")
    observed = _time(source.get("source_observed_at_utc"), "source_observed_at_utc")
    if not observed <= created <= observed + timedelta(minutes=60):
        raise StageError("derived stage creation time cannot attest original source observation")
    # This is a replay of the frozen source at the original instant. NOT a
    # current-time/fixture status attestation. Rank must check kickoff now.
    # This exact run was sealed against the old registry-only intake
    # policy. Replay must attest its ORIGINAL meaning, not retroactively
    # reclassify Brazil/unknown leagues under a new admission policy.
    legacy_policy = (
        source.get("run_id") == "V4-20261012-003037-0600"
        and derived.get("source_ledger_hash")
        == "6fdbb087773f9eb1fdfea01c1a59de7974c06a47e8eaa9c9d15de02a9cc52863"
    )
    real = sweep(
        source, now=created.isoformat(),
        _historical_registry_only=legacy_policy,
        _historical_replay=True,
    )
    claimed = {k: v for k, v in derived.items() if k not in IGNORABLE}
    recomputed = {k: v for k, v in real.items() if k not in IGNORABLE}
    if claimed != recomputed:
        changed = sorted(set(claimed) ^ set(recomputed) |
                         {k for k in set(claimed) & set(recomputed)
                          if claimed[k] != recomputed[k]})
        raise StageError("derived candidate ledger does not match actual V4 engine recomputation: "
                         + ", ".join(changed[:12]))
    if real["status"] != "V4_SWEEP_READY":
        raise StageError("production stage did not produce V4_SWEEP_READY")
    return real


def main() -> int:
    p = argparse.ArgumentParser(description="Rerun actual V4 stage over archived source and compare derived intake")
    p.add_argument("--source", required=True)
    p.add_argument("--derived", required=True)
    p.add_argument("--output", required=True)
    p.add_argument("--report", required=True)
    args = p.parse_args()
    try:
        source_bytes = Path(args.source).read_bytes()
        derived_bytes = Path(args.derived).read_bytes()
        real = replay(json.loads(source_bytes), json.loads(derived_bytes))
        digest = real["integrity_sha256"]
        Path(args.output).write_text(json.dumps(real, indent=2, ensure_ascii=False,
                             sort_keys=True)+"\n", encoding="utf-8")
        report = {
            "status": "V4_ORIGINAL_SNAPSHOT_REEXECUTED_AND_RECONCILED",
            "run_id": real["run_id"],
            "original_source_file_sha256": hashlib.sha256(source_bytes).hexdigest(),
            "unattested_intake_file_sha256": hashlib.sha256(derived_bytes).hexdigest(),
            "attested_V4_SWEEP_READY_integrity_sha256": digest,
            "fixture_count": real["fixture_count"],
            "eligible_count_as_of_original_snapshot": real["eligible_count"],
            "replay_as_of_utc": real["created_at_utc"],
            "fresh_live_fixture_status_attested": False,
            "C_C2_ranked": False,
            "Airtable_persisted": False,
            "bet_recorded": False,
        }
        Path(args.report).write_text(json.dumps(report, indent=2, sort_keys=True)+"\n",
                                      encoding="utf-8")
        print(json.dumps(report, indent=2, sort_keys=True))
        return 0
    except (OSError, KeyError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "V4_ATTESTATION_BLOCKED", "error": str(exc)}),file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
