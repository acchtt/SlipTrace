# Current LoL Session Lock

**Lock ID:** `LOL-2026-09-01-V13-GEN-KT-DRAFTONLY-FORCEDCHOICE-1335-UTC7`  
**Status:** `ACTIVE`  
**Scope:** `LCK 2026 Season Playoffs — ROUND2 / Upper Bracket Semifinal — Gen.G vs KT Rolster — Bo5 Fearless Draft`  
**Supersedes:** `LOL-2026-08-31-V13-NSC-DNSC-DRAFTONLY-FORCEDCHOICE` prospectively  
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
- when an offered board contains a binary market in an enabled family, choose **exactly one side** and record it as a `FORCED-CHOICE` shadow Position;
- `PASS` is disabled for offered binary markets in this mode;
- old minimum-odds, edge, and selected-side thesis gates remain diagnostic metadata only, not execution vetoes;
- price still must not alter the benchmark, draft read, ML probability, kill-margin distribution, duration F, or total-kill distribution;
- after price-blind projections are locked, choose the side with the better model-vs-book expected value / fit; if both are negative EV, choose the less-negative side;
- if odds are missing for one side or settlement semantics are unclear, HOLD that market until an executable two-sided quote/clear settlement is supplied;
- supplied final draft + board counts as standing authorization for all forced-choice shadow Positions; no extra per-line confirmation required;
- shadow stake `0.25u` per selected market; actual exposure `0u`;
- no chasing, rescue, martingale, averaging down, or stake escalation.

Forced-choice results remain a distinct experimental cohort from threshold-qualified selective calibration. Micro-review each settled map; checkpoint audit after 10 forced-choice Positions total.

## Timing / information controls

- ignore displayed match time for execution eligibility when final draft + board are supplied;
- do not use in-map kills, gold, objectives, structures, role resources, or other live-state evidence in prediction;
- prediction inputs remain frozen to pre-series benchmark + final draft/mechanisms + supplied market board only.

## Series identification

Current series identified from official/public schedules and Gol.gg as:
- `Gen.G` vs `KT Rolster`;
- competition: `LCK 2026 Season Playoffs`;
- stage: `ROUND2 / Upper Bracket Semifinal`;
- date: `2026-09-01`;
- scheduled: `08:00 UTC / 15:00 UTC+7`;
- format: `Bo5 Fearless Draft`.

Series score/current map at lock: `0-0 / pre-series`.

## Frozen Gen.G vs KT benchmark

Primary source: Games of Legends / gol.gg. Current window is completed `LCK 2026 Rounds 3-4`; previous comparable window is `LCK 2026 Rounds 1-2`. Sportsbook prices and today's series are excluded.

Current Rounds 3-4 core inputs:
- `Gen.G`: 19 games, WinRate `63.2%`, GDM `+91`, GD@15 `+638`, Towers `6.5-5.3`, DRA% `55.6`, NASH% `48.0`;
- `KT Rolster`: 21 games, WinRate `38.1%`, GDM `-167`, GD@15 `-715`, Towers `4.5-7.3`, DRA% `41.7`, NASH% `41.7`.

Previous Rounds 1-2 core inputs:
- `Gen.G`: 41 games, WinRate `73.2%`, GDM `+228`, GD@15 `+897`, Towers `7.6-3.8`, DRA% `64.2`, NASH% `72.6`;
- `KT Rolster`: 41 games, WinRate `63.4%`, GDM `+46`, GD@15 `+566`, Towers `6.5-5.0`, DRA% `52.6`, NASH% `53.8`.

League-relative split scores under the frozen benchmark formula:
- `B_current(GEN)=+1.044`;
- `B_current(KT)=-1.458`;
- `B_previous(GEN)=+1.253`;
- `B_previous(KT)=+0.503`.

Roster continuity: no decision-critical starter change across the two benchmark windows for the expected playoff fives, so use normal `70/30 current/previous` blend.

Blended raw scores:
- `B_raw(GEN)=+1.107`;
- `B_raw(KT)=-0.870`.

After re-standardizing the full 10-team LCK peer set:
- `B(GEN)=+1.505`;
- `B(KT)=-1.183`;
- `GAP(GEN-KT)=+2.688 SD`.

Frozen series prior:
- `Gen.G K=+2 / P0=60%`;
- `KT Rolster K=-2 / P0=40%`.

KT's 3-0 win over Dplus KIA in Playoffs Round 1 is pre-series context but does not replace or back-fit the frozen league-relative benchmark construction. Same-series results and sportsbook prices never change K/P0.

## Expected roster context

Gen.G:
- Kiin — TOP
- Canyon — JUNGLE
- Chovy — MID
- Ruler — ADC
- Duro — SUPPORT

KT Rolster:
- PerfecT — TOP
- Cuzz — JUNGLE
- Bdd — MID
- Jiwoo — ADC
- Effort — SUPPORT

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
