# Football v0.2.53 — Ranking Integrity + Execution Validation

**Status:** ACTIVE OFFICIAL PATCH  
**Base:** Football v0.2.47 CLEAN  
**Depends on:** v0.2.49, v0.2.50, v0.2.51 and v0.2.52  
**Effective:** 2026-09-12 ICT onward  
**Purpose:** make board rank reflect proven scoring routes, prevent compensation across failed gates, and block invalid MCE/live execution states.

This patch is prospective. It does not rewrite frozen PRE states, historical verdicts, or settled P/L.

---

## 1. Why this patch exists

The Sep 11–12 post-slate audit found a ranking inversion: the displayed FOCUS set reached 3+ goals less often than WATCHLIST, while several later execution labels were applied outside their defined eligibility.

That result is a calibration warning, not proof that every losing FOCUS was wrongly selected or every winning WATCHLIST should have been promoted. v0.2.53 therefore tightens process in four places:

1. prove each scoring route separately;
2. apply non-compensatory ranking gates;
3. validate MCE and live evidence mechanically;
4. monitor rank separation on rolling completed samples.

No rule below may be bypassed because a fixture has attractive names, high raw GF/GA, a protected line, or a favorable final result.

---

## 2. Per-team route state is mandatory

Before assigning a board tier, grade each team's independent scoring route:

- `PROVEN` — repeatable current scoring and chance-quality evidence in the relevant home/away and competition context;
- `SUPPORTED` — credible route with more than one independent support channel, but below PROVEN confidence;
- `NOMINAL` — theoretical contribution inferred mainly from names, opponent leakage, raw goals, or lineup preservation;
- `FAILED` — route is materially suppressed, absent, damaged, or contradicted.

Record the pair as:

`HOME_ROUTE + AWAY_ROUTE`

Examples: `PROVEN + SUPPORTED`, `SUPPORTED + NOMINAL`, `PROVEN + FAILED`.

A genuine `TWO-SIDED — QUALITY PROVEN` label requires both routes to be at least SUPPORTED and at least one route to be PROVEN. `NOMINAL` is never equivalent to a second supported route.

---

## 3. Non-compensatory decision order

Official ranking and execution must follow:

`SCOPE / LEAGUE REGIME → ROUTE PAIR → DOMINANT FAILURE MODE → CHANCE QUALITY → CC+ → BURDEN FIT → EVIDENCE CONFIDENCE → XI / MARKET VALIDATION → CURRENT PRICE`

Earlier failed gates cannot be averaged away by later positives.

Specifically:

- price cannot repair structure;
- market movement cannot create a scoring route;
- raw GF/GA cannot replace chance quality where quality evidence is available;
- lineup preservation cannot upgrade NOMINAL to SUPPORTED;
- a second theoretical route cannot outrank a demonstrated self-funded CC+ carrier;
- a protected Asian line cannot neutralize a dominant compression branch.

---

## 4. PRE tier caps

Apply these maximum PRE states before relative reranking:

| Route pair / structure | Maximum PRE state |
|---|---|
| PROVEN + PROVEN | A1 / FOCUS eligible |
| PROVEN + SUPPORTED | A2 / FOCUS eligible |
| SUPPORTED + SUPPORTED | A2 / FOCUS only if chance quality and failure resistance are both strong; otherwise WATCHLIST |
| PROVEN + NOMINAL | WATCHLIST, unless the PROVEN route independently qualifies as true CC+ |
| SUPPORTED + NOMINAL | B+ / WATCHLIST |
| NOMINAL + NOMINAL | PASS |
| Any FAILED route | WATCHLIST at most; PASS unless a true CC+ carrier survives the failure branch |
| Data-poor substitute used for either route | A2 at most; never A1 |

These are ceilings, not automatic awards. League regime, failure mode, chance quality, burden, and evidence confidence may still lower the state.

### FOCUS admission test

A fixture may enter FOCUS only when all are true:

1. it is in actionable scope and passes its league regime;
2. its route pair clears a FOCUS-eligible ceiling above;
3. the selected burden survives the named dominant failure branch;
4. chance-quality evidence supports the burden;
5. the evidence is not dependent on one recent score or one unresolved lineup assumption.

If any item fails, use WATCHLIST, PASS, or UNRESOLVED as appropriate.

---

## 5. Same-window relative rerank

After absolute eligibility, compare every surviving candidate in the same practical kickoff window.

Rank in this order:

1. route pair strength;
2. chance-quality support;
3. self-funded CC+ ceiling;
4. resistance to the named failure mode;
5. lower supported burden;
6. evidence completeness/confidence;
7. current executable price, only after the football order is stable.

The printed grade is an output of this comparison, not an input that automatically wins it.

A nominal B+ two-sided match must not outrank a lower-label candidate with materially stronger route proof, a true CC+ carrier, and a safer supported burden.

---

## 6. League modifiers

League modifiers are applied before PRE promotion and again before final burden selection.

### Japan domestic leagues

The existing registry rule remains a HARD EXCLUDE from 2026-09-12 ICT onward, including J1 League.

Use:

`JAPANESE DOMESTIC LEAGUE — HARD EXCLUSION`

One winning exception, cup result, or isolated high-scoring match does not reopen the domestic-league pool. Japanese domestic cups and senior continental fixtures remain governed by the separate registry rule.

### China Super League

China Super League remains CONDITIONAL for admission.

For any CSL `O3.0+` or MCE assessment, require at least one of:

- both teams' relevant current home/away evidence independently supports a credible 3+ match environment; or
- one team qualifies as true `CC+ — CARRIER CEILING` and the selected burden survives weak opponent contribution.

If neither clears:

`CSL HIGH-BURDEN GATE FAILED — HOLD/PASS`

Recent all-venue averages alone do not clear this gate.

---

## 7. MCE hard validator

MCE remains the narrow v0.2.51 prematch exception. It is valid only when every required field passes.

Required validator fields:

- `mce_stage = PREMATCH_POST_XI`;
- `pre_grade` is exactly A2 FOCUS or B+ WATCHLIST;
- structure is TWO-SIDED and the route pair is at least SUPPORTED + SUPPORTED;
- frozen burden is at least O2.5;
- final XI preserves both required routes;
- football evidence supports a credible 3-goal ceiling;
- same-source or explicitly normalized OPEN → post-XI prematch total moved bullish by at least +0.25;
- current line is exactly +0.25 above frozen burden;
- current price is at least 1.75;
- no dominant suppression, compression, or DUAL-ROUTE XI DAMAGE state;
- any league-specific high-burden gate clears.

Any failed or unknown required field means:

`MCE INVALID — STANDARD BURDEN OR HOLD`

Automatic hard failures include:

- A1, B/PASS, or UNRESOLVED PRE grade;
- live/in-play assessment;
- price shortening or normal live price decay at the same line;
- cross-book movement presented as a continuous line history;
- a bullish move smaller than +0.25;
- use of market movement to create route quality.

A live price improving after scoreless minutes is `STANDARD DECAY`, never MCE.

---

## 8. Live Over evidence gate

Do not issue an official live Over from score/minute/price alone.

A live LOCK requires a synchronized evidence epoch containing:

- current score and minute;
- current executable total and odds;
- current attacking/chance-quality evidence for the same match state;
- conversion-quality assessment;
- remaining-goal-budget assessment;
- confirmation that the live line is not merely a goal-driven expansion chase.

If the live chance-quality channel is missing, stale, or not synchronized:

`LIVE CHANCE QUALITY UNAVAILABLE — HOLD`

A future separately documented and tested exception may override this rule. No implied exception exists in v0.2.53.

---

## 9. Coverage and identity integrity

AiScore fixture identity is the primary unique key.

The preferred coverage key is:

`AISCORE:<fixture_id>`

Only when the AiScore ID is unavailable may the fallback be used:

`competition + normalized_home + normalized_away + kickoff_utc`

Before publishing or reading a board:

1. collapse exact duplicate keys;
2. detect same-match rows with conflicting date, kickoff, grade, tier, eligibility, or completeness;
3. block active publication/ranking until the conflict is resolved;
4. preserve the conflict for audit.

Use:

`COVERAGE IDENTITY CONFLICT — PUBLICATION BLOCKED`

No conflicting duplicate may appear twice in the same ranking pool or on two slate dates.

---

## 10. Rolling ranking calibration

For every completed official board, retain at minimum:

- frozen board tier;
- PRE grade;
- route pair;
- route-quality label;
- CC+ state;
- league regime;
- burden and regime;
- MCE validator result;
- whether both routes contributed;
- whether one carrier supplied the total;
- final total-goal settlement and official P/L where applicable.

Review rank separation on a rolling sample only after at least:

- 30 finished FOCUS/WATCHLIST fixtures in total; and
- 10 finished fixtures in each compared tier.

Before that threshold, results are diagnostic only.

At threshold, if FOCUS does not outperform WATCHLIST on the predeclared primary ranking metric, declare:

`RANKING CALIBRATION HOLD`

Then tighten FOCUS admission and inspect route-label accuracy, burden mix, league mix, and evidence completeness. Do not automatically promote WATCHLIST selections or fit a new rule to isolated winners.

The primary ranking metric must be chosen before the comparison window. Default:

- for structural board quality: rate reaching the frozen structural goal threshold;
- for official betting performance: settled ROI and closing-line/burden discipline, reported separately.

---

## 11. Audit labels

Use these labels prospectively where applicable:

- `ROUTE PROOF FAILURE`
- `FOCUS ADMISSION FAILURE`
- `LEAGUE HIGH-BURDEN FAILURE`
- `MCE ELIGIBILITY FAILURE`
- `LIVE EVIDENCE FAILURE`
- `COVERAGE IDENTITY CONFLICT`
- `RELATIVE-RANKING MISS`
- `RANKING CALIBRATION HOLD`

Outcome labels do not retroactively change the evidence state or settlement.

---

## 12. Authority

v0.2.53 overrides subordinate wording that:

- treats nominal two-sidedness as equivalent to proven two-sidedness;
- allows compensating positives to overcome an earlier hard failure;
- applies MCE outside A2 FOCUS/B+ WATCHLIST prematch eligibility;
- treats live price decay as market-confirmed edge;
- permits live LOCK without synchronized chance-quality evidence;
- ranks or publishes unresolved duplicate fixture identities.

All unchanged v0.2.47/v0.2.49/v0.2.50/v0.2.51/v0.2.52 rules remain active.
