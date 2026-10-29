"""No-FT prospective smoke/regression tests for 29 Oct Football C repairs."""
from __future__ import annotations

import unittest

from models.football.stages_v4.tools import normal_source  # noqa: F401
from models.football.stages_v4.g3_bridge_shadow import (
    portfolio_challengers, review_g3_bridge,
)

# Stage modules use their historically existing top-level import paths.
import pathlib
import sys
STAGE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(STAGE))
from league_registry import classify
from cheap_sweep_filters import classify_research_priority


def fixture(country, competition, kind="DOMESTIC_CUP"):
    return {
        "country": country, "competition": competition,
        "competition_kind": kind, "home": "Club A", "away": "Club B",
    }


class ProspectiveSelectionRepairTests(unittest.TestCase):
    def test_oct28_frozen_aliases_preserved(self):
        at = "2026-10-28T09:43:08Z"
        for competition in ("DFB Cup: Round 2", "KNVB Beker: Round 1",
                            "EFL Cup: Round 4", "NM Cup: Round 3"):
            country = {"DFB": "Germany", "KNVB": "Netherlands",
                       "EFL": "England", "NM": "Norway"}[competition.split()[0]]
            row = fixture(country, competition)
            self.assertEqual(classify(row, at_utc=at)["lane"], "DISCOVERY")
            self.assertEqual(classify_research_priority(row, at_utc=at)["priority"],
                             "NEUTRAL_RESEARCH")

    def test_new_aliases_research_but_never_goal_certify(self):
        at = "2026-10-29T02:05:00Z"
        for country, competition in [
            ("Germany", "DFB Cup: Round 2"),
            ("Netherlands", "KNVB Beker: Round 1"),
            ("England", "EFL Cup: Round 4"),
            ("Spain", "Copa del Rey: Round 1"),
            ("Norway", "NM Cup: Round 3"),
        ]:
            with self.subTest(competition=competition):
                row = fixture(country, competition)
                self.assertEqual(classify(row, at_utc=at)["lane"], "CONDITIONAL")
                mark = classify_research_priority(row, at_utc=at)
                self.assertEqual(mark["priority"], "SPECIAL_RESEARCH")
                self.assertNotIn("goal3_funded", mark)
                self.assertTrue(mark["requires_competition_format_proof"])

    def test_exclusions_are_not_rescued(self):
        at = "2026-10-29T02:05:00Z"
        for row in [
            fixture("Israel", "EFL Cup: Round 4"),
            fixture("Kenya", "Kenyan Cup"),
            fixture("Germany", "DFB Cup U19: Round 2"),
            fixture("Germany", "DFB Cup: Round 2", "YOUTH_CONTINENTAL"),
        ]:
            self.assertNotEqual(classify(row, at_utc=at)["lane"], "CONDITIONAL")
            self.assertEqual(classify_research_priority(row, at_utc=at)["priority"],
                             "NEUTRAL_RESEARCH")

    def test_future_cup_requires_fixture_bound_format_and_incentive_evidence(self):
        from unittest.mock import patch
        from stage import sweep
        src = {
            "schema_version": "football-stages-v4",
            "run_id": "V4-20261029-0910-1100-CUP-PROOF",
            "source_family": "Frozen Provider Test",
            "source_url": "https://example.org/fixtures",
            "window_start_utc": "2026-10-29T02:10:00Z",
            "window_end_utc": "2026-10-29T04:00:00Z",
            "source_observed_at_utc": "2026-10-29T01:59:00Z",
            "fixtures": [{
                "match_id": "CUP-1",
                **fixture("Netherlands", "KNVB Beker: Round 1"),
                "home": "MVV", "away": "Excelsior",
                "fixture_status": "PREMATCH_CONFIRMED",
                "kickoff_utc": "2026-10-29T03:00:00Z",
                "source_url": "https://example.org/fixtures/CUP-1",
                "observed_at_utc": "2026-10-29T01:59:00Z",
                "researchability_status": "VERIFIED",
                "researchability_proof": {
                    "match_id": "CUP-1",
                    "checked_at_utc": "2026-10-29T01:59:00Z",
                    "source_url": "https://example.org/fixtures/CUP-1",
                    "current_channels_checked": True,
                },
            }],
        }
        evidence = {
            "source_completeness_contract": "V2_TEST",
            "source_completeness_sha256": "test",
        }
        with patch("stage.validate_source_completeness", return_value=evidence):
            unverified = sweep(src, now="2026-10-29T02:00:00Z")
            lane = unverified["source_ledger"][0]["intake_lane"]
            self.assertEqual(lane, "CUP_PROOF_LIMITED")
            self.assertEqual(unverified["eligible_count"], 0)
            self.assertEqual(unverified["window_status"], "COMPLETE")
            self.assertTrue(unverified["whole_requested_surface_complete"])
            self.assertEqual(unverified["upstream_remaining_fixture_count"], 0)
            self.assertEqual(unverified["cup_proof_limited_count"], 1)
            self.assertIn("CUP_FORMAT_AND_INCENTIVES", unverified["source_ledger"][0]["reason"])

            src["fixtures"][0]["tournament_format_proof"] = {
                "match_id": "CUP-1",
                "source_url": "https://example.org/rules",
                "checked_at_utc": "2026-10-29T01:59:00Z",
                "competition_format_verified": True,
                "incentive_review_verified": True,
            }
            proven = sweep(src, now="2026-10-29T02:00:00Z")
            self.assertNotEqual(proven["source_ledger"][0]["intake_lane"], "CUP_PROOF_LIMITED")
            # Format proof is necessary, never sufficient for G3 admission.
            self.assertEqual(proven["eligible_count"], 0)

    def test_cup_proof_limited_is_terminal_without_blocking_ready_rows(self):
        from stage import _unresolved_sweep_intake_rows
        receipt = {
            "source_ledger": [
                {
                    "match_id": "CUP-1",
                    "intake_lane": "CUP_PROOF_LIMITED",
                    "reason": "APPROVED_CUP_FORMAT_AND_INCENTIVES_PROOF_REQUIRED",
                },
                {
                    "match_id": "LEAGUE-1",
                    "intake_lane": "GOAL_PRIORITY",
                    "reason": "DISCOVERY_GOAL_QUALIFIED",
                },
            ]
        }
        self.assertEqual(_unresolved_sweep_intake_rows(receipt), [])

    def test_unverified_g3_proof_requires_recheck_but_never_vetoes(self):
        row = {"match_id": "M1", "goal3_funded": True,
               "goal3_mechanism_class": "DISTRIBUTED"}
        frozen = {k: "MEDIUM" for k in (
            "route_reliability", "failure_resistance", "burden_protection",
            "burden_stall_risk", "opponent_leakage",
        )}
        result = review_g3_bridge(row, frozen)
        self.assertTrue(result["source_recheck_required"])
        self.assertIn("goal3_comparable_context.independent_proof_missing",
                      result["missing_independent_g3_proofs"])
        self.assertIn("goal3_stall_endpoints.source_proof_missing",
                      result["missing_independent_g3_proofs"])
        self.assertTrue(result["goal3_funded_frozen"])
        self.assertFalse(result["production_authority"])

    def test_malformed_proof_does_not_crash_or_authorize(self):
        row = {"match_id": "M2", "goal3_funded": True}
        found = review_g3_bridge(row, {"goal_route_proof": {"goal3_reply": "bad"}})
        self.assertTrue(found["source_recheck_required"])
        self.assertFalse(found["production_authority"])

    def test_follow_shadows_are_outcome_blind_and_leave_lanes_intact(self):
        rows = [
            {"match_id": str(n), "rank": n, "board_state": "FOCUS",
             "operational_viability_grade": "A",
             "kickoff_ict": "2026-10-29T02:00:00+07:00" if n >= 6
                              else "2026-10-28T20:00:00+07:00",
             "follow_lane": "FOLLOW" if n in {1, 2, 3, 4, 5, 6, 7}
                             else "FOCUS_UNFOLLOWED",
             "supported_line": 2.5} for n in range(1, 10)
        ]
        initial = [dict(r) for r in rows]
        result = portfolio_challengers(rows)
        self.assertEqual(result["global_rank_shadow_ids"], list(map(str, range(1, 8))))
        self.assertEqual(len(result["late_block_protected_shadow_ids"]), 7)
        self.assertIn("6", result["late_block_protected_shadow_ids"])
        self.assertIn("7", result["late_block_protected_shadow_ids"])
        self.assertEqual(rows, initial)
        self.assertFalse(result["changed_official_lanes"])


if __name__ == "__main__":
    unittest.main()
