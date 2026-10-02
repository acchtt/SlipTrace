# Football Decision States — Airtable Contract

**Status:** ACTIVE  
**Base:** `SlipTrace Football Decision Control`  
**Table:** `Decision States`  
**Official model:** Football A  
**Current execution authority:** `models/football/procedures/FOOTBALL_STEP2_EXECUTION_SPEC.md`  
**Shadow comparison models:** v0.2.47 CLEAN and v0.2.48-SHADOW

This table records material football assessment states after the frozen coverage/PRE stage. It must preserve version fidelity and must not rewrite historical PRE state.

---

## 1. Model/version rule

Every material record must identify the model version that actually produced it.

Current tracks:

- **Official:** `Football A`
- **Shadow:** `Football v0.2.47 CLEAN`
- **Shadow:** `Football v0.2.48-SHADOW`

For every new XI/odds assessment, `FOOTBALL_STEP2_EXECUTION_SPEC.md` is the final semantic authority.

Historical v0.2.49/v0.2.50/v0.2.51/v0.2.52/v0.2.53/v0.2.54/v0.2.55 Decision States retain the version that actually produced them. Do not relabel historical decisions as Football A.

Older version-numbered sections later in this contract are **historical compatibility guidance only** when they conflict with the current compiled Step-2 specification.

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
- evidence summary;
- `Current Completion Mode`;
- `Current Completion Quality`;
- `Current Continuation Quality`;
- `Current Opponent Leakage`;
- `Current Stall Risk`.

For Football C decisions after the burden-completion selector activation, these five fields preserve the Step-2 XI/research recheck. They are current-epoch fields and must not overwrite the frozen Step-1 completion fields in Daily Coverage.

Use provider/evidence-version fields when the decision depends on an external normalized evidence snapshot.

For new Football A Step-2 states, also preserve in dedicated fields where available, otherwise in `Evidence Summary`:

- frozen PRE compiler reference / frozen burden;
- XI mechanism state for each material route/carrier;
- post-XI football research status;
- H2H transferability/state + tested mechanism when material;
- CURRENT CQ / CURRENT FAILURE;
- market-history status;
- `FROZEN_PRE_MARKET_ALIGNMENT`;
- current market center, AH and 1X2;
- market carrier state;
- EGE current regime/burden when assessed;
- market-calibrated current PRE when applicable;
- `CURRENT_PRE_EXECUTION_FIT`;
- execution burden authority/source;
- upper-tail state;
- decay target/gap/reachability when waiting;
- final canonical execution state and exact blocker.

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
- when it is prematch, treat the displayed line/price as currently available and executable; do not request a second confirmation;
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

New Football A material decisions follow only:

`FROZEN PRE TRACE -> IDENTITY/STATUS -> EPOCH CLASS -> XI ROLE-MECHANISM MATRIX -> POST-XI FOOTBALL RESEARCH -> H2H/MATCHUP GATE -> CURRENT CQ/FAILURE UPDATE -> MARKET-HISTORY ATTEMPT -> FROZEN_PRE_MARKET_ALIGNMENT -> EGE/CARRIER CURRENT-EPOCH COMPILER -> CURRENT_PRE_EXECUTION_FIT -> BURDEN AUTHORITY -> B+/UPPER-TAIL GATES -> DECAY/REACHABILITY -> PRICE -> LIVE/PREMATCH ELIGIBILITY -> PROVISIONAL/FINAL VERDICT -> PERSISTENCE TRANSACTION`

Detailed authority: `FOOTBALL_STEP2_EXECUTION_SPEC.md`.

Do not use the old v0.2.54 two-sided-first ranking hierarchy, preservation-only B+ hardener, generic HMA direct lane, or MCE official execution as current decision authority.

## 8. Price policy in final assessment

Current Football A:

- hard minimum decimal odds = `1.65`;
- preferred = `1.70+`;
- burden before price;
- lowest authorized burden first;
- price as tie-breaker only;
- higher payout never compensates for higher burden;
- MCE-specific historical price thresholds do not create current official exposure.

Record the line actually selected/evaluated and the user-supplied current executable price for that evidence epoch.

## 9. Official verdict semantics

### Current Football A official states

- `OFFICIAL LOCK`
- `B+ PROTECTED-LINE — OFFICIAL LOCK`
- `OFFICIAL LOCK — MARKET-CALIBRATED ELITE CARRIER`
- `OFFICIAL LOCK — LIVE DECAY PLAN` only from a valid predeclared plan/active exact-match exception

Qualified non-exposure:
- `QUALIFIED — LIVE DECAY PLAN`
- `QUALIFIED — PRICE BELOW FLOOR`

Hold/shadow states follow the compiled specification.

For user-supplied **prematch** odds, a final OFFICIAL LOCK is published in the same assessment after all mandatory research/execution gates clear. No second "take/publish" confirmation is required.

A `PROVISIONAL FAST VERDICT` is not by itself sufficient for Website Pick publication.

A frozen PASS/current weak state can become actionable only through a documented material football/current-PRE epoch allowed by the active compiler. Market movement alone cannot resurrect PASS.

Historical shadow/versioned states keep their original labels and do not enter current official P/L.

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

Live evidence validates or invalidates the current thesis without rewriting frozen PRE history.

Before any official live exposure classify:

- `JUST-STARTED/LIVE — PREDECLARED PLAN EXISTS`;
- `JUST-STARTED/LIVE — ACTIVE MATCH-SPECIFIC EXCEPTION`;
- `JUST-STARTED/LIVE — NO PREDECLARED PLAN`.

No predeclared plan/exception:

`SHADOW LIVE/DECAY — NO OFFICIAL EXPOSURE`

A plan/exception may use a latency-first `PROVISIONAL FAST VERDICT`, followed immediately by the mandatory research attempt. Final Website Pick publication occurs only after final same-epoch clearance.

A goal, red card or material state change voids the old quote and creates a new reset/evidence epoch. Preserve old decision history; never backfill the prior quote.

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

## 15. Current Football A execution-state recording

For every new material Football A assessment preserve separately using the existing dedicated fields where available:

- `Structural Rank` (`fldSNhIWdJlVezjAo`);
- `Execution Class` (`fldZcms9JtuDejyFf`);
- `Supported Target Line` (`fldiO8CMqfNsXEElI`);
- `Target Min Odds` (`fldJaMBKCbHQEwzbY`);
- actual offered line/price;
- frozen supported burden;
- current execution burden authority;
- frozen-PRE market alignment;
- current-PRE execution fit;
- market carrier/current PRE;
- H2H/current-failure/upper-tail state when material;
- exact reason the execution state differs from frozen PRE.

Current canonical semantics come from `FOOTBALL_STEP2_EXECUTION_SPEC.md`.

Historical v0.2.54 fields such as Calibration Track/Result/P&L remain valid for historical/shadow records but do not override the current Football A execution taxonomy.

MCE remains shadow/audit for new decisions unless a future explicit active authority promotes it.

Completed FOCUS/WATCHLIST rows may retain target-burden outcomes without official exposure; these remain counterfactual calibration only and separate from official P/L.
