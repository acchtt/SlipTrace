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
