import json, pathlib, tempfile, unittest
from models.football.engine import xi_portable

TOURNAMENT={
 "tournament_incentive_required":True,"tournament_format_status":"VERIFIED",
 "competition_stage":"2026-27 ADIB Cup league phase, Gameweek 3 of 6",
 "competition_format":"14-club unified league phase; each club plays six matches; top eight advance to quarter-finals",
 "draw_resolution":"League-phase draw stands and awards one point; no extra time or penalties",
 "aggregate_state":"No aggregate score in league phase",
 "simultaneous_results_status":"VERIFIED",
 "simultaneous_results_note":"Concurrent Gameweek 3 results can alter position/cutoff but are non-terminal with three league-phase matches remaining after this round",
 "tiebreak_margin_relevance":"YES",
}

BASE={
 "operational_viability_grade":"A","raw_operational_viability_grade":"A",
 "competition_reliability_state":"UNPROVEN","competition_reliability_reason":"No Competition Reliability row; default UNPROVEN.",
 "competition_reliability_manual_override":"NONE","demoted_probation":False,
 "xi_expected":"YES","market_observability":"HIGH","team_news_observability":"HIGH",
 "operational_viability_reason":"Confirmed user-supplied AiScore XI plus executable Asian-total ladder immediately before kickoff.",
 "route_reliability":"HIGH","chance_quality":"HIGH","xi_robustness":"HIGH","evidence_confidence":"HIGH","burden_protection":"HIGH",
 "failure_attacks_route":False,"material_suppression":False,
 **TOURNAMENT,
}

WASL_COMMON={
 **BASE,"match_id":"bpd-3da187d113852602","kickoff_ict":"2026-10-08T22:45:00+07:00",
 "common_evidence_basis":"Confirmed Al Wasl XI preserves a senior attacking spine including Mehdi Taremi, Renato Junior, Brahian Palacios and Yahia Nader, with Adryelson, Soufiane Bouftini and Rodrigo behind them. Al Wasl have current non-market outputs of 3-2 and 4-0 in this cup and beat Khorfakkan 5-2 in the league on 4 September. Khorfakkan's confirmed XI retains a usable response route and is chasing its first cup points.",
 "home_route":"USABLE","away_route":"STRONG","carrier":"STRONG","independent_route_quality":"HIGH",
 "failure_resistance":"HIGH","main_failure":"A one-sided Wasl lead can still create a late control branch, but the present XI and current-season evidence continue to fund three goals strongly.",
 "h2h_state":"LIMITED","h2h_effect":"NOT_MATERIAL","h2h_transferability":"LIMITED","h2h_current_corroboration":"VERIFIED","h2h_material_effect":False,
 "h2h_basis":"The 5-2 Wasl league win on 4 September is highly current and corroborates the same carrier/leakage mechanisms, but competition transfer is partial so H2H is not used alone.",
 "carrier_self_fund":True,"carrier_self_fund_basis":"Wasl's same current attacking structure has produced 3, 4 and 5-goal team outputs across relevant recent matches and the confirmed XI retains multiple senior scorers/creators.",
 "independent_upper_tail":True,"independent_upper_tail_basis":"Independent current evidence includes Wasl 3-2, 4-0 and 5-2 environments driven by the same carrier and opponent-leakage mechanisms.",
 "failure_attacks_route_basis":"Potential control after leading affects continuation, not the existence of Wasl's primary scoring route.",
 "material_suppression_basis":"No current XI, injury, H2H or incentive suppression veto is verified.",
 "qualification_state":"Al Wasl have six points from two wins and lead the current table; Khorfakkan have zero points and are outside the top eight. Top eight advance after six matches.",
 "home_incentive":"WIN_PREFERRED","away_incentive":"WIN_PREFERRED","incentive_effect":"EXPANSIVE",
}

NASR_COMMON={
 **BASE,"match_id":"bpd-c03f185d9977dd8c","kickoff_ict":"2026-10-08T22:45:00+07:00",
 "common_evidence_basis":"Confirmed Al Nasr XI preserves a strong senior route through Ajdin Hrustic, Kevin Agudelo, Ruben Mierez, Cristian Bedia and attacking support, while Hatta's confirmed XI retains enough forward continuity for a response route. Hatta's two cup matches finished 2-2 and 2-3, and Al Nasr opened the cup 3-1 before a 1-1 draw with Shabab Al Ahli. This gives current non-market third-goal/upper-tail evidence without relying on the market.",
 "home_route":"STRONG","away_route":"USABLE","carrier":"STRONG","independent_route_quality":"HIGH",
 "failure_resistance":"MEDIUM","main_failure":"Al Nasr can control the match after leading and old H2H was often one-sided/low, so the fourth-goal tail is less secure than the third.",
 "h2h_state":"LIMITED","h2h_effect":"NOT_MATERIAL","h2h_transferability":"LIMITED","h2h_current_corroboration":"NOT_APPLICABLE","h2h_material_effect":False,
 "h2h_basis":"Older H2H includes 1-0, 3-0 and 2-0 Nasr wins, but it predates the current personnel and conflicts with Hatta scoring twice in each current cup match; treated as limited/non-material.",
 "carrier_self_fund":False,"carrier_self_fund_basis":"Nasr have one recent three-goal cup output but not enough repeated current carrier-only evidence to certify self-funding above three.",
 "independent_upper_tail":True,"independent_upper_tail_basis":"Hatta's current cup environments are 2-2 and 2-3, Nasr also produced 3-1 in GW1, and the confirmed senior Nasr attack plus Hatta leakage preserve the same mechanisms.",
 "failure_attacks_route_basis":"Control risk caps continuation but does not remove Nasr's strong route or Hatta's current response route.",
 "material_suppression_basis":"No current XI or injury veto removes the primary scoring mechanisms.",
 "qualification_state":"Al Nasr have four points and sit inside the current top eight; Hatta have one point and are outside it. Top eight advance after six matches.",
 "home_incentive":"WIN_PREFERRED","away_incentive":"WIN_PREFERRED","incentive_effect":"EXPANSIVE",
}

def c_match(common,supported,basis,completion,cont,failure,stall):
 return {**common,"supported_line":supported,"supported_line_basis":basis,
  "completion_mode":completion,"burden_completion_quality":"HIGH","continuation_quality":cont,
  "opponent_leakage":"HIGH","burden_stall_risk":stall}

WASL_C=c_match(WASL_COMMON,2.75,"C protects O2.75: confirmed XI preserves Wasl's self-funding carrier and a usable Khorfakkan response route; the current executable O3.0 is above C burden.","MIXED","HIGH","HIGH","MEDIUM")
WASL_C2={**WASL_COMMON,"supported_line":3.0,"supported_line_basis":"C2 independently protects O3.0 from Wasl's strong self-funding carrier, current upper-tail proof and a usable Khorfakkan route."}
NASR_C=c_match(NASR_COMMON,2.5,"C protects O2.5: confirmed senior Nasr route plus Hatta's current response/leakage funds goal three, but current O3.0 remains above official burden.","TWO_SIDED","MEDIUM","MEDIUM","MEDIUM")
NASR_C2={**NASR_COMMON,"supported_line":2.75,"supported_line_basis":"C2 independently protects O2.75 from one strong route, one usable route and current Hatta/Nasr 3+ environments."}

COMMON_CTX={
 "official_follow_lane":"RESERVE","step2_authorization":"USER_EXCEPTION","xi_status":"CONFIRMED",
 "post_xi_research_status":"FOUND","fixture_status":"PREMATCH_CONFIRMED","quote_revalidated":True,
 "h2h_review_status":"REVIEWED_LIMITED","h2h_rechecked":True,
 "tournament_incentive_rechecked":True,"tournament_incentive_recheck_status":"VERIFIED",
 "thesis_state":"PRESERVED","completion_rechecked":True,"c2_route_quality_rechecked":True,
 "top_ranked_focus":False,"primary_mechanism_intact":True,"material_veto":False,
}

WASL_NOTE="Fresh post-XI research confirms Wasl explicitly want to continue scoring/winning, the confirmed XI retains Taremi, Renato Junior, Palacios and Nader, and current outputs 3-2/4-0 plus the September 5-2 over Khorfakkan preserve the carrier and upper tail."
NASR_NOTE="Fresh post-XI research confirms Nasr explicitly target three points and keep their style, while the confirmed XI retains Hrustic, Agudelo, Mierez/Bedia and Hatta retain a usable response unit after scoring twice in both cup matches."

def ctx(board,quote,note,h2h,history_status,history_move,history_note,wait_reach,wait_neg,wait_basis,neg_basis,mech_basis,veto_basis):
 return {**COMMON_CTX,"board_state":board,"quote":quote,"post_xi_research_note":note,
  "h2h_basis":h2h,"market_history_status":history_status,"market_history_movement":history_move,
  "market_history_conflict_recheck":"NOT_REQUIRED","market_history_note":history_note,
  "thesis_state_basis":"Confirmed XI preserves the prospective exception thesis and primary scoring mechanisms.",
  "primary_mechanism_basis":mech_basis,"wait_reachable":wait_reach,"wait_requires_negative_info":wait_neg,
  "wait_reachability_basis":wait_basis,"wait_negative_info_basis":neg_basis,"material_veto_basis":veto_basis}

WASL_C_CTX=ctx("C-FOCUS",{"line":3.0,"odds":1.73},WASL_NOTE,
 "Current-season 5-2 corroborates the same football mechanisms but is not sole proof.",
 "FOUND","STABLE","Public Asian O3 trace was approximately 1.758 opening to 1.763 current; user executable O3.0@1.73 is consistent and shows no material XI-driven conflict.",
 False,True,"O2.75 at >=1.65 is not realistically reachable before kickoff with O3.0 already 1.73.","A lower line rising to the normal floor would require material negative market movement rather than healthy pre-kick decay.",
 "Wasl's confirmed senior attack and Khorfakkan's usable response route remain intact.","No material suppression veto.")
WASL_C2_CTX={**WASL_C_CTX,"board_state":"C2-FOCUS"}

NASR_C_CTX=ctx("C-FOCUS",{"line":3.0,"odds":1.73},NASR_NOTE,
 "Older H2H is limited and not transferable enough to override current Hatta scoring form.",
 "PARTIAL","STABLE","Current public market brackets O2.5 around 1.50-1.57 and O3.5 around 2.16-2.30; user Asian O3.0@1.73 fits the same market center. Reliable OPEN->PRE-XI trace was not established.",
 False,True,"O2.5 at >=1.65 is not realistically reachable before kickoff with O3.0 at 1.73.","A half-goal lower line reaching the normal floor would require material negative movement rather than healthy pre-kick decay.",
 "Nasr's confirmed senior attack remains strong and Hatta preserve a usable response route.","No current XI or incentive suppression veto.")
NASR_C2_CTX={**NASR_C_CTX,"board_state":"C2-FOCUS"}

def payload(model,match,context):
 return {"schema_version":"football-engine-v1","stage":"decision","model":model,"match":match,"context":context}

class TestUaeXiExceptionBlock(unittest.TestCase):
 def test_pairs(self):
  self.assertTrue(xi_portable.self_check()["ok"])
  cases=[
   ("WASL",payload("c",WASL_C,WASL_C_CTX),payload("c2",WASL_C2,WASL_C2_CTX),"PASS","BET"),
   ("NASR",payload("c",NASR_C,NASR_C_CTX),payload("c2",NASR_C2,NASR_C2_CTX),"PASS","BET"),
  ]
  for label,c,c2,ca,c2a in cases:
   with tempfile.TemporaryDirectory() as td:
    root=pathlib.Path(td); p1=root/"c.json"; p2=root/"c2.json"
    p1.write_text(json.dumps(c),encoding="utf-8"); p2.write_text(json.dumps(c2),encoding="utf-8")
    pair=xi_portable.run_pair_files(str(p1),str(p2))
   print(label+"_XI_PAIR="+json.dumps(pair,sort_keys=True))
   self.assertEqual(pair["engine_execution_status"],"EXECUTED_C_C2_PAIR")
   self.assertEqual(pair["results"]["c"]["action"],ca)
   self.assertEqual(pair["results"]["c2"]["action"],c2a)
   self.assertEqual(pair["results"]["c2"]["selection_floor"],"CLEAR")

if __name__=="__main__": unittest.main()
