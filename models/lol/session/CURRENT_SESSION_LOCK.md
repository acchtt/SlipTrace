# Current LoL Session Lock

**Lock ID:** `LOL-2026-09-03-V13-DK-BFX-DRAFTONLY-FORCEDCHOICE-1644-UTC7`  
**Status:** `ACTIVE`  
**Scope:** `LCK 2026 Season Playoffs — Lower Bracket Round 1 — Dplus KIA vs BNK FearX — Bo5 Fearless Draft`  
**Supersedes:** `LOL-2026-09-02-V13-HLE-T1-DRAFTONLY-FORCEDCHOICE-1459-UTC7` prospectively; HLE-T1 is complete and its lock is stale historical state  
**Authority commit:** `7420942bee48a943a076239d2b9acf074fb833f0`  
**Active analytical model:** `LoL v1.3 — benchmark-aware core + lock-scoped Draft-Only Forced-Choice Execution Mode + post-audit DIM enforcement`  
**Execution mode:** `POSTDRAFT-ONLY INPUTS / IGNORE DISPLAYED MATCH CLOCK / FORCE ONE SIDE PER OFFERED MARKET`  
**Circuit breaker / actual exposure:** `CLEAR / 0u actual`  
**Default shadow stake:** `0.25u per market family`

## Required authority stack

Load from authority commit `7420942bee48a943a076239d2b9acf074fb833f0`:

1. `models/lol/CURRENT_MODEL.md`;
2. `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. `models/lol/procedures/LOL_V1.3_TEAM_BENCHMARK_GOLGG_2026-08-30.md`;
4. `models/lol/rules/MODEL_RULES_LOL_V1.3_MONEYLINE_HIERARCHY_CORE.md`;
5. `models/lol/procedures/LOL_V1.3_MONEYLINE_LIVE_PROCEDURE_2026-08-29.md` as base analytical context, superseded on timing/live inputs by the draft-only overlay;
6. `models/lol/rules/MODEL_RULES_LOL_V1.1_DURATION_CORE.md`;
7. `models/lol/procedures/LOL_V1.1_DURATION_LIVE_PROCEDURE_2026-08-29.md` as base analytical context, superseded on timing/live inputs by the draft-only overlay;
8. `models/lol/procedures/LOL_V1.3_VALIDATION_PROTOCOL_2026-08-29.md`;
9. `models/lol/procedures/LOL_V1.3_SESSION_AUTHORITY_AND_EXECUTION_2026-08-29.md`;
10. `models/lol/procedures/LOL_DRAFT_INTERACTION_MATRIX_2026-08-20.md`;
11. `models/lol/procedures/LOL_DRAFT_ONLY_EXECUTION_MODE_2026-08-31.md` as the lock-scoped execution overlay;
12. `models/lol/reviews/LOL_FORCED_CHOICE_CHECKPOINT_AUDIT_2026-09-02.md` for procedural enforcement only; no coefficient change;
13. this mutable lock's forced-choice and portfolio-coherence overrides last.

Latest migration state loaded separately and does not override analytical authority:
`models/lol/handoffs/CHAT_MIGRATION_HANDOFF_2026-09-03.md`.

## User-directed forced-choice override — ACTIVE prospectively

Operational interpretation for the current forced-choice shadow cohort:
- no live-state predictions;
- enabled families: `Moneyline + Kill Handicap + Duration + Total Kills`;
- exactly one canonical forced-choice Position per executable family per map;
- when alternate lines exist inside a family, evaluate all supplied lines but select only the single best-fit canonical line/side;
- `PASS` is disabled for executable offered binary markets;
- old minimum-odds, edge, and selected-side thesis gates remain diagnostic only and are not forced-choice execution vetoes;
- price cannot alter benchmark, DIM/draft classification, ML probability, KH margin distribution, duration F, or Total Kills distribution;
- after price-blind projections are locked, choose the better model-vs-book side; if both sides are negative EV, choose the less-negative side;
- tag every selected side with `MODEL_EDGE` and `FORCED_NEG_EV=YES/NO`;
- if quote/settlement data are insufficient, use execution-data `HOLD` until clarified;
- supplied final draft + board is standing authorization for all selected forced-choice shadow Positions; no extra per-line confirmation required;
- shadow stake `0.25u` per family; actual exposure `0u`;
- no chasing, rescue, martingale, averaging down, or stake escalation.

Forced-choice results remain a separate experimental cohort from threshold-qualified selective calibration.

## Portfolio-coherence override — ACTIVE prospectively

Kill Handicap must be portfolio-consistent with the selected Moneyline side when the absolute handicap is below 5 kills:
- for `±4.5` or any smaller absolute kill handicap, the selected KH team must be the same team selected on ML;
- do not select opposite-side `+4.5` while selecting the other team ML;
- for `±5.5` or wider, KH may be evaluated independently because the cushion is materially different;
- this rule is prospective only and does not rewrite HLE-T1 Game 5 or any earlier Position.

## Timing / information controls

- final draft/roles plus exact market board are the prediction inputs;
- ignore displayed match clock for execution eligibility;
- do not use in-map kills, gold, objectives, structures, role resources, or other live-state evidence in prediction;
- pre-series benchmark remains frozen for the entire series;
- same-series results are quarantined from benchmark construction and never update K/P0;
- because this lock is being established after the scheduled series start, no Position may be created retroactively for any map already started or completed before this lock existed.

## Series identification

Current series:
- `Dplus KIA (DK)` vs `BNK FearX (BFX)`;
- competition: `LCK 2026 Season Playoffs`;
- stage: `Lower Bracket Round 1`;
- date: `2026-09-03`;
- scheduled: `08:00 UTC / 15:00 UTC+7`;
- format: `Bo5 Fearless Draft`.

Identification sources checked fresh on 2026-09-03: Riot LoL Esports schedule and Games of Legends / gol.gg playoff match list.

Series score/current map at lock: `NOT USED FOR ANALYSIS — same-series state intentionally quarantined`.

## Frozen DK vs BFX Gol.gg benchmark

Primary source: Games of Legends / gol.gg team tournament tables. Current window is completed `LCK 2026 Rounds 3-4`; previous comparable window is completed `LCK 2026 Rounds 1-2`. Sportsbook prices, playoff results, and all 2026-09-03 same-series state are excluded.

Current Rounds 3-4 core inputs:
- `DK`: 20 games, WinRate `55.0%`, GDM `+25`, GD@15 `-694`, Towers `6.6-5.5`, DRA% `54.4`, NASH% `61.1`;
- `BFX`: 20 games, WinRate `50.0%`, GDM `+14`, GD@15 `+579`, Towers `6.4-5.2`, DRA% `44.9`, NASH% `52.8`.

Previous Rounds 1-2 core inputs:
- `DK`: 42 games, WinRate `57.1%`, GDM `+64`, GD@15 `+619`, Towers `6.3-5.1`, DRA% `48.8`, NASH% `49.1`;
- `BFX`: 39 games, WinRate `35.9%`, GDM `-100`, GD@15 `-741`, Towers `5.0-6.3`, DRA% `45.1`, NASH% `41.7`.

League-relative split scores under the frozen benchmark formula:
- `B_current(DK)=+0.174447`;
- `B_current(BFX)=+0.278708`;
- `B_previous(DK)=+0.412956`;
- `B_previous(BFX)=-0.624751`.

Roster continuity: current expected playoff fives are meaningfully continuous with the prior benchmark window; use the normal `70/30 current/previous` blend. BFX had earlier Rounds 1-2 rotations, but the current Clear/Raptor/VicLa/Taeyoon/Kellin core was already active inside that window; no new between-window material role rebuild is applied. User-supplied final draft/lineup evidence overrides public roster context if different.

Blended raw scores:
- `B_raw(DK)=+0.246000`;
- `B_raw(BFX)=+0.007670`.

After re-standardizing the full 10-team LCK peer set:
- `B(DK)=+0.334587`;
- `B(BFX)=+0.010432`;
- `GAP(DK-BFX)=+0.324155 SD`.

Frozen series prior:
- `DK K=0 / P0=50%`;
- `BFX K=0 / P0=50%`.

Compact record:
`TEAM_BENCH[LEAGUE=LCK2026;CURRENT=R3-4;PREVIOUS=R1-2;G_DK=20;G_BFX=20;B_CUR_DK=0.174447;B_CUR_BFX=0.278708;B_PREV_DK=0.412956;B_PREV_BFX=-0.624751;BLEND_DK=0.246000;BLEND_BFX=0.007670;B_DK=0.334587;B_BFX=0.010432;GAP_DK_BFX=0.324155;K_DK=0;K_BFX=0;ROSTER_ADJ=NORMAL;PRICE_USED=N;SAME_SERIES_USED=N]`.

## Expected roster context

Dplus KIA:
- Siwoo — TOP
- Lucid — JUNGLE
- ShowMaker — MID
- Smash — ADC
- Career — SUPPORT

BNK FearX:
- Clear — TOP
- Raptor — JUNGLE
- VicLa — MID
- Taeyoon — ADC
- Kellin — SUPPORT

Public roster evidence is contextual only. Final user-supplied draft/roles are authoritative for map-specific DIM.

## Price-blind family projections

### Moneyline
With no live variables in draft-only mode:
`P(A)=clamp(P0(A)+4.5*D pp,15%,85%)`.

Post-audit certification rule:
- complete full DIM first;
- certify `D=+1/-1` only when at least two independent mechanism advantages survive the adversarial failure-path pass;
- otherwise use `D=0 / EVEN-STYLE-DEPENDENT`.

Lock P before price, then choose one quoted side in forced-choice mode.

### Kill Handicap
Construct a full side-neutral signed final kill-margin distribution before line/price. Explicitly include clean-cascade, ordinary-margin, close-game, and opponent return-kill branches. The distribution must be consistent with the draft-only ML probability.

Apply the portfolio-coherence rule after ML side selection:
- absolute handicap `<5`: KH team must align with ML team;
- absolute handicap `>=5.5`: KH can remain independent.

### Duration
Use the v1.1 core at `t=0`; score draft-only `V/Q/H/T`, lock `F` before line/price, then choose Over or Under.

### Total Kills
Current-window pre-series environments:
- `BFX`: `16.1 kills/game + 14.8 deaths/game = 30.9` total-kill environment;
- `DK`: `12.9 kills/game + 13.0 deaths/game = 25.9` total-kill environment.

Frozen current-window baseline:
`TK0=(30.9+25.9)/2=28.4 kills`.

Current samples are 20 games each, so no previous-window blend is required for TK0. Build full total-kill bins before line/price and explicitly separate clean-cascade, two-sided brawl, and controlled low-contact close branches.

## Forced-choice cohort state at lock

Canonical cohort entering this series:
- `28 Positions / 7 samples per family`;
- overall `13W-15L`;
- shadow P/L `-0.9980u`;
- actual exposure `0u`.

By family:
- Moneyline `1-6 / -1.3305u`;
- Kill Handicap `3-4 / -0.3475u`;
- Duration `4-3 / +0.0795u`;
- Total Kills `5-2 / +0.6005u`.

Next formal checkpoint:
- `40 canonical Positions / 10 samples per family`;
- exactly `3 more fully recorded maps / 12 positions` from this lock state.

No structural coefficient change before that checkpoint unless a clear implementation bug is identified.

## Speed-first map workflow

1. Receive final current-map draft/roles plus exact board.
2. Complete full DIM and all four price-blind family projections/distributions before using price as analytical evidence.
3. Select exactly one canonical line/side per executable family, applying the `<5 kills => ML-aligned KH` rule.
4. User-visible first line immediately: `[Map]: ML / KH / Duration / Total Kills — 1.00u shadow total.`
5. Follow with only the shortest necessary DIM/mechanism, probability/distribution, `MODEL_EDGE`, and `FORCED_NEG_EV` notes.
6. Record each selected family as `FORCED-CHOICE`, `0.25u shadow / 0u actual`.
7. Defer Airtable writes until map end; then settle the map and all canonical Positions in one batch.
8. Perform the full post-audit micro-review and update cohort counts after settlement.

If authority/overlay mismatch occurs outside this explicit override: `MODEL LOCK MISMATCH — HOLD`.
