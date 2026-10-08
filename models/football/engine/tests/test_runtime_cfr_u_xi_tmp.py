import json, pathlib, tempfile, unittest
from models.football.engine import xi_portable
MID="bpd-57f99117f232d539"
COMMON={
 "match_id":MID,"kickoff_ict":"2026-10-09T00:30:00+07:00",
 "operational_viability_grade":"A","raw_operational_viability_grade":"A",
 "competition_reliability_state":"UNPROVEN","competition_reliability_reason":"No Competition Reliability row; default UNPROVEN.",
 "competition_reliability_manual_override":"NONE","demoted_probation":False,
 "xi_expected":"YES","market_observability":"HIGH","team_news_observability":"HIGH",
 "operational_viability_reason":"Confirmed user-supplied AiScore XI plus executable Asian-total ladder inside the prematch window.",
 "common_evidence_basis":"Confirmed XI resolves most of the pre-match CFR illness uncertainty: CFR still field a senior spine including Camora, Rocha, Braun, Omic, Nalic and Perianu, while Universitatea retain Nistor, Bic, Aliev and other first-team attackers. U Cluj are chasing a third straight league win and have scored 11 across their last five; CFR's recent league sequence includes 3-1, 1-3, 0-0, 3-2 and 1-0. This supports two usable routes with U Cluj upgraded to STRONG, but derby control/draw acceptance still caps continuation.",
 "home_route":"USABLE","away_route":"STRONG","carrier":"USABLE",
 "route_reliability":"MEDIUM","independent_route_quality":"MEDIUM","chance_quality":"MEDIUM",
 "failure_resistance":"MEDIUM","xi_robustness":"HIGH","evidence_confidence":"HIGH","burden_protection":"HIGH",
 "main_failure":"Local-derby control and explicit draw acceptance can stall the match after one exchange; neither side is independently proven to self-fund three.",
 "h2h_state":"LIMITED","h2h_effect":"MIXED","h2h_transferability":"LIMITED","h2h_current_corroboration":"VERIFIED","h2h_material_effect":False,
 "h2h_basis":"Recent same-venue 1-0 and 3-2 outcomes remain mixed, so H2H is corroborative only.",
 "carrier_self_fund":False,"carrier_self_fund_basis":"No single team has enough current evidence to certify repeated three-goal self-funding in this derby context.",
 "independent_upper_tail":False,"independent_upper_tail_basis":"Current form supports goal-three possibility but not a repeatable four-goal tail.",
 "failure_attacks_route":False,"failure_attacks_route_basis":"Control risk affects continuation, not the existence of either primary route.",
 "material_suppression":False,"material_suppression_basis":"No current XI or injury veto removes the primary mechanisms.",
 "tournament_incentive_required":False,"tournament_format_status":"NOT_APPLICABLE",
 "competition_stage":"NOT_APPLICABLE","competition_format":"NOT_APPLICABLE","draw_resolution":"NOT_APPLICABLE","aggregate_state":"NOT_APPLICABLE","qualification_state":"NOT_APPLICABLE",
 "simultaneous_results_status":"NOT_APPLICABLE","simultaneous_results_note":"NOT_APPLICABLE","home_incentive":"NOT_APPLICABLE","away_incentive":"NOT_APPLICABLE","tiebreak_margin_relevance":"NOT_APPLICABLE","incentive_effect":"NOT_APPLICABLE",
}
C={**COMMON,"supported_line":2.25,"supported_line_basis":"Frozen C burden remains O2.25. Confirmed XI improves robustness but does not justify a higher protected burden.","completion_mode":"TWO_SIDED","burden_completion_quality":"MEDIUM","continuation_quality":"MEDIUM","opponent_leakage":"MEDIUM","burden_stall_risk":"MEDIUM"}
C2={**COMMON,"supported_line":2.25,"supported_line_basis":"Frozen C2 burden remains O2.25. Confirmed XI upgrades the away route enough for a CLEAR two-route floor, but does not justify raising the burden."}
BASECTX={
 "official_follow_lane":"STOP","step2_authorization":"USER_EXCEPTION","xi_status":"CONFIRMED",
 "post_xi_research_status":"FOUND","post_xi_research_note":"Fresh post-XI research confirms U Cluj seek a third straight league win and Bergodi says they will try to win, while a draw is acceptable only if the team shows winning intent. CFR's official recent results include 3-1 vs Botosani, 0-0 vs Farul, 3-2 at Csikszereda and 1-0 vs FCSB. The confirmed XI materially reduces the earlier CFR personnel-uncertainty concern.",
 "fixture_status":"PREMATCH_CONFIRMED","quote_revalidated":True,
 "market_history_status":"PARTIAL","market_history_movement":"STABLE","market_history_conflict_recheck":"NOT_REQUIRED",
 "market_history_note":"Public O2.5 was around 1.76-1.80 in recent snapshots; user executable O2.5@1.82 and O2.25@1.60 are consistent with a stable market centered near 2.5. Trustworthy Asian OPEN->PRE-XI trace remains partial.",
 "h2h_review_status":"REVIEWED_LIMITED","h2h_rechecked":True,"h2h_basis":"Recent H2H remains mixed and non-determinative.",
 "tournament_incentive_rechecked":False,"tournament_incentive_recheck_status":"NOT_APPLICABLE",
 "thesis_state":"PRESERVED","thesis_state_basis":"Confirmed XI improves route robustness without changing the derby-control failure mode.",
 "primary_mechanism_intact":True,"primary_mechanism_basis":"Both sides retain their main creators/attackers and U Cluj's route is stronger than at Step 1.",
 "material_veto":False,"material_veto_basis":"No hard veto.",
 "wait_reachable":True,"wait_reachability_basis":"O2.25 is already available at 1.60; only a small price move to 1.65 is needed and is plausibly reachable through ordinary pre-kick/early scoreless decay.",
 "wait_requires_negative_info":False,"wait_negative_info_basis":"The target price can arise from ordinary clock decay rather than adverse football information.","top_ranked_focus":False
}
CC={**BASECTX,"board_state":"C-WATCH","quote":{"line":2.25,"odds":1.60},"completion_rechecked":True}
C2C={**BASECTX,"board_state":"C2-WATCH","quote":{"line":2.25,"odds":1.60},"c2_route_quality_rechecked":True}
def p(model,m,c): return {"schema_version":"football-engine-v1","stage":"decision","model":model,"match":m,"context":c}
class T(unittest.TestCase):
 def test_pair(self):
  self.assertTrue(xi_portable.self_check()["ok"])
  with tempfile.TemporaryDirectory() as td:
   root=pathlib.Path(td); a=root/"c.json"; b=root/"c2.json"
   a.write_text(json.dumps(p("c",C,CC))); b.write_text(json.dumps(p("c2",C2,C2C)))
   out=xi_portable.run_pair_files(str(a),str(b))
  print("CFR_U_PAIR="+json.dumps(out,sort_keys=True))
  self.assertEqual(out["engine_execution_status"],"EXECUTED_C_C2_PAIR")
  self.assertEqual(out["results"]["c"]["action"],"WAIT")
  self.assertEqual(out["results"]["c2"]["action"],"WAIT")
  self.assertEqual(out["results"]["c2"]["selection_floor"],"CLEAR")
if __name__=="__main__": unittest.main()
