# Current Football Model

**Canonical namespace:** `models/football/`

- Active model: **Football v0.2.46 — AUDIT MODE**
- Organized loading guide: `models/football/ORGANIZED_FILE_LOADING_GUIDE.md`
- Main procedure: `models/football/procedures/FOOTBALL_BETTING_PROCEDURE.md`
- Procedure addendum: `models/football/procedures/FOOTBALL_BETTING_PROCEDURE_ADDENDUM_2026-08-01.md`
- Mandatory validator: `models/football/procedures/FOOTBALL_PRE_VERDICT_VALIDATOR.md`
- Airtable control map: `models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md`
- Active rule directory: `models/football/rules/`
- Active audit: `models/football/reviews/FOOTBALL_DIRECTIONAL_AUDIT_2026-08-11.md`
- Parallel early-totals benchmark: `models/football/reviews/FOOTBALL_V026_V029_BENCHMARK_PROTOCOL_2026-08-11.md`
- Latest process review: `models/football/reviews/FOOTBALL_PROCESS_REVIEW_WILLEM_NEC_2026-08-15.md`
- Active cross-chat handoff: `models/football/handoffs/CHAT_TRANSFER_HANDOFF_2026-08-16.md`
- Historical baseline: `models/LEGACY_MODEL_CHANGELOG.md`
- Authoritative betting feed: `/ledger.json`

## Required load order

Load in this order, applying the newest active football rule over older conflicts:

1. `models/football/ORGANIZED_FILE_LOADING_GUIDE.md`
2. `models/LEGACY_MODEL_CHANGELOG.md` — retained pre-v0.2.5 football baseline
3. `models/football/procedures/FOOTBALL_BETTING_PROCEDURE.md`
4. `models/football/procedures/FOOTBALL_BETTING_PROCEDURE_ADDENDUM_2026-08-01.md`
5. `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.5.md` through `MODEL_RULES_FOOTBALL_V0.2.46.md`, ascending
6. `models/football/procedures/FOOTBALL_PRE_VERDICT_VALIDATOR.md`
7. `models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md`
8. `models/football/reviews/FOOTBALL_DIRECTIONAL_AUDIT_2026-08-11.md`
9. `models/football/reviews/FOOTBALL_V026_V029_BENCHMARK_PROTOCOL_2026-08-11.md`
10. `models/football/handoffs/CHAT_TRANSFER_HANDOFF_2026-08-16.md`
11. `/ledger.json` only when official record, bankroll, exposure, placement, or settlement status is relevant

Older handoffs are historical context only and must not override v0.2.46 or the active 2026-08-16 handoff.

## Audit-mode operating values

- 1u = 1,000,000 VND.
- Minimum odds reference = 1.70.
- Official football betting is **PAUSED**.
- Execution mode is **SHADOW CALIBRATION ONLY** until audit exit criteria are met and the user explicitly approves resumption.
- Ledger writes remain **ON HOLD** until explicitly approved.
- Normal current audit small-test convention = 0.125u when a simulated shadow stake is needed and no newer rule supersedes it.
- Directional AH/DNB/ML selections remain quarantined from official promotion.
- Totals are not automatically approved; they remain subject to synchronization, settlement, provider-quality, style, benchmark, timing, pressure-inflection and post-goal gates.
- xG/xGOT are secondary only and may be discarded when provider quality is unreliable.
- Every material checkpoint must scan the major market families and preserve exact score/minute/line/odds synchronization.

## v0.2.43 style layer — retained

Before every serious preview and before the first live recommendation in a match, both teams require an evidence-based style profile covering base build-up/tempo, attacking routes, defensive block, transitions, chance-generation signature, lead behaviour, trailing behaviour, expected matchup adaptation, and confidence/sample caveat.

Always distinguish `Base style` from `Expected matchup style`.

If style is materially incomplete, use `STYLE PROFILE INCOMPLETE` and cap the prematch verdict at `NO BET — HOLD`.

After every goal, perform the full tactical/state reset and report:

- `Prematch style expectation:`
- `Leader post-goal behaviour:`
- `Trailer post-goal behaviour:`
- `Style deviation:`
- `Post-goal persistence:`
- `Market implication:`

Normally require two comparable post-goal observations, or one observation plus strong event-level evidence over a meaningful interval, except where v0.2.45's terminal-goal bridge explicitly applies because the observation window genuinely does not exist.

## v0.2.44 timeliness layer — retained

If a synchronized **pre-goal** state is stable and all applicable candidate gates are complete, deliver the verdict immediately. Do not wait for a goal or an extra snapshot solely for reassurance.

Required delivery order:

1. synchronized score/minute;
2. verdict;
3. line/odds;
4. compact reasoning and invalidation.

If a goal, red card, awarded penalty, material VAR event, major injury, or tactical substitution cluster occurs before delivery, invalidate the pending candidate as:

`NOT COUNTED — STATE CHANGED BEFORE DELIVERY`

Then reset and reprice.

Timing classifications:

- `ON TIME — DELIVERED IN STATE`
- `VALID HOLD — GATE INCOMPLETE`
- `LATE — GATES WERE COMPLETE BUT VERDICT DELAYED`
- `STATE-CHANGE RACE — NOT COUNTED`

## v0.2.45 terminal-goal / leader-driven Over layer — retained as fallback

When a goal arrives so close to halftime that the normal post-goal persistence window cannot honestly be completed, label:

`POST-GOAL OBSERVATION WINDOW UNAVAILABLE — HALFTIME BRIDGE`

The goal still triggers the full reset, but high-quality pre-goal process may carry into the halftime total assessment when the bridge gates pass.

A live Over does not universally require both teams to have strong scoring routes. If the leader can credibly supply the remaining goal budget itself, classify the candidate as `LEADER-DRIVEN OVER` and treat trailer chase as a modifier rather than an automatic veto.

v0.2.45 is now explicitly a **post-goal fallback**. It must not distract from identifying a valid pre-goal acceleration earlier.

## v0.2.46 pre-goal pressure-inflection layer — ACTIVE EMPHASIS

The corrected Willem II vs NEC lesson is that the key missed window was around **42' at 0-0**, when NEC had already increased pressure, not primarily halftime after the 45+2 goal.

From approximately 35:00 to halftime, every material checkpoint must compare the recent 5-10 minute interval with the prior synchronized state.

Classify:

- `PRESSURE INFLECTION: YES`
- `PRESSURE INFLECTION: POSSIBLE / UNRESOLVED`
- `PRESSURE INFLECTION: NO`

A valid inflection normally needs at least two independent primary changes, including:

- at least one direct-threat channel: new SOT, big chance, inside-box shot, repeated box entries/touches, dangerous set-piece sequence, or repeated transitions ending in final actions; and
- at least one structural/territorial channel: sustained final-third occupation, repeated high recoveries, opponent pinned into clearances, recurring overloads, deteriorating defensive spacing, or possession becoming materially more advanced.

A specific contemporaneous user live observation may support the structural channel when consistent with the synchronized feed, but cannot be the only channel.

xG/xGOT remain secondary.

### Attacker-driven pre-goal Over

At 0-0 or another tied score, do not wait for a future `trailing-team chase` condition that does not yet exist.

A one-team surge may support:

`ATTACKER-DRIVEN PRE-GOAL OVER`

when that team can plausibly fund the remaining goal budget itself.

Classify opponent contribution:

- `ESSENTIAL`
- `HELPFUL`
- `OPTIONAL`

For low protected totals, opponent contribution may be `OPTIONAL` if the attacking team can plausibly produce the required goals itself.

### Protected total comparison

When one team is driving the Over, compare adjacent low totals explicitly, including the nearest eligible quarter/full lines such as Over 1.5, 1.75, 2.0 and 2.25.

Prefer the settlement boundary that best preserves value if the attacking team produces only one or two further goals. Quarter-goal protection may be preferable to a larger price on a worse boundary.

### No goal-confirmation tax

If `PRESSURE INFLECTION: YES` and all validator/market/style gates are complete, deliver immediately under v0.2.44.

Do not wait for:

- the first goal;
- halftime;
- proof that the opponent will chase after conceding;
- an extra snapshot used only for reassurance.

If the goal arrives first, invalidate the old state as `STATE-CHANGE RACE — NOT COUNTED`, reset, and only then apply v0.2.45 if a terminal-goal bridge is relevant.

### Required late-half fields

For serious live assessments from 35' to halftime, include:

- `Recent interval:`
- `Pressure inflection:` YES / POSSIBLE / NO
- `Primary acceleration channels:`
- `Attacker-driven goal route:` STRONG / MODERATE / WEAK / N/A
- `Opponent contribution:` ESSENTIAL / HELPFUL / OPTIONAL
- `Best protected total:` exact line and odds if available
- `Timing status:` ON TIME / VALID HOLD / LATE / STATE-CHANGE RACE

## Parallel benchmark mode

Every suitable synchronized live checkpoint with an available totals board supports two shadow-only research outputs:

- **Arm A — Current audit model:** Football v0.2.46 with full validator, style, timing, v0.2.45 fallback, v0.2.46 pressure-inflection, market-scan and audit controls. Directional markets remain quarantined.
- **Arm B — Early totals benchmark:** v0.2.6-v0.2.9 live-total philosophy reconstructed with current synchronization, provider-quality, v0.2.43 style, v0.2.44 timeliness, v0.2.45 terminal-goal fallback and v0.2.46 pre-goal acceleration logic.

Arm B evaluates totals only and may output:

- `BENCHMARK SHADOW — DO NOT PLACE`
- `BENCHMARK NO BET`

When a stable pre-goal state already passes exact-line, independent-primary-channel, adjacent-line, adverse-branch and NO-BET comparator gates, Arm B should decide immediately rather than waiting for the next goal.

## Competition/provider exclusion

Per explicit user instruction, **AFC Challenge/AFC Challenge League matches are excluded from the current audit workflow because live-stat coverage is insufficient**. Do not use them for current shadow calibration unless the user explicitly reverses this exclusion and adequate synchronized live data is available.

This is not a blanket exclusion of all AFC or Asian competitions.

## Audit trigger and exit criteria

The directional decision boundary remains untrusted following the poor recent directional sample recorded in `FOOTBALL_DIRECTIONAL_AUDIT_2026-08-11.md`.

Official football betting cannot resume until all existing audit exit criteria are satisfied, including:

- at least 20 newly assessed shadow decisions after audit start;
- at least 10 directional-eligible decision points;
- no retrospective rewriting;
- no unresolved repeated structural loss pattern;
- formal simplification review;
- explicit user approval to restore official betting.

The early-totals benchmark cannot shorten the audit.

## Existing controls retained

- Full synchronization after every material event.
- Hard pre-verdict validator and Airtable decision-state logging for Arm A shadow candidates.
- One best expression per assessment.
- Competition-format and utility verification.
- Side-versus-total comparator under v0.2.42.
- Protected-underdog and favorite-first-goal burden under v0.2.41.
- Directional persistence/reset logic under v0.2.33-v0.2.40.
- Mandatory style/post-goal behaviour profiling under v0.2.43.
- Timeliness/pre-goal decision completion under v0.2.44.
- Terminal-goal bridge and leader-driven remaining-goal sufficiency under v0.2.45.
- Pre-goal pressure-inflection and attacker-driven remaining-goal logic under v0.2.46.

## Response behavior during audit

- Use `SHADOW LEAN — DO NOT PLACE` only when an Arm A candidate clears the validator and all active style/timing/pressure/reset gates.
- Otherwise use `NO BET` or `NO BET — HOLD` for Arm A.
- Report Arm B separately as `BENCHMARK SHADOW — DO NOT PLACE` or `BENCHMARK NO BET` when synchronized totals information is sufficient.
- Do not issue `OFFICIAL BET` while audit mode is active.
- State the verdict before extended explanation once the gates are resolved.
- A market that would have won is not a model win unless it was prospectively selected in the synchronized state.

## Willem II vs NEC corrected audit note

The process review records the around-42' pre-goal state as the key missed window. The around-42' Over 1.75 price is a **missed synchronized decision state only**, not a retrospective shadow selection. The later 0-4 score adds no shadow P/L.

## Active cross-chat continuation

The 2026-08-16 handoff preserves the completed Atlas–Tigres shadow sequence, the user-enabled add-on workflow, and the immediate next-match lock on **Racing Santander vs Villarreal CF**.

## Write boundary

All football audit material, reviews, procedures, handoffs, and model updates remain under `models/football/`. `/ledger.json` remains authoritative for official accounting when writes are authorized.