# Current League of Legends Model

**Canonical namespace:** `models/lol/`

- Active model: **LoL v0.3.48**
- Active rules: `models/lol/rules/MODEL_RULES_LOL_V0.3.48.md`
- Prior deltas: v0.3.47 through v0.3.26 under `models/lol/rules/`
- Mandatory live checklist: `models/lol/procedures/LOL_LIVE_VERDICT_EXECUTION_CHECKLIST_2026-08-09.md`
- Latest handicap conversion review: `models/lol/reviews/G2_TH_KILL_HANDICAP_CONVERSION_REVIEW_2026-08-09.md`
- Draft primacy review: `models/lol/reviews/JDG_WE_GAME2_DRAFT_PRIMACY_REVIEW_2026-08-09.md`
- Total Kills review: `models/lol/reviews/BFX_KRX_GAME2_TOTAL_KILLS_REVIEW_2026-08-09.md`
- Duration review: `models/lol/reviews/DURATION_MARKET_REBUILD_REVIEW_2026-08-09.md`
- Handicap directional review: `models/lol/reviews/KILL_HANDICAP_DIRECTIONAL_BIAS_REVIEW_2026-08-09.md`
- Portable baseline context: `models/lol/context/lol-v0.3.25/`
- Shared stake policy: `shared/STAKE_POLICY_V2.json`

## Required load order

1. `models/lol/CURRENT_MODEL.md`
2. v0.3.48 through v0.3.26 rule deltas
3. mandatory live checklist
4. item-verification suspension
5. v0.3.25 consolidated rules / probation / calibration handbook
6. live fast path and main betting procedure
7. connected-stack procedure and addenda
8. scoreboard protocol
9. shared stake policy
10. latest handoff last

Where conflicts exist, **v0.3.48 controls**.

## Operating state

- Official betting remains **paused** until explicit restoration.
- Official probation: **13/20 settled/completed**, record 7-6, net -0.16425u / -164,250 VND.
- Next official wager after restoration: 14.
- Duration remains official-ineligible through wager 20.
- Default shadow stake: **0.25u**.
- Actual exposure while paused: **0u**.
- Minimum odds: **1.60**.
- Same-map shadow add-ons are enabled when each independently qualifies and correlation is priced.
- Airtable is the canonical position/map ledger; do not infer the full ledger from abbreviated model notes.

## Mandatory verdict format

First visible line on active maps:

- `TAKE — [selection] @[odds] — shadow 0.25u; actual 0u.`
- `PASS — [selection/market] @[odds] — 0u.`
- `HOLD — [selection/market] @[odds] — 0u.`

Logging/connectors occur after the live verdict and must not delay it.

# v0.3.48 — Draft Primacy + Conversion-Rate Calibration

## Core principle

**Draft remains the most important post-lock conditional engine.** Team strength establishes the verified pre-draft baseline; once draft is locked, project the synchronized state through the exact matchup.

But kill handicap now has two mandatory layers:

1. **Draft direction:** who can force, survive, access, protect, damage and repeat?
2. **Conversion mode/speed:** if that team is winning, does the advantage become kills, picks, structures, objectives, side-lane pressure, or a mixture?

Do not equate map dominance with kill-margin dominance.

## Draft-to-Conversion classification

After the Draft Function Matrix, classify the likely win/conversion mode:

- Fight Cascade;
- Pick-and-Reset;
- Side-Lane / Global Overload;
- Objective / Structure Snowball;
- Siege / Choke;
- Scaling Front-to-Back;
- Mixed.

For Kill Handicap, estimate how much of the favorite-win branch is **kill-centric** versus **structure/objective-centric**.

## Kill Conversion Velocity (KCV)

With >=2 synchronized snapshots, track:

- signed kill-margin change;
- gold-lead change;
- tower/inhibitor change;
- objective gains;
- repeated 2+ net-kill fights;
- cleanup/chase after first contact.

Classify:

- `HIGH`: kill margin expands with the lead; repeated multi-kill conversion;
- `MEDIUM`: mixed kill/structure conversion;
- `LOW / STRUCTURE-SUBSTITUTED`: gold/structures expand while kill margin stays flat/slow.

## Structure Substitution (SS)

If a leader converts superiority mainly through towers, objectives, side lanes, Baron or inhibitors without corresponding kill-margin expansion:

- compress extreme favorite-margin bins;
- increase underdog +kills survival probability;
- recognize that efficient structure conversion can shorten the map and cannibalize future kills.

Baron/inhibitors are not automatically positive for favorite -kills.

## Net-Kill Burden (NKB) and Remaining Fight Inventory (RFI)

For every kill handicap, calculate how many additional **net kills** the favorite needs to beat the line from the current score.

Then inventory remaining windows and classify them:

- forced/high-contact;
- likely but avoidable;
- structure-only plausible;
- unlikely before end.

Relevant windows include dragon/soul, Baron/Elder, inhibitor siege, terminal base defense, side-lane collapse and demonstrated repeat-pick cycles.

A large NKB is not an automatic veto, but there must be a credible route from RFI to enough **net** kills.

## Wide Favorite Conversion Gate

For favorite **-10.5 or wider**, DED/DDC alone is insufficient.

Require at least one:

1. observed HIGH KCV;
2. NKB <=5 plus a high-contact fight/base-defense sequence;
3. >=2 high-contact forced windows plus demonstrated multi-kill cleanup/return denial;
4. early-live fast-path state with no evidence of structure-substituted conversion.

### Slow-conversion veto

If across two synchronized snapshots gold expands materially while kill margin is flat or expands by <=1, favorite -10.5+ is PASS/HOLD unless NKB <=5 or two clear high-contact windows remain.

This preserves cheap early favorite opportunities such as JDG -9.5 while preventing overextension into wide later lines without proven kill velocity.

## Handicap survival != map survival

For underdog +kills, separately estimate:

- `P(underdog wins map)`;
- `P(underdog covers | loses map)`.

The underdog can be strategically dead but still have a strong handicap position through return kills, counter-engage, peel, terminal base-defense kills, structure-substituted leader conversion or a large NKB relative to remaining fight inventory.

Do not invalidate +kills solely because favorite ML becomes overwhelming, DED appears, or Baron/inhibitors fall.

## Anti-cascade tools are graded

Classify defensive mechanisms as:

- `MAP-SAVING`;
- `MARGIN-SAVING`;
- `NONFUNCTIONAL`.

For kill handicap, MARGIN-SAVING tools matter even when they cannot save the map.

## G2 vs TH calibration

### Game 1

At 17:21 G2 led 5-2, +3.3k, towers 1-0 while TH held three dragons. G2 -11.5 @2.254 required +9 additional net kills.

From 15:50 to 17:21, gold expanded but kill margin stayed +3. KCV was not HIGH.

**Correct v0.3.48 process verdict: PASS — G2 -11.5 @2.254.**

Final G2 16-5, +12k, 8-2 towers, two Barons: dominant map, only +11 kill margin.

### Game 2

At 12:16 G2 led 8-3, +3.5k, towers 0-0. TH +13.5 @2.336 left G2 needing +9 additional net kills to beat the handicap, while TH retained K'Sante/Orianna/Lulu/Yunara margin-saving architecture.

**Correct entry remains TAKE — TH +13.5 @2.336.**

At 17:06 G2 led 11-3, +7k, towers 2-0. DED/DDC made the bet dangerous, but G2 still needed +6 additional net kills. Without a fresh reprice below TH's 42.81% break-even, the correct thesis state was **DEGRADED, not INVALIDATED**.

Final G2 17-7, +14k, 11-0 towers, Baron and three inhibitors: TH +13.5 still covered by 3.5 kills.

# v0.3.47 — Draft Primacy retained

## Mandatory Draft Function Matrix

Before any post-draft TAKE in ML, Kill Handicap or Total Kills, compare:

1. reliable first contact;
2. hard-CC density;
3. CC reliability and range;
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

Every credited tool must remain functional against the opponent's actual answers.

## CC Scarcity / Proactivity Tax

If the trailing team has zero/one reliable hard first-contact source or mostly conditional/defensive control while the leader has multiple reliable initiation layers:

- reduce trailing comeback forcing;
- reduce positive-handicap resilience;
- increase leader repeat-pick/chase branches;
- increase leader +10/+15 margin tail when already ahead.

**Durability is not control.**

## Distributed Economic Dominance (DED)

When role-level gold is shown, flag DED when the favorite leads in >=4 of 5 roles, the team gold lead is material for the clock, and at least one engage/control role plus one primary damage role are ahead/online.

Reference points only: approximately >=2.5k by 15:00, >=3.5k by 18:00, >=5k by 22:00.

## Draft-Dominance Cascade (DDC)

Flag DDC when:

- favorite has material live lead or DED;
- favorite has reliable first-contact / hard-CC edge;
- favorite has target-access plus damage-continuation advantage;
- trailer has weak proactive forcing or CC Scarcity Tax;
- >=3 meaningful future fight/pressure windows remain;
- no functioning hard anti-cascade mechanism is demonstrated.

DDC expands the favorite wide-margin tail, but v0.3.48 KCV/SS/NKB/RFI controls now govern whether that tail is large enough for a wide favorite handicap TAKE.

## Early Favorite Handicap Fast Path

Explicitly scan favorite -H when broad economic control, DED/DDC, draft access and future fight inventory align. This remains especially important for **-5.5 to -9.5** lines before the market widens.

"They still need +8/+9 more net kills" is arithmetic, not a veto — but for -10.5+ the v0.3.48 conversion gate is mandatory.

# v0.3.44 Kill Handicap controls retained

Use one side-neutral signed favorite-margin distribution:

`M = favorite final kills - underdog final kills`.

Minimum bins: `M<=0`, `+1..3`, `+4..6`, `+7..9`, `+10..14`, `15+`.

Price both handicap sides from the same distribution.

Lower-bound cover surcharge remains:

- +7pp pregame;
- +6pp early live;
- +5pp mid/late live.

Underdog resilience must be matchup-functional; v0.3.48 additionally distinguishes MAP-SAVING from MARGIN-SAVING mechanisms.

# v0.3.46 Total Kills controls retained

Total Kills must explicitly price current kills, line-cross arithmetic, fight-creation channels, unresolved forced-fight windows, soul-point conflict, Baron/Elder/base-defense reserve and clean-close versus kill-inflation branches.

Lower-bound gates:

- +5pp pregame;
- +4pp early live;
- +3pp mid/late;
- pregame Under with >=4 fight channels and >=3 forced-fight windows: +7pp.

Objective-only updates cannot positively upgrade an Under without synchronized kills.

# v0.3.45 Duration controls retained

Duration remains live-only:

- no pregame TAKE;
- no TAKE before 12:00;
- 12:00-13:59 high-friction two-snapshot gate;
- 14:00+ requires observed stall/acceleration;
- dead-zone, survival-horizon and regime-change repricing remain mandatory.

Draft is only a mechanism prior for Duration until observed functioning proves the acceleration/stall state.

# Position-blind reassessment

- ACTIVE: lower bound clears original break-even by current buffer.
- DEGRADED: above break-even but below buffer.
- INVALIDATED: at/below break-even or hard veto.
- CONFIRMED: materially strengthened under the current framework.

For +kills positions, do not infer INVALIDATED from favorite map dominance alone. Reprice the signed margin distribution first.

# Execution / settlement

- A TAKE is conditional/unrecorded until explicit confirmation of the same executable line/price.
- Disappeared/locked/deteriorated before confirmation => NO BET / 0u.
- User correction overrides visual scoreboard bugs.
- User statement `Final` controls settlement when latest synchronized grading statistic is available.
- Unconfirmed recommendations are never graded.
- No martingale, rescue or loss chasing.
- Missing decision-critical information => PASS/HOLD.
