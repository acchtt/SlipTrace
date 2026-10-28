"""The /xi runtime index is a durable fallback, never a fake Sheets readback."""
import unittest

from xi_runtime_backend import _assessment_index


class AssessmentIndexTests(unittest.TestCase):
    def test_exception_user_screenshot_is_reconcilable_without_fake_fill(self):
        request = {
            "request_id": "XI-EXC-NEFTCHI-001",
            "authority": {"mode": "EXCEPTION"},
            "c_football": {
                "evidence_epoch_id": "E-NEFTCHI",
                "match": {"match_id": "1873570"},
                "context": {
                    "assessment_at_utc": "2026-10-26T13:33:55+00:00",
                    "fixture_status": "PREMATCH_CONFIRMED",
                    "score": None, "match_minute": None,
                },
            },
            "screenshot_quote": {
                "capture_reference": "user-neftchi-screenshot",
                "observed_at_utc": "2026-10-26T13:33:40+00:00",
            },
        }
        runtime = {
            "decision_state_persistence": {"row": {
                "Assessment ID": "XI-C-E-NEFTCHI",
                "Evaluated Line": 2.75,
                "Evaluated Odds": 1.77,
            }},
            "price_check": {
                "evidence": {"visible_ladder": [
                    {"line": 2.5, "odds": 1.61},
                    {"line": 2.75, "odds": 1.77},
                ]},
                "model": {"conditional_action": "PASS"},
            },
        }
        got = _assessment_index(request, runtime)
        self.assertEqual(got["match_id"], "1873570")
        self.assertEqual(got["authority_mode"], "EXCEPTION")
        self.assertEqual(got["evaluated_line"], 2.75)
        self.assertEqual(len(got["visible_user_quote_ladder"]), 2)
        self.assertFalse(got["decision_state_readback_verified"])
        self.assertFalse(got["real_bet_fill_verified"])
        self.assertTrue(got["decision_state_persistence_required"])

    def test_empty_priced_fields_are_not_synthetic(self):
        got = _assessment_index({
            "request_id": "XI-UNPRICED", "authority": {"mode": "RANKED"},
            "c_football": {
                "evidence_epoch_id": "A",
                "match": {"match_id": "m1"},
                "context": {"assessment_at_utc": "2026-10-26T09:00:00+00:00"},
            },
        }, {"decision_state_persistence": {"row": {"Assessment ID": "XI-A"}}})
        self.assertIsNone(got["evaluated_odds"])
        self.assertIsNone(got["screenshot_capture_reference"])
        self.assertFalse(got["real_bet_fill_verified"])


if __name__ == "__main__":
    unittest.main()
