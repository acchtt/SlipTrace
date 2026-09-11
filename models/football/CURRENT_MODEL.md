# Current Football Model

**Active official model:** Football **v0.2.51**  
**Official base:** Football **v0.2.47 CLEAN**  
**Active official patches:**  
- `rules/MODEL_RULES_FOOTBALL_V0.2.49.md` — **TWO-SIDED PRIORITY**  
- `rules/MODEL_RULES_FOOTBALL_V0.2.50.md` — **EXTREME GOAL ENVIRONMENT / PERSISTENT HIGH-LINE**  
- `rules/MODEL_RULES_FOOTBALL_V0.2.51.md` — **CHANCE-QUALITY + MARKET-CONFIRMATION CALIBRATION**  
**Shadow comparison tracks:** Football **v0.2.47 CLEAN** and Football **v0.2.48-SHADOW**  
**Fixture authority:** **AiScore only**  
**Operating workflow:** **Normal Chat AiScore fetch/filter → scope-pruned Work handoff → price/XI/market-history-blind Work structural sweep → frozen FOCUS/WATCHLIST board → Normal Chat first-pass XI → OPEN/PRE-XI/POST-XI market-history conflict check → final XI rerank → chance-quality hardening / burden regime → MCE test when eligible → user-supplied current executable odds → v0.2.51 verdict**  
**Canonical timezone:** `Asia/Ho_Chi_Minh` (ICT, UTC+7)

This file is the operating authority for Football. Historical rules are recoverable from Git history and must not be inferred into current decisions.

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
9. `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.48-SHADOW.md`
10. `models/football/procedures/FOOTBALL_BETTING_PROCEDURE.md`
11. `models/football/airtable/FOOTBALL_COVERAGE_AIRTABLE.md`
12. `models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md`

**Conditional auxiliary trial load:** when the user explicitly invokes UEFA Youth League / U19 trial work, additionally load `models/football/trials/UEFA_YOUTH_LEAGUE_TRIAL.md`. It is trial memory only and does not whitelist youth football for the normal senior board or create official v0.2.51 exposure.

Do not load superseded rule files from memory, old handoffs, or Git history into current decisions.

---

## 2. Fixture-source and scope directive

**AiScore is the sole fixture-discovery authority.** Other sources may research an AiScore-established fixture but may not add fixtures to the universe.

Normal Chat Step 0 owns fixture discovery, time normalization, cheap league/scope filtering, and the handoff. Work must **not** repeat the AiScore sweep when the handoff passes integrity checks.

The normal actionable board uses the current senior-quality overlay. Exclude youth/Uxx, academy, reserves/B/development, amateur/semi-pro, regional/state/provincial, unapproved lower divisions, weak obscure competitions, all Finnish domestic leagues, and the current low-goal hard/cheap-gate exclusions defined by the scope/league registry. Senior continental and domestic cup matches are not excluded merely because they are cups.

If the AiScore universe cannot be reconciled, state `COVERAGE INCOMPLETE — board provisional`.

---

## 3. Time and schedule integrity

Follow `FOOTBALL_TIME_AND_SCHEDULE_INTEGRITY.md`.

Canonical invariant:

`AISCORE IDENTITY → kickoff_utc → ONE conversion to Asia/Ho_Chi_Minh → kickoff_ict → slate_date_ict → status revalidation → schedule display`

Never add +7 twice. A `Z` timestamp is UTC. Near-term upcoming schedules must be revalidated against AiScore status.

---

## 4. Production sequence

`NORMAL CHAT AISCORE UNIVERSE → TIME/SCOPE FILTER → WORK STRUCTURAL SCREEN → FOCUS/WATCHLIST/PASS/UNRESOLVED → FREEZE PRE → NORMAL CHAT FIRST-PASS XI → MARKET-HISTORY CONFLICT CHECK → FINAL XI → CHANCE-QUALITY HARDENING → STANDARD/EGE BURDEN → MCE TEST WHEN ELIGIBLE → CURRENT PRICE → OFFICIAL VERDICT + SHADOWS`

Work is structural and price/XI/market-history blind. Normal Chat owns XI, opening-to-close odds watch, execution, and live review.

---

## 5. Official decision order

Official v0.2.51 order:

`STRUCTURAL QUALITY → CARRIER CEILING → FAILURE-MODE RESISTANCE → TEAM GF/GA PROFILE → CHANCE-QUALITY HARDENING → FIRST-PASS XI → MARKET-HISTORY CONFLICT CHECK → FINAL XI → GOAL BURDEN / REGIME → MCE TEST → CURRENT PRICE → LOCK / HOLD`

For comparable grades:

`TWO-SIDED > ELITE CARRIER > CARRIER-LED > FRAGILE / OTHER`

A genuine TWO-SIDED label requires independent credible scoring routes from both teams. An ELITE CARRIER can outrank only when clearly superior on self-funded ceiling and failure-mode resistance.

---

## 6. Structural bands

- **A1** — genuine Tier-A TWO-SIDED, or exceptional ELITE CARRIER.
- **A2** — strong two-sided environment, or strong carrier with one meaningful weakness.
- **B+** — good environment but materially dependent on contribution, rotation, game state, or another failure mode.
- **B / PASS** — fragile route, strong resistance, cohesion issue, weak chance quality, or excessive burden.

Grade and structure rank ahead of market and price.

---

## 7. Chance quality and v0.2.51 hardening

Before promotion, evaluate season/recent GF-GA, scoring/conceding 2+ frequency, suppression tendency, home/away splits and competition context. Where available use big chances, central/box access, SOT quality, xG/xGA/xGOT and comparable creation evidence.

For **STANDARD O3.0+** from A1/A2 TWO-SIDED, apply `MODEL_RULES_FOOTBALL_V0.2.51.md`: both routes together need repeatable high-value chance support or a strong data-poor substitute. Raw goals, names, possession, or generic attacking reputation are not enough by themselves. If evidence is weak, cap burden lower, downgrade confidence, or reclassify the archetype.

---

## 8. Frozen PRE and XI rerank

Frozen Work PRE remains history. Confirmed XI is the first legitimate rerank gate.

Classify rotation as:

- `ROTATION — ATTACKING DEPTH PRESERVED`; or
- `ROTATION — COHESION / ROUTE DAMAGE`.

Only the second is an automatic burden downgrade.

If both teams lose important creators/finishers, or the primary route plus opponent contribution are both materially weakened, apply `DUAL-ROUTE XI DAMAGE` under v0.2.51. A protected line alone cannot rescue that state.

---

## 9. Mandatory market-history conflict check

Normal Chat should attempt:

`OPEN → PRE-XI → POST-XI / CURRENT PREMATCH`

Prefer same-source/bookmaker history. Mixed sources are `CROSS-BOOK — CONTEXT ONLY`. If unavailable, record `MARKET HISTORY UNAVAILABLE` and continue.

Movement labels:

- `BULLISH LINE` — total +0.25 or more;
- `BEARISH LINE` — total -0.25 or more;
- `BULLISH PRICE` / `BEARISH PRICE` — meaningful same-line price movement;
- `STABLE`;
- `MIXED`.

First-pass XI must be football-led. Market history then challenges/corroborates it. A bullish line move against an apparent XI downgrade requires explicit reinspection before finalizing route damage.

Market history cannot rewrite frozen PRE, create TWO-SIDED, create EGE, or rescue PASS.

---

## 10. Goal-burden regimes

After final XI, classify:

- `STANDARD`; or
- `EGE — EXTREME GOAL ENVIRONMENT` under v0.2.50.

EGE is structural/team/XI driven, normally A1 FOCUS TWO-SIDED or ELITE CARRIER. A2 only via the strict v0.2.50 exception. A high market line cannot create EGE.

Persistent high-line acceptance and the no-chase rule remain active: a goal-driven expansion is never a reason to raise burden.

---

## 11. v0.2.51 Market-Confirmed Edge (MCE)

For eligible STANDARD A2/B+ TWO-SIDED cases, v0.2.51 permits the narrow tag:

`MCE +0.25 — MARKET-CONFIRMED EDGE`

Use only when all v0.2.51 conditions clear: preserved XI, credible 3-goal ceiling, same-source/normalized bullish +0.25 move, current line only +0.25 above frozen burden, price at least 1.75, and no dominant compression/suppression branch.

MCE does not create EGE or structural quality and cannot override DUAL-ROUTE XI DAMAGE.

---

## 12. B+ compression hardening

For B+ with an explicit derby/first-leg/1-0/1-1/control or weak-secondary-route failure mode, protection alone is not enough. Require an additional positive gate from XI improvement, strong market corroboration with intact football evidence, fresh chance-quality evidence, or clearly intact two-sided routes at a materially protected line.

---

## 13. User-supplied XI + current odds

The user normally supplies confirmed XI and current executable Asian-total odds. Do not substitute an external current price unless explicitly asked.

Historical odds research is the exception: Normal Chat may automatically retrieve opening/PRE-XI/post-XI context because it is calibration, not execution-price authority.

Do not issue an OFFICIAL LOCK without required current XI + executable price.

---

## 14. Executable price policy

- hard minimum decimal odds: **1.65**;
- preferred: **1.70+**;
- MCE +0.25 requires **1.75+**;
- below 1.65 → `NO BET — HOLD — PRICE TOO SHORT`;
- never stretch merely to improve price;
- burden is chosen before current price.

---

## 15. Official and shadow tracks

Use the same frozen evidence snapshot:

- **Official:** Football v0.2.51
- **Shadow:** Football v0.2.47 CLEAN
- **Shadow:** Football v0.2.48-SHADOW

v0.2.49/v0.2.50/v0.2.51 patches apply only to the official track. Shadows remain version-faithful and never enter official P/L.

---

## 16. Live and audit boundary

Live evidence validates or invalidates frozen PRE; it does not rewrite it. Keep v0.2.50 no-chase and HT compression/remaining-goal-budget logic.

Audit high-scoring one-team results carefully:

- both routes contribute → `CLEAN TWO-SIDED VALIDATION`;
- one carrier supplies the total → `CARRIER VALIDATION — NOT CLEAN TWO-SIDED`;
- expected chance quality never appears → `CHANCE-QUALITY MISS`;
- chances appear but goals do not → `CONVERSION VARIANCE`;
- named control branch dominates → `COMPRESSION FAILURE`.

A temporarily active failure mode is not automatically a model invalidation if the protected prematch line, carrier route and second-half escalation capacity remain intact.

Standard full-match Asian totals settle on 90 minutes + stoppage unless stated otherwise. Counterfactual HOLD/PASS/shadow outcomes never enter official P/L.

---

## 17. Authority and history

For current decisions, this file and the canonical load order win over stale chat text, old handoffs, archived screenshots and superseded documentation. v0.2.51 is prospective from 2026-09-11 ICT; historical decisions remain settled under the model/version that produced them.
