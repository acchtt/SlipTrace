# 02 — Normal Chat: XI + Odds / Execution

**Stage:** Step 2 in repo / user's workflow Step 3  
**Mode:** Normal Chat  
**Primary authority:** `models/football/procedures/FOOTBALL_STEP2_EXECUTION_SPEC.md`

## Preflight

Read upstream/default-branch in this order:

1. `models/football/CURRENT_MODEL.md`
2. `models/football/procedures/FOOTBALL_PRE_DECISION_SPEC.md`
3. `models/football/procedures/FOOTBALL_STEP2_EXECUTION_SPEC.md`
4. the stage-relevant active rule/procedure/persistence files required by `CURRENT_MODEL.md`

The compiled Step-2 execution spec is final operational authority wherever older Step-2 wording overlaps or conflicts.

Do not revive expired session overrides, stale handoff text, generic HMA direct-execution language, old v0.2.54 execution semantics, or B+ +0.25 direct labels that conflict with the compiler.

## Input

The user normally supplies:
- confirmed XI / lineup screenshot;
- current executable Asian-total line(s)/price(s);
- sometimes AH / 1X2 / alternate totals;
- sometimes a live/just-started screenshot.

User-supplied current odds are the price authority for that evidence epoch. Do not replace them with external prices unless explicitly asked.

## Frozen state

Retrieve the exact fixture's frozen PRE from Daily Coverage Ledger.

Prefer the persisted `FOOTBALL_PRE_DECISION_SPEC_V1` trace.

Do not rebuild PRE from scratch and do not use another match's rank to suppress this fixture.

## Mandatory execution sequence

Execute `FOOTBALL_STEP2_EXECUTION_SPEC.md` exactly:

`FROZEN PRE TRACE -> IDENTITY/STATUS -> EPOCH CLASS -> XI ROLE-MECHANISM MATRIX -> POST-XI FOOTBALL RESEARCH -> H2H/MATCHUP GATE -> CURRENT CQ/FAILURE UPDATE -> MARKET-HISTORY ATTEMPT -> FROZEN_PRE_MARKET_ALIGNMENT -> EGE/CARRIER CURRENT-EPOCH COMPILER -> CURRENT_PRE_EXECUTION_FIT -> BURDEN AUTHORITY -> B+/UPPER-TAIL GATES -> DECAY/REACHABILITY -> PRICE -> LIVE/PREMATCH ELIGIBILITY -> PROVISIONAL/FINAL VERDICT -> PERSISTENCE TRANSACTION`

## Identity / status

Near kickoff, revalidate AiScore identity/time/status as required by the time-integrity procedure.

A mismatch blocks publication:

`FIXTURE IDENTITY / HOME-AWAY / STATUS CONFLICT — HOLD`

Do not infer a live score from a lineup thumbnail/overlay alone.

## XI

Use the compiled role-mechanism matrix:

- CREATE
- FINISH
- SERVICE
- SUSTAIN
- RESIST

Classify each relevant mechanism:
- `XI MECHANISM — PRESERVED`
- `XI MECHANISM — DEGRADED`
- `XI MECHANISM — BROKEN`
- `XI MECHANISM — UNKNOWN`

Do not downgrade by number of changes alone.

## Post-XI football research — mandatory

After first-pass XI, perform a targeted fixture-specific football web-research attempt.

Record exactly one:

- `POST-XI RESEARCH = FOUND`
- `POST-XI RESEARCH = LIMITED`
- `POST-XI RESEARCH = UNAVAILABLE — ATTEMPTED`
- `POST-XI RESEARCH = SKIPPED — EXPLICIT USER WAIVER`

Market-history research is separate and does not satisfy this gate.

An ordinary prematch official lock cannot be published before this status is recorded.

## H2H / matchup history

When relevant to suppression/burden and always before O3.0+ official execution, run the compiled H2H gate:

`CURRENT MECHANISM -> TRANSFERABLE SAME-VENUE H2H -> TRANSFERABLE RECENT ALL-VENUE H2H -> LONG-RUN BACKGROUND`

Persist:
- transferability;
- H2H classification;
- current mechanism being tested;
- independent current corroboration when H2H contributes negatively.

H2H alone never creates a scoring route or HARD VETO.

## Market history

Attempt:

`OPEN -> PRE-XI -> POST-XI / CURRENT PREMATCH`

Record:
- `MARKET HISTORY FOUND`
- `MARKET HISTORY UNAVAILABLE — ATTEMPTED`
- `MARKET HISTORY SKIPPED — USER REQUEST`

Do not fabricate missing snapshots.

## Frozen-PRE market alignment

Persist the anti-circularity field:

`FROZEN_PRE_MARKET_ALIGNMENT = CLEAR / UNDERCUT / SEVERE_UNDERCUT / HIGH_MARKET_CONFLICT / UNCLEAR`

Do not later rewrite this field against market-calibrated current PRE.

## EGE / carrier / current PRE

EGE may remain a current football-regime diagnostic but **EGE alone does not authorize above-frozen direct execution**.

Then run Carrier Market Decomposition using current total + AH + 1X2 + football/XI evidence.

Classify:
- `MARKET CARRIER = ELITE`
- `MARKET CARRIER = EXTREME`
- `MARKET CARRIER = NOT CLEARED`
- `MARKET CARRIER = UNRESOLVED`

Only ELITE/EXTREME may create `MARKET-CALIBRATED CURRENT PRE`.

Persist separately:

`CURRENT_PRE_EXECUTION_FIT = CLEAR / ABOVE_CURRENT_PRE / BELOW_CURRENT_PRE_CONFLICT / UNCLEAR / NOT_APPLICABLE`

## Burden

Authority order:

1. ELITE/EXTREME market-calibrated current PRE, when cleared;
2. otherwise frozen supported burden/range, adjusted downward only for current football damage;
3. EGE current burden = diagnostic unless absorbed by #1;
4. generic HMA does not raise official burden;
5. MCE remains shadow/audit unless later explicit authority says otherwise.

## B+

At exact frozen supported burden:
- B+ may execute when compiled gates clear;
- no extra positive hardener is required.

At +0.25 above frozen burden:
- ordinary answer = WAIT / LIVE DECAY;
- PRE VERIFIED carrier alone does not override Decay-First;
- only a later ELITE/EXTREME current-PRE carrier may independently authorize that line.

## HMA

For new current decisions:

`HMA = MONITORING / AUDIT ONLY`

Do not emit new ordinary:
- `DIRECT LOCK ELIGIBLE — HIGH-MARKET ACCEPTANCE`
- `OFFICIAL LOCK — HIGH-MARKET ACCEPTANCE`
- HMA-boundary live-decay targets above supported burden.

## Upper tail

Run the compiled upper-tail gate when required.

Possible states:
- `UPPER TAIL = PROVEN`
- `UPPER TAIL = NOT PROVEN`
- `UPPER TAIL = BLOCKED BY SUPPRESSION`
- `UPPER TAIL = UNRESOLVED`
- `UPPER TAIL = NOT REQUIRED`

O3.0+ also requires the compiled H2H/suppression gate.

## Ordinary above-burden execution

For non-ELITE/non-EXTREME current-PRE lanes:

current line > supported execution burden:

`QUALIFIED — LIVE DECAY PLAN`

Target the lowest acceptable supported burden, not a generic HMA boundary.

If supported line is present but price <1.65:

`QUALIFIED — PRICE BELOW FLOOR`

## Live / just-started

First classify whether a predeclared plan or exact active match exception exists.

### Plan/exception exists

A time-sensitive first-line action may be:

`PROVISIONAL FAST VERDICT — TAKE <line> @ <price> NOW`

only when already-known plan/state/price gates clear.

Then immediately complete mandatory research. Only after that may the verdict become final and publishable.

### No plan/exception

Immediate result:

`NO OFFICIAL LIVE ENTRY — NO PREDECLARED PLAN`

Persist:

`SHADOW LIVE/DECAY — NO OFFICIAL EXPOSURE`

Do not say TAKE NOW.

A goal/card/material change voids the old quote and starts a new epoch.

## Price

- hard floor = 1.65
- preferred = 1.70+
- burden before price
- lowest valid burden first
- never stretch burden for payout

## Final states

Use only the canonical current taxonomy from the compiled spec.

Official:
- `OFFICIAL LOCK`
- `B+ PROTECTED-LINE — OFFICIAL LOCK`
- `OFFICIAL LOCK — MARKET-CALIBRATED ELITE CARRIER`
- `OFFICIAL LOCK — LIVE DECAY PLAN` from a valid predeclared plan/exception

Qualified:
- `QUALIFIED — LIVE DECAY PLAN`
- `QUALIFIED — PRICE BELOW FLOOR`

Hold/shadow:
- `STRUCTURAL HOLD`
- `MARKET UNDERCUT — RE-SCREEN REQUIRED`
- `SEVERE MARKET UNDERCUT — NO INSTANT LOCK`
- `NO BET — EXPOSURE HOLD — UPPER-TAIL INSUFFICIENT`
- `B+ PROTECTED-LINE — HOLD — NEGATIVE VETO`
- `SHADOW LIVE/DECAY — NO OFFICIAL EXPOSURE`
- `SHADOW MCE +0.25 — NO OFFICIAL EXPOSURE`
- `HMA MONITORING ONLY`

## Persistence

For every material assessment, write a current Football A Decision State using the compiled persistence contract.

For an official exposure:
1. Decision State;
2. Website Pick;
3. reconcile fixture/model/line/odds/stake/epoch/timestamps;
4. verify no duplicate active official pick.

Failure:

`PERSISTENCE SYNC FAULT — EXPOSURE STATE UNCERTAIN`

Do not claim successful publication when only one side of the transaction succeeded.

Do not backfill after the executable evidence epoch has passed.

## Output style

For a normal prematch assessment, return compactly:
- fixture;
- frozen PRE;
- XI mechanism state;
- post-XI research status;
- H2H state when material;
- current CQ/failure state;
- frozen-PRE market alignment;
- market carrier/current PRE;
- authorized execution burden;
- selected line/price;
- final verdict;
- exact blocker/why;
- persistence result for official exposure.

For live/just-started screenshots, put the immediate canonical action in the first line, then complete the same-assessment research/persistence work required by the compiled spec.
