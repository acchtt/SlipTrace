import json
import pathlib
import tempfile
import unittest

from models.football.engine import xi_portable


MATCH_ID = "bdpd_0967261e50599f5ba11a"

COMMON_MATCH = {
    "match_id": MATCH_ID,
    "kickoff_ict": "2026-10-06T22:00:00+07:00",
    "operational_viability_grade": "A",
    "raw_operational_viability_grade": "A",
    "competition_reliability_state": "UNPROVEN",
    "competition_reliability_reason": "No matching Competition Reliability row; default UNPROVEN under the frozen Step-0 reliability procedure.",
    "competition_reliability_manual_override": "NONE",
    "demoted_probation": False,
    "xi_expected": "YES",
    "market_observability": "HIGH",
    "team_news_observability": "MEDIUM",
    "operational_viability_reason": "Confirmed XI supplied immediately before kickoff, executable Asian-total ladder available, and current club/competition evidence is researchable.",
    "common_evidence_basis": (
        "The confirmed Raufoss XI preserves the Zekhnini-Karlsen attack and most of the side used in the recent 0-2 loss to Stromsgodset, where Raufoss created well in the first half but failed to convert and then lost pressing intensity. "
        "Start rotate from their latest Eliteserien XI but retain Norheim, Ujkani, Ugland, Toure and Lorentzen, while Storm Strand-Kolbjornsen, Meyer, Jojic and Cornelius are proven cup starters from the 3-2 win at Vindbjart. "
        "That makes Raufoss a usable home route and Start a strong away route against a Raufoss defence that has shown major leakage, but neither the confirmed personnel nor current form independently proves a reliable fourth-goal tail."
    ),
    "home_route": "USABLE",
    "away_route": "STRONG",
    "carrier": "STRONG",
    "route_reliability": "MEDIUM",
    "independent_route_quality": "MEDIUM",
    "chance_quality": "MEDIUM",
    "failure_resistance": "MEDIUM",
    "xi_robustness": "MEDIUM",
    "evidence_confidence": "HIGH",
    "burden_protection": "MEDIUM",
    "main_failure": "The third-goal route is credible, but conversion and sustained continuation remain uneven; regulation draw protection also leaves a natural control branch.",
    "h2h_state": "REVIEWED",
    "h2h_effect": "NOT_MATERIAL",
    "h2h_transferability": "LIMITED",
    "h2h_current_corroboration": "NOT_APPLICABLE",
    "h2h_material_effect": False,
    "h2h_basis": "The May 2025 0-0 at Raufoss and October 2025 Start 4-0 were rechecked; different divisions, personnel and cup context make them limited rather than determinative.",
    "carrier_self_fund": False,
    "carrier_self_fund_basis": "Start are the strongest route and clear favourites, but the rotated XI omits several recent first-choice attacking pieces and does not independently certify three Start goals plus continued fourth-goal pressure.",
    "independent_upper_tail": False,
    "independent_upper_tail_basis": "Recent evidence supports a credible three-goal environment, not a repeatable independent fourth-goal mechanism under this exact XI.",
    "failure_attacks_route": False,
    "failure_attacks_route_basis": "Conversion and game-control risk reduce continuation but do not remove either team's current route.",
    "material_suppression": False,
    "material_suppression_basis": "No transferable H2H, weather, injury or tactical suppression veto was verified at this XI epoch.",
    "tournament_incentive_required": True,
    "tournament_format_status": "VERIFIED",
    "competition_stage": "NM menn 2027, round three, played in the autumn 2026 phase.",
    "competition_format": "Single-elimination single match; the winner advances to round four.",
    "draw_resolution": "If level after regulation, two 15-minute extra-time periods are played, followed by penalties if still level.",
    "aggregate_state": "Single leg; no aggregate or away-goal rule.",
    "qualification_state": "Both teams are alive; the winner advances and the loser is eliminated.",
    "simultaneous_results_status": "NOT_APPLICABLE",
    "simultaneous_results_note": "No other result affects qualification from this tie.",
    "home_incentive": "DRAW_ACCEPTABLE",
    "away_incentive": "DRAW_ACCEPTABLE",
    "tiebreak_margin_relevance": "NO",
    "incentive_effect": "MIXED",
}

COMMON_CONTEXT = {
    "official_follow_lane": "STOP",
    "step2_authorization": "USER_EXCEPTION",
    "xi_status": "CONFIRMED",
    "post_xi_research_status": "FOUND",
    "post_xi_research_note": (
        "Fresh post-XI research confirmed Raufoss keep Zekhnini and Karlsen after a recent match where their first-half press created chances but faded after the break. "
        "Start's current XI is a cup/league mix: it keeps Norheim, Ujkani, Ugland, Toure and Lorentzen but leaves out recent league starters including Mvoue and Koutsakos; "
        "Storm Strand-Kolbjornsen, Meyer, Jojic and Cornelius were part of the cup XI that won 3-2 at Vindbjart. Current personnel preserve two scoring routes but do not upgrade the match to a reliably funded four-goal environment."
    ),
    "fixture_status": "PREMATCH_CONFIRMED",
    "quote_revalidated": True,
    "market_history_status": "PARTIAL",
    "market_history_movement": "UNCLEAR",
    "market_history_conflict_recheck": "NOT_REQUIRED",
    "market_history_note": (
        "A 5 Oct odds snapshot showed O2.5 around 1.52-1.60 and O3.5 around 2.38-2.55. The user's current executable ladder is O2.75 1.68, O3.0 1.90 and O3.25 2.16. "
        "The center remains roughly around three goals, but the different quoted lines do not support a precise OPEN-to-current movement classification."
    ),
    "h2h_review_status": "REVIEWED_LIMITED",
    "h2h_rechecked": True,
    "h2h_basis": "The 0-0 at this venue in May 2025 and Start 4-0 in October 2025 were rechecked and remain limited/non-material under the current cup/XI state.",
    "tournament_incentive_rechecked": True,
    "tournament_incentive_recheck_status": "VERIFIED",
}

C_MATCH = {
    **COMMON_MATCH,
    "supported_line": 2.25,
    "supported_line_basis": "Frozen C O2.25 remains the protected burden: two current routes exist, but the current evidence still does not strongly fund sustained continuation beyond the third goal.",
    "completion_mode": "TWO_SIDED",
    "burden_completion_quality": "MEDIUM",
    "continuation_quality": "MEDIUM",
    "opponent_leakage": "HIGH",
    "burden_stall_risk": "MEDIUM",
}

C2_MATCH = {
    **COMMON_MATCH,
    "supported_line": 2.5,
    "supported_line_basis": "Frozen C2 O2.5 remains independently supported because Start's strong route plus Raufoss' usable route can reach three, but the current O2.75 market is above the protected burden.",
}

C_CONTEXT = {
    **COMMON_CONTEXT,
    "board_state": "C-WATCH",
    "thesis_state": "PRESERVED",
    "thesis_state_basis": "Confirmed XI preserves the frozen two-sided scoring thesis but does not add enough continuation proof to raise the protected burden.",
    "quote": {"line": 2.75, "odds": 1.68},
    "completion_rechecked": True,
    "top_ranked_focus": False,
    "primary_mechanism_intact": True,
    "primary_mechanism_basis": "Zekhnini/Karlsen remain for Raufoss and Start retain a strong senior attacking route through Lorentzen with Ugland/Toure support.",
    "wait_reachable": False,
    "wait_reachability_basis": "The protected O2.25 line would price materially below the 1.65 floor with O2.75 already 1.68, so a healthy prematch target is not realistically reachable.",
    "wait_requires_negative_info": True,
    "wait_negative_info_basis": "For O2.25 to rise to at least 1.65 before kickoff would require a major downward market move normally associated with adverse football information.",
    "material_veto": False,
    "material_veto_basis": "No hard football veto remains; the blocker is burden/price mismatch plus only medium continuation."
}

C2_CONTEXT = {
    **COMMON_CONTEXT,
    "board_state": "C2-WATCH",
    "thesis_state": "PRESERVED",
    "thesis_state_basis": "Confirmed XI preserves C2's two-route thesis and now gives Start the stronger route, but the market remains one quarter above C2's protected line.",
    "quote": {"line": 2.75, "odds": 1.68},
    "c2_route_quality_rechecked": True,
    "top_ranked_focus": False,
    "primary_mechanism_intact": True,
    "primary_mechanism_basis": "Both routes remain usable and Start's away route is strong under the current personnel/class matchup.",
    "wait_reachable": False,
    "wait_reachability_basis": "O2.5 at the required minimum 1.65 is not a healthy realistic target while O2.75 itself is only 1.68.",
    "wait_requires_negative_info": True,
    "wait_negative_info_basis": "A price rise on the lower O2.5 line to the model floor would require material market deterioration.",
    "material_veto": False,
    "material_veto_basis": "No hard route/suppression veto; C2 is blocked by above-burden pricing and an unhealthy wait path."
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
            "board_state": "C-WATCH",
            "supported_line": 2.25,
            "step2_action": "C-PASS",
        },
        {
            "model": "c2",
            "board_state": "C2-WATCH",
            "supported_line": 2.5,
            "step2_action": "C2-PASS",
        },
    ],
    "total_goals": None,
}

RECONCILE = {
    "schema_version": "football-step2-reconcile-v1",
    "stage": "step2_reconcile",
    "session_id": "XI-EXC-20261006-RAU-STA-212800",
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


class RuntimeExceptionRaufossStartTests(unittest.TestCase):
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
        self.assertEqual(pair["results"]["c2"]["selection_floor"], "CLEAR")
        self.assertEqual(accounting["models"][0]["basis"], "WATCH_ASSUMED")
        self.assertEqual(accounting["models"][1]["basis"], "SHADOW_WATCH_ASSUMED")
        self.assertTrue(reconciliation["all_due_accounted"])


if __name__ == "__main__":
    unittest.main()
