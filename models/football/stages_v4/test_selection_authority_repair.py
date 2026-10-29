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

    def test_prospective_negative_screens_enter_bounded_deprioritized_research(self):
        source_rows = []
        ledger = []
        provisional = []
        for i in range(15):
            mid = f"secondary-{i:02d}"
            source_rows.append({
                "match_id": mid,
                "competition_kind": "DOMESTIC_LEAGUE",
                "researchability_status": "VERIFIED",
            })
            ledger.append({
                "match_id": mid,
                "country": "Test",
                "competition": "Test League",
                "home": f"H{i}",
                "away": f"A{i}",
                "kickoff_utc": f"2026-10-29T{i % 10:02d}:00:00+00:00",
                "source_url": "https://example.com/fixture",
                "registry_lane": "ROUTINE",
                "intake_lane": "ROUTINE",
                "discovery_screen": self._screen(i),
            })
            provisional.append({
                "match_id": mid,
                "kickoff_utc": f"2026-10-29T{i % 10:02d}:00:00+00:00",
            })

        result = select(
            run_id="secondary-repair-test",
            at_utc="2026-10-29T02:00:00+00:00",
            source_hash="frozen-source",
            source_rows=source_rows,
            ledger=ledger,
            provisional_queue=provisional,
            apply_cheap_filters=False,
        )

        self.assertEqual(result["deprioritized_research_capacity"], 12)
        self.assertEqual(result["deprioritized_research_count"], 12)
        self.assertEqual(len(result["eligible_queue"]), 12)
        self.assertTrue(all(
            row["intake_lane"] == "DEPRIORITIZED_RESEARCH"
            and row["deprioritized_research_certificate_authority"] is False
            and row["deprioritized_research_rank_permission"] is True
            for row in result["eligible_queue"]
        ))
        self.assertEqual(result["control_review_count"], 3)

    def test_frozen_false_negative_controls_receive_research_permission_only(self):
        controls = [
            (
                "1799027", "Puebla", "Monterrey", "DISCOVERY",
                {**self._screen(7), "priority_score": 41, "carrier_route": 1.4,
                 "second_route": 1.3, "mean_over_two_rate": 0.4,
                 "mean_over_three_rate": 0.3,
                 "mean_0_0_or_1_1_rate": 0.25},
            ),
            (
                "1873639", "Gamba Osaka", "Buriram United", "CONDITIONAL",
                {**self._screen(1), "priority_score": 47, "carrier_route": 1.4625,
                 "second_route": 1.45, "mean_over_two_rate": 0.4875,
                 "mean_over_three_rate": 0.4375,
                 "mean_0_0_or_1_1_rate": 0.125},
            ),
        ]
        source_rows = []
        ledger = []
        provisional = []
        for mid, home, away, lane, screen in controls:
            source_rows.append({
                "match_id": mid,
                "competition_kind": "DOMESTIC_LEAGUE",
                "researchability_status": "VERIFIED",
            })
            ledger.append({
                "match_id": mid, "country": "Control",
                "competition": "Control Competition", "home": home, "away": away,
                "kickoff_utc": "2026-10-29T10:00:00+00:00",
                "source_url": "https://example.com/control", "registry_lane": lane,
                "intake_lane": lane, "discovery_screen": screen,
            })
            provisional.append({
                "match_id": mid, "kickoff_utc": "2026-10-29T10:00:00+00:00",
            })

        result = select(
            run_id="frozen-false-negative-controls",
            at_utc="2026-10-29T02:00:00+00:00",
            source_hash="frozen-control-source",
            source_rows=source_rows,
            ledger=ledger,
            provisional_queue=provisional,
            apply_cheap_filters=False,
        )
        by_id = {row["match_id"]: row for row in result["eligible_queue"]}
        self.assertEqual(set(by_id), {"1799027", "1873639"})
        self.assertTrue(all(
            row["intake_lane"] == "DEPRIORITIZED_RESEARCH"
            and row["deprioritized_research_certificate_authority"] is False
            for row in by_id.values()
        ))


if __name__ == "__main__":
    unittest.main()
