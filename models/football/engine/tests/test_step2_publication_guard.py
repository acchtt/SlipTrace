import copy
import pathlib
import sys
import unittest

ENGINE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE))

from decision_pair_cli import run_pair
from step2_publication_guard import PublicationBlocked, check_publication
from test_adapter import pair_payload


def sample():
    c, c2 = pair_payload("c"), pair_payload("c2")
    receipt = run_pair(c, c2)
    a, b = receipt["results"]["c"], receipt["results"]["c2"]
    snapshot = {
        "match_id": c["match"]["match_id"],
        "record_id": "rec12345678901234",
        "engine_source_revision": "a" * 40,
        "evidence_epoch_id": "current-20261009T2010",
        "c_action": "C-" + a["action"],
        "c2_shadow_action": "C2-" + b["action"] + " — SHADOW",
        "engine_c_result": copy.deepcopy(a),
        "engine_c2_result": copy.deepcopy(b),
    }
    return {
        "schema_version": "football-step2-publication-v2",
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
    def test_exact_pair_readback_can_publish(self):
        result = check_publication(sample())
        self.assertEqual(result["status"], "STEP2_PUBLICATION_ELIGIBLE")
        self.assertIn("current-20261009T2010", result["publication_key"])
        self.assertTrue(result["readback_verified"])

    def test_pair_is_not_reexecuted_or_given_duplicate_input_payloads(self):
        row = sample()
        self.assertNotIn("c_input", row)
        self.assertNotIn("c2_input", row)
        self.assertEqual(check_publication(row)["status"], "STEP2_PUBLICATION_ELIGIBLE")

    def test_incomplete_c2_action_blocked(self):
        row = sample()
        row["decision_state_snapshot"]["c2_shadow_action"] = "C2-INCOMPLETE"
        with self.assertRaisesRegex(PublicationBlocked, "c2_shadow_action"):
            check_publication(row)

    def test_unexecuted_pair_blocked(self):
        row = sample()
        row["pair_receipt"]["engine_execution_status"] = "FAILED_AFTER_ATTEMPT"
        with self.assertRaisesRegex(PublicationBlocked, "pair receipt"):
            check_publication(row)

    def test_forged_action_blocked(self):
        row = sample()
        row["decision_state_snapshot"]["c_action"] = "C-PASS"
        with self.assertRaisesRegex(PublicationBlocked, "c_action"):
            check_publication(row)

    def test_changed_persisted_engine_result_blocked(self):
        row = sample()
        row["decision_state_snapshot"]["engine_c_result"]["reason"] = "forged"
        with self.assertRaisesRegex(PublicationBlocked, "engine_c_result"):
            check_publication(row)

    def test_missing_readback_blocked(self):
        row = sample()
        row.pop("decision_state_snapshot")
        with self.assertRaisesRegex(PublicationBlocked, "readback"):
            check_publication(row)

    def test_newer_evidence_epoch_blocks_old_readback(self):
        row = sample()
        row["latest_evidence_epoch_id"] = "goal-at-21"
        with self.assertRaisesRegex(PublicationBlocked, "newer evidence"):
            check_publication(row)

    def test_source_update_requires_fresh_readback(self):
        row = sample()
        row["active_engine_source_revision"] = "b" * 40
        with self.assertRaisesRegex(PublicationBlocked, "source revision"):
            check_publication(row)

    def test_quote_moved_blocks(self):
        row = sample()
        row["quote_still_executable"] = False
        with self.assertRaisesRegex(PublicationBlocked, "quote"):
            check_publication(row)

    def test_started_match_blocks_publication(self):
        row = sample()
        row["fixture_status_still_valid"] = False
        with self.assertRaisesRegex(PublicationBlocked, "fixture status"):
            check_publication(row)

    def test_duplicate_same_epoch_blocks(self):
        row = sample()
        row["previously_published_keys"] = ["m1:current-20261009T2010"]
        with self.assertRaisesRegex(PublicationBlocked, "duplicate"):
            check_publication(row)


if __name__ == "__main__":
    unittest.main()
