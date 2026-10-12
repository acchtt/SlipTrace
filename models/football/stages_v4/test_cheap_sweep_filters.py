"""Cheap sweep-filter profiles for researched competitions."""
from __future__ import annotations

import pathlib
import sys
import unittest

DIR = pathlib.Path(__file__).resolve().parent
ENGINE = DIR.parent / "engine"
sys.path.insert(0, str(DIR))
sys.path.insert(0, str(ENGINE))

from cheap_sweep_filters import (
    DEFERRED, NEUTRAL, PRIMARY, SECONDARY, SPECIAL,
    classify_research_priority,
)
from goals_first_intake import _research_order, select
from league_registry import classify
from stage import sweep, verify_rank_source_and_status
from test_source_completeness import source as complete_source


NOW = "2026-10-13T00:30:00Z"


def fixture(country, competition, home="Home", away="Away", kind="DOMESTIC_LEAGUE"):
    return {
        "country": country,
        "competition": competition,
        "competition_kind": kind,
        "home": home,
        "away": away,
    }


class CheapSweepFilterTests(unittest.TestCase):
    def test_big_five_league_status_is_never_auto_research_priority(self):
        for country, competition in (
            ("England", "Premier League"),
            ("Germany", "Bundesliga"),
            ("Spain", "La Liga"),
            ("Italy", "Serie A"),
            ("France", "Ligue 1"),
        ):
            with self.subTest(country=country, competition=competition):
                result = classify_research_priority(
                    fixture(country, competition, "Team A", "Team B"),
                    at_utc=NOW,
                )
                self.assertEqual(result["priority"], DEFERRED)
                self.assertEqual(result["reason"], "TOP_FIVE_STATUS_NOT_A_GOAL_SIGNAL")
                self.assertFalse(result["hard_exclude"])

    def test_big_five_pending_fixture_stays_out_of_active_research_list(self):
        src = {
            "match_id": "top5-pending", "country": "England",
            "competition": "Premier League", "competition_kind": "DOMESTIC_LEAGUE",
            "home": "Team A", "away": "Team B",
        }
        ledger = [{
            "match_id": "top5-pending", "country": "England",
            "competition": "Premier League", "home": "Team A", "away": "Team B",
            "kickoff_utc": "2026-10-13T04:00:00Z",
            "registry_lane": "ROUTINE", "intake_lane": "ROUTINE",
            "reason": "RESEARCHED_LEAGUE_ROUTINE",
            "source_url": "https://sports.example.org/top5",
            "discovery_screen": {
                "status": "PENDING_GOAL_HISTORY",
                "reason": "RECENT_COMPETITIVE_HISTORY_REQUIRED",
            },
        }]
        provisional = [{
            "match_id": "top5-pending",
            "kickoff_utc": "2026-10-13T04:00:00Z",
        }]
        result = select(
            run_id="V4-TEST", at_utc=NOW, source_hash="abc",
            source_rows=[src], ledger=ledger, provisional_queue=provisional,
        )
        self.assertEqual(result["priority_research_count"], 0)
        self.assertEqual(result["deferred_research_count"], 1)
        self.assertEqual(result["deferred_research_queue"][0]["match_id"], "top5-pending")

    def test_verified_goal_evidence_can_still_promote_big_five_fixture(self):
        src = {
            "match_id": "top5-qualified", "country": "Italy",
            "competition": "Serie A", "competition_kind": "DOMESTIC_LEAGUE",
            "home": "Team A", "away": "Team B",
        }
        ledger = [{
            "match_id": "top5-qualified", "country": "Italy",
            "competition": "Serie A", "home": "Team A", "away": "Team B",
            "kickoff_utc": "2026-10-13T04:00:00Z",
            "registry_lane": "ROUTINE", "intake_lane": "ROUTINE",
            "reason": "RESEARCHED_LEAGUE_ROUTINE",
            "source_url": "https://sports.example.org/top5q",
            "discovery_screen": {
                "status": "DISCOVERY_GOAL_QUALIFIED",
                "reason": "SOURCE_BACKED_GOAL_SIGNAL_QUALIFIED",
                "priority_score": 9,
            },
        }]
        provisional = [{
            "match_id": "top5-qualified",
            "kickoff_utc": "2026-10-13T04:00:00Z",
        }]
        result = select(
            run_id="V4-TEST", at_utc=NOW, source_hash="abc",
            source_rows=[src], ledger=ledger, provisional_queue=provisional,
        )
        self.assertEqual([x["match_id"] for x in result["eligible_queue"]], ["top5-qualified"])
        self.assertEqual(result["priority_research_count"], 0)
        self.assertEqual(result["deferred_research_count"], 0)

    def test_eredivisie_high_event_primary_otherwise_secondary(self):
        high = classify_research_priority(
            fixture("Netherlands", "Eredivisie", "PSV Eindhoven", "AZ Alkmaar"),
            at_utc=NOW,
        )
        base = classify_research_priority(
            fixture("Netherlands", "Eredivisie", "AZ Alkmaar", "Heerenveen"),
            at_utc=NOW,
        )
        self.assertEqual(high["priority"], PRIMARY)
        self.assertEqual(base["priority"], SECONDARY)

    def test_iceland_top_and_first_are_goal_positive_but_second_stays_pilot_deferred(self):
        top = classify_research_priority(
            fixture("Iceland", "Besta deild karla", "KR Reykjavik", "Valur"),
            at_utc=NOW,
        )
        first = classify_research_priority(
            fixture("Iceland", "Lengjudeild karla", "Afturelding", "Njardvik"),
            at_utc=NOW,
        )
        second = classify_research_priority(
            fixture("Iceland", "2. deild karla", "Club A", "Club B"),
            at_utc=NOW,
        )
        self.assertEqual(top["priority"], PRIMARY)
        self.assertEqual(first["priority"], PRIMARY)
        self.assertEqual(second["priority"], DEFERRED)
        self.assertTrue(second["requires_team_identity_check"])

    def test_faroe_top_selective_but_first_division_high_goal(self):
        top_event = classify_research_priority(
            fixture("Faroe Islands", "Meistaradeildin menn", "HB Torshavn", "KI Klaksvik"),
            at_utc=NOW,
        )
        top_base = classify_research_priority(
            fixture("Faroe Islands", "Meistaradeildin menn", "KI Klaksvik", "07 Vestur"),
            at_utc=NOW,
        )
        first = classify_research_priority(
            fixture("Faroe Islands", "1. deild menn", "B36 Torshavn II", "Club B"),
            at_utc=NOW,
        )
        self.assertEqual(top_event["priority"], SECONDARY)
        self.assertEqual(top_base["priority"], DEFERRED)
        self.assertEqual(first["priority"], PRIMARY)
        self.assertTrue(first["requires_team_identity_check"])

    def test_norway_first_is_stronger_than_eliteserien_base(self):
        elite_event = classify_research_priority(
            fixture("Norway", "Eliteserien", "Viking FK", "Sandefjord"),
            at_utc=NOW,
        )
        elite_base = classify_research_priority(
            fixture("Norway", "Eliteserien", "Tromso", "Sandefjord"),
            at_utc=NOW,
        )
        first_high = classify_research_priority(
            fixture("Norway", "OBOS-ligaen", "Ranheim", "Lyn"),
            at_utc=NOW,
        )
        first_base = classify_research_priority(
            fixture("Norway", "1. divisjon", "Bryne", "Lyn"),
            at_utc=NOW,
        )
        self.assertEqual(elite_event["priority"], SECONDARY)
        self.assertEqual(elite_base["priority"], DEFERRED)
        self.assertEqual(first_high["priority"], PRIMARY)
        self.assertEqual(first_base["priority"], SECONDARY)

    def test_denmark_first_keeps_draw_trap_caution_and_superliga_is_selective(self):
        super_event = classify_research_priority(
            fixture("Denmark", "Superliga", "FC Copenhagen", "Odense BK"),
            at_utc=NOW,
        )
        super_base = classify_research_priority(
            fixture("Denmark", "Superliga", "Midtjylland", "Nordsjaelland"),
            at_utc=NOW,
        )
        first_event = classify_research_priority(
            fixture("Denmark", "1st Division", "Hobro", "Aalborg"),
            at_utc=NOW,
        )
        first_base = classify_research_priority(
            fixture("Denmark", "1st Division", "Hillerod", "Fredericia"),
            at_utc=NOW,
        )
        self.assertEqual(super_event["priority"], SECONDARY)
        self.assertEqual(super_base["priority"], DEFERRED)
        self.assertEqual(first_event["priority"], SECONDARY)
        self.assertEqual(first_base["priority"], DEFERRED)
        self.assertTrue(first_base["draw_trap_caution"])

    def test_sweden_top_and_second_divisions_are_team_selective(self):
        all_event = classify_research_priority(
            fixture("Sweden", "Allsvenskan", "IK Sirius", "GAIS"),
            at_utc=NOW,
        )
        all_base = classify_research_priority(
            fixture("Sweden", "Allsvenskan", "GAIS", "Halmstad"),
            at_utc=NOW,
        )
        sup_event = classify_research_priority(
            fixture("Sweden", "Superettan", "Falkenbergs FF", "Ostersunds FK"),
            at_utc=NOW,
        )
        sup_base = classify_research_priority(
            fixture("Sweden", "Superettan", "Ostersunds FK", "IFK Norrkoping"),
            at_utc=NOW,
        )
        self.assertEqual(all_event["priority"], SECONDARY)
        self.assertEqual(all_base["priority"], DEFERRED)
        self.assertEqual(sup_event["priority"], SECONDARY)
        self.assertEqual(sup_base["priority"], DEFERRED)

    def test_registry_recognizes_researched_iceland_faroe_and_graduated_nordic_seconds(self):
        checks = (
            ("Iceland", "Besta deild karla", "CONDITIONAL"),
            ("Iceland", "Lengjudeild karla", "CONDITIONAL"),
            ("Iceland", "2. deild karla", "PILOT"),
            ("Faroe Islands", "Meistaradeildin menn", "CONDITIONAL"),
            ("Faroe Islands", "1. deild menn", "PILOT"),
            ("Sweden", "Superettan", "CONDITIONAL"),
            ("Denmark", "1st Division", "CONDITIONAL"),
        )
        for country, competition, lane in checks:
            with self.subTest(country=country, competition=competition):
                self.assertEqual(classify(fixture(country, competition))["lane"], lane)

    def test_eerste_high_event_team_is_primary_otherwise_secondary(self):
        high = classify_research_priority(
            fixture("Netherlands", "Eerste Divisie", "FC Dordrecht", "Roda JC"),
            at_utc=NOW,
        )
        base = classify_research_priority(
            fixture("Netherlands", "Eerste Divisie", "Roda JC", "Almere City"),
            at_utc=NOW,
        )
        self.assertEqual(high["priority"], PRIMARY)
        self.assertEqual(base["priority"], SECONDARY)
        self.assertFalse(high["hard_exclude"])

    def test_we_league_is_selective_not_blanket_primary(self):
        high = classify_research_priority(
            fixture("Japan", "WE League", "NTV Beleza", "JEF United", "WOMENS_TOP_FLIGHT"),
            at_utc=NOW,
        )
        base = classify_research_priority(
            fixture("Japan", "WE League", "Sanfrecce Hiroshima Regina", "Albirex Niigata W", "WOMENS_TOP_FLIGHT"),
            at_utc=NOW,
        )
        self.assertEqual(high["priority"], PRIMARY)
        self.assertEqual(base["priority"], SECONDARY)

    def test_we_cup_keeps_draw_trap_caution(self):
        event = classify_research_priority(
            fixture("Japan", "WE League Cup", "Urawa W", "INAC Kobe Leonesa", "DOMESTIC_CUP"),
            at_utc=NOW,
        )
        ordinary = classify_research_priority(
            fixture("Japan", "WE League Cup", "Mynavi Sendai Ladies", "Albirex Niigata W", "DOMESTIC_CUP"),
            at_utc=NOW,
        )
        self.assertEqual(event["priority"], SECONDARY)
        self.assertEqual(ordinary["priority"], DEFERRED)
        self.assertTrue(event["draw_trap_caution"])
        self.assertTrue(ordinary["draw_trap_caution"])

    def test_nadeshiko_one_selective_and_two_deferred(self):
        one_event = classify_research_priority(
            fixture("Japan", "Nadeshiko League 1", "Nittaidai FC", "Iga Kunoichi"),
            at_utc=NOW,
        )
        one_base = classify_research_priority(
            fixture("Japan", "Nadeshiko League 1", "Iga Kunoichi", "Speranza Osaka"),
            at_utc=NOW,
        )
        two = classify_research_priority(
            fixture("Japan", "Nadeshiko League 2", "Team A", "Team B"),
            at_utc=NOW,
        )
        self.assertEqual(one_event["priority"], SECONDARY)
        self.assertEqual(one_base["priority"], DEFERRED)
        self.assertEqual(two["priority"], DEFERRED)
        self.assertTrue(two["draw_trap_caution"])

    def test_empress_cup_is_special_not_blanket_goal_positive(self):
        result = classify_research_priority(
            fixture("Japan", "Empress's Cup Women", "Club A", "Club B", "DOMESTIC_CUP"),
            at_utc=NOW,
        )
        self.assertEqual(result["priority"], SPECIAL)
        self.assertTrue(result["requires_tier_round_context"])
        self.assertFalse(result["hard_exclude"])

    def test_profiles_expire_to_neutral(self):
        result = classify_research_priority(
            fixture("Netherlands", "Eerste Divisie", "Heracles", "VVV"),
            at_utc="2026-11-14T00:00:00Z",
        )
        self.assertEqual(result["priority"], NEUTRAL)
        self.assertTrue(result["profile_expired"])

    def test_registry_recognizes_japanese_women_competitions(self):
        self.assertEqual(
            classify(fixture("Japan", "Nadeshiko League 1"))["lane"],
            "CONDITIONAL",
        )
        self.assertEqual(
            classify(fixture("Japan", "Nadeshiko League 2"))["lane"],
            "CONDITIONAL",
        )
        self.assertEqual(
            classify(fixture("Japan", "Empress's Cup Women", kind="DOMESTIC_CUP"))["lane"],
            "CONDITIONAL",
        )

    def test_pending_research_order_uses_cheap_filter_before_kickoff(self):
        early_deferred = {
            "goal_screen": {"status": "PENDING_GOAL_HISTORY"},
            "cheap_filter": {"priority_rank": 3},
            "kickoff_utc": "2026-10-13T01:00:00Z",
            "match_id": "deferred",
        }
        later_primary = {
            "goal_screen": {"status": "PENDING_GOAL_HISTORY"},
            "cheap_filter": {"priority_rank": 0},
            "kickoff_utc": "2026-10-13T04:00:00Z",
            "match_id": "primary",
        }
        ordered = sorted([early_deferred, later_primary], key=_research_order)
        self.assertEqual([x["match_id"] for x in ordered], ["primary", "deferred"])

    def test_pre_filter_frozen_receipt_replays_without_retroactive_filter_fields(self):
        src = complete_source()
        old = sweep(src, now="2026-10-12T18:05:00Z", _historical_no_cheap_filters=True)
        self.assertNotIn("cheap_filter_policy", old)
        refresh = {
            "schema_version": "football-v4-rank-status-refresh-v1",
            "run_id": old["run_id"],
            "sweep_integrity_sha256": old["integrity_sha256"],
            "checked_at_utc": "2026-10-12T18:05:00Z",
            "matches": [],
        }
        proof = verify_rank_source_and_status(
            old, src, refresh, now="2026-10-12T18:05:00Z"
        )
        self.assertEqual(proof["status_by_match"], {})

    def test_new_sweep_receipt_declares_filter_policy(self):
        new = sweep(complete_source(), now="2026-10-12T18:05:00Z")
        self.assertEqual(new["cheap_filter_policy"], "RESEARCH_PRIORITY_V1")
        self.assertIn("cheap_filter_counts", new)

    def test_verified_goal_signal_still_beats_cheap_defer(self):
        qualified = {
            "goal_screen": {"status": "DISCOVERY_GOAL_QUALIFIED", "priority_score": 1},
            "cheap_filter": {"priority_rank": 3},
            "kickoff_utc": "2026-10-13T05:00:00Z",
            "match_id": "qualified",
        }
        pending = {
            "goal_screen": {"status": "PENDING_GOAL_HISTORY"},
            "cheap_filter": {"priority_rank": 0},
            "kickoff_utc": "2026-10-13T01:00:00Z",
            "match_id": "pending",
        }
        ordered = sorted([pending, qualified], key=_research_order)
        self.assertEqual([x["match_id"] for x in ordered], ["qualified", "pending"])


if __name__ == "__main__":
    unittest.main()
