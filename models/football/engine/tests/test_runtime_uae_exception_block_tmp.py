import json, pathlib, subprocess, sys, tempfile, unittest

COMMON_TOURNAMENT = {
    "tournament_incentive_required": True,
    "tournament_format_status": "VERIFIED",
    "competition_stage": "2026-27 ADIB Cup league phase, Gameweek 3 of 6",
    "competition_format": "14-club unified league phase; each club plays six matches; top eight advance to the quarter-finals",
    "draw_resolution": "League-phase draw stands and awards one point; no extra time or penalties",
    "aggregate_state": "No aggregate score in league phase",
    "simultaneous_results_status": "VERIFIED",
    "simultaneous_results_note": "Other Gameweek 3 results can alter position/cutoff but are non-terminal with three league-phase matches still remaining after this round",
    "tiebreak_margin_relevance": "YES",
}

BASE = {
    "kickoff_ict": "2026-10-08T22:45:00+07:00",
    "operational_viability_grade": "A",
    "raw_operational_viability_grade": "A",
    "competition_reliability_state": "UNPROVEN",
    "competition_reliability_reason": "No Competition Reliability row; default UNPROVEN.",
    "competition_reliability_manual_override": "NONE",
    "demoted_probation": False,
    "xi_expected": "YES",
    "market_observability": "HIGH",
    "team_news_observability": "HIGH",
    "operational_viability_reason": "A operational grade from reconciled kickoff plus high XI, market and team-news observability.",
    "h2h_state": "LIMITED",
    "h2h_effect": "NOT_MATERIAL",
    "h2h_transferability": "LIMITED",
    "h2h_current_corroboration": "FOUND",
    "h2h_material_effect": False,
    "failure_attacks_route": False,
    "material_suppression": False,
    **COMMON_TOURNAMENT,
}

NASR_COMMON = {
    **BASE,
    "match_id": "bpd-c03f185d9977dd8c",
    "common_evidence_basis": "Al Nasr opened the ADIB Cup with a 3-1 win over United, then drew 1-1 with Shabab Al Ahli after leading until stoppage time. Hatta drew 2-2 with Shabab Al Ahli and lost 3-2 to United, scoring twice in both cup matches. Al Nasr therefore provide the strong route and Hatta a usable response route; Hatta's current defensive leakage plus their need to recover from 10th place improves third-goal funding, while Al Nasr can still control a lead.",
    "home_route": "STRONG",
    "away_route": "USABLE",
    "carrier": "STRONG",
    "route_reliability": "HIGH",
    "independent_route_quality": "MEDIUM",
    "chance_quality": "HIGH",
    "failure_resistance": "MEDIUM",
    "xi_robustness": "MEDIUM",
    "evidence_confidence": "HIGH",
    "burden_protection": "HIGH",
    "main_failure": "Al Nasr have shown they can protect/manage a lead and Hatta remain inconsistent, so a natural two-goal endpoint is still possible.",
    "h2h_basis": "Historical Al Nasr-Hatta meetings are older and not strongly transferable; current cup form is more relevant.",
    "carrier_self_fund": False,
    "carrier_self_fund_basis": "Al Nasr scored three against United but one current 3-goal carrier result is insufficient to certify repeated self-funding above the protected burden.",
    "independent_upper_tail": False,
    "independent_upper_tail_basis": "The current two-route evidence funds goal three better than it independently funds a fourth.",
    "failure_attacks_route_basis": "Control risk affects continuation, not the existence of the two scoring routes.",
    "material_suppression_basis": "No current tactical/personnel or H2H suppression veto verified.",
    "qualification_state": "Al Nasr have 4 points and sit inside the current top eight; Hatta have 1 point and sit outside it. Top eight advance after six league-phase matches.",
    "home_incentive": "WIN_PREFERRED",
    "away_incentive": "WIN_PREFERRED",
    "incentive_effect": "EXPANSIVE",
}

WASL_COMMON = {
    **BASE,
    "match_id": "bpd-3da187d113852602",
    "common_evidence_basis": "Al Wasl have won both ADIB Cup matches, 3-2 over Al Ain and 4-0 over Kalba, scoring seven goals. They also beat Khorfakkan 5-2 in the league on 4 September. Khorfakkan lost 2-1 to Kalba and 2-0 to Al Jazira in the cup and are still on zero points, but they scored twice in the recent league meeting with Wasl and now have strong need for points. Wasl provide a strong self-funding carrier and Khorfakkan retain a usable response route.",
    "home_route": "USABLE",
    "away_route": "STRONG",
    "carrier": "STRONG",
    "route_reliability": "HIGH",
    "independent_route_quality": "HIGH",
    "chance_quality": "HIGH",
    "failure_resistance": "HIGH",
    "xi_robustness": "MEDIUM",
    "evidence_confidence": "HIGH",
    "burden_protection": "HIGH",
    "main_failure": "A one-sided Wasl lead could reduce late urgency, but current evidence repeatedly funds both a strong carrier and continuation beyond two goals.",
    "h2h_basis": "The current-season 5-2 Wasl league win is highly current but competition-context transfer is partial; it supports route evidence without being used alone.",
    "carrier_self_fund": True,
    "carrier_self_fund_basis": "Wasl scored 3 and 4 in their two cup matches and 5 against this opponent in the current league season, giving independent current self-funding evidence.",
    "independent_upper_tail": True,
    "independent_upper_tail_basis": "Current non-market evidence includes 3-2, 4-0 and 5-2 outputs with repeated second-half continuation.",
    "failure_attacks_route_basis": "Potential game control after a lead is a continuation risk but does not attack Wasl's scoring route.",
    "material_suppression_basis": "No current categorical suppression veto verified.",
    "qualification_state": "Al Wasl lead on 6 points from two wins; Khorfakkan have 0 points and are outside the top eight. Top eight advance after six league-phase matches.",
    "home_incentive": "WIN_PREFERRED",
    "away_incentive": "WIN_PREFERRED",
    "incentive_effect": "EXPANSIVE",
}

C_MATCHES = [
    {
        **WASL_COMMON,
        "supported_line": 2.75,
        "supported_line_basis": "C protects O2.75 because Wasl's current carrier can self-fund three and Khorfakkan retain a usable response route; the fourth goal is plausible but not required for the protected burden.",
        "board_state": "FOCUS",
        "board_state_basis": "High-quality current carrier, strong continuation evidence, opponent leakage and expansive league-phase incentive support a C-FOCUS state.",
        "completion_mode": "MIXED",
        "burden_completion_quality": "HIGH",
        "continuation_quality": "HIGH",
        "opponent_leakage": "HIGH",
        "burden_stall_risk": "MEDIUM",
    },
    {
        **NASR_COMMON,
        "supported_line": 2.5,
        "supported_line_basis": "C protects O2.5: Al Nasr's strong route plus Hatta's proven cup response route credibly fund goal three, while control risk limits a higher protected burden.",
        "board_state": "FOCUS",
        "board_state_basis": "Two current scoring routes, Hatta leakage and table pressure support FOCUS, but only medium failure resistance prevents a stronger burden.",
        "completion_mode": "TWO_SIDED",
        "burden_completion_quality": "HIGH",
        "continuation_quality": "MEDIUM",
        "opponent_leakage": "HIGH",
        "burden_stall_risk": "MEDIUM",
    },
]

C2_MATCHES = [
    {
        **{k:v for k,v in WASL_COMMON.items()},
        "supported_line": 3.0,
        "supported_line_basis": "C2 independently supports O3.0 from Wasl's strong self-funding carrier, current upper-tail proof and a usable Khorfakkan response route.",
        "board_state": "FOCUS",
        "board_state_basis": "C2 route-quality floor is strong: a strong carrier self-funds and independent upper-tail evidence is current and non-market.",
    },
    {
        **{k:v for k,v in NASR_COMMON.items()},
        "supported_line": 2.75,
        "supported_line_basis": "C2 independently supports O2.75 because both routes are usable with Al Nasr strong, while Hatta's two cup goals in each match preserve response quality.",
        "board_state": "FOCUS",
        "board_state_basis": "C2 clears the exact two-route floor with one strong route and no hard suppression veto.",
    },
]

C_PAYLOAD={"schema_version":"football-engine-v1","stage":"board","model":"c","matches":C_MATCHES}
C2_PAYLOAD={"schema_version":"football-engine-v1","stage":"board","model":"c2","matches":C2_MATCHES}

class TestUaeExceptionBlock(unittest.TestCase):
    def test_pair(self):
        with tempfile.TemporaryDirectory() as td:
            root=pathlib.Path(td)
            c=root/"c.json"; c2=root/"c2.json"
            c.write_text(json.dumps(C_PAYLOAD),encoding="utf-8")
            c2.write_text(json.dumps(C2_PAYLOAD),encoding="utf-8")
            p=subprocess.run([sys.executable,"models/football/engine/board_pair_cli.py","--c",str(c),"--c2",str(c2)],capture_output=True,text=True)
            print("BOARD_PAIR_STDOUT="+p.stdout.strip())
            print("BOARD_PAIR_STDERR="+p.stderr.strip())
            self.assertEqual(p.returncode,0,p.stderr)
            out=json.loads(p.stdout)
            self.assertTrue(out["ok"])
            self.assertEqual(out["board_engine_execution_status"],"EXECUTED_C_C2_BOARDS")
            self.assertTrue(out["common_evidence_reconciled"])

if __name__=="__main__": unittest.main()
