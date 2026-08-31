# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-31-V13-KTC-KRXC-DRAFTONLY`  
**Status:** `ACTIVE`  
**Scope:** `LCK CL 2026 Season — Playoffs Upper Round 1 — KT Rolster Challengers vs DRX/KRX Challengers — Bo5 Fearless Draft`  
**Supersedes:** `LOL-2026-08-31-V13-KTC-KRXC-BENCH-1205-UTC7` prospectively  
**Authority commit:** `3e11a3a2b94a710dbc2d9ef16d88c3ac4ea0335c`  
**Active analytical model:** `LoL v1.3 — benchmark-aware core + lock-scoped Draft-Only Execution Mode`  
**Execution mode:** `POSTDRAFT_ONLY / NO LIVE PREDICTIONS`  
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
7. `models/lol/procedures/LOL_DRAFT_ONLY_EXECUTION_MODE_2026-08-31.md` **last as the lock-scoped execution override**.

The draft-only overlay supersedes only conflicting timing/market-retirement clauses. All non-conflicting benchmark, anti-price-only, confirmation, position-blind, and anti-chasing controls remain active.

## Temporary user-directed market mode

User instruction on 2026-08-31:

- no live predictions at the moment;
- evaluate only after final draft + exact odds/line;
- enabled families: `Moneyline + Kill Handicap + Duration + Total Kills`;
- corrected ML minimum decimal odds: `1.50`;
- the earlier `0.5` entry was a transcription/misunderstanding and is superseded;
- KH / Duration / Total Kills retain minimum decimal odds `1.60` unless user changes them;
- exact line confirmation is still required before an accepted shadow Position;
- once a map starts, do not update predictions from live kills/gold/objectives/structures. In-map evidence is settlement/context only.

## Price-independence

For all enabled markets, construct the benchmark + draft mechanism + family projection/distribution before odds are analytical evidence.

`PRICE CANNOT CREATE THE BET` remains hard.

## Frozen KT.C vs KRX.C benchmark

Pre-series-only Gol.gg LCK CL data; sportsbook prices and same-series results excluded.

Current window: `LCK CL 2026 Rounds 3-4`  
Previous comparable window: `LCK CL 2026 Rounds 1-2`

Participant scores:
- `B_current(KRX)=+1.666`
- `B_current(KT)=-0.206`
- `B_previous(KRX)=-0.127`
- `B_previous(KT)=+0.765`

Roster adjustment:
- KT expected five continuous -> `70/30` current/previous;
- KRX one material bot change `Jiwoo -> Vincenzo` -> `85/15`.

Final league-relative benchmark:
- `B(KRX)=+1.623`
- `B(KT)=+0.069`
- `GAP(KRX-KT)=+1.554 SD`

Frozen series prior:
- `KRX/DRX.C K=+2 / P0=60%`
- `KT.C K=-2 / P0=40%`

Same-series results never change this K/P0.

## Current Game 1 draft

KT.C:
- Sero — `Rumble`
- Sylvie — `Wukong`
- Hwichan — `Ahri`
- FenRir — `Xayah`
- Pollu — `Milio`

KRX.C:
- Frog — `Olaf`
- Winner — `Qiyana`
- AKaJe — `Viktor`
- Vincenzo — `Lucian`
- Minous — `Nautilus`

Current price-blind draft verdict from the completed interaction read: `SLIGHT KT.C`.

## Draft-only Moneyline

With no live variables:

`R=X=O=T=0`

`P(A)=clamp(P0(A)+4.5*D pp,15%,85%)`

Selected-side positive draft thesis is still required. Team strength or attractive price alone cannot create an ML TAKE.

ML required edge remains `+5.0pp`.
ML minimum decimal odds: `1.50`.

## Kill Handicap

Postdraft KH is enabled under the lock-scoped distribution framework in `LOL_DRAFT_ONLY_EXECUTION_MODE_2026-08-31.md`.

- side-neutral final kill-margin distribution first;
- sign cannot be selected first;
- favorite -5.5 or wider retains CoverShare conversion gate;
- dog +H retains resilience / clean-cascade stress;
- minimum odds `1.60`;
- initial reactivation edge threshold `+7.5pp`.

## Duration

Postdraft Duration is enabled using the v1.1 core at `t=0`, with draft-only `V/Q/H/T`.

- lock `F` before line/price;
- minimum odds `1.60`;
- edge threshold `+7.5pp`.

## Total Kills

Postdraft Total Kills is enabled.

- construct price-independent `TK0` from reliable pre-series same-competition team kill+death environments;
- build draft-adjusted total-kill distribution before seeing line/price;
- if `TK0` cannot be reliably reconstructed, HOLD rather than anchor to the sportsbook line;
- minimum odds `1.60`;
- initial reactivation edge threshold `+7.5pp`.

## Workflow

1. Final draft/roles.
2. Draft Interaction Matrix and price-blind market projections/distributions.
3. Exact offered lines/odds.
4. Compact verdicts for ML / KH / Duration / Total Kills.
5. Exact user confirmation for any TAKE CANDIDATE before map start.
6. No live prediction updates after map start.
7. Airtable writes remain deferred to map end.

If authority/overlay mismatch: `MODEL LOCK MISMATCH — HOLD`.
