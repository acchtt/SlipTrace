import pathlib
import sys
import unittest

ENGINE_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE_DIR))

from adapter import ContractError, run_board, run_decision  # noqa: E402


def match(match_id="m1", **overrides):
    row = {
        "match_id": match_id,
        "home_route": "STRONG",
        "away_route": "USABLE",
        "carrier": "USABLE",
        "route_reliability": "HIGH",
        "independent_route_quality": "HIGH",
        "chance_quality": "HIGH",
        "failure_resistance": "HIGH",
        "xi_robustness": "MEDIUM",
        "evidence_confidence": "HIGH",
        "burden_protection": "HIGH",
        "supported_line": 2.5,
        "board_state": "C2-FOCUS",
    }
    row.update(overrides)
    return row


class BoardContractTests(unittest.TestCase):
    def test_board_is_ranked_and_floor_is_computed(self):
        result = run_board(
            {
                "schema_version": "football-engine-v1",
                "stage": "board",
                "model": "c2",
                "matches": [
                    match("weak", route_reliability="MEDIUM"),
                    match("strong"),
                ],
            }
        )
        self.assertEqual(result["matches"][0]["match_id"], "strong")
        self.assertEqual(
            result["matches"][0]["selection_floor"],
            "CLEAR",
        )

    def test_bad_schema_fails(self):
        with self.assertRaises(ContractError):
            run_board(
                {
                    "schema_version": "wrong",
                    "stage": "board",
                    "model": "c",
                    "matches": [match()],
                }
            )


class DecisionContractTests(unittest.TestCase):
    def test_c_decision_is_computed_from_structured_input(self):
        result = run_decision(
            {
                "schema_version": "football-engine-v1",
                "stage": "decision",
                "model": "c",
                "match": match(board_state="C-FOCUS"),
                "context": {
                    "board_state": "C-FOCUS",
                    "thesis_state": "PRESERVED",
                    "quote": {"line": 2.5, "odds": 1.70},
                    "top_ranked_focus": True,
                },
            }
        )
        self.assertEqual(result["action"], "BET")

    def test_c2_floor_blocks_weak_protected_line(self):
        result = run_decision(
            {
                "schema_version": "football-engine-v1",
                "stage": "decision",
                "model": "c2",
                "match": match(
                    home_route="USABLE",
                    away_route="WEAK",
                    carrier="USABLE",
                ),
                "context": {
                    "board_state": "C2-WATCH",
                    "thesis_state": "PRESERVED",
                    "quote": {"line": 2.0, "odds": 1.90}
                },
            }
        )
        self.assertEqual(result["action"], "PASS")
        self.assertNotEqual(result["selection_floor"], "CLEAR")


if __name__ == "__main__":
    unittest.main()
