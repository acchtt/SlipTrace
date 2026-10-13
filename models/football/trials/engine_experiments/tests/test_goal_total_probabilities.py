import pathlib
import sys
import unittest
from datetime import datetime, timedelta, timezone

sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
from goal_total_probabilities import GoalProbabilityError, estimate, validate_holdout

FROZEN=datetime(2026,10,11,10,0,tzinfo=timezone.utc)
ASSESS=FROZEN+timedelta(minutes=5)
KO=FROZEN+timedelta(hours=2)


def evidence(venue,for_goals,against_goals):
    return {"source_url":"https://example.org/league/team-results",
            "observed_at_utc":FROZEN.isoformat(),
            "venue_matched_games":[
                {"fixture_id":venue+str(i),
                 "kickoff_utc":(FROZEN-timedelta(days=2+i)).isoformat(),
                 "venue":venue,"goals_for":for_goals,
                 "goals_against":against_goals}
                for i in range(6)
            ]}


def payload():
    return {"schema_version":"football-goal-probability-experiment-v1",
            "match_id":"fixture-one","evidence_epoch_id":"fixture-one-signed",
            "market_independent_inputs":True,
            "frozen_at_utc":FROZEN.isoformat(),
            "assessment_at_utc":ASSESS.isoformat(),
            "kickoff_utc":KO.isoformat(),
            "home":evidence("HOME",2,1),
            "away":evidence("AWAY",1,2),
            "quotes":[{"market_phase":"PREMATCH","line":2.75,
                       "decimal_odds":1.9,
                       "source_url":"https://example.org/market/game",
                       "observed_at_utc":(ASSESS-timedelta(seconds=35)).isoformat()}]}


class GoalDistributionQATests(unittest.TestCase):
    def test_source_derived_expected_total_and_tail(self):
        r=estimate(payload())
        self.assertAlmostEqual(r["expected_home_goals"],2)
        self.assertAlmostEqual(r["expected_away_goals"],1)
        self.assertAlmostEqual(r["expected_total_goals"],3)
        self.assertAlmostEqual(r["p_at_least_3"],0.57681,places=4)
        self.assertGreater(r["p_at_least_3"],r["p_at_least_4"])
        self.assertGreater(r["p_at_least_4"],r["p_at_least_5"])
        self.assertAlmostEqual(sum(r["total_goal_probs_0_to_24"])+r["tail_probability_over_24"],1,places=8)
        self.assertEqual(r["calibration_status"],"UNVALIDATED_RESEARCH_ONLY")

    def test_real_quote_indicative_ev_never_authorizes_bet(self):
        r=estimate(payload())
        self.assertEqual(r["quotes"][0]["at_three_goals"],"HALF WIN")
        self.assertEqual(r["quotes"][0]["full_win_goals"],4)
        self.assertIsInstance(r["quotes"][0]["model_conditional_unit_profit"],float)
        self.assertFalse(r["quotes"][0]["positive_ev_established"])
        self.assertFalse(r["bet_authorized"])

    def test_absent_quote_cannot_be_inferred_from_distribution(self):
        p=payload()
        p["quotes"]=[]
        r=estimate(p)
        self.assertEqual(r["quotes"],[])
        self.assertFalse(r["bet_authorized"])

    def test_post_kickoff_and_unobserved_old_quote_rejected(self):
        for quote_age in (timedelta(minutes=3),timedelta(hours=-1)):
            p=payload()
            p["quotes"][0]["observed_at_utc"]=(ASSESS-quote_age).isoformat()
            with self.assertRaises(GoalProbabilityError):
                estimate(p)
        p=payload()
        p["assessment_at_utc"]=KO.isoformat()
        with self.assertRaisesRegex(GoalProbabilityError,"prospectively"):
            estimate(p)

    def test_no_league_venue_mixing_or_future_results(self):
        p=payload()
        p["away"]["venue_matched_games"][0]["venue"]="HOME"
        with self.assertRaisesRegex(GoalProbabilityError,"non-venue-matched"):
            estimate(p)
        p=payload()
        p["home"]["venue_matched_games"][0]["kickoff_utc"]=(FROZEN-timedelta(minutes=10)).isoformat()
        with self.assertRaisesRegex(GoalProbabilityError,"not provably final"):
            estimate(p)

    def test_no_market_derived_lambda_or_hindsight(self):
        for key in ("bookmaker_implied_lambda","ft_total","live_score","actual_bet"):
            p=payload()
            p[key]=4
            with self.assertRaisesRegex(GoalProbabilityError,"contamination"):
                estimate(p)
        p=payload()
        p["market_independent_inputs"]=False
        with self.assertRaisesRegex(GoalProbabilityError,"independent"):
            estimate(p)

    def test_price_sensitive_correct_asian_line(self):
        a=payload()
        r=estimate(a)
        quote=r["quotes"][0]
        a["quotes"][0]["line"]=2.25
        a["quotes"][0]["decimal_odds"]=1.9
        lower=estimate(a)["quotes"][0]
        self.assertEqual(lower["at_three_goals"],"WIN")
        self.assertEqual(quote["at_three_goals"],"HALF WIN")
        self.assertGreater(lower["model_conditional_unit_profit"],quote["model_conditional_unit_profit"])

    def test_holdout_requires_valid_prospective_timestamps_and_sample_size(self):
        sample={"match_id":"one","frozen_at_utc":FROZEN.isoformat(),
                "kickoff_utc":KO.isoformat(),
                "result_observed_at_utc":(KO+timedelta(hours=3)).isoformat(),
                "actual_total_goals":3,
                "p_at_least_3":0.58,"p_at_least_4":0.35,"p_at_least_5":0.18}
        input_data={"schema_version":"football-goal-probability-holdout-v1",
                    "sealed_matches":[sample]}
        result=validate_holdout(input_data)
        self.assertEqual(result["validation_status"],"INSUFFICIENT_UNIQUE_PROSPECTIVE_HOLDOUTS")
        self.assertEqual(result["tail_metrics"]["3"]["observed_rate"],1)
        input_data["sealed_matches"].append(dict(sample))
        with self.assertRaisesRegex(GoalProbabilityError,"duplicate"):
            validate_holdout(input_data)
        input_data["sealed_matches"]=[dict(sample,result_observed_at_utc=KO.isoformat())]
        with self.assertRaisesRegex(GoalProbabilityError,"chronology"):
            validate_holdout(input_data)


if __name__=="__main__":
    unittest.main()
