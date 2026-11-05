from __future__ import annotations

import json
import pathlib
import tempfile
import unittest

ENGINE = pathlib.Path(__file__).resolve().parents[1]
import sys
sys.path.insert(0, str(ENGINE))

import xi_runtime_backend
from block_runtime import run_block
from xi_authority import _engine_policy_fingerprint
from tests.test_xi_user_screenshot_only import (
    assessment_depth,
    exception_authority,
    football,
    snapshot,
)


def direct_authority(c, reference="test-user-direct-xi"):
    authority = exception_authority(c, reference=reference)
    authority["mode"] = "DIRECT"
    authority["direct_reference"] = reference
    authority["user_requested_direct_xi"] = True
    authority.pop("exception_reference", None)
    authority.pop("user_requested_exception", None)
    return authority


def block_ready_football():
    c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
    c["context"]["assessment_at_utc"] = "2026-11-04T10:00:00+00:00"
    c["evidence_epoch_id"] = "BLOCK-XI-EPOCH-1"
    c["assessment_depth"] = assessment_depth(c)
    c["assessment_depth"]["contract"] = "ASSESSMENT_DEPTH_V2"
    c["assessment_depth"]["evidence_epoch_id"] = c["evidence_epoch_id"]
    c["assessment_depth"]["assessed_at_utc"] = c["context"]["assessment_at_utc"]
    refs = list(c["assessment_depth"]["evidence_refs"])
    c["match"].update(
        activation_quality="HIGH",
        activation_basis=(
            "Current attack availability and opponent opening patterns support "
            "fast activation from frozen prematch football evidence."
        ),
        activation_evidence_refs=refs,
    )
    other = dict(c["match"])
    other["match_id"] = "block-xi-control"
    other["activation_quality"] = "MEDIUM"
    request = {
        "schema_version": "football-block-runtime-v1",
        "model": "c",
        "matches": [dict(c["match"]), other],
        "evidence_epochs": {
            c["match"]["match_id"]: c["evidence_epoch_id"],
            other["match_id"]: "BLOCK-XI-CONTROL-EPOCH",
        },
    }
    result = run_block(request)
    authority = {
        "mode": "BLOCK",
        "match_id": c["match"]["match_id"],
        "verified_block_package": {
            "request": request,
            "result": result,
        },
        "material_evidence_updates": [],
    }
    return c, authority


class XIRuntimeBackendTests(unittest.TestCase):
    def test_direct_xi_executes_without_block_or_rank_receipt(self):
        c, _ = block_ready_football()
        result = xi_runtime_backend.execute({
            "schema_version": xi_runtime_backend.REQUEST_SCHEMA,
            "request_id": "XI-test-direct-authority",
            "c_football": c,
            "authority": direct_authority(c),
            "screenshot_quote": snapshot(c, captured=None),
        })
        self.assertTrue(result["ok"], result)
        self.assertEqual(result["authority"]["mode"], "DIRECT")
        self.assertTrue(result["authority"]["user_requested_direct_xi"])
        self.assertEqual(result["authority"]["rank_state_display"], "DIRECT")

    def test_direct_xi_requires_explicit_exact_user_request_flag(self):
        c, _ = block_ready_football()
        authority = direct_authority(c)
        authority.pop("user_requested_direct_xi")
        result = xi_runtime_backend.execute({
            "schema_version": xi_runtime_backend.REQUEST_SCHEMA,
            "request_id": "XI-test-direct-missing-flag",
            "c_football": c,
            "authority": authority,
            "screenshot_quote": snapshot(c, captured=None),
        })
        self.assertFalse(result["ok"])
        self.assertEqual(result["status"], "XI_AUTHORITY_REQUIRED")
        self.assertEqual(result["failure_class"], "XI_AUTHORITY")

    def test_block_authority_executes_without_rank_receipt(self):
        c, authority = block_ready_football()
        result = xi_runtime_backend.execute({
            "schema_version": xi_runtime_backend.REQUEST_SCHEMA,
            "request_id": "XI-test-block-authority",
            "c_football": c,
            "authority": authority,
            "screenshot_quote": snapshot(c, captured=None),
        })
        self.assertTrue(result["ok"], result)
        self.assertEqual(result["authority"]["mode"], "BLOCK")
        self.assertEqual(
            result["authority"]["block_priority_policy"],
            "BLOCK_PRIORITY_V1",
        )
        self.assertFalse(
            result["authority"]["global_rank_is_selection_authority"]
        )

    def test_block_authority_rejects_tampered_persisted_request(self):
        c, authority = block_ready_football()
        authority["verified_block_package"]["request"]["matches"][0][
            "chance_quality"
        ] = "LOW"
        result = xi_runtime_backend.execute({
            "schema_version": xi_runtime_backend.REQUEST_SCHEMA,
            "request_id": "XI-test-block-tamper",
            "c_football": c,
            "authority": authority,
            "screenshot_quote": snapshot(c, captured=None),
        })
        self.assertFalse(result["ok"])
        self.assertEqual(result["status"], "BLOCK_RECEIPT_REQUIRED")
        self.assertEqual(result["failure_class"], "BLOCK_AUTHORITY")

    def test_block_authority_allows_declared_current_football_update(self):
        c, authority = block_ready_football()
        c["match"]["chance_quality"] = "MEDIUM"
        authority["material_evidence_updates"] = ["chance_quality"]
        result = xi_runtime_backend.execute({
            "schema_version": xi_runtime_backend.REQUEST_SCHEMA,
            "request_id": "XI-test-block-current-update",
            "c_football": c,
            "authority": authority,
            "screenshot_quote": snapshot(c, captured=None),
        })
        self.assertTrue(result["ok"], result)
        self.assertEqual(
            result["authority"]["material_evidence_updates"],
            ["chance_quality"],
        )

    def test_block_authority_cannot_rewrite_activation_selection_evidence(self):
        c, authority = block_ready_football()
        c["match"]["activation_quality"] = "LOW"
        authority["material_evidence_updates"] = ["activation_quality"]
        result = xi_runtime_backend.execute({
            "schema_version": xi_runtime_backend.REQUEST_SCHEMA,
            "request_id": "XI-test-block-activation-rewrite",
            "c_football": c,
            "authority": authority,
            "screenshot_quote": snapshot(c, captured=None),
        })
        self.assertFalse(result["ok"])
        self.assertEqual(result["status"], "BLOCK_RECEIPT_REQUIRED")
        self.assertIn("authority-owned fields", result["error"])

    def test_on_demand_screenshot_executes_shared_runtime(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        request = {
            "schema_version": xi_runtime_backend.REQUEST_SCHEMA,
            "request_id": "XI-test-1",
            "c_football": c,
            "authority": exception_authority(c, reference="test-user-exception"),
            "screenshot_quote": snapshot(c),
        }
        result = xi_runtime_backend.execute(request)
        self.assertTrue(result["ok"])
        self.assertEqual(
            result["runtime"]["engine_execution_status"],
            "EXECUTED_C_FOOTBALL_ONLY",
        )
        self.assertEqual(
            result["runtime"]["price_check"]["status"],
            "OBSERVED_QUOTE_EVALUATED",
        )
        handoff = result["sheets_handoff"]
        self.assertTrue(handoff["required_before_user_verdict"])
        self.assertEqual(
            handoff["status"],
            "DECISION_STATE_PERSISTENCE_READBACK_REQUIRED",
        )
        self.assertEqual(handoff["sheet_name"], "Decision States")
        self.assertEqual(handoff["key_column"], "Assessment ID")
        self.assertEqual(
            handoff["assessment_id"],
            result["runtime"]["decision_state_persistence"]["row"]["Assessment ID"],
        )
        self.assertTrue(handoff["github_runtime_result_is_not_sheets_persistence"])
        self.assertIn(
            "INDEPENDENT_GOOGLE_SHEETS_REFETCH",
            handoff["orchestrator_required_actions"],
        )

    def test_contract_error_is_persisted_not_analysis_only(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        bad = snapshot(c)
        bad["match_id"] = "wrong"
        request = {
            "schema_version": xi_runtime_backend.REQUEST_SCHEMA,
            "request_id": "XI-test-2",
            "c_football": c,
            "authority": exception_authority(c, reference="test-user-exception"),
            "screenshot_quote": bad,
        }
        result = xi_runtime_backend.execute(request)
        # xi_portable preserves football assessment and marks only the observed
        # quote invalid, which is still a real runtime result.
        self.assertTrue(result["ok"])
        self.assertEqual(
            result["runtime"]["price_check"]["status"],
            "OBSERVED_QUOTE_INVALID",
        )

    def test_exception_authority_requires_explicit_user_request(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        result = xi_runtime_backend.execute({
            "schema_version": xi_runtime_backend.REQUEST_SCHEMA,
            "request_id": "XI-test-implicit-exception",
            "c_football": c,
            "authority": {
                "mode": "EXCEPTION",
                "exception_reference": "automatic-fallback-is-forbidden",
            },
            "screenshot_quote": snapshot(c),
        })
        self.assertFalse(result["ok"])
        self.assertEqual(result["status"], "RANK_RECEIPT_REQUIRED")
        self.assertIn("explicit user /xi exception request", result["error"])

    def test_exception_requires_fresh_full_research_proof(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        result = xi_runtime_backend.execute({
            "schema_version": xi_runtime_backend.REQUEST_SCHEMA,
            "request_id": "XI-test-thin-exception",
            "c_football": c,
            "authority": {
                "mode": "EXCEPTION",
                "exception_reference": "thin-exception",
                "user_requested_exception": True,
            },
            "screenshot_quote": snapshot(c),
        })
        self.assertFalse(result["ok"])
        self.assertIn("EXCEPTION_RESEARCH_REQUIRED", result["error"])

    def test_challenged_exception_cannot_reuse_same_evidence_epoch(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        authority = exception_authority(
            c,
            reference="exception-v2",
            revision="REASSESSMENT",
            supersedes_reference="exception-v1",
            supersedes_epoch=c["evidence_epoch_id"],
            challenge_reason="user challenged the first assessment as incomplete",
        )
        result = xi_runtime_backend.execute({
            "schema_version": xi_runtime_backend.REQUEST_SCHEMA,
            "request_id": "XI-test-reused-exception-epoch",
            "c_football": c,
            "authority": authority,
            "screenshot_quote": snapshot(c),
        })
        self.assertFalse(result["ok"])
        self.assertIn("new evidence epoch", result["error"])

    def test_watch_to_focus_exception_requires_explicit_state_change_evidence(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        authority = exception_authority(
            c,
            reference="watch-to-focus-without-proof",
            upstream_state="WATCH",
        )
        result = xi_runtime_backend.execute({
            "schema_version": xi_runtime_backend.REQUEST_SCHEMA,
            "request_id": "XI-test-watch-focus-proof",
            "c_football": c,
            "authority": authority,
            "screenshot_quote": snapshot(c),
        })
        self.assertFalse(result["ok"])
        self.assertIn("WATCH/PASS -> FOCUS", result["error"])

    def test_cartagines_olimpia_challenge_requires_new_full_exception_epoch(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        c["match"]["match_id"] = "1894831"
        c["evidence_epoch_id"] = "cartagines-olimpia-exception-v1"
        first = xi_runtime_backend.execute({
            "schema_version": xi_runtime_backend.REQUEST_SCHEMA,
            "request_id": "XI-cartagines-olimpia-thin-v1",
            "c_football": c,
            "authority": {
                "mode": "EXCEPTION",
                "exception_reference": "cartagines-olimpia-v1",
                "user_requested_exception": True,
            },
            "screenshot_quote": snapshot(c),
        })
        self.assertFalse(first["ok"])
        self.assertEqual(first["status"], "EXCEPTION_RESEARCH_REQUIRED")

        c2 = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        c2["match"]["match_id"] = "1894831"
        c2["evidence_epoch_id"] = "cartagines-olimpia-exception-v2"
        c2["context"]["assessment_at_utc"] = "2026-10-22T02:34:07+00:00"
        authority = exception_authority(
            c2,
            reference="cartagines-olimpia-v2",
            upstream_state="UNVERIFIED",
            revision="REASSESSMENT",
            supersedes_reference="cartagines-olimpia-v1",
            supersedes_epoch="cartagines-olimpia-exception-v1",
            challenge_reason="user flagged the first exception assessment as half-baked",
        )
        second = xi_runtime_backend.execute({
            "schema_version": xi_runtime_backend.REQUEST_SCHEMA,
            "request_id": "XI-cartagines-olimpia-research-v2",
            "c_football": c2,
            "authority": authority,
            "screenshot_quote": snapshot(c2, captured=None),
        })
        self.assertTrue(second["ok"])
        trace = second["authority"]["exception_research"]
        self.assertEqual(trace["revision"], "REASSESSMENT")
        self.assertEqual(
            trace["supersedes_evidence_epoch_id"],
            "cartagines-olimpia-exception-v1",
        )
        self.assertEqual(trace["upstream_state"], "UNVERIFIED")

    def test_post_activation_assessment_requires_substantive_depth_manifest(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        c["context"]["assessment_at_utc"] = "2026-11-02T01:46:00+00:00"
        result = xi_runtime_backend.execute({
            "schema_version": xi_runtime_backend.REQUEST_SCHEMA,
            "request_id": "XI-test-depth-missing",
            "c_football": c,
            "authority": exception_authority(c, reference="depth-missing"),
            "screenshot_quote": snapshot(c, captured=None),
        })
        self.assertFalse(result["ok"])
        self.assertEqual(result["status"], "ASSESSMENT_RESEARCH_INCOMPLETE")
        self.assertEqual(result["failure_class"], "ASSESSMENT_DEPTH")

    def test_post_activation_assessment_rejects_checked_only_endpoint_label(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        c["context"]["assessment_at_utc"] = "2026-11-02T01:46:00+00:00"
        c["assessment_depth"] = assessment_depth(c)
        c["assessment_depth"]["checks"]["stall_1_1"] = "CHECKED"
        result = xi_runtime_backend.execute({
            "schema_version": xi_runtime_backend.REQUEST_SCHEMA,
            "request_id": "XI-test-depth-thin-endpoint",
            "c_football": c,
            "authority": exception_authority(c, reference="depth-thin"),
            "screenshot_quote": snapshot(c, captured=None),
        })
        self.assertFalse(result["ok"])
        self.assertEqual(result["status"], "ASSESSMENT_RESEARCH_INCOMPLETE")
        self.assertIn("stall_1_1", result["error"])

    def test_post_activation_substantive_assessment_depth_executes(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        c["context"]["assessment_at_utc"] = "2026-11-02T01:46:00+00:00"
        c["assessment_depth"] = assessment_depth(c)
        result = xi_runtime_backend.execute({
            "schema_version": xi_runtime_backend.REQUEST_SCHEMA,
            "request_id": "XI-test-depth-complete",
            "c_football": c,
            "authority": exception_authority(c, reference="depth-complete"),
            "screenshot_quote": snapshot(c, captured=None),
        })
        self.assertTrue(result["ok"], result)
        self.assertEqual(result["authority"]["assessment_depth"]["contract"], "ASSESSMENT_DEPTH_V1")
        self.assertEqual(result["authority"]["assessment_depth"]["evidence_ref_count"], 2)

    def test_request_envelope_filename_must_match_id(self):
        with tempfile.TemporaryDirectory() as td:
            root = pathlib.Path(td)
            c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
            req = root / "different.json"
            out = root / "result.json"
            req.write_text(json.dumps({
                "schema_version": xi_runtime_backend.REQUEST_SCHEMA,
                "request_id": "XI-test-3",
                "c_football": c,
                "authority": {"mode": "EXCEPTION", "exception_reference": "test-user-exception", "user_requested_exception": True},
            }))
            self.assertEqual(xi_runtime_backend.run(req, out), 0)
            result = json.loads(out.read_text())
            self.assertFalse(result["ok"])
            self.assertEqual(result["failure_class"], "REQUEST_ENVELOPE")

    def test_xi_without_any_authority_fails_closed(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        result = xi_runtime_backend.execute({
            "schema_version": xi_runtime_backend.REQUEST_SCHEMA,
            "request_id": "XI-test-no-authority",
            "c_football": c,
            "screenshot_quote": snapshot(c),
        })
        self.assertFalse(result["ok"])
        self.assertEqual(result["status"], "XI_AUTHORITY_REQUIRED")

    def test_post_activation_assessment_requires_locked_rank_receipt(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        c["context"]["assessment_at_utc"] = "2026-10-24T18:01:00+00:00"
        frozen = dict(c["match"])
        package = {
            "status": "V4_RANK_PERSISTENCE_VERIFIED",
            "native_rank": {
                "run_id": "V4-test-legacy-unlocked",
                "integrity_sha256": "legacy-unlocked-hash",
                "board": {"matches": [{
                    "match_id": frozen["match_id"],
                    "rank": 1,
                    "board_state": "FOCUS",
                    "follow_lane": "FOLLOW",
                    "supported_line": 2.5,
                }]},
                "frozen_model_input": {"matches": [frozen]},
            },
        }
        result = xi_runtime_backend.execute({
            "schema_version": xi_runtime_backend.REQUEST_SCHEMA,
            "request_id": "XI-test-legacy-unlocked-after-activation",
            "c_football": c,
            "authority": {
                "mode": "RANKED",
                "match_id": frozen["match_id"],
                "verified_rank_package": package,
                "material_evidence_updates": [],
            },
        })
        self.assertFalse(result["ok"])
        self.assertEqual(result["status"], "RANK_POLICY_LOCK_REQUIRED")
        self.assertIn("rerank/reseal", result["error"])

    def test_ranked_policy_fingerprint_drift_fails_closed(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        frozen = dict(c["match"])
        package = {
            "status": "V4_RANK_PERSISTENCE_VERIFIED",
            "native_rank": {
                "run_id": "V4-test-policy-drift",
                "integrity_sha256": "sealed-policy-drift-hash",
                "engine_policy_lock": "SLATE_PINNED_V1",
                "engine_policy_fingerprint": "not-the-current-policy",
                "board": {"matches": [{
                    "match_id": frozen["match_id"],
                    "rank": 1,
                    "board_state": "FOCUS",
                    "follow_lane": "FOLLOW",
                    "supported_line": 2.5,
                }]},
                "frozen_model_input": {"matches": [frozen]},
            },
        }
        result = xi_runtime_backend.execute({
            "schema_version": xi_runtime_backend.REQUEST_SCHEMA,
            "request_id": "XI-test-policy-drift",
            "c_football": c,
            "authority": {
                "mode": "RANKED",
                "match_id": frozen["match_id"],
                "verified_rank_package": package,
                "material_evidence_updates": [],
            },
        })
        self.assertFalse(result["ok"])
        self.assertEqual(result["status"], "RANK_ENGINE_POLICY_DRIFT")
        self.assertIn("differs from the revision", result["error"])

    def test_ranked_matching_policy_fingerprint_executes(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        frozen = dict(c["match"])
        fingerprint = _engine_policy_fingerprint()
        package = {
            "status": "V4_RANK_PERSISTENCE_VERIFIED",
            "native_rank": {
                "run_id": "V4-test-policy-match",
                "integrity_sha256": "sealed-policy-match-hash",
                "engine_policy_lock": "SLATE_PINNED_V1",
                "engine_policy_fingerprint": fingerprint,
                "board": {"matches": [{
                    "match_id": frozen["match_id"],
                    "rank": 1,
                    "board_state": "FOCUS",
                    "follow_lane": "FOLLOW",
                    "supported_line": 2.5,
                }]},
                "frozen_model_input": {"matches": [frozen]},
            },
        }
        result = xi_runtime_backend.execute({
            "schema_version": xi_runtime_backend.REQUEST_SCHEMA,
            "request_id": "XI-test-policy-match",
            "c_football": c,
            "authority": {
                "mode": "RANKED",
                "match_id": frozen["match_id"],
                "verified_rank_package": package,
                "material_evidence_updates": [],
            },
        })
        self.assertTrue(result["ok"], result)

    def test_ranked_fixture_cannot_override_context_board_state(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        frozen = dict(c["match"])
        package = {
            "status": "V4_RANK_PERSISTENCE_VERIFIED",
            "native_rank": {
                "run_id": "V4-test-rank-context",
                "integrity_sha256": "sealed-context-hash",
                "board": {"matches": [{
                    "match_id": frozen["match_id"],
                    "rank": 1,
                    "board_state": "FOCUS",
                    "follow_lane": "FOLLOW",
                    "supported_line": 2.5,
                }]},
                "frozen_model_input": {"matches": [frozen]},
            },
        }
        c["context"]["board_state"] = "C-WATCH"
        result = xi_runtime_backend.execute({
            "schema_version": xi_runtime_backend.REQUEST_SCHEMA,
            "request_id": "XI-test-context-override",
            "c_football": c,
            "authority": {
                "mode": "RANKED",
                "match_id": frozen["match_id"],
                "verified_rank_package": package,
                "material_evidence_updates": [],
            },
        })
        self.assertFalse(result["ok"])
        self.assertEqual(result["status"], "RANK_RECEIPT_REQUIRED")
        self.assertIn("context board_state conflicts", result["error"])

    def test_ranked_fixture_cannot_silently_override_frozen_c_evidence(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        frozen = dict(c["match"])
        package = {
            "status": "V4_RANK_PERSISTENCE_VERIFIED",
            "native_rank": {
                "run_id": "V4-test-rank",
                "integrity_sha256": "sealed-test-hash",
                "board": {"matches": [{
                    "match_id": frozen["match_id"],
                    "board_state": "FOCUS", "follow_lane": "FOLLOW", "supported_line": 2.5,
                }]},
                "frozen_model_input": {"matches": [frozen]},
            },
        }
        c["match"]["board_state"] = "C-WATCH"
        result = xi_runtime_backend.execute({
            "schema_version": xi_runtime_backend.REQUEST_SCHEMA,
            "request_id": "XI-test-ranked-override",
            "c_football": c,
            "authority": {
                "mode": "RANKED", "match_id": frozen["match_id"],
                "verified_rank_package": package,
                "material_evidence_updates": [],
            },
        })
        self.assertFalse(result["ok"])
        self.assertEqual(result["status"], "RANK_RECEIPT_REQUIRED")
        self.assertIn("undeclared override", result["error"])


if __name__ == "__main__":
    unittest.main()
