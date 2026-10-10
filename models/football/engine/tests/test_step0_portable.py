"""Guard Step0 one-file runtime, correctness and source freshness in CI."""
import hashlib
import importlib.util
import json
import pathlib
import sys
import tempfile
import unittest

ENGINE = pathlib.Path(__file__).resolve().parents[1]
ROOT = ENGINE.parents[2]
BUNDLE = ENGINE / "step0_portable.py"


class PortableStep0Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location("step0_portable_test", BUNDLE)
        assert spec and spec.loader
        cls.portable = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.portable)

    def test_exact_source_freshness_and_self_check(self):
        for rel, blob in self.portable.SOURCE_BLOB_SHA.items():
            data = (ROOT / rel).read_bytes()
            got = hashlib.sha1(
                b"blob " + str(len(data)).encode("ascii") + b"\0" + data
            ).hexdigest()
            self.assertEqual(got, blob, rel)
        result = self.portable.self_check()
        self.assertTrue(result["ok"], result)
        self.assertEqual(result["module_count"], 6)

    def test_bangladesh_scope_rejected_inside_portable(self):
        self.portable._load()
        from sweep_competition_scope import classify_competition
        x = classify_competition({
            "competition_name": "Bangladesh Premier League",
            "competition_kind": "DOMESTIC_LEAGUE",
            "country": "Bangladesh",
        })
        self.assertEqual(x["lane"], "SCOPE_EXCLUDED")

    def test_portable_package_same_guarded_success_and_failure(self):
        self.portable._load()
        from step0_package_cli import package, Step0HandoffError
        from test_step0_package_cli import scenario
        handoff, run = scenario()
        with tempfile.TemporaryDirectory() as d:
            root = pathlib.Path(d)
            h = root / "STEP0_HANDOFF.json"
            t = root / "AISCORE_FIXTURES_TEST.txt"
            proof = root / "proof.json"
            output = root / "AISCORE_FIXTURES_TEST.zip"
            h.write_text(json.dumps(handoff))
            proof.write_text(json.dumps(run))
            t.write_text("validated senior Work handoff")
            result = package(h, t, proof, output)
            self.assertEqual(result["status"], "STEP0 WORK ZIP VALIDATED")
            self.assertTrue(output.exists())
            output.unlink()
            handoff["work_ready"] = False
            h.write_text(json.dumps(handoff))
            with self.assertRaises(Step0HandoffError):
                package(h, t, proof, output)
            self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
