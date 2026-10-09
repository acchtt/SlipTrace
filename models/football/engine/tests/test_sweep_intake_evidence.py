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

    def test_xi_uncertain_b_is_not_work_eligible(self):
        row = valid_fixture()
        row["xi_expected"] = "UNCERTAIN"
        self.assertIn("XI_CHANNEL_NOT_VERIFIABLE", validate_work_candidate(row))

    def test_both_sides_recent_xi_needed(self):
        row = valid_fixture()
        del row["xi_away_recent_match_id"]
        self.assertIn("XI_BOTH_TEAMS_RECENT_CONFIRMED_EVIDENCE_MISSING",
                      validate_work_candidate(row))

    def test_historical_xi_must_precede_match(self):
        row = valid_fixture()
        row["xi_home_recent_match_kickoff_utc"] = "2026-10-11T00:00:00Z"
        self.assertIn("XI_HOME_HISTORICAL_FIXTURE_TIME_STALE",
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

    def test_protected_national_team_does_not_bypass_xi(self):
        row = valid_fixture()
        row["competition_support_tier"] = "PROTECTED_OFFICIAL"
        row["xi_expected"] = "UNCERTAIN"
        self.assertIn("XI_CHANNEL_NOT_VERIFIABLE", validate_work_candidate(row))

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
