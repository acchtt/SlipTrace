# Current League of Legends Model

**Canonical namespace:** `models/lol/`

- Active model: **LoL v0.3.49**
- Active rules: `models/lol/rules/MODEL_RULES_LOL_V0.3.49.md`
- Prior deltas: v0.3.48 through v0.3.26 under `models/lol/rules/`
- Mandatory live checklist: `models/lol/procedures/LOL_LIVE_VERDICT_EXECUTION_CHECKLIST_2026-08-10.md`
- Latest Total Kills / add-on correlation review: `models/lol/reviews/KC_FNC_GAME2_TOTAL_KILLS_CORRELATION_REVIEW_2026-08-10.md`
- Latest handicap conversion review: `models/lol/reviews/G2_TH_KILL_HANDICAP_CONVERSION_REVIEW_2026-08-09.md`
- Draft primacy review: `models/lol/reviews/JDG_WE_GAME2_DRAFT_PRIMACY_REVIEW_2026-08-09.md`
- Earlier Total Kills review: `models/lol/reviews/BFX_KRX_GAME2_TOTAL_KILLS_REVIEW_2026-08-09.md`
- Duration review: `models/lol/reviews/DURATION_MARKET_REBUILD_REVIEW_2026-08-09.md`
- Handicap directional review: `models/lol/reviews/KILL_HANDICAP_DIRECTIONAL_BIAS_REVIEW_2026-08-09.md`
- Portable baseline context: `models/lol/context/lol-v0.3.25/`
- Shared stake policy: `shared/STAKE_POLICY_V2.json`

## Required load order

1. `models/lol/CURRENT_MODEL.md`
2. v0.3.49 through v0.3.26 rule deltas
3. mandatory live checklist
4. item-verification suspension
5. v0.3.25 consolidated rules / probation / calibration handbook
6. live fast path and main betting procedure
7. connected-stack procedure and addenda
8. scoreboard protocol
9. shared stake policy
10. latest handoff last

Where conflicts exist, **v0.3.49 controls**.

## Operating state

- Official betting remains **paused** until explicit restoration.
- Official probation: **13/20 settled/completed**, record 7-6, net -0.16425u / -164,250 VND.
- Next official wager after restoration: 14.
- Duration remains official-ineligible through wager 20.
- Default shadow stake: **0.25u**.
- Actual exposure while paused: **0u**.
- Minimum odds: **1.60**.
- Same-map shadow add-ons are enabled when each independently qualifies and joint correlation is explicitly priced.
- Airtable is the canonical position/map ledger; do not infer the full ledger from abbreviated model notes.

## Mandatory verdict format

First visible line on active maps:

- `TAKE — [selection] @[odds] — shadow 0.25u; actual 0u.`
- `PASS — [selection/market] @[odds] — 0u.`
- `HOLD — [selection/market] @[odds] — 0u.`

Logging/connectors occur after the live verdict and must not delay it.

# v0.3.49 — Forward Contact Inventory + Joint Correlation Calibration

## Core correction

For Total Kills, **observed pace is not future pace**.

Every Total Kills evaluation must separately model:

1. **Observed Kill Pace (OKP)** — what has happened so far;
2. **Forward Contact Inventory (FCI)** — how many future matchup-functional contact windows remain;
3. **Contact Lethality (CL)** — how many deaths are likely when those contacts occur.

A low current kill count cannot by itself support or upgrade an Under. A quiet start can still become a high-contact mid/late game when objective pressure makes contests compulsory.

## Quiet-start non-persistence

Before 15:00, low kills or low kills/minute cannot by themselves increase Under probability.

An early Under upgrade requires at least one:

- >=2 synchronized snapshots showing both low OKP and declining/limited FCI;
- repeated contact resolving with low CL because disengage/peel is demonstrably functional;
- a clean structure-only/terminal branch that removes future contact windows faster than it creates them.

`Quiet so far` is not `quiet later`.

## Forward Contact Inventory

For each remaining window, classify actual expected contact:

- `FORCED / HIGH-CONTACT`;
- `LIKELY CONTACT`;
- `AVOIDABLE / TRADEABLE`;
- `STRUCTURE-ONLY PLAUSIBLE`;
- `UNLIKELY BEFORE END`.

Relevant windows include dragon/soul, Baron/Elder, inhibitor/base defense, side-lane collapses, repeat-pick cycles, vision face-checks and terminal chases.

Objectives are not automatically fights.

## Contest Compulsion

A trailing team can become more kill-generating as the map worsens because it loses the option to concede indefinitely.

Flag Contest Compulsion when the leader controls objective terrain and the trailer must eventually enter enemy control to contest soul, Baron, inhibitors or terminal pressure.

When active, increase FCI.

Poke, waveclear and globals only suppress kills if they actually allow safe avoidance or disengage.

## Contact Lethality

Set CL `LOW / MEDIUM / HIGH` using:

- reliable first contact;
- hard-access reliability;
- CC chain;
- damage continuation;
- chase/cleanup;
- re-engage;
- disengage/peel;
- mobility/escape;
- return-kill capability;
- terrain/choke amplification;
- live economic concentration.

**Range is not disengage.** If the leader has reliable hard access and the trailer cannot escape after contact, raise CL even if the trailer draft is nominally poke/waveclear/side-lane oriented.

## Total Kills forward projection

Use:

`Final Total Kills = Current Kills + kills from remaining FCI windows + low-contact residual kills`.

Internally lock low/central/high final-kill branches, line-cross probability and uncertainty.

For Under, large cushion is arithmetic rather than evidence.

## Hard-access Under surcharge

For pregame or early-live Under, if all are true:

- one side has >=1 highly reliable hard-access tool plus follow-up;
- the opponent has weak functional disengage after first contact;
- >=3 meaningful future objective/base-defense windows are likely;

add **+2pp** to the normal Total Kills lower-bound requirement, capped at a total required cushion of +9pp over break-even.

If FCI contains >=3 forced/high-contact windows and CL is HIGH, Under defaults PASS unless explicit window arithmetic still clears the gate.

Base Total Kills lower-bound gates remain:

- +5pp pregame;
- +4pp early live;
- +3pp mid/late;
- retained high-friction pregame Under gate from v0.3.46, with v0.3.49 surcharge layered where applicable.

## Total Kills and Kill Handicap are separate axes

Define:

- `T = favorite kills + underdog kills`;
- `M = favorite kills - underdog kills`.

Project T and M separately.

Possible branches:

- high T, low/moderate M: traded fights / return kills;
- low T, high M: clean one-sided kill conversion;
- low T, low M: structure-heavy controlled map;
- high T, high M: true kill cascade.

A +kills handicap can be strong while an Under is weak because return kills can raise T while keeping M inside the cushion.

## Same-map add-on joint distribution

For positions A and B, estimate:

- `P(A win, B win)`;
- `P(A win, B lose)`;
- `P(A lose, B win)`;
- `P(A lose, B lose)`.

Identify concrete mechanisms for materially non-zero one-win/one-loss branches.

Each add-on must independently clear its market gate and remain +EV after joint-distribution adjustment. Do not reuse one narrative as two independent edges. No stake escalation.

## KC vs FNC Game 2 calibration

Draft:

KC Yorick / Vi / Viktor / Kalista / Renata  
FNC Jayce / Olaf / Ryze / Ziggs / Shen

Confirmed positions:

- Under 27.5 @1.955 — LOSS;
- FNC +13.5 @2.122 — WIN.

Final KC 20-8 at 31:53: T=28, M=+12.

The Under engine correctly saw structure/side-lane conversion routes but underweighted Vi hard access, Renata fight extension, FNC's weak full disengage and later compulsory contests.

Correct v0.3.49 interpretation of the pregame Under is **PASS unless the explicit OKP/FCI/CL projection clears the higher hard-access gate**.

At 10:48, KC 5-1 with only six total kills did **not** justify an Under upgrade by itself because FCI and CL remained substantial.

The FNC +13.5 entry remains correct: KC still needed +10 additional net kills from entry and ultimately won by +12, validating the v0.3.48 handicap-survival framework.

# v0.3.48 — Kill Handicap Conversion Framework retained

## Draft-to-Conversion

After the Draft Function Matrix, classify likely win/conversion mode:

- Fight Cascade;
- Pick-and-Reset;
- Side-Lane / Global Overload;
- Objective / Structure Snowball;
- Siege / Choke;
- Scaling Front-to-Back;
- Mixed.

For Kill Handicap, estimate how much of the favorite-win branch is kill-centric versus structure/objective-centric.

## Kill Conversion Velocity (KCV)

With >=2 synchronized snapshots track signed margin, gold, structures, objectives, multi-kill conversion and cleanup.

Set:

- `HIGH` — margin expands with lead; repeated 2+ net-kill conversion;
- `MEDIUM` — mixed kill/structure conversion;
- `LOW / STRUCTURE-SUBSTITUTED` — map control expands while margin stays flat/slow.

## Structure Substitution

If superiority converts mainly through towers/objectives/side lanes/Baron without corresponding kill-margin expansion:

- compress extreme favorite-margin bins;
- increase underdog +kills survival;
- recognize map compression can cannibalize future net kills.

## Net-Kill Burden and Remaining Fight Inventory

For every kill handicap calculate additional net kills required to beat the line, then compare against remaining forced/high-contact, avoidable, structure-only and unlikely windows.

## Wide Favorite Conversion Gate

For favorite -10.5 or wider, DED/DDC alone is insufficient.

Require at least one:

1. observed HIGH KCV;
2. NKB <=5 plus a high-contact fight/base-defense sequence;
3. >=2 high-contact forced windows plus demonstrated multi-kill cleanup/return denial;
4. early-live fast-path state with no evidence of Structure Substitution.

Slow-conversion veto remains active when gold expands but margin stays flat/near-flat.

## Handicap survival != map survival

For underdog +kills separately estimate map-win probability and cover probability conditional on losing.

Do not invalidate +kills solely because favorite ML becomes overwhelming, DED appears, or Baron/inhibitors fall.

Defensive tools are graded `MAP-SAVING / MARGIN-SAVING / NONFUNCTIONAL`.

# v0.3.47 — Draft Primacy retained

Before post-draft ML, Kill Handicap or Total Kills TAKE, compare:

1. reliable first contact;
2. hard-CC density;
3. CC reliability and range;
4. anti-engage/disengage;
5. frontline access;
6. backline access;
7. carry protection;
8. damage continuation;
9. chase/cleanup;
10. re-engage/repeat forcing;
11. objective/choke control;
12. waveclear/base defense under pressure;
13. side-lane/global numbers creation;
14. execution simplicity.

Draft remains the most important post-lock conditional mechanism layer. Team strength remains the verified pre-draft baseline.

CC Scarcity / Proactivity Tax, Distributed Economic Dominance, Draft-Dominance Cascade and the Early Favorite Handicap Fast Path remain active.

# v0.3.44 Kill Handicap controls retained

Use one side-neutral signed favorite-margin distribution:

`M = favorite final kills - underdog final kills`.

Minimum bins: `M<=0`, `+1..3`, `+4..6`, `+7..9`, `+10..14`, `15+`.

Price both sides from the same distribution.

Lower-bound cover surcharge remains:

- +7pp pregame;
- +6pp early live;
- +5pp mid/late live.

# v0.3.45 Duration controls retained

Duration remains live-only:

- no pregame TAKE;
- no TAKE before 12:00;
- 12:00-13:59 high-friction two-snapshot gate;
- 14:00+ requires observed stall/acceleration;
- dead-zone, survival-horizon and regime-change repricing remain mandatory.

Draft is only a mechanism prior for Duration until observed functioning proves the state.

# Position-blind reassessment

- ACTIVE: lower bound clears original break-even by current buffer.
- DEGRADED: above break-even but below buffer.
- INVALIDATED: at/below break-even or hard veto.
- CONFIRMED: materially strengthened under current framework.

For +kills positions, do not infer INVALIDATED from favorite map dominance alone. Reprice the signed margin distribution first.

For Total Kills positions, do not infer CONFIRMED from quiet current score alone. Reprice OKP/FCI/CL first.

# Execution / settlement

- A TAKE is conditional/unrecorded until explicit confirmation of the same executable line/price.
- Disappeared/locked/deteriorated before confirmation => NO BET / 0u.
- User correction overrides visual scoreboard bugs.
- User statement `Final` controls settlement when latest synchronized grading statistic is available.
- Unconfirmed recommendations are never graded.
- No martingale, rescue or loss chasing.
- Missing decision-critical information => PASS/HOLD.
