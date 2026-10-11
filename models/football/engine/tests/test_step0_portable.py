"""Guard Step0 one-file runtime, correctness and source freshness in CI."""
import hashlib
import importlib.util
import json
import pathlib
import sys
import tempfile
import unittest

ENGINE = pathlib.Path(__file__).resolve().parents[1]
ROOT = ENGINE.parents[2]
BUNDLE = ENGINE / "step0_portable.py"


class PortableStep0Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location("step0_portable_test", BUNDLE)
        assert spec and spec.loader
        cls.portable = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.portable)

    def test_exact_source_freshness_and_self_check(self):
        for rel, blob in self.portable.SOURCE_BLOB_SHA.items():
            data = (ROOT / rel).read_bytes()
            got = hashlib.sha1(
                b"blob " + str(len(data)).encode("ascii") + b"\0" + data
            ).hexdigest()
            self.assertEqual(got, blob, rel)
        result = self.portable.self_check()
        self.assertTrue(result["ok"], result)
        self.assertEqual(result["module_count"], 7)

    def test_bangladesh_scope_rejected_inside_portable(self):
        self.portable._load()
        from sweep_competition_scope import classify_competition
        x = classify_competition({
            "competition_name": "Bangladesh Premier League",
            "competition_kind": "DOMESTIC_LEAGUE",
            "country": "Bangladesh",
        })
        self.assertEqual(x["lane"], "SCOPE_EXCLUDED")

    def test_researchable_japan_and_korean_leagues_preserved_in_portable(self):
        self.portable._load()
        from sweep_competition_scope import classify_competition
        for competition, country, expected in (
            ("J1 League","Japan","ROUTINE_LEAGUE_PROFILE"),
            ("J2 League","Japan","ROUTINE_LEAGUE_PROFILE"),
            ("K League 1","South Korea","ROUTINE_LEAGUE_PROFILE"),
            ("K League 2","South Korea","CONDITIONAL_CHEAP_GATE"),
            ("WE League Cup","Japan","CUP_CHANNEL_REVIEW"),
        ):
            kind = "DOMESTIC_CUP" if competition == "WE League Cup" else "DOMESTIC_LEAGUE"
            result = classify_competition({"competition_name":competition,"country":country,"competition_kind":kind})
            self.assertEqual(result["lane"],expected)

    def test_portable_second_division_pilot_and_championship_validator(self):
        self.portable._load()
        from sweep_competition_scope import classify_competition
        from sweep_intake_evidence import validate_work_candidate
        from test_sweep_intake_evidence import league_candidate, LeagueChannelFirstTests
        for label,country,expected in (
            ("2. Bundesliga","Germany","ROUTINE_LEAGUE_PROFILE"),
            ("Championship","England","CONDITIONAL_CHEAP_GATE"),
            ("3. Liga","Germany","SCOPE_EXCLUDED"),
            ("Serie B","Italy","SCOPE_EXCLUDED"),
            ("Ligue 2","France","SCOPE_EXCLUDED"),
        ):
            decision = classify_competition({
                "competition_name":label, "country":country,
                "competition_kind":"DOMESTIC_LEAGUE"})
            self.assertEqual(decision["lane"],expected, (label,country))
        row = league_candidate("Championship", "PROVEN_LEAGUE")
        self.assertIn("CHAMPIONSHIP_CHEAP_SIGNAL_MISSING",
                      validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"))
        row["championship_recent_goal_evidence"] = LeagueChannelFirstTests.championship_evidence()
        self.assertEqual(validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"), [])

    def test_obos_portable_scope_and_proven_channel_policy(self):
        self.portable._load()
        from sweep_competition_scope import classify_competition
        from sweep_intake_evidence import validate_work_candidate
        from test_sweep_intake_evidence import league_candidate
        for alias in ("OBOS-ligaen", "1. divisjon", "Norway First Division"):
            self.assertEqual(classify_competition({
                "competition_name": alias,
                "competition_kind": "DOMESTIC_LEAGUE",
                "country": "Norway"})["lane"], "ROUTINE_LEAGUE_PROFILE")
        for league in ("2. divisjon", "3. divisjon"):
            self.assertEqual(classify_competition({
                "competition_name": league,
                "competition_kind": "DOMESTIC_LEAGUE",
                "country": "Norway"})["lane"], "SCOPE_EXCLUDED")
        row = league_candidate("OBOS-ligaen", "PROVEN_LEAGUE")
        self.assertEqual(validate_work_candidate(
            row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"), [])
        row["league_channel_profile"]["recent_xi_fixture_count"] = 0
        self.assertIn("LEAGUE_PROFILE_RECENT_XI_FIXTURE_COUNT_UNPROVEN",
                      validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"))

    def test_portable_poland_ekstraklasa_conditional_requires_source_results(self):
        self.portable._load()
        from sweep_competition_scope import classify_competition
        from sweep_intake_evidence import validate_work_candidate
        from test_sweep_intake_evidence import league_candidate, LeagueChannelFirstTests
        result = classify_competition({
            "competition_name":"Ekstraklasa", "country":"Poland",
            "competition_kind":"DOMESTIC_LEAGUE"})
        self.assertEqual(result["lane"], "CONDITIONAL_CHEAP_GATE")
        self.assertIn("SOURCE-LOCAL", result["reason"])
        row = league_candidate("Ekstraklasa", "PROVEN_LEAGUE")
        row["country"] = "Poland"
        self.assertIn("POLAND_EKSTRAKLASA_CHEAP_SIGNAL_MISSING",
                      validate_work_candidate(row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"))
        row["poland_ekstraklasa_recent_goal_evidence"] = LeagueChannelFirstTests.championship_evidence()
        self.assertEqual(validate_work_candidate(
            row, intake_policy="LEAGUE_CHANNEL_FIRST_V1"), [])

    def test_portable_hk_malaysia_pilot_parity(self):
        self.portable._load()
        from sweep_competition_scope import classify_competition
        from sweep_intake_evidence import validate_work_candidate
        from test_sweep_intake_evidence import league_candidate, LeagueChannelFirstTests
        for league,country in (("Premier League","Hong Kong"),
                               ("Liga Super","Malaysia")):
            decision=classify_competition({"competition_name":league,"country":country,
                                           "competition_kind":"DOMESTIC_LEAGUE"})
            self.assertEqual(decision["lane"],"CONDITIONAL_CHEAP_GATE")
            row=league_candidate(league,"PROVEN_LEAGUE")
            row["country"]=country
            row["asia_topflight_recent_goal_evidence"]=LeagueChannelFirstTests.asia_goal_evidence()
            self.assertEqual(validate_work_candidate(row,intake_policy="LEAGUE_CHANNEL_FIRST_V1"),[])
        self.assertEqual(classify_competition({
            "competition_name":"Premier League U22","country":"Hong Kong",
            "competition_kind":"DOMESTIC_LEAGUE"})["lane"],"SCOPE_EXCLUDED")

    def test_portable_package_same_guarded_success_and_failure(self):
        self.portable._load()
        from step0_package_cli import package, Step0HandoffError
        from test_step0_package_cli import scenario
        handoff, run = scenario()
        with tempfile.TemporaryDirectory() as d:
            root = pathlib.Path(d)
            h = root / "STEP0_HANDOFF.json"
            t = root / "AISCORE_FIXTURES_TEST.txt"
            proof = root / "proof.json"
            output = root / "AISCORE_FIXTURES_TEST.zip"
            h.write_text(json.dumps(handoff))
            proof.write_text(json.dumps(run))
            t.write_text("validated senior Work handoff")
            result = package(h, t, proof, output)
            self.assertEqual(result["status"], "STEP0 WORK ZIP VALIDATED")
            self.assertTrue(output.exists())
            output.unlink()
            handoff["work_ready"] = False
            h.write_text(json.dumps(handoff))
            with self.assertRaises(Step0HandoffError):
                package(h, t, proof, output)
            self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
