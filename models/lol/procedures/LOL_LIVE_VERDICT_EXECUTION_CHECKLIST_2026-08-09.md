# LoL Live Verdict Execution Checklist — 2026-08-09

**Status:** Mandatory  
**Authority:** LoL v0.3.45  
**Purpose:** mechanical pre-verdict gate for every League of Legends pregame/live snapshot.

Complete internally before every verdict. User-facing output remains brief.

## A. Current-frame fingerprint

Verify from newest synchronized evidence:

- event / game / sides;
- game clock;
- kills and orientation;
- gold lead and direction;
- towers / inhibitors / base access;
- dragons / soul point / soul;
- Void Grubs / Herald;
- Baron / Elder;
- exact market line and odds;
- market open / locked / delayed status.

Do not carry forward a prior mutable field unless explicitly reconciled.

## B. Position-state check

Set exactly one:

- `RECORDED POSITION: NONE`
- `CONDITIONAL / UNRECORDED`
- `RECORDED SHADOW POSITION`

If a position exists, separately set thesis state: `ACTIVE / DEGRADED / INVALIDATED / CONFIRMED`.

### B1. Position-blind reassessment

On every material new snapshot, and whenever the user asks to reassess draft/compositions, recompute the current thesis from scratch.

Do not use recorded entry, prior recommendation, sunk stake, desire for consistency, or adverse market movement as supporting evidence.

- ACTIVE: lower-bound probability still clears original break-even by required current buffer and no hard veto.
- DEGRADED: lower bound remains above break-even but no longer clears buffer.
- INVALIDATED: lower bound at/below break-even or a hard veto applies.
- CONFIRMED: materially strengthened only.

Mandatory triggers include explicit reassessment request; >=2k meaningful gold swing; tower differential change >=2; first Baron/Elder; inhibitor/base access; material dragon/soul alignment; >=2 net-kill swing; repeated failure of a theoretical defensive mechanism; demonstrated pick-to-objective cascade.

## C. Verified team-strength gate — v0.3.42+

Before any pregame/0:00 numeric team-strength or map prior:

1. verify/obtain current five-player lineup;
2. identify roster discontinuity;
3. prioritize current-lineup results;
4. adjust for opponent quality;
5. score role-by-role current strength/fit;
6. separately score macro, early creation, objective setup, teamfight execution, lead conversion, comeback resistance and volatility;
7. establish uncertainty band.

If lineup or representative sample is uncertain, fail closed on a numeric edge.

### C1. Market-divergence sanity gate

Calculate de-vigged pregame market prior.

- 0–6pp model-vs-market difference: normal;
- >6–10pp: require >=2 independent verified reasons;
- >10pp: require >=3 independent verified reasons including current-lineup performance and matchup/role evidence.

Unsupported divergence => shrink toward market and widen uncertainty. Uncertainty is not edge.

## D. Matchup-adjusted draft gate — v0.3.42+

Do not count draft tools additively. Test:

- range vs engage/flank/global access;
- waveclear vs siege/side/dive;
- disengage vs repeat/multi-axis engage;
- peel vs simultaneous dive routes;
- engage vs anti-engage/terrain/mobility denial;
- objective access vs poke/zone/choke/face-check burden;
- return kills vs cleanup/chase/ranged follow-up;
- scaling vs actual safe damage delivery.

Apply Functional Counter Tax, execution burden and damage-access mapping. Normal draft adjustment is 0–4pp; >4pp requires >=3 independent functional advantages after counter testing.

## E. Moneyline gate

For ML:

- odds >=1.60;
- map prior distinct from series prior;
- no automatic transfer from team strength to handicap confidence;
- pregame lower `P_win` bound must clear break-even by >=3pp.

Failure => `PASS/HOLD`.

## F. Kill-handicap gate — v0.3.44 retained

Kill-handicap analysis is side-neutral and distribution-first.

### F1. Phase

Set `PREGAME / 0:00`, `EARLY LIVE`, or `MID/LATE LIVE`.

### F2. Define favorite and signed margin

`M = favorite final kills - underdog final kills`.

Pregame favorite = de-vigged map favorite after lineup/draft reconciliation. Live favorite = synchronized live ML favorite when available, otherwise position-blind current-state favorite.

### F3. Blind fair-margin lock

Before using displayed handicap as evidence, lock:

1. current kill margin;
2. final total-kill low / central / high range;
3. fair central favorite kill margin;
4. signed final-margin distribution;
5. favorite map-win probability range;
6. conditional favorite-win margin distribution;
7. underdog-win/tie branch;
8. uncertainty width.

Minimum bins: `M<=0`, `+1..3`, `+4..6`, `+7..9`, `+10..14`, `15+`.

### F4. Symmetric pricing

For half-kill line `H`:

- `P(dog +H covers) = P(M < H)`;
- `P(favorite -H covers) = P(M > H)`.

Price both displayed sides from the same distribution before selecting either side.

### F5. Wide-win and resilience branches

Favorite high-margin tail must price team-strength gap, lead conversion, repeatable engage, target access, structure/objective pressure, chase/cleanup, serial cascades and terminal kill inflation.

Underdog resilience remains matchup-adjusted: safe range, disengage/reset, waveclear/base defense, anti-dive/peel, objective contest and return-kill reliability. Theoretical tools only count when they plausibly reduce the favorite wide-margin tail.

### F6. v0.3.44 temporary surcharge

For next 20 settled new v0.3.44+ handicap entries, lower `P_cover` bound must clear break-even by:

- +7pp pregame;
- +6pp early live;
- +5pp mid/late.

Apply symmetrically. Review after 10 and 20. Directional skew is diagnostic, not a quota.

Retain Objective-Control Handicap Veto and Draft Cascade-Structure Veto.

## G. Total-kills gate

Calculate:

- current total kills;
- whole kills to cross line;
- unresolved major fight triggers;
- low/central/high remaining-kill branches;
- objective-density reserve;
- clean-close/return-kill suppression state;
- global/engage/cascade fight-creation channels.

For TAKE, lower probability bound must clear break-even by +4pp early live and +3pp mid/late.

High early fight density and >=4 collective fight-creation channels widen the high-kill branch and penalize early Unders.

**Total Kills is never inferred from Duration, and Duration is never inferred from Total Kills.**

## H. Duration gate — v0.3.45 rebuild

Duration is a specialized **live-only** market.

### H1. Hard timing gates

- Pregame / 0:00 duration: `PASS/HOLD`; no TAKE.
- Before 12:00: `HOLD`; no TAKE.
- 12:00–13:59: high-friction; requires all normal evidence plus two synchronized snapshots >=90 seconds apart showing the same mechanism.
- 14:00 onward: may qualify only through the gates below.

### H2. Survival horizon

Calculate:

`R = duration line L - current game clock t`.

Price `P(game survives R more minutes)`.

Lock fast-close interval, central closing interval, extension interval and central expected finish `C`.

### H3. Correlated quiet-state collapse

Low kills, 0-0/low towers, near-even gold, split/low objectives and no Baron/inhibitor at one snapshot count as at most **one generic quiet-state signal** unless separate causal mechanisms are demonstrated.

Historical quietness is not observed future stall.

### H4. Over requires observed stall

Over requires >=2 independent observed stall mechanisms, such as repeated pushes denied, repeated successful waveclear after lost tempo, repeated failed pick/engage conversion, stable/shrinking leader gold despite initiative, demonstrated repeat disengage/reset, cross-map compensation, or major objective buff yielding little/no structure.

At least one stall mechanism must persist across temporally separate snapshots unless after 25:00 a major objective conversion failure has just been directly observed.

Theoretical waveclear/peel/scaling/disengage is not enough.

### H5. Under requires observed acceleration

Under requires >=2 independent observed acceleration mechanisms, such as repeated fight-to-structure conversion, first tower unlocking multiple structures, widening gold plus structure access, Herald/Baron/soul forcing base access, deep-vision repeat picks, side-lane overload, inhibitor/base access, or functioning high-LCP conversion.

At least one acceleration mechanism must persist across temporally separate snapshots unless the post-25 terminal exception applies.

Aggressive draft theory alone is not enough.

### H6. Two-snapshot persistence gate

Except for H7, every duration TAKE requires >=2 synchronized snapshots separated by >=90 seconds. The claimed stall/acceleration mechanism must persist or strengthen.

If mechanism reverses, widen uncertainty and `HOLD`.

### H7. Post-25 terminal Under exception

After 25:00, one synchronized snapshot may support an Under without two-snapshot persistence only if multiple terminal features align: inhibitor/base access, Baron/Elder/soul plus major structural/gold lead, exposed Nexus towers, no credible defender reset, reliable first contact/follow-up, and shortest realistic route to Nexus inside the survival horizon.

No equivalent single-snapshot exception exists for Overs.

### H8. Forecast dead zone

Automatic `PASS/HOLD` if:

1. market line `L` lies inside the central closing interval; or
2. `|L - C| < 2.0 minutes`.

If forecast uncertainty exceeds two minutes, use the wider uncertainty band.

### H9. Regime-change repricing

Immediately recompute duration after first tower, material Herald opening, first Baron, first inhibitor, soul/Elder, >=2-tower swing in one conversion cycle, short-interval >=3k gold swing, or repeated major-objective conversion failure.

Do not carry a pre-break finish forecast through a structural regime change.

### H10. LCP retained but demoted to mechanism prior

Retain LCP components: reliable first contact, numbers creation, safe follow-up/chase, wave/structure access, objective leverage, suppression of defender stall tools.

Before 25:00, LCP alone cannot authorize a TAKE; it must be observed functioning on the current map.

### H11. v0.3.45 probability buffers

Lower probability bound must clear break-even by:

- +6pp from 12:00–17:59;
- +5pp from 18:00–24:59;
- +4pp from 25:00 onward.

Market divergence:

- 0–5pp: normal;
- >5–9pp: require >=2 independent observed current-map mechanisms;
- >9pp: require >=3 mechanisms including >=1 temporally persistent stall/acceleration mechanism.

Unsupported divergence => shrink toward market, widen uncertainty and `PASS/HOLD`.

### H12. Mandatory duration lock

Before any Duration TAKE verify all of:

1. `t`, `L`, `R`;
2. fast/central/extension finish intervals;
3. central expected finish `C`;
4. dead-zone test;
5. two-snapshot status;
6. correlated quiet-state collapse;
7. observed stall count;
8. observed acceleration count;
9. LCP and whether functioning;
10. structural regime-change state;
11. shortest structure-to-Nexus route;
12. break-even and model probability range;
13. rebuild buffer;
14. market divergence;
15. no Total-Kills-to-Duration inference.

Missing any decision-critical item => `PASS/HOLD`.

## I. Execution and correlation gate

Before TAKE:

- exact line/odds executable;
- minimum odds clear;
- no prohibited correlated add-on unless user explicitly designates a separate independent bet and it independently qualifies;
- no chase/wider-line rescue;
- state synchronized.

TAKE remains conditional/unrecorded until user confirms executable line/price. Locked/disappeared/deteriorated before confirmation => NO BET / 0u.

## J. Settlement gate

- `Live`/`Pending` screenshot alone is not final;
- explicit user correction overrides visual bugs;
- when user states `Final`, treat latest synchronized scoreboard as authoritative final evidence if grading statistic is present;
- unconfirmed recommendation is never graded.

## K. Output gate

First line:

- `TAKE — [selection] @[odds] — shadow 0.25u; actual 0u.`
- `PASS — [selection/market] @[odds] — 0u.`
- `HOLD — [selection/market] @[odds] — 0u.`

If a recorded position exists and reassessment trigger fires, include thesis label separately.

## L. Fail-closed rule

If decision-critical input/calculation is unavailable, ambiguous or incomplete, `PASS/HOLD`. Never fill a missing gate with intuition.

## M. Tool order

For active maps:

1. checklist;
2. verdict;
3. logging / GitHub / Airtable / other connector work.

No connected-stack operation may delay the live verdict.
