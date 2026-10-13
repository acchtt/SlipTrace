from __future__ import annotations

import json
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
                    out["sample_keys"] = sorted(ev.keys())[:20]
                    out["sample"] = {
                        "id": ev.get("id"),
                        "startTimestamp": ev.get("startTimestamp"),
                        "homeTeam": (ev.get("homeTeam") or {}).get("name") if isinstance(ev.get("homeTeam"), dict) else None,
                        "awayTeam": (ev.get("awayTeam") or {}).get("name") if isinstance(ev.get("awayTeam"), dict) else None,
                        "tournament": ((ev.get("tournament") or {}).get("name") if isinstance(ev.get("tournament"), dict) else None),
                    }
        elif isinstance(payload.get("event"), list):
            out["event_count"] = len(payload["event"])
        elif isinstance(payload.get("events"), dict):
            out["events_type"] = "dict"
        else:
            out["keys"] = sorted(payload.keys())[:30]
    else:
        out["payload_type"] = type(payload).__name__
    return out


def probe(name: str, template: str, date_value: str) -> tuple[dict[str, object], bool]:
    """Probe one independent provider without blocking other providers."""
    url = template.format(date=date_value)
    try:
        status, head, payload, full_text = fetch(url)
        extra: dict[str, object] = {}
        if payload is None:
            extra["body_length"] = len(full_text)
            extra["has_fixture_heading"] = any(
                phrase in full_text for phrase in ("Football Fixtures", "Fixtures", "matches scheduled")
            )
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
