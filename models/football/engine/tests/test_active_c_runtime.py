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
from evidence_fixtures import attach_g4_evidence


class ActiveCRuntimeTests(unittest.TestCase):
    def test_c_board_executes(self):
        result = run_board(payload("c", c_row()))
        self.assertEqual(result["model"], "c")
        self.assertEqual(result["stage"], "board_result")
        self.assertEqual(len(result["matches"]), 1)

    def test_c_compiles_state_and_retains_researcher_mismatch(self):
        funded = c_row()
        funded["declared_board_state"] = "C-WATCH"
        funded["declared_board_state_basis"] = (
            "researcher attempted a manual demotion"
        )
        row = run_board(payload("c", funded))["matches"][0]
        self.assertEqual(row["board_state"], "FOCUS")
        self.assertEqual(row["declared_board_state"], "WATCH")
        self.assertTrue(row["board_state_mismatch"])
        self.assertEqual(row["declared_board_state_source"], "declared_board_state")

        unfunded = c_row()
        unfunded.update(
            home_route="WEAK",
            away_route="WEAK",
            carrier="NONE",
            carrier_self_fund=False,
            independent_upper_tail=False,
            independent_upper_tail_basis="no independent upper-tail route",
            completion_mode="CARRIER_LED",
            burden_completion_quality="LOW",
            continuation_quality="LOW",
            opponent_leakage="LOW",
            route_reliability="LOW",
            independent_route_quality="LOW",
            chance_quality="LOW",
            failure_resistance="LOW",
            declared_board_state="C-FOCUS",
            declared_board_state_basis="researcher attempted a manual promotion",
        )
        row = run_board(payload("c", unfunded))["matches"][0]
        self.assertEqual(row["board_state"], "WATCH")
        self.assertEqual(row["declared_board_state"], "FOCUS")
        self.assertTrue(row["board_state_mismatch"])

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

    def test_c_upper_tail_requires_comparable_context(self):
        row = c_row()
        row.pop("upper_tail_comparable_context_signal")
        row.pop("upper_tail_comparable_context_basis")
        with self.assertRaisesRegex(
            ContractError,
            "independent_upper_tail requires explicit "
            "upper_tail_comparable_context_signal",
        ):
            run_board(payload("c", row))

    def test_c_upper_tail_rejects_invalid_comparable_context_signal(self):
        row = c_row()
        row["upper_tail_comparable_context_signal"] = "DOMESTIC_ONLY"
        with self.assertRaisesRegex(
            ContractError,
            "upper_tail_comparable_context_signal",
        ):
            run_board(payload("c", row))

    def test_c_football_assessment_executes(self):
        result = run_football_assessment(football("c"))
        self.assertEqual(result["model"], "c")
        self.assertTrue(result["football_assessment_completed"])

    def test_g3_only_board_is_explicitly_incomplete_without_g4_contract(self):
        source = c_row()
        source["independent_upper_tail"] = False
        source["independent_upper_tail_basis"] = (
            "G3 is funded but no independent fourth-goal tail is established."
        )
        result = run_board(payload("c", source))
        row = result["matches"][0]
        self.assertTrue(row["goal3_funded"])
        self.assertFalse(row["goal4_funded"])
        self.assertEqual(row["g4_research_status"], "G4_RESEARCH_INCOMPLETE")

    def test_legacy_complete_mixed_normalizes_to_rejected_terminal(self):
        source = c_row()
        source.update(
            independent_upper_tail=False,
            independent_upper_tail_basis="completed research does not fund G4",
            g4_research_status="G4_RESEARCH_COMPLETE_MIXED",
            g4_carrier_path="MIXED",
            g4_distributed_path="FAILED",
            g4_reply_path="MIXED",
            g4_continuation_after_g3="MEDIUM",
            g4_research_basis="resolved mixed paths do not fund G4",
        )
        source = attach_g4_evidence(source)
        row = run_board(payload("c", source))["matches"][0]
        self.assertEqual(row["g4_research_status"], "G4_RESEARCH_COMPLETE_REJECTED")
        self.assertEqual(row["g4_declared_research_status"], "G4_RESEARCH_COMPLETE_MIXED")
        self.assertTrue(row["g4_status_normalized_from_mixed"])
        self.assertEqual(row["g4_path_diagnostic"], "MIXED")

    def test_board_flags_systematic_incomplete_g4_research(self):
        rows = []
        for i in range(5):
            row = c_row()
            row["match_id"] = f"g4-incomplete-{i}"
            row["independent_upper_tail"] = False
            row["independent_upper_tail_basis"] = (
                "G3 is funded but the fourth-goal investigation is unfinished."
            )
            rows.append(row)
        board = payload("c", rows[0])
        board["matches"] = rows
        result = run_board(board)
        self.assertIn("UPPER_TAIL_RESEARCH_ANOMALY", result["qa_flags"])

    def test_board_flags_operational_grade_b_saturation(self):
        rows = []
        for i in range(5):
            row = c_row()
            row["match_id"] = f"grade-b-{i}"
            row.update(
                operational_viability_grade="B",
                raw_operational_viability_grade="B",
                xi_expected="UNCERTAIN",
                market_observability="MEDIUM",
                team_news_observability="MEDIUM",
            )
            rows.append(row)
        board = payload("c", rows[0])
        board["matches"] = rows
        result = run_board(board)
        self.assertIn("OPERATIONAL_GRADE_SATURATION", result["qa_flags"])

    def test_explicit_g4_rejection_requires_structured_path_research(self):
        row = c_row()
        row["independent_upper_tail"] = False
        row["independent_upper_tail_basis"] = (
            "Completed research rejects an independently transferable fourth-goal tail."
        )
        row["g4_research_status"] = "G4_RESEARCH_COMPLETE_REJECTED"
        row["g4_research_basis"] = "All plausible fourth-goal completion paths were checked."
        with self.assertRaisesRegex(ContractError, "g4_carrier_path"):
            run_board(payload("c", row))

        row.update(
            g4_carrier_path="FAILED",
            g4_distributed_path="FAILED",
            g4_reply_path="UNAVAILABLE",
            g4_continuation_after_g3="MEDIUM",
        )
        result = run_board(payload("c", row))
        self.assertEqual(
            result["matches"][0]["g4_research_status"],
            "G4_RESEARCH_INCOMPLETE",
        )

    def test_retired_c2_football_assessment_is_rejected(self):
        retired = football("c")
        retired["model"] = "c2"
        with self.assertRaisesRegex(ContractError, "retired"):
            run_football_assessment(retired)

    def test_c_decision_executes(self):
        result = run_decision(pair_payload("c"))
        self.assertEqual(result["model"], "c")
        self.assertIn(result["action"], {"BET", "WAIT", "PASS"})

    def test_ranked_certificate_upgrade_requires_verified_new_football_evidence(self):
        upgraded = pair_payload("c")
        upgraded["context"]["frozen_board_certified_burden"] = 2.5
        upgraded["context"]["certificate_upgrade_status"] = "NOT_UPGRADED"
        upgraded["context"]["certificate_upgrade_basis"] = (
            "market showed a higher burden but no new football evidence was frozen"
        )
        with self.assertRaisesRegex(
            ContractError,
            "CERTIFICATE UPGRADE BLOCKED",
        ):
            run_decision(upgraded)

        upgraded["context"]["certificate_upgrade_status"] = (
            "VERIFIED_NEW_FOOTBALL_EVIDENCE"
        )
        upgraded["context"]["certificate_upgrade_basis"] = (
            "confirmed XI changed the carrier and upper-tail evidence relative "
            "to the frozen board"
        )
        upgraded["context"]["certificate_upgrade_new_evidence_fields"] = [
            "carrier_self_fund",
            "upper_tail_comparable_context_signal",
        ]
        result = run_decision(upgraded)
        self.assertTrue(result["certificate_upgraded"])
        self.assertEqual(
            result["frozen_board_certified_burden"], 2.5
        )

    def test_incomplete_frozen_g4_can_be_completed_without_chronologically_new_evidence(self):
        current = pair_payload("c")
        current["context"].update(
            frozen_board_certified_burden=2.5,
            frozen_board_g4_research_status="G4_RESEARCH_INCOMPLETE",
            certificate_upgrade_status="VERIFIED_CERTIFICATE_COMPLETENESS_RESEARCH",
            certificate_upgrade_basis=(
                "Completed the previously unfinished G4 investigation using "
                "certificate-relevant football evidence; market was trigger only."
            ),
            certificate_upgrade_new_evidence_fields=[
                "g4_research_status",
                "upper_tail_transferability",
                "upper_tail_comparable_context_signal",
            ],
        )
        result = run_decision(current)
        self.assertTrue(result["certificate_upgraded"])
        self.assertGreater(result["supported_line"], 2.5)
        self.assertEqual(
            result["certificate_upgrade_status"],
            "VERIFIED_CERTIFICATE_COMPLETENESS_RESEARCH",
        )

    def test_complete_frozen_g4_rejection_still_requires_genuinely_new_evidence(self):
        current = pair_payload("c")
        current["context"].update(
            frozen_board_certified_burden=2.5,
            frozen_board_g4_research_status="G4_RESEARCH_COMPLETE_REJECTED",
            certificate_upgrade_status="VERIFIED_CERTIFICATE_COMPLETENESS_RESEARCH",
            certificate_upgrade_basis="Attempted to reuse the completeness-repair path.",
            certificate_upgrade_new_evidence_fields=["g4_research_status"],
        )
        with self.assertRaisesRegex(ContractError, "CERTIFICATE UPGRADE BLOCKED"):
            run_decision(current)

    def test_market_only_field_cannot_authorize_certificate_upgrade(self):
        upgraded = pair_payload("c")
        upgraded["context"]["frozen_board_certified_burden"] = 2.5
        upgraded["context"]["certificate_upgrade_status"] = (
            "VERIFIED_NEW_FOOTBALL_EVIDENCE"
        )
        upgraded["context"]["certificate_upgrade_basis"] = (
            "higher market total triggered a recheck"
        )
        upgraded["context"]["certificate_upgrade_new_evidence_fields"] = [
            "market_history"
        ]
        with self.assertRaisesRegex(
            ContractError,
            "non-football/unsupported fields",
        ):
            run_decision(upgraded)

    def test_retired_c2_decision_is_rejected(self):
        retired = copy.deepcopy(pair_payload("c"))
        retired["model"] = "c2"
        with self.assertRaisesRegex(ContractError, "retired"):
            run_decision(retired)

    def test_observed_quote_uses_c_only(self):
        c = football(
            "c",
            status="PREMATCH_CONFIRMED",
            minute=None,
            score=None,
            event="NONE_VERIFIED",
        )
        result = evaluate_observed_quote(c, {"line": 2.5, "odds": 1.70})
        self.assertEqual(result["model"], "c")
        self.assertFalse(result["execution_authorized"])

    def test_observed_quote_cannot_upgrade_frozen_certificate_without_new_evidence(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        c["match"]["carrier_self_fund"] = True
        c["match"]["carrier_self_fund_basis"] = (
            "confirmed current carrier is independently self-funding"
        )
        c["match"]["continuation_quality"] = "HIGH"
        c["context"]["thesis_state"] = "PRESERVED"
        c["context"]["primary_mechanism_intact"] = True
        c["context"]["material_veto"] = False
        c["context"]["frozen_board_certified_burden"] = 2.5
        c["context"]["certificate_upgrade_status"] = "NOT_UPGRADED"
        with self.assertRaisesRegex(
            ContractError,
            "CERTIFICATE UPGRADE BLOCKED",
        ):
            evaluate_observed_quote(c, {"line": 3.25, "odds": 1.82})

        c["context"]["certificate_upgrade_status"] = (
            "VERIFIED_NEW_FOOTBALL_EVIDENCE"
        )
        c["context"]["certificate_upgrade_basis"] = (
            "confirmed XI materially upgraded the self-funded carrier"
        )
        c["context"]["certificate_upgrade_new_evidence_fields"] = [
            "carrier_self_fund"
        ]
        result = evaluate_observed_quote(c, {"line": 3.25, "odds": 1.82})
        self.assertGreater(result["supported_line"], 2.5)

    def test_retired_c2_cannot_enter_observed_quote_path(self):
        retired = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        retired["model"] = "c2"
        with self.assertRaisesRegex(ContractError, "retired"):
            evaluate_observed_quote(retired, {"line": 2.5, "odds": 1.70})


if __name__ == "__main__":
    unittest.main()
