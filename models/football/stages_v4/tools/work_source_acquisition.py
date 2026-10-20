"""Bounded, non-browser Work sweep acquisition transport.

This retrieves provider date JSON and preserves raw evidence; it does NOT
certify V4 completeness, verify individual fixtures or run Football C.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

ICT = ZoneInfo("Asia/Ho_Chi_Minh")
PROVIDERS = (
    ("sofascore_www", "https://www.sofascore.com/api/v1/sport/football/scheduled-events/{date}"),
    ("sofascore_api", "https://api.sofascore.com/api/v1/sport/football/scheduled-events/{date}"),
    ("thesportsdb", "https://www.thesportsdb.com/api/v1/json/123/eventsday.php?d={date}&s=Soccer"),
)
MAX_WINDOW_HOURS = 36
MAX_RESPONSE_BYTES = 12_000_000


def parse_request(obj: dict) -> tuple[datetime, datetime, list[tuple[str, str]]]:
    if set(obj) != {"run_id", "window_start_ict", "window_end_ict"}:
        raise ValueError("request must contain exactly run_id, window_start_ict, window_end_ict")
    run_id = obj["run_id"]
    if not isinstance(run_id, str) or not run_id.startswith("V4-") or not all(
        c.isalnum() or c in "-_" for c in run_id
    ) or len(run_id) > 100:
        raise ValueError("invalid V4 run_id")
    start = datetime.fromisoformat(obj["window_start_ict"])
    end = datetime.fromisoformat(obj["window_end_ict"])
    if start.tzinfo is None or end.tzinfo is None:
        raise ValueError("window timestamps must be timezone-aware")
    start, end = start.astimezone(ICT), end.astimezone(ICT)
    if end <= start or (end - start) > timedelta(hours=MAX_WINDOW_HOURS):
        raise ValueError("invalid or oversized sweep window")
    keys = []
    for tz_name, tz in (("ICT", ICT), ("UTC", timezone.utc)):
        day = start.astimezone(tz).date()
        final = (end - timedelta(microseconds=1)).astimezone(tz).date()
        while day <= final:
            keys.append((tz_name, day.isoformat()))
            day += timedelta(days=1)
    return start, end, keys


def fetch(url: str, attempts: int = 5) -> tuple[bytes, str]:
    errors = []
    for attempt in range(attempts):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": "Mozilla/5.0 (compatible; SlipTraceV4Acquisition/1.0)",
                "Accept": "application/json",
            })
            with urllib.request.urlopen(req, timeout=12) as resp:
                if resp.status != 200:
                    raise ValueError(f"HTTP {resp.status}")
                body = resp.read(MAX_RESPONSE_BYTES + 1)
                if len(body) > MAX_RESPONSE_BYTES:
                    raise ValueError("response exceeds size limit")
                return body, datetime.now(timezone.utc).isoformat()
        except urllib.error.HTTPError as exc:
            errors.append(f"{type(exc).__name__}: {exc}")
            # Authentication/anti-bot/client denials do not improve with blind
            # retries from the same egress. Fail this route immediately so the
            # next canonical provider can be tried.
            if exc.code in {400, 401, 403, 404, 405, 410, 429}:
                break
            if attempt + 1 < attempts:
                time.sleep(min(8, 2 ** attempt))
        except (OSError, ValueError) as exc:
            errors.append(f"{type(exc).__name__}: {exc}")
            if attempt + 1 < attempts:
                # Provider 5xx bursts have repeatedly cleared after a few seconds.
                # Keep retries bounded so source acquisition still fails closed.
                time.sleep(min(8, 2 ** attempt))
    raise RuntimeError("; ".join(errors))


def acquire_day(day: str) -> tuple[dict, bytes | None]:
    errors = []
    for name, template in PROVIDERS:
        url = template.format(date=day)
        try:
            body, observed = fetch(url)
            payload = json.loads(body)
            if not isinstance(payload, dict):
                raise ValueError("provider JSON is not an object")
            if name == "thesportsdb":
                events = payload.get("events")
                if not isinstance(events, list):
                    raise ValueError("TheSportsDB has no events array for date")
                ids = [e.get("idEvent") for e in events if isinstance(e, dict)]
            else:
                events = payload.get("events")
                if not isinstance(events, list):
                    raise ValueError("SofaScore JSON lacks events array")
                ids = [e.get("id") for e in events if isinstance(e, dict)]
            if len(ids) != len(events) or any(i is None for i in ids) or len(set(map(str, ids))) != len(ids):
                raise ValueError("missing or duplicate provider event IDs")
            return ({
                "status": "FETCHED_UNVERIFIED_COMPLETENESS",
                "provider": name,
                "source_url": url,
                "observed_at_utc": observed,
                "event_count": len(events),
                "provider_ids": ids,
                "sha256": hashlib.sha256(body).hexdigest(),
            }, body)
        except (RuntimeError, ValueError, json.JSONDecodeError) as exc:
            errors.append({"provider": name, "url": url, "error": str(exc)})
    return ({"status": "FETCH_FAILED", "errors": errors}, None)


def run(request_path: Path, output: Path) -> int:
    obj = json.loads(request_path.read_text(encoding="utf-8"))
    start, end, keys = parse_request(obj)
    output.mkdir(parents=True, exist_ok=True)
    days = sorted({day for _, day in keys})
    surfaces = {}
    for day in days:
        entry, raw = acquire_day(day)
        if raw is not None:
            name = f"provider-{day}.json"
            (output / name).write_bytes(raw)
            entry["raw_file"] = name
        surfaces[day] = entry
    # An independent second fetch is required for the terminal window.
    # This is evidence only, not a claim of fixture-union reconciliation.
    terminal_days = sorted({(end - timedelta(microseconds=1)).date().isoformat(),
                            (end - timedelta(hours=min(6, (end-start).total_seconds()/3600))).date().isoformat()})
    sentinels = {}
    for day in terminal_days:
        entry, raw = acquire_day(day)
        if raw is not None:
            name = f"terminal-refetch-{day}.json"
            (output / name).write_bytes(raw)
            entry["raw_file"] = name
        sentinels[day] = entry
    ok = all(s["status"] == "FETCHED_UNVERIFIED_COMPLETENESS" for s in surfaces.values())
    result = {
        "schema_version": "football-v4-work-acquisition-evidence-v1",
        "run_id": obj["run_id"],
        "window_start_ict": start.isoformat(),
        "window_end_ict": end.isoformat(),
        "required_surface_keys": [f"{tz}:{day}" for tz, day in keys],
        "surfaces_by_date": surfaces,
        "terminal_refetch_by_date": sentinels,
        "status": "RAW_ACQUISITION_FETCHED_NOT_V4_READY" if ok else "ACQUISITION_BLOCKED",
        "native_v4_executed": False,
        "source_completeness_proven": False,
        "eligible_queue_produced": False,
        "next_step": "Verify date-surface pagination, competition blocks, IDs, fixture statuses, terminal reconciliation and goal histories; construct genuine V4 source.json and run stage.py via existing attestation workflow.",
        "coverage_warning": "Provider APIs may return only a subset of worldwide football fixtures. A successful fetch never proves full provider/date surface or competition-block completeness.",
    }
    (output / "acquisition-evidence.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps({"run_id": obj["run_id"], "status": result["status"],
                      "days": days, "output": str(output),
                      "failed_surfaces": {k: v.get("errors", []) for k, v in surfaces.items()
                                          if v["status"] == "FETCH_FAILED"}}))
    return 0 if ok else 2


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--request", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    try:
        return run(args.request, args.output)
    except (ValueError, TypeError, KeyError, OSError, json.JSONDecodeError) as exc:
        print(f"ACQUISITION_REQUEST_INVALID: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
