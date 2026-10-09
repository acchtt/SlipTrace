"""Isolated repair QA. Only branch audit/sweep-20261009-2123-repair.

Never treat the QA candidate's completion booleans as an operational
Airtable COMPLETE event unless the repository export validator passes.
"""
import json
import pathlib
import subprocess
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[3]
ENGINE = ROOT / "models" / "football" / "engine"
HANDOFF = ROOT / "models" / "football" / "handoffs" / "SWEEP-20261009-2123-20261010-0300" / "STEP0_HANDOFF.json"


class SweepRepairOriginalExportCLITests(unittest.TestCase):
    def test_original_export_validator_runs_and_passes(self):
        self.assertTrue(HANDOFF.is_file(), "Step0 repair fixture missing")
        run = subprocess.run(
            [
                sys.executable,
                str(ENGINE / "step0_handoff_cli.py"),
                "--input", str(HANDOFF), "--consumer", "export",
            ],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(run.returncode, 0, f"validator failed:\n{run.stdout}\n{run.stderr}")
        body = json.loads(run.stdout)
        self.assertEqual(body["step0_handoff_validation_status"], "PASS")
        self.assertEqual(body["admitted_count"], 8)
        self.assertEqual(body["capacity_queue_count"], 8)
        self.assertEqual(body["capacity_deferred_count"], 0)

    def test_required_fixtures_come_from_independently_reconciled_source_inventory(self):
        payload = json.loads(HANDOFF.read_text(encoding="utf-8"))
        block = next(
            b for b in payload["required_competition_blocks"]
            if b["block_id"] == "NED_EERSTE_DIVISIE"
        )
        self.assertEqual(block["fixture_count"], 10)
        self.assertEqual(
            sorted(x["match_id"] for x in block["fixtures"]),
            sorted(payload["required_competition_source_fixture_ids"]["NED_EERSTE_DIVISIE"]),
        )
        self.assertTrue(all(x["disposition"] == "OPERATIONAL_EXCLUDED" for x in block["fixtures"]))
        self.assertEqual(payload["production_universe_count"], 66)


if __name__ == "__main__":
    unittest.main()
