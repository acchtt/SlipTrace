"""V4 opt-in goal-route research checkpoint, with historical policy compatibility."""
import unittest

from test_stage import NOW, fixture, snapshot, model_input, rank, sweep
from goal_route_proof import POLICY


def proved_goal_route():
    def fact(fid):
        return {
            "fact_id": fid,
            "basis": "Dated separately attested matchup-specific football observation " + fid,
            "evidence_refs": ["https://example.org/official/" + fid],
            "observed_at_utc": "2026-10-11T15:45:00Z",
        }
    return {
        "version": POLICY,
        "facts": [fact(fid) for fid in ("carrier", "service", "reply", "stop", "fourth", "failure")],
        "goal3_primary": {
            "status": "SUPPORTED", "fact_ids": ["carrier", "service"],
            "basis": "Existing team supply supports a current repeatable goal three.",
        },
        "goal3_reply": {
            "status": "SUPPORTED", "fact_ids": ["reply"],
            "basis": "The opposing side has a distinct and current reply path.",
        },
        "two_goal_endpoint": {
            "status": "CONTROL_RISK_MATERIAL", "fact_ids": ["stop"],
            "basis": "Two-goal control and finish variance could stop the match.",
        },
        "fourth_goal_after_three": {
            "status": "SUPPORTED", "fact_ids": ["fourth"],
            "basis": "Independent fourth-goal continuation is documented.",
        },
        "main_failure": {
            "status": "ASSESSED", "fact_ids": ["failure"],
            "basis": "Specific matchup counterevidence is documented.",
        },
        "grade_fact_links": {
            "route_reliability": ["carrier", "service"],
            "chance_quality": ["service"],
            "failure_resistance": ["failure", "stop"],
            "burden_completion_quality": ["carrier", "fourth"],
            "continuation_quality": ["fourth", "reply"],
        },
    }


class GoalRouteRankBoundaryTests(unittest.TestCase):
    def test_missing_prospective_proof_is_checkpointed_not_pass(self):
        src = sweep(snapshot(), now=NOW)
        c = model_input()
        c["goal_route_proof_contract"] = POLICY
        out = rank(src, c, {"m2": "RESEARCH_EVIDENCE_MISSING"},
                   now="2026-10-11T16:05:00Z")
        self.assertEqual(out["status"], "V4_RANK_RESEARCH_PENDING")
        self.assertEqual(out["assessed_count"], 0)
        self.assertEqual(out["unranked_reasons"]["m1"], "RESEARCH_EVIDENCE_MISSING")
        self.assertEqual(out["goal_route_incomplete_match_ids"], ["m1"])
        self.assertEqual(out["goal_route_proof_reviews"]["m1"]["status"], "INCOMPLETE")
        self.assertTrue(any(
            row["research_status"] == "GOAL_ROUTE_PROOF_PENDING"
            for row in out["resume_queue"]
        ))
        self.assertFalse(out["publication_authorized"])

    def test_valid_current_distinct_proof_can_pass_checkpoint(self):
        src = sweep(snapshot(), now=NOW)
        c = model_input()
        c["goal_route_proof_contract"] = POLICY
        c["matches"][0]["goal_route_proof"] = proved_goal_route()
        out = rank(src, c, {"m2": "RESEARCH_EVIDENCE_MISSING"},
                   now="2026-10-11T16:05:00Z")
        self.assertEqual(out["goal_route_incomplete_match_ids"], [])
        self.assertEqual(out["goal_route_proof_reviews"]["m1"]["status"], "COMPLETE")
        self.assertEqual(out["assessed_count"], 1)
        self.assertEqual(out["goal_route_proof_policy"], POLICY)

    def test_legacy_frozen_input_unchanged(self):
        src = sweep(snapshot(), now=NOW)
        out = rank(src, model_input(), {"m2": "RESEARCH_EVIDENCE_MISSING"},
                   now="2026-10-11T16:05:00Z")
        self.assertEqual(out["assessed_count"], 1)
        self.assertEqual(out["goal_route_proof_policy"], "LEGACY_FROZEN_COMPATIBILITY")
        self.assertEqual(out["goal_route_incomplete_match_ids"], [])

    def test_unknown_contract_is_rejected(self):
        src = sweep(snapshot(), now=NOW)
        c = model_input()
        c["goal_route_proof_contract"] = "WEAKENING_UNAUTHORIZED_V2"
        with self.assertRaisesRegex(Exception, "UNKNOWN_GOAL_ROUTE_PROOF_CONTRACT"):
            rank(src, c, {"m2": "RESEARCH_EVIDENCE_MISSING"},
                 now="2026-10-11T16:05:00Z")


if __name__ == "__main__":
    unittest.main()
