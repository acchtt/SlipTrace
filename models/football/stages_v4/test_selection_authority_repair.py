import pathlib
import sys
import unittest

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from goals_first_intake import select


class SelectionAuthorityRepairTests(unittest.TestCase):
    def _screen(self, i):
        return {
            "status": "WATCH_GOAL_SIGNAL",
            "reason": "GOAL_ROUTE_OR_LOW_DRAW_TRAP_SCREEN_NOT_YET_PERSUASIVE",
            "priority_score": 48 - i,
            "carrier_route": 1.9 - i * 0.05,
            "mean_over_two_rate": 0.50,
            "mean_over_three_rate": 0.30,
            "mean_0_0_or_1_1_rate": 0.20,
        }

    def test_control_review_stays_research_only_and_never_enters_eligible_queue(self):
        source_rows = []
        ledger = []
        provisional = []
        for i in range(5):
            mid = f"control-{i}"
            source_rows.append({
                "match_id": mid,
                "competition_kind": "DOMESTIC_LEAGUE",
            })
            ledger.append({
                "match_id": mid,
                "country": "Test",
                "competition": "Test League",
                "home": f"H{i}",
                "away": f"A{i}",
                "kickoff_utc": f"2026-10-26T1{i}:00:00+00:00",
                "source_url": "https://example.com/fixture",
                "registry_lane": "ROUTINE",
                "intake_lane": "ROUTINE",
                "discovery_screen": self._screen(i),
            })
            provisional.append({
                "match_id": mid,
                "kickoff_utc": f"2026-10-26T1{i}:00:00+00:00",
            })

        result = select(
            run_id="repair-test",
            at_utc="2026-10-26T02:00:00+00:00",
            source_hash="frozen-source",
            source_rows=source_rows,
            ledger=ledger,
            provisional_queue=provisional,
            apply_cheap_filters=False,
        )

        self.assertEqual(result["eligible_queue"], [])
        self.assertEqual(result["control_review_count"], 4)
        self.assertFalse(result["control_review_production_authority"])
        self.assertEqual(len(result["control_review_match_ids"]), 4)

        research_by_id = {
            row["match_id"]: row for row in result["goal_research_queue"]
        }
        controls = [
            row for row in research_by_id.values()
            if row["intake_lane"] == "CONTROL_REVIEW"
        ]
        watches = [
            row for row in research_by_id.values()
            if row["intake_lane"] == "WATCH_GOAL_SIGNAL"
        ]
        self.assertEqual(len(controls), 4)
        self.assertEqual(len(watches), 1)
        self.assertTrue(all(row["control_review_selected"] for row in controls))


if __name__ == "__main__":
    unittest.main()
