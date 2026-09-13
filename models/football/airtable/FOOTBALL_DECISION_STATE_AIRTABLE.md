# Football Decision States — Airtable Contract

**Status:** ACTIVE  
**Base:** `SlipTrace Football Decision Control`  
**Table:** `Decision States`  
**Official model:** Football v0.2.54  
**Shadow comparison models:** v0.2.47 CLEAN and v0.2.48-SHADOW

This table records material football assessment states after the frozen coverage/PRE stage. It must preserve version fidelity and must not rewrite historical PRE state.

---

## 1. Model/version rule

Every material record must identify the model version that actually produced it.

Current tracks:

- **Official:** `Football v0.2.54`
- **Shadow:** `Football v0.2.47 CLEAN`
- **Shadow:** `Football v0.2.48-SHADOW`

Historical v0.2.49/v0.2.50/v0.2.51/v0.2.52/v0.2.53 decisions remain under the version that actually produced them. Do not relabel them as v0.2.54.

Do not import v0.2.49/v0.2.50/v0.2.51/v0.2.52/v0.2.53/v0.2.54 patches into either shadow track.

---

## 2. Frozen PRE dependency

Before a later XI/market assessment is written, resolve the fixture against the frozen Work PRE state persisted in `Daily Coverage Ledger`.

Preserve:

- original PRE grade;
- original structural archetype;
- original FOCUS/WATCHLIST/PASS/UNRESOLVED state;
- original route-quality / CC+ candidate state where available;
- original primary/secondary routes and failure mode;
- original frozen structural burden.

A Decision State may record a later downgrade/rerank, v0.2.50 EGE reopen, v0.2.51 MCE state, or v0.2.52 `CARRIER REOPEN — XI CONFIRMED`, but it must not imply that the later state was the original PRE.

If the coverage row demonstrably conflicts with the original Work artifact, classify a persistence sync fault and use the original frozen Work thesis until the bridge is corrected.

---

## 3. Time and fixture-identity rule

Decision States must resolve against the corrected fixture identity and time contract in `FOOTBALL_TIME_AND_SCHEDULE_INTEGRITY.md`.

When a serialized timestamp ends in `Z`, treat it as UTC and convert to ICT exactly once for display.

If a material decision is made near kickoff, confirm the fixture is actually in the expected PRE/LIVE state rather than trusting a stale stored schedule.

A later schedule correction does not rewrite the timestamp/evidence state that actually existed when the historical decision was made; annotate the correction separately.

---

## 4. Material assessment fields

Use the existing schema to record material state, including where applicable:

- `Assessment ID`;
- `Match`;
- `Competition`;
- `Model Version`;
- `Assessment Time`;
- `Minute`;
- `Score`;
- `Reset Epoch`;
- `Assessment Period`;
- `Verdict`;
- `Candidate`;
- `Line`;
- `Odds`;
- `Goal Environment`;
- synchronized/reset fields;
- competition-format / utility checks when relevant;
- xG/chance-quality role;
- primary evidence channels;
- failure-mode / favorite-fade / directional-persistence fields where applicable;
- market scan status where applicable;
- validator result;
- fail reasons;
- evidence summary.

Use provider/evidence-version fields when the decision depends on an external normalized evidence snapshot.

---

## 5. v0.2.52 regime / route / carrier recording

For material official v0.2.52 decisions, preserve the burden regime:

- `STANDARD`; or
- `EGE — EXTREME GOAL ENVIRONMENT`.

Also preserve route/carrier state where relevant:

- `TWO-SIDED — QUALITY PROVEN`;
- `TWO-SIDED — NOMINAL / WEAK SECONDARY`;
- `CC+ — CARRIER CEILING`;
- `CC+ CANDIDATE — XI SENSITIVE`;
- `CARRIER REOPEN — XI CONFIRMED`;
- `B+ PRESERVATION-ONLY HOLD`.

For EGE, preserve frozen PRE burden, post-XI EGE burden, structural/team/XI reasons, current market line/price, execution mode and failure mode.

For carrier reopen, preserve why the original PASS was not a hard structural rejection, what carrier ceiling already existed, what confirmed XI evidence created the new football epoch, and the conservative burden selected.

A high market line alone must never be documented as the reason EGE or carrier reopen was created.

Use audit labels where useful:

- `STANDARD DIRECT`
- `STANDARD DECAY`
- `EGE DIRECT`
- `EGE RELATIVE DECAY`
- `NON-DECAY HOLD`
- `GOAL-EXPANSION HOLD`
- `RELATIVE-RANKING MISS`
- `RECENT-SCORE SUPPRESSION OVERWEIGHTED`

---

## 6. User-supplied XI + odds + market-history workflow

Current normal prematch execution expects the user to supply confirmed XI and the **current executable odds**.

When a user screenshot/text is the current evidence:

- treat it as the execution-price input for that assessment epoch;
- match it to the frozen PRE fixture;
- record the actual current line/odds evaluated;
- do not fabricate missing current market data;
- do not automatically search for missing confirmed XI/current executable odds unless the user explicitly requests external verification.

For every Step-2 review, including frozen PASS, Normal Chat must attempt the contextual market-history series:

`OPEN → PRE-XI → POST-XI / CURRENT PREMATCH`

Historical odds research is allowed automatically because it is a conflict/corroboration layer, not a substitute executable price.

Where available, preserve:

- opening total + Over price;
- PRE-XI total + Over price;
- POST-XI/current total + Over price;
- source/bookmaker and snapshot time;
- line delta;
- movement label (`BULLISH LINE`, `BEARISH LINE`, `BULLISH PRICE`, `BEARISH PRICE`, `STABLE`, `MIXED`);
- whether the market signal agreed or conflicted with the first-pass XI interpretation;
- how that conflict was resolved.

Recommended compact format:

`MARKET WATCH: OPEN O2.5 @1.85 → PRE-XI O2.5 @1.76 → POST-XI O2.75 @1.89 | signal=BULLISH LINE | XI conflict=resolved as ATTACKING DEPTH PRESERVED | source=...`

If unavailable, write:

`MARKET HISTORY UNAVAILABLE — ATTEMPTED — no movement signal used`

Do not compare different bookmakers as one continuous move unless the source explicitly normalizes them. Otherwise label `CROSS-BOOK — CONTEXT ONLY`.

If either required final input is missing:

`WAITING FOR USER XI/ODDS — NO OFFICIAL DECISION`

---

## 7. Current decision order

Official v0.2.54 material decisions follow:

`STRUCTURAL QUALITY → ROUTE QUALITY PROOF → CARRIER CEILING / CC+ → FAILURE-MODE RESISTANCE → TEAM GF/GA PROFILE → CHANCE QUALITY → FIRST-PASS XI → MARKET-HISTORY CONFLICT CHECK → FINAL XI / CARRIER REOPEN → GOAL BURDEN / REGIME → MCE TEST → CURRENT PRICE → LOCK / HOLD`

Two-Sided Tier A remains the primary lane. For comparable non-Tier-A cases:

`QUALITY-PROVEN TWO-SIDED > CC+ ELITE CARRIER > NOMINAL / WEAK-SECONDARY TWO-SIDED > ordinary CARRIER-LED > FRAGILE / OTHER`

Historical market movement may challenge an XI interpretation, but it cannot create structure, create EGE, or rescue a genuine PASS by itself.

For a fragile B+ with a named compression branch, `ATTACKING DEPTH PRESERVED` plus a protected line is not enough for LOCK; record `B+ PRESERVATION-ONLY HOLD` unless an independent positive gate clears.

---

## 8. Price policy in final assessment

Current user overlay:

- hard minimum decimal odds = `1.65`;
- preferred = `1.70+`;
- MCE +0.25 requires `1.75+`;
- below 1.65 = `NO BET — HOLD — PRICE TOO SHORT`;
- do not stretch the Asian-total line merely to obtain a better price;
- higher burden must be independently supported by structure + XI;
- under EGE, the reopened burden must be set before current price is evaluated.

Record the line actually selected/evaluated, not merely the bookmaker’s headline total.

Historical price/line movement is contextual evidence; the user-supplied current executable price is the final price gate.

---

## 9. Official verdict semantics

### Official v0.2.54

- affirmative final selection = **OFFICIAL LOCK**;
- HOLD/PASS = no official exposure.

A frozen PASS can become actionable only through a valid material football epoch such as the strict v0.2.52 `CARRIER REOPEN — XI CONFIRMED`; never from market movement alone.

### Shadows

Shadow selections are comparison states only. They do not enter official P/L and do not suppress the official v0.2.53 verdict.

When all three tracks are materially assessed, create/version the states so the evidence snapshot is comparable but each model remains identifiable.

---

## 10. Synchronization rule

For a material three-track comparison, all tracks should use the same underlying fixture/XI/market evidence epoch where possible.

Synchronize:

- match identity;
- assessment time;
- score/minute for live assessments;
- XI evidence;
- evaluated line and current price snapshot;
- market-history snapshot when used;
- relevant team/chance-quality evidence.

Version-specific conclusions may differ. Evidence synchronization does not mean verdict synchronization.

---

## 11. Live-state rules

Live evidence validates or invalidates the frozen prematch thesis; it does not rewrite PRE history.

Use reset/synchronization fields when score/minute/market state materially changes.

For inherited v0.2.47 halftime logic, use the existing HT fields where applicable:

- `HT Goals`;
- `HT Saturation Gate`;
- `Conversion Quality Gate`;
- `Second-Half Hazard`;
- `Remaining Goal Budget`.

For EGE, a quiet opening may corroborate a previously established high-line calibration, but an early goal must not be used to justify chasing an expanded line. Record such states as `GOAL-EXPANSION HOLD` when applicable.

Manual live overrides must be separately labelled.

---

## 12. Result/P&L boundary

Only official selections that actually became official exposure belong in official result/P&L accounting.

Do not convert:

- HOLD;
- PASS;
- shadow;
- counterfactual;
- missed-opportunity review

into official P/L.

Standard full-match Asian totals settle on 90 minutes + stoppage time unless the market explicitly includes extra time.

Historical decisions remain settled under the model version that produced them. v0.2.52 never retroactively rewrites v0.2.51 P/L.

---

## 13. Coverage vs Decision States

`Daily Coverage Ledger` = fixture coverage + frozen PRE bridge.

`Decision States` = material later assessment epochs, including market-history conflict checks, STANDARD/EGE, MCE, carrier-reopen states, official/shadow verdict evidence and audits.

Do not use a later Decision State to overwrite what the frozen Work PRE originally was.

---

## 14. v0.2.53 ranking and execution record

For every material prospective official assessment, preserve:

- home and away route states;
- combined route pair;
- evidence confidence;
- league regime and league high-burden result;
- named dominant failure mode and whether the burden survives it;
- same-window relative-rank position and reason;
- MCE validator result, including every required field when MCE is considered;
- live evidence synchronization state when a live Over is considered.

Use the v0.2.53 non-compensatory order. A failed scope, route, failure-mode, chance-quality, CC+, burden, or evidence-confidence gate cannot be repaired by later market or price evidence.

### MCE recording

The validator must hard-fail MCE outside A2 FOCUS/B+ WATCHLIST prematch eligibility, for a route pair below SUPPORTED + SUPPORTED, without a verified same-source/normalized +0.25 OPEN → post-XI prematch line move, or when any other required field is failed/unknown.

Record:

`MCE INVALID — STANDARD BURDEN OR HOLD`

Live price decay is `STANDARD DECAY`, not MCE.

### Live recording

A live official Over requires synchronized score, minute, line/odds, current chance-quality evidence, conversion-quality assessment, and remaining-goal-budget assessment.

If missing:

`LIVE CHANCE QUALITY UNAVAILABLE — HOLD`

### Coverage identity

Resolve the Decision State to one canonical AiScore fixture ID. If multiple conflicting coverage rows exist, do not choose one silently or publish a material verdict. Record:

`COVERAGE IDENTITY CONFLICT — PUBLICATION BLOCKED`


---

## 15. v0.2.54 execution-class and shadow recording

For each material final assessment preserve separately:

- `Structural Rank` and same-window position;
- supported target burden;
- actual offered line/price;
- `Execution Class`: DIRECT LOCK ELIGIBLE / QUALIFIED — WAIT FOR DECAY / STRUCTURAL HOLD / SHADOW ONLY;
- reason the execution class differs from the structural rank;
- any lower-rank exposure exception and its football reason.

Use `QUALIFIED — WAIT FOR DECAY` only when football gates clear at a recorded target burden but the offered line is higher or the target-line price is below the floor. Use `STRUCTURAL HOLD` for failed or unresolved football gates. Never collapse these states.

MCE/+0.25 and all new live/relative-decay Over entries are shadow-only under v0.2.54. Record the contemporaneous line, odds, minute/evidence epoch and later settlement in Decision States, but never write them to Website Picks or official P/L.

For completed FOCUS/WATCHLIST rows retain final score and target-burden outcome even without official exposure. These outcomes are counterfactual calibration only and must remain separate from official betting results.
