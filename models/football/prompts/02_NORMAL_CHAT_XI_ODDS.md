# 02 — Normal Chat: XI + Market-History + Odds Review

Use Normal Chat with high reasoning.

## Authority

Read `models/football/CURRENT_MODEL.md` first. It defines the active official model, active patches, time rules and load order. Never infer the version from this prompt.

Then load the stage-relevant execution files declared by `CURRENT_MODEL.md`, including `MODEL_RULES_FOOTBALL_A.md`, `MODEL_RULES_FOOTBALL_A_LIVE_DECAY.md`, the betting procedure, time/schedule integrity, coverage contract and Decision States contract.

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

## Targeted frozen-state read

Retrieve the fixture's frozen PRE from Daily Coverage Ledger. Preserve structural rank, PRE grade/tier, route pair, chance-quality state, CC+ state, dominant failure mode, supported burden/range, evidence confidence and schedule identity.

Do not rebuild Work PRE from scratch.

When Model A same-window comparison is required, retrieve higher-ranked active candidates in the same practical exposure window for the priority-inversion guard.

## Decision sequence

Use:

`FROZEN PRE → FIRST-PASS XI → MARKET-HISTORY ATTEMPT → CONFLICT CHECK → FINAL XI → CHANCE-QUALITY HARDENING → STANDARD/EGE BURDEN → MCE/+0.25 SHADOW TESTS → CURRENT PREMATCH PRICE → EXECUTION PATH → MODEL A UPPER-TAIL GATE → MODEL A PRIORITY-INVERSION GUARD → EXPOSURE DECISION`

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

Supported burden is fixed **before** current price.

## Execution path

After burden is fixed, assign the technical execution path.

### DIRECT LOCK ELIGIBLE

Use when the actual prematch line is no higher than supported burden, price clears the active floor, and no quarantined mechanism is required.

### QUALIFIED — LIVE DECAY PLAN

Use when football/XI/evidence clears at a supported target burden but the **prematch line is above that burden**.

This replaces the old assumption that the total will conveniently drop by 0.25 before kickoff.

Do **not** plan around prematch line decay. Prematch movement may still be accepted if the user supplies it, but it is not the expected route.

Before kickoff persist:

- target supported line;
- minimum price;
- current prematch line/price;
- cancellation triggers / dominant failure mode;
- `Execution Plan = LIVE DECAY`.

### QUALIFIED — PRICE BELOW FLOOR

Use when the line is already at supported burden but its price is below the hard floor.

A same-line prematch price improvement can still make it directly executable.

### STRUCTURAL HOLD

Use only when football/evidence fails or remains materially unresolved.

### SHADOW ONLY

Use for quarantined mechanisms.

Price or market movement may change execution state but may not increase Structural Rank.

## Football A exposure gate

**DIRECT LOCK ELIGIBLE is not an automatic official bet.**

### A2 upper-tail gate

If an A2 candidate is executable at the top of its supported burden/range, require at least one:

- `4+ TOTAL PATH — QUALITY PROVEN`;
- `TRUE CC+ PATH` with credible additional-goal support;
- `ELITE TWO-SIDED PATH` with strong chance quality and failure resistance.

If none clears:

- Execution Class stays `DIRECT LOCK ELIGIBLE`;
- Exposure Decision = `NO BET — EXPOSURE HOLD`;
- persist `UPPER-TAIL INSUFFICIENT`.

### Priority-inversion guard

Before an OFFICIAL LOCK, compare against higher-ranked active candidates in the same practical exposure window.

Do not expose a materially weaker lower-ranked candidate merely because its lower total is easier to execute when a higher-ranked clean-XI A1/A2 FOCUS remains structurally qualified and is withheld only by line/price.

A lower-ranked override requires a documented football-led reason.

Exposure order:

`STRUCTURAL RANK → UPPER-TAIL PROOF → ROUTE QUALITY / FAILURE RESISTANCE → BURDEN PROTECTION → PRICE AS TIE-BREAKER`

## Predeclared live-decay execution

A fixture with a frozen `QUALIFIED — LIVE DECAY PLAN` may become official after kickoff.

At each user-supplied live line/price, recheck:

1. plan existed before kickoff;
2. live line is at or below target supported burden;
3. price clears the floor;
4. score/time state has not materially invalidated the original thesis;
5. no red card, major injury, tactical collapse or route damage;
6. the target was reached by ordinary clock decay rather than a completely new match thesis;
7. upper-tail and priority-inversion gates clear at the actual live burden.

A first goal does **not automatically cancel** the plan. It triggers a state-integrity recheck.

If all clear:

`DIRECT LOCK ELIGIBLE — PREDECLARED LIVE DECAY`

then, after exposure approval:

`OFFICIAL LOCK — LIVE DECAY PLAN`

Create the Website Pick only at the moment of approval. Never backfill after the market moves or another goal occurs.

## Opportunistic live quarantine

If there was **no predeclared live-decay plan before kickoff**, an attractive live Over remains:

`SHADOW LIVE/DECAY — NO OFFICIAL EXPOSURE`

unless the user grants a separate match-specific exception.

`PREDECLARED LIVE DECAY != OPPORTUNISTIC LIVE BET`

## Other quarantined mechanisms

Keep unchanged:

- qualifying A1/A2 FOCUS exact +0.25 above supported ceiling: `HIGH-SCORING +0.25 ACCEPTANCE BAND — SHADOW ONLY`;
- MCE: `SHADOW MCE +0.25 — NO OFFICIAL EXPOSURE`.

B+ / CC+ remains a separate audit lane with no automatic promotion.

## Price

- hard floor **1.65**;
- preferred **1.70+**;
- MCE +0.25 shadow validator **1.75+**;
- never stretch burden merely to get a better price.

## Persistence

For every material Football A review persist:

- `Model Version = Football A`;
- Structural Rank;
- supported burden;
- supplied line/price;
- Execution Class / Plan;
- `UPPER-TAIL = PASS / FAIL / NOT REQUIRED`;
- `PRIORITY INVERSION = CLEAR / BLOCKED / FOOTBALL OVERRIDE`;
- Exposure Decision;
- exact blocker/reason.

For every `QUALIFIED — LIVE DECAY PLAN`, additionally log whenever observable:

- prematch offered line/price;
- target line/minimum price;
- first target-line timestamp;
- score and minute when target first appears;
- target price;
- `STATE INTEGRITY = CLEAR / DAMAGED / NEW THESIS`;
- final live exposure decision.

Do not rewrite frozen PRE.

## Output

Compactly return:

match; active model `Football A`; frozen PRE; structural rank; first-pass/final XI; market-history completion status; chance-quality state; supported burden; supplied line/price; Execution Class / Plan; upper-tail gate; priority-inversion state; state-integrity result when live; final Exposure Decision; concise reason; Airtable persistence PASS/FAIL.

Use exact final labels where applicable:

- `OFFICIAL LOCK`
- `OFFICIAL LOCK — LIVE DECAY PLAN`
- `NO BET — EXPOSURE HOLD — UPPER-TAIL INSUFFICIENT`
- `NO BET — EXPOSURE HOLD — PRIORITY INVERSION GUARD`
- `QUALIFIED — LIVE DECAY PLAN`
- `QUALIFIED — PRICE BELOW FLOOR`
- `STRUCTURAL HOLD`
- `SHADOW ONLY`
