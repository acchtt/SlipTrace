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


# Football C/C2 research can run without a bookmaker quote. Price-dependent
# decisions still require the strict fixture-market validation path.
FOOTBALL_ONLY_MODE = "FOOTBALL_ONLY"
PRICED_OBSERVED_MODE = "PRICED_OBSERVED"


def validate_step1_fixture_evidence(data: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(data, dict) or data.get("source_intake_policy") != LEAGUE_CHANNEL_POLICY:
        raise Step1FixtureIntakeError("STEP1 EVIDENCE BLOCKED — league-first source policy required")
    mode = data.get("evidence_mode", PRICED_OBSERVED_MODE)
    if mode not in {FOOTBALL_ONLY_MODE, PRICED_OBSERVED_MODE}:
        raise Step1FixtureIntakeError("STEP1 EVIDENCE BLOCKED — unknown evidence_mode")
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
    if frozen_kickoff is None or researched_kickoff is None:
        raise Step1FixtureIntakeError("STEP1 EVIDENCE BLOCKED — valid zoned kickoff evidence required")
    # The frozen Step0 source clock is immutable historical provenance.
    # A same-ID/same-competition provider KO revision is NOT evidence that
    # the scoring fixture should be dropped from Step1 research. Keep both
    # clocks and require fresh status/KO reconciliation at /xi, rather than
    # pretending a 10-minute drift is a different football match.
    kickoff_recheck = researched_kickoff != frozen_kickoff
    kickoff_drift_minutes = round(
        (researched_kickoff - frozen_kickoff).total_seconds() / 60, 3
    )
    if researched.get("operational_viability_grade") != frozen.get("operational_viability_grade"):
        raise Step1FixtureIntakeError("STEP1 EVIDENCE BLOCKED — Step0 operational grade rewritten")
    for key in ("user_scope_excluded", "hard_scope_excluded", "is_friendly", "friendly_scope_excluded"):
        if frozen.get(key) is True and researched.get(key) is not True:
            raise Step1FixtureIntakeError("STEP1 EVIDENCE BLOCKED — Step0 scope exclusion cleared")
    if mode == FOOTBALL_ONLY_MODE and any(key.startswith("asian_total_") for key in researched):
        raise Step1FixtureIntakeError(
            "STEP1 EVIDENCE BLOCKED — supplied Asian-total fields require PRICED_OBSERVED validation"
        )
    defects = validate_work_candidate(researched, intake_policy="XI_MARKET_FIRST_V1")
    if mode == FOOTBALL_ONLY_MODE:
        defects = [d for d in defects if not d.startswith("CURRENT_ASIAN_TOTAL_")]
    if defects:
        raise Step1FixtureIntakeError(
            "STEP1 RESEARCH BLOCKED — ACTUAL MATCH EVIDENCE MISSING: "
            + ", ".join(defects)
        )
    return {
        "status": (
            "STEP1 MATCH EVIDENCE VERIFIED — KICKOFF RECHECK REQUIRED"
            if kickoff_recheck else "STEP1 MATCH EVIDENCE VERIFIED"
        ),
        "match_id": frozen["match_id"],
        # Never overwrite the frozen Step0 time or source payload hash.
        "fixture_kickoff_utc": frozen_kickoff.astimezone(timezone.utc).isoformat(),
        "researched_fixture_kickoff_utc": researched_kickoff.astimezone(timezone.utc).isoformat(),
        "kickoff_drift_minutes": kickoff_drift_minutes,
        "kickoff_reconciliation_status": (
            "KICKOFF_RECHECK_REQUIRED" if kickoff_recheck else "MATCHED"
        ),
        "kickoff_recheck_required_at_xi": kickoff_recheck,
        "prematch_executable_status": (
            "NOT_VERIFIED_RECHECK_KO_AND_MATCH_STATUS" if kickoff_recheck
            else "NOT_VERIFIED_CURRENT_PRICE_AND_XI" if mode == FOOTBALL_ONLY_MODE
            else "NOT_VERIFIED_XI_AND_CURRENT_ODDS_PENDING"
        ),
        "source_intake_policy": LEAGUE_CHANNEL_POLICY,
        "verified_match_specific_market": mode == PRICED_OBSERVED_MODE,
        "price_evidence_mode": mode,
        "pricing_status": (
            "PRICED_FIXTURE_MARKET_OBSERVED_NOT_EXECUTABLE_AT_XI"
            if mode == PRICED_OBSERVED_MODE else "UNOBSERVED_NOT_REQUIRED_FOR_FOOTBALL"
        ),
        "quote_required_for_football_research": False,
        "verified_team_xi_publication_channels": True,
        "confirmed_starting_xi": False,
        # This allows C and C2 board research only, never executable bets.
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
