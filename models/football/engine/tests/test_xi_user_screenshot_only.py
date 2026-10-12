"""Screenshot-only /xi price evidence regression (no replacement quotes)."""
import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

ENGINE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE))
from test_adapter import pair_payload
from test_football_assessment_pair import football
from xi_assessment_reconcile import (verify_football_assessment, STATUS_FIELD_ID,
    EVIDENCE_SUMMARY_FIELD_ID, screenshot_evidence_summary_line, XIAssessmentReadbackError)


CAPTURE = "2026-10-11T05:05:00+00:00"
OLDER = "2026-10-11T05:04:00+00:00"


def snapshot(c, *, line=2.5, odds=1.70, captured=CAPTURE, **changes):
    obj = {
        "evidence_mode": "USER_SCREENSHOT_ONLY",
        "source": "USER_SCREENSHOT",
        "capture_reference": "user-attachment-screenshot-1",
        "match_id": c["match"]["match_id"],
        "bookmaker": "User-displayed bookmaker",
        "quote": {"line": line, "odds": odds},
        "observed_at_utc": captured,
        "fixture_status": c["context"]["fixture_status"],
        "score": c["context"]["score"],
        "match_minute": c["context"]["match_minute"],
    }
    obj.update(changes)
    return obj


def run_xi(c=None, c2=None, shot=None, priced=False, price_mutator=None):
    c = c or football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
    c2 = c2 or football("c2", status="PREMATCH_CONFIRMED", minute=None, score=None)
    shot = shot if shot is not None else snapshot(c)
    with tempfile.TemporaryDirectory() as td:
        root = pathlib.Path(td)
        paths = {}
        docs = {"c": c, "c2": c2, "screenshot": shot}
        if priced:
            p, p2 = pair_payload("c"), pair_payload("c2")
            for model, obj in (("c", p), ("c2", p2)):
                obj["evidence_epoch_id"] = c["evidence_epoch_id"]
                obj["context"]["quote"] = dict(shot["quote"])
            if price_mutator:
                price_mutator(p, p2)
            docs.update({"pc": p, "pc2": p2})
        for name, doc in docs.items():
            f = root / (name + ".json")
            f.write_text(json.dumps(doc), encoding="utf-8")
            paths[name] = str(f)
        args = [sys.executable, str(ENGINE / "xi_portable.py"), "xi",
                "--c", paths["c"], "--c2", paths["c2"],
                "--screenshot-quote", paths["screenshot"]]
        if priced:
            args += ["--price-c", paths["pc"], "--price-c2", paths["pc2"]]
        result = subprocess.run(args, text=True, capture_output=True, timeout=30)
        if result.returncode:
            raise AssertionError(result.stderr)
        return json.loads(result.stdout)


class ScreenshotOnlyXIRegression(unittest.TestCase):
    def test_01_prematch_line_and_bookmaker_preserved(self):
        out = run_xi()
        ev = out["price_check"]["evidence"]
        self.assertEqual(ev["quote"], {"line": 2.5, "odds": 1.70})
        self.assertEqual(ev["bookmaker"], "User-displayed bookmaker")
        self.assertEqual(ev["capture_reference"], "user-attachment-screenshot-1")
        self.assertEqual(ev["observed_at_utc"], CAPTURE)
        self.assertEqual(ev["assessment_at_utc"], CAPTURE)
        self.assertEqual(out["models_executed"], ["c", "c2"])
        self.assertFalse(out["price_check"]["bet_authorized"])

    def test_02_focus_over_275_at_163_evaluates_without_new_quote(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        out = run_xi(c=c, shot=snapshot(c, line=2.75, odds=1.63, captured=OLDER), priced=True)
        self.assertEqual(out["xi_mode"], "FOOTBALL_ASSESSED_SCREENSHOT_PRICE_LIMITED")
        self.assertEqual(out["price_check"]["evidence"]["quote"], {"line": 2.75, "odds": 1.63})
        for model in ("c", "c2"):
            self.assertEqual(out["price_check"]["models"][model]["snapshot_line_relation"], "ABOVE_SUPPORTED_BURDEN")
            self.assertIn(out["price_check"]["models"][model]["conditional_action"],
                          {"ACT", "PASS", "WAIT", "NOT_EVALUATED_RULES_INCOMPLETE"})
        self.assertFalse(out["price_check"]["bet_authorized"])

    def test_03_missing_capture_time_remains_conditional_not_retimed(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        out = run_xi(c=c, shot=snapshot(c, captured=None), priced=True)
        price = out["price_check"]
        self.assertIsNone(price["evidence"]["observed_at_utc"])
        self.assertIsNone(price["evidence"]["observation_age_seconds"])
        self.assertIn("SCREENSHOT_CAPTURE_TIME_UNKNOWN", price["limitations"])
        self.assertFalse(price["bet_authorized"])

    def test_04_live_score_and_minute_no_prematch_pricing(self):
        c, c2 = football("c"), football("c2")
        out = run_xi(c, c2, snapshot(c), priced=True)
        price = out["price_check"]
        self.assertEqual(price["evidence"]["score"], "1-0")
        self.assertEqual(price["evidence"]["match_minute"], 5)
        self.assertIn("LIVE_SCREENSHOT_NOT_EXECUTABLE_BY_PREMATCH_ENGINE", price["limitations"])
        self.assertEqual(price["models"]["c"]["conditional_action"], "NOT_EVALUATED_LIVE_REQUIRES_SEPARATE_LIVE_ENGINE")

    def test_05_outside_entry_price_keeps_protections(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        out = run_xi(c=c, shot=snapshot(c, odds=1.01, captured=OLDER), priced=True)
        self.assertFalse(out["price_check"]["bet_authorized"])
        self.assertNotEqual(out["price_check"]["models"]["c"]["conditional_action"], "ACT")

    def test_06_candidate_price_not_executable_after_capture(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        out = run_xi(c=c, shot=snapshot(c, captured=OLDER,
                     open_offer_verified_in_screenshot=True), priced=True)
        self.assertEqual(out["price_check"]["evidence"]["observation_age_seconds"], 60)
        self.assertIn("SCREENSHOT_PRICE_NOT_VERIFIED_EXECUTABLE_AT_ASSESSMENT",
                      out["price_check"]["limitations"])
        self.assertFalse(out["price_check"]["bet_authorized"])

    def test_07_snapshot_failure_never_erases_both_football_engines(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        out = run_xi(c=c, shot=snapshot(c, match_id="wrong-id"), priced=True)
        self.assertEqual(out["xi_mode"], "FOOTBALL_ASSESSED_PRICE_CHECK_BLOCKED")
        self.assertEqual(out["price_check"]["status"], "PRICE_CHECK_BLOCKED")
        self.assertEqual(set(out["results"]), {"c", "c2"})
        self.assertEqual(out["engine_execution_status"], "EXECUTED_C_C2_FOOTBALL_ONLY")

    def test_08_no_external_price_search_or_replacement(self):
        out = run_xi()
        evidence = out["price_check"]["evidence"]
        self.assertEqual(evidence["external_price_searches"], 0)
        self.assertEqual(evidence["replacement_quotes"], 0)
        self.assertFalse(out["quote_research_required"])
        self.assertFalse(out["price_check"]["quote_research_required"])

    def test_09_independent_c2_burden_and_disallowed_competing_quote(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        c2 = football("c2", status="PREMATCH_CONFIRMED", minute=None, score=None)
        c2["match"]["supported_line"] = 3.0
        out = run_xi(c, c2, snapshot(c, line=2.75, captured=OLDER))
        self.assertEqual(out["price_check"]["models"]["c"]["supported_line"], 2.5)
        self.assertEqual(out["price_check"]["models"]["c2"]["supported_line"], 3.0)
        self.assertEqual(out["price_check"]["models"]["c2"]["snapshot_line_relation"], "BELOW_SUPPORTED_BURDEN")
        def bad(p, p2):
            p2["context"]["quote"] = {"line": 3.5, "odds": 1.88}
            p2["match"]["supported_line"] = 3.0
        out = run_xi(c, c2, snapshot(c, line=2.75, captured=OLDER), priced=True, price_mutator=bad)
        self.assertEqual(out["price_check"]["status"], "PRICE_CHECK_BLOCKED")
        self.assertIn("replacement quote", out["price_check"]["reason"])

    def test_10_no_ledger_update_and_airtable_enum_compatible(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        out = run_xi(c=c, shot=snapshot(c, captured=OLDER), priced=True)
        self.assertFalse(out["model_bets_created"])
        self.assertFalse(out["price_check"]["model_bets_created"])
        self.assertFalse(out["price_check"]["priced_publication_authorized"])
        self.assertEqual(out["model_accounting_status"], "NONE")
        readback = {
            "base_id": "appbzxqXYf0lKfD4P", "record_id": "rec1234567890ABCDE",
            "assessment_id": "XI-SCREENSHOT-EXAMPLE",
            "match_id": out["results"]["c"]["match_id"],
            "readback_method": "INDEPENDENT_AIRTABLE_REFETCH",
            "xi_status_field_id": STATUS_FIELD_ID,
            "xi_assessment_execution_status": "EXECUTED_C_C2_FOOTBALL_PRICE_BLOCKED",
            "engine_c_result": out["results"]["c"],
            "engine_c2_result": out["results"]["c2"],
            "evidence_summary_field_id": EVIDENCE_SUMMARY_FIELD_ID,
            "evidence_summary": "Other football evidence retained" + chr(10)
                                + screenshot_evidence_summary_line(out),
        }
        verified = verify_football_assessment(out, readback)
        self.assertTrue(verified["football_pair_verified"])
        self.assertTrue(verified["screenshot_price_evidence_verified"])
        self.assertFalse(verified["actual_bet_created"])
        bad = dict(readback)
        bad["evidence_summary"] = bad["evidence_summary"].replace('"odds":1.7', '"odds":1.9')
        with self.assertRaisesRegex(XIAssessmentReadbackError, "screenshot quote"):
            verify_football_assessment(out, bad)
        missing = dict(readback)
        missing.pop("evidence_summary")
        with self.assertRaisesRegex(XIAssessmentReadbackError, "persisted screenshot price evidence missing"):
            verify_football_assessment(out, missing)

    def test_11_no_timestamp_or_current_flag_can_forge_executable(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        out = run_xi(c=c, shot=snapshot(c, captured=None,
                     open_offer_verified_in_screenshot=True), priced=True)
        self.assertFalse(out["price_check"]["bet_authorized"])

    def test_12_live_minute_mismatch_blocks_only_price(self):
        c, c2 = football("c"), football("c2")
        out = run_xi(c, c2, snapshot(c, match_minute=4))
        self.assertEqual(out["price_check"]["status"], "PRICE_CHECK_BLOCKED")
        self.assertEqual(set(out["results"]), {"c", "c2"})

    def test_13_true_same_instant_open_offer_runs_unchanged_strict_pair(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        out = run_xi(c=c, shot=snapshot(c, open_offer_verified_in_screenshot=True),
                     priced=True)
        self.assertEqual(out["xi_mode"], "FOOTBALL_AND_SCREENSHOT_PRICE_CHECK")
        self.assertTrue(out["price_check"]["ok"])
        self.assertEqual(out["price_check"]["receipt"]["engine_execution_status"],
                         "EXECUTED_C_C2_PAIR")
        self.assertFalse(out["model_bets_created"])


if __name__ == "__main__":
    unittest.main()
