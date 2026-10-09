import json
import pathlib
import sys
import unittest

ENGINE_DIR = pathlib.Path(__file__).resolve().parents[1]
ROOT = ENGINE_DIR.parents[2]
sys.path.insert(0, str(ENGINE_DIR))

from step2_queue_guard import freeze_queue
from step2_queue_audit import audit_queue_outcomes


class October9ExceptionSnapshotTests(unittest.TestCase):
    def test_four_live_exceptions_stay_open(self):
        path = ROOT / "models/football/qa/replays/2026-10-09-kleague-live-exception-audit.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        q = data["queue_receipt"]
        self.assertEqual(q["mode"], "EXCEPTION_ONLY")
        self.assertEqual(len(q["due"]), 4)
        rebuilt = freeze_queue({
            "schema_version": "football-step2-queue-v1",
            "session_id": q["session_id"],
            "mode": "EXCEPTION_ONLY",
            "board": [],
            "activated_reserves": [],
            "user_exceptions": [
                {"match_id": x["match_id"], "user_authorization_reference": x["authorization_reference"]}
                for x in q["due"]
            ],
        })
        self.assertEqual(rebuilt, q)
        result = audit_queue_outcomes(data)
        self.assertTrue(result["all_due_accounted"])
        self.assertFalse(result["all_due_completed"])
        self.assertEqual(result["verified_decision_count"], 0)
        self.assertEqual(result["open_follow_up_count"], 4)
        self.assertEqual({x["status"] for x in result["open_follow_ups"]}, {"INTEGRITY_BLOCKED"})


if __name__ == "__main__":
    unittest.main()
