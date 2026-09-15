# Current Football Model

**Active official model:** Football **A**  
**Official base:** Football **v0.2.47 CLEAN**  
**Immediate parent:** Football **v0.2.55**  
**Active official patches:**  
- `rules/MODEL_RULES_FOOTBALL_V0.2.49.md` — **TWO-SIDED PRIORITY**  
- `rules/MODEL_RULES_FOOTBALL_V0.2.50.md` — **EXTREME GOAL ENVIRONMENT / PERSISTENT HIGH-LINE**  
- `rules/MODEL_RULES_FOOTBALL_V0.2.51.md` — **CHANCE-QUALITY + MARKET-CONFIRMATION CALIBRATION**  
- `rules/MODEL_RULES_FOOTBALL_V0.2.52.md` — **CARRIER CEILING + B+ EVIDENCE HARDENING**  
- `rules/MODEL_RULES_FOOTBALL_V0.2.53.md` — **RANKING INTEGRITY + EXECUTION VALIDATION**  
- `rules/MODEL_RULES_FOOTBALL_V0.2.54.md` — **SELECTION INVERSION GUARD + PROMOTION QUARANTINE**  
- `rules/MODEL_RULES_FOOTBALL_V0.2.55.md` — **EXECUTION CALIBRATION ADDENDUM**  
- `rules/MODEL_RULES_FOOTBALL_A.md` — **EXECUTION SELECTION CORRECTION / EXPOSURE GATE + FRAGILE SUPPORTED-ROUTE A2 FOCUS GUARD**  
- `rules/MODEL_RULES_FOOTBALL_A_LIVE_DECAY.md` — **PREDECLARED LIVE-DECAY EXECUTION / NO PLANNED PREMATCH LINE-DECAY WAIT**  
**Shadow comparison tracks:** Football **v0.2.47 CLEAN** and Football **v0.2.48-SHADOW**  
**Fixture authority:** **AiScore only**  
**Operational display timezone:** `Asia/Ho_Chi_Minh` (ICT, UTC+7)  
**Step-0 time policy:** preserve AiScore source local time + timezone/offset; convert to ICT later when scheduling.

This file is the operating authority for Football. **Football A is the main active model.** Historical assessments remain tied to the model version/state that actually produced them.

---

## 1. Canonical load order

Load only the current active stack:

1. `models/football/CURRENT_MODEL.md`
2. `models/football/procedures/FOOTBALL_TIME_AND_SCHEDULE_INTEGRITY.md`
3. `models/football/procedures/FOOTBALL_MATCH_SWEEP_AND_RESEARCH_PROCEDURE.md`
4. `models/football/procedures/FOOTBALL_COVERAGE_CONTROLLER.md`
5. `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.47.md`
6. `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.49.md`
7. `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.50.md`
8. `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.51.md`
9. `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.52.md`
10. `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.53.md`
11. `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.54.md`
12. `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.55.md`
13. `models/football/rules/MODEL_RULES_FOOTBALL_A.md`
14. `models/football/rules/MODEL_RULES_FOOTBALL_A_LIVE_DECAY.md`
15. `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.48-SHADOW.md`
16. `models/football/procedures/FOOTBALL_BETTING_PROCEDURE.md`
17. `models/football/airtable/FOOTBALL_COVERAGE_AIRTABLE.md`
18. `models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md`

Conditional auxiliary trials remain opt-in only and do not change the normal senior board.

Do not load superseded rules from memory, old handoffs, or Git history into current decisions.

---

## 2. Fixture, scope, and time authority

**AiScore is the sole fixture-discovery authority.** Other sources may research an AiScore-established fixture but may not add fixtures to the actionable universe.

Normal Chat Step 0 owns fixture discovery, source-time capture, cheap league/scope filtering, and handoff creation. Work must not repeat the fixture sweep after the actionable-completeness gate passes.

The normal actionable board excludes youth/Uxx, academy, reserves/B/development, amateur/semi-pro, regional/state/provincial, unapproved lower divisions, weak obscure competitions, all Finnish domestic leagues, Japanese domestic leagues under the current hard exclusion, and current low-goal hard/cheap-gate exclusions. Senior continental and domestic cup matches are not generically excluded.

Canonical time invariant:

`AISCORE IDENTITY → PRESERVE SOURCE LOCAL TIME + TIMEZONE/OFFSET → ACTIONABLE FILTER / WORK HANDOFF → ONE-TIME ICT CONVERSION WHEN SCHEDULING → slate_date_ict → status revalidation`

A `Z` timestamp means UTC. Never convert the same timestamp twice.

---

## 3. Production sequence

`NORMAL CHAT AISCORE ACTIONABLE SENIOR UNIVERSE → UNIQUE IDENTITY + SCOPE / LEAGUE GATE → ACTIONABLE COMPLETENESS → WORK ROUTE PROOF + STRUCTURAL SCREEN → NON-COMPENSATORY PRE CAPS → SAME-WINDOW STRUCTURAL RANK → FOCUS/WATCHLIST/PASS/UNRESOLVED → FREEZE PRE → NORMAL CHAT XI → MARKET-HISTORY CONFLICT CHECK → FINAL XI / CARRIER REOPEN → CHANCE QUALITY + REGIME/BURDEN → CURRENT USER-SUPPLIED PRICE → EXECUTION PATH → MODEL A EXPOSURE GATE → OFFICIAL LOCK / EXPOSURE HOLD / QUALIFIED LIVE-DECAY PLAN / STRUCTURAL HOLD / SHADOW`

Work remains structural and price/XI/market-history blind. Normal Chat owns XI, market-history checks, current price, exposure selection, planned live-decay execution, schedule display, and live review.

---

## 4. Structural model

Football A remains v0.2.55-compatible with one narrow FOCUS cap.

- **A1:** maximum for `PROVEN + PROVEN`; data-poor substitutes are never A1.
- **A2:** normal maximum for `PROVEN + SUPPORTED`; `SUPPORTED + SUPPORTED` reaches A2/FOCUS only with strong chance quality and failure resistance.
- **B+:** normal ceiling for `SUPPORTED + NOMINAL`; `PROVEN + NOMINAL` is WATCHLIST unless the proven route is true CC+.
- **B / PASS:** weak/failed route combinations, strong resistance, cohesion damage, weak chance quality, or unsupported burden.

### Fragile SUPPORTED-route FOCUS guard

For `PROVEN + SUPPORTED`, A2 may remain valid, but **A2 FOCUS is not allowed** when the SUPPORTED route is materially dependent on score/form-proxy evidence, away/venue-sensitive contribution, meaningful XI sensitivity, or defensive-leakage inference unless at least one hardener clears:

- `SUPPORTED-ROUTE CHANCE QUALITY — STRONG`; or
- `TRUE CC+` on the PROVEN side with a genuine independent 3+ team-goal ceiling that survives weak opponent contribution.

If neither clears, cap at `A2 WATCHLIST` and persist `A2 FOCUS CAP — FRAGILE SUPPORTED ROUTE`.

Recent Over/BTTS frequency by itself cannot clear the cap.

Two-Sided Tier A remains the primary lane. For comparable non-Tier-A cases:

`QUALITY-PROVEN TWO-SIDED > CC+ ELITE CARRIER > NOMINAL / WEAK-SECONDARY TWO-SIDED > ordinary CARRIER-LED > FRAGILE / OTHER`

Supported burden is chosen before current price. Price cannot create structural quality.

---

## 5. Current decision order

Football A order:

`SCOPE / LEAGUE REGIME → HOME + AWAY ROUTE STATES → DOMINANT FAILURE MODE → CHANCE QUALITY → CC+ / CARRIER CEILING → BURDEN FIT → EVIDENCE CONFIDENCE → FIRST-PASS XI → MARKET-HISTORY CONFLICT CHECK → FINAL XI / CARRIER REOPEN → STANDARD/EGE → MCE SHADOW TEST IF ELIGIBLE → CURRENT PRICE → STRUCTURAL RANK + EXECUTION PATH → MODEL A UPPER-TAIL GATE → MODEL A PRIORITY-INVERSION GUARD → EXPOSURE DECISION`

Three outputs remain mandatory:

1. **Structural Rank**
2. **Execution Class / Plan**
3. **Exposure Decision**

Execution states now include:

- `DIRECT LOCK ELIGIBLE`
- `QUALIFIED — LIVE DECAY PLAN`
- `QUALIFIED — PRICE BELOW FLOOR`
- `STRUCTURAL HOLD`
- `SHADOW ONLY`

`DIRECT LOCK ELIGIBLE != AUTOMATIC OFFICIAL LOCK`

---

## 6. Football A exposure gate

### A2 upper-tail gate

When an A2 candidate is executable at the top of its supported burden/range, official exposure requires at least one of:

- `4+ TOTAL PATH — QUALITY PROVEN`;
- `TRUE CC+ PATH` with credible additional-goal support;
- `ELITE TWO-SIDED PATH` with strong chance quality and failure resistance.

If none clears:

`DIRECT LOCK ELIGIBLE — NO BET — EXPOSURE HOLD — UPPER-TAIL INSUFFICIENT`

A1 remains the strongest primary lane. B+ receives no relaxation.

### Priority-inversion guard

Before any official exposure, compare against higher-ranked active candidates in the same practical exposure window.

A materially weaker lower-ranked DIRECT candidate must not become official merely because its lower total is easier to execute when a higher-ranked clean-XI A1/A2 FOCUS remains structurally qualified and is withheld only by line/price.

A lower-ranked override requires a documented football-led reason.

Official exposure priority remains:

`STRUCTURAL RANK → UPPER-TAIL PROOF → ROUTE QUALITY / FAILURE RESISTANCE → BURDEN PROTECTION → PRICE AS TIE-BREAKER`

---

## 7. Live-decay execution policy

Football A no longer plans around a prematch quarter-line drop.

### 7.1 No planned prematch line-decay wait

If the prematch market is above supported burden, do **not** treat a lower line as something expected to appear before kickoff.

Instead use:

`QUALIFIED — LIVE DECAY PLAN`

Prematch movement can still be accepted if the user supplies it, but the model must never require or expect it as the normal execution route.

### 7.2 Predeclared live decay can become official

A predeclared `QUALIFIED — LIVE DECAY PLAN` may become official after kickoff when:

- the plan was frozen before kickoff;
- the user supplies a current executable live line/price;
- the live line is at or below the supported target burden;
- price clears the hard floor;
- the original football/XI thesis remains substantially intact;
- score/time state has not created a materially different thesis;
- no red card, major injury, tactical collapse, or route damage invalidates the plan;
- Model A upper-tail and priority-inversion gates are re-run at the actual live burden.

If all clear:

`DIRECT LOCK ELIGIBLE — PREDECLARED LIVE DECAY`

and, after exposure approval:

`OFFICIAL LOCK — LIVE DECAY PLAN`

A first goal does not automatically cancel the plan; it triggers a state-integrity recheck.

### 7.3 Opportunistic live remains quarantined

If no live-decay plan was frozen before kickoff, an attractive live Over remains:

`SHADOW LIVE/DECAY — NO OFFICIAL EXPOSURE`

unless the user grants a match-specific exception.

`PREDECLARED LIVE DECAY != OPPORTUNISTIC LIVE BET`

### 7.4 Same-line price wait

If the line is already at supported burden but price is below the hard floor, use:

`QUALIFIED — PRICE BELOW FLOOR`

This can become directly executable before kickoff if the same supported line later clears the floor.

---

## 8. Price and user-supplied execution authority

The user normally supplies confirmed XI and current executable Asian-total odds. Do not replace those current prices with external prices unless explicitly asked.

Active price policy:

- hard minimum decimal odds: **1.65**;
- preferred: **1.70+**;
- MCE +0.25 shadow validator threshold: **1.75+**;
- never stretch burden merely to improve price.

---

## 9. Quarantined mechanisms

Continue:

- `HIGH-SCORING +0.25 ACCEPTANCE BAND — SHADOW ONLY`;
- `SHADOW MCE +0.25 — NO OFFICIAL EXPOSURE`;
- opportunistic/non-predeclared `SHADOW LIVE/DECAY — NO OFFICIAL EXPOSURE`.

The +0.25 acceptance band remains quarantined until its existing release gate clears. B+ / CC+ remains a separate audit lane with no automatic promotion.

---

## 10. Persistence

For every material Football A review, persist:

- `Model Version = Football A`;
- Structural Rank;
- supported burden;
- prematch/current line and price;
- Execution Class / Plan;
- upper-tail state;
- priority-inversion state;
- Exposure Decision;
- exact blocker/reason.

For `QUALIFIED — LIVE DECAY PLAN`, also persist:

- target line and minimum price;
- prematch offered line/price;
- cancellation triggers;
- first target-line timestamp, score and minute;
- actual target price;
- state integrity: `CLEAR / DAMAGED / NEW THESIS`;
- final live exposure decision.

Create Website Picks only when an actual `OFFICIAL LOCK` is approved at that moment. Never create retroactive exposure.

---

## 11. Audit separation

Post-slate audit must report separately:

- official Football A prematch locks and P/L;
- official predeclared live-decay locks and P/L;
- predeclared live-decay plans that never reached target;
- target reached but state damaged/new thesis;
- target reached but exposure suppressed by Model A;
- opportunistic live shadows;
- DIRECT candidates suppressed by upper-tail/priority-inversion gates;
- `A2 FOCUS CAP — FRAGILE SUPPORTED ROUTE` cases;
- structural holds;
- +0.25 acceptance-band shadows;
- B+ / CC+ audit lane;
- MCE shadows;
- FOCUS vs WATCHLIST 3+ and 4+ performance.

Counterfactual/shadow outcomes never enter official P/L.

---

## 12. Authority and history

Football A is the active official model. The fragile A2 FOCUS guard and the predeclared live-decay patch are prospective from their activation commits and do not retroactively reclassify earlier decisions or P/L.

For current decisions, this file plus the canonical active stack wins over stale chat text, old handoffs, archived screenshots, and superseded documentation.
