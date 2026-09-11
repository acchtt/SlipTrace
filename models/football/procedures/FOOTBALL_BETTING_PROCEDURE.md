# Football Betting Procedure

**Status:** ACTIVE  
**Official model:** Football v0.2.50  
**Base:** v0.2.47 CLEAN  
**Active patches:** v0.2.49 Two-Sided Priority + v0.2.50 Extreme Goal Environment  
**Shadow comparisons:** v0.2.47 CLEAN and v0.2.48-SHADOW  
**Fixture authority:** AiScore only

This is the current execution procedure from frozen PRE through official LOCK/HOLD/PASS. Detailed structural rules remain in the active rule files; this procedure defines ordering and operating boundaries.

---

## 1. Preconditions

Do not issue an official prematch verdict unless:

1. the requested AiScore fixture window passed coverage and time/schedule reconciliation;
2. the fixture is actionable under the current senior-quality overlay;
3. the fixture has a frozen Work PRE state or a clearly documented equivalent current PRE state;
4. the required current confirmed XI and executable Asian-total price are available from the user, unless the user explicitly requested external verification.

If XI or current executable price is missing under the normal workflow:

`WAITING FOR USER XI/ODDS — NO OFFICIAL DECISION`

Do not reconstruct a new structural PRE merely because later evidence is available.

A historical odds snapshot is useful context but is not a required precondition. If opening/pre-XI history cannot be recovered quickly, record `MARKET HISTORY UNAVAILABLE` and continue with the valid frozen PRE + XI + current executable price.

---

## 2. Frozen structural state

Start from the frozen Work artifact:

- PRE grade;
- structural archetype;
- FOCUS/WATCHLIST/PASS/UNRESOLVED;
- primary route;
- secondary route/opponent contribution;
- main failure mode;
- XI sensitivity;
- structural total range/ceiling.

FOCUS and WATCHLIST are provisional candidates, not bets.

A genuine frozen PRE PASS is not rescued by attractive price. A documented material structural change may justify a new assessment epoch, but it must be labelled rather than silently rewriting PRE.

If Airtable conflicts with the original Work board, use the original frozen Work state and classify the discrepancy as a persistence sync fault until corrected.

---

## 3. Official structural hierarchy

Official v0.2.50 order:

`STRUCTURAL QUALITY → CARRIER CEILING → FAILURE-MODE RESISTANCE → TEAM GF/GA PROFILE → CHANCE QUALITY → XI RERANK → MARKET-HISTORY CONFLICT CHECK → GOAL BURDEN / REGIME → CURRENT PRICE → LOCK / HOLD`

For comparable grades, the active v0.2.49 rule remains:

`TWO-SIDED > ELITE CARRIER > CARRIER-LED > FRAGILE / OTHER`

A genuine TWO-SIDED profile requires credible independent scoring routes from both teams.

An ELITE CARRIER may outrank a genuine same-grade TWO-SIDED candidate only when clearly superior on both repeatable chance quality/self-funding 3+ capacity and failure-mode resistance.

Price cannot create structure. Historical market movement cannot create structure either.

---

## 4. Confirmed-XI rerank

Confirmed XI is the first legitimate rerank gate after frozen PRE.

Review:

- creators;
- finishers;
- defensive absences;
- formation and attacking shape;
- rotation;
- starter/bench quality;
- cohesion;
- whether the frozen primary and secondary routes remain intact;
- whether the frozen failure mode strengthens or weakens.

For TWO-SIDED profiles, verify both independent routes still exist.

For carrier profiles, verify the carrier still has credible self-funding capacity and that the opponent/suppression failure branch remains acceptable.

Do not treat rotation as automatically negative. Classify it as either:

- `ROTATION — ATTACKING DEPTH PRESERVED`; or
- `ROTATION — COHESION / ROUTE DAMAGE`.

Only the second is an automatic burden downgrade.

Make this **first-pass XI classification from football evidence before consulting market movement**.

---

## 5. Prematch market-history watch

For every FOCUS/WATCHLIST fixture reaching final Normal Chat review, make a lightweight attempt to recover the total-market path:

`OPEN → PRE-XI → POST-XI / CURRENT PREMATCH`

This is a Normal Chat task. Work remains price/XI blind and must not spend usage on opening-odds research.

### 5.1 Evidence priority

Prefer:

1. user-supplied history from the same bookmaker/source;
2. same-bookmaker opening/history data;
3. a reputable odds-history source with timestamped totals;
4. consensus history only when a same-source sequence is unavailable.

The user's supplied current line/price remains the execution authority unless the user explicitly asks for external current-price verification.

Do not fabricate missing history. Do not compare different bookmakers as if they were one continuous series. Mixed-source comparisons must be labelled:

`CROSS-BOOK — CONTEXT ONLY`

### 5.2 Snapshot fields

Where available preserve:

- opening Asian total;
- opening Over price;
- PRE-XI Asian total and Over price;
- POST-XI/current prematch Asian total and Over price;
- bookmaker/source;
- snapshot times;
- line delta;
- same-line price direction.

### 5.3 Movement labels

Use:

- `BULLISH LINE` — total rises by at least 0.25;
- `BEARISH LINE` — total falls by at least 0.25;
- `BULLISH PRICE` — same total with materially shorter Over price;
- `BEARISH PRICE` — same total with materially longer Over price;
- `STABLE` — no meaningful move;
- `MIXED` — line/price/source evidence conflicts.

A quarter-line move is stronger evidence than a small price-only shift.

### 5.4 XI/market conflict check

After the first-pass XI rerank, compare it with market history.

If XI appears to be `COHESION / ROUTE DAMAGE` but the total market strengthens materially, re-inspect whether the supposed downgrade is actually `ATTACKING DEPTH PRESERVED` or otherwise overstated.

If XI appears stronger but the total falls materially, re-inspect for missing context such as tactical shape, additional absences, incentives, weather/data faults, or source mismatch.

The market does **not** automatically win the disagreement. A conflict triggers reinspection.

Market history may:

- corroborate or weaken confidence in an already-supported burden;
- challenge an XI upgrade/downgrade interpretation;
- justify a cautious HOLD when a sharp unexplained bearish move conflicts with the football thesis;
- reveal that a perceived XI downgrade was not priced as meaningful route damage.

Market history may **not**:

- rewrite frozen PRE;
- create a stronger structural grade;
- create a TWO-SIDED route;
- create EGE by itself;
- raise supported burden above what structure + XI independently justify;
- justify selecting a higher line simply for a better price.

Finalize the XI rerank only after this conflict check.

---

## 6. Team-profile and chance-quality check

Before final promotion, retain the current model’s mandatory team-profile review:

- season GF/GA;
- recent relevant GF/GA;
- scoring/conceding 2+ frequencies;
- clean-sheet/suppression tendency;
- home/away splits;
- competition-specific context where useful.

Where data exists, use repeatable chance-quality evidence such as big chances, central/box access, shots-on-target quality, box touches, xG/xGA/xGOT and comparable indicators.

Chance quality is a modifier/supporting gate, not a rigid universal veto.

---

## 7. Failure-mode check

Before any LOCK, state how the Over thesis can fail and decide whether the selected line survives that branch well enough.

Common branches:

- favorite/carrier reaches 1-0 or 2-0 and slows;
- opponent has little independent scoring route;
- strong defensive opponent suppresses central access;
- possession is sterile despite volume;
- rotation damages cohesion;
- game-state incentives compress rather than expand;
- the total relies too heavily on late goals;
- attacker names are present but service/shape is weak.

A structurally attractive match may remain HOLD when the failure branch is too live.

---

## 8. Goal-burden regime

Choose the Asian-total burden **after structure, XI, and the market-history conflict check, but before current execution price**.

First classify:

- `STANDARD`; or
- `EGE — EXTREME GOAL ENVIRONMENT` under `MODEL_RULES_FOOTBALL_V0.2.50.md`.

### STANDARD

Prefer the lowest protected line that faithfully expresses the frozen thesis and remains inside the model-supported burden/range.

Do not move from O2.5 to O2.75, O3.0, O3.25, etc. merely to obtain a better price or because the market itself moved upward.

A higher total is permitted only when structural/XI evidence independently supports the extra goal burden.

### EGE

When EGE independently clears after XI:

1. preserve the frozen PRE burden as historical state;
2. create and record a new post-XI `EGE supported burden`;
3. state the structural/team/XI reasons for the higher burden;
4. compare the market line against the EGE burden only after that burden is fixed.

The market total may corroborate calibration but may not create EGE.

If the current total lies inside the EGE burden and price clears the floor, a prematch OFFICIAL LOCK is allowed. Do not wait for an arbitrary absolute decay target merely because the number looks high.

If the line is only 0.25 above the EGE ceiling, HOLD for a relative quarter-line improvement.

---

## 9. Persistent high-line / no-chase boundary

For confirmed EGE matches, a stubborn high total is not automatically a reason to HOLD forever.

A 0-0 opening around 8–15 minutes with no structural veto may corroborate the already-established EGE calibration if the total remains elevated.

However, an early goal that expands the line is different:

- do not chase the expansion;
- do not raise burden because the bookmaker raised it;
- wait for post-goal normalization;
- compare the normalized line to the previously documented supported burden.

Use audit labels where useful:

- `STANDARD DIRECT`
- `STANDARD DECAY`
- `EGE DIRECT`
- `EGE RELATIVE DECAY`
- `NON-DECAY HOLD`
- `GOAL-EXPANSION HOLD`

---

## 10. Asian-total settlement references

Standard examples:

- O2.5: 3+ goals win;
- O2.75: exactly 3 = half win / half push; 4+ = full win;
- O3.0: exactly 3 = push; 4+ = win;
- O3.25: exactly 3 = half loss / half push; 4+ = win;
- O3.5: 4+ = win;
- O3.75: exactly 4 = half win / half push; 5+ = full win;
- O4.0: exactly 4 = push; 5+ = win;
- O4.25: exactly 4 = half loss / half push; 5+ = full win.

---

## 11. Executable price policy

Current user overlay:

- hard minimum decimal odds: **1.65**;
- preferred decimal odds: **1.70+**;
- below 1.65 → `NO BET — HOLD — PRICE TOO SHORT`;
- never stretch the line just to clear 1.65/1.70;
- structural ranking is price-independent.

Current executable price is evaluated only after the correct STANDARD or EGE burden is chosen.

Historical movement is a calibration/conflict signal, not the execution-price gate.

---

## 12. Official verdict semantics

### OFFICIAL LOCK

Issue only when all required gates clear:

- actionable competition;
- valid frozen FOCUS/WATCHLIST structural thesis;
- XI does not invalidate the thesis after conflict recheck;
- main failure mode is acceptable for the proposed burden;
- selected Asian total is model-supported under STANDARD or EGE;
- current price meets the executable policy.

An affirmative official v0.2.50 final selection is an **OFFICIAL LOCK**.

### HOLD

Use when the thesis remains live but one or more final gates do not clear: unresolved contribution, XI sensitivity, failure-mode risk, goal burden, short price, missing current input, line still above supported EGE burden, or a material unexplained bearish market-history conflict.

### PASS

Use when the structural route is no longer sufficient or new evidence materially invalidates it.

HOLD/PASS creates no official exposure.

---

## 13. Shadow tracks

When a material final comparison is required, run the same frozen evidence state through:

- official v0.2.50;
- shadow v0.2.47 CLEAN;
- shadow v0.2.48-SHADOW.

Keep each version faithful to its own rules. Do not import the v0.2.49 or v0.2.50 patches into the shadow tracks.

Shadow decisions never suppress an official v0.2.50 decision and never enter official P/L.

---

## 14. User-supplied screenshot workflow

When the user sends XI/odds screenshots or text:

1. identify the fixture;
2. retrieve the frozen PRE state from the current Work/Airtable bridge;
3. verify the fixture time/status if near kickoff under the time-integrity procedure;
4. read the supplied XI;
5. make a first-pass XI rerank without using the market;
6. attempt the OPEN → PRE-XI → POST-XI/current market-history watch;
7. resolve any XI/market conflict and finalize the XI rerank;
8. read the supplied current Asian-total lines/prices;
9. classify STANDARD vs EGE;
10. choose the correct burden before comparing current prices;
11. apply the 1.65 hard floor / 1.70+ preference;
12. issue LOCK/HOLD/PASS.

Do not automatically search missing XI/current executable price unless the user explicitly asks for external verification. Historical market lookup is the exception and may be attempted automatically because it is contextual research rather than execution-price substitution.

If the screenshot shows only 1X2 or handicap markets and no usable Asian total, wait for the total rather than inventing one.

---

## 15. Same-window comparison

When multiple FOCUS/WATCHLIST fixtures overlap in the same practical kickoff window, rerank them together after XI rather than promoting each in isolation.

Use corrected ICT kickoff from the time/schedule integrity procedure. Grade and structural quality remain ahead of market movement and price.

---

## 16. Live review

Live evidence validates or invalidates the frozen prematch thesis; it does not rewrite PRE history.

For inherited v0.2.47 logic, apply the documented halftime compression/saturation gate when relevant, especially after high-scoring first halves.

A manual live override must be separately labelled. Do not convert a missed prematch opportunity into a retroactive prematch lock based on the live score.

EGE does not bypass the no-chase rule after goal-driven market expansion.

---

## 17. Settlement

Unless the specific market says otherwise, full-match Asian totals settle on:

**90 minutes + stoppage time only.**

Extra time is excluded unless explicitly included by the market.

Record official results and P/L only for actually official selections under the model/version that produced them. HOLD, PASS, shadow, and counterfactual selections do not enter official P/L.

---

## 18. Authority

`CURRENT_MODEL.md` plus the current active rule files and `FOOTBALL_TIME_AND_SCHEDULE_INTEGRITY.md` are authoritative. This procedure intentionally contains no legacy fixture-union rule, no old competition whitelist, and no obsolete version routing.