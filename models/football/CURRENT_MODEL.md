# Current Football Model

**Canonical namespace:** `models/football/`

- Active model: **Football v0.2.47 — AUDIT MODE**
- Organized loading guide: `models/football/ORGANIZED_FILE_LOADING_GUIDE.md`
- Main procedure: `models/football/procedures/FOOTBALL_BETTING_PROCEDURE.md`
- Procedure addendum: `models/football/procedures/FOOTBALL_BETTING_PROCEDURE_ADDENDUM_2026-08-01.md`
- Mandatory validator: `models/football/procedures/FOOTBALL_PRE_VERDICT_VALIDATOR.md`
- Airtable control map: `models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md`
- Active rule directory: `models/football/rules/`
- Active audit: `models/football/reviews/FOOTBALL_DIRECTIONAL_AUDIT_2026-08-11.md`
- Parallel early-totals benchmark: `models/football/reviews/FOOTBALL_V026_V029_BENCHMARK_PROTOCOL_2026-08-11.md`
- Latest process review: `models/football/reviews/FOOTBALL_PROCESS_REVIEW_RACING_VILLARREAL_HT_COMPRESSION_2026-08-16.md`
- Active cross-chat handoff: `models/football/handoffs/CHAT_TRANSFER_HANDOFF_2026-08-16_V2.md`
- Historical baseline: `models/LEGACY_MODEL_CHANGELOG.md`
- Authoritative betting feed: `/ledger.json`

## Required load order

Load in this order, applying the newest active football rule over older conflicts:

1. `models/football/ORGANIZED_FILE_LOADING_GUIDE.md`
2. `models/LEGACY_MODEL_CHANGELOG.md` — retained pre-v0.2.5 football baseline
3. `models/football/procedures/FOOTBALL_BETTING_PROCEDURE.md`
4. `models/football/procedures/FOOTBALL_BETTING_PROCEDURE_ADDENDUM_2026-08-01.md`
5. `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.5.md` through `MODEL_RULES_FOOTBALL_V0.2.47.md`, ascending
6. `models/football/procedures/FOOTBALL_PRE_VERDICT_VALIDATOR.md`
7. `models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md`
8. `models/football/reviews/FOOTBALL_DIRECTIONAL_AUDIT_2026-08-11.md`
9. `models/football/reviews/FOOTBALL_V026_V029_BENCHMARK_PROTOCOL_2026-08-11.md`
10. `models/football/handoffs/CHAT_TRANSFER_HANDOFF_2026-08-16_V2.md`
11. `/ledger.json` only when official record, bankroll, exposure, placement, or settlement status is relevant

Older handoffs are historical context only and must not override v0.2.47 or the active V2 handoff.

## Audit-mode operating values

- 1u = 1,000,000 VND.
- Minimum odds reference = 1.70.
- Official football betting is **PAUSED**.
- Execution mode is **SHADOW CALIBRATION ONLY** until audit exit criteria are met and the user explicitly approves resumption.
- Ledger writes remain **ON HOLD** until explicitly approved.
- Normal current audit small-test convention = 0.125u when a simulated shadow stake is needed and no newer user instruction supersedes it.
- Directional AH/DNB/ML selections remain quarantined from official promotion.
- Totals are not automatically approved; they remain subject to synchronization, settlement, provider-quality, style, timing, reset, pressure-inflection, halftime-compression and market-scan gates.
- xG/xGOT are secondary only.
- Every material checkpoint must preserve exact score/minute/line/odds synchronization.

## Retained active layers

### v0.2.43 — style/post-goal layer

Before every serious preview and before the first live recommendation, both teams require an evidence-based style profile covering base build-up/tempo, attacking routes, defensive block, transitions, chance-generation signature, lead behaviour, trailing behaviour, expected matchup adaptation, and confidence/sample caveat.

After every goal, perform the full tactical/state reset. Normally require comparable post-goal evidence before re-promoting a thesis unless v0.2.45's genuine terminal-goal bridge applies.

### v0.2.44 — timeliness

If a synchronized state is stable and all applicable gates are complete, deliver the verdict immediately. Do not wait for a goal or an extra snapshot solely for reassurance.

A material event before delivery invalidates the pending quote as `STATE-CHANGE RACE — NOT COUNTED` / `NOT COUNTED — STATE CHANGED BEFORE DELIVERY`, followed by reset and reprice.

### v0.2.45 — terminal-goal / leader-driven fallback

A goal arriving too close to halftime for a genuine post-goal window may use the explicit halftime bridge when its gates pass. A leader may fund the remaining Over goal budget itself; trailer contribution is not universally mandatory.

v0.2.45 is a post-goal fallback, not a reason to miss an earlier pre-goal acceleration.

### v0.2.46 — pre-goal pressure inflection

From approximately 35:00 to halftime, every material checkpoint must compare the recent 5-10 minute interval with the prior synchronized state.

Classify `PRESSURE INFLECTION: YES / POSSIBLE / NO` using independent forward-looking direct-threat and structural/territorial channels. At a tied score, a one-team surge may support `ATTACKER-DRIVEN PRE-GOAL OVER` when that team can plausibly fund the protected remaining goal budget.

Do not impose a goal-confirmation tax: if the pre-goal state qualifies, decide immediately.

## v0.2.47 — High-Scoring Halftime Compression / Goal-Saturation Gate — ACTIVE EMPHASIS

The Racing Santander vs Villarreal audit exposed a distinct failure mode: a match can remain visibly active after halftime while **scoring hazard compresses**. Continued pressure is not equivalent to continued goal production.

### Trigger

- 0-2 HT goals: normal halftime reset.
- 3 HT goals: `HT COMPRESSION GATE — MODERATE`.
- 4+ HT goals: `HT GOAL-SATURATION GATE — STRONG`.

This is a model-risk gate, not an automatic Under signal.

### Hard rule

After 3+ first-half goals, **first-half openness becomes context only**. First-half goals, pressure, shots, SOT, corners, box touches and pressure inflections cannot satisfy the minimum fresh evidence count for a post-HT Over.

A post-HT Over must stand on **second-half-only forward-looking evidence**.

### Conversion-quality requirement

Generic possession, raw shots, raw SOT, corners, territory and box touches cannot establish renewed scoring hazard by themselves.

At least one fresh conversion-quality channel is required, such as a genuine big chance, repeated high-value inside-box attempts, meaningful keeper interventions from threatening locations, a clear defensive-error chance, strong cutback/one-v-one/free-header sequence, or repeated transitions ending in high-quality final actions.

xG/xGOT cannot substitute for this channel.

### Strong 4+ goal halftime gate

For 4+ HT goals, a new second-half Over normally requires:

1. halftime reset resolved;
2. a score-stable second-half sample, normally about 6-10 minutes unless an earlier high-quality event cluster clearly establishes the regime;
3. at least two independent second-half primary channels;
4. at least one conversion-quality channel;
5. evidence from the current interval, not cumulative match appearance;
6. an exact remaining-goal budget supported by second-half evidence alone;
7. adjacent protected-line comparison;
8. NO-BET comparator passed.

At tied high-scoring halftime states such as 2-2, apply a `HIGH-SCORE EQUILIBRIUM MODIFIER`: territory alone is insufficient; require evidence of continued meaningful risk acceptance or repeated high-quality chances.

### Remaining-goal budget

State exactly how many additional goals are needed for full win and for push/half-win/half-loss.

If two or more additional goals are required for a full win, the second-half evidence must support a credible **multi-goal route**. Quarter-goal protection cannot rescue an unsupported multi-goal thesis.

### Score-stable decay

After a high-scoring halftime, re-check the recent second-half interval approximately every 8-10 score-stable minutes. If 15+ second-half minutes pass without a goal, require a fresh current-quality assessment before any new Over/re-entry.

Classify:

- `SECOND-HALF HAZARD: RE-ACCELERATING`
- `SECOND-HALF HAZARD: PERSISTENT BUT UNPROVEN`
- `SECOND-HALF HAZARD: COMPRESSING`

`PERSISTENT BUT UNPROVEN` cannot promote an Over.

### Add-ons

Any post-HT add-on after 3+ first-half goals must independently clear v0.2.47 using second-half-only evidence and its own remaining-goal budget. Do not add merely because the original thesis is alive, cumulative pressure is high, or the line has become more protected.

### Racing-Villarreal audit note

At 2-2 HT the strong gate would have applied. The v0.2.46 shadow promotion at 55:51 — Over 5.25 @1.88 — remains recorded exactly as issued for audit integrity. Under v0.2.47, that state would remain HOLD unless the second-half evidence showed stronger repeated conversion-quality support for the two-goal full-win budget.

The user's separate Ajax observation is qualitative corroboration only until reconstructed/audited; it is not counted evidence or P/L.

## Parallel benchmark mode

- **Arm A — Current audit model:** Football v0.2.47 with the full validator and all retained controls.
- **Arm B — Early totals benchmark:** v0.2.6-v0.2.9 totals philosophy reconstructed with modern synchronization/provider-quality/style/timing controls. After 3+ HT goals, first-half activity cannot count as fresh second-half primary evidence; Arm B may remain more permissive on protected boundaries but must prove the post-HT regime independently.

Arm B outputs only `BENCHMARK SHADOW — DO NOT PLACE` or `BENCHMARK NO BET`.

## Validator interaction

`FOOTBALL_PRE_VERDICT_VALIDATOR.md` remains the mandatory enforcement layer. Its primary-evidence and regime-consistency gates are explicitly subject to stricter active rules; therefore v0.2.47 is mandatory even though the validator file predates this amendment.

After 3+ HT goals, unresolved conversion-quality evidence or an unsupported remaining-goal budget means validator result cannot be PASS.

## Competition/provider exclusion

Per explicit user instruction, **AFC Challenge/AFC Challenge League matches are excluded from the current audit workflow because live-stat coverage is insufficient** unless the user explicitly reverses this exclusion and adequate synchronized live data is available.

## Audit exit criteria

Official football betting cannot resume until all existing audit exit criteria are satisfied, including at least 20 newly assessed shadow decisions after audit start, at least 10 directional-eligible decision points, no retrospective rewriting, no unresolved repeated structural loss pattern, formal simplification review, and explicit user approval.

The early-totals benchmark cannot shorten the audit.

## Response behavior during audit

- Use `SHADOW LEAN — DO NOT PLACE` only when Arm A clears the validator and all active gates.
- Otherwise use `NO BET` or `NO BET — HOLD`.
- Do not issue `OFFICIAL BET` while audit mode is active.
- State the verdict before extended explanation once gates resolve.
- A market that later wins is not a model win unless it was prospectively selected in the synchronized state.

For serious post-HT Over assessments after 3+ first-half goals, include compactly:

- `HT saturation gate:` MODERATE / STRONG
- `Second-half-only sample:` interval/deltas
- `Conversion-quality channel:` PASS / UNRESOLVED / FAIL
- `Second-half hazard:` RE-ACCELERATING / PERSISTENT BUT UNPROVEN / COMPRESSING
- `Remaining goal budget:` exact settlement requirement
- `Best protected total:` exact line/odds
- `Validator status:` PASS / HOLD / FAIL

## Active cross-chat continuation

Use `models/football/handoffs/CHAT_TRANSFER_HANDOFF_2026-08-16_V2.md`. Racing Santander vs Villarreal remains the active match until the user confirms its final state or moves to another target.

## Write boundary

All football audit material, reviews, procedures, handoffs and model updates remain under `models/football/`. `/ledger.json` remains authoritative for official accounting when writes are authorized.