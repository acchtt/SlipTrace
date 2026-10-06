import json
import pathlib
import tempfile
import unittest

from models.football.engine import xi_portable


MATCH_ID = "2026-10-06|TURKEY_CUP_R2|Sakaryaspor|Arit_Kayadibispor"

COMMON_MATCH = {
    "match_id": MATCH_ID,
    "kickoff_ict": "2026-10-06T21:00:00+07:00",
    "operational_viability_grade": "A",
    "raw_operational_viability_grade": "A",
    "competition_reliability_state": "UNPROVEN",
    "competition_reliability_reason": "No current reliability sample sufficient to alter this user-exception epoch.",
    "competition_reliability_manual_override": "NONE",
    "demoted_probation": False,
    "xi_expected": "YES",
    "market_observability": "HIGH",
    "team_news_observability": "HIGH",
    "operational_viability_reason": "User supplied both confirmed XI graphics and executable Asian totals immediately before kickoff; public fixture identity and status were independently rechecked.",
    "common_evidence_basis": (
        "Sakaryaspor retain the only strong scoring route because they are a professional TFF 2. Lig side facing Bartin 1. Amateur opposition, "
        "and their current league run has repeatedly produced two or three goals. However the supplied XI is extremely rotated relative to their recent league core: "
        "the September 6 TFF starting XI had only Mertcan Acikgoz in common, while Ibrahim Demir, Ozgur Coban, Yasin Eratilla, Erdem Dagli, Abdulkerim Canli, "
        "Muhammet Ali Ozbaskici, Mert Akoglu and Ayberk Acikgoz were substitutes. Arit Kayadibispor are not a zero-route opponent: they won 3-0 away to Sinopspor "
        "in the previous cup round and were first in the Bartin amateur competition. The class gap supports home dominance, but the five-goal market requires sustained "
        "continuation from a rotated favorite or an away contribution that is not independently reliable."
    ),
    "home_route": "STRONG",
    "away_route": "WEAK",
    "carrier": "STRONG",
    "route_reliability": "MEDIUM",
    "independent_route_quality": "MEDIUM",
    "chance_quality": "MEDIUM",
    "failure_resistance": "MEDIUM",
    "xi_robustness": "LOW",
    "evidence_confidence": "MEDIUM",
    "burden_protection": "MEDIUM",
    "main_failure": "Class-gap control after a two- or three-goal lead, amplified by heavy Sakaryaspor rotation and a weak independent away scoring route.",
    "h2h_state": "UNAVAILABLE",
    "h2h_effect": "UNAVAILABLE",
    "h2h_transferability": "UNAVAILABLE",
    "h2h_current_corroboration": "NOT_APPLICABLE",
    "h2h_material_effect": False,
    "h2h_basis": "No prior Sakaryaspor-Arıt Kayadibispor meeting was found; there is no transferable H2H sample.",
    "carrier_self_fund": True,
    "carrier_self_fund_basis": "The professional/amateur class gap makes four Sakaryaspor goals plausible without requiring Arıt to score, even with rotation.",
    "independent_upper_tail": False,
    "independent_upper_tail_basis": "Sakaryaspor's current league sequence shows repeated two- and three-goal outputs but no current independent five-goal carrier proof, while today's XI removes most of the regular attacking core.",
    "failure_attacks_route": False,
    "failure_attacks_route_basis": "Rotation weakens ceiling and continuation more than it removes Sakaryaspor's primary home dominance route.",
    "material_suppression": False,
    "material_suppression_basis": "No weather, injury, H2H or tactical suppression veto was verified; the main concern is high-end continuation and class-gap control.",
    "tournament_incentive_required": True,
    "tournament_format_status": "VERIFIED",
    "competition_stage": "2026-27 Ziraat Turkiye Kupasi, second qualifying round.",
    "competition_format": "Single-match knockout in a five-qualifying-round cup structure; all rounds except the semifinal are single-match knockout.",
    "draw_resolution": "A level single-match cup tie proceeds to extra time and then penalties if still level.",
    "aggregate_state": "Single match; no aggregate score.",
    "qualification_state": "Winner advances to the third qualifying round; loser is eliminated.",
    "simultaneous_results_status": "NOT_APPLICABLE",
    "simultaneous_results_note": "No table or simultaneous-result dependency applies to this knockout tie.",
    "home_incentive": "MUST_WIN",
    "away_incentive": "MUST_WIN",
    "tiebreak_margin_relevance": "NO",
    "incentive_effect": "MIXED",
}

COMMON_CONTEXT = {
    "official_follow_lane": "STOP",
    "step2_authorization": "USER_EXCEPTION",
    "xi_status": "CONFIRMED",
    "post_xi_research_status": "FOUND",
    "post_xi_research_note": (
        "Fresh post-XI research confirmed Sakaryaspor's strong 2026-27 TFF 2. Lig scoring start, the heavy rotation relative to the September 6 official league XI, "
        "and Arıt Kayadibispor's 3-0 away cup win over Sinopspor plus amateur-league first-place context. The class gap is real, but the rotated home XI weakens the "
        "self-funded five-goal tail and raises the risk of control after establishing a safe lead."
    ),
    "fixture_status": "PREMATCH_CONFIRMED",
    "quote_revalidated": True,
    "market_history_status": "UNAVAILABLE_ATTEMPTED",
    "market_history_movement": "UNCLEAR",
    "market_history_conflict_recheck": "RECHECKED_FOOTBALL_EXPLAINED",
    "market_history_note": "No trustworthy OPEN->PRE-XI history was found. Current user-executable ladder: O4.25 1.80, O4.5 2.00, O4.75 2.20; the high center is explained by the extreme class gap, but XI rotation prevents treating price as upper-tail proof.",
    "h2h_review_status": "UNAVAILABLE",
    "h2h_rechecked": True,
    "h2h_basis": "No previous meeting found; H2H is unavailable and non-material.",
    "tournament_incentive_rechecked": True,
    "tournament_incentive_recheck_status": "VERIFIED",
}

C_MATCH = {
    **COMMON_MATCH,
    "supported_line": 4.0,
    "supported_line_basis": "C protects O4.0: the class gap can plausibly fund four home-led goals, but a fifth goal is an optimistic tail under this heavily rotated XI.",
    "completion_mode": "CARRIER_LED",
    "burden_completion_quality": "MEDIUM",
    "continuation_quality": "MEDIUM",
    "opponent_leakage": "HIGH",
    "burden_stall_risk": "HIGH",
}

C2_MATCH = {
    **COMMON_MATCH,
    "supported_line": 4.0,
    "supported_line_basis": "C2 independently supports O4.0 from the dominant home route and opponent class gap, but does not certify the five-goal tail because independent upper-tail evidence is missing.",
}

C_CONTEXT = {
    **COMMON_CONTEXT,
    "board_state": "C-PASS",
    "thesis_state": "DEGRADED",
    "thesis_state_basis": "The class-gap scoring route is intact, but heavy rotation degrades continuation and upper-tail confidence relative to the raw market expectation.",
    "quote": {"line": 4.25, "odds": 1.80},
    "completion_rechecked": True,
    "top_ranked_focus": False,
    "primary_mechanism_intact": True,
    "primary_mechanism_basis": "Sakaryaspor still own a strong home dominance route despite rotation.",
    "wait_reachable": False,
    "wait_reachability_basis": "O4.0 was not currently offered in the supplied executable ladder and kickoff was imminent, so a protected prematch wait was not realistically reachable.",
    "wait_requires_negative_info": False,
    "wait_negative_info_basis": "No wait is proposed; reaching the protected line is not being conditioned on adverse football information.",
    "material_veto": False,
    "material_veto_basis": "No separate hard veto was verified; the C rejection is driven by HIGH stall risk at this burden and the quote sitting above the protected line.",
}

C2_CONTEXT = {
    **COMMON_CONTEXT,
    "board_state": "C2-WATCH",
    "thesis_state": "DEGRADED",
    "thesis_state_basis": "The class-gap scoring route remains, but the rotated XI and missing independent upper-tail proof keep route quality below direct-exposure standard.",
    "quote": {"line": 4.25, "odds": 1.80},
    "c2_route_quality_rechecked": True,
    "top_ranked_focus": False,
    "primary_mechanism_intact": True,
    "primary_mechanism_basis": "Sakaryaspor retain the primary home scoring mechanism, but today's rotated personnel reduce its proven ceiling.",
    "wait_reachable": False,
    "wait_reachability_basis": "No lower protected line was executable in the supplied ladder before kickoff.",
    "wait_requires_negative_info": False,
    "wait_negative_info_basis": "No wait is proposed.",
    "material_veto": False,
    "material_veto_basis": "No hard suppression veto; C2 fails because its exact selection-quality floor lacks independent upper-tail proof.",
}

C_PAYLOAD = {
    "schema_version": "football-engine-v1",
    "stage": "decision",
    "model": "c",
    "match": C_MATCH,
    "context": C_CONTEXT,
}

C2_PAYLOAD = {
    "schema_version": "football-engine-v1",
    "stage": "decision",
    "model": "c2",
    "match": C2_MATCH,
    "context": C2_CONTEXT,
}

ACCOUNTING = {
    "match_id": MATCH_ID,
    "models": [
        {
            "model": "c",
            "board_state": "C-PASS",
            "supported_line": 4.0,
            "step2_action": "C-PASS",
        },
        {
            "model": "c2",
            "board_state": "C2-WATCH",
            "supported_line": 4.0,
            "step2_action": "C2-PASS",
        },
    ],
    "total_goals": None,
}

RECONCILE = {
    "schema_version": "football-step2-reconcile-v1",
    "stage": "step2_reconcile",
    "session_id": "XI-EXC-20261006-SAK-ARIT-210332",
    "due": [
        {
            "match_id": MATCH_ID,
            "official_follow_lane": "STOP",
            "step2_authorization": "USER_EXCEPTION",
        }
    ],
    "outcomes": [
        {
            "match_id": MATCH_ID,
            "status": "DECISION_STATE_PERSISTED",
        }
    ],
}


class RuntimeExceptionSakaryasporAritTests(unittest.TestCase):
    def test_exact_current_pair(self):
        check = xi_portable.self_check()
        print("XI_RUNTIME_SELF_CHECK=" + json.dumps(check, sort_keys=True))
        self.assertTrue(check["ok"])

        with tempfile.TemporaryDirectory() as td:
            root = pathlib.Path(td)
            c_path = root / "c.json"
            c2_path = root / "c2.json"
            acc_path = root / "accounting.json"
            rec_path = root / "reconcile.json"
            c_path.write_text(json.dumps(C_PAYLOAD), encoding="utf-8")
            c2_path.write_text(json.dumps(C2_PAYLOAD), encoding="utf-8")
            acc_path.write_text(json.dumps(ACCOUNTING), encoding="utf-8")
            rec_path.write_text(json.dumps(RECONCILE), encoding="utf-8")

            pair = xi_portable.run_pair_files(str(c_path), str(c2_path))
            accounting = xi_portable.run_accounting_file(str(acc_path))
            reconciliation = xi_portable.run_reconcile_file(str(rec_path))

        print("XI_PAIR_RESULT=" + json.dumps(pair, sort_keys=True))
        print("XI_ACCOUNTING_RESULT=" + json.dumps(accounting, sort_keys=True))
        print("XI_RECONCILE_RESULT=" + json.dumps(reconciliation, sort_keys=True))

        self.assertEqual(pair["engine_execution_status"], "EXECUTED_C_C2_PAIR")
        self.assertEqual(pair["results"]["c"]["action"], "PASS")
        self.assertEqual(pair["results"]["c2"]["action"], "PASS")
        self.assertEqual(accounting["models"][0]["basis"], "NONE")
        self.assertEqual(accounting["models"][1]["basis"], "SHADOW_WATCH_ASSUMED")
        self.assertTrue(reconciliation["all_due_accounted"])


if __name__ == "__main__":
    unittest.main()
