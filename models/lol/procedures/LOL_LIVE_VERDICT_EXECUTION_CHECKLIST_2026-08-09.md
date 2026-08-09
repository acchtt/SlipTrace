# LoL Live Verdict Execution Checklist — 2026-08-09

**Status:** Mandatory  
**Authority:** LoL v0.3.44  
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

## C. Verified team-strength gate — v0.3.42+

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

## D. Matchup-adjusted draft gate — v0.3.42+

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

## F. Kill-handicap gate — v0.3.44

Kill-handicap analysis is **side-neutral and distribution-first**.

### F1. Phase classification

Set exactly one:

- `PREGAME / 0:00`
- `EARLY LIVE`
- `MID/LATE LIVE`

### F2. Define favorite and signed margin

Define:

`M = favorite final kills - underdog final kills`

Pregame/0:00 favorite = de-vigged map favorite after lineup/draft reconciliation. Live favorite = synchronized live ML favorite when available, otherwise position-blind current map-state favorite.

### F3. Blind fair-margin lock

**Before using the displayed handicap as evidence**, lock:

1. current kill margin;
2. projected final total-kill low / central / high range;
3. fair central favorite kill margin;
4. signed final-margin distribution;
5. favorite map-win probability range;
6. conditional favorite-win margin distribution;
7. underdog-win/tie branch;
8. uncertainty width.

Minimum margin bins:

- `M <= 0`;
- `M +1 to +3`;
- `M +4 to +6`;
- `M +7 to +9`;
- `M +10 to +14`;
- `M >= +15`.

Probabilities must sum to approximately 100% and remain consistent with team strength, draft function, projected total kills and live structure.

### F4. Symmetric price calculation

For half-kill line `H`:

- `P(dog +H covers) = P(M < H)`;
- `P(favorite -H covers) = P(M > H)`.

For whole lines, account explicitly for push rules if applicable.

Price **both displayed sides from the same locked distribution** before selecting either side.

Do not create one distribution for the positive side and another for the negative side.

### F5. Favorite wide-win branch

Apply the same analytical depth to favorite margin expansion as to underdog resilience.

Widen the favorite high-margin tail for supported:

- team-strength gap;
- early creation / lead conversion;
- simpler or repeatable engage;
- multi-axis target access;
- carry concentration;
- wave/structure pressure;
- objective forcing / face-check burden;
- Baron/soul/base access;
- safe chase/cleanup;
- serial pick-to-objective-to-structure cascades;
- end-game kill inflation from forced base defense and terminal chase.

A small current kill margin does **not** imply a narrow final margin when structural conversion is aligned.

### F6. Matchup-adjusted underdog resilience

Evaluate:

1. safe range;
2. disengage/reset;
3. waveclear/base defense;
4. anti-dive/peel;
5. objective-contest access;
6. return-kill reliability.

Then apply v0.3.42 opponent-counter testing. A theoretical tool only earns close-loss probability if it can realistically reduce the favorite's wide-margin tail in this matchup.

### F7. Conditional winner/margin consistency

Retain:

`P(dog +H covers) = P(dog wins) + P(favorite wins AND favorite margin <= H)`

But all branches must come from the same signed distribution used for the opposite side.

Do not combine a large favorite win probability with a very high dog-cover probability unless affirmative evidence shows favorite wins are usually narrow.

### F8. Live margin-expansion hazard

For live snapshots explicitly assess:

- gold lead and trajectory;
- tower differential / repeatable structure access;
- dragon/soul/Baron/Elder alignment;
- carry concentration and shutdown distribution;
- reliable engage / pick channels;
- defender face-check burden;
- observed return-kill resistance;
- inhibitor/base access;
- terminal kill inflation.

If leader has aligned gold + structure/objective pressure + reliable first contact, widen the high-margin tail even if current kills are close.

### F9. Arithmetic is not evidence

Calculate exact current margin and exact future net-kill swing required, but statements such as "the favorite still needs another +7 net kills" are arithmetic only.

A visually large positive cushion is not supporting evidence until the margin distribution prices it.

### F10. v0.3.44 temporary calibration surcharge

For the next 20 settled **new v0.3.44 kill-handicap entries**, lower `P_cover` bound must clear break-even by:

- **+7pp** pregame / 0:00;
- **+6pp** early live;
- **+5pp** mid/late live.

This applies symmetrically to positive and negative handicaps.

Review after 10 and 20 settled v0.3.44 handicap positions.

The already-recorded KT +3.5 kills @1.935 vs DK Game 2 remains a v0.3.43 entry. Any future thesis reassessment of that open ticket uses v0.3.44.

### F11. Directional-skew monitor

At each 10-position review window:

- >=80% one sign => mandatory directional-bias audit before relaxing controls;
- >=90% one sign plus negative ROI => keep/strengthen surcharge and perform explicit process review;
- never force the next selection to the opposite sign just to balance counts.

### F12. Positive-handicap structural vetoes retained

Retain the Objective-Control Handicap Veto and Draft Cascade-Structure Veto from v0.3.41/v0.3.42.

For positive handicap, cushion alone cannot override aligned gold + structure/objective control + repeatable cascade architecture without demonstrated return-kill/contest resistance.

### F13. Side-neutral scan order

When both sides are visible:

1. locked fair distribution;
2. positive-side break-even/edge;
3. negative-side break-even/edge;
4. uncertainty and surcharge;
5. vetoes;
6. choose one qualifying side or `PASS/HOLD`.

If both sides appear to qualify because uncertainty is too wide or distributions conflict, fail closed.

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

## H. Duration gate — v0.3.43 retained

Duration is a **survival event**, not a generic pace read.

Before any duration verdict calculate:

1. current clock `t`;
2. duration line `L`;
3. remaining survival horizon `R = L - t`;
4. fast-close branch;
5. central closing branch;
6. extension branch;
7. leader gold/state trajectory;
8. Latent Conversion Potential `LCP`;
9. observed stall-signal count;
10. first-break elasticity / fastest realistic structure-to-Nexus route;
11. break-even probability and model probability range;
12. duration market-divergence check.

### H1. Structural absence is neutral

From 14:00 onward, 0-0 or low towers is **neutral by default**, not positive Over evidence. Towerlessness becomes stall evidence only with >=2 independent observed stall signals.

### H2. Latent Conversion Potential

Score six accelerants: reliable first contact; numbers creation; safe follow-up/chase; wave/structure access; objective leverage; functional suppression of defender waveclear/disengage/peel.

`LCP 0-1 = low`, `2 = moderate`, `3-4 = high`, `5-6 = very high`.

### H3. High-friction Over veto

For a live Over, `PASS/HOLD` when all are true unless exceptional synchronized counterevidence exists:

- leader >=+1.5k gold after 14:00;
- Over requires >=15 additional minutes of survival;
- leader `LCP >=3`;
- fewer than two observed stall signals.

### H4. Duration probability buffers

Lower end must clear break-even by:

- **+5pp** before 18:00;
- **+4pp** from 18:00 through 24:59;
- **+3pp** from 25:00 onward.

### H5. Duration market-divergence sanity gate

Model central probability vs market break-even:

- 0-5pp: normal;
- >5-9pp: require >=2 independent current-map reasons;
- >9pp: require >=3 independent current-map reasons, including >=1 observed stall/acceleration reason.

Unsupported divergence => shrink toward market, widen uncertainty, fail closed if buffer is not met.

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
