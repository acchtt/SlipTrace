# Current League of Legends Model

**Canonical namespace:** `models/lol/`

- Active model: **LoL v0.3.47**
- Active rules: `models/lol/rules/MODEL_RULES_LOL_V0.3.47.md`
- Prior deltas: v0.3.46 through v0.3.26 under `models/lol/rules/`
- Mandatory live checklist: `models/lol/procedures/LOL_LIVE_VERDICT_EXECUTION_CHECKLIST_2026-08-09.md`
- Latest draft calibration review: `models/lol/reviews/JDG_WE_GAME2_DRAFT_PRIMACY_REVIEW_2026-08-09.md`
- Total Kills review: `models/lol/reviews/BFX_KRX_GAME2_TOTAL_KILLS_REVIEW_2026-08-09.md`
- Duration review: `models/lol/reviews/DURATION_MARKET_REBUILD_REVIEW_2026-08-09.md`
- Handicap directional review: `models/lol/reviews/KILL_HANDICAP_DIRECTIONAL_BIAS_REVIEW_2026-08-09.md`
- Portable baseline context: `models/lol/context/lol-v0.3.25/`
- Shared stake policy: `shared/STAKE_POLICY_V2.json`

## Required load order

1. `models/lol/CURRENT_MODEL.md`
2. v0.3.47 through v0.3.26 rule deltas
3. mandatory live checklist
4. item-verification suspension
5. v0.3.25 consolidated rules / probation / calibration handbook
6. live fast path and main betting procedure
7. connected-stack procedure and addenda
8. scoreboard protocol
9. shared stake policy
10. latest handoff last

Where conflicts exist, **v0.3.47 controls**.

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

## v0.3.47 — Draft Primacy

### Core principle

**Team strength sets the pre-draft baseline. Draft interaction is the primary conditional engine after draft lock.**

Once the draft is known, do not treat composition as a small cosmetic probability adjustment. For live markets, project how the synchronized state converts through the exact matchup.

The central question is:

`Given the current state, which composition can force, survive, convert and repeat the next sequence?`

### Mandatory Draft Function Matrix

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

### CC Scarcity / Proactivity Tax

If the trailing team has zero/one reliable hard first-contact source or mostly conditional/defensive control while the leader has multiple reliable initiation layers:

- reduce trailing comeback forcing;
- reduce positive-handicap resilience;
- increase leader repeat-pick/chase branches;
- increase leader +10/+15 margin tail when already ahead.

**Durability is not control.** Do not count tankiness as engage, peel, disengage or comeback forcing.

### Distributed Economic Dominance (DED)

When role-level gold is shown, flag DED when the favorite leads in >=4 of 5 roles, the team gold lead is material for the clock, and at least one engage/control role plus one primary damage role are ahead/online.

Reference points only: approximately >=2.5k by 15:00, >=3.5k by 18:00, >=5k by 22:00.

Do not invent DED without role-level economic evidence.

### Draft-Dominance Cascade (DDC)

Flag DDC when:

- favorite has material live lead or DED;
- favorite has reliable first-contact / hard-CC edge;
- favorite has target-access plus damage-continuation advantage;
- trailer has weak proactive forcing or CC Scarcity Tax;
- >=3 meaningful future fight/pressure windows remain;
- no functioning hard anti-cascade mechanism is demonstrated.

When DDC is active, materially expand the favorite `+10..14` and `15+` margin bins.

If `P(favorite wins by 10+ | favorite wins) <60%` during DDC, require >=2 independent matchup-functional anti-cascade mechanisms or recalculate the tail upward.

### Early Favorite Handicap Fast Path

Before defaulting to the positive handicap, explicitly scan favorite -H when:

- favorite controls the map economically;
- DED or equivalent broad control is present;
- DDC is active/nearly active;
- current line remains inside projected cascade tail;
- enough objective/fight inventory remains;
- exact price clears v0.3.44 surcharge.

"They still need +8/+9 more net kills" is arithmetic, not a veto.

### JDG vs WE calibration

At 11:46:

- JDG 6-4 WE;
- JDG +2.9k;
- towers 0-0;
- WE 1-0 dragons;
- JDG ahead economically in four roles, especially jungle and mid;
- JDG draft: Olaf / Jarvan IV / Syndra / Ezreal / Nautilus;
- WE draft: Mundo / Xin Zhao / Viktor / Lucian / Milio;
- JDG -9.5 @1.844.

The old model over-credited WE's nominal durability/waveclear/peel and underweighted its limited reliable proactive CC versus JDG's layered initiation and safe follow-up.

Reconstructed `P(JDG margin >=10)` is approximately 60-67%; break-even 54.23%; early-live surcharge threshold ~60.23%.

**Correct v0.3.47 process verdict: TAKE — JDG -9.5 @1.844.**

Final 19-5 confirms the mechanism but does not enter the ledger because the bet was not actually taken.

## v0.3.44 Kill Handicap controls retained

Use one side-neutral signed favorite-margin distribution:

`M = favorite final kills - underdog final kills`.

Minimum bins: `M<=0`, `+1..3`, `+4..6`, `+7..9`, `+10..14`, `15+`.

Price both handicap sides from the same distribution.

Lower-bound cover surcharge remains:

- +7pp pregame;
- +6pp early live;
- +5pp mid/late live.

v0.3.47 changes construction of the distribution through draft/state interaction; it does **not** weaken the probability threshold.

Underdog resilience must be matchup-functional: demonstrated disengage, safe waveclear, anti-dive, counter-initiation, safe retreat damage, objective contest or return kills. Durability alone is insufficient.

## v0.3.46 Total Kills controls retained

Total Kills must explicitly price:

- current kills and line-cross arithmetic;
- functional fight-creation channels;
- unresolved dragon/soul/Baron/Elder/base-defense windows;
- clean-close versus kill-inflation branches;
- low/central/high final-kill distributions.

Lower-bound gates:

- +5pp pregame;
- +4pp early live;
- +3pp mid/late;
- pregame Under with >=4 fight channels and >=3 forced-fight windows: +7pp.

Current kill count is decision-critical. Objective-only updates cannot positively upgrade an Under without synchronized kills.

If an existing Under has <=4 kills of cushion and a major forced contest/base-defense sequence remains, default to INVALIDATED absent a near-terminal clean close.

## v0.3.45 Duration controls retained

Duration remains live-only:

- no pregame TAKE;
- no TAKE before 12:00;
- 12:00-13:59 high-friction two-snapshot gate;
- 14:00+ requires observed stall/acceleration;
- dead-zone, survival-horizon and regime-change repricing remain mandatory.

Draft is only a mechanism prior for Duration until observed functioning proves the acceleration/stall state.

## Position-blind reassessment

Recorded position and current thesis remain separate.

- ACTIVE: lower bound clears original break-even by current buffer.
- DEGRADED: above break-even but below buffer.
- INVALIDATED: at/below break-even or hard veto.
- CONFIRMED: materially strengthened under the current framework.

Re-run the Draft Function Matrix after meaningful gold/kill/structure/objective changes or when a theoretical defensive mechanism fails.

## Execution / settlement

- A TAKE is conditional/unrecorded until explicit confirmation of the same executable line/price.
- Disappeared/locked/deteriorated before confirmation => NO BET / 0u.
- User correction overrides visual scoreboard bugs.
- User statement `Final` controls settlement when latest synchronized grading statistic is available.
- Unconfirmed recommendations are never graded.
- No martingale, rescue or loss chasing.
- Missing decision-critical information => PASS/HOLD.
