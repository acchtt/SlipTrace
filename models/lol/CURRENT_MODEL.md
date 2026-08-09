# Current League of Legends Model

**Canonical namespace:** `models/lol/`

- Active model: **LoL v0.3.45**
- Active rules: `models/lol/rules/MODEL_RULES_LOL_V0.3.45.md`
- Prior active deltas: v0.3.44 through v0.3.26 under `models/lol/rules/`
- Portable baseline context: `models/lol/context/lol-v0.3.25/`
- Mandatory live checklist: `models/lol/procedures/LOL_LIVE_VERDICT_EXECUTION_CHECKLIST_2026-08-09.md`
- Item-verification suspension: `models/lol/procedures/LOL_ITEM_VERIFICATION_SUSPENSION_2026-08-05.md`
- Live fast path: `models/lol/procedures/LOL_LIVE_RESPONSE_FAST_PATH_2026-08-05.md`
- Main procedure: `models/lol/procedures/LOL_BETTING_PROCEDURE.md`
- Connected-stack procedure: `models/lol/procedures/LOL_CONNECTED_STACK_SYNC_AND_RECORDING_PROCEDURE_2026-08-07.md`
- Procedure addenda: `models/lol/procedures/LOL_BETTING_PROCEDURE_ADDENDUM_2026-08-01.md` and `models/lol/procedures/LOL_BETTING_PROCEDURE_ADDENDUM_2026-08-02.md`
- Scoreboard protocol: `models/lol/procedures/LOL_LIVE_SCOREBOARD_READING_PROTOCOL_2026-08-01.md`
- Shared stake policy: `shared/STAKE_POLICY_V2.json`
- Latest handoff: `models/lol/handoffs/CHAT_TRANSFER_HANDOFF_2026-08-08.md`

## Required load order

Every new chat must load these before its first LoL analysis:

1. `models/lol/CURRENT_MODEL.md`
2. v0.3.45 through v0.3.26 rule deltas
3. item-verification suspension
4. v0.3.25 consolidated rules, probation status, calibration handbook
5. mandatory live verdict execution checklist
6. live fast path
7. main betting procedure
8. connected-stack sync/recording procedure
9. both procedure addenda
10. scoreboard protocol
11. pre-match/pregame procedure
12. shared stake policy
13. latest handoff last

Where conflicts exist, **v0.3.45 controls**.

## Official probation

- 13/20 settled/completed
- Record: 7-6
- Net: -0.16425u / -164,250 VND
- Next official wager after explicit restoration: 14
- Standard/default stake after restoration: **0.25u**
- Minimum odds: **1.60**
- Duration markets official-ineligible through wager 20
- Official betting remains **paused** until the user explicitly restores it

## Shadow state

Official wagering remains paused; tracked recommendations are shadow unless explicitly restored.

Recent post-breaker settled sequence:

- DNS +1.5 maps @1.913 vs NS — WIN +0.22825u
- DNS G2 ML @1.979 vs NS — WIN +0.24475u
- EDG +10.5 kills @1.810 vs BLG G2 — LOSS -0.25u
- SK G1 ML @2.239 vs NAVI — LOSS -0.25u
- NAVI +5.5 kills @1.886 vs SK G2 — LOSS -0.25u
- SK +7.5 kills @2.124 vs NAVI G3 — WIN +0.281u
- LNG +9.5 kills @1.970 vs IG G1 — LOSS -0.25u
- Over 33 minutes @2.020 in DK vs KT G1 — LOSS -0.25u

Current post-breaker settled shadow record: **3-5, -0.49600u**. Actual exposure remains **0u**.

Open position at v0.3.45 activation:

- KT +3.5 kills @1.935 vs DK Game 2 — **OPEN**, 0.25u shadow, entered under v0.3.43.

The KT +3.5 entry is grandfathered as a valid v0.3.43 entry. It is not retroactively voided or reclassified. Any future position-blind reassessment uses the current v0.3.45 framework, including v0.3.44 handicap rules.

## Mandatory verdict discipline

First visible line while official wagering remains paused:

- `TAKE — [selection] @[odds] — shadow 0.25u; actual 0u.`
- `PASS — [market/selection] @[odds] — 0u.`
- `HOLD — [market/selection] @[odds] — 0u.`

Before every verdict internally verify:

1. current-frame fingerprint;
2. recorded-position state versus position-blind current thesis state;
3. verified current lineup and team-strength prior when relevant;
4. de-vigged market prior and model-vs-market divergence at pregame/0:00;
5. matchup-adjusted draft function, execution burden and damage-access map;
6. independent moneyline scan;
7. v0.3.44 side-neutral kill-margin distribution and symmetric handicap scan;
8. independent total-kills low/central/high projection and fight-density reserve;
9. **v0.3.45 live-only duration rebuild: survival horizon, two-snapshot persistence, observed stall/acceleration, correlated quiet-state collapse, dead-zone and regime-change repricing**;
10. line/price availability, minimum odds, correlation and chasing controls;
11. settlement state.

Missing decision-critical data => fail closed with `PASS` or `HOLD`.

## Executable-price rule

A `TAKE` remains **CONDITIONAL / UNRECORDED** until the user confirms the same qualifying executable line/price remained available and was accepted for tracking.

If the line locks, disappears, or deteriorates before confirmation, the recommendation becomes **NO BET / 0u** and is never graded later.

## v0.3.45 Duration Rebuild

Tracked Duration history at activation: **1-5, -1.03425u** among six known settled duration positions.

Review: `models/lol/reviews/DURATION_MARKET_REBUILD_REVIEW_2026-08-09.md`.

Duration is now a **specialized live-only market** until a future explicit revision.

### Timing gate

- Pregame / 0:00: no Duration TAKE; analysis-only.
- Before 12:00: no Duration TAKE; `HOLD`.
- 12:00–13:59: high-friction; requires at least two synchronized snapshots >=90 seconds apart demonstrating the same observed mechanism.
- 14:00 onward: may qualify only under the evidence gates below.

### Survival event

For line `L` at clock `t`:

`R = L - t`

Price `P(game survives R more minutes)`.

Lock fast-close, central-close and extension intervals plus central expected finish `C`.

### Correlated quiet-state collapse

Low kills, 0-0/low towers, near-even gold, split/low neutral objectives and no Baron/inhibitor observed at the same snapshot count as at most **one generic quiet-state signal** unless independent mechanisms are demonstrated.

Historical quietness is not future stall evidence.

### Over requires observed stall

An Over requires at least two independent observed stall mechanisms, such as repeated pushes denied, repeated functioning waveclear after lost tempo, repeated failed pick/engage conversion, stable/shrinking leader gold despite initiative, demonstrated repeat disengage/reset, cross-map compensation, or a major objective buff yielding little/no structural gain.

At least one mechanism must persist across temporally separate snapshots except a post-25 observed major-objective conversion failure.

Theoretical waveclear, peel, scaling or disengage does not qualify by itself.

### Under requires observed acceleration

An Under requires at least two independent observed acceleration mechanisms, such as repeated fight-to-structure conversion, first tower unlocking multiple structures, widening gold plus repeatable structure access, Herald/Baron/soul forcing base access, deep-vision repeat picks, side-lane overload, inhibitor/base access, or high LCP demonstrated functioning on the current map.

At least one mechanism must persist across temporally separate snapshots except the post-25 terminal exception.

Aggressive draft theory alone is not enough.

### Two-snapshot persistence

Except for the post-25 terminal Under exception, every Duration TAKE requires >=2 synchronized snapshots separated by >=90 seconds. Claimed stall/acceleration must persist or strengthen.

If the mechanism reverses, widen uncertainty and `HOLD`.

### Post-25 terminal Under exception

After 25:00, one synchronized snapshot may support an Under without two-snapshot persistence only when multiple terminal features align: inhibitor/base access, major structural/gold lead with Baron/Elder/soul, exposed Nexus structures, no credible defender reset, reliable first contact/follow-up, and shortest realistic structure-to-Nexus route inside the survival horizon.

There is no equivalent one-snapshot Over exception.

### Forecast dead zone

Automatic `PASS/HOLD` when either:

1. market line `L` lies inside the central closing interval; or
2. `|L - C| < 2.0 minutes`.

If uncertainty is wider than two minutes, use the wider uncertainty band.

A central estimate barely beyond the line is not value.

### Structural regime-change repricing

Immediately recompute duration after:

- first tower;
- material Herald opening;
- first Baron;
- first inhibitor;
- soul/Elder;
- >=2-tower swing in one conversion cycle;
- short-interval >=3k gold swing;
- repeated major-objective conversion failure.

Do not carry a pre-break forecast through a structural regime change.

### LCP retained but demoted

Retain v0.3.43 Latent Conversion Potential components, but before 25:00 LCP is a mechanism prior only. It must be observed functioning before it can support an Under TAKE.

### Duration rebuild probability buffers

Lower `P_duration` bound must clear break-even by:

- **+6pp** from 12:00 through 17:59;
- **+5pp** from 18:00 through 24:59;
- **+4pp** from 25:00 onward.

Market divergence:

- 0–5pp: normal;
- >5–9pp: require >=2 independent observed current-map mechanisms;
- >9pp: require >=3 mechanisms, including >=1 temporally persistent stall/acceleration mechanism.

Unsupported divergence => shrink toward market, widen uncertainty and `PASS/HOLD`.

### Duration rebuild review window

Review after the next 10 settled v0.3.45 duration positions if that many qualify. Track direction, phase, line-to-central-finish distance, two-snapshot compliance, observed mechanisms, regime changes, closing-time calibration error and ROI.

Do not loosen controls merely because few duration bets qualify.

## v0.3.44 Symmetric Kill-Handicap Margin Calibration retained

Kill handicaps are modeled from a side-neutral signed final kill-margin distribution, not from the attractiveness of a positive cushion.

Define:

`M = favorite final kills - underdog final kills`

Before evaluating a displayed handicap, lock projected total-kill range, fair central favorite margin, signed margin bins (`M<=0`, `+1..3`, `+4..6`, `+7..9`, `+10..14`, `15+`), favorite map-win probability, conditional favorite-win margin distribution, underdog-win/tie branch and uncertainty.

Price both displayed sides from the same distribution.

The favorite wide-win tail explicitly prices team-strength gap, execution simplicity, objective/structure control, reliable engage, chase/cleanup, serial cascades and terminal base-defense kill inflation.

Underdog resilience remains matchup-adjusted. Cushion size and exact future net kills required are arithmetic only, not evidence.

### Temporary handicap surcharge

For the next 20 settled new v0.3.44+ kill-handicap entries, lower `P_cover` bound must clear break-even by:

- +7pp pregame / 0:00;
- +6pp early live;
- +5pp mid/late live.

Apply symmetrically. Review after 10 and 20. Directional skew is diagnostic, not a quota.

Review: `models/lol/reviews/KILL_HANDICAP_DIRECTIONAL_BIAS_REVIEW_2026-08-09.md`.

## Retained v0.3.42 team-strength and draft controls

No numerical pregame team-strength prior without verified/current five-player lineup or explicit user-supplied lineup.

Use current-lineup evidence first, opponent adjustment, role-by-role strength/fit, macro/early/objective/teamfight/lead-conversion traits, de-vigged market anchor and uncertainty band.

Draft tools are matchup-adjusted, not additive. Apply functional counter tax, execution burden, damage-access mapping and normal 0-4pp draft adjustment cap unless >=3 independent functional advantages justify more.

## Retained v0.3.41 position-blind reassessment

Recorded position and current thesis are separate objects. Recompute from scratch on material state changes and explicit reassessment requests.

- ACTIVE: lower bound clears original break-even by current applicable buffer and no hard veto.
- DEGRADED: lower bound above break-even but no longer clears required buffer.
- INVALIDATED: lower bound at/below break-even or hard veto active.
- CONFIRMED: materially strengthened only.

## Structural controls retained

- Objective-Control Handicap Veto remains active.
- Draft Cascade-Structure Veto remains active.
- Favorite Structural Margin-Expansion Ladder remains active.
- Pick-cascade fights are serially dependent, not independent.
- Grubs alone do not prove structural acceleration.
- Current-map hard evidence overrides pregame narratives once synchronized live evidence exists.

## Total Kills and Duration remain separate

Total Kills models fight inventory and kill generation.

Duration models clock survival and structural conversion efficiency.

A Total Kills thesis cannot support a Duration TAKE unless independent v0.3.45 duration evidence qualifies.

## Settlement verification

A screenshot marked `Live` or `Pending` is never final evidence by itself. User correction controls visual bugs. When the user explicitly states **`Final`**, treat the attached/latest synchronized scoreboard as authoritative final-state evidence if the grading statistic is present.

## Retained controls

- 1u = 1,000,000 VND.
- Default individual shadow size while official wagering is paused: 0.25u simulated.
- No automatic stake escalation, martingale behavior or loss chasing.
- Minimum odds 1.60.
- No correlated same-map add-ons unless the user explicitly designates a separate independent bet and it independently qualifies.
- Multiple same-map shadow positions require distinct theses, synchronized state and qualifying prices.
- Item verification remains suspended until explicit restoration; unknown items are neutral and never guessed.
- For active maps: checklist -> verdict -> logging/plugins.

## Connected-stack authority

- GitHub is authoritative for model/rule policy.
- Airtable tracks maps, snapshots and positions.
- Google calibration workbook mirrors completed maps and rule changes.
- If stack records disagree, run the startup sync audit; do not silently merge conflicting states.

## Write boundary

All new LoL rules, procedures, context, reviews and handoffs belong under `models/lol/`. Shared policies belong under `shared/`.
