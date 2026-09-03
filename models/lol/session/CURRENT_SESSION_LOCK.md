# Current LoL Session Lock

**Lock ID:** `LOL-2026-09-04-V13-KT-DK-DRAFTONLY-FORCEDCHOICE-Q2-1955-UTC7`  
**Status:** `ACTIVE`  
**Scope:** `LCK 2026 Season Playoffs — Lower Bracket Round 2 — KT Rolster vs Dplus KIA — Bo5 Fearless Draft`  
**Supersedes:** `LOL-2026-09-03-V13-DK-BFX-DRAFTONLY-FORCEDCHOICE-1644-UTC7` (closed historical lock)  
**Authority commit:** `6018e7706772554d6318c1af4a9548ca4f25cd95`  
**Active analytical model:** `LoL v1.3 — benchmark-aware core + lock-scoped Draft-Only Forced-Choice Validation Block Q2`  
**Execution mode:** `POSTDRAFT-ONLY INPUTS / IGNORE DISPLAYED MATCH CLOCK / FORCE ONE SIDE PER OFFERED MARKET`  
**Circuit breaker / actual exposure:** `CLEAR / 0u actual`  
**Default shadow stake:** `0.25u per market family`

## Required authority stack

Load from authority commit `6018e7706772554d6318c1af4a9548ca4f25cd95`:

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
11. `models/lol/procedures/LOL_DRAFT_ONLY_EXECUTION_MODE_2026-08-31.md`;
12. `models/lol/reviews/LOL_FORCED_CHOICE_CHECKPOINT_AUDIT_2026-09-03_40_POSITIONS.md`;
13. this mutable lock's Q2 forced-choice / quarantine / portfolio overrides last.

Canonical `CURRENT_MODEL.md` remains unchanged. The Q2 controls below apply only to this forced-choice validation overlay.

## User-directed forced-choice override — ACTIVE

- no live-state predictions;
- enabled families: `Moneyline + Kill Handicap + Duration + Total Kills`;
- exactly one canonical forced-choice Position per executable family per map;
- when alternate lines exist inside a family, evaluate supplied lines but select exactly one canonical line/side;
- `PASS` is disabled for executable offered binary markets;
- old minimum-odds, edge and selective causal-thesis gates are diagnostic only, not forced-choice vetoes;
- price cannot alter benchmark, DIM classification, ML probability, KH margin distribution, Duration F or TK distribution;
- after price-blind projections are locked, choose the better model-vs-book side; if both sides are negative EV choose the less-negative side;
- tag every selected side with `MODEL_EDGE` and `FORCED_NEG_EV=YES/NO`;
- if quote/settlement data are insufficient use execution-data `HOLD` until clarified;
- supplied final draft + exact board is standing authorization for all four selected shadow Positions; no extra line confirmation required;
- `0.25u shadow / 0u actual` per family;
- no chasing, rescue, martingale, averaging down or stake escalation.

## Q2 checkpoint quarantine — ACTIVE prospectively

From the 40-position checkpoint audit:

### Moneyline
- full `PKM / SKM / TAM / OSG / DAU / SLI / FNF / CAS / ETS / AFP` DIM remains mandatory and persisted;
- still certify and record `D=+1/0/-1` under the two-independent-mechanism adversarial rule;
- **`D_DIAGNOSTIC_ONLY=YES`**;
- **`D_PROBABILITY_CONTRIBUTION=0`** inside this forced-choice overlay;
- forced-choice ML probability is therefore frozen team benchmark `P0` only;
- price is used only after `P0` and diagnostic DIM are locked.

### Kill Handicap
- full side-neutral signed final kill-margin bins must be locked before line/price;
- explicitly allocate numeric mass to both teams' `10+ kill` clean-cascade tails;
- persist raw cover probability;
- **`KH_MODEL_PROB_CAP=70%`** for execution-edge reporting and side comparison;
- `KH_CAPPED_PROB=min(raw_cover,70%)` is the probability used for `MODEL_EDGE`;
- no fitted new tail/variance coefficients are authorized.

### Duration
- v1.1 formula and `31.0m` anchor remain frozen;
- persist draft-only `V/Q/H/T/F` before price;
- if the selected forced-choice side is Over, persist `OVER_BRANCH_WARNING=YES` diagnostically;
- no coefficient or probability-slope change.

### Total Kills
- benchmark construction remains unchanged;
- full pre-price TK bins remain mandatory;
- every map must include explicit numeric `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION` mass, distinct from clean-cascade and two-sided-brawl branches;
- no coefficient or baseline change.

## Portfolio-coherence override — ACTIVE

Kill Handicap must be portfolio-consistent with selected ML when absolute handicap is below 5 kills:
- `±4.5` or smaller: selected KH team must match selected ML team;
- `±5.5` or wider: KH may be evaluated independently;
- this rule is prospective and does not rewrite historical Positions.

## Timing / information controls

- final draft/roles plus exact market board are the only prediction inputs;
- ignore displayed match clock for execution eligibility;
- do not use in-map kills, gold, objectives, structures, role resources or other live-state evidence in prediction;
- pre-series benchmark is frozen for the entire KT-DK series;
- same-series map results never update `K/P0` or `TK0`;
- same-series maps may inform only structurally required Fearless champion availability;
- sportsbook prices and prior playoff results are not benchmark inputs;
- no Position is created before a final map draft + exact board is supplied.

## Series identification

Current next LCK series:
- `KT Rolster (KT)` vs `Dplus KIA (DK)`;
- competition: `LCK 2026 Season Playoffs`;
- stage: `Lower Bracket Round 2`;
- date: `2026-09-04`;
- scheduled: `08:00 UTC / 15:00 UTC+7`;
- format: `Bo5 Fearless Draft`.

Fresh identification state on 2026-09-03 UTC+7:
- public LCK schedule lists Sep 4 lower-bracket Round 2 as `KT vs TBD`;
- DK defeated BFX `3-2` in the preceding lower-bracket Round 1, resolving that TBD slot to DK;
- no current-series map has started at lock construction.

## Expected roster context

KT Rolster:
- Perfect — TOP
- Cuzz — JUNGLE
- Bdd — MID
- Jiwoo — ADC
- Effort — SUPPORT

Dplus KIA:
- Siwoo — TOP
- Lucid — JUNGLE
- ShowMaker — MID
- Smash — ADC
- Career — SUPPORT

Saved/live-verified roster context is subordinate to user-supplied final map roles.

Roster-continuity benchmark adjustment:
- DK retains meaningful continuity with Rounds 1-2 -> normal `70/30 current/previous` blend;
- KT used Aiming as the primary Rounds 1-2 ADC and now uses Jiwoo -> one material starter change;
- per benchmark procedure, halve KT previous-window weight from 30% to 15% and transfer it to current -> **KT `85/15 current/previous`**.

## Frozen KT vs DK Gol.gg benchmark

Primary source: Games of Legends / gol.gg completed team tables.
- current competitive window: completed `LCK 2026 Rounds 3-4`;
- previous comparable window: completed `LCK 2026 Rounds 1-2`;
- full 10-team LCK peer set, population z-scores;
- prior playoff series/results and sportsbook prices are excluded from the benchmark metrics.

Current Rounds 3-4 core inputs:
- `DK`: 20 games, WinRate `55.0%`, GDM `+25`, GD@15 `-694`, Towers `6.6-5.5`, DRA% `54.4`, NASH% `61.1`;
- `KT`: 21 games, WinRate `38.1%`, GDM `-167`, GD@15 `-715`, Towers `4.5-7.3`, DRA% `41.7`, NASH% `41.7`.

Previous Rounds 1-2 core inputs:
- `DK`: 42 games, WinRate `57.1%`, GDM `+64`, GD@15 `+619`, Towers `6.3-5.1`, DRA% `48.8`, NASH% `49.1`;
- `KT`: 41 games, WinRate `63.4%`, GDM `+46`, GD@15 `+566`, Towers `6.5-5.0`, DRA% `52.6`, NASH% `53.8`.

League-relative split scores:
- `B_current(DK)=+0.174447`;
- `B_current(KT)=-1.458375`;
- `B_previous(DK)=+0.412956`;
- `B_previous(KT)=+0.503116`.

Roster-adjusted blended raw scores:
- `B_raw(DK)=+0.246000` using 70/30;
- `B_raw(KT)=-1.164151` using 85/15.

After re-standardizing the full 10-team blended peer set:
- `B(DK)=+0.355702`;
- `B(KT)=-1.465479`;
- `GAP(DK-KT)=+1.821180 SD`.

Frozen series prior:
- `DK K=+2 / P0=60%`;
- `KT K=-2 / P0=40%`.

Compact record:
`TEAM_BENCH[LEAGUE=LCK2026;CURRENT=R3-4;PREVIOUS=R1-2;G_DK=20;G_KT=21;B_CUR_DK=0.174447;B_CUR_KT=-1.458375;B_PREV_DK=0.412956;B_PREV_KT=0.503116;BLEND_DK=0.246000;BLEND_KT=-1.164151;B_DK=0.355702;B_KT=-1.465479;GAP_DK_KT=1.821180;K_DK=+2;K_KT=-2;ROSTER_ADJ_DK=NORMAL70_30;ROSTER_ADJ_KT=ONE_STARTER_85_15;PRICE_USED=N;PLAYOFF_RESULT_USED=N;SAME_SERIES_USED=N]`.

## Frozen Total Kills baseline

Current-window total-kill environments:
- `DK = 12.9 kills/game + 13.0 deaths/game = 25.9`;
- `KT = 12.0 kills/game + 13.0 deaths/game = 25.0`.

Both current samples exceed 15 games, so no previous-window TK blend is required.

`TK0=(25.9+25.0)/2=25.45 kills`.

## Forced-choice cohort state entering KT-DK

Checkpoint-complete historical cohort:
- `40 Positions / 10 per family`;
- overall `17W-23L`;
- shadow P/L `-2.0755u`;
- actual exposure `0u`.

By family:
- ML `1-9 / -2.0805u`;
- KH `4-6 / -0.6225u`;
- Duration `7-3 / +0.7770u`;
- TK `5-5 / -0.1495u`.

Next preferred structural checkpoint:
- `80 total Positions / 20 per family`;
- `10 additional fully recorded maps / 40 Positions` from this lock state;
- no structural coefficient fitting before that checkpoint unless a clear implementation/data-integrity bug is found.

## Speed-first map workflow

1. Receive final current-map draft/roles plus exact board.
2. Complete full DIM and all four price-blind family projections/distributions before price evidence.
3. ML: record diagnostic `D`, but use frozen `P0` only for forced-choice probability.
4. KH: construct full signed bins including both 10+ tails, apply 70% execution cap, then apply `<5 => ML-aligned` rule.
5. Duration: lock `V/Q/H/T/F`; tag selected Over with `OVER_BRANCH_WARNING=YES`.
6. TK: lock full bins including explicit numeric one-sided-fast-close / return-kill-suppression branch.
7. Select exactly one canonical ML/KH/Duration/TK line/side.
8. User-visible first line immediately: `[Map]: ML / KH / Duration / Total Kills — 1.00u shadow total.`
9. Persist shortest necessary DIM/probability/distribution notes plus `MODEL_EDGE` and `FORCED_NEG_EV`.
10. Airtable only at map end; settle map + four canonical Positions, then run the map micro-audit and update cohort state.

If authority/overlay mismatch occurs: `MODEL LOCK MISMATCH — HOLD`.
