import copy
import pathlib
import sys
import unittest

ENGINE = pathlib.Path(__file__).resolve().parents[1]
TESTS = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ENGINE))
sys.path.insert(0, str(TESTS))

from adapter import (
    ContractError,
    evaluate_observed_quote,
    run_board,
    run_decision,
    run_football_assessment,
)
from test_adapter import pair_payload
from test_board_pair import c_row, payload
from test_football_assessment_pair import football


class ActiveCRuntimeTests(unittest.TestCase):
    def test_c_board_executes(self):
        result = run_board(payload("c", c_row()))
        self.assertEqual(result["model"], "c")
        self.assertEqual(result["stage"], "board_result")
        self.assertEqual(len(result["matches"]), 1)

    def test_retired_c2_board_is_rejected(self):
        retired = payload("c2", {
            k: v for k, v in c_row().items()
            if k not in {
                "completion_mode",
                "burden_completion_quality",
                "continuation_quality",
                "opponent_leakage",
                "burden_stall_risk",
            }
        })
        retired["matches"][0]["board_state"] = "C2-FOCUS"
        with self.assertRaisesRegex(ContractError, "retired"):
            run_board(retired)

    def test_c_upper_tail_requires_explicit_transferability(self):
        row = c_row()
        row.pop("upper_tail_transferability")
        row.pop("upper_tail_transferability_basis")
        with self.assertRaisesRegex(
            ContractError,
            "independent_upper_tail requires explicit upper_tail_transferability",
        ):
            run_board(payload("c", row))

    def test_c_football_assessment_executes(self):
        result = run_football_assessment(football("c"))
        self.assertEqual(result["model"], "c")
        self.assertTrue(result["football_assessment_completed"])

    def test_retired_c2_football_assessment_is_rejected(self):
        retired = football("c")
        retired["model"] = "c2"
        with self.assertRaisesRegex(ContractError, "retired"):
            run_football_assessment(retired)

    def test_c_decision_executes(self):
        result = run_decision(pair_payload("c"))
        self.assertEqual(result["model"], "c")
        self.assertIn(result["action"], {"BET", "WAIT", "PASS"})

    def test_retired_c2_decision_is_rejected(self):
        retired = copy.deepcopy(pair_payload("c"))
        retired["model"] = "c2"
        with self.assertRaisesRegex(ContractError, "retired"):
            run_decision(retired)

    def test_observed_quote_uses_c_only(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        result = evaluate_observed_quote(c, {"line": 2.5, "odds": 1.70})
        self.assertEqual(result["model"], "c")
        self.assertFalse(result["execution_authorized"])

    def test_retired_c2_cannot_enter_observed_quote_path(self):
        retired = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        retired["model"] = "c2"
        with self.assertRaisesRegex(ContractError, "retired"):
            evaluate_observed_quote(retired, {"line": 2.5, "odds": 1.70})


if __name__ == "__main__":
    unittest.main()
