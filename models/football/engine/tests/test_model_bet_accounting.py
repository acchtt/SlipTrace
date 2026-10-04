import pathlib
import sys
import unittest

ENGINE_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE_DIR))

from model_bet_accounting import (  # noqa: E402
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
        "wait_resolution": kwargs.get("wait_resolution", "ASSUMED_REACHED"),
        "stake_u": kwargs.get("stake_u", 1.0),
        "user_confirmed_line": kwargs.get("user_confirmed_line"),
        "user_confirmed_odds": kwargs.get("user_confirmed_odds"),
        "user_confirmed_stake_u": kwargs.get("user_confirmed_stake_u"),
    }


class ModelBetAccountingTests(unittest.TestCase):
    def test_watch_counts_for_all_four_models(self):
        cases = [
            ("c", "C-WATCH", "WATCH_ASSUMED"),
            ("c2", "C2-WATCH", "SHADOW_WATCH_ASSUMED"),
            ("c3", "C3-WATCH", "SHADOW_WATCH_ASSUMED"),
            ("c4", "C4-WATCH", "SHADOW_WATCH_ASSUMED"),
        ]
        for model, state, basis in cases:
            terms = compile_model_bet(row(model, state, 2.5))
            self.assertEqual(terms.basis, basis)
            self.assertEqual(terms.line, 2.5)
            self.assertEqual(terms.odds, 1.65)
            self.assertEqual(terms.stake_u, 1.0)

    def test_wait_replaces_watch_for_c_c2_c3(self):
        for model, state, action, basis in [
            ("c", "C-WATCH", "C-WAIT", "WAIT_ASSUMED"),
            ("c2", "C2-WATCH", "C2-WAIT", "SHADOW_WAIT_ASSUMED"),
            ("c3", "C3-WATCH", "C3-WAIT", "SHADOW_WAIT_ASSUMED"),
        ]:
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
            self.assertEqual(terms.basis, basis)
            self.assertEqual(terms.line, 2.25)

    def test_direct_bet_replaces_wait_and_watch(self):
        terms = compile_model_bet(
            row(
                "c2",
                "C2-WATCH",
                2.5,
                "C2-BET",
                direct_line=2.75,
                direct_odds=1.82,
                wait_target_line=2.25,
                wait_min_odds=1.65,
            )
        )
        self.assertEqual(terms.basis, "SHADOW_DIRECT_BET")
        self.assertEqual(terms.line, 2.75)
        self.assertEqual(terms.odds, 1.82)

    def test_line_never_reached_removes_wait_but_watch_remains_countable(self):
        terms = compile_model_bet(
            row(
                "c",
                "C-WATCH",
                2.5,
                "C-WAIT",
                wait_target_line=2.25,
                wait_min_odds=1.65,
                wait_resolution="USER_DECLARED_NOT_REACHED",
            )
        )
        self.assertEqual(terms.basis, "WATCH_ASSUMED")
        self.assertEqual(terms.line, 2.5)

    def test_c4_watch_never_creates_website_pick(self):
        terms = compile_model_bet(row("c4", "C4-WATCH", 2.0))
        self.assertFalse(terms.creates_website_pick)
        self.assertEqual(terms.scope, "SHADOW_MODEL_ACCOUNTING")

    def test_focus_without_step2_action_is_not_changed(self):
        terms = compile_model_bet(row("c", "C-FOCUS", 2.5))
        self.assertEqual(terms.basis, "NONE")

    def test_step2_pass_does_not_erase_frozen_watch_accounting(self):
        terms = compile_model_bet(row("c3", "C3-WATCH", 2.25, "C3-PASS"))
        self.assertEqual(terms.basis, "SHADOW_WATCH_ASSUMED")

    def test_user_confirmed_wait_is_official_c_only(self):
        terms = compile_model_bet(
            row(
                "c",
                "C-WATCH",
                2.5,
                "C-WAIT",
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

    def test_asian_quarter_settlement(self):
        self.assertEqual(settle_over(3, 2.75, 1.65, 1.0)[0], "HALF_WIN")
        self.assertEqual(settle_over(2, 2.25, 1.65, 1.0)[0], "HALF_LOSS")
        self.assertEqual(settle_over(3, 2.5, 1.65, 1.0)[0], "WIN")

    def test_all_model_fixture_output(self):
        result = compile_fixture_accounting(
            {
                "match_id": "m1",
                "total_goals": 3,
                "models": [
                    row("c", "C-WATCH", 2.5),
                    row("c2", "C2-WATCH", 2.25),
                    row("c3", "C3-PASS", 2.0),
                    row("c4", "C4-WATCH", 2.75),
                ],
            }
        )
        self.assertEqual(len(result["models"]), 4)
        by_model = {r["model"]: r for r in result["models"]}
        self.assertEqual(by_model["c"]["pnl_u"], 0.65)
        self.assertEqual(by_model["c2"]["settlement"], "WIN")
        self.assertEqual(by_model["c3"]["settlement"], "NO_BET")
        self.assertEqual(by_model["c4"]["settlement"], "HALF_WIN")


if __name__ == "__main__":
    unittest.main()
