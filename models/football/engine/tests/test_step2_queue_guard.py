import copy
import hashlib
import json
import pathlib
import sys
import unittest

ENGINE_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE_DIR))

from adapter import run_board
from step2_queue_guard import Step2QueueError, freeze_queue
from test_board_pair import c_row, payload


def digest(value):
    return hashlib.sha256(
        json.dumps(
            value, sort_keys=True, ensure_ascii=True, separators=(",", ":")
        ).encode()
    ).hexdigest()


def native_v4_case():
    row = c_row()
    board_result = run_board(payload("c", row))
    cr = board_result["matches"][0]
    rank = {
        "schema_version": "football-stages-v4",
        "status": "V4_RANK_EXECUTED_AWAITING_SHEETS_READBACK",
        "run_id": "V4-TEST-C-ONLY",
        "ranked_count": 1,
        "board": board_result,
        "active_model": "c",
        "retired_models": ["c2", "c3", "c4"],
        "source_replayed": True,
        "current_fixture_status_checked": True,
    }
    rank["integrity_sha256"] = digest(rank)
    persisted = {
        "schema_version": "football-stages-v4",
        "status": "V4_RANK_PERSISTENCE_VERIFIED",
        "run_id": rank["run_id"],
        "rank_sha256": rank["integrity_sha256"],
        "ranked_count": 1,
        "active_model": "c",
        "retired_models": ["c2", "c3", "c4"],
        "model_evidence_readback_verified": True,
        "model_evidence_sha256": digest(board_result),
        "source_replayed": True,
        "current_fixture_status_checked": True,
    }
    board = [{
        "match_id": cr["match_id"],
        "kickoff_ict": cr["kickoff_ict"],
        "official_follow_lane": cr["follow_lane"],
        "c_board_state": "C-" + cr["board_state"],
        "c_supported_line": cr["supported_line"],
        "xi_window_open": True,
    }]
    return {
        "schema_version": "football-step2-queue-v2",
        "session_id": "XI-C-ONLY",
        "mode": "V4_ROUTINE",
        "v4_rank_receipt": rank,
        "v4_persistence_receipt": persisted,
        "board": board,
        "activated_reserves": [],
        "user_exceptions": [],
    }


def rehash(case):
    rank = case["v4_rank_receipt"]
    rank["integrity_sha256"] = digest(
        {k: v for k, v in rank.items() if k != "integrity_sha256"}
    )
    persisted = case["v4_persistence_receipt"]
    persisted["rank_sha256"] = rank["integrity_sha256"]
    persisted["model_evidence_sha256"] = digest(rank["board"])


class Step2QueueTests(unittest.TestCase):
    def test_verified_v4_follow_is_due(self):
        result = freeze_queue(native_v4_case())
        self.assertEqual(result["schema_version"], "football-step2-queue-v2")
        self.assertEqual(result["mode"], "V4_ROUTINE")
        self.assertEqual(result["due_count"], 1)
        self.assertEqual(
            result["due"][0]["step2_authorization"],
            "ROUTINE_FOLLOW",
        )
        self.assertTrue(result["model_evidence_sha256"])

    def test_partial_verified_board_retains_due_rows_and_coverage(self):
        case = native_v4_case()
        coverage = {"schema_version": "football-v4-research-coverage-v1",
                    "research_complete": False, "status": "INCOMPLETE",
                    "assessed_count": 1, "pending_count": 24}
        case["v4_rank_receipt"].update(research_complete=False, research_coverage=coverage)
        case["v4_persistence_receipt"].update(
            status="V4_RANK_PARTIAL_PERSISTENCE_VERIFIED",
            research_complete=False, research_coverage=copy.deepcopy(coverage))
        rehash(case)
        result = freeze_queue(case)
        self.assertEqual(result["due_count"], 1)
        self.assertFalse(result["research_complete"])
        self.assertEqual(result["research_coverage"], coverage)
        case["v4_persistence_receipt"]["status"] = "V4_RANK_PERSISTENCE_VERIFIED"
        with self.assertRaisesRegex(Step2QueueError, "coverage/persistence"):
            freeze_queue(case)

    def test_partial_status_without_coverage_is_rejected(self):
        case = native_v4_case()
        case["v4_persistence_receipt"]["status"] = "V4_RANK_PARTIAL_PERSISTENCE_VERIFIED"
        with self.assertRaisesRegex(Step2QueueError, "requires research coverage"):
            freeze_queue(case)

    def test_retired_v1_routine_contract_is_rejected(self):
        case = native_v4_case()
        case["schema_version"] = "football-step2-queue-v1"
        case["mode"] = "ROUTINE"
        with self.assertRaisesRegex(Step2QueueError, "queue-v2"):
            freeze_queue(case)

    def test_missing_verified_rank_chain_blocks(self):
        for key in ("v4_rank_receipt", "v4_persistence_receipt"):
            with self.subTest(key=key):
                case = native_v4_case()
                case.pop(key)
                with self.assertRaisesRegex(
                    Step2QueueError,
                    "rank and persistence",
                ):
                    freeze_queue(case)

    def test_tampered_persistence_model_hash_blocks(self):
        case = native_v4_case()
        case["v4_persistence_receipt"]["model_evidence_sha256"] = "0" * 64
        with self.assertRaisesRegex(Step2QueueError, "model evidence"):
            freeze_queue(case)

    def test_retired_c2_board_fields_are_not_required(self):
        case = native_v4_case()
        self.assertNotIn("c2_supported_line", case["board"][0])
        self.assertNotIn("c2_shadow_state", case["board"][0])
        self.assertEqual(freeze_queue(case)["due_count"], 1)

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
        case["v4_rank_receipt"]["board"]["matches"][0]["follow_lane"] = "RESERVE"
        case["board"] = [row]
        rehash(case)

        result = freeze_queue(case)
        self.assertEqual(result["due_count"], 0)
        self.assertEqual(
            result["not_due"][0]["reason"],
            "RESERVE_NOT_ACTIVATED",
        )

        case["activated_reserves"] = [{
            "match_id": mid,
            "activation_reference": "user activated reserve",
        }]
        result = freeze_queue(case)
        self.assertEqual(result["due_count"], 1)
        self.assertEqual(
            result["due"][0]["step2_authorization"],
            "RESERVE_ACTIVATED",
        )

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
        self.assertEqual(
            result["due"][0]["step2_authorization"],
            "USER_EXCEPTION",
        )

    def test_exception_only_cannot_smuggle_board(self):
        case = native_v4_case()
        case["mode"] = "EXCEPTION_ONLY"
        with self.assertRaisesRegex(Step2QueueError, "cannot import board"):
            freeze_queue(case)


if __name__ == "__main__":
    unittest.main()
