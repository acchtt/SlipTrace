# Football Cross-Chat Handoff — 2026-08-16

**Status:** Active cross-chat handoff  
**Active model:** Football v0.2.46 — AUDIT MODE  
**Canonical namespace:** `models/football/`

This handoff supersedes `CHAT_TRANSFER_HANDOFF_2026-08-15.md` for normal startup. Older handoffs remain historical context only and must not override v0.2.46 or this handoff.

## Startup state

- Official football betting remains **PAUSED**.
- Execution mode remains **SHADOW CALIBRATION ONLY**.
- Ledger writes remain **ON HOLD until explicit user approval**.
- 1u = 1,000,000 VND.
- Minimum eligible odds reference remains 1.70.
- Normal audit shadow stake convention remains 0.125u unless the user changes it.
- Directional AH/DNB/ML markets remain quarantined from official promotion.
- xG/xGOT remain secondary only and cannot carry a thesis.
- Exact score/minute/line/odds/settlement synchronization remains mandatory.
- A market that later wins is not a model win unless it was prospectively selected in-state.
- If a material event occurs before verdict delivery, invalidate the pending quote as `STATE-CHANGE RACE — NOT COUNTED` / `NOT COUNTED — STATE CHANGED BEFORE DELIVERY` and reset.

## Immediate next-match lock

**LOCKED TARGET:** R. Racing Club vs Villarreal CF  
**Competition:** LALIGA EA SPORTS, 2026/27 Matchday 1  
**Date:** 2026-08-16  
**Kickoff:** 17:00 Spain local / approximately **22:00 Vietnam (ICT)**  
**Venue:** El Sardinero

The user explicitly selected this as the next match before moving chats.

### New-chat priority

1. Load the full Football v0.2.46 stack and this handoff.
2. Treat Racing–Villarreal as the current active target immediately.
3. Obtain/inspect the user's latest bookmaker board and confirmed lineups before any serious prematch verdict.
4. Do **not** reuse stale web odds as authoritative. A prior external indication suggested the Over market might be around a playable 2.5 boundary, but only the user's synchronized bookmaker screenshot controls live selection.
5. Build both-team style profiles before the first serious recommendation.
6. Live checkpoints: early baseline around 8'–10', regime check around 18'–20', and mandatory v0.2.46 pressure-inflection scan from about 35'–42'.
7. If a valid attacking surge appears and the protected total clears gates, decide immediately; do not wait for the scoreboard to confirm it.

## User live-workflow preference carried forward

The user has enabled **add-on assessment** during shadow calibration.

Operational interpretation unless the user changes it:

- Base shadow entry: normally 0.125u.
- One additional 0.125u add-on may be considered when a **fresh synchronized state independently qualifies**.
- Do not add merely because the original position is losing, because price improved, or because an earlier thesis remains open.
- Default maximum shadow exposure per match under this user instruction: **0.25u**.
- Every add-on needs its own exact line/odds, settlement check, primary evidence, style/state reset resolution, and NO-BET comparator.
- This is a user workflow instruction preserved across the chat transfer; it is not permission to bypass the active model or official-betting pause.

## Active model emphasis — v0.2.43 through v0.2.46

### v0.2.43 style/post-goal layer

Before the first serious prematch/live recommendation, profile both teams:

- base build-up;
- attacking route;
- tempo;
- defensive block;
- transition behavior;
- chance-generation signature;
- lead behavior;
- trailing behavior;
- expected matchup adaptation;
- confidence/sample caveat.

Always distinguish `Base style` from `Expected matchup style`.

After every goal, perform the full reset and report:

- `Prematch style expectation:`
- `Leader post-goal behaviour:`
- `Trailer post-goal behaviour:`
- `Style deviation:`
- `Post-goal persistence:`
- `Market implication:`

Normally require two comparable post-goal observations, or one observation plus strong event-level evidence over a meaningful interval, except where v0.2.45's terminal-goal bridge genuinely applies.

### v0.2.44 timeliness

If a stable pre-goal state already clears all applicable gates, deliver the verdict immediately. No extra snapshot for reassurance.

Verdict-first order:

1. synchronized state;
2. verdict;
3. line/odds;
4. compact reasoning/invalidation.

Timing classification:

- `ON TIME — DELIVERED IN STATE`
- `VALID HOLD — GATE INCOMPLETE`
- `LATE — GATES WERE COMPLETE BUT VERDICT DELAYED`
- `STATE-CHANGE RACE — NOT COUNTED`

### v0.2.45 terminal-goal / leader-driven fallback

If a first-half goal arrives so late that a genuine post-goal observation window does not exist, perform the reset but allow high-quality pre-goal process to bridge into halftime if the v0.2.45 gates pass.

A live Over does not require both teams to contribute. If the leader can credibly fund the remaining-goal budget itself, trailer chase is a modifier rather than an automatic veto.

v0.2.45 is a fallback after a terminal goal, not a reason to miss an earlier pre-goal pressure surge.

### v0.2.46 pre-goal pressure inflection — active emphasis

The corrected Willem II–NEC lesson is that the key missed window was around 42' at **0-0**, when NEC had already increased pressure before scoring at 45+2.

From about 35' to halftime, compare the latest 5–10 minute interval with the prior synchronized state and classify:

- `PRESSURE INFLECTION: YES`
- `PRESSURE INFLECTION: POSSIBLE / UNRESOLVED`
- `PRESSURE INFLECTION: NO`

A valid inflection normally needs at least two independent primary changes:

- one direct-threat channel (new SOT, big chance, inside-box shot, repeated box entries/touches, dangerous set pieces, repeated transitions with final action); and
- one structural/territorial channel (sustained final-third occupation, high recoveries, opponent pinned into clearances, overloads, deteriorating spacing, possession becoming materially more advanced).

xG/xGOT remain secondary only.

At a tied score, do not wait for a future trailing-team chase condition. A one-team surge may support `ATTACKER-DRIVEN PRE-GOAL OVER` if that team can plausibly fund the protected goal budget itself. Opponent contribution must be classified `ESSENTIAL / HELPFUL / OPTIONAL`.

If the pre-goal state qualifies, deliver immediately. If a goal beats delivery, invalidate the quote and reset.

## Willem II vs NEC — corrected process lesson from this chat

Observed sequence and correction:

- Around 31' at 0-0 the game still looked genuinely suppressed and Under 2.25 around 1.82 was qualitatively strong on the football evidence, though operational validation remained on hold.
- By around 42', NEC had **materially increased pressure**. The important error was failing to detect that new interval regime quickly enough.
- Around that late-first-half state, a protected Over 1.75 was visible around 1.84.
- NEC scored at 45+2 to lead 0-1 at halftime and later the score reached 0-4.
- The original diagnosis focused too much on halftime and on whether Willem would chase. The user correctly clarified that the first real miss happened **before the goal**, when NEC pressure was already rising.

Primary classification:

`LATE — PRE-GOAL PRESSURE INFLECTION NOT CONVERTED TO DECISION`

The around-42' Over state is a **missed synchronized decision state only**, not a retrospective shadow win. The later goals add no P/L.

This chat caused the active model to advance first to v0.2.45 (terminal-goal/leader-driven logic) and then to **v0.2.46**, which corrected the emphasis to pre-goal acceleration detection.

## Utrecht vs AZ — session note

This match was used as a low-event calibration example.

- Early Utrecht pressure at ~5' did not persist.
- Around 15'–20' the match remained controlled: few total shots, few SOT, no big chances, and very weak AZ box penetration despite possession.
- No shadow entry was issued in the captured checkpoints.
- The important lesson was to distinguish real pressure persistence from an early burst and not infer Over merely from league reputation or possession.

No settlement/result from this match was recorded in this chat.

## Atlas vs Tigres — completed shadow sequence

**Final score:** Atlas 2–1 Tigres.

### Prematch / opening

- Prematch board from user: Atlas +0.25 around 1.86, Tigres -0.25 around 2.04, O2.25 around 1.97, O2.5 around 2.23.
- Confirmed lineup overrode stale external personnel assumptions; notably Duk started for Atlas.
- Atlas scored in the 2nd minute, creating a full post-goal reset.

### Early Tigres chase

By ~8'–9' Tigres had moved from sterile possession into a genuine chase through shots, box access, corners/set pieces and territorial pressure.

A preliminary O3 @1.83 shadow lean was stated, but the user immediately preferred waiting for the better-protected **O2.75** boundary. The O3 was therefore not the tracked match position in the later settlement accounting.

### Base tracked shadow

At **19:14, Atlas 1–0 Tigres**:

`SHADOW LEAN — DO NOT PLACE: Over 2.75 @1.78, 0.125u`

Rationale at delivery:

- sustained Tigres territorial chase;
- 4 shots and heavy corner pressure;
- Atlas reactive/counter route remained credible;
- O2.75 had improved above the 1.70 floor and gave materially better settlement protection than O3/O3.25.

Tigres equalized around 21'. The base shadow remained live.

### No add-on at ~31'

At ~31', 1-1, the post-equalizer interval had cooled. Tigres shot/box production had stalled and only set-piece pressure persisted.

Verdict:

`NO ADD-ON — VALID HOLD`

### Halftime add-on

At HT, 1-1, the late first-half interval had re-accelerated materially:

- Tigres roughly 5 -> 11 shots from the prior checkpoint;
- 1 -> 2 SOT;
- 7 -> 9 corners;
- 5 -> 14 opposition-box touches;
- Atlas also increased total shots.

Add-on issued:

`SHADOW LEAN — DO NOT PLACE: Over 3.25 @1.96, 0.125u`

Total match shadow exposure became 0.25u.

### Settlement

FT Atlas 2–1 Tigres:

- Base O2.75 @1.78, 0.125u -> **HALF WIN** = **+0.04875u**.
- Add-on O3.25 @1.96, 0.125u -> **HALF LOSS** = **-0.0625u**.
- **Match net = -0.01375u** = approximately **-13,750 VND**.

No official ledger write was authorized or made.

### Atlas–Tigres process takeaway

The first protected entry did its job. The halftime add-on was the weaker decision: late-H1 acceleration was real, but moving to the higher 3.25 boundary increased the remaining-goal burden and the second half did not sustain the regime.

For future add-ons, fresh evidence must independently justify both:

1. continuation of the attacking regime into the new state; and
2. the **higher settlement boundary / remaining-goal budget** being preferable to simply holding the base position.

Do not add merely because the original thesis is still alive or because cumulative first-half pressure was high.

## User interaction / live response preference

- The user sends frequent bookmaker + Soccerway screenshots.
- Prioritize **fast verdict-first delivery** during live play.
- Avoid long explanations before the actionable status.
- If a goal occurs while deciding, call the old quote stale/not-counted immediately and reset.
- The user explicitly wants the model less conservative when multi-channel evidence is already synchronized, especially on protected Asian totals.
- Do not over-weight clock decay, possession, or xG in isolation.
- Detect **interval acceleration** before the scoreboard confirms it.
- Protected quarter-goal totals are often preferred when they materially improve adverse-branch settlement.

## Arm A / Arm B

### Arm A — current audit model

Apply Football v0.2.46 with the full validator, style layer, v0.2.44 timing, v0.2.45 post-goal fallback, v0.2.46 pressure-inflection logic, market-family scan, directional quarantine and best-expression comparison.

Allowed outputs:

- `SHADOW LEAN — DO NOT PLACE`
- `NO BET`
- `NO BET — HOLD`

### Arm B — early totals benchmark

Continue the v0.2.6-v0.2.9 totals philosophy with modern synchronization, provider-quality, settlement, style and v0.2.44-v0.2.46 timing/pressure controls.

Allowed outputs:

- `BENCHMARK SHADOW — DO NOT PLACE`
- `BENCHMARK NO BET`

Arm B should explicitly test protected totals immediately when a pressure-inflection state appears rather than waiting for a goal.

## Competition/provider exclusion

Per explicit user instruction, **AFC Challenge/AFC Challenge League matches remain excluded from the current audit workflow because live-stat coverage is insufficient** unless the user explicitly reverses this exclusion and adequate synchronized live data is available.

## Audit integrity

- Never retrofit a candidate after the result.
- Genuine misses remain misses.
- Official football betting remains paused until all audit exit criteria are satisfied and the user explicitly approves resumption.
- Directional markets remain quarantined.
- No official ledger writes without explicit user approval.
- `/ledger.json` remains authoritative for official accounting when writes are authorized.

## New-chat continuation instruction

After loading, respond with `FOOTBALL FILES LOADED`, confirm **Football v0.2.46 — AUDIT MODE**, confirm **Racing Santander vs Villarreal is LOCKED as the next target**, and immediately continue prep/live assessment from the newest user-supplied lineup, odds or match-state screenshot without asking the user to repeat this chat.