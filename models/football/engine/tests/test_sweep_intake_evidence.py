import pathlib
import sys
import unittest

ENGINE_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE_DIR))

from sweep_intake_evidence import classify_preflight, validate_work_candidate  # noqa: E402


def valid_fixture():
    return {
        "match_id": "upcoming-fixture",
        "operational_viability_grade": "B",
        "competition_support_tier": "VERIFIED_PROFESSIONAL",
        "competition_official_url": "https://league.example.org/fixtures",
        "competition_support_reason": "Professional first-team competition, official league schedule",
        "preflight_complete": True,
        "user_scope_excluded": False,
        "hard_scope_excluded": False,
        "fixture_identity_verified": True,
        "fixture_kickoff_utc": "2026-10-10T00:00:00Z",
        "xi_expected": "YES",
        "xi_home_channel_type": "RECENT_CONFIRMED_XI",
        "xi_away_channel_type": "PROVIDER_MATCHDAY_COVERAGE",
        "xi_home_channel_source_url": "https://match.example.org/home-last",
        "xi_away_channel_source_url": "https://match.example.org/away-provider",
        "xi_channel_basis": "Both teams' preceding XI/channel published through AiScore",
        "xi_recheck_due_utc": "2026-10-09T22:45:00Z",
        "xi_home_recent_match_id": "historic-home-1",
        "xi_away_recent_match_id": "historic-away-1",
        "xi_home_recent_match_kickoff_utc": "2026-10-02T17:00:00Z",
        "xi_away_recent_match_kickoff_utc": "2026-10-04T17:00:00Z",
        "xi_home_lineup_source_url": "https://match.example.org/home-last",
        "xi_away_lineup_source_url": "https://match.example.org/away-last",
        "market_observability": "MEDIUM",
        "asian_total_fixture_source_url": "https://book.example.org/upcoming-fixture/totals",
        "asian_total_market_match_id": "upcoming-fixture",
        "asian_total_market_observed_at_utc": "2026-10-09T15:00:00Z",
        "asian_total_market_line": 2.75,
        "asian_total_market_bookmaker": "Example bookmaker",
        "team_news_observability": "MEDIUM",
        "team_news_source_url": "https://club.example.org/match-preview",
    }


class StrictIntakeEvidenceTests(unittest.TestCase):
    def test_verified_fixture_can_enter_work(self):
        row = valid_fixture()
        self.assertEqual(validate_work_candidate(row), [])
        self.assertTrue(classify_preflight(row)["work_queue_eligible"])

    def test_full_day_b_conditional_can_have_unconfirmed_upcoming_xi(self):
        row = valid_fixture()
        row["xi_expected"] = "UNCERTAIN"
        # Matchday XI is not due yet, but both publication channels exist.
        self.assertEqual(validate_work_candidate(row), [])
        self.assertTrue(classify_preflight(row)["work_queue_eligible"])

    def test_no_upcoming_xi_confirmation_field_needed(self):
        row = valid_fixture()
        self.assertNotIn("confirmed_upcoming_xi", row)
        self.assertEqual(validate_work_candidate(row), [])

    def test_missing_lineup_channel_still_fails(self):
        row = valid_fixture()
        del row["xi_away_channel_source_url"]
        self.assertIn("XI_AWAY_PUBLISHING_CHANNEL_UNVERIFIED", validate_work_candidate(row))

    def test_recent_xi_ids_are_helpful_but_not_mandatory(self):
        row = valid_fixture()
        for side in ("home", "away"):
            row.pop(f"xi_{side}_recent_match_id")
            row.pop(f"xi_{side}_recent_match_kickoff_utc")
            row.pop(f"xi_{side}_lineup_source_url")
        self.assertEqual(validate_work_candidate(row), [])

    def test_invalid_historical_xi_must_not_pass_when_provided(self):
        row = valid_fixture()
        row["xi_home_recent_match_kickoff_utc"] = "2026-10-11T00:00:00Z"
        self.assertIn("XI_HOME_HISTORICAL_FIXTURE_TIME_INVALID",
                      validate_work_candidate(row))

    def test_conditional_b_may_use_official_squad_for_one_side(self):
        row = valid_fixture()
        row["xi_expected"] = "UNCERTAIN"
        row["xi_away_channel_type"] = "OFFICIAL_SQUAD_NEWS"
        self.assertEqual(validate_work_candidate(row), [])

    def test_two_squad_lists_alone_are_not_lineup_coverage(self):
        row = valid_fixture()
        row["xi_expected"] = "UNCERTAIN"
        row["xi_home_channel_type"] = "OFFICIAL_SQUAD_NEWS"
        row["xi_away_channel_type"] = "OFFICIAL_SQUAD_NEWS"
        self.assertIn("XI_CHANNEL_NO_PUBLISHING_PATH", validate_work_candidate(row))

    def test_a_grade_cannot_claim_reliable_xi_from_squad_list_only(self):
        row = valid_fixture()
        row["xi_away_channel_type"] = "OFFICIAL_SQUAD_NEWS"
        self.assertIn("XI_EXPECTATION_OVERSTATED", validate_work_candidate(row))

    def test_uncertain_xi_must_have_conditional_b_not_a(self):
        row = valid_fixture()
        row["operational_viability_grade"] = "A"
        row["xi_expected"] = "UNCERTAIN"
        self.assertIn("XI_UNCERTAIN_MUST_BE_CONDITIONAL_B", validate_work_candidate(row))

    def test_xi_recheck_near_kickoff_is_required(self):
        row = valid_fixture()
        row["xi_recheck_due_utc"] = "2026-10-09T08:00:00Z"
        self.assertIn("XI_PREMATCH_RECHECK_PLAN_MISSING_OR_INVALID",
                      validate_work_candidate(row))

    def test_market_fixture_specific_id_required(self):
        row = valid_fixture()
        row["asian_total_market_match_id"] = "wrong-match"
        self.assertIn("CURRENT_ASIAN_TOTAL_FIXTURE_ID_MISMATCH",
                      validate_work_candidate(row))

    def test_asian_total_quote_not_generic_percentage(self):
        row = valid_fixture()
        row["asian_total_market_line"] = None
        self.assertIn("CURRENT_ASIAN_TOTAL_LINE_MISSING",
                      validate_work_candidate(row))

    def test_market_capture_staleness_fails(self):
        row = valid_fixture()
        row["asian_total_market_observed_at_utc"] = "2026-10-01T00:00:00Z"
        self.assertIn("CURRENT_ASIAN_TOTAL_STALE_OR_POST_KO",
                      validate_work_candidate(row))

    def test_post_kickoff_capture_fails(self):
        row = valid_fixture()
        row["asian_total_market_observed_at_utc"] = "2026-10-10T01:00:00Z"
        self.assertIn("CURRENT_ASIAN_TOTAL_STALE_OR_POST_KO",
                      validate_work_candidate(row))

    def test_amateur_unsupported_tier_fails(self):
        row = valid_fixture()
        row["competition_support_tier"] = "UNVERIFIED_MICRO"
        self.assertIn("COMPETITION_SUPPORT_UNVERIFIED",
                      validate_work_candidate(row))

    def test_professional_lower_division_not_blanket_excluded(self):
        row = valid_fixture()
        row["competition_support_reason"] = "Established second division with independent XI & total lines"
        self.assertEqual(validate_work_candidate(row), [])

    def test_womens_verified_topflight_equal_proof_can_pass(self):
        row = valid_fixture()
        row["competition_support_tier"] = "VERIFIED_WOMEN_TOP_FLIGHT"
        self.assertEqual(validate_work_candidate(row), [])

    def test_protected_national_team_with_evidenced_matchday_channel_can_be_conditional(self):
        row = valid_fixture()
        row["competition_support_tier"] = "PROTECTED_OFFICIAL"
        row["xi_expected"] = "UNCERTAIN"
        self.assertEqual(validate_work_candidate(row), [])

    def test_incomplete_evidence_preserved_but_not_admitted(self):
        row = valid_fixture()
        row["preflight_complete"] = False
        self.assertEqual(classify_preflight(row)["disposition"],
                         "PREFLIGHT_INCOMPLETE_NO_WORK")

    def test_user_exception_still_requires_market(self):
        row = valid_fixture()
        row["competition_support_tier"] = "USER_EXCEPTION"
        del row["asian_total_fixture_source_url"]
        self.assertIn("CURRENT_ASIAN_TOTAL_SOURCE_MISSING",
                      validate_work_candidate(row))

    def test_user_excluded_fixture_cannot_leak(self):
        row = valid_fixture()
        row["user_scope_excluded"] = True
        self.assertIn("USER_SCOPE_EXCLUDED", validate_work_candidate(row))

    def test_team_news_must_be_available(self):
        row = valid_fixture()
        row["team_news_observability"] = "LOW"
        self.assertIn("TEAM_NEWS_NOT_OBSERVABLE",
                      validate_work_candidate(row))


if __name__ == "__main__":
    unittest.main()
