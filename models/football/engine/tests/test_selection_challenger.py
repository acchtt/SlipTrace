"""Regression tests for selection SHADOW; production stays authoritative."""
import unittest

from test_adapter import match
from adapter import run_board
from selection_challenger import entry_readiness, shadow_follow_allocation, grade_provenance_dependency


def board(rows, **kwargs):
    return run_board({
        "schema_version": "football-engine-v1",
        "stage": "board",
        "model": "c",
        "matches": rows,
        **kwargs,
    })


class CoordinatedSelectionChallengerTests(unittest.TestCase):
    def test_repeated_grade_sources_are_flagged_not_counted_independently(self):
        reused = {
            "grade_evidence": {
                key: {"basis": f"{key}: generic same scoreline history", "evidence_refs": [
                    "https://source.example/team-1",
                    "https://source.example/team-2",
                ]}
                for key in (
                    "route_reliability", "chance_quality", "failure_resistance",
                    "burden_completion_quality", "continuation_quality"
                )
            }
        }
        result = grade_provenance_dependency(reused)
        self.assertEqual(result["status"], "REPEATED_SOURCE_SET")
        self.assertEqual(result["assessed_grade_dimensions"], 5)
        self.assertEqual(result["distinct_reference_sets"], 1)
        self.assertEqual(result["shared_reference_count"], 2)
        self.assertEqual(grade_provenance_dependency({})["status"], "UNKNOWN_LEGACY")

    def test_entry_access_is_not_inferred_from_final_score_or_missing_clock(self):
        self.assertEqual(entry_readiness("2026-10-26T18:00:00+07:00", None)["entry_state"], "UNKNOWN")
        self.assertEqual(entry_readiness(
            "2026-10-26T18:00:00+07:00",
            "2026-10-26T17:54:00+07:00"
        )["entry_state"], "CRITICAL")
        self.assertEqual(entry_readiness(
            "2026-10-26T18:00:00+07:00",
            "2026-10-26T16:00:00+07:00"
        )["entry_state"], "RESEARCH_LEAD_READY")
        self.assertEqual(entry_readiness(
            "2026-10-26T18:00:00+07:00",
            "2026-10-26T18:20:00+07:00"
        )["entry_state"], "CLOSED")

    def test_stacked_moderate_warnings_lower_shadow_tier_without_removing_g3(self):
        high = match(
            match_id="current-reliable",
            board_state="C-FOCUS",
            carrier="STRONG",
            carrier_self_fund=True,
            independent_upper_tail=False,
            home_route="STRONG",
            away_route="USABLE",
            kickoff_ict="2026-10-26T18:00:00+07:00",
        )
        medium = match(
            match_id="carrier-all-medium",
            board_state="C-FOCUS",
            carrier="STRONG",
            carrier_self_fund=True,
            independent_upper_tail=False,
            home_route="STRONG",
            away_route="WEAK",
            independent_route_quality="MEDIUM",
            route_reliability="MEDIUM",
            chance_quality="MEDIUM",
            failure_resistance="MEDIUM",
            burden_protection="MEDIUM",
            burden_completion_quality="MEDIUM",
            continuation_quality="MEDIUM",
            opponent_leakage="MEDIUM",
            burden_stall_risk="MEDIUM",
            kickoff_ict="2026-10-26T19:00:00+07:00",
        )
        original_ids = [high["match_id"], medium["match_id"]]
        result = board([high, medium], rank_at_utc="2026-10-26T15:00:00+07:00")
        out = {row["match_id"]: row for row in result["matches"]}
        self.assertEqual(set(out), set(original_ids))
        self.assertEqual(out["current-reliable"]["board_state"], "FOCUS")
        self.assertEqual(out["carrier-all-medium"]["board_state"], "FOCUS")
        self.assertEqual(out["carrier-all-medium"]["selection_challenger_tier"], "CONDITIONAL")
        self.assertEqual(out["current-reliable"]["selection_challenger_tier"], "HIGH_CONVICTION")
        self.assertGreater(
            out["current-reliable"]["selection_challenger_score"],
            out["carrier-all-medium"]["selection_challenger_score"],
        )
        self.assertIn("carrier-all-medium", original_ids)
        self.assertNotIn("carrier-all-medium", result["selection_challenger"]["shadow_follow_match_ids"])

    def test_challenger_never_changes_champion_follow_or_certificates(self):
        rows = [
            match(
                match_id="m1",
                board_state="C-FOCUS",
                carrier="STRONG", carrier_self_fund=True,
                independent_upper_tail=False,
                kickoff_ict="2026-10-26T18:00:00+07:00",
            ),
            match(
                match_id="m2",
                board_state="C-FOCUS",
                carrier="STRONG", carrier_self_fund=True,
                independent_upper_tail=False,
                kickoff_ict="2026-10-26T19:00:00+07:00",
                route_reliability="MEDIUM", chance_quality="MEDIUM",
                failure_resistance="MEDIUM",
                burden_completion_quality="MEDIUM",
                continuation_quality="MEDIUM",
                burden_stall_risk="MEDIUM",
            ),
        ]
        original = board(rows)
        timed = board(rows, rank_at_utc="2026-10-26T17:56:00+07:00")
        for old,new in zip(original["matches"],timed["matches"]):
            self.assertEqual(old["match_id"], new["match_id"])
            self.assertEqual(old["board_state"], new["board_state"])
            self.assertEqual(old["follow_lane"], new["follow_lane"])
            self.assertEqual(old["certified_supported_burden"], new["certified_supported_burden"])
        self.assertNotIn("m1", timed["selection_challenger"]["shadow_follow_match_ids"])
        self.assertEqual(timed["selection_challenger"]["shadow_does_not_authorize_execution"], True)

    def test_shadow_allocation_is_bounded_and_can_leave_slots_unfilled(self):
        rows = [{
            "match_id":f"r{i}",
            "board_state":"FOCUS",
            "operational_viability_grade":"A",
            "selection_challenger_tier":"HIGH_CONVICTION",
            "selection_challenger_score":90-i,
            "selection_challenger_entry_state":"RESEARCH_LEAD_READY",
            "follow_clearability_score":50,
            "kickoff_ict":"2026-10-26T18:00:00+07:00",
        } for i in range(9)]
        rows += [{
            "match_id":"conditional",
            "board_state":"FOCUS",
            "operational_viability_grade":"A",
            "selection_challenger_tier":"CONDITIONAL",
            "selection_challenger_score":120,
            "selection_challenger_entry_state":"RESEARCH_LEAD_READY",
            "follow_clearability_score":99,
            "kickoff_ict":"2026-10-26T18:00:00+07:00",
        }]
        selected = shadow_follow_allocation(rows)
        self.assertEqual(selected["shadow_follow_count"], 3)
        self.assertEqual(selected["shadow_capacity_unused"], 4)
        self.assertNotIn("conditional", selected["shadow_follow_match_ids"])
        self.assertTrue(all("follow_lane" not in r for r in rows))


if __name__ == "__main__":
    unittest.main()
