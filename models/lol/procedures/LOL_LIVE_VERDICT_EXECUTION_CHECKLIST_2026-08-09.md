# LoL Live Verdict Execution Checklist — 2026-08-09

**Status:** Mandatory  
**Authority:** LoL v0.3.48  
**Purpose:** mechanical pre-verdict gate for every League of Legends post-draft/live snapshot.

Complete internally before every verdict. User-facing output remains brief and verdict-first.

## A. Current-frame fingerprint

Verify from newest synchronized evidence:

- event / game / sides;
- clock;
- kills and orientation;
- gold lead and direction;
- role-level gold deltas when shown;
- towers / inhibitors / base access;
- dragons / soul point / soul;
- Grubs / Herald;
- Baron / Elder;
- exact market line and odds;
- line open / locked / delayed.

Do not carry forward mutable fields unless reconciled. For Total Kills and Kill Handicap, current kills are always decision-critical.

## B. Position state

Set one:

- `RECORDED POSITION: NONE`
- `CONDITIONAL / UNRECORDED`
- `RECORDED SHADOW POSITION`

If a position exists, separately set thesis: `ACTIVE / DEGRADED / INVALIDATED / CONFIRMED`.

Reassess position-blind after any material state change. Entry price, sunk stake or desire for consistency are never supporting evidence.

For open kill handicaps, INVALIDATED requires a fresh cover reprice at/below break-even or a hard veto. Map dominance alone is not enough.

## C. Verified team-strength prior

Before numeric pregame team-strength/map priors:

1. verify current five-player lineup;
2. identify roster discontinuity;
3. prioritize current-lineup/current-stage evidence;
4. adjust for opponent quality;
5. score role-by-role strength/fit;
6. score macro, early creation, objective setup, teamfight execution, lead conversion, comeback resistance and volatility;
7. anchor against de-vigged market and establish uncertainty.

Unsupported model-market divergence must shrink toward market. Team strength is the **pre-draft baseline**, not the post-draft conversion engine.

## D. Draft Primacy Gate — v0.3.48 / v0.3.47

Once draft is locked, draft interaction becomes the **primary mechanism layer** for projecting how the current state converts.

### D1. Mandatory Draft Function Matrix

Before any post-draft TAKE in ML, Kill Handicap or Total Kills, score both teams relatively on:

1. reliable first contact;
2. hard-CC density;
3. CC reliability: immediate/conditional, range, execution burden;
4. anti-engage/disengage;
5. frontline access;
6. backline access;
7. carry protection;
8. damage continuation after first contact;
9. chase/cleanup;
10. re-engage/repeat forcing;
11. objective/choke control;
12. waveclear/base defense under actual pressure;
13. side-lane/global numbers creation;
14. execution simplicity.

Use `material edge / slight edge / even / slight disadvantage / material disadvantage`.

Do not count champion names or generic tools. Every credited function must survive opponent-counter testing.

### D2. Draft-to-Conversion classification — v0.3.48

For each team, classify the likely conversion mode:

- Fight Cascade;
- Pick-and-Reset;
- Side-Lane / Global Overload;
- Objective / Structure Snowball;
- Siege / Choke;
- Scaling Front-to-Back;
- Mixed.

For Kill Handicap, explicitly ask:

`If this team wins from the current state, how much of the winning branch is kill-centric versus structure/objective-centric?`

Draft strength can increase ML while only modestly increasing kill margin.

### D3. CC Scarcity / Proactivity Tax

Flag when the trailing team has zero/one reliable hard first-contact source, or most control is conditional/short-range/defensive-only, while the leader has two or more independent reliable initiation layers with follow-up.

When active:

- reduce trailing comeback forcing;
- reduce positive-handicap resilience;
- increase leader repeat-pick/chase branches;
- increase leader +10/+15 margin tail when already ahead.

**Durability is not control.**

### D4. Distributed Economic Dominance (DED)

When role-level gold is available, flag DED if:

- current favorite leads in >=4 of 5 roles;
- team gold lead is material for the clock;
- at least one engage/control role and one primary damage role are ahead/online.

Reference points only: about >=2.5k by 15:00, >=3.5k by 18:00, >=5k by 22:00.

Do not invent DED when role-level gold is unavailable.

### D5. Draft-Dominance Cascade (DDC)

Flag DDC when:

1. favorite has a material live lead or DED;
2. favorite has a material reliable first-contact / hard-CC edge;
3. favorite has target-access plus damage-continuation advantage;
4. trailer has weak proactive forcing or CC Scarcity Tax;
5. >=3 meaningful future fight/pressure windows remain;
6. no demonstrated hard anti-cascade mechanism is functioning.

When DDC is active, expand favorite wide-margin bins — **subject to v0.3.48 conversion-speed controls in F**.

### D6. Anti-cascade tools are graded

For Kill Handicap classify defensive tools as:

- `MAP-SAVING`;
- `MARGIN-SAVING`;
- `NONFUNCTIONAL`.

A mechanism can fail to save the map while still producing return kills or reducing final kill margin.

### D7. Reassess draft mechanisms live

Re-run D after:

- >=2k meaningful gold swing;
- broad role-level lead distribution or concentration change;
- first tower/material Herald opening;
- material dragon/soul alignment change;
- first Baron;
- >=2 net-kill swing;
- repeated failure of waveclear/disengage/anti-dive;
- repeated first-contact -> objective/structure conversion.

## E. Moneyline gate

- odds >=1.60;
- map prior distinct from series prior;
- draft-conditioned map probability after D;
- pregame lower P_win bound must clear break-even by >=3pp.

Draft edge must be matchup-functional, not narrative.

## F. Kill Handicap Gate — v0.3.48 + v0.3.47 + v0.3.44

### F1. Phase and signed margin

Set `PREGAME`, `EARLY LIVE`, or `MID/LATE LIVE`.

Define `M = favorite final kills - underdog final kills`.

### F2. Blind fair-margin lock

Before using displayed handicap as evidence, lock:

- current kill margin;
- projected total-kill low/central/high range;
- favorite map-win probability range;
- conditional favorite-win margin distribution;
- signed margin bins `M<=0`, `+1..3`, `+4..6`, `+7..9`, `+10..14`, `15+`;
- underdog-win/tie branch;
- uncertainty width;
- DED/DDC/CC-scarcity status.

### F3. Net-Kill Burden (NKB)

Calculate the minimum additional **net kills** the favorite needs to beat the displayed handicap from the current score.

Do not use NKB as a standalone veto or reason to TAKE. Compare it to remaining fight inventory.

### F4. Remaining Fight Inventory (RFI)

Inventory remaining windows:

- dragon / soul point / soul;
- Baron / Elder;
- inhibitor siege;
- terminal base defense;
- unavoidable side-lane collapse;
- demonstrated repeat-pick cycles.

Classify each as:

- forced/high-contact;
- likely but avoidable;
- structure-only plausible;
- unlikely before end.

Do not count every objective as an automatic full fight.

### F5. Kill Conversion Velocity (KCV)

When >=2 synchronized snapshots are available, assess:

- signed-margin change;
- gold-lead change;
- structure change;
- whether fights produce repeated 2+ net kills;
- whether first contact leads to cleanup.

Set:

- `HIGH` — margin expands with lead; repeated multi-kill conversion;
- `MEDIUM` — mixed kill/structure conversion;
- `LOW / STRUCTURE-SUBSTITUTED` — gold/structures expand while margin stays flat/slow.

### F6. Structure Substitution (SS)

Flag when map control expands primarily through towers/objectives/side lanes rather than kill margin.

When active:

- compress extreme favorite-margin tail;
- increase +kills survival probability;
- remember Baron/inhibitor pressure can shorten the game and cannibalize future kills.

### F7. Symmetric pricing

For line H:

- dog +H cover = `P(M < H)`;
- favorite -H cover = `P(M > H)`.

Price both sides from the same distribution.

### F8. Early Favorite Handicap Fast Path

Before defaulting toward the positive cushion, explicitly test favorite -H when:

- favorite controls the map economically;
- DED or equivalent broad control is present;
- DDC is active/nearly active;
- trailer lacks functional proactive control;
- line remains inside the projected cascade tail;
- enough map remains for serial pressure;
- exact price can clear the surcharge.

This fast path is especially important around **-5.5 to -9.5** so the model does not miss JDG -9.5-type spots before the line widens.

### F9. Wide Favorite Conversion Gate — v0.3.48

For favorite **-10.5 or wider**, DED/DDC alone is insufficient.

Require at least one:

1. observed HIGH KCV;
2. NKB <=5 plus >=1 high-contact fight/base-defense sequence;
3. >=2 high-contact forced windows plus demonstrated multi-kill cleanup/return denial;
4. early-live fast-path state with no evidence of structure-substituted conversion.

**Slow-conversion veto:** if across two synchronized snapshots gold expands materially while kill margin is flat or expands by <=1, favorite -10.5+ is PASS/HOLD unless NKB <=5 or two clear high-contact windows remain.

### F10. Underdog handicap survival != map survival

For +kills, separately estimate:

- P(underdog wins map);
- P(underdog covers | loses map).

Do not invalidate +kills solely because favorite ML becomes overwhelming, DED appears, or Baron/inhibitors fall.

Credit MARGIN-SAVING return kills, counter-engage, peel, terminal base-defense kills and structure-substituted leader conversion even when the underdog is strategically dead.

### F11. Temporary v0.3.44 surcharge retained

Lower cover bound must clear break-even by:

- +7pp pregame;
- +6pp early live;
- +5pp mid/late.

No directional quota. Objective-Control Handicap Veto and Draft Cascade-Structure Veto remain active.

## G. Total Kills Gate — v0.3.46 retained

Lock:

- current kills;
- kills required to cross line;
- low/central/high final-kill branches;
- functional fight-creation channels;
- unresolved forced-fight windows;
- soul-point conflict;
- Baron/Elder/base-defense reserve;
- clean-close vs kill-inflation branches;
- break-even and probability range.

Probability lower-bound gates:

- +5pp pregame;
- +4pp early live;
- +3pp mid/late;
- pregame Under with >=4 fight channels and >=3 forced-fight windows: +7pp.

For Under, large cushion is arithmetic, not evidence. If <=4 kills of cushion and a major forced fight/base-defense sequence remains, default existing thesis to INVALIDATED absent near-terminal clean close.

Major objectives are ambiguous: shorter duration can still mean more base-defense kills.

No positive Total Kills thesis upgrade after objective-only/timer-only updates without synchronized current kills.

## H. Duration Gate — v0.3.45 retained

Duration remains specialized live-only.

- no pregame TAKE;
- no TAKE before 12:00;
- 12:00-13:59 requires two synchronized snapshots >=90s apart showing same mechanism;
- 14:00+ requires observed stall/acceleration evidence;
- all normal dead-zone, survival-horizon, regime-change and probability-buffer rules remain active.

Draft remains a mechanism prior for Duration; it is not sufficient observed evidence by itself.

## I. Execution / Same-map Add-ons

Before TAKE:

- exact line/odds executable;
- odds >=1.60;
- synchronized state;
- no rescue/chasing;
- each same-map add-on independently qualifies;
- correlation explicitly priced;
- every add-on logged separately;
- no stake escalation.

Shadow default remains 0.25u, actual 0u while official wagering is paused.

TAKE remains conditional/unrecorded until user confirms line/price. Disappeared/locked/deteriorated before confirmation => NO BET / 0u.

## J. Settlement

- Live/Pending UI alone is not final;
- explicit user correction overrides visual bugs;
- when user states `Final`, treat latest synchronized grading statistic as authoritative;
- unconfirmed recommendation is never graded.

## K. Output

First visible line:

- `TAKE — [selection] @[odds] — shadow 0.25u; actual 0u.`
- `PASS — [selection/market] @[odds] — 0u.`
- `HOLD — [selection/market] @[odds] — 0u.`

If an open position exists, include thesis state separately.

## L. Fail Closed

Missing decision-critical draft, state, line, NKB, conversion-mode, KCV/RFI evidence or synchronization input => widen uncertainty and `PASS/HOLD`.

## M. Tool order

For active maps:

1. checklist;
2. verdict;
3. logging / GitHub / Airtable / other connector work.

Connector work must never delay the live verdict.
