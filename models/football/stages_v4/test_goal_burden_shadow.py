"""Shadow diagnostics must not change Football C funded selection."""
import unittest
from goal_burden_shadow import review_goal_burden_shadow


class GoalBurdenShadowTests(unittest.TestCase):
    def test_many_medium_g3_risks_are_flagged_not_demoted(self):
        row = {
            "match_id": "copenhagen",
            "goal3_funded": True, "goal4_funded": False,
            "board_state": "FOCUS", "follow_lane": "FOLLOW",
            "supported_line": 2.5,
            "carrier": "STRONG", "carrier_self_fund": True,
            "route_reliability": "MEDIUM", "failure_resistance": "MEDIUM",
            "burden_protection": "MEDIUM", "burden_completion_quality": "MEDIUM",
            "continuation_quality": "MEDIUM", "burden_stall_risk": "MEDIUM",
        }
        got = review_goal_burden_shadow(row)
        self.assertIn("CARRIER_G3_MULTI_MEDIUM_CONTROL", got["flags"])
        self.assertFalse(got["production_authority"])
        self.assertEqual(row["board_state"], "FOCUS")
        self.assertEqual(row["follow_lane"], "FOLLOW")

    def test_g4_medium_tail_continuation_warning_does_not_change_cert(self):
        row = {
            "match_id": "al-ahli", "goal3_funded": True,
            "goal4_funded": True, "supported_line": 3.5,
            "upper_tail_transferability": "MEDIUM",
            "continuation_quality": "MEDIUM",
        }
        got = review_goal_burden_shadow(row)
        self.assertIn("G4_MEDIUM_TRANSFER_REQUIRES_INDEPENDENT_CONTINUATION", got["flags"])
        self.assertIn("G4_CONTINUATION_NOT_STRONG", got["flags"])
        self.assertEqual(row["supported_line"], 3.5)

    def test_unfunded_early_review_not_auto_pass(self):
        got = review_goal_burden_shadow({
            "match_id": "neftchi", "goal3_funded": False,
            "board_state": "WATCH",
        })
        self.assertEqual(got["flags"], [])
        self.assertFalse(got["production_authority"])


if __name__ == "__main__":
    unittest.main()
