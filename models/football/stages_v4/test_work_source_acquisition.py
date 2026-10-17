"""Offline regressions for the Work acquisition transport."""
from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from datetime import datetime
from pathlib import Path
from unittest.mock import patch

MODULE = Path(__file__).parent / "tools" / "work_source_acquisition.py"
spec = importlib.util.spec_from_file_location("work_source_acquisition", MODULE)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class WorkSourceAcquisitionTests(unittest.TestCase):
    def request(self):
        return {
            "run_id": "V4-20261017-1800-20261018-0300",
            "window_start_ict": "2026-10-17T18:00:00+07:00",
            "window_end_ict": "2026-10-18T03:00:00+07:00",
        }

    def test_required_ict_utc_surfaces(self):
        _, _, keys = mod.parse_request(self.request())
        self.assertEqual(keys, [("ICT", "2026-10-17"), ("ICT", "2026-10-18"),
                                ("UTC", "2026-10-17")])

    def test_rejects_oversized_and_naive(self):
        request = self.request()
        request["window_end_ict"] = "2026-10-20T03:00:00+07:00"
        with self.assertRaises(ValueError):
            mod.parse_request(request)
        request = self.request()
        request["window_start_ict"] = "2026-10-17T18:00:00"
        with self.assertRaises(ValueError):
            mod.parse_request(request)

    def test_rejects_incomplete_or_duplicate_event_ids(self):
        with patch.object(mod, "fetch", return_value=(b'{"events":[{"id":1},{"id":1}]}', "2026-10-17T00:00:00+00:00")):
            row, raw = mod.acquire_day("2026-10-17")
        self.assertEqual(row["status"], "FETCH_FAILED")
        self.assertIsNone(raw)

    def test_saves_raw_but_never_certifies_v4(self):
        with tempfile.TemporaryDirectory() as tmp:
            request = Path(tmp) / "request.json"
            request.write_text(json.dumps(self.request()))
            out = Path(tmp) / "out"
            raw = b'{"events":[{"id":123,"homeTeam":{"name":"Home"}}]}'
            with patch.object(mod, "fetch", return_value=(raw, "2026-10-17T11:00:00+00:00")):
                self.assertEqual(mod.run(request, out), 0)
            result = json.loads((out / "acquisition-evidence.json").read_text())
            self.assertEqual(result["status"], "RAW_ACQUISITION_FETCHED_NOT_V4_READY")
            self.assertFalse(result["native_v4_executed"])
            self.assertFalse(result["source_completeness_proven"])
            self.assertEqual((out / "provider-2026-10-17.json").read_bytes(), raw)

    def test_failed_date_does_not_create_ready_receipt(self):
        with tempfile.TemporaryDirectory() as tmp:
            request = Path(tmp) / "request.json"
            request.write_text(json.dumps(self.request()))
            out = Path(tmp) / "out"
            with patch.object(mod, "acquire_day", return_value=({"status": "FETCH_FAILED"}, None)):
                self.assertEqual(mod.run(request, out), 2)
            result = json.loads((out / "acquisition-evidence.json").read_text())
            self.assertEqual(result["status"], "ACQUISITION_BLOCKED")
            self.assertFalse(result["eligible_queue_produced"])


if __name__ == "__main__":
    unittest.main()
