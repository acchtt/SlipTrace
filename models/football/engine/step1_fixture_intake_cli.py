#!/usr/bin/env python3
"""Step 01 match-specific evidence gate for a league-first Step-0 handoff.

This runs locally on source records provided by Work. It cannot fetch prices
or confirm whether a URL is live: Work must capture authentic, contemporaneous
match-specific evidence before invoking this validator.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import timezone
from pathlib import Path
from typing import Any

from sweep_intake_evidence import (
    _utc_timestamp,
    validate_work_candidate,
    LEAGUE_CHANNEL_POLICY,
)


class Step1FixtureIntakeError(ValueError):
    pass


def validate_step1_fixture_evidence(data: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(data, dict) or data.get("source_intake_policy") != LEAGUE_CHANNEL_POLICY:
        raise Step1FixtureIntakeError("STEP1 EVIDENCE BLOCKED — league-first source policy required")
    frozen = data.get("frozen_step0_candidate")
    researched = data.get("researched_fixture")
    if not isinstance(frozen, dict) or not isinstance(researched, dict):
        raise Step1FixtureIntakeError("STEP1 EVIDENCE BLOCKED — frozen and researched fixture rows required")
    if frozen.get("intake_evidence_scope") != "LEAGUE_CHANNEL_ONLY":
        raise Step1FixtureIntakeError("STEP1 EVIDENCE BLOCKED — frozen league-channel provenance missing")
    for key in ("match_id", "competition_name"):
        if not isinstance(frozen.get(key), str) or not frozen[key].strip():
            raise Step1FixtureIntakeError(f"STEP1 EVIDENCE BLOCKED — frozen {key} missing")
        if researched.get(key) != frozen[key]:
            raise Step1FixtureIntakeError(f"STEP1 EVIDENCE BLOCKED — {key} differs from frozen Step0")
    frozen_kickoff = _utc_timestamp(frozen.get("fixture_kickoff_utc"))
    researched_kickoff = _utc_timestamp(researched.get("fixture_kickoff_utc"))
    if frozen_kickoff is None or researched_kickoff != frozen_kickoff:
        raise Step1FixtureIntakeError("STEP1 EVIDENCE BLOCKED — fixture kickoff differs from frozen Step0")
    if researched.get("operational_viability_grade") != frozen.get("operational_viability_grade"):
        raise Step1FixtureIntakeError("STEP1 EVIDENCE BLOCKED — Step0 operational grade rewritten")
    for key in ("user_scope_excluded", "hard_scope_excluded", "is_friendly", "friendly_scope_excluded"):
        if frozen.get(key) is True and researched.get(key) is not True:
            raise Step1FixtureIntakeError("STEP1 EVIDENCE BLOCKED — Step0 scope exclusion cleared")
    defects = validate_work_candidate(researched, intake_policy="XI_MARKET_FIRST_V1")
    if defects:
        raise Step1FixtureIntakeError(
            "STEP1 RESEARCH BLOCKED — ACTUAL MATCH EVIDENCE MISSING: "
            + ", ".join(defects)
        )
    return {
        "status": "STEP1 MATCH EVIDENCE VERIFIED",
        "match_id": frozen["match_id"],
        "fixture_kickoff_utc": frozen_kickoff.astimezone(timezone.utc).isoformat(),
        "source_intake_policy": LEAGUE_CHANNEL_POLICY,
        "verified_match_specific_market": True,
        "verified_team_xi_publication_channels": True,
        "confirmed_starting_xi": False,
        "model_execution_authorized": True,
        "actual_odds_must_be_rechecked_at_xi": True,
    }


def main() -> int:
    p = argparse.ArgumentParser(description="Validate /rank fixture-specific research after league-first Step0")
    p.add_argument("--input", required=True, help="Frozen Step0 + real Step01 match research JSON")
    args = p.parse_args()
    try:
        value = json.loads(Path(args.input).read_text(encoding="utf-8"))
        print(json.dumps(validate_step1_fixture_evidence(value), sort_keys=True, indent=2))
        return 0
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "STEP1 RESEARCH BLOCKED", "error": str(exc)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
