from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

HANDOFF_VERSION = "football-step0-handoff-v2"
FIELDS = (
    "xi_expected",
    "market_observability",
    "team_news_observability",
    "operational_viability_reason",
    "competition_reliability_state",
    "competition_reliability_reason",
)
SOURCE_SCOPES = {"EXACT_DATE_UNIVERSE", "BOUNDED_PRODUCTION_DISCOVERY"}


class Step0HandoffError(ValueError):
    pass


def _mid(row: dict[str, Any]) -> str:
    value = row.get("match_id")
    if not isinstance(value, str) or not value.strip():
        raise Step0HandoffError(
            "HANDOFF INCOMPLETE — STABLE FIXTURE ID MISSING"
        )
    return value.strip()


def _nonempty(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise Step0HandoffError(
            f"HANDOFF INCOMPLETE — {field} missing"
        )
    return value.strip()


def _validate_source_contract(payload: dict[str, Any]) -> str:
    """Validate Step-0 source semantics consumed by /rank.

    Older v2 handoffs may predate source_scope. They remain readable as
    LEGACY_EXACT_OR_PRE_SCOPE so historical completed handoffs are not broken.
    Every new bounded-production handoff is validated explicitly.
    """
    scope = payload.get("source_scope")
    if scope is None:
        return "LEGACY_EXACT_OR_PRE_SCOPE"

    if scope not in SOURCE_SCOPES:
        raise Step0HandoffError(
            "HANDOFF INCOMPLETE — source_scope must be "
            "EXACT_DATE_UNIVERSE or BOUNDED_PRODUCTION_DISCOVERY"
        )

    _nonempty(payload.get("source_transport"), "source_transport")

    if scope == "EXACT_DATE_UNIVERSE":
        if payload.get("global_raw_exact") is False:
            raise Step0HandoffError(
                "HANDOFF INCOMPLETE — EXACT_DATE_UNIVERSE cannot set "
                "global_raw_exact=false"
            )
        return scope

    # New FAST_PRODUCTION fallback contract.
    if payload.get("coverage_mode") != "FALLBACK_PRODUCTION_SCOPE":
        raise Step0HandoffError(
            "HANDOFF INCOMPLETE — bounded source scope requires "
            "coverage_mode=FALLBACK_PRODUCTION_SCOPE"
        )
    if payload.get("global_raw_exact") is not False:
        raise Step0HandoffError(
            "HANDOFF INCOMPLETE — bounded source scope requires "
            "global_raw_exact=false"
        )
    if payload.get("production_scope_complete") is not True:
        raise Step0HandoffError(
            "HANDOFF INCOMPLETE — bounded source scope requires "
            "production_scope_complete=true"
        )
    if payload.get("source_transport") != "MULTISOURCE_BOUNDED_PRODUCTION_DISCOVERY":
        raise Step0HandoffError(
            "HANDOFF INCOMPLETE — bounded source scope requires "
            "source_transport=MULTISOURCE_BOUNDED_PRODUCTION_DISCOVERY"
        )

    manifest = payload.get("discovery_seed_manifest")
    if not isinstance(manifest, dict):
        raise Step0HandoffError(
            "HANDOFF INCOMPLETE — bounded source scope missing "
            "discovery_seed_manifest"
        )

    sources = manifest.get("sources")
    if not isinstance(sources, list) or len(sources) < 2:
        raise Step0HandoffError(
            "HANDOFF INCOMPLETE — bounded source scope requires at least "
            "two discovery seed sources"
        )

    families = set()
    for source in sources:
        if not isinstance(source, dict):
            raise Step0HandoffError(
                "HANDOFF INCOMPLETE — discovery seed source must be an object"
            )
        family = _nonempty(source.get("family"), "discovery seed source family")
        families.add(family.casefold())

    if len(families) < 2:
        raise Step0HandoffError(
            "HANDOFF INCOMPLETE — bounded source scope requires at least "
            "two independent source families"
        )

    if not isinstance(payload.get("production_universe_count"), int) or isinstance(
        payload.get("production_universe_count"), bool
    ) or payload.get("production_universe_count") < 0:
        raise Step0HandoffError(
            "HANDOFF INCOMPLETE — bounded source scope requires exact "
            "production_universe_count"
        )

    if not isinstance(payload.get("block_excluded_summary"), (list, dict)):
        raise Step0HandoffError(
            "HANDOFF INCOMPLETE — bounded source scope requires "
            "block_excluded_summary"
        )

    return scope


def validate_step0_handoff(payload: dict[str, Any]) -> dict[str, Any]:
    if payload.get("handoff_version") != HANDOFF_VERSION:
        raise Step0HandoffError(
            f"handoff_version must be {HANDOFF_VERSION}"
        )

    for key in ("complete", "actionable_complete", "work_ready"):
        if payload.get(key) is not True:
            raise Step0HandoffError(
                f"HANDOFF INCOMPLETE — {key}=true required"
            )

    source_scope = _validate_source_contract(payload)

    admitted = payload.get("admitted_fixtures")
    queue = payload.get("capacity_queue")
    if not isinstance(admitted, list):
        raise Step0HandoffError(
            "HANDOFF INCOMPLETE — admitted_fixtures missing"
        )
    if not isinstance(queue, list):
        raise Step0HandoffError(
            "HANDOFF INCOMPLETE — STEP0 CAPACITY QUEUE MISSING"
        )
    if len(admitted) > 15:
        raise Step0HandoffError(
            "HANDOFF INCOMPLETE — OPERATIONAL CAPACITY BREACH"
        )

    admitted_ids = set()
    for row in admitted:
        match_id = _mid(row)
        admitted_ids.add(match_id)
        if row.get("operational_viability_grade") not in {"A", "B"}:
            raise Step0HandoffError(
                f"HANDOFF INCOMPLETE — {match_id} not grade A/B"
            )
        for key in FIELDS:
            if not isinstance(row.get(key), str) or not row[key].strip():
                raise Step0HandoffError(
                    "HANDOFF INCOMPLETE — STEP0 OPERATIONAL CONTRACT MISSING: "
                    f"{match_id} missing {key}"
                )

    queue_ids = set()
    ranks = set()
    for row in queue:
        match_id = _mid(row)
        if match_id in queue_ids:
            raise Step0HandoffError(
                f"HANDOFF INCOMPLETE — DUPLICATE QUEUE FIXTURE ID: {match_id}"
            )
        queue_ids.add(match_id)

        disposition = row.get(
            "final_step0_disposition", row.get("disposition")
        )
        if disposition not in {
            "ADMITTED_TO_C",
            "OPERATIONAL_CAPACITY_DEFERRED",
        }:
            raise Step0HandoffError(
                f"HANDOFF INCOMPLETE — invalid queue disposition: {match_id}"
            )

        for key in FIELDS:
            if not isinstance(row.get(key), str) or not row[key].strip():
                raise Step0HandoffError(
                    "HANDOFF INCOMPLETE — STEP0 OPERATIONAL CONTRACT MISSING: "
                    f"{match_id} missing {key}"
                )

        rank = row.get("step0_capacity_queue_rank")
        if (
            isinstance(rank, bool)
            or not isinstance(rank, int)
            or rank < 1
            or rank in ranks
        ):
            raise Step0HandoffError(
                "HANDOFF INCOMPLETE — STEP0 CAPACITY QUEUE INVALID: "
                f"{match_id}"
            )
        ranks.add(rank)

    if ranks != set(range(1, len(queue) + 1)):
        raise Step0HandoffError(
            "HANDOFF INCOMPLETE — STEP0 CAPACITY QUEUE INVALID: "
            "ranks not contiguous"
        )

    if not admitted_ids.issubset(queue_ids):
        raise Step0HandoffError(
            "HANDOFF INCOMPLETE — STEP0 CAPACITY QUEUE MISSING "
            f"ADMITTED FIXTURES: {sorted(admitted_ids - queue_ids)}"
        )

    if payload.get("admitted_to_c_count") != len(admitted):
        raise Step0HandoffError(
            "HANDOFF INCOMPLETE — admitted count mismatch"
        )

    deferred = sum(
        row.get("final_step0_disposition", row.get("disposition"))
        == "OPERATIONAL_CAPACITY_DEFERRED"
        for row in queue
    )
    if payload.get("capacity_deferred_count") != deferred:
        raise Step0HandoffError(
            "HANDOFF INCOMPLETE — deferred count mismatch"
        )

    return {
        "step0_handoff_validation_status": "PASS",
        "source_scope": source_scope,
        "admitted_count": len(admitted),
        "capacity_queue_count": len(queue),
        "capacity_deferred_count": deferred,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    args = parser.parse_args()

    try:
        payload = json.loads(
            Path(args.input).read_text(encoding="utf-8")
        )
        out = validate_step0_handoff(payload)
    except (OSError, json.JSONDecodeError, Step0HandoffError) as exc:
        print(
            json.dumps({"ok": False, "error": str(exc)}),
            file=sys.stderr,
        )
        return 2

    print(json.dumps({"ok": True, **out}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
