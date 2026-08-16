# Football Cross-Chat Handoff — 2026-08-16 V2

**Status:** Active cross-chat handoff  
**Active model:** Football v0.2.47 — AUDIT MODE  
**Canonical namespace:** `models/football/`

This handoff supersedes `CHAT_TRANSFER_HANDOFF_2026-08-16.md` for normal startup. Older handoffs remain historical context only and must not override v0.2.47.

## Startup state

- Official football betting remains **PAUSED**.
- Execution mode remains **SHADOW CALIBRATION ONLY**.
- Ledger writes remain **ON HOLD until explicit user approval**.
- 1u = 1,000,000 VND.
- Minimum eligible odds reference = 1.70.
- Normal audit shadow stake convention = 0.125u unless a newer user instruction changes it.
- Directional AH/DNB/ML markets remain quarantined from official promotion.
- xG/xGOT remain secondary only.
- Exact score/minute/line/odds/settlement synchronization remains mandatory.
- Never retrofit a candidate after a result.

## Active target state

**R. Racing Club vs Villarreal CF** remains the active match in this thread.

Known sequence from the synchronized/user-supplied live states:

- Racing led 1-0 from a 21' penalty.
- Racing led 2-0 after a 34' goal.
- Villarreal scored at 45' and 45+1 to make halftime **2-2**.
- HT stats showed an open first half with meaningful attacking activity from both teams.
- At 55:51 the then-active v0.2.46 model issued `SHADOW LEAN — DO NOT PLACE: Over 5.25 @1.88`.
- At 63:57, still 2-2, current best protected reference had improved to Over 5 @1.86; this was logged as continuation only, not a second counted ticket.
- User later reported **still 2-2 at 82'**.
- No final score is assumed unless the user provides or confirms it.

The original 55:51 shadow record must remain exactly as issued for audit integrity. v0.2.47 is a prospective process correction and must not rewrite that selection.

## Why v0.2.47 was added

The user identified a repeated pattern: matches can score 2-3+ goals before halftime, then retain apparently similar second-half pressure while producing only one or zero additional goals. The user cited this Racing-Villarreal match and a separate Ajax example as same-direction observations.

The model weakness was:

`PRESSURE PERSISTENCE -> TREATED TOO EASILY AS SCORING-HAZARD PERSISTENCE`

v0.2.47 adds a mandatory **High-Scoring Halftime Compression / Goal-Saturation Gate**.

### Trigger

- 0-2 HT goals: normal halftime reset.
- 3 HT goals: `HT COMPRESSION GATE — MODERATE`.
- 4+ HT goals: `HT GOAL-SATURATION GATE — STRONG`.

### Core enforcement

After 3+ HT goals:

1. first-half openness becomes context only and cannot count toward fresh second-half primary evidence;
2. post-HT Over promotion must stand on **second-half-only** evidence;
3. at least one fresh **conversion-quality channel** is mandatory;
4. generic shots, SOT totals, possession, corners, territory and box touches cannot establish renewed scoring hazard by themselves;
5. a candidate needing two or more additional goals for a full win needs a credible second-half multi-goal route, not merely persistent activity;
6. after a meaningful score-stable second-half interval, reclassify current hazard rather than carrying the old `OPEN` label indefinitely;
7. post-HT add-ons after 3+ first-half goals must independently clear the new gate.

Required hazard labels:

- `SECOND-HALF HAZARD: RE-ACCELERATING`
- `SECOND-HALF HAZARD: PERSISTENT BUT UNPROVEN`
- `SECOND-HALF HAZARD: COMPRESSING`

`PERSISTENT BUT UNPROVEN` cannot promote an Over.

## Racing-Villarreal corrected interpretation

At 2-2 HT the strong saturation gate should have been active.

The 55:51 second-half evidence showed activity, including Racing box access and a big chance plus some Villarreal threat, but the remaining Over 5.25 full-win budget required **two more goals**.

Under v0.2.47 that state would remain:

`NO BET — HOLD`

unless repeated second-half conversion-quality evidence established a credible multi-goal route.

This does not retroactively cancel or rewrite the existing v0.2.46 shadow selection; it identifies why the promotion threshold was too permissive.

## Retained v0.2.43-v0.2.46 controls

- v0.2.43: mandatory both-team style profile and full post-goal tactical reset.
- v0.2.44: verdict-first delivery; do not delay once the current state genuinely clears gates.
- v0.2.45: terminal-goal halftime bridge and leader-driven remaining-goal sufficiency.
- v0.2.46: late-first-half pressure-inflection detection and attacker-driven pre-goal Over logic.
- v0.2.47: high-scoring HT compression/saturation gate; first-half pressure cannot satisfy post-HT promotion evidence.

v0.2.47 is not a blanket Under bias and is not permission to become generally slower. If strong second-half conversion-quality evidence appears quickly, decide quickly.

## User live-workflow preference

The user has enabled add-on assessment during shadow calibration:

- base shadow normally 0.125u;
- one 0.125u add-on may be considered when a fresh synchronized state independently qualifies;
- default max shadow exposure per match = 0.25u;
- do not add because price improved, the original position is losing, or cumulative pressure remains high;
- after a 3+ goal HT, any add-on must also clear v0.2.47 using second-half-only evidence.

## Arm A / Arm B

### Arm A — current audit model

Apply Football v0.2.47 with the full validator, style layer, v0.2.44 timeliness, v0.2.45 fallback, v0.2.46 pressure-inflection, v0.2.47 halftime compression gate, market scan and audit controls.

Allowed outputs:

- `SHADOW LEAN — DO NOT PLACE`
- `NO BET`
- `NO BET — HOLD`

### Arm B — early totals benchmark

Continue the v0.2.6-v0.2.9 totals philosophy with modern synchronization/provider-quality/settlement/style controls. After 3+ HT goals, first-half activity cannot count as fresh second-half primary evidence. Arm B may remain more permissive on protected boundaries but must still prove the post-HT regime independently.

Allowed outputs:

- `BENCHMARK SHADOW — DO NOT PLACE`
- `BENCHMARK NO BET`

## Competition/provider exclusion

Per explicit user instruction, AFC Challenge/AFC Challenge League matches remain excluded from the current audit workflow because live-stat coverage is insufficient unless the user explicitly reverses that exclusion and adequate synchronized live data is available.

## Audit integrity

- Official football betting remains paused until all audit exit criteria are satisfied and the user explicitly approves resumption.
- Directional markets remain quarantined.
- No official ledger writes without explicit user approval.
- `/ledger.json` remains authoritative for official accounting when writes are authorized.
- A market that later wins is not a model win unless it was prospectively selected in-state.
- New rules correct future behavior; they do not rewrite past shadow decisions.

## New-chat continuation instruction

After loading, respond with `FOOTBALL FILES LOADED`, confirm **Football v0.2.47 — AUDIT MODE**, confirm the high-scoring halftime compression/saturation gate is active, and continue from the newest user-supplied match state without asking the user to repeat prior context.