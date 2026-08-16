# Football Organized Repository Loading Guide

**Status:** Active immediately  
**Effective:** 2026-08-16  
**Repository:** `acchtt/SlipTrace`  
**Canonical namespace:** `models/football/`

## 1. Entry point

Always open:

`models/football/CURRENT_MODEL.md`

The pointer controls the active version and exact load order. Do not reconstruct the model from memory or stale root-level files.

## 2. Repository map

```text
models/
  LEGACY_MODEL_CHANGELOG.md
  football/
    CURRENT_MODEL.md
    ORGANIZED_FILE_LOADING_GUIDE.md
    rules/
    procedures/
    airtable/
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

The pre-verdict validator is an enforcement layer over **all active rules**, including later rules that postdate the validator file. A newer rule's stricter evidence burden cannot be bypassed because the validator document itself has an older effective date.

### `models/football/handoffs/`

Load the active handoff named by `CURRENT_MODEL.md`. Older handoffs are historical context only and must not override the active handoff or newer rules.

### `models/football/reviews/`

Load active audit/benchmark reviews named by `CURRENT_MODEL.md`. Reviews provide audit evidence and research protocol but do not outrank newer football rules.

### `models/LEGACY_MODEL_CHANGELOG.md`

Retains the pre-v0.2.5 football baseline. Load the football portion before the versioned amendment chain.

### `/ledger.json`

This is the single authoritative official betting record. Read it for official P/L, placement, settlement, bankroll or exposure. Do not write to it without explicit approval.

## 4. Current exact sequence

1. `models/football/CURRENT_MODEL.md`
2. `models/football/ORGANIZED_FILE_LOADING_GUIDE.md`
3. `models/LEGACY_MODEL_CHANGELOG.md` — football baseline only
4. `models/football/procedures/FOOTBALL_BETTING_PROCEDURE.md`
5. `models/football/procedures/FOOTBALL_BETTING_PROCEDURE_ADDENDUM_2026-08-01.md`
6. `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.5.md`
7. Continue sequentially through `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.47.md`
8. `models/football/procedures/FOOTBALL_PRE_VERDICT_VALIDATOR.md`
9. `models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md`
10. `models/football/reviews/FOOTBALL_DIRECTIONAL_AUDIT_2026-08-11.md`
11. `models/football/reviews/FOOTBALL_V026_V029_BENCHMARK_PROTOCOL_2026-08-11.md`
12. `models/football/handoffs/CHAT_TRANSFER_HANDOFF_2026-08-16_V2.md`
13. `/ledger.json` only when official accounting/exposure is relevant

## 5. Minimal loading by task

- General football analysis: pointer, guide, baseline, procedures, complete active rule chain.
- Live match: general set plus validator, Airtable control, active reviews, active handoff and current synchronized evidence.
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

Football v0.2.47 retains:

- v0.2.43 style/post-goal reset requirements;
- v0.2.44 verdict-first timeliness;
- v0.2.45 terminal-goal/leader-driven fallback;
- v0.2.46 pre-goal pressure-inflection detection;

and adds a mandatory **High-Scoring Halftime Compression / Goal-Saturation Gate**.

### High-scoring halftime rule

- 0-2 HT goals: normal halftime reset.
- 3 HT goals: `HT COMPRESSION GATE — MODERATE`.
- 4+ HT goals: `HT GOAL-SATURATION GATE — STRONG`.

After 3+ first-half goals, first-half openness is context only and cannot satisfy fresh second-half promotion evidence.

A post-HT Over must be supported by **second-half-only** evidence and at least one fresh conversion-quality channel. Generic possession, raw shots/SOT, corners, territory and box touches cannot prove renewed scoring hazard by themselves.

If the candidate needs two or more additional goals for a full win, the second-half evidence must support a credible multi-goal route.

After a meaningful score-stable interval, classify the current second-half scoring regime as:

- `SECOND-HALF HAZARD: RE-ACCELERATING`
- `SECOND-HALF HAZARD: PERSISTENT BUT UNPROVEN`
- `SECOND-HALF HAZARD: COMPRESSING`

`PERSISTENT BUT UNPROVEN` cannot promote an Over.

This is not a blanket Under bias. If high-quality second-half evidence appears quickly, v0.2.44 still requires immediate decision delivery once all gates genuinely pass.

### Racing Santander vs Villarreal process correction

At 2-2 HT, v0.2.47's strong saturation gate would have applied. The v0.2.46 shadow Over 5.25 @1.88 issued at 55:51 remains historically unchanged, but under v0.2.47 that state would remain HOLD unless repeated second-half conversion-quality evidence supported the two-goal full-win budget.

The user's Ajax observation remains qualitative corroboration only until formally reconstructed.

## 10. Compact startup prompt

> Load the football model from `acchtt/SlipTrace`. Open `models/football/CURRENT_MODEL.md` first and follow its exact canonical load order. Load the retained football baseline, procedures, complete v0.2.5-v0.2.47 rule chain, mandatory validator, Airtable control, active audit/benchmark reviews, and `CHAT_TRANSFER_HANDOFF_2026-08-16_V2.md`. Keep official betting paused and ledger writes on hold. Apply v0.2.43 style/post-goal resets, v0.2.44 verdict-first timeliness, v0.2.45 terminal-goal/leader-driven fallback, v0.2.46 pre-goal pressure-inflection logic, and v0.2.47 high-scoring halftime compression logic: after 3+ HT goals, first-half pressure is context only, demand second-half-only conversion-quality evidence for the exact remaining goal budget, and do not equate continued pressure with continued scoring hazard. Preserve the user-enabled independent add-on workflow. Exclude AFC Challenge/AFC Challenge League from current audit calibration. Return `FOOTBALL FILES LOADED` before analysis.