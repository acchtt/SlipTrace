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


if __name__ == "__main__":
    unittest.main()
