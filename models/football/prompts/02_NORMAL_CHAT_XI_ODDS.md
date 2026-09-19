# 02 — Normal Chat: XI + Market-History + Odds Review

Use Normal Chat with high reasoning.

## Authority

Read `models/football/CURRENT_MODEL.md` first. It defines the active official model, active patches, time rules and load order. Never infer the version from this prompt.

Then load the stage-relevant execution files declared by `CURRENT_MODEL.md`, including `MODEL_RULES_FOOTBALL_AB_MARKET_ALIGNMENT.md`, `MODEL_RULES_FOOTBALL_A.md`, `MODEL_RULES_FOOTBALL_A_LIVE_DECAY.md`, `MODEL_RULES_FOOTBALL_A_HIGH_MARKET_ACCEPTANCE.md`, `MODEL_RULES_FOOTBALL_A_NO_CROSS_MATCH_EXPOSURE_SUPPRESSION.md`, `MODEL_RULES_FOOTBALL_A_AUTO_PUBLISH_USER_PREMATCH_ODDS.md`, the betting procedure, time/schedule integrity, coverage contract and Decision States contract.

For decisions inside an active temporary-session window declared by `CURRENT_MODEL.md`, load and apply the referenced session override before final exposure selection. During 2026-09-19/20 this includes the temporary burden-specific prematch upper-tail rule: O2.5 may use a quality-proven 3+ path; O2.75 may use a robust 3+ path plus non-trivial fourth-goal support; O3.0+ retains the permanent 4+ standard. A2 WATCHLIST may use this temporary O2.5/O2.75 exposure relaxation without being structurally promoted; B+/B/PASS do not.

For all new official Model A decisions after activation, persist `Model Version = Football A`.

**The market-alignment patch applies to both Football A and Model B. HMA remains Football A-only. Do not apply HMA to Model B or any shadow comparison track.**

## Airtable

Base ID `appWyZJjitSBATXAU`.
Daily Coverage Ledger `tblcl1UAyMqZT6Ub0`.
Decision States `tblQmUpd5WjBLQ38X`.
Website Picks `tblg3J5sbJYbzuTYD`.
Use direct IDs unless one fails.

## Input

The user normally supplies confirmed XI and **current executable Asian-total line(s)/price(s)**. Any user-supplied prematch odds screenshot/text is treated as currently available and executable for that assessment epoch; do not ask for a second confirmation that the line/price is still available.

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

Do not retrieve higher-ranked matches for exposure suppression. Structural Rank remains useful for board context only; the active no-cross-match patch requires each fixture to be decided independently.

## Decision sequence

Use:

`FROZEN PRE → FIRST-PASS XI → MARKET-HISTORY ATTEMPT → CONFLICT CHECK → FINAL XI → CHANCE-QUALITY HARDENING → STANDARD/EGE BURDEN → CURRENT MARKET CENTER + LINE/PRICE BOARD → SHARED A/B MARKET-ALIGNMENT GATE → FOOTBALL A HMA OR MODEL B PARTICIPATION TEST → EXECUTION PATH → MODEL-SPECIFIC EXPOSURE GATE → EXPOSURE DECISION`

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

## Shared A/B market-alignment gate

This gate is mandatory **before any instant/direct lock or Model B direct participation decision**.

### Determine the market center

Use the current main Asian total / line nearest balanced Over-Under pricing as the **market center**. Adjacent alternate totals may confirm the distribution, but do not cherry-pick the lowest alternate line and call it value.

Persist the market center and compare it with the frozen supported burden/range.

### MARKET UNDERCUT — RE-SCREEN REQUIRED

If the market center is `0.25+` below the lower edge of the frozen supported range, or `0.25+` below a single-point frozen burden:

`MARKET UNDERCUT — RE-SCREEN REQUIRED — NO INSTANT LOCK`

Re-screen for attacking absences, tactical suppression, competition incentives, opponent resistance, stale/misleading goal evidence, source/time mismatch, lineup quality and any other football-led explanation for the lower market.

A lower total is mechanically safer but is **not automatically value**.

### SEVERE MARKET UNDERCUT

If the market center is `0.50+` below the frozen lower edge / single burden:

`SEVERE MARKET UNDERCUT — NO INSTANT LOCK`

A direct decision can be restored only with a specific football-led explanation plus independent corroboration. Otherwise HOLD.

### HIGH-MARKET CONFLICT — MANDATORY RE-SCREEN

If a B/PASS, unsupported, or materially lower-ranked fixture carries a market center `0.50+` above the model's implied burden, or is among the slate's clearly highest total environments, do not silently retain an ordinary PASS.

Trigger:

`HIGH-MARKET CONFLICT — MANDATORY RE-SCREEN`

Recheck carrier depth, class-gap/cross-league context, competition volatility, lineup quality, misleading suppression from a small recent-score sample, and two-sided chance quality.

The market may force reinspection but cannot create structure by itself.

### Protected-line integrity

Keep these concepts separate:

- **best protected line** = lowest acceptable burden;
- **best price** = highest decimal payout;
- **best execution** = strongest combination after football + market-alignment + model-specific gates.

Example: `O2.0 @1.69` is more protected than `O2.25 @2.01`. O2.25 has a better price but is a **higher-price / higher-burden alternative**, not a better line.

After all gates clear, line-selection order is:

`LOWEST ACCEPTABLE BURDEN → PRICE FLOOR → PRICE AS TIE-BREAKER`

## Chance quality / burden

For STANDARD O3.0+ A1/A2 TWO-SIDED candidates, require repeatable high-value chance support across the relevant routes where data exists. Raw goals, names or possession alone are insufficient.

Supported burden is fixed **before** current price.

**Do not rewrite the structural ceiling upward or downward merely after seeing the market. Market disagreement triggers re-screening; it does not rewrite frozen PRE. HMA is an execution overlay only.**

## Football A High-Market Acceptance test

Run HMA **after market alignment/re-screening** and before assigning a live-decay plan when the actual market is above the frozen structural ceiling.

### A1 FOCUS

- up to `+0.25` above frozen ceiling under normal clean A1 integrity;
- up to `+0.50` only with a strong upper-tail hardener: `4+ TOTAL PATH — QUALITY PROVEN`, `ELITE TWO-SIDED PATH`, or TRUE CC+/equivalent carrier support.

### A2 FOCUS

- up to `+0.25` only when the A2 upper-tail gate clears at the actual offered burden;
- up to `+0.50` only with exceptional TRUE CC+ / repeatable 4+ / elite two-sided proof.

### No HMA extension

No automatic HMA extension for:

- A2 WATCHLIST;
- B+ WATCHLIST;
- PASS / unresolved;
- fragile A2 cases capped to WATCHLIST.

A line `+0.75` or more above frozen ceiling is outside immediate HMA.

If HMA passes, persist the structural ceiling separately from the actual HMA line.

## Model B participation test

When Model B is explicitly run side-by-side, preserve its existing participation behavior and +0.25 allowance where otherwise valid.

However, **Model B must clear the shared A/B market-alignment gate first**.

A bearish market undercut cannot be treated as free value or as an automatic reason for direct participation.

## Execution path

After burden is fixed, market alignment is resolved, and the relevant model-specific HMA/participation test is complete, assign the technical execution path.

### DIRECT LOCK ELIGIBLE

Use only when:

- football/XI structure remains valid;
- `MARKET ALIGNMENT = CLEAR` or `MARKET UNDERCUT OVERRIDE — FOOTBALL EXPLAINED`;
- the selected prematch line is no higher than supported burden;
- price clears the active floor;
- no quarantined mechanism is required.

**The old shortcut `line <= supported burden + price floor = direct` is invalid.**

### DIRECT LOCK ELIGIBLE — HIGH-MARKET ACCEPTANCE

Use when:

- the match is a qualifying Football A A1/A2 FOCUS case;
- market-alignment / high-market re-screen is complete;
- the offered line is inside its permitted HMA band;
- price clears the active floor;
- confirmed XI remains sufficiently intact;
- required upper-tail hardener clears;
- cross-match / same-window priority inversion is not an exposure blocker under the active patch.

If exposure is approved:

`OFFICIAL LOCK — HIGH-MARKET ACCEPTANCE`

Do not wait for the raw structural line merely because the HMA line is higher.

### QUALIFIED — EARLY SAME-LINE PRICE PLAN

Use when the line is already inside a valid HMA band but price is below the hard floor.

Freeze before kickoff:

- HMA line;
- minimum acceptable price;
- frozen structural ceiling;
- HMA excess burden (`+0.25` or `+0.50`);
- upper-tail hardener;
- cancellation triggers.

During approximately `0'–12'` at `0-0`, the frozen PRE + XI remain primary and live stats are veto/context rather than a required promotion signal. If the **same HMA line** clears the floor with no material state damage, execute promptly.

A goal, red card, major attacking injury, tactical collapse or route damage ends the simple trigger and requires a fresh state-integrity review. Do not chase a goal-driven line expansion.

### QUALIFIED — LIVE DECAY PLAN

Use when football/XI/evidence clears but the **prematch line remains outside the permitted HMA band**.

Do **not** automatically wait all the way back to the raw structural ceiling.

Predeclare the **nearest independently qualified HMA boundary** as the live-decay target when HMA rules allow one.

Examples:

- strong A1 with ceiling O3.0 and valid +0.50 hardener: O3.75 market may target O3.5;
- exceptional A2 FOCUS/TRUE CC+ with ceiling O3.0: O3.75 market may target O3.5;
- ordinary A2 FOCUS with ceiling O3.0: O3.75 market may target no higher than O3.25.

Before kickoff persist:

- target line;
- whether target is raw structural burden or HMA boundary;
- minimum price;
- current prematch line/price;
- cancellation triggers / dominant failure mode;
- `Execution Plan = LIVE DECAY`.

### QUALIFIED — PRICE BELOW FLOOR

Use when the line is already at supported burden but its price is below the hard floor.

A same-line prematch price improvement can still make it directly executable, subject to market alignment still being clear.

### STRUCTURAL HOLD

Use only when football/evidence fails or remains materially unresolved.

### SHADOW ONLY

Use for quarantined mechanisms not promoted by the Football A-only HMA patch.

Price or market movement may change execution state but may not increase Structural Rank.

## Football A exposure gate

**DIRECT LOCK ELIGIBLE is not an automatic official bet.**

### A2 upper-tail gate

If an A2 candidate is executable at the top of its supported burden/range **or above the structural ceiling through HMA**, require at least one:

- `4+ TOTAL PATH — QUALITY PROVEN`;
- `TRUE CC+ PATH` with credible additional-goal support;
- `ELITE TWO-SIDED PATH` with strong chance quality and failure resistance.

If none clears:

- Execution Class stays technically direct where applicable;
- Exposure Decision = `NO BET — EXPOSURE HOLD`;
- persist `UPPER-TAIL INSUFFICIENT`.

### Cross-match exposure suppression removed

The active Football A patch removes the old same-window / priority-inversion exposure blocker.

Do not suppress an otherwise valid candidate because another match is higher-ranked, waiting, executable, or already exposed in the same window.

Evaluate each fixture independently after its own structural, XI, market-alignment, burden, upper-tail and price gates.

For compatibility, persist:

`PRIORITY INVERSION = NOT APPLICABLE — PATCH REMOVED`

Exposure order within a fixture:

`STRUCTURAL VALIDITY → MARKET ALIGNMENT → UPPER-TAIL / ROUTE PROOF → BURDEN PROTECTION → PRICE FLOOR → EXPOSURE DECISION`

## Predeclared live-decay execution

A fixture with a frozen `QUALIFIED — LIVE DECAY PLAN` may become official after kickoff.

At each user-supplied live line/price, recheck:

1. plan existed before kickoff;
2. live line is at or below the predeclared target, which may be a valid HMA boundary;
3. price clears the floor;
4. score/time state has not materially invalidated the original thesis;
5. no red card, major injury, tactical collapse or route damage;
6. the target was reached by ordinary clock decay rather than a completely new match thesis;
7. HMA/upper-tail and all remaining fixture-specific exposure gates clear at the actual live burden.

A first goal does **not automatically cancel** the plan. It triggers a state-integrity recheck.

If all clear:

`DIRECT LOCK ELIGIBLE — PREDECLARED LIVE DECAY`

then, after exposure approval:

`OFFICIAL LOCK — LIVE DECAY PLAN`

Create the Website Pick only at the moment of approval. Never backfill after the market moves or another goal occurs.

## Opportunistic live quarantine

If there was **no predeclared HMA same-line plan or live-decay plan before kickoff**, an attractive live Over remains:

`SHADOW LIVE/DECAY — NO OFFICIAL EXPOSURE`

unless the user grants a separate match-specific exception.

`PREDECLARED LIVE DECAY != OPPORTUNISTIC LIVE BET`

## Other quarantined mechanisms

Keep quarantined:

- generic/historical +0.25 acceptance cases that **do not satisfy the Football A HMA conditions**: `HIGH-SCORING +0.25 ACCEPTANCE BAND — SHADOW ONLY`;
- MCE outside a valid HMA case: `SHADOW MCE +0.25 — NO OFFICIAL EXPOSURE`.

The HMA patch is **not** a blanket release of the legacy +0.25 shadow sample.

B+ / CC+ remains a separate audit lane with no automatic HMA promotion unless the fixture is actually A2 FOCUS under the active structural rules.

## Price

- hard floor **1.65**;
- preferred **1.70+**;
- never stretch burden merely to get a better price;
- never describe a higher total as a better line merely because its odds are higher;
- after structure/XI/market alignment clear, prefer the lowest acceptable burden that clears the floor, then use price as a tie-breaker.

Price cannot create HMA eligibility, market alignment, upper-tail proof or Model B participation eligibility.

## Persistence

For every material Football A review, and every side-by-side Model B review, persist when observable:

- model / track;
- Structural Rank;
- supported burden / frozen structural ceiling;
- current market center;
- market-center delta vs frozen lower edge / burden;
- `MARKET ALIGNMENT = CLEAR / UNDERCUT / SEVERE UNDERCUT / HIGH-MARKET CONFLICT / UNCLEAR`;
- re-screen result and `MARKET UNDERCUT OVERRIDE = NONE / FOOTBALL EXPLAINED`;
- selected protected line;
- higher-price / higher-burden alternative(s) where relevant;
- supplied line/price;
- HMA excess burden for Football A: `+0.25 / +0.50 / OUTSIDE BAND / N/A`;
- HMA eligibility and hardener where relevant;
- Execution Class / Plan;
- `UPPER-TAIL = PASS / FAIL / NOT REQUIRED` where applicable;
- `PRIORITY INVERSION = NOT APPLICABLE — PATCH REMOVED` for new decisions;
- Exposure Decision;
- exact blocker/reason.

For every `QUALIFIED — EARLY SAME-LINE PRICE PLAN`, additionally log whenever observable:

- accepted HMA line;
- minimum price;
- first same-line floor-clear timestamp;
- score/minute at trigger;
- `STATE INTEGRITY = CLEAR / DAMAGED / NEW THESIS`;
- final execution decision.

For every `QUALIFIED — LIVE DECAY PLAN`, additionally log whenever observable:

- prematch offered line/price;
- target line/minimum price;
- whether target is raw structural burden or HMA boundary;
- first target-line timestamp;
- score and minute when target first appears;
- target price;
- `STATE INTEGRITY = CLEAR / DAMAGED / NEW THESIS`;
- final live exposure decision.

Do not rewrite frozen PRE.

## Output

Compactly return:

match; model/track; frozen PRE; structural rank; first-pass/final XI; market-history completion status; chance-quality state; supported burden/structural ceiling; **market center + delta + alignment state**; supplied line/price; protected-line hierarchy; HMA/Model-B participation eligibility; Execution Class / Plan; upper-tail gate; cross-match suppression state (`NOT APPLICABLE — PATCH REMOVED`); state-integrity result when live; final Exposure Decision; concise reason; Airtable persistence PASS/FAIL.

## AUTO-PUBLISH RULE

For the prematch XI/odds workflow, if all gates clear and no exposure blocker remains, do not stop at `DIRECT LOCK ELIGIBLE`. Finalize the Exposure Decision as `OFFICIAL LOCK` and immediately create/update the Website Picks record using the user-supplied line/price, default 1u unless the user specified otherwise.

Do not ask for "take it", "publish it", "still available", or any second confirmation. The user's prematch odds submission is the availability authority for that evidence epoch.

Do not retroactively backfill after kickoff.

Use exact final labels where applicable:

- `OFFICIAL LOCK`
- `OFFICIAL LOCK — HIGH-MARKET ACCEPTANCE`
- `OFFICIAL LOCK — LIVE DECAY PLAN`
- `MARKET UNDERCUT — RE-SCREEN REQUIRED`
- `SEVERE MARKET UNDERCUT — NO INSTANT LOCK`
- `MARKET UNDERCUT OVERRIDE — FOOTBALL EXPLAINED`
- `HIGH-MARKET CONFLICT — MANDATORY RE-SCREEN`
- `NO BET — EXPOSURE HOLD — UPPER-TAIL INSUFFICIENT`
- `QUALIFIED — EARLY SAME-LINE PRICE PLAN`
- `QUALIFIED — LIVE DECAY PLAN`
- `QUALIFIED — PRICE BELOW FLOOR`
- `STRUCTURAL HOLD`
- `SHADOW ONLY`