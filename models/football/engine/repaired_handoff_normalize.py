from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
from typing import Any


VALID_DISPOSITIONS = {
    "ADMITTED_TO_C",
    "OPERATIONAL_EXCLUDED",
    "RESEARCHABILITY_EXCLUDED",
    "OPERATIONAL_CAPACITY_DEFERRED",
    "UNRESOLVED",
    "HARD_EXCLUDED",
}

WOMEN_COUNT_KEYS = {
    "ADMITTED_TO_C": "women_top_flight_admitted_count",
    "OPERATIONAL_EXCLUDED": "women_top_flight_operational_excluded_count",
    "RESEARCHABILITY_EXCLUDED": "women_top_flight_researchability_excluded_count",
    "OPERATIONAL_CAPACITY_DEFERRED": "women_top_flight_capacity_deferred_count",
    "UNRESOLVED": "women_top_flight_unresolved_count",
}


class RepairedHandoffNormalizationError(ValueError):
    pass


def _fixture_id(row: dict[str, Any]) -> str:
    for key in ("match_id", "aiscore_id", "fixture_id", "id"):
        value = row.get(key)
        if value is not None and str(value).strip():
            return str(value).strip()
    raise RepairedHandoffNormalizationError("fixture row missing stable identity")


def _manifest(payload: dict[str, Any]) -> list[dict[str, Any]]:
    manifest = payload.get("women_top_flight_disposition_manifest")
    if not isinstance(manifest, list):
        raise RepairedHandoffNormalizationError(
            "women_top_flight_disposition_manifest must be a fixture-level array"
        )
    return manifest


def _all_fixture_arrays(payload: dict[str, Any]) -> list[list[dict[str, Any]]]:
    arrays: list[list[dict[str, Any]]] = []
    for key, value in payload.items():
        if not isinstance(value, list) or not value:
            continue
        if all(isinstance(item, dict) for item in value):
            keys = set().union(*(item.keys() for item in value))
            if keys.intersection({"match_id", "aiscore_id", "fixture_id"}) and keys.intersection(
                {"disposition", "final_step0_disposition", "operational_viability_grade"}
            ):
                arrays.append(value)
    return arrays


def normalize_repaired_handoff(payload: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    if not isinstance(payload, dict):
        raise RepairedHandoffNormalizationError("handoff payload must be an object")

    out = copy.deepcopy(payload)
    manifest = _manifest(out)

    women_ids: set[str] = set()
    counts = {key: 0 for key in WOMEN_COUNT_KEYS.values()}
    manifest_conflicts = 0

    for row in manifest:
        if not isinstance(row, dict):
            raise RepairedHandoffNormalizationError("women manifest row must be an object")
        match_id = _fixture_id(row)
        women_ids.add(match_id)

        final_disp = row.get("final_step0_disposition", row.get("disposition"))
        if final_disp not in VALID_DISPOSITIONS:
            raise RepairedHandoffNormalizationError(
                f"women fixture {match_id}: invalid final disposition {final_disp!r}"
            )

        if row.get("disposition") not in (None, final_disp):
            manifest_conflicts += 1
        row["final_step0_disposition"] = final_disp
        row["disposition"] = final_disp
        row["women_top_flight"] = True

        if final_disp in WOMEN_COUNT_KEYS:
            counts[WOMEN_COUNT_KEYS[final_disp]] += 1

    out["women_top_flight_raw_count"] = len(manifest)
    for key, value in counts.items():
        out[key] = value

    fixture_conflicts = 0
    bool_repairs = 0
    touched_ids: set[str] = set()

    for rows in _all_fixture_arrays(out):
        for row in rows:
            match_id = _fixture_id(row)
            final_disp = row.get("final_step0_disposition")
            alias_disp = row.get("disposition")

            if final_disp is not None:
                if final_disp not in VALID_DISPOSITIONS:
                    raise RepairedHandoffNormalizationError(
                        f"fixture {match_id}: invalid final_step0_disposition {final_disp!r}"
                    )
                if alias_disp not in (None, final_disp):
                    fixture_conflicts += 1
                row["disposition"] = final_disp
            elif alias_disp is not None:
                if alias_disp not in VALID_DISPOSITIONS:
                    raise RepairedHandoffNormalizationError(
                        f"fixture {match_id}: invalid disposition {alias_disp!r}"
                    )
                row["final_step0_disposition"] = alias_disp

            expected_women = match_id in women_ids
            if row.get("women_top_flight") is not expected_women:
                bool_repairs += 1
            row["women_top_flight"] = expected_women
            touched_ids.add(match_id)

    unresolved = out.get("women_top_flight_unresolved_count")
    if unresolved != 0:
        raise RepairedHandoffNormalizationError(
            f"women_top_flight_unresolved_count must be 0 after normalization, got {unresolved!r}"
        )

    report = {
        "status": "REPAIRED HANDOFF LOCAL NORMALIZATION: PASS",
        "manifest_rows": len(manifest),
        "manifest_disposition_conflicts_fixed": manifest_conflicts,
        "fixture_disposition_conflicts_fixed": fixture_conflicts,
        "women_boolean_repairs": bool_repairs,
        "fixture_rows_touched": len(touched_ids),
        "women_counts": {
            "raw": out["women_top_flight_raw_count"],
            **counts,
        },
    }
    return out, report


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Normalize duplicate metadata in a completed repaired football handoff"
    )
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    try:
        payload = json.loads(Path(args.input).read_text(encoding="utf-8"))
        normalized, report = normalize_repaired_handoff(payload)
        Path(args.output).write_text(
            json.dumps(normalized, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        print(json.dumps({"ok": True, **report}, indent=2, sort_keys=True))
        return 0
    except (OSError, json.JSONDecodeError, RepairedHandoffNormalizationError) as exc:
        print(
            json.dumps(
                {
                    "ok": False,
                    "status": "REPAIRED HANDOFF LOCAL NORMALIZATION: FAIL",
                    "error": str(exc),
                },
                indent=2,
                sort_keys=True,
            )
        )
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
