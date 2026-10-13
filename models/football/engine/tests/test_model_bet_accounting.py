import pathlib
import sys
import unittest

ENGINE_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE_DIR))

from model_bet_accounting import (
    ModelBetAccountingError,
    compile_fixture_accounting,
    compile_model_bet,
    settle_over,
)


def row(model, state, line, action=None, **kwargs):
    return {
        "model": model,
        "board_state": state,
        "supported_line": line,
        "step2_action": action,
        "direct_line": kwargs.get("direct_line"),
        "direct_odds": kwargs.get("direct_odds"),
        "wait_target_line": kwargs.get("wait_target_line"),
        "wait_min_odds": kwargs.get("wait_min_odds"),
        "wait_resolution": kwargs.get("wait_resolution", "UNRESOLVED"),
        "stake_u": kwargs.get("stake_u", 1.0),
        "user_confirmed_line": kwargs.get("user_confirmed_line"),
        "user_confirmed_odds": kwargs.get("user_confirmed_odds"),
        "user_confirmed_stake_u": kwargs.get("user_confirmed_stake_u"),
    }


class ModelBetAccountingTests(unittest.TestCase):
    def test_watch_never_creates_synthetic_exposure(self):
        for model, state in (
            ("c", "C-WATCH"),
            ("c2", "C2-WATCH"),
            ("c3", "C3-WATCH"),
            ("c4", "C4-WATCH"),
        ):
            with self.subTest(model=model):
                terms = compile_model_bet(row(model, state, 2.5))
                self.assertEqual(terms.basis, "NONE")
                self.assertIsNone(terms.line)
                self.assertIsNone(terms.odds)
                self.assertEqual(terms.stake_u, 0.0)
                self.assertFalse(terms.synthetic_price)

    def test_unresolved_wait_is_plan_not_exposure(self):
        for model, state, action in (
            ("c", "C-WATCH", "C-WAIT"),
            ("c2", "C2-WATCH", "C2-WAIT"),
        ):
            with self.subTest(model=model):
                terms = compile_model_bet(
                    row(
                        model,
                        state,
                        2.5,
                        action,
                        wait_target_line=2.25,
                        wait_min_odds=1.65,
                    )
                )
                self.assertEqual(terms.basis, "NONE")
                self.assertEqual(terms.stake_u, 0.0)

    def test_direct_bet_uses_actual_observed_terms(self):
        terms = compile_model_bet(
            row(
                "c2",
                "C2-WATCH",
                2.5,
                "C2-BET",
                direct_line=2.75,
                direct_odds=1.82,
            )
        )
        self.assertEqual(terms.basis, "SHADOW_DIRECT_BET")
        self.assertEqual(terms.line, 2.75)
        self.assertEqual(terms.odds, 1.82)
        self.assertFalse(terms.synthetic_price)

    def test_user_confirmed_wait_is_official_c_only(self):
        terms = compile_model_bet(
            row(
                "c",
                "C-WATCH",
                2.5,
                "C-WAIT",
                wait_target_line=2.25,
                wait_min_odds=1.65,
                wait_resolution="USER_CONFIRMED",
                user_confirmed_line=2.25,
                user_confirmed_odds=1.9,
                user_confirmed_stake_u=1.5,
            )
        )
        self.assertEqual(terms.basis, "WAIT_USER_CONFIRMED")
        self.assertEqual(terms.line, 2.25)
        self.assertEqual(terms.odds, 1.9)
        self.assertEqual(terms.stake_u, 1.5)

        with self.assertRaisesRegex(
            ModelBetAccountingError, "official Football C"
        ):
            compile_model_bet(
                row(
                    "c2",
                    "C2-WATCH",
                    2.5,
                    "C2-WAIT",
                    wait_target_line=2.25,
                    wait_min_odds=1.65,
                    wait_resolution="USER_CONFIRMED",
                    user_confirmed_line=2.25,
                    user_confirmed_odds=1.9,
                )
            )

    def test_asian_quarter_settlement(self):
        self.assertEqual(settle_over(3, 2.75, 1.65, 1.0)[0], "HALF_WIN")
        self.assertEqual(settle_over(2, 2.25, 1.65, 1.0)[0], "HALF_LOSS")
        self.assertEqual(settle_over(3, 2.5, 1.65, 1.0)[0], "WIN")

    def test_active_fixture_watch_rows_settle_as_no_bet(self):
        result = compile_fixture_accounting(
            {
                "match_id": "m1",
                "total_goals": 3,
                "models": [
                    row("c", "C-WATCH", 2.5),
                    row("c2", "C2-WATCH", 2.25),
                ],
            }
        )
        self.assertEqual(result["roster"], "ACTIVE_C_C2")
        by_model = {item["model"]: item for item in result["models"]}
        self.assertEqual(by_model["c"]["settlement"], "NO_BET")
        self.assertEqual(by_model["c2"]["settlement"], "NO_BET")

    def test_active_fixture_rejects_retired_rows(self):
        with self.assertRaisesRegex(
            ModelBetAccountingError,
            "active accounting permits C/C2 only",
        ):
            compile_fixture_accounting(
                {
                    "match_id": "m1",
                    "models": [
                        row("c", "C-WATCH", 2.5),
                        row("c2", "C2-WATCH", 2.25),
                        row("c3", "C3-PASS", 2.0),
                    ],
                }
            )

    def test_historical_roster_remains_readable_without_synthetic_repricing(self):
        result = compile_fixture_accounting(
            {
                "match_id": "m1",
                "historical_roster": True,
                "total_goals": 3,
                "models": [
                    row("c", "C-WATCH", 2.5),
                    row("c2", "C2-WATCH", 2.25),
                    row("c3", "C3-PASS", 2.0),
                    row("c4", "C4-WATCH", 2.75),
                ],
            }
        )
        self.assertEqual(result["roster"], "HISTORICAL_C_C2_C3_C4")
        self.assertTrue(all(
            item["settlement"] == "NO_BET" for item in result["models"]
        ))


if __name__ == "__main__":
    unittest.main()
