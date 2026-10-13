"""V4 replacement contract: researched league scope + single immutable C/C2 board."""
from __future__ import annotations

import copy
import json
import pathlib
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone

DIR = pathlib.Path(__file__).resolve().parent
ENGINE_TESTS = DIR.parent / "engine" / "tests"
sys.path.insert(0, str(DIR))
sys.path.insert(0, str(ENGINE_TESTS))

from league_registry import classify, REGISTRY
from stage import StageError, sweep, rank as production_rank, verify_rank
from test_board_pair import c_row, c2_row, payload

NOW = "2026-10-11T16:00:00Z"
KICKOFF = "2026-10-11T17:00:00Z"
KICKOFF_ICT = "2026-10-12T00:00:00+07:00"


def fixture(mid, country="England", league="Premier League", kind="DOMESTIC_LEAGUE",
            *, proof=None, ko=KICKOFF, goals="HIGH"):
    result = {
        "match_id": mid, "country": country, "competition": league,
        "competition_kind": kind, "home": "Home FC", "away": "Away FC",
        "kickoff_utc": ko, "fixture_status": "PREMATCH_CONFIRMED",
        "source_url": "https://sports.example.org/fixture/" + mid,
        "observed_at_utc": "2026-10-11T15:59:00Z",
    }
    if goals:
        if goals == "HIGH":
            scores = [(3,2), (2,1), (4,1), (2,2)]
        elif goals == "TRAP":
            scores = [(0,0), (1,1), (0,0), (1,1)]
        else:
            raise ValueError("invalid test goals")
        games = [{
            "kickoff_utc": f"2026-09-{day:02d}T12:00:00Z",
            "goals_for": gf, "goals_against": ga,
        } for day, (gf, ga) in zip((1,8,15,22), scores)]
        result["football_evidence"] = {
            side: {
                "source_url": f"https://results.example.org/{mid}/{side}",
                "observed_at_utc": "2026-10-11T15:58:00Z",
                "recent": copy.deepcopy(games),
            } for side in ("home","away")
        }
    if proof:
        result["researchability_status"] = proof
        if proof == "VERIFIED":
            result["researchability_proof"] = {
                "match_id": mid,
                "source_url": "https://sports.example.org/league/researchability",
                "checked_at_utc": "2026-10-11T15:59:00Z",
                "current_channels_checked": True,
            }
    return result


def snapshot(fixtures=None):
    return {
        "schema_version": "football-stages-v4",
        "run_id": "V4-20261011-1600",
        "window_start_utc": "2026-10-11T15:50:00Z",
        "window_end_utc": "2026-10-11T23:00:00Z",
        "source_family": "Fixture Provider One",
        "source_url": "https://sports.example.org/20261011/fixtures",
        "source_observed_at_utc": "2026-10-11T15:59:00Z",
        "fixtures": fixtures if fixtures is not None else [
            fixture("m1"), fixture("m2","Netherlands","Eerste Divisie"),
        ],
    }


def model_inputs(mid="m1"):
    a, b = c_row(), c2_row()
    a["match_id"] = mid
    b["match_id"] = mid
    a["kickoff_ict"] = KICKOFF_ICT
    b["kickoff_ict"] = KICKOFF_ICT
    return payload("c", a), payload("c2", b)


class ResearchedRegistryTests(unittest.TestCase):
    def test_top_five_and_key_pilots_are_present(self):
        for country, league in (
            ("England","Premier League"),("Germany","Bundesliga"),
            ("Spain","La Liga"),("Italy","Serie A"),("France","Ligue 1"),
            ("Netherlands","Eredivisie"),("Netherlands","Eerste Divisie"),
            ("Norway","Eliteserien"),("Norway","OBOS-ligaen"),
            ("Sweden","Allsvenskan"),("Denmark","Danish Superliga"),
            ("Finland","Finnish Veikkausliiga"),
            ("Japan","J1 League"),("Japan","J2 League"),
        ):
            with self.subTest(country=country, league=league):
                self.assertEqual(classify(fixture("a",country,league))["lane"], "ROUTINE")
        for country, league in (
            ("England","Championship"), ("Spain","Segunda Division"),
            ("Germany","2. Bundesliga"),
            ("Poland","Ekstraklasa"), ("Poland","PKO Bank Polski EKSTRAKLASA"),
            ("Poland","I Liga"), ("Poland","Liga 1"),
            ("Czech Republic","Czech FNL"),
            ("Hong Kong","Hong Kong Premier League"),
            ("Malaysia","Liga Super"),("Qatar","Qatar Stars League"),
            ("UAE","UAE Pro League"),
            ("Japan","Nadeshiko League 1"),("Japan","Nadeshiko League 2"),
            ("Thailand","Thai League 1"),
            ("Indonesia","Liga 1"),
        ):
            with self.subTest(country=country, league=league):
                expected = "ROUTINE" if country == "Germany" else (
                    "PILOT" if country in ("Thailand","Indonesia") else "CONDITIONAL")
                self.assertEqual(classify(fixture("a",country,league))["lane"], expected)

    def test_user_exclusions_friends_and_weak_data_remain_protected(self):
        for country, league in (
            ("Germany","3. Liga"), ("France","Ligue 2"),
            ("Italy","Serie B"),("Israel","Premier League"),
            ("Bangladesh","Premier League"),("Norway","3. divisjon"),
        ):
            self.assertEqual(classify(fixture("a",country,league))["lane"], "EXCLUDED")
        self.assertEqual(classify(fixture("a","England","Club Friendlies"))["lane"], "EXCLUDED")
        self.assertEqual(classify(fixture("a","Pakistan","Premier League"))["lane"], "DISCOVERY")

    def test_verified_women_topflight_and_competitive_cups_without_global_scan(self):
        self.assertEqual(classify(fixture(
            "w1","England","Women's Super League","WOMENS_TOP_FLIGHT"
        ))["lane"],"CONDITIONAL")
        self.assertEqual(classify(fixture(
            "cup1","Japan","WE League Cup","DOMESTIC_CUP"
        ))["lane"],"CONDITIONAL")
        self.assertEqual(classify(fixture(
            "cup2","Japan","Empress's Cup Women","DOMESTIC_CUP"
        ))["lane"],"CONDITIONAL")


class SweepV4Tests(unittest.TestCase):
    def test_intake_does_not_require_odds_xi_or_worldwide_women_proof(self):
        result = sweep(snapshot(), now=NOW)
        self.assertEqual(result["status"],"V4_SWEEP_READY")
        self.assertEqual(result["eligible_count"],2)
        self.assertEqual(len(result["research_order"]),2)
        self.assertTrue(result["no_fixed_eight_match_cap"])
        self.assertFalse(result["price_required_for_football"])
        self.assertFalse(result["published"])

    def test_goal_quality_beats_urgency_and_registered_league_status(self):
        urgent=fixture("urgent","England","Premier League",
                       ko="2026-10-11T16:10:00Z")
        # A moderate but still qualified source-backed 3+ history.
        games=[(2,2),(3,1),(2,1),(2,1)]
        for side in ("home","away"):
            urgent["football_evidence"][side]["recent"]=[
                {"kickoff_utc":f"2026-09-{day:02d}T12:00:00Z",
                 "goals_for":gf,"goals_against":ga}
                for day,(gf,ga) in zip((1,8,15,22),games)
            ]
        later=fixture("later","Netherlands","Eerste Divisie")
        out=sweep(snapshot([urgent,later]),now=NOW)
        self.assertEqual(out["eligible_count"],2)
        self.assertEqual(out["research_order"][0],"later")
        self.assertEqual(out["goal_screen_manifest"]["priority_profile"],
                         "GOAL_SIGNAL_FIRST_V1")
        from goal_route_prescreen import verified_research_order
        validated=verified_research_order(
            out["goal_screen_manifest"],
            [{"match_id":row["match_id"],"queue_rank":row["queue_rank"],
              "operational_grade":row["operational_grade"]}
             for row in out["eligible_queue"]],
            out["source_ledger_hash"],
        )
        self.assertEqual(validated,out["research_order"])

    def test_registered_fixture_without_goal_history_is_not_a_rank_selection(self):
        src=snapshot([
            fixture("registered","England","Premier League",goals=None),
            fixture("qualified","Brazil","Serie A",proof="VERIFIED"),
        ])
        out=sweep(src,now=NOW)
        self.assertEqual(out["eligible_count"],1)
        self.assertEqual(out["eligible_queue"][0]["match_id"],"qualified")
        self.assertEqual(out["goal_research_queue"][0]["match_id"],"registered")
        self.assertEqual(out["unresearched_goal_history_count"],1)
        self.assertEqual(out["source_ledger"][0]["registry_lane"],"ROUTINE")
        self.assertEqual(out["source_ledger"][0]["intake_lane"],"PENDING_GOAL_RESEARCH")
        self.assertEqual(out["goal_selection_policy"],
                         "EQUAL_SOURCE_BACKED_GOAL_SIGNAL_ALL_LEAGUES_V1")

    def test_registered_low_goals_do_not_displace_high_goals_lower_league(self):
        src=snapshot([
            fixture("weak","England","Premier League",goals="TRAP"),
            fixture("strong","Netherlands","Eerste Divisie",goals="HIGH"),
        ])
        out=sweep(src,now=NOW)
        self.assertEqual(out["eligible_count"],1)
        self.assertEqual(out["eligible_queue"][0]["match_id"],"strong")
        self.assertEqual(out["low_goal_signal_count"],1)
        self.assertEqual(out["goal_research_queue"][0]["match_id"],"weak")
        self.assertEqual(out["goal_research_queue"][0]["goal_screen"]["status"],"WATCH_GOAL_SIGNAL")

    def test_all_registered_missing_results_returns_honest_zero_goal_shortlist(self):
        out=sweep(snapshot([
            fixture("x","England","Premier League",goals=None),
            fixture("y","Germany","Bundesliga",goals=None),
        ]),now=NOW)
        self.assertEqual(out["eligible_count"],0)
        self.assertEqual(out["fixture_count"],2)
        self.assertEqual(out["pending_goal_research_count"],2)
        self.assertEqual(len(out["goal_research_order"]),2)
        self.assertEqual(out["research_order"],[])
        self.assertFalse(out["bet_recorded"])

    def test_researched_conditional_kept_pending_until_current_channels_verified(self):
        src = snapshot([
            fixture("m1"), fixture("m2","Poland","Ekstraklasa"),
            fixture("m3","Malaysia","Liga Super",proof="VERIFIED"),
            fixture("m4","England","Women's Super League","WOMENS_TOP_FLIGHT",proof="VERIFIED"),
        ])
        result = sweep(src,now=NOW)
        self.assertEqual(result["eligible_count"],3)
        self.assertEqual(result["pending_researchability_count"],1)
        self.assertEqual(result["fixture_count"],4)
        self.assertEqual({x["match_id"] for x in result["eligible_queue"]},{"m1","m3","m4"})

    def test_unverified_conditional_proof_is_quarantined_not_global_blocker(self):
        a = fixture("m2", "Poland", "Ekstraklasa", proof="VERIFIED")
        a.pop("researchability_proof")
        out = sweep(snapshot([fixture("m1"), a]), now=NOW)
        self.assertEqual(out["eligible_count"],1)
        self.assertEqual(out["pending_source_count"],1)
        self.assertIn("requires source evidence",out["source_ledger"][1]["reason"])
        a = fixture("m2", "Poland", "Ekstraklasa", proof="VERIFIED")
        a["researchability_proof"]["match_id"] = "wrong-match"
        out = sweep(snapshot([fixture("m1"), a]), now=NOW)
        self.assertEqual(out["pending_source_count"],1)
        self.assertIn("not bound to fixture",out["source_ledger"][1]["reason"])

    def test_researched_leagues_not_arbitrarily_capped_at_eight(self):
        rows = [fixture(f"match-{i}", country="Netherlands",league="Eerste Divisie")
                for i in range(1,21)]
        result = sweep(snapshot(rows),now=NOW)
        self.assertEqual(result["eligible_count"],20)
        self.assertEqual(len(result["research_order"]),20)

    def test_one_malformed_goal_history_is_evidence_limited_not_global_failure(self):
        a=fixture("m1")
        bad_games=[
            {"kickoff_utc":f"2026-09-{d:02d}T12:00:00Z",
             "goals_for":2,"goals_against":0}
            for d in (1,8,15,22)
        ]
        a["football_evidence"]={
            "home":{"source_url":"http://bad.source", "recent":bad_games,
                    "observed_at_utc":"2026-10-11T15:58:00Z"},
            "away":{"source_url":"http://bad.source", "recent":bad_games,
                    "observed_at_utc":"2026-10-11T15:58:00Z"},
        }
        out=sweep(snapshot([a,fixture("m2","Norway","OBOS-ligaen")]),now=NOW)
        self.assertEqual(out["eligible_count"],1)
        self.assertEqual(out["pending_goal_research_count"],1)
        self.assertEqual(out["goal_research_queue"][0]["match_id"],"m1")
        self.assertEqual(out["goal_research_queue"][0]["goal_screen"]["status"],
                         "PENDING_SOURCE_SCORING_EVIDENCE")
        self.assertEqual(len(out["invalid_historical_form_sources"]),0)
        self.assertEqual(len(out["research_order"]),1)

    def test_real_recent_high_scoring_team_evidence_is_prioritized(self):
        good=fixture("m1","Netherlands","Eredivisie")
        games=[
            {"kickoff_utc":f"2026-09-{d:02d}T12:00:00Z",
             "goals_for":3,"goals_against":1}
            for d in (1,8,15,22)
        ]
        proof={"source_url":"https://sports.example.org/recent-results",
               "observed_at_utc":"2026-10-11T15:58:00Z",
               "recent":games}
        good["football_evidence"]={"home":proof,"away":proof}
        out=sweep(snapshot([good,fixture("m2","England","Premier League")]),now=NOW)
        self.assertEqual(out["eligible_count"],2)
        self.assertEqual(out["goal_screen_manifest"]["priority_profile"],"GOAL_SIGNAL_FIRST_V1")
        screened=out["goal_screen_manifest"]["original_rows"]
        strongest=sorted(screened,key=lambda row:(-(row["priority_score"] or 0),row["queue_rank"]))[0]
        self.assertEqual(out["research_order"][0],strongest["match_id"])
        self.assertEqual(screened[0]["screen_status"],"QUANTIFIED")
        self.assertIsNotNone(screened[0]["dutch_route_screen"])

    def test_single_invalid_source_fixture_does_not_block_other_leagues(self):
        cases = [
            ("match_id","DISCOVERY-notreal","canonical unique"),
            ("observed_at_utc","2026-10-09T12:00:00Z","stale"),
            ("odds",1.9,"bookmaker/live/FT"),
            ("source_url","http://unverified.example.org/1","HTTPS"),
        ]
        for field, value, expected in cases:
            with self.subTest(field=field):
                p=snapshot()
                p["fixtures"][0][field]=value
                result=sweep(p,now=NOW)
                self.assertEqual(result["eligible_count"],1)
                self.assertEqual(result["pending_source_count"],1)
                self.assertIn(expected,result["source_ledger"][0]["reason"])
        p=snapshot()
        p["fixtures"][1]["match_id"]="m1"
        with self.assertRaisesRegex(StageError,"conflicting duplicate"):
            sweep(p,now=NOW)



def fresh_status(sweep_receipt, *, now="2026-10-11T16:05:00Z"):
    return {
        "schema_version": "football-v4-rank-status-refresh-v1",
        "run_id": sweep_receipt["run_id"],
        "sweep_integrity_sha256": sweep_receipt["integrity_sha256"],
        "checked_at_utc": now,
        "matches": [
            {
                "match_id": row["match_id"],
                "kickoff_utc": row["kickoff_utc"],
                "fixture_status": "PREMATCH_CONFIRMED",
                "source_url": row["source_url"],
                "observed_at_utc": now,
            } for row in sweep_receipt["eligible_queue"]
        ],
    }


def _hash_for_test(value):
    import hashlib
    return hashlib.sha256(json.dumps(value,sort_keys=True,ensure_ascii=True,
        separators=(",",":")).encode("utf-8")).hexdigest()


def rank(src, c, c2, reasons, *, now, original_source=None, status_refresh=None):
    """Existing regression scenarios use authentic matching source and status."""
    return production_rank(
        src, c, c2, reasons, now=now,
        original_source=original_source if original_source is not None else snapshot(),
        status_refresh=status_refresh if status_refresh is not None else fresh_status(src, now=now),
    )




class RankV4Tests(unittest.TestCase):
    def test_missing_source_and_status_are_fail_closed(self):
        src = sweep(snapshot(), now=NOW)
        c, c2 = model_inputs()
        reasons = {"m2": "RESEARCH_EVIDENCE_MISSING"}
        with self.assertRaisesRegex(StageError, "V4_SOURCE_REPLAY_REQUIRED"):
            production_rank(src, c, c2, reasons, now="2026-10-11T16:05:00Z")
        with self.assertRaisesRegex(StageError, "V4_STATUS_REFRESH_REQUIRED"):
            production_rank(src, c, c2, reasons, now="2026-10-11T16:05:00Z",
                            original_source=snapshot())

    def test_forged_receipt_does_not_pass_native_source_replay(self):
        from stage import _hash
        src = sweep(snapshot(), now=NOW)
        src["source_url"] = "https://other.example.org/forged"
        src["integrity_sha256"] = _hash({k: v for k, v in src.items() if k != "integrity_sha256"})
        c, c2 = model_inputs()
        statuses = fresh_status(src)
        with self.assertRaisesRegex(StageError, "V4_SOURCE_REPLAY_MISMATCH"):
            production_rank(src, c, c2, {"m2": "RESEARCH_EVIDENCE_MISSING"},
                            now="2026-10-11T16:05:00Z", original_source=snapshot(),
                            status_refresh=statuses)

    def test_started_status_and_stale_or_changed_ko_are_rejected(self):
        src = sweep(snapshot(), now=NOW)
        c, c2 = model_inputs()
        reasons = {"m2": "RESEARCH_EVIDENCE_MISSING"}
        changed = fresh_status(src)
        changed["matches"][0]["fixture_status"] = "STARTED"
        with self.assertRaisesRegex(StageError, "PREMATCH_WINDOW_CLOSED"):
            production_rank(src, c, c2, reasons, now="2026-10-11T16:05:00Z",
                            original_source=snapshot(), status_refresh=changed)
        changed = fresh_status(src)
        changed["matches"][0]["kickoff_utc"] = "2026-10-11T17:30:00Z"
        with self.assertRaisesRegex(StageError, "V4_KICKOFF_CHANGED"):
            production_rank(src, c, c2, reasons, now="2026-10-11T16:05:00Z",
                            original_source=snapshot(), status_refresh=changed)
        changed = fresh_status(src)
        changed["checked_at_utc"] = "2026-10-11T15:00:00Z"
        with self.assertRaisesRegex(StageError, "V4_STATUS_REFRESH_STALE"):
            production_rank(src, c, c2, reasons, now="2026-10-11T16:05:00Z",
                            original_source=snapshot(), status_refresh=changed)

    def test_full_status_cohort_mandatory(self):
        src = sweep(snapshot(), now=NOW)
        c, c2 = model_inputs()
        refresh = fresh_status(src)
        refresh["matches"].pop()
        with self.assertRaisesRegex(StageError, "V4_STATUS_REFRESH_INCOMPLETE"):
            production_rank(src, c, c2, {"m2": "RESEARCH_EVIDENCE_MISSING"},
                            now="2026-10-11T16:05:00Z", original_source=snapshot(),
                            status_refresh=refresh)

    def test_real_C_and_C2_independent_engine_execution(self):
        snapshot_data=sweep(snapshot(),now=NOW)
        c,c2=model_inputs()
        reason={"m2":"RESEARCH_EVIDENCE_MISSING"}
        result=rank(snapshot_data,c,c2,reason,now="2026-10-11T16:05:00Z")
        self.assertEqual(result["status"],"V4_RANK_EXECUTED_AWAITING_AIRTABLE_READBACK")
        self.assertEqual(result["ranked_count"],1)
        self.assertEqual(result["board_pair"]["models_executed"],["c","c2"])
        self.assertFalse(result["publication_authorized"])
        self.assertFalse(result["bet_recorded"])

    def test_rank_binds_cohort_clock_and_unranked_reasons(self):
        src=sweep(snapshot(),now=NOW);c,c2=model_inputs()
        with self.assertRaisesRegex(StageError,"every unranked"):
            rank(src,c,c2,{},now="2026-10-11T16:05:00Z")
        c2["matches"][0]["match_id"]="changed"
        with self.assertRaisesRegex(StageError,"cohort"):
            rank(src,c,c2,{"m2":"RESEARCH_EVIDENCE_MISSING"},
                 now="2026-10-11T16:05:00Z")
        c2["matches"][0]["match_id"]="m1"
        with self.assertRaisesRegex(StageError,"retroactive"):
            rank(src,c,c2,{"m2":"RESEARCH_EVIDENCE_MISSING"},
                 now="2026-10-11T17:01:00Z")
        src["eligible_queue"][0]["home"]="forged"
        with self.assertRaisesRegex(StageError,"integrity"):
            rank(src,c,c2,{"m2":"RESEARCH_EVIDENCE_MISSING"},
                 now="2026-10-11T16:05:00Z")

    def test_rank_rejects_non_goal_qualified_registered_selection(self):
        from stage import _hash
        src=sweep(snapshot(),now=NOW)
        c,c2=model_inputs()
        src["eligible_queue"][0]["goal_screen"]["status"]="WATCH_GOAL_SIGNAL"
        # Even if a caller recomputes the outer JSON hash, rank checks the
        # underlying goal-quality admission contract independently.
        src["integrity_sha256"]=_hash({
            k:v for k,v in src.items() if k!="integrity_sha256"
        })
        with self.assertRaisesRegex(StageError,"goal-first shortlist violated"):
            rank(src,c,c2,{"m2":"RESEARCH_EVIDENCE_MISSING"},
                 now="2026-10-11T16:05:00Z")

    def test_C2_common_evidence_drift_not_allowed(self):
        src=sweep(snapshot(),now=NOW);c,c2=model_inputs()
        c2["matches"][0]["chance_quality"]="LOW"
        with self.assertRaisesRegex(ValueError,"COMMON EVIDENCE DRIFT"):
            rank(src,c,c2,{"m2":"RESEARCH_EVIDENCE_MISSING"},
                 now="2026-10-11T16:05:00Z")

    def test_independent_active_airtable_readback_required(self):
        src=sweep(snapshot(),now=NOW);c,c2=model_inputs()
        c2["matches"][0]["c2_opponent_leakage"] = "HIGH"
        c2["matches"][0]["c2_opponent_leakage_basis"] = (
            "Independent current opponent-specific leakage evidence"
        )
        result=rank(src,c,c2,{"m2":"RESEARCH_EVIDENCE_MISSING"},
                    now="2026-10-11T16:05:00Z")
        cr=result["board_pair"]["results"]["c"]["matches"][0]
        c2r=result["board_pair"]["results"]["c2"]["matches"][0]
        readback={
            "active_base_id":"appbzxqXYf0lKfD4P",
            "method":"INDEPENDENT_AIRTABLE_REFETCH",
            "run_id":result["run_id"],
            "rank_integrity_sha256":result["integrity_sha256"],
            "sweep_integrity_sha256":result["sweep_integrity_sha256"],
            "readback_at_utc":"2026-10-11T16:06:00Z",
            "ranked_rows":[{
                "match_id":"m1",
                "coverage_id":result["run_id"] + "|m1",
                "follow_lane":cr["follow_lane"],
                "c_rank":cr["rank"],"c_board_state":"C-"+cr["board_state"],
                "c_supported_line":cr["supported_line"],
                "c2_rank":c2r["rank"],"c2_board_state":"C2-"+c2r["board_state"],
                "c2_supported_line":c2r["supported_line"],
                "step1_engine_c_result":json.dumps(cr,sort_keys=True),
                "step1_engine_c_result_field_id":"fldhUWNoyXzXfQJ3C",
                "step1_engine_c2_result":json.dumps(c2r,sort_keys=True),
                "step1_engine_c2_result_field_id":"fldq0n2tDlS58goAm",
            }],
        }
        verified=verify_rank(readback,result)
        self.assertEqual(verified["status"],"V4_RANK_PERSISTENCE_VERIFIED")
        self.assertTrue(verified["model_evidence_readback_verified"])
        self.assertEqual(verified["model_evidence_sha256"],
                         _hash_for_test(result["board_pair"]["results"]))
        self.assertTrue(verified["source_replayed"])
        self.assertTrue(verified["current_fixture_status_checked"])
        self.assertEqual(verified["original_source_sha256"],result["original_source_sha256"])
        self.assertEqual(verified["status_refresh_sha256"],result["status_refresh_sha256"])
        readback["ranked_rows"][0]["c_rank"] = 20
        with self.assertRaisesRegex(StageError,"rank"):
            verify_rank(readback,result)
        readback["ranked_rows"][0]["c_rank"] = cr["rank"]
        readback["ranked_rows"][0]["follow_lane"] = "STOP" if cr["follow_lane"] != "STOP" else "FOLLOW"
        with self.assertRaisesRegex(StageError,"lane differs"):
            verify_rank(readback,result)
        readback["ranked_rows"][0]["follow_lane"] = cr["follow_lane"]
        stored_c2=json.loads(readback["ranked_rows"][0]["step1_engine_c2_result"])
        stored_c2["c2_opponent_leakage"]="MEDIUM"
        readback["ranked_rows"][0]["step1_engine_c2_result"]=json.dumps(stored_c2)
        with self.assertRaisesRegex(StageError,"exact Step1 engine evidence differs"):
            verify_rank(readback,result)
        readback["ranked_rows"][0]["step1_engine_c2_result"]=json.dumps(c2r,sort_keys=True)
        readback["ranked_rows"][0]["step1_engine_c2_result_field_id"]="fldWRONG000000000"
        with self.assertRaisesRegex(StageError,"field ID not verified"):
            verify_rank(readback,result)
        readback["ranked_rows"][0]["step1_engine_c2_result_field_id"]="fldq0n2tDlS58goAm"
        readback["rank_integrity_sha256"] = "forged"
        with self.assertRaisesRegex(StageError,"hashes required"):
            verify_rank(readback,result)


if __name__ == "__main__":
    unittest.main()
