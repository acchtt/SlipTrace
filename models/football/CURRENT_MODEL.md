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
**Shadow comparison tracks:** Football **v0.2.47 CLEAN** and Football **v0.2.48-SHADOW**  
**Model B comparison rule:** when Model B is explicitly run side-by-side, it inherits `MODEL_RULES_FOOTBALL_AB_MARKET_ALIGNMENT.md` **and** `MODEL_RULES_FOOTBALL_AB_DECAY_FIRST_EXECUTION.md`. Its structural participation bands remain available for audit/qualification, but they may not create direct prematch exposure above frozen supported burden or pre-reserve exposure slots by rank.  
**Fixture authority:** **AiScore only**  
**Operational display timezone:** `Asia/Ho_Chi_Minh` (ICT, UTC+7)  
**Step-0 time policy:** preserve AiScore source local time + timezone/offset; convert to ICT later when scheduling.

This file is the operating authority for Football. **Football A is the main active model.** Historical assessments remain tied to the model version/state that actually produced them.

## LIVE VERDICT-FIRST / EXECUTION LATENCY CONTROL — ACTIVE

Effective 2026-09-20 ICT:

For live and just-started user-supplied markets, execution order is:

`MINIMAL STATE READ -> ACTIONABLE VERDICT -> PERSIST / RESEARCH / EXPLANATION`

Do not delay a clear live action for web research, H2H lookup, Airtable writes, or explanatory prose. If a goal/state change occurs before action, the old quote is VOID and requires a new score-epoch reprice.

This changes response order only; it does not lower structural, burden, price, suppression, or state-integrity standards.

---

## DECAY-FIRST EXECUTION AUTHORITY — ACTIVE

Effective prospectively from 2026-09-20 ICT, load and apply:

`models/football/rules/MODEL_RULES_FOOTBALL_AB_DECAY_FIRST_EXECUTION.md`

This rule is authoritative over conflicting HMA / participation language.

Core invariant:

`STRONGER STRUCTURE = MORE CONFIDENCE TO WAIT, NOT PERMISSION TO BUY A HIGHER TOTAL`

- Direct prematch official exposure requires the selected line to be at or below the frozen supported execution burden.
- If the market is above supported burden, use `QUALIFIED — LIVE DECAY PLAN` and freeze the supported target line + minimum price.
- Football A HMA may no longer auto-lock +0.25/+0.50 above burden; it is monitoring/audit tolerance only.
- Model B participation expansion may no longer create direct exposure above burden; those cases become Model B live-decay waits.
- Model B exposure slots are not pre-reserved by rank for fixtures whose markets are still above burden.
- Recent same-venue H2H / suppression re-screen is mandatory before O3.0+ execution.

The active Sep19–20 O2.5/O2.75 temporary relaxation remains compatible: qualify the lower protected burden first, then WAIT if the market is higher.

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

## TEMPORARY SESSION OVERRIDES — 2026-09-19 / 2026-09-20

### A. Sep-18 execution-relaxation experiment — extended to noon Sep 19

For **decision timestamps from 2026-09-18 12:24 ICT through 2026-09-19 11:59:59 ICT**, load and apply:

`models/football/session_overrides/SESSION_OVERRIDE_2026-09-18_EXECUTION_RELAXATION.md`

This remains a **session-only experiment, not a permanent official model patch**. The user explicitly extended its expiry to **2026-09-19 12:00 ICT**. At noon Sep 19 it expires automatically; none of its O2.5/O2.75, -0.25 undercut, or general session relaxations survive beyond noon unless separately authorized.

### B. Early-Conversion trial — Saturday + Sunday

For **decision timestamps from 2026-09-19 10:40 ICT through 2026-09-20 23:59:59 ICT**, load and apply:

`models/football/session_overrides/SESSION_OVERRIDE_2026-09-19_TO_2026-09-20_EARLY_CONVERSION.md`

This is a **temporary two-day execution experiment, not a permanent model patch**. It adds:
- the narrow `EARLY-CONVERSION ELIGIBLE` lane for qualifying **A1/A2 FOCUS TRUE CC+ / elite two-sided** profiles when a goal arrives before planned decay; and
- from **2026-09-19 23:10 ICT**, a temporary **burden-specific prematch upper-tail relaxation** for **A1/A2 FOCUS and A2 WATCHLIST** at protected **O2.5/O2.75** only.

For the temporary prematch relaxation:
- O2.5 requires a **QUALITY-PROVEN 3+ path** rather than separate 4+ proof;
- O2.75 requires a **ROBUST 3+ path + non-trivial fourth-goal support**;
- O3.0+ keeps the permanent 4+ upper-tail standard;
- B+/B/PASS remain outside this automatic relaxation.

It does **not** rewrite frozen PRE, promote A2 WATCHLIST/B+/PASS, or create a blanket Over rule.

From **10:40–11:59:59 ICT on Sep 19**, both temporary files may apply. If both apply, use the interaction rules in the Early-Conversion override. From **12:00 ICT Sep 19 through Sunday**, only the Early-Conversion override remains active.

At **2026-09-21 00:00 ICT**, all listed temporary overrides have expired and must be ignored unless the user explicitly promotes a tested rule after audit.


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
24. `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.48-SHADOW.md`
25. `models/football/procedures/FOOTBALL_BETTING_PROCEDURE.md`
26. `models/football/airtable/FOOTBALL_COVERAGE_AIRTABLE.md`
27. `models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md`

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

`NORMAL CHAT AISCORE ACTIONABLE SENIOR UNIVERSE → UNIQUE IDENTITY + SCOPE / LEAGUE GATE → ACTIONABLE COMPLETENESS → WORK ROUTE PROOF + STRUCTURAL SCREEN → NON-COMPENSATORY PRE CAPS → SAME-WINDOW STRUCTURAL RANK → FOCUS/WATCHLIST/PASS/UNRESOLVED → FREEZE PRE → NORMAL CHAT XI → MARKET-HISTORY CONFLICT CHECK → FINAL XI / CARRIER REOPEN → CHANCE QUALITY + REGIME/BURDEN → CURRENT USER-SUPPLIED MARKET CENTER + LINES/PRICES → SHARED A/B MARKET-ALIGNMENT GATE → FOOTBALL A HMA / MODEL B PARTICIPATION RULE → EXECUTION PATH → MODEL-SPECIFIC EXPOSURE GATE → OFFICIAL LOCK / EXPOSURE HOLD / EARLY SAME-LINE PRICE PLAN / QUALIFIED LIVE-DECAY PLAN / STRUCTURAL HOLD / SHADOW`

Work remains structural and price/XI/market-history blind. Normal Chat owns XI, market-history checks, market-center/alignment checks, current price, HMA testing, Model B participation testing, exposure selection, planned live-decay execution, schedule display, and live review.

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

## 5. Current decision order

Football A order:

`SCOPE / LEAGUE REGIME → HOME + AWAY ROUTE STATES → DOMINANT FAILURE MODE → PRACTICAL 3+ CEILING → PASS RESCUE SCREEN IF PROVISIONAL PASS → OPPONENT FAILURE/LEAKAGE COMPATIBILITY → CHANCE QUALITY / URGENCY → BURDEN FIT → EVIDENCE CONFIDENCE → STRUCTURAL RANK (PRE, PRICE-BLIND) → FIRST-PASS XI → MARKET-HISTORY CONFLICT CHECK → FINAL XI → CHANCE-QUALITY HARDENING → STANDARD/EGE BURDEN → CURRENT MARKET CENTER + LINE/PRICE BOARD → SHARED A/B MARKET-ALIGNMENT GATE → FOOTBALL A HMA OR MODEL B PARTICIPATION TEST → EXECUTION PATH → MODEL-SPECIFIC EXPOSURE GATE → EXPOSURE DECISION`

When Model B is run side-by-side, the same market-alignment gate runs before Model B's participation lane.

Three outputs remain mandatory:

1. **Structural Rank**
2. **Execution Class / Plan**
3. **Exposure Decision**

Execution/blocker states now include:

- `DIRECT LOCK ELIGIBLE`
- `DIRECT LOCK ELIGIBLE — HIGH-MARKET ACCEPTANCE`
- `MARKET UNDERCUT — RE-SCREEN REQUIRED`
- `SEVERE MARKET UNDERCUT — NO INSTANT LOCK`
- `HIGH-MARKET CONFLICT — MANDATORY RE-SCREEN`
- `QUALIFIED — EARLY SAME-LINE PRICE PLAN`
- `QUALIFIED — LIVE DECAY PLAN`
- `QUALIFIED — PRICE BELOW FLOOR`
- `STRUCTURAL HOLD`
- `SHADOW ONLY`

`DIRECT LOCK ELIGIBLE != AUTOMATIC OFFICIAL LOCK`

### Shared A/B market-alignment gate

A lower Over total is mechanically more protected, but it is **not automatically evidence of value**.

Before any instant/direct decision for either model, identify the current market center and compare it with the frozen structural burden.

- market center `0.25+` below the lower edge / single frozen burden → `MARKET UNDERCUT — RE-SCREEN REQUIRED`;
- market center `0.50+` below → `SEVERE MARKET UNDERCUT — NO INSTANT LOCK` unless a specific football-led override is documented;
- a B/PASS or materially lower-ranked fixture carrying a market center `0.50+` above the model's implied burden, or among the slate's clearly highest goal totals, triggers `HIGH-MARKET CONFLICT — MANDATORY RE-SCREEN` rather than an ordinary silent PASS.

The market may force reinspection but cannot create structural quality.

Line hierarchy is explicit:

`LOWEST ACCEPTABLE BURDEN → PRICE FLOOR → PRICE AS TIE-BREAKER`

A higher total with a higher payout is a **higher-price / higher-burden alternative**, not a better protected line.

Detailed authority: `MODEL_RULES_FOOTBALL_AB_MARKET_ALIGNMENT.md`.

---

## 6. Football A exposure gate

### A2 upper-tail gate

When an A2 candidate is executable at the top of its supported burden/range, or above the structural ceiling through HMA, official exposure requires at least one of:

- `4+ TOTAL PATH — QUALITY PROVEN`;
- `TRUE CC+ PATH` with credible additional-goal support;
- `ELITE TWO-SIDED PATH` with strong chance quality and failure resistance.

If none clears:

`DIRECT LOCK ELIGIBLE — NO BET — EXPOSURE HOLD — UPPER-TAIL INSUFFICIENT`

A1 remains the strongest primary lane.

### B+ protected-line lane — ACTIVE

For Football A, a frozen `B+ WATCHLIST` candidate may now become directly executable at the **exact frozen supported burden** without an extra positive hardener when:

- confirmed XI preserves the frozen route construction;
- the exact frozen supported line is available;
- price is **>=1.65**;
- market alignment is acceptable; and
- there is no strong current, mechanism-compatible negative veto.

Use `B+ PROTECTED-LINE — DIRECT LOCK ELIGIBLE`, then finalize `B+ PROTECTED-LINE — OFFICIAL LOCK` when no other blocker remains.

This does **not** structurally promote B+ and does not create automatic B+ HMA. A strong negative veto still blocks exposure. For `CARRIER-LED / PROVEN+NOMINAL`, +0.25 above burden is allowed only when `PRACTICAL CARRIER CEILING — VERIFIED` clears; generic carrier-led or candidate-only evidence is insufficient. +0.50 or more remains non-automatic.

For every B+ no-bet/wait, persist one primary reason from the active B+ taxonomy: `LINE NEVER REACHED — NO EXECUTION OPPORTUNITY`, `EXECUTABLE LINE AVAILABLE — MODEL HELD`, `+0.25 AVAILABLE — WAITED FOR LOWER BURDEN`, `STRONG VETO HOLD — EXECUTABLE PRICE REJECTED`, or `ABOVE BURDEN — NO QUALIFIED EXTENSION`. Never infer line non-arrival merely from the absence of a ticket.

### High-Market Acceptance overlay

HMA applies to **Football A only** and never changes the frozen structural ceiling.

- `A1 FOCUS`: up to `+0.25` normally; up to `+0.50` only with a strong upper-tail hardener.
- `A2 FOCUS`: up to `+0.25` only with the A2 upper-tail gate cleared at the offered burden.
- `A2 FOCUS` with exceptional TRUE CC+ / repeatable 4+ / elite two-sided proof: up to `+0.50`.
- `A2 WATCHLIST`, `B+`, PASS, unresolved, and fragile capped cases: **no automatic HMA extension**. The separate B+ protected-line patch may authorize the exact frozen supported burden, and a narrow carrier-specific +0.25 extension only under its explicit hardener.
- `+0.75` or more above the frozen structural ceiling: no immediate HMA exposure.

The detailed authority is `MODEL_RULES_FOOTBALL_A_HIGH_MARKET_ACCEPTANCE.md`.

### Cross-match exposure suppression removed

Effective 2026-09-19 ICT, Football A no longer blocks an otherwise valid exposure because a higher-ranked match exists in the same practical kickoff/exposure window.

Structural Rank remains an ordering/audit field, but each fixture is approved or held on its own football, XI, market-alignment, burden, upper-tail and price evidence.

A higher-ranked match being active, waiting, executable or already exposed is **not** a blocker for another match.

Use:

`PRIORITY INVERSION = NOT APPLICABLE — PATCH REMOVED`

for compatibility where that field is still persisted.

Detailed authority: `MODEL_RULES_FOOTBALL_A_NO_CROSS_MATCH_EXPOSURE_SUPPRESSION.md`.

Official exposure evaluation now uses:

`STRUCTURAL VALIDITY → MARKET ALIGNMENT → UPPER-TAIL / ROUTE PROOF → BURDEN PROTECTION → PRICE FLOOR → EXPOSURE DECISION`

---

## 7. High-market and live-decay execution policy

Football A no longer plans around a prematch quarter-line drop, and it no longer forces every strong high-market match to decay all the way back to the raw structural ceiling.

### 7.1 Test market alignment, then HMA before assigning live decay

If the prematch market is below frozen burden, resolve the shared A/B market-undercut gate first.

If the prematch market is above supported burden:

1. complete the market-alignment / high-market conflict re-screen;
2. test whether the offered line is inside the Football A HMA band;
3. if HMA clears and price/exposure gates clear, execute prematch;
4. if HMA clears but only price blocks, use `QUALIFIED — EARLY SAME-LINE PRICE PLAN`;
5. if the line is outside HMA, use `QUALIFIED — LIVE DECAY PLAN` toward the **nearest independently qualified HMA boundary**;
6. do not automatically wait all the way back to the raw structural ceiling.

### 7.2 Early same-line price plan

When the line is already inside a valid HMA band but price is below the hard floor, freeze the same line and minimum price before kickoff.

During approximately the first **0'–12' at 0-0**:

- PRE structure and confirmed XI remain primary;
- live stats are veto/context, not a mandatory promotion gate;
- if the same line clears the price floor and all exposure gates remain clear, execute promptly;
- a goal, red card, major injury, tactical collapse, or route damage expires the simple trigger and requires a fresh state-integrity reassessment.

Do not chase goal-driven line expansion.

### 7.3 Predeclared live decay can become official

A predeclared `QUALIFIED — LIVE DECAY PLAN` may become official after kickoff when:

- the plan was frozen before kickoff;
- the user supplies a current executable live line/price;
- the live line is at or below the predeclared target, which may be a valid HMA boundary rather than only the raw structural ceiling;
- price clears the hard floor;
- the original football/XI thesis remains substantially intact;
- score/time state has not created a materially different thesis;
- no red card, major injury, tactical collapse, or route damage invalidates the plan;
- Model A HMA, upper-tail and priority-inversion gates are re-run at the actual live burden.

If all clear:

`DIRECT LOCK ELIGIBLE — PREDECLARED LIVE DECAY`

and, after exposure approval:

`OFFICIAL LOCK — LIVE DECAY PLAN`

A first goal does not automatically cancel the plan; it triggers a state-integrity recheck.

### 7.4 Opportunistic live remains quarantined

If no HMA same-line plan or live-decay plan was frozen before kickoff, an attractive live Over remains:

`SHADOW LIVE/DECAY — NO OFFICIAL EXPOSURE`

unless the user grants a match-specific exception.

### 7.5 Same-line price wait at raw supported burden

If the line is already at the raw supported burden but price is below the hard floor, use:

`QUALIFIED — PRICE BELOW FLOOR`

This can become directly executable before kickoff if the same supported line later clears the floor.

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