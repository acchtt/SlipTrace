import copy
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from step2_price_aware_shadow import PriceShadowError, compare
from test_goal_burden_qa import factors


def raw_factors(**kwargs):
    f = factors()
    f.update({
        "carrier": "STRONG",
        "carrier_self_fund": False,
        "independent_upper_tail": True,
        "completion_mode": "CARRIER_LED",
        "home_route": "STRONG",
        "away_route": "USABLE",
        "burden_completion_quality": "HIGH",
        "continuation_quality": "MEDIUM",
        "opponent_leakage": "MEDIUM",
        "burden_stall_risk": "MEDIUM",
        "route_reliability": "HIGH",
        "independent_route_quality": "HIGH",
        "chance_quality": "HIGH",
        "failure_resistance": "MEDIUM",
    })
    f.update(kwargs)
    return f


def example():
    return {
        "schema_version": "football-step2-price-calibration-shadow-v1",
        "mode": "PROSPECTIVE_PREMATCH_SHADOW",
        "fixture": {
            "match_id": "m-frozen",
            "evidence_epoch_id": "m-20261010-1500",
            "fixture_status": "PREMATCH_CONFIRMED",
            "kickoff_utc": "2026-10-10T16:00:00Z",
            "assessment_at_utc": "2026-10-10T15:42:00Z",
            "xi_status": "CONFIRMED",
            "thesis_state": "PRESERVED",
            "primary_mechanism_intact": True,
            "material_veto": False,
        },
        "models": {
            "c": {
                "board_state": "FOCUS", "supported_line": 2.75,
                "frozen_at_utc": "2026-10-10T15:01:00Z",
                "frozen_factors": raw_factors(),
            },
            "c2": {
                "board_state": "FOCUS", "supported_line": 3.0,
                "frozen_at_utc": "2026-10-10T15:01:00Z",
                "frozen_factors": raw_factors(),
            },
        },
        "forecast_total": 3.30,
        "forecast_frozen_at_utc": "2026-10-10T15:01:00Z",
        "market_independent_forecast": True,
        "quotes": [{
            "market_phase": "PREMATCH",
            "line": 2.75, "decimal_odds": 1.83,
            "source_url": "https://example.org/odds/match-1",
            "observed_at_utc": "2026-10-10T15:41:10Z",
        }],
    }


class PriceAwareShadowQATests(unittest.TestCase):
    def test_c_production_unfunded_but_alternative_funding_candidate_not_bet(self):
        result = compare(example())
        c = result["c_official_production_unchanged"]
        self.assertFalse(c["funded_at_own_supported_line"])
        self.assertTrue(c["alternative_shadow_funded_at_own_support"])
        self.assertEqual(c["quotes_evaluated"][0]["research_priority_code"],
                         "SHADOW_PRICE_AWARE_ELIGIBILITY_ONLY")
        self.assertTrue(c["quotes_evaluated"][0]["shadow_price_candidate_for_backtest"])
        self.assertFalse(c["bet_authorized"])
        self.assertIsNone(result["expected_value"])
        self.assertIsNone(result["official_c_exposure"])

    def test_no_quote_is_not_a_hypothetical_executable_price(self):
        x = example()
        x["quotes"] = []
        result = compare(x)
        self.assertEqual(result["status"], "NO_VALIDATED_EXECUTABLE_OFFERS_TO_COMPARE")
        self.assertFalse(result["c_official_production_unchanged"]["has_current_quoted_shadow_candidate"])

    def test_high_market_quote_stays_unresolved_not_fake_wait(self):
        x = example()
        x["quotes"][0]["line"] = 3.25
        out = compare(x)
        q = out["c_official_production_unchanged"]["quotes_evaluated"][0]
        self.assertEqual(q["research_priority_code"], "MARKET_ABOVE_FROZEN_SUPPORT_RECHECK_NO_INFERRED_WAIT")
        self.assertFalse(q["shadow_price_candidate_for_backtest"])
        self.assertEqual(q["payoff_scenarios"]["full_win_from_total_goals"], 4)

    def test_quarterline_settlement_at_exact_three(self):
        out = compare(example())
        q = out["c_official_production_unchanged"]["quotes_evaluated"][0]
        self.assertEqual(q["payoff_scenarios"]["at_3_goals"]["settlement"], "HALF WIN")
        self.assertAlmostEqual(q["payoff_scenarios"]["at_3_goals"]["hypothetical_profit_per_1u"], .415)
        self.assertIsNone(q["payoff_scenarios"]["computed_expected_value"])

    def test_c2_is_truly_independent(self):
        x = example()
        x["models"]["c2"]["frozen_factors"] = raw_factors(
            home_route="WEAK", independent_route_quality="LOW",
            route_reliability="LOW", failure_resistance="LOW")
        out = compare(x)
        self.assertFalse(out["c2_independent_shadow"]["alternative_shadow_funded_at_own_support"])
        self.assertTrue(out["c_official_production_unchanged"]["alternative_shadow_funded_at_own_support"])

    def test_two_strong_routes_can_raise_o3_0_shadow_challenge(self):
        x = example()
        x["models"]["c"]["supported_line"] = 3.0
        x["models"]["c"]["frozen_factors"] = raw_factors(
            home_route="STRONG", away_route="STRONG", completion_mode="TWO_SIDED")
        x["quotes"][0]["line"] = 3.0
        out = compare(x)
        self.assertFalse(out["c_official_production_unchanged"]["funded_at_own_supported_line"])
        self.assertTrue(out["c_official_production_unchanged"]["alternative_shadow_funded_at_own_support"])

    def test_material_veto_prevents_candidate_even_when_price_is_present(self):
        x = example()
        x["fixture"]["material_veto"] = True
        out = compare(x)
        self.assertFalse(out["c_official_production_unchanged"]["has_current_quoted_shadow_candidate"])

    def test_an_unconfirmed_xi_can_still_be_analyzed_without_action(self):
        x = example()
        x["fixture"]["xi_status"] = "UNAVAILABLE"
        out = compare(x)
        self.assertEqual(out["c_official_production_unchanged"]["quotes_evaluated"][0]["research_priority_code"],
                         "XI_OR_PRIMARY_THESIS_RECHECK_REQUIRED")
        self.assertFalse(out["c_official_production_unchanged"]["has_current_quoted_shadow_candidate"])

    def test_stale_future_and_postkickoff_quotes_rejected(self):
        for clock in ("2026-10-10T15:39:00Z", "2026-10-10T15:43:00Z",
                      "2026-10-10T16:01:00Z"):
            with self.subTest(clock=clock):
                x = example()
                x["quotes"][0]["observed_at_utc"] = clock
                with self.assertRaises(PriceShadowError):
                    compare(x)

    def test_expired_prematch_sends_user_to_live(self):
        x = example()
        x["fixture"]["assessment_at_utc"] = x["fixture"]["kickoff_utc"]
        with self.assertRaisesRegex(PriceShadowError, "postkickoff"):
            compare(x)
        x = example()
        x["fixture"]["fixture_status"] = "STARTED"
        with self.assertRaisesRegex(PriceShadowError, "prematch"):
            compare(x)

    def test_unverified_url_nonquarter_line_and_no_shadow_rejected(self):
        for key, val in (("line", 2.33), ("source_url", "http://example.org"),
                         ("decimal_odds", 1.0)):
            with self.subTest(key=key):
                x = example()
                x["quotes"][0][key] = val
                with self.assertRaises(PriceShadowError):
                    compare(x)
        x = example()
        x["models"].pop("c2")
        with self.assertRaisesRegex(PriceShadowError, "independent"):
            compare(x)

    def test_no_results_or_actual_bets_in_prospective_comparator(self):
        for key, val in (("final_score", "4-1"), ("pnl", 100), ("actual_bet", "BET")):
            with self.subTest(key=key):
                x = example()
                x[key] = val
                with self.assertRaisesRegex(PriceShadowError, "forbidden"):
                    compare(x)

    def test_unfunded_alternative_without_price_floor_remains_only_diagnostic(self):
        x = example()
        x["quotes"][0]["decimal_odds"] = 1.58
        out = compare(x)
        self.assertFalse(out["c_official_production_unchanged"]["has_current_quoted_shadow_candidate"])
        self.assertEqual(out["c_official_production_unchanged"]["quotes_evaluated"][0]["research_priority_code"],
                         "QUOTE_BELOW_COMPARISON_PRICE_FLOOR")

    def test_forecast_cannot_be_generated_from_current_market_or_future(self):
        x = example()
        x["forecast_frozen_at_utc"] = x["fixture"]["assessment_at_utc"]
        with self.assertRaisesRegex(PriceShadowError, "predate"):
            compare(x)
        x = example()
        x["market_independent_forecast"] = False
        with self.assertRaisesRegex(PriceShadowError, "independence"):
            compare(x)


if __name__ == "__main__":
    unittest.main()
