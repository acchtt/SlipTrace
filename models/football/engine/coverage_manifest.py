from __future__ import annotations

from dataclasses import dataclass
from typing import Any


MANIFEST_VERSION = "required-competition-manifest-v1"
REQUIRED_BLOCKS = ("NED_EERSTE_DIVISIE",)
VALID_STATUSES = {
    "CHECKED_WITH_FIXTURES",
    "CHECKED_NO_IN_WINDOW_FIXTURES",
    "SOURCE_BLOCKED",
}
VALID_DISPOSITIONS = {
    "ADMITTED_TO_C",
    "HARD_EXCLUDED",
    "OPERATIONAL_EXCLUDED",
    "RESEARCHABILITY_EXCLUDED",
    "OPERATIONAL_CAPACITY_DEFERRED",
    "UNRESOLVED",
}


class CoverageManifestError(ValueError):
    pass


def validate_required_competition_manifest(payload: dict[str, Any]) -> dict[str, Any]:
    version = payload.get("required_competition_manifest_version")
    if version != MANIFEST_VERSION:
        raise CoverageManifestError(
            f"required competition manifest version must be {MANIFEST_VERSION}"
        )

    blocks = payload.get("required_competition_blocks")
    if not isinstance(blocks, list):
        raise CoverageManifestError("required_competition_blocks must be an array")

    by_id: dict[str, dict[str, Any]] = {}
    for block in blocks:
        if not isinstance(block, dict):
            raise CoverageManifestError("required competition block must be an object")
        block_id = block.get("block_id")
        if block_id in by_id:
            raise CoverageManifestError(f"duplicate required competition block: {block_id}")
        by_id[str(block_id)] = block

    for required in REQUIRED_BLOCKS:
        if required not in by_id:
            raise CoverageManifestError(
                f"HANDOFF INCOMPLETE — REQUIRED COMPETITION COVERAGE GAP: missing {required}"
            )

        block = by_id[required]
        status = block.get("status")
        if status not in VALID_STATUSES:
            raise CoverageManifestError(f"{required}: invalid status {status!r}")
        if status == "SOURCE_BLOCKED":
            raise CoverageManifestError(
                f"HANDOFF INCOMPLETE — REQUIRED COMPETITION COVERAGE GAP: {required} SOURCE_BLOCKED"
            )

        fixture_count = block.get("fixture_count")
        fixtures = block.get("fixtures")
        if not isinstance(fixture_count, int) or fixture_count < 0:
            raise CoverageManifestError(f"{required}: fixture_count must be a non-negative integer")
        if not isinstance(fixtures, list):
            raise CoverageManifestError(f"{required}: fixtures must be an array")
        if fixture_count != len(fixtures):
            raise CoverageManifestError(
                f"{required}: fixture_count {fixture_count} != fixture list {len(fixtures)}"
            )

        if status == "CHECKED_NO_IN_WINDOW_FIXTURES" and fixture_count != 0:
            raise CoverageManifestError(
                f"{required}: CHECKED_NO_IN_WINDOW_FIXTURES requires fixture_count=0"
            )
        if status == "CHECKED_WITH_FIXTURES" and fixture_count == 0:
            raise CoverageManifestError(
                f"{required}: CHECKED_WITH_FIXTURES requires at least one fixture"
            )

        seen_match_ids: set[str] = set()
        for fixture in fixtures:
            if not isinstance(fixture, dict):
                raise CoverageManifestError(f"{required}: fixture must be an object")
            match_id = str(fixture.get("match_id", "")).strip()
            if not match_id:
                raise CoverageManifestError(f"{required}: fixture missing match_id")
            if match_id in seen_match_ids:
                raise CoverageManifestError(f"{required}: duplicate match_id {match_id}")
            seen_match_ids.add(match_id)
            if not str(fixture.get("match", "")).strip():
                raise CoverageManifestError(f"{required}: fixture missing match")
            if not str(fixture.get("kickoff_ict", "")).strip():
                raise CoverageManifestError(f"{required}: fixture missing kickoff_ict")
            disposition = fixture.get("disposition")
            if disposition not in VALID_DISPOSITIONS:
                raise CoverageManifestError(
                    f"{required}: fixture {match_id} has invalid disposition {disposition!r}"
                )

    return {
        "version": version,
        "required_blocks_complete": True,
        "required_blocks": list(REQUIRED_BLOCKS),
    }
