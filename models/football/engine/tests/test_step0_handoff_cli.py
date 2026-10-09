import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

ENGINE = pathlib.Path(__file__).resolve().parents[1]
CLI = ENGINE / "step0_handoff_cli.py"


def row(mid, rank, disp="ADMITTED_TO_C"):
    return {
        "match_id": mid,
        "step0_capacity_queue_rank": rank,
        "final_step0_disposition": disp,
        "operational_viability_grade": "A",
        "xi_expected": "YES",
        "market_observability": "HIGH",
        "team_news_observability": "HIGH",
        "operational_viability_reason": "ok",
        "competition_reliability_state": "UNPROVEN",
        "competition_reliability_reason": "sample",
    }


def proof(row):
    row = dict(row)
    row.update({
        "preflight_complete": True,
        "competition_support_tier": "VERIFIED_PROFESSIONAL",
        "competition_official_url": "https://league.example.org",
        "competition_support_reason": "Verified first-team professional league",
        "fixture_identity_verified": True,
        "fixture_kickoff_utc": "2026-10-10T00:00:00Z",
        "xi_home_recent_match_id": "home-previous",
        "xi_away_recent_match_id": "away-previous",
        "xi_home_recent_match_kickoff_utc": "2026-10-01T00:00:00Z",
        "xi_away_recent_match_kickoff_utc": "2026-10-02T00:00:00Z",
        "xi_home_lineup_source_url": "https://aiscore.example.org/home-previous",
        "xi_away_lineup_source_url": "https://aiscore.example.org/away-previous",
        "asian_total_fixture_source_url": "https://odds.example.org/totals",
        "asian_total_market_match_id": row["match_id"],
        "asian_total_market_observed_at_utc": "2026-10-09T15:00:00Z",
        "asian_total_market_line": 2.5,
        "asian_total_market_bookmaker": "Bookmaker fixture screen",
        "team_news_source_url": "https://club.example.org/news",
    })
    return row


def payload():
    r = row("m1", 1)
    return {
        "handoff_version": "football-step0-handoff-v2",
        "complete": True,
        "actionable_complete": True,
        "work_ready": True,
        "admitted_to_c_count": 1,
        "capacity_deferred_count": 0,
        "admitted_fixtures": [dict(r)],
        "capacity_queue": [dict(r)],
    }


def bounded_payload():
    p = payload()
    p.update(
        {
            "source_scope": "BOUNDED_PRODUCTION_DISCOVERY",
            "source_transport": "MULTISOURCE_BOUNDED_PRODUCTION_DISCOVERY",
            "coverage_mode": "FALLBACK_PRODUCTION_SCOPE",
            "global_raw_exact": False,
            "production_scope_complete": True,
            "production_universe_count": 7,
            "block_excluded_summary": [],
            "discovery_seed_manifest": {
                "sources": [
                    {
                        "family": "FootballFixtures.org",
                        "date": "2026-10-06",
                    },
                    {
                        "family": "FootballInfo",
                        "date": "2026-10-06",
                    },
                ]
            },
        }
    )
    return p


class T(unittest.TestCase):
    def runp(self, p, consumer="export"):
        with tempfile.NamedTemporaryFile(
            "w", suffix=".json", delete=False
        ) as f:
            json.dump(p, f)
            name = f.name
        return subprocess.run(
            [
                sys.executable,
                str(CLI),
                "--input",
                name,
                "--consumer",
                consumer,
            ],
            capture_output=True,
            text=True,
        )

    def test_pass_legacy_v2(self):
        result = self.runp(payload())
        self.assertEqual(result.returncode, 0)
        self.assertIn("LEGACY_EXACT_OR_PRE_SCOPE", result.stdout)

    def test_bounded_production_handoff_passes(self):
        result = self.runp(bounded_payload())
        self.assertEqual(result.returncode, 0)
        self.assertIn("BOUNDED_PRODUCTION_DISCOVERY", result.stdout)

    def test_bounded_array_manifest_passes_export_and_rank(self):
        for consumer in ("export", "rank"):
            p = bounded_payload()
            p["discovery_seed_manifest"] = p["discovery_seed_manifest"]["sources"]
            result = self.runp(p, consumer=consumer)
            self.assertEqual(result.returncode, 0)
            self.assertIn(
                "BOUNDED_SOURCE_PROVENANCE_PRESENT_ARRAY",
                result.stdout,
            )

    def test_bounded_array_manifest_accepts_source_family_alias(self):
        p = bounded_payload()
        p["discovery_seed_manifest"] = [
            {
                "source_family": "FootballFixtures.org",
                "date": "2026-10-06",
            },
            {
                "source_family": "FootballInfo",
                "date": "2026-10-06",
            },
        ]
        result = self.runp(p, consumer="rank")
        self.assertEqual(result.returncode, 0)
        self.assertIn(
            "BOUNDED_SOURCE_PROVENANCE_PRESENT_ARRAY",
            result.stdout,
        )

    def test_rank_accepts_transitional_bounded_handoff_without_manifest(self):
        p = bounded_payload()
        del p["discovery_seed_manifest"]
        result = self.runp(p, consumer="rank")
        self.assertEqual(result.returncode, 0)
        self.assertIn(
            "LEGACY_MISSING_DISCOVERY_SEED_MANIFEST",
            result.stdout,
        )

    def test_export_rejects_bounded_handoff_without_manifest(self):
        p = bounded_payload()
        del p["discovery_seed_manifest"]
        result = self.runp(p, consumer="export")
        self.assertEqual(result.returncode, 2)
        self.assertIn("discovery_seed_manifest", result.stderr)

    def test_rank_accepts_transitional_bounded_handoff_without_block_summary(self):
        p = bounded_payload()
        del p["block_excluded_summary"]
        result = self.runp(p, consumer="rank")
        self.assertEqual(result.returncode, 0)
        self.assertIn(
            "LEGACY_MISSING_BLOCK_EXCLUDED_SUMMARY",
            result.stdout,
        )

    def test_bounded_requires_fallback_coverage_mode(self):
        p = bounded_payload()
        p["coverage_mode"] = "EXACT"
        result = self.runp(p)
        self.assertEqual(result.returncode, 2)
        self.assertIn("coverage_mode=FALLBACK_PRODUCTION_SCOPE", result.stderr)

    def test_bounded_requires_production_scope_complete(self):
        p = bounded_payload()
        p["production_scope_complete"] = False
        result = self.runp(p)
        self.assertEqual(result.returncode, 2)
        self.assertIn("production_scope_complete=true", result.stderr)

    def test_bounded_requires_two_independent_source_families(self):
        p = bounded_payload()
        p["discovery_seed_manifest"]["sources"][1]["family"] = (
            "FootballFixtures.org"
        )
        result = self.runp(p)
        self.assertEqual(result.returncode, 2)
        self.assertIn("two independent source families", result.stderr)

    def test_bounded_requires_production_universe_count(self):
        p = bounded_payload()
        del p["production_universe_count"]
        result = self.runp(p)
        self.assertEqual(result.returncode, 2)
        self.assertIn("production_universe_count", result.stderr)

    def test_missing_queue(self):
        p = payload()
        del p["capacity_queue"]
        result = self.runp(p)
        self.assertEqual(result.returncode, 2)
        self.assertIn("CAPACITY QUEUE MISSING", result.stderr)

    def test_missing_id(self):
        p = payload()
        del p["capacity_queue"][0]["match_id"]
        result = self.runp(p)
        self.assertEqual(result.returncode, 2)
        self.assertIn("STABLE FIXTURE ID MISSING", result.stderr)

    def test_missing_field(self):
        p = payload()
        del p["capacity_queue"][0]["xi_expected"]
        result = self.runp(p)
        self.assertEqual(result.returncode, 2)
        self.assertIn("OPERATIONAL CONTRACT MISSING", result.stderr)


    def test_compact_handoff_accepts_exact_operational_top_eight(self):
        p = payload()
        p["sweep_work_budget_policy"] = "COMPACT_GOAL_ROUTE_V1"
        p["capacity_queue"] = [
            proof(row(f"m{i}", i, "ADMITTED_TO_C" if i <= 8 else "OPERATIONAL_CAPACITY_DEFERRED"))
            for i in range(1, 14)
        ]
        p["admitted_fixtures"] = [dict(r) for r in p["capacity_queue"][:8]]
        p["admitted_to_c_count"] = 8
        p["capacity_deferred_count"] = 5
        out = self.runp(p)
        self.assertEqual(out.returncode, 0)
        self.assertIn('"admitted_count": 8', out.stdout)

    def test_compact_handoff_rejects_nine_admitted(self):
        p = payload()
        p["sweep_work_budget_policy"] = "COMPACT_GOAL_ROUTE_V1"
        p["admitted_fixtures"] = [row(f"m{i}", i) for i in range(1, 10)]
        p["capacity_queue"] = list(p["admitted_fixtures"])
        p["admitted_to_c_count"] = 9
        out = self.runp(p)
        self.assertEqual(out.returncode, 2)
        self.assertIn("OPERATIONAL CAPACITY BREACH", out.stderr)

    def test_compact_handoff_rejects_skipped_better_rank(self):
        p = payload()
        p["sweep_work_budget_policy"] = "COMPACT_GOAL_ROUTE_V1"
        p["capacity_queue"] = [
            proof(row(f"m{i}", i, "ADMITTED_TO_C" if (i <= 9 and i != 3) else "OPERATIONAL_CAPACITY_DEFERRED"))
            for i in range(1, 10)
        ]
        p["admitted_fixtures"] = [dict(r) for r in p["capacity_queue"] if r["final_step0_disposition"] == "ADMITTED_TO_C"]
        p["admitted_to_c_count"] = 8
        p["capacity_deferred_count"] = 1
        out = self.runp(p)
        self.assertEqual(out.returncode, 2)
        self.assertIn("compact ranks 1-8", out.stderr)


    def test_compact_handoff_blocks_uncertain_xi_even_if_grade_b(self):
        p = payload()
        p["sweep_work_budget_policy"] = "COMPACT_GOAL_ROUTE_V1"
        r = proof(row("m1", 1))
        r["operational_viability_grade"] = "B"
        r["xi_expected"] = "UNCERTAIN"
        p["capacity_queue"] = [r]
        p["admitted_fixtures"] = [dict(r)]
        out = self.runp(p)
        self.assertEqual(out.returncode, 2)
        self.assertIn("XI_CHANNEL_NOT_VERIFIABLE", out.stderr)

    def test_compact_handoff_blocks_unproven_market(self):
        p = payload()
        p["sweep_work_budget_policy"] = "COMPACT_GOAL_ROUTE_V1"
        r = proof(row("m1", 1))
        r.pop("asian_total_fixture_source_url")
        p["capacity_queue"] = [r]
        p["admitted_fixtures"] = [dict(r)]
        out = self.runp(p)
        self.assertEqual(out.returncode, 2)
        self.assertIn("CURRENT_ASIAN_TOTAL_SOURCE_MISSING", out.stderr)


    def test_unfinished_legacy_strict_marker_rejects_uncertain_xi(self):
        p = payload()
        p["strict_intake_policy"] = "XI_MARKET_FIRST_V1"
        r = proof(row("m1", 1))
        r["xi_expected"] = "UNCERTAIN"
        p["capacity_queue"] = [r]
        p["admitted_fixtures"] = [dict(r)]
        out = self.runp(p)
        self.assertEqual(out.returncode, 2)
        self.assertIn("XI_CHANNEL_NOT_VERIFIABLE", out.stderr)

    def test_unfinished_legacy_strict_marker_preserves_fifteen_slot_budget(self):
        p = payload()
        p["strict_intake_policy"] = "XI_MARKET_FIRST_V1"
        p["capacity_queue"] = [proof(row(f"m{i}", i)) for i in range(1, 16)]
        p["admitted_fixtures"] = [dict(r) for r in p["capacity_queue"]]
        p["admitted_to_c_count"] = 15
        out = self.runp(p)
        self.assertEqual(out.returncode, 0)



if __name__ == "__main__":
    unittest.main()
