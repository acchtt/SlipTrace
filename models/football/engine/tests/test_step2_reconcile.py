import pathlib
import sys
import unittest

ENGINE_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE_DIR))

from step2_reconcile import (  # noqa: E402
    Step2ReconciliationError,
    reconcile_step2,
)


def payload(**overrides):
    data = {
        "schema_version": "football-step2-reconcile-v1",
        "stage": "step2_reconcile",
        "session_id": "S2-20261004-evening",
        "due": [
            {
                "match_id": "follow-1",
                "official_follow_lane": "FOLLOW",
                "step2_authorization": "ROUTINE_FOLLOW",
            },
            {
                "match_id": "reserve-1",
                "official_follow_lane": "RESERVE",
                "step2_authorization": "RESERVE_ACTIVATED",
            },
            {
                "match_id": "exception-1",
                "official_follow_lane": "STOP",
                "step2_authorization": "USER_EXCEPTION",
            },
        ],
        "outcomes": [
            {"match_id": "follow-1", "status": "DECISION_STATE_PERSISTED"},
            {"match_id": "reserve-1", "status": "WAITING_FOR_USER_XI_ODDS"},
            {"match_id": "exception-1", "status": "LIVE_REROUTED"},
        ],
    }
    data.update(overrides)
    return data


class Step2ReconciliationTests(unittest.TestCase):
    def test_every_due_fixture_must_be_accounted(self):
        result = reconcile_step2(payload())
        self.assertTrue(result["all_due_accounted"])
        self.assertEqual(result["due_count"], 3)
        self.assertEqual(result["persisted_decision_count"], 1)

    def test_missing_follow_is_a_hard_failure(self):
        row = payload()
        row["outcomes"] = row["outcomes"][1:]
        with self.assertRaisesRegex(
            Step2ReconciliationError,
            "SILENT OMISSION: follow-1",
        ):
            reconcile_step2(row)

    def test_outcome_without_authorization_is_a_hard_failure(self):
        row = payload()
        row["outcomes"].append(
            {"match_id": "ghost", "status": "DECISION_STATE_PERSISTED"}
        )
        with self.assertRaisesRegex(
            Step2ReconciliationError,
            "OUTCOME WITHOUT AUTHORIZATION: ghost",
        ):
            reconcile_step2(row)

    def test_routine_follow_requires_follow_lane(self):
        row = payload()
        row["due"][0]["official_follow_lane"] = "STOP"
        with self.assertRaisesRegex(
            Step2ReconciliationError,
            "ROUTINE_FOLLOW REQUIRES FOLLOW",
        ):
            reconcile_step2(row)

    def test_stop_requires_user_exception(self):
        row = payload()
        row["due"][2]["step2_authorization"] = "ROUTINE_FOLLOW"
        with self.assertRaisesRegex(
            Step2ReconciliationError,
            "ROUTINE_FOLLOW REQUIRES FOLLOW",
        ):
            reconcile_step2(row)

    def test_duplicate_outcome_is_blocked(self):
        row = payload()
        row["outcomes"].append(
            {"match_id": "follow-1", "status": "INTEGRITY_BLOCKED"}
        )
        with self.assertRaisesRegex(
            Step2ReconciliationError,
            "DUPLICATE OUTCOME",
        ):
            reconcile_step2(row)


if __name__ == "__main__":
    unittest.main()
