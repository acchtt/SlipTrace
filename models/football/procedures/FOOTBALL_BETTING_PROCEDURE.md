# Football Betting Procedure

**Status:** ACTIVE  
**Official model:** Football v0.2.51  
**Base:** v0.2.47 CLEAN  
**Active patches:** v0.2.49 TWO-SIDED PRIORITY + v0.2.50 EGE + v0.2.51 CHANCE-QUALITY / MARKET-CONFIRMATION  
**Shadow comparisons:** v0.2.47 CLEAN and v0.2.48-SHADOW  
**Fixture authority:** AiScore only

This procedure defines execution from frozen PRE through LOCK/HOLD/PASS. `CURRENT_MODEL.md` and active rule files are authoritative.

---

## 1. Preconditions

Do not issue an official prematch verdict unless:
1. AiScore coverage/time reconciliation passed;
2. the fixture is actionable under current scope;
3. frozen Work PRE exists or a documented equivalent current PRE exists;
4. required confirmed XI and current executable Asian-total price are available from the user, unless external verification was explicitly requested.

If XI/current price is missing: `WAITING FOR USER XI/ODDS — NO OFFICIAL DECISION`.

Market history is contextual rather than executable-price authority, but a Step-2 final verdict must not be issued with `MARKET HISTORY NOT CHECKED`. Normal Chat must first attempt a lightweight lookup and resolve to one of:
- `MARKET HISTORY FOUND`;
- `MARKET HISTORY UNAVAILABLE — ATTEMPTED`;
- `MARKET HISTORY SKIPPED — USER REQUEST`.

Unavailability does not block the assessment once the attempt has been made.

---

## 2. Frozen state

Start from frozen Work PRE:
- grade;
- archetype;
- board tier;
- primary/secondary routes;
- main failure mode;
- XI sensitivity;
- structural burden.

Do not rebuild PRE later. Airtable sync conflicts are persistence faults, not permission to reconstruct history.

A genuine frozen PRE PASS remains non-actionable unless a documented material football change creates a valid new assessment epoch under the active model. Market movement alone cannot resurrect PASS.

---

## 3. Official order

`STRUCTURAL QUALITY → CARRIER CEILING → FAILURE-MODE RESISTANCE → TEAM GF/GA PROFILE → CHANCE-QUALITY HARDENING → FIRST-PASS XI → MANDATORY MARKET-HISTORY ATTEMPT → MARKET-HISTORY CONFLICT CHECK → FINAL XI → BURDEN / REGIME → MCE TEST → CURRENT PRICE → LOCK / HOLD / PASS`

Comparable-grade hierarchy:

`TWO-SIDED > ELITE CARRIER > CARRIER-LED > FRAGILE / OTHER`

Price and market history cannot create structure.

---

## 4. Confirmed XI

First-pass XI is football-led and market-blind.

Review creators, finishers, shape, defensive absences, rotation, cohesion, starter/bench quality, route survival and failure-mode changes.

Classify rotation as:
- `ROTATION — ATTACKING DEPTH PRESERVED`;
- `ROTATION — COHESION / ROUTE DAMAGE`.

If both sides lose important attacking routes, or primary + secondary route are both materially weakened, apply `DUAL-ROUTE XI DAMAGE`. A lower protected line cannot by itself rescue an A2/B+ under this tag.

---

## 5. Market-history watch

For **every fixture the user brings to the normal Step-2 XI/odds review**, including frozen PASS, Normal Chat must make a lightweight attempt to recover:

`OPEN → PRE-XI → POST-XI / CURRENT PREMATCH`

Do not skip this step merely because the frozen structural verdict is PASS.

Prefer same-source/bookmaker history. Cross-book comparisons are `CROSS-BOOK — CONTEXT ONLY`.

Movement labels:
- `BULLISH LINE` +0.25+;
- `BEARISH LINE` -0.25+;
- `BULLISH PRICE`;
- `BEARISH PRICE`;
- `STABLE`;
- `MIXED`.

If a first-pass XI downgrade conflicts with a bullish +0.25 move, explicitly recheck whether attacking depth is actually preserved. If an XI upgrade conflicts with a bearish move, recheck hidden route loss/context.

The market does not automatically win; it forces reinspection.

### 5.1 Frozen PASS handling

For frozen PASS, market history is still captured for audit/calibration and to identify strong market disagreement with the structural read.

However:
- MCE cannot rescue PASS;
- a bullish move cannot create a scoring route;
- a line move cannot by itself create a new structural assessment epoch;
- final PASS may be reaffirmed after market history is FOUND or UNAVAILABLE-AFTER-ATTEMPT.

A response that says `PASS` while also saying opening odds were never checked is procedurally incomplete unless the user explicitly requested the market-history step be skipped.

---

## 6. Chance-quality hardening

Before final promotion, retain team-profile review: season/recent GF-GA, scoring/conceding 2+, suppression, home/away and competition context.

For **STANDARD O3.0+ from A1/A2 TWO-SIDED**, v0.2.51 requires repeatable high-value chance support across both routes where available: big chances, central/box access, quality SOT, xG/xGOT, or a strong data-poor substitute.

If the thesis is mostly names, raw goals, possession or generic attacking reputation, cap burden lower, downgrade confidence or reclassify.

---

## 7. Failure-mode gate

Before LOCK, state how the Over fails and whether the selected line survives that branch.

Common branches:
- carrier slows at 1-0/2-0;
- weak opponent route;
- central suppression;
- sterile possession;
- XI cohesion damage;
- derby/first-leg control;
- late-goal dependence.

For **B+** with an explicit derby/first-leg/1-0/1-1/control or weak-secondary branch, protection alone is insufficient under v0.2.51. Require an extra positive gate before LOCK.

---

## 8. Goal-burden regime

After final XI choose:
- `STANDARD`; or
- `EGE — EXTREME GOAL ENVIRONMENT` under v0.2.50.

### STANDARD
Use the lowest protected model-supported line. Do not stretch for price.

### EGE
Preserve frozen PRE burden, document post-XI EGE burden and independent structural/team/XI reasons, then compare current line/price. A high market line cannot create EGE.

---

## 9. MCE +0.25

After STANDARD burden is set, test the narrow v0.2.51 exception:

`MCE +0.25 — MARKET-CONFIRMED EDGE`

All active v0.2.51 conditions must clear, including:
- A2 FOCUS or B+ WATCHLIST TWO-SIDED;
- frozen burden >= O2.5;
- final XI preserved;
- credible 3-goal ceiling from football evidence;
- same-source/normalized bullish +0.25 OPEN→post-XI move;
- current line only +0.25 above frozen burden;
- current price >=1.75;
- no dominant suppression/compression branch.

MCE cannot rescue PASS, create TWO-SIDED/EGE, jump more than +0.25, override DUAL-ROUTE XI DAMAGE, or override a dominant failure mode.

---

## 10. Price policy

- hard minimum 1.65;
- preferred 1.70+;
- MCE +0.25 requires 1.75+;
- below 1.65 = `NO BET — HOLD — PRICE TOO SHORT`;
- burden before price;
- never stretch merely for a better number.

---

## 11. Verdicts

### OFFICIAL LOCK
Require actionable scope, valid frozen candidate, surviving XI, acceptable failure mode, supported STANDARD/EGE/MCE burden, and current price clearing policy.

### HOLD
Use when thesis remains live but one or more gates fail: XI uncertainty, dual-route damage, chance-quality hardening, failure-mode risk, burden, price, missing input or unexplained bearish market conflict.

### PASS
Use when the structure is materially invalidated or the frozen PRE was already a genuine PASS and no valid material football change creates a new assessment epoch.

Before final PASS in Step 2, market-history status must be FOUND / UNAVAILABLE-ATTEMPTED / USER-SKIPPED.

HOLD/PASS = no exposure.

---

## 12. Same-window rerank

When multiple FOCUS/WATCHLIST matches overlap, rerank together after XI/market-history review. Grade and structural quality remain ahead of price.
