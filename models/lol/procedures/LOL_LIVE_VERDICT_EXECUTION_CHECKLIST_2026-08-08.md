# LoL Live Verdict Execution Checklist — 2026-08-08

**Status:** Mandatory  
**Authority:** LoL v0.3.42  
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

- ACTIVE: lower-bound probability still clears original break-even by required phase buffer and no hard veto.
- DEGRADED: lower bound remains above break-even but no longer clears buffer.
- INVALIDATED: lower bound at/below break-even or a hard veto applies.
- CONFIRMED: materially strengthened only.

Mandatory triggers: explicit reassessment request; >=2k meaningful gold swing; tower differential change >=2; first Baron/Elder; inhibitor/base access; material dragon/soul alignment; >=2 net-kill swing; repeated failure of a theoretical defensive mechanism; demonstrated pick-to-objective cascade.

## C. Verified team-strength gate — v0.3.42

Before any pregame/0:00 numeric team-strength or map prior:

1. verify or obtain the current five-player lineup;
2. identify roster discontinuity versus older samples;
3. use current-lineup results first;
4. adjust for opponent quality;
5. score role-by-role current strength/fit;
6. separately score macro coordination, early creation, objective setup, teamfight execution, lead conversion, comeback resistance and volatility;
7. establish an uncertainty band.

If the lineup is uncertain or stale samples dominate, fail closed on a numeric edge.

### C1. Market-divergence sanity gate

Calculate de-vigged market prior when pregame odds are available.

Model central probability vs de-vigged market:

- 0–6pp: normal;
- >6–10pp: require >=2 independent verified reasons;
- >10pp: require >=3 independent verified reasons, including one current-lineup-performance reason and one matchup/role reason.

If unsupported, shrink model toward market until divergence <=6pp and widen uncertainty.

**Uncertainty is not edge.** Do not turn a wide band into automatic underdog value.

Series prior and map prior must remain separate.

## D. Matchup-adjusted draft gate — v0.3.42

Do not count draft tools additively. For every claimed tool, test whether it remains functional into the opposing draft.

Test:

- safe range vs engage/flank/global access;
- waveclear vs siege/side pressure/dive;
- disengage vs reliable multi-axis/repeat engage;
- peel vs simultaneous dive routes;
- engage vs anti-engage/terrain/mobility denial;
- objective contest vs poke/zone/choke/face-check burden;
- return kills vs cleanup/chase/ranged follow-up;
- scaling vs actual safe damage delivery.

A tool directly suppressed by the opponent is weakened/nonfunctional, not a full resilience category.

### D1. Functional counter tax

If one opposing interaction materially degrades two or more core functions, reduce those functions explicitly. Apply by function, not by champion-name hard-coding.

### D2. Execution burden

Identify:

- simpler first successful sequence;
- side requiring more precise spacing/flank timing/targeting;
- number of independent reliable fight-start channels;
- first composition likely to become nonfunctional if one role falls behind.

If the stronger team also has the simpler/reliable execution path, widen its clean-win and high-margin branches.

### D3. Damage-access map

Identify:

1. who can hit frontline safely;
2. who can access backline;
3. who must cross enemy control to deal meaningful damage;
4. easiest carry to isolate;
5. main-DPS uptime after first contact;
6. retreating-side return-kill capability.

Multiple carries do not equal resilience if target access is poor.

### D4. Draft adjustment cap

Normal draft adjustment from verified pre-draft map prior: **0–4pp**.

A move >4pp requires >=3 independent **functional** matchup advantages after opponent-counter testing.

Draft should rarely erase a large verified team-strength gap by itself.

## E. Moneyline gate

For all ML:

- odds >=1.60;
- current-map evidence sufficient;
- map prior distinct from series prior;
- no transfer from generic team strength alone;
- no automatic transfer to handicap confidence.

### E1. Pregame / 0:00 ML probability gate

Construct:

1. verified baseline map `P_win` range;
2. market de-vig prior and divergence check;
3. verified side adjustment;
4. matchup-adjusted draft adjustment;
5. supported execution/form adjustment;
6. final reasonable `P_win` range;
7. `P_break_even = 1 / odds`.

Lower end must clear break-even by at least **+3pp**.

Failure => `PASS` or `HOLD`.

## F. Kill-handicap gate

### F1. Phase classification

Set exactly one:

- `PREGAME / 0:00`
- `EARLY LIVE`
- `MID/LATE LIVE`

### F2. Exact arithmetic and distribution

Calculate:

1. current kill margin;
2. exact final margin required;
3. exact future net-kill swing required;
4. projected final total-kill low / central / high range;
5. low / central / high final kill-margin branches;
6. handicap magnitude `H`, central projected total kills `T`, and `H/T`;
7. next two likely forced-fight/objective sequences;
8. gold/tower/neutral-objective alignment;
9. return-kill evidence level;
10. line-chasing/repair/dominance state.

### F3. Conditional winner/margin decomposition — v0.3.42

For positive handicap:

`P(dog +H covers) = P(dog wins) + P(favorite wins AND favorite margin <= H)`

Required branches:

- underdog wins;
- favorite wins close;
- favorite wins moderate;
- favorite wins high-margin.

The favorite-win margin branches must be conditional on the favorite winning and reflect team-strength gap, matchup-adjusted draft, execution burden, expected total kills and cascade architecture.

Do not assume a large favorite win probability and a high dog cover rate simultaneously without explicit close-loss evidence.

### F4. Break-even / cover-probability gate

For any handicap TAKE calculate `P_break_even` and a reasonable `P_cover` range. Require lower end to clear break-even by:

- **+5pp** pregame positive handicap;
- **+4pp** early-live handicap;
- **+3pp** mid/late-live handicap.

If unsupported => `PASS` / `HOLD`.

### F5. Pregame positive-handicap high-friction rule

Draft resilience, scaling, engage/disengage, globals or a visually large cushion are insufficient. Require projected total kills, conditional final-margin distribution, probability edge and cascade-tail assessment.

### F6. Cascade-tail penalty

Widen favorite high-margin branch for layered engage, globals, point-and-click initiation, reset/chase, objective forcing, dive/follow-up and safe cleanup DPS.

Do not model repeatable cascade fights as independent. `pick -> numbers advantage -> objective/structure -> vision denial -> second pick` increases subsequent margin-expansion probability.

### F7. Return-kill evidence hierarchy

1. theoretical draft tools;
2. lane-state survival/parity;
3. observed repeated return kills;
4. objective contest/cross-map trade;
5. repeated multi-cycle resistance.

Pregame level-1 evidence is supporting only. Mid/late positive handicaps generally require level 3+ when opponent structural control is aligned.

### F8. Matchup-adjusted mechanistic resilience

Evaluate positive-handicap side for:

1. safe range;
2. disengage/reset;
3. waveclear/base defense;
4. anti-dive/peel;
5. objective-contest access;
6. return-kill reliability.

Then apply opponent interaction from Section D. A category that is functionally countered cannot be credited at full strength.

### Objective-Control Handicap Veto

If opponent has aligned gold + meaningful neutral-objective control, cushion alone is not evidence. Without affirmative repeated contest/trade/return-kill evidence, `PASS`.

### Draft Cascade-Structure Veto

For positive handicap, `PASS` unless strong counterevidence exists when:

- opponent leads gold;
- opponent leads structures or has repeatable structure access;
- opponent has >=3 meaningful pick/cascade components;
- positive-handicap side lacks demonstrated level-3+ return-kill/contest evidence or >=3 **matchup-adjusted** resilience categories.

Split neutral-objective control does not cancel this veto.

### Favorite Structural Margin-Expansion Ladder

When a leader has aligned gold + objective pressure + structural conversion/access, scan smaller favorite negative handicaps **before** next kill conversion. Price independently, prefer least aggressive qualifying line, do not chase after conversion.

## G. Total-kills gate

Calculate:

- current total kills;
- whole kills to cross line;
- unresolved major fight triggers;
- low/central/high remaining-kill branches;
- objective-density reserve;
- clean-close/return-kill suppression state;
- global/engage/cascade fight-creation channels.

For a TAKE, lower probability bound must clear break-even by **+4pp early live** and **+3pp mid/late**.

High early fight-density: >=8 kills by 8:00, >=10 by 10:00, repeated early multi-player skirmishes, or multiple global/engage chains coming online. If active with >=3 fight windows remaining, assign high-kill branch >=25–30% absent strong suppression evidence.

Four or more collective fight-creation channels => extra volatility penalty against early Under.

Total Kills is never inferred from Duration.

## H. Duration gate

Calculate separately:

- fast-close branch;
- central branch;
- extension branch;
- fastest realistic structure-to-Nexus route;
- genuine stall/anti-conversion signals;
- terminal access / resets / methodical-control tax.

Retained corrections:

- no Over before 10:00 without two genuine stall signals beyond towerlessness;
- >=6 kills by 8:00 widens fast-finish branch;
- >=14 kills by 16:00 means 0-0 towers is not confirming Over evidence;
- around 20:00, >=+5k gold and +2 towers invalidates short Overs absent exceptional counterevidence;
- comeback tools widen distribution;
- Grubs alone do not prove completed acceleration;
- kill suppression != duration compression.

## I. Execution and correlation gate

Before `TAKE`:

- exact line/odds executable;
- minimum odds and market threshold clear;
- no prohibited correlated add-on unless user explicitly designates a separate independent bet and it independently qualifies;
- no chase/wider-line rescue;
- state synchronized.

A `TAKE` is CONDITIONAL / UNRECORDED until user confirms same qualifying line/price was available and accepted.

Locked/disappeared/deteriorated before confirmation => NO BET / 0u; never grade later.

If recorded position becomes INVALIDATED: do not add, rescue or automatically flip opposite as repair/chasing.

## J. Settlement gate

- `Live` screenshot alone => do not settle;
- `Pending` screenshot alone => do not settle;
- explicit user correction overrides a visual-status bug;
- when user states `Final`, treat latest synchronized scoreboard as authoritative final-state evidence if grading statistic is present;
- unavailable/unconfirmed recommendations remain NO BET even if outcome later wins.

## K. Output gate

First line:

- `TAKE — [selection] @[odds] — shadow 0.25u; actual 0u.`
- `PASS — [selection/market] @[odds] — 0u.`
- `HOLD — [selection/market] @[odds] — 0u.`

When recorded position exists and reassessment trigger fires, include thesis label separately.

## L. Fail-closed rule

If decision-critical input/calculation is unavailable, ambiguous or incomplete, output `PASS` or `HOLD`. Never fill a missing gate with intuition.

## M. Tool order

For active maps:

1. checklist;
2. verdict;
3. logging / GitHub / Airtable / Sheets / other connector work.

No connected-stack operation may delay the live verdict.
