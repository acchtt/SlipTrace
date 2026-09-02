# Current LoL Session Lock

**Lock ID:** `LOL-2026-09-02-V13-HLE-T1-DRAFTONLY-FORCEDCHOICE-1459-UTC7`  
**Status:** `ACTIVE`  
**Scope:** `LCK 2026 Season Playoffs — Upper Bracket Round 2 — Hanwha Life Esports vs T1 — Bo5 Fearless Draft`  
**Supersedes:** `LOL-2026-09-01-V13-GEN-KT-DRAFTONLY-FORCEDCHOICE-1335-UTC7` prospectively  
**Authority commit:** `3e11a3a2b94a710dbc2d9ef16d88c3ac4ea0335c`  
**Active analytical model:** `LoL v1.3 — benchmark-aware core + lock-scoped Draft-Only Forced-Choice Execution Mode`  
**Execution mode:** `POSTDRAFT-ONLY INPUTS / IGNORE DISPLAYED MATCH CLOCK / FORCE ONE SIDE PER OFFERED MARKET`  
**Circuit breaker / actual exposure:** `CLEAR / 0u actual`  
**Default shadow stake:** `0.25u per market`

## Required authority stack

Load from authority commit `3e11a3a2b94a710dbc2d9ef16d88c3ac4ea0335c`:

1. `models/lol/CURRENT_MODEL.md`;
2. `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. `models/lol/procedures/LOL_V1.3_TEAM_BENCHMARK_GOLGG_2026-08-30.md`;
4. `models/lol/rules/MODEL_RULES_LOL_V1.3_MONEYLINE_HIERARCHY_CORE.md`;
5. `models/lol/rules/MODEL_RULES_LOL_V1.1_DURATION_CORE.md`;
6. `models/lol/procedures/LOL_DRAFT_INTERACTION_MATRIX_2026-08-20.md`;
7. `models/lol/procedures/LOL_DRAFT_ONLY_EXECUTION_MODE_2026-08-31.md` as the base draft-only overlay;
8. this mutable lock's forced-choice override last.

## User-directed forced-choice override — ACTIVE prospectively

Standing user instruction remains:

`From now on, take all available markets, no more pass. If you pass under then the over will be taken.`

Operational interpretation for shadow tracking:
- no live-state predictions;
- enabled families: `Moneyline + Kill Handicap + Duration + Total Kills`;
- for every executable binary offered market in an enabled family, choose exactly one side and record it as a `FORCED-CHOICE` shadow Position;
- `PASS` is disabled for offered binary markets;
- old minimum-odds, edge, and selected-side thesis gates are diagnostic only, not execution vetoes;
- price cannot alter benchmark, draft read, ML probability, kill-margin distribution, duration F, or total-kill distribution;
- after price-blind projections are locked, choose the better model-vs-book side; if both sides are negative EV, choose the less-negative side;
- if quote/settlement data are insufficient, use execution-data HOLD until clarified;
- supplied final draft + board is standing authorization for all selected forced-choice shadow Positions; no extra per-line confirmation required;
- shadow stake `0.25u` per market; actual exposure `0u`;
- no chasing, rescue, martingale, averaging down, or stake escalation.

Forced-choice results remain a separate experimental cohort from threshold-qualified selective calibration. Micro-review each settled map; checkpoint audit after 10 forced-choice Positions total.

## Timing / information controls

- ignore displayed match time for execution eligibility when final draft + board are supplied;
- do not use in-map kills, gold, objectives, structures, role resources, or other live-state evidence in prediction;
- prediction inputs are frozen to pre-series benchmark + final draft/mechanisms + supplied market board only.

## Series identification

Current series:
- `Hanwha Life Esports (HLE)` vs `T1`;
- competition: `LCK 2026 Season Playoffs`;
- stage: `Upper Bracket Round 2`;
- date: `2026-09-02`;
- scheduled: `08:00 UTC / 15:00 UTC+7`;
- format: `Bo5 Fearless Draft`.

Series score/current map at lock: `0-0 / pre-series`.

## Frozen HLE vs T1 benchmark

Primary source: Games of Legends / gol.gg. Current window is completed `LCK 2026 Rounds 3-4`; previous comparable window is `LCK 2026 Rounds 1-2`. Sportsbook prices and today's series are excluded.

Current Rounds 3-4 core inputs:
- `HLE`: 21 games, WinRate `52.4%`, GDM `+56`, GD@15 `+596`, Towers `6.3-5.4`, DRA% `48.7`, NASH% `49.1`;
- `T1`: 19 games, WinRate `42.1%`, GDM `+5`, GD@15 `+222`, Towers `5.7-6.1`, DRA% `50.3`, NASH% `50.9`.

Previous Rounds 1-2 core inputs:
- `HLE`: 43 games, WinRate `74.4%`, GDM `+188`, GD@15 `+883`, Towers `7.5-3.7`, DRA% `54.4`, NASH% `71.7`;
- `T1`: 40 games, WinRate `75.0%`, GDM `+139`, GD@15 `+674`, Towers `6.9-4.4`, DRA% `53.9`, NASH% `54.2`.

League-relative split scores under the frozen benchmark formula:
- `B_current(HLE)=+0.502`;
- `B_current(T1)=-0.178`;
- `B_previous(HLE)=+1.135`;
- `B_previous(T1)=+0.902`.

Roster continuity: expected playoff fives are continuous across these two benchmark windows, so use normal `70/30 current/previous` blend.

Blended raw scores:
- `B_raw(HLE)=+0.692`;
- `B_raw(T1)=+0.146`.

After re-standardizing the full 10-team LCK peer set:
- `B(HLE)=+0.941`;
- `B(T1)=+0.199`;
- `GAP(HLE-T1)=+0.742 SD`.

Frozen series prior:
- `HLE K=+1 / P0=55%`;
- `T1 K=-1 / P0=45%`.

Recent HLE-T1 head-to-head results are context only and do not independently override the league-relative benchmark. Same-series results and sportsbook prices never change K/P0.

## Expected roster context

HLE:
- Zeus — TOP
- Kanavi — JUNGLE
- Zeka — MID
- Gumayusi — ADC
- Delight — SUPPORT

T1:
- Doran — TOP
- Oner — JUNGLE
- Faker — MID
- Peyz — ADC
- Keria — SUPPORT

User-supplied draft/scoreboard overrides public roster context if different.

## Price-blind projections

### Moneyline
With no live variables in draft-only mode:
`P(A)=clamp(P0(A)+4.5*D pp,15%,85%)`.
Lock P before price, then choose one quoted side in forced-choice mode.

### Kill Handicap
Construct the side-neutral final kill-margin distribution before line/price, explicitly stress-testing clean-cascade and return-kill branches, then choose one quoted handicap side.

### Duration
Use the v1.1 core at `t=0`; lock `F` before line/price, then choose Over or Under.

### Total Kills
Use price-independent `TK0` plus draft-adjusted kill distribution before line/price, then choose Over or Under. HOLD only if baseline/settlement data are insufficient.

## Workflow

1. Receive final current-map draft/roles plus exact board.
2. Ignore displayed match clock and all live-state statistics.
3. Lock price-blind DIM + ML probability + KH margin distribution + duration F + TK distribution.
4. Compare both sides of each offered enabled market.
5. Choose exactly one side for each executable offered market — no PASS.
6. Record each as `FORCED-CHOICE`, 0.25u shadow / 0u actual, without additional confirmation.
7. Airtable writes remain deferred to map end.

If authority/overlay mismatch outside this explicit override: `MODEL LOCK MISMATCH — HOLD`.
