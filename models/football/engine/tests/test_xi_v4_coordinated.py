"""Coordinated regression for the post-C2 single-model production chain."""

from __future__ import annotations

import copy
import pathlib
import sys
import unittest

ENGINE = pathlib.Path(__file__).resolve().parents[1]
TESTS = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ENGINE))
sys.path.insert(0, str(TESTS))

from adapter import ContractError, run_board, run_decision, run_football_assessment
from model_bet_accounting import ModelBetAccountingError, compile_fixture_accounting
from test_adapter import pair_payload
from test_board_pair import c_row, payload
from test_football_assessment_pair import football


class CoordinatedSingleCRegression(unittest.TestCase):
    def test_one_model_chain_is_consistent(self):
        board = run_board(payload("c", c_row()))
        self.assertEqual(board["model"], "c")
        self.assertNotIn("models_executed", board)

        football_result = run_football_assessment(
            football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        )
        self.assertEqual(football_result["model"], "c")
        self.assertTrue(football_result["football_assessment_completed"])

        decision = run_decision(pair_payload("c"))
        self.assertEqual(decision["model"], "c")

        accounting = compile_fixture_accounting({
            "match_id": decision["match_id"],
            "models": [{
                "model": "c",
                "board_state": "C-FOCUS",
                "supported_line": decision["supported_line"],
                "step2_action": "C-" + decision["action"],
                "direct_line": decision.get("model_accounting_line"),
                "direct_odds": decision.get("model_accounting_odds"),
                "wait_target_line": decision.get("wait_target_line"),
                "wait_min_odds": decision.get("wait_min_odds"),
            }],
        })
        self.assertEqual(accounting["roster"], "ACTIVE_C")
        self.assertEqual([x["model"] for x in accounting["models"]], ["c"])

    def test_retired_c2_cannot_reenter_any_active_adapter_stage(self):
        board = payload("c", c_row())
        board["model"] = "c2"
        with self.assertRaisesRegex(ContractError, "retired"):
            run_board(board)

        assessment = football(
            "c", status="PREMATCH_CONFIRMED", minute=None, score=None
        )
        assessment["model"] = "c2"
        with self.assertRaisesRegex(ContractError, "retired"):
            run_football_assessment(assessment)

        decision = copy.deepcopy(pair_payload("c"))
        decision["model"] = "c2"
        with self.assertRaisesRegex(ContractError, "retired"):
            run_decision(decision)

    def test_retired_c2_cannot_enter_active_accounting_roster(self):
        with self.assertRaisesRegex(
            ModelBetAccountingError,
            "active accounting permits Football C only",
        ):
            compile_fixture_accounting({
                "match_id": "m1",
                "models": [
                    {
                        "model": "c",
                        "board_state": "C-WATCH",
                        "supported_line": 2.5,
                        "step2_action": None,
                    },
                    {
                        "model": "c2",
                        "board_state": "C2-WATCH",
                        "supported_line": 2.5,
                        "step2_action": None,
                    },
                ],
            })


if __name__ == "__main__":
    unittest.main()
