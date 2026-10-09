import copy
import json
import pathlib
import sys
import unittest

ENGINE_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE_DIR))

from step2_reconcile import (  # noqa: E402
    Step2ReconciliationError,
    reconcile_step2,
)


def persisted_snapshot(**overrides):
    row = {
        "match_id": "follow-1",
        "record_id": "rec12345678901234",
        "engine_execution_status": "EXECUTED_C_C2_PAIR",
        "engine_source_revision": "a" * 40,
        "c_action": "C-WAIT",
        "c2_shadow_action": "C2-PASS — SHADOW",
        "c_supported_line": 2.5,
        "c2_supported_line": 2.25,
        "engine_c_result": json.dumps({"action": "WAIT", "supported_line": 2.5}),
        "engine_c2_result": json.dumps({"action": "PASS", "supported_line": 2.25}),
    }
    row.update(overrides)
    return row


def payload(**overrides):
    data = {
        "schema_version": "football-step2-reconcile-v2",
        "stage": "step2_reconcile",
        "session_id": "S2-20261009-synthetic",
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
            {
                "match_id": "follow-1",
                "status": "DECISION_STATE_PERSISTED",
                "decision_state_snapshot": persisted_snapshot(),
            },
            {
                "match_id": "reserve-1",
                "status": "WAITING_FOR_USER_XI_ODDS",
                "blocker_reason": "Quote not supplied for frozen XI epoch",
            },
            {
                "match_id": "exception-1",
                "status": "LIVE_REROUTED",
                "live_handoff_reference": "LIVE-EXCEPTION-20261009-synthetic",
            },
        ],
    }
    data.update(overrides)
    return data


class Step2ReconciliationTests(unittest.TestCase):
    def test_every_due_fixture_is_accounted_with_attestation(self):
        result = reconcile_step2(payload())
        self.assertTrue(result["all_due_accounted"])
        self.assertEqual(result["due_count"], 3)
        self.assertEqual(result["persisted_decision_count"], 1)
        self.assertEqual(result["verified_decision_count"], 1)
        self.assertEqual(result["decision_state_attestations"][0]["record_id"], "rec12345678901234")

    def test_missing_follow_is_hard_failure(self):
        row = payload()
        row["outcomes"] = row["outcomes"][1:]
        with self.assertRaisesRegex(Step2ReconciliationError, "SILENT OMISSION: follow-1"):
            reconcile_step2(row)

    def test_outcome_without_authorization_is_hard_failure(self):
        row = payload()
        row["outcomes"].append({
            "match_id": "ghost",
            "status": "INTEGRITY_BLOCKED",
            "blocker_reason": "Synthetic ghost not authorized",
        })
        with self.assertRaisesRegex(Step2ReconciliationError, "OUTCOME WITHOUT AUTHORIZATION: ghost"):
            reconcile_step2(row)

    def test_routine_follow_requires_follow_lane(self):
        row = payload()
        row["due"][0]["official_follow_lane"] = "STOP"
        with self.assertRaisesRegex(Step2ReconciliationError, "ROUTINE_FOLLOW REQUIRES FOLLOW"):
            reconcile_step2(row)

    def test_stop_requires_user_exception(self):
        row = payload()
        row["due"][2]["step2_authorization"] = "ROUTINE_FOLLOW"
        with self.assertRaisesRegex(Step2ReconciliationError, "ROUTINE_FOLLOW REQUIRES FOLLOW"):
            reconcile_step2(row)

    def test_duplicate_outcome_is_blocked(self):
        row = payload()
        row["outcomes"].append({
            "match_id": "follow-1",
            "status": "INTEGRITY_BLOCKED",
            "blocker_reason": "Duplicate",
        })
        with self.assertRaisesRegex(Step2ReconciliationError, "DUPLICATE OUTCOME"):
            reconcile_step2(row)

    def test_persisted_requires_snapshot(self):
        row = payload()
        row["outcomes"][0].pop("decision_state_snapshot")
        with self.assertRaisesRegex(Step2ReconciliationError, "decision_state_snapshot"):
            reconcile_step2(row)

    def test_persisted_rejects_incomplete_engine_status(self):
        row = payload()
        row["outcomes"][0]["decision_state_snapshot"]["engine_execution_status"] = "NOT_RUN_INPUT_INCOMPLETE"
        with self.assertRaisesRegex(Step2ReconciliationError, "pair not executed"):
            reconcile_step2(row)

    def test_persisted_rejects_missing_c2_result(self):
        row = payload()
        row["outcomes"][0]["decision_state_snapshot"].pop("engine_c2_result")
        with self.assertRaisesRegex(Step2ReconciliationError, "engine_c2_result"):
            reconcile_step2(row)

    def test_persisted_rejects_incomplete_c2_action(self):
        row = payload()
        row["outcomes"][0]["decision_state_snapshot"]["c2_shadow_action"] = "C2-INCOMPLETE"
        with self.assertRaisesRegex(Step2ReconciliationError, "invalid C2 shadow action"):
            reconcile_step2(row)

    def test_persisted_rejects_engine_action_mismatch(self):
        row = payload()
        row["outcomes"][0]["decision_state_snapshot"]["engine_c_result"] = json.dumps({
            "action": "BET", "supported_line": 2.5
        })
        with self.assertRaisesRegex(Step2ReconciliationError, "engine_c_result.action"):
            reconcile_step2(row)

    def test_persisted_rejects_engine_line_mismatch(self):
        row = payload()
        row["outcomes"][0]["decision_state_snapshot"]["engine_c2_result"] = {
            "action": "PASS", "supported_line": 2.5
        }
        with self.assertRaisesRegex(Step2ReconciliationError, "engine_c2_result.supported_line"):
            reconcile_step2(row)

    def test_persisted_rejects_invalid_airtable_reference(self):
        row = payload()
        row["outcomes"][0]["decision_state_snapshot"]["record_id"] = "guessed"
        with self.assertRaisesRegex(Step2ReconciliationError, "RECORD ID INVALID"):
            reconcile_step2(row)

    def test_blocked_outcome_requires_reason(self):
        row = payload()
        row["outcomes"][1].pop("blocker_reason")
        with self.assertRaisesRegex(Step2ReconciliationError, "blocker_reason"):
            reconcile_step2(row)

    def test_live_reroute_requires_handoff(self):
        row = payload()
        row["outcomes"][2].pop("live_handoff_reference")
        with self.assertRaisesRegex(Step2ReconciliationError, "live_handoff_reference"):
            reconcile_step2(row)

    def test_engine_failure_requires_exact_failure_reason(self):
        row = payload()
        row["outcomes"][1] = {
            "match_id": "reserve-1",
            "status": "ENGINE_FAILED_AFTER_ATTEMPT",
            "blocker_reason": "Runtime attempted but failed",
        }
        with self.assertRaisesRegex(Step2ReconciliationError, "engine_failure_reason"):
            reconcile_step2(row)

    def test_v1_cannot_satisfy_current_session(self):
        row = payload(schema_version="football-step2-reconcile-v1")
        with self.assertRaisesRegex(Step2ReconciliationError, "historical_replay=true"):
            reconcile_step2(row)

    def test_v1_historical_replay_is_explicit_and_not_attested(self):
        row = payload(
            schema_version="football-step2-reconcile-v1",
            historical_replay=True,
        )
        row["outcomes"][0].pop("decision_state_snapshot")
        row["outcomes"][1].pop("blocker_reason")
        row["outcomes"][2].pop("live_handoff_reference")
        result = reconcile_step2(row)
        self.assertEqual(result["schema_version"], "football-step2-reconcile-v1")
        self.assertEqual(result["verified_decision_count"], 0)


if __name__ == "__main__":
    unittest.main()
