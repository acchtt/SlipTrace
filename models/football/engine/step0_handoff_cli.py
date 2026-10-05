from __future__ import annotations
import argparse, json, sys
from pathlib import Path
from typing import Any

HANDOFF_VERSION = "football-step0-handoff-v2"
FIELDS = ("xi_expected","market_observability","team_news_observability","operational_viability_reason","competition_reliability_state","competition_reliability_reason")
class Step0HandoffError(ValueError): pass

def _mid(r):
    v=r.get("match_id")
    if not isinstance(v,str) or not v.strip(): raise Step0HandoffError("HANDOFF INCOMPLETE — STABLE FIXTURE ID MISSING")
    return v.strip()

def validate_step0_handoff(p: dict[str,Any]):
    if p.get("handoff_version") != HANDOFF_VERSION: raise Step0HandoffError(f"handoff_version must be {HANDOFF_VERSION}")
    for k in ("complete","actionable_complete","work_ready"):
        if p.get(k) is not True: raise Step0HandoffError(f"HANDOFF INCOMPLETE — {k}=true required")
    a,q=p.get("admitted_fixtures"),p.get("capacity_queue")
    if not isinstance(a,list): raise Step0HandoffError("HANDOFF INCOMPLETE — admitted_fixtures missing")
    if not isinstance(q,list): raise Step0HandoffError("HANDOFF INCOMPLETE — STEP0 CAPACITY QUEUE MISSING")
    if len(a)>15: raise Step0HandoffError("HANDOFF INCOMPLETE — OPERATIONAL CAPACITY BREACH")
    aids=set()
    for r in a:
        m=_mid(r); aids.add(m)
        if r.get("operational_viability_grade") not in {"A","B"}: raise Step0HandoffError(f"HANDOFF INCOMPLETE — {m} not grade A/B")
        for k in FIELDS:
            if not isinstance(r.get(k),str) or not r[k].strip(): raise Step0HandoffError(f"HANDOFF INCOMPLETE — STEP0 OPERATIONAL CONTRACT MISSING: {m} missing {k}")
    qids=set(); ranks=set()
    for r in q:
        m=_mid(r)
        if m in qids: raise Step0HandoffError(f"HANDOFF INCOMPLETE — DUPLICATE QUEUE FIXTURE ID: {m}")
        qids.add(m)
        if r.get("final_step0_disposition",r.get("disposition")) not in {"ADMITTED_TO_C","OPERATIONAL_CAPACITY_DEFERRED"}: raise Step0HandoffError(f"HANDOFF INCOMPLETE — invalid queue disposition: {m}")
        for k in FIELDS:
            if not isinstance(r.get(k),str) or not r[k].strip(): raise Step0HandoffError(f"HANDOFF INCOMPLETE — STEP0 OPERATIONAL CONTRACT MISSING: {m} missing {k}")
        n=r.get("step0_capacity_queue_rank")
        if isinstance(n,bool) or not isinstance(n,int) or n<1 or n in ranks: raise Step0HandoffError(f"HANDOFF INCOMPLETE — STEP0 CAPACITY QUEUE INVALID: {m}")
        ranks.add(n)
    if ranks != set(range(1,len(q)+1)): raise Step0HandoffError("HANDOFF INCOMPLETE — STEP0 CAPACITY QUEUE INVALID: ranks not contiguous")
    if not aids.issubset(qids): raise Step0HandoffError(f"HANDOFF INCOMPLETE — STEP0 CAPACITY QUEUE MISSING ADMITTED FIXTURES: {sorted(aids-qids)}")
    if p.get("admitted_to_c_count") != len(a): raise Step0HandoffError("HANDOFF INCOMPLETE — admitted count mismatch")
    deferred=sum(r.get("final_step0_disposition",r.get("disposition"))=="OPERATIONAL_CAPACITY_DEFERRED" for r in q)
    if p.get("capacity_deferred_count") != deferred: raise Step0HandoffError("HANDOFF INCOMPLETE — deferred count mismatch")
    return {"step0_handoff_validation_status":"PASS","admitted_count":len(a),"capacity_queue_count":len(q),"capacity_deferred_count":deferred}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--input",required=True); ns=ap.parse_args()
    try: out=validate_step0_handoff(json.loads(Path(ns.input).read_text(encoding="utf-8")))
    except (OSError,json.JSONDecodeError,Step0HandoffError) as e:
        print(json.dumps({"ok":False,"error":str(e)}),file=sys.stderr); return 2
    print(json.dumps({"ok":True,**out},indent=2)); return 0
if __name__=="__main__": raise SystemExit(main())
