import pathlib
import sys
import unittest

ENGINE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE))

from adapter import ContractError, run_football_assessment, run_decision
from decision_pair_cli import run_football_pair
from test_adapter import match, decision_context


def football(model, *, status="STARTED", score="1-0", minute=5, event="GOAL"):
    m = match(
        board_state="C-FOCUS" if model == "c" else "C2-FOCUS",
        carrier="STRONG", carrier_self_fund=False, independent_upper_tail=True,
        continuation_quality="MEDIUM",
    )
    if model == "c2":
        for field in ("completion_mode", "burden_completion_quality",
                      "continuation_quality", "opponent_leakage",
                      "burden_stall_risk"):
            m.pop(field, None)
    return {
        "schema_version": "football-engine-v1",
        "stage": "football_assessment",
        "model": model,
        "evidence_epoch_id": "current-started-minute-five",
        "match": m,
        "context": {
            "assessment_at_utc": "2026-10-11T05:05:00+00:00",
            "fixture_status": status,
            "score": score, "match_minute": minute,
            "material_event_since_frozen": event,
            "board_state": "C-FOCUS" if model == "c" else "C2-FOCUS",
            "thesis_state": "UNKNOWN",
            "primary_mechanism_intact": None,
            "material_veto": None,
        },
    }


class QuoteFreeFootballPairTests(unittest.TestCase):
    def test_started_goals_assess_both_models_without_quote(self):
        out = run_football_pair(football("c"), football("c2"))
        self.assertEqual(out["engine_execution_status"], "EXECUTED_C_C2_FOOTBALL_ONLY")
        self.assertFalse(out["quotes_required"])
        self.assertFalse(out["model_bets_created"])
        for model in ("c", "c2"):
            r = out["results"][model]
            self.assertEqual(r["stage"], "football_assessment_result")
            self.assertTrue(r["football_assessment_completed"])
            self.assertEqual(r["quote_status"], "UNPRICED_NOT_REQUIRED_FOR_FOOTBALL")
            self.assertEqual(r["decision_action"], "NOT_EVALUATED_NO_CURRENT_PRICE")
            self.assertFalse(r["bet_authorized"])
            self.assertEqual(r["model_accounting_status"], "NONE")
            self.assertEqual(r["score"], "1-0")
            self.assertIn("MATERIAL_EVENT_FOOTBALL_RECHECK", r["limitations"])
        self.assertIn("continuation_quality", out["results"]["c"])
        self.assertIn("selection_floor", out["results"]["c2"])
        self.assertNotIn("continuation_quality", out["results"]["c2"])

    def test_assessment_complete_with_no_score_and_no_quote_is_explicitly_limited(self):
        a = football("c")
        a["context"]["score"] = None
        a["context"]["match_minute"] = None
        result = run_football_assessment(a)
        self.assertTrue(result["football_assessment_completed"])
        self.assertIn("LIVE_SCORE_OR_MINUTE_UNVERIFIED", result["limitations"])
        self.assertFalse(result["bet_authorized"])

    def test_unquoted_near_kickoff_and_later_live_allowed(self):
        for status, minute, score in (
            ("PREMATCH_CONFIRMED", None, None),
            ("STARTED", 2, "0-0"),
            ("STARTED", 16, "1-0"),
            ("HALFTIME", 45, "2-0"),
        ):
            with self.subTest(status=status, minute=minute):
                c = football("c", status=status, minute=minute, score=score)
                c2 = football("c2", status=status, minute=minute, score=score)
                r = run_football_pair(c, c2)
                self.assertEqual(len(r["results"]), 2)
                self.assertTrue(r["results"]["c"]["football_assessment_completed"])
                self.assertFalse(r["results"]["c2"]["quote_required_for_football_assessment"])

    def test_verified_intact_thesis_distinct_from_price(self):
        p = football("c", status="STARTED", score="0-0", minute=3,
                     event="NONE_VERIFIED")
        p["context"].update(thesis_state="PRESERVED",
                            primary_mechanism_intact=True, material_veto=False)
        r = run_football_assessment(p)
        self.assertEqual(r["football_read"], "FOOTBALL_THESIS_CURRENTLY_INTACT")
        self.assertFalse(r["bet_authorized"])
        self.assertTrue(r["frozen_line_not_live_executable"])

    def test_an_actual_deterioration_can_be_reported_without_market(self):
        p = football("c")
        p["context"].update(thesis_state="BROKEN",
                            primary_mechanism_intact=False, material_veto=True)
        r = run_football_assessment(p)
        self.assertEqual(r["football_read"], "FOOTBALL_THESIS_ADVERSE")
        self.assertEqual(r["decision_action"], "NOT_EVALUATED_NO_CURRENT_PRICE")

    def test_pair_must_be_same_current_epoch_and_independent(self):
        c, c2 = football("c"), football("c2")
        c2["context"]["score"] = "0-1"
        with self.assertRaisesRegex(ContractError, "epoch/status/score mismatch"):
            run_football_pair(c, c2)
        c2 = football("c2")
        c2["evidence_epoch_id"] = "retroactively-shifted"
        with self.assertRaisesRegex(ContractError, "epoch/status/score mismatch"):
            run_football_pair(c, c2)
        c2 = football("c2")
        c2["match"]["match_id"] = "unrelated-fixture"
        with self.assertRaisesRegex(ContractError, "epoch/status/score mismatch"):
            run_football_pair(c, c2)

    def test_no_legacy_quote_requirement_reintroduced_in_priced_engine(self):
        c = football("c")
        with self.assertRaisesRegex(ContractError, "stage must be 'decision'"):
            run_decision(c)
        p = {"schema_version": "football-engine-v1",
             "stage": "decision", "model": "c",
             "match": match(), "context": decision_context(quote_revalidated=False)}
        with self.assertRaisesRegex(ContractError, "CURRENT QUOTE NOT REVALIDATED"):
            run_decision(p)

    def test_source_model_inputs_remain_genuine(self):
        p = football("c2")
        p["match"].pop("carrier_self_fund_basis")
        with self.assertRaises(ContractError):
            run_football_assessment(p)
        p = football("c")
        p["context"]["board_state"] = "PASS_UNKNOWN"
        with self.assertRaises(ContractError):
            run_football_assessment(p)


if __name__ == "__main__":
    unittest.main()
