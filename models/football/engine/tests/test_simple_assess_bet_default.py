import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

ENGINE = pathlib.Path(__file__).resolve().parents[1]
FOOTBALL = ENGINE.parent
sys.path.insert(0, str(ENGINE))

from test_adapter import pair_payload
from test_football_assessment_pair import football


def run(command, c, c2):
    with tempfile.TemporaryDirectory() as tmp:
        root = pathlib.Path(tmp)
        cp, c2p = root / "c.json", root / "c2.json"
        cp.write_text(json.dumps(c), encoding="utf-8")
        c2p.write_text(json.dumps(c2), encoding="utf-8")
        return subprocess.run(
            [sys.executable, str(ENGINE / "xi_portable.py"), command,
             "--c", str(cp), "--c2", str(c2p)],
            text=True, capture_output=True, check=False, timeout=20,
        )


class SimpleAssessBetRoutingTests(unittest.TestCase):
    def test_xi_without_odds_executes_c_and_c2_football(self):
        for state, minute, score in (
            ("PREMATCH_CONFIRMED", None, None),
            ("STARTED", 2, "0-0"),
            ("STARTED", 16, "2-0"),
            ("HALFTIME", 45, "2-1"),
        ):
            with self.subTest(state=state):
                proc = run(
                    "xi",
                    football("c", status=state, minute=minute, score=score),
                    football("c2", status=state, minute=minute, score=score),
                )
                self.assertEqual(proc.returncode, 0, proc.stderr[-1200:])
                out = json.loads(proc.stdout)
                self.assertEqual(out["xi_mode"], "FOOTBALL_ASSESSMENT")
                self.assertEqual(
                    out["engine_execution_status"],
                    "EXECUTED_C_C2_FOOTBALL_ONLY",
                )
                self.assertEqual(out["models_executed"], ["c", "c2"])
                self.assertFalse(out["quotes_required"])
                self.assertFalse(out["model_bets_created"])

    def test_football_pair_is_the_direct_quote_free_engine_command(self):
        proc = run("football-pair", football("c"), football("c2"))
        self.assertEqual(proc.returncode, 0, proc.stderr[-1200:])
        out = json.loads(proc.stdout)
        self.assertEqual(
            out["engine_execution_status"], "EXECUTED_C_C2_FOOTBALL_ONLY"
        )

    def test_pair_requires_decision_payloads(self):
        proc = run("pair", football("c"), football("c2"))
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("stage=decision", proc.stderr)

    def test_xi_with_decision_payloads_runs_strict_pair(self):
        proc = run("xi", pair_payload("c"), pair_payload("c2"))
        self.assertEqual(proc.returncode, 0, proc.stderr[-2000:])
        out = json.loads(proc.stdout)
        self.assertEqual(out["xi_mode"], "STRICT_EXECUTABLE_PRICE_PAIR")
        self.assertEqual(out["engine_execution_status"], "EXECUTED_C_C2_PAIR")
        self.assertEqual(out["models_executed"], ["c", "c2"])

    def test_one_xi_cannot_mix_football_and_decision_stages(self):
        proc = run("xi", football("c"), pair_payload("c2"))
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("same /xi stage", proc.stderr)

    def test_strict_decision_safeguards_still_apply(self):
        c, c2 = pair_payload("c"), pair_payload("c2")
        c["context"]["quote_revalidated"] = False
        c2["context"]["quote_revalidated"] = False
        proc = run("xi", c, c2)
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("QUOTE NOT REVALIDATED", proc.stderr)

    def test_active_documents_describe_one_user_xi_command(self):
        current = (FOOTBALL / "CURRENT_MODEL.md").read_text(encoding="utf-8")
        aliases = (
            FOOTBALL / "prompts" / "COMMAND_ALIASES.md"
        ).read_text(encoding="utf-8")
        simple = (
            FOOTBALL / "procedures" / "FOOTBALL_SIMPLE_ASSESS_AND_BET.md"
        ).read_text(encoding="utf-8")
        self.assertIn("one football assessment, one quote policy", current)
        self.assertIn("/xi is one command", aliases)
        self.assertIn("Football comes first. Price is optional.", simple)
        self.assertIn("No bet price checked", simple)
        self.assertNotIn("Only explicit /bet", aliases)


if __name__ == "__main__":
    unittest.main()
