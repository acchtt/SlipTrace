"""Observed screenshot quote uses canonical Football C policy only."""
from __future__ import annotations

import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

ENGINE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE))

from evidence_fixtures import attach_g4_evidence
from test_football_assessment_pair import football
from xi_assessment_reconcile import (
    STATUS_COLUMN,
    XIAssessmentReadbackError,
    verify_football_assessment,
)

CAPTURE = "2026-10-11T05:05:00+00:00"

EXCEPTION_RESEARCH_FIELDS = [
    "fixture_identity_status",
    "competition_format_incentive",
    "home_scoring_route",
    "away_scoring_route",
    "carrier_and_chance_creation",
    "availability_and_replacements",
    "failure_mechanisms",
    "completion_continuation_stall",
    "upper_tail_and_comparable_context",
    "h2h_materiality",
    "g4_research_if_g3_funded",
]


def exception_authority(
    c,
    *,
    reference="test-user-explicit-exception",
    upstream_state="NOT_RANKED",
    revision="INITIAL",
    supersedes_reference=None,
    supersedes_epoch=None,
    challenge_reason=None,
):
    research = {
        "fresh_research_completed": True,
        "market_independent": True,
        "research_epoch_id": c["evidence_epoch_id"],
        "researched_at_utc": c["context"]["assessment_at_utc"],
        "upstream_state": upstream_state,
        "source_reference": "test-source-surface",
        "evidence_refs": [
            "test-football-source-1",
            "test-football-source-2",
        ],
        "checked_fields": list(EXCEPTION_RESEARCH_FIELDS),
        "revision": revision,
    }
    if revision == "REASSESSMENT":
        research.update({
            "supersedes_exception_reference": supersedes_reference,
            "supersedes_evidence_epoch_id": supersedes_epoch,
            "challenge_reason": challenge_reason,
        })
    return {
        "mode": "EXCEPTION",
        "exception_reference": reference,
        "user_requested_exception": True,
        "exception_research": research,
    }


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


def complete_market_disagreement_recheck(payload, *, fields=None):
    payload["context"].update(
        market_disagreement_recheck_status="COMPLETED",
        market_disagreement_recheck_basis=(
            "Current football evidence was rechecked against the higher "
            "screenshot burden and the deterministic certificate was rerun."
        ),
        market_disagreement_recheck_fields=(
            fields
            if fields is not None
            else [
                "upper_tail_transferability",
                "upper_tail_comparable_context_signal",
            ]
        ),
        market_disagreement_recheck_evidence_refs=[
            "source-backed-current-football-recheck-1"
        ],
    )
    return payload


def wait_ready(payload, *, top=False):
    payload["match"].update(
        carrier="STRONG",
        carrier_self_fund=True,
        carrier_self_fund_basis=(
            "Strong current carrier independently funds the frozen protected burden."
        ),
        independent_upper_tail=True,
        independent_upper_tail_basis=(
            "Separate current non-market upper-tail route is verified."
        ),
    )
    payload["context"].update(
        thesis_state="PRESERVED",
        primary_mechanism_intact=True,
        material_veto=False,
        material_event_since_frozen="NONE_VERIFIED",
        wait_reachable=True,
        wait_reachability_basis=(
            "clean clock decay to the model's frozen burden is reachable "
            "without requiring a negative football event"
        ),
        wait_requires_negative_info=False,
        wait_negative_info_basis="no negative information required",
        top_ranked_focus=top,
    )
    return payload


def run_xi(c=None, shot=None, authority=None):
    c = c or football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
    shot = shot if shot is not None else snapshot(c)
    authority = authority or exception_authority(c)
    with tempfile.TemporaryDirectory() as td:
        root = pathlib.Path(td)
        cp = root / "c.json"
        sp = root / "shot.json"
        ap = root / "authority.json"
        cp.write_text(json.dumps(c), encoding="utf-8")
        sp.write_text(json.dumps(shot), encoding="utf-8")
        ap.write_text(json.dumps(authority), encoding="utf-8")
        proc = subprocess.run(
            [
                sys.executable,
                str(ENGINE / "xi_portable.py"),
                "xi",
                "--c",
                str(cp),
                "--screenshot-quote",
                str(sp),
                "--authority",
                str(ap),
            ],
            text=True,
            capture_output=True,
            timeout=30,
            check=False,
        )
        if proc.returncode:
            raise AssertionError(proc.stderr)
        return json.loads(proc.stdout)


class ScreenshotOnlyXIRegression(unittest.TestCase):
    def test_direct_xi_without_authority_fails_closed(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        shot = snapshot(c)
        with tempfile.TemporaryDirectory() as td:
            root = pathlib.Path(td)
            cp, sp = root / "c.json", root / "shot.json"
            cp.write_text(json.dumps(c), encoding="utf-8")
            sp.write_text(json.dumps(shot), encoding="utf-8")
            proc = subprocess.run(
                [
                    sys.executable,
                    str(ENGINE / "xi_portable.py"),
                    "xi",
                    "--c",
                    str(cp),
                    "--screenshot-quote",
                    str(sp),
                ],
                text=True,
                capture_output=True,
                timeout=30,
                check=False,
            )
            self.assertNotEqual(proc.returncode, 0)
            payload = json.loads(proc.stderr)
            self.assertEqual(payload["status"], "RANK_RECEIPT_REQUIRED")
            self.assertEqual(payload["failure_class"], "RANK_AUTHORITY")

    def test_exact_screenshot_quote_is_preserved(self):
        out = run_xi()
        self.assertEqual(out["xi_mode"], "FOOTBALL_AND_OBSERVED_QUOTE")
        price = out["price_check"]
        self.assertTrue(price["ok"])
        self.assertEqual(price["status"], "OBSERVED_QUOTE_EVALUATED")
        self.assertEqual(price["evidence"]["quote"], {"line": 2.5, "odds": 1.7})
        self.assertEqual(
            price["evidence"]["capture_reference"],
            "user-attachment-screenshot-1",
        )
        self.assertFalse(price["execution_authorized"])
        self.assertFalse(price["bet_authorized"])
        self.assertIn("model", price)
        self.assertNotIn("models", price)

    def test_credible_tail_profile_is_invariant_to_screenshot_line(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        low = run_xi(c, snapshot(c, line=2.5, odds=1.70))
        high = run_xi(c, snapshot(c, line=4.0, odds=2.00))
        fields = (
            "credible_tail_state",
            "credible_tail_target_goal",
            "credible_burden_band_low",
            "credible_burden_band_high",
            "credible_tail_basis",
        )
        for field in fields:
            self.assertEqual(low["result"][field], high["result"][field])
        self.assertTrue(low["result"]["credible_tail_market_independent"])
        self.assertFalse(low["result"]["credible_tail_execution_authority"])

    def test_no_external_or_replacement_quote(self):
        out = run_xi()
        evidence = out["price_check"]["evidence"]
        self.assertEqual(evidence["external_price_searches"], 0)
        self.assertEqual(evidence["replacement_quotes"], 0)
        self.assertFalse(out["price_check"]["quote_research_required"])

    def test_missing_capture_time_is_not_retimed(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        out = run_xi(c=c, shot=snapshot(c, captured=None))
        price = out["price_check"]
        self.assertIsNone(price["evidence"]["observed_at_utc"])
        self.assertIsNone(price["evidence"]["observation_age_seconds"])
        self.assertIn("SCREENSHOT_CAPTURE_TIME_UNKNOWN", price["limitations"])

    def test_live_screenshot_never_recreates_prematch_action(self):
        c = football("c")
        out = run_xi(c, snapshot(c))
        price = out["price_check"]
        self.assertEqual(price["evidence"]["score"], "1-0")
        self.assertEqual(price["evidence"]["match_minute"], 5)
        self.assertEqual(
            price["model"]["conditional_action"],
            "LIVE_PRICE_BURDEN_COMPARISON_ONLY",
        )
        self.assertFalse(price["execution_authorized"])

    def test_invalid_screenshot_blocks_price_only_not_football(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        out = run_xi(c=c, shot=snapshot(c, match_id="wrong-id"))
        self.assertEqual(out["xi_mode"], "FOOTBALL_ASSESSMENT")
        self.assertEqual(out["price_check"]["status"], "OBSERVED_QUOTE_INVALID")
        self.assertEqual(
            out["engine_execution_status"],
            "EXECUTED_C_FOOTBALL_ONLY",
        )
        self.assertEqual(out["model"], "c")
        self.assertEqual(out["result"]["model"], "c")

    def test_material_gap_cannot_wait_for_far_lower_certificate(self):
        c = complete_market_disagreement_recheck(
            wait_ready(
                football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
            )
        )
        out = run_xi(c, snapshot(c, line=5.0, odds=1.72))
        verdict = out["price_check"]["model"]
        self.assertEqual(verdict["conditional_action"], "PASS")
        self.assertIsNone(verdict["wait_target_line"])
        self.assertIn("more than 0.25", verdict["reason"])
        self.assertTrue(verdict["wait_reachable"])

    def test_one_step_unsupported_line_becomes_book_target_when_evidenced(self):
        c = complete_market_disagreement_recheck(
            wait_ready(
                football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
            )
        )
        # This fixture compiles O3.5; O3.75 is one quarter-goal step above it.
        out = run_xi(c, snapshot(c, line=3.75, odds=1.72))
        verdict = out["price_check"]["model"]
        self.assertEqual(verdict["conditional_action"], "BOOK")
        self.assertEqual(verdict["book_target_line"], 3.5)
        self.assertTrue(verdict["book_target_state"] == "BOOK_TARGET_AVAILABLE")
        self.assertIsNone(verdict["wait_target_line"])

    def test_material_market_disagreement_blocks_until_rechecked(self):
        c = wait_ready(
            football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        )
        first = run_xi(c, snapshot(c, line=5.0, odds=1.72))
        price = first["price_check"]
        self.assertEqual(price["status"], "MARKET_DISAGREEMENT_RECHECK_REQUIRED")
        self.assertTrue(price["quote_research_required"])
        self.assertEqual(
            price["model"]["conditional_action"],
            "MARKET_DISAGREEMENT_RECHECK_REQUIRED",
        )
        self.assertFalse(price["model"]["market_disagreement_recheck_completed"])

        complete_market_disagreement_recheck(c)
        second = run_xi(c, snapshot(c, line=5.0, odds=1.72))
        self.assertEqual(second["price_check"]["status"], "OBSERVED_QUOTE_EVALUATED")
        self.assertFalse(second["price_check"]["quote_research_required"])
        self.assertTrue(
            second["price_check"]["model"]["market_disagreement_recheck_completed"]
        )
        self.assertIn(
            second["price_check"]["model"]["conditional_action"],
            {"ACT", "BOOK", "PASS"},
        )

    def test_incomplete_frozen_g4_marks_certificate_completeness_recheck(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        c["match"]["carrier_self_fund"] = True
        c["match"]["carrier_self_fund_basis"] = (
            "The current carrier independently funds goal three."
        )
        c["match"]["independent_upper_tail"] = False
        c["match"]["independent_upper_tail_basis"] = (
            "Frozen rank funded G3 but did not complete the fourth-goal investigation."
        )
        c["context"]["frozen_board_certified_burden"] = 2.5
        c["context"]["frozen_board_g4_research_status"] = "G4_RESEARCH_INCOMPLETE"
        out = run_xi(c, snapshot(c, line=3.25, odds=1.72))
        price = out["price_check"]
        self.assertEqual(price["status"], "MARKET_DISAGREEMENT_RECHECK_REQUIRED")
        self.assertTrue(
            price["model"]["certificate_completeness_recheck_required"]
        )
        self.assertEqual(
            price["model"]["frozen_board_g4_research_status"],
            "G4_RESEARCH_INCOMPLETE",
        )

    def test_complete_rejected_g4_disagreement_requires_independent_reclassification_recheck(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        c["match"].update(
            carrier_self_fund=True,
            carrier_self_fund_basis=(
                "Frozen carrier independently funds G3 but no transferable "
                "upper-tail route was accepted at rank."
            ),
            independent_upper_tail=False,
            independent_upper_tail_basis=(
                "Frozen rank rejected the independent fourth-goal tail."
            ),
            g4_research_status="G4_RESEARCH_COMPLETE_REJECTED",
            g4_carrier_path="FAILED",
            g4_distributed_path="FAILED",
            g4_reply_path="FAILED",
            g4_continuation_after_g3="MEDIUM",
            g4_research_basis=(
                "Frozen rank completed the G4 review and rejected the fourth goal."
            ),
        )
        c["context"].update(
            frozen_board_certified_burden=2.5,
            frozen_board_g4_research_status="G4_RESEARCH_COMPLETE_REJECTED",
        )
        out = run_xi(c, snapshot(c, line=3.25, odds=1.72))
        price = out["price_check"]
        self.assertEqual(price["status"], "MARKET_DISAGREEMENT_RECHECK_REQUIRED")
        self.assertTrue(
            price["model"]["prior_certificate_reclassification_recheck_required"]
        )

    def test_complete_rejected_g4_can_be_corrected_after_source_backed_reclassification(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        c["match"].update(
            carrier_self_fund=True,
            carrier_self_fund_basis=(
                "Frozen carrier independently funds G3 but no transferable "
                "upper-tail route was accepted at rank."
            ),
            independent_upper_tail=False,
            independent_upper_tail_basis=(
                "Frozen rank rejected the independent fourth-goal tail."
            ),
            g4_research_status="G4_RESEARCH_COMPLETE_REJECTED",
            g4_carrier_path="FAILED",
            g4_distributed_path="FAILED",
            g4_reply_path="FAILED",
            g4_continuation_after_g3="MEDIUM",
            g4_research_basis=(
                "Frozen rank completed the G4 review and rejected the fourth goal."
            ),
        )
        c["context"].update(
            frozen_board_certified_burden=2.5,
            frozen_board_g4_research_status="G4_RESEARCH_COMPLETE_REJECTED",
        )

        # The market triggers the recheck, but the upgrade comes from a
        # source-backed football correction of the prior certificate.
        c = wait_ready(c)
        c["match"].update(
            g4_research_status="G4_RESEARCH_COMPLETE_FUNDED",
            g4_carrier_path="SUPPORTED",
            g4_distributed_path="FAILED",
            g4_reply_path="SUPPORTED",
            g4_continuation_after_g3="MEDIUM",
            g4_research_basis=(
                "Independent recheck found the same prospective football evidence "
                "had been underweighted at rank; the carrier/reply G4 path is funded."
            ),
        )
        complete_market_disagreement_recheck(
            c,
            fields=[
                "g4_carrier_path",
                "g4_reply_path",
                "g4_continuation_after_g3",
                "upper_tail_transferability",
                "upper_tail_comparable_context_signal",
            ],
        )
        c["context"].update(
            certificate_upgrade_status="VERIFIED_PRIOR_CERTIFICATE_MISCLASSIFICATION",
            certificate_upgrade_basis=(
                "Independent source-backed recheck corrected the prior rank "
                "classification; the bookmaker line did not create the certificate."
            ),
            certificate_upgrade_new_evidence_fields=[
                "g4_carrier_path",
                "g4_reply_path",
                "upper_tail_transferability",
                "upper_tail_comparable_context_signal",
            ],
        )
        attach_g4_evidence(c["match"])
        out = run_xi(c, snapshot(c, line=3.5, odds=1.72))
        price = out["price_check"]
        self.assertEqual(price["status"], "OBSERVED_QUOTE_EVALUATED")
        self.assertEqual(price["model"]["supported_line"], 3.5)
        self.assertFalse(price["model"]["prior_certificate_reclassification_recheck_required"])
        self.assertIn(
            price["model"]["conditional_action"],
            {"ACT", "WAIT", "PASS"},
        )

    def test_prior_misclassification_upgrade_requires_completed_source_backed_recheck(self):
        c = wait_ready(
            football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        )
        c["match"].update(
            g4_research_status="G4_RESEARCH_COMPLETE_FUNDED",
            g4_carrier_path="SUPPORTED",
            g4_distributed_path="FAILED",
            g4_reply_path="SUPPORTED",
            g4_continuation_after_g3="MEDIUM",
            g4_research_basis="Current deterministic football recheck funds G4.",
        )
        c["context"].update(
            frozen_board_certified_burden=2.5,
            frozen_board_g4_research_status="G4_RESEARCH_COMPLETE_REJECTED",
            certificate_upgrade_status="VERIFIED_PRIOR_CERTIFICATE_MISCLASSIFICATION",
            certificate_upgrade_basis=(
                "Claimed prior misclassification without completed disagreement recheck."
            ),
            certificate_upgrade_new_evidence_fields=["g4_carrier_path"],
        )
        out = run_xi(c, snapshot(c, line=3.5, odds=1.72))
        self.assertEqual(
            out["price_check"]["status"],
            "OBSERVED_QUOTE_INVALID",
        )
        self.assertIn(
            "PRIOR CERTIFICATE RECLASSIFICATION BLOCKED",
            out["price_check"]["reason"],
        )

    def test_g4_disagreement_requires_upper_tail_and_comparable_context_fields(self):
        c = complete_market_disagreement_recheck(
            wait_ready(
                football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
            ),
            fields=["upper_tail_transferability"],
        )
        out = run_xi(c, snapshot(c, line=5.0, odds=1.72))
        price = out["price_check"]
        self.assertEqual(price["status"], "MARKET_DISAGREEMENT_RECHECK_REQUIRED")
        self.assertIn(
            "upper_tail_comparable_context_signal",
            price["model"]["market_disagreement_recheck_missing_fields"],
        )

    def test_quarter_goal_disagreement_does_not_trigger_material_recheck(self):
        c = wait_ready(
            football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        )
        baseline = run_xi(c, snapshot(c, line=2.5, odds=1.70))
        supported = baseline["price_check"]["model"]["supported_line"]
        self.assertIsNotNone(supported)
        out = run_xi(c, snapshot(c, line=supported + 0.25, odds=1.70))
        self.assertEqual(out["price_check"]["status"], "OBSERVED_QUOTE_EVALUATED")
        self.assertFalse(out["price_check"]["quote_research_required"])

    def test_unestablished_wait_is_not_invented(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        out = run_xi(c, snapshot(c, line=3.25, odds=1.72))
        self.assertNotEqual(
            out["price_check"]["model"]["conditional_action"],
            "WAIT",
        )

    def test_observed_quote_persists_in_normal_line_odds_fields(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        out = run_xi(c=c, shot=snapshot(c, line=2.75, odds=1.71))
        readback = {
            "spreadsheet_id": "1ojWKj5aT3VEJUyX3NSbAOZNTaUM0Mb8I8e4lvFy7kGM",
            "sheet_name": "Decision States",
            "row_key": "XI-SCREENSHOT-EXAMPLE",
            "assessment_id": "XI-SCREENSHOT-EXAMPLE",
            "match_id": out["result"]["match_id"],
            "readback_method": "INDEPENDENT_GOOGLE_SHEETS_REFETCH",
            "xi_status_column": STATUS_COLUMN,
            "xi_assessment_execution_status":
                "EXECUTED_C_FOOTBALL_AND_PRICE",
            "engine_c_result": out["result"],
            "evaluated_line": 2.75,
            "evaluated_odds": 1.71,
        }
        verified = verify_football_assessment(out, readback)
        self.assertTrue(verified["football_c_verified"])
        self.assertTrue(verified["observed_quote_readback_verified"])
        self.assertFalse(verified["actual_bet_created"])

        bad = dict(readback)
        bad["evaluated_odds"] = 1.91
        with self.assertRaisesRegex(
            XIAssessmentReadbackError,
            "evaluated line/odds",
        ):
            verify_football_assessment(out, bad)


if __name__ == "__main__":
    unittest.main()
