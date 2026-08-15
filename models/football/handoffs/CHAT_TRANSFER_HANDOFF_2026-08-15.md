# Football Cross-Chat Handoff — 2026-08-15

**Status:** Active cross-chat handoff  
**Active model:** Football v0.2.45 — AUDIT MODE  
**Canonical namespace:** `models/football/`

This handoff supersedes `CHAT_TRANSFER_HANDOFF_2026-08-14.md` for normal startup. Older handoffs remain historical context only and must not override v0.2.45.

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

## v0.2.45 terminal-goal / leader-driven Over correction

A late first-half goal must not create an impossible confirmation requirement.

When a goal occurs so near halftime that the normal v0.2.43 two-observation post-goal persistence window cannot honestly be completed, label:

`POST-GOAL OBSERVATION WINDOW UNAVAILABLE — HALFTIME BRIDGE`

The goal still triggers a full reset, but strong pre-goal process may carry into the halftime total assessment when the v0.2.45 bridge gates pass.

For a terminal-goal halftime assessment, report:

- `Prematch style expectation:`
- `Pre-goal process:`
- `Terminal-goal bridge:` PASS / FAIL / N/A
- `Leader continuation route:` STRONG / MODERATE / WEAK
- `Trailer role:` ESSENTIAL / HELPFUL / OPTIONAL
- `Remaining-goal budget:` exact settlement requirement
- `Halftime tactical-change risk:` LOW / MODERATE / HIGH / UNRESOLVED
- `Market implication:`

### Leader-driven Over principle

A live Over does not automatically require both teams to have strong scoring routes.

If the leader has a credible route to producing the remaining goal budget itself, the trailer's chase is a modifier rather than a universal gate.

For a leader-driven Over with a weak trailer route, require at least three independent primary continuation channels, including a direct chance/box-production channel and a separate structural/territorial channel. The goal itself cannot be counted as one of the channels. xG/xGOT remain secondary only.

The key question is:

`Can the leader plausibly fund the remaining goal budget by itself?`

Do not automatically replace it with:

`Has the trailer already proved a chase?`

### Halftime fast-path

If the terminal-goal bridge passes, the halftime market is synchronized, adjacent totals are compared, and no material halftime tactical change invalidates the carried process, v0.2.44 verdict-first timing applies immediately. Do not automatically wait 5-10 second-half minutes for reassurance.

The opening second-half interval becomes an invalidation/repricing check, not a mandatory confirmation tax.

## Willem II vs NEC process lesson

At halftime NEC led 0-1 after scoring at 45+2. The detailed live screenshots showed a materially stronger NEC first-half attacking process, including multiple shots on target, two big chances, heavy box occupation and territorial control. The halftime board offered approximately Over 2.5 @ 1.73.

The model remained too dependent on proving Willem II's chase and did not issue a prospective shadow Over. NEC later extended the score and the user reported 0-4.

This is classified as:

- `EXCESSIVE POST-GOAL CONFIRMATION / TRAILER-CHASE DEPENDENCY`;
- `FAILURE TO RECOGNIZE LEADER-DRIVEN REMAINING-GOAL SUFFICIENCY`.

The later score is a process diagnostic only. The missed halftime Over is **not** a shadow win and must not be added to shadow P/L.

Canonical review:

`models/football/reviews/FOOTBALL_PROCESS_REVIEW_WILLEM_NEC_2026-08-15.md`

## v0.2.44 timeliness layer remains active

When a stable pre-goal state already clears all applicable gates, output the verdict immediately rather than waiting for an unnecessary extra snapshot or the next goal.

If a goal, red card, awarded penalty, material VAR event, major injury, or tactical substitution cluster occurs before delivery, invalidate the pending candidate as:

`NOT COUNTED — STATE CHANGED BEFORE DELIVERY`

Then reset and reprice from zero.

Track timing as:

- `ON TIME — DELIVERED IN STATE`
- `VALID HOLD — GATE INCOMPLETE`
- `LATE — GATES WERE COMPLETE BUT VERDICT DELAYED`
- `STATE-CHANGE RACE — NOT COUNTED`

## v0.2.43 style layer remains mandatory

Before the first serious prematch/live recommendation, profile both teams' base style, expected matchup style, attacking routes, defensive block, transitions, chance-generation signature, lead behaviour, trailing behaviour, and confidence caveat.

After every goal, perform the strict style reset. v0.2.45 provides a bridge only when the post-goal observation window genuinely does not exist before halftime; it does not erase the reset.

## Arm A / Arm B

### Arm A — current audit model

Apply Football v0.2.45 with the full validator, style layer, v0.2.44 timing layer, v0.2.45 terminal-goal bridge, market-family scan, directional quarantine and best-expression comparison.

Allowed outputs:

- `SHADOW LEAN — DO NOT PLACE`
- `NO BET`
- `NO BET — HOLD`

### Arm B — early-totals benchmark

Continue the v0.2.6-v0.2.9 totals philosophy with current synchronization, provider-quality, settlement, v0.2.43 style, v0.2.44 timeliness and v0.2.45 terminal-goal/leader-driven controls.

Allowed outputs:

- `BENCHMARK SHADOW — DO NOT PLACE`
- `BENCHMARK NO BET`

Arm B may decide at halftime without a second-half confirmation snapshot when the terminal-goal bridge, exact-line, primary-channel, adjacent-line, adverse-branch and NO-BET-comparator gates pass.

## Competition/provider exclusion

Per explicit user instruction, **AFC Challenge/AFC Challenge League matches remain excluded from the current audit workflow because live-stat coverage is insufficient** unless the user explicitly reverses the exclusion and adequate synchronized data is available.

This is not a blanket exclusion of all AFC or Asian competitions.

## Audit integrity

- Never retrofit a rule or candidate after the result.
- A market that would have won is not a model win unless it was prospectively selected in the synchronized state.
- Genuine misses remain misses.
- Official betting cannot resume until existing audit exit criteria are met and the user explicitly approves resumption.
- `/ledger.json` remains authoritative for official accounting when ledger writes are authorized.