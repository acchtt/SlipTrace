import copy
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from goal_burden_forecast import GoalForecastError, validate_forecast
from goal_gate_shadow_audit import GateAuditError, audit


def forecast():
    return {
        "schema_version": "football-step1-goal-burden-v1",
        "match_id": "m1",
        "evidence_epoch_id": "m1-pre-20261010",
        "forecast_frozen_at_utc": "2026-10-10T11:00:00+07:00",
        "kickoff_utc": "2026-10-10T16:00:00+07:00",
        "market_independent_forecast": True,
        "forecast_status": "QUANTIFIED",
        "home": {
            "central": 1.65, "low": 1.0, "high": 2.3,
            "basis": "Home side's healthy attackers create repeated open-play entries.",
            "evidence_urls": ["https://club.example.org/home"],
        },
        "away": {
            "central": 1.15, "low": 0.6, "high": 1.7,
            "basis": "Away side's progression and set pieces support a second route.",
            "evidence_urls": ["https://club.example.org/away"],
        },
        "declared_total": 2.8,
        "goal_three_mechanism": "Two routes with at least one repeatable carrier",
        "goal_four_mechanism": "Requires improved finishing and open transitions",
        "failure_scenario": "Tied control tempo after first goal",
    }


def factors():
    return {
        "home_route": "STRONG", "away_route": "USABLE",
        "carrier": "USABLE",
        "route_reliability": "HIGH",
        "independent_route_quality": "HIGH",
        "chance_quality": "MEDIUM",
        "failure_resistance": "HIGH",
        "carrier_self_fund": False,
        "independent_upper_tail": False,
        "material_suppression": False,
        "failure_attacks_route": False,
        "completion_mode": "TWO_SIDED",
        "burden_completion_quality": "MEDIUM",
        "continuation_quality": "HIGH",
        "opponent_leakage": "MEDIUM",
        "burden_stall_risk": "MEDIUM",
    }


def gate(model="c", **overrides):
    row = {
        "match_id": "m1",
        "evidence_epoch_id": "m1-pre-20261010",
        "model": model,
        "freeze_status": "PROSPECTIVE_VERIFIED",
        "frozen_at_utc": "2026-10-10T11:00:00+07:00",
        "kickoff_utc": "2026-10-10T16:00:00+07:00",
        "selected_line": 2.25,
        "frozen_factors": factors(),
        "observed_ft_total_goals": 3,
    }
    row.update(overrides)
    return row


class GoalBurdenForecastTests(unittest.TestCase):
    def test_two_team_forecast_and_market_compared_without_gate(self):
        row = forecast()
        row["market"] = {
            "center": 3.75,
            "source_url": "https://odds.example.org/fixture",
            "observed_at_utc": "2026-10-10T11:15:00+07:00",
        }
        got = validate_forecast(row)
        self.assertAlmostEqual(got["expected_total"], 2.8)
        self.assertAlmostEqual(got["market_comparison"]["market_gap"], -0.95)
        self.assertEqual(got["market_comparison"]["status"], "RECHECK_REQUIRED")
        self.assertTrue(got["advisory_only"])
        row["market"]["conflict_recheck_note"] = "Bookmaker higher than our estimate; recheck projected service and likely control"
        got = validate_forecast(row)
        self.assertEqual(got["market_comparison"]["status"], "COMPARE_ONLY")

    def test_evidence_limited_never_invents_numeric_total(self):
        row = forecast()
        row["forecast_status"] = "EVIDENCE_LIMITED"
        row["limitation_reason"] = "Missing independently reliable scoring-role evidence"
        for team in ("home", "away"):
            for field in ("central", "low", "high"):
                row[team].pop(field)
        row.pop("declared_total")
        out = validate_forecast(row)
        self.assertIsNone(out["expected_total"])
        self.assertEqual(out["forecast_status"], "EVIDENCE_LIMITED")

    def test_limitation_cannot_include_made_up_numbers(self):
        row = forecast()
        row["forecast_status"] = "EVIDENCE_LIMITED"
        row["limitation_reason"] = "No observed evidence"
        with self.assertRaisesRegex(GoalForecastError, "cannot imply numerical"):
            validate_forecast(row)

    def test_total_sum_and_frozen_clock_enforced(self):
        row = forecast()
        row["declared_total"] = 3.8
        with self.assertRaisesRegex(GoalForecastError, "sum"):
            validate_forecast(row)
        row = forecast()
        row["forecast_frozen_at_utc"] = row["kickoff_utc"]
        with self.assertRaisesRegex(GoalForecastError, "prospective"):
            validate_forecast(row)

    def test_no_fake_source_or_market_based_forecast(self):
        row = forecast()
        row["home"]["evidence_urls"] = ["http://not-secure.example.org"]
        with self.assertRaisesRegex(GoalForecastError, "https"):
            validate_forecast(row)
        row = forecast()
        row["market_independent_forecast"] = False
        with self.assertRaisesRegex(GoalForecastError, "independent"):
            validate_forecast(row)


class ShadowRuleAuditTests(unittest.TestCase):
    def test_matched_c_c2_gate_only_with_distinct_policy(self):
        rows = [gate("c"), gate("c2")]
        report = audit({"schema_version": "football-goal-gate-ablation-v1", "frozen_rows": rows})
        self.assertEqual(report["independent_verified_c_c2_matched_epochs"], 1)
        self.assertEqual(report["counts"]["c"]["gate_disagreements"], 1)
        self.assertEqual(report["counts"]["c2"]["gate_disagreements"], 1)
        self.assertEqual(report["counts"]["c"]["retrospective_disagreement_settlements"], {"WIN": 1})
        self.assertFalse(report["rows"][0]["bet_authorized"])
        self.assertIsNone(report["rows"][0]["actual_user_bet"])

    def test_no_c2_snapshot_means_no_paired_claim(self):
        report = audit({"schema_version": "football-goal-gate-ablation-v1", "frozen_rows": [gate("c")]})
        self.assertEqual(report["independent_verified_c_c2_matched_epochs"], 0)
        self.assertEqual(report["counts"]["c2"]["n"], 0)

    def test_c_legacy_low_burden_only(self):
        older = gate("c", selected_line=2.5)
        report = audit({"schema_version": "football-goal-gate-ablation-v1", "frozen_rows": [older]})
        self.assertEqual(report["counts"]["c"]["gate_disagreements"], 0)

    def test_stale_or_duplicate_snapshots_fail(self):
        stale = gate("c", frozen_at_utc="2026-10-10T17:00:00+07:00")
        with self.assertRaisesRegex(GateAuditError, "after kickoff"):
            audit({"schema_version": "football-goal-gate-ablation-v1", "frozen_rows": [stale]})
        with self.assertRaisesRegex(GateAuditError, "duplicate"):
            audit({"schema_version": "football-goal-gate-ablation-v1", "frozen_rows": [gate(), gate()]})

    def test_untimed_historical_excluded_from_confirmatory_pair(self):
        rows = [
            gate("c", freeze_status="HISTORICAL_FROZEN_UNTIMED", frozen_at_utc=None),
            gate("c2", freeze_status="HISTORICAL_FROZEN_UNTIMED", frozen_at_utc=None),
        ]
        report = audit({"schema_version": "football-goal-gate-ablation-v1", "frozen_rows": rows})
        self.assertEqual(report["independent_verified_c_c2_matched_epochs"], 0)
        self.assertEqual(report["unpaired_or_unverified_epochs"], 1)

    def test_retired_and_bad_model_rejected(self):
        with self.assertRaisesRegex(GateAuditError, "retired"):
            audit({"schema_version": "football-goal-gate-ablation-v1", "frozen_rows": [gate("c3")]})


if __name__ == "__main__":
    unittest.main()
