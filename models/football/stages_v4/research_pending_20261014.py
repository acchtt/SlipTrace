#!/usr/bin/env python3
from __future__ import annotations
import json, re, time, unicodedata
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

UTC=timezone.utc
CUTOFF=datetime.fromisoformat("2026-10-14T10:27:20.963200+00:00")
SOURCE=Path("models/football/stages_v4/recovery/V4-20261014-1725-20261015-0000/source.json")
OUT=Path("models/football/stages_v4/recovery/V4-20261014-1725-20261015-0000/pending-goal-research-assessment.json")
TARGET_IDS={
"1886563","1886570","1886565","1886569","1886664","1886670","1886671","1886678",
"1886562","1886564","1886566","1886676","1886667","1873820","1873862","1873831","1885201","1873819"
}
HEADERS={"User-Agent":"Mozilla/5.0","Accept":"application/json,text/plain,*/*","Origin":"https://www.livescore.com","Referer":"https://www.livescore.com/"}
FRIENDLY_RE=re.compile("friendl",re.I)
NONSTANDARD_RE=re.compile(r"(?:futsal|beach soccer|esoccer|e-soccer|efootball|virtual|kings league|baller league|7s\\b|six-a-side|6-a-side)",re.I)

ALIASES={
"Feyenoord U19":["Feyenoord U19","Feyenoord"],
"Como U19":["Como U19","Como 1907 U19"],
"Shakhtar Donetsk U19":["Shakhtar Donetsk U19","Shakhtar U19"],
"AEK Athens U19":["AEK Athens U19","AEK U19"],
"Roma U19":["Roma U19","AS Roma U19"],
"Real Madrid U19":["Real Madrid U19"],
"Slovan Bratislava U19":["Slovan Bratislava U19","Slovan U19"],
"VfB Stuttgart U19":["VfB Stuttgart U19","Stuttgart U19"],
"Partizani U19":["Partizani U19","FK Partizani U19"],
"Valletta U19":["Valletta U19"],
"Dinamo Minsk U19":["Dinamo Minsk U19","Dynamo Minsk U19"],
"Dinamo Tbilisi U19":["Dinamo Tbilisi U19","Dynamo Tbilisi U19"],
"Ballkani U19":["Ballkani U19","FC Ballkani U19"],
"HJK U19":["HJK U19","HJK Helsinki U19"],
"AP Brera Strumica U19":["AP Brera Strumica U19","Brera Strumica U19","Brera U19"],
"FC Santa Coloma U19":["FC Santa Coloma U19","Santa Coloma U19"],
"Aston Villa U19":["Aston Villa U19"],
"Fenerbahce U19":["Fenerbahce U19","Fenerbahçe U19"],
"Manchester City U19":["Manchester City U19","Man City U19"],
"Paris Saint-Germain U19":["Paris Saint-Germain U19","Paris SG U19","PSG U19"],
"Real Betis U19":["Real Betis U19","Betis U19"],
"FC Porto U19":["FC Porto U19","Porto U19"],
"SK Super Nova U19":["SK Super Nova U19","Super Nova U19"],
"Cliftonville U19":["Cliftonville U19"],
"Zalgiris Vilnius U19":["Zalgiris Vilnius U19","FK Zalgiris Vilnius U19","Zalgiris U19"],
"Thor Akureyri U19":["Thor Akureyri U19","Thór Akureyri U19","Þór Akureyri U19"],
"Al-Jazira":["Al-Jazira","Al Jazira"],
"Arkadag":["Arkadag","FK Arkadag"],
}

def norm(s:str)->str:
    s=unicodedata.normalize("NFKD",s or "").encode("ascii","ignore").decode().lower()
    s=s.replace("&"," and ")
    s=re.sub(r"[^a-z0-9]+"," ",s).strip()
    return re.sub(r"\\s+"," ",s)

ALIAS_NORMS={team:{norm(x) for x in vals+[team]} for team,vals in ALIASES.items()}

def fetch_json(url,retries=3):
    last=None
    for i in range(retries):
        try:
            req=Request(url,headers=HEADERS)
            with urlopen(req,timeout=25) as resp:
                return json.loads(resp.read())
        except Exception as e:
            last=e; time.sleep(1+i)
    raise RuntimeError(f"{url}: {last}")

def fetch_day(d):
    ds=d.strftime("%Y%m%d")
    urls=[
      f"https://prod-public-api.livescore.com/v1/api/app/date/soccer/{ds}/0?MD=1&countryCode=US&locale=en",
      f"https://prod-public-api.livescore.com/v1/api/app/date/soccer/{ds}/0?MD=1&locale=en",
    ]
    for u in urls:
        try:
            b=fetch_json(u)
            if isinstance(b.get("Stages"),list):
                return ds,u,b
        except Exception:
            pass
    return ds,None,{"Stages":[]}

def clean(v):
    return " ".join(v.split()) if isinstance(v,str) else ""

def team(evt,key):
    rows=evt.get(key)
    if not isinstance(rows,list) or not rows or not isinstance(rows[0],dict): return ""
    return clean(rows[0].get("Nm") or rows[0].get("Name") or "")

def parse_esd(evt):
    s=str(evt.get("Esd") or "")
    if not re.fullmatch(r"\\d{14}",s): return None
    return datetime.strptime(s,"%Y%m%d%H%M%S").replace(tzinfo=UTC)

def finished(evt):
    eps=clean(evt.get("Eps")).upper()
    return eps in {"FT","AET","PEN","AFTER PEN.","AFTER ET"} or evt.get("Esid") in {6,"6"}

def score(evt):
    try: a,b=int(evt.get("Tr1")),int(evt.get("Tr2"))
    except: return None
    return (a,b) if 0<=a<=20 and 0<=b<=20 else None

def match_targets(name):
    n=norm(name)
    return [team for team,als in ALIAS_NORMS.items() if n in als]

def collect_history():
    by=defaultdict(list); seen=set(); matched_names=defaultdict(set)
    start=datetime(2026,6,16,tzinfo=UTC)
    end=datetime(2026,10,13,tzinfo=UTC)
    days=[]; d=end
    while d>=start:
        days.append(d); d-=timedelta(days=1)
    with ThreadPoolExecutor(max_workers=12) as ex:
        futs={ex.submit(fetch_day,d):d for d in days}
        for fut in as_completed(futs):
            ds,url,b=fut.result()
            if not url: continue
            for st in b.get("Stages",[]):
                if not isinstance(st,dict): continue
                country=clean(st.get("Cnm") or st.get("Csnm") or st.get("Ccd"))
                comp=clean(st.get("Snm") or st.get("Sdn") or st.get("CompN"))
                text=f"{country} {comp}"
                if FRIENDLY_RE.search(text) or NONSTANDARD_RE.search(text): continue
                for e in st.get("Events",[]) or []:
                    if not isinstance(e,dict) or not finished(e): continue
                    sc=score(e); ko=parse_esd(e)
                    if sc is None or ko is None or ko>=CUTOFF-timedelta(hours=2): continue
                    hn,an=team(e,"T1"),team(e,"T2")
                    if not hn or not an: continue
                    eid=str(e.get("Eid") or e.get("Id") or f"{ds}:{hn}:{an}")
                    for target,perspective,opp,gf,ga in (
                        *[(t,"home",an,sc[0],sc[1]) for t in match_targets(hn)],
                        *[(t,"away",hn,sc[1],sc[0]) for t in match_targets(an)],
                    ):
                        key=(target,eid)
                        if key in seen: continue
                        seen.add(key); matched_names[target].add(hn if perspective=="home" else an)
                        by[target].append({
                          "kickoff_utc":ko.isoformat(),"goals_for":gf,"goals_against":ga,
                          "opponent":opp,"competition":comp,"country":country,
                          "source_url":url,"event_id":eid,
                        })
    for k in by: by[k].sort(key=lambda x:x["kickoff_utc"],reverse=True)
    return by,matched_names

def metrics(games):
    g=games[:8]; n=len(g)
    if n<4:return None
    return {
      "gf":sum(x["goals_for"] for x in g)/n,
      "ga":sum(x["goals_against"] for x in g)/n,
      "over2":sum(x["goals_for"]+x["goals_against"]>=3 for x in g)/n,
      "over3":sum(x["goals_for"]+x["goals_against"]>=4 for x in g)/n,
      "stall":sum(x["goals_for"]+x["goals_against"]<=2 for x in g)/n,
      "trap":sum((x["goals_for"],x["goals_against"]) in {(0,0),(1,1)} for x in g)/n,
      "n":n,
    }

def gate(h,a):
    hr=(h["gf"]+a["ga"])/2; ar=(a["gf"]+h["ga"])/2
    carrier=max(hr,ar); second=min(hr,ar)
    over2=(h["over2"]+a["over2"])/2
    over3=(h["over3"]+a["over3"])/2
    stall=(h["stall"]+a["stall"])/2
    trap=(h["trap"]+a["trap"])/2
    score=max(0,min(100,round(15*carrier+14*second+22*over2-12*stall)))
    ok=score>=60 and over2>=.55 and trap<=.35
    return {"status":"DISCOVERY_GOAL_QUALIFIED" if ok else "WATCH_GOAL_SIGNAL",
      "priority_score":score,"mean_over_two_rate":round(over2,4),
      "mean_over_three_rate":round(over3,4),"mean_0_0_or_1_1_rate":round(trap,4),
      "home_route":round(hr,3),"away_route":round(ar,3),"carrier_route":round(carrier,3),
      "thresholds":{"minimum_priority_score":60,"minimum_mean_over_two_rate":.55,"maximum_mean_0_0_or_1_1_rate":.35}}

def main():
    src=json.loads(SOURCE.read_text())
    rows={r["match_id"]:r for r in src["fixtures"] if r.get("match_id") in TARGET_IDS}
    history,matched=collect_history()
    out=[]
    for mid in sorted(TARGET_IDS,key=lambda x:rows[x]["kickoff_utc"]):
        r=rows[mid]; evidence=r.get("football_evidence")
        origin="FROZEN_SOURCE"
        if not isinstance(evidence,dict):
            hg=history.get(r["home"],[])[:8]; ag=history.get(r["away"],[])[:8]
            evidence={"home":{"recent":hg},"away":{"recent":ag}}
            origin="PREMATCH_NAME_ALIAS_REPAIR"
        hm=metrics(evidence.get("home",{}).get("recent",[])); am=metrics(evidence.get("away",{}).get("recent",[]))
        if hm and am:
            assessment=gate(hm,am)
            status=assessment["status"]
        else:
            assessment=None; status="EVIDENCE_STILL_MISSING"
        out.append({
          "match_id":mid,"competition":r["competition"],"home":r["home"],"away":r["away"],
          "kickoff_utc":r["kickoff_utc"],"evidence_origin":origin,
          "home_history_count":len(evidence.get("home",{}).get("recent",[])),
          "away_history_count":len(evidence.get("away",{}).get("recent",[])),
          "home_matched_names":sorted(matched.get(r["home"],set())),
          "away_matched_names":sorted(matched.get(r["away"],set())),
          "home_recent":evidence.get("home",{}).get("recent",[])[:8],
          "away_recent":evidence.get("away",{}).get("recent",[])[:8],
          "assessment_status":status,"goal_screen":assessment,
        })
    payload={
      "schema_version":"football-v4-pending-goal-research-assessment-v1",
      "run_id":"V4-20261014-1725-20261015-0000",
      "historical_cutoff_utc":CUTOFF.isoformat(),
      "assessment_note":"Only finished competitive matches before the frozen sweep cutoff were admitted; Oct 14 target outcomes are excluded.",
      "count":len(out),
      "goal_priority_count":sum(x["assessment_status"]=="DISCOVERY_GOAL_QUALIFIED" for x in out),
      "watch_count":sum(x["assessment_status"]=="WATCH_GOAL_SIGNAL" for x in out),
      "evidence_missing_count":sum(x["assessment_status"]=="EVIDENCE_STILL_MISSING" for x in out),
      "matches":out,
    }
    OUT.write_text(json.dumps(payload,indent=2,ensure_ascii=False,sort_keys=True)+"\n")
    print(json.dumps(payload,indent=2,ensure_ascii=False))
if __name__=="__main__":main()
