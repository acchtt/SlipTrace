"""Prospective /sweep source-completeness contract.

The sweep stage must never confuse the league registry with fixture discovery.
For new production sweeps, the caller first enumerates complete provider
date/listing surfaces, reconciles provider page/block counts, then supplies the
full senior-football fixture set to stage.py.

This module is deterministic. It does not browse providers itself.
"""
from __future__ import annotations

import hashlib
import json
from datetime import date, datetime, timedelta, timezone
from typing import Any
from urllib.parse import urlsplit
from zoneinfo import ZoneInfo

SCHEMA = "football-v4-source-completeness-v2"
CONTRACT = "DATE_SURFACE_BATCH_V2"
LEAGUE_QUERY_MODE = "DATE_SURFACE_ONLY"
SCOPE_POLICY = "ALL_SOURCE_VISIBLE_SENIOR_FOOTBALL_BLOCKS"
ICT = ZoneInfo("Asia/Ho_Chi_Minh")
MAX_AGE = timedelta(minutes=60)


class SourceCompletenessError(ValueError):
    pass


def _time(value: Any, label: str) -> datetime:
    if not isinstance(value, str):
        raise SourceCompletenessError(f"{label}: timezone-aware timestamp required")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise SourceCompletenessError(f"{label}: invalid timestamp") from exc
    if parsed.tzinfo is None:
        raise SourceCompletenessError(f"{label}: timezone-aware timestamp required")
    return parsed.astimezone(timezone.utc)


def _url(value: Any, label: str) -> str:
    if not isinstance(value, str):
        raise SourceCompletenessError(f"{label}: HTTPS source required")
    parsed = urlsplit(value)
    if parsed.scheme != "https" or not parsed.hostname or "." not in parsed.hostname:
        raise SourceCompletenessError(f"{label}: valid public HTTPS source required")
    if parsed.username or parsed.password:
        raise SourceCompletenessError(f"{label}: credential-bearing URL forbidden")
    return value


def _hash(value: Any) -> str:
    return hashlib.sha256(json.dumps(
        value, sort_keys=True, ensure_ascii=True, separators=(",", ":")
    ).encode("utf-8")).hexdigest()


def _dates_touched(start: datetime, end: datetime, tz) -> list[date]:
    """Return calendar dates touched by [start, end), preserving local basis."""
    last = end - timedelta(microseconds=1)
    first_date = start.astimezone(tz).date()
    last_date = last.astimezone(tz).date()
    days: list[date] = []
    current = first_date
    while current <= last_date:
        days.append(current)
        current += timedelta(days=1)
    return days


def required_surface_keys(window_start_utc: str, window_end_utc: str) -> list[str]:
    start = _time(window_start_utc, "window_start_utc")
    end = _time(window_end_utc, "window_end_utc")
    if end <= start:
        raise SourceCompletenessError("window end must be after start")
    keys = [f"ICT:{d.isoformat()}" for d in _dates_touched(start, end, ICT)]
    keys += [f"UTC:{d.isoformat()}" for d in _dates_touched(start, end, timezone.utc)]
    return keys


def _ids(value: Any, label: str) -> list[str]:
    if not isinstance(value, list):
        raise SourceCompletenessError(f"{label}: fixture ID list required")
    if any(not isinstance(x, str) or not x.strip() for x in value):
        raise SourceCompletenessError(f"{label}: canonical non-empty fixture IDs required")
    if len(value) != len(set(value)):
        raise SourceCompletenessError(f"{label}: duplicate fixture ID")
    return value


def _fresh(value: Any, at: datetime, label: str) -> datetime:
    observed = _time(value, label)
    if not at - MAX_AGE <= observed <= at:
        raise SourceCompletenessError(f"{label}: source observation stale or future")
    return observed


def validate_source_completeness(source: dict[str, Any], *, now: str) -> dict[str, Any]:
    """Validate a complete date-surface acquisition manifest.

    This proves internal extraction completeness against the provider counts
    recorded by the caller. It does not independently prove that the external
    provider told the truth or exposed every football fixture worldwide.
    """
    if not isinstance(source, dict):
        raise SourceCompletenessError("source snapshot object required")
    at = _time(now, "now")
    start = _time(source.get("window_start_utc"), "window_start_utc")
    end = _time(source.get("window_end_utc"), "window_end_utc")
    manifest = source.get("source_completeness_manifest")
    if not isinstance(manifest, dict):
        raise SourceCompletenessError(
            "SWEEP_SOURCE_COMPLETENESS_REQUIRED: complete date-surface manifest missing"
        )
    if manifest.get("schema_version") != SCHEMA:
        raise SourceCompletenessError("SWEEP_SOURCE_COMPLETENESS_SCHEMA_MISMATCH")
    if manifest.get("acquisition_mode") != CONTRACT:
        raise SourceCompletenessError("SWEEP_ACQUISITION_MODE_MUST_BE_DATE_SURFACE_BATCH_V2")
    if manifest.get("league_query_mode") != LEAGUE_QUERY_MODE:
        raise SourceCompletenessError("SWEEP_LEAGUE_BY_LEAGUE_DISCOVERY_FORBIDDEN")
    if manifest.get("registry_prefilter_applied") is not False:
        raise SourceCompletenessError("SWEEP_REGISTRY_PREFILTER_FORBIDDEN_DURING_DISCOVERY")
    if manifest.get("scope_policy") != SCOPE_POLICY:
        raise SourceCompletenessError("SWEEP_SOURCE_SCOPE_POLICY_MISMATCH")
    if manifest.get("extraction_complete") is not True:
        raise SourceCompletenessError("SWEEP_SOURCE_EXTRACTION_INCOMPLETE")
    if manifest.get("provider_family") != source.get("source_family"):
        raise SourceCompletenessError("SWEEP_PROVIDER_FAMILY_MISMATCH")
    if _time(manifest.get("window_start_utc"), "manifest.window_start_utc") != start:
        raise SourceCompletenessError("SWEEP_MANIFEST_WINDOW_START_MISMATCH")
    if _time(manifest.get("window_end_utc"), "manifest.window_end_utc") != end:
        raise SourceCompletenessError("SWEEP_MANIFEST_WINDOW_END_MISMATCH")
    _fresh(manifest.get("checked_at_utc"), at, "manifest.checked_at_utc")

    expected_keys = required_surface_keys(
        source.get("window_start_utc"), source.get("window_end_utc")
    )
    declared_keys = manifest.get("required_surface_keys")
    if declared_keys != expected_keys:
        raise SourceCompletenessError(
            "SWEEP_DATE_ENVELOPE_INCOMPLETE: ICT+UTC date surfaces do not match requested window"
        )

    surfaces = manifest.get("date_surfaces")
    if not isinstance(surfaces, list) or not surfaces:
        raise SourceCompletenessError("SWEEP_DATE_SURFACES_REQUIRED")
    by_key: dict[str, dict[str, Any]] = {}
    fixture_union: set[str] = set()
    block_count_total = 0
    for index, surface in enumerate(surfaces):
        label = f"date_surfaces[{index}]"
        if not isinstance(surface, dict):
            raise SourceCompletenessError(f"{label}: object required")
        key = surface.get("surface_key")
        if key not in expected_keys or key in by_key:
            raise SourceCompletenessError(f"{label}: missing/duplicate/foreign required surface key")
        by_key[key] = surface
        _url(surface.get("source_url"), f"{label}.source_url")
        _fresh(surface.get("observed_at_utc"), at, f"{label}.observed_at_utc")
        if surface.get("pagination_complete") is not True:
            raise SourceCompletenessError(f"{label}: pagination not exhausted")
        pages = surface.get("provider_page_count")
        fetched = surface.get("pages_fetched")
        if not isinstance(pages, int) or isinstance(pages, bool) or pages < 1:
            raise SourceCompletenessError(f"{label}: positive provider_page_count required")
        if not isinstance(fetched, list) or fetched != list(range(1, pages + 1)):
            raise SourceCompletenessError(f"{label}: pages_fetched must exactly cover 1..provider_page_count")
        surface_ids = _ids(surface.get("extracted_fixture_ids"), f"{label}.extracted_fixture_ids")
        fixture_count = surface.get("provider_senior_fixture_count")
        if not isinstance(fixture_count, int) or isinstance(fixture_count, bool) or fixture_count < 0:
            raise SourceCompletenessError(f"{label}: provider_senior_fixture_count required")
        if fixture_count != len(surface_ids):
            raise SourceCompletenessError(f"{label}: provider fixture count differs from extracted IDs")

        blocks = surface.get("competition_blocks")
        block_count = surface.get("provider_senior_competition_block_count")
        if not isinstance(blocks, list) or not isinstance(block_count, int) or isinstance(block_count, bool):
            raise SourceCompletenessError(f"{label}: provider competition block reconciliation required")
        if block_count != len(blocks):
            raise SourceCompletenessError(f"{label}: provider competition block count mismatch")
        block_ids: list[str] = []
        for block_index, block in enumerate(blocks):
            block_label = f"{label}.competition_blocks[{block_index}]"
            if not isinstance(block, dict):
                raise SourceCompletenessError(f"{block_label}: object required")
            for field in ("country", "competition"):
                if not isinstance(block.get(field), str) or not block[field].strip():
                    raise SourceCompletenessError(f"{block_label}.{field}: non-empty value required")
            ids = _ids(block.get("extracted_fixture_ids"), f"{block_label}.extracted_fixture_ids")
            reported = block.get("provider_fixture_count")
            if not isinstance(reported, int) or isinstance(reported, bool) or reported < 0:
                raise SourceCompletenessError(f"{block_label}: provider_fixture_count required")
            if reported != len(ids):
                raise SourceCompletenessError(f"{block_label}: provider fixture count mismatch")
            block_ids.extend(ids)
        if len(block_ids) != len(set(block_ids)):
            raise SourceCompletenessError(f"{label}: fixture appears in multiple competition blocks")
        if set(block_ids) != set(surface_ids):
            raise SourceCompletenessError(f"{label}: competition blocks do not reconcile to surface fixture IDs")
        fixture_union.update(surface_ids)
        block_count_total += block_count

    if set(by_key) != set(expected_keys):
        missing = sorted(set(expected_keys) - set(by_key))
        raise SourceCompletenessError(
            "SWEEP_DATE_ENVELOPE_INCOMPLETE: missing required surfaces " + ",".join(missing)
        )

    fixtures = source.get("fixtures")
    if not isinstance(fixtures, list):
        raise SourceCompletenessError("source fixtures list required")
    source_ids: list[str] = []
    for row in fixtures:
        if isinstance(row, dict) and isinstance(row.get("match_id"), str) and row["match_id"].strip():
            source_ids.append(row["match_id"])
    if len(source_ids) != len(set(source_ids)):
        # stage.py has a more specific duplicate error, but completeness must
        # also never certify a duplicate source set.
        raise SourceCompletenessError("SWEEP_SOURCE_DUPLICATE_MATCH_ID")
    if set(source_ids) != fixture_union:
        missing = sorted(fixture_union - set(source_ids))
        extra = sorted(set(source_ids) - fixture_union)
        raise SourceCompletenessError(
            "SWEEP_SOURCE_FIXTURE_UNION_MISMATCH: "
            f"missing_from_source={missing[:8]} extra_vs_surfaces={extra[:8]}"
        )

    sentinel = manifest.get("terminal_sentinel")
    if not isinstance(sentinel, dict) or sentinel.get("complete") is not True:
        raise SourceCompletenessError("SWEEP_TERMINAL_SENTINEL_REQUIRED")
    terminal_start = max(start, end - timedelta(hours=6))
    if _time(sentinel.get("interval_start_utc"), "terminal.interval_start_utc") != terminal_start:
        raise SourceCompletenessError("SWEEP_TERMINAL_SENTINEL_START_MISMATCH")
    if _time(sentinel.get("interval_end_utc"), "terminal.interval_end_utc") != end:
        raise SourceCompletenessError("SWEEP_TERMINAL_SENTINEL_END_MISMATCH")
    _fresh(sentinel.get("checked_at_utc"), at, "terminal.checked_at_utc")
    if sentinel.get("independent_refetch") is not True:
        raise SourceCompletenessError("SWEEP_TERMINAL_SENTINEL_MUST_BE_INDEPENDENT_REFETCH")
    urls = sentinel.get("source_urls")
    if not isinstance(urls, list) or not urls:
        raise SourceCompletenessError("terminal.source_urls: at least one listing URL required")
    for index, url in enumerate(urls):
        _url(url, f"terminal.source_urls[{index}]")
    sentinel_ids = _ids(
        sentinel.get("extracted_fixture_ids"), "terminal.extracted_fixture_ids"
    )
    if sentinel.get("provider_senior_fixture_count") != len(sentinel_ids):
        raise SourceCompletenessError("SWEEP_TERMINAL_SENTINEL_COUNT_MISMATCH")
    if not set(sentinel_ids).issubset(fixture_union):
        raise SourceCompletenessError("SWEEP_TERMINAL_SENTINEL_FOREIGN_FIXTURE")

    expected_terminal: set[str] = set()
    for row in fixtures:
        if not isinstance(row, dict) or not isinstance(row.get("match_id"), str):
            continue
        try:
            kickoff = _time(row.get("kickoff_utc"), f"{row['match_id']}.kickoff_utc")
        except SourceCompletenessError:
            continue
        if terminal_start <= kickoff < end:
            expected_terminal.add(row["match_id"])
    if set(sentinel_ids) != expected_terminal:
        missing = sorted(expected_terminal - set(sentinel_ids))
        extra = sorted(set(sentinel_ids) - expected_terminal)
        raise SourceCompletenessError(
            "SWEEP_TERMINAL_SENTINEL_RECONCILIATION_MISMATCH: "
            f"missing={missing[:8]} extra={extra[:8]}"
        )

    return {
        "source_completeness_contract": CONTRACT,
        "source_completeness_sha256": _hash(manifest),
        "required_surface_keys": expected_keys,
        "date_surface_count": len(surfaces),
        "provider_senior_fixture_union_count": len(fixture_union),
        "provider_senior_competition_block_observations": block_count_total,
        "terminal_interval_start_utc": terminal_start.isoformat(),
        "terminal_interval_end_utc": end.isoformat(),
        "terminal_fixture_count": len(sentinel_ids),
        "registry_prefilter_applied": False,
        "league_query_mode": LEAGUE_QUERY_MODE,
    }
