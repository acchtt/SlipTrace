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
        self.assertIn("without searching for any replacement odds", wrapper)
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

    def test_actual_user_bets_remain_separate_from_shadow(self):
        report = (PROMPTS / "06_NORMAL_CHAT_REPORT.md").read_text()
        self.assertIn("Actual Bets — Current", report)
        self.assertIn("C2 shadow", report)
        self.assertIn("screenshot-only", report)


if __name__ == "__main__":
    unittest.main()
