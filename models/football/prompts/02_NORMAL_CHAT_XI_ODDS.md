# 02 — Normal Chat: XI + Market-History + Odds Review

Use Normal Chat with high reasoning.

## Authority
Read `models/football/CURRENT_MODEL.md` first. It defines the active official model, active patches, time rules and load order. Never infer the version from this prompt.

Then load the stage-relevant execution files declared by `CURRENT_MODEL.md`, including the betting procedure, active official rule files, time/schedule integrity, coverage contract and Decision States contract.

## Airtable
Base ID `appWyZJjitSBATXAU`.
Daily Coverage Ledger `tblcl1UAyMqZT6Ub0`.
Decision States `tblQmUpd5WjBLQ38X`.
Website Picks `tblg3J5sbJYbzuTYD`.
Use direct IDs unless one fails.

## Input
The user normally supplies confirmed XI and **current executable Asian-total line(s)/price(s)**.

Do not automatically fetch missing confirmed XI or substitute an externally found current price unless the user explicitly asks.

## Mandatory market-history attempt — ALL Step-2 fixtures
For **every fixture the user brings to this Step 2 review**, automatically attempt a lightweight total-history check before issuing the final LOCK/HOLD/PASS verdict, including fixtures whose frozen PRE is already PASS:

`OPEN → PRE-XI → POST-XI / CURRENT PREMATCH`

Do not short-circuit the market-history step merely because frozen PRE is PASS.

Why:
- for FOCUS/WATCHLIST, history is part of XI-conflict resolution and MCE testing;
- for frozen PASS, history is still required for calibration/audit and to detect whether the market strongly disagreed with the structural read, even though market movement alone cannot resurrect a genuine PRE PASS.

Historical lookup is calibration/context, not current execution-price authority.

### Market-history completion status
Before any final verdict, set exactly one status:
- `MARKET HISTORY FOUND`;
- `MARKET HISTORY UNAVAILABLE — ATTEMPTED`;
- `MARKET HISTORY SKIPPED — USER REQUEST`.

`MARKET HISTORY NOT CHECKED` is **not** a valid final-assessment state.

If history is unavailable after a reasonable lightweight attempt, do not stall the assessment; use `MARKET HISTORY UNAVAILABLE — ATTEMPTED` and continue.

Keep this lookup lightweight and targeted. Do not turn it into broad deep research.

Preferred evidence order:
1. user-supplied same-source history;
2. same-bookmaker opening/history;
3. reputable timestamped odds-history source;
4. normalized/consensus history only when same-source history is unavailable.

Mixed-source evidence is `CROSS-BOOK — CONTEXT ONLY`. Never fabricate missing snapshots.

## Targeted read
Retrieve only the fixture's frozen PRE from Daily Coverage Ledger unless same-window reranking is required. Preserve original grade, structural type, board tier, primary/secondary routes, failure mode, XI sensitivity, frozen burden and schedule context.

Do not rebuild Work PRE from scratch.

## Mandatory market watch
Capture where available:
- opening total + Over price;
- PRE-XI total + Over price;
- POST-XI/current prematch total + Over price;
- source and snapshot time;
- line delta;
- comparable same-line price direction.

Movement labels:
- `BULLISH LINE` — total rises 0.25+;
- `BEARISH LINE` — total falls 0.25+;
- `BULLISH PRICE` — same line, Over shortens materially;
- `BEARISH PRICE` — same line, Over drifts materially;
- `STABLE`;
- `MIXED`.

## Decision sequence
Use:

`FROZEN PRE → FIRST-PASS XI → MANDATORY MARKET-HISTORY ATTEMPT → MARKET-HISTORY CONFLICT CHECK → FINAL XI → CHANCE-QUALITY HARDENING → STANDARD/EGE BURDEN → MCE SHADOW TEST IF ELIGIBLE → CURRENT PRICE → STRUCTURAL RANK + EXECUTION CLASS → LOCK/WAIT/HOLD`

First-pass XI must be football-led and market-blind.

At XI assess creators, finishers, shape, defensive absences, rotation/cohesion, bench quality, route survival and failure-mode changes.

Classify rotation as:
- `ROTATION — ATTACKING DEPTH PRESERVED`; or
- `ROTATION — COHESION / ROUTE DAMAGE`.

If both teams lose important attacking creators/finishers, or both scoring routes are materially weakened, apply `DUAL-ROUTE XI DAMAGE` from v0.2.51. In that state, protection alone cannot create an official lock.

### Frozen PRE PASS handling
A genuine frozen PRE PASS remains non-actionable unless there is a **documented material football change** that legitimately creates a new assessment epoch under the active model.

Market movement by itself cannot resurrect PASS, and MCE cannot rescue PASS.

However, even for PASS:
- complete the market-history attempt;
- record the opening→current signal if found;
- note whether the market materially agreed/disagreed with the frozen structural read;
- preserve that information for later audit/model calibration.

Do not respond `PASS` before the market-history attempt has resolved to FOUND / UNAVAILABLE-ATTEMPTED / USER-SKIPPED.

### XI/market conflict rule
If XI appears damaged but the same-source total strengthens by +0.25 or more, explicitly recheck whether the downgrade is overstated and the lineup is actually `ATTACKING DEPTH PRESERVED`.

If XI appears stronger but the total moves down materially, recheck for missing absences, tactical shape, competition incentives, weather/data faults or source mismatch.

The market does not automatically win. It triggers reinspection.

For frozen PASS, a strong bullish move is an **audit flag**, not an automatic promotion.

## v0.2.51 chance-quality hardening
For STANDARD **O3.0+** from A1/A2 TWO-SIDED, verify repeatable high-value chance support across both routes where data exists: big chances, central/box access, quality SOT, xG/xGOT or a strong data-poor substitute using scoring/conceding 2+ frequencies and credible tactical routes.

If the O3+ thesis rests mainly on names, raw goals, possession or generic attacking reputation, cap burden lower, downgrade confidence or reclassify the archetype.

## v0.2.54 MCE +0.25 shadow test
After final XI and STANDARD burden, test `SHADOW MCE +0.25 — NO OFFICIAL EXPOSURE` only if all legacy v0.2.51/v0.2.53 validator conditions clear. It is tracked for calibration but cannot create an official LOCK under v0.2.54.

Core requirements:
- A2 FOCUS or B+ WATCHLIST, structurally TWO-SIDED;
- frozen burden at least O2.5;
- final XI = `ATTACKING DEPTH PRESERVED` or stronger;
- football evidence independently supports a credible 3-goal ceiling;
- same-source/normalized OPEN → post-XI line rises at least +0.25;
- current line is only +0.25 above frozen burden;
- current Over price at higher line is at least 1.75;
- no dominant compression/suppression branch.

MCE cannot create TWO-SIDED, EGE, rescue PASS, jump more than +0.25, override DUAL-ROUTE XI DAMAGE, or override a dominant derby/first-leg/control branch. If only the higher line is offered, retain the supported lower burden as `QUALIFIED — WAIT FOR DECAY`.

## B+ compression hardening
If frozen B+ explicitly names derby control, first-leg compression, 1-0/1-1 suppression or weak secondary contribution, protection alone is insufficient. Require an additional positive gate under v0.2.51 before LOCK.

## Goal regime
Classify `STANDARD` vs `EGE` after final XI. EGE remains governed by v0.2.50 and cannot be created by market movement.

For STANDARD, use the protected-line principle unless the narrow v0.2.51 MCE rule clears.

For EGE, preserve frozen PRE burden, document post-XI EGE burden and independent reasons, then compare current price.

## v0.2.54 structural rank and execution class

After burden is fixed, preserve the same-window structural rank and assign exactly one execution class:

- `DIRECT LOCK ELIGIBLE` — actual prematch line is no higher than the supported burden, price clears the floor, and no quarantined mechanism is required;
- `QUALIFIED — WAIT FOR DECAY` — football clears at a recorded target burden, but the offered line is higher or target-line price is too short;
- `STRUCTURAL HOLD` — a football/evidence gate fails or remains materially unresolved;
- `SHADOW ONLY` — MCE/+0.25 or any live/decay Over under v0.2.54.

Price or market movement may change execution class but must not increase structural rank. Keep qualified waiting candidates visible in the active same-window comparison instead of grouping them with structural HOLD.

## Price
Apply the active current model after burden is fixed:
- hard floor 1.65;
- preferred 1.70+;
- MCE +0.25 requires 1.75+;
- never stretch merely to get a better price.

## Persistence
For material final assessments, update only later-stage coverage fields and write Decision States. Do not rewrite frozen PRE.

Persist market history compactly, e.g.:

`MARKET WATCH: OPEN O2.5 @1.85 → PRE-XI O2.5 @1.76 → POST-XI O2.75 @1.89 | signal=BULLISH LINE | source=... | status=FOUND`

If unavailable:

`MARKET WATCH: unavailable after targeted attempt | status=UNAVAILABLE-ATTEMPTED`

Add v0.2.51 tags when relevant:
- `CQ HARDENED`
- `DUAL-ROUTE XI DAMAGE`
- `SHADOW MCE +0.25 — NO OFFICIAL EXPOSURE`
- `QUALIFIED — WAIT FOR DECAY`
- `STRUCTURAL HOLD`
- `FAILURE MODE TEMPORARILY ACTIVE`
- `CARRIER VALIDATION — NOT CLEAN TWO-SIDED`

Use Website Picks only for an actual direct official final selection. Persist shadow/counterfactual states in Decision States without official P/L.

## Output
Compactly return: match, frozen PRE, structural rank, first-pass XI, **market-history completion status**, opening→current signal if found, conflict resolution, final XI, chance-quality status, regime/burden, MCE shadow status, target supported line, supplied line/price class, execution class, final action, concise reason and Airtable persistence PASS/FAIL.
