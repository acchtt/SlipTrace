"""Production /sweep and /rank retirement must be fail-closed.

Legacy pure validators remain importable for historical QA, but the old
production command entrypoints may not restart work by accident.
"""
from __future__ import annotations

import pathlib
import subprocess
import sys
import unittest

ENGINE = pathlib.Path(__file__).resolve().parents[1]
ROOT = ENGINE.parent
sys.path.insert(0, str(ENGINE))

from sweep_rank_retired import (
    ACTIVE_SWEEP_RANK_ENABLED, RETIRED_COMMANDS,
    RETIRED_STATUS, retirement_receipt,
)


class SweepRankRetirementTests(unittest.TestCase):
    def test_active_stages_are_decommissioned(self):
        self.assertFalse(ACTIVE_SWEEP_RANK_ENABLED)
        self.assertEqual(RETIRED_STATUS, "SWEEP_RANK_RETIRED")
        self.assertIn("/sweep resume", RETIRED_COMMANDS)
        self.assertIn("/rank reassess", RETIRED_COMMANDS)
        result = retirement_receipt("sweep")
        self.assertFalse(result["production_enabled"])
        self.assertFalse(result["may_resume_old_run"])
        self.assertFalse(result["may_issue_official_zip"])
        self.assertFalse(result["may_publish_rank"])

    def test_all_production_cli_entrypoints_refuse_without_input(self):
        for filename in (
            "sweep_rank_pipeline.py",
            "step0_package_cli.py",
            "step0_portable.py",
            "board_pair_cli.py",
            "rank_persistence_reconcile.py",
        ):
            with self.subTest(filename=filename):
                result = subprocess.run(
                    [sys.executable, str(ENGINE / filename)],
                    text=True, capture_output=True, timeout=8,
                )
                self.assertEqual(result.returncode, 2, result.stderr)
                self.assertIn("SWEEP_RANK_RETIRED", result.stderr)
                self.assertIn('"production_enabled": false', result.stderr)

    def test_old_launchers_retired_new_v4_routed_and_xi_independent(self):
        for name in ("00_NORMAL_CHAT_AISCORE_FETCH.md", "01_WORK_DAILY_SWEEP.md"):
            content = (ROOT / "prompts" / name).read_text(encoding="utf-8")
            with self.subTest(name=name):
                self.assertIn("RETIRED V1–V3 ENTRYPOINT ONLY", content.splitlines()[0])
                self.assertIn("V4", content.splitlines()[0])
        for name, launcher in (("sweep.md", "stages_v4/SWEEP.md"),
                               ("rank.md", "stages_v4/RANK.md")):
            content = (ROOT / "prompts" / name).read_text(encoding="utf-8")
            with self.subTest(name=name):
                self.assertIn(launcher, content)
                self.assertIn("V4", content)
        commands = (ROOT / "prompts" / "COMMAND_ALIASES.md").read_text(encoding="utf-8")
        self.assertIn("NEW V4", commands)
        self.assertIn("SWEEP_RANK_RETIRED", commands)
        self.assertIn("**/xi, /xi exception, /live, /audit and /report remain available**", commands)
        current = (ROOT / "CURRENT_MODEL.md").read_text(encoding="utf-8")
        self.assertIn("SWEEP_RANK_RETIRED", current)
        self.assertIn("ACTIVE NEW STAGES", current)
        self.assertIn("/live, /audit and /report remain available", current)

    def test_legacy_validation_functions_still_import_for_audit(self):
        from step0_handoff_cli import validate_step0_handoff
        from board_pair_cli import run_board_pair
        from sweep_checkpoint import validate_checkpoint
        self.assertTrue(callable(validate_step0_handoff))
        self.assertTrue(callable(run_board_pair))
        self.assertTrue(callable(validate_checkpoint))


if __name__ == "__main__":
    unittest.main()
