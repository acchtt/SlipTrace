from __future__ import annotations

import json
import re
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import date

URLS = {
    "sofascore_www": "https://www.sofascore.com/api/v1/sport/football/scheduled-events/{date}",
    "sofascore_api": "https://api.sofascore.com/api/v1/sport/football/scheduled-events/{date}",
    "footballfixtures": "https://www.footballfixtures.org/fixtures/{date}",
    "footballinfo": "https://www.footballinfo.net/Fixtures?date={date}",
    "livescoresx": "https://livescoresx.com/fixtures/{date}",
    "thesportsdb": "https://www.thesportsdb.com/api/v1/json/123/eventsday.php?d={date}&s=Soccer",
    "espn_all": "https://site.api.espn.com/apis/site/v2/sports/soccer/all/scoreboard?dates={date_compact}&limit=1000",
    "fotmob": "https://www.fotmob.com/api/data/matches?date={date_compact}",
    "foxscore_web": "https://web.foxscore.vn/",
    "foxsports_web": "https://www.foxsports.com/scores/soccer",
}


def fetch(url: str) -> tuple[int, str, object, str]:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; SlipTraceFootballSourceProbe/1.0)",
            "Accept": "application/json,text/plain,*/*",
        },
    )
    with urllib.request.urlopen(req, timeout=8) as resp:
        body = resp.read()
        text = body.decode("utf-8", errors="replace")
        try:
            payload = json.loads(text)
        except json.JSONDecodeError:
            payload = None
        return resp.status, text[:300], payload, text


def summarize(name: str, payload: object) -> dict[str, object]:
    out: dict[str, object] = {"provider": name}
    if isinstance(payload, dict):
        if isinstance(payload.get("events"), list):
            out["event_count"] = len(payload["events"])
            if payload["events"]:
                ev = payload["events"][0]
                if isinstance(ev, dict):
                    competition = None
                    competitions = ev.get("competitions")
                    if isinstance(competitions, list) and competitions:
                        c0 = competitions[0]
                        if isinstance(c0, dict):
                            competition = {
                                "date": c0.get("date"),
                                "type": (c0.get("type") or {}).get("text") if isinstance(c0.get("type"), dict) else None,
                                "competitors": [
                                    ((x.get("team") or {}).get("displayName") if isinstance(x.get("team"), dict) else None)
                                    for x in (c0.get("competitors") or [])
                                    if isinstance(x, dict)
                                ][:2],
                            }
                    out["sample_keys"] = sorted(ev.keys())[:20]
                    out["sample"] = {
                        "id": ev.get("id"),
                        "date": ev.get("date"),
                        "name": ev.get("name"),
                        "startTimestamp": ev.get("startTimestamp"),
                        "homeTeam": (ev.get("homeTeam") or {}).get("name") if isinstance(ev.get("homeTeam"), dict) else None,
                        "awayTeam": (ev.get("awayTeam") or {}).get("name") if isinstance(ev.get("awayTeam"), dict) else None,
                        "tournament": ((ev.get("tournament") or {}).get("name") if isinstance(ev.get("tournament"), dict) else None),
                        "competition": competition,
                    }
        elif isinstance(payload.get("event"), list):
            out["event_count"] = len(payload["event"])
        elif isinstance(payload.get("events"), dict):
            out["events_type"] = "dict"
        elif isinstance(payload.get("leagues"), list):
            leagues = payload["leagues"]
            out["league_count"] = len(leagues)
            out["match_count"] = sum(
                len(x.get("matches") or []) for x in leagues if isinstance(x, dict)
            )
            samples = []
            for league in leagues:
                if not isinstance(league, dict):
                    continue
                for match in league.get("matches") or []:
                    if isinstance(match, dict):
                        samples.append({
                            "id": match.get("id"),
                            "league": league.get("name"),
                            "home": (match.get("home") or {}).get("name") if isinstance(match.get("home"), dict) else None,
                            "away": (match.get("away") or {}).get("name") if isinstance(match.get("away"), dict) else None,
                            "utcTime": ((match.get("status") or {}).get("utcTime") if isinstance(match.get("status"), dict) else None),
                        })
                    if len(samples) >= 5:
                        break
                if len(samples) >= 5:
                    break
            out["samples"] = samples
        elif isinstance(payload.get("events"), list):
            pass
        elif isinstance(payload.get("sports"), list):
            out["sports_count"] = len(payload["sports"])
        else:
            out["keys"] = sorted(payload.keys())[:30]
    else:
        out["payload_type"] = type(payload).__name__
    return out


def probe(name: str, template: str, date_value: str) -> tuple[dict[str, object], bool]:
    """Probe one independent provider without blocking other providers."""
    url = template.format(date=date_value, date_compact=date_value.replace("-", ""))
    try:
        status, head, payload, full_text = fetch(url)
        extra: dict[str, object] = {}
        if payload is None:
            extra["body_length"] = len(full_text)
            extra["has_fixture_heading"] = any(
                phrase in full_text for phrase in ("Football Fixtures", "Fixtures", "matches scheduled")
            )
            lowered = full_text.lower()
            extra["html_markers"] = {
                marker: lowered.count(marker.lower())
                for marker in (
                    "hometeam", "awayteam", "fixture", "match", "kickoff",
                    "__next_f.push", "data-event", "data-match", "competition"
                )
            }
            hrefs = re.findall(r'href=["\\\']([^"\\\']+)["\\\']', full_text, re.I)
            extra["sample_hrefs"] = hrefs[:20]
            scripts = re.findall(r'<script[^>]+src=["\\\']([^"\\\']+)["\\\']', full_text, re.I)
            extra["sample_scripts"] = scripts[:20]
            urls = re.findall(r'https?://[^"\\\'<> ]+', full_text, re.I)
            extra["api_like_urls"] = [u for u in urls if "api" in u.lower() or "score" in u.lower()][:20]
            for marker in ("Champions League", "Premier League", "Superliga", "UEFA"):
                at = full_text.find(marker)
                if at >= 0:
                    extra["sample_marker"] = marker
                    extra["sample_fragment"] = re.sub(r"\\s+", " ", full_text[max(0, at-500):at+1500])[:2000]
                    break
            for label, token in (("fixture_html", 'class="fi-fixture'), ("home_team_json", '"homeTeam"')):
                at = full_text.find(token)
                if at >= 0:
                    extra[label] = re.sub(r"\\s+", " ", full_text[max(0, at-700):at+3500])[:4200]
        if name == "footballinfo" and payload is None:
            team_ids = re.findall(r"media\.api-sports\.io/football/teams/(\d+)\.png", full_text)
            if team_ids:
                team_url = "https://www.footballinfo.net/Teams/Details/" + team_ids[0]
                try:
                    _, _, _, team_text = fetch(team_url)
                    extra["team_detail_url"] = team_url
                    extra["team_detail_length"] = len(team_text)
                    at = team_text.find('fi-fixture')
                    if at < 0:
                        at = team_text.lower().find("fixtures")
                    extra["team_detail_fragment"] = re.sub(r"\\s+", " ", team_text[max(0, at-500):at+4500])[:5000] if at >= 0 else team_text[:3000]
                    detail_ids = re.findall(r'/Fixtures/Details/(\d+)', team_text)
                    if detail_ids:
                        fixture_url = "https://www.footballinfo.net/Fixtures/Details/" + detail_ids[-1]
                        try:
                            _, _, _, detail_text = fetch(fixture_url)
                            extra["fixture_detail_url"] = fixture_url
                            extra["fixture_detail_length"] = len(detail_text)
                            extra["fixture_detail_fragment"] = re.sub(r"\\s+", " ", detail_text[:9000])[:9000]
                        except Exception as detail_exc:
                            extra["fixture_detail_error"] = f"{type(detail_exc).__name__}: {detail_exc}"
                except Exception as exc:
                    extra["team_detail_error"] = f"{type(exc).__name__}: {exc}"
        item = {"provider": name, "status": status, "head": head, **extra, **summarize(name, payload)}
        usable = status == 200 and (isinstance(payload, dict) or len(full_text) > 5000)
        return item, usable
    except Exception as exc:
        return {"provider": name, "error": f"{type(exc).__name__}: {exc}"}, False


def main() -> int:
    d = sys.argv[1] if len(sys.argv) > 1 else date.today().isoformat()
    # Each source has its own bounded connection timeout. Keep output in
    # provider order, but don't pay six sequential provider waits.
    with ThreadPoolExecutor(max_workers=len(URLS)) as pool:
        results = list(pool.map(lambda item: probe(item[0], item[1], d), URLS.items()))
    for item, _ in results:
        print(json.dumps(item, ensure_ascii=False))
    return 0 if any(success for _, success in results) else 2


if __name__ == "__main__":
    raise SystemExit(main())
