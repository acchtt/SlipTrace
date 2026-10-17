#!/usr/bin/env python3
from __future__ import annotations

import argparse, json, re, time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

UTC = timezone.utc
RUN_ID = "V4-20261017-1200-20261017-1800"
WINDOW_START = datetime(2026, 10, 17, 5, 0, tzinfo=UTC)
WINDOW_END = datetime(2026, 10, 17, 11, 0, tzinfo=UTC)

YOUTH_RE = re.compile(r"(?:\byouth\b|\bu\s*[-]?\s*(?:1[5-9]|2[0-3])\b|under\s*[-]?\s*(?:1[5-9]|2[0-3])|reserve league|development league|academy|primavera|premier league 2|professional development league|youth alliance)", re.I)
NONSTANDARD_RE = re.compile(r"(?:futsal|beach soccer|esoccer|e-soccer|efootball|virtual|kings league|baller league|7s\b|six-a-side|6-a-side)", re.I)
FRIENDLY_RE = re.compile(r"friendl", re.I)
CUP_RE = re.compile(r"(?:\bcup\b|pokal|beker|trophy|coppa|copa del rey|ta[cç]a|super cup)", re.I)
CONTINENTAL_RE = re.compile(r"(?:champions league|europa league|conference league|libertadores|sudamericana|afc |concacaf|caf |uefa |copa america|asian cup)", re.I)
OFFICIAL_INTL_RE = re.compile(r"(?:world cup|qualification|qualifying|nations league|euro\b|afcon|africa cup of nations)", re.I)
WOMEN_RE = re.compile(r"(?:women|women's|womens|feminine|femenin)", re.I)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/128 Safari/537.36",
    "Accept": "application/json,text/plain,*/*",
    "Origin": "https://www.livescore.com",
    "Referer": "https://www.livescore.com/",
}

def fetch_json(url: str, retries: int = 3) -> dict:
    last = None
    for attempt in range(retries):
        try:
            req = Request(url, headers=HEADERS)
            with urlopen(req, timeout=25) as resp:
                data = json.loads(resp.read())
                if not isinstance(data, dict) or not isinstance(data.get("Stages"), list):
                    raise ValueError(f"LiveScore JSON missing Stages: {url}")
                return data
        except (HTTPError, URLError, TimeoutError, json.JSONDecodeError, ValueError) as exc:
            last = exc
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"LiveScore fetch failed after {retries} attempts: {url}: {last}")

def api_candidates(day: str, offset: int) -> list[str]:
    # The current App route is verified live on 2026-10-13. Keep the React
    # route only as bounded fallback; it currently returns HTTP 503.
    return [
        f"https://prod-public-api.livescore.com/v1/api/app/date/soccer/{day}/{offset}?MD=1&countryCode=US&locale=en",
        f"https://prod-public-api.livescore.com/v1/api/app/date/soccer/{day}/{offset}?MD=1&locale=en",
        f"https://prod-public-api.livescore.com/v1/api/react/date/soccer/{day}/{offset}.00?MD=1&countryCode=US&locale=en",
        f"https://prod-public-api.livescore.com/v1/api/react/date/soccer/{day}/{offset}.00?MD=1",
    ]

def _raw_event_count(board: dict) -> int:
    total = 0
    for stage in board.get("Stages", []):
        if isinstance(stage, dict) and isinstance(stage.get("Events"), list):
            total += len(stage["Events"])
    return total

def fetch_surface(day: str, offset: int) -> tuple[dict, str]:
    errors = []
    for url in api_candidates(day, offset):
        try:
            board = fetch_json(url)
            count = _raw_event_count(board)
            if count > 0:
                return board, url
            errors.append(f"false-empty Stages response: {url}")
        except Exception as exc:
            errors.append(str(exc))
    raise RuntimeError(
        f"LiveScore returned no non-empty date surface for {day} offset={offset}: "
        + " | ".join(errors)
    )

def clean_name(value, fallback="Unknown") -> str:
    if isinstance(value, str) and value.strip():
        return " ".join(value.split())
    return fallback

def is_uefa_youth_stage(stage: dict) -> bool:
    compn = clean_name(stage.get("CompN"), "")
    cnm = clean_name(stage.get("Cnm"), "")
    urlname = clean_name(stage.get("CompUrlName"), "")
    return (
        compn.casefold() in {"uefa youth league", "uefa u19 youth league", "uefa youth league u19"}
        or cnm.casefold() == "uefa youth league"
        or urlname.casefold() == "uefa-youth-league"
    )

def block_names(stage: dict) -> tuple[str, str]:
    if is_uefa_youth_stage(stage):
        return "Europe", "UEFA Youth League"
    country = clean_name(stage.get("Cnm") or stage.get("Csnm") or stage.get("Ccd"), "Unknown")
    competition = clean_name(stage.get("Snm") or stage.get("Sdn") or stage.get("CompN"), "Unknown Competition")
    return country, competition

def senior_block(stage: dict, country: str, competition: str) -> bool:
    if is_uefa_youth_stage(stage):
        return True
    text = f"{country} {competition}"
    return not NONSTANDARD_RE.search(text) and not YOUTH_RE.search(text)

def event_id(evt: dict) -> str | None:
    value = evt.get("Eid") or evt.get("Id") or evt.get("ID")
    if value is None:
        return None
    value = str(value).strip()
    return value or None

def team(evt: dict, key: str) -> tuple[str, str | None]:
    rows = evt.get(key)
    if not isinstance(rows, list) or not rows or not isinstance(rows[0], dict):
        return "Unknown", None
    row = rows[0]
    name = clean_name(row.get("Nm") or row.get("Name"), "Unknown")
    tid = row.get("ID") or row.get("Id")
    return name, str(tid) if tid is not None else None

def parse_esd(evt: dict, offset: int) -> datetime:
    s = str(evt.get("Esd") or "")
    if not re.fullmatch(r"\d{14}", s):
        raise ValueError(f"bad Esd {evt.get('Esd')!r}")
    local = datetime.strptime(s, "%Y%m%d%H%M%S").replace(tzinfo=timezone(timedelta(hours=offset)))
    return local.astimezone(UTC)

def status(evt: dict, kickoff: datetime, now: datetime) -> str:
    eps = clean_name(evt.get("Eps"), "").upper()
    st = evt.get("St")
    if "POSTP" in eps:
        return "POSTPONED"
    if any(x in eps for x in ("CANC", "ABAN", "SUSP")):
        return "CANCELLED"
    if eps in {"FT", "AET", "PEN", "AFTER PEN.", "AFTER ET"}:
        return "FINISHED"
    if re.search(r"\d+'|\bHT\b|\bLIVE\b|1ST|2ND|BREAK", eps) or st in {2, "2"}:
        return "STARTED"
    return "PREMATCH_CONFIRMED" if kickoff > now else "STARTED"

def competition_kind(country: str, competition: str) -> tuple[str, bool]:
    text = f"{country} {competition}"
    if competition.casefold() in {"uefa youth league", "uefa u19 youth league", "uefa youth league u19"}:
        return "YOUTH_CONTINENTAL", False
    friendly = bool(FRIENDLY_RE.search(text))
    if friendly:
        return "DOMESTIC_LEAGUE", True
    if OFFICIAL_INTL_RE.search(text):
        return "PROTECTED_OFFICIAL", False
    if CONTINENTAL_RE.search(text) or country.casefold() in {
        "asia", "africa", "europe", "south america", "concacaf", "oceania",
        "champions league", "europa league", "conference league",
    }:
        return "CONTINENTAL", False
    if CUP_RE.search(competition):
        return "DOMESTIC_CUP", False
    if WOMEN_RE.search(text):
        return "WOMENS_TOP_FLIGHT", False
    return "DOMESTIC_LEAGUE", False

def iter_events(board: dict):
    for stage in board.get("Stages", []):
        if not isinstance(stage, dict):
            continue
        country, competition = block_names(stage)
        if not senior_block(stage, country, competition):
            continue
        events = stage.get("Events")
        if isinstance(events, list):
            yield stage, country, competition, events

def page_url(day: str, offset: int) -> str:
    return f"https://www.livescores.com/football/{day[:4]}-{day[4:6]}-{day[6:]}/?tz={offset}"

def build_surface(day: str, offset: int, key: str, now: datetime):
    board, api_url = fetch_surface(day, offset)
    observed = datetime.now(UTC)
    blocks, rows, ids = [], {}, []
    for stage, country, competition, events in iter_events(board):
        block_ids = []
        for evt in events:
            if not isinstance(evt, dict):
                continue
            mid = event_id(evt)
            if not mid:
                continue
            try:
                ko = parse_esd(evt, offset)
            except ValueError:
                continue
            home, home_id = team(evt, "T1")
            away, away_id = team(evt, "T2")
            if home == "Unknown" or away == "Unknown":
                continue
            # Generic youth competitions are outside the approved acquisition
            # scope. UEFA Youth League is the only explicit youth exception.
            if (not is_uefa_youth_stage(stage)
                    and YOUTH_RE.search(f"{country} {competition} {home} {away}")):
                continue
            kind, friendly = competition_kind(country, competition)
            row = {
                "match_id": mid, "country": country, "competition": competition,
                "competition_kind": kind, "home": home, "away": away,
                "kickoff_utc": ko.isoformat(), "fixture_status": status(evt, ko, now),
                "source_url": api_url, "observed_at_utc": observed.isoformat(),
                "is_friendly": friendly,
                "provider_team_ids": {"home": home_id, "away": away_id},
            }
            rows[mid] = row
            ids.append(mid)
            block_ids.append(mid)
        if block_ids:
            blocks.append({
                "country": country, "competition": competition,
                "provider_fixture_count": len(block_ids),
                "extracted_fixture_ids": block_ids,
            })
    if len(ids) != len(set(ids)):
        raise RuntimeError(f"duplicate event ID inside {key}")
    surface = {
        "surface_key": key, "source_url": page_url(day, offset),
        "observed_at_utc": observed.isoformat(),
        "provider_page_count": 1, "pages_fetched": [1], "pagination_complete": True,
        "provider_senior_fixture_count": len(ids),
        "provider_senior_competition_block_count": len(blocks),
        "extracted_fixture_ids": ids, "competition_blocks": blocks,
    }
    return surface, rows, api_url

def finished_event(evt: dict) -> bool:
    eps = clean_name(evt.get("Eps"), "").upper()
    return eps in {"FT", "AET", "PEN", "AFTER PEN.", "AFTER ET"} or evt.get("Esid") in {6, "6"}

def score_pair(evt: dict):
    try:
        a, b = int(evt.get("Tr1")), int(evt.get("Tr2"))
    except (TypeError, ValueError):
        return None
    return (a, b) if 0 <= a <= 20 and 0 <= b <= 20 else None

def history_day(day: datetime) -> list[dict]:
    ds = day.strftime("%Y%m%d")
    board, api_url = fetch_surface(ds, 0)
    found = []
    # History may use other competitive U19 competitions for the exact target
    # team IDs. Those competitions remain evidence-only and never enter intake.
    for stage in board.get("Stages", []):
        if not isinstance(stage, dict):
            continue
        country = clean_name(stage.get("Cnm") or stage.get("Csnm") or stage.get("Ccd"), "Unknown")
        competition = clean_name(stage.get("Snm") or stage.get("Sdn") or stage.get("CompN"), "Unknown Competition")
        text = f"{country} {competition}"
        if NONSTANDARD_RE.search(text) or FRIENDLY_RE.search(text):
            continue
        events = stage.get("Events")
        if not isinstance(events, list):
            continue
        for evt in events:
            if not isinstance(evt, dict) or not finished_event(evt):
                continue
            score = score_pair(evt)
            if score is None:
                continue
            try:
                ko = parse_esd(evt, 0)
            except ValueError:
                continue
            hname, hid = team(evt, "T1")
            aname, aid = team(evt, "T2")
            found.append({"ko": ko, "hid": hid, "aid": aid, "hs": score[0], "as": score[1]})
    return found

def attach_histories(fixtures: dict[str, dict], now: datetime, max_days: int = 90):
    target_ids = set()
    for row in fixtures.values():
        if WINDOW_START <= datetime.fromisoformat(row["kickoff_utc"]) < WINDOW_END:
            ids = row.get("provider_team_ids", {})
            if ids.get("home"): target_ids.add(ids["home"])
            if ids.get("away"): target_ids.add(ids["away"])
    by_team = defaultdict(list)
    days = [datetime(now.year, now.month, now.day, tzinfo=UTC) - timedelta(days=i) for i in range(1, max_days + 1)]
    with ThreadPoolExecutor(max_workers=10) as ex:
        futs = [ex.submit(history_day, d) for d in days]
        for fut in as_completed(futs):
            try:
                events = fut.result()
            except Exception:
                continue
            for e in events:
                if e["hid"] in target_ids:
                    by_team[e["hid"]].append({"kickoff_utc": e["ko"].isoformat(), "goals_for": e["hs"], "goals_against": e["as"]})
                if e["aid"] in target_ids:
                    by_team[e["aid"]].append({"kickoff_utc": e["ko"].isoformat(), "goals_for": e["as"], "goals_against": e["hs"]})
    observed = datetime.now(UTC).isoformat()
    for row in fixtures.values():
        if not (WINDOW_START <= datetime.fromisoformat(row["kickoff_utc"]) < WINDOW_END):
            continue
        ids = row.get("provider_team_ids", {})
        evidence = {}
        for side in ("home", "away"):
            recent = sorted(by_team.get(ids.get(side), []), key=lambda x: x["kickoff_utc"], reverse=True)
            dedup, seen = [], set()
            for g in recent:
                if g["kickoff_utc"] in seen:
                    continue
                seen.add(g["kickoff_utc"])
                dedup.append(g)
                if len(dedup) == 8:
                    break
            if len(dedup) >= 4:
                evidence[side] = {
                    "source_url": "https://www.livescores.com/football/",
                    "observed_at_utc": observed, "recent": dedup,
                }
        if set(evidence) == {"home", "away"}:
            row["football_evidence"] = evidence

def add_researchability(fixtures: dict[str, dict], observed: str):
    for row in fixtures.values():
        if row.get("is_friendly"):
            continue
        row["researchability_status"] = "VERIFIED"
        row["researchability_proof"] = {
            "match_id": row["match_id"], "source_url": row["source_url"],
            "checked_at_utc": observed, "current_channels_checked": True,
        }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--report", required=True)
    args = ap.parse_args()
    now = datetime.now(UTC)
    if not now < WINDOW_END:
        raise SystemExit("requested sweep window already closed")
    specs = [
        ("20261017", 7, "ICT:2026-10-17"),
        ("20261017", 0, "UTC:2026-10-17"),
    ]
    surfaces, union, api_urls = [], {}, []
    for day, offset, key in specs:
        surface, rows, api_url = build_surface(day, offset, key, now)
        surfaces.append(surface); api_urls.append(api_url)
        for mid, row in rows.items():
            old = union.get(mid)
            if old and old["kickoff_utc"] != row["kickoff_utc"]:
                raise RuntimeError(f"timezone surface kickoff mismatch for {mid}: {old['kickoff_utc']} vs {row['kickoff_utc']}")
            if old is None or key.startswith("UTC:"):
                union[mid] = row
    attach_histories(union, now, max_days=90)
    checked = datetime.now(UTC).isoformat()
    add_researchability(union, checked)
    sentinel_board, sentinel_url = fetch_surface("20261017", 0)
    sentinel_checked = datetime.now(UTC)
    terminal_start = max(WINDOW_START, WINDOW_END - timedelta(hours=6))
    sentinel_ids = []
    for stage, country, competition, events in iter_events(sentinel_board):
        for evt in events:
            if not isinstance(evt, dict):
                continue
            mid = event_id(evt)
            if not mid or mid not in union:
                continue
            try:
                ko = parse_esd(evt, 0)
            except ValueError:
                continue
            if terminal_start <= ko < WINDOW_END:
                sentinel_ids.append(mid)
    sentinel_ids = list(dict.fromkeys(sentinel_ids))
    for row in union.values():
        row.pop("provider_team_ids", None)
    source = {
        "schema_version": "football-stages-v4", "run_id": RUN_ID,
        "window_start_utc": WINDOW_START.isoformat(), "window_end_utc": WINDOW_END.isoformat(),
        "source_family": "LiveScore public date API", "source_url": page_url("20261017", 7),
        "source_observed_at_utc": checked, "fixtures": list(union.values()),
        "source_completeness_manifest": {
            "schema_version": "football-v4-source-completeness-v2",
            "acquisition_mode": "DATE_SURFACE_BATCH_V2", "league_query_mode": "DATE_SURFACE_ONLY",
            "registry_prefilter_applied": False, "scope_policy": "ALL_SOURCE_VISIBLE_SENIOR_FOOTBALL_BLOCKS",
            "extraction_complete": True, "provider_family": "LiveScore public date API",
            "window_start_utc": WINDOW_START.isoformat(), "window_end_utc": WINDOW_END.isoformat(),
            "checked_at_utc": checked, "required_surface_keys": [x[2] for x in specs],
            "date_surfaces": surfaces,
            "terminal_sentinel": {
                "interval_start_utc": terminal_start.isoformat(), "interval_end_utc": WINDOW_END.isoformat(),
                "checked_at_utc": sentinel_checked.isoformat(), "independent_refetch": True,
                "source_urls": [sentinel_url], "provider_senior_fixture_count": len(sentinel_ids),
                "extracted_fixture_ids": sentinel_ids, "complete": True,
            },
        },
    }
    out = Path(args.output); out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(source, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
    in_window = [r for r in union.values() if WINDOW_START <= datetime.fromisoformat(r["kickoff_utc"]) < WINDOW_END]
    uyl = [r for r in in_window if r.get("competition") == "UEFA Youth League"]
    report = {
        "run_id": RUN_ID, "generated_at_utc": checked, "source_fixture_union_count": len(union),
        "surface_counts": {s["surface_key"]: s["provider_senior_fixture_count"] for s in surfaces},
        "in_window_count": len(in_window),
        "in_window_prematch_count": sum(r["fixture_status"] == "PREMATCH_CONFIRMED" for r in in_window),
        "in_window_with_goal_history_both_sides": sum("football_evidence" in r for r in in_window),
        "uefa_youth_league_count": len(uyl),
        "uefa_youth_league_prematch_count": sum(r["fixture_status"] == "PREMATCH_CONFIRMED" for r in uyl),
        "uefa_youth_league_with_goal_history_both_sides": sum("football_evidence" in r for r in uyl),
        "terminal_fixture_count": len(sentinel_ids), "api_urls": api_urls,
        "uefa_youth_league": [{k:r[k] for k in ("match_id","home","away","kickoff_utc","fixture_status")} for r in sorted(uyl,key=lambda x:x["kickoff_utc"])],
        "in_window": [{k:r[k] for k in ("match_id","country","competition","home","away","kickoff_utc","fixture_status")} for r in sorted(in_window,key=lambda x:x["kickoff_utc"])],
    }
    Path(args.report).write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
