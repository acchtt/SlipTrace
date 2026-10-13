#!/usr/bin/env python3
"""Source-backed prospective goal-count distributions and Asian Over sensitivity.

Independent Poisson is an explicitly UNCALIBRATED statistical hypothesis.
Unlike researcher-entered central estimates, lambda is calculated from
verified pre-KO venue-matched goals-for and goals-against game samples.
No calculated EV, market quote, model state, or final score can authorise BET.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlsplit

from core import settle_over

SCHEMA = "football-goal-probability-experiment-v1"
CALIBRATION_SCHEMA = "football-goal-probability-holdout-v1"
MIN_TEAM_GAMES = 6
MAX_TEAM_GAMES = 30
MIN_VALIDATION_FIXTURES = 100
QUOTE_MAX_AGE_SECONDS = 120
MAX_GOALS = 24


class GoalProbabilityError(ValueError):
    pass


def _date(value, field):
    if not isinstance(value, str):
        raise GoalProbabilityError(f"{field} requires timestamp")
    try:
        d = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as e:
        raise GoalProbabilityError(f"{field} invalid ISO timestamp") from e
    if d.utcoffset() is None:
        raise GoalProbabilityError(f"{field} requires explicit timezone")
    return d.astimezone(timezone.utc)


def _source(value, field):
    if not isinstance(value, str):
        raise GoalProbabilityError(f"{field} missing HTTPS source")
    p = urlsplit(value)
    if p.scheme != "https" or not p.hostname or "." not in p.hostname or p.username or p.password:
        raise GoalProbabilityError(f"{field} must be public HTTPS")
    return value


def _num(value, field, lo, hi):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise GoalProbabilityError(f"{field} needs numeric value")
    val = float(value)
    if not math.isfinite(val) or not lo <= val <= hi:
        raise GoalProbabilityError(f"{field} out of range")
    return val


def _events(obj, side, forecast_time):
    if not isinstance(obj, dict):
        raise GoalProbabilityError(f"{side} evidence missing")
    _source(obj.get("source_url"), f"{side}.source_url")
    observed = _date(obj.get("observed_at_utc"), f"{side}.observed_at_utc")
    if observed > forecast_time or forecast_time-observed > timedelta(days=7):
        raise GoalProbabilityError(f"{side} source future/stale")
    games = obj.get("venue_matched_games")
    if not isinstance(games, list) or not MIN_TEAM_GAMES <= len(games) <= MAX_TEAM_GAMES:
        raise GoalProbabilityError(f"{side} needs 6-30 venue-matched completed games")
    used, gf, ga = set(), 0, 0
    for i, game in enumerate(games):
        if not isinstance(game, dict):
            raise GoalProbabilityError(f"{side}[{i}] game object missing")
        key = game.get("fixture_id")
        if not isinstance(key, str) or not key or key in used:
            raise GoalProbabilityError(f"{side} duplicate/missing historical fixture id")
        used.add(key)
        kickoff = _date(game.get("kickoff_utc"), f"{side}[{i}].kickoff_utc")
        if kickoff > forecast_time-timedelta(minutes=120):
            raise GoalProbabilityError(f"{side} recent result not provably final before forecast")
        if kickoff < forecast_time-timedelta(days=365):
            raise GoalProbabilityError(f"{side} games older than one year unsupported")
        if game.get("venue") != ("HOME" if side == "home" else "AWAY"):
            raise GoalProbabilityError(f"{side} non-venue-matched historical fixture")
        for field in ("goals_for", "goals_against"):
            value = game.get(field)
            if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value <= 20:
                raise GoalProbabilityError(f"{side}[{i}].{field} must be recorded integer goals")
        gf += game["goals_for"]
        ga += game["goals_against"]
    return {"sample_size":len(games), "goals_for_per_game":gf/len(games),
            "goals_against_per_game":ga/len(games), "source_url":obj["source_url"]}


def _poisson(lam):
    if not 0 <= lam <= 12:
        raise GoalProbabilityError("unsupported expected-goals rate")
    probs = [math.exp(-lam)]
    for k in range(1, MAX_GOALS+1):
        probs.append(probs[-1]*lam/k)
    return probs


def _distribution(total):
    p = _poisson(total)
    tail = max(0.0, 1-sum(p))
    return p, tail


def _outcome_profit(line, odds, n):
    return settle_over(line,n,odds)[1]


def _quote(raw, frozen, now, ko, distribution, tail):
    if not isinstance(raw, dict) or raw.get("market_phase") != "PREMATCH":
        raise GoalProbabilityError("quote must be a genuine prematch offer")
    observed = _date(raw.get("observed_at_utc"), "quote.observed_at_utc")
    if not frozen <= observed <= now < ko or (now-observed).total_seconds()>QUOTE_MAX_AGE_SECONDS:
        raise GoalProbabilityError("quote not prospectively fresh/current")
    _source(raw.get("source_url"),"quote.source_url")
    line = _num(raw.get("line"),"quote.line",0,12)
    if abs(line*4-round(line*4))>1e-8:
        raise GoalProbabilityError("quoted Asian total must be quarter-goal line")
    odds = _num(raw.get("decimal_odds"),"quote.decimal_odds",1.001,1000)
    values = [_outcome_profit(line,odds,n) for n in range(MAX_GOALS+1)]
    model_ev = sum(v*p for v,p in zip(values,distribution))+tail*(odds-1)
    return {
        "line":line,"decimal_odds":odds,
        "observed_at_utc":observed.isoformat(),"source_url":raw["source_url"],
        "model_conditional_unit_profit":round(model_ev,6),
        "model_conditional_break_even_or_better":model_ev>0,
        "probability_model_calibrated":False,
        "positive_ev_established":False,
        "bet_authorized":False,
        "at_two_goals":settle_over(line,2,odds)[0].value,
        "at_three_goals":settle_over(line,3,odds)[0].value,
        "at_four_goals":settle_over(line,4,odds)[0].value,
        "full_win_goals":next((n for n in range(MAX_GOALS+1)
                               if settle_over(line,n)[0].value=="WIN"),None),
    }


def estimate(payload):
    if not isinstance(payload,dict) or payload.get("schema_version")!=SCHEMA:
        raise GoalProbabilityError("goal-probability schema invalid")
    if payload.get("market_independent_inputs") is not True:
        raise GoalProbabilityError("football inputs must be independent of bookmaker pricing")
    illegal = {"ft_score","ft_total","actual_result","live_score","actual_bet","pnl",
               "model_action","market_center","bookmaker_implied_lambda"}
    if illegal.intersection(payload):
        raise GoalProbabilityError("live/outcome/market-implied feature contamination")
    for field in ("match_id","evidence_epoch_id"):
        if not isinstance(payload.get(field),str) or not payload[field]:
            raise GoalProbabilityError(f"{field} required")
    now = _date(payload.get("assessment_at_utc"),"assessment_at_utc")
    frozen = _date(payload.get("frozen_at_utc"),"frozen_at_utc")
    ko = _date(payload.get("kickoff_utc"),"kickoff_utc")
    if not frozen<=now<ko:
        raise GoalProbabilityError("probability must be frozen prospectively")
    h = _events(payload.get("home"),"home",frozen)
    a = _events(payload.get("away"),"away",frozen)
    # Transparent independent-Poisson attack / opponent-defence averaging.
    # NO claimed team strength prior or market-derived adjustment.
    home_lambda=(h["goals_for_per_game"]+a["goals_against_per_game"])/2
    away_lambda=(a["goals_for_per_game"]+h["goals_against_per_game"])/2
    p,tail=_distribution(home_lambda+away_lambda)
    q=payload.get("quotes",[])
    if not isinstance(q,list) or len(q)>20:
        raise GoalProbabilityError("quotes must be bounded array")
    quotes=[_quote(x,frozen,now,ko,p,tail) for x in q]
    if len({(x["line"],x["observed_at_utc"],x["source_url"]) for x in quotes})!=len(quotes):
        raise GoalProbabilityError("duplicate quote source/epoch/line")
    result = {
        "schema_version":SCHEMA,"match_id":payload["match_id"],
        "evidence_epoch_id":payload["evidence_epoch_id"],
        "model":"INDEPENDENT_POISSON_VENUE_SCORES_UNCALIBRATED",
        "calibration_status":"UNVALIDATED_RESEARCH_ONLY",
        "expected_home_goals":round(home_lambda,6),
        "expected_away_goals":round(away_lambda,6),
        "expected_total_goals":round(home_lambda+away_lambda,6),
        "home_evidence":h,"away_evidence":a,
        "p_at_least_3":round(sum(p[3:])+tail,6),
        "p_at_least_4":round(sum(p[4:])+tail,6),
        "p_at_least_5":round(sum(p[5:])+tail,6),
        "total_goal_probs_0_to_24":[round(v,10) for v in p],
        "tail_probability_over_24":round(tail,12),
        "quotes":quotes,
        "bet_authorized":False,
        "c_or_c2_policy_changed":False,
        "validation_required_minimum_unique_fixtures":MIN_VALIDATION_FIXTURES,
        "interpretation":"Research distribution assumes independent Poisson home/away goals and venue-matched goals history; neither goals nor modeled quote returns are calibrated/positive-EV guarantees. Cross-validate before changing C/C2 thresholds.",
    }
    return result


def validate_holdout(payload):
    if not isinstance(payload,dict) or payload.get("schema_version")!=CALIBRATION_SCHEMA:
        raise GoalProbabilityError("holdout schema invalid")
    records=payload.get("sealed_matches")
    if not isinstance(records,list):
        raise GoalProbabilityError("sealed_matches required")
    seen=set()
    buckets={k:{"n":0,"predicted":0.0,"realized":0} for k in (3,4,5)}
    brier={3:0.0,4:0.0,5:0.0}
    for r in records:
        if not isinstance(r,dict):
            raise GoalProbabilityError("holdout record invalid")
        mid=r.get("match_id")
        if not isinstance(mid,str) or not mid or mid in seen:
            raise GoalProbabilityError("missing or duplicate holdout fixture")
        seen.add(mid)
        freeze=_date(r.get("frozen_at_utc"),"holdout.frozen_at_utc")
        ko=_date(r.get("kickoff_utc"),"holdout.kickoff_utc")
        observed=_date(r.get("result_observed_at_utc"),"holdout.result_observed_at_utc")
        if not freeze<ko or observed<ko+timedelta(minutes=90):
            raise GoalProbabilityError("holdout forecast/result chronology invalid")
        total=r.get("actual_total_goals")
        if isinstance(total,bool) or not isinstance(total,int) or not 0<=total<=30:
            raise GoalProbabilityError("holdout total goals invalid")
        for k in (3,4,5):
            pr=_num(r.get(f"p_at_least_{k}"),f"holdout.p{k}",0,1)
            y=int(total>=k)
            brier[k]+=(pr-y)**2
            buckets[k]["n"]+=1
            buckets[k]["predicted"]+=pr
            buckets[k]["realized"]+=y
    n=len(records)
    out={
        "schema_version":CALIBRATION_SCHEMA,"n":n,
        "validation_status":"ENOUGH_FOR_OUT_OF_SAMPLE_REVIEW" if n>=MIN_VALIDATION_FIXTURES else "INSUFFICIENT_UNIQUE_PROSPECTIVE_HOLDOUTS",
        "minimum_required":MIN_VALIDATION_FIXTURES,
        "no_threshold_or_bet_authority":True,
    }
    out["tail_metrics"]={str(k):{
        "mean_predicted":round(buckets[k]["predicted"]/n,6) if n else None,
        "observed_rate":round(buckets[k]["realized"]/n,6) if n else None,
        "brier_score":round(brier[k]/n,6) if n else None,
    } for k in (3,4,5)}
    return out


def main():
    a=argparse.ArgumentParser()
    a.add_argument("--input",required=True)
    a.add_argument("--output")
    a.add_argument("--mode",choices=["estimate","holdout"],default="estimate")
    z=a.parse_args()
    try:
        p=json.loads(Path(z.input).read_text(encoding="utf-8"))
        out=estimate(p) if z.mode=="estimate" else validate_holdout(p)
        s=json.dumps(out,indent=2,sort_keys=True)+"\n"
        if z.output:Path(z.output).write_text(s,encoding="utf-8")
        else:print(s)
        return 0
    except (ValueError,TypeError,OSError) as ex:
        print(json.dumps({"ok":False,"error":str(ex)}),file=sys.stderr)
        return 2


if __name__=="__main__":
    raise SystemExit(main())
