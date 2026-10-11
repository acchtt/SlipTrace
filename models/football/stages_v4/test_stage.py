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
from stage import StageError, sweep, rank, verify_rank
from test_board_pair import c_row, c2_row, payload

NOW = "2026-10-11T16:00:00Z"
KICKOFF = "2026-10-11T17:00:00Z"
KICKOFF_ICT = "2026-10-12T00:00:00+07:00"


def fixture(mid, country="England", league="Premier League", kind="DOMESTIC_LEAGUE",
            *, proof=None, ko=KICKOFF):
    result = {
        "match_id": mid, "country": country, "competition": league,
        "competition_kind": kind, "home": "Home FC", "away": "Away FC",
        "kickoff_utc": ko, "fixture_status": "PREMATCH_CONFIRMED",
        "source_url": "https://sports.example.org/fixture/" + mid,
        "observed_at_utc": "2026-10-11T15:59:00Z",
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
            ("Japan","J1 League"),("Japan","J2 League"),
        ):
            with self.subTest(country=country, league=league):
                self.assertEqual(classify(fixture("a",country,league))["lane"], "ROUTINE")
        for country, league in (
            ("England","Championship"), ("Spain","Segunda Division"),
            ("Germany","2. Bundesliga"),
            ("Poland","Ekstraklasa"), ("Czech Republic","Czech FNL"),
            ("Hong Kong","Hong Kong Premier League"),
            ("Malaysia","Liga Super"),("Qatar","Qatar Stars League"),
            ("UAE","UAE Pro League"),("Thailand","Thai League 1"),
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
        self.assertEqual(classify(fixture("a","Pakistan","Premier League"))["lane"], "EXCLUDED")

    def test_verified_women_topflight_and_competitive_cups_without_global_scan(self):
        self.assertEqual(classify(fixture(
            "w1","England","Women's Super League","WOMENS_TOP_FLIGHT"
        ))["lane"],"CONDITIONAL")
        self.assertEqual(classify(fixture(
            "cup1","Japan","WE League Cup","DOMESTIC_CUP"
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

    def test_conditionally_verified_proof_cannot_be_bare_boolean_or_other_fixture(self):
        a = fixture("m1", "Poland", "Ekstraklasa", proof="VERIFIED")
        a.pop("researchability_proof")
        with self.assertRaisesRegex(StageError, "requires source evidence"):
            sweep(snapshot([a]), now=NOW)
        a = fixture("m1", "Poland", "Ekstraklasa", proof="VERIFIED")
        a["researchability_proof"]["match_id"] = "wrong-match"
        with self.assertRaisesRegex(StageError, "not bound to fixture"):
            sweep(snapshot([a]), now=NOW)

    def test_researched_leagues_not_arbitrarily_capped_at_eight(self):
        rows = [fixture(f"match-{i}", country="Netherlands",league="Eerste Divisie")
                for i in range(1,21)]
        result = sweep(snapshot(rows),now=NOW)
        self.assertEqual(result["eligible_count"],20)
        self.assertEqual(len(result["research_order"]),20)

    def test_bad_source_ko_fixtures_and_lookahead_block(self):
        p=snapshot()
        p["fixtures"][0]["match_id"]="DISCOVERY-notreal"
        with self.assertRaisesRegex(StageError,"canonical unique"):
            sweep(p,now=NOW)
        p=snapshot()
        p["fixtures"][0]["observed_at_utc"]="2026-10-09T12:00:00Z"
        with self.assertRaisesRegex(StageError,"stale"):
            sweep(p,now=NOW)
        p=snapshot()
        p["fixtures"][0]["odds"]=1.9
        with self.assertRaisesRegex(StageError,"bookmaker/live/FT"):
            sweep(p,now=NOW)
        p=snapshot()
        p["fixtures"][0]["source_url"]="http://unverified.example.org/1"
        with self.assertRaisesRegex(StageError,"HTTPS"):
            sweep(p,now=NOW)


class RankV4Tests(unittest.TestCase):
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

    def test_C2_common_evidence_drift_not_allowed(self):
        src=sweep(snapshot(),now=NOW);c,c2=model_inputs()
        c2["matches"][0]["chance_quality"]="LOW"
        with self.assertRaisesRegex(ValueError,"COMMON EVIDENCE DRIFT"):
            rank(src,c,c2,{"m2":"RESEARCH_EVIDENCE_MISSING"},
                 now="2026-10-11T16:05:00Z")

    def test_independent_active_airtable_readback_required(self):
        src=sweep(snapshot(),now=NOW);c,c2=model_inputs()
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
            }],
        }
        verified=verify_rank(readback,result)
        self.assertEqual(verified["status"],"V4_RANK_PERSISTENCE_VERIFIED")
        readback["ranked_rows"][0]["c_rank"] = 20
        with self.assertRaisesRegex(StageError,"rank"):
            verify_rank(readback,result)
        readback["ranked_rows"][0]["c_rank"] = cr["rank"]
        readback["ranked_rows"][0]["follow_lane"] = "STOP" if cr["follow_lane"] != "STOP" else "FOLLOW"
        with self.assertRaisesRegex(StageError,"lane differs"):
            verify_rank(readback,result)
        readback["ranked_rows"][0]["follow_lane"] = cr["follow_lane"]
        readback["rank_integrity_sha256"] = "forged"
        with self.assertRaisesRegex(StageError,"hashes required"):
            verify_rank(readback,result)


if __name__ == "__main__":
    unittest.main()
