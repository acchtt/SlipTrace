import copy
import pathlib
import sys
import unittest

ENGINE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE))

from decision_pair_cli import run_pair  # noqa: E402
from step2_publication_guard import check_publication, PublicationBlocked  # noqa: E402
from test_adapter import pair_payload  # noqa: E402


def sample():
    c, c2 = pair_payload("c"), pair_payload("c2")
    for payload in (c, c2):
        payload["context"]["evidence_epoch_id"] = "current-20261009T2010"
    receipt = run_pair(c, c2)
    a, b = receipt["results"]["c"], receipt["results"]["c2"]
    snapshot = {
        "match_id": c["match"]["match_id"],
        "record_id": "rec12345678901234",
        "engine_execution_status": "EXECUTED_C_C2_PAIR",
        "engine_source_revision": "a" * 40,
        "evidence_epoch_id": "current-20261009T2010",
        "c_action": "C-" + a["action"],
        "c2_shadow_action": "C2-" + b["action"] + " — SHADOW",
        "c_supported_line": c["match"]["supported_line"],
        "c2_supported_line": c2["match"]["supported_line"],
        "engine_c_result": {**a, "supported_line": c["match"]["supported_line"]},
        "engine_c2_result": {**b, "supported_line": c2["match"]["supported_line"]},
    }
    return {
        "schema_version": "football-step2-publication-v1",
        "c_input": c,
        "c2_input": c2,
        "pair_receipt": receipt,
        "decision_state_snapshot": snapshot,
        "active_evidence_epoch_id": "current-20261009T2010",
        "latest_evidence_epoch_id": "current-20261009T2010",
        "active_engine_source_revision": "a" * 40,
        "quote_still_executable": True,
        "fixture_status_still_valid": True,
        "previously_published_keys": [],
    }


class PublicationGuardTests(unittest.TestCase):
    def test_complete_paired_readback_can_publish(self):
        row = sample()
        result = check_publication(row)
        self.assertEqual(result["status"], "STEP2 PUBLICATION ELIGIBLE")
        self.assertIn("current-20261009T2010", result["publication_key"])

    def test_incomplete_c2_action_blocked(self):
        row = sample()
        row["decision_state_snapshot"]["c2_shadow_action"] = "C2-INCOMPLETE"
        with self.assertRaisesRegex(PublicationBlocked, "invalid C2 shadow action"):
            check_publication(row)

    def test_unexecuted_pair_blocked(self):
        row = sample()
        row["pair_receipt"]["engine_execution_status"] = "FAILED_AFTER_ATTEMPT"
        with self.assertRaisesRegex(PublicationBlocked, "PAIR RECEIPT"):
            check_publication(row)

    def test_forged_action_blocked_even_if_persisted_and_receipt_shape_valid(self):
        row = sample()
        row["decision_state_snapshot"]["c_action"] = "C-PASS"
        with self.assertRaisesRegex(PublicationBlocked, "engine_c_result.action"):
            check_publication(row)

    def test_changed_pair_inputs_block_stale_receipt(self):
        row = sample()
        row["c_input"]["context"]["quote"]["odds"] = 1.62
        with self.assertRaisesRegex(PublicationBlocked, "PAIR RECEIPT"):
            check_publication(row)

    def test_missing_readback_blocked(self):
        row = sample()
        row.pop("decision_state_snapshot")
        with self.assertRaisesRegex(PublicationBlocked, "independent read-back"):
            check_publication(row)

    def test_new_goal_epoch_blocks_old_readback(self):
        row = sample()
        row["latest_evidence_epoch_id"] = "goal-at-21"
        with self.assertRaisesRegex(PublicationBlocked, "NEWER EVIDENCE EPOCH"):
            check_publication(row)

    def test_mixed_model_epochs_blocked(self):
        row = sample()
        row["c2_input"]["context"]["evidence_epoch_id"] = "older"
        with self.assertRaisesRegex(PublicationBlocked, "C2 STALE EVIDENCE EPOCH"):
            check_publication(row)

    def test_source_update_requires_fresh_pair_readback(self):
        row = sample()
        row["active_engine_source_revision"] = "b" * 40
        with self.assertRaisesRegex(PublicationBlocked, "STALE ENGINE SOURCE"):
            check_publication(row)

    def test_quote_moved_blocks(self):
        row = sample()
        row["quote_still_executable"] = False
        with self.assertRaisesRegex(PublicationBlocked, "EXECUTABLE QUOTE"):
            check_publication(row)

    def test_started_match_reroutes(self):
        row = sample()
        row["fixture_status_still_valid"] = False
        with self.assertRaisesRegex(PublicationBlocked, "FIXTURE STATUS"):
            check_publication(row)

    def test_duplicate_same_epoch_reassessment_blocks(self):
        row = sample()
        row["previously_published_keys"] = ["m1:current-20261009T2010"]
        with self.assertRaisesRegex(PublicationBlocked, "DUPLICATE"):
            check_publication(row)


if __name__ == "__main__":
    unittest.main()
