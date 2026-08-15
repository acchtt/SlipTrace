# Current Football Model

**Canonical namespace:** `models/football/`

- Active model: **Football v0.2.45 — AUDIT MODE**
- Organized loading guide: `models/football/ORGANIZED_FILE_LOADING_GUIDE.md`
- Main procedure: `models/football/procedures/FOOTBALL_BETTING_PROCEDURE.md`
- Procedure addendum: `models/football/procedures/FOOTBALL_BETTING_PROCEDURE_ADDENDUM_2026-08-01.md`
- Mandatory validator: `models/football/procedures/FOOTBALL_PRE_VERDICT_VALIDATOR.md`
- Airtable control map: `models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md`
- Active rule directory: `models/football/rules/`
- Active audit: `models/football/reviews/FOOTBALL_DIRECTIONAL_AUDIT_2026-08-11.md`
- Parallel early-totals benchmark: `models/football/reviews/FOOTBALL_V026_V029_BENCHMARK_PROTOCOL_2026-08-11.md`
- Latest process review: `models/football/reviews/FOOTBALL_PROCESS_REVIEW_WILLEM_NEC_2026-08-15.md`
- Active cross-chat handoff: `models/football/handoffs/CHAT_TRANSFER_HANDOFF_2026-08-15.md`
- Historical baseline: `models/LEGACY_MODEL_CHANGELOG.md`
- Authoritative betting feed: `/ledger.json`

## Required load order

Load the following in this order, applying the newest active football rule over older conflicts:

1. `models/football/ORGANIZED_FILE_LOADING_GUIDE.md`
2. `models/LEGACY_MODEL_CHANGELOG.md` for the retained pre-v0.2.5 football baseline
3. `models/football/procedures/FOOTBALL_BETTING_PROCEDURE.md`
4. `models/football/procedures/FOOTBALL_BETTING_PROCEDURE_ADDENDUM_2026-08-01.md`
5. `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.5.md` through `MODEL_RULES_FOOTBALL_V0.2.45.md`, ascending
6. `models/football/procedures/FOOTBALL_PRE_VERDICT_VALIDATOR.md`
7. `models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md`
8. `models/football/reviews/FOOTBALL_DIRECTIONAL_AUDIT_2026-08-11.md`
9. `models/football/reviews/FOOTBALL_V026_V029_BENCHMARK_PROTOCOL_2026-08-11.md`
10. `models/football/handoffs/CHAT_TRANSFER_HANDOFF_2026-08-15.md`
11. `/ledger.json` only when official record, bankroll, exposure, placement, or settlement status is relevant

Older handoffs, including `CHAT_TRANSFER_HANDOFF_2026-08-14.md` and `CHAT_TRANSFER_HANDOFF_2026-08-12.md`, are historical context only and must not override v0.2.45 or the 2026-08-15 handoff.

## Audit-mode operating values

- 1u = 1,000,000 VND.
- Minimum odds reference = 1.70.
- Official football betting is **PAUSED**.
- Execution mode is **SHADOW CALIBRATION ONLY** until the audit exit criteria are met and the user explicitly approves resumption.
- Ledger writes remain **ON HOLD** until explicitly approved.
- Directional AH/DNB/ML selections remain quarantined from official promotion.
- Totals are not automatically approved; they remain subject to synchronization, settlement, provider-quality, style, benchmark and active timing/bridge gates.
- xG/xGOT are secondary only and may be discarded when the provider feed is unreliable.
- Every material checkpoint must scan the major market families and preserve exact score/minute/line/odds synchronization.

## Mandatory style layer — v0.2.43 retained

Before every serious preview, and before the first live recommendation in a match, both teams require an evidence-based style profile covering base build-up/tempo, attacking routes, defensive block, transitions, chance-generation signature, lead behaviour, trailing behaviour, expected matchup adaptation, and confidence/sample caveat.

Always distinguish `Base style` from `Expected matchup style`.

If the style profile is materially incomplete, use `STYLE PROFILE INCOMPLETE` and cap the prematch verdict at `NO BET — HOLD`.

After every goal, perform the full v0.2.43 tactical/state reset. Before a new post-goal candidate, report:

- `Prematch style expectation:`
- `Leader post-goal behaviour:`
- `Trailer post-goal behaviour:`
- `Style deviation:`
- `Post-goal persistence:`
- `Market implication:`

Normally require two comparable post-goal observations, or one observation plus strong event-level evidence over a meaningful interval, except where the v0.2.45 terminal-goal bridge explicitly applies because the observation window does not exist before halftime.

## Timeliness layer — v0.2.44 retained

If a synchronized **pre-goal** state is stable and all applicable candidate gates are complete, deliver the verdict immediately. Do not wait for a goal or an extra snapshot solely for reassurance.

The v0.2.43 post-goal persistence requirement applies after a goal or material reset; it must not be misapplied to delay a qualified pre-goal total.

Once gates resolve, use verdict-first delivery: synchronized state -> verdict -> line/odds -> compact reasoning/invalidation.

If a goal, red card, awarded penalty, material VAR event, major injury, or tactical substitution cluster occurs before delivery, invalidate the pending candidate as:

`NOT COUNTED — STATE CHANGED BEFORE DELIVERY`

Then reset and reprice. Never backfill the old market after the outcome.

Track live timing as `ON TIME`, `VALID HOLD`, `LATE`, or `STATE-CHANGE RACE — NOT COUNTED`.

## Terminal-goal / leader-driven Over layer — v0.2.45

v0.2.45 is STRICT and prospective.

When a goal arrives so close to halftime that the normal post-goal persistence window cannot honestly be completed, label:

`POST-GOAL OBSERVATION WINDOW UNAVAILABLE — HALFTIME BRIDGE`

The goal still triggers the full reset, but high-quality pre-goal process may carry into the halftime total assessment when the bridge gates pass.

A terminal-goal bridge requires sustained pre-goal superiority by the scoring team, at least three independent primary forward channels, at least one direct chance/box-production channel, a separate structural/territorial channel, no unresolved material-event regime break, and a synchronized halftime line/price with adjacent-line comparison. The goal itself cannot count as one of the evidence channels. xG/xGOT remain secondary only.

A live Over does **not** universally require both teams to have strong scoring routes. If the leader can credibly supply the remaining goal budget itself, classify the candidate as `LEADER-DRIVEN OVER` and treat the trailer's chase as a modifier rather than an automatic veto.

For every terminal-goal halftime assessment report:

- `Terminal-goal bridge:` PASS / FAIL / N/A
- `Leader continuation route:` STRONG / MODERATE / WEAK
- `Trailer role:` ESSENTIAL / HELPFUL / OPTIONAL
- `Remaining-goal budget:` exact settlement requirement
- `Halftime tactical-change risk:` LOW / MODERATE / HIGH / UNRESOLVED
- `Timing status:` ON TIME / VALID HOLD / LATE / STATE-CHANGE RACE

If the bridge passes and no material halftime tactical change is unresolved, do not automatically wait 5-10 second-half minutes for confirmation. Apply v0.2.44 verdict-first timing at the synchronized halftime price; the opening second-half interval becomes an invalidation/repricing check rather than a confirmation tax.

Canonical process example: Willem II vs NEC Nijmegen, 2026-08-15. NEC scored at 45+2 after already showing the stronger attacking process. The model over-weighted the need for Willem II chase and failed to recognize NEC's independent continuation route. The later 0-4 state is a process diagnostic only and is **not** a retrospective shadow win.

## Parallel benchmark mode

Every suitable synchronized live checkpoint with an available totals board supports two shadow-only research outputs:

- **Arm A — Current audit model:** Football v0.2.45 with all active validator, style, timing, terminal-goal bridge, market-scan, and audit controls. Directional markets remain quarantined.
- **Arm B — Early totals benchmark:** the v0.2.6-v0.2.9 live-total philosophy reconstructed with current synchronization, provider-quality, v0.2.43 style, v0.2.44 timeliness and v0.2.45 leader-driven/terminal-goal controls.

Arm B evaluates totals only. It may output `BENCHMARK SHADOW — DO NOT PLACE` or `BENCHMARK NO BET`.

For Arm B, prioritize exact score/minute, remaining-goal branches, adjacent totals, boundary protection, competition utility, reliable non-xG forward evidence, team-specific style, and NO BET discipline. Evaluate both Over and Under.

When a stable pre-goal state already passes the exact-line, two-primary-channel, adjacent-line, adverse-branch and NO-BET comparator gates, Arm B should decide immediately rather than waiting for the next goal.

When a terminal first-half goal leaves no usable post-goal observation window, Arm B may decide at halftime from the v0.2.45 bridge without a second-half confirmation snapshot if all bridge and market gates pass.

## Competition/provider exclusion

Per explicit user instruction, **AFC Challenge/AFC Challenge League matches are excluded from the current audit workflow because live-stat coverage is insufficient**. Do not use them for current shadow calibration unless the user explicitly reverses this exclusion and adequate synchronized live data is available.

This is not a blanket exclusion of all AFC or Asian competitions; provider quality is assessed separately for other competitions.

## Audit trigger and exit criteria

The directional decision boundary remains untrusted following the poor recent directional sample recorded in `FOOTBALL_DIRECTIONAL_AUDIT_2026-08-11.md`.

Official football betting cannot resume until all existing audit exit criteria are satisfied, including:

- at least 20 newly assessed shadow decisions after audit start;
- at least 10 directional-eligible decision points;
- no retrospective rewriting;
- no unresolved repeated structural loss pattern;
- formal simplification review;
- explicit user approval to restore official betting.

The early-totals benchmark cannot shorten the audit. The v0.2.43 style layer also remains subject to its prospective review threshold.

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

## Response behavior during audit

- Use `SHADOW LEAN — DO NOT PLACE` only when an Arm A candidate clears the validator and all active style/timing/bridge gates.
- Otherwise use `NO BET` or `NO BET — HOLD` for Arm A.
- Report Arm B separately as `BENCHMARK SHADOW — DO NOT PLACE` or `BENCHMARK NO BET` when synchronized totals information is sufficient.
- Do not issue `OFFICIAL BET` while audit mode is active.
- State the verdict before extended explanation once the gates are resolved.
- A market that would have won is not a model win unless it was prospectively selected in the synchronized state.

## Write boundary

All football audit material, reviews, procedures, handoffs, and model updates remain under `models/football/`. `/ledger.json` remains authoritative for official accounting when writes are authorized.