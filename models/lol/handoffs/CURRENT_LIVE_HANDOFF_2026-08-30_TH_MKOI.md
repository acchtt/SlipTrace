# Current Live Handoff — Team Heretics vs Movistar KOI — 2026-08-30

**State only — not analytical authority**

## Series
- Competition: `LEC 2026 Summer`
- Stage: `Week 6 / Regular Season`
- Match: `Team Heretics vs Movistar KOI`
- Format: `Bo3 Fearless Draft`
- Scheduled: `2026-08-30 21:15 UTC+7 / 16:15 CEST`
- Series score: `not supplied / do not infer`
- Current map: `Game 2 completed — Movistar KOI won`
- Blue/Red: `not explicitly supplied; do not infer from scoreboard orientation`

## Active model
- Model: `LoL v1.3 — Hierarchy Moneyline + Duration Core`
- Active lock: `LOL-2026-08-30-V13-TH-MKOI-2150-UTC7`
- Frozen authority commit: `083a7a97c04e9fb4fd40b74c3dd931643539aaa0`
- Circuit breaker: `CLEAR`
- Active markets: `Moneyline + Duration Over/Under`
- Kill Handicap / Total Kills: `RETIRED_FROM_BETTING`
- Actual exposure: `0u`
- Shadow stake: `0.25u`
- Minimum odds: `1.60`
- ML edge threshold: `+5.0pp`
- Duration edge threshold: `+7.5pp`
- Accepted v1.3 samples after Game 2: `ML_SAMPLE_N=3; DURATION_SAMPLE_N=0`

## Series-frozen strength prior
Price-independent and frozen before same-series results:
- Team Heretics: `K=-1 / P0=45%`
- Movistar KOI: `K=+1 / P0=55%`

Basis:
- current LEC Summer team-level game results entering Aug 30 materially favored MKOI over TH (`40.0%` vs `23.5%` game win rate in current Games of Legends tournament data);
- TH recently lost `0-2` to GIANTX and `0-2` to Shifters, with a `2-0` over SK in between;
- MKOI recently beat NAVI `2-0` and lost `0-2` to SK;
- MKOI's established 2026 top-level baseline was stronger, including 3rd in LEC Spring;
- mixed recent form prevents a maximum strength tier.

Same-series results and prices must not change K/P0.

## Confirmed live lineups from Game 2 scoreboard
TH:
- Tracyn — top
- Daglas — jungle
- Serin — mid
- Hype — ADC
- Way — support

MKOI:
- Myrwn — top
- Elyoya — jungle
- Jojopyun — mid
- Supa — ADC
- Alvaro — support

## Game 2 draft
TH:
- Aatrox / Xin Zhao / Syndra / Ezreal / Karma

MKOI:
- Ambessa / Skarner / Viktor / Ashe / Seraphine

Game 2 draft prior used from TH perspective:
- `D=-1` — MKOI draft edge.
- Mechanism initially `INTACT`.

## Game 2 confirmed position and settlement
Decision window at `03:50`:
- kills `0-0`
- towers `0-0`
- dragons `0-0`
- barons `0-0`
- MKOI held about `+322g` overall

Price-blind ML state from TH perspective:
- `K=-1 / P0=45%`
- `D=-1`
- `MC=INTACT`
- `R=-1`
- `X=0`
- `O=0`
- `T=0`
- model `TH 36.0% / MKOI 64.0%`

Market:
- MKOI `1.289`
- TH `3.396` -> book implied `29.45%`
- TH edge `+6.55pp`

Verdict:
- `TAKE CANDIDATE — TH ML @3.396`
- User explicitly confirmed exact line before any reported material state change.
- Accepted shadow Position ID: `LEC-2026-08-30-TH-MKOI-G2-ML-TH-0350`
- Shadow stake `0.25u`; actual exposure `0u`
- Result: `LOSS`; shadow P/L `-0.25u`

Airtable map-end logging completed:
- Position record: `recxJWOaEYGhaf0N4`
- Map record: `recaTAM7cHvQAZOmC`
- Snapshot record: `receTc67nmlpfuhhW`

No audit-error classification assigned solely from the loss. Final duration/kills/structures were not supplied.

## Validation running context
Known v1.3 accepted ML positions through this Game 2:
1. KT ML @4.259 vs DK — WIN `+0.81475u`
2. DK ML @3.114 vs KT — LOSS `-0.25u`
3. TH ML @3.396 vs MKOI — LOSS `-0.25u`

Running known v1.3 ML shadow P/L: `+0.31475u`.

## Core formulas
Moneyline:
`S=1.5*D_eff+1.5*R+1.5*X+1.25*O+1.0*T`
`P(A)=clamp(P0(A)+3*S pp,15%,85%)`

Duration:
`R0=max(5.0,31.0-t)`
`ER=max(2.0,R0-1.5*V+Q+H+0.75*T)`
`F=t+ER`
`P(OVER)=clamp(50%+7*(F-L) pp,15%,85%)`

## User workflow preference
- `VERDICT FIRST` on live assessments.
- Keep visible verdict compact.
- No Airtable writes during a map; perform snapshot/position/map logging at map end.
- Exact user confirmation still required for any TAKE CANDIDATE before it becomes an accepted shadow Position.

## Next workflow
1. If series continues, receive current series score/map and Blue/Red.
2. Resolve Fearless consumed pool from Games 1-2; Game 1 draft/result still need user supply if not already available elsewhere.
3. Lock map-specific `D` price-blind after draft.
4. No immediate-postdraft TAKE.
5. On synchronized live state + executable market, score ML `R/X/O/T` and Duration `V/Q/H/T/F` before price evidence.
6. Verdict first, compact.
7. Candidate requires exact line confirmation; material state change expires it.
8. Defer Airtable writes to map end.

## Bootstrap next continuation
Fetch default `models/lol/CURRENT_MODEL.md`, load `LOL_SESSION_BOOTSTRAP.md`, fetch lock `LOL-2026-08-30-V13-TH-MKOI-2150-UTC7`, re-fetch `CURRENT_MODEL.md` at authority `083a7a97c04e9fb4fd40b74c3dd931643539aaa0`, load exact v1.3 authority stack, then this or a newer TH-MKOI handoff last.
