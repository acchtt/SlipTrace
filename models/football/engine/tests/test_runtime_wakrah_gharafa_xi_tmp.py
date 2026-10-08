import json, pathlib, tempfile, unittest
from models.football.engine import xi_portable

MATCH_ID="bpd-0c3a76c6061207fa"

COMMON={
 "match_id":MATCH_ID,
 "kickoff_ict":"2026-10-09T00:00:00+07:00",
 "operational_viability_grade":"A","raw_operational_viability_grade":"A",
 "competition_reliability_state":"UNPROVEN","competition_reliability_reason":"No Competition Reliability row; default UNPROVEN.",
 "competition_reliability_manual_override":"NONE","demoted_probation":False,
 "xi_expected":"YES","market_observability":"HIGH","team_news_observability":"HIGH",
 "operational_viability_reason":"Confirmed user-supplied Soccerway XI and executable Asian-total ladder inside the prematch window.",
 "common_evidence_basis":"Confirmed XIs preserve two usable routes and materially strengthen Al Gharafa's attacking options relative to Step 1, but the current league evidence is still mixed: Al Wakrah drew 1-1 last round, Al Gharafa drew 0-0, while Al Gharafa's cup team recently beat Mesaimeer 4-2 with Brahimi and Ounas contributing. Both clubs are outside the early top group and need a win, but the present league mechanism still has a credible 1-1/2-goal stall branch.",
 "home_route":"USABLE","away_route":"STRONG","carrier":"STRONG",
 "route_reliability":"MEDIUM","independent_route_quality":"MEDIUM","chance_quality":"MEDIUM",
 "failure_resistance":"MEDIUM","xi_robustness":"HIGH","evidence_confidence":"HIGH","burden_protection":"HIGH",
 "main_failure":"A first exchange can still stall at 1-1; Al Gharafa's improved attacking options have not yet translated into repeatable multi-goal league production.",
 "h2h_state":"LIMITED","h2h_effect":"NOT_MATERIAL","h2h_transferability":"LIMITED",
 "h2h_current_corroboration":"NOT_APPLICABLE","h2h_material_effect":False,
 "h2h_basis":"No current same-venue H2H mechanism is strong enough to override the recent league stall evidence; historical H2H remains limited.",
 "carrier_self_fund":False,
 "carrier_self_fund_basis":"Al Gharafa's 4-2 cup win shows upside but does not independently certify repeated three-goal league self-funding under this exact XI.",
 "independent_upper_tail":False,
 "independent_upper_tail_basis":"The cup 4-2 is useful corroboration, but one open cup match does not establish a repeatable fourth-goal league tail.",
 "failure_attacks_route":False,
 "failure_attacks_route_basis":"The main risk is continuation/stall after the first exchange, not removal of either team's primary scoring route.",
 "material_suppression":False,
 "material_suppression_basis":"No categorical current injury, tactical or H2H suppression veto is verified.",
 "tournament_incentive_required":False,
 "tournament_format_status":"NOT_APPLICABLE","competition_stage":"NOT_APPLICABLE","competition_format":"NOT_APPLICABLE",
 "draw_resolution":"NOT_APPLICABLE","aggregate_state":"NOT_APPLICABLE","qualification_state":"NOT_APPLICABLE",
 "simultaneous_results_status":"NOT_APPLICABLE","simultaneous_results_note":"NOT_APPLICABLE",
 "home_incentive":"NOT_APPLICABLE","away_incentive":"NOT_APPLICABLE","tiebreak_margin_relevance":"NOT_APPLICABLE","incentive_effect":"NOT_APPLICABLE",
}

C_MATCH={
 **COMMON,
 "supported_line":2.0,
 "supported_line_basis":"Frozen C support remains O2.0. The confirmed XI improves Al Gharafa's route but does not repair the original LOW completion / HIGH stall profile enough to raise official burden.",
 "completion_mode":"NONE","burden_completion_quality":"LOW","continuation_quality":"LOW","opponent_leakage":"MEDIUM","burden_stall_risk":"HIGH",
}

C2_MATCH={
 **COMMON,
 "supported_line":2.25,
 "supported_line_basis":"Frozen C2 support remains O2.25. The confirmed XI improves Al Gharafa to a strong route, but current evidence still does not create independent upper-tail proof or a lawful WATCH-to-market bridge.",
}

COMMON_CTX={
 "official_follow_lane":"STOP","step2_authorization":"USER_EXCEPTION",
 "xi_status":"CONFIRMED",
 "post_xi_research_status":"FOUND",
 "post_xi_research_note":"Fresh post-XI research confirms Al Gharafa's coach has more options available after Bennacer and Ounas completed 90 minutes in the cup, and the squad is explicitly targeting a win. Al Gharafa also beat Mesaimeer 4-2 in the cup with Brahimi twice, Ounas and Magri scoring. However, the current league baseline remains Al Wakrah 1-1 last round and Al Gharafa 0-0 last round; the improved XI raises the away route but does not prove sustained league continuation.",
 "fixture_status":"PREMATCH_CONFIRMED","quote_revalidated":True,
 "market_history_status":"PARTIAL","market_history_movement":"STABLE","market_history_conflict_recheck":"NOT_REQUIRED",
 "market_history_note":"Public totals were centered around O2.5 about 1.50-1.55 and O3.5 about 2.25-2.30; the user's executable Asian ladder O3.0@1.66, O3.25@1.90, O3.5@2.12 is consistent with roughly a three-goal center. A trustworthy OPEN->PRE-XI Asian trace was not established.",
 "h2h_review_status":"REVIEWED_LIMITED","h2h_rechecked":True,
 "h2h_basis":"Historical H2H was rechecked at a high level and remains limited/non-material versus the current league/XI state.",
 "tournament_incentive_rechecked":False,"tournament_incentive_recheck_status":"NOT_APPLICABLE",
 "thesis_state":"PRESERVED",
 "thesis_state_basis":"Confirmed XI strengthens the Al Gharafa route but preserves the main failure: recent league stall and insufficient repeated upper-tail production.",
 "primary_mechanism_intact":True,
 "primary_mechanism_basis":"Both teams retain credible scoring personnel; Al Gharafa's attacking depth is improved and Al Wakrah preserve a usable home route.",
 "material_veto":False,"material_veto_basis":"No hard veto; burden and continuation quality remain the blockers.",
}

C_CTX={
 **COMMON_CTX,
 "board_state":"C-PASS",
 "quote":{"line":3.0,"odds":1.66},
 "completion_rechecked":True,"top_ranked_focus":False,
 "wait_reachable":False,
 "wait_reachability_basis":"C's O2.0 support is a full goal below the current O3.0 line with kickoff imminent; a healthy prematch wait is not realistically reachable.",
 "wait_requires_negative_info":True,
 "wait_negative_info_basis":"Reaching O2.0 at the normal price floor before kickoff would require a major negative market move rather than ordinary decay.",
}

C2_CTX={
 **COMMON_CTX,
 "board_state":"C2-WATCH",
 "quote":{"line":3.0,"odds":1.66},
 "c2_route_quality_rechecked":True,"top_ranked_focus":False,
 "wait_reachable":False,
 "wait_reachability_basis":"C2's O2.25 support is 0.75 below the current O3.0 line with kickoff imminent. C2-WATCH is not eligible for the Focus Market-Gap Bridge, and the target is not realistically reachable pre-event.",
 "wait_requires_negative_info":True,
 "wait_negative_info_basis":"A 0.75-goal drop to the supported burden at >=1.65 would require adverse market movement rather than a healthy prematch path.",
}

def payload(model,match,ctx):
 return {"schema_version":"football-engine-v1","stage":"decision","model":model,"match":match,"context":ctx}

ACCOUNTING={
 "match_id":MATCH_ID,
 "models":[
  {"model":"c","board_state":"C-PASS","supported_line":2.0,"step2_action":"C-PASS"},
  {"model":"c2","board_state":"C2-WATCH","supported_line":2.25,"step2_action":"C2-PASS"},
 ],
 "total_goals":None,
}

RECONCILE={
 "schema_version":"football-step2-reconcile-v1","stage":"step2_reconcile",
 "session_id":"XI-EXC-20261008-WAKRAH-GHARAFA-2358",
 "due":[{"match_id":MATCH_ID,"official_follow_lane":"STOP","step2_authorization":"USER_EXCEPTION"}],
 "outcomes":[{"match_id":MATCH_ID,"status":"DECISION_STATE_PERSISTED"}],
}

class TestWakrahGharafaXiException(unittest.TestCase):
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
  print("WAKRAH_GHARAFA_PAIR="+json.dumps(pair,sort_keys=True))
  print("WAKRAH_GHARAFA_ACCOUNTING="+json.dumps(accounting,sort_keys=True))
  print("WAKRAH_GHARAFA_RECONCILE="+json.dumps(reconciliation,sort_keys=True))
  self.assertEqual(pair["engine_execution_status"],"EXECUTED_C_C2_PAIR")
  self.assertEqual(pair["results"]["c"]["action"],"PASS")
  self.assertEqual(pair["results"]["c2"]["action"],"PASS")
  self.assertTrue(reconciliation["all_due_accounted"])

if __name__=="__main__": unittest.main()
