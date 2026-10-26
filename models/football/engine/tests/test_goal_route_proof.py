"""Unit coverage: prospective scoring evidence is not the same as reused grades."""
import unittest
from goal_route_proof import POLICY, review_goal_route_proof

RANK_AT = "2026-10-26T10:00:00+00:00"
KICKOFF = "2026-10-26T12:00:00+00:00"


def fact(fid, url=None, when="2026-10-26T08:00:00Z"):
    return {
        "fact_id": fid,
        "basis": "Specific dated independent current football observation for " + fid,
        "evidence_refs": [url or ("https://official.example/" + fid)],
        "observed_at_utc": when,
    }


def valid_row():
    return {
        "match_id": "trial-fixture",
        "carrier_self_fund": True,
        "independent_upper_tail": True,
        "goal_route_proof": {
            "version": POLICY,
            "facts": [
                fact("scorer"), fact("supplier"), fact("reply"),
                fact("stop"), fact("fourth"), fact("failure"),
            ],
            "goal3_primary": {
                "status": "SUPPORTED", "fact_ids": ["scorer", "supplier"],
                "basis": "Current carrier has multiple distinct finish and supply routes for 3.",
            },
            "goal3_reply": {
                "status": "SUPPORTED", "fact_ids": ["reply"],
                "basis": "Opposing independent reply route is currently evidenced.",
            },
            "two_goal_endpoint": {
                "status": "CONTROL_RISK_MATERIAL", "fact_ids": ["stop"],
                "basis": "Defensive control at 2-0 is a factual material counterargument.",
            },
            "fourth_goal_after_three": {
                "status": "SUPPORTED", "fact_ids": ["fourth"],
                "basis": "A separate factual post-third-goal attacking mechanism exists.",
            },
            "main_failure": {
                "status": "ASSESSED", "fact_ids": ["failure"],
                "basis": "A concrete current conversion/fatigue/incentive failure exists.",
            },
            "grade_fact_links": {
                "route_reliability": ["scorer", "supplier"],
                "chance_quality": ["supplier"],
                "failure_resistance": ["stop", "failure"],
                "burden_completion_quality": ["scorer", "fourth"],
                "continuation_quality": ["reply", "fourth"],
            },
        },
    }


def review(row):
    return review_goal_route_proof(row, rank_at_utc=RANK_AT, kickoff_utc=KICKOFF)


class GoalRouteProofTests(unittest.TestCase):
    def test_independent_current_routes_are_complete(self):
        x = review(valid_row())
        self.assertEqual(x["status"], "COMPLETE")
        self.assertEqual(x["fact_count"], 6)
        self.assertTrue(x["no_certificate_or_grade_changes"])

    def test_recycled_primary_fact_not_independent_reply(self):
        row = valid_row()
        row["goal_route_proof"]["goal3_reply"]["fact_ids"] = ["scorer"]
        x = review(row)
        self.assertEqual(x["status"], "INCOMPLETE")
        self.assertIn("goal3_reply.fact_recycled_from_primary", x["gaps"])

    def test_all_grade_boxes_point_to_same_facts(self):
        row = valid_row()
        row["goal_route_proof"]["grade_fact_links"] = {
            k: ["scorer"] for k in row["goal_route_proof"]["grade_fact_links"]
        }
        x = review(row)
        self.assertIn("grade_fact_links.all_dimensions_recycle_same_facts", x["gaps"])

    def test_fourth_goal_cannot_reuse_only_third_goal_facts(self):
        row = valid_row()
        row["goal_route_proof"]["fourth_goal_after_three"]["fact_ids"] = ["scorer"]
        x = review(row)
        self.assertIn("fourth_goal_after_three.no_additional_fact", x["gaps"])

    def test_future_observation_is_not_prospective(self):
        row = valid_row()
        row["goal_route_proof"]["facts"][0]["observed_at_utc"] = "2026-10-26T13:00:00Z"
        x = review(row)
        self.assertTrue(any("prospective_timestamp" in gap for gap in x["gaps"]))

    def test_shared_official_url_with_distinct_facts_flags_review_not_false_veto(self):
        row = valid_row()
        row["goal_route_proof"]["facts"][0]["evidence_refs"] = ["https://official.example/report"]
        row["goal_route_proof"]["facts"][2]["evidence_refs"] = ["https://official.example/report"]
        x = review(row)
        self.assertEqual(x["status"], "COMPLETE")
        self.assertTrue(any("shared_source" in text for text in x["warnings"]))

    def test_missing_proof_is_pending_not_a_negative_football_verdict(self):
        x = review_goal_route_proof(
            {"match_id": "winning-undetected", "carrier_self_fund": False},
            rank_at_utc=RANK_AT, kickoff_utc=KICKOFF,
        )
        self.assertEqual(x["status"], "INCOMPLETE")
        self.assertEqual(x["gaps"], ["goal_route_proof.missing"])

    def test_no_unsupported_upper_tail_claim_without_post_third_review(self):
        row = valid_row()
        row["goal_route_proof"]["fourth_goal_after_three"]["status"] = "NOT_APPLICABLE"
        x = review(row)
        self.assertIn("independent_upper_tail.fourth_goal_not_reviewed", x["gaps"])


if __name__ == "__main__":
    unittest.main()
