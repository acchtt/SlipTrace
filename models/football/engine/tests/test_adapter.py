import pathlib
import sys
import unittest

ENGINE_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE_DIR))

from adapter import ContractError, run_board, run_decision  # noqa: E402


def match(match_id="m1", **overrides):
    row = {
        "match_id": match_id,
        "operational_viability_grade": "A",
        "xi_expected": "YES",
        "market_observability": "HIGH",
        "team_news_observability": "HIGH",
        "operational_viability_reason": "reliable XI/news and executable totals expected",
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
        "tournament_incentive_required": False,
        "tournament_format_status": "NOT_APPLICABLE",
        "competition_stage": "NOT_APPLICABLE",
        "competition_format": "NOT_APPLICABLE",
        "draw_resolution": "NOT_APPLICABLE",
        "aggregate_state": "NOT_APPLICABLE",
        "qualification_state": "NOT_APPLICABLE",
        "simultaneous_results_status": "NOT_APPLICABLE",
        "simultaneous_results_note": "NOT_APPLICABLE",
        "home_incentive": "NOT_APPLICABLE",
        "away_incentive": "NOT_APPLICABLE",
        "tiebreak_margin_relevance": "NOT_APPLICABLE",
        "incentive_effect": "NOT_APPLICABLE",
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

    def test_missing_operational_gate_fails(self):
        row = match()
        row.pop("operational_viability_grade")
        with self.assertRaises(ContractError):
            run_board(
                {
                    "schema_version": "football-engine-v1",
                    "stage": "board",
                    "model": "c",
                    "matches": [row],
                }
            )

    def test_low_observability_fixture_is_blocked(self):
        with self.assertRaisesRegex(
            ContractError,
            "ASSESSMENT BLOCKED — LOW OPERATIONAL OBSERVABILITY",
        ):
            run_board(
                {
                    "schema_version": "football-engine-v1",
                    "stage": "board",
                    "model": "c",
                    "matches": [
                        match(
                            operational_viability_grade="C",
                            xi_expected="NO",
                            market_observability="LOW",
                            team_news_observability="LOW",
                        )
                    ],
                }
            )

    def test_grade_a_requires_expected_xi(self):
        with self.assertRaisesRegex(
            ContractError,
            "operational grade A requires xi_expected=YES",
        ):
            run_board(
                {
                    "schema_version": "football-engine-v1",
                    "stage": "board",
                    "model": "c",
                    "matches": [match(xi_expected="UNCERTAIN")],
                }
            )

    def test_grade_b_is_capped_at_reserve(self):
        result = run_board(
            {
                "schema_version": "football-engine-v1",
                "stage": "board",
                "model": "c",
                "matches": [
                    match(
                        operational_viability_grade="B",
                        xi_expected="UNCERTAIN",
                        market_observability="MEDIUM",
                        carrier="STRONG",
                        board_state="C-FOCUS",
                    )
                ],
            }
        )
        self.assertEqual(result["matches"][0]["follow_lane"], "RESERVE")
        self.assertEqual(result["follow_count"], 0)
        self.assertEqual(result["reserve_count"], 1)

    def test_missing_tournament_gate_fails(self):
        row = match()
        row.pop("tournament_incentive_required")
        with self.assertRaises(ContractError):
            run_board(
                {
                    "schema_version": "football-engine-v1",
                    "stage": "board",
                    "model": "c",
                    "matches": [row],
                }
            )

    def test_required_tournament_block_must_not_be_na(self):
        with self.assertRaises(ContractError):
            run_board(
                {
                    "schema_version": "football-engine-v1",
                    "stage": "board",
                    "model": "c",
                    "matches": [match(tournament_incentive_required=True)],
                }
            )

    def test_limited_tournament_block_is_blocked(self):
        row = match(
            tournament_incentive_required=True,
            tournament_format_status="LIMITED",
            competition_stage="GROUP D ROUND 6",
            competition_format="GROUP",
            draw_resolution="90-minute group result",
            aggregate_state="NOT A TWO-LEG TIE",
            qualification_state="UNKNOWN",
            simultaneous_results_status="UNKNOWN",
            simultaneous_results_note="qualification and tiebreak impact unresolved",
            home_incentive="UNKNOWN",
            away_incentive="UNKNOWN",
            tiebreak_margin_relevance="UNKNOWN",
            incentive_effect="UNKNOWN",
        )
        with self.assertRaisesRegex(
            ContractError,
            "ASSESSMENT BLOCKED — TOURNAMENT INCENTIVE UNRESOLVED",
        ):
            run_board(
                {
                    "schema_version": "football-engine-v1",
                    "stage": "board",
                    "model": "c",
                    "matches": [row],
                }
            )

    def test_verified_format_with_unknown_tiebreak_is_blocked(self):
        row = match(
            tournament_incentive_required=True,
            tournament_format_status="VERIFIED",
            competition_stage="GROUP D ROUND 6",
            competition_format="GROUP",
            draw_resolution="90-minute group result",
            aggregate_state="NOT A TWO-LEG TIE",
            qualification_state="top two advance; current exact need verified",
            simultaneous_results_status="VERIFIED",
            simultaneous_results_note="other group match impact checked",
            home_incentive="WIN_PREFERRED",
            away_incentive="MUST_WIN",
            tiebreak_margin_relevance="UNKNOWN",
            incentive_effect="MIXED",
        )
        with self.assertRaisesRegex(
            ContractError,
            "ASSESSMENT BLOCKED — TOURNAMENT INCENTIVE UNRESOLVED",
        ):
            run_board(
                {
                    "schema_version": "football-engine-v1",
                    "stage": "board",
                    "model": "c",
                    "matches": [row],
                }
            )

    def test_complete_tournament_block_passes(self):
        row = match(
            tournament_incentive_required=True,
            tournament_format_status="VERIFIED",
            competition_stage="GROUP FINAL ROUND",
            competition_format="GROUP",
            draw_resolution="draw qualifies home",
            aggregate_state="NOT A TWO-LEG TIE",
            qualification_state="home qualifies with draw; away must win",
            simultaneous_results_status="VERIFIED",
            simultaneous_results_note="simultaneous group result impact checked",
            home_incentive="DRAW_ACCEPTABLE",
            away_incentive="MUST_WIN",
            tiebreak_margin_relevance="YES",
            incentive_effect="MIXED",
        )
        result = run_board(
            {
                "schema_version": "football-engine-v1",
                "stage": "board",
                "model": "c",
                "matches": [row],
            }
        )
        self.assertTrue(result["matches"][0]["tournament_incentive_required"])
        self.assertEqual(result["matches"][0]["incentive_effect"], "MIXED")

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
                    "tournament_incentive_rechecked": False,
                    "tournament_incentive_recheck_status": "NOT_APPLICABLE",
                },
            }
        )
        self.assertEqual(result["action"], "BET")

    def test_tournament_decision_requires_recheck(self):
        row = match(
            board_state="C-FOCUS",
            tournament_incentive_required=True,
            tournament_format_status="VERIFIED",
            competition_stage="KNOCKOUT",
            competition_format="TWO_LEG",
            draw_resolution="extra time if aggregate level",
            aggregate_state="home trails by one",
            qualification_state="winner on aggregate advances",
            simultaneous_results_status="NOT_APPLICABLE",
            simultaneous_results_note="no simultaneous result affects this tie",
            home_incentive="MUST_WIN",
            away_incentive="PROTECT_AGGREGATE",
            tiebreak_margin_relevance="NO",
            incentive_effect="MIXED",
        )
        with self.assertRaises(ContractError):
            run_decision(
                {
                    "schema_version": "football-engine-v1",
                    "stage": "decision",
                    "model": "c",
                    "match": row,
                    "context": {
                        "board_state": "C-FOCUS",
                        "thesis_state": "PRESERVED",
                        "quote": {"line": 2.5, "odds": 1.70},
                        "tournament_incentive_rechecked": False,
                        "tournament_incentive_recheck_status": "VERIFIED",
                    },
                }
            )

    def test_tournament_decision_limited_recheck_is_blocked(self):
        row = match(
            board_state="C-FOCUS",
            tournament_incentive_required=True,
            tournament_format_status="VERIFIED",
            competition_stage="KNOCKOUT",
            competition_format="TWO_LEG",
            draw_resolution="extra time if aggregate level",
            aggregate_state="home trails by one",
            qualification_state="winner on aggregate advances",
            simultaneous_results_status="NOT_APPLICABLE",
            simultaneous_results_note="no simultaneous result affects this tie",
            home_incentive="MUST_WIN",
            away_incentive="PROTECT_AGGREGATE",
            tiebreak_margin_relevance="NO",
            incentive_effect="MIXED",
        )
        with self.assertRaisesRegex(
            ContractError,
            "DECISION BLOCKED — TOURNAMENT INCENTIVE UNRESOLVED",
        ):
            run_decision(
                {
                    "schema_version": "football-engine-v1",
                    "stage": "decision",
                    "model": "c",
                    "match": row,
                    "context": {
                        "board_state": "C-FOCUS",
                        "thesis_state": "PRESERVED",
                        "quote": {"line": 2.5, "odds": 1.70},
                        "tournament_incentive_rechecked": True,
                        "tournament_incentive_recheck_status": "LIMITED",
                    },
                }
            )

    def test_tournament_decision_with_recheck_passes(self):
        row = match(
            board_state="C-FOCUS",
            tournament_incentive_required=True,
            tournament_format_status="VERIFIED",
            competition_stage="KNOCKOUT",
            competition_format="TWO_LEG",
            draw_resolution="extra time if aggregate level",
            aggregate_state="home trails by one",
            home_incentive="MUST_WIN",
            away_incentive="PROTECT_AGGREGATE",
            tiebreak_margin_relevance="NO",
            incentive_effect="MIXED",
        )
        result = run_decision(
            {
                "schema_version": "football-engine-v1",
                "stage": "decision",
                "model": "c",
                "match": row,
                "context": {
                    "board_state": "C-FOCUS",
                    "thesis_state": "PRESERVED",
                    "quote": {"line": 2.5, "odds": 1.70},
                    "tournament_incentive_rechecked": True,
                    "tournament_incentive_recheck_status": "VERIFIED",
                },
            }
        )
        self.assertTrue(result["tournament_incentive_rechecked"])

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
                    "quote": {"line": 2.0, "odds": 1.90},
                    "tournament_incentive_rechecked": False,
                    "tournament_incentive_recheck_status": "NOT_APPLICABLE",
                },
            }
        )
        self.assertEqual(result["action"], "PASS")
        self.assertNotEqual(result["selection_floor"], "CLEAR")


if __name__ == "__main__":
    unittest.main()
