# Football Betting Procedure

**Status:** ACTIVE  
**Official model:** Football v0.2.54  
**Base:** v0.2.47 CLEAN  
**Active patches:** v0.2.49 TWO-SIDED PRIORITY + v0.2.50 EGE + v0.2.51 CHANCE-QUALITY / MARKET-CONFIRMATION + v0.2.52 CARRIER CEILING / B+ EVIDENCE HARDENING + v0.2.53 RANKING INTEGRITY + v0.2.54 SELECTION INVERSION GUARD / PROMOTION QUARANTINE  
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
- route-quality label where available;
- CC+/CC+ candidate state where available;
- primary/secondary routes;
- main failure mode;
- XI sensitivity;
- structural burden.

Do not rebuild PRE later. Airtable sync conflicts are persistence faults, not permission to reconstruct history.

A genuine frozen PRE PASS remains non-actionable unless a documented material football change creates a valid new assessment epoch under the active model. Market movement alone cannot resurrect PASS.

---

## 3. Official order

`STRUCTURAL QUALITY → ROUTE QUALITY PROOF → CARRIER CEILING / CC+ → FAILURE-MODE RESISTANCE → TEAM GF/GA PROFILE → CHANCE-QUALITY HARDENING → FIRST-PASS XI → MANDATORY MARKET-HISTORY ATTEMPT → MARKET-HISTORY CONFLICT CHECK → FINAL XI / CARRIER REOPEN TEST → BURDEN / REGIME → MCE TEST → CURRENT PRICE → LOCK / HOLD / PASS`

Two-Sided Tier A remains the primary lane. For comparable non-Tier-A cases:

`QUALITY-PROVEN TWO-SIDED > CC+ ELITE CARRIER > NOMINAL / WEAK-SECONDARY TWO-SIDED > ordinary CARRIER-LED > FRAGILE / OTHER`

Price and market history cannot create structure.

---

## 4. Confirmed XI

First-pass XI is football-led and market-blind.

Review creators, finishers, shape, defensive absences, rotation, cohesion, starter/bench quality, route survival, carrier ceiling and failure-mode changes.

Classify rotation as:
- `ROTATION — ATTACKING DEPTH PRESERVED`;
- `ROTATION — COHESION / ROUTE DAMAGE`.

Under v0.2.52, `ATTACKING DEPTH PRESERVED` is **neutral baseline confirmation**, not a positive upgrade. Use `XI UPGRADE` only when the confirmed lineup materially improves the attacking case relative to the frozen uncertainty.

If both sides lose important attacking routes, or primary + secondary route are both materially weakened, apply `DUAL-ROUTE XI DAMAGE`. A lower protected line cannot by itself rescue an A2/B+ under this tag.

### 4.1 Carrier reopen — XI confirmed

A frozen B/PASS may enter a narrow new assessment epoch only as:

`CARRIER REOPEN — XI CONFIRMED`

All must be true:

1. the frozen PASS was not a hard structural rejection such as severe chance-quality failure, elite suppression, deep control/format risk, or scope exclusion;
2. PRE already contained a plausible self-funded carrier ceiling or `CC+ CANDIDATE — XI SENSITIVE` signal;
3. the PASS was driven mainly by recent-score suppression, weak opponent contribution, or lineup uncertainty;
4. confirmed XI preserves the principal carrier creators/finishers or equivalent senior replacements;
5. independent football evidence still supports a 3-goal team ceiling;
6. the proposed burden is conservative, normally no higher than O2.5 unless the active model independently supports more;
7. price is evaluated only after this football gate clears.

Market movement alone cannot trigger this reopen.

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
- only the strict v0.2.52 `CARRIER REOPEN — XI CONFIRMED` football gate may reopen a qualifying carrier PASS;
- final PASS may be reaffirmed after market history is FOUND or UNAVAILABLE-AFTER-ATTEMPT.

A response that says `PASS` while also saying opening odds were never checked is procedurally incomplete unless the user explicitly requested the market-history step be skipped.

---

## 6. Chance-quality and route-quality hardening

Before final promotion, retain team-profile review: season/recent GF-GA, scoring/conceding 2+, suppression, home/away and competition context.

For **STANDARD O3.0+ from A1/A2 TWO-SIDED**, v0.2.51 requires repeatable high-value chance support across both routes where available: big chances, central/box access, quality SOT, xG/xGOT, or a strong data-poor substitute.

Under v0.2.52, also decide whether the matchup is:

- `TWO-SIDED — QUALITY PROVEN`; or
- `TWO-SIDED — NOMINAL / WEAK SECONDARY`.

If the second route is mainly theoretical, lineup-preserved, or inferred from defensive leakage, it does not receive the full Two-Sided Priority premium.

For a carrier case, separately test `CC+ — CARRIER CEILING`: credible independent 3+ team-goal potential, repeatable attacking evidence, enough depth to sustain pressure, and no dominant opponent suppression.

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

For **B+** with an explicit derby/first-leg/1-0/1-1/control/weak-secondary/late-goal-dependence branch, v0.2.52 hardens the rule:

- XI preservation is neutral;
- protected line is execution protection, not football evidence;
- price is not a structural gate.

Therefore **XI preservation + protected line alone cannot LOCK**.

Require at least one independent positive gate beyond preservation:

- fresh chance-quality evidence materially stronger than the frozen uncertainty;
- a genuine `XI UPGRADE`;
- verified same-source bullish market corroboration that agrees with intact football evidence;
- material opponent defensive weakening;
- strong `CC+` self-funded carrier evidence that survives the named compression branch.

If none clears:

`B+ PRESERVATION-ONLY HOLD`

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

## 9. MCE +0.25 — shadow only

After STANDARD burden is set, the legacy v0.2.51 validator may be run only as a prospective shadow comparison:

`SHADOW MCE +0.25 — NO OFFICIAL EXPOSURE`

All active v0.2.51 conditions must clear, including:
- A2 FOCUS or B+ WATCHLIST TWO-SIDED;
- frozen burden >= O2.5;
- final XI preserved;
- credible 3-goal ceiling from football evidence;
- same-source/normalized bullish +0.25 OPEN→post-XI move;
- current line only +0.25 above frozen burden;
- current price >=1.75;
- no dominant suppression/compression branch.

MCE cannot rescue PASS, create TWO-SIDED/EGE, jump more than +0.25, override DUAL-ROUTE XI DAMAGE, or override a dominant failure mode. Under v0.2.54 it cannot create official exposure even when every validator field passes. Use the supported STANDARD/EGE burden directly when available; otherwise use `QUALIFIED — WAIT FOR DECAY` at the recorded target burden/price.

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
Require actionable scope, valid frozen candidate or strict prematch carrier reopen, surviving XI, acceptable failure mode, a directly offered supported STANDARD/EGE burden, current prematch price clearing policy, and no dependence on a quarantined mechanism.

A fragile B+ may not LOCK from preservation + protection alone.

### QUALIFIED — WAIT FOR DECAY
Use when every football gate clears at a recorded target burden but the current line is higher than that burden or the price at the target burden is below the executable floor. Preserve structural rank and keep the candidate active; record target line and minimum price.

### STRUCTURAL HOLD
Use when route proof, chance quality, failure mode, league regime, XI integrity, burden fit, or evidence confidence fails/remains materially unresolved. Price or clock decay cannot promote this state.

### SHADOW ONLY
Use for MCE/+0.25 and all new live/decay Over entries under v0.2.54. Record the contemporaneous hypothetical exposure for audit, but create no official exposure or official P/L.

### PASS
Use when the structure is materially invalidated or the frozen PRE was already a genuine PASS and no valid `CARRIER REOPEN — XI CONFIRMED` epoch exists.

Before final PASS in Step 2, market-history status must be FOUND / UNAVAILABLE-ATTEMPTED / USER-SKIPPED.

HOLD/PASS = no exposure.

---

## 12. Same-window rerank

When multiple FOCUS/WATCHLIST/eligible carrier-reopen matches overlap, rerank them together after XI/market-history review.

Do not compare only grades. Compare:

- quality-proven vs nominal two-sidedness;
- self-funded carrier ceiling / CC+;
- chance-quality support;
- failure-mode resistance;
- dependence on the weaker team's contribution;
- burden required by the executable total.

A nominal B+ TWO-SIDED candidate must not outrank a materially stronger CC+ carrier solely because it has two theoretical scoring routes.

Price remains a tie-breaker/execution factor after structural ranking, not the primary sorter.

---

## 13. v0.2.53 execution validators

### Non-compensatory order

For prospective official decisions, apply:

`SCOPE / LEAGUE REGIME → ROUTE PAIR → DOMINANT FAILURE MODE → CHANCE QUALITY → CC+ → BURDEN FIT → EVIDENCE CONFIDENCE → XI / MARKET VALIDATION → CURRENT PRICE`

An earlier hard failure cannot be offset by price, market movement, raw GF/GA, familiar attackers, or lineup preservation.

### MCE validator

Under v0.2.54 this validator is shadow-only. Before recording `SHADOW MCE +0.25 — NO OFFICIAL EXPOSURE`, preserve every v0.2.53 validator field. MCE is valid only for a prematch post-XI A2 FOCUS or B+ WATCHLIST whose route pair is at least `SUPPORTED + SUPPORTED`, with all original v0.2.51 conditions satisfied.

Hard-fail MCE when any of the following applies:

- PRE grade is A1, B/PASS, or UNRESOLVED;
- the assessment is live/in-play;
- the claimed signal is same-line price decay after scoreless minutes;
- there is no verified same-source/normalized OPEN → post-XI prematch line move of at least +0.25;
- the current line is not exactly +0.25 above the frozen burden;
- price is below 1.75;
- route proof, XI preservation, chance quality, failure mode, or a league-specific gate is unresolved or failed.

On any failure use:

`MCE INVALID — STANDARD BURDEN OR HOLD`

Live price decay is `STANDARD DECAY`, never MCE.

### Live Over gate

Under v0.2.54, every new live/decay Over is `SHADOW LIVE/DECAY — NO OFFICIAL EXPOSURE`. A valid shadow observation still requires one synchronized evidence epoch containing score, minute, executable line/odds, current chance-quality evidence, conversion-quality assessment, and remaining-goal-budget assessment.

If current live chance quality is missing, stale, or unsynchronized:

`LIVE CHANCE QUALITY UNAVAILABLE — HOLD`

Score/minute/price alone cannot produce a live LOCK. Goal-driven line expansion remains a no-chase state.

### CSL high-burden gate

China Super League remains CONDITIONAL. Before O3.0+ or MCE, require both relevant home/away environments to support 3+ or one true CC+ carrier whose burden survives weak opponent contribution. Otherwise HOLD/PASS.

### Same-window final rerank

Rerank surviving matches by route pair, chance quality, CC+, failure-mode resistance, lower supported burden, and evidence confidence. Price is considered only after this football order is stable.


---

## 14. v0.2.54 structural rank and execution class

Keep separate fields for `Structural Rank` and `Execution Class`. Final XI or a genuine football change may downgrade/upgrade structural rank; price, line movement and elapsed time may not increase it.

Same-window output must list every surviving candidate by structural rank, then classify it as:

- `DIRECT LOCK ELIGIBLE`;
- `QUALIFIED — WAIT FOR DECAY`;
- `STRUCTURAL HOLD`; or
- `SHADOW ONLY`.

Only DIRECT LOCK ELIGIBLE candidates enter the official exposure pool. Qualified waiting candidates remain on the active watch list at their structural position. A lower-ranked direct candidate may receive exposure ahead of a higher-ranked waiting candidate only because the higher candidate is not executable; record the distinction rather than calling the higher candidate structurally weaker.

MCE/+0.25 and all live/relative-decay Over entries remain shadow-only until the release gate in `MODEL_RULES_FOOTBALL_V0.2.54.md` is satisfied and a later user-approved model version removes the quarantine.
