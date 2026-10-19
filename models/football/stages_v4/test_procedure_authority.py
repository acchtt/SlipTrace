"""Compact active-authority regression for V4 + Football C; no network I/O."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[3]
FOOTBALL = ROOT / "models" / "football"
PROMPTS = FOOTBALL / "prompts"
STAGES = FOOTBALL / "stages_v4"
ENGINE = FOOTBALL / "engine"


class CurrentProcedureAuthorityTests(unittest.TestCase):
    def test_command_map_routes_only_to_active_v4_and_c(self):
        router = (PROMPTS / "COMMAND_ALIASES.md").read_text()
        current = (FOOTBALL / "CURRENT_MODEL.md").read_text()
        self.assertIn("models/football/stages_v4/SWEEP.md", router)
        self.assertIn("models/football/stages_v4/RANK.md", router)
        self.assertIn("Football C", current)
        self.assertIn("Retired models", current)
        self.assertIn("C2, C3 and C4", current)
        self.assertIn("Football V4 only", current)
        self.assertIn("There is no active shadow model", current)
        self.assertNotIn("work_ready", router)

    def test_sweep_acquires_complete_surfaces_before_filters(self):
        completeness = (STAGES / "source_completeness.py").read_text()
        stage = (STAGES / "stage.py").read_text()
        sweep = (STAGES / "SWEEP.md").read_text()
        for required in (
            "DATE_SURFACE_BATCH_V2",
            "DATE_SURFACE_ONLY",
            "registry_prefilter_applied",
            "terminal_sentinel",
            "provider_senior_competition_block_count",
        ):
            self.assertIn(required, completeness)
        self.assertIn("validate_source_completeness", stage)
        self.assertIn("COMPLETE PROVIDER DATE SURFACES", sweep)
        self.assertIn("CHEAP RESEARCH-PRIORITY FILTERS", sweep)

    def test_sweep_resume_is_checkpointed_and_does_not_restart_resolved_work(self):
        sweep_doc = (STAGES / "SWEEP.md").read_text()
        runner = (STAGES / "tools" / "work_sweep.py").read_text()
        self.assertIn("football-v4-sweep-research-checkpoint-v2", sweep_doc)
        self.assertIn("resume_queue", sweep_doc)
        self.assertIn("--resume-from", runner)
        self.assertIn("RESOLVED_RESEARCH", runner)
        self.assertIn("reused_match_ids", runner)
        self.assertIn("EVIDENCE_LIMITED", runner)

    def test_sweep_scope_keeps_exclusions_and_youth_exception(self):
        sweep = (STAGES / "SWEEP.md").read_text()
        registry = (STAGES / "league_registry.py").read_text()
        self.assertIn("USER_AFRICA_DOMESTIC_EXCLUSION", sweep)
        self.assertIn("AFRICAN_DOMESTIC_COUNTRIES", registry)
        self.assertIn("UEFA Youth League", sweep)
        self.assertIn("UEFA_YOUTH_LEAGUE_NAMES", registry)
        self.assertIn("Generic youth competitions remain excluded", sweep)

    def test_big_five_is_not_automatic_goal_admission(self):
        cheap = (STAGES / "cheap_sweep_filters.py").read_text()
        intake = (STAGES / "goals_first_intake.py").read_text()
        self.assertIn("TOP_FIVE_NO_AUTO_PROMOTION", cheap)
        self.assertIn("TOP_FIVE_STATUS_NOT_A_GOAL_SIGNAL", cheap)
        self.assertIn("GOAL_PRIORITY", intake)

    def test_rank_replays_source_refreshes_cohort_and_reads_back_once(self):
        stage = (STAGES / "stage.py").read_text()
        rank = (STAGES / "RANK.md").read_text()
        for required in (
            "V4_SOURCE_REPLAY_REQUIRED",
            "V4_STATUS_REFRESH_INCOMPLETE",
            "PREMATCH_WINDOW_CLOSED by current fixture status",
            "V4_RANK_PERSISTENCE_VERIFIED",
            "model_evidence_readback_verified",
        ):
            self.assertIn(required, stage)
        self.assertIn("original-source replay", rank)
        self.assertIn("full-cohort status", rank)
        self.assertIn("Step1 Engine C Result", rank)
        self.assertNotIn("Step1 Engine C2 Result JSON", rank)
        self.assertIn("does not replay", rank)
        self.assertIn("source.json/status_refresh.json again", rank)

    def test_rank_handoff_is_one_canonical_bundle(self):
        rank = (STAGES / "RANK.md").read_text()
        redirect = (PROMPTS / "rank.md").read_text()
        workflow = (
            ROOT / ".github" / "workflows" /
            "football-v4-replay-attestation.yml"
        ).read_text()
        for doc in (rank, redirect):
            self.assertIn("v4-original-source-attested-receipts", doc)
        self.assertIn("<run>-source.json", rank)
        self.assertIn("<run>-v4_sweep_ready.json", rank)
        self.assertIn("-source.json", workflow)
        self.assertIn("-rank-handoff.json", workflow)
        self.assertIn("does not search historical", rank)

    def test_routine_xi_uses_verified_rank_not_second_source_replay(self):
        guard = (ENGINE / "step2_queue_guard.py").read_text()
        self.assertIn("football-step2-queue-v2", guard)
        self.assertIn("V4_RANK_PERSISTENCE_VERIFIED", guard)
        self.assertIn("model_evidence_readback_verified", guard)
        self.assertNotIn("v4_original_source", guard)
        self.assertNotIn("v4_status_refresh", guard)
        self.assertNotIn("validate_v4_queue_authority", guard)

    def test_xi_has_one_quote_policy_and_no_wrapper_decay_rule(self):
        core = (ENGINE / "core.py").read_text()
        adapter = (ENGINE / "adapter.py").read_text()
        runner = (ENGINE / "xi_portable.py").read_text()
        self.assertIn("def evaluate_c_quote", core)
        self.assertIn('ACTIVE_MODEL = "c"', adapter)
        self.assertIn("def evaluate_observed_quote", adapter)
        self.assertIn("THIN_SHARED_MODULES", runner)
        self.assertNotIn("--c2", runner)
        self.assertNotIn("decision_pair_cli", runner)
        self.assertNotIn("MAX_ASSESSMENT_LIVE_DECAY_GAP", runner)
        self.assertNotIn("SOURCE_BLOB_SHA", runner)

    def test_screenshot_is_normal_observed_quote_and_non_executable(self):
        xi = (PROMPTS / "02_NORMAL_CHAT_XI_ODDS.md").read_text()
        reconcile = (ENGINE / "xi_assessment_reconcile.py").read_text()
        self.assertIn("USER_SCREENSHOT_ONLY", xi)
        self.assertIn("evaluated line/odds", xi)
        self.assertIn("evaluated_line", reconcile)
        self.assertIn("evaluated_odds", reconcile)
        self.assertNotIn("USER_SCREENSHOT_ONLY_JSON=", reconcile)

    def test_live_uses_same_football_path_without_transition_machine(self):
        live = (PROMPTS / "03_NORMAL_CHAT_LIVE.md").read_text()
        self.assertIn("same football-assessment runtime as /xi", live)
        self.assertIn("There is no active step2_fixture_transition", live)
        self.assertIn("LIVE_PRICE_BURDEN_COMPARISON_ONLY", live)

    def test_no_synthetic_watch_or_unresolved_wait_exposure(self):
        accounting = (ENGINE / "model_bet_accounting.py").read_text()
        current = (FOOTBALL / "CURRENT_MODEL.md").read_text()
        for forbidden in (
            "WATCH_ASSUMED",
            "SHADOW_WATCH_ASSUMED",
            "WAIT_ASSUMED",
            "SHADOW_WAIT_ASSUMED",
        ):
            self.assertNotIn(forbidden, accounting)
        self.assertIn("WATCH creates no model bet", current)
        self.assertIn("Unresolved WAIT creates no model bet", current)

    def test_active_production_spec_has_no_retired_rule_drift(self):
        production = (FOOTBALL / "production" / "FOOTBALL_C.md").read_text()
        core = (ENGINE / "core.py").read_text()
        for forbidden in (
            "15-fixture normal Work admission cap",
            "every frozen `C-WATCH` is also a model-accounting bet",
            "WAIT assumed-exposure accounting record",
            "AISCORE SENIOR UNIVERSE",
        ):
            with self.subTest(forbidden=forbidden):
                self.assertNotIn(forbidden, production)
        self.assertIn("There is no predictive board-size target", production)
        self.assertIn("unresolved WAIT -> no model bet", production)
        self.assertIn("gap is at most **0.25 goals**", production)
        self.assertIn("MAX_C_PREGOAL_UNSUPPORTED_WAIT_DROP = 0.25", core)

    def test_legacy_procedure_files_are_hard_retired(self):
        retired = (
            "FOOTBALL_MATCH_SWEEP_AND_RESEARCH_PROCEDURE.md",
            "FOOTBALL_COMPACT_SWEEP_WORK_BUDGET.md",
            "FOOTBALL_CAPACITY_REPLENISHMENT.md",
            "FOOTBALL_OPERATIONAL_VIABILITY_GATE.md",
            "FOOTBALL_PRE_DECISION_SPEC.md",
            "FOOTBALL_STEP2_EXECUTION_SPEC.md",
            "FOOTBALL_XI_MARKET_FIRST_INTAKE.md",
        )
        procedures = FOOTBALL / "procedures"
        for name in retired:
            with self.subTest(name=name):
                first = (procedures / name).read_text().splitlines()[0]
                self.assertIn("RETIRED", first)

    def test_active_wait_authority_blocks_material_decay_target(self):
        current = (FOOTBALL / "CURRENT_MODEL.md").read_text()
        xi = (PROMPTS / "02_NORMAL_CHAT_XI_ODDS.md").read_text()
        production = (FOOTBALL / "production" / "FOOTBALL_C.md").read_text()
        for doc in (current, xi, production):
            self.assertIn("0.25", doc)
            self.assertIn("0.50", doc)
        self.assertIn("do not manufacture a pre-goal decay WAIT", (ENGINE / "core.py").read_text())

    def test_actual_user_bets_are_user_pnl_authority(self):
        current = (FOOTBALL / "CURRENT_MODEL.md").read_text()
        routing = (
            FOOTBALL / "google_sheets" / "ACTIVE_STORE_ROUTING.md"
        ).read_text()
        self.assertIn("Actual Bets — Current", current)
        self.assertIn("Actual Bets — Current", routing)
        self.assertIn("user P/L", routing)


if __name__ == "__main__":
    unittest.main()
