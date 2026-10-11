import pathlib
import sys
import unittest

ENGINE_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE_DIR))

from sweep_intake_evidence import classify_preflight, validate_work_candidate, validate_shared_league_profiles  # noqa: E402


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


def league_candidate(name="Premier League", profile_type="TIER1_STANDARD"):
    row = valid_fixture()
    row["competition_name"] = name
    row["intake_evidence_scope"] = "LEAGUE_CHANNEL_ONLY"
    row["league_channel_profile"] = {
        "competition_name": name,
        "profile_type": profile_type,
        "season": "2026/27",
        "coverage_status": "VERIFIED_CHANNELS",
        "evidence_checked_at_utc": "2026-10-09T10:00:00Z",
        "evidence_basis": "Current league-provider XI, Asian totals and official news channels",
        "xi_provider_url": "https://fotmob.example.org/league/lineups",
        "asian_total_provider_url": "https://book.example.org/league/totals",
        "team_news_provider_url": "https://league.example.org/news",
        "recent_xi_fixture_count": 3,
        "recent_asian_total_fixture_count": 3,
    }
    for k in (
        "xi_home_channel_type", "xi_home_channel_source_url",
        "xi_away_channel_type", "xi_away_channel_source_url",
        "asian_total_market_match_id", "asian_total_fixture_source_url",
        "asian_total_market_line", "asian_total_market_bookmaker",
        "asian_total_market_observed_at_utc", "team_news_source_url",
    ):
        row.pop(k, None)
    return row


class LeagueChannelFirstTests(unittest.TestCase):
    def test_same_league_reuses_exact_same_frozen_profile(self):
        first = league_candidate()
        second = league_candidate()
        second["match_id"] = "later-fixture"
        self.assertEqual(validate_shared_league_profiles([first, second]), [])
        second["league_channel_profile"]["asian_total_provider_url"] = (
            "https://differentbook.example.org/league/totals"
        )
        self.assertIn("LEAGUE_CHANNEL_PROFILE_INCONSISTENT: Premier League",
                      validate_shared_league_profiles([first, second]))

    def test_different_leagues_may_have_distinct_verified_profiles(self):
        rows = [league_candidate("Premier League"), league_candidate("Bundesliga")]
        self.assertEqual(validate_shared_league_profiles(rows), [])


    def test_tier1_enter_work_without_match_quote_or_individual_xi(self):
        row = league_candidate()
        self.assertEqual(
            validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"), []
        )
        self.assertTrue(classify_preflight(
            row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"
        )["work_queue_eligible"])
        self.assertIn(
            "CURRENT_ASIAN_TOTAL_FIXTURE_ID_MISMATCH",
            validate_work_candidate(row),
        )

    def test_tier1_claim_must_match_explicit_known_competition(self):
        row = league_candidate("Unknown Unverified Premier")
        self.assertIn("LEAGUE_TIER1_NOT_ALLOWLISTED",
                      validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"))

    def test_non_tier1_league_requires_observed_xi_and_market_evidence(self):
        row = league_candidate("Professional Second Division", "PROVEN_LEAGUE")
        self.assertEqual(validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"), [])
        row["league_channel_profile"]["recent_xi_fixture_count"] = 1
        self.assertIn("LEAGUE_PROFILE_RECENT_XI_FIXTURE_COUNT_UNPROVEN",
                      validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"))

    @staticmethod
    def championship_evidence():
        def team(prefix, scores):
            return {
                "source_url": "https://scores.example.org/" + prefix,
                "recent_competitive_matches": [
                    {"match_id": prefix + str(i), "kickoff_utc": "2026-10-0" + str(i+1) + "T12:00:00Z",
                     "goals_for": gf, "goals_against": ga, "competitive": True}
                    for i, (gf, ga) in enumerate(scores)
                ],
            }
        return {
            "captured_at_utc": "2026-10-09T10:00:00Z",
            "home": team("home-", [(2,1),(2,2),(3,1),(1,2),(2,1)]),
            "away": team("away-", [(1,2),(2,2),(2,1),(2,1),(1,2)]),
        }

    def test_german_second_tier_requires_proven_profile_not_tier_one(self):
        row = league_candidate("2. Bundesliga", "PROVEN_LEAGUE")
        self.assertEqual(validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"), [])
        row["league_channel_profile"]["recent_asian_total_fixture_count"] = 1
        self.assertIn("LEAGUE_PROFILE_RECENT_ASIAN_TOTAL_FIXTURE_COUNT_UNPROVEN",
                      validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"))
        row = league_candidate("2. Bundesliga", "TIER1_STANDARD")
        self.assertIn("LEAGUE_TIER1_NOT_ALLOWLISTED",
                      validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"))

    def test_obos_profile_requires_two_actual_xi_and_asian_total_fixture_channels(self):
        row = league_candidate("OBOS-ligaen", "PROVEN_LEAGUE")
        self.assertEqual(validate_work_candidate(
            row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"), [])
        row["league_channel_profile"]["recent_xi_fixture_count"] = 1
        self.assertIn("LEAGUE_PROFILE_RECENT_XI_FIXTURE_COUNT_UNPROVEN",
                      validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"))
        row["league_channel_profile"]["recent_xi_fixture_count"] = 3
        row["league_channel_profile"]["recent_asian_total_fixture_count"] = 1
        self.assertIn("LEAGUE_PROFILE_RECENT_ASIAN_TOTAL_FIXTURE_COUNT_UNPROVEN",
                      validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"))

    def test_obos_is_not_tier_one_and_cannot_claim_channel_without_sources(self):
        row = league_candidate("OBOS-ligaen", "TIER1_STANDARD")
        self.assertIn("LEAGUE_TIER1_NOT_ALLOWLISTED",
                      validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"))
        row["league_channel_profile"]["profile_type"] = "PROVEN_LEAGUE"
        row["league_channel_profile"]["xi_provider_url"] = ""
        self.assertIn("LEAGUE_XI_PROVIDER_URL_MISSING",
                      validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"))

    def test_obos_no_match_odds_made_up_at_step0_and_step1_strict(self):
        row = league_candidate("OBOS-ligaen", "PROVEN_LEAGUE")
        self.assertEqual(validate_work_candidate(
            row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"), [])
        self.assertIn("CURRENT_ASIAN_TOTAL_FIXTURE_ID_MISMATCH",
                      validate_work_candidate(row))
        row["is_friendly"] = True
        self.assertIn("USER_SCOPE_EXCLUDED_FRIENDLY",
                      validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"))

    def test_poland_requires_five_historical_results_and_real_channel_profile(self):
        row = league_candidate("Ekstraklasa", "PROVEN_LEAGUE")
        row["country"] = "Poland"
        self.assertIn("POLAND_EKSTRAKLASA_CHEAP_SIGNAL_MISSING",
                      validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"))
        row["poland_ekstraklasa_recent_goal_evidence"] = self.championship_evidence()
        self.assertEqual(validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"), [])
        row["league_channel_profile"]["recent_xi_fixture_count"] = 1
        self.assertIn("LEAGUE_PROFILE_RECENT_XI_FIXTURE_COUNT_UNPROVEN",
                      validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"))
        row["league_channel_profile"]["recent_xi_fixture_count"] = 3
        row["league_channel_profile"]["recent_asian_total_fixture_count"] = 0
        self.assertIn("LEAGUE_PROFILE_RECENT_ASIAN_TOTAL_FIXTURE_COUNT_UNPROVEN",
                      validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"))

    def test_poland_is_never_auto_tier1_and_must_have_country_identity(self):
        row = league_candidate("Ekstraklasa", "TIER1_STANDARD")
        row["country"] = "Poland"
        row["poland_ekstraklasa_recent_goal_evidence"] = self.championship_evidence()
        self.assertIn("LEAGUE_TIER1_NOT_ALLOWLISTED",
                      validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"))
        row["league_channel_profile"]["profile_type"] = "PROVEN_LEAGUE"
        row.pop("country")
        self.assertIn("POLAND_EKSTRAKLASA_COUNTRY_UNVERIFIED",
                      validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"))
        row["country"] = "Czech Republic"
        self.assertIn("POLAND_EKSTRAKLASA_COUNTRY_UNVERIFIED",
                      validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"))

    def test_poland_trap_and_stall_block_even_with_dominant_carrier(self):
        row = league_candidate("Ekstraklasa", "PROVEN_LEAGUE")
        row["country"] = "Poland"
        row["poland_ekstraklasa_recent_goal_evidence"] = self.championship_evidence()
        recent = row["poland_ekstraklasa_recent_goal_evidence"]["away"]["recent_competitive_matches"]
        for m in recent[:3]:
            m["goals_for"], m["goals_against"] = 1, 1
        self.assertIn("POLAND_EKSTRAKLASA_LOW_TOTAL_STALL_OR_DRAW_TRAP",
                      validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"))

    def test_poland_unverified_stale_or_post_capture_history_rejected(self):
        row = league_candidate("Ekstraklasa", "PROVEN_LEAGUE")
        row["country"] = "Poland"
        row["poland_ekstraklasa_recent_goal_evidence"] = self.championship_evidence()
        evidence = row["poland_ekstraklasa_recent_goal_evidence"]
        evidence["captured_at_utc"] = "2026-10-11T11:00:00Z"
        self.assertIn("POLAND_EKSTRAKLASA_CHEAP_SIGNAL_STALE_OR_POST_KO",
                      validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"))
        evidence["captured_at_utc"] = "2026-10-09T10:00:00Z"
        evidence["home"]["recent_competitive_matches"][0]["kickoff_utc"] = "2026-10-09T09:50:00Z"
        self.assertIn("POLAND_EKSTRAKLASA_HOME_HISTORY_INVALID",
                      validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"))
        row["poland_ekstraklasa_recent_goal_evidence"] = self.championship_evidence()
        row["poland_ekstraklasa_recent_goal_evidence"]["away"]["source_url"] = "http://invalid.local"
        self.assertIn("POLAND_EKSTRAKLASA_AWAY_GOAL_SOURCE_UNVERIFIED",
                      validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"))

    def test_poland_screen_does_not_require_old_finished_game_odds_or_create_live_quotes(self):
        row = league_candidate("Ekstraklasa", "PROVEN_LEAGUE")
        row["country"] = "Poland"
        row["poland_ekstraklasa_recent_goal_evidence"] = self.championship_evidence()
        self.assertEqual(validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"), [])
        self.assertIn("CURRENT_ASIAN_TOTAL_FIXTURE_ID_MISMATCH",
                      validate_work_candidate(row))
        self.assertEqual(validate_work_candidate(
            league_candidate("Premier League"), intake_policy="LEAGUE_CHANNEL_FIRST_V1"), [])

    def test_championship_requires_individual_five_match_signal(self):
        row = league_candidate("Championship", "PROVEN_LEAGUE")
        self.assertIn("CHAMPIONSHIP_CHEAP_SIGNAL_MISSING",
                      validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"))
        row["championship_recent_goal_evidence"] = self.championship_evidence()
        self.assertEqual(validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"), [])

    def test_championship_low_goal_and_draw_traps_block(self):
        row = league_candidate("Championship", "PROVEN_LEAGUE")
        row["championship_recent_goal_evidence"] = self.championship_evidence()
        recent = row["championship_recent_goal_evidence"]["away"]["recent_competitive_matches"]
        for m in recent[:4]:
            m["goals_for"] = 1
            m["goals_against"] = 1
        self.assertIn("CHAMPIONSHIP_LOW_TOTAL_STALL_OR_DRAW_TRAP",
                      validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"))

    def test_championship_stale_or_post_ko_history_fails_closed(self):
        row = league_candidate("EFL Championship", "PROVEN_LEAGUE")
        row["championship_recent_goal_evidence"] = self.championship_evidence()
        row["championship_recent_goal_evidence"]["captured_at_utc"] = "2026-10-11T00:00:00Z"
        self.assertIn("CHAMPIONSHIP_CHEAP_SIGNAL_STALE_OR_POST_KO",
                      validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"))
        row["championship_recent_goal_evidence"]["captured_at_utc"] = "2026-10-09T10:00:00Z"
        row["championship_recent_goal_evidence"]["home"]["recent_competitive_matches"][0]["kickoff_utc"] = "2026-10-12T12:00:00Z"
        self.assertIn("CHAMPIONSHIP_HOME_HISTORY_INVALID",
                      validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"))

    def test_championship_not_made_tier_one_and_existing_league_untouched(self):
        row = league_candidate("Championship", "TIER1_STANDARD")
        row["championship_recent_goal_evidence"] = self.championship_evidence()
        self.assertIn("LEAGUE_TIER1_NOT_ALLOWLISTED",
                      validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"))
        self.assertEqual(validate_work_candidate(league_candidate(),
                         intake_policy="LEAGUE_CHANNEL_FIRST_V1"), [])

    def test_unsupported_profile_does_not_bypass_missing_line(self):
        row = league_candidate()
        row["league_channel_profile"]["asian_total_provider_url"] = ""
        self.assertIn("LEAGUE_ASIAN_TOTAL_PROVIDER_URL_MISSING",
                      validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"))
        row = league_candidate()
        row["league_channel_profile"]["coverage_status"] = "UNKNOWN"
        self.assertIn("LEAGUE_CHANNEL_COVERAGE_UNVERIFIED",
                      validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"))

    def test_profile_cannot_be_reused_for_different_league_or_season(self):
        row = league_candidate()
        row["competition_name"] = "Bundesliga"
        self.assertIn("LEAGUE_PROFILE_COMPETITION_MISMATCH",
                      validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"))
        row = league_candidate()
        row["league_channel_profile"]["evidence_checked_at_utc"] = "2026-07-01T00:00:00Z"
        self.assertIn("LEAGUE_PROFILE_EVIDENCE_STALE_OR_POST_KO",
                      validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"))

    def test_protected_scope_and_fixture_time_still_fail_closed(self):
        row = league_candidate()
        row["is_friendly"] = True
        row["fixture_identity_verified"] = False
        row["fixture_kickoff_utc"] = "not-a-time"
        defects = validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1")
        self.assertIn("USER_SCOPE_EXCLUDED_FRIENDLY", defects)
        self.assertIn("FIXTURE_IDENTITY_UNVERIFIED", defects)
        self.assertIn("FIXTURE_KICKOFF_UTC_UNVERIFIED", defects)

    def test_league_proof_does_not_create_confirmed_starting_xi(self):
        row = league_candidate()
        row["xi_expected"] = "UNCERTAIN"
        row["operational_viability_grade"] = "A"
        self.assertIn("XI_UNCERTAIN_MUST_BE_CONDITIONAL_B",
                      validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"))


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

    def test_noncompetitive_womens_national_friendly_excluded(self):
        row = valid_fixture()
        row["competition_name"] = "Senior Women's International Friendlies"
        self.assertIn("USER_SCOPE_EXCLUDED_FRIENDLY", validate_work_candidate(row))

    def test_noncompetitive_mens_friendly_excluded(self):
        row = valid_fixture()
        row["competition_name"] = "Men's International Friendly"
        self.assertIn("USER_SCOPE_EXCLUDED_FRIENDLY", validate_work_candidate(row))

    def test_noncompetitive_club_preseason_excluded(self):
        row = valid_fixture()
        row["fixture_type"] = "Club Preseason Friendly"
        self.assertIn("USER_SCOPE_EXCLUDED_FRIENDLY", validate_work_candidate(row))

    def test_explicit_friendly_flag_excluded(self):
        row = valid_fixture()
        row["is_friendly"] = True
        self.assertIn("USER_SCOPE_EXCLUDED_FRIENDLY", validate_work_candidate(row))

    def test_friendly_skips_preflight_and_closes_scope_early(self):
        row = valid_fixture()
        row["competition_name"] = "National Team Friendly Women"
        row["preflight_complete"] = False
        row["asian_total_fixture_source_url"] = None
        self.assertEqual(
            classify_preflight(row)["disposition"],
            "STEP0_OPERATIONAL_OR_SCOPE_EXCLUDED",
        )
        self.assertIn(
            "USER_SCOPE_EXCLUDED_FRIENDLY",
            classify_preflight(row)["defects"],
        )

    def test_competitive_qualifier_not_mistaken_for_friendly(self):
        row = valid_fixture()
        row["competition_name"] = "FIFA Women's World Cup Qualification UEFA"
        self.assertEqual(validate_work_candidate(row), [])

    def test_team_news_must_be_available(self):
        row = valid_fixture()
        row["team_news_observability"] = "LOW"
        self.assertIn("TEAM_NEWS_NOT_OBSERVABLE",
                      validate_work_candidate(row))


if __name__ == "__main__":
    unittest.main()
