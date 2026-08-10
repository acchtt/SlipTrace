# Current League of Legends Model

**Canonical namespace:** `models/lol/`

- Active model: **LoL v0.3.51**
- Active rules: `models/lol/rules/MODEL_RULES_LOL_V0.3.51.md`
- Prior deltas: v0.3.50 through v0.3.26 under `models/lol/rules/`
- Mandatory live checklist: `models/lol/procedures/LOL_LIVE_VERDICT_EXECUTION_CHECKLIST_2026-08-10.md`
- Latest Total Kills recurrence review: `models/lol/reviews/HLE_GGA_G2_UNDER_SKIRMISH_RECURRENCE_REVIEW_2026-08-10.md`
- Prior Total Kills contact-realization review: `models/lol/reviews/FURIA_FLUXO_G2_OVER_CONTACT_REALIZATION_REVIEW_2026-08-10.md`
- Prior Total Kills / add-on correlation review: `models/lol/reviews/KC_FNC_GAME2_TOTAL_KILLS_CORRELATION_REVIEW_2026-08-10.md`
- Latest handicap conversion review: `models/lol/reviews/G2_TH_KILL_HANDICAP_CONVERSION_REVIEW_2026-08-09.md`
- Draft primacy review: `models/lol/reviews/JDG_WE_GAME2_DRAFT_PRIMACY_REVIEW_2026-08-09.md`
- Earlier Total Kills review: `models/lol/reviews/BFX_KRX_GAME2_TOTAL_KILLS_REVIEW_2026-08-09.md`
- Duration review: `models/lol/reviews/DURATION_MARKET_REBUILD_REVIEW_2026-08-09.md`
- Handicap directional review: `models/lol/reviews/KILL_HANDICAP_DIRECTIONAL_BIAS_REVIEW_2026-08-09.md`
- Portable baseline context: `models/lol/context/lol-v0.3.25/`
- Shared stake policy: `shared/STAKE_POLICY_V2.json`

## Required load order

1. `models/lol/CURRENT_MODEL.md`
2. v0.3.51 through v0.3.26 rule deltas
3. mandatory live checklist
4. latest reviews referenced above
5. item-verification suspension
6. v0.3.25 consolidated rules / probation / calibration handbook
7. live fast path and main betting procedure
8. connected-stack procedure and addenda
9. scoreboard protocol
10. shared stake policy
11. latest handoff last

Where conflicts exist, **v0.3.51 controls**.

## Operating state

- Official betting remains **paused** until explicit restoration.
- Official probation remains **13/20 settled/completed**, record 7-6, net -0.16425u / -164,250 VND.
- Next official wager after restoration: 14.
- Duration remains official-ineligible through wager 20.
- Default shadow stake: **0.25u**.
- Actual exposure while paused: **0u**.
- Minimum odds: **1.60**.
- Same-map shadow add-ons are enabled when each independently qualifies and joint correlation is explicitly priced.
- Airtable is the canonical position/map ledger; GitHub is the model/rules authority.

## Mandatory verdict format

First visible line on active maps:

- `TAKE — [selection] @[odds] — shadow 0.25u; actual 0u.`
- `PASS — [selection/market] @[odds] — 0u.`
- `HOLD — [selection/market] @[odds] — 0u.`

Logging/connectors occur after the live verdict and must not delay it.

# v0.3.51 — Early Under + Skirmish Recurrence Calibration

## Core correction

v0.3.50 correctly de-duplicates objective/event contact windows, but that must not erase repeatable **between-objective skirmish creation**.

Total Kills now separates:

1. **OKP** — Observed Kill Pace;
2. **FCI** — de-duplicated objective/event Forward Contact Inventory;
3. **CRR** — Contact Realization Rate for those windows;
4. **SRR** — Skirmish Recurrence Reserve between formal windows;
5. **CL** — Contact Lethality conditional on realized contact.

Conceptual projection:

`Final kills = current kills + CRR-weighted event-window kills + SRR kills + residual terminal/pick/chase kills`.

## Hard pre-12:00 Under gate

Before 12:00, an Under may not be TAKEN primarily because the current kill count is low or the line cushion is large.

Require at least one:

- two synchronized live snapshots >=90 seconds apart showing low OKP and stable/declining contact pressure;
- repeated realized contact already showing LOW CL through functioning disengage/peel/reset;
- an observed near-terminal structure-only branch removing future contact windows.

If only one live snapshot exists and repeatable hard access remains functional, default **HOLD/PASS**.

## Skirmish Recurrence Reserve (SRR)

Classify `LOW / MEDIUM / HIGH` recurrence from:

- vision/jungle collisions;
- lane-transition catches;
- side-lane collapses;
- support/jungle roam contact;
- post-reset re-engages;
- repeatable neutral picks after cooldown reset;
- flank/contact mechanisms not tied to a major objective.

Do not count engage champions as independent future fights. SRR measures **repeatability of contact triggers**, not champion count.

## Bidirectional Forcing (BF)

Flag `ACTIVE` when both teams can independently start meaningful contact without waiting for a voluntary objective-choke entry.

When active:

- raise SRR unless live evidence suppresses it;
- do not globally discount CRR from one side's poke/zone control;
- raise the high-total branch;
- explicitly increase high-T / low-to-moderate-M probability.

## Threat Deterrence override

Threat Deterrence must be classified `GLOBAL / LOCAL / NONE`.

If the opponent can bypass the zone via flank, fog, dash, displacement, point-click engage or transition timing, TD is only LOCAL and cannot support a broad Under CRR discount.

## Under cushion stress test

For every Under calculate:

- current kills;
- maximum additional kills that still win;
- additional kills required to lose;
- remaining map-time range;
- whether a plausible high-SRR branch of repeated 2-4 kill skirmishes plus objective/base fights can cross the line.

A large cushion never substitutes for the early confirmation gate.

## HLE.C vs GGA G2 calibration

Draft:

GGA Jayce / Skarner / Syndra / Varus / Leona  
HLE.C Yorick / Lee Sin / Annie / Jhin / Alistar

At 7:47: GGA 2-1, +1.0k, 0-0 towers, HLE.C 1-0 dragons.

Confirmed Under 33.5 @1.690 lost; final GGA 20-15 at 30:30, 35 total kills.

Correct v0.3.51 read:

- early Under confirmation gate: FAILED;
- FCI: medium;
- SRR: HIGH;
- BF: ACTIVE;
- Threat Deterrence: LOCAL only;
- CL: medium/high;
- high-T / low-M branch: material;
- verdict: **HOLD/PASS**, not TAKE.

# Retained Total Kills controls from v0.3.50 / v0.3.49

- Count event windows, not engage champions.
- For each major window test CONTEST / CONCEDE / TRADE / DELAY.
- Contest Compulsion only when concession/trade/delay becomes strategically or mechanically unavailable.
- Threat Deterrence can reduce contact, but v0.3.51 hard-access override applies.
- Loser return-kill floor must be matchup-functional.
- Quiet early score is not evidence of quiet future pace.
- Base Total Kills lower-bound gates remain +5pp pregame, +4pp early live, +3pp mid/late, with applicable surcharges capped at +9pp over break-even.
- Same-map Total Kills and handicap require separate `T` and `M` projections and an explicit four-cell joint distribution.

# Retained Kill Handicap controls

- Draft Primacy remains the primary post-lock mechanism layer.
- Build one side-neutral signed favorite kill-margin distribution before viewing directional attractiveness.
- Price +H and -H from the same distribution.
- Calculate NKB and Remaining Fight Inventory.
- Track KCV `HIGH / MEDIUM / LOW-STRUCTURE-SUBSTITUTED` from synchronized snapshots.
- Structure Substitution can make map dominance diverge from kill-margin dominance.
- Handicap lower-bound surcharge remains +7pp pregame, +6pp early live, +5pp mid/late.
- Handicap survival is not map survival.

# Retained Duration controls

- No pregame TAKE.
- No TAKE before 12:00.
- 12:00-13:59 requires two synchronized snapshots >=90 sec apart showing the same observed stall/acceleration mechanism.
- 14:00+ still requires observed stall/acceleration.
- Reprice after first tower, Baron, inhibitor, major structure/gold regime change.
- Duration and Total Kills remain separate.

# Position-blind reassessment

- ACTIVE: lower bound clears original break-even by current buffer.
- DEGRADED: above break-even but below buffer.
- INVALIDATED: at/below break-even or hard veto.
- CONFIRMED: materially strengthened under current framework.

Do not defend a recorded position because of entry price, stake, prior verdict or desire for consistency.

# Execution / settlement

- A TAKE is conditional/unrecorded until explicit confirmation of the same executable line/price.
- Disappeared/locked/deteriorated before confirmation => NO BET / 0u.
- User correction overrides visual scoreboard bugs.
- User statement `Final`, `final score`, or `X won` controls settlement when latest synchronized grading statistic is available.
- Unconfirmed recommendations are never graded.
- No martingale, rescue or loss chasing.
- Missing decision-critical information => PASS/HOLD.
