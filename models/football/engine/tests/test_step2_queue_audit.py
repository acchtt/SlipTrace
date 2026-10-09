import copy
import pathlib
import sys
import unittest

ENGINE_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE_DIR))

from step2_queue_guard import freeze_queue  # noqa: E402
from step2_queue_audit import Step2QueueAuditError, audit_queue_outcomes  # noqa: E402
from test_step2_queue_guard import payload as queue_payload  # noqa: E402
from test_step2_reconcile import persisted_snapshot  # noqa: E402


def audit_fixture():
    receipt = freeze_queue(queue_payload())
    outcomes = []
    for row in receipt["due"]:
        match_id = row["match_id"]
        if match_id == "follow-open":
            outcomes.append({
                "match_id": match_id,
                "status": "DECISION_STATE_PERSISTED",
                "decision_state_snapshot": persisted_snapshot(match_id=match_id),
            })
        elif match_id == "reserve-activated":
            outcomes.append({
                "match_id": match_id,
                "status": "WAITING_FOR_USER_XI_ODDS",
                "blocker_reason": "Activated reserve, XI decision window not yet open",
            })
        else:
            outcomes.append({
                "match_id": match_id,
                "status": "LIVE_REROUTED",
                "live_handoff_reference": "LIVE-EXCEPTION-SYNTHETIC-" + match_id,
            })
    return {
        "schema_version": "football-step2-queue-audit-v1",
        "queue_receipt": receipt,
        "reconciliation_input": {
            "schema_version": "football-step2-reconcile-v2",
            "stage": "step2_reconcile",
            "session_id": receipt["session_id"],
            "due": [
                {
                    "match_id": r["match_id"],
                    "official_follow_lane": r["official_follow_lane"],
                    "step2_authorization": r["step2_authorization"],
                }
                for r in receipt["due"]
            ],
            "outcomes": outcomes,
        },
    }


class Step2QueueAuditTests(unittest.TestCase):
    def test_accounted_outcomes_with_open_items_are_not_completed(self):
        result = audit_queue_outcomes(audit_fixture())
        self.assertTrue(result["all_due_accounted"])
        self.assertFalse(result["all_due_completed"])
        self.assertEqual(result["verified_decision_count"], 1)
        self.assertEqual(result["open_follow_up_count"], 3)
        self.assertEqual(result["status"], "STEP2 ACCOUNTED WITH OPEN FOLLOW_UPS")
        self.assertIn("VERIFY_LIVE_HANDOFF_AND_LIVE_DECISION_STATUS", {r["follow_up"] for r in result["open_follow_ups"]})

    def test_silent_drop_from_reconciliation_due_is_rejected(self):
        data = audit_fixture()
        data["reconciliation_input"]["due"].pop()
        with self.assertRaisesRegex(Step2QueueAuditError, "DUE FIXTURE DROPPED"):
            audit_queue_outcomes(data)

    def test_missing_outcome_is_rejected(self):
        data = audit_fixture()
        data["reconciliation_input"]["outcomes"].pop()
        with self.assertRaisesRegex(Step2QueueAuditError, "STEP2 OUTCOME COVERAGE MISMATCH"):
            audit_queue_outcomes(data)

    def test_lane_drift_is_rejected(self):
        data = audit_fixture()
        data["reconciliation_input"]["due"][0]["official_follow_lane"] = "FOLLOW"
        with self.assertRaisesRegex(Step2QueueAuditError, "FROZEN AUTHORITY DRIFT"):
            audit_queue_outcomes(data)

    def test_bad_c2_result_not_marked_completed(self):
        data = audit_fixture()
        persisted = next(x for x in data["reconciliation_input"]["outcomes"] if x["status"] == "DECISION_STATE_PERSISTED")
        persisted["decision_state_snapshot"].pop("engine_c2_result")
        with self.assertRaisesRegex(Step2QueueAuditError, "engine_c2_result"):
            audit_queue_outcomes(data)

    def test_v1_historical_replay_cannot_complete_current_session(self):
        data = audit_fixture()
        data["reconciliation_input"]["schema_version"] = "football-step2-reconcile-v1"
        data["reconciliation_input"]["historical_replay"] = True
        with self.assertRaisesRegex(Step2QueueAuditError, "requires v2 reconciliation"):
            audit_queue_outcomes(data)

    def test_exception_only_can_account_without_completed_board(self):
        q = queue_payload()
        q.update(mode="EXCEPTION_ONLY", board=[], activated_reserves=[])
        data = audit_fixture()
        receipt = freeze_queue(q)
        data["queue_receipt"] = receipt
        data["reconciliation_input"]["due"] = [
            {"match_id": x["match_id"], "official_follow_lane": "STOP", "step2_authorization": "USER_EXCEPTION"}
            for x in receipt["due"]
        ]
        data["reconciliation_input"]["outcomes"] = [
            {"match_id": x["match_id"], "status": "INTEGRITY_BLOCKED", "blocker_reason": "No independent C2 burden at current epoch"}
            for x in receipt["due"]
        ]
        result = audit_queue_outcomes(data)
        self.assertEqual(result["due_count"], 2)
        self.assertEqual(result["open_follow_up_count"], 2)
        self.assertFalse(result["all_due_completed"])


if __name__ == "__main__":
    unittest.main()
