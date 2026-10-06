from __future__ import annotations

import json
import sys
import urllib.request
from datetime import date

URLS = {
    "sofascore_www": "https://www.sofascore.com/api/v1/sport/football/scheduled-events/{date}",
    "sofascore_api": "https://api.sofascore.com/api/v1/sport/football/scheduled-events/{date}",
    "thesportsdb": "https://www.thesportsdb.com/api/v1/json/123/eventsday.php?d={date}&s=Soccer",
}


def fetch(url: str) -> tuple[int, str, object]:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; SlipTraceFootballSourceProbe/1.0)",
            "Accept": "application/json,text/plain,*/*",
        },
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        body = resp.read()
        text = body.decode("utf-8", errors="replace")
        try:
            payload = json.loads(text)
        except json.JSONDecodeError:
            payload = None
        return resp.status, text[:300], payload


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


def main() -> int:
    d = sys.argv[1] if len(sys.argv) > 1 else date.today().isoformat()
    any_success = False
    for name, template in URLS.items():
        url = template.format(date=d)
        try:
            status, head, payload = fetch(url)
            print(json.dumps({"provider": name, "status": status, "head": head, **summarize(name, payload)}, ensure_ascii=False))
            if status == 200 and isinstance(payload, dict):
                any_success = True
        except Exception as exc:
            print(json.dumps({"provider": name, "error": f"{type(exc).__name__}: {exc}"}, ensure_ascii=False))
    return 0 if any_success else 2


if __name__ == "__main__":
    raise SystemExit(main())
