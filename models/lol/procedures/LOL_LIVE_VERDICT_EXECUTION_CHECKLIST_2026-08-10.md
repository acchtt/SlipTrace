# LoL Live Verdict Execution Checklist — 2026-08-10

**Status:** Mandatory  
**Authority:** LoL v0.3.49  
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

Unsupported model-market divergence must shrink toward market. Team strength is the pre-draft baseline, not the post-draft conversion engine.

## D. Draft Primacy Gate — v0.3.49 / v0.3.48 / v0.3.47

Once draft is locked, draft interaction becomes the primary mechanism layer for projecting how the current state converts.

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

### D2. Draft-to-Conversion classification

For each team, classify likely conversion mode:

- Fight Cascade;
- Pick-and-Reset;
- Side-Lane / Global Overload;
- Objective / Structure Snowball;
- Siege / Choke;
- Scaling Front-to-Back;
- Mixed.

For Kill Handicap ask how much of the win branch is kill-centric versus structure/objective-centric.

For Total Kills, do not infer low future combat merely because conversion is side-lane/structure-oriented; apply G's forward-contact analysis.

### D3. CC Scarcity / Proactivity Tax

Flag when the trailing team has zero/one reliable hard first-contact source, or most control is conditional/short-range/defensive-only, while the leader has multiple independent reliable initiation layers with follow-up.

When active:

- reduce trailing comeback forcing;
- reduce positive-handicap resilience;
- increase leader repeat-pick/chase branches;
- increase leader wide-margin tail when already ahead;
- for Total Kills, separately test whether this creates compulsory losing contests rather than low combat.

**Durability is not control. Range is not disengage.**

### D4. Distributed Economic Dominance (DED)

When role-level gold is available, flag DED if:

- current favorite leads in >=4 of 5 roles;
- team gold lead is material for the clock;
- at least one engage/control role and one primary damage role are ahead/online.

Reference points only: about >=2.5k by 15:00, >=3.5k by 18:00, >=5k by 22:00.

### D5. Draft-Dominance Cascade (DDC)

Flag DDC when:

1. favorite has a material live lead or DED;
2. favorite has reliable first-contact / hard-CC edge;
3. favorite has target-access plus damage-continuation advantage;
4. trailer has weak proactive forcing or CC Scarcity Tax;
5. >=3 meaningful future fight/pressure windows remain;
6. no demonstrated hard anti-cascade mechanism is functioning.

DDC expands favorite margin tails subject to v0.3.48 conversion-speed controls and can raise Total Kills if G identifies high Forward Contact Inventory + Contact Lethality.

### D6. Anti-cascade tools are graded

For Kill Handicap classify defensive tools as:

- `MAP-SAVING`;
- `MARGIN-SAVING`;
- `NONFUNCTIONAL`.

For Total Kills additionally ask whether those tools **avoid contact** or merely generate return kills. Return kills can save +kills while hurting an Under.

### D7. Reassess live

Re-run D after:

- >=2k meaningful gold swing;
- role-level lead distribution change;
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

## F. Kill Handicap Gate — v0.3.48 retained

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

Calculate minimum additional net kills the favorite needs to beat the displayed handicap from the current score.

### F4. Remaining Fight Inventory (RFI)

Inventory dragon/soul, Baron/Elder, inhibitor siege, terminal base defense, side-lane collapse and repeat-pick cycles. Classify each as forced/high-contact, likely but avoidable, structure-only plausible, or unlikely before end.

### F5. Kill Conversion Velocity (KCV)

With >=2 synchronized snapshots set:

- `HIGH` — margin expands with lead; repeated multi-kill conversion;
- `MEDIUM` — mixed kill/structure conversion;
- `LOW / STRUCTURE-SUBSTITUTED` — gold/structures expand while margin stays flat/slow.

### F6. Structure Substitution (SS)

When map control expands through towers/objectives/side lanes rather than kill margin:

- compress extreme favorite-margin tail;
- increase +kills survival probability;
- remember Baron/inhibitor pressure can shorten the map and cannibalize future net kills.

### F7. Symmetric pricing

For line H:

- dog +H cover = `P(M < H)`;
- favorite -H cover = `P(M > H)`.

Price both sides from the same distribution.

### F8. Early Favorite Handicap Fast Path

Explicitly test favorite -H when broad economic control, DED/DDC, draft access and future fight inventory align. Especially important around -5.5 to -9.5 before the line widens.

### F9. Wide Favorite Conversion Gate

For favorite -10.5 or wider require at least one:

1. observed HIGH KCV;
2. NKB <=5 plus >=1 high-contact fight/base-defense sequence;
3. >=2 high-contact forced windows plus demonstrated multi-kill cleanup/return denial;
4. early-live fast-path state with no evidence of Structure Substitution.

Slow-conversion veto remains active.

### F10. Handicap survival != map survival

For +kills separately estimate P(underdog wins map) and P(underdog covers | loses map). Do not invalidate from favorite ML/DED/Baron alone.

### F11. Surcharge

Lower cover bound must clear break-even by:

- +7pp pregame;
- +6pp early live;
- +5pp mid/late.

## G. Total Kills Gate — v0.3.49

### G1. Line arithmetic

Lock:

- current kills;
- exact line;
- kills needed to cross;
- exact break-even;
- low/central/high final-kill branches.

Large cushion is arithmetic, not evidence.

### G2. Observed Kill Pace (OKP)

Record:

- kills/minute;
- kills added since prior synchronized snapshot;
- recent fight outcomes;
- whether recent kills are repeatable mechanisms or isolated anomalies.

Set `LOW / MEDIUM / HIGH`.

**Quiet-start non-persistence:** before 15:00, low kills or low kills/minute cannot by themselves increase Under probability.

An early Under upgrade requires low OKP plus limited/declining forward contact, demonstrated low contact lethality, or a clean-close mechanism that removes future contact windows.

### G3. Forward Contact Inventory (FCI)

List meaningful remaining windows and classify:

- `FORCED / HIGH-CONTACT`;
- `LIKELY CONTACT`;
- `AVOIDABLE / TRADEABLE`;
- `STRUCTURE-ONLY PLAUSIBLE`;
- `UNLIKELY BEFORE END`.

Include objective contests, Baron/Elder, inhibitor/base defense, repeat-pick cycles, side-lane collapses and forced face-checks.

Do not count every objective as a fight.

### G4. Contest Compulsion

Flag when the trailing team is losing the option to concede because of soul/Baron/inhibitor/terminal pressure and must enter enemy-controlled terrain.

When active, increase FCI. Poke/waveclear/global tools only suppress kills if they actually permit safe avoidance or disengage.

### G5. Contact Lethality (CL)

Set `LOW / MEDIUM / HIGH` using:

- reliable access;
- hard-CC chain;
- damage continuation;
- cleanup/chase;
- re-engage;
- disengage/peel;
- mobility/escape;
- return-kill capability;
- current gold concentration.

**Access/disengage mismatch:** reliable hard access versus weak functional disengage raises CL even against a nominal poke/waveclear/side-lane composition.

### G6. Forward projection

Project:

`Final Total Kills = Current Kills + kills from remaining FCI windows + low-contact residual kills`.

Answer explicitly:

1. how many meaningful contact windows remain;
2. which are forced;
3. expected lethality per contact;
4. whether acceleration removes windows or creates compulsory defense first;
5. whether return kills remain likely.

### G7. Under vetoes / surcharge

An Under cannot be TAKEN/upgraded merely because current kills are low, towers are low, Grubs/Herald exist, or drafts have generic poke/waveclear/side-lane tools.

If pregame/early Under has all:

- >=1 highly reliable hard-access tool plus follow-up on one side;
- weak functional disengage on the opponent;
- >=3 meaningful future objective/base-defense windows likely;

add **+2pp** to the normal Total Kills lower-bound requirement, capped at +9pp total cushion over break-even.

If FCI has >=3 forced/high-contact windows and CL is HIGH, Under defaults PASS unless explicit window arithmetic still clears the applicable gate.

### G8. Over discipline

High FCI is not an automatic Over. Account for clean close, Structure Substitution, objective trades and LOW CL.

### G9. Probability gates

Base lower-bound gates remain:

- +5pp pregame;
- +4pp early live;
- +3pp mid/late;
- previous high-friction pregame Under conditions remain, with v0.3.49 surcharge layered where applicable.

If <=4 kills of Under cushion and a major forced fight/base-defense sequence remains, default existing Under thesis to INVALIDATED absent near-terminal clean close.

## H. Duration Gate — v0.3.45 retained

- no pregame TAKE;
- no TAKE before 12:00;
- 12:00-13:59 requires two synchronized snapshots >=90s apart showing same mechanism;
- 14:00+ requires observed stall/acceleration;
- dead-zone, survival-horizon and regime-change rules remain mandatory.

## I. Execution / Same-map Add-ons — v0.3.49

Before TAKE:

- exact line/odds executable;
- odds >=1.60;
- synchronized state;
- no rescue/chasing;
- each add-on independently qualifies;
- every add-on logged separately;
- no stake escalation.

### I1. Total Kills + Kill Handicap decomposition

Define:

- `T = favorite kills + underdog kills`;
- `M = favorite kills - underdog kills`.

Project T and M separately. Do not use a Total Kills thesis as direct evidence for a handicap without mapping the relevant joint branch.

### I2. Four-cell joint matrix

For existing position A and candidate add-on B, estimate:

- P(A win, B win);
- P(A win, B lose);
- P(A lose, B win);
- P(A lose, B lose).

Identify concrete scenarios for each materially non-zero one-win/one-loss branch.

The add-on must still clear its own edge after joint-distribution adjustment. Reusing the existing thesis narrative is not an independent edge.

Shadow default remains 0.25u, actual 0u while official wagering is paused.

TAKE remains conditional/unrecorded until user confirms line/price. Disappeared/locked/deteriorated before confirmation => NO BET / 0u.

## J. Settlement

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

Missing decision-critical draft, state, line, NKB, KCV/RFI, OKP/FCI/CL or synchronization input => widen uncertainty and `PASS/HOLD`.

## M. Tool order

For active maps:

1. checklist;
2. verdict;
3. logging / GitHub / Airtable / other connector work.

Connector work must never delay the live verdict.
