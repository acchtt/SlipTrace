# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-31-V13-NSC-DNSC-DRAFTONLY-FORCEDCHOICE`  
**Status:** `ACTIVE`  
**Scope:** `LCK CL 2026 Season — Playoffs Upper Round 1 — Nongshim Esports Academy vs DN SOOPers Challengers — Bo5 Fearless Draft`  
**Supersedes:** `LOL-2026-08-31-V13-NSC-DNSC-DRAFTONLY-1715-UTC7` prospectively  
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

## User-directed forced-choice override — prospective from this lock

The user explicitly instructed:

`From now on, take all available markets, no more pass. If you pass under then the over will be taken.`

Operational interpretation for shadow tracking:

- no live-state predictions;
- enabled families: `Moneyline + Kill Handicap + Duration + Total Kills`;
- when an offered board contains a binary market in an enabled family, choose **exactly one side** and record it as a `FORCED-CHOICE` shadow Position;
- `PASS` is disabled for offered binary markets in this mode;
- if the initially preferred side is rejected by the old selective gate, the opposite side is still evaluated and one side must ultimately be selected;
- minimum-odds and edge thresholds remain diagnostic metadata only and are **not execution vetoes** in forced-choice mode;
- selected-side causal-thesis gate remains diagnostic only and is **not an execution veto** in forced-choice mode;
- price still must not alter the benchmark, draft read, ML probability, kill-margin distribution, duration F, or total-kill distribution;
- after price-blind projections are locked, choose the side with the better model-vs-book expected value / fit among the two offered sides; if both are negative EV, choose the less-negative side;
- if odds are missing for one side or settlement semantics are unclear, HOLD that market until an executable two-sided quote/clear settlement is supplied — this is an execution-data HOLD, not a model PASS;
- the user's standing instruction counts as blanket line authorization for supplied boards: no extra `Confirm` message is required for each forced-choice shadow Position;
- shadow stake stays `0.25u` per selected market; actual exposure remains `0u`;
- no chasing, rescue, martingale, averaging down, or stake escalation.

## Validation separation

Forced-choice positions are a distinct experimental cohort:

- tag every such Position `FORCED-CHOICE` in evidence/thesis text;
- do **not** blend forced-choice results with threshold-qualified selective TAKE calibration when estimating whether the old +5pp / +7.5pp gates were calibrated;
- audit forced-choice results separately by market family and direction;
- micro-review every settled map;
- checkpoint audit after 10 forced-choice Positions total;
- architecture changes still require explicit user authorization, except procedural bugs which are fixed immediately.

## Timing / information controls

- ignore displayed match time for execution eligibility when the user supplies final draft + board;
- do not use in-map kills, gold, objectives, structures, role resources, or other live-state evidence in prediction;
- prediction inputs remain frozen to pre-series benchmark + final draft/mechanisms + supplied market board only.

## Frozen NS.C vs DNS.C benchmark

Primary source: Games of Legends / gol.gg, using completed LCK CL 2026 Rounds 3-4 as current window and Rounds 1-2 as previous comparable window. Sportsbook prices and same-series results excluded.

- `B_current(NS)=+0.317`
- `B_current(DNS)=-0.690`
- `B_previous(NS)=+0.733`
- `B_previous(DNS)=+0.495`
- normal `70/30` current/previous blend
- `B_raw(NS)=+0.442`
- `B_raw(DNS)=-0.334`
- `B(NS)=+0.550`
- `B(DNS)=-0.417`
- `GAP(NS-DNS)=+0.967 SD`
- `NS.C K=+1 / P0=55%`
- `DNS.C K=-1 / P0=45%`

Same-series results and sportsbook prices never change K/P0.

## Price-blind projections

### Moneyline
With no live variables: `R=X=O=T=0`.

`P(A)=clamp(P0(A)+4.5*D pp,15%,85%)`

Lock P before price. In forced-choice mode, compare both quoted sides after the lock and select one even if the old selective thesis/edge gate would have produced PASS.

### Kill Handicap
Construct the side-neutral final kill-margin distribution before line/price. Explicitly stress-test clean-cascade and return-kill branches. Then select one quoted handicap side.

### Duration
Use the v1.1 core at `t=0`; lock `F` before line/price. Then select Over or Under.

### Total Kills
Use price-independent `TK0` plus draft-adjusted kill distribution before line/price. Then select Over or Under. If TK0 cannot be reconstructed reliably, execution-data HOLD until a reliable baseline is available.

## Workflow

1. Final draft/roles.
2. Price-blind DIM + ML/KH/Duration/TK projections.
3. Exact offered board.
4. Ignore displayed match clock and all live-state statistics.
5. For every executable offered enabled market, choose exactly one side.
6. Record each as `FORCED-CHOICE`, 0.25u shadow / 0u actual, without additional confirmation.
7. Airtable writes remain deferred to map end.

If authority/overlay mismatch outside this explicit override: `MODEL LOCK MISMATCH — HOLD`.
