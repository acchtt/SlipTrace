import copy
import pathlib
import sys
import unittest

ENGINE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE))

from step2_fixture_transition import TransitionError, route_fixture


def sample(**changes):
    row = {
        "schema_version": "football-step2-kickoff-transition-v1",
        "match_id": "match-123",
        "kickoff_utc": "2026-10-10T17:30:00+07:00",
        "assessment_at_utc": "2026-10-10T17:39:00+07:00",
        "fixture_status": "STARTED",
        "score": "0-0",
        "match_minute": 9,
        "material_event_since_frozen": "NONE_VERIFIED",
        "live_quote": {
            "market_phase": "LIVE",
            "total_line": 2.5,
            "decimal_odds": 1.85,
            "source_url": "https://book.example.org/fixture/123",
            "observed_at_utc": "2026-10-10T17:38:30+07:00",
        },
    }
    row.update(changes)
    return row


class KickoffTransitionTests(unittest.TestCase):
    def test_nine_minutes_late_is_fast_live_not_blocked(self):
        x = route_fixture(sample())
        self.assertEqual(x["route"], "EARLY_LIVE_FAST_PATH")
        self.assertTrue(x["assessment_allowed"])
        self.assertTrue(x["live_context_complete"])
        self.assertTrue(x["live_quote_verified_for_epoch"])
        self.assertEqual(x["assessment_status"], "CURRENT_LIVE_FOOTBALL_ASSESSMENT_READY")
        self.assertTrue(x["football_assessment_ready"])
        self.assertFalse(x["football_assessment_quote_required"])
        self.assertEqual(x["executable_quote_status"], "CURRENT_LIVE_QUOTE_OBSERVED_NO_ACTION_ENGINE")
        self.assertTrue(x["live_price_comparison_allowed"])
        self.assertEqual(x["live_price_action_engine_status"], "NOT_IMPLEMENTED_V4")
        self.assertFalse(x["prematch_bet_authorized"])
        self.assertFalse(x["live_bet_authorized"])

    def test_two_minutes_late_qualitative_assessment_without_quote(self):
        row = sample(assessment_at_utc="2026-10-10T17:32:00+07:00", match_minute=2, live_quote=None)
        out = route_fixture(row)
        self.assertTrue(out["assessment_allowed"])
        self.assertEqual(out["route"], "EARLY_LIVE_FAST_PATH")
        self.assertEqual(out["assessment_status"], "CURRENT_LIVE_FOOTBALL_ASSESSMENT_READY")
        self.assertTrue(out["football_assessment_ready"])
        self.assertFalse(out["football_assessment_quote_required"])
        self.assertFalse(out["live_quote_required_for_football_assessment"])
        self.assertTrue(out["live_quote_required_for_executable_bet"])
        self.assertEqual(out["executable_quote_status"], "UNPRICED_NO_EXECUTABLE_BET")
        self.assertFalse(out["live_quote_verified_for_epoch"])
        self.assertFalse(out["live_bet_authorized"])

    def test_current_live_quote_never_becomes_executable_without_action_engine(self):
        out = route_fixture(sample())
        self.assertTrue(out["live_quote_verified_for_epoch"])
        self.assertTrue(out["live_price_comparison_allowed"])
        self.assertEqual(out["live_price_action_engine_status"], "NOT_IMPLEMENTED_V4")
        self.assertFalse(out["live_bet_authorized"])

    def test_missing_stale_or_prematch_quote_does_not_block_c_c2_football(self):
        quotes = (
            None,
            "provider-error-not-a-quote",
            {"market_phase": "PREMATCH"},
            {"market_phase": "LIVE", "total_line": 2.5,
             "decimal_odds": 1.85,
             "source_url": "https://book.example.org/game",
             "observed_at_utc": "2026-10-10T17:31:00+07:00"},
        )
        for quote in quotes:
            with self.subTest(quote=quote):
                result = route_fixture(sample(live_quote=quote))
                self.assertEqual(result["route"], "EARLY_LIVE_FAST_PATH")
                self.assertTrue(result["football_assessment_ready"])
                self.assertEqual(result["assessment_status"],
                                 "CURRENT_LIVE_FOOTBALL_ASSESSMENT_READY")
                self.assertFalse(result["live_quote_verified_for_epoch"])
                self.assertFalse(result["live_bet_authorized"])
                self.assertTrue(result["quote_free_football_assessment_allowed"])
                self.assertEqual(result["executable_quote_status"],
                                 "UNPRICED_NO_EXECUTABLE_BET")

    def test_quote_free_assessment_continues_after_fast_live_window(self):
        out = route_fixture(sample(
            assessment_at_utc="2026-10-10T17:46:00+07:00",
            match_minute=16, live_quote=None,
        ))
        self.assertEqual(out["route"], "STANDARD_LIVE")
        self.assertEqual(out["assessment_status"],
                         "CURRENT_LIVE_FOOTBALL_ASSESSMENT_READY")
        self.assertTrue(out["football_assessment_ready"])
        self.assertFalse(out["live_bet_authorized"])

    def test_goal_reassessment_can_proceed_without_quote(self):
        out = route_fixture(sample(
            score="1-0", match_minute=6,
            assessment_at_utc="2026-10-10T17:36:00+07:00",
            material_event_since_frozen="GOAL", live_quote=None,
        ))
        self.assertTrue(out["assessment_allowed"])
        self.assertEqual(out["assessment_status"],
                         "LIVE_FOOTBALL_MECHANISM_RECHECK_REQUIRED")
        self.assertTrue(out["material_football_recheck_required"])
        self.assertFalse(out["live_quote_required_for_football_assessment"])
        self.assertEqual(out["executable_quote_status"],
                         "UNPRICED_NO_EXECUTABLE_BET")

    def test_fifteen_min_boundary_not_hard_assessment_cutoff(self):
        a = route_fixture(sample(assessment_at_utc="2026-10-10T17:45:00+07:00", match_minute=15, live_quote=None))
        b = route_fixture(sample(assessment_at_utc="2026-10-10T17:46:00+07:00", match_minute=16, live_quote=None))
        self.assertEqual(a["route"], "EARLY_LIVE_FAST_PATH")
        self.assertEqual(b["route"], "STANDARD_LIVE")
        self.assertTrue(b["assessment_allowed"])

    def test_prematch_quote_is_never_current_live_quote(self):
        row = sample()
        row["live_quote"]["market_phase"] = "PREMATCH"
        x = route_fixture(row)
        self.assertEqual(x["quote_status"], "PREMATCH_QUOTE_EXPIRED")
        self.assertFalse(x["live_quote_verified_for_epoch"])

    def test_expired_or_pre_kickoff_live_quote_not_valid(self):
        for stamp in ("2026-10-10T17:30:30+07:00", "2026-10-10T17:29:59+07:00"):
            with self.subTest(stamp=stamp):
                row = sample()
                row["live_quote"]["observed_at_utc"] = stamp
                x = route_fixture(row)
                self.assertEqual(x["quote_status"], "LIVE_QUOTE_EXPIRED_OR_PRE_KICKOFF")
                self.assertFalse(x["live_bet_authorized"])

    def test_goal_red_card_and_unknown_event_do_not_end_analysis(self):
        for event in ("GOAL", "RED_CARD", "OTHER_MATERIAL", "UNKNOWN"):
            with self.subTest(event=event):
                out = route_fixture(sample(material_event_since_frozen=event))
                self.assertTrue(out["assessment_allowed"])
                self.assertTrue(out["material_football_recheck_required"])
                self.assertEqual(out["assessment_status"], "LIVE_FOOTBALL_MECHANISM_RECHECK_REQUIRED")

    def test_unverified_score_minute_still_allows_qualitative_assessment(self):
        for altered in ({"score": None}, {"match_minute": None}):
            out = route_fixture(sample(**altered))
            self.assertTrue(out["assessment_allowed"])
            self.assertEqual(out["assessment_status"], "LIVE_SCORE_AND_MINUTE_RECHECK_FOR_FOOTBALL")
            self.assertFalse(out["live_context_complete"])

    def test_prematch_remains_prematch_before_kickoff(self):
        out = route_fixture(sample(fixture_status="PREMATCH_CONFIRMED", assessment_at_utc="2026-10-10T17:28:00+07:00"))
        self.assertEqual(out["route"], "PREMATCH_STEP2")

    def test_stale_prematch_after_kickoff_routes_to_status_recheck(self):
        out = route_fixture(sample(fixture_status="PREMATCH_CONFIRMED"))
        self.assertEqual(out["route"], "VERIFY_LIVE_STATUS")
        self.assertTrue(out["assessment_allowed"])
        self.assertFalse(out["prematch_bet_authorized"])

    def test_finished_is_historical_not_an_executable_bet(self):
        out = route_fixture(sample(fixture_status="FINISHED"))
        self.assertEqual(out["route"], "NON_ACTIONABLE_STATUS")
        self.assertTrue(out["assessment_allowed"])
        self.assertFalse(out["live_bet_authorized"])

    def test_started_before_kickoff_is_invalid(self):
        with self.assertRaisesRegex(TransitionError, "precede"):
            route_fixture(sample(assessment_at_utc="2026-10-10T17:28:00+07:00"))

    def test_bad_quote_or_bad_schema_cannot_create_action(self):
        for quote in (
            {"market_phase": "LIVE", "total_line": 2.33, "decimal_odds": 1.85},
            {"market_phase": "LIVE", "total_line": 2.5, "decimal_odds": 1.85,
             "source_url": "http://book.example.org", "observed_at_utc": "2026-10-10T17:39:00+07:00"},
        ):
            with self.subTest(quote=quote):
                out = route_fixture(sample(live_quote=quote))
                self.assertFalse(out["live_quote_verified_for_epoch"])
                self.assertFalse(out["live_bet_authorized"])
        with self.assertRaisesRegex(TransitionError, "schema_version"):
            route_fixture(sample(schema_version="nonsense"))


if __name__ == "__main__":
    unittest.main()
