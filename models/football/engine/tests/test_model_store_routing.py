import pathlib
import sys
import unittest

STORE_DIR = pathlib.Path(__file__).resolve().parents[2] / "google_sheets"
sys.path.insert(0, str(STORE_DIR))

from route import (
    GoogleSheetsRouteError,
    _configuration,
    resolve_tab,
    parent_first_persistence_plan,
    verify_parent_before_children,
    verify_receipt,
)


SPREADSHEET_ID = "1ojWKj5aT3VEJUyX3NSbAOZNTaUM0Mb8I8e4lvFy7kGM"


class ActiveModelStoreRoutingTests(unittest.TestCase):
    def test_all_workflows_use_active_google_sheet(self):
        config = _configuration()
        self.assertEqual(config["spreadsheet_id"], SPREADSHEET_ID)
        for workflow in config["workflow_scope"]:
            for tab in config["tabs"]:
                if tab == "Actual Bets — Current":
                    continue
                with self.subTest(workflow=workflow, tab=tab):
                    resolved = resolve_tab(workflow, tab)
                    self.assertEqual(resolved["spreadsheetId"], SPREADSHEET_ID)
                    self.assertEqual(resolved["sheetName"], tab)

    def test_sweep_is_in_same_active_store(self):
        route = resolve_tab("sweep", "Sweep Runs", action="upsert")
        self.assertEqual(route["sheetName"], "Sweep Runs")
        self.assertEqual(route["keyColumn"], "Run ID")

    def test_rank_and_xi_tabs_are_pinned(self):
        self.assertEqual(
            resolve_tab("rank", "Daily Coverage Ledger", action="upsert")["keyColumn"],
            "Coverage ID",
        )

    def test_rank_persistence_plan_is_parent_first(self):
        plan = parent_first_persistence_plan(
            run_id="RUN",
            coverage_ids=["RUN|m1", "RUN|m2"],
        )
        self.assertEqual(
            [(step["step"], step["sheet"], step["operation"])
             for step in plan["steps"]],
            [
                (1, "Sweep Runs", "UPSERT"),
                (2, "Sweep Runs", "INDEPENDENT_REFETCH"),
                (3, "Daily Coverage Ledger", "UPSERT"),
                (4, "Daily Coverage Ledger", "INDEPENDENT_REFETCH"),
            ],
        )
        with self.assertRaisesRegex(GoogleSheetsRouteError, "children"):
            parent_first_persistence_plan(
                run_id="RUN", coverage_ids=["OTHER|m1"]
            )

    def test_parent_readback_must_precede_coverage(self):
        parent = {
            "spreadsheet_id": SPREADSHEET_ID,
            "sheet_name": "Sweep Runs",
            "method": "INDEPENDENT_GOOGLE_SHEETS_REFETCH",
            "run_id": "RUN",
            "sweep_integrity_sha256": "abc",
            "exists": True,
            "readback_at_utc": "2026-10-29T01:00:00Z",
        }
        self.assertTrue(verify_parent_before_children(
            run_id="RUN",
            sweep_integrity_sha256="abc",
            parent_readback=parent,
            coverage_write_started_at_utc="2026-10-29T01:01:00Z",
            coverage_readback_at_utc="2026-10-29T01:02:00Z",
        ))
        parent["readback_at_utc"] = "2026-10-29T01:03:00Z"
        with self.assertRaisesRegex(
            GoogleSheetsRouteError, "PARENT_CHILD_PERSISTENCE_ORDER_INVALID"
        ):
            verify_parent_before_children(
                run_id="RUN",
                sweep_integrity_sha256="abc",
                parent_readback=parent,
                coverage_write_started_at_utc="2026-10-29T01:01:00Z",
                coverage_readback_at_utc="2026-10-29T01:02:00Z",
            )
        self.assertEqual(
            resolve_tab("xi", "Decision States", action="upsert")["keyColumn"],
            "Assessment ID",
        )

    def test_single_c_columns_are_pinned(self):
        config = _configuration()
        self.assertEqual(config["active_models"], ["c"])
        self.assertEqual(config["retired_models"], ["c2", "c3", "c4"])
        self.assertEqual(
            config["step1_engine_result"]["column_name"],
            "Step1 Engine C Result",
        )
        status = config["xi_assessment_execution_status_column"]
        self.assertEqual(status["column_name"], "XI Assessment Execution Status")
        self.assertEqual(status["football_only_value"], "EXECUTED_C_FOOTBALL_ONLY")
        self.assertEqual(
            status["football_and_price_value"],
            "EXECUTED_C_FOOTBALL_AND_PRICE",
        )

    def test_airtable_is_historical_read_only(self):
        config = _configuration()
        legacy = config["legacy_airtable"]
        self.assertEqual(
            legacy["policy"],
            "HISTORICAL_READ_ONLY_NO_NEW_WRITES",
        )
        self.assertEqual(
            legacy["quota_state_at_migration"],
            "MONTHLY_API_LIMIT_EXCEEDED",
        )

    def test_cross_workbook_readback_fails(self):
        route = resolve_tab("rank", "Daily Coverage Ledger")
        with self.assertRaisesRegex(
            GoogleSheetsRouteError,
            "MODEL_SPREADSHEET_MISMATCH",
        ):
            verify_receipt(
                expected_spreadsheet=route["spreadsheetId"],
                expected_sheet=route["sheetName"],
                actual_spreadsheet="wrong-sheet-id",
                actual_sheet=route["sheetName"],
                row_key="RUN|MATCH",
                original_record_identity="RUN|MATCH",
                readback_record_identity="RUN|MATCH",
            )

    def test_requires_exact_immutable_row_key(self):
        route = resolve_tab("rank", "Daily Coverage Ledger")
        with self.assertRaisesRegex(
            GoogleSheetsRouteError,
            "READBACK_MISMATCH",
        ):
            verify_receipt(
                expected_spreadsheet=route["spreadsheetId"],
                expected_sheet=route["sheetName"],
                actual_spreadsheet=route["spreadsheetId"],
                actual_sheet=route["sheetName"],
                row_key="RUN|MATCH",
                original_record_identity="RUN|MATCH",
                readback_record_identity="OTHER",
            )
        self.assertTrue(
            verify_receipt(
                expected_spreadsheet=route["spreadsheetId"],
                expected_sheet=route["sheetName"],
                actual_spreadsheet=route["spreadsheetId"],
                actual_sheet=route["sheetName"],
                row_key="RUN|MATCH",
                original_record_identity="RUN|MATCH",
                readback_record_identity="RUN|MATCH",
            )
        )

    def test_actual_bets_require_confirmed_slip(self):
        with self.assertRaisesRegex(
            GoogleSheetsRouteError,
            "verified user slip",
        ):
            resolve_tab("xi", "Actual Bets — Current", action="upsert")
        ok = resolve_tab(
            "xi",
            "Actual Bets — Current",
            action="upsert",
            confirmed_user_slip=True,
        )
        self.assertEqual(ok["sheetName"], "Actual Bets — Current")

    def test_unknown_tabs_actions_and_workflows_fail(self):
        with self.assertRaises(GoogleSheetsRouteError):
            resolve_tab("rank", "Unknown Tab")
        with self.assertRaises(GoogleSheetsRouteError):
            resolve_tab("rank", "Decision States", action="delete")
        with self.assertRaises(GoogleSheetsRouteError):
            resolve_tab("unsupported", "Decision States")


if __name__ == "__main__":
    unittest.main()
