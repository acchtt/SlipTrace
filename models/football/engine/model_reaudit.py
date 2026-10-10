#!/usr/bin/env python3
"""Non-blocking model QA: ranking/selection/funding consistency across frozen C+C2.

Consumes actual engine board_results and existing prospective funding QA.
No rankings, grades, prices, supported lines, user slips or BETs are changed.
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

SCHEMA = "football-model-reaudit-v1"


class ModelReauditError(ValueError):
    pass


def _board(value, expected):
    if not isinstance(value, dict) or value.get("stage") != "board_result" or value.get("model") != expected:
        raise ModelReauditError(f"{expected}: original engine board_result required")
    if value.get("schema_version") != "football-engine-v1":
        raise ModelReauditError(f"{expected}: engine schema invalid")
    rows = value.get("matches")
    if not isinstance(rows, list) or not rows:
        raise ModelReauditError(f"{expected}: full ranked matches required")
    if len(rows) != value.get("match_count"):
        raise ModelReauditError(f"{expected}: match_count discrepancy")
    ids = [r.get("match_id") for r in rows]
    ranks = [r.get("rank") for r in rows]
    if any(not isinstance(i, str) or not i for i in ids) or len(ids) != len(set(ids)):
        raise ModelReauditError(f"{expected}: match identities missing or duplicate")
    if ranks != list(range(1, len(rows) + 1)):
        raise ModelReauditError(f"{expected}: ranks must equal actual engine output order")
    for r in rows:
        if r.get("board_state") not in {"FOCUS", "WATCH", "PASS"}:
            raise ModelReauditError(f"{expected}: board state invalid")
        line = r.get("supported_line")
        if isinstance(line, bool) or not isinstance(line, (int, float)) or abs(line*4-round(line*4))>1e-9:
            raise ModelReauditError(f"{expected}: unsupported Asian line")
        if expected == "c" and r.get("follow_lane") not in {"FOLLOW", "RESERVE", "STOP"}:
            raise ModelReauditError("official C follow lane invalid")
    return rows


def _inversions(rows):
    # A higher-ranked WATCH/PASS ahead of a later FOCUS can consume positions
    # despite the board intending FOCUS to represent better opportunity.
    found = []
    for i, a in enumerate(rows):
        if a["board_state"] == "FOCUS":
            continue
        for b in rows[i+1:]:
            if b["board_state"] == "FOCUS":
                found.append({"higher_rank": a["rank"], "higher_match": a["match_id"],
                              "higher_state": a["board_state"],
                              "lower_rank": b["rank"], "lower_match": b["match_id"],
                              "lower_state": b["board_state"]})
    return found


def audit(payload):
    if not isinstance(payload, dict) or payload.get("schema_version") != SCHEMA:
        raise ModelReauditError(f"schema_version must be {SCHEMA}")
    board_id = payload.get("board_id")
    if not isinstance(board_id, str) or not board_id.strip():
        raise ModelReauditError("board_id required")
    c = _board(payload.get("c_board_result"), "c")
    c2 = _board(payload.get("c2_board_result"), "c2")
    cm = {r["match_id"]: r for r in c}
    c2m = {r["match_id"]: r for r in c2}
    if set(cm) != set(c2m):
        raise ModelReauditError("C and C2 must cover identical match identities")
    qa = payload.get("funding_readiness")
    if not isinstance(qa, dict) or qa.get("schema_version") != "football-follow-funding-readiness-v1":
        raise ModelReauditError("prospective C/C2 funding-readiness report required")
    if qa.get("board_id") != board_id or not qa.get("advisory_only") or qa.get("thresholds_changed") is not False:
        raise ModelReauditError("foreign/nonadvisory funding-readiness data")
    info = qa.get("fixtures")
    if not isinstance(info, list):
        raise ModelReauditError("complete funding-readiness rows required")
    qm = {r.get("match_id"): r for r in info}
    if len(qm)!=len(info) or set(qm)!=set(cm):
        raise ModelReauditError("funding readiness does not match the exact C/C2 board")
    missing = []
    for mid in cm:
        row = qm[mid]
        for model, board_row in (("c", cm[mid]), ("c2", c2m[mid])):
            d = row.get(model, {})
            if d.get("board_state") != board_row["board_state"] or d.get("supported_line") != board_row["supported_line"]:
                raise ModelReauditError(f"{mid}: {model} frozen state/support mismatched")
            if not isinstance(d.get("funded_at_own_supported_line"), bool):
                raise ModelReauditError(f"{mid}: {model} funding not validated")
        if row.get("official_c_follow_lane") != cm[mid]["follow_lane"]:
            raise ModelReauditError(f"{mid}: official C lane contradicts funding QA")
        if cm[mid]["follow_lane"] == "FOLLOW" and not row["c"]["funded_at_own_supported_line"]:
            missing.append(mid)
    ranked_c = _inversions(c)
    ranked_c2 = _inversions(c2)
    follow = [r for r in c if r["follow_lane"] == "FOLLOW"]
    cf = sum(qm[r["match_id"]]["c"]["funded_at_own_supported_line"] for r in follow)
    shadow_focus = [r for r in c2 if r["board_state"] == "FOCUS"]
    c2f = sum(qm[r["match_id"]]["c2"]["funded_at_own_supported_line"] for r in shadow_focus)
    warnings = []
    if ranked_c: warnings.append("C_RANK_HAS_WATCH_OR_PASS_AHEAD_OF_FOCUS")
    if ranked_c2: warnings.append("C2_RANK_HAS_WATCH_OR_PASS_AHEAD_OF_FOCUS")
    if follow and cf==0: warnings.append("ALL_C_FOLLOW_OWN_SUPPORTED_LINES_UNFUNDED")
    if shadow_focus and c2f==0: warnings.append("ALL_C2_FOCUS_OWN_SUPPORTED_LINES_UNFUNDED")
    return {
        "schema_version": SCHEMA,"board_id":board_id,
        "qa_status":"WARN_REVIEW_MODEL_DESIGN" if warnings else "NO_MODEL_ALIGNMENT_WARNING",
        "warnings":warnings,
        "c": {"match_count":len(c),"focus_count":sum(x["board_state"]=="FOCUS" for x in c),
              "follow_count":len(follow),"follow_supported_funded":cf,
              "cross_state_rank_inversion_pairs":len(ranked_c),"inversion_examples":ranked_c[:15],
              "unfunded_follow_match_ids":missing},
        "c2": {"match_count":len(c2),"focus_count":len(shadow_focus),
               "focus_supported_funded":c2f,
               "cross_state_rank_inversion_pairs":len(ranked_c2),"inversion_examples":ranked_c2[:15]},
        "model_policy_changed":False, "actions_created":False,
        "no_user_or_model_exposure_created":True,
        "interpretation":"FOCUS/WAIT/PASS classification and own-line funding are separate. Cross-state rank inversions and 0/N readiness require QA, not invented price, betting opportunity, C2 promotion, or automatic rank/policy change."
    }


def main():
    parser=argparse.ArgumentParser(description="Immutable C/C2 full-board model alignment QA")
    parser.add_argument("--input",required=True)
    parser.add_argument("--output")
    args=parser.parse_args()
    try:
        result=audit(json.loads(Path(args.input).read_text(encoding="utf-8")))
        rendered=json.dumps(result,indent=2,sort_keys=True)+"\n"
        if args.output:Path(args.output).write_text(rendered,encoding="utf-8")
        else:print(rendered)
        return 0
    except (ValueError,TypeError,OSError) as exc:
        print(json.dumps({"ok":False,"error":str(exc)}),file=sys.stderr)
        return 2


if __name__=="__main__":
    raise SystemExit(main())
