import copy
import pathlib
import sys
import unittest

ENGINE_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE_DIR))

from step2_queue_guard import Step2QueueError, freeze_queue
from test_xi_v4_coordinated import native_v4_case


class Step2QueueTests(unittest.TestCase):
    def test_verified_v4_follow_is_due(self):
        result = freeze_queue(native_v4_case())
        self.assertEqual(result["schema_version"], "football-step2-queue-v2")
        self.assertEqual(result["mode"], "V4_ROUTINE")
        self.assertEqual(result["due_count"], 1)
        self.assertEqual(result["due"][0]["step2_authorization"], "ROUTINE_FOLLOW")
        self.assertTrue(result["model_evidence_sha256"])

    def test_retired_v1_routine_contract_is_rejected(self):
        case = native_v4_case()
        case["schema_version"] = "football-step2-queue-v1"
        case["mode"] = "ROUTINE"
        case["source_run"] = {"work_ready": True}
        with self.assertRaisesRegex(Step2QueueError, "queue-v2"):
            freeze_queue(case)

    def test_missing_verified_rank_chain_blocks(self):
        for key in ("v4_rank_receipt", "v4_persistence_receipt"):
            with self.subTest(key=key):
                case = native_v4_case()
                case.pop(key)
                with self.assertRaisesRegex(Step2QueueError, "rank and persistence"):
                    freeze_queue(case)

    def test_tampered_persistence_model_hash_blocks(self):
        case = native_v4_case()
        case["v4_persistence_receipt"]["model_evidence_sha256"] = "0" * 64
        with self.assertRaisesRegex(Step2QueueError, "model evidence"):
            freeze_queue(case)

    def test_c2_frozen_line_required(self):
        case = native_v4_case()
        case["board"][0]["c2_supported_line"] = None
        with self.assertRaisesRegex(Step2QueueError, "C2 supported line|c2_supported_line"):
            freeze_queue(case)

    def test_lane_cannot_drift_from_verified_rank(self):
        case = native_v4_case()
        case["board"][0]["official_follow_lane"] = "STOP"
        with self.assertRaisesRegex(Step2QueueError, "lane differs"):
            freeze_queue(case)

    def test_reserve_requires_explicit_activation(self):
        case = native_v4_case()
        row = copy.deepcopy(case["board"][0])
        mid = row["match_id"]
        row["official_follow_lane"] = "RESERVE"
        rank_c = case["v4_rank_receipt"]["board_pair"]["results"]["c"]["matches"][0]
        rank_c["follow_lane"] = "RESERVE"
        case["v4_rank_receipt"]["integrity_sha256"] = __import__("hashlib").sha256(
            __import__("json").dumps(
                {k:v for k,v in case["v4_rank_receipt"].items() if k != "integrity_sha256"},
                sort_keys=True, ensure_ascii=True, separators=(",", ":")
            ).encode()
        ).hexdigest()
        case["v4_persistence_receipt"]["rank_sha256"] = case["v4_rank_receipt"]["integrity_sha256"]
        case["v4_persistence_receipt"]["model_evidence_sha256"] = __import__("hashlib").sha256(
            __import__("json").dumps(
                case["v4_rank_receipt"]["board_pair"]["results"],
                sort_keys=True, ensure_ascii=True, separators=(",", ":")
            ).encode()
        ).hexdigest()
        case["board"] = [row]
        result = freeze_queue(case)
        self.assertEqual(result["due_count"], 0)
        self.assertEqual(result["not_due"][0]["reason"], "RESERVE_NOT_ACTIVATED")

        case["activated_reserves"] = [{
            "match_id": mid,
            "activation_reference": "user activated reserve",
        }]
        result = freeze_queue(case)
        self.assertEqual(result["due_count"], 1)
        self.assertEqual(result["due"][0]["step2_authorization"], "RESERVE_ACTIVATED")

    def test_duplicate_board_match_rejected(self):
        case = native_v4_case()
        case["board"].append(copy.deepcopy(case["board"][0]))
        with self.assertRaises(Step2QueueError):
            freeze_queue(case)

    def test_exception_only_is_minimal_and_explicit(self):
        case = {
            "schema_version": "football-step2-queue-v2",
            "session_id": "XI-EXCEPTION",
            "mode": "EXCEPTION_ONLY",
            "board": [],
            "activated_reserves": [],
            "user_exceptions": [{
                "match_id": "outside-board",
                "user_authorization_reference": "user requested /xi exception",
            }],
        }
        result = freeze_queue(case)
        self.assertEqual(result["due_count"], 1)
        self.assertEqual(result["due"][0]["step2_authorization"], "USER_EXCEPTION")

    def test_exception_only_cannot_smuggle_board(self):
        case = native_v4_case()
        case["mode"] = "EXCEPTION_ONLY"
        with self.assertRaisesRegex(Step2QueueError, "cannot import board"):
            freeze_queue(case)

    def test_exception_reference_required(self):
        case = {
            "schema_version": "football-step2-queue-v2",
            "session_id": "XI-EXCEPTION",
            "mode": "EXCEPTION_ONLY",
            "board": [],
            "activated_reserves": [],
            "user_exceptions": [{
                "match_id": "outside-board",
                "user_authorization_reference": "",
            }],
        }
        with self.assertRaisesRegex(Step2QueueError, "user_authorization_reference"):
            freeze_queue(case)


if __name__ == "__main__":
    unittest.main()
