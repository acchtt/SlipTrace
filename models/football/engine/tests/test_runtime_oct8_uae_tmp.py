import json, pathlib, tempfile, unittest
from models.football.engine import xi_portable

REV="afe75450f246a36ffe7e3029ee519f94cba5a24a"

def base(match_id,kickoff,basis,h2h_basis,home_route,away_route,carrier,upper_tail,carrier_self_fund,incentive_effect,home_incentive,away_incentive,qualification_state):
    return {
      "match_id":match_id,"kickoff_ict":kickoff,
      "operational_viability_grade":"A","raw_operational_viability_grade":"A",
      "competition_reliability_state":"UNPROVEN","competition_reliability_reason":"No current reliability sample sufficient to cap this explicit exception epoch.",
      "competition_reliability_manual_override":"NONE","demoted_probation":False,
      "xi_expected":"YES","market_observability":"HIGH","team_news_observability":"MEDIUM",
      "operational_viability_reason":"Confirmed user-supplied AiScore XI and current public totals market immediately before kickoff.",
      "common_evidence_basis":basis,
      "home_route":home_route,"away_route":away_route,"carrier":carrier,
      "route_reliability":"HIGH","independent_route_quality":"HIGH","chance_quality":"HIGH",
      "failure_resistance":"MEDIUM","xi_robustness":"MEDIUM","evidence_confidence":"HIGH","burden_protection":"MEDIUM",
      "main_failure":"High market burden may require a fourth goal that is less securely funded than the first three.",
      "h2h_state":"REVIEWED","h2h_effect":"LIMITED","h2h_transferability":"LIMITED","h2h_current_corroboration":"CURRENT_FORM_RECHECKED",
      "h2h_material_effect":False,"h2h_basis":h2h_basis,
      "carrier_self_fund":carrier_self_fund,
      "carrier_self_fund_basis":"Current personnel and opponent leakage provide a dominant scoring route, but self-funding is frozen separately from the market price.",
      "independent_upper_tail":upper_tail,
      "independent_upper_tail_basis":"Independent upper-tail proof is based only on current results/mechanisms and opponent leakage; market price itself is excluded.",
      "failure_attacks_route":False,"failure_attacks_route_basis":"The main risk is burden/continuation rather than removal of the primary scoring route.",
      "material_suppression":False,"material_suppression_basis":"No material current suppression veto was verified.",
      "tournament_incentive_required":True,"tournament_format_status":"VERIFIED",
      "competition_stage":"2026-27 ADIB Cup league phase, Gameweek 3 of 6.",
      "competition_format":"Fourteen-club league phase; each club plays six matches, top eight advance to the quarter-finals.",
      "draw_resolution":"League-phase draw awards one point; no extra time or penalties.",
      "aggregate_state":"No aggregate score.","qualification_state":qualification_state,
      "simultaneous_results_status":"VERIFIED","simultaneous_results_note":"Concurrent Gameweek 3 results can move the cutoff but no single concurrent result is determinative at this mid-phase epoch.",
      "home_incentive":home_incentive,"away_incentive":away_incentive,
      "tiebreak_margin_relevance":"YES","incentive_effect":incentive_effect
    }

def context(board_state,quote,post_note,h2h_note,wait_reason,wait_negative,top=False):
    return {
      "board_state":board_state,"official_follow_lane":"STOP","step2_authorization":"USER_EXCEPTION",
      "thesis_state":"PRESERVED","thesis_state_basis":"Confirmed XI preserves the current scoring routes frozen for this exception epoch.",
      "quote":quote,"xi_status":"CONFIRMED","post_xi_research_status":"FOUND","post_xi_research_note":post_note,
      "fixture_status":"PREMATCH_CONFIRMED","quote_revalidated":True,
      "market_history_status":"UNAVAILABLE_ATTEMPTED","market_history_movement":"UNCLEAR",
      "market_history_conflict_recheck":"NOT_REQUIRED","market_history_note":"Current public market revalidated; trustworthy OPEN to PRE-XI trace not established before kickoff.",
      "h2h_review_status":"REVIEWED_LIMITED","h2h_rechecked":True,"h2h_basis":h2h_note,
      "completion_rechecked":True,"c2_route_quality_rechecked":True,"top_ranked_focus":top,
      "primary_mechanism_intact":True,"primary_mechanism_basis":"Confirmed XI preserves the modelled primary route(s).",
      "wait_reachable":False,"wait_reachability_basis":wait_reason,
      "wait_requires_negative_info":wait_negative,"wait_negative_info_basis":"A lower protected line reaching the normal price floor before kickoff would require a material market move rather than ordinary pre-kick decay.",
      "material_veto":False,"material_veto_basis":"No separate current football veto.",
      "tournament_incentive_rechecked":True,"tournament_incentive_recheck_status":"VERIFIED"
    }

SH_BASIS=("Shabab Al Ahli confirmed XI includes Donelli, Keita, Jorge Fernandes, Renan, Rikelme, Damian Garcia, Elian Irala, Markelo, Cartabia, Juma and Ghandipour. "
"United retain Maouhoub and other senior attacking pieces. Shabab opened the league phase 2-2 and 1-1; United opened 1-3 and 3-2. "
"United have conceded three in both league-phase matches, while Shabab remain a strong home carrier and United retain a usable response route. "
"This supplies non-market evidence for a third/fourth-goal tail, though O3.5 is still above Football C's protected burden.")
SH=base("EXC-20261008-SHABAB-UNITED","2026-10-08T20:10:00+07:00",SH_BASIS,
        "Only one recent meeting, a 1-1 in September 2026, so H2H is limited and not suppressive.",
        "STRONG","USABLE","STRONG",True,True,"ATTACKING","WIN_PREFERRED","DRAW_USEFUL_WIN_PREFERRED",
        "Shabab are 9th on 2 points and United 7th on 3; top eight after six matches qualify, so both have material point utility and goal difference matters.")
SH_C={**SH,"supported_line":2.75,"supported_line_basis":"C protects O2.75: the third goal is funded, but O3.5 asks for a less-protected fourth-goal outcome.",
      "completion_mode":"CARRIER_LED","burden_completion_quality":"HIGH","continuation_quality":"HIGH","opponent_leakage":"HIGH","burden_stall_risk":"MEDIUM"}
SH_C2={**SH,"supported_line":3.0,"supported_line_basis":"C2 independently supports O3.0 from Shabab's strong carrier plus United's usable route and repeated current high-goal leakage."}
SH_CTX_C=context("C-FOCUS",{"line":3.5,"odds":1.73},"Fresh post-XI research confirmed Shabab's 2-2/1-1 league-phase start, United's 1-3/3-2 start, United conceding three in both matches, the confirmed senior Shabab XI, and current top-eight qualification pressure.","Recent 1-1 H2H is limited/non-material.","O2.75 at >=1.65 is not realistically reachable before kickoff while O3.5 is already 1.73.",True)
SH_CTX_C2=context("C2-FOCUS",{"line":3.5,"odds":1.73},"Fresh post-XI research confirmed Shabab's 2-2/1-1 league-phase start, United's 1-3/3-2 start, United conceding three in both matches, the confirmed senior Shabab XI, and current top-eight qualification pressure.","Recent 1-1 H2H is limited/non-material.","A lower O3.0 target is not realistically reachable at >=1.65 before kickoff.",True)

AA_BASIS=("Al Ain confirmed XI is materially changed from the cup teams led by Giakoumakis/Kaku but still contains senior attacking quality including Soufiane Rahimi and Baba Bello. "
"Al Ain's first two league-phase matches both finished 2-3, while Kalba opened 2-1 then lost 0-4. "
"Al Ain have zero points and must materially improve their qualification position; Kalba sit on the cutoff with three points and a -3 goal difference. "
"The two-route environment is credible, but today's Al Ain changes weaken independent proof that the match can sustain a fourth goal.")
AA=base("EXC-20261008-ALAIN-KALBA","2026-10-08T20:10:00+07:00",AA_BASIS,
        "Recent H2H is Al Ain-favouring (including 2-0 and 3-1 wins plus a 0-0/1-1 pair); it is mixed and not a standalone current veto.",
        "STRONG","USABLE","STRONG",False,False,"ATTACKING","WIN_HIGH_UTILITY","DRAW_USEFUL_WIN_PREFERRED",
        "Al Ain are 11th on 0 points after two losses; Kalba are 8th on 3 points with -3 GD. Top eight qualify after six matches, so Al Ain have strong win utility and Kalba have both point and GD incentives.")
AA_C={**AA,"supported_line":2.75,"supported_line_basis":"C protects O2.75: both routes can contribute, but today's altered Al Ain attack does not independently fund O3.5.",
      "completion_mode":"TWO_SIDED","burden_completion_quality":"HIGH","continuation_quality":"MEDIUM","opponent_leakage":"HIGH","burden_stall_risk":"MEDIUM"}
AA_C2={**AA,"supported_line":3.0,"supported_line_basis":"C2 independently supports O3.0 from Al Ain's strong route, Kalba's usable response route and current leakage, but not the O3.5 tail under this XI."}
AA_CTX_C=context("C-FOCUS",{"line":3.5,"odds":1.83},"Fresh post-XI research confirmed Al Ain's 2-3/2-3 league-phase start, Kalba's 2-1/0-4 start, current top-eight qualification pressure, and a materially changed Al Ain attack that still includes senior quality but weakens upper-tail continuity.","Recent Al Ain-dominant H2H was rechecked and remains limited rather than determinative.","O2.75 at >=1.65 is not realistically reachable before kickoff while O3.5 is around 1.83.",True)
AA_CTX_C2=context("C2-FOCUS",{"line":3.5,"odds":1.83},"Fresh post-XI research confirmed Al Ain's 2-3/2-3 league-phase start, Kalba's 2-1/0-4 start, current top-eight qualification pressure, and a materially changed Al Ain attack that still includes senior quality but weakens upper-tail continuity.","Recent H2H is mixed/limited and does not create upper-tail proof.","O3.0 at >=1.65 is not realistically reachable before kickoff.",True)

def payload(model,match,ctx):
    return {"schema_version":"football-engine-v1","stage":"decision","model":model,"match":match,"context":ctx}

class RuntimeOct8Uae(unittest.TestCase):
    def run_pair(self,label,c,c2):
        check=xi_portable.self_check(); self.assertTrue(check["ok"])
        with tempfile.TemporaryDirectory() as td:
            root=pathlib.Path(td); p1=root/"c.json"; p2=root/"c2.json"
            p1.write_text(json.dumps(c),encoding="utf-8"); p2.write_text(json.dumps(c2),encoding="utf-8")
            pair=xi_portable.run_pair_files(str(p1),str(p2))
        print(label+"_PAIR="+json.dumps(pair,sort_keys=True))
        return pair
    def test_pairs(self):
        sh=self.run_pair("SHABAB_UNITED",payload("c",SH_C,SH_CTX_C),payload("c2",SH_C2,SH_CTX_C2))
        aa=self.run_pair("ALAIN_KALBA",payload("c",AA_C,AA_CTX_C),payload("c2",AA_C2,AA_CTX_C2))
        self.assertEqual(sh["results"]["c"]["action"],"PASS")
        self.assertEqual(sh["results"]["c2"]["action"],"BET")
        self.assertTrue(sh["results"]["c2"]["bridge_used"])
        self.assertEqual(aa["results"]["c"]["action"],"PASS")
        self.assertEqual(aa["results"]["c2"]["action"],"PASS")

if __name__=="__main__": unittest.main()
