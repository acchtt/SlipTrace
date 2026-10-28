"""Custom line review cannot fabricate odds or a prematch execution window."""
import unittest

from xi_portable import _unquoted_custom_line_review


class CustomLineReviewTests(unittest.TestCase):
    def test_rizespor_supported_lower_goal3_is_unquoted_not_booked(self):
        output = _unquoted_custom_line_review(
            {"custom_lines_available": True},
            [{"line": 3.0, "odds": 1.81}, {"line": 3.25, "odds": 2.06}],
            {"supported_line": 2.5, "action": "PASS"},
            "PREMATCH_CONFIRMED",
        )
        self.assertEqual(output["status"], "UNQUOTED_CUSTOM_LINE_REVIEW")
        self.assertEqual(output["candidate_line"], 2.5)
        self.assertIsNone(output["candidate_odds"])
        self.assertTrue(output["requires_user_confirmed_quote"])
        self.assertFalse(output["execution_authorized"])

    def test_started_exception_never_invents_old_quote(self):
        output = _unquoted_custom_line_review(
            {}, [{"line": 3.0, "odds": 1.8}],
            {"supported_line": 2.5, "action": "PASS"},
            "STARTED",
        )
        self.assertEqual(output["status"], "STARTED_MATCH_CUSTOM_LINE_NOT_PREMATCH_EXECUTABLE")
        self.assertFalse(output["execution_authorized"])

    def test_no_cert_never_becomes_act(self):
        output = _unquoted_custom_line_review(
            {"custom_lines_available": True},
            [{"line": 2.75, "odds": 1.77}],
            {"supported_line": None, "action": "PASS"},
            "PREMATCH_CONFIRMED",
        )
        self.assertEqual(output["status"], "NO_FUNDED_CUSTOM_LINE")
        self.assertFalse(output["execution_authorized"])

    def test_visible_lower_line_must_be_evaluated_as_visible(self):
        output = _unquoted_custom_line_review(
            {"custom_lines_available": True},
            [{"line": 2.5, "odds": 1.61}, {"line": 2.75, "odds": 1.77}],
            {"supported_line": 2.5, "action": "PASS"},
            "PREMATCH_CONFIRMED",
        )
        self.assertEqual(output["status"], "CUSTOM_LINE_NOT_BELOW_VISIBLE_LADDER")


if __name__ == "__main__":
    unittest.main()
