# Football Cross-Chat Handoff — 2026-08-14

**Status:** Active cross-chat handoff  
**Active model:** Football v0.2.44 — AUDIT MODE  
**Canonical namespace:** `models/football/`

This handoff supersedes `CHAT_TRANSFER_HANDOFF_2026-08-12.md` for normal startup. The 2026-08-12 handoff remains historical context only where a prior sample needs reconstruction.

## Startup state

- Official football betting remains **PAUSED**.
- Execution mode remains **SHADOW CALIBRATION ONLY**.
- Ledger writes remain **ON HOLD until explicit user approval**.
- 1u = 1,000,000 VND.
- Minimum odds reference remains 1.70.
- Normal current audit small-test convention remains 0.125u when a simulated shadow stake is needed and no newer rule supersedes it.
- Directional AH/DNB/ML markets remain quarantined from official promotion.
- xG/xGOT remain secondary only and may be discarded if provider quality is unreliable.
- Exact score/minute/line/odds/settlement synchronization remains mandatory.

## v0.2.44 timeliness change

The current model must not delay an already-qualified **pre-goal** total candidate merely to obtain another confirmation snapshot or wait for the next goal.

When the current synchronized state is stable and all applicable gates are complete, output the verdict first, then the reasoning.

The v0.2.43 two-observation post-goal persistence requirement applies only **after a goal or other material state reset**. It does not create a generic confirmation tax for stable pre-goal states.

If a goal/red/penalty/VAR/tactical cluster occurs before delivery, invalidate the pending candidate and record:

`NOT COUNTED — STATE CHANGED BEFORE DELIVERY`

Then reset and reprice from zero. Do not backfill the old market after the outcome.

### Process example retained

Portland Timbers vs Club Tijuana, around 61' at 1-1, showed Over 3 @ 1.96 while Portland had sustained forward pressure and Tijuana retained an independent scoring route. The model delayed; the state changed with Portland's next goal. Later 3-1 confirmed the timing cost but the missed Over 3 is **not** a shadow win because no prospective verdict was delivered in time.

Use the case only as a timeliness/process lesson.

## v0.2.43 style layer remains mandatory

Before the first serious prematch/live recommendation, profile both teams' base style, expected matchup style, attacking routes, defensive block, transitions, chance-generation signature, lead behaviour, trailing behaviour, and confidence caveat.

After every goal, perform the strict style reset and report:

- `Prematch style expectation:`
- `Leader post-goal behaviour:`
- `Trailer post-goal behaviour:`
- `Style deviation:`
- `Post-goal persistence:`
- `Market implication:`

Normally require two comparable post-goal observations, or one observation plus strong event-level evidence over a meaningful interval, before a new post-goal candidate.

## Arm A / Arm B

### Arm A — current audit model

Apply Football v0.2.44 with the full validator, style layer, market-family scan, directional quarantine and best-expression comparison.

Allowed outputs:

- `SHADOW LEAN — DO NOT PLACE`
- `NO BET`
- `NO BET — HOLD`

### Arm B — early-totals benchmark

Continue the v0.2.6-v0.2.9 totals philosophy with modern synchronization, provider-quality, settlement, style and v0.2.44 timeliness controls.

Allowed outputs:

- `BENCHMARK SHADOW — DO NOT PLACE`
- `BENCHMARK NO BET`

Arm B should decide immediately in a stable pre-goal state once its exact-line, two-primary-channel, adjacent-line, adverse-branch and NO-BET-comparator gates are complete. Do not wait for the next goal to validate a total thesis that is already complete.

## Live response priority

At every screenshot/checkpoint:

1. confirm exact score and clock;
2. detect any material event since prior snapshot;
3. if reset is unresolved, HOLD;
4. otherwise evaluate forward evidence and the market board immediately;
5. if gates are complete, state the verdict before extended explanation;
6. if the state changes while deciding, invalidate and reset.

Track timing outcome as:

- `ON TIME — DELIVERED IN STATE`
- `VALID HOLD — GATE INCOMPLETE`
- `LATE — GATES WERE COMPLETE BUT VERDICT DELAYED`
- `STATE-CHANGE RACE — NOT COUNTED`

## Competition/provider exclusion

Per explicit user instruction, **discard AFC Challenge/AFC Challenge League matches from the audit workflow because live-stat coverage is insufficient**. Do not use them for current shadow calibration unless the user explicitly reverses this exclusion and adequate synchronized live data is available.

This exclusion does not automatically apply to all AFC or Asian competitions; evaluate provider quality separately for other competitions.

## Audit integrity

- Never retrofit a rule or candidate after the result.
- A market that would have won is not a model win unless it was prospectively selected in the synchronized state.
- Genuine misses remain misses.
- Official betting cannot resume until the existing audit exit criteria are met and the user explicitly approves resumption.
- `/ledger.json` remains authoritative for official accounting when ledger writes are authorized.