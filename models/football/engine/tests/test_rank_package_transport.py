import hashlib
import json
import unittest

from rank_package_transport import RankTransportError, build_capsule


def artifact_bytes():
    rank = {
        "schema_version": "football-stages-v4",
        "run_id": "V4-TEST",
        "integrity_sha256": "a" * 64,
        "engine_source_revision": "rev",
        "engine_policy_lock": "SLATE_PINNED_V1",
        "engine_policy_fingerprint": "b" * 64,
        "context_contract_version": "football-context-v1",
        "rank_at_utc": "2026-10-30T08:00:00+00:00",
        "slate_window_class": "CUSTOM_EXPLICIT_WINDOW",
        "slate_window_start_ict": "2026-10-30T15:00:00+07:00",
        "slate_window_end_ict": "2026-10-31T03:00:00+07:00",
        "active_model": "c",
        "retired_models": ["c2", "c3", "c4"],
        "board": {
            "matches": [
                {
                    "match_id": "M1",
                    "board_state": "FOCUS",
                    "follow_lane": "FOLLOW",
                    "rank": 1,
                    "supported_line": 2.5,
                },
                {
                    "match_id": "M2",
                    "board_state": "FOCUS",
                    "follow_lane": "RESERVE",
                    "rank": 2,
                    "supported_line": 3.5,
                },
            ]
        },
        "frozen_model_input": {
            "matches": [
                {"match_id": "M1", "home_route": "STRONG"},
                {"match_id": "M2", "home_route": "USABLE"},
                {"match_id": "WATCH", "home_route": "USABLE"},
            ]
        },
    }
    verified = {
        "status": "V4_RANK_PERSISTENCE_VERIFIED",
        "persistence_verified": True,
        "run_id": "V4-TEST",
        "rank_sha256": "a" * 64,
        "engine_policy_lock": "SLATE_PINNED_V1",
        "engine_policy_fingerprint": "b" * 64,
    }
    artifact = {
        "schema_version": "football-c-verified-rank-artifact-v1",
        "run_id": "V4-TEST",
        "artifacts": {
            "rank.json": rank,
            "verified.json": verified,
            "huge-unneeded-evidence.json": {"payload": "x" * 5000},
        },
    }
    return json.dumps(artifact, separators=(",", ":")).encode("utf-8")


class RankPackageTransportTests(unittest.TestCase):
    def test_capsule_preserves_only_ranked_rows_and_exact_frozen_inputs(self):
        raw = artifact_bytes()
        capsule = build_capsule(raw)
        self.assertEqual(
            capsule["schema_version"],
            "football-c-rank-authority-capsule-v1",
        )
        self.assertEqual(
            capsule["source_artifact_sha256"],
            hashlib.sha256(raw).hexdigest(),
        )
        receipt = capsule["rank_receipt"]
        self.assertEqual(
            [x["match_id"] for x in receipt["board"]["matches"]],
            ["M1", "M2"],
        )
        self.assertEqual(
            [x["match_id"] for x in receipt["frozen_model_input"]["matches"]],
            ["M1", "M2"],
        )
        self.assertEqual(receipt["integrity_sha256"], "a" * 64)

    def test_match_scoped_capsule_is_exact(self):
        capsule = build_capsule(artifact_bytes(), match_id="M2")
        self.assertEqual(
            [x["match_id"] for x in capsule["rank_receipt"]["board"]["matches"]],
            ["M2"],
        )
        self.assertEqual(
            [
                x["match_id"]
                for x in capsule["rank_receipt"]["frozen_model_input"]["matches"]
            ],
            ["M2"],
        )

    def test_unverified_or_hash_mismatched_artifact_fails_closed(self):
        obj = json.loads(artifact_bytes())
        obj["artifacts"]["verified.json"]["rank_sha256"] = "c" * 64
        with self.assertRaisesRegex(
            RankTransportError,
            "verified rank hash does not match",
        ):
            build_capsule(json.dumps(obj).encode("utf-8"))

    def test_unknown_match_fails_closed(self):
        with self.assertRaisesRegex(RankTransportError, "not on the sealed rank board"):
            build_capsule(artifact_bytes(), match_id="MISSING")


if __name__ == "__main__":
    unittest.main()
