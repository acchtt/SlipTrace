# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-31-V13-NSC-DNSC-DRAFTONLY-1715-UTC7`  
**Status:** `ACTIVE`  
**Scope:** `LCK CL 2026 Season — Playoffs Upper Round 1 — Nongshim Esports Academy vs DN SOOPers Challengers — Bo5 Fearless Draft`  
**Supersedes:** `LOL-2026-08-31-V13-KTC-KRXC-DRAFTONLY` prospectively  
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

The mutable session timing override remains active. All non-conflicting benchmark, anti-price-only, confirmation, position-blind, and anti-chasing controls remain active.

## Temporary user-directed market mode

User instructions carried prospectively into this series:

- no live-state predictions;
- enabled families: `Moneyline + Kill Handicap + Duration + Total Kills`;
- ML minimum decimal odds: `1.50`;
- KH / Duration / Total Kills minimum decimal odds: `1.60`;
- ML edge threshold `+5.0pp`; KH / Duration / Total Kills initial edge threshold `+7.5pp`;
- exact user confirmation required before an accepted shadow Position;
- ignore displayed match time for execution eligibility when the user supplies final draft + board;
- do not use in-map kills, gold, objectives, structures, role resources, or other live-state evidence in prediction;
- prediction inputs remain frozen to pre-series benchmark + final draft/mechanisms + supplied market board only.

## Series identification

Current LCK CL playoff series identified from public schedule as:
- `Nongshim Esports Academy / Nongshim Challengers (NS.C)` vs `DN SOOPers Challengers (DNS.C)`;
- scheduled `2026-08-31 17:30 KST`, equivalent to `15:30 UTC+7`;
- format `Bo5 Fearless Draft`.

Series score/current map at lock: `not supplied / do not infer`.

## Frozen NS.C vs DNS.C benchmark

Primary source: Games of Legends / gol.gg, using completed LCK CL 2026 Rounds 3-4 as current window and Rounds 1-2 as previous comparable window. Sportsbook prices and same-series results excluded.

Core split inputs relevant to the two teams:

Current — Rounds 3-4:
- `NS.C`: 21 games, WinRate `47.6%`, GDM `+37`, GD@15 `+1076`, Towers `5.6-5.9`, DRA% `59.1`, NASH% `50.0`;
- `DNS.C`: 21 games, WinRate `38.1%`, GDM `-103`, GD@15 `-152`, Towers `5.3-7.2`, DRA% `50.6`, NASH% `41.3`.

Previous — Rounds 1-2:
- `NS.C`: 45 games, WinRate `55.6%`, GDM `+66`, GD@15 `+967`, Towers `6.4-5.4`, DRA% `56.5`, NASH% `57.0`;
- `DNS.C`: 45 games, WinRate `57.8%`, GDM `+63`, GD@15 `-75`, Towers `6.7-5.2`, DRA% `60.7`, NASH% `59.5`.

League-relative split scores from the frozen benchmark formula:
- `B_current(NS)=+0.317`;
- `B_current(DNS)=-0.690`;
- `B_previous(NS)=+0.733`;
- `B_previous(DNS)=+0.495`.

Roster continuity:
- NS expected five `Janus / MihawK / SeTab / Lucy / Pleata` matches the established prior-window core;
- DNS expected five `Lancer / DDoiV / Flip / Enosh / Quantum` matches the established prior-window core, despite earlier support rotation during Rounds 1-2;
- treat both as no decision-critical roster change for blend purposes.

With `G>=15`, both use normal `70/30 current/previous` blend:
- `B_raw(NS)=+0.442`;
- `B_raw(DNS)=-0.334`.

After re-standardizing the full LCK CL peer set:
- `B(NS)=+0.550`;
- `B(DNS)=-0.417`;
- `GAP(NS-DNS)=+0.967 SD`.

Frozen series prior:
- `NS.C K=+1 / P0=55%`;
- `DNS.C K=-1 / P0=45%`.

Same-series results and sportsbook prices never change this K/P0.

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

If authority/overlay mismatch outside the explicit timing override: `MODEL LOCK MISMATCH — HOLD`.
