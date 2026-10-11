import copy
import pathlib
import sys
import unittest

ENGINE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE))

from rank_persistence_reconcile import RankReadbackError, validate_rank_readback


def scenario():
    source = "a" * 64
    c = {
        "match_id": "fixture-A", "rank": 1,
        "board_state": "FOCUS", "supported_line": 2.5, "follow_lane": "FOLLOW",
    }
    c2 = {
        "match_id": "fixture-A", "rank": 1,
        "board_state": "WATCH", "supported_line": 2.25,
    }
    return {
        "schema_version": "football-step1-readback-v1",
        "run_id": "SWEEP-20261012-0001-20261012-0300",
        "source_payload_hash": source,
        "active_base_id": "appbzxqXYf0lKfD4P",
        "readback_method": "INDEPENDENT_AIRTABLE_REFETCH",
        "readback_at_utc": "2026-10-11T15:00:00Z",
        "frozen_ab_queue": [
            {"match_id": "fixture-A", "step0_capacity_queue_rank": 1},
            {"match_id": "fixture-B", "step0_capacity_queue_rank": 2},
        ],
        "board_pair": {
            "board_engine_execution_status": "EXECUTED_C_C2_BOARDS",
            "common_evidence_reconciled": True,
            "results": {"c": {"matches": [c]}, "c2": {"matches": [c2]}},
        },
        "sweep_run_readback": {
            "run_id": "SWEEP-20261012-0001-20261012-0300",
            "source_payload_hash": source, "run_status": "COMPLETE",
        },
        "readback_rows": [{
            "match_id": "fixture-A",
            "coverage_id": "SWEEP-20261012-0001-20261012-0300|fixture-A",
            "step0_capacity_queue_rank": 1,
            "c_rank": 1, "c_board_state": "C-FOCUS",
            "c_supported_line": 2.5, "follow_lane": "FOLLOW",
            "c2_rank": 1, "c2_board_state": "C2-WATCH",
            "c2_supported_line": 2.25,
        }],
        "unranked_reasons": {"fixture-B": "RESEARCH_BUDGET_EXHAUSTED"},
        "terminal_status": {
            "complete": True, "blocked": False,
            "ranked_eligible_count": 1,
            "follow_count": 1, "reserve_count": 0, "stop_count": 0,
        },
    }


class RankPersistenceTests(unittest.TestCase):
    def test_valid_pair_and_readback(self):
        out = validate_rank_readback(scenario())
        self.assertEqual(out["status"], "STEP1_PERSISTENCE_READBACK_VERIFIED")
        self.assertEqual(out["ranked_count"], 1)
        self.assertEqual(out["unranked_count"], 1)

    def test_readback_drift_is_fail_closed(self):
        for field, value in (
            ("c_rank", 2),
            ("c_supported_line", 3.5),
            ("follow_lane", "STOP"),
            ("coverage_id", "SWEEP-other|fixture-A"),
            ("step0_capacity_queue_rank", 2),
        ):
            p = scenario()
            p["readback_rows"][0][field] = value
            with self.subTest(field=field), self.assertRaises(RankReadbackError):
                validate_rank_readback(p)

    def test_unranked_queue_member_requires_reason(self):
        p = scenario()
        p["unranked_reasons"] = {}
        with self.assertRaisesRegex(RankReadbackError, "unranked"):
            validate_rank_readback(p)

    def test_pair_must_be_independent_and_executed(self):
        p = scenario()
        p["board_pair"]["results"]["c2"]["matches"] = []
        with self.assertRaisesRegex(RankReadbackError, "universe"):
            validate_rank_readback(p)
        p = scenario()
        p["board_pair"]["board_engine_execution_status"] = "NOT_RUN"
        with self.assertRaisesRegex(RankReadbackError, "paired engine"):
            validate_rank_readback(p)

    def test_legacy_archive_or_self_report_is_not_readback(self):
        p = scenario()
        p["active_base_id"] = "appWyZJjitSBATXAU"
        with self.assertRaisesRegex(RankReadbackError, "independent readback"):
            validate_rank_readback(p)
        p = scenario()
        p["readback_method"] = "PREWRITE_PAYLOAD"
        with self.assertRaisesRegex(RankReadbackError, "independent readback"):
            validate_rank_readback(p)


if __name__ == "__main__":
    unittest.main()
