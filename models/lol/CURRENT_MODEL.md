# Current League of Legends Model

**Canonical namespace:** `models/lol/`

- Active model: **LoL v0.3.43**
- Active rules: `models/lol/rules/MODEL_RULES_LOL_V0.3.43.md`
- Prior active deltas: v0.3.42 through v0.3.26 under `models/lol/rules/`
- Portable baseline context: `models/lol/context/lol-v0.3.25/`
- Mandatory live checklist: `models/lol/procedures/LOL_LIVE_VERDICT_EXECUTION_CHECKLIST_2026-08-08.md`
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
2. v0.3.43 through v0.3.26 rule deltas
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

Where conflicts exist, **v0.3.43 controls**.

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

Recent post-breaker sequence after the completed 20-map circuit breaker:

- DNS +1.5 maps @1.913 vs NS — WIN +0.22825u
- DNS G2 ML @1.979 vs NS — WIN +0.24475u
- EDG +10.5 kills @1.810 vs BLG G2 — LOSS -0.25u
- SK G1 ML @2.239 vs NAVI — LOSS -0.25u
- NAVI +5.5 kills @1.886 vs SK G2 — LOSS -0.25u
- SK +7.5 kills @2.124 vs NAVI G3 — WIN +0.281u
- LNG +9.5 kills @1.970 vs IG G1 — LOSS -0.25u
- Over 33 minutes @2.020 in DK vs KT G1 — LOSS -0.25u

Current post-breaker shadow record: **3-5, -0.49600u**. Actual exposure remains **0u**.

## Mandatory verdict discipline

First visible line while official wagering remains paused:

- `TAKE — [selection] @[odds] — shadow 0.25u; actual 0u.`
- `PASS — [market/selection] @[odds] — 0u.`
- `HOLD — [market/selection] @[odds] — 0u.`

Before every live verdict internally verify:

1. current-frame fingerprint;
2. recorded-position state versus **position-blind current thesis state**;
3. verified current lineup and representative team-strength prior when team strength is decision-relevant;
4. de-vigged market prior and model-vs-market divergence when pregame/0:00;
5. matchup-adjusted draft function, execution burden and damage-access map;
6. independent moneyline scan including v0.3.40/v0.3.42 probability gates;
7. phase-aware exact kill-handicap arithmetic, conditional winner/margin decomposition, cascade test, mechanistic resilience and structural vetoes;
8. independent total-kills low/central/high projection and fight-density reserve;
9. independent duration survival-horizon analysis including `R = line - clock`, latent conversion potential, observed stall evidence, first-break elasticity, fast/central/extension branches and v0.3.43 duration divergence/buffer gates;
10. line/price availability, minimum odds, correlation and chasing controls;
11. settlement state.

Missing decision-critical data => fail closed with `PASS` or `HOLD`.

## Executable-price rule

A `TAKE` remains **CONDITIONAL / UNRECORDED** until the user confirms the same qualifying executable line/price remained available and was accepted for tracking.

If the line locks, disappears, or deteriorates before confirmation, the recommendation becomes **NO BET / 0u** and is never graded later.

## v0.3.43 Live Duration Survival and Latent Conversion

Duration is modeled as a **survival event**. For duration line `L` at current clock `t`, calculate `R = L - t` and price the probability that the map survives at least `R` additional minutes.

Before any duration TAKE, lock fast-close, central and extension branches, the leader's state trajectory, the fastest realistic structure-to-Nexus route, and the first structural break as a possible regime-change event.

### Structural absence is neutral

From 14:00 onward, 0-0 or low towers is neutral by default. It does **not** count as positive Over evidence unless at least two independent observed stall signals show that conversion is actually being denied.

Theoretical waveclear, peel, scaling, split dragons or generic comeback tools are not observed stall evidence until demonstrated on the current map.

### Latent Conversion Potential

Score the advantaged team across six matchup-adjusted accelerants:

1. reliable first contact;
2. numbers creation / globals / fast collapse;
3. safe follow-up damage / chase;
4. wave and structure access / side pressure / siege / dive;
5. objective leverage into structures;
6. functional suppression of defender waveclear/disengage/peel.

`LCP 0-1 = low`, `2 = moderate`, `3-4 = high`, `5-6 = very high`.

When `LCP >=3`, towerlessness cannot by itself support an Over.

### Observed stall evidence

Qualifying signals include repeated pushes neutralized without tower loss, repeated successful waveclear after lost tempo, multiple failed leader picks with no conversion, leader gold lead stable/shrinking across synchronized snapshots despite initiative, repeated cross-map compensation, demonstrated repeat disengage/reset, or a major objective buff producing little/no structural gain.

### First-break elasticity

Before an Over, ask whether the next successful pick/objective/first tower can realistically produce **two or more additional structures** before the defender fully resets. If yes, widen the fast-close branch and treat the cascade as serially dependent.

### High-friction Over veto

`PASS/HOLD` a live Over when all are true absent exceptional synchronized counterevidence:

- leader >=+1.5k gold after 14:00;
- Over requires >=15 additional minutes of survival;
- leader `LCP >=3`;
- fewer than two observed stall signals.

This veto is independent of current tower count.

### Duration probability buffers

For a duration TAKE, lower end of the modeled probability range must clear break-even by:

- +5pp before 18:00;
- +4pp from 18:00 through 24:59;
- +3pp from 25:00 onward.

### Duration market-divergence sanity gate

Central model probability versus market break-even:

- 0-5pp: normal;
- >5-9pp: require at least two independent current-map reasons;
- >9pp: require at least three independent current-map reasons, including at least one observed stall/acceleration reason rather than draft theory.

Unsupported disagreement => shrink toward market, widen uncertainty and fail closed if the lower-bound buffer is not met.

### DK vs KT G1 calibration

At 16:00, KT led 5-3 and +2.1k with 0-0 towers and 1-1 dragons. Over 33 @2.020 required ~17 more minutes and was estimated at 59-66% despite ~49.5% break-even.

KT's Pantheon/Nautilus first contact, Pantheon/Ryze numbers creation, Ezreal/Ryze follow-up and Olaf run-through pressure created high latent conversion potential. DK's Taliyah/Milio stall tools were theoretical rather than demonstrated. Under v0.3.43 the correct verdict is `PASS/HOLD`.

Review: `models/lol/reviews/DK_KT_GAME1_DURATION_REVIEW_2026-08-09.md`.

## v0.3.42 Verified Team-Strength Prior

No numerical team-strength or map-win prior may be issued until the current expected/confirmed five-player lineup is verified or explicitly supplied by the user.

When the roster has materially changed, downweight stale full-year/team-name statistics and prioritize the current five. Build strength in this order: verified lineup -> current-lineup results -> opponent-adjusted quality -> role-by-role strength/fit -> macro/early/objective/lead conversion -> map side/format if verified -> de-vigged market anchor -> uncertainty band.

The role matrix must distinguish material edge / slight edge / even / slight disadvantage / material disadvantage across all five roles and separately score macro coordination, early creation, objective setup, teamfight execution, lead conversion, comeback resistance and volatility.

### Market-divergence sanity gate

The market is an external calibration anchor, not an oracle.

Before draft, if the model central probability differs from the de-vigged market by:

- 0-6pp: normal;
- >6-10pp: require at least two independent verified reasons;
- >10pp: require at least three independent verified reasons, including one current-lineup-performance reason and one matchup/role reason.

Absent those reasons, shrink toward the market until divergence is <=6pp and widen uncertainty.

**Uncertainty is not edge.** Do not convert a wide band into automatic underdog value.

Series probability and single-map probability remain separate objects.

## v0.3.42 Matchup-Adjusted Draft Function

Draft scoring is relative. A composition gets credit for a tool only if it remains functional into the opponent's actual answers.

Test:

- safe range vs engage/flank/global access;
- waveclear vs siege/side pressure/dive;
- disengage vs reliable multi-axis or repeat engage;
- peel vs simultaneous dive routes;
- engage vs anti-engage/terrain/mobility denial;
- objective access vs poke/zone/choke/face-check burden;
- return kills vs cleanup/chase/ranged follow-up;
- scaling vs whether carries can actually deliver damage safely.

A nominal tool directly suppressed by an opposing interaction is weakened/nonfunctional, not a full resilience point.

### Functional Counter Tax

If one opposing tool materially degrades two or more core functions of the other composition, those functions cannot be counted at full value. Apply this by function, not by hard-coded champion name.

### Execution-burden adjustment

Identify the simpler first successful sequence, the side requiring more precise spacing/flank/targeting, independent fight-start channels, and which composition fails first when one role falls behind.

When the stronger team also has the simpler/reliable execution path, increase clean-win and high-margin branches. Underdog theoretical tools receive less weight when accessing them requires materially higher execution precision.

### Damage-access map

Before any post-draft TAKE identify who can hit frontline safely, who can access backline, who must cross enemy control, easiest carry to isolate, main-DPS uptime after first contact, and retreating-side return-kill capability.

Multiple damage champions do not equal handicap resilience if they cannot safely access targets.

## v0.3.42 Conditional Kill-Margin Decomposition

For a positive kill handicap:

`P(dog +H covers) = P(dog wins) + P(favorite wins AND favorite margin <= H)`

Required branches: underdog wins; favorite wins close; favorite wins moderate; favorite wins high-margin.

The close/moderate/high-margin probabilities must be conditional on the favorite winning and must reflect team-strength gap, draft execution asymmetry, expected total kills and cascade architecture.

A high dog-cover estimate is invalid if it simultaneously assumes a large favorite win probability and an unsupported high close-loss rate.

Pregame positive-handicap lower-bound edge requirement remains +5pp over break-even; early-live +4pp; mid/late +3pp.

## v0.3.42 Draft Adjustment Cap

Normal draft move from the verified pre-draft map prior remains **0-4pp**. A move >4pp requires at least three independent **functional** advantages after opponent-counter testing.

Draft should rarely erase a large verified team-strength gap by itself.

## LNG vs IG G1 calibration

Verified lineups supplied by the user:

- LNG: sheer / Weiwei / Nia / 1xn / Missing
- IG: TheShy / Wei / Rookie / Assum / Meiko

Draft:

- LNG: K'Sante / Naafiri / Akali / Corki / Nautilus
- IG: Olaf / Jarvan IV / Ryze / Kai'Sa / Poppy

0:00 market included IG ML 1.231, LNG ML 4.032, IG -9.5 kills 1.793, LNG +9.5 kills 1.970. LNG +9.5 was recorded for 0.25u shadow. Final: IG 26-13 LNG; position lost -0.25u.

The failure was process-level, not simply result-level. Team strength moved too far across successive assessments because roster verification and market-divergence controls were weak. Draft analysis then over-counted nominal LNG resilience without sufficiently testing it against IG's mobility denial, multi-axis target access, run-through pressure and cleaner execution path. The model also failed to decompose the dog cover probability into LNG-win probability plus the conditional probability of an IG win staying within nine kills.

Under v0.3.42, this selection is a `PASS` absent a supportable conditional close-loss distribution.

## v0.3.41 Position-Blind Reassessment retained

Recorded positions and current thesis are separate objects. On every material state change, and whenever the user explicitly asks to reassess drafts/compositions, recompute current thesis from scratch without anchoring to the entry recommendation, recorded position, sunk stake, prior wording or sportsbook move.

For the original recorded selection:

- **ACTIVE:** lower bound still clears original entry break-even by the applicable phase buffer and no hard veto is active;
- **DEGRADED:** lower bound is above break-even but no longer clears the required buffer;
- **INVALIDATED:** lower bound is at/below break-even or a hard veto is active;
- **CONFIRMED:** materially strengthened only.

Positive-handicap resilience remains mechanistic: safe range, disengage/reset, waveclear/base defense, anti-dive/peel, objective-contest access and return-kill reliability.

### Draft Cascade-Structure Veto retained

For a positive kill handicap, `PASS` unless strong counterevidence exists when the opponent has a gold lead, structural lead/repeatable structure access, a clear pick-to-kill-to-objective cascade with at least three meaningful components, while the positive-handicap side lacks demonstrated level-3+ return-kill/contest evidence or at least three credible matchup-adjusted resilience categories.

Split neutral-objective control does not cancel this veto.

## v0.3.40 Pregame ML calibration retained

For pregame/0:00 ML:

- construct baseline map `P_win` range before draft;
- separate series prior from map prior;
- apply verified side;
- apply disciplined matchup-adjusted draft adjustment;
- apply supported execution/form adjustment;
- calculate break-even;
- require lower end of final `P_win` range to clear break-even by at least +3pp.

## v0.3.40 Early Total-Kills calibration retained

For total-kills TAKEs:

- early live: lower end must clear break-even by +4pp;
- mid/late: lower end must clear by +3pp.

High fight density and multiple fight-creation channels widen the high-kill branch and penalize early Unders.

## v0.3.39 Phase-Aware Kill-Handicap calibration retained

Require lower end of `P_cover` to clear break-even by:

- +5pp pregame positive handicap;
- +4pp early live;
- +3pp mid/late.

Pregame positive handicaps remain high-friction and require projected total kills, final-margin branches, H/T scaling, conditional winner/margin decomposition, explicit probability edge and cascade-tail assessment.

## Structural controls retained

- Objective-Control Handicap Veto remains active.
- Favorite Structural Margin-Expansion Ladder remains active.
- Pick-cascade fights are serially dependent, not independent.
- Grubs alone do not prove structural acceleration.
- Current-map hard evidence overrides pregame narratives once synchronized live evidence exists.

## Total Kills and Duration remain separate

Total Kills requires current kills, exact kills to line, unresolved fight inventory, objective-density reserve, low/central/high branches and probability controls.

Duration requires the v0.3.43 survival-horizon calculation, latent conversion potential, observed stall evidence, first-break elasticity, fast/central/extension branches, structure/base route and phase-aware probability/divergence gates.

Retained duration corrections remain mandatory: no Over before 10:00 without two genuine stall signals beyond towerlessness; >=6 kills by 8:00 widens fast-finish risk; >=14 kills by 16:00 prevents 0-0 towers from confirming an Over; around 20:00 a >=+5k gold and +2-tower leader invalidates short Overs absent exceptional counterevidence; comeback tools widen distribution; Grubs alone do not prove completed acceleration; kill suppression does not equal time compression.

## Settlement verification

A screenshot marked `Live` or `Pending` is never final evidence by itself. User correction controls visual bugs. When the user explicitly states **`Final`**, treat the attached/latest synchronized scoreboard as authoritative final-state evidence even if UI says `Live`, provided the grading statistic is present.

## Retained controls

- 1u = 1,000,000 VND.
- Default individual shadow size while official wagering is paused: 0.25u simulated.
- No automatic stake escalation, martingale behavior or loss chasing.
- Minimum odds 1.60.
- No correlated same-map add-ons unless the user explicitly designates a separate independent bet and it independently qualifies.
- Multiple same-map shadow positions require distinct theses, synchronized state and qualifying prices.
- Item verification remains suspended until explicit restoration; unknown items are neutral and never guessed.
- Apply dominance override, multi-snapshot stabilization, role-gold breadth, observed-execution scoring, late objective-density kill reserves, soul-cascade routing, Baron acquisition/conversion separation and comeback-shape correction.
- For active live maps: checklist -> verdict -> logging/plugins.

## Connected-stack authority

- GitHub is authoritative for model/rule policy.
- Airtable tracks maps, snapshots and positions.
- Google calibration workbook mirrors completed maps and rule changes.
- If stack records disagree, run the startup sync audit; do not silently merge conflicting states.

## Write boundary

All new LoL rules, procedures, context, reviews and handoffs belong under `models/lol/`. Shared policies belong under `shared/`.
