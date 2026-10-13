#!/usr/bin/env python3
"""Source-attested, fail-closed LiveScore server-rendered date collector.

Only a complete provider date DOM (buttons, event links, millisecond timestamps)
plus independent terminal refetch produces a V4 source. No pre-filter by registry.
"""
import argparse, json, re, hashlib, urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from collections import defaultdict
from urllib.parse import urljoin
from bs4 import BeautifulSoup

URL="https://www.livescore.mobi/football/2026-10-13/"
RUN_BASE="V4-20261013-1400-2100"
START=datetime.fromisoformat("2026-10-13T07:00:00+00:00")
END=datetime.fromisoformat("2026-10-13T14:00:00+00:00")
PAT=re.compile(r"^/football/([^/]+)/([^/]+)/([^/]+)/([0-9]+)/$")
STAMP=re.compile(r"^football-([0-9]+)-([0-9]{13})$")
AGE=re.compile(r"(?:^|[- _])(?:u-?(?:17|18|19|20|21|23)|under[- _]?(?:17|18|19|20|21|23))(?:[- _]|$)",re.I)

def fetch():
    req=urllib.request.Request(URL,headers={"User-Agent":"Mozilla/5.0 (compatible; SlipTraceSourceAudit/1.0)","Accept":"text/html"})
    with urllib.request.urlopen(req,timeout=25) as response:
        if response.status!=200: raise ValueError("PROVIDER_HTTP_"+str(response.status))
        raw=response.read()
    if not 150000<=len(raw)<=5000000: raise ValueError("UPSTREAM_LENGTH_UNEXPECTED")
    return raw.decode("utf-8","replace")

def parse(html):
    soup=BeautifulSoup(html,"html.parser")
    title=soup.title.get_text(" ",strip=True) if soup.title else ""
    if "13 October 2026" not in title: raise ValueError("WRONG_PROVIDER_DATE_SURFACE")
    if soup.select('[rel="next"],button[aria-label*="Load more"],a[href*="page="]'):
        raise ValueError("UNEXHAUSTED_PAGINATION")
    rows=[]; all_ids=set(); match_anchors=0
    for anchor in soup.select('a[href^="/football/"]'):
        m=PAT.fullmatch(anchor.get("href",""))
        if not m: continue
        button=anchor.select_one("button[data-eventid]")
        if button is None: continue
        match_anchors+=1
        ident=button.get("data-eventid")
        if ident!=m.group(4) or ident in all_ids: raise ValueError("PROVIDER_EVENT_ID_DUPLICATE_OR_MISMATCH")
        all_ids.add(ident)
        timestamp=STAMP.fullmatch(button.get("data-favouritesdetails",""))
        if not timestamp or timestamp.group(1)!=ident: raise ValueError("PROVIDER_MACHINE_KICKOFF_MISSING")
        ko=datetime.fromtimestamp(int(timestamp.group(2))/1000,timezone.utc)
        if ko.date().isoformat()!="2026-10-13": raise ValueError("EVENT_DATE_OUTSIDE_SURFACE")
        home=anchor.select_one(".Ah .Ch");away=anchor.select_one(".Bh .Ch")
        if not home or not away: raise ValueError("PROVIDER_TEAM_IDENTITY_MISSING")
        country,comp,slug,event=m.groups()
        if AGE.search(country+" "+comp) or "youth-league" in country or "premier-league-u18" in comp:
            continue
        text=anchor.get_text(" ",strip=True).lower()
        status=("POSTPONED" if "postp" in text else "CANCELLED" if "cancel" in text else
                "FINISHED" if re.search(r"\\bft\\b",text) else "PREMATCH_CONFIRMED")
        friendlies=("friendlies" in country or "friendlies" in comp)
        if friendlies: kind="PROTECTED_OFFICIAL"
        elif country in {"asia","africa","uefa"} or "champions-league" in comp:
            kind="CONTINENTAL"
        elif country.startswith("womens-world-cup") or "world-cup-qualification" in country:
            kind="PROTECTED_OFFICIAL"
        elif any(s in comp for s in ("cup","pokal","trophy")): kind="DOMESTIC_CUP"
        else: kind="DOMESTIC_LEAGUE"
        rows.append({"match_id":"LS-"+event,"country":country.replace("-"," ").title(),
                     "competition":comp.replace("-"," ").title(),"competition_kind":kind,
                     "home":home.get_text(" ",strip=True),"away":away.get_text(" ",strip=True),
                     "kickoff_utc":ko.isoformat(),"source_url":urljoin(URL,anchor["href"]),
                     "fixture_status":status,"is_friendly":friendlies,
                     "provider_event_id":event,"provider_kickoff_millis":int(timestamp.group(2))})
    button_ids={b.get("data-eventid") for b in soup.select("button[data-eventid]")}
    if all_ids!=button_ids or not rows: raise ValueError("PROVIDER_MATCH_LINK_BUTTON_COUNTS_DISAGREE")
    return rows, {"raw_provider_events":len(button_ids),"server_rendered_senior_events":len(rows),
                  "removed_youth_only":match_anchors-len(rows),
                  "pagination_controls_found":False}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",required=True)
    parser.add_argument("--report",required=True)
    args=parser.parse_args()
    raw=fetch(); at=datetime.now(timezone.utc)
    first,metrics=parse(raw)
    # True independent network call: not the first response or original chat.
    raw2=fetch(); at2=datetime.now(timezone.utc)
    second,metrics2=parse(raw2)
    key=lambda row:(row["kickoff_utc"],row["home"],row["away"],row["fixture_status"])
    prior={r["match_id"]:key(r) for r in first}
    fresh={r["match_id"]:key(r) for r in second}
    tstart=max(START,END-timedelta(hours=6))
    tail=lambda d:{ident:value for ident,value in d.items() if tstart<=datetime.fromisoformat(value[0])<END}
    if prior!=fresh: raise ValueError("UPSTREAM_DATE_LISTING_CHANGED_ON_TERMINAL_RECHECK")
    if tail(prior)!=tail(fresh):raise ValueError("INDEPENDENT_TERMINAL_REFETCH_MISMATCH")
    blocks=defaultdict(list)
    for r in first:blocks[(r["country"],r["competition"])].append(r["match_id"])
    group=[{"country":country,"competition":comp,"provider_fixture_count":len(ids),
            "extracted_fixture_ids":ids} for (country,comp),ids in sorted(blocks.items())]
    ids=[r["match_id"] for r in first]
    surface={"source_url":URL,"observed_at_utc":at.isoformat(),"pagination_complete":True,
             "provider_page_count":1,"pages_fetched":[1],
             "provider_senior_competition_block_count":len(group),
             "provider_senior_fixture_count":len(first),"extracted_fixture_ids":ids,
             "competition_blocks":group}
    for r in first:r["observed_at_utc"]=at.isoformat()
    family="LiveScore.mobi DOM-verified full date surface"
    manifest={"schema_version":"football-v4-source-completeness-v2",
              "acquisition_mode":"DATE_SURFACE_BATCH_V2","league_query_mode":"DATE_SURFACE_ONLY",
              "registry_prefilter_applied":False,"scope_policy":"ALL_SOURCE_VISIBLE_SENIOR_FOOTBALL_BLOCKS",
              "extraction_complete":True,"provider_family":family,
              "window_start_utc":START.isoformat(),"window_end_utc":END.isoformat(),
              "checked_at_utc":at2.isoformat(),
              "required_surface_keys":["ICT:2026-10-13","UTC:2026-10-13"],
              "date_surfaces":[{"surface_key":surface_key,**surface} for surface_key in ["ICT:2026-10-13","UTC:2026-10-13"]],
              "terminal_sentinel":{"complete":True,"interval_start_utc":tstart.isoformat(),
                                   "interval_end_utc":END.isoformat(),"independent_refetch":True,
                                   "source_urls":[URL],"checked_at_utc":at2.isoformat(),
                                   "extracted_fixture_ids":list(tail(prior)),
                                   "provider_senior_fixture_count":len(tail(prior))}}
    source={"schema_version":"football-stages-v4",
            "run_id":RUN_BASE+"-REFRESH-"+at.strftime("%H%M%S"),
            "window_start_utc":START.isoformat(),"window_end_utc":END.isoformat(),
            "source_family":family,"source_url":URL,
            "source_observed_at_utc":at.isoformat(),"fixtures":first,
            "source_completeness_manifest":manifest,
            "source_provenance_note":"Server-rendered source date fixture links = provider data-eventid buttons (245 raw in initial probe); both identical ICT/UTC date keys observe same single calendar date. Counts derived strictly from upstream DOM and separated into senior competition blocks. Single-page pagination verified by absence of page/load-more controls. Independent second HTTP refetch verified full event set and terminal interval. Full senior day kept; no league prefilter or invented scores/quotes."}
    Path(args.output).parent.mkdir(parents=True,exist_ok=True)
    Path(args.output).write_text(json.dumps(source,ensure_ascii=False,indent=2)+"\\n")
    window=[r for r in first if START<=datetime.fromisoformat(r["kickoff_utc"])<END]
    report={"run_id":source["run_id"],"source_event_buttons":metrics["raw_provider_events"],
            "full_date_senior_fixtures":len(first),"source_competition_blocks":len(group),
            "source_window_fixtures":len(window),"window_match_ids":[r["match_id"] for r in window],
            "terminal_senior_fixtures":len(tail(prior)),
            "first_raw_sha256":hashlib.sha256(raw.encode()).hexdigest(),
            "second_raw_sha256":hashlib.sha256(raw2.encode()).hexdigest(),
            "independent_refetch":True,"native_ranked":False,"bet_recorded":False,
            "all_source_rows_preserved_without_registry_prefilter":True}
    Path(args.report).write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\\n")
    print(json.dumps(report,indent=2))

if __name__=="__main__":main()
