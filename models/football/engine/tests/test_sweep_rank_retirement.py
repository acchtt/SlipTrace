"""Retired V1-V3 mechanisms must stay absent from the active engine tree."""
from __future__ import annotations

import pathlib
import unittest

ENGINE = pathlib.Path(__file__).resolve().parents[1]
FOOTBALL = ENGINE.parent
REPO = FOOTBALL.parent.parent


class SweepRankRetirementTests(unittest.TestCase):
    def test_current_router_uses_v4_without_legacy_runtime_contract(self):
        router = (FOOTBALL / "prompts" / "COMMAND_ALIASES.md").read_text(encoding="utf-8")
        current = (FOOTBALL / "CURRENT_MODEL.md").read_text(encoding="utf-8")
        self.assertIn("models/football/stages_v4/SWEEP.md", router)
        self.assertIn("models/football/stages_v4/RANK.md", router)
        self.assertIn("Football V4 only", current)
        self.assertIn("Retired V1-V3", current)
        self.assertNotIn("work_ready", router)
        self.assertNotIn("Step0 ZIP", router)

    def test_retired_engine_modules_are_physically_absent(self):
        retired = (
            "sweep_rank_pipeline.py",
            "sweep_rank_retired.py",
            "sweep_checkpoint.py",
            "capacity_replenishment.py",
            "rank_terminal_status.py",
            "repaired_handoff_normalize.py",
            "step0_portable.py",
            "step0_handoff_cli.py",
            "step0_package_cli.py",
            "goal_route_prescreen.py",
        )
        for name in retired:
            with self.subTest(name=name):
                self.assertFalse((ENGINE / name).exists(), name)

    def test_experimental_engines_live_under_trials_not_active_engine(self):
        for name in (
            "goal_burden_forecast.py",
            "goal_gate_shadow_audit.py",
            "goal_total_probabilities.py",
            "follow_funding_readiness_qa.py",
            "model_reaudit.py",
            "step2_price_aware_shadow.py",
        ):
            with self.subTest(name=name):
                self.assertFalse((ENGINE / name).exists(), name)
                self.assertTrue(
                    (FOOTBALL / "trials" / "engine_experiments" / name).exists(),
                    name,
                )

    def test_active_production_ci_does_not_execute_retired_mechanics(self):
        workflow = (
            REPO / ".github" / "workflows" / "football-step2-research-gate.yml"
        ).read_text(encoding="utf-8")
        for old in (
            "sweep_checkpoint.py",
            "capacity_replenishment.py",
            "rank_terminal_status.py",
            "repaired_handoff_normalize.py",
            "step0_handoff_cli.py",
            "step2_reconcile.py",
        ):
            with self.subTest(old=old):
                self.assertNotIn(old, workflow)


if __name__ == "__main__":
    unittest.main()
