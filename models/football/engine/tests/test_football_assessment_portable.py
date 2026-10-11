import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

ENGINE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE))
from test_football_assessment_pair import football


class PortableQuoteFreePairTests(unittest.TestCase):
    def test_generated_single_file_runtime_executes_both_unpriced(self):
        with tempfile.TemporaryDirectory() as folder:
            root = pathlib.Path(folder)
            c, c2 = root / "c.json", root / "c2.json"
            c.write_text(json.dumps(football("c")), encoding="utf-8")
            c2.write_text(json.dumps(football("c2")), encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(ENGINE / "xi_portable.py"),
                 "football-pair", "--c", str(c), "--c2", str(c2)],
                capture_output=True, text=True, check=False, timeout=15,
            )
            self.assertEqual(result.returncode, 0, result.stderr[-3000:])
            value = json.loads(result.stdout)
            self.assertTrue(value["ok"])
            self.assertEqual(value["engine_execution_status"],
                             "EXECUTED_C_C2_FOOTBALL_ONLY")
            self.assertEqual(value["models_executed"], ["c", "c2"])
            self.assertFalse(value["quotes_required"])
            self.assertFalse(value["model_bets_created"])
            self.assertFalse(value["results"]["c"]["bet_authorized"])
            self.assertEqual(value["results"]["c2"]["quote_status"],
                             "UNPRICED_NOT_REQUIRED_FOR_FOOTBALL")

    def test_original_pair_still_rejects_unpriced_payload(self):
        with tempfile.TemporaryDirectory() as folder:
            root = pathlib.Path(folder)
            c, c2 = root / "c.json", root / "c2.json"
            c.write_text(json.dumps(football("c")), encoding="utf-8")
            c2.write_text(json.dumps(football("c2")), encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(ENGINE / "xi_portable.py"),
                 "pair", "--c", str(c), "--c2", str(c2)],
                capture_output=True, text=True, check=False, timeout=15,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("must use stage=decision", result.stderr)

    def test_portable_self_check_still_pins_current_adapter_blob(self):
        result = subprocess.run(
            [sys.executable, str(ENGINE / "xi_portable.py"), "self-check"],
            capture_output=True, text=True, check=False, timeout=15,
        )
        self.assertEqual(result.returncode, 0, result.stderr[-2000:])
        self.assertIn("XI PORTABLE RUNTIME: PASS", result.stdout)


if __name__ == "__main__":
    unittest.main()
