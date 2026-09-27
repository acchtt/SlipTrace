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
- `rules/MODEL_RULES_FOOTBALL_AB_MARKET_ALIGNMENT.md` — **SHARED A/B MARKET-ALIGNMENT + PROTECTED-LINE INTEGRITY**  
- `rules/MODEL_RULES_FOOTBALL_A.md` — **EXECUTION SELECTION CORRECTION / EXPOSURE GATE + FRAGILE SUPPORTED-ROUTE A2 FOCUS GUARD**  
- `rules/MODEL_RULES_FOOTBALL_A_LIVE_DECAY.md` — **PREDECLARED LIVE-DECAY EXECUTION / NO PLANNED PREMATCH LINE-DECAY WAIT**  
- `rules/MODEL_RULES_FOOTBALL_A_HIGH_MARKET_ACCEPTANCE.md` — **FOOTBALL A-ONLY HIGH-MARKET ACCEPTANCE / EARLY SAME-LINE PRICE EXECUTION**
- `rules/MODEL_RULES_FOOTBALL_AB_DECAY_FIRST_EXECUTION.md` — **DECAY-FIRST BURDEN PROTECTION / NO AUTOMATIC ABOVE-BURDEN PREMATCH LOCK**
- `rules/MODEL_RULES_FOOTBALL_A_NO_CROSS_MATCH_EXPOSURE_SUPPRESSION.md` — **REMOVE SAME-WINDOW / CROSS-MATCH EXPOSURE SUPPRESSION**
- `rules/MODEL_RULES_FOOTBALL_A_AUTO_PUBLISH_USER_PREMATCH_ODDS.md` — **AUTO-PUBLISH OFFICIAL LOCKS FROM USER PREMATCH ODDS**  
- `rules/MODEL_RULES_FOOTBALL_A_BPLUS_PROTECTED_LINE.md` — **B+ EXACT-SUPPORTED-BURDEN EXECUTION LANE**  
- `rules/MODEL_RULES_FOOTBALL_A_PRACTICAL_CEILING_RANKING.md` — **PRACTICAL 3+ CEILING / CROSS-GRADE STRUCTURAL RANKING**  
- `rules/MODEL_RULES_FOOTBALL_A_PASS_RESCUE.md` — **B/PASS PRACTICAL-CEILING RESCUE / VERIFIED-CARRIER RE-SCREEN**  
- `rules/MODEL_RULES_FOOTBALL_A_TWO_ROUTE_HARDENING.md` — **A2 TWO-ROUTE INDEPENDENCE / FOCUS HARDENING**  
- `rules/MODEL_RULES_FOOTBALL_A_CARRIER_MARKET_DECOMPOSITION.md` — **AH + TOTAL + 1X2 CARRIER DECOMPOSITION / MARKET-CALIBRATED CURRENT PRE**  
- `rules/MODEL_RULES_FOOTBALL_A_POST_XI_WEB_RESEARCH_GATE.md` — **MANDATORY POST-XI FOOTBALL WEB-RESEARCH / WORKFLOW REGRESSION GUARD**  
**Shadow comparison tracks:** Football **v0.2.47 CLEAN** and Football **v0.2.48-SHADOW**  
**Model B comparison rule:** when Model B is explicitly run side-by-side, it inherits `MODEL_RULES_FOOTBALL_AB_MARKET_ALIGNMENT.md` **and** `MODEL_RULES_FOOTBALL_AB_DECAY_FIRST_EXECUTION.md`. Its structural participation bands remain available for audit/qualification, but they may not create direct prematch exposure above frozen supported burden or pre-reserve exposure slots by rank.  
**Fixture authority:** **AiScore only**  
**Operational display timezone:** `Asia/Ho_Chi_Minh` (ICT, UTC+7)  
**Step-0 time policy:** preserve raw AiScore source time during broad discovery; before a Work handoff is finalized, every Work-admitted fixture must have one authoritative explicitly-zoned AiScore kickoff (explicit Match-Info UTC, machine timestamp/epoch, or explicit offset), one verified UTC value, and one one-time ICT conversion. Localized/display-only clocks are not UTC authority. Work validates the verified handoff time and must not guess or reconvert from display text.

This file is the operating authority for Football. **Football A is the main active model.** Historical assessments remain tied to the model version/state that actually produced them.

### Step-1 PRE compiler authority

For all new Step-1 / Work structural assessments, `models/football/procedures/FOOTBALL_PRE_DECISION_SPEC.md` is the compiled final operational authority. It does not change the predictive model; it resolves overlapping active PRE wording into one deterministic decision sequence. Older route-symmetry, PRE-XI, carrier, PASS-rescue, burden, or rank wording must not be executed independently when the compiled spec gives the Step-1 rule.

For all new Step-2 XI/odds assessments (the user's workflow Step 3), `models/football/procedures/FOOTBALL_STEP2_EXECUTION_SPEC.md` is the compiled final operational authority. It preserves frozen PRE history while resolving H2H, XI mechanism integrity, EGE/Decay-First, HMA, B+, carrier-current-PRE, live eligibility, verdict finality and persistence order into one deterministic sequence. Older Step-2 wording must not be executed independently when the compiled spec defines the outcome.

## MATCH-SPECIFIC LIVE EXCEPTION — MIDTJYLLAND WOMEN vs FC COPENHAGEN WOMEN — ACTIVE UNTIL FT

For the exact Denmark A-Liga Women fixture **Midtjylland Women vs FC Copenhagen Women** on 2026-09-27 ICT, load and apply:

`models/football/session_overrides/SESSION_OVERRIDE_2026-09-27_MIDTJYLLAND_W_FC_COPENHAGEN_W.md`

This is a one-fixture live exception. It permits a fresh live structural epoch despite no frozen Work PRE and bypasses opportunistic-live shadow quarantine for this match only. All normal research, price, burden, carrier, state-integrity and persistence rules remain active. It expires at full time.

---

## MATCH-SPECIFIC LIVE EXCEPTION — INTER WOMEN vs FIORENTINA WOMEN — ACTIVE UNTIL FT

For the exact Italy Serie A Women fixture **Inter Women vs Fiorentina Women** on 2026-09-27 ICT, load and apply:

`models/football/session_overrides/SESSION_OVERRIDE_2026-09-27_INTER_W_FIORENTINA_W.md`

This is a one-fixture live exception. It prospectively bypasses the earlier missed-screen/unresolved state, permits a fresh live structural epoch, and bypasses opportunistic-live shadow quarantine for this match only. All normal research, price, burden, carrier, state-integrity and persistence rules remain active. It expires at full time.

---

## MATCH-SPECIFIC PREMATCH EXCEPTION — AJAX WOMEN vs ADO DEN HAAG WOMEN — ACTIVE UNTIL FT

For the exact Netherlands Eredivisie Women fixture **Ajax Women vs ADO Den Haag Women** on 2026-09-26 ICT, load and apply:

`models/football/session_overrides/SESSION_OVERRIDE_2026-09-26_AJAX_W_ADO_DEN_HAAG_W.md`

This one-fixture exception bypasses the prior Step-0 cheap-gate exclusion and missing frozen Work PRE, and permits a fresh prematch structural epoch. It does **not** waive confirmed XI, mandatory post-XI football research, market-history/context review, burden protection, the 1.65 floor, carrier/market-alignment, upper-tail checks, state integrity, or persistence. It expires automatically at full time.

---

## MATCH-SPECIFIC LIVE EXCEPTION — VIETNAM vs PHILIPPINES — ACTIVE UNTIL FT

For the exact FIFA ASEAN Cup Division 1 fixture **Vietnam vs Philippines** on 2026-09-26 ICT, load and apply:

`models/football/session_overrides/SESSION_OVERRIDE_2026-09-26_VIETNAM_PHILIPPINES.md`

This is a one-fixture prospective exception. It permits a fresh live structural epoch despite the missing frozen Work PRE and bypasses the opportunistic-live shadow quarantine for this fixture only. All normal research, price-floor, burden, market-alignment, carrier, state-integrity, no-chase and publication-timing rules remain active. Historical quotes are not retroactively upgraded.

---

## MATCH-SPECIFIC PREMATCH EXCEPTION — JAPAN U23 vs NORTH KOREA U23 — ACTIVE UNTIL FT

For the exact OCA Asian Games fixture **Japan U23 vs North Korea U23** on 2026-09-26 ICT, load and apply:

`models/football/session_overrides/SESSION_OVERRIDE_2026-09-26_JAPAN_U23_NORTH_KOREA_U23.md`

This is a one-fixture exception. It permits a fresh prematch structural epoch despite the missing frozen Work PRE caused by the earlier time-integrity/completeness block. All normal research, price-floor, burden, market-alignment, carrier, upper-tail, state-integrity and persistence rules remain active. It expires automatically at full time.

---

## MATCH-SPECIFIC LIVE EXCEPTION — ICELAND U21 vs FRANCE U21 — ACTIVE UNTIL FT

For the exact UEFA U21 Qualification fixture **Iceland U21 vs France U21** currently in progress on 2026-09-25 ICT, load and apply:

`models/football/session_overrides/SESSION_OVERRIDE_2026-09-25_ICELAND_U21_FRANCE_U21.md`

This is a one-fixture prospective exception only. It bypasses the normal U21 scope exclusion and the opportunistic-live shadow quarantine for this fixture, and permits a fresh live structural epoch despite no frozen PRE. All normal price-floor, burden, market-alignment, carrier, state-integrity, no-chase and publication-timing rules remain active. The exception expires automatically at full time and does not retroactively upgrade earlier shadow quotes.


## LIVE VERDICT-FIRST / EXECUTION LATENCY CONTROL — ACTIVE

For just-started/live user-supplied markets, first classify live eligibility under `FOOTBALL_STEP2_EXECUTION_SPEC.md`.

- predeclared live plan or active match-specific exception: a latency-first **PROVISIONAL FAST VERDICT** may be surfaced before extended research;
- no predeclared plan/exception: immediate result is `NO OFFICIAL LIVE ENTRY — NO PREDECLARED PLAN` / shadow only;
- mandatory post-XI football research still follows immediately in the same assessment;
- Website Pick publication waits for the final same-epoch verdict after the research attempt;
- a goal/card/material state change voids the old quote and starts a new evidence epoch.

Verdict-first changes response order only. It never creates opportunistic official live exposure.

---

## POST-XI FOOTBALL WEB-RESEARCH GATE — ACTIVE

Effective prospectively from **2026-09-26 ICT**, load and apply:

`models/football/rules/MODEL_RULES_FOOTBALL_A_POST_XI_WEB_RESEARCH_GATE.md`

This is a **PROCESS COMPLIANCE FIX**, not a predictive model change.

For every Step-2 XI+odds fixture:

- read the confirmed XI and form a first-pass football interpretation;
- run a fresh targeted fixture-specific football web-research attempt;
- record `POST-XI RESEARCH = FOUND / LIMITED / UNAVAILABLE — ATTEMPTED / SKIPPED — EXPLICIT USER WAIVER`;
- run market-history research separately;
- resolve XI + fresh football evidence + market-history/current-market conflicts before the final prematch verdict.

A market-history lookup does **not** satisfy the football-research gate. Frozen PRE/Airtable/GitHub/model files alone do **not** satisfy it.

An ordinary prematch official lock may not be published when post-XI research status is missing or `NOT CHECKED`.

For just-started/live states, verdict-first still applies, but the research attempt must follow immediately in the same assessment unless already completed for the current XI epoch.

Any future workflow edit that silently removes, merges, or makes this gate optional is a **WORKFLOW REGRESSION** and must fail deterministic operational QA.

---

## CARRIER MARKET DECOMPOSITION / MARKET-CALIBRATED CURRENT PRE — ACTIVE

Effective prospectively from **2026-09-24 ICT**, load and apply:

`models/football/rules/MODEL_RULES_FOOTBALL_A_CARRIER_MARKET_DECOMPOSITION.md`

This is the final Football A authority when its ELITE/EXTREME carrier screen clears.

Core changes:

- Asian handicap, total and 1X2 are mandatory carrier-identification inputs at XI+odds stage.
- Preserve frozen Work PRE historically, but create a separate **MARKET-CALIBRATED CURRENT PRE** for the active decision epoch.
- Use `MCL ≈ (Total + |AH|)/2` and `MOS ≈ max(0,(Total-|AH|)/2)` as carrier-decomposition heuristics.
- Extreme favorite + large AH + high total + intact attacking mechanism triggers an elite-carrier re-screen even when recent raw scorelines are muted.
- When the carrier lane clears, the current PRE may move materially above frozen PRE; the old fixed +0.25/+0.50 HMA caps and raw-burden decay requirement do not constrain this lane.
- Preferred current PRE normally anchors around one quarter-goal below the verified market center; the market-center line itself may be the upper execution boundary when football/XI support it and price clears.
- A WAIT with a decay gap of 1.0+ goals requires an unreachable-decay review; 1.5+ goals may not remain a raw-burden WAIT without documented market distortion.
- XI/absence downgrades are mechanism-based, not headcount-based.
- Cup/first-leg status is not a generic suppression veto.
- B+ leakage-only matches require stronger carrier failure-resistance and must not outrank elite carrier environments merely because their lower line is easier to execute.

Historical frozen states remain unchanged.

---

## DECAY-FIRST EXECUTION AUTHORITY — ACTIVE

`MODEL_RULES_FOOTBALL_AB_DECAY_FIRST_EXECUTION.md` remains the ordinary execution anchor and is compiled by `FOOTBALL_STEP2_EXECUTION_SPEC.md`.

Current compiled meaning:

- ordinary direct prematch exposure may not buy a line above frozen supported burden;
- generic HMA is monitoring/audit only above frozen burden;
- EGE may remain a current football-regime diagnostic but does not itself create above-frozen direct execution;
- ordinary B+ +0.25 is WAIT/live-decay despite older direct-label text;
- exact B+ frozen supported burden remains directly eligible under the B+ protected-line rule;
- ELITE/EXTREME `MARKET-CALIBRATED CURRENT PRE` under Carrier Market Decomposition is the explicit later current-PRE exception that may create a different executable burden;
- O3.0+ still requires the compiled H2H/suppression and upper-tail gates.

---

## TEMPORARY BLOCK OVERRIDE — ROMANIA LIGA II + UAE PRESIDENT CUP — 2026-09-22

For the exact four-match block authorized by the user on 2026-09-22, load and apply:

`models/football/session_overrides/SESSION_OVERRIDE_2026-09-22_ROMANIA_LIGA2_UAE_PRESIDENT_CUP_BLOCK.md`

This is an identity-limited one-block exception only. It bypasses the normal lower-division / small non-European cup scope exclusions for those four fixtures and changes nothing else. Normal XI, burden and execution gates remain active.

---

## TEMPORARY SCOPE OVERRIDE — 2026-09-22 THROUGH 2026-09-27

For **2026-09-22 14:26 ICT through 2026-09-27 23:59:59 ICT**, load and apply:

`models/football/session_overrides/SESSION_OVERRIDE_2026-09-22_TO_2026-09-27_AGS_U23_QATAR_STARS_CUP.md`

This is a **temporary scope exception only**, not a permanent model/registry promotion.

During the active interval:

- official **OCA Asian Games U23 football** bypasses the generic youth/Uxx scope exclusion;
- official **Qatar Stars Cup / Qatari Stars Cup** bypasses the small non-European domestic-cup exclusion;
- both competition families enter Work for normal Football A structural assessment when in-window;
- all normal source-time, status, structural, burden, XI, market-alignment and execution gates remain unchanged.

The override expires automatically at **2026-09-28 00:00 ICT**.

---

## EXPIRED TEMPORARY SESSION OVERRIDES — HISTORICAL ONLY

The Sep-18/19 execution-relaxation and Sep-19/20 Early-Conversion experiments are expired. They remain in Git history/session-override files for audit only and must not enter current production decisions unless the user explicitly starts a new tested override.

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
13. `models/football/rules/MODEL_RULES_FOOTBALL_AB_MARKET_ALIGNMENT.md`
14. `models/football/rules/MODEL_RULES_FOOTBALL_A.md`
15. `models/football/rules/MODEL_RULES_FOOTBALL_A_LIVE_DECAY.md`
16. `models/football/rules/MODEL_RULES_FOOTBALL_A_HIGH_MARKET_ACCEPTANCE.md`
17. `models/football/rules/MODEL_RULES_FOOTBALL_A_NO_CROSS_MATCH_EXPOSURE_SUPPRESSION.md`
18. `models/football/rules/MODEL_RULES_FOOTBALL_A_AUTO_PUBLISH_USER_PREMATCH_ODDS.md`
19. `models/football/rules/MODEL_RULES_FOOTBALL_AB_DECAY_FIRST_EXECUTION.md` — load after HMA/live-decay; final authority on above-burden execution
20. `models/football/rules/MODEL_RULES_FOOTBALL_A_BPLUS_PROTECTED_LINE.md` — Football A B+ exact-supported-burden exposure authority
21. `models/football/rules/MODEL_RULES_FOOTBALL_A_PRACTICAL_CEILING_RANKING.md` — final Football A authority on PRE Structural Rank ordering
22. `models/football/rules/MODEL_RULES_FOOTBALL_A_PASS_RESCUE.md` — final Football A authority on provisional B/PASS practical-ceiling rescue
23. `models/football/rules/MODEL_RULES_FOOTBALL_A_TWO_ROUTE_HARDENING.md` — final Football A authority on A2 two-route independence / FOCUS privilege
24. `models/football/procedures/FOOTBALL_PRE_DECISION_SPEC.md` — **compiled final Step-1 PRE authority; deterministic route/carrier/veto/grade/tier/burden/rank execution**
25. `models/football/rules/MODEL_RULES_FOOTBALL_A_CARRIER_MARKET_DECOMPOSITION.md` — **final Football A authority on post-XI carrier identification, market-calibrated current PRE, and unreachable-decay override**
26. `models/football/rules/MODEL_RULES_FOOTBALL_A_POST_XI_WEB_RESEARCH_GATE.md` — **mandatory Step-2 post-XI football research + regression guard**
27. `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.48-SHADOW.md`
28. `models/football/procedures/FOOTBALL_BETTING_PROCEDURE.md`
29. `models/football/airtable/FOOTBALL_COVERAGE_AIRTABLE.md`
30. `models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md`
31. `models/football/procedures/FOOTBALL_STEP2_EXECUTION_SPEC.md` — **compiled final Step-2 XI/odds execution authority; loaded last for current verdict semantics**

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

`NORMAL CHAT AISCORE ACTIONABLE SENIOR UNIVERSE -> UNIQUE IDENTITY + SCOPE / LEAGUE GATE -> ACTIONABLE COMPLETENESS -> WORK PRE COMPILER -> FREEZE PRE -> NORMAL CHAT STEP-2 EXECUTION COMPILER -> OFFICIAL LOCK / QUALIFIED WAIT / STRUCTURAL HOLD / SHADOW`

Work remains structural and price/XI/market-history blind. Normal Chat Step 2 executes `FOOTBALL_STEP2_EXECUTION_SPEC.md`, which owns XI, post-XI football research, H2H, market-history, frozen-PRE alignment, carrier/current-PRE, burden authority, execution, publication and live-state handling.

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

### A2 two-route independence hardening — ACTIVE

Prospective from 2026-09-23 10:27 ICT, every A2 TWO-SIDED candidate must classify the weaker route as `INDEPENDENT SECOND ROUTE` or `CONDITIONAL SECOND ROUTE` under `MODEL_RULES_FOOTBALL_A_TWO_ROUTE_HARDENING.md`.

- `PROVEN + SUPPORTED` with a conditional weaker route is capped at `A2 WATCHLIST` unless TRUE CC+ / VERIFIED practical carrier ceiling independently supports the required total or direct chance-quality evidence upgrades the weaker route.
- `SUPPORTED + SUPPORTED` defaults to `A2 WATCHLIST`; FOCUS requires both routes to have independent current chance-quality/creation proof and XI preservation.
- Opponent leakage, BTTS/Over frequency, H2H scorelines, score/form proxy, or merely naming expected attackers in the XI cannot by themselves harden a second route.
- Supported burden must come from the reliable 3+ mechanism; do not raise burden by adding two weak one-goal routes together.

PRE Structural Rank is now governed by `MODEL_RULES_FOOTBALL_A_PRACTICAL_CEILING_RANKING.md`.

**Route symmetry no longer receives automatic ranking priority.** Rank the most reliable practical path to the supported total using:

`PRACTICAL SELF-FUNDED 3+ CEILING > OPPONENT FAILURE/LEAKAGE COMPATIBILITY > CHANCE QUALITY/URGENCY > FAILURE-MODE RESISTANCE > SECONDARY-ROUTE QUALITY > ROUTE SYMMETRY/GRADE AS TIE-BREAKER`

A `B+ WATCHLIST / CARRIER-LED` fixture with a `PRACTICAL CARRIER CEILING — VERIFIED` independent 3+ carrier path and compatible opponent failure may rank above an ordinary `A2 FOCUS / TWO-SIDED` fixture. Preserve the original grade/tier; do not promote B+ to A2 merely to justify the rank.

**Carrier verification hardener:** `CARRIER-LED` alone receives no ranking bonus. Every carrier-priority candidate must be tagged `VERIFIED`, `CANDIDATE`, or `UNVERIFIED`; only `VERIFIED` receives first-order practical-ceiling rank credit or cross-grade inversion authority.

Before freezing B/PASS, apply `MODEL_RULES_FOOTBALL_A_PASS_RESCUE.md`. A provisional PASS with at least one usable route must receive the practical-ceiling rescue screen. If `PRACTICAL CARRIER CEILING — VERIFIED` plus compatible opponent failure clears and no strong veto remains, rescue to `B+ WATCHLIST / CARRIER-LED`. Candidate-only or unverified carriers remain PASS. Strong current, mechanism-compatible negative vetoes remain authoritative.

Supported burden is chosen before current price. **PRE Structural Rank is price/market blind.** Price cannot create structural quality or improve rank.

**HMA does not change the structural burden or structural ceiling.** It is an execution overlay only.

---

## 5. Compiled Step-2 decision order

For all new XI/odds assessments use:

`FROZEN PRE TRACE -> IDENTITY/STATUS -> EPOCH CLASS -> XI ROLE-MECHANISM MATRIX -> POST-XI FOOTBALL RESEARCH -> H2H/MATCHUP GATE -> CURRENT CQ/FAILURE UPDATE -> MARKET HISTORY -> FROZEN_PRE_MARKET_ALIGNMENT -> EGE/CARRIER CURRENT-EPOCH COMPILER -> CURRENT_PRE_EXECUTION_FIT -> BURDEN AUTHORITY -> B+/UPPER-TAIL GATES -> DECAY/REACHABILITY -> PRICE -> LIVE/PREMATCH ELIGIBILITY -> PROVISIONAL/FINAL VERDICT -> PERSISTENCE TRANSACTION`

Detailed authority: `models/football/procedures/FOOTBALL_STEP2_EXECUTION_SPEC.md`.

Three outputs remain separate:

1. frozen **Structural Rank / PRE**;
2. current **Execution Class / Plan**;
3. final **Exposure Decision**.

Current execution invariants:

- frozen PRE is never overwritten;
- `FROZEN_PRE_MARKET_ALIGNMENT` and `CURRENT_PRE_EXECUTION_FIT` are separate;
- generic HMA never creates ordinary above-burden direct exposure;
- EGE alone does not bypass Decay-First;
- exact B+ frozen burden may execute under the protected-line rule;
- ordinary B+ +0.25 waits unless an ELITE/EXTREME current-PRE carrier independently authorizes that burden;
- opportunistic live without a predeclared plan/active exception remains shadow-only;
- H2H can corroborate a current mechanism but cannot create a route or hard veto alone.

---

## 6. Football A exposure gate

Use the compiled B+/upper-tail/H2H/current-failure gates in `FOOTBALL_STEP2_EXECUTION_SPEC.md`.

Official ordinary prematch exposure requires:

`IDENTITY CLEAR -> XI MECHANISM VALID -> RESEARCH COMPLETE -> MARKET ALIGNMENT RESOLVED -> EXECUTION BURDEN AUTHORIZED -> REQUIRED H2H/UPPER-TAIL GATES CLEAR -> PRICE >=1.65 -> NO HARD VETO`

Carrier Market Decomposition may create a separate current-PRE execution burden only when its ELITE/EXTREME screen clears. Price/market alone cannot create that state.

---

## 7. High-market and live-decay execution policy

For current production:

- **HMA = monitoring/audit only** above frozen supported burden;
- ordinary market above supported burden -> `QUALIFIED — LIVE DECAY PLAN` to the supported burden;
- EGE above frozen burden without ELITE/EXTREME current-PRE carrier -> WAIT;
- ELITE/EXTREME carrier -> evaluate market-calibrated current PRE before WAIT;
- just-started/live official exposure requires a predeclared plan or active exact-match exception;
- no predeclared plan/exception -> `SHADOW LIVE/DECAY — NO OFFICIAL EXPOSURE`;
- latency-first live verdict is provisional until the mandatory research attempt completes;
- score/card/material state change voids the old quote and starts a new epoch.

---

## 8. Price and user-supplied execution authority

The user normally supplies confirmed XI and current executable Asian-total odds. A user-supplied prematch odds screenshot/text is deemed currently available and executable at that evidence epoch. Do not ask for a second availability/placement confirmation. Do not replace those current prices with external prices unless explicitly asked.

Active price policy:

- hard minimum decimal odds: **1.65**;
- preferred: **1.70+**;
- never stretch burden merely to improve price;
- never call a higher total a better line merely because the price is higher;
- once structure/XI/market alignment clear, prefer the **lowest acceptable burden that clears the floor**, then use price as a tie-breaker.

Example: `O2.0 @1.69` is more protected than `O2.25 @2.01`; O2.25 may have the better price, but it is a higher-burden alternative.

HMA does not change the price floor. Price cannot create HMA eligibility, market alignment, or upper-tail proof.

---

## 9. Quarantined mechanisms

Continue:

- generic/historical `HIGH-SCORING +0.25 ACCEPTANCE BAND — SHADOW ONLY` outside the new HMA conditions;
- `SHADOW MCE +0.25 — NO OFFICIAL EXPOSURE` where not otherwise superseded by a valid Football A HMA case;
- opportunistic/non-predeclared `SHADOW LIVE/DECAY — NO OFFICIAL EXPOSURE`.

The new HMA lane is **not** a blanket release of the old +0.25 shadow sample. It is a narrower Football A-only official lane with explicit class and upper-tail gates. Model B remains unchanged by HMA.

Model B **is** changed prospectively by the shared A/B market-alignment patch: its existing participation lane must clear market alignment before direct participation.

B+ / CC+ remains a separate audit lane with no automatic structural promotion unless the match is actually A2 FOCUS under the active structural rules. Separately, Football A may execute a B+ WATCHLIST fixture at its exact frozen supported burden under `MODEL_RULES_FOOTBALL_A_BPLUS_PROTECTED_LINE.md`.

---

## 10. Persistence

For every material Football A review, and every side-by-side Model B execution review, persist when observable:

- model / track;
- Structural Rank;
- supported burden and structural ceiling;
- current market center;
- market-center delta vs frozen lower edge / burden;
- `MARKET ALIGNMENT = CLEAR / UNDERCUT / SEVERE UNDERCUT / HIGH-MARKET CONFLICT / UNCLEAR`;
- market re-screen result and any football-led override;
- selected protected line;
- higher-price / higher-burden alternatives where relevant;
- prematch/current line and price;
- HMA excess burden for Football A: `+0.25 / +0.50 / OUTSIDE BAND / N/A`;
- HMA eligibility and hardener when relevant;
- Execution Class / Plan;
- upper-tail state;
- priority-inversion state (`NOT APPLICABLE — PATCH REMOVED` for new decisions);
- Exposure Decision;
- exact blocker/reason.

For `QUALIFIED — EARLY SAME-LINE PRICE PLAN`, also persist:

- accepted HMA line;
- minimum price;
- structural ceiling;
- first timestamp the same line clears the floor;
- score/minute at trigger;
- state integrity;
- final execution decision.

For `QUALIFIED — LIVE DECAY PLAN`, also persist:

- target line and minimum price;
- whether target is raw structural burden or an HMA boundary;
- prematch offered line/price;
- cancellation triggers;
- first target-line timestamp, score and minute;
- actual target price;
- state integrity: `CLEAR / DAMAGED / NEW THESIS`;
- final live exposure decision.

Create Website Picks immediately when an actual `OFFICIAL LOCK` is approved from user-supplied prematch odds. No second confirmation is required. If `DIRECT LOCK ELIGIBLE` has no remaining exposure blocker, finalize it as `OFFICIAL LOCK` and publish in the same assessment. Never create retroactive exposure after kickoff.

---

## 11. Audit separation

Post-slate audit must report separately:

- official Football A normal protected-line locks and P/L;
- `OFFICIAL LOCK — HIGH-MARKET ACCEPTANCE` at +0.25;
- `OFFICIAL LOCK — HIGH-MARKET ACCEPTANCE` at +0.50;
- HMA early same-line price locks;
- official predeclared live-decay locks and P/L;
- predeclared live-decay plans that never reached the nearest valid target;
- target reached but state damaged/new thesis;
- target reached but exposure suppressed by Model A;
- HMA candidates invalidated by early goal/state change;
- A2 WATCHLIST/B+ cases correctly denied HMA;
- opportunistic live shadows;
- DIRECT candidates suppressed by upper-tail or other fixture-specific gates;
- `A2 FOCUS CAP — FRAGILE SUPPORTED ROUTE` cases;
- structural holds;
- legacy +0.25 acceptance-band shadows;
- B+ / CC+ audit lane;
- B+ PROTECTED-LINE exact-burden official locks, negative-veto holds, carrier-specific +0.25 extensions, and above-burden waits;
- MCE shadows;
- FOCUS vs WATCHLIST 3+ and 4+ performance;
- market-undercut fixtures rejected by the shared A/B gate;
- market-undercut fixtures overridden with explicit football evidence;
- low-line instant-lock candidates prevented by the patch;
- high-market PASS/WATCHLIST fixtures reopened by mandatory re-screen;
- selected protected line vs higher-price/higher-burden alternative outcomes;
- Model A vs Model B outcomes separately.

For HMA cases, track both the frozen structural target outcome and the actual HMA line outcome.

Counterfactual/shadow outcomes never enter official P/L.

---

## 12. Authority and history

Football A is the active official model. The fragile A2 FOCUS guard, A2 two-route independence hardening patch, predeclared live-decay patch, Football A-only HMA patch, and shared A/B market-alignment patch are prospective from their activation commits and do not retroactively reclassify earlier decisions or P/L.

`MODEL_RULES_FOOTBALL_AB_MARKET_ALIGNMENT.md` overrides earlier Football A/Model B wording wherever a lower-than-structural market line was treated as automatically favorable or directly executable without first resolving the market disagreement. It also requires a mandatory re-screen when a structurally weak/pass fixture carries a materially higher market center than the model expected.

`MODEL_RULES_FOOTBALL_A_HIGH_MARKET_ACCEPTANCE.md` overrides earlier Football A/v0.2.55/live-decay wording only where those rules forced a qualifying high-ranked FOCUS candidate to wait for the raw structural ceiling despite a valid HMA line or targeted live decay farther than the nearest independently qualified HMA boundary.

`MODEL_RULES_FOOTBALL_A_BPLUS_PROTECTED_LINE.md` is prospective from 2026-09-21 ICT and overrides earlier Football A wording that required an additional positive hardener for every B+ exposure when the **exact frozen supported burden** is already available at >=1.65 and no strong mechanism-compatible negative veto exists. It does not retroactively change Sep 19–20 official P/L.

`MODEL_RULES_FOOTBALL_A_PRACTICAL_CEILING_RANKING.md` is prospective from 2026-09-22 12:38 ICT and is the final Football A authority on PRE Structural Rank. It removes automatic rank privilege from route symmetry / A2 FOCUS labels and explicitly permits a verified B+ carrier-led 3+ path to rank above an ordinary A2 two-sided fixture. It changes ranking only; historical grades/ranks/P&L remain frozen and execution still follows the active burden, veto, market-alignment, decay-first, upper-tail, and B+ protected-line rules.

**Model B is unchanged by the HMA patch and by the Football A B+ protected-line patch. Model B is prospectively governed by the shared A/B market-alignment patch before its own participation rules.**

For current decisions, this file plus the canonical active stack wins over stale chat text, old handoffs, archived screenshots, and superseded documentation.