# Football Organized Repository Loading Guide

**Status:** Active immediately  
**Effective:** 2026-08-15  
**Repository:** `acchtt/SlipTrace`  
**Canonical namespace:** `models/football/`

## 1. Entry point

Always open:

`models/football/CURRENT_MODEL.md`

The pointer controls the active version and exact load order. Do not reconstruct the model from memory or from stale root-level files.

## 2. Repository map

```text
models/
  LEGACY_MODEL_CHANGELOG.md
  football/
    CURRENT_MODEL.md
    ORGANIZED_FILE_LOADING_GUIDE.md
    rules/
    procedures/
    context/
    handoffs/
    reviews/
  lol/
shared/
ledger.json
```

A football chat uses `models/football/`, the retained football baseline in `models/LEGACY_MODEL_CHANGELOG.md`, explicitly required shared files, and `/ledger.json` only when accounting is relevant. Never load `models/lol/` into football context.

## 3. Folder rules

### `models/football/rules/`

Contains the cumulative amendment chain. Load every active football rule from v0.2.5 through the version named by `CURRENT_MODEL.md`, in ascending order. Newer rules control where they conflict; earlier rules remain active where not superseded.

### `models/football/procedures/`

Contains operational procedures and validators. Load all procedure files named by `CURRENT_MODEL.md` before issuing a recommendation.

### `models/football/handoffs/`

Load the active handoff named by `CURRENT_MODEL.md`. Older handoffs are historical context only and must not override the active handoff or newer rules.

### `models/football/reviews/`

Load active audit/benchmark reviews named by `CURRENT_MODEL.md`. They provide audit evidence and research protocol but do not outrank newer football rules. Process reviews may be referenced by the active handoff without becoming mandatory startup files unless `CURRENT_MODEL.md` explicitly adds them to the load order.

### `models/LEGACY_MODEL_CHANGELOG.md`

Retains the pre-v0.2.5 football baseline. Load the football portion before the versioned amendment chain.

### `/ledger.json`

This is the single authoritative official betting record. Read it for official P/L, placement, settlement, bankroll, or exposure. Do not write to it without explicit approval.

## 4. Current exact sequence

1. `models/football/CURRENT_MODEL.md`
2. `models/football/ORGANIZED_FILE_LOADING_GUIDE.md`
3. `models/LEGACY_MODEL_CHANGELOG.md` — football baseline only
4. `models/football/procedures/FOOTBALL_BETTING_PROCEDURE.md`
5. `models/football/procedures/FOOTBALL_BETTING_PROCEDURE_ADDENDUM_2026-08-01.md`
6. `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.5.md`
7. Continue sequentially through `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.45.md`
8. `models/football/procedures/FOOTBALL_PRE_VERDICT_VALIDATOR.md`
9. `models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md`
10. `models/football/reviews/FOOTBALL_DIRECTIONAL_AUDIT_2026-08-11.md`
11. `models/football/reviews/FOOTBALL_V026_V029_BENCHMARK_PROTOCOL_2026-08-11.md`
12. `models/football/handoffs/CHAT_TRANSFER_HANDOFF_2026-08-15.md`
13. `/ledger.json` only when official accounting/exposure is relevant

## 5. Minimal loading by task

- General football analysis: pointer, guide, baseline, procedures, complete active rule chain.
- Live match: general set plus validator, Airtable control, active reviews, active handoff, and current synchronized evidence.
- Settlement/bankroll: relevant model set plus `/ledger.json`.
- Historical review: active model plus specifically relevant historical evidence.
- Secondary-thread/reminder-style analysis: same active football gates as the main workflow; no reduced standard.

## 6. Precedence

1. Explicit user correction in the current chat
2. Current synchronized match and market evidence
3. Newest active football rule
4. Earlier retained football rule or procedure
5. Active handoff
6. Review evidence and historical material

For official accounting, `/ledger.json` is authoritative unless the user supplies newer confirmed placement or settlement evidence not yet written.

## 7. Missing-file rule

If a required canonical file is missing, do not substitute a stale copy. Use:

`NO BET — MODEL CONTEXT INCOMPLETE`

State the missing canonical path and resume only after it is restored.

## 8. Required acknowledgment

After loading, return:

- `FOOTBALL FILES LOADED`
- active version
- canonical namespace
- procedures and rule range loaded
- handoff status
- ledger loaded or `LEDGER NOT REQUIRED`
- any missing canonical path

## 9. Current operating emphasis

Football v0.2.45 retains the strict v0.2.43 style/post-goal layer and v0.2.44 timeliness rule, then adds a terminal-goal halftime bridge and leader-driven Over logic.

When a stable pre-goal state already clears the applicable gates, deliver the verdict immediately rather than waiting for the next goal or an unnecessary confirmation snapshot.

When a goal arrives too close to halftime for the normal post-goal persistence window to exist, do not manufacture an automatic HOLD. Perform the reset, carry forward strong pre-goal process only if v0.2.45's bridge gates pass, and test whether the leader can credibly supply the remaining goal budget itself. Trailer chase is a modifier unless the Over actually depends on trailer contribution.

Any material event before delivery invalidates the pending candidate and requires a fresh reset. Material halftime tactical changes invalidate the terminal-goal bridge until the new regime is synchronized.

Per user instruction, AFC Challenge/AFC Challenge League matches are excluded from the current audit workflow because live-stat coverage is insufficient.

## 10. Compact startup prompt

> Load the football model from `acchtt/SlipTrace`. Open `models/football/CURRENT_MODEL.md` first and follow its exact canonical load order. Load the retained football baseline, procedures, complete v0.2.5-v0.2.45 rule chain, mandatory validator, Airtable control, active audit/benchmark reviews, and the 2026-08-15 handoff. Keep official betting paused and ledger writes on hold. Apply strict v0.2.43 style/post-goal resets, v0.2.44 verdict-first timeliness, and v0.2.45 terminal-goal/leader-driven Over logic: do not delay a qualified stable total merely for extra confirmation; when a late first-half goal leaves no valid persistence window, use the halftime bridge only if its evidence gates pass and test whether the leader can fund the remaining goal budget without requiring trailer chase. Exclude AFC Challenge/AFC Challenge League from current audit calibration. Return `FOOTBALL FILES LOADED` before analysis.