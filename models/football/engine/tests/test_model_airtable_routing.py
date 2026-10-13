import pathlib
import sys
import unittest

AIRTABLE_DIR = pathlib.Path(__file__).resolve().parents[2] / "airtable"
sys.path.insert(0, str(AIRTABLE_DIR))
from route import AirtableRouteError, resolve_table, verify_receipt, _configuration


class ActiveModelRoutingTests(unittest.TestCase):
    def test_all_model_workflows_use_new_active_base(self):
        config = _configuration()
        self.assertEqual(config["base_id"], "appbzxqXYf0lKfD4P")
        for workflow in config["workflow_scope"]:
            for table, target in config["tables"].items():
                if table == "Actual Bets — Current":
                    continue
                with self.subTest(workflow=workflow, table=table):
                    resolved = resolve_table(workflow, table)
                    self.assertEqual(resolved["baseId"], config["base_id"])
                    self.assertEqual(resolved["tableId"], target)

    def test_step1_engine_result_fields_are_pinned(self):
        config = _configuration()
        fields = config["step1_engine_result_fields"]
        self.assertEqual(fields["table"], "Daily Coverage Ledger")
        self.assertEqual(fields["c_field_id"], "fldhUWNoyXzXfQJ3C")
        self.assertEqual(fields["c2_field_id"], "fldq0n2tDlS58goAm")
        self.assertTrue(fields["exact_json_readback_required"])
        self.assertFalse(fields["historical_backfill"])

    def test_sweep_is_not_rerouted(self):
        with self.assertRaisesRegex(AirtableRouteError, "sweep"):
            resolve_table("sweep", "Daily Coverage Ledger", action="upsert")
        with self.assertRaisesRegex(AirtableRouteError, "Sweep Runs"):
            resolve_table("rank", "Sweep Runs", action="upsert")

    def test_rank_to_new_coverage_and_xi_to_new_decisions(self):
        self.assertEqual(
            resolve_table("rank", "Daily Coverage Ledger", action="upsert")["tableId"],
            "tbl20jBW5dfgNnTV6",
        )
        self.assertEqual(
            resolve_table("xi", "Decision States", action="create")["tableId"],
            "tblzMyYuDTi1UMd66",
        )
        self.assertEqual(
            resolve_table("audit", "Factor Calibration Observations", action="create")["tableId"],
            "tblCfYuxmc1FfHS76",
        )
        self.assertEqual(
            resolve_table("report", "Actual Bets — Current")["tableId"],
            "tblGsnU4Ht0OpmdH8",
        )

    def test_never_back_write_old_base(self):
        route = resolve_table("rank", "Daily Coverage Ledger")
        with self.assertRaisesRegex(AirtableRouteError, "MODEL_BASE_MISMATCH"):
            verify_receipt(
                expected_base=route["baseId"],
                expected_table=route["tableName"],
                actual_base="appWyZJjitSBATXAU",
                actual_table=route["tableId"],
                record_id="rec3LXqoqcHmlpoql",
                original_record_identity="SWEEP-20261011-0858-20261011-1200|K3-GAN-SIH",
                readback_record_identity="SWEEP-20261011-0858-20261011-1200|K3-GAN-SIH",
            )

    def test_requires_record_identity_readback(self):
        route = resolve_table("rank", "Daily Coverage Ledger")
        with self.assertRaisesRegex(AirtableRouteError, "READBACK_MISMATCH"):
            verify_receipt(
                expected_base=route["baseId"],
                expected_table=route["tableName"],
                actual_base=route["baseId"],
                actual_table=route["tableId"],
                record_id="rec6WUutrjqOXKXcy",
                original_record_identity="expected-fixture",
                readback_record_identity="other-fixture",
            )
        self.assertTrue(verify_receipt(
            expected_base=route["baseId"],
            expected_table=route["tableName"],
            actual_base=route["baseId"],
            actual_table=route["tableId"],
            record_id="rec6WUutrjqOXKXcy",
            original_record_identity="SWEEP-20261011-0858-20261011-1200|K3-GAN-SIH",
            readback_record_identity="SWEEP-20261011-0858-20261011-1200|K3-GAN-SIH",
        ))

    def test_actual_bets_cannot_be_written_without_real_confirmed_slip(self):
        with self.assertRaisesRegex(AirtableRouteError, "verified user slip"):
            resolve_table("xi", "Actual Bets — Current", action="create")
        with self.assertRaisesRegex(AirtableRouteError, "verified user slip"):
            resolve_table("audit", "Actual Bets — Current", action="create")
        ok = resolve_table("model_accounting", "Actual Bets — Current",
                           action="upsert", confirmed_user_slip=True)
        self.assertEqual(ok["baseId"], "appbzxqXYf0lKfD4P")

    def test_excludes_unknown_tables_and_unsupported_workflows(self):
        with self.assertRaises(AirtableRouteError):
            resolve_table("rank", "Unknown Table")
        with self.assertRaises(AirtableRouteError):
            resolve_table("sweep", "Sweep Runs")
        with self.assertRaises(AirtableRouteError):
            resolve_table("rank", "Decision States", action="delete")


if __name__ == "__main__":
    unittest.main()
