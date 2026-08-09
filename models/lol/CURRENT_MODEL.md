# Current League of Legends Model

**Canonical namespace:** `models/lol/`

- Active model: **LoL v0.3.44**
- Active rules: `models/lol/rules/MODEL_RULES_LOL_V0.3.44.md`
- Prior active deltas: v0.3.43 through v0.3.26 under `models/lol/rules/`
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
2. v0.3.44 through v0.3.26 rule deltas
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

Where conflicts exist, **v0.3.44 controls**.

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

Open position at v0.3.44 activation:

- KT +3.5 kills @1.935 vs DK Game 2 — **OPEN**, 0.25u shadow, entered under v0.3.43.

The KT +3.5 entry is grandfathered as a valid v0.3.43 entry. It is not retroactively voided or reclassified. Any future position-blind reassessment uses v0.3.44.

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
7. **v0.3.44 side-neutral kill-margin distribution and symmetric handicap scan**;
8. independent total-kills low/central/high projection and fight-density reserve;
9. v0.3.43 duration survival-horizon / LCP / observed-stall analysis;
10. line/price availability, minimum odds, correlation and chasing controls;
11. settlement state.

Missing decision-critical data => fail closed with `PASS` or `HOLD`.

## Executable-price rule

A `TAKE` remains **CONDITIONAL / UNRECORDED** until the user confirms the same qualifying executable line/price remained available and was accepted for tracking.

If the line locks, disappears, or deteriorates before confirmation, the recommendation becomes **NO BET / 0u** and is never graded later.

## v0.3.44 Symmetric Kill-Handicap Margin Calibration

Kill handicaps are now modeled from a **side-neutral signed final kill-margin distribution**, not from the attractiveness of a positive cushion.

Define:

`M = favorite final kills - underdog final kills`

Before evaluating a displayed handicap, lock:

- projected total-kill low / central / high range;
- fair central favorite kill margin;
- signed margin bins (`M<=0`, `+1..3`, `+4..6`, `+7..9`, `+10..14`, `15+`);
- favorite map-win probability range;
- conditional favorite-win margin distribution;
- underdog-win/tie branch;
- uncertainty width.

Then price both displayed handicap sides from the **same** distribution.

For half-kill line `H`:

- `P(dog +H covers) = P(M < H)`;
- `P(favorite -H covers) = P(M > H)`.

The favorite wide-win tail must explicitly price team-strength gap, execution simplicity, carry concentration, objective/structure control, reliable engage, chase/cleanup, serial pick-to-objective cascades and terminal base-defense kill inflation.

Underdog resilience remains mechanistic and matchup-adjusted, but theoretical range/waveclear/disengage does not automatically imply a close loss.

The size of a positive cushion and exact future net kills required are **arithmetic only**, not evidence of value.

### Temporary v0.3.44 handicap surcharge

The tracked kill-handicap sample at activation showed **12/12 selections on +kills**. Among 10 settled positions with known results: **3-7, -0.9635u**. This triggers temporary high-friction calibration.

For the next 20 settled new v0.3.44 kill-handicap entries, lower `P_cover` bound must clear break-even by:

- **+7pp** pregame / 0:00;
- **+6pp** early live;
- **+5pp** mid/late live.

These gates apply symmetrically to positive and negative handicaps.

Review after 10 and 20 settled v0.3.44 handicap entries. Track ROI, probability calibration, positive/negative share, line magnitude, team-strength prior, game phase and wide-margin-tail calibration.

Directional skew is a diagnostic, not a quota: do not force negative handicaps merely to balance counts.

Review: `models/lol/reviews/KILL_HANDICAP_DIRECTIONAL_BIAS_REVIEW_2026-08-09.md`.

## Retained v0.3.43 duration controls

Duration remains a survival event with `R = line - current clock`, Latent Conversion Potential, observed stall evidence, first-break elasticity, phase buffers and market-divergence sanity checks.

0-0/low towers after 14:00 is neutral unless observed stall is demonstrated. High-LCP leaders with meaningful gold advantage can create rapid first-break cascades.

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

For open kill-handicap tickets, current thesis uses v0.3.44 even if the original entry was generated under an older version.

## Structural controls retained

- Objective-Control Handicap Veto remains active.
- Draft Cascade-Structure Veto remains active.
- Favorite Structural Margin-Expansion Ladder remains active.
- Pick-cascade fights are serially dependent, not independent.
- Grubs alone do not prove structural acceleration.
- Current-map hard evidence overrides pregame narratives once synchronized live evidence exists.

## Total Kills and Duration remain separate

Total Kills requires current kills, exact kills to line, unresolved fight inventory, objective-density reserve, low/central/high branches and probability controls.

Duration requires v0.3.43 survival-horizon analysis and cannot be inferred from kill pace alone.

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
