from __future__ import annotations

import json
import pathlib
import tempfile
import unittest

ENGINE = pathlib.Path(__file__).resolve().parents[1]
import sys
sys.path.insert(0, str(ENGINE))

import xi_runtime_backend
from tests.test_xi_user_screenshot_only import football, snapshot


class XIRuntimeBackendTests(unittest.TestCase):
    def test_on_demand_screenshot_executes_shared_runtime(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        request = {
            "schema_version": xi_runtime_backend.REQUEST_SCHEMA,
            "request_id": "XI-test-1",
            "c_football": c,
            "authority": {"mode": "EXCEPTION", "exception_reference": "test-user-exception"},
            "screenshot_quote": snapshot(c),
        }
        result = xi_runtime_backend.execute(request)
        self.assertTrue(result["ok"])
        self.assertEqual(
            result["runtime"]["engine_execution_status"],
            "EXECUTED_C_FOOTBALL_ONLY",
        )
        self.assertEqual(
            result["runtime"]["price_check"]["status"],
            "OBSERVED_QUOTE_EVALUATED",
        )

    def test_contract_error_is_persisted_not_analysis_only(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        bad = snapshot(c)
        bad["match_id"] = "wrong"
        request = {
            "schema_version": xi_runtime_backend.REQUEST_SCHEMA,
            "request_id": "XI-test-2",
            "c_football": c,
            "authority": {"mode": "EXCEPTION", "exception_reference": "test-user-exception"},
            "screenshot_quote": bad,
        }
        result = xi_runtime_backend.execute(request)
        # xi_portable preserves football assessment and marks only the observed
        # quote invalid, which is still a real runtime result.
        self.assertTrue(result["ok"])
        self.assertEqual(
            result["runtime"]["price_check"]["status"],
            "OBSERVED_QUOTE_INVALID",
        )

    def test_request_envelope_filename_must_match_id(self):
        with tempfile.TemporaryDirectory() as td:
            root = pathlib.Path(td)
            c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
            req = root / "different.json"
            out = root / "result.json"
            req.write_text(json.dumps({
                "schema_version": xi_runtime_backend.REQUEST_SCHEMA,
                "request_id": "XI-test-3",
                "c_football": c,
                "authority": {"mode": "EXCEPTION", "exception_reference": "test-user-exception"},
            }))
            self.assertEqual(xi_runtime_backend.run(req, out), 0)
            result = json.loads(out.read_text())
            self.assertFalse(result["ok"])
            self.assertEqual(result["failure_class"], "REQUEST_ENVELOPE")

    def test_ranked_fixture_without_sealed_receipt_fails_closed(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        result = xi_runtime_backend.execute({
            "schema_version": xi_runtime_backend.REQUEST_SCHEMA,
            "request_id": "XI-test-no-rank",
            "c_football": c,
            "screenshot_quote": snapshot(c),
        })
        self.assertFalse(result["ok"])
        self.assertEqual(result["status"], "RANK_RECEIPT_REQUIRED")

    def test_ranked_fixture_cannot_silently_override_frozen_c_evidence(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        frozen = dict(c["match"])
        package = {
            "status": "V4_RANK_PERSISTENCE_VERIFIED",
            "native_rank": {
                "run_id": "V4-test-rank",
                "integrity_sha256": "sealed-test-hash",
                "board": {"matches": [{
                    "match_id": frozen["match_id"],
                    "board_state": "FOCUS", "supported_line": 2.5,
                }]},
                "frozen_model_input": {"matches": [frozen]},
            },
        }
        c["match"]["board_state"] = "C-WATCH"
        result = xi_runtime_backend.execute({
            "schema_version": xi_runtime_backend.REQUEST_SCHEMA,
            "request_id": "XI-test-ranked-override",
            "c_football": c,
            "authority": {
                "mode": "RANKED", "match_id": frozen["match_id"],
                "verified_rank_package": package,
                "material_evidence_updates": [],
            },
        })
        self.assertFalse(result["ok"])
        self.assertEqual(result["status"], "RANK_RECEIPT_REQUIRED")
        self.assertIn("undeclared override", result["error"])


if __name__ == "__main__":
    unittest.main()
