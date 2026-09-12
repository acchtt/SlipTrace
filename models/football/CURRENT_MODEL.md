# Current Football Model

**Active official model:** Football **v0.2.52**  
**Official base:** Football **v0.2.47 CLEAN**  
**Active official patches:**  
- `rules/MODEL_RULES_FOOTBALL_V0.2.49.md` — **TWO-SIDED PRIORITY**  
- `rules/MODEL_RULES_FOOTBALL_V0.2.50.md` — **EXTREME GOAL ENVIRONMENT / PERSISTENT HIGH-LINE**  
- `rules/MODEL_RULES_FOOTBALL_V0.2.51.md` — **CHANCE-QUALITY + MARKET-CONFIRMATION CALIBRATION**  
- `rules/MODEL_RULES_FOOTBALL_V0.2.52.md` — **CARRIER CEILING + B+ EVIDENCE HARDENING**  
**Shadow comparison tracks:** Football **v0.2.47 CLEAN** and Football **v0.2.48-SHADOW**  
**Fixture authority:** **AiScore only**  
**Operating workflow:** **Normal Chat AiScore actionable-senior fetch/filter → scope-pruned Work handoff → price/XI/market-history-blind Work structural sweep → frozen FOCUS/WATCHLIST board with route-quality + CC+ audit → Normal Chat first-pass XI → OPEN/PRE-XI/POST-XI market-history conflict check → final XI rerank / carrier reopen test → chance-quality hardening / burden regime → MCE test when eligible → user-supplied current executable odds → v0.2.52 verdict**  
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
9. `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.52.md`
10. `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.48-SHADOW.md`
11. `models/football/procedures/FOOTBALL_BETTING_PROCEDURE.md`
12. `models/football/airtable/FOOTBALL_COVERAGE_AIRTABLE.md`
13. `models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md`

**Conditional auxiliary trial load:** when the user explicitly invokes UEFA Youth League / U19 trial work, additionally load `models/football/trials/UEFA_YOUTH_LEAGUE_TRIAL.md`. It is trial memory only and does not whitelist youth football for the normal senior board or create official v0.2.52 exposure.

Do not load superseded rule files from memory, old handoffs, or Git history into current decisions.

---

## 2. Fixture-source and scope directive

**AiScore is the sole fixture-discovery authority.** Other sources may research an AiScore-established fixture but may not add fixtures to the universe.

Normal Chat Step 0 owns fixture discovery, time normalization, cheap league/scope filtering, and the handoff. Work must **not** repeat the AiScore sweep when the handoff passes the actionable-completeness gate.

The normal actionable board uses the current senior-quality overlay. Exclude youth/Uxx, academy, reserves/B/development, amateur/semi-pro, regional/state/provincial, unapproved lower divisions, weak obscure competitions, all Finnish domestic leagues, and the current low-goal hard/cheap-gate exclusions defined by the scope/league registry. Senior continental and domestic cup matches are not excluded merely because they are cups.

### Actionable completeness vs raw audit completeness

For production, `complete=true` means **actionable senior completeness** for the requested ICT window. Step 0 must prove that every potentially actionable senior league/cup/continental block in scope was checked, the terminal requested interval was checked, and every admitted fixture is accounted for.

Exact one-by-one enumeration of already-excluded youth/reserve/lower/amateur/regional/hard-excluded fixtures is a separate audit dimension. If AiScore exposes those only through fragmented dynamic snapshots, Step 0 may set:

- `raw_audit_complete=false`;
- `raw_count_mode=lower_bound`;
- explicit `nonblocking_raw_gaps`.

Those raw gaps do not block Work when they are confined to categories already excluded from the actionable model scope.

If the **actionable senior universe** cannot be reconciled, state `COVERAGE INCOMPLETE — ACTIONABLE SENIOR GAP` and do not send the handoff to Work.

---

## 3. Time and schedule integrity

Follow `FOOTBALL_TIME_AND_SCHEDULE_INTEGRITY.md`.

Canonical invariant:

`AISCORE IDENTITY → kickoff_utc → ONE conversion to Asia/Ho_Chi_Minh → kickoff_ict → slate_date_ict → status revalidation → schedule display`

Never add +7 twice. A `Z` timestamp is UTC. Near-term upcoming schedules must be revalidated against AiScore status.

---

## 4. Production sequence

`NORMAL CHAT AISCORE ACTIONABLE SENIOR UNIVERSE → TIME/SCOPE FILTER → ACTIONABLE_COMPLETENESS / WORK_READY GATE → WORK STRUCTURAL SCREEN → ROUTE-QUALITY + CC+ AUDIT → FOCUS/WATCHLIST/PASS/UNRESOLVED → FREEZE PRE → NORMAL CHAT FIRST-PASS XI → MARKET-HISTORY CONFLICT CHECK → FINAL XI / CARRIER REOPEN TEST → CHANCE-QUALITY HARDENING → STANDARD/EGE BURDEN → MCE TEST WHEN ELIGIBLE → CURRENT PRICE → OFFICIAL VERDICT + SHADOWS`

Work is structural and price/XI/market-history blind. Normal Chat owns XI, opening-to-close odds watch, execution, and live review. Work must not repair non-blocking raw-audit gaps.

---

## 5. Official decision order

Official v0.2.52 order:

`STRUCTURAL QUALITY → ROUTE QUALITY PROOF → CARRIER CEILING / CC+ → FAILURE-MODE RESISTANCE → TEAM GF/GA PROFILE → CHANCE-QUALITY HARDENING → FIRST-PASS XI → MARKET-HISTORY CONFLICT CHECK → FINAL XI / CARRIER REOPEN → GOAL BURDEN / REGIME → MCE TEST → CURRENT PRICE → LOCK / HOLD`

Two-Sided Tier A remains the primary lane. For comparable non-Tier-A cases use:

`QUALITY-PROVEN TWO-SIDED > CC+ ELITE CARRIER > NOMINAL / WEAK-SECONDARY TWO-SIDED > ordinary CARRIER-LED > FRAGILE / OTHER`

A genuine TWO-SIDED label requires independent credible scoring routes from both teams. Mere lineup preservation does not prove route quality.

---

## 6. Structural bands

- **A1** — genuine Tier-A quality-proven TWO-SIDED, or exceptional ELITE CARRIER.
- **A2** — strong two-sided environment, or strong carrier with one meaningful weakness.
- **B+** — good environment but materially dependent on contribution, rotation, game state, or another failure mode.
- **B / PASS** — fragile route, strong resistance, cohesion issue, weak chance quality, or excessive burden.

Grade and structure rank ahead of market and price.

---

## 7. Chance quality and route-quality hardening

Before promotion, evaluate season/recent GF-GA, scoring/conceding 2+ frequency, suppression tendency, home/away splits and competition context. Where available use big chances, central/box access, SOT quality, xG/xGA/xGOT and comparable creation evidence.

For **STANDARD O3.0+** from A1/A2 TWO-SIDED, apply v0.2.51: both routes together need repeatable high-value chance support or a strong data-poor substitute. Raw goals, names, possession, or generic attacking reputation are not enough by themselves.

Under v0.2.52, also distinguish:

- `TWO-SIDED — QUALITY PROVEN`; and
- `TWO-SIDED — NOMINAL / WEAK SECONDARY`.

A nominal second route does not receive the full Two-Sided Priority ranking premium.

---

## 8. Carrier Ceiling / CC+

Use `CC+ — CARRIER CEILING` for a team with credible independent 3+ team-goal potential supported by repeatable scoring/chance evidence and enough attacking depth to sustain pressure after the first goal.

At PRE, before burying a strong favorite/carrier as B/PASS, explicitly audit whether recent low scoring is true chance suppression or merely outcome/finishing/schedule noise. If a credible self-funded ceiling exists but XI uncertainty blocks promotion, tag:

`CC+ CANDIDATE — XI SENSITIVE`

At final XI, a narrow football-led `CARRIER REOPEN — XI CONFIRMED` is allowed for a frozen B/PASS only under the strict v0.2.52 conditions. Market movement alone still cannot rescue PASS.

---

## 9. Frozen PRE and XI rerank

Frozen Work PRE remains history. Confirmed XI is the first legitimate rerank gate.

Classify rotation as:

- `ROTATION — ATTACKING DEPTH PRESERVED`; or
- `ROTATION — COHESION / ROUTE DAMAGE`.

Only the second is an automatic burden downgrade.

Under v0.2.52, **ATTACKING DEPTH PRESERVED is baseline confirmation, not a positive upgrade**. A genuine `XI UPGRADE` requires materially stronger attacking evidence than the frozen uncertainty.

If both teams lose important creators/finishers, or the primary route plus opponent contribution are both materially weakened, apply `DUAL-ROUTE XI DAMAGE` under v0.2.51. A protected line alone cannot rescue that state.

---

## 10. Mandatory market-history conflict check

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

Market history cannot rewrite frozen PRE, create TWO-SIDED, create EGE, or rescue PASS by itself.

---

## 11. Goal-burden regimes

After final XI choose:

- `STANDARD`; or
- `EGE — EXTREME GOAL ENVIRONMENT` under v0.2.50.

EGE is structural/team/XI driven, normally A1 FOCUS TWO-SIDED or ELITE CARRIER. A2 only via the strict v0.2.50 exception. A high market line cannot create EGE.

Persistent high-line acceptance and the no-chase rule remain active: a goal-driven expansion is never a reason to raise burden.

---

## 12. v0.2.51 Market-Confirmed Edge (MCE)

For eligible STANDARD A2/B+ TWO-SIDED cases, v0.2.51 permits:

`MCE +0.25 — MARKET-CONFIRMED EDGE`

Use only when all v0.2.51 conditions clear: preserved XI, credible 3-goal ceiling, same-source/normalized bullish +0.25 move, current line only +0.25 above frozen burden, price at least 1.75, and no dominant compression/suppression branch.

MCE does not create EGE or structural quality and cannot override DUAL-ROUTE XI DAMAGE.

---

## 13. B+ compression hardening

For B+ with an explicit derby/first-leg/1-0/1-1/control/weak-secondary/late-goal-dependence failure mode, protection alone is not enough.

Under v0.2.52:

- XI preservation is neutral;
- line protection is execution protection, not football evidence;
- price is not a structural positive gate.

Require at least one independent positive gate beyond preservation: fresh chance-quality support, a genuine XI upgrade, verified same-source market corroboration that agrees with intact football evidence, material opponent defensive weakening, or a strong CC+ self-funded ceiling.

If none exists:

`B+ PRESERVATION-ONLY HOLD`

---

## 14. User-supplied XI + current odds

The user normally supplies confirmed XI and current executable Asian-total odds. Do not substitute an external current price unless explicitly asked.

Historical odds research is the exception: Normal Chat may automatically retrieve opening/PRE-XI/post-XI context because it is calibration, not execution-price authority.

Do not issue an OFFICIAL LOCK without required current XI + executable price.

---

## 15. Executable price policy

- hard minimum decimal odds: **1.65**;
- preferred: **1.70+**;
- MCE +0.25 requires **1.75+**;
- below 1.65 → `NO BET — HOLD — PRICE TOO SHORT`;
- never stretch merely to improve price;
- burden is chosen before current price.

---

## 16. Official and shadow tracks

Use the same frozen evidence snapshot:

- **Official:** Football v0.2.52
- **Shadow:** Football v0.2.47 CLEAN
- **Shadow:** Football v0.2.48-SHADOW

v0.2.49/v0.2.50/v0.2.51/v0.2.52 patches apply only to the official track. Shadows remain version-faithful and never enter official P/L.

---

## 17. Live and audit boundary

Live evidence validates or invalidates frozen PRE; it does not rewrite it. Keep v0.2.50 no-chase and HT compression/remaining-goal-budget logic.

Audit outcomes carefully:

- both routes contribute → `CLEAN TWO-SIDED VALIDATION`;
- one carrier supplies the total → `CARRIER VALIDATION — NOT CLEAN TWO-SIDED`;
- expected chance quality never appears → `CHANCE-QUALITY MISS`;
- chances appear but goals do not → `CONVERSION VARIANCE`;
- named control branch dominates → `COMPRESSION FAILURE`;
- a nominal two-sided candidate was ranked above a materially stronger self-funded carrier and failed → `RELATIVE-RANKING MISS`;
- a carrier was buried because low recent scores were overweighted despite preserved ceiling → `RECENT-SCORE SUPPRESSION OVERWEIGHTED`.

A temporarily active failure mode is not automatically a model invalidation if the protected prematch line, carrier route and second-half escalation capacity remain intact.

Standard full-match Asian totals settle on 90 minutes + stoppage unless stated otherwise. Counterfactual HOLD/PASS/shadow outcomes never enter official P/L.

---

## 18. Authority and history

For current decisions, this file and the canonical load order win over stale chat text, old handoffs, archived screenshots and superseded documentation. v0.2.52 is prospective from 2026-09-12 ICT. The Sep 12 Tijuana–Querétaro official loss remains settled under v0.2.51 and Atlante–Pachuca remains a historical PASS with no retrospective P/L rewrite.