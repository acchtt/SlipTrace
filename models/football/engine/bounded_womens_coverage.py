"""Verify Step0 women's parity *within frozen bounded production discovery*.

Unlike EXACT_DATE_UNIVERSE, a bounded discovery receipt must never claim that
unseen AiScore competitions do not exist. It reconciles every women's senior
top-flight fixture surfaced by the acquired source family set and the extra
current women's-specific corroborators. Caller must independently OPEN each
listed source and freeze its real fixture identities before validation.
"""
from __future__ import annotations

from datetime import datetime
from typing import Any
from urllib.parse import urlparse

COVERAGE_SCOPE = "BOUNDED_DISCOVERED_BLOCKS"
CHECK_STATUS = "OPENED_WINDOW_VERIFIED"
VALID_DISPOSITIONS = {
    "ADMITTED_TO_C", "OPERATIONAL_CAPACITY_DEFERRED",
    "OPERATIONAL_EXCLUDED", "RESEARCHABILITY_EXCLUDED",
}
COUNT_FIELDS = {
    "ADMITTED_TO_C": "women_top_flight_admitted_count",
    "OPERATIONAL_CAPACITY_DEFERRED": "women_top_flight_capacity_deferred_count",
    "OPERATIONAL_EXCLUDED": "women_top_flight_operational_excluded_count",
    "RESEARCHABILITY_EXCLUDED": "women_top_flight_researchability_excluded_count",
}


class BoundedWomensCoverageError(ValueError):
    pass


def _ids(value: Any, label: str) -> set[str]:
    if not isinstance(value, list):
        raise BoundedWomensCoverageError(f"{label} must be a fixture-ID array")
    seen: set[str] = set()
    for item in value:
        if not isinstance(item, str) or not item.strip():
            raise BoundedWomensCoverageError(f"{label} contains blank fixture ID")
        mid = item.strip()
        if mid.upper().startswith("DISCOVERY-") or mid in seen:
            raise BoundedWomensCoverageError(f"{label} has duplicate/provisional fixture ID: {mid}")
        seen.add(mid)
    return seen


def _utc(value: Any) -> None:
    if not isinstance(value, str):
        raise BoundedWomensCoverageError("women coverage checked_at_utc missing")
    try:
        date = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if date.utcoffset() is None:
            raise ValueError("naive clock")
    except ValueError:
        raise BoundedWomensCoverageError("women coverage checked_at_utc must be zoned") from None


def _url(value: Any) -> None:
    if not isinstance(value, str):
        raise BoundedWomensCoverageError("women coverage source URL missing")
    parsed = urlparse(value)
    if parsed.scheme != "https" or not parsed.hostname or "." not in parsed.hostname:
        raise BoundedWomensCoverageError("women coverage requires an opened HTTPS source URL")


def validate_bounded_womens_coverage(payload: dict[str, Any]) -> dict[str, Any]:
    if payload.get("women_coverage_scope") != COVERAGE_SCOPE:
        raise BoundedWomensCoverageError(
            "women coverage must explicitly say BOUNDED_DISCOVERED_BLOCKS, never GLOBAL_AISCORE_COMPLETE"
        )
    # Include every women's fixture surfaced by ANY of the discovery seeds,
    # not just the league calendars that happened to be checked.
    seed_ids = _ids(payload.get("women_top_flight_seed_fixture_ids"), "women seed fixture IDs")
    checks = payload.get("women_top_flight_source_checks")
    if not isinstance(checks, list) or len(checks) < 2:
        raise BoundedWomensCoverageError("two independent source-family women's-window scans required")
    source_ids: set[str] = set()
    families: set[str] = set()
    for check in checks:
        if not isinstance(check, dict) or check.get("status") != CHECK_STATUS:
            raise BoundedWomensCoverageError("women source check not opened/verified for requested window")
        if check.get("scope") != "SENIOR_WOMENS_TOPFLIGHT":
            raise BoundedWomensCoverageError("women source check wrong competition scope")
        family = check.get("source_family")
        if not isinstance(family, str) or not family.strip():
            raise BoundedWomensCoverageError("women source family missing")
        families.add(family.strip().casefold())
        _url(check.get("source_url"))
        _utc(check.get("checked_at_utc"))
        if check.get("requested_window") != payload.get("requested_window"):
            raise BoundedWomensCoverageError("women source check not for frozen sweep window")
        source_ids.update(_ids(check.get("visible_fixture_ids"), "women source fixture IDs"))
    if len(families) < 2:
        raise BoundedWomensCoverageError("women scans not from two independent source families")
    manifest = payload.get("women_top_flight_disposition_manifest")
    if not isinstance(manifest, list):
        raise BoundedWomensCoverageError("women top-flight disposition manifest required, even when empty")
    found: dict[str, str] = {}
    for item in manifest:
        if not isinstance(item, dict):
            raise BoundedWomensCoverageError("women disposition row invalid")
        mid = item.get("match_id")
        if not isinstance(mid, str) or not mid.strip() or mid.upper().startswith("DISCOVERY-"):
            raise BoundedWomensCoverageError("women disposition lacks canonical fixture ID")
        if mid in found:
            raise BoundedWomensCoverageError("women fixture duplicated in disposition manifest")
        disposition = item.get("disposition")
        if disposition not in VALID_DISPOSITIONS:
            raise BoundedWomensCoverageError("women fixture unresolved or invalid disposition")
        if not isinstance(item.get("kickoff_ict"), str) or not item["kickoff_ict"].strip():
            raise BoundedWomensCoverageError("women fixture kickoff missing")
        found[mid] = disposition
    # Discovery-seed fixture IDs and independently consulted women's-specific
    # sources are both authoritative for the observed, bounded set.
    if set(found) != seed_ids | source_ids:
        raise BoundedWomensCoverageError(
            "women surfaced fixture IDs disagree with source checks or final manifest"
        )
    count = payload.get("women_top_flight_raw_count")
    if isinstance(count, bool) or not isinstance(count, int) or count != len(found):
        raise BoundedWomensCoverageError("women top-flight raw counter/manifest mismatch")
    unresolved = payload.get("women_top_flight_unresolved_count")
    if type(unresolved) is not int or unresolved != 0:
        raise BoundedWomensCoverageError("women top-flight unresolved fixtures not cleared")
    for disposition, field in COUNT_FIELDS.items():
        observed = payload.get(field)
        if type(observed) is not int or observed != sum(x == disposition for x in found.values()):
            raise BoundedWomensCoverageError(f"women counter mismatch: {field}")
    return {
        "status": "BOUNDED_WOMEN_SURFACED_FIXTURES_RECONCILED",
        "global_aiscore_completeness_claimed": False,
        "source_family_count": len(families),
        "surfaced_womens_topflight_fixture_count": len(found),
    }
