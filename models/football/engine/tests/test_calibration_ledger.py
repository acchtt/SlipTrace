import pathlib
import sys
import unittest

ENGINE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE))

from calibration_ledger import (  # noqa: E402
    asian_over_settlement,
    audit_metrics,
    board_records,
    settle,
    sweep_records,
    with_quote_decision,
    xi_record,
)


class CalibrationLedgerTests(unittest.TestCase):
    def test_sweep_records_every_fixture_without_hindsight(self):
        receipt = {
            "run_id": "V4-test",
            "source_ledger": [
                {
                    "match_id": "priority",
                    "intake_lane": "GOAL_PRIORITY",
                    "goal_screen": {"status": "DISCOVERY_GOAL_QUALIFIED"},
                },
                {
                    "match_id": "control",
                    "intake_lane": "CONTROL_REVIEW",
                    "goal_screen": {"status": "WATCH_GOAL_SIGNAL"},
                },
                {
                    "match_id": "screened",
                    "intake_lane": "WATCH_GOAL_SIGNAL",
                    "goal_screen": {"status": "WATCH_GOAL_SIGNAL"},
                },
            ],
        }
        rows = sweep_records(receipt)
        self.assertEqual(len(rows), 3)
        self.assertEqual([r["decision"] for r in rows], [
            "REVIEW_ONLY", "REVIEW_ONLY", "SCREENED_OUT"
        ])
        self.assertTrue(rows[1]["control_review"])
        self.assertTrue(all("settlement" not in row for row in rows))
        self.assertTrue(all(row["selection_authority"] == "ZERO" for row in rows))

    def test_settlement_is_append_only_and_metrics_use_universal_denominator(self):
        base = sweep_records({
            "run_id": "V4-test",
            "source_ledger": [{
                "match_id": "act",
                "intake_lane": "GOAL_PRIORITY",
                "goal_screen": {"status": "DISCOVERY_GOAL_QUALIFIED"},
            }],
        })[0]
        decided = with_quote_decision(
            base,
            visible_ladder=[{"line": 2.5, "odds": 1.7}],
            selected_line=2.5,
            selected_odds=1.7,
            decision="ACT",
        )
        settled = settle(
            decided, home_goals=2, away_goals=1,
            settled_at_utc="2026-10-24T12:00:00Z",
        )
        self.assertNotIn("settlement", decided)
        self.assertEqual(settled["settlement"]["act_settlement"], "WIN")
        metrics = audit_metrics([settled])
        self.assertEqual(metrics["execution"]["act_count"], 1)
        self.assertEqual(metrics["execution"]["act_clear_rate"], 1.0)
        self.assertEqual(metrics["screening"]["goal_priority_count"], 1)

    def test_asian_quarter_settlement(self):
        self.assertEqual(asian_over_settlement(3, 2.75), "HALF_WIN")
        self.assertEqual(asian_over_settlement(3, 3.25), "HALF_LOSS")
        self.assertEqual(asian_over_settlement(3, 3.0), "PUSH")

    def test_decision_result_populates_calibration_without_live_context(self):
        row = xi_record(
            {
                "evidence_epoch_id": "epoch-1",
                "context": {"official_follow_lane": "FOLLOW"},
            },
            {
                "match_id": "m1",
                "rank_state_internal": "FOCUS",
                "declared_board_state": "WATCH",
                "goal3_funded": True,
                "goal4_funded": False,
                "goal5_funded": False,
                "goal6_funded": False,
                "supported_line": 2.5,
                "execution_strength": "CONDITIONAL",
                "g3_endpoint_control_pressure": "MODERATE",
                "upper_tail_control_pressure": "HIGH",
                "direct_act_ceiling": 2.5,
            },
            {
                "action": "ACT",
                "visible_ladder": [{"line": 2.5, "odds": 1.7}],
                "selected_visible_line": 2.5,
                "selected_visible_odds": 1.7,
            },
        )
        self.assertEqual(row["certified_burden"], 2.5)
        self.assertEqual(row["robustness"], "CONDITIONAL")
        self.assertEqual(row["decision"], "ACT")
        self.assertEqual(row["screenshot_visible_ladder"], [{"line": 2.5, "odds": 1.7}])

    def test_board_record_uses_compiled_execution_strength_as_robustness(self):
        rows = board_records(
            {
                "matches": [{
                    "match_id": "m1",
                    "board_state": "FOCUS",
                    "declared_board_state": "WATCH",
                    "execution_strength": "ROBUST",
                    "supported_line": 2.5,
                }],
            },
            evidence_epoch="epoch-1",
        )
        self.assertEqual(rows[0]["robustness"], "ROBUST")
        self.assertEqual(rows[0]["compiled_board_state"], "FOCUS")
        self.assertEqual(rows[0]["researcher_declared_board_state"], "WATCH")


if __name__ == "__main__":
    unittest.main()
