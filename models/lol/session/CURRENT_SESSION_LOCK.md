# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-31-V13-KTC-KRXC-DRAFTONLY`  
**Status:** `ACTIVE`  
**Scope:** `LCK CL 2026 Season — Playoffs Upper Round 1 — KT Rolster Challengers vs DRX/KRX Challengers — Bo5 Fearless Draft`  
**Supersedes:** `LOL-2026-08-31-V13-KTC-KRXC-BENCH-1205-UTC7` prospectively  
**Authority commit:** `3e11a3a2b94a710dbc2d9ef16d88c3ac4ea0335c`  
**Active analytical model:** `LoL v1.3 — benchmark-aware core + lock-scoped Draft-Only Execution Mode`  
**Execution mode:** `POSTDRAFT-ONLY INPUTS / IGNORE DISPLAYED MATCH CLOCK`  
**Circuit breaker / actual exposure:** `CLEAR / 0u actual`  
**Default shadow stake:** `0.25u`

## Required authority stack

Load from authority commit `3e11a3a2b94a710dbc2d9ef16d88c3ac4ea0335c`:

1. `models/lol/CURRENT_MODEL.md`;
2. `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. `models/lol/procedures/LOL_V1.3_TEAM_BENCHMARK_GOLGG_2026-08-30.md`;
4. `models/lol/rules/MODEL_RULES_LOL_V1.3_MONEYLINE_HIERARCHY_CORE.md`;
5. `models/lol/rules/MODEL_RULES_LOL_V1.1_DURATION_CORE.md`;
6. `models/lol/procedures/LOL_DRAFT_INTERACTION_MATRIX_2026-08-20.md`;
7. `models/lol/procedures/LOL_DRAFT_ONLY_EXECUTION_MODE_2026-08-31.md` last as the base lock-scoped execution overlay.

This mutable session lock carries the user's later timing override below. All non-conflicting benchmark, anti-price-only, confirmation, position-blind, and anti-chasing controls remain active.

## Temporary user-directed market mode

User instructions on 2026-08-31:

- no live-state predictions at the moment;
- enabled families: `Moneyline + Kill Handicap + Duration + Total Kills`;
- ML minimum decimal odds: `1.50`;
- KH / Duration / Total Kills minimum decimal odds: `1.60`;
- ML edge threshold `+5.0pp`; KH / Duration / Total Kills initial edge threshold `+7.5pp`;
- exact user confirmation is still required before an accepted shadow Position;
- **ignore displayed match time for execution eligibility** when the user supplies a final draft + board;
- a board shown after the map clock has begun may still be evaluated and recorded as the intended postdraft decision snapshot;
- **do not use any in-map kills, gold, objectives, structures, role gold, or other live-state evidence in the prediction**;
- prediction inputs remain frozen to pre-series benchmark + final draft/mechanisms + the supplied market board only.

Thus, `match clock > 0` is no longer a veto in this session. This overrides only the overlay's `before map start` / `no new position after start` timing clauses. It does **not** re-enable live prediction updates.

## Price-independence

For all enabled markets, construct the benchmark + draft mechanism + family projection/distribution before odds are analytical evidence.

`PRICE CANNOT CREATE THE BET` remains hard.

## Frozen KT.C vs KRX.C benchmark

- `B(KRX)=+1.623`
- `B(KT)=+0.069`
- `GAP(KRX-KT)=+1.554 SD`
- `KRX/DRX.C K=+2 / P0=60%`
- `KT.C K=-2 / P0=40%`

Same-series results never change K/P0.

## Draft-only Moneyline

With no live variables: `R=X=O=T=0`.

`P(A)=clamp(P0(A)+4.5*D pp,15%,85%)`

Selected-side positive draft thesis remains required. Team strength or attractive price alone cannot create an ML TAKE.

## Kill Handicap

Postdraft KH uses the locked side-neutral final kill-margin distribution before line/price. Favorite -5.5 or wider retains CoverShare protection; underdog +H requires real resilience/return-kill mechanisms and clean-cascade stress. Better price cannot repair a failed thesis.

## Duration

Postdraft Duration uses the v1.1 core at `t=0`; lock `F` before line/price.

## Total Kills

Postdraft Total Kills uses price-independent `TK0` plus draft-adjusted kill distribution before line/price. HOLD if TK0 cannot be reconstructed reliably.

## Workflow

1. Final draft/roles.
2. Draft Interaction Matrix and price-blind ML/KH/Duration/TK projections.
3. Exact offered board.
4. Ignore displayed match clock; ignore all live-state statistics.
5. Compact verdicts for ML / KH / Duration / Total Kills.
6. Exact user confirmation before accepted shadow Position.
7. Airtable writes remain deferred to map end.

If authority/overlay mismatch outside this explicit timing override: `MODEL LOCK MISMATCH — HOLD`.
