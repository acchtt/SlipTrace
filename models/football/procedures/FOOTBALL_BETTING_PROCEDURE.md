# Football Betting Procedure

**Status:** ACTIVE  
**Official model:** Football v0.2.49  
**Base:** v0.2.47 CLEAN  
**Shadow comparisons:** v0.2.47 CLEAN and v0.2.48-SHADOW  
**Fixture authority:** AiScore only

This is the current execution procedure from frozen PRE through official LOCK/HOLD/PASS. Detailed structural rules remain in the active rule files; this procedure defines ordering and operating boundaries.

---

## 1. Preconditions

Do not issue an official prematch verdict unless:

1. the requested AiScore fixture window passed coverage reconciliation;
2. the fixture is actionable under the current senior-quality overlay;
3. the fixture has a frozen Work PRE state or a clearly documented equivalent current PRE state;
4. the required current confirmed XI and executable Asian-total price are available from the user, unless the user explicitly requested external verification.

If XI or price is missing under the normal workflow:

`WAITING FOR USER XI/ODDS — NO OFFICIAL DECISION`

Do not reconstruct a new structural PRE merely because later evidence is available.

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

Official v0.2.49 order:

`STRUCTURAL QUALITY → CARRIER CEILING → FAILURE-MODE RESISTANCE → TEAM GF/GA PROFILE → CHANCE QUALITY → XI RERANK → GOAL BURDEN → PRICE → LOCK / HOLD`

For comparable grades:

`TWO-SIDED > ELITE CARRIER > CARRIER-LED > FRAGILE / OTHER`

A genuine TWO-SIDED profile requires credible independent scoring routes from both teams.

An ELITE CARRIER may outrank a genuine same-grade TWO-SIDED candidate only when clearly superior on both repeatable chance quality/self-funding 3+ capacity and failure-mode resistance.

Price cannot create structure.

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

XI can downgrade or rerank a thesis. Do not over-promote solely because recognizable attackers start.

---

## 5. Team-profile and chance-quality check

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

## 6. Failure-mode check

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

## 7. Goal-burden selection

Choose the Asian-total burden **after structure and XI, before price**.

Prefer the lowest protected line that faithfully expresses the frozen thesis and remains inside the model-supported burden/range.

Do not move from O2.5 to O2.75, O3.0, O3.25, etc. merely to obtain a better price.

A higher total is permitted only when the structural/XI evidence independently supports the extra goal burden.

Settlement examples for standard Asian totals:

- O2.5: 3+ goals win;
- O2.75: exactly 3 = half win / half push; 4+ = full win;
- O3.0: exactly 3 = push; 4+ = win;
- O3.25: exactly 3 = half loss / half push; 4+ = win.

---

## 8. Executable price policy

Current user overlay:

- hard minimum decimal odds: **1.65**;
- preferred decimal odds: **1.70+**;
- below 1.65 → `NO BET — HOLD — PRICE TOO SHORT`;
- never stretch the line just to clear 1.65/1.70;
- structural ranking is price-independent.

Price is evaluated only after the correct model-supported line is chosen.

---

## 9. Official verdict semantics

### OFFICIAL LOCK

Issue only when all required gates clear:

- actionable competition;
- valid frozen FOCUS/WATCHLIST structural thesis;
- XI does not invalidate the thesis;
- main failure mode is acceptable for the proposed burden;
- selected Asian total is model-supported;
- price meets the current executable policy.

An affirmative official v0.2.49 final selection is an **OFFICIAL LOCK**.

### HOLD

Use when the thesis remains live but one or more final gates do not clear: unresolved contribution, XI sensitivity, failure-mode risk, goal burden, short price, or missing current input.

### PASS

Use when the structural route is no longer sufficient or new evidence materially invalidates it.

HOLD/PASS creates no official exposure.

---

## 10. Shadow tracks

When a material final comparison is required, run the same frozen evidence state through:

- official v0.2.49;
- shadow v0.2.47 CLEAN;
- shadow v0.2.48-SHADOW.

Keep each version faithful to its own rules. Do not import the v0.2.49 Two-Sided Priority patch into the shadow tracks.

Shadow decisions never suppress an official v0.2.49 decision and never enter official P/L.

---

## 11. User-supplied screenshot workflow

When the user sends XI/odds screenshots or text:

1. identify the fixture;
2. retrieve the frozen PRE state from the current Work/Airtable bridge;
3. read the supplied XI;
4. read the supplied Asian-total lines/prices;
5. rerank from frozen PRE using the current official order;
6. choose the correct burden before comparing prices;
7. apply the 1.65 hard floor / 1.70+ preference;
8. issue LOCK/HOLD/PASS.

Do not automatically search missing XI/price unless the user explicitly asks for external verification.

If the screenshot shows only 1X2 or handicap markets and no usable Asian total, wait for the total rather than inventing one.

---

## 12. Same-window comparison

When multiple FOCUS/WATCHLIST fixtures overlap in the same practical kickoff window, rerank them together after XI rather than promoting each in isolation.

Grade and structural quality remain ahead of price. For comparable grades, apply the official v0.2.49 archetype priority before price selection.

---

## 13. Live review

Live evidence validates or invalidates the frozen prematch thesis; it does not rewrite PRE history.

For inherited v0.2.47 logic, apply the documented halftime compression/saturation gate when relevant, especially after high-scoring first halves.

A manual live override must be separately labelled. Do not convert a missed prematch opportunity into a retroactive prematch lock based on the live score.

---

## 14. Settlement

Unless the specific market says otherwise, full-match Asian totals settle on:

**90 minutes + stoppage time only.**

Extra time is excluded unless explicitly included by the market.

Record official results and P/L only for actually official selections under the model/version that produced them. HOLD, PASS, shadow, and counterfactual selections do not enter official P/L.

---

## 15. Authority

`CURRENT_MODEL.md` plus the current active rule files are authoritative. This procedure intentionally contains no legacy fixture-union rule, no old competition whitelist, and no obsolete “v0.2.47 is official” routing.
