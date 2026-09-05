# Current LoL Session Lock

**Lock ID:** `LOL-2026-09-05-V13-GEN-HLE-DRAFTONLY-FORCEDCHOICE-Q2-1306-UTC7`  
**Status:** `ACTIVE`  
**Scope:** `LCK 2026 Season Playoffs — Upper Bracket Final — Gen.G vs Hanwha Life Esports — Bo5 Fearless Draft`  
**Supersedes:** `LOL-2026-09-04-V13-KT-DK-DRAFTONLY-FORCEDCHOICE-Q2-1955-UTC7` (closed historical lock)  
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

Canonical `CURRENT_MODEL.md` remains unchanged. The controls below apply only to the forced-choice validation overlay.

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

### Moneyline
- full `PKM / SKM / TAM / OSG / DAU / SLI / FNF / CAS / ETS / AFP` DIM remains mandatory and persisted;
- certify and record `D=+1/0/-1` under the adversarial two-independent-mechanism rule;
- `D_DIAGNOSTIC_ONLY=YES`;
- `D_PROBABILITY_CONTRIBUTION=0` inside this forced-choice overlay;
- forced-choice ML probability is frozen team benchmark `P0` only;
- price is used only after `P0` and diagnostic DIM are locked.

### Kill Handicap
- full side-neutral signed final kill-margin bins must be locked before line/price;
- explicitly allocate numeric mass to both teams' `10+ kill` clean-cascade tails;
- persist raw cover probability;
- `KH_MODEL_PROB_CAP=70%` for execution-edge reporting and side comparison;
- `KH_CAPPED_PROB=min(raw_cover,70%)` is the probability used for `MODEL_EDGE`;
- no fitted new tail/variance coefficients are authorized.

### Duration
- v1.1 formula and `31.0m` anchor remain frozen;
- persist draft-only `V/Q/H/T/F` before price;
- if selected forced-choice side is Over, persist `OVER_BRANCH_WARNING=YES` diagnostically;
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
- pre-series benchmark is frozen for the entire GEN-HLE series;
- same-series map results never update `K/P0` or `TK0`;
- same-series maps may inform only structurally required Fearless champion availability;
- sportsbook prices and prior playoff results are not benchmark inputs;
- no Position is created before a final map draft + exact board is supplied;
- Airtable writes occur only at map end.

## Series identification

Current series:
- `Gen.G (GEN)` vs `Hanwha Life Esports (HLE)`;
- competition: `LCK 2026 Season Playoffs`;
- stage: `Upper Bracket Final`;
- date: `2026-09-05`;
- scheduled: `08:00 UTC / 15:00 UTC+7`;
- format: `Bo5 Fearless Draft`.

Fresh public identification on 2026-09-05 UTC+7:
- LoL Esports schedule lists GEN vs HLE on Sep 5 at 08:00 UTC as an LCK Playoffs Bo5;
- Gol.gg LCK 2026 Season Playoffs match list lists `Gen.G vs HLE` on 2026-09-05, ROUND4;
- no current-series map result is used in benchmark construction.

## Expected roster context

Gen.G:
- Kiin — TOP
- Canyon — JUNGLE
- Chovy — MID
- Ruler — ADC
- Duro — SUPPORT

Hanwha Life Esports:
- Zeus — TOP
- Kanavi — JUNGLE
- Zeka — MID
- Gumayusi — ADC
- Delight — SUPPORT

Saved Airtable roster context and current Gol.gg Rounds 3-4 lineups support these primary fives. HLE's Bluffing is a listed support sub, not the primary current starter. User-supplied final map roles/lineup override saved context if contradictory.

Roster-continuity benchmark adjustment:
- GEN retains the same primary five across Rounds 1-2 and Rounds 3-4 -> normal `70/30 current/previous` blend;
- HLE retains the same primary five across Rounds 1-2 and Rounds 3-4 -> normal `70/30 current/previous` blend;
- full peer-set re-standardization preserves the previously established KT one-starter adjustment (`85/15`) for peer-set consistency; all other peers use their applicable previously established normal blend.

## Frozen GEN vs HLE Gol.gg benchmark

Primary source: Games of Legends / gol.gg completed team tables.
- current competitive window: completed `LCK 2026 Rounds 3-4`;
- previous comparable window: completed `LCK 2026 Rounds 1-2`;
- full 10-team LCK peer set, population z-scores;
- prior playoff series/results and sportsbook prices are excluded from benchmark metrics.

Current Rounds 3-4 core inputs:
- `GEN`: 19 games, WinRate `63.2%`, GDM `+91`, GD@15 `+638`, Towers `6.5-5.3`, DRA% `55.6`, NASH% `48.0`;
- `HLE`: 21 games, WinRate `52.4%`, GDM `+56`, GD@15 `+596`, Towers `6.3-5.4`, DRA% `48.7`, NASH% `49.1`.

Previous Rounds 1-2 core inputs:
- `GEN`: 41 games, WinRate `73.2%`, GDM `+228`, GD@15 `+897`, Towers `7.6-3.8`, DRA% `64.2`, NASH% `72.6`;
- `HLE`: 43 games, WinRate `74.4%`, GDM `+188`, GD@15 `+883`, Towers `7.5-3.7`, DRA% `54.4`, NASH% `71.7`.

League-relative split scores:
- `B_current(GEN)=+1.043999`;
- `B_current(HLE)=+0.501517`;
- `B_previous(GEN)=+1.253139`;
- `B_previous(HLE)=+1.135456`.

Blended raw scores at normal 70/30:
- `B_raw(GEN)=+1.106741`;
- `B_raw(HLE)=+0.691699`.

After re-standardizing the full 10-team blended peer set:
- `B(GEN)=+1.467332`;
- `B(HLE)=+0.931313`;
- `GAP(GEN-HLE)=+0.536019 SD`.

Frozen series prior:
- `GEN K=+1 / P0=55%`;
- `HLE K=-1 / P0=45%`.

Compact record:
`TEAM_BENCH[LEAGUE=LCK2026;CURRENT=R3-4;PREVIOUS=R1-2;G_GEN=19;G_HLE=21;B_CUR_GEN=1.043999;B_CUR_HLE=0.501517;B_PREV_GEN=1.253139;B_PREV_HLE=1.135456;BLEND_GEN=1.106741;BLEND_HLE=0.691699;B_GEN=1.467332;B_HLE=0.931313;GAP_GEN_HLE=0.536019;K_GEN=+1;K_HLE=-1;ROSTER_ADJ_GEN=NORMAL70_30;ROSTER_ADJ_HLE=NORMAL70_30;PRICE_USED=N;PLAYOFF_RESULT_USED=N;SAME_SERIES_USED=N]`.

## Frozen Total Kills baseline

Current-window total-kill environments from the Gol.gg Rounds 3-4 peer table:
- `GEN = 12.5 kills/game + 11.1 deaths/game = 23.6`;
- `HLE = 15.1 kills/game + 15.2 deaths/game = 30.3`.

Both current samples exceed 15 games, so no previous-window TK blend is required.

`TK0=(23.6+30.3)/2=26.95 kills`.

## Forced-choice cohort state entering GEN-HLE

Corrected historical cohort after KT-DK G4 source-board correction:
- `48 Positions / 12 per family`;
- overall `24W-24L`;
- shadow P/L `-0.77275u`;
- actual exposure `0u`.

By family:
- ML `3-9 / -1.71425u`;
- KH `6-6 / -0.16750u`;
- Duration `9-3 / +1.23700u`;
- TK `6-6 / -0.12800u`.

KT-DK G4 carries no `DATA-INTEGRITY MISMATCH` tag after Renekton reassessment left all corrected canonical selections unchanged. The sportsbook board-transcription correction remains historical execution documentation only.

Next preferred structural checkpoint:
- `80 total Positions / 20 per family`;
- `8 additional fully recorded maps / 32 Positions` from this lock state;
- no structural coefficient fitting before that checkpoint unless a clear implementation bug is found.

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
