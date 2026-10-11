import pathlib
import sys
import unittest

ENGINE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE))

from step1_fixture_intake_cli import (  # noqa: E402
    Step1FixtureIntakeError,
    validate_step1_fixture_evidence,
)
from test_sweep_intake_evidence import valid_fixture, league_candidate  # noqa: E402


def sample():
    frozen = league_candidate()
    match = valid_fixture()
    match["competition_name"] = frozen["competition_name"]
    return {
        "source_intake_policy": "LEAGUE_CHANNEL_FIRST_V1",
        "frozen_step0_candidate": frozen,
        "researched_fixture": match,
    }


class Step1FixtureEvidenceTests(unittest.TestCase):
    def test_real_match_specific_evidence_allows_c_c2_research(self):
        result = validate_step1_fixture_evidence(sample())
        self.assertTrue(result["model_execution_authorized"])
        self.assertTrue(result["verified_match_specific_market"])
        self.assertFalse(result["confirmed_starting_xi"])

    def test_league_coverage_does_not_replace_current_match_quote(self):
        payload = sample()
        for k in ("asian_total_fixture_source_url", "asian_total_market_line"):
            payload["researched_fixture"].pop(k)
        with self.assertRaisesRegex(Step1FixtureIntakeError, "CURRENT_ASIAN_TOTAL_SOURCE_MISSING"):
            validate_step1_fixture_evidence(payload)

    def test_missing_actual_two_team_lineup_sources_block(self):
        payload = sample()
        payload["researched_fixture"].pop("xi_away_channel_source_url")
        with self.assertRaisesRegex(Step1FixtureIntakeError, "XI_AWAY_PUBLISHING_CHANNEL_UNVERIFIED"):
            validate_step1_fixture_evidence(payload)

    def test_different_fixture_identity_or_competition_still_blocks(self):
        for key, newvalue in (
            ("match_id", "other-fixture"),
            ("competition_name", "Bundesliga"),
        ):
            with self.subTest(key=key):
                payload = sample()
                payload["researched_fixture"][key] = newvalue
                with self.assertRaisesRegex(Step1FixtureIntakeError, "differs from frozen Step0"):
                    validate_step1_fixture_evidence(payload)

    def test_same_match_provider_kickoff_ten_minutes_later_does_not_block_rank(self):
        payload = sample()
        payload["researched_fixture"]["fixture_kickoff_utc"] = "2026-10-10T00:10:00Z"
        out = validate_step1_fixture_evidence(payload)
        self.assertTrue(out["model_execution_authorized"])
        self.assertEqual(out["kickoff_reconciliation_status"], "KICKOFF_RECHECK_REQUIRED")
        self.assertTrue(out["kickoff_recheck_required_at_xi"])
        self.assertEqual(out["fixture_kickoff_utc"], "2026-10-10T00:00:00+00:00")
        self.assertEqual(out["researched_fixture_kickoff_utc"], "2026-10-10T00:10:00+00:00")
        self.assertEqual(out["kickoff_drift_minutes"], 10)
        self.assertEqual(
            out["prematch_executable_status"], "NOT_VERIFIED_RECHECK_KO_AND_MATCH_STATUS"
        )

    def test_providers_can_disagree_earlier_or_later_without_mutating_step0(self):
        for provider_ko, drift in (
            ("2026-10-09T23:50:00Z", -10),
            ("2026-10-10T00:10:00Z", 10),
            ("2026-10-10T01:00:00Z", 60),
        ):
            with self.subTest(provider_ko=provider_ko):
                payload = sample()
                payload["researched_fixture"]["fixture_kickoff_utc"] = provider_ko
                out = validate_step1_fixture_evidence(payload)
                self.assertEqual(out["kickoff_drift_minutes"], drift)
                self.assertTrue(out["model_execution_authorized"])
                self.assertEqual(out["fixture_kickoff_utc"], "2026-10-10T00:00:00+00:00")

    def test_matching_kickoff_is_verified_without_reconciliation_flag(self):
        out = validate_step1_fixture_evidence(sample())
        self.assertEqual(out["kickoff_reconciliation_status"], "MATCHED")
        self.assertFalse(out["kickoff_recheck_required_at_xi"])
        self.assertEqual(out["kickoff_drift_minutes"], 0)

    def test_unparseable_or_missing_provider_clock_still_blocks(self):
        for provider_ko in (None, "invalid-clock", "2026-10-10T00:00:00"):
            with self.subTest(provider_ko=provider_ko):
                payload = sample()
                payload["researched_fixture"]["fixture_kickoff_utc"] = provider_ko
                with self.assertRaisesRegex(Step1FixtureIntakeError, "valid zoned kickoff"):
                    validate_step1_fixture_evidence(payload)

    def test_old_odds_and_a_future_market_timestamp_are_blocked(self):
        for timestamp in ("2026-09-01T00:00:00Z", "2026-10-10T01:00:00Z"):
            with self.subTest(timestamp=timestamp):
                payload = sample()
                payload["researched_fixture"]["asian_total_market_observed_at_utc"] = timestamp
                with self.assertRaisesRegex(Step1FixtureIntakeError, "CURRENT_ASIAN_TOTAL_STALE_OR_POST_KO"):
                    validate_step1_fixture_evidence(payload)

    def test_no_grade_rewrite_or_user_exclusion_bypass(self):
        payload = sample()
        payload["researched_fixture"]["operational_viability_grade"] = "A"
        with self.assertRaisesRegex(Step1FixtureIntakeError, "operational grade rewritten"):
            validate_step1_fixture_evidence(payload)
        payload = sample()
        payload["frozen_step0_candidate"]["user_scope_excluded"] = True
        payload["researched_fixture"]["user_scope_excluded"] = False
        with self.assertRaisesRegex(Step1FixtureIntakeError, "scope exclusion cleared"):
            validate_step1_fixture_evidence(payload)


if __name__ == "__main__":
    unittest.main()
