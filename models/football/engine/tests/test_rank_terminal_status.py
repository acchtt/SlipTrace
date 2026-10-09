import pathlib
import sys
import unittest

ENGINE_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE_DIR))

from rank_terminal_status import RankTerminalStatusError, rank_terminal_status  # noqa: E402


class RankTerminalStatusTests(unittest.TestCase):
    def test_empty_ranked_universe_with_hold_is_complete_not_blocked(self):
        out = rank_terminal_status({
            "ranked_eligible_count": 0,
            "quarantine_count": 1,
            "follow_count": 0,
            "reserve_count": 0,
            "stop_count": 0,
            "remaining_prematch_deferred_count": 0,
            "board_integrity_failure": False,
            "integrity_failure_reason": "",
        })
        self.assertEqual(out["code"], "COMPLETE_EMPTY_RANKED_UNIVERSE")
        self.assertFalse(out["blocked"])

    def test_zero_follow_ranked_board_is_complete(self):
        out = rank_terminal_status({
            "ranked_eligible_count": 4,
            "quarantine_count": 0,
            "follow_count": 0,
            "reserve_count": 1,
            "stop_count": 3,
            "remaining_prematch_deferred_count": 0,
            "board_integrity_failure": False,
            "integrity_failure_reason": "",
        })
        self.assertEqual(out["code"], "COMPLETE_ZERO_FOLLOW")
        self.assertTrue(out["complete"])

    def test_hold_with_deferred_queue_requires_replenishment(self):
        out = rank_terminal_status({
            "ranked_eligible_count": 0,
            "quarantine_count": 1,
            "follow_count": 0,
            "reserve_count": 0,
            "stop_count": 0,
            "remaining_prematch_deferred_count": 3,
            "board_integrity_failure": False,
            "integrity_failure_reason": "",
        })
        self.assertEqual(out["code"], "REPLENISHMENT_REQUIRED")
        self.assertTrue(out["replenishment_required"])

    def test_integrity_failure_is_blocked(self):
        out = rank_terminal_status({
            "ranked_eligible_count": 0,
            "quarantine_count": 0,
            "follow_count": 0,
            "reserve_count": 0,
            "stop_count": 0,
            "remaining_prematch_deferred_count": 0,
            "board_integrity_failure": True,
            "integrity_failure_reason": "HANDOFF INCOMPLETE",
        })
        self.assertEqual(out["code"], "BLOCKED_INTEGRITY")
        self.assertTrue(out["blocked"])

    def test_compact_time_budget_exhaustion_is_a_valid_terminal_state(self):
        p = {
            "ranked_eligible_count": 12,
            "quarantine_count": 0,
            "follow_count": 0,
            "reserve_count": 2,
            "stop_count": 10,
            "remaining_prematch_deferred_count": 9,
            "board_integrity_failure": False,
            "integrity_failure_reason": "",
            "budget_policy": "COMPACT_GOAL_ROUTE_V1",
            "capacity_replenishment_status": "COMPACT_RESEARCH_BUDGET_EXHAUSTED",
            "research_budget_remaining": 0,
        }
        status = rank_terminal_status(p)
        self.assertTrue(status["complete"])
        self.assertFalse(status["replenishment_required"])

    def test_compact_four_active_finishes_with_deferred_rows(self):
        p = {
            "ranked_eligible_count": 8,
            "quarantine_count": 0,
            "follow_count": 2,
            "reserve_count": 2,
            "stop_count": 4,
            "remaining_prematch_deferred_count": 14,
            "board_integrity_failure": False,
            "integrity_failure_reason": "",
            "budget_policy": "COMPACT_GOAL_ROUTE_V1",
            "capacity_replenishment_status": "COMPACT_ACTIVE_TARGET_SATISFIED",
            "research_budget_remaining": 4,
        }
        status = rank_terminal_status(p)
        self.assertTrue(status["complete"])

    def test_compact_wave_required_until_approved_budget_consumed(self):
        p = {
            "ranked_eligible_count": 8,
            "quarantine_count": 0,
            "follow_count": 0,
            "reserve_count": 1,
            "stop_count": 7,
            "remaining_prematch_deferred_count": 11,
            "board_integrity_failure": False,
            "integrity_failure_reason": "",
            "budget_policy": "COMPACT_GOAL_ROUTE_V1",
            "capacity_replenishment_status": "REPLENISHMENT_REQUIRED",
            "research_budget_remaining": 4,
        }
        self.assertEqual(rank_terminal_status(p)["code"], "REPLENISHMENT_REQUIRED")

    def test_compact_terminal_cannot_claim_budget_exhaustion_with_remaining_time(self):
        p = {
            "ranked_eligible_count": 8,
            "quarantine_count": 0,
            "follow_count": 0,
            "reserve_count": 1,
            "stop_count": 7,
            "remaining_prematch_deferred_count": 10,
            "board_integrity_failure": False,
            "integrity_failure_reason": "",
            "budget_policy": "COMPACT_GOAL_ROUTE_V1",
            "capacity_replenishment_status": "COMPACT_RESEARCH_BUDGET_EXHAUSTED",
            "research_budget_remaining": 4,
        }
        with self.assertRaisesRegex(RankTerminalStatusError, "0 remaining budget"):
            rank_terminal_status(p)

    def test_compact_status_must_be_provided_and_consistent(self):
        p = {
            "ranked_eligible_count": 8,
            "quarantine_count": 0,
            "follow_count": 0,
            "reserve_count": 1,
            "stop_count": 7,
            "remaining_prematch_deferred_count": 10,
            "board_integrity_failure": False,
            "integrity_failure_reason": "",
            "budget_policy": "COMPACT_GOAL_ROUTE_V1",
            "research_budget_remaining": 4,
        }
        with self.assertRaisesRegex(RankTerminalStatusError, "capacity_replenishment_status"):
            rank_terminal_status(p)
        p["capacity_replenishment_status"] = "COMPACT_ACTIVE_TARGET_SATISFIED"
        with self.assertRaisesRegex(RankTerminalStatusError, "4 active"):
            rank_terminal_status(p)

    def test_ranked_count_must_reconcile(self):
        with self.assertRaises(RankTerminalStatusError):
            rank_terminal_status({
                "ranked_eligible_count": 2,
                "quarantine_count": 0,
                "follow_count": 0,
                "reserve_count": 0,
                "stop_count": 1,
                "remaining_prematch_deferred_count": 0,
                "board_integrity_failure": False,
                "integrity_failure_reason": "",
            })


if __name__ == "__main__":
    unittest.main()
