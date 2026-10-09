import copy
import json
import pathlib
import sys
import tempfile
import unittest

ENGINE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE))

from step0_package_cli import package, Step0HandoffError  # noqa: E402
from test_step0_handoff_cli import bounded_payload, proof, row, required_proof  # noqa: E402


def scenario():
    p = bounded_payload()
    p["run_id"] = "SWEEP-20261009-2123-20261010-0300"
    p["source_payload_hash"] = "frozen-source-epoch"
    p["verification_policy"] = "FAST_FINISH_V1"
    p["terminal_unresolved_verification_blocks"] = []
    p["sweep_work_budget_policy"] = "COMPACT_GOAL_ROUTE_V1"
    p["strict_intake_policy"] = "XI_MARKET_FIRST_V1"
    p["production_universe_count"] = 66
    required_proof(p)
    p["capacity_queue"] = [
        proof(row(f"m{i}", i, "ADMITTED_TO_C" if i <= 8 else "OPERATIONAL_CAPACITY_DEFERRED"))
        for i in range(1, 11)
    ]
    p["admitted_fixtures"] = [dict(a) for a in p["capacity_queue"][:8]]
    p["admitted_to_c_count"] = 8
    p["capacity_deferred_count"] = 2
    run = {
        "run_id": p["run_id"],
        "run_status": "RUNNING",
        "phase": "PACKAGING",
        "reconciliation_complete": True,
        "capacity_queue_frozen": True,
        "required_competition_blocks_complete": True,
        "pending_verification_blocks": 0,
        "unresolved_count": 0,
        "source_payload_hash": p["source_payload_hash"],
        "admitted_count": 8,
        "production_universe_count": 66,
        "required_competition_source_fixture_ids": copy.deepcopy(p["required_competition_source_fixture_ids"]),
        "admitted_dispositions": {x["match_id"]: "ADMITTED_TO_C" for x in p["admitted_fixtures"]},
    }
    return p, run


class Step0PackagingTests(unittest.TestCase):
    def do_package(self, handoff, run, text="RESEARCHABLE SENIOR HANDOFF COMPLETE"):
        with tempfile.TemporaryDirectory() as temp:
            root = pathlib.Path(temp)
            handoff_path = root / "STEP0_HANDOFF.json"
            text_path = root / "AISCORE_FIXTURES_TEST.txt"
            proof_path = root / "sweep_run_proof.json"
            output = root / "AISCORE_FIXTURES_TEST.zip"
            handoff_path.write_text(json.dumps(handoff), encoding="utf-8")
            text_path.write_text(text, encoding="utf-8")
            proof_path.write_text(json.dumps(run), encoding="utf-8")
            try:
                result = package(handoff_path, text_path, proof_path, output)
                return result, output.exists()
            except Step0HandoffError:
                self.assertFalse(output.exists(), "invalid package must never leave an artifact")
                raise

    def test_valid_final_handoff_generates_canonical_zip(self):
        handoff, run = scenario()
        result, exists = self.do_package(handoff, run)
        self.assertTrue(exists)
        self.assertEqual(result["status"], "STEP0 WORK ZIP VALIDATED")
        self.assertEqual(result["admitted"], 8)

    def test_screenshot_provisional_flags_do_not_generate_zip(self):
        handoff, run = scenario()
        handoff.update(complete=False, actionable_complete=False, work_ready=False)
        with self.assertRaisesRegex(Step0HandoffError, "complete=true required"):
            self.do_package(handoff, run)

    def test_missing_ten_fixture_manifest_is_rejected(self):
        handoff, run = scenario()
        block = handoff["required_competition_blocks"][0]
        block["fixture_count"] = 10
        block["fixtures"] = []
        with self.assertRaisesRegex(Step0HandoffError, "fixture_count"):
            self.do_package(handoff, run)

    def test_unfrozen_eight_candidates_block_zip(self):
        handoff, run = scenario()
        run["capacity_queue_frozen"] = False
        with self.assertRaisesRegex(Step0HandoffError, "capacity queue not frozen"):
            self.do_package(handoff, run)
        run["capacity_queue_frozen"] = True
        run["admitted_dispositions"]["m1"] = "UNRESOLVED"
        with self.assertRaisesRegex(Step0HandoffError, "still provisional"):
            self.do_package(handoff, run)

    def test_source_inventory_mismatch_blocked(self):
        handoff, run = scenario()
        run["required_competition_source_fixture_ids"]["NED_EERSTE_DIVISIE"] = ["different-id"]
        with self.assertRaisesRegex(Step0HandoffError, "source ledger"):
            self.do_package(handoff, run)

    def test_run_did_not_complete_reconciliation(self):
        handoff, run = scenario()
        run["reconciliation_complete"] = False
        with self.assertRaisesRegex(Step0HandoffError, "reconciliation not complete"):
            self.do_package(handoff, run)

    def test_provisional_text_does_not_generate_zip(self):
        handoff, run = scenario()
        with self.assertRaisesRegex(Step0HandoffError, "provisional handoff text"):
            self.do_package(handoff, run, text="PROVISIONAL BOARD — 8 matches")


if __name__ == "__main__":
    unittest.main()
