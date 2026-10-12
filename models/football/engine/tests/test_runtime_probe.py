import pathlib
import sys
import unittest

ENGINE_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE_DIR))

from runtime_probe import RuntimeProbeError, probe_stage, required_files  # noqa: E402


class RuntimeProbeTests(unittest.TestCase):
    def test_stage_manifests_include_runtime_probe(self):
        for stage in ("sweep", "rank", "xi", "audit"):
            self.assertIn(
                "models/football/engine/runtime_probe.py",
                required_files(stage),
            )

    def test_sweep_and_rank_manifests_contain_current_v4_stage_not_retired_step0_stack(self):
        for stage in ("sweep", "rank"):
            files = required_files(stage)
            for filename in (
                "models/football/stages_v4/stage.py",
                "models/football/stages_v4/league_registry.py",
                "models/football/stages_v4/discovery_goal_gate.py",
                "models/football/stages_v4/goals_first_intake.py",
                "models/football/stages_v4/source_completeness.py",
                "models/football/engine/board_pair_cli.py",
                "models/football/engine/goal_route_prescreen.py",
            ):
                self.assertIn(filename, files)
            for retired in (
                "models/football/engine/sweep_intake_evidence.py",
                "models/football/engine/step0_handoff_cli.py",
                "models/football/engine/coverage_manifest.py",
                "models/football/engine/capacity_replenishment.py",
                "models/football/engine/rank_terminal_status.py",
                "models/football/engine/repaired_handoff_normalize.py",
            ):
                self.assertNotIn(retired, files)

    def test_xi_manifest_contains_pair_and_reconciliation(self):
        files = required_files("xi")
        self.assertIn("models/football/engine/xi_portable.py", files)
        self.assertIn("models/football/engine/decision_pair_cli.py", files)
        self.assertIn("models/football/engine/step2_reconcile_cli.py", files)

    def test_audit_manifest_contains_factor_calibration(self):
        files = required_files("audit")
        self.assertIn("models/football/engine/factor_calibration.py", files)
        self.assertIn("models/football/engine/factor_calibration_cli.py", files)

    def test_model_accounting_loaded_only_where_current_stage_uses_it(self):
        for stage in ("sweep", "rank"):
            self.assertNotIn(
                "models/football/engine/model_bet_accounting.py",
                required_files(stage),
            )
        self.assertIn(
            "models/football/engine/model_bet_accounting.py",
            required_files("xi"),
        )
        self.assertIn(
            "models/football/engine/model_bet_accounting.py",
            required_files("audit"),
        )
        self.assertIn(
            "models/football/engine/model_bet_accounting_cli.py",
            required_files("audit"),
        )

    def test_current_repo_runtime_probe_passes_all_stages(self):
        for stage in ("sweep", "rank", "xi", "audit"):
            result = probe_stage(stage)
            self.assertTrue(result["ok"], result)

    def test_unknown_stage_fails_closed(self):
        with self.assertRaises(RuntimeProbeError):
            required_files("live")


if __name__ == "__main__":
    unittest.main()
