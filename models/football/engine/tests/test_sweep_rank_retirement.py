"""Retired V1-V3 stages remain dormant while current commands route to V4."""
from __future__ import annotations

import pathlib
import sys
import unittest

ENGINE = pathlib.Path(__file__).resolve().parents[1]
FOOTBALL = ENGINE.parent
REPO = FOOTBALL.parent.parent
sys.path.insert(0, str(ENGINE))

from sweep_rank_retired import ACTIVE_SWEEP_RANK_ENABLED, RETIRED_STATUS


class SweepRankRetirementTests(unittest.TestCase):
    def test_old_pipeline_tombstone_stays_off(self):
        self.assertFalse(ACTIVE_SWEEP_RANK_ENABLED)
        self.assertEqual(RETIRED_STATUS, "SWEEP_RANK_RETIRED")

    def test_current_router_uses_v4_without_legacy_runtime_contract(self):
        router = (
            FOOTBALL / "prompts" / "COMMAND_ALIASES.md"
        ).read_text(encoding="utf-8")
        current = (FOOTBALL / "CURRENT_MODEL.md").read_text(encoding="utf-8")
        self.assertIn("models/football/stages_v4/SWEEP.md", router)
        self.assertIn("models/football/stages_v4/RANK.md", router)
        self.assertIn("Football V4 only", current)
        self.assertIn("Retired V1-V3", router)
        self.assertNotIn("work_ready", router)
        self.assertNotIn("Step0 ZIP", router)

    def test_old_launcher_documents_are_explicitly_retired(self):
        for name in (
            "00_NORMAL_CHAT_AISCORE_FETCH.md",
            "01_WORK_DAILY_SWEEP.md",
        ):
            text = (FOOTBALL / "prompts" / name).read_text(encoding="utf-8")
            with self.subTest(name=name):
                self.assertIn("RETIRED", text.splitlines()[0])

    def test_active_production_ci_does_not_execute_retired_mechanics(self):
        workflow = (
            REPO / ".github" / "workflows" /
            "football-step2-research-gate.yml"
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
