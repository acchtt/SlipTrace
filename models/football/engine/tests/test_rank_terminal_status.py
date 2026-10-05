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
