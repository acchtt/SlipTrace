"""Cross-command V4 operational precedence regression; no provider/network I/O."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[3]
PROMPTS = ROOT / "models" / "football" / "prompts"
PROCEDURES = ROOT / "models" / "football" / "procedures"
STAGES = ROOT / "models" / "football" / "stages_v4"


class CurrentProcedureAuthorityTests(unittest.TestCase):
    def test_canonical_command_map_is_v4_not_legacy(self):
        router = (PROMPTS / "COMMAND_ALIASES.md").read_text()
        readme = (PROMPTS / "README.md").read_text()
        for canonical in ("stages_v4/SWEEP.md", "stages_v4/RANK.md"):
            self.assertIn(canonical, router)
            self.assertIn(canonical, readme)
        self.assertNotIn("PRODUCTION RETIREMENT — EFFECTIVE 2026-10-11: /sweep and /rank are SCRAPPED", readme)
        self.assertIn("V4", (PROMPTS / "sweep.md").read_text())
        self.assertIn("V4", (PROMPTS / "rank.md").read_text())

    def test_sweep_requires_complete_date_surfaces_before_registry(self):
        stage = (STAGES / "stage.py").read_text()
        completeness = (STAGES / "source_completeness.py").read_text()
        sweep = (STAGES / "SWEEP.md").read_text()
        current = (ROOT / "models" / "football" / "CURRENT_MODEL.md").read_text()
        for required in (
            "DATE_SURFACE_BATCH_V2",
            "DATE_SURFACE_ONLY",
            "registry_prefilter_applied",
            "terminal_sentinel",
            "provider_senior_competition_block_count",
        ):
            self.assertIn(required, completeness)
        self.assertIn("validate_source_completeness", stage)
        self.assertIn("SWEEP_COMPLETENESS_V2_EFFECTIVE_UTC", stage)
        self.assertIn("complete provider **date/listing surfaces**", sweep)
        self.assertIn("registry is **never** a fixture-discovery query", sweep.lower())
        self.assertIn("source_completeness_manifest", current)
        self.assertIn("registry_prefilter_applied=false", current)

    def test_rank_requires_source_and_status_on_every_cli_invocation(self):
        stage = (STAGES / "stage.py").read_text()
        self.assertIn('"source", "status-refresh"', stage)
        self.assertIn("_check_rank_source_and_status(", stage)
        self.assertIn("V4_SOURCE_REPLAY_REQUIRED", stage)
        self.assertIn("V4_STATUS_REFRESH_INCOMPLETE", stage)
        self.assertIn("PREMATCH_WINDOW_CLOSED by current fixture status", stage)
        rank = (STAGES / "RANK.md").read_text()
        self.assertIn("--source source.json", rank)
        self.assertIn("--status-refresh status_refresh.json", rank)

    def test_screenshot_only_preserves_original_odds_and_blocks_fake_executability(self):
        xi = (PROMPTS / "02_NORMAL_CHAT_XI_ODDS.md").read_text()
        simple = (PROCEDURES / "FOOTBALL_SIMPLE_ASSESS_AND_BET.md").read_text()
        history = (PROCEDURES / "FOOTBALL_MARKET_HISTORY_RECHECK.md").read_text()
        portable = (ROOT / "models" / "football" / "engine" / "xi_portable.py").read_text()
        for doc in (xi, simple, history):
            self.assertIn("USER_SCREENSHOT_ONLY", doc) if doc != simple else self.assertIn("Screenshot-only", doc)
            self.assertIn("screenshot", doc.lower())
        self.assertIn("SCREENSHOT_CANNOT_INDEPENDENTLY_PROVE_EXECUTABLE_OFFER", portable)
        self.assertNotIn('if same_instant and screenshotted_live_offer', portable)

    def test_live_wrapper_does_not_require_an_additional_bet_command(self):
        wrapper = (PROMPTS / "live.md").read_text()
        self.assertIn("Do not require /bet", wrapper)
        self.assertIn("without searching for replacement odds", wrapper)
        self.assertIn("LIVE_ENGINE_AUTHORIZATION_NOT_EXECUTED", (
            ROOT / "models" / "football" / "engine" / "xi_portable.py"
        ).read_text())

    def test_legacy_operations_are_marked_non_authoritative(self):
        names = (
            "FOOTBALL_BETTING_PROCEDURE.md", "FOOTBALL_COVERAGE_CONTROLLER.md",
            "FOOTBALL_SWEEP_SCOPE.md", "FOOTBALL_RANK_TERMINAL_STATUS.md",
            "FOOTBALL_TIME_AND_SCHEDULE_INTEGRITY.md",
            "FOOTBALL_XI_MARKET_FIRST_INTAKE.md",
        )
        for filename in names:
            with self.subTest(filename=filename):
                doc = (PROCEDURES / filename).read_text()
                self.assertTrue(doc.startswith("> **V4 AUTHORITY NOTICE"), filename)

    def test_current_model_has_one_v4_router_only(self):
        current = (ROOT / "models" / "football" / "CURRENT_MODEL.md").read_text()
        self.assertIn("Historical V3 coordinator — non-authoritative", current)
        self.assertIn("/sweep` -> `models/football/stages_v4/SWEEP.md", current)
        self.assertIn("/rank` -> `models/football/stages_v4/RANK.md", current)
        self.assertNotIn("- `/sweep` -> `00_NORMAL_CHAT_AISCORE_FETCH.md`", current)
        self.assertNotIn("- `/rank` -> `01_WORK_DAILY_SWEEP.md`", current)
        self.assertNotIn("## Unified /sweep and /rank V3", current)

    def test_routine_xi_binds_rank_to_original_source_and_status_refresh(self):
        bridge = (ROOT / "models" / "football" / "engine" / "xi_v4_queue.py").read_text()
        guard = (ROOT / "models" / "football" / "engine" / "step2_queue_guard.py").read_text()
        for required in (
            "source_replayed", "current_fixture_status_checked",
            "original_source_sha256", "status_refresh_sha256",
            "v4_original_source", "v4_status_refresh",
        ):
            self.assertIn(required, bridge)
        self.assertIn("v4_provenance_chain_verified", guard)
        self.assertNotIn('result["v4_source_attested"] = True', guard)

    def test_current_xi_bootstrap_is_football_first_not_priced_pair(self):
        active = (PROCEDURES / "FOOTBALL_C_C2_ACTIVE_PAIR.md").read_text()
        engine = (PROCEDURES / "FOOTBALL_ENGINE_EXECUTION_BOOTSTRAP.md").read_text()
        runtime = (PROCEDURES / "FOOTBALL_RUNTIME_EXECUTION_BOOTSTRAP.md").read_text()
        for doc in (active, engine, runtime):
            self.assertIn("xi_portable.py xi", doc)
            self.assertIn("EXECUTED_C_C2_FOOTBALL_ONLY", doc)
        self.assertIn("decision_pair_cli.py --football-only", engine)
        self.assertIn("strict prematch", engine.lower())
        self.assertIn("deterministic live priced-action engine", runtime)

    def test_current_live_pricing_is_explicitly_non_executable(self):
        transition = (ROOT / "models" / "football" / "engine" / "step2_fixture_transition.py").read_text()
        launcher = (PROMPTS / "03_NORMAL_CHAT_LIVE.md").read_text()
        self.assertIn('live_price_action_engine_status": "NOT_IMPLEMENTED_V4"', transition)
        self.assertIn("CURRENT_LIVE_QUOTE_OBSERVED_NO_ACTION_ENGINE", transition)
        self.assertIn("no deterministic live priced-action engine", launcher)
        self.assertIn("live_price_action_engine_status=NOT_IMPLEMENTED_V4", launcher)

    def test_audit_branches_v4_from_legacy_and_honors_screenshot_mode(self):
        audit = (PROMPTS / "04_WORK_POST_SLATE_AUDIT.md").read_text()
        self.assertIn("For **current V4**, check only:", audit)
        self.assertIn("For **historical V1–V3** records", audit)
        self.assertIn("MARKET_HISTORY_NOT_RESEARCHED_USER_SCREENSHOT_ONLY", audit)
        self.assertIn("Current V4 intake does **not** consume this memory", audit)

    def test_reliability_memory_uses_current_tables_and_is_v4_non_gating(self):
        rel = (PROCEDURES / "FOOTBALL_COMPETITION_RELIABILITY_MEMORY.md").read_text()
        self.assertIn("tbl8ZRExZfMce7lqY", rel)
        self.assertIn("tblg3uz2Bvz6bcCm9", rel)
        self.assertIn("CURRENT V4 NON-GATING", rel)
        self.assertIn("do **not** consume this memory", rel)

    def test_football_a_betting_wrapper_is_historical_for_all_v4_commands(self):
        legacy = (PROCEDURES / "FOOTBALL_BETTING_PROCEDURE.md").read_text()
        self.assertIn("RETIRED FOR NEW V4 /xi AND /live", legacy)
        self.assertIn("zero", legacy.lower())
        self.assertIn("Historical model:** Football A", legacy)

    def test_actual_user_bets_remain_separate_from_shadow(self):
        report = (PROMPTS / "06_NORMAL_CHAT_REPORT.md").read_text()
        self.assertIn("Actual Bets — Current", report)
        self.assertIn("C2 shadow", report)
        self.assertIn("screenshot-only", report)


if __name__ == "__main__":
    unittest.main()
