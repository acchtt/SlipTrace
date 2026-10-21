import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

ENGINE = pathlib.Path(__file__).resolve().parents[1]
RUNNER = ENGINE / "xi_portable.py"
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from test_adapter import pair_payload
from test_football_assessment_pair import football


def run(command, c):
    with tempfile.TemporaryDirectory() as td:
        root = pathlib.Path(td)
        cp = root / "c.json"
        cp.write_text(json.dumps(c), encoding="utf-8")
        args = [sys.executable, str(RUNNER), command, "--c", str(cp)]
        if command in {"xi", "decision"}:
            ap = root / "authority.json"
            ap.write_text(json.dumps({
                "mode": "EXCEPTION",
                "exception_reference": "test-explicit-exception",
                "user_requested_exception": True,
            }), encoding="utf-8")
            args.extend(["--authority", str(ap)])
        proc = subprocess.run(
            args,
            text=True,
            capture_output=True,
            check=False,
        )
        return proc


class SimpleAssessBetDefaultTests(unittest.TestCase):
    def test_xi_without_odds_executes_c_football(self):
        for state, minute, score in (
            ("PREMATCH_CONFIRMED", None, None),
            ("STARTED", 12, "0-0"),
            ("HALFTIME", 45, "1-0"),
        ):
            with self.subTest(state=state):
                proc = run(
                    "xi",
                    football("c", status=state, minute=minute, score=score),
                )
                self.assertEqual(proc.returncode, 0, proc.stderr)
                out = json.loads(proc.stdout)
                self.assertEqual(out["xi_mode"], "FOOTBALL_ASSESSMENT")
                self.assertEqual(
                    out["engine_execution_status"],
                    "EXECUTED_C_FOOTBALL_ONLY",
                )
                self.assertEqual(out["model"], "c")
                self.assertEqual(out["result"]["model"], "c")

    def test_football_command_is_direct_quote_free_engine_command(self):
        proc = run("football", football("c"))
        self.assertEqual(proc.returncode, 0, proc.stderr)
        out = json.loads(proc.stdout)
        self.assertEqual(
            out["engine_execution_status"],
            "EXECUTED_C_FOOTBALL_ONLY",
        )

    def test_xi_with_decision_payload_runs_strict_c(self):
        proc = run("xi", pair_payload("c"))
        self.assertEqual(proc.returncode, 0, proc.stderr)
        out = json.loads(proc.stdout)
        self.assertEqual(out["xi_mode"], "STRICT_EXECUTABLE_PRICE_C")
        self.assertEqual(out["engine_execution_status"], "EXECUTED_C_DECISION")
        self.assertEqual(out["model"], "c")

    def test_retired_c2_is_rejected(self):
        retired = pair_payload("c")
        retired["model"] = "c2"
        proc = run("decision", retired)
        self.assertNotEqual(proc.returncode, 0)
        out = json.loads(proc.stderr)
        self.assertEqual(out["status"], "XI ENGINE CONTRACT REJECTED")
        self.assertIn("retired", out["error"].lower())


if __name__ == "__main__":
    unittest.main()
