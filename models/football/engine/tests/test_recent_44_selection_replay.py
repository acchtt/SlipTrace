import json
import pathlib
import sys
import unittest

QA = pathlib.Path(__file__).resolve().parents[2] / "qa"
sys.path.insert(0, str(QA))

from replay_recent_44_selection import replay  # noqa: E402


class Recent44SelectionReplayTests(unittest.TestCase):
    def test_same_information_recent_44_replay(self):
        result = replay()
        self.assertEqual(result["source_fixture_count"], 44)
        self.assertTrue(result["same_information_replay"])
        self.assertFalse(result["outcome_fields_read"])
        self.assertGreater(result["assessment_batch_count"], 1)
        summary = {
            "source_fixture_count": result["source_fixture_count"],
            "assessment_batch_count": result["assessment_batch_count"],
            "original_state_distribution": result["original_state_distribution"],
            "new_compiled_state_distribution": result["new_compiled_state_distribution"],
            "new_lane_distribution": result["new_lane_distribution"],
            "state_change_count": result["state_change_count"],
            "rank_movement_count": result["rank_movement_count"],
            "review_challenger_count": result["review_challenger_count"],
            "dominated_focus_count": result["dominated_focus_count"],
            "state_changes": result["state_changes"],
            "rank_movements": result["rank_movements"],
            "review_challengers": result["review_challengers"],
            "dominated_focus": result["dominated_focus"],
        }
        print("RECENT44_REPLAY_SUMMARY=" + json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    unittest.main()
