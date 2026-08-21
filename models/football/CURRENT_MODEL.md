# Current Football Model

**Canonical namespace:** `models/football/`

- Active model: **Football v0.2.49 — AUDIT MODE**
- Organized loading guide: `models/football/ORGANIZED_FILE_LOADING_GUIDE.md`
- Main procedure: `models/football/procedures/FOOTBALL_BETTING_PROCEDURE.md`
- Procedure addendum: `models/football/procedures/FOOTBALL_BETTING_PROCEDURE_ADDENDUM_2026-08-01.md`
- Mandatory validator: `models/football/procedures/FOOTBALL_PRE_VERDICT_VALIDATOR.md`
- Airtable control map: `models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md`
- Active rule directory: `models/football/rules/`
- Active audit: `models/football/reviews/FOOTBALL_DIRECTIONAL_AUDIT_2026-08-11.md`
- Parallel early-totals benchmark: `models/football/reviews/FOOTBALL_V026_V029_BENCHMARK_PROTOCOL_2026-08-11.md`
- Latest process review: `models/football/reviews/FOOTBALL_PROCESS_REVIEW_SETTLEMENT_LESSONS_2026-08-18.md`
- Nõmme enforcement review: `models/football/reviews/FOOTBALL_PROCESS_REVIEW_NOMME_KALJU_EARLY_SOT_EFFICIENCY_2026-08-18.md`
- Prior HT-compression review: `models/football/reviews/FOOTBALL_PROCESS_REVIEW_RACING_VILLARREAL_HT_COMPRESSION_2026-08-16.md`
- Active cross-chat handoff: `models/football/handoffs/CHAT_TRANSFER_HANDOFF_2026-08-21.md`
- Historical baseline: `models/LEGACY_MODEL_CHANGELOG.md`
- Authoritative official betting feed: `/ledger.json`

## Required load order

Load in this order, applying the newest active football rule over older conflicts:

1. `models/football/ORGANIZED_FILE_LOADING_GUIDE.md`
2. `models/LEGACY_MODEL_CHANGELOG.md` — retained pre-v0.2.5 football baseline
3. `models/football/procedures/FOOTBALL_BETTING_PROCEDURE.md`
4. `models/football/procedures/FOOTBALL_BETTING_PROCEDURE_ADDENDUM_2026-08-01.md`
5. `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.5.md` through `MODEL_RULES_FOOTBALL_V0.2.49.md`, ascending
6. `models/football/procedures/FOOTBALL_PRE_VERDICT_VALIDATOR.md`
7. `models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md`
8. `models/football/reviews/FOOTBALL_DIRECTIONAL_AUDIT_2026-08-11.md`
9. `models/football/reviews/FOOTBALL_V026_V029_BENCHMARK_PROTOCOL_2026-08-11.md`
10. `models/football/reviews/FOOTBALL_PROCESS_REVIEW_NOMME_KALJU_EARLY_SOT_EFFICIENCY_2026-08-18.md`
11. `models/football/reviews/FOOTBALL_PROCESS_REVIEW_SETTLEMENT_LESSONS_2026-08-18.md`
12. `models/football/handoffs/CHAT_TRANSFER_HANDOFF_2026-08-21.md` as the active continuation context
13. `/ledger.json` only when official record, bankroll, exposure, placement, or settlement status is relevant and explicitly authorized

Older handoffs are historical context only and must not override v0.2.49.

## Audit-mode operating values

- 1u = 1,000,000 VND.
- Minimum odds reference = 1.70 unless explicitly overridden.
- Official football betting is **PAUSED**.
- Execution mode is **SHADOW CALIBRATION ONLY** until audit exit criteria are met and the user explicitly approves resumption.
- Ledger writes remain **ON HOLD** until explicitly approved.
- Normal current audit small-test convention = 0.125u when a simulated shadow stake is needed and no newer user instruction supersedes it.
- Directional AH/DNB/ML selections remain quarantined from official promotion.
- Totals are not automatically approved; they remain subject to synchronization, settlement, provider-quality, style, timing, reset, pressure-inflection, halftime-compression, goal-budget, team-profile and market-scan gates.
- xG/xGOT are secondary only.
- Every material checkpoint must preserve exact score/minute/line/odds synchronization.
- Airtable Decision State + Validator PASS remain mandatory for every shadow/executable verdict. If decision-state validation is unavailable, output `NO BET — HOLD — decision-state validation unavailable`.
- Raw shots/SOT cannot be relabeled into independent primary channels; the same event cluster cannot count twice; persistence requires comparable score-stable evidence or a clearly repeated sequence.
- Evidence strength must match the exact settlement burden.
- Team goals-for/goals-against profile is a structural prior whose importance increases with remaining-goal burden.
- Live Unders require affirmative current deceleration/suppression, not conservation narratives alone.
- When an Over thesis clears all gates, prefer the lowest eligible protected boundary that preserves acceptable price quality and reduces unnecessary goal-budget burden.

## Retained active layers

### v0.2.43 — style/post-goal layer

Before every serious preview and before the first live recommendation, maintain evidence-based style/personnel context. After every goal, perform the full tactical/state reset and require fresh post-goal evidence unless an active fallback explicitly applies.

### v0.2.44 — timeliness

If a synchronized state is stable and all applicable gates are complete, deliver the verdict immediately. Do not add reassurance checkpoints after PASS.

A material event before delivery invalidates the pending quote as `STATE-CHANGE RACE — NOT COUNTED`, followed by reset and reprice.

### v0.2.45 — terminal-goal / leader-driven fallback

A leader may fund the remaining Over goal budget itself where the exact live evidence and protected line support that route. Opponent contribution is not universally mandatory.

### v0.2.46 — pre-goal pressure inflection

From approximately 35:00 to halftime, compare the recent 5-10 minute interval with the prior synchronized state. A one-team surge may support an attacker-driven Over if it can plausibly fund the protected remaining goal budget. Do not impose a goal-confirmation tax.

## v0.2.47 — High-Scoring Halftime Compression / Goal-Saturation Gate

- 0-2 HT goals: normal halftime reset.
- 3 HT goals: `HT COMPRESSION GATE — MODERATE`.
- 4+ HT goals: `HT GOAL-SATURATION GATE — STRONG`.
- After 3+ HT goals, first-half activity is context only and cannot satisfy new second-half Over evidence.
- A fresh second-half conversion-quality channel is mandatory for Over promotion.
- For 4+ HT goals, normally require a resolved reset, score-stable 2H sample, two independent 2H primary channels, at least one conversion-quality channel, exact remaining-goal budget, protected-line comparison and NO-BET comparator.
- `SECOND-HALF HAZARD: PERSISTENT BUT UNPROVEN` cannot promote an Over.
- Under also cannot be promoted merely from saturation/conservation; require observed suppression.

## v0.2.48 — Dominant Goal-Carrier Slate Priority — ACTIVE EMPHASIS

The 2026-08-20 European slate review showed a pre-match selection-allocation error: good/notable European teams were being ranked too similarly to elite or near-elite attacking favorites that could realistically score 3+ by themselves against weaker opposition.

### Goal-carrier tiers

**T1 — Dominant Goal Carrier**

Matchup-specific profile with a credible solo 3+ goal route. Normally supported by strong attacking talent, lineup quality, material opponent mismatch, suitable tactical access and acceptable competition/format incentives. Ajax-, Benfica-, Beşiktaş-type mismatches are examples of the profile, not permanent hard-coded membership.

**T2 — Strong Attacking Side / Secondary Carrier**

Strong team with meaningful attacking quality but a less reliable solo 3+ route in the current matchup. Salzburg-, Copenhagen-, Midtjylland-, Nordsjælland-type situations may fall here depending on opponent, lineup and format.

**T3 — Shared-Route / Two-Sided Over**

The total depends materially on both teams contributing or on a balanced open-game route.

### Ranking rule

Initial slate monitoring priority is normally:

1. T1 dominant-carrier mismatch with strong/acceptable lineup and low format drag.
2. T1 with one material uncertainty.
3. T2 strong favorite with plausible solo route.
4. High-quality T3 two-sided open match.
5. Lower-information/provider-quality matches.

Do not rank a T2/T3 match above a clear T1 carrier simply because the lower-tier game looks more balanced or theoretically open.

### One-team funding rule

A one-team blowout path is a first-class Over environment. Before penalizing a match for weak underdog attack, ask whether the stronger team can plausibly cash the target total by itself.

This affects **ranking and monitoring priority only**. It does not replace the live validator.

### Monitoring allocation / anti-sunk-cost rule

When matches overlap, T1 carriers receive the first checkpoint and primary monitoring slot. Do not keep repeatedly checking an unproven T2/T3 match while a higher-ranked T1 carrier begins, unless the existing match has already reached a materially stronger synchronized live state.

### Required ranking fields

For serious slate candidates, record:

- `Goal-carrier tier:` T1 / T2 / T3
- `Primary carrier:` team or shared
- `Solo 3+ route:` STRONG / PLAUSIBLE / WEAK
- `Opponent mismatch:` STRONG / MODERATE / LOW
- `Lineup attack status:` FULL / ACCEPTABLE / ROTATED / UNKNOWN
- `Format/incentive drag:` LOW / MODERATE / HIGH
- `Initial monitoring priority:` rank number

These fields are priors and are not live evidence channels.

### Separate ranking tracker from entry P/L

Track prospectively assigned slate ranking separately from betting results:

- final total goals;
- O2.5 hit/miss;
- T1 carrier final goals where applicable;
- 3+ and 4+ total-goal hit indicators;
- assigned tier and rank.

Shadow P/L continues to include only prospectively issued synchronized PASS entries. A high-scoring ranked match with no entry is a selection success / execution miss, not a betting win.

### Anti-hindsight rule

Tier labels must be assigned before kickoff or before the result is known. Do not promote a team to T1 because it later scored heavily, and do not demote a T1 carrier solely because one match finished 1-0.

## v0.2.49 — Team Goal/Concede Profile Weighting Gate — ACTIVE EMPHASIS

Team goals-for and goals-against profile must now carry substantially more weight before slate classification and live Over promotion.

### Structural profile requirements

For serious candidates, assess:

- recent goals scored per match and 2+/3+ scoring frequency;
- recent goals conceded per match and 2+/3+ concession frequency;
- frequency of being held to 0-1 goals;
- clean-sheet / one-goal concession tendency;
- home/away split where relevant;
- opponent quality and competition context;
- lineup attack/defense availability;
- whether multi-goal results are repeatable or outlier-driven;
- post-lead behavior where evidence is available.

### Goal-route matrix

Explicitly compare:

1. primary carrier goals-for vs opponent goals-against;
2. opponent goals-for vs primary carrier goals-against;
3. primary carrier multi-goal frequency vs opponent multi-goal concession frequency;
4. one-team carrier route vs two-sided contribution route.

A one-team Over remains valid, but the solo route must be supported by demonstrated multi-goal capacity rather than reputation, possession, forced-chase incentive or raw shot volume alone.

### Team profile support field

Every serious live Over candidate should be classified as:

- `TEAM PROFILE SUPPORT: STRONG`
- `TEAM PROFILE SUPPORT: ACCEPTABLE`
- `TEAM PROFILE SUPPORT: CONFLICTING`
- `TEAM PROFILE SUPPORT: UNKNOWN`

### Remaining-goal burden

- One additional goal: ACCEPTABLE profile support may be enough with strong live evidence.
- Two additional goals: normally require at least ACCEPTABLE profile support plus repeated live conversion quality.
- Three or more additional goals: normally require STRONG profile support plus clearly re-accelerating live evidence; one upgraded snapshot is insufficient.
- If profile is CONFLICTING, pressure/SOT dominance alone cannot clear the Over gate.

### Revised T1 gate

T1 should normally require strong multi-goal scoring history relative to opponent level plus meaningful opponent 2+/3+ concession vulnerability, or a clearly exceptional matchup mismatch. If the carrier is commonly held to 0-1 or the opponent repeatedly limits stronger teams to 0-1, cap at T2 unless extraordinary evidence exists.

### No arbitrary coefficient

Do not invent a fixed numeric weighting such as `40% profile / 60% live` until prospective calibration supports it. Profile is a gating prior whose burden rises with remaining goals required.

## Parallel benchmark mode

- **Arm A — Current audit model:** Football v0.2.49 with the full validator and all retained controls.
- **Arm B — Early totals benchmark:** reconstructed v0.2.6-v0.2.9 totals philosophy with modern synchronization/provider-quality/style/timing controls and v0.2.47 post-HT separation.

Arm B outputs only `BENCHMARK SHADOW — DO NOT PLACE` or `BENCHMARK NO BET` and cannot shorten the audit.

## Validator interaction

`FOOTBALL_PRE_VERDICT_VALIDATOR.md` remains the mandatory execution layer. v0.2.49 adds the question: `Does the team goals-for / goals-against profile support the exact remaining goal burden?`

If the profile is materially conflicting and the live state is not exceptional enough to overcome that conflict, output `NO BET — HOLD — team-profile burden not cleared`.

Goal-carrier tier remains a prematch/slate prior only; synchronized live evidence, conversion quality, independence, persistence, utility, settlement and regime consistency remain mandatory.

## Competition/provider exclusion

AFC Challenge/AFC Challenge League matches remain excluded from the current audit workflow unless explicitly reversed and adequate synchronized live data is available.

## Audit exit criteria

Official football betting cannot resume until existing audit exit criteria are satisfied, including the required shadow-decision sample, directional-eligible decision points, no retrospective rewriting, no unresolved repeated structural loss pattern, formal simplification review, and explicit user approval.

## Response behavior during audit

- Use `SHADOW LEAN — DO NOT PLACE` only when Arm A clears the validator and all active gates.
- Otherwise use `NO BET` or `NO BET — HOLD`.
- Do not issue `OFFICIAL BET` while audit mode is active.
- State the verdict before extended explanation once gates resolve.
- A market that later wins is not a model win unless it was prospectively selected in the synchronized state.
- When ranking a slate, distinguish T1/T2/T3 and put T1 solo-carrier routes first when justified.
- Before promoting an Over with 2+ additional goals required, state or internally verify team-profile support and do not let raw pressure erase a conflicting scoring/conceding baseline.

## Operating principle

**Rank goal carriers by demonstrated goal production and opponent concession vulnerability, not badges or live pressure alone. Treat goals-for/goals-against profile as structural evidence. The higher the remaining goal burden, the heavier the profile gate; then let synchronized live evidence decide timing.**