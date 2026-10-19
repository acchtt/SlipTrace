"""V4 replacement contract: researched league scope + single immutable Football C board."""
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
from test_board_pair import c_row, payload
from evidence_fixtures import attach_g4_evidence

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
        elif goals == "BORDERLINE":
            scores = [(6,0), (5,0), (1,1), (1,0)]
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


def model_input(mid="m1"):
    a = c_row()
    for field in ('country', 'competition', 'competition_kind'):
        a.pop(field, None)
    a["match_id"] = mid
    a["kickoff_ict"] = KICKOFF_ICT
    return payload("c", a)


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

    def test_latvia_domestic_leagues_are_excluded_but_continental_remains(self):
        for league in ("Virsliga", "1. Liga", "Latvian First League"):
            with self.subTest(league=league):
                result = classify(fixture("lv", "Latvia", league, "DOMESTIC_LEAGUE"))
                self.assertEqual(result["lane"], "EXCLUDED")
                self.assertEqual(result["reason"], "USER_LATVIA_LEAGUE_EXCLUSION")

        continental = classify(
            fixture("lv-eu", "Latvia", "UEFA Conference League", "CONTINENTAL")
        )
        self.assertEqual(continental["lane"], "CONDITIONAL")

    def test_uefa_youth_league_is_specific_conditional_exception(self):
        for country, name, kind in (
            ("Europe", "UEFA Youth League", "YOUTH_CONTINENTAL"),
            ("Europe", "UEFA U19 Youth League", "YOUTH_CONTINENTAL"),
            ("Spain", "UEFA Youth League", "CONTINENTAL"),
        ):
            with self.subTest(country=country, name=name, kind=kind):
                result = classify(fixture("uyl", country, name, kind))
                self.assertEqual(result["lane"], "CONDITIONAL")
                self.assertEqual(
                    result["reason"],
                    "UEFA_YOUTH_LEAGUE_SOURCE_GOAL_FORMAT_REQUIRED",
                )

        other = classify(fixture(
            "other-youth", "Europe", "Generic Continental Youth Cup",
            "YOUTH_CONTINENTAL"
        ))
        self.assertEqual(other["lane"], "EXCLUDED")
        self.assertEqual(other["reason"], "UNAPPROVED_YOUTH_COMPETITION")

    def test_african_domestic_competitions_are_excluded_but_continental_remains(self):
        for country, league, kind in (
            ("Egypt", "Premier League", "DOMESTIC_LEAGUE"),
            ("Morocco", "Botola Pro", "DOMESTIC_LEAGUE"),
            ("South Africa", "Premiership", "DOMESTIC_LEAGUE"),
            ("Nigeria", "NPFL", "DOMESTIC_LEAGUE"),
            ("Ghana", "Premier League", "DOMESTIC_LEAGUE"),
            ("Tunisia", "Ligue 1", "DOMESTIC_LEAGUE"),
            ("Algeria", "Ligue 1", "DOMESTIC_LEAGUE"),
            ("Ivory Coast", "Ligue 1", "DOMESTIC_LEAGUE"),
            ("DR Congo", "Linafoot", "DOMESTIC_LEAGUE"),
            ("Kenya", "FKF Premier League", "DOMESTIC_LEAGUE"),
            ("Egypt", "Egypt Cup", "DOMESTIC_CUP"),
            ("South Africa", "Women's Super League", "WOMENS_TOP_FLIGHT"),
        ):
            with self.subTest(country=country, league=league, kind=kind):
                result = classify(fixture("af", country, league, kind))
                self.assertEqual(result["lane"], "EXCLUDED")
                self.assertEqual(result["reason"], "USER_AFRICA_DOMESTIC_EXCLUSION")

        self.assertEqual(
            classify(fixture("caf", "Egypt", "CAF Champions League", "CONTINENTAL"))["lane"],
            "CONDITIONAL",
        )
        self.assertEqual(
            classify(fixture("afcon", "Africa", "Africa Cup of Nations", "PROTECTED_OFFICIAL"))["lane"],
            "CONDITIONAL",
        )

    def test_non_japan_women_topflight_excluded_but_japan_women_cups_retained(self):
        england = classify(fixture(
            "w1","England","Women's Super League","WOMENS_TOP_FLIGHT"
        ))
        self.assertEqual(england["lane"],"EXCLUDED")
        self.assertEqual(england["reason"],"USER_WOMENS_DOMESTIC_EXCLUSION")
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

    def test_verified_uefa_youth_league_can_enter_goal_first_shortlist(self):
        youth = fixture(
            "uyl-1", "Europe", "UEFA Youth League",
            "YOUTH_CONTINENTAL", proof="VERIFIED"
        )
        out = sweep(snapshot([youth]), now=NOW)
        self.assertEqual(out["fixture_count"], 1)
        self.assertEqual(out["eligible_count"], 1)
        self.assertEqual(out["eligible_queue"][0]["match_id"], "uyl-1")
        row = out["source_ledger"][0]
        self.assertEqual(row["registry_lane"], "CONDITIONAL")
        self.assertEqual(row["intake_lane"], "GOAL_PRIORITY")
        self.assertIn("uyl-1", out["research_order"])

    def test_african_domestic_fixture_stays_visible_but_never_reaches_goal_research(self):
        src = snapshot([
            fixture("egy", "Egypt", "Premier League"),
            fixture("eng", "England", "Premier League"),
        ])
        out = sweep(src, now=NOW)
        self.assertEqual(out["fixture_count"], 2)
        self.assertEqual(out["eligible_count"], 1)
        self.assertEqual(out["eligible_queue"][0]["match_id"], "eng")
        egypt = next(x for x in out["source_ledger"] if x["match_id"] == "egy")
        self.assertEqual(egypt["registry_lane"], "EXCLUDED")
        self.assertEqual(egypt["intake_lane"], "EXCLUDED")
        self.assertEqual(egypt["reason"], "USER_AFRICA_DOMESTIC_EXCLUSION")
        self.assertNotIn("egy", out["research_order"])
        self.assertNotIn("egy", out["goal_research_order"])

    def test_latvia_domestic_fixture_stays_visible_but_never_reaches_goal_research(self):
        src = snapshot([
            fixture("lat", "Latvia", "Virsliga"),
            fixture("eng", "England", "Premier League"),
        ])
        out = sweep(src, now=NOW)
        self.assertEqual(out["fixture_count"], 2)
        self.assertEqual(out["eligible_count"], 1)
        self.assertEqual(out["eligible_queue"][0]["match_id"], "eng")
        latvia = next(x for x in out["source_ledger"] if x["match_id"] == "lat")
        self.assertEqual(latvia["registry_lane"], "EXCLUDED")
        self.assertEqual(latvia["intake_lane"], "EXCLUDED")
        self.assertEqual(latvia["reason"], "USER_LATVIA_LEAGUE_EXCLUSION")
        self.assertNotIn("lat", out["research_order"])
        self.assertNotIn("lat", out["goal_research_order"])

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
                         "GOAL_SIGNAL_FIRST_V3")
        self.assertEqual(
            out["goal_screen_manifest"]["ordered_eligible_match_ids"],
            out["research_order"],
        )
        self.assertTrue(out["goal_screen_manifest"]["screen_fingerprint"])

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

    def test_borderline_goal_signal_reaches_rank_as_review_lane(self):
        src=snapshot([
            fixture("review","England","Premier League",goals="BORDERLINE"),
            fixture("strong","Netherlands","Eerste Divisie",goals="HIGH"),
        ])
        out=sweep(src,now=NOW)
        self.assertEqual(out["eligible_count"],2)
        lanes={x["match_id"]:x["intake_lane"] for x in out["eligible_queue"]}
        self.assertEqual(lanes["strong"],"GOAL_PRIORITY")
        self.assertEqual(lanes["review"],"GOAL_REVIEW")
        self.assertEqual(out["goal_review_count"],1)
        self.assertEqual(out["research_order"][0],"strong")
        self.assertEqual(out["goal_screen_manifest"]["priority_profile"],
                         "GOAL_SIGNAL_FIRST_V3")

    def test_verified_discovery_borderline_reaches_review_queue(self):
        review = fixture(
            "review-unregistered", "Pakistan", "Premier League",
            proof="VERIFIED", goals="BORDERLINE"
        )
        self.assertEqual(classify(review)["lane"], "DISCOVERY")
        out = sweep(snapshot([
            fixture("strong", "England", "Premier League", goals="HIGH"),
            review,
        ]), now=NOW)
        row = next(x for x in out["source_ledger"]
                   if x["match_id"] == "review-unregistered")
        self.assertEqual(row["discovery_screen"]["status"], "DISCOVERY_GOAL_REVIEW")
        self.assertEqual(row["intake_lane"], "GOAL_REVIEW")
        self.assertIn("review-unregistered", out["research_order"])
        self.assertEqual(out["research_order"][0], "strong")
        self.assertEqual(out["goal_review_count"], 1)
        self.assertIn("review-unregistered", [x["match_id"] for x in out["discovery_watchlist"]])
        eligible = next(
            x for x in out["eligible_queue"]
            if x["match_id"] == "review-unregistered"
        )
        self.assertEqual(eligible["operational_grade"], "A")
        self.assertEqual(
            eligible["operational_grade_basis"],
            "CURRENT_FIXTURE_BOUND_RESEARCHABILITY_VERIFIED",
        )

    def test_discovery_review_without_channel_proof_stays_pending(self):
        review = fixture(
            "review-no-proof", "Pakistan", "Premier League",
            goals="BORDERLINE"
        )
        out = sweep(snapshot([review]), now=NOW)
        self.assertEqual(out["eligible_count"], 0)
        self.assertEqual(out["source_ledger"][0]["intake_lane"], "PENDING_DISCOVERY")
        self.assertNotIn("review-no-proof", out["research_order"])

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
        self.assertEqual(result["eligible_count"],2)
        self.assertEqual(result["pending_researchability_count"],1)
        self.assertEqual(result["fixture_count"],4)
        self.assertEqual({x["match_id"] for x in result["eligible_queue"]},{"m1","m3"})
        by_id = {x["match_id"]: x for x in result["eligible_queue"]}
        self.assertEqual(by_id["m1"]["operational_grade"], "A")
        self.assertEqual(by_id["m3"]["operational_grade"], "A")
        m4 = next(x for x in result["source_ledger"] if x["match_id"] == "m4")
        self.assertEqual(m4["registry_lane"], "EXCLUDED")
        self.assertEqual(m4["reason"], "USER_WOMENS_DOMESTIC_EXCLUSION")
        self.assertEqual(
            by_id["m3"]["operational_grade_basis"],
            "CURRENT_FIXTURE_BOUND_RESEARCHABILITY_VERIFIED",
        )

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
        self.assertEqual(out["goal_screen_manifest"]["priority_profile"],"GOAL_SIGNAL_FIRST_V3")
        screened=out["goal_screen_manifest"]["original_rows"]
        strongest=sorted(screened,key=lambda row:(-(row["priority_score"] or 0),row["queue_rank"]))[0]
        self.assertEqual(out["research_order"][0],strongest["match_id"])
        self.assertEqual(screened[0]["screen_status"],"QUANTIFIED")
        self.assertTrue(screened[0]["source_screen_fingerprint"])
        self.assertNotIn("dutch_route_screen",screened[0])

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


def rank(src, c, reasons, *, now, original_source=None, status_refresh=None):
    """Regression scenarios use authentic matching source and status."""
    return production_rank(
        src, c, reasons, now=now,
        original_source=original_source if original_source is not None else snapshot(),
        status_refresh=status_refresh if status_refresh is not None else fresh_status(src, now=now),
    )



class RankV4Tests(unittest.TestCase):
    def test_missing_source_and_status_are_fail_closed(self):
        src = sweep(snapshot(), now=NOW)
        c = model_input()
        reasons = {"m2": "RESEARCH_EVIDENCE_MISSING"}
        with self.assertRaisesRegex(StageError, "V4_SOURCE_REPLAY_REQUIRED"):
            production_rank(src, c, reasons, now="2026-10-11T16:05:00Z")
        with self.assertRaisesRegex(StageError, "V4_STATUS_REFRESH_REQUIRED"):
            production_rank(
                src, c, reasons,
                now="2026-10-11T16:05:00Z",
                original_source=snapshot(),
            )

    def test_forged_receipt_does_not_pass_native_source_replay(self):
        from stage import _hash
        src = sweep(snapshot(), now=NOW)
        src["source_url"] = "https://other.example.org/forged"
        src["integrity_sha256"] = _hash(
            {k: v for k, v in src.items() if k != "integrity_sha256"}
        )
        c = model_input()
        statuses = fresh_status(src)
        with self.assertRaisesRegex(StageError, "V4_SOURCE_REPLAY_MISMATCH"):
            production_rank(
                src, c, {"m2": "RESEARCH_EVIDENCE_MISSING"},
                now="2026-10-11T16:05:00Z",
                original_source=snapshot(),
                status_refresh=statuses,
            )

    def test_started_status_and_stale_or_changed_ko_are_rejected(self):
        src = sweep(snapshot(), now=NOW)
        c = model_input()
        reasons = {"m2": "RESEARCH_EVIDENCE_MISSING"}

        changed = fresh_status(src)
        changed["matches"][0]["fixture_status"] = "STARTED"
        with self.assertRaisesRegex(StageError, "PREMATCH_WINDOW_CLOSED"):
            production_rank(
                src, c, reasons,
                now="2026-10-11T16:05:00Z",
                original_source=snapshot(),
                status_refresh=changed,
            )

        changed = fresh_status(src)
        changed["matches"][0]["kickoff_utc"] = "2026-10-11T17:30:00Z"
        with self.assertRaisesRegex(StageError, "V4_KICKOFF_CHANGED"):
            production_rank(
                src, c, reasons,
                now="2026-10-11T16:05:00Z",
                original_source=snapshot(),
                status_refresh=changed,
            )

        changed = fresh_status(src)
        changed["checked_at_utc"] = "2026-10-11T15:00:00Z"
        with self.assertRaisesRegex(StageError, "V4_STATUS_REFRESH_STALE"):
            production_rank(
                src, c, reasons,
                now="2026-10-11T16:05:00Z",
                original_source=snapshot(),
                status_refresh=changed,
            )

    def test_full_status_cohort_mandatory(self):
        src = sweep(snapshot(), now=NOW)
        c = model_input()
        refresh = fresh_status(src)
        refresh["matches"].pop()
        with self.assertRaisesRegex(StageError, "V4_STATUS_REFRESH_INCOMPLETE"):
            production_rank(
                src, c, {"m2": "RESEARCH_EVIDENCE_MISSING"},
                now="2026-10-11T16:05:00Z",
                original_source=snapshot(),
                status_refresh=refresh,
            )

    def test_incomplete_g4_focus_is_checkpointed_not_boarded(self):
        src = sweep(snapshot(), now=NOW)
        c = model_input()
        c["matches"][0]["independent_upper_tail"] = False
        c["matches"][0]["independent_upper_tail_basis"] = (
            "G3 is funded, but the bounded G4 investigation is not yet complete."
        )

        result = rank(
            src, c, {"m2": "RESEARCH_EVIDENCE_MISSING"},
            now="2026-10-11T16:05:00Z",
        )

        self.assertEqual(result["status"], "V4_RANK_RESEARCH_PENDING")
        self.assertEqual(result["assessed_count"], 0)
        self.assertEqual(result["ranked_count"], 0)
        self.assertIsNone(result["board"])
        self.assertEqual(result["g4_incomplete_match_ids"], ["m1"])
        self.assertEqual(
            next(x for x in result["coverage_manifest"] if x["match_id"] == "m1")[
                "disposition"
            ],
            "G4_RESEARCH_PENDING",
        )
        pending = next(x for x in result["resume_queue"] if x["match_id"] == "m1")
        self.assertEqual(pending["research_status"], "G4_RESEARCH_PENDING")
        self.assertIn("bounded G4 pass", pending["next_action"])
        self.assertNotIn(
            "m1",
            [row["match_id"] for row in result["frozen_model_input"]["matches"]],
        )

    def test_complete_g4_rejection_can_finalize_o25_focus(self):
        src = sweep(snapshot(), now=NOW)
        c = model_input()
        row = c["matches"][0]
        row.update(
            independent_upper_tail=False,
            independent_upper_tail_basis=(
                "Completed upper-tail research rejects an independently "
                "transferable fourth-goal mechanism."
            ),
            g4_research_status="G4_RESEARCH_COMPLETE_REJECTED",
            g4_carrier_path="FAILED",
            g4_distributed_path="FAILED",
            g4_reply_path="FAILED",
            g4_continuation_after_g3="MEDIUM",
            g4_research_basis=(
                "Carrier, distributed, reply and continuation paths were "
                "prospectively checked; none clears the existing G4 rules."
            ),
        )

        attach_g4_evidence(row)
        result = rank(
            src, c, {"m2": "RESEARCH_EVIDENCE_MISSING"},
            now="2026-10-11T16:05:00Z",
        )

        self.assertEqual(
            result["status"], "V4_RANK_EXECUTED_AWAITING_SHEETS_READBACK"
        )
        self.assertEqual(result["ranked_count"], 1)
        board_row = result["board"]["matches"][0]
        self.assertEqual(board_row["match_id"], "m1")
        self.assertEqual(
            board_row["g4_research_status"], "G4_RESEARCH_COMPLETE_REJECTED"
        )
        self.assertEqual(board_row["supported_line"], 2.5)
        self.assertEqual(result["g4_incomplete_match_ids"], [])

    def test_incomplete_g4_focus_does_not_block_completed_focus_rows(self):
        src = sweep(snapshot(), now=NOW)
        incomplete = c_row()
        incomplete["match_id"] = "m1"
        incomplete["kickoff_ict"] = KICKOFF_ICT
        incomplete["independent_upper_tail"] = False
        incomplete["independent_upper_tail_basis"] = (
            "G3 is funded but G4 research remains unfinished."
        )
        complete = c_row()
        complete["match_id"] = "m2"
        complete.update(country="Netherlands", competition="Eerste Divisie")
        complete["kickoff_ict"] = KICKOFF_ICT
        c = payload("c", incomplete)
        c["matches"].append(complete)

        result = rank(src, c, {}, now="2026-10-11T16:05:00Z")

        self.assertEqual(
            result["status"], "V4_RANK_EXECUTED_AWAITING_SHEETS_READBACK"
        )
        self.assertEqual(result["assessed_count"], 1)
        self.assertEqual(result["ranked_count"], 1)
        self.assertEqual(
            [row["match_id"] for row in result["board"]["matches"]], ["m2"]
        )
        self.assertEqual(result["g4_incomplete_match_ids"], ["m1"])
        self.assertEqual(
            next(x for x in result["coverage_manifest"] if x["match_id"] == "m1")[
                "disposition"
            ],
            "G4_RESEARCH_PENDING",
        )

    def test_real_single_c_engine_execution(self):
        snapshot_data = sweep(snapshot(), now=NOW)
        c = model_input()
        reason = {"m2": "RESEARCH_EVIDENCE_MISSING"}
        result = rank(
            snapshot_data, c, reason,
            now="2026-10-11T16:05:00Z",
        )
        self.assertEqual(
            result["status"],
            "V4_RANK_EXECUTED_AWAITING_SHEETS_READBACK",
        )
        self.assertEqual(result["ranked_count"], 1)
        self.assertEqual(result["active_model"], "c")
        self.assertEqual(result["retired_models"], ["c2", "c3", "c4"])
        self.assertEqual(result["board"]["model"], "c")
        self.assertEqual(result["board"]["stage"], "board_result")
        self.assertFalse(result["publication_authorized"])
        self.assertFalse(result["bet_recorded"])

    def test_rank_researches_watch_but_only_focus_enters_official_board(self):
        src = sweep(snapshot(), now=NOW)
        focus = c_row()
        focus["match_id"] = "m1"
        focus["kickoff_ict"] = KICKOFF_ICT
        watch = c_row()
        watch["match_id"] = "m2"
        watch.update(country="Netherlands", competition="Eerste Divisie")
        watch["kickoff_ict"] = KICKOFF_ICT
        watch["board_state"] = "C-WATCH"
        watch["board_state_basis"] = "credible research case, but below C focus admission"
        c = payload("c", focus)
        c["matches"].append(watch)

        result = rank(src, c, {}, now="2026-10-11T16:05:00Z")

        self.assertEqual(result["assessed_count"], 2)
        self.assertEqual(result["ranked_count"], 1)
        self.assertEqual(result["watch_count"], 1)
        self.assertEqual(result["pass_count"], 0)
        self.assertEqual(result["board_admission_policy"], "C_FOCUS_ONLY_NO_FIXED_COUNT_CAP")
        self.assertEqual([x["match_id"] for x in result["board"]["matches"]], ["m1"])
        self.assertEqual(result["research_assessment"]["match_count"], 2)
        self.assertEqual(result["board_excluded_count"], 1)
        self.assertEqual(result["board_exclusions"][0]["match_id"], "m2")
        self.assertEqual(result["board_exclusions"][0]["board_state"], "WATCH")

    def test_focus_board_has_no_arbitrary_numeric_cap(self):
        source_rows = [fixture(f"focus-{i}") for i in range(11)]
        src_data = snapshot(source_rows)
        src = sweep(src_data, now=NOW)
        crows = []
        for i in range(11):
            row = c_row()
            row["match_id"] = f"focus-{i}"
            row["kickoff_ict"] = KICKOFF_ICT
            crows.append(row)
        c = {
            "schema_version": "football-engine-v1",
            "stage": "board",
            "model": "c",
            "matches": crows,
        }

        result = production_rank(
            src, c, {}, now="2026-10-11T16:05:00Z",
            original_source=src_data,
            status_refresh=fresh_status(src),
        )

        self.assertEqual(result["assessed_count"], 11)
        self.assertEqual(result["ranked_count"], 11)
        self.assertEqual(result["board"]["match_count"], 11)
        self.assertEqual(len(result["board"]["matches"]), 11)
        self.assertGreater(
            sum(x["follow_lane"] == "STOP" for x in result["board"]["matches"]),
            0,
        )

    def test_rank_binds_cohort_clock_and_unranked_reasons(self):
        src = sweep(snapshot(), now=NOW)
        c = model_input()
        with self.assertRaisesRegex(StageError, "every unranked"):
            rank(src, c, {}, now="2026-10-11T16:05:00Z")

        c["matches"][0]["match_id"] = "changed"
        with self.assertRaisesRegex(StageError, "cohort"):
            rank(
                src, c, {"m2": "RESEARCH_EVIDENCE_MISSING"},
                now="2026-10-11T16:05:00Z",
            )
        c["matches"][0]["match_id"] = "m1"

        with self.assertRaisesRegex(StageError, "retroactive"):
            rank(
                src, c, {"m2": "RESEARCH_EVIDENCE_MISSING"},
                now="2026-10-11T17:01:00Z",
            )

        src["eligible_queue"][0]["home"] = "forged"
        with self.assertRaisesRegex(StageError, "integrity"):
            rank(
                src, c, {"m2": "RESEARCH_EVIDENCE_MISSING"},
                now="2026-10-11T16:05:00Z",
            )

    def test_rank_rejects_non_goal_qualified_registered_selection(self):
        from stage import _hash
        src = sweep(snapshot(), now=NOW)
        c = model_input()
        src["eligible_queue"][0]["goal_screen"]["status"] = "WATCH_GOAL_SIGNAL"
        src["integrity_sha256"] = _hash({
            k: v for k, v in src.items() if k != "integrity_sha256"
        })
        with self.assertRaisesRegex(StageError, "goal-first shortlist violated"):
            rank(
                src, c, {"m2": "RESEARCH_EVIDENCE_MISSING"},
                now="2026-10-11T16:05:00Z",
            )

    def test_retired_c2_payload_is_not_part_of_rank_signature(self):
        import inspect
        parameters = inspect.signature(production_rank).parameters
        self.assertIn("c", parameters)
        self.assertNotIn("c2", parameters)

    def test_independent_active_google_sheets_readback_required(self):
        src = sweep(snapshot(), now=NOW)
        c = model_input()
        result = rank(
            src, c, {"m2": "RESEARCH_EVIDENCE_MISSING"},
            now="2026-10-11T16:05:00Z",
        )
        cr = result["board"]["matches"][0]
        readback = {
            "spreadsheet_id": "1ojWKj5aT3VEJUyX3NSbAOZNTaUM0Mb8I8e4lvFy7kGM",
            "sheet_name": "Daily Coverage Ledger",
            "method": "INDEPENDENT_GOOGLE_SHEETS_REFETCH",
            "run_id": result["run_id"],
            "rank_integrity_sha256": result["integrity_sha256"],
            "sweep_integrity_sha256": result["sweep_integrity_sha256"],
            "readback_at_utc": "2026-10-11T16:06:00Z",
            "ranked_rows": [{
                "match_id": "m1",
                "coverage_id": result["run_id"] + "|m1",
                "follow_lane": cr["follow_lane"],
                "c_rank": cr["rank"],
                "c_board_state": "C-" + cr["board_state"],
                "c_supported_line": cr["supported_line"],
                "step1_engine_c_result": json.dumps(cr, sort_keys=True),
                "step1_engine_c_result_column": "Step1 Engine C Result",
            }],
        }

        verified = verify_rank(readback, result)
        self.assertEqual(
            verified["status"],
            "V4_RANK_PARTIAL_PERSISTENCE_VERIFIED",
        )
        self.assertEqual(verified["active_model"], "c")
        self.assertEqual(
            verified["retired_models"],
            ["c2", "c3", "c4"],
        )
        self.assertTrue(verified["model_evidence_readback_verified"])
        self.assertEqual(
            verified["model_evidence_sha256"],
            _hash_for_test(result["board"]),
        )
        self.assertTrue(verified["source_replayed"])
        self.assertTrue(verified["current_fixture_status_checked"])

        readback["ranked_rows"][0]["c_rank"] = 20
        with self.assertRaisesRegex(StageError, "rank"):
            verify_rank(readback, result)
        readback["ranked_rows"][0]["c_rank"] = cr["rank"]

        readback["ranked_rows"][0]["follow_lane"] = (
            "STOP" if cr["follow_lane"] != "STOP" else "FOLLOW"
        )
        with self.assertRaisesRegex(StageError, "lane differs"):
            verify_rank(readback, result)
        readback["ranked_rows"][0]["follow_lane"] = cr["follow_lane"]

        stored_c = json.loads(
            readback["ranked_rows"][0]["step1_engine_c_result"]
        )
        stored_c["chance_quality"] = "LOW"
        readback["ranked_rows"][0]["step1_engine_c_result"] = json.dumps(stored_c)
        with self.assertRaisesRegex(StageError, "exact Step1 engine evidence differs"):
            verify_rank(readback, result)

        readback["ranked_rows"][0]["step1_engine_c_result"] = json.dumps(
            cr, sort_keys=True
        )
        readback["ranked_rows"][0]["step1_engine_c_result_column"] = "Wrong Column"
        with self.assertRaisesRegex(StageError, "Google Sheets column not verified"):
            verify_rank(readback, result)

        readback["ranked_rows"][0]["step1_engine_c_result_column"] = (
            "fldhUWNoyXzXfQJ3C"
        )
        readback["rank_integrity_sha256"] = "forged"
        with self.assertRaisesRegex(StageError, "hashes required"):
            verify_rank(readback, result)


if __name__ == "__main__":
    unittest.main()
