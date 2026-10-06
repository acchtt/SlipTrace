import pathlib
import sys
import unittest

ENGINE_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE_DIR))

from adapter import ContractError  # noqa: E402
from board_pair_cli import run_board_pair  # noqa: E402


COMMON = {
    "match_id": "alpha",
    "kickoff_ict": "2026-10-04T19:00:00+07:00",
    "operational_viability_grade": "A",
    "raw_operational_viability_grade": "A",
    "competition_reliability_state": "UNPROVEN",
    "competition_reliability_reason": "fewer than 3 countable operational observations",
    "competition_reliability_manual_override": "NONE",
    "demoted_probation": False,
    "xi_expected": "YES",
    "market_observability": "HIGH",
    "team_news_observability": "HIGH",
    "operational_viability_reason": "reliable XI/news and executable totals expected",
    "common_evidence_basis": "one shared Step-1 football research freeze",
    "home_route": "STRONG",
    "away_route": "USABLE",
    "carrier": "STRONG",
    "route_reliability": "HIGH",
    "independent_route_quality": "HIGH",
    "chance_quality": "HIGH",
    "failure_resistance": "HIGH",
    "xi_robustness": "MEDIUM",
    "evidence_confidence": "HIGH",
    "burden_protection": "HIGH",
    "main_failure": "no unresolved material failure",
    "h2h_state": "REVIEWED_NOT_MATERIAL",
    "h2h_effect": "NOT_MATERIAL",
    "h2h_transferability": "VERIFIED",
    "h2h_current_corroboration": "NOT_APPLICABLE",
    "h2h_material_effect": False,
    "h2h_basis": "historical matchup evidence reviewed",
    "carrier_self_fund": True,
    "carrier_self_fund_basis": "strong carrier has repeated independent scoring capacity",
    "independent_upper_tail": True,
    "independent_upper_tail_basis": "current non-market evidence supports upper-tail scoring",
    "failure_attacks_route": False,
    "failure_attacks_route_basis": "main failure does not remove the primary scoring route",
    "material_suppression": False,
    "material_suppression_basis": "no current material suppression trigger",
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
}


def c_row():
    return {
        **COMMON,
        "supported_line": 2.5,
        "supported_line_basis": "C independently supports O2.5",
        "completion_mode": "CARRIER_LED",
        "burden_completion_quality": "HIGH",
        "continuation_quality": "HIGH",
        "opponent_leakage": "MEDIUM",
        "burden_stall_risk": "LOW",
        "board_state": "C-FOCUS",
        "board_state_basis": "C completion path supports focus",
    }


def c2_row():
    return {
        **COMMON,
        "supported_line": 2.25,
        "supported_line_basis": "C2 independently supports O2.25",
        "board_state": "C2-FOCUS",
        "board_state_basis": "C2 route-quality floor supports focus",
    }


def payload(model, row):
    return {
        "schema_version": "football-engine-v1",
        "stage": "board",
        "model": model,
        "matches": [row],
    }


class BoardPairTests(unittest.TestCase):
    def test_pair_reconciles_same_common_evidence(self):
        result = run_board_pair(
            payload("c", c_row()),
            payload("c2", c2_row()),
        )
        self.assertTrue(result["common_evidence_reconciled"])
        self.assertEqual(result["board_engine_execution_status"], "EXECUTED_C_C2_BOARDS")
        self.assertEqual(result["models_executed"], ["c", "c2"])
        self.assertEqual(result["match_count"], 1)

    def test_common_evidence_drift_fails(self):
        row = c2_row()
        row["chance_quality"] = "MEDIUM"
        with self.assertRaisesRegex(ContractError, "COMMON EVIDENCE DRIFT"):
            run_board_pair(payload("c", c_row()), payload("c2", row))

    def test_missing_common_evidence_basis_fails_closed(self):
        row = c2_row()
        del row["common_evidence_basis"]
        with self.assertRaisesRegex(ContractError, "COMMON EVIDENCE INCOMPLETE"):
            run_board_pair(payload("c", c_row()), payload("c2", row))

    def test_ranked_universe_mismatch_fails(self):
        row = c2_row()
        row["match_id"] = "different"
        with self.assertRaisesRegex(ContractError, "RANKED ELIGIBLE UNIVERSE MISMATCH"):
            run_board_pair(payload("c", c_row()), payload("c2", row))

    def test_c_policy_field_leak_into_c2_fails(self):
        row = c2_row()
        row["completion_mode"] = "TWO_SIDED"
        with self.assertRaisesRegex(ContractError, "C POLICY FIELD LEAK"):
            run_board_pair(payload("c", c_row()), payload("c2", row))


if __name__ == "__main__":
    unittest.main()
