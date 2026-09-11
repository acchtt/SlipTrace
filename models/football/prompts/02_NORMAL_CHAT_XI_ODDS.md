# 02 — Normal Chat: XI + Market-History + Odds Review

Use Normal Chat with high reasoning.

## Authority
Read `models/football/CURRENT_MODEL.md` first. It defines the active official model, active patches, canonical time rules, and load order. Never infer the current version from this prompt.

Then load the current stage-relevant execution files declared by `CURRENT_MODEL.md`, including the betting procedure, active official rule files, time/schedule integrity, coverage contract, and Decision States contract. If an older procedure contains an older version label, `CURRENT_MODEL.md` has higher authority.

## Airtable
Base ID `appWyZJjitSBATXAU`.
Daily Coverage Ledger `tblcl1UAyMqZT6Ub0`.
Decision States `tblQmUpd5WjBLQ38X`.
Website Picks `tblg3J5sbJYbzuTYD`.
Use the direct IDs unless one fails.

## Input
The user normally supplies the confirmed XI and the **current executable Asian-total line(s)/price(s)**.

Do not automatically fetch missing confirmed XI or substitute an externally found current price for the user's executable price unless the user explicitly asks.

### Market-history exception
For a FOCUS/WATCHLIST fixture that reaches this stage, automatically attempt a lightweight historical total-market check **before the final XI/odds assessment**:

`OPEN → PRE-XI → POST-XI / CURRENT PREMATCH`

This historical lookup is research/context, not execution-price authority. It does not violate the user-supplied-current-price rule.

Preferred evidence order:
1. user-supplied history from the same bookmaker/source;
2. same-bookmaker historical/opening snapshot;
3. reputable odds-history source with clearly timestamped totals;
4. consensus/multi-book history only when a same-source series is unavailable.

Do not fabricate missing snapshots. If a usable historical series cannot be recovered quickly, label:

`MARKET HISTORY UNAVAILABLE — PROCEED WITHOUT MOVEMENT SIGNAL`

Historical odds availability must not block an otherwise valid final assessment.

## Targeted read
Identify the fixture, then retrieve only that fixture's frozen PRE from Daily Coverage Ledger. Read the fields needed to preserve the original grade, structural type, board tier, scoring routes, failure mode, XI sensitivity, frozen burden, and time/status context.

Do not read the entire day's board unless the user asks for ranking/next-best comparison or the current procedure requires same-window comparison.

Near kickoff, follow the current time/schedule integrity procedure and revalidate fixture state when required.

## Mandatory market-history watch
Capture, where available:
- opening Asian total and Over price;
- latest comparable PRE-XI total and Over price;
- latest comparable POST-XI/current prematch total and Over price;
- source/bookmaker and snapshot time for each;
- line delta from OPEN to current;
- price movement at the same line where comparable.

Compare like with like whenever possible. Do not call cross-book differences 'movement' unless the source explicitly provides a normalized market history. Label mixed-source comparisons `CROSS-BOOK — CONTEXT ONLY`.

Movement labels:
- `BULLISH LINE` — total rises by 0.25+;
- `BEARISH LINE` — total falls by 0.25+;
- `BULLISH PRICE` — same total with materially shorter Over price;
- `BEARISH PRICE` — same total with materially longer Over price;
- `STABLE` — no meaningful change;
- `MIXED` — line and price/source evidence conflict.

Price-only moves are weaker than a full quarter-line move. Small price changes are context, not a gate.

## Decision sequence
Do not rebuild Work PRE from scratch. Start from frozen PRE.

Use this order inside Normal Chat:

`FROZEN PRE → FIRST-PASS XI RERANK → MARKET-HISTORY CONFLICT CHECK → FINAL XI RERANK → GOAL BURDEN / REGIME → CURRENT EXECUTABLE PRICE → LOCK/HOLD/PASS`

The first-pass XI read must be made from football evidence, not from the market. Then use market history as a **conflict/corroboration check**.

At XI, assess creators/finishers, shape, defensive absences, rotation/cohesion, starter/bench quality, route survival, and failure-mode changes. Apply the current model's rotation interpretation rather than treating all rotation as negative.

### Market/XI conflict rule
If the first-pass XI interpretation says `COHESION / ROUTE DAMAGE` but the total market simultaneously strengthens materially — for example O2.5 → O2.75 — recheck whether the supposed downgrade is actually `ROTATION — ATTACKING DEPTH PRESERVED`.

Likewise, if the XI looks stronger but the total falls materially, recheck for missing context such as tactical shape, additional absences, competition incentives, weather/data faults, or source mismatch.

Do **not** automatically follow the market. A market conflict triggers reinspection, not automatic promotion/demotion.

### Hard boundary
Market movement may:
- corroborate or weaken confidence in an already-supported burden;
- challenge an XI downgrade/upgrade interpretation;
- justify HOLD when a sharp unexplained bearish move conflicts with the model;
- help identify whether rotation is being priced as real route damage.

Market movement may **not**:
- rewrite frozen PRE;
- create a stronger structural grade;
- create a TWO-SIDED route that football evidence does not support;
- create EGE by itself;
- raise the supported goal burden above what structure + XI independently justify;
- justify moving to a higher total merely because the price looks attractive.

After the conflict check, finalize the XI rerank.

Then classify whatever goal-burden/regime system the current official model declares. For any EGE/high-environment regime currently active, preserve the frozen PRE burden, document the new supported post-XI burden, state the independent structural/team/XI reasons, evaluate the failure mode, and only then compare the supplied current market line/price. A high market line or bullish move by itself cannot create the regime.

For STANDARD/normal states, keep the protected-line principle. Never move to a higher total merely to improve price.

Apply the current price policy from `CURRENT_MODEL.md` only after the supported burden/regime is fixed.

Run official and shadow comparisons only to the extent the current model/procedure requires for a material final assessment, keeping each track version-faithful.

## Persistence
For a material final assessment, update only the later-stage coverage status fields that belong there and write the current Decision State(s) according to the active Decision States contract. Do not rewrite frozen PRE history.

Persist the market-history comparison in `Evidence Summary` / `Fail Reasons` / coverage notes using a compact format such as:

`MARKET WATCH: OPEN O2.5 @1.85 → PRE-XI O2.5 @1.76 → POST-XI O2.75 @1.89 | signal=BULLISH LINE | source=...`

If history is unavailable, record that fact rather than inventing values.

Use Website Picks only when an actual official final selection needs to be persisted under the current workflow. Do not touch it for simple waiting states.

## Output
Compactly return: match, frozen PRE, first-pass XI read, market-history signal, any XI/market conflict resolution, final XI rerank, current goal regime/burden, best supported supplied line, price class, final action, concise reason, and Airtable persistence PASS/FAIL.