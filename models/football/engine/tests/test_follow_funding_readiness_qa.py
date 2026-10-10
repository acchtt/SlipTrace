import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from follow_funding_readiness_qa import analyze, FollowFundingQAError
from test_goal_burden_qa import factors


def case(mid="demo"):
    f = factors()
    f.update(dict(carrier="STRONG", carrier_self_fund=False,
                  independent_upper_tail=True, continuation_quality="MEDIUM",
                  burden_completion_quality="HIGH", failure_resistance="MEDIUM",
                  completion_mode="TWO_SIDED"))
    return {
        "match_id": mid, "evidence_epoch_id": mid+"-frozen",
        "kickoff_utc": "2026-10-10T16:00:00Z",
        "assessment_at_utc": "2026-10-10T15:08:00Z",
        "official_c_follow_lane": "FOLLOW",
        "forecast_total": 3.3, "market_center": 3.25,
        "c": {"board_state": "FOCUS", "supported_line": 2.75,
              "frozen_at_utc": "2026-10-10T15:01:00Z", "frozen_factors": dict(f)},
        "c2": {"board_state": "FOCUS", "supported_line": 3.0,
               "frozen_at_utc": "2026-10-10T15:01:00Z", "frozen_factors": dict(f)},
    }


def board(rows):
    return {"schema_version": "football-follow-funding-readiness-v1",
            "board_id": "B-TEST", "source_revision": "test-aabb1234",
            "fixtures": rows}


class FundingQARegression(unittest.TestCase):
    def test_unfunded_supported_line_is_detected(self):
        out = analyze(board([case()]))
        self.assertEqual(out["official_c_follow_funded_at_supported"], 0)
        self.assertEqual(out["c2_shadow_focus_funded_at_supported"], 0)
        self.assertIn("CRITICAL_ALL_FOLLOW_SUPPORTED_BURDENS_UNFUNDED", out["warning_codes"])

    def test_five_independent_follow_rows(self):
        out = analyze(board([case("demo-"+str(i)) for i in range(5)]))
        self.assertEqual(out["official_c_follow"], 5)
        self.assertEqual(out["official_c_follow_funded_at_supported"], 0)
        self.assertEqual(out["c2_shadow_focus_funded_at_supported"], 0)

    def test_funding_ready_does_not_imply_any_published_action(self):
        row = case()
        for name in ("c", "c2"):
            row[name]["frozen_factors"].update(
                carrier_self_fund=True, failure_resistance="HIGH", chance_quality="HIGH"
            )
        out = analyze(board([row]))
        self.assertEqual(out["official_c_follow_funded_at_supported"], 1)
        self.assertEqual(out["c2_shadow_focus_funded_at_supported"], 1)
        self.assertFalse(out["fixtures"][0]["c"]["bet_authorized"])
        self.assertEqual(out["fixtures"][0]["c"]["action"], "NOT_ASSESSED")

    def test_independent_shadow_required(self):
        row = case()
        row["c2"]["frozen_factors"] = None
        with self.assertRaisesRegex(FollowFundingQAError, "independent frozen_factors"):
            analyze(board([row]))

    def test_no_future_assessments(self):
        row = case()
        row["assessment_at_utc"] = row["kickoff_utc"]
        with self.assertRaisesRegex(FollowFundingQAError, "precede kickoff"):
            analyze(board([row]))

    def test_no_outcomes_in_forecast_review(self):
        row = case()
        row["final_score"] = "3-3"
        with self.assertRaisesRegex(FollowFundingQAError, "forbidden"):
            analyze(board([row]))


if __name__ == "__main__":
    unittest.main()
