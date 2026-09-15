# 02 — Normal Chat: XI + Market-History + Odds Review

Use Normal Chat with high reasoning.

## Authority

Read `models/football/CURRENT_MODEL.md` first. It defines the active official model, active patches, time rules and load order. Never infer the version from this prompt.

Then load the stage-relevant execution files declared by `CURRENT_MODEL.md`, including `MODEL_RULES_FOOTBALL_A.md`, the betting procedure, time/schedule integrity, coverage contract and Decision States contract.

For all new decisions after activation, persist `Model Version = Football A`.

## Airtable

Base ID `appWyZJjitSBATXAU`.
Daily Coverage Ledger `tblcl1UAyMqZT6Ub0`.
Decision States `tblQmUpd5WjBLQ38X`.
Website Picks `tblg3J5sbJYbzuTYD`.
Use direct IDs unless one fails.

## Input

The user normally supplies confirmed XI and **current executable Asian-total line(s)/price(s)**.

Do not automatically replace a user-supplied current price with an external price. Historical market research may be fetched for calibration/context.

## Mandatory market-history attempt

For every Step-2 fixture, attempt a lightweight total-history check before final action:

`OPEN → PRE-XI → POST-XI / CURRENT PREMATCH`

Set exactly one completion status:

- `MARKET HISTORY FOUND`;
- `MARKET HISTORY UNAVAILABLE — ATTEMPTED`;
- `MARKET HISTORY SKIPPED — USER REQUEST`.

If unavailable after a reasonable targeted attempt, continue. Never fabricate snapshots.

Prefer:

1. user-supplied same-source history;
2. same-bookmaker history;
3. reputable timestamped odds history;
4. normalized/consensus history only as context.

Mixed-source evidence is `CROSS-BOOK — CONTEXT ONLY`.

## Targeted frozen-state read

Retrieve the fixture's frozen PRE from Daily Coverage Ledger. Preserve:

- structural rank;
- PRE grade and board tier;
- home/away route states and route pair;
- chance-quality state;
- CC+ state;
- dominant failure mode;
- supported burden/range;
- evidence confidence;
- schedule identity.

Do not rebuild Work PRE from scratch.

When Model A same-window comparison is required, retrieve the other active higher-ranked candidates in the same practical exposure window so the priority-inversion guard can be evaluated.

## Decision sequence

Use:

`FROZEN PRE → FIRST-PASS XI → MARKET-HISTORY ATTEMPT → CONFLICT CHECK → FINAL XI → CHANCE-QUALITY HARDENING → STANDARD/EGE BURDEN → MCE/+0.25 SHADOW TESTS → CURRENT PRICE → STRUCTURAL RANK + EXECUTION CLASS → MODEL A UPPER-TAIL GATE → MODEL A PRIORITY-INVERSION GUARD → EXPOSURE DECISION`

First-pass XI is football-led and market-blind.

At XI assess creators, finishers, shape, defensive absences, rotation/cohesion, bench quality, route survival and failure-mode changes.

Classify rotation as:

- `ROTATION — ATTACKING DEPTH PRESERVED`; or
- `ROTATION — COHESION / ROUTE DAMAGE`.

If both routes are materially weakened, apply the active DUAL-ROUTE XI DAMAGE rule. Protection alone cannot rescue it.

## Market-history conflict rule

If XI appears damaged but the same-source total strengthens by +0.25 or more, explicitly recheck whether the downgrade is overstated.

If XI appears stronger but the total weakens materially, recheck for missing absences, tactical changes, incentives, weather/data faults or source mismatch.

The market triggers reinspection; it does not automatically win and cannot create structural quality.

## Chance quality / burden

For STANDARD O3.0+ A1/A2 TWO-SIDED candidates, require repeatable high-value chance support across the relevant routes where data exists. Raw goals, names or possession alone are insufficient.

Classify `STANDARD` vs `EGE` after final XI. EGE remains governed by the active v0.2.50 rules and cannot be created by market movement.

Supported burden is fixed **before** current price.

## Execution class

After burden is fixed, assign exactly one technical Execution Class:

- `DIRECT LOCK ELIGIBLE` — actual prematch line is no higher than supported burden, price clears the active floor, and no quarantined mechanism is required;
- `QUALIFIED — WAIT FOR DECAY` — football clears at a supported target burden, but offered line is higher or target-line price is below floor;
- `STRUCTURAL HOLD` — football/evidence gate fails or remains materially unresolved;
- `SHADOW ONLY` — quarantined mechanism.

For qualified waits, persist one of:

- `PRICE-ONLY WAIT — LINE ABOVE BURDEN`;
- `PRICE-ONLY WAIT — PRICE BELOW FLOOR`;
- `PRICE-ONLY WAIT — BOTH`.

Price or market movement may change Execution Class but may not increase Structural Rank.

## Football A exposure gate

**DIRECT LOCK ELIGIBLE is not an automatic official bet.**

Every DIRECT candidate must pass the exposure gate before a Website Pick is created.

### 1. A2 upper-tail gate

If an **A2** candidate is executable at the **top of its supported burden/range**, require at least one:

- `4+ TOTAL PATH — QUALITY PROVEN`;
- `TRUE CC+ PATH` with credible support for the additional goal(s);
- `ELITE TWO-SIDED PATH` with strong chance quality and failure resistance.

If none clears:

- Execution Class stays `DIRECT LOCK ELIGIBLE`;
- Exposure Decision = `NO BET — EXPOSURE HOLD`;
- persist `UPPER-TAIL INSUFFICIENT`.

Do not mislabel this as STRUCTURAL HOLD.

A clean-XI A1 PROVEN+PROVEN candidate normally clears the upper-tail exposure requirement unless a named compression/failure branch, chance-quality downgrade or burden-specific rule blocks it.

B+ receives no relaxation.

### 2. Priority-inversion guard

Before issuing an OFFICIAL LOCK, compare against higher-ranked active candidates in the same practical exposure window.

If a higher-ranked **clean-XI A1/A2 FOCUS** is still structurally qualified and is withheld **only** because its line is above supported burden or target price is below floor, do not expose a materially weaker lower-ranked candidate merely because its lower total is easier to execute.

A lower-ranked candidate can override only with a documented football-led reason, such as:

- clearly stronger upper-tail proof at the actual burden;
- materially stronger post-XI route quality;
- genuine failure-mode deterioration in the higher-ranked fixture;
- another recognized football-led model change.

Price, nominally easier line, and simple availability are not valid overrides.

If blocked:

- keep `Execution Class = DIRECT LOCK ELIGIBLE`;
- Exposure Decision = `NO BET — EXPOSURE HOLD`;
- persist `PRIORITY INVERSION GUARD`.

### 3. Exposure ordering

When multiple DIRECT candidates survive, prioritize:

`STRUCTURAL RANK → UPPER-TAIL PROOF → ROUTE QUALITY / FAILURE RESISTANCE → BURDEN PROTECTION → PRICE AS TIE-BREAKER`

Do not let market accessibility become the primary selector.

## Quarantined mechanisms

Keep active quarantines unchanged:

- qualifying A1/A2 FOCUS exact +0.25 above supported ceiling: `HIGH-SCORING +0.25 ACCEPTANCE BAND — SHADOW ONLY`;
- MCE: `SHADOW MCE +0.25 — NO OFFICIAL EXPOSURE`;
- ordinary live/relative-decay Over: `SHADOW LIVE/DECAY — NO OFFICIAL EXPOSURE`.

The +0.25 acceptance band remains shadow-only until the full release gate clears, including at least 20 valid settled predeclared observations and explicit user approval of a later model version.

B+ / CC+ remains a separate audit lane with no automatic promotion.

## Price

Apply the active model after burden is fixed:

- hard floor **1.65**;
- preferred **1.70+**;
- MCE +0.25 shadow validator requires **1.75+**;
- never stretch burden merely to get a better price.

## Persistence

For every material Football A final review, persist:

- `Model Version = Football A`;
- Structural Rank;
- Execution Class;
- supported burden;
- supplied actual line/price;
- `UPPER-TAIL = PASS / FAIL / NOT REQUIRED`;
- `PRIORITY INVERSION = CLEAR / BLOCKED / FOOTBALL OVERRIDE`;
- Exposure Decision;
- exact blocker/reason.

Without a schema migration:

- keep the existing Execution Class as technically true;
- use Airtable `Verdict = NO BET — HOLD` for `NO BET — EXPOSURE HOLD`;
- write `UPPER-TAIL INSUFFICIENT` or `PRIORITY INVERSION GUARD` into Candidate/Evidence Summary;
- create Website Picks **only** for actual `OFFICIAL LOCK` exposure.

Do not rewrite frozen PRE.

For every QUALIFIED — WAIT candidate, continue market-path logging whenever observable: target line/min price, first offered line/price, lowest pre-kick line, best target-line price, whether/when target became obtainable, first-goal-before-target state and final score.

## Output

Compactly return:

match; active model `Football A`; frozen PRE; structural rank; first-pass/final XI; market-history completion status; chance-quality state; regime; supported burden; supplied line/price; Execution Class; **upper-tail gate**; **priority-inversion state**; final Exposure Decision; concise reason; Airtable persistence PASS/FAIL.

Use exact final labels where applicable:

- `OFFICIAL LOCK`
- `NO BET — EXPOSURE HOLD — UPPER-TAIL INSUFFICIENT`
- `NO BET — EXPOSURE HOLD — PRIORITY INVERSION GUARD`
- `QUALIFIED — WAIT FOR DECAY`
- `STRUCTURAL HOLD`
- `SHADOW ONLY`
