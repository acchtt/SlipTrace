# Football Cross-Chat Handoff — 2026-08-15

**Status:** Active cross-chat handoff  
**Active model:** Football v0.2.46 — AUDIT MODE  
**Canonical namespace:** `models/football/`

This handoff supersedes `CHAT_TRANSFER_HANDOFF_2026-08-14.md` for normal startup. Older handoffs remain historical context only and must not override v0.2.46.

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

## v0.2.46 correction — pre-goal pressure inflection

The Willem II vs NEC lesson is now correctly anchored **before halftime**, not primarily at halftime.

The user clarified that around 42' at 0-0, NEC had already increased pressure. The live board around that state showed approximately Over 1.75 @ 1.84. No prospective shadow verdict was issued.

Primary classification:

`LATE — PRE-GOAL PRESSURE INFLECTION NOT CONVERTED TO DECISION`

From approximately 35' to halftime, every material checkpoint must compare the recent 5-10 minute interval with the prior synchronized state and classify:

- `PRESSURE INFLECTION: YES`
- `PRESSURE INFLECTION: POSSIBLE / UNRESOLVED`
- `PRESSURE INFLECTION: NO`

A valid inflection normally needs at least two independent primary changes, including one direct-threat channel and one structural/territorial channel. xG/xGOT remain secondary.

At 0-0 or another tied score, do not wait for a future trailing-team chase condition. A one-team surge may support an:

`ATTACKER-DRIVEN PRE-GOAL OVER`

when the attacking team can plausibly fund the protected remaining-goal budget itself.

Opponent contribution must be classified as `ESSENTIAL / HELPFUL / OPTIONAL`.

When the pre-goal gates are complete, v0.2.44 verdict-first timing applies immediately. Do not wait for the first goal, halftime, or another snapshot solely for reassurance.

If the goal arrives before delivery:

`STATE-CHANGE RACE — NOT COUNTED`

then reset and reprice.

## v0.2.45 remains as post-goal fallback

The terminal-goal halftime bridge remains active, but it is now explicitly secondary.

If a goal occurs so near halftime that the normal v0.2.43 post-goal persistence window cannot honestly exist, perform the full reset and use v0.2.45 only as the post-goal fallback.

Strong pre-goal process may carry through the bridge when its evidence gates pass. A leader-driven Over may still qualify without requiring the trailer to provide the remaining goals.

The operational priority is:

1. detect and act on the pre-goal acceleration first;
2. if a terminal goal beats delivery, invalidate the old state;
3. then use the v0.2.45 halftime bridge only on the new state.

## Required late-half fields

For serious assessments from 35' to halftime, report:

- `Recent interval:`
- `Pressure inflection:` YES / POSSIBLE / NO
- `Primary acceleration channels:`
- `Attacker-driven goal route:` STRONG / MODERATE / WEAK / N/A
- `Opponent contribution:` ESSENTIAL / HELPFUL / OPTIONAL
- `Best protected total:` exact line and odds if available
- `Timing status:` ON TIME / VALID HOLD / LATE / STATE-CHANGE RACE

If `PRESSURE INFLECTION: YES` and all candidate gates clear, state the verdict before extended explanation.

## v0.2.44 timeliness layer remains active

When any stable pre-goal state already clears all applicable gates, output the verdict immediately rather than waiting for an unnecessary extra snapshot or the next goal.

If a goal, red card, awarded penalty, material VAR event, major injury, or tactical substitution cluster occurs before delivery, invalidate the pending candidate and reprice from zero.

Track timing as:

- `ON TIME — DELIVERED IN STATE`
- `VALID HOLD — GATE INCOMPLETE`
- `LATE — GATES WERE COMPLETE BUT VERDICT DELAYED`
- `STATE-CHANGE RACE — NOT COUNTED`

## v0.2.43 style layer remains mandatory

Before the first serious prematch/live recommendation, profile both teams' base style, expected matchup style, attacking routes, defensive block, transitions, chance-generation signature, lead behaviour, trailing behaviour, and confidence caveat.

After every goal, perform the strict style reset. v0.2.46 changes how quickly a **pre-goal** pressure acceleration is recognized; it does not erase post-goal discipline.

## Arm A / Arm B

### Arm A — current audit model

Apply Football v0.2.46 with the full validator, style layer, v0.2.44 timing, v0.2.45 post-goal fallback, v0.2.46 pressure-inflection logic, market-family scan, directional quarantine and best-expression comparison.

Allowed outputs:

- `SHADOW LEAN — DO NOT PLACE`
- `NO BET`
- `NO BET — HOLD`

### Arm B — early totals benchmark

Continue the v0.2.6-v0.2.9 totals philosophy with current synchronization, provider-quality, settlement, v0.2.43 style, v0.2.44 timeliness, v0.2.45 terminal-goal fallback and v0.2.46 pre-goal acceleration controls.

Allowed outputs:

- `BENCHMARK SHADOW — DO NOT PLACE`
- `BENCHMARK NO BET`

Arm B must explicitly test a protected live Over when a late-half pre-goal pressure inflection is detected. Do not wait for the first goal if the exact-line, independent-primary-channel, adjacent-line, adverse-branch and NO-BET gates already pass.

## Willem II vs NEC corrected lesson

The around-42' 0-0 state is the key process lesson. NEC's pressure was already rising before the 45+2 goal. The model should have immediately rescanned the protected totals board instead of waiting for a goal to create a Willem chase narrative.

The later 0-4 score is diagnostic only. The missed around-42' state and missed halftime state are **not** shadow wins and add no P/L.

Canonical review:

`models/football/reviews/FOOTBALL_PROCESS_REVIEW_WILLEM_NEC_2026-08-15.md`

## Competition/provider exclusion

Per explicit user instruction, **AFC Challenge/AFC Challenge League matches remain excluded from the current audit workflow because live-stat coverage is insufficient** unless the user explicitly reverses the exclusion and adequate synchronized data is available.

This is not a blanket exclusion of all AFC or Asian competitions.

## Audit integrity

- Never retrofit a rule or candidate after the result.
- A market that would have won is not a model win unless it was prospectively selected in the synchronized state.
- Genuine misses remain misses.
- Official betting cannot resume until existing audit exit criteria are met and the user explicitly approves resumption.
- `/ledger.json` remains authoritative for official accounting when ledger writes are authorized.