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

Historical odds are useful but not required. If unavailable, record `MARKET HISTORY UNAVAILABLE` and continue.

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

---

## 3. Official order

`STRUCTURAL QUALITY → CARRIER CEILING → FAILURE-MODE RESISTANCE → TEAM GF/GA PROFILE → CHANCE-QUALITY HARDENING → FIRST-PASS XI → MARKET-HISTORY CONFLICT CHECK → FINAL XI → BURDEN / REGIME → MCE TEST → CURRENT PRICE → LOCK / HOLD`

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

Normal Chat attempts:

`OPEN → PRE-XI → POST-XI / CURRENT PREMATCH`

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
Use when the structure is materially invalidated.

HOLD/PASS = no exposure.

---

## 12. Same-window rerank

When multiple FOCUS/WATCHLIST matches overlap, rerank together after XI/market-history review. Grade and structural quality remain ahead of price.

---

## 13. Live review

Live evidence validates/invalidates frozen PRE; it does not rewrite it.

Keep:
- no chase after goal-driven total expansion;
- post-goal normalization;
- HT compression/saturation/remaining-goal-budget logic;
- fresh chance-quality requirement after a strong first half that stalls.

A quiet half does not retroactively invalidate a protected prematch bet if carrier route and escalation capacity remain intact, but it may make a new live entry inappropriate.

---

## 14. Audit classification

Use where relevant:
- `CLEAN TWO-SIDED VALIDATION`;
- `CARRIER VALIDATION — NOT CLEAN TWO-SIDED`;
- `CHANCE-QUALITY MISS`;
- `CONVERSION VARIANCE`;
- `COMPRESSION FAILURE`;
- `FAILURE MODE TEMPORARILY ACTIVE`;
- `CQ HARDENED`;
- `DUAL-ROUTE XI DAMAGE`;
- `MCE +0.25`.

A 3-0/4-0/5-0 total win validates carrier ceiling, not automatically the losing side's scoring route.

---

## 15. Settlement and persistence

Standard full-match Asian totals settle on 90 minutes + stoppage unless explicitly stated otherwise.

Record official P/L only for actual official selections under the version that produced them. HOLD/PASS/shadow/counterfactual outcomes never enter official P/L.

Persist material Decision States and market-history evidence without rewriting frozen PRE.

---

## 16. Shadows

Official: v0.2.51. Shadows: v0.2.47 CLEAN and v0.2.48-SHADOW. Do not import v0.2.49/50/51 patches into shadows.
