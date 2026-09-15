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
- `rules/MODEL_RULES_FOOTBALL_A.md` — **EXECUTION SELECTION CORRECTION / EXPOSURE GATE**  
**Shadow comparison tracks:** Football **v0.2.47 CLEAN** and Football **v0.2.48-SHADOW**  
**Fixture authority:** **AiScore only**  
**Operational display timezone:** `Asia/Ho_Chi_Minh` (ICT, UTC+7)  
**Step-0 time policy:** preserve AiScore source local time + timezone/offset; convert to ICT later when scheduling.

This file is the operating authority for Football. **Football A is the main active model.** Historical assessments remain tied to the model version that actually produced them.

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
14. `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.48-SHADOW.md`
15. `models/football/procedures/FOOTBALL_BETTING_PROCEDURE.md`
16. `models/football/airtable/FOOTBALL_COVERAGE_AIRTABLE.md`
17. `models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md`

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

`NORMAL CHAT AISCORE ACTIONABLE SENIOR UNIVERSE → UNIQUE IDENTITY + SCOPE / LEAGUE GATE → ACTIONABLE COMPLETENESS → WORK ROUTE PROOF + STRUCTURAL SCREEN → NON-COMPENSATORY PRE CAPS → SAME-WINDOW STRUCTURAL RANK → FOCUS/WATCHLIST/PASS/UNRESOLVED → FREEZE PRE → NORMAL CHAT XI → MARKET-HISTORY CONFLICT CHECK → FINAL XI / CARRIER REOPEN → CHANCE QUALITY + REGIME/BURDEN → CURRENT USER-SUPPLIED PRICE → EXECUTION CLASS → MODEL A EXPOSURE GATE → OFFICIAL LOCK / EXPOSURE HOLD / QUALIFIED WAIT / STRUCTURAL HOLD / SHADOW`

Work remains structural and price/XI/market-history blind. Normal Chat owns XI, market-history checks, current price, exposure selection, schedule display, and live review.

---

## 4. Structural model remains v0.2.55-compatible

Football A does **not** change the structural board.

Continue the active standards:

- **A1:** maximum for `PROVEN + PROVEN`; data-poor substitutes are never A1.
- **A2:** normal maximum for `PROVEN + SUPPORTED`; `SUPPORTED + SUPPORTED` reaches A2/FOCUS only with strong chance quality and failure resistance.
- **B+:** normal ceiling for `SUPPORTED + NOMINAL`; `PROVEN + NOMINAL` is WATCHLIST unless the proven route is true CC+.
- **B / PASS:** weak/failed route combinations, strong resistance, cohesion damage, weak chance quality, or unsupported burden.

Two-Sided Tier A remains the primary lane. For comparable non-Tier-A cases:

`QUALITY-PROVEN TWO-SIDED > CC+ ELITE CARRIER > NOMINAL / WEAK-SECONDARY TWO-SIDED > ordinary CARRIER-LED > FRAGILE / OTHER`

Supported burden is chosen before current price. Price cannot create structural quality.

---

## 5. Current official decision order

Football A order:

`SCOPE / LEAGUE REGIME → HOME + AWAY ROUTE STATES → DOMINANT FAILURE MODE → CHANCE QUALITY → CC+ / CARRIER CEILING → BURDEN FIT → EVIDENCE CONFIDENCE → FIRST-PASS XI → MARKET-HISTORY CONFLICT CHECK → FINAL XI / CARRIER REOPEN → STANDARD/EGE → MCE SHADOW TEST IF ELIGIBLE → CURRENT PRICE → STRUCTURAL RANK + EXECUTION CLASS → MODEL A UPPER-TAIL GATE → MODEL A PRIORITY-INVERSION GUARD → EXPOSURE DECISION`

Three outputs are mandatory:

1. **Structural Rank**
2. **Execution Class**
3. **Exposure Decision**

Execution Class remains:

- `DIRECT LOCK ELIGIBLE`
- `QUALIFIED — WAIT FOR DECAY`
- `STRUCTURAL HOLD`
- `SHADOW ONLY`

Under Football A:

`DIRECT LOCK ELIGIBLE != AUTOMATIC OFFICIAL LOCK`

A DIRECT candidate can remain technically executable while receiving:

`NO BET — EXPOSURE HOLD`

because of the Model A exposure gate.

---

## 6. Model A exposure gate

### A2 upper-tail gate

When an A2 candidate is executable at the **supported-burden ceiling**, official exposure requires a genuine upper-tail pass through at least one of:

- `4+ TOTAL PATH — QUALITY PROVEN`;
- `TRUE CC+ PATH` with credible additional-goal support;
- `ELITE TWO-SIDED PATH` with strong chance quality and failure resistance.

If none clears, preserve `DIRECT LOCK ELIGIBLE` but final action becomes:

`NO BET — EXPOSURE HOLD — UPPER-TAIL INSUFFICIENT`

A1 remains the strongest primary lane and normally clears this exposure requirement when PROVEN+PROVEN, clean XI, chance quality, failure mode, and burden rules remain intact.

B+ is **not relaxed** by Football A.

### Priority-inversion guard

Before any official exposure, compare the candidate with higher-ranked active candidates in the same practical kickoff/exposure window.

If a higher-ranked clean-XI A1/A2 FOCUS is still structurally qualified and is withheld **only** because its offered line is above burden or its target price is below floor, a materially weaker lower-ranked DIRECT candidate must not become official merely because its lower line is easier to execute.

A lower-ranked exposure requires a documented football-led override: materially stronger upper-tail proof, materially stronger route quality after XI, a genuine failure-mode downgrade to the higher-ranked match, or another active-model football change.

Price, nominally lower total, or simple availability is not a valid override.

If blocked:

- keep `Execution Class = DIRECT LOCK ELIGIBLE`;
- set `Exposure Decision = NO BET — EXPOSURE HOLD`;
- persist `PRIORITY INVERSION GUARD`.

Official exposure priority is:

`STRUCTURAL RANK → UPPER-TAIL PROOF → ROUTE QUALITY / FAILURE RESISTANCE → BURDEN PROTECTION → PRICE AS TIE-BREAKER`

---

## 7. Qualified waits and structural holds

Use `QUALIFIED — WAIT FOR DECAY` when football/XI/evidence gates clear at a supported burden and the only blocker is line or price.

Required blocker labels remain:

- `PRICE-ONLY WAIT — LINE ABOVE BURDEN`
- `PRICE-ONLY WAIT — PRICE BELOW FLOOR`
- `PRICE-ONLY WAIT — BOTH`

Keep these candidates visible at their structural rank and continue market-path logging.

Use `STRUCTURAL HOLD` only when football structure fails or remains materially unresolved. Do not collapse price-only waits into structural holds.

---

## 8. Price and user-supplied execution authority

The user normally supplies confirmed XI and current executable Asian-total odds. Do not substitute externally found current prices unless explicitly asked.

Historical odds research is permitted for calibration/context.

Active prematch price policy remains:

- hard minimum decimal odds: **1.65**;
- preferred: **1.70+**;
- MCE +0.25 shadow validator threshold: **1.75+**;
- never stretch burden merely to improve price.

Do not issue an official lock without required current XI, executable price, and Model A exposure approval.

---

## 9. Quarantined mechanisms remain quarantined

Football A does not reactivate quarantined promotion mechanisms.

Continue:

- `HIGH-SCORING +0.25 ACCEPTANCE BAND — SHADOW ONLY` for qualifying A1/A2 FOCUS observations;
- `SHADOW MCE +0.25 — NO OFFICIAL EXPOSURE`;
- `SHADOW LIVE/DECAY — NO OFFICIAL EXPOSURE`.

The +0.25 acceptance band remains quarantined until the full v0.2.55 release gate clears, including at least 20 valid settled predeclared observations, positive quarter-line-aware ROI, diversified sample, two consecutive release audits, and explicit user approval of a later model version.

B+ / CC+ remains a separate audit lane with no automatic promotion.

---

## 10. Persistence under Football A

For every material final review, persist:

- `Model Version = Football A`;
- Structural Rank;
- Execution Class;
- supported burden;
- current line/price;
- upper-tail state: `PASS / FAIL / NOT REQUIRED`;
- priority-inversion state: `CLEAR / BLOCKED / FOOTBALL OVERRIDE`;
- Exposure Decision;
- exact reason for any DIRECT-eligible exposure hold.

Without a schema migration, keep technical DIRECT eligibility in the existing Execution Class field. Use `NO BET — HOLD` as the Airtable verdict for `NO BET — EXPOSURE HOLD`, with the Model A blocker written in Candidate/Evidence Summary.

Create Website Picks only for actual `OFFICIAL LOCK` exposure.

---

## 11. Audit separation

Post-slate audit must report separately:

- official Football A locks and P/L;
- DIRECT candidates suppressed by the upper-tail gate;
- DIRECT candidates suppressed by the priority-inversion guard;
- QUALIFIED — WAIT target-burden outcomes;
- STRUCTURAL HOLD outcomes;
- +0.25 acceptance-band shadows;
- B+ / CC+ audit lane;
- MCE shadows;
- live/decay shadows;
- FOCUS vs WATCHLIST 3+ and 4+ performance.

Counterfactual/shadow outcomes never enter official P/L.

---

## 12. Authority and history

Football A is prospective from **2026-09-15 11:01 ICT** onward. It does not retroactively reclassify earlier locks, waits, holds, shadows, or P/L.

Historical order:

- v0.2.53 remains historical for decisions it actually produced;
- v0.2.54 remains historical for its activation period;
- v0.2.55 remains historical for decisions from 2026-09-14 ICT until Football A activation;
- **Football A is the active official model for new decisions after activation.**

For current decisions, this file plus the canonical active stack wins over stale chat text, old handoffs, archived screenshots, and superseded documentation.
