import pathlib
import sys
import unittest

ENGINE_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE_DIR))

from runtime_probe import RuntimeProbeError, probe_stage, required_files  # noqa: E402


class RuntimeProbeTests(unittest.TestCase):
    def test_stage_manifests_include_runtime_probe(self):
        for stage in ("rank", "xi", "audit"):
            self.assertIn(
                "models/football/engine/runtime_probe.py",
                required_files(stage),
            )

    def test_rank_manifest_contains_active_board_pair(self):
        files = required_files("rank")
        self.assertIn("models/football/engine/board_pair_cli.py", files)
        self.assertNotIn("models/football/engine/board_triplet_cli.py", files)
        self.assertNotIn("models/football/engine/c4_semantic_cli.py", files)
        self.assertIn(
            "models/football/engine/repaired_handoff_normalize.py",
            files,
        )

    def test_xi_manifest_contains_pair_and_reconciliation(self):
        files = required_files("xi")
        self.assertIn("models/football/engine/xi_portable.py", files)
        self.assertIn("models/football/engine/decision_pair_cli.py", files)
        self.assertIn("models/football/engine/step2_reconcile_cli.py", files)

    def test_audit_manifest_contains_factor_calibration(self):
        files = required_files("audit")
        self.assertIn("models/football/engine/factor_calibration.py", files)
        self.assertIn("models/football/engine/factor_calibration_cli.py", files)

    def test_all_stages_include_model_accounting(self):
        for stage in ("rank", "xi", "audit"):
            self.assertIn(
                "models/football/engine/model_bet_accounting.py",
                required_files(stage),
            )
        self.assertIn(
            "models/football/engine/model_bet_accounting_cli.py",
            required_files("rank"),
        )
        self.assertIn(
            "models/football/engine/model_bet_accounting_cli.py",
            required_files("audit"),
        )

    def test_current_repo_runtime_probe_passes_all_stages(self):
        for stage in ("rank", "xi", "audit"):
            result = probe_stage(stage)
            self.assertTrue(result["ok"], result)

    def test_unknown_stage_fails_closed(self):
        with self.assertRaises(RuntimeProbeError):
            required_files("live")


if __name__ == "__main__":
    unittest.main()
