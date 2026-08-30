# Current Live Handoff — Dplus KIA vs KT Rolster — 2026-08-30

**State only — not analytical authority**

## Series

- Competition: `LCK 2026 Playoffs`
- Round: `Round 1`
- Match: `Dplus KIA vs KT Rolster`
- Format: `Bo5 Fearless Draft`
- Scheduled: `2026-08-30 15:00 UTC+7 / 17:00 KST`
- Series score: `not supplied / do not infer`
- Current map: `not supplied / do not infer`

## Active model

- Model: `LoL v1.3 — Hierarchy Moneyline + Duration Core`
- Active lock: `LOL-2026-08-30-V13-DK-KT-1612-UTC7`
- Frozen authority commit: `083a7a97c04e9fb4fd40b74c3dd931643539aaa0`
- Circuit breaker: `CLEAR`
- Active markets: `Moneyline + Duration Over/Under`
- Kill Handicap: `RETIRED_FROM_BETTING`
- Total Kills: `RETIRED_FROM_BETTING`
- Actual exposure: `0u`
- Shadow stake: `0.25u`
- Minimum odds: `1.60`
- ML required edge: `+5.0pp`
- Duration required edge: `+7.5pp`
- Accepted v1.3 samples at relock: `ML_SAMPLE_N=0; DURATION_SAMPLE_N=0`

## Series-frozen Moneyline strength prior

Assigned from pre-series non-price evidence only; sportsbook odds and same-series results are excluded.

- Dplus KIA: `K=+1 / P0=55%`
- KT Rolster: `K=-1 / P0=45%`

Basis available before the series:
- DK beat KT `2-1` in LCK Week 11 on 2026-08-09;
- DK beat KT `2-0` in LCK Week 12 on 2026-08-12;
- DK beat T1 `2-1` on 2026-08-14;
- KT reached this playoff round through Play-Ins, defeating Hanjin BRION `3-2` on 2026-08-26.

This is a meaningful but not maximum strength tier. Freeze it for the series absent genuine roster/availability change.

## v1.3 Moneyline hierarchy

`P0=50%+5*K pp`

`S=1.5*D_eff+1.5*R+1.5*X+1.25*O+1.0*T`

`P(A)=clamp(P0(A)+3*S pp,15%,85%)`

Hierarchy:
`LIGHT TEAM-STRENGTH PRIOR -> MEANINGFUL DRAFT CORRECTION -> LIVE STATE DOMINATES AS EVIDENCE ACCUMULATES`

## Duration

Unchanged v1.1 Duration Core:

`R0=max(5.0,31.0-t)`

`ER=max(2.0,R0-1.5*V+Q+H+0.75*T)`

`F=t+ER`

`P(OVER)=clamp(50%+7*(F-L) pp,15%,85%)`

Absent conversion opportunity is neutral.

## DK vs KT initialization

- Blue/Red side assignment: `not supplied`.
- Exact five / substitutions: `not yet resolved in this handoff`.
- Draft: `not supplied`.
- Fearless consumed pool: `none recorded yet`.
- Live scoreboard/market: `not supplied`.
- No betting verdict or Position has been issued under this DK-KT lock.

## Next workflow

1. Resolve current map number / series score if the series has already started.
2. Resolve Blue/Red side.
3. Use saved LCK rosters first; user exact lineup/card overrides generic roster context.
4. Read the completed draft separately from team strength and track Fearless consumption map by map.
5. No pregame/immediate-postdraft TAKE.
6. On synchronized live state + executable market:
   - ML: lock K/P0 + D/R/X/O/T price-blind, then read odds;
   - Duration: score V/Q/H/T, lock F, then read line/odds.
7. TAKE CANDIDATE only if family threshold clears.
8. Accepted Position only after exact live user confirmation before material state change.

## Bootstrap next continuation

Every new continuation must:

1. fetch default `models/lol/CURRENT_MODEL.md`;
2. immediately load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch mutable `models/lol/session/CURRENT_SESSION_LOCK.md`;
4. verify lock `LOL-2026-08-30-V13-DK-KT-1612-UTC7` and authority `083a7a97c04e9fb4fd40b74c3dd931643539aaa0`;
5. load the exact v1.3 authority stack in locked order;
6. use Airtable only as ledger/history authority;
7. load this or a newer DK-KT handoff last.
