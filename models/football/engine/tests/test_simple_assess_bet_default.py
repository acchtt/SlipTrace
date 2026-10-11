import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

ENGINE = pathlib.Path(__file__).resolve().parents[1]
FOOTBALL = ENGINE.parent
sys.path.insert(0, str(ENGINE))
from test_football_assessment_pair import football


def run_portable(command, c, c2):
    with tempfile.TemporaryDirectory() as tmp:
        root = pathlib.Path(tmp)
        cp, sp = root / "c.json", root / "c2.json"
        cp.write_text(json.dumps(c), encoding="utf-8")
        sp.write_text(json.dumps(c2), encoding="utf-8")
        return subprocess.run(
            [sys.executable, str(ENGINE / "xi_portable.py"), command,
             "--c", str(cp), "--c2", str(sp)],
            text=True, capture_output=True, check=False, timeout=20,
        )


class SimpleAssessBetRoutingTests(unittest.TestCase):
    def test_assess_without_odds_executes_c_and_c2(self):
        for state, minute, score in (
            ("PREMATCH_CONFIRMED", None, None),
            ("STARTED", 2, "0-0"),
            ("STARTED", 9, "1-0"),
            ("STARTED", 16, "2-0"),
            ("HALFTIME", 45, "2-1"),
        ):
            with self.subTest(state=state, minute=minute):
                c = football("c", status=state, minute=minute, score=score)
                c2 = football("c2", status=state, minute=minute, score=score)
                response = run_portable("assess", c, c2)
                self.assertEqual(response.returncode, 0, response.stderr[-1200:])
                body = json.loads(response.stdout)
                self.assertTrue(body["ok"])
                self.assertEqual(body["engine_execution_status"],
                                 "EXECUTED_C_C2_FOOTBALL_ONLY")
                self.assertEqual(body["models_executed"], ["c", "c2"])
                self.assertFalse(body["quotes_required"])
                self.assertFalse(body["model_bets_created"])
                for model in ("c", "c2"):
                    self.assertFalse(body["results"][model]["bet_authorized"])
                    self.assertFalse(body["results"][model]["quote_requested"])
                    self.assertFalse(body["results"][model]["quote_required_for_football_assessment"])

    def test_legacy_football_pair_alias_still_works(self):
        c, c2 = football("c"), football("c2")
        for command in ("assess", "football-pair"):
            p = run_portable(command, c, c2)
            self.assertEqual(p.returncode, 0, p.stderr[-1200:])
            self.assertEqual(json.loads(p.stdout)["engine_execution_status"],
                             "EXECUTED_C_C2_FOOTBALL_ONLY")

    def test_explicit_bet_check_remains_strict(self):
        c, c2 = football("c"), football("c2")
        for cmd in ("bet-check", "pair"):
            p = run_portable(cmd, c, c2)
            self.assertNotEqual(p.returncode, 0)
            self.assertIn("stage=decision", p.stderr)

    def test_model_authority_cannot_require_quotes_for_default_assess(self):
        current = (FOOTBALL / "CURRENT_MODEL.md").read_text(encoding="utf-8")
        aliases = (FOOTBALL / "prompts" / "COMMAND_ALIASES.md").read_text(encoding="utf-8")
        simple = (FOOTBALL / "procedures" / "FOOTBALL_SIMPLE_ASSESS_AND_BET.md").read_text(encoding="utf-8")
        self.assertIn("ASSESS is the default for /xi", current)
        self.assertIn("without requesting", current)
        self.assertIn("Only explicit", current)
        self.assertIn("## Simple commands", aliases)
        self.assertIn("Only two actions", aliases)
        self.assertIn("ASSESS is the default", simple)

    def test_xi_and_live_entrypoints_read_simple_authority(self):
        for path in (
            FOOTBALL / "prompts" / "xi.md",
            FOOTBALL / "prompts" / "live.md",
            FOOTBALL / "prompts" / "02_NORMAL_CHAT_XI_ODDS.md",
            FOOTBALL / "prompts" / "03_NORMAL_CHAT_LIVE.md",
        ):
            with self.subTest(path=path):
                contents = path.read_text(encoding="utf-8")
                self.assertIn("FOOTBALL_SIMPLE_ASSESS_AND_BET.md", contents)
                self.assertIn("only if explicitly requested", contents.lower())

if __name__ == "__main__":
    unittest.main()
