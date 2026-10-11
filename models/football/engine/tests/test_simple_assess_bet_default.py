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

    def test_single_xi_assesses_c_and_c2_without_odds(self):
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
                p = run_portable("xi", c, c2)
                self.assertEqual(p.returncode, 0, p.stderr[-2500:])
                out = json.loads(p.stdout)
                self.assertEqual(out["xi_mode"], "FOOTBALL_ASSESSMENT")
                self.assertEqual(out["engine_execution_status"],
                                 "EXECUTED_C_C2_FOOTBALL_ONLY")
                self.assertFalse(out["quotes_required"])
                self.assertFalse(out["model_bets_created"])

    def test_single_xi_automatically_uses_verified_priced_payload(self):
        from test_adapter import pair_payload
        c, c2 = pair_payload("c"), pair_payload("c2")
        p = run_portable("xi", c, c2)
        self.assertEqual(p.returncode, 0, p.stderr[-2500:])
        out = json.loads(p.stdout)
        self.assertEqual(out["xi_mode"], "FOOTBALL_AND_PRICE_CHECK")
        self.assertEqual(out["engine_execution_status"], "EXECUTED_C_C2_PAIR")
        self.assertEqual(out["models_executed"], ["c", "c2"])

    def test_one_xi_cannot_mix_football_and_priced_epochs(self):
        from test_adapter import pair_payload
        p = run_portable("xi", football("c"), pair_payload("c2"))
        self.assertNotEqual(p.returncode, 0)
        self.assertIn("same /xi mode", p.stderr)

    def test_one_xi_priced_offer_remains_safeguarded(self):
        from test_adapter import pair_payload
        c, c2 = pair_payload("c"), pair_payload("c2")
        c["context"]["quote_revalidated"] = False
        c2["context"]["quote_revalidated"] = False
        p = run_portable("xi", c, c2)
        self.assertNotEqual(p.returncode, 0)
        self.assertIn("QUOTE NOT REVALIDATED", p.stderr)
        c = pair_payload("c")
        c2 = pair_payload("c2")
        c["context"]["fixture_status"] = "STARTED"
        c2["context"]["fixture_status"] = "STARTED"
        p = run_portable("xi", c, c2)
        self.assertNotEqual(p.returncode, 0)
        self.assertIn("NOT CONFIRMED PREMATCH", p.stderr)

    def test_single_command_authority_and_entrypoints(self):
        current = (FOOTBALL / "CURRENT_MODEL.md").read_text(encoding="utf-8")
        aliases = (FOOTBALL / "prompts" / "COMMAND_ALIASES.md").read_text(encoding="utf-8")
        simple = (FOOTBALL / "procedures" / "FOOTBALL_SIMPLE_ASSESS_AND_BET.md").read_text(encoding="utf-8")
        self.assertIn("one assessment, just as before", current)
        self.assertIn("one", simple.lower())
        self.assertIn("no extra user step", simple.lower())
        self.assertIn("without asking", aliases)
        self.assertIn("Single /xi command", simple)
        for path in (
            FOOTBALL / "prompts" / "xi.md",
            FOOTBALL / "prompts" / "live.md",
            FOOTBALL / "prompts" / "02_NORMAL_CHAT_XI_ODDS.md",
            FOOTBALL / "prompts" / "03_NORMAL_CHAT_LIVE.md",
        ):
            with self.subTest(path=path):
                text = path.read_text(encoding="utf-8")
                self.assertIn("FOOTBALL_SIMPLE_ASSESS_AND_BET.md", text)
                self.assertNotIn("Only explicit /bet or /xi bet requests", text)


if __name__ == "__main__":
    unittest.main()
