import json, pathlib, tempfile, unittest
from models.football.engine import xi_portable

MATCH_ID="bpd-9b754e50b055684e"

COMMON={
 "match_id":MATCH_ID,
 "kickoff_ict":"2026-10-08T23:00:00+07:00",
 "operational_viability_grade":"A",
 "raw_operational_viability_grade":"A",
 "competition_reliability_state":"UNPROVEN",
 "competition_reliability_reason":"No Competition Reliability row; default UNPROVEN.",
 "competition_reliability_manual_override":"NONE",
 "demoted_probation":False,
 "xi_expected":"YES","market_observability":"HIGH","team_news_observability":"HIGH",
 "operational_viability_reason":"Confirmed user-supplied AiScore XI and executable Asian-total ladder inside the pre-kickoff window.",
 "common_evidence_basis":"Confirmed KuPS XI restores Bob Nii Armah to the starting attack and also keeps Clinton Antwi and Petteri Pennanen, improving the home route versus Step 1. KuPS nevertheless enter from 0-0 vs HJK and 2-0 vs VPS, while AC Oulu have produced little recent championship-group scoring and remain a weak away route despite beating KuPS 2-0 at home in May. KuPS are in the title race and need three points; AC Oulu seek their first championship-group points. The current XI strengthens KuPS' carrier but does not create a second reliable route or independent upper-tail proof.",
 "home_route":"STRONG","away_route":"WEAK","carrier":"STRONG",
 "route_reliability":"HIGH","independent_route_quality":"LOW","chance_quality":"MEDIUM",
 "failure_resistance":"MEDIUM","xi_robustness":"HIGH","evidence_confidence":"HIGH","burden_protection":"HIGH",
 "main_failure":"KuPS still have a credible clean-sheet / two-goal control endpoint and AC Oulu's current away scoring route remains weak.",
 "h2h_state":"LIMITED","h2h_effect":"NOT_MATERIAL","h2h_transferability":"LIMITED",
 "h2h_current_corroboration":"VERIFIED","h2h_material_effect":False,
 "h2h_basis":"AC Oulu beat KuPS 2-0 in May 2026, which proves Oulu can score against this opponent, but the venue and current championship-group form differ; it is corroborative only and does not by itself upgrade the away route.",
 "carrier_self_fund":False,
 "carrier_self_fund_basis":"Armah's return improves KuPS' attack, but current competitive evidence still does not independently certify three KuPS goals or repeated self-funding above O2.0.",
 "independent_upper_tail":False,
 "independent_upper_tail_basis":"No sufficiently current non-market evidence proves a reliable third/fourth-goal tail under this exact XI; recent KuPS league outputs were 0 and 2 goals.",
 "failure_attacks_route":False,
 "failure_attacks_route_basis":"The failure mode is control/stall after a KuPS lead, not loss of KuPS' primary scoring route.",
 "material_suppression":False,
 "material_suppression_basis":"No categorical current personnel or tactical suppression veto is verified; the concern is insufficient second-route and continuation quality.",
 "tournament_incentive_required":True,
 "tournament_format_status":"VERIFIED",
 "competition_stage":"Veikkausliiga 2026 championship group; KuPS and AC Oulu have played 25 league matches entering this fixture.",
 "competition_format":"Top six retained regular-season points/goals and play a double round-robin championship group; no relegation risk inside this group.",
 "draw_resolution":"A 90-minute draw awards one point; no extra time or penalties.",
 "aggregate_state":"No aggregate score.",
 "qualification_state":"KuPS are one point behind FC Inter before this fixture and a win restores first place; AC Oulu are sixth and seek their first championship-group points while remaining in the European-place race.",
 "simultaneous_results_status":"VERIFIED",
 "simultaneous_results_note":"HJK-VPS is played one hour earlier and can alter medal gaps, but no possible result makes this fixture a dead rubber or creates a mutual draw-qualification condition; KuPS remain win-preferred and AC Oulu still need points.",
 "home_incentive":"WIN_PREFERRED","away_incentive":"WIN_PREFERRED",
 "tiebreak_margin_relevance":"YES","incentive_effect":"MIXED",
}

C_MATCH={
 **COMMON,
 "supported_line":2.0,
 "supported_line_basis":"Frozen C support remains O2.0. The confirmed XI improves KuPS' route but does not fund the third goal strongly enough to raise the protected burden.",
 "completion_mode":"CARRIER_LED",
 "burden_completion_quality":"MEDIUM","continuation_quality":"LOW","opponent_leakage":"MEDIUM","burden_stall_risk":"HIGH",
}

C2_MATCH={
 **COMMON,
 "supported_line":2.25,
 "supported_line_basis":"Frozen C2 support remains O2.25, but current route quality still lacks a usable AC Oulu route or a self-funding/upper-tail KuPS carrier.",
}

COMMON_CTX={
 "official_follow_lane":"STOP","step2_authorization":"USER_EXCEPTION",
 "xi_status":"CONFIRMED","post_xi_research_status":"FOUND",
 "post_xi_research_note":"Fresh post-XI research confirms Bob Nii Armah is fully fit and starts for KuPS after returning from injury; KuPS explicitly frame every remaining match as a final and target three points. AC Oulu explicitly seek their first championship-group points. Current official results still show KuPS 0-0 vs HJK and 2-0 vs VPS, while AC Oulu's recent group scoring remains weak. The XI improves KuPS but does not establish a second strong scoring route.",
 "fixture_status":"PREMATCH_CONFIRMED","quote_revalidated":True,
 "market_history_status":"PARTIAL","market_history_movement":"UNCLEAR","market_history_conflict_recheck":"NOT_REQUIRED",
 "market_history_note":"User executable ladder is O2.25@1.72, O2.5@2.00 and O2.75@2.25. Public 1X2 prices remain broadly consistent with KuPS as a strong favourite, but a trustworthy Asian-total OPEN->PRE-XI trace was not established before kickoff.",
 "h2h_review_status":"REVIEWED_LIMITED","h2h_rechecked":True,
 "h2h_basis":"The May 2026 AC Oulu 2-0 KuPS result was rechecked. It is current-season corroboration but venue/form transfer is limited and it does not override the present Oulu scoring weakness.",
 "tournament_incentive_rechecked":True,"tournament_incentive_recheck_status":"VERIFIED",
 "thesis_state":"PRESERVED",
 "thesis_state_basis":"Confirmed XI strengthens KuPS' home mechanism but preserves the frozen main failure: weak Oulu contribution and a credible KuPS control endpoint.",
 "primary_mechanism_intact":True,
 "primary_mechanism_basis":"KuPS retain Pennanen/Antwi and regain Armah, so the primary home scoring mechanism is intact and stronger than at Step 1.",
 "material_veto":False,"material_veto_basis":"No hard veto; selection is limited by burden/route quality rather than categorical suppression.",
}

C_CTX={
 **COMMON_CTX,
 "board_state":"C-WATCH",
 "quote":{"line":2.25,"odds":1.72},
 "completion_rechecked":True,
 "top_ranked_focus":False,
 "wait_reachable":True,
 "wait_reachability_basis":"Only a quarter-goal gap separates the executable O2.25 from C's O2.0 support. If the match remains 0-0 with mechanisms intact, normal early clock decay can plausibly bring O2.0 to the 1.65 floor.",
 "wait_requires_negative_info":False,
 "wait_negative_info_basis":"The target can arise from ordinary scoreless clock decay rather than needing adverse football information.",
}

C2_CTX={
 **COMMON_CTX,
 "board_state":"C2-WATCH",
 "quote":{"line":2.25,"odds":1.72},
 "c2_route_quality_rechecked":True,
 "top_ranked_focus":False,
 "wait_reachable":False,
 "wait_reachability_basis":"Price is already at C2's supported line; the blocker is the selection-quality floor, not market reachability.",
 "wait_requires_negative_info":False,
 "wait_negative_info_basis":"Not applicable to a route-quality blocker.",
}

def payload(model,match,ctx):
 return {"schema_version":"football-engine-v1","stage":"decision","model":model,"match":match,"context":ctx}

ACCOUNTING={
 "match_id":MATCH_ID,
 "models":[
   {"model":"c","board_state":"C-WATCH","supported_line":2.0,"step2_action":"C-WAIT","wait_target_line":2.0,"wait_min_odds":1.65},
   {"model":"c2","board_state":"C2-WATCH","supported_line":2.25,"step2_action":"C2-PASS"},
 ],
 "total_goals":None,
}

RECONCILE={
 "schema_version":"football-step2-reconcile-v1","stage":"step2_reconcile",
 "session_id":"XI-EXC-20261008-KUPS-OULU-2245",
 "due":[{"match_id":MATCH_ID,"official_follow_lane":"STOP","step2_authorization":"USER_EXCEPTION"}],
 "outcomes":[{"match_id":MATCH_ID,"status":"DECISION_STATE_PERSISTED"}],
}

class TestKuPSOuluXiException(unittest.TestCase):
 def test_pair(self):
  check=xi_portable.self_check()
  print("XI_RUNTIME_SELF_CHECK="+json.dumps(check,sort_keys=True))
  self.assertTrue(check["ok"])
  with tempfile.TemporaryDirectory() as td:
   root=pathlib.Path(td)
   c=root/"c.json"; c2=root/"c2.json"; acc=root/"acc.json"; rec=root/"rec.json"
   c.write_text(json.dumps(payload("c",C_MATCH,C_CTX)),encoding="utf-8")
   c2.write_text(json.dumps(payload("c2",C2_MATCH,C2_CTX)),encoding="utf-8")
   acc.write_text(json.dumps(ACCOUNTING),encoding="utf-8")
   rec.write_text(json.dumps(RECONCILE),encoding="utf-8")
   pair=xi_portable.run_pair_files(str(c),str(c2))
   accounting=xi_portable.run_accounting_file(str(acc))
   reconciliation=xi_portable.run_reconcile_file(str(rec))
  print("KUPS_OULU_PAIR="+json.dumps(pair,sort_keys=True))
  print("KUPS_OULU_ACCOUNTING="+json.dumps(accounting,sort_keys=True))
  print("KUPS_OULU_RECONCILE="+json.dumps(reconciliation,sort_keys=True))
  self.assertEqual(pair["engine_execution_status"],"EXECUTED_C_C2_PAIR")
  self.assertEqual(pair["results"]["c"]["action"],"WAIT")
  self.assertEqual(pair["results"]["c2"]["action"],"PASS")
  self.assertEqual(pair["results"]["c2"]["selection_floor"],"BORDERLINE")
  self.assertTrue(reconciliation["all_due_accounted"])

if __name__=="__main__": unittest.main()
