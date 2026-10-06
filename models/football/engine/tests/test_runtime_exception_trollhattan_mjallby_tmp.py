import json
import pathlib
import tempfile
import unittest

from models.football.engine import xi_portable


MATCH_ID = "bdpd_f3718a93a110b3267920"

COMMON_MATCH = {
    "match_id": MATCH_ID,
    "kickoff_ict": "2026-10-06T22:00:00+07:00",
    "operational_viability_grade": "A",
    "raw_operational_viability_grade": "A",
    "competition_reliability_state": "UNPROVEN",
    "competition_reliability_reason": "No matching Competition Reliability row; default UNPROVEN under frozen Step-0 procedure.",
    "competition_reliability_manual_override": "NONE",
    "demoted_probation": False,
    "xi_expected": "YES",
    "market_observability": "HIGH",
    "team_news_observability": "MEDIUM",
    "operational_viability_reason": "User supplied confirmed XI graphics and an executable totals ladder immediately before kickoff; fixture and cup status are independently verified.",
    "common_evidence_basis": (
        "Trollhattan's confirmed XI keeps the recent attacking core: Svensson, Jensen and Berg all scored in the 4-2 win over Tvaaker and Hassan added the late fourth, while Burubwa and Hermansson also remain involved. "
        "Mjallby's confirmed XI is not a reserve side: eight of the eleven from the 0-3 league loss to GAIS remain (Wallinder, Noren, Pettersson, Granath, both Gustafsson/Gustavsson midfielders, Bergstrom and Youssef), with Svanberg, Kjaer and Tidstrand the changes. "
        "This upgrades Mjallby's route to strong against lower-tier opposition and preserves a usable Trollhattan route, but Mjallby's poor current league form and the knockout structure still do not provide independent proof for a reliable fourth-goal tail."
    ),
    "home_route": "USABLE",
    "away_route": "STRONG",
    "carrier": "STRONG",
    "route_reliability": "MEDIUM",
    "independent_route_quality": "MEDIUM",
    "chance_quality": "MEDIUM",
    "failure_resistance": "MEDIUM",
    "xi_robustness": "HIGH",
    "evidence_confidence": "HIGH",
    "burden_protection": "MEDIUM",
    "main_failure": "The current XI supports three-goal access, but a fourth goal still depends on sustained favourite continuation or a meaningful home contribution; Mjallby's recent league attack has been inconsistent.",
    "h2h_state": "REVIEWED",
    "h2h_effect": "NOT_MATERIAL",
    "h2h_transferability": "NOT_TRANSFERABLE",
    "h2h_current_corroboration": "NOT_APPLICABLE",
    "h2h_material_effect": False,
    "h2h_basis": "Old meetings are not transferable to the 2026 personnel, coaching and division context and do not create a current suppressive mechanism.",
    "carrier_self_fund": False,
    "carrier_self_fund_basis": "Mjallby are a strong favourite and retain most of the senior XI, but their current form does not independently certify three away goals plus continued pressure for a fourth.",
    "independent_upper_tail": False,
    "independent_upper_tail_basis": "No current non-market evidence independently certifies the fourth goal; class gap and current price alone cannot supply upper-tail proof.",
    "failure_attacks_route": False,
    "failure_attacks_route_basis": "Form and continuation concerns cap the ceiling but do not remove Mjallby's strong away route or Trollhattan's usable home route.",
    "material_suppression": False,
    "material_suppression_basis": "No current personnel, weather or transferable-H2H suppression veto was verified.",
    "tournament_incentive_required": True,
    "tournament_format_status": "VERIFIED",
    "competition_stage": "Svenska Cupen 2026/27 men, round two.",
    "competition_format": "Single-elimination match; the round-two winner qualifies for the 2027 group stage.",
    "draw_resolution": "If level after regulation, two 15-minute extra-time periods are played and then penalties if still level.",
    "aggregate_state": "Single leg; no aggregate or away-goal rule.",
    "qualification_state": "Winner advances to the group stage; loser is eliminated.",
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
        "Fresh research confirmed Trollhattan's current XI retains the scorers/service from the recent 4-2 Tvaaker win, while Mjallby retain eight starters from the recent GAIS league XI. "
        "Mjallby's side is therefore much stronger than a heavy-rotation cup team, but their current run is poor and the evidence supports a strong favourite route rather than an independently funded four-goal tail."
    ),
    "fixture_status": "PREMATCH_CONFIRMED",
    "quote_revalidated": True,
    "market_history_status": "PARTIAL",
    "market_history_movement": "STABLE",
    "market_history_conflict_recheck": "NOT_REQUIRED",
    "market_history_note": "Earlier bookmaker snapshots around the fixture had O2.5 about 1.40-1.45 and O3.5 about 2.06-2.13. Current user ladder is O3.0 1.68, O3.25 1.93 and O3.5 2.12; current public averages are similar (O3.0 about 1.69, O3.25 about 1.86, O3.5 about 2.13), so no material football-driven shift is established.",
    "h2h_review_status": "REVIEWED_LIMITED",
    "h2h_rechecked": True,
    "h2h_basis": "Historical Trollhattan-Mjallby meetings were rechecked and remain non-transferable/non-material.",
    "tournament_incentive_rechecked": True,
    "tournament_incentive_recheck_status": "VERIFIED",
}

C_MATCH = {
    **COMMON_MATCH,
    "supported_line": 2.25,
    "supported_line_basis": "Frozen C O2.25 remains the protected burden. The XI upgrade improves route confidence but does not lawfully move the prospectively frozen supported line.",
    "completion_mode": "TWO_SIDED",
    "burden_completion_quality": "MEDIUM",
    "continuation_quality": "MEDIUM",
    "opponent_leakage": "HIGH",
    "burden_stall_risk": "MEDIUM",
}

C2_MATCH = {
    **COMMON_MATCH,
    "supported_line": 2.5,
    "supported_line_basis": "Frozen C2 O2.5 remains independently protected. The confirmed XI now clears route quality with a strong Mjallby route plus usable Trollhattan route, but current O3.0 is still above burden.",
}

C_CONTEXT = {
    **COMMON_CONTEXT,
    "board_state": "C-WATCH",
    "thesis_state": "PRESERVED",
    "thesis_state_basis": "Confirmed XI strengthens the frozen football thesis but does not change the protected C burden or remove medium continuation/stall risk.",
    "quote": {"line": 3.0, "odds": 1.68},
    "completion_rechecked": True,
    "top_ranked_focus": False,
    "primary_mechanism_intact": True,
    "primary_mechanism_basis": "Trollhattan retain their recent attacking core and Mjallby retain most of a senior league XI.",
    "wait_reachable": False,
    "wait_reachability_basis": "O2.25 at the required 1.65 price is not realistically reachable before kickoff while O3.0 is only 1.68.",
    "wait_requires_negative_info": True,
    "wait_negative_info_basis": "A lower O2.25 line rising to the model price floor would require major adverse market movement.",
    "material_veto": False,
    "material_veto_basis": "No hard veto; the blocker is unsupported current burden and an unhealthy wait path."
}

C2_CONTEXT = {
    **COMMON_CONTEXT,
    "board_state": "C2-WATCH",
    "thesis_state": "PRESERVED",
    "thesis_state_basis": "The current XI improves C2 route quality to a clear two-route floor, but its protected burden remains O2.5.",
    "quote": {"line": 3.0, "odds": 1.68},
    "c2_route_quality_rechecked": True,
    "top_ranked_focus": False,
    "primary_mechanism_intact": True,
    "primary_mechanism_basis": "Mjallby supply the strong route and Trollhattan retain a usable home route.",
    "wait_reachable": False,
    "wait_reachability_basis": "O2.5 at at least 1.65 is not a healthy/reachable target with O3.0 already 1.68.",
    "wait_requires_negative_info": True,
    "wait_negative_info_basis": "A rise of the lower O2.5 line to the minimum price would require material negative movement.",
    "material_veto": False,
    "material_veto_basis": "No hard route/suppression veto; current market is simply above the protected burden."
}

C_PAYLOAD = {"schema_version":"football-engine-v1","stage":"decision","model":"c","match":C_MATCH,"context":C_CONTEXT}
C2_PAYLOAD = {"schema_version":"football-engine-v1","stage":"decision","model":"c2","match":C2_MATCH,"context":C2_CONTEXT}

ACCOUNTING = {
    "match_id": MATCH_ID,
    "models": [
        {"model":"c","board_state":"C-WATCH","supported_line":2.25,"step2_action":"C-PASS"},
        {"model":"c2","board_state":"C2-WATCH","supported_line":2.5,"step2_action":"C2-PASS"},
    ],
    "total_goals": None,
}

RECONCILE = {
    "schema_version":"football-step2-reconcile-v1",
    "stage":"step2_reconcile",
    "session_id":"XI-EXC-20261006-FCT-MJA-213000",
    "due":[{"match_id":MATCH_ID,"official_follow_lane":"STOP","step2_authorization":"USER_EXCEPTION"}],
    "outcomes":[{"match_id":MATCH_ID,"status":"DECISION_STATE_PERSISTED"}],
}

class RuntimeExceptionTrollhattanMjallbyTests(unittest.TestCase):
    def test_exact_current_pair(self):
        check=xi_portable.self_check()
        print("XI_RUNTIME_SELF_CHECK="+json.dumps(check,sort_keys=True))
        self.assertTrue(check["ok"])
        with tempfile.TemporaryDirectory() as td:
            root=pathlib.Path(td)
            c=root/"c.json"; c2=root/"c2.json"; acc=root/"acc.json"; rec=root/"rec.json"
            c.write_text(json.dumps(C_PAYLOAD),encoding="utf-8")
            c2.write_text(json.dumps(C2_PAYLOAD),encoding="utf-8")
            acc.write_text(json.dumps(ACCOUNTING),encoding="utf-8")
            rec.write_text(json.dumps(RECONCILE),encoding="utf-8")
            pair=xi_portable.run_pair_files(str(c),str(c2))
            accounting=xi_portable.run_accounting_file(str(acc))
            reconciliation=xi_portable.run_reconcile_file(str(rec))
        print("XI_PAIR_RESULT="+json.dumps(pair,sort_keys=True))
        print("XI_ACCOUNTING_RESULT="+json.dumps(accounting,sort_keys=True))
        print("XI_RECONCILE_RESULT="+json.dumps(reconciliation,sort_keys=True))
        self.assertEqual(pair["engine_execution_status"],"EXECUTED_C_C2_PAIR")
        self.assertEqual(pair["results"]["c"]["action"],"PASS")
        self.assertEqual(pair["results"]["c2"]["action"],"PASS")
        self.assertEqual(pair["results"]["c2"]["selection_floor"],"CLEAR")
        self.assertEqual(accounting["models"][0]["basis"],"WATCH_ASSUMED")
        self.assertEqual(accounting["models"][1]["basis"],"SHADOW_WATCH_ASSUMED")
        self.assertTrue(reconciliation["all_due_accounted"])

if __name__=="__main__":
    unittest.main()
