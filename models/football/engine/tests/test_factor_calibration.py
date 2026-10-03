import sys
import unittest
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE_DIR))

from factor_calibration import (  # noqa: E402
    analyze,
    observation_result,
    parse_observation,
    same_kickoff_ablation,
    trace_score,
)


def row(match_id="a", **overrides):
    data = {
        "observation_id": f"B1:{match_id}",
        "board_id": "B1",
        "match_id": match_id,
        "competition": "Test League",
        "kickoff_ict": "2026-10-04T01:00:00+07:00",
        "c_rank": 1,
        "lane": "FOLLOW",
        "supported_line": 2.5,
        "home_route": "STRONG",
        "away_route": "USABLE",
        "carrier": "STRONG",
        "carrier_self_fund": True,
        "independent_upper_tail": True,
        "route_reliability": "HIGH",
        "independent_route_quality": "HIGH",
        "chance_quality": "HIGH",
        "failure_resistance": "HIGH",
        "xi_robustness": "HIGH",
        "evidence_confidence": "HIGH",
        "burden_protection": "HIGH",
        "completion_mode": "MIXED",
        "burden_completion_quality": "HIGH",
        "continuation_quality": "HIGH",
        "opponent_leakage": "MEDIUM",
        "burden_stall_risk": "LOW",
        "failure_attacks_route": False,
        "material_suppression": False,
        "total_goals": 4,
        "completion_materialized": "YES",
        "continuation_materialized": "YES",
        "stall_endpoint_observed": "NO",
    }
    data.update(overrides)
    return data


class FactorCalibrationTests(unittest.TestCase):
    def test_trace_score_is_transparent_and_non_market(self):
        a = parse_observation(row())
        self.assertEqual(trace_score(a), 8.5)

    def test_quarter_line_support_settlement_is_recorded(self):
        a = parse_observation(row(supported_line=2.75, total_goals=3))
        result = observation_result(a)
        self.assertEqual(result["support_settlement"], "HALF_WIN")
        self.assertEqual(result["support_value"], 0.5)

    def test_missing_frozen_field_fails(self):
        data = row()
        data.pop("continuation_quality")
        with self.assertRaisesRegex(ValueError, "missing calibration fields"):
            parse_observation(data)

    def test_continuation_ablation_can_expose_priority_inversion(self):
        higher = parse_observation(
            row(
                "higher",
                c_rank=1,
                continuation_quality="HIGH",
                burden_stall_risk="MEDIUM",
                total_goals=2,
            )
        )
        lower = parse_observation(
            row(
                "lower",
                c_rank=2,
                continuation_quality="MEDIUM",
                burden_stall_risk="LOW",
                total_goals=4,
            )
        )
        changes = same_kickoff_ablation([higher, lower], "continuation_quality")
        self.assertEqual(len(changes), 1)
        self.assertEqual(changes[0]["original_top"], "higher")
        self.assertEqual(changes[0]["ablated_top"], "lower")
        self.assertEqual(changes[0]["ablation_delta"], 2.0)

    def test_analyzer_excludes_ineligible_rows_from_buckets(self):
        good = parse_observation(row("good"))
        old = parse_observation(
            row(
                "old",
                eligible=False,
                contamination_reason="factor not prospectively frozen",
            )
        )
        result = analyze([good, old])
        self.assertEqual(result["observation_count"], 2)
        self.assertEqual(result["eligible_count"], 1)
        self.assertEqual(
            result["factor_buckets"]["continuation_quality"]["HIGH"]["n"],
            1,
        )


if __name__ == "__main__":
    unittest.main()
