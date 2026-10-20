"""Executable Work fallback: full date evidence -> team research -> native V4.

No model logic lives here. All admission decisions belong to stage.sweep.
Provider failures and unsupported channel/format evidence remain checkpointed.
"""
from __future__ import annotations

import argparse
import hashlib
import html as html_lib
import json
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from league_registry import classify
from source_completeness import required_surface_keys
from stage import sweep
from work_source_acquisition import fetch, parse_request

FAMILY = "LiveScore public date API"
DATE_URL = "https://prod-public-api.livescore.com/v1/api/app/date/soccer/{day}/{offset}?MD=1&countryCode=US&locale=en"
REACT_DATE_URL = "https://prod-public-api.livescore.com/v1/api/react/date/soccer/{day}/{offset}.00?MD=1&countryCode=US&locale=en"
TEAM_URL = "https://prod-cdn-team-api.lsmedia1.com/v1/api/app/team/{team}/details?locale=en"
SOFASCORE_FAMILY = "SofaScore public scheduled-events API"
SOFASCORE_DATE_URLS = (
    "https://www.sofascore.com/api/v1/sport/football/scheduled-events/{day}",
    "https://api.sofascore.com/api/v1/sport/football/scheduled-events/{day}",
)
SOFASCORE_TEAM_LAST_URL = "https://api.sofascore.com/api/v1/team/{team}/events/last/{page}"
SOFASCORE_EVENT_URL = "https://api.sofascore.com/api/v1/event/{match}"
FOOTBALLINFO_FAMILY = "FootballInfo complete fixtures HTML"
FOOTBALLINFO_DATE_URL = "https://www.footballinfo.net/Fixtures?date={day}"
FOOTBALLINFO_TEAM_URL = "https://www.footballinfo.net/Teams/Details/{team}"
FOOTBALLINFO_EVENT_URL = "https://www.footballinfo.net/Fixtures/Details/{match}"
THESPORTSDB_FAMILY = "TheSportsDB public eventsday API"
THESPORTSDB_DATE_URL = "https://www.thesportsdb.com/api/v1/json/123/eventsday.php?d={day}&s=Soccer"
THESPORTSDB_TEAM_LAST_URL = "https://www.thesportsdb.com/api/v1/json/123/eventslast.php?id={team}"
THESPORTSDB_EVENT_URL = "https://www.thesportsdb.com/api/v1/json/123/lookupevent.php?id={match}"


def utcnow():
    return datetime.now(timezone.utc).isoformat()


def stamp(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def save(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temp.replace(path)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


CHECKPOINT_SCHEMA = "football-v4-sweep-research-checkpoint-v2"
RESOLVED_RESEARCH = {"COMPLETE", "EVIDENCE_LIMITED", "STATUS_EXCLUDED"}
STATIC_EVIDENCE_GAPS = {
    "PROVIDER_TEAM_ID_MAPPING_REQUIRED",
    "CURRENT_MECHANISM_STAT_NEWS_CHANNEL_PROOF_REQUIRED",
}


def _resolved(state):
    return isinstance(state, dict) and state.get("research_disposition") in RESOLVED_RESEARCH


def _finish_research_state(state):
    reasons = list(dict.fromkeys(state.get("pending_reasons") or []))
    state["pending_reasons"] = reasons
    if not reasons:
        state["research_disposition"] = "COMPLETE"
        return
    static = all(
        reason in STATIC_EVIDENCE_GAPS
        or reason.endswith("_COMPETITIVE_HISTORY_UNDER_FOUR")
        for reason in reasons
    )
    attempts = int(state.get("attempt_count") or 1)
    if static or attempts >= 2:
        state["research_disposition"] = "EVIDENCE_LIMITED"
        if attempts >= 2 and not static:
            state["retry_exhausted"] = True
    else:
        state["research_disposition"] = "RESEARCH_PENDING"


def _resume_queue(checkpoint):
    order = checkpoint.get("research_order") or []
    states = checkpoint.get("fixtures") or {}
    return [mid for mid in order if not _resolved(states.get(mid))]


def event_time(event, surface_offset_hours=0):
    # LiveScore returns Esd in the timezone requested by the date endpoint.
    # Normalize ICT and UTC views to one instant before merging date surfaces.
    source_tz = timezone(timedelta(hours=surface_offset_hours))
    return datetime.strptime(str(event["Esd"]), "%Y%m%d%H%M%S").replace(
        tzinfo=source_tz
    ).astimezone(timezone.utc).isoformat()


def event_identity(event):
    return tuple(str(event[side][0]["ID"]) for side in ("T1", "T2"))


def event_status(event):
    status = str(event.get("Eps", "")).upper()
    if status == "NS" and event.get("Esid") == 1:
        return "PREMATCH_CONFIRMED"
    if status in {"FT", "AET", "AP"}:
        return "FINISHED"
    if status in {"POSTP", "POSTPONED", "PST"}:
        return "POSTPONED"
    if status in {"CANC", "CANCELLED", "ABANDONED", "AWD"}:
        return "CANCELLED"
    if status in {"HT", "ET", "BT", "PEN"} or re.fullmatch(r"\d+(?:\+\d+)?'?", status):
        return "STARTED"
    # Never silently turn unknown provider codes into a confirmed fixture.
    return "UNKNOWN_PROVIDER_STATUS"


def senior(stage):
    label = stage["Snm"] + " " + (stage.get("Cnm") or stage.get("Csnm") or "")
    if "uefa youth league" in label.lower():
        return True
    if any(x in label.lower() for x in ("premier league 2", "primavera")):
        return False
    # Team names are intentionally absent: a U23 team can play an adult league.
    return not re.search(r"\b(?:u[ -]?(?:1[5-9]|2[0-3])|under[ -]?(?:1[5-9]|2[0-3])|youth)\b", label, re.I)


def competition_kind(stage):
    name = stage["Snm"].lower()
    country = (stage.get("Cnm") or stage.get("Csnm") or "").lower()
    if "uefa youth league" in name:
        return "YOUTH_CONTINENTAL"
    if country in {"international", "world", "europe", "asia", "africa", "south america", "north america", "oceania"}:
        if any(x in name for x in ("champions league", "europa league", "conference league", "libertadores", "sudamericana")):
            return "CONTINENTAL"
        # Generic international labels must not manufacture protected status.
        return "UNVERIFIED"
    if any(x in name for x in ("cup", "copa", "trophy", "pokal", "coupe", "beker")):
        return "DOMESTIC_CUP"
    return "DOMESTIC_LEAGUE"


def stage_blocks(payload):
    if not isinstance(payload, dict) or not isinstance(payload.get("Stages"), list):
        raise ValueError("provider date response lacks full Stages array")
    # The date endpoint is a single full-array surface. Stop on contract drift.
    for key in payload:
        if any(word in key.lower() for word in ("pagination", "nextpage", "hasmore", "cursor")):
            raise ValueError("provider pagination contract changed: " + key)
    seen = set()
    result = []
    for block in payload["Stages"]:
        if not isinstance(block.get("Events"), list) or not block.get("Snm"):
            raise ValueError("malformed competition block")
        if not (block.get("Cnm") or block.get("Csnm")):
            raise ValueError("competition country absent")
        if not senior(block):
            continue
        for event in block["Events"]:
            mid = str(event["Eid"])
            if not mid or mid == "None" or mid in seen:
                raise ValueError("missing/duplicate provider event ID")
            seen.add(mid)
            event_identity(event)
            event_time(event)
        result.append(block)
    return result


class Evidence:
    def __init__(self, output):
        self.output = output
        self.index = []

    def get(self, url, name):
        raw, observed = fetch(url)
        payload = json.loads(raw)
        path = self.output / "raw" / (name + ".json")
        path.parent.mkdir(parents=True, exist_ok=True)
        # An invocation writes into a fresh output directory; no evidence overwrite.
        path.write_bytes(raw)
        item = {"source_url": url, "observed_at_utc": observed,
                "file": str(path.relative_to(self.output)), "sha256": digest(path)}
        self.index.append(item)
        save(self.output / "provenance.json", self.index)
        return payload, item

    def get_text(self, url, name):
        raw, observed = fetch(url)
        text = raw.decode("utf-8", errors="strict")
        path = self.output / "raw" / (name + ".html")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
        item = {"source_url": url, "observed_at_utc": observed,
                "file": str(path.relative_to(self.output)), "sha256": digest(path)}
        self.index.append(item)
        save(self.output / "provenance.json", self.index)
        return text, item


def date_surface(evidence, day: str, offset: int, name: str):
    """Fetch one LiveScore date surface, preserving the exact successful URL.

    /app/date remains primary. /react/date is a same-provider schema-compatible
    transport fallback used only when the primary route is unavailable.
    """
    primary = DATE_URL.format(day=day, offset=offset)
    try:
        return evidence.get(primary, name)
    except Exception as primary_exc:
        fallback = REACT_DATE_URL.format(day=day, offset=offset)
        try:
            return evidence.get(fallback, name + "-react")
        except Exception as fallback_exc:
            raise RuntimeError(
                f"LiveScore date surface failed on app and react routes: "
                f"{primary_exc}; {fallback_exc}"
            ) from fallback_exc


def acquire_livescore(request, evidence):
    start, end, _ = parse_request(request)
    start, end = start.astimezone(timezone.utc), end.astimezone(timezone.utc)
    keys = required_surface_keys(start.isoformat(), end.isoformat())
    fixtures, identities, surfaces = {}, {}, []
    for key in keys:
        basis, day = key.split(":")
        offset = 7 if basis == "ICT" else 0
        requested_day = day.replace("-", "")
        payload, proof = date_surface(evidence, requested_day, offset, key.replace(":", "-"))
        url = proof["source_url"]
        blocks, ids = [], []
        for block in stage_blocks(payload):
            mids = [str(e["Eid"]) for e in block["Events"]]
            blocks.append({"country": block.get("Cnm") or block["Csnm"], "competition": block["Snm"],
                           "provider_fixture_count": len(mids), "extracted_fixture_ids": mids})
            ids.extend(mids)
            for event in block["Events"]:
                mid = str(event["Eid"])
                identity = event_identity(event)
                if mid in identities and identities[mid] != identity:
                    raise ValueError("conflicting date-surface team identity: " + mid)
                if mid in fixtures and fixtures[mid]["kickoff_utc"] != event_time(event, offset):
                    raise ValueError("conflicting date-surface kickoff: " + mid)
                identities[mid] = identity
                fixtures[mid] = {"match_id": mid, "country": block.get("Cnm") or block["Csnm"],
                                 "competition": block["Snm"], "competition_kind": competition_kind(block),
                                 "is_friendly": any(x in block["Snm"].lower() for x in ("friendly", "friendlies")),
                                 "home": event["T1"][0]["Nm"], "away": event["T2"][0]["Nm"],
                                 "kickoff_utc": event_time(event, offset), "fixture_status": event_status(event),
                                 "source_url": url, "observed_at_utc": proof["observed_at_utc"],
                                 "provider_team_ids": list(identity)}
        surfaces.append({"surface_key": key, "source_url": url, "observed_at_utc": proof["observed_at_utc"],
                         "pagination_complete": True, "provider_page_count": 1, "pages_fetched": [1],
                         "provider_senior_fixture_count": len(ids), "extracted_fixture_ids": ids,
                         "provider_senior_competition_block_count": len(blocks), "competition_blocks": blocks})
    terminal_start = max(start, end - timedelta(hours=6))
    terminal_ids, terminal_proofs = set(), []
    for key in required_surface_keys(terminal_start.isoformat(), end.isoformat()):
        if not key.startswith("UTC:"):
            continue
        day = key.split(":")[1]
        requested_day = day.replace("-", "")
        payload, proof = date_surface(evidence, requested_day, 0, "terminal-" + day)
        url = proof["source_url"]
        terminal_proofs.append(proof)
        for block in stage_blocks(payload):
            for event in block["Events"]:
                mid = str(event["Eid"])
                if terminal_start <= stamp(event_time(event)) < end:
                    terminal_ids.add(mid)
                    if mid in fixtures and (event_identity(event) != identities[mid] or event_time(event) != fixtures[mid]["kickoff_utc"]):
                        raise ValueError("terminal identity/kickoff changed: " + mid)
                if mid in fixtures:
                    fixtures[mid].update(fixture_status=event_status(event), observed_at_utc=proof["observed_at_utc"], source_url=url)
    now = utcnow()
    return {"schema_version": "football-stages-v4", "run_id": request["run_id"],
            "window_start_utc": start.isoformat(), "window_end_utc": end.isoformat(),
            "source_family": FAMILY, "source_url": surfaces[0]["source_url"],
            "source_observed_at_utc": max(x["observed_at_utc"] for x in surfaces),
            "fixtures": list(fixtures.values()),
            "source_completeness_manifest": {
                "schema_version": "football-v4-source-completeness-v2", "acquisition_mode": "DATE_SURFACE_BATCH_V2",
                "league_query_mode": "DATE_SURFACE_ONLY", "registry_prefilter_applied": False,
                "scope_policy": "ALL_SOURCE_VISIBLE_SENIOR_FOOTBALL_BLOCKS", "extraction_complete": True,
                "provider_family": FAMILY, "window_start_utc": start.isoformat(), "window_end_utc": end.isoformat(),
                "checked_at_utc": now, "required_surface_keys": keys, "date_surfaces": surfaces,
                "terminal_sentinel": {"interval_start_utc": terminal_start.isoformat(), "interval_end_utc": end.isoformat(),
                    "checked_at_utc": max(x["observed_at_utc"] for x in terminal_proofs),
                    "complete": True, "independent_refetch": True,
                    "source_urls": [x["source_url"] for x in terminal_proofs],
                    "provider_senior_fixture_count": len(terminal_ids), "extracted_fixture_ids": sorted(terminal_ids)}}}


def sofascore_event_time(event):
    value = event.get("startTimestamp")
    if isinstance(value, bool) or not isinstance(value, (int, float)) or value <= 0:
        raise ValueError("SofaScore event startTimestamp required")
    return datetime.fromtimestamp(value, tz=timezone.utc).isoformat()


def sofascore_event_identity(event):
    try:
        return (str(event["homeTeam"]["id"]), str(event["awayTeam"]["id"]))
    except (KeyError, TypeError) as exc:
        raise ValueError("SofaScore home/away identity missing") from exc


def sofascore_event_status(event):
    value = str((event.get("status") or {}).get("type") or "").lower()
    if value in {"notstarted", "not_started"}:
        return "PREMATCH_CONFIRMED"
    if value == "finished":
        return "FINISHED"
    if value in {"postponed", "delayed"}:
        return "POSTPONED"
    if value in {"canceled", "cancelled", "abandoned"}:
        return "CANCELLED"
    if value in {"inprogress", "in_progress", "live"}:
        return "STARTED"
    return "UNKNOWN_PROVIDER_STATUS"


def sofascore_stage(event):
    tournament = event.get("tournament") or {}
    category = tournament.get("category") or {}
    competition = tournament.get("name") or (tournament.get("uniqueTournament") or {}).get("name")
    country = category.get("name")
    if not isinstance(competition, str) or not competition.strip():
        raise ValueError("SofaScore competition missing")
    if not isinstance(country, str) or not country.strip():
        country = "International"
    return {"Snm": competition.strip(), "Cnm": country.strip()}


def sofascore_senior(event):
    stage = sofascore_stage(event)
    label = stage["Snm"] + " " + stage["Cnm"]
    if "uefa youth league" in label.lower():
        return True
    if any(x in label.lower() for x in ("premier league 2", "primavera")):
        return False
    return not re.search(r"\b(?:u[ -]?(?:1[5-9]|2[0-3])|under[ -]?(?:1[5-9]|2[0-3])|youth)\b", label, re.I)


def sofascore_events(payload):
    if not isinstance(payload, dict) or not isinstance(payload.get("events"), list):
        raise ValueError("SofaScore scheduled-events response missing events")
    if payload.get("hasNextPage") is True:
        raise ValueError("SofaScore scheduled-events pagination unexpectedly required")
    seen = set()
    rows = []
    for event in payload["events"]:
        mid = str(event.get("id"))
        if not mid or mid == "None" or mid in seen:
            raise ValueError("SofaScore missing/duplicate event ID")
        seen.add(mid)
        sofascore_event_identity(event)
        sofascore_event_time(event)
        if sofascore_senior(event):
            rows.append(event)
    return rows


def sofascore_date_surface(evidence, day, name):
    errors = []
    for index, template in enumerate(SOFASCORE_DATE_URLS):
        url = template.format(day=day)
        try:
            return evidence.get(url, name + ("-www" if index == 0 else "-api"))
        except Exception as exc:
            errors.append(str(exc))
    raise RuntimeError("SofaScore date surface failed: " + "; ".join(errors))


def acquire_sofascore(request, evidence):
    start, end, _ = parse_request(request)
    start, end = start.astimezone(timezone.utc), end.astimezone(timezone.utc)
    keys = required_surface_keys(start.isoformat(), end.isoformat())
    fixtures, identities, surfaces = {}, {}, []

    for key in keys:
        _, day = key.split(":")
        payload, proof = sofascore_date_surface(evidence, day, "sofa-" + key.replace(":", "-"))
        events = sofascore_events(payload)
        grouped = {}
        ids = []
        for event in events:
            mid = str(event["id"])
            identity = sofascore_event_identity(event)
            kickoff = sofascore_event_time(event)
            stage = sofascore_stage(event)
            group_key = (stage["Cnm"], stage["Snm"])
            grouped.setdefault(group_key, []).append(mid)
            ids.append(mid)
            if mid in identities and identities[mid] != identity:
                raise ValueError("conflicting SofaScore date-surface team identity: " + mid)
            if mid in fixtures and fixtures[mid]["kickoff_utc"] != kickoff:
                raise ValueError("conflicting SofaScore date-surface kickoff: " + mid)
            identities[mid] = identity
            fixtures[mid] = {
                "match_id": mid,
                "country": stage["Cnm"],
                "competition": stage["Snm"],
                "competition_kind": competition_kind(stage),
                "is_friendly": any(x in stage["Snm"].lower() for x in ("friendly", "friendlies")),
                "home": event["homeTeam"]["name"],
                "away": event["awayTeam"]["name"],
                "kickoff_utc": kickoff,
                "fixture_status": sofascore_event_status(event),
                "source_url": proof["source_url"],
                "observed_at_utc": proof["observed_at_utc"],
                "provider_team_ids": list(identity),
            }
        blocks = [
            {"country": country, "competition": competition,
             "provider_fixture_count": len(mids), "extracted_fixture_ids": mids}
            for (country, competition), mids in sorted(grouped.items())
        ]
        surfaces.append({
            "surface_key": key,
            "source_url": proof["source_url"],
            "observed_at_utc": proof["observed_at_utc"],
            "pagination_complete": True,
            "provider_page_count": 1,
            "pages_fetched": [1],
            "provider_senior_fixture_count": len(ids),
            "extracted_fixture_ids": ids,
            "provider_senior_competition_block_count": len(blocks),
            "competition_blocks": blocks,
        })

    terminal_start = max(start, end - timedelta(hours=6))
    terminal_ids, terminal_proofs = set(), []
    for key in required_surface_keys(terminal_start.isoformat(), end.isoformat()):
        if not key.startswith("UTC:"):
            continue
        day = key.split(":")[1]
        payload, proof = sofascore_date_surface(evidence, day, "sofa-terminal-" + day)
        terminal_proofs.append(proof)
        for event in sofascore_events(payload):
            mid = str(event["id"])
            kickoff = sofascore_event_time(event)
            if terminal_start <= stamp(kickoff) < end:
                terminal_ids.add(mid)
                if mid in fixtures and (
                    sofascore_event_identity(event) != identities[mid]
                    or kickoff != fixtures[mid]["kickoff_utc"]
                ):
                    raise ValueError("SofaScore terminal identity/kickoff changed: " + mid)
            if mid in fixtures:
                fixtures[mid].update(
                    fixture_status=sofascore_event_status(event),
                    observed_at_utc=proof["observed_at_utc"],
                    source_url=proof["source_url"],
                )

    now = utcnow()
    return {
        "schema_version": "football-stages-v4",
        "run_id": request["run_id"],
        "window_start_utc": start.isoformat(),
        "window_end_utc": end.isoformat(),
        "source_family": SOFASCORE_FAMILY,
        "source_url": surfaces[0]["source_url"],
        "source_observed_at_utc": max(x["observed_at_utc"] for x in surfaces),
        "fixtures": list(fixtures.values()),
        "source_completeness_manifest": {
            "schema_version": "football-v4-source-completeness-v2",
            "acquisition_mode": "DATE_SURFACE_BATCH_V2",
            "league_query_mode": "DATE_SURFACE_ONLY",
            "registry_prefilter_applied": False,
            "scope_policy": "ALL_SOURCE_VISIBLE_SENIOR_FOOTBALL_BLOCKS",
            "extraction_complete": True,
            "provider_family": SOFASCORE_FAMILY,
            "window_start_utc": start.isoformat(),
            "window_end_utc": end.isoformat(),
            "checked_at_utc": now,
            "required_surface_keys": keys,
            "date_surfaces": surfaces,
            "terminal_sentinel": {
                "interval_start_utc": terminal_start.isoformat(),
                "interval_end_utc": end.isoformat(),
                "checked_at_utc": max(x["observed_at_utc"] for x in terminal_proofs),
                "complete": True,
                "independent_refetch": True,
                "source_urls": [x["source_url"] for x in terminal_proofs],
                "provider_senior_fixture_count": len(terminal_ids),
                "extracted_fixture_ids": sorted(terminal_ids),
            },
        },
    }



def _footballinfo_text(value):
    if value is None:
        return ""
    no_tags = re.sub(r"<[^>]+>", " ", str(value))
    return re.sub(r"\s+", " ", html_lib.unescape(no_tags)).strip()


def _footballinfo_status(time_text, badge_text):
    time_value = _footballinfo_text(time_text).upper()
    badge = _footballinfo_text(badge_text).upper()
    if badge in {"NS", "NOT STARTED", "SCHEDULED"}:
        return "PREMATCH_CONFIRMED"
    if badge in {"FT", "AET", "AP", "PEN"}:
        return "FINISHED"
    if badge in {"POSTP", "POSTPONED", "PST"}:
        return "POSTPONED"
    if badge in {"CANC", "CANCELLED", "CANCELED", "ABANDONED", "AWD"}:
        return "CANCELLED"
    if badge == "LIVE" or "live" in str(time_text).lower() or re.fullmatch(r"\d+(?:\+\d+)?'?", time_value):
        return "STARTED"
    if re.fullmatch(r"\d{1,2}:\d{2}", time_value):
        return "PREMATCH_CONFIRMED"
    return "UNKNOWN_PROVIDER_STATUS"


def _footballinfo_datetime(day, time_text):
    value = _footballinfo_text(time_text)
    if not re.fullmatch(r"\d{1,2}:\d{2}", value):
        return None
    parsed = datetime.strptime(day + " " + value, "%Y-%m-%d %H:%M").replace(tzinfo=timezone.utc)
    return parsed.isoformat()


def footballinfo_date_events(text, day):
    if not isinstance(text, str) or "fi-league-section" not in text:
        raise ValueError("FootballInfo fixtures page missing league sections")
    section_matches = list(re.finditer(
        r'<div class="fi-league-section\b[^>]*data-fav-name="([^"]+)"[^>]*>',
        text, re.I
    ))
    if not section_matches:
        raise ValueError("FootballInfo fixtures page missing competition blocks")
    events = []
    seen = set()
    for index, section in enumerate(section_matches):
        start = section.start()
        end = section_matches[index + 1].start() if index + 1 < len(section_matches) else len(text)
        block = text[start:end]
        competition = _footballinfo_text(section.group(1))
        country_match = re.search(r'data-collapse-key="league:([^:"]+):\d+"', block, re.I)
        country = _footballinfo_text(country_match.group(1).replace("-", " ")) if country_match else "International"
        stage = {"Snm": competition, "Cnm": country}
        if not senior(stage):
            continue
        for match in re.finditer(
            r'<a class="fi-fixture[^"]*"[^>]*href="/Fixtures/Details/(\d+)"[^>]*>(.*?)</a>',
            block, re.I | re.S
        ):
            mid, frag = match.group(1), match.group(2)
            if mid in seen:
                raise ValueError("FootballInfo duplicate event ID")
            team_ids = re.findall(r'media\.api-sports\.io/football/teams/(\d+)\.png', frag, re.I)
            team_names = [
                _footballinfo_text(x)
                for x in re.findall(r'<span class="fi-team-name[^"]*"[^>]*>(.*?)</span>', frag, re.I | re.S)
            ]
            if len(team_ids) < 2 or len(team_names) < 2:
                raise ValueError("FootballInfo fixture team identity missing: " + mid)
            time_match = re.search(r'<div class="fi-fixture-time[^"]*"[^>]*>(.*?)</div>', frag, re.I | re.S)
            badge_match = re.search(r'<span class="fi-badge[^"]*"[^>]*>(.*?)</span>', frag, re.I | re.S)
            if not time_match:
                raise ValueError("FootballInfo fixture time/status missing: " + mid)
            time_text = _footballinfo_text(time_match.group(1))
            badge_text = _footballinfo_text(badge_match.group(1)) if badge_match else ""
            status = _footballinfo_status(time_text, badge_text)
            kickoff = _footballinfo_datetime(day, time_text)
            seen.add(mid)
            events.append({
                "match_id": mid,
                "country": country,
                "competition": competition,
                "home": team_names[0],
                "away": team_names[1],
                "provider_team_ids": [team_ids[0], team_ids[1]],
                "fixture_status": status,
                "kickoff_utc": kickoff,
            })
    return events


def footballinfo_fixture_detail(evidence, match):
    mid = str(match)
    text, proof = evidence.get_text(FOOTBALLINFO_EVENT_URL.format(match=mid), "fi-event-" + mid)
    meta_match = re.search(r'<div class="fi-match-meta"[^>]*>(.*?)</div>', text, re.I | re.S)
    if not meta_match:
        raise ValueError("FootballInfo fixture detail kickoff missing: " + mid)
    meta = _footballinfo_text(meta_match.group(1))
    # FootballInfo uses "Sept" on some historical pages while Python's
    # locale-independent %b parser expects "Sep".
    meta = re.sub(r"\bSept\b", "Sep", meta)
    meta_parts = re.search(
        r"(\d{1,2}\s+[A-Za-z]{3}\s+\d{4}).*?(\d{1,2}:\d{2})",
        meta
    )
    if not meta_parts:
        raise ValueError("FootballInfo fixture detail kickoff invalid: " + mid + ": " + meta)
    try:
        kickoff = datetime.strptime(
            meta_parts.group(1) + " " + meta_parts.group(2), "%d %b %Y %H:%M"
        ).replace(tzinfo=timezone.utc)
    except ValueError as exc:
        raise ValueError("FootballInfo fixture detail kickoff invalid: " + mid + ": " + meta) from exc
    team_matches = re.findall(
        r'href="/Teams/Details/(\d+)"[^>]*>.*?<div class="name">(.*?)</div>',
        text, re.I | re.S
    )
    if len(team_matches) < 2:
        raise ValueError("FootballInfo fixture detail team identity missing: " + mid)
    score_match = re.search(r'<div class="fi-match-score"[^>]*>(.*?)</div>', text, re.I | re.S)
    score = None
    if score_match:
        score_numbers = re.findall(r'\d+', _footballinfo_text(score_match.group(1)))
        if len(score_numbers) >= 2:
            score = (int(score_numbers[0]), int(score_numbers[1]))
    league_match = re.search(
        r'href="/Leagues/Details/\d+[^"]*"[^>]*>(.*?)</a>', text, re.I | re.S
    )
    competition = None
    if league_match:
        competition = _footballinfo_text(league_match.group(1)).split("·", 1)[0].strip()
    now = stamp(proof["observed_at_utc"])
    lowered = text.lower()
    if kickoff > now:
        status = "PREMATCH_CONFIRMED"
    elif "fi-badge-ft" in lowered or score is not None:
        status = "FINISHED"
    else:
        status = "STARTED"
    return {
        "match_id": mid,
        "kickoff_utc": kickoff.isoformat(),
        "provider_team_ids": [team_matches[0][0], team_matches[1][0]],
        "home": _footballinfo_text(team_matches[0][1]),
        "away": _footballinfo_text(team_matches[1][1]),
        "competition": competition,
        "score": score,
        "fixture_status": status,
    }, proof


def acquire_footballinfo(request, evidence):
    start, end, _ = parse_request(request)
    start, end = start.astimezone(timezone.utc), end.astimezone(timezone.utc)
    keys = required_surface_keys(start.isoformat(), end.isoformat())
    fixtures, identities, surfaces = {}, {}, []
    day_cache = {}
    detail_cache = {}

    for key in keys:
        _, day = key.split(":")
        if day not in day_cache:
            text, proof = evidence.get_text(
                FOOTBALLINFO_DATE_URL.format(day=day), "fi-date-" + day
            )
            day_cache[day] = (footballinfo_date_events(text, day), proof)
        rows, proof = day_cache[day]
        grouped = {}
        ids = []
        for raw in rows:
            row = dict(raw)
            mid = row["match_id"]
            if row["kickoff_utc"] is None:
                if mid not in detail_cache:
                    detail_cache[mid] = footballinfo_fixture_detail(evidence, mid)
                detail, _ = detail_cache[mid]
                if detail["provider_team_ids"] != row["provider_team_ids"]:
                    raise ValueError("FootballInfo detail/date team identity changed: " + mid)
                if detail["home"] != row["home"] or detail["away"] != row["away"]:
                    raise ValueError("FootballInfo detail/date team name changed: " + mid)
                row["kickoff_utc"] = detail["kickoff_utc"]
                row["fixture_status"] = detail["fixture_status"]
            identity = tuple(row["provider_team_ids"])
            if mid in identities and identities[mid] != identity:
                raise ValueError("conflicting FootballInfo date-surface team identity: " + mid)
            if mid in fixtures and fixtures[mid]["kickoff_utc"] != row["kickoff_utc"]:
                raise ValueError("conflicting FootballInfo date-surface kickoff: " + mid)
            identities[mid] = identity
            stage = {"Snm": row["competition"], "Cnm": row["country"]}
            fixtures[mid] = {
                "match_id": mid,
                "country": row["country"],
                "competition": row["competition"],
                "competition_kind": competition_kind(stage),
                "is_friendly": any(x in row["competition"].lower() for x in ("friendly", "friendlies")),
                "home": row["home"],
                "away": row["away"],
                "kickoff_utc": row["kickoff_utc"],
                "fixture_status": row["fixture_status"],
                "source_url": proof["source_url"],
                "observed_at_utc": proof["observed_at_utc"],
                "provider_team_ids": list(identity),
            }
            grouped.setdefault((row["country"], row["competition"]), []).append(mid)
            ids.append(mid)
        blocks = [
            {
                "country": country,
                "competition": competition,
                "provider_fixture_count": len(mids),
                "extracted_fixture_ids": mids,
            }
            for (country, competition), mids in grouped.items()
        ]
        surfaces.append({
            "surface_key": key,
            "source_url": proof["source_url"],
            "observed_at_utc": proof["observed_at_utc"],
            "pagination_complete": True,
            "provider_page_count": 1,
            "pages_fetched": [1],
            "provider_senior_fixture_count": len(ids),
            "extracted_fixture_ids": ids,
            "provider_senior_competition_block_count": len(blocks),
            "competition_blocks": blocks,
        })

    terminal_start = max(start, end - timedelta(hours=6))
    terminal_days = sorted({
        terminal_start.date().isoformat(),
        (end - timedelta(microseconds=1)).date().isoformat(),
    })
    terminal_ids = set()
    terminal_proofs = []
    for day in terminal_days:
        text, proof = evidence.get_text(
            FOOTBALLINFO_DATE_URL.format(day=day), "fi-terminal-" + day
        )
        terminal_proofs.append(proof)
        for raw in footballinfo_date_events(text, day):
            mid = raw["match_id"]
            kickoff_value = raw["kickoff_utc"]
            if kickoff_value is None:
                detail, _ = footballinfo_fixture_detail(evidence, mid)
                kickoff_value = detail["kickoff_utc"]
                current_status = detail["fixture_status"]
            else:
                current_status = raw["fixture_status"]
            kickoff = stamp(kickoff_value)
            if terminal_start <= kickoff < end:
                terminal_ids.add(mid)
                if mid in fixtures and (
                    tuple(raw["provider_team_ids"]) != identities[mid]
                    or kickoff_value != fixtures[mid]["kickoff_utc"]
                ):
                    raise ValueError("FootballInfo terminal identity/kickoff changed: " + mid)
            if mid in fixtures:
                fixtures[mid].update(
                    fixture_status=current_status,
                    observed_at_utc=proof["observed_at_utc"],
                    source_url=proof["source_url"],
                )

    now = utcnow()
    return {
        "schema_version": "football-stages-v4",
        "run_id": request["run_id"],
        "window_start_utc": start.isoformat(),
        "window_end_utc": end.isoformat(),
        "source_family": FOOTBALLINFO_FAMILY,
        "source_url": surfaces[0]["source_url"],
        "source_observed_at_utc": max(x["observed_at_utc"] for x in surfaces),
        "fixtures": list(fixtures.values()),
        "source_completeness_manifest": {
            "schema_version": "football-v4-source-completeness-v2",
            "acquisition_mode": "DATE_SURFACE_BATCH_V2",
            "league_query_mode": "DATE_SURFACE_ONLY",
            "registry_prefilter_applied": False,
            "scope_policy": "ALL_SOURCE_VISIBLE_SENIOR_FOOTBALL_BLOCKS",
            "extraction_complete": True,
            "provider_family": FOOTBALLINFO_FAMILY,
            "window_start_utc": start.isoformat(),
            "window_end_utc": end.isoformat(),
            "checked_at_utc": now,
            "required_surface_keys": keys,
            "date_surfaces": surfaces,
            "terminal_sentinel": {
                "interval_start_utc": terminal_start.isoformat(),
                "interval_end_utc": end.isoformat(),
                "checked_at_utc": max(x["observed_at_utc"] for x in terminal_proofs),
                "complete": True,
                "independent_refetch": True,
                "source_urls": [x["source_url"] for x in terminal_proofs],
                "provider_senior_fixture_count": len(terminal_ids),
                "extracted_fixture_ids": sorted(terminal_ids),
            },
        },
    }


def footballinfo_competitive_history(evidence, team, now):
    team = str(team)
    text, proof = evidence.get_text(
        FOOTBALLINFO_TEAM_URL.format(team=team), "fi-team-" + team
    )
    recent_marker = text.find("<!-- Recent fixtures -->")
    section = text[recent_marker:] if recent_marker >= 0 else text
    fixture_ids = []
    for match in re.finditer(
        r'<a class="fi-fixture[^"]*"[^>]*href="/Fixtures/Details/(\d+)"[^>]*>(.*?)</a>',
        section, re.I | re.S
    ):
        frag = match.group(2)
        badge_match = re.search(r'<span class="fi-badge[^"]*"[^>]*>(.*?)</span>', frag, re.I | re.S)
        badge = _footballinfo_text(badge_match.group(1)).upper() if badge_match else ""
        if badge == "FT":
            fixture_ids.append(match.group(1))
        if len(fixture_ids) >= 8:
            break
    results = {}
    for mid in fixture_ids:
        detail, _ = footballinfo_fixture_detail(evidence, mid)
        ids = tuple(detail["provider_team_ids"])
        if team not in ids:
            raise ValueError("unrelated event in FootballInfo team history")
        kickoff = stamp(detail["kickoff_utc"])
        if not now - timedelta(days=120) <= kickoff <= now - timedelta(hours=2):
            continue
        competition = detail.get("competition") or ""
        if any(x in competition.lower() for x in ("friendly", "friendlies", "testimonial")):
            continue
        if detail.get("score") is None:
            continue
        hg, ag = detail["score"]
        home = ids[0] == team
        row = {
            "event_id": mid,
            "kickoff_utc": kickoff.isoformat(),
            "goals_for": hg if home else ag,
            "goals_against": ag if home else hg,
            "competition": competition,
        }
        results[mid] = row
        if len(results) >= 6:
            break
    recent = sorted(results.values(), key=lambda x: x["kickoff_utc"], reverse=True)[:10]
    return recent, proof


def footballinfo_fixture_refresh(evidence, fixture):
    detail, proof = footballinfo_fixture_detail(evidence, fixture["match_id"])
    ids = tuple(map(str, fixture.get("provider_team_ids") or []))
    if tuple(detail["provider_team_ids"]) != ids:
        raise ValueError("FootballInfo event detail team identity changed")
    if detail["kickoff_utc"] != fixture["kickoff_utc"]:
        raise ValueError("FootballInfo event detail kickoff changed")
    return detail["fixture_status"], proof


def thesportsdb_event_time(event):
    value = event.get("strTimestamp")
    if not isinstance(value, str) or not value.strip():
        raise ValueError("TheSportsDB strTimestamp required")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("TheSportsDB invalid strTimestamp") from exc
    if parsed.tzinfo is None:
        # TheSportsDB occasionally omits the explicit +00:00 suffix while
        # keeping strTimestamp in its UTC event-time field. Normalize that
        # documented provider field to UTC rather than rejecting the surface.
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc).isoformat()


def thesportsdb_event_identity(event):
    home, away = event.get("idHomeTeam"), event.get("idAwayTeam")
    if home is None or away is None:
        raise ValueError("TheSportsDB home/away identity missing")
    home, away = str(home), str(away)
    if not home or not away or home == "None" or away == "None":
        raise ValueError("TheSportsDB home/away identity missing")
    return home, away


def thesportsdb_event_status(event):
    value = str(event.get("strStatus") or "").strip().lower()
    if value in {"not started", "notstarted", "scheduled", "ns"}:
        return "PREMATCH_CONFIRMED"
    if value in {"match finished", "finished", "ft"}:
        return "FINISHED"
    if value in {"postponed", "delayed"}:
        return "POSTPONED"
    if value in {"cancelled", "canceled", "abandoned"}:
        return "CANCELLED"
    if value in {"in progress", "live", "1h", "2h", "ht"}:
        return "STARTED"
    return "UNKNOWN_PROVIDER_STATUS"


def thesportsdb_stage(event):
    competition = event.get("strLeague")
    country = event.get("strCountry") or "International"
    if not isinstance(competition, str) or not competition.strip():
        raise ValueError("TheSportsDB competition missing")
    if not isinstance(country, str) or not country.strip():
        country = "International"
    return {"Snm": competition.strip(), "Cnm": country.strip()}


def thesportsdb_senior(event):
    stage = thesportsdb_stage(event)
    label = stage["Snm"] + " " + stage["Cnm"]
    if "uefa youth league" in label.lower():
        return True
    if any(x in label.lower() for x in ("premier league 2", "primavera")):
        return False
    return not re.search(r"\b(?:u[ -]?(?:1[5-9]|2[0-3])|under[ -]?(?:1[5-9]|2[0-3])|youth)\b", label, re.I)


def thesportsdb_events(payload):
    if not isinstance(payload, dict) or "events" not in payload:
        raise ValueError("TheSportsDB eventsday response missing events")
    events = payload.get("events")
    if events is None:
        events = []
    if not isinstance(events, list):
        raise ValueError("TheSportsDB eventsday events must be a list or null")
    seen, rows = set(), []
    for event in events:
        if not isinstance(event, dict):
            raise ValueError("TheSportsDB malformed event")
        if str(event.get("strSport") or "Soccer").lower() != "soccer":
            continue
        mid = str(event.get("idEvent"))
        if not mid or mid == "None" or mid in seen:
            raise ValueError("TheSportsDB missing/duplicate event ID")
        seen.add(mid)
        thesportsdb_event_identity(event)
        thesportsdb_event_time(event)
        if thesportsdb_senior(event):
            rows.append(event)
    return rows


def thesportsdb_date_surface(evidence, day, name):
    return evidence.get(THESPORTSDB_DATE_URL.format(day=day), name + "-thesportsdb")


def acquire_thesportsdb(request, evidence):
    start, end, _ = parse_request(request)
    start, end = start.astimezone(timezone.utc), end.astimezone(timezone.utc)
    keys = required_surface_keys(start.isoformat(), end.isoformat())
    fixtures, identities, surfaces = {}, {}, []
    cached = {}

    for key in keys:
        _, day = key.split(":")
        if day not in cached:
            cached[day] = thesportsdb_date_surface(evidence, day, "tdb-" + day)
        payload, proof = cached[day]
        events = thesportsdb_events(payload)
        grouped, ids = {}, []
        for event in events:
            mid = str(event["idEvent"])
            identity = thesportsdb_event_identity(event)
            kickoff = thesportsdb_event_time(event)
            stage = thesportsdb_stage(event)
            group_key = (stage["Cnm"], stage["Snm"])
            grouped.setdefault(group_key, []).append(mid)
            ids.append(mid)
            if mid in identities and identities[mid] != identity:
                raise ValueError("conflicting TheSportsDB date-surface team identity: " + mid)
            if mid in fixtures and fixtures[mid]["kickoff_utc"] != kickoff:
                raise ValueError("conflicting TheSportsDB date-surface kickoff: " + mid)
            identities[mid] = identity
            fixtures[mid] = {
                "match_id": mid,
                "country": stage["Cnm"],
                "competition": stage["Snm"],
                "competition_kind": competition_kind(stage),
                "is_friendly": any(x in stage["Snm"].lower() for x in ("friendly", "friendlies")),
                "home": str(event.get("strHomeTeam") or "").strip(),
                "away": str(event.get("strAwayTeam") or "").strip(),
                "kickoff_utc": kickoff,
                "fixture_status": thesportsdb_event_status(event),
                "source_url": proof["source_url"],
                "observed_at_utc": proof["observed_at_utc"],
                "provider_team_ids": list(identity),
            }
            if not fixtures[mid]["home"] or not fixtures[mid]["away"]:
                raise ValueError("TheSportsDB home/away names missing")
        blocks = [
            {"country": country, "competition": competition,
             "provider_fixture_count": len(mids), "extracted_fixture_ids": mids}
            for (country, competition), mids in sorted(grouped.items())
        ]
        surfaces.append({
            "surface_key": key,
            "source_url": proof["source_url"],
            "observed_at_utc": proof["observed_at_utc"],
            "pagination_complete": True,
            "provider_page_count": 1,
            "pages_fetched": [1],
            "provider_senior_fixture_count": len(ids),
            "extracted_fixture_ids": ids,
            "provider_senior_competition_block_count": len(blocks),
            "competition_blocks": blocks,
        })

    terminal_start = max(start, end - timedelta(hours=6))
    terminal_days = sorted({
        terminal_start.date().isoformat(),
        (end - timedelta(microseconds=1)).date().isoformat(),
    })
    terminal_ids, terminal_proofs = set(), []
    for day in terminal_days:
        payload, proof = thesportsdb_date_surface(evidence, day, "tdb-terminal-" + day)
        terminal_proofs.append(proof)
        for event in thesportsdb_events(payload):
            mid = str(event["idEvent"])
            kickoff = stamp(thesportsdb_event_time(event))
            if terminal_start <= kickoff < end:
                terminal_ids.add(mid)
                if mid in fixtures and (
                    thesportsdb_event_identity(event) != identities[mid]
                    or thesportsdb_event_time(event) != fixtures[mid]["kickoff_utc"]
                ):
                    raise ValueError("TheSportsDB terminal identity/kickoff changed: " + mid)
            if mid in fixtures:
                fixtures[mid].update(
                    fixture_status=thesportsdb_event_status(event),
                    observed_at_utc=proof["observed_at_utc"],
                    source_url=proof["source_url"],
                )
    now = utcnow()
    return {
        "schema_version": "football-stages-v4",
        "run_id": request["run_id"],
        "window_start_utc": start.isoformat(),
        "window_end_utc": end.isoformat(),
        "source_family": THESPORTSDB_FAMILY,
        "source_url": surfaces[0]["source_url"],
        "source_observed_at_utc": max(x["observed_at_utc"] for x in surfaces),
        "fixtures": list(fixtures.values()),
        "source_completeness_manifest": {
            "schema_version": "football-v4-source-completeness-v2",
            "acquisition_mode": "DATE_SURFACE_BATCH_V2",
            "league_query_mode": "DATE_SURFACE_ONLY",
            "registry_prefilter_applied": False,
            "scope_policy": "ALL_SOURCE_VISIBLE_SENIOR_FOOTBALL_BLOCKS",
            "extraction_complete": True,
            "provider_family": THESPORTSDB_FAMILY,
            "window_start_utc": start.isoformat(),
            "window_end_utc": end.isoformat(),
            "checked_at_utc": now,
            "required_surface_keys": keys,
            "date_surfaces": surfaces,
            "terminal_sentinel": {
                "interval_start_utc": terminal_start.isoformat(),
                "interval_end_utc": end.isoformat(),
                "checked_at_utc": max(x["observed_at_utc"] for x in terminal_proofs),
                "complete": True,
                "independent_refetch": True,
                "source_urls": [x["source_url"] for x in terminal_proofs],
                "provider_senior_fixture_count": len(terminal_ids),
                "extracted_fixture_ids": sorted(terminal_ids),
            },
        },
    }


def thesportsdb_competitive_history(evidence, team, now):
    url = THESPORTSDB_TEAM_LAST_URL.format(team=team)
    payload, proof = evidence.get(url, "tdb-team-" + str(team))
    rows = payload.get("results") if isinstance(payload, dict) else None
    if rows is None:
        rows = []
    if not isinstance(rows, list):
        raise ValueError("TheSportsDB team history results missing")
    results = {}
    for event in rows:
        if not isinstance(event, dict):
            continue
        if str(event.get("strSport") or "Soccer").lower() != "soccer":
            continue
        stage = thesportsdb_stage(event)
        if any(x in stage["Snm"].lower() for x in ("friendly", "friendlies", "testimonial")):
            continue
        identity = thesportsdb_event_identity(event)
        if str(team) not in identity:
            raise ValueError("unrelated event in TheSportsDB team history")
        kickoff = stamp(thesportsdb_event_time(event))
        if not now - timedelta(days=120) <= kickoff <= now - timedelta(hours=2):
            continue
        try:
            hg, ag = int(event.get("intHomeScore")), int(event.get("intAwayScore"))
        except (TypeError, ValueError) as exc:
            raise ValueError("TheSportsDB final score missing") from exc
        home = identity[0] == str(team)
        row = {
            "event_id": str(event["idEvent"]),
            "kickoff_utc": kickoff.isoformat(),
            "goals_for": hg if home else ag,
            "goals_against": ag if home else hg,
            "competition": stage["Snm"],
        }
        existing = results.get(row["event_id"])
        if existing is not None and existing != row:
            raise ValueError("conflicting TheSportsDB historical event")
        results[row["event_id"]] = row
    recent = sorted(results.values(), key=lambda x: x["kickoff_utc"], reverse=True)[:10]
    return recent, proof


def thesportsdb_fixture_refresh(evidence, fixture):
    mid = str(fixture["match_id"])
    payload, proof = evidence.get(THESPORTSDB_EVENT_URL.format(match=mid), "tdb-event-" + mid)
    events = payload.get("events") if isinstance(payload, dict) else None
    if not isinstance(events, list) or len(events) != 1:
        raise ValueError("TheSportsDB event detail identity missing")
    event = events[0]
    if str(event.get("idEvent")) != mid:
        raise ValueError("TheSportsDB event detail identity changed")
    ids = tuple(map(str, fixture.get("provider_team_ids") or []))
    if thesportsdb_event_identity(event) != ids:
        raise ValueError("TheSportsDB event detail team identity changed")
    if thesportsdb_event_time(event) != fixture["kickoff_utc"]:
        raise ValueError("TheSportsDB event detail kickoff changed")
    return thesportsdb_event_status(event), proof


def acquire(request, evidence):
    try:
        return acquire_livescore(request, evidence)
    except Exception as livescore_exc:
        try:
            return acquire_sofascore(request, evidence)
        except Exception as sofascore_exc:
            try:
                return acquire_footballinfo(request, evidence)
            except Exception as footballinfo_exc:
                # TheSportsDB is intentionally not a canonical production
                # fallback: its free date endpoint can expose a small subset of
                # worldwide fixtures and therefore cannot satisfy the sweep's
                # completeness invariant.
                raise RuntimeError(
                    f"all canonical date-surface providers failed; "
                    f"LiveScore: {livescore_exc}; SofaScore: {sofascore_exc}; "
                    f"FootballInfo: {footballinfo_exc}"
                ) from footballinfo_exc


def sofascore_competitive_history(evidence, team, now):
    results = {}
    proofs = []
    for page in range(3):
        url = SOFASCORE_TEAM_LAST_URL.format(team=team, page=page)
        payload, proof = evidence.get(url, f"sofa-team-{team}-{page}")
        proofs.append(proof)
        events = payload.get("events")
        if not isinstance(events, list):
            raise ValueError("SofaScore team history events missing")
        for event in events:
            if str((event.get("status") or {}).get("type") or "").lower() != "finished":
                continue
            stage = sofascore_stage(event)
            if any(x in stage["Snm"].lower() for x in ("friendly", "friendlies", "testimonial")):
                continue
            identity = sofascore_event_identity(event)
            if team not in identity:
                raise ValueError("unrelated event in SofaScore team history")
            kickoff = stamp(sofascore_event_time(event))
            if not now - timedelta(days=120) <= kickoff <= now - timedelta(hours=2):
                continue
            hs = event.get("homeScore") or {}
            aas = event.get("awayScore") or {}
            hg, ag = hs.get("normaltime"), aas.get("normaltime")
            if isinstance(hg, bool) or isinstance(ag, bool) or not isinstance(hg, int) or not isinstance(ag, int):
                continue
            home = identity[0] == team
            row = {
                "event_id": str(event["id"]),
                "kickoff_utc": kickoff.isoformat(),
                "goals_for": hg if home else ag,
                "goals_against": ag if home else hg,
                "competition": stage["Snm"],
            }
            existing = results.get(row["event_id"])
            if existing is not None and existing != row:
                raise ValueError("conflicting SofaScore historical event")
            results[row["event_id"]] = row
        if len(results) >= 10 or payload.get("hasNextPage") is not True:
            break
    recent = sorted(results.values(), key=lambda x: x["kickoff_utc"], reverse=True)[:10]
    if not proofs:
        raise ValueError("SofaScore team history proof missing")
    return recent, {
        "source_url": proofs[0]["source_url"],
        "observed_at_utc": max(x["observed_at_utc"] for x in proofs),
    }


def sofascore_fixture_refresh(evidence, fixture):
    mid = str(fixture["match_id"])
    url = SOFASCORE_EVENT_URL.format(match=mid)
    payload, proof = evidence.get(url, "sofa-event-" + mid)
    event = payload.get("event") if isinstance(payload, dict) else None
    if not isinstance(event, dict) or str(event.get("id")) != mid:
        raise ValueError("SofaScore event detail identity missing")
    ids = tuple(map(str, fixture.get("provider_team_ids") or []))
    if sofascore_event_identity(event) != ids:
        raise ValueError("SofaScore event detail team identity changed")
    if sofascore_event_time(event) != fixture["kickoff_utc"]:
        raise ValueError("SofaScore event detail kickoff changed")
    return sofascore_event_status(event), proof


def competitive_history(payload, team, now):
    if str(payload.get("ID")) != team or not isinstance(payload.get("Stages"), list):
        raise ValueError("team feed identity/schema mismatch")
    results = {}
    for block in payload["Stages"]:
        competition = block.get("Snm", "")
        if not competition or any(x in competition.lower() for x in ("friendly", "friendlies", "testimonial")):
            continue
        for event in block.get("Events", []):
            if event.get("Eps") != "FT":
                continue  # Extra-time/penalty totals cannot replace regulation scores.
            identity = event_identity(event)
            if team not in identity:
                raise ValueError("unrelated event in team history")
            kickoff = stamp(event_time(event))
            if not now - timedelta(days=120) <= kickoff <= now - timedelta(hours=2):
                continue
            home = identity[0] == team
            gf, ga = event["Tr1" if home else "Tr2"], event["Tr2" if home else "Tr1"]
            if not re.fullmatch(r"\d+", str(gf)) or not re.fullmatch(r"\d+", str(ga)):
                raise ValueError("invalid final score")
            row = {"event_id": str(event["Eid"]), "kickoff_utc": kickoff.isoformat(),
                   "goals_for": int(gf), "goals_against": int(ga), "competition": competition}
            if row["event_id"] in results and results[row["event_id"]] != row:
                raise ValueError("conflicting historical result")
            results[row["event_id"]] = row
    return sorted(results.values(), key=lambda x: x["kickoff_utc"], reverse=True)[:10]


def research(source, receipt, evidence, checkpoint):
    fixtures = {f["match_id"]: f for f in source["fixtures"]}
    # Native priority, then all remaining research candidates; no fixed cap.
    order = list(dict.fromkeys(receipt.get("priority_research_order", []) + receipt.get("goal_research_order", [])))
    previous_order = checkpoint.get("research_order")
    if previous_order and previous_order != order:
        # A resume may not silently change its research cohort. A newly refreshed
        # source epoch must create a new checkpoint and explicitly remap reusable IDs.
        raise ValueError("RESEARCH_ORDER_CHANGED: new source epoch/remap required")
    checkpoint["research_order"] = order
    checkpoint.setdefault("fixtures", {})
    resolved_before = [mid for mid in order if _resolved(checkpoint["fixtures"].get(mid))]
    unresolved = [mid for mid in order if mid not in resolved_before]
    checkpoint["reused_match_ids"] = resolved_before
    checkpoint["resume_queue"] = unresolved
    feeds = {}
    deadline = time.monotonic() + 20 * 60
    for index, mid in enumerate(unresolved):
        if time.monotonic() >= deadline:
            checkpoint["unfinished_research_order"] = unresolved[index:]
            checkpoint["resume_queue"] = unresolved[index:]
            checkpoint["resource_limit_reason"] = "RESEARCH_TIME_BUDGET_CHECKPOINTED"
            checkpoint["status"] = "RESEARCH_PENDING"
            save(evidence.output / "checkpoint.json", checkpoint)
            break
        fixture = fixtures[mid]
        previous = checkpoint["fixtures"].get(mid) or {}
        state = {
            "pending_reasons": [],
            "attempt_count": int(previous.get("attempt_count") or 0) + 1,
            "last_attempted_at_utc": utcnow(),
        }
        checkpoint["fixtures"][mid] = state
        ids = fixture.get("provider_team_ids", [])
        if len(ids) != 2 or source["source_family"] != FAMILY:
            state["pending_reasons"].append("PROVIDER_TEAM_ID_MAPPING_REQUIRED")
        else:
            histories, checks = dict(fixture.get("football_evidence") or {}), []
            for side, team in zip(("home", "away"), ids):
                team = str(team)
                try:
                    if not team.isdigit():
                        raise ValueError("unsafe provider team ID")
                    if team not in feeds:
                        try:
                            feeds[team] = evidence.get(TEAM_URL.format(team=team), "team-" + team)
                        except Exception as exc:
                            feeds[team] = exc
                    if isinstance(feeds[team], Exception):
                        raise feeds[team]
                    payload, proof = feeds[team]
                    recent = competitive_history(payload, team, stamp(proof["observed_at_utc"]))
                    histories[side] = {"source_url": proof["source_url"], "observed_at_utc": proof["observed_at_utc"], "recent": recent}
                    if len(recent) < 4:
                        state["pending_reasons"].append(side.upper() + "_COMPETITIVE_HISTORY_UNDER_FOUR")
                    matches = [e for b in payload["Stages"] for e in b.get("Events", []) if str(e.get("Eid")) == mid]
                    if len(matches) != 1 or event_identity(matches[0]) != tuple(map(str, ids)) or event_time(matches[0]) != fixture["kickoff_utc"]:
                        raise ValueError("fixture identity/kickoff not reconciled in team feed")
                    checks.append({"team_id": team, "status": event_status(matches[0]), **proof})
                except Exception as exc:
                    state["pending_reasons"].append(side.upper() + ": " + str(exc))
            fixture["football_evidence"] = histories
            state["status_checks"] = checks
            if len(checks) == 2 and checks[0]["status"] == checks[1]["status"]:
                fixture.update(fixture_status=checks[0]["status"], observed_at_utc=max(x["observed_at_utc"] for x in checks))
            else:
                fixture["fixture_status"] = "UNVERIFIED_STATUS_REFRESH"
                state["pending_reasons"].append("BOTH_TEAM_STATUS_REFRESH_NOT_RECONCILED")
            if classify(fixture)["lane"] in {"CONDITIONAL", "PILOT", "DISCOVERY"} and fixture.get("researchability_status") != "VERIFIED":
                state["pending_reasons"].append("CURRENT_MECHANISM_STAT_NEWS_CHANNEL_PROOF_REQUIRED")
                # An advertised hasStats/hasLineups flag is not actual evidence.
        _finish_research_state(state)
        checkpoint["resume_queue"] = _resume_queue(checkpoint)
        checkpoint["completed_research_count"] = sum(
            1 for mid2 in order if _resolved(checkpoint["fixtures"].get(mid2))
        )
        checkpoint["pending_research_count"] = len(checkpoint["resume_queue"])
        # Persist after every fixture. The normal-chat launcher may mirror these
        # durable checkpoints to GitHub in batches of 3-5 fixtures.
        save(evidence.output / "source.json", source)
        save(evidence.output / "checkpoint.json", checkpoint)



def run(request_path, output, source_path=None, resume_from=None):
    if output.exists() and any(output.iterdir()):
        raise ValueError("output must be fresh; preserve previous evidence and resume into a new directory")
    if source_path and resume_from:
        raise ValueError("choose either --source or --resume-from")
    output.mkdir(parents=True, exist_ok=True)
    evidence = Evidence(output)
    checkpoint = {"schema_version": CHECKPOINT_SCHEMA, "status": "RUNNING", "fixtures": {}, "resume_generation": 0}
    save(output / "checkpoint.json", checkpoint)
    try:
        request = json.loads(request_path.read_text())
        start, end, _ = parse_request(request)
        checkpoint["run_id"] = request["run_id"]
        if end <= stamp(utcnow()):
            raise ValueError("REQUEST_WINDOW_EXPIRED: no network acquisition performed")
        if resume_from:
            resume_path = Path(resume_from)
            if resume_path.is_dir():
                resume_path = resume_path / "checkpoint.json"
            previous = json.loads(resume_path.read_text())
            previous_dir = resume_path.parent
            original_path = previous_dir / "original-source.json"
            working_path = previous_dir / "source.json"
            if not original_path.exists() or not working_path.exists():
                raise ValueError("RESUME_EVIDENCE_MISSING: original-source.json and source.json required")
            raw = original_path.read_bytes()
            original_sha = hashlib.sha256(raw).hexdigest()
            if previous.get("original_source_sha256") != original_sha:
                raise ValueError("RESUME_SOURCE_SHA_MISMATCH")
            source = json.loads(working_path.read_text())
            original = json.loads(raw)
            for candidate in (source, original):
                if candidate["run_id"] != request["run_id"] or stamp(candidate["window_start_utc"]) != start or stamp(candidate["window_end_utc"]) != end:
                    raise ValueError("resume request does not match original source")
            (output / "original-source.json").write_bytes(raw)
            checkpoint = json.loads(json.dumps(previous))
            checkpoint.update(
                schema_version=CHECKPOINT_SCHEMA,
                status="RUNNING",
                resume_generation=int(previous.get("resume_generation") or 0) + 1,
                resumed_from=str(resume_path),
                original_source_sha256=original_sha,
            )
            checkpoint.pop("unfinished_research_order", None)
            checkpoint.pop("resource_limit_reason", None)
            save(output / "checkpoint.json", checkpoint)
        elif source_path:
            raw = source_path.read_bytes()
            (output / "original-source.json").write_bytes(raw)
            source = json.loads(raw)
            if source["run_id"] != request["run_id"] or stamp(source["window_start_utc"]) != start or stamp(source["window_end_utc"]) != end:
                raise ValueError("resume request does not match original source")
            checkpoint["original_source_sha256"] = hashlib.sha256(raw).hexdigest()
        else:
            source = acquire(request, evidence)
            save(output / "original-source.json", source)
            checkpoint["original_source_sha256"] = digest(output / "original-source.json")
        save(output / "source.json", source)
        preliminary = sweep(source, now=utcnow())
        save(output / "listing-receipt.json", preliminary)
        # V4_SWEEP_READY is a structural receipt, never an early-return condition.
        research(source, preliminary, evidence, checkpoint)
        receipt = sweep(source, now=utcnow())
        save(output / "v4_sweep_ready.json", receipt)
        pending = [r for r in receipt["source_ledger"] if r["intake_lane"].startswith("PENDING") or r["intake_lane"] == "UNVERIFIED"]
        limited_ids = {
            mid for mid, state in checkpoint.get("fixtures", {}).items()
            if state.get("research_disposition") == "EVIDENCE_LIMITED"
        }
        actionable_pending = [r for r in pending if r.get("match_id") not in limited_ids]
        if checkpoint.get("unfinished_research_order") or actionable_pending or checkpoint.get("resume_queue"):
            research_status = "RESEARCH_PENDING"
        elif pending:
            research_status = "RESEARCH_COMPLETE_WITH_EVIDENCE_LIMITS"
        else:
            research_status = "RESEARCH_COMPLETE"
        checkpoint.update(
            status=research_status,
            native_v4_executed=True,
            pending_rows=actionable_pending,
            evidence_limited_rows=[r for r in pending if r.get("match_id") in limited_ids],
            eligible_count=receipt["eligible_count"],
            pending_research_count=len(checkpoint.get("resume_queue") or []),
        )
        save(output / "checkpoint.json", checkpoint)
        save(output / "rank-handoff.json", {
            "schema_version": "football-v4-rank-handoff-v1", "status": "V4_RANK_HANDOFF_READY",
            "run_id": source["run_id"], "source_run_id": source["run_id"],
            "source_filename": "source.json", "source_file_sha256": digest(output / "source.json"),
            "receipt_filename": "v4_sweep_ready.json", "receipt_integrity_sha256": receipt["integrity_sha256"],
            "research_status": checkpoint["status"], "eligible_count": receipt["eligible_count"],
            "pending_count": len(actionable_pending), "evidence_limited_count": len(pending) - len(actionable_pending),
            "checkpoint_filename": "checkpoint.json",
            "requires_fresh_status_refresh": True, "rank_must_not_reconstruct_source_from_airtable": True})
        return 0
    except Exception as exc:
        checkpoint.update(status="BLOCKED", error=type(exc).__name__ + ": " + str(exc), checked_at_utc=utcnow())
        save(output / "checkpoint.json", checkpoint)
        return 2


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--source", type=Path, help="start from an unchanged saved source; no date-surface acquisition")
    parser.add_argument("--resume-from", type=Path, help="previous output directory or checkpoint.json; reuse enriched source and resolved fixture states")
    args = parser.parse_args()
    return run(args.request, args.output, args.source, args.resume_from)


if __name__ == "__main__":
    raise SystemExit(main())
