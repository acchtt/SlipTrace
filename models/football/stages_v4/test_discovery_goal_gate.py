"""Unknown leagues must be considered on football evidence, not registry familiarity."""
from __future__ import annotations
import copy
import json
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
from stage import sweep,rank,StageError
from league_registry import classify
from discovery_goal_gate import _qualifies_goal_research

NOW="2026-10-11T16:00:00Z"
def row(mid,country="Brazil",competition="Serie A",kind="DOMESTIC_LEAGUE",
        *, research=True,goals="HIGH"):
    raw={
        "match_id":mid,"country":country,"competition":competition,
        "competition_kind":kind,"home":"Home FC","away":"Away FC",
        "kickoff_utc":"2026-10-11T18:00:00Z",
        "fixture_status":"PREMATCH_CONFIRMED",
        "source_url":"https://fixture.example.org/match/"+mid,
        "observed_at_utc":"2026-10-11T15:59:00Z",
    }
    if research:
        raw["researchability_status"]="VERIFIED"
        raw["researchability_proof"]={
            "match_id":mid,
            "source_url":"https://league.example.org/research/current/"+mid,
            "checked_at_utc":"2026-10-11T15:59:00Z",
            "current_channels_checked":True,
        }
    if goals:
        if goals=="HIGH":
            results=[(3,2),(4,1),(2,2),(3,1)]
        elif goals=="TRAP":
            results=[(0,0),(1,1),(1,1),(0,0)]
        else:
            raise ValueError(goals)
        games=[{
            "kickoff_utc":f"2026-09-{day:02d}T12:00:00Z",
            "goals_for":gf,"goals_against":ga,
        } for day,(gf,ga) in zip((1,8,15,22),results)]
        raw["football_evidence"]={
            side:{
                "source_url":f"https://results.example.org/{mid}/{side}",
                "observed_at_utc":"2026-10-11T15:58:00Z",
                "recent":copy.deepcopy(games),
            } for side in ("home","away")
        }
    return raw

def source(rows):
    return {
        "schema_version":"football-stages-v4",
        "run_id":"V4-20261011-1600-UNREGISTERED",
        "window_start_utc":"2026-10-11T15:50:00Z",
        "window_end_utc":"2026-10-11T22:00:00Z",
        "source_family":"FixtureFeed",
        "source_url":"https://fixture.example.org/calendar/20261011",
        "source_observed_at_utc":"2026-10-11T15:59:00Z",
        "fixtures":rows,
    }

class Step0BoundaryRegressionTests(unittest.TestCase):
    def test_high_rate_signal_can_qualify_below_composite_sixty(self):
        # Frozen San Diego-Houston prematch summary from
        # V4-20261015-0734-20261015-1200: result is intentionally not used.
        self.assertTrue(
            _qualifies_goal_research(57, 0.6875, 0.50, 0.125)
        )

    def test_low_route_and_low_rate_shape_stays_watch(self):
        # Frozen LAFC-Austin prematch summary: a later scoreline must not
        # retroactively turn a weak Step-0 signal into a research certificate.
        self.assertFalse(
            _qualifies_goal_research(41, 0.4375, 0.3125, 0.375)
        )

    def test_borderline_three_plus_without_four_plus_tail_stays_watch(self):
        # Frozen RSL-San Jose prematch summary. Mean 3+ barely clears the
        # legacy floor, but the 4+ tail is not strong enough for alt admission.
        self.assertFalse(
            _qualifies_goal_research(48, 0.5625, 0.3125, 0.1875)
        )

    def test_existing_route_score_path_is_preserved(self):
        self.assertTrue(
            _qualifies_goal_research(60, 0.55, 0.20, 0.35)
        )

    def test_g3_distribution_can_qualify_without_four_plus_tail(self):
        # Frozen Benfica-Celtic shape: enough source-backed 3+ evidence to
        # deserve C research even though the 4+ tail is not an intake gate.
        self.assertTrue(
            _qualifies_goal_research(53, 0.6875, 0.3125, 0.0)
        )

    def test_one_sided_carrier_leakage_can_qualify_for_g3_research(self):
        # Frozen NEC-Levski shape: one route is materially stronger because
        # NEC's recent opponent leakage is high. Step 0 may research it; only
        # Football C can decide whether G3 is actually funded.
        self.assertTrue(
            _qualifies_goal_research(
                53, 0.625, 0.4375, 0.1875, carrier_route=1.813
            )
        )

    def test_moderate_carrier_does_not_open_same_shape(self):
        # Frozen Bournemouth-Sturm shape remains below the one-sided route
        # threshold and should not be promoted by the new carrier path alone.
        self.assertFalse(
            _qualifies_goal_research(
                52, 0.625, 0.375, 0.1875, carrier_route=1.563
            )
        )


class OpenLeagueGoalDiscoveryTests(unittest.TestCase):
    def test_high_scoring_brazilian_serie_a_was_missing_but_now_reaches_rank_queue(self):
        unknown=row("br1")
        self.assertEqual(classify(unknown)["lane"],"DISCOVERY")
        result=sweep(source([unknown]),now=NOW)
        self.assertEqual(result["status"],"V4_SWEEP_READY")
        self.assertEqual(result["eligible_count"],1)
        self.assertEqual(result["discovery_qualified_count"],1)
        self.assertEqual(result["research_order"],["br1"])
        self.assertEqual(result["eligible_queue"][0]["intake_lane"],"GOAL_PRIORITY")
        screen=result["eligible_queue"][0]["discovery_screen"]
        self.assertEqual(screen["status"],"DISCOVERY_GOAL_QUALIFIED")
        self.assertGreaterEqual(screen["priority_score"],60)
        self.assertEqual(screen["home_sample_n"],4)
        self.assertEqual(screen["away_sample_n"],4)
        self.assertFalse(screen["is_model_prediction"])
        self.assertFalse(result["bet_recorded"])

    def test_missing_form_or_current_channel_proof_is_visible_not_hard_excluded(self):
        fixtures=[
            row("br1", research=False,goals="HIGH"),
            row("mx1","Mexico","Liga MX",goals=None),
            row("br2",goals="TRAP"),
            row("regular","Netherlands","Eerste Divisie",research=False,goals=None),
        ]
        res=sweep(source(fixtures),now=NOW)
        self.assertEqual(res["eligible_count"],0)
        self.assertEqual(res["pending_discovery_count"],3)
        self.assertEqual(res["pending_goal_research_count"],1)
        self.assertEqual(res["discovery_qualified_count"],0)
        self.assertEqual(len(res["discovery_watchlist"]),3)
        signals={i["match_id"]:i for i in res["discovery_watchlist"]}
        self.assertEqual(signals["br1"]["discovery_screen"]["status"],"DISCOVERY_GOAL_QUALIFIED")
        self.assertEqual(signals["mx1"]["discovery_screen"]["status"],"PENDING_GOAL_HISTORY")
        self.assertEqual(signals["br2"]["discovery_screen"]["status"],"WATCH_GOAL_SIGNAL")
        self.assertEqual(res["excluded_or_closed_count"],0)
        self.assertIn("br1",{i["match_id"] for i in res["source_ledger"]})

    def test_high_scoring_unregistered_domestic_cup_needs_format_and_incentives(self):
        cup=row("cup1","Mexico","Copa MX","DOMESTIC_CUP")
        self.assertEqual(classify(cup)["lane"],"DISCOVERY")
        out=sweep(source([cup]),now=NOW)
        self.assertEqual(out["pending_discovery_count"],1)
        self.assertEqual(out["discovery_watchlist"][0]["reason"],"OFFICIAL_CUP_FORMAT_AND_INCENTIVES_NOT_VERIFIED")
        cup["tournament_format_proof"]={
            "match_id":"cup1",
            "competition_format_verified":True,
            "source_url":"https://official.example.org/cup/format",
            "checked_at_utc":"2026-10-11T15:58:00Z",
        }
        out=sweep(source([cup]),now=NOW)
        self.assertEqual(out["eligible_count"],1)
        self.assertEqual(out["discovery_qualified_count"],1)

    def test_explicitly_excluded_leagues_and_friendlies_never_reopen_on_goals(self):
        cases=[
            ("de","Germany","3. Liga","DOMESTIC_LEAGUE"),
            ("fr","France","Ligue 2","DOMESTIC_LEAGUE"),
            ("it","Italy","Serie B","DOMESTIC_LEAGUE"),
            ("ban","Bangladesh","Premier League","DOMESTIC_LEAGUE"),
            ("isr","Israel","Premier League","DOMESTIC_LEAGUE"),
            ("friendly","Brazil","Friendlies","DOMESTIC_LEAGUE"),
        ]
        rows=[row(*case,goals="HIGH") for case in cases]
        out=sweep(source(rows),now=NOW)
        self.assertEqual(out["eligible_count"],0)
        self.assertEqual(out["pending_discovery_count"],0)
        self.assertEqual(out["excluded_or_closed_count"],len(rows))
        self.assertFalse(out["discovery_watchlist"])

    def test_existing_routine_priority_is_kept_and_source_identity_is_immutable(self):
        out=sweep(source([
            row("br1"),row("known1","Germany","Bundesliga",goals=None),
        ]),now=NOW)
        self.assertEqual(out["eligible_count"],1)
        self.assertEqual(out["research_order"][0],"br1")
        self.assertEqual({x["queue_rank"] for x in out["eligible_queue"]},{1})
        self.assertEqual(out["goal_research_queue"][0]["match_id"],"known1")
        out["eligible_queue"][0]["home"]="Altered FC"
        from stage import _verified
        with self.assertRaisesRegex(StageError,"integrity SHA256"):
            _verified(out,"V4_SWEEP_READY")


if __name__=="__main__":
    unittest.main()
