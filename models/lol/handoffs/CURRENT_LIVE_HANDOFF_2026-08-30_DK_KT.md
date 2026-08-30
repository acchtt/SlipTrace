# Current Live Handoff — Dplus KIA vs KT Rolster — 2026-08-30

**State only — not analytical authority**

## Series

- Competition: `LCK 2026 Playoffs`
- Round: `Round 1`
- Match: `Dplus KIA vs KT Rolster`
- Format: `Bo5 Fearless Draft`
- Scheduled: `2026-08-30 15:00 UTC+7 / 17:00 KST`
- Current series score: `KT Rolster 2-0 Dplus KIA`
- Current map: `Game 3 — prep / not yet supplied`

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
- Current accepted v1.3 samples: `ML_SAMPLE_N=1; DURATION_SAMPLE_N=0`

## Series-frozen Moneyline strength prior

Assigned from pre-series non-price evidence only; sportsbook odds and same-series results are excluded.

- Dplus KIA: `K=+1 / P0=55%`
- KT Rolster: `K=-1 / P0=45%`

Basis available before the series:
- DK beat KT `2-1` in LCK Week 11 on 2026-08-09;
- DK beat KT `2-0` in LCK Week 12 on 2026-08-12;
- DK beat T1 `2-1` on 2026-08-14;
- KT reached this playoff round through Play-Ins, defeating Hanjin BRION `3-2` on 2026-08-26.

This is a meaningful but not maximum strength tier. Freeze it for the series absent genuine roster/availability change. Games 1-2 results do not modify K/P0.

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

## Game 1 — completed before DK-KT relock

Final screenshot supplied after relock confirms:
- Winner: `KT Rolster`
- Duration: `38:44`
- Kills: `KT 15-11 DK`
- Towers: `KT 10-4 DK`
- Dragons: `KT 5-1 DK`
- Barons: `KT 1-0 DK`
- Inhibitors: `KT 2-0 DK`

Game 1 draft / consumed champions:
- KT: `Trundle / Jarvan IV / Syndra / Ezreal / Nautilus`
- DK: `Olaf / Xin Zhao / Orianna / Caitlyn / Bard`

This map completed before the DK-KT-specific lock was created at 16:12 UTC+7, so it is historical context only and is not a certified DK-KT Position/sample under the new lock.

## Game 2 — completed

Exact draft:

### KT Rolster
- PerfecT — `Rumble` top
- Cuzz — `Skarner` jungle
- Bdd — `Ahri` mid
- Jiwoo — `Kalista` bot
- Effort — `Renata Glasc` support

### Dplus KIA
- Siwoo — `Jayce` top
- Lucid — `Vi` jungle
- ShowMaker — `Annie` mid
- Smash — `Taliyah` bot
- Career — `Alistar` support

Blue/Red side assignment was not explicitly supplied; do not infer from display placement alone.

### Game 2 draft prior

Under v1.3, from DK perspective:
- `D=-1` — KT slight draft edge.
- KT had the cleaner front-to-back / objective shell through `Skarner + Rumble + Kalista + Renata`, with Ahri pick access.
- DK had more execution-dependent pick/poke chains through `Jayce + Vi + Annie + Taliyah + Alistar`.

With DK `P0=55%`, the immediate pre-live draft-adjusted reference was `DK 50.5% / KT 49.5%`.

### Game 2 clock correction

User instructed for Game 2: subtract `1:10` from the displayed game clock for model time.

Examples:
- displayed `9:45` -> effective `8:35`;
- displayed `14:46` -> effective `13:36`;
- final displayed `43:11` -> effective `42:01`.

This correction was specific to Game 2 unless the user extends it.

### Confirmed Game 2 Position

Decision window at displayed `14:46` / effective `13:36`:
- kills: `DK 2-0 KT`;
- gold: `DK +2.8k`;
- towers: `0-0`;
- dragons: `1-1`;
- barons: `0-0`.

Price-blind v1.3 ML state from DK perspective:
- `K=+1 / P0=55%`;
- `D=-1`;
- `MC=INTACT`;
- `R=+2`;
- `X=+1`;
- `O=0`;
- `T=+1`;
- `S=4.0`;
- model `P(DK)=67.0% / P(KT)=33.0%`.

Executable market:
- DK `1.197`;
- KT `4.259`.

KT @4.259 raw implied = `23.48%`; model KT = `33.0%`; edge = `+9.52pp`.

User immediately confirmed exact `KT Rolster ML @4.259` before any reported material state change.

Accepted shadow Position:
- Position ID: `LCK-2026-08-30-DK-KT-G2-ML-KT-1356`;
- selection: `KT Rolster ML`;
- odds: `4.259`;
- entry clock: `13:36 effective (14:46 displayed; -1:10 offset)`;
- shadow stake: `0.25u`;
- actual exposure: `0u`;
- result: `WIN`;
- shadow P/L: `+0.81475u`;
- Airtable record: `recjcpAqK1BGgDCT7`.

Compact entry record:
`ML_CORE[K(DK)=+1;P0(DK)=55%;D=-1;MC=INTACT;R=+2;X=+1;O=0;T=+1;S=4.0;P(DK)=67.0%;P(KT)=33.0%;BOOK(KT@4.259)=23.48%;EDGE(KT)=+9.52pp;SYNC=P;EXEC=P;ODDS=P;POSBLIND=P;EXPOSURE=0u]`

Duration at that window remained PASS: effective `13:36`, `V=0,Q=0,H=+2,T=0`, central `F=33.0m`; line 32 did not clear the +7.5pp threshold.

### Game 2 final

User final screenshot confirms:
- Winner: `KT Rolster`
- Displayed duration: `43:11`
- Effective duration under the user-specified Game 2 clock correction: `42:01`
- Kills: `KT 15-13 DK`
- Towers: `KT 6-9 DK`
- Dragons: `3-3`
- Barons: `KT 1-2 DK`
- Inhibitors: `1-1`

The confirmed KT ML Position won despite DK finishing ahead in structures and barons. No audit error classification is assigned at settlement.

## Fearless consumed entering Game 3

KT consumed:
- Game 1: `Trundle, Jarvan IV, Syndra, Ezreal, Nautilus`
- Game 2: `Rumble, Skarner, Ahri, Kalista, Renata Glasc`

DK consumed:
- Game 1: `Olaf, Xin Zhao, Orianna, Caitlyn, Bard`
- Game 2: `Jayce, Vi, Annie, Taliyah, Alistar`

All twenty champions above are consumed entering Game 3 subject to tournament Fearless rules.

## Next workflow

1. Current series is `KT 2-0 DK`; prepare Game 3 without changing the frozen strength prior.
2. Resolve Game 3 Blue/Red side when supplied.
3. Read completed Game 3 draft separately from team strength and Fearless history.
4. No pregame/immediate-postdraft TAKE.
5. On synchronized live state + executable market:
   - ML: lock K/P0 + D/R/X/O/T price-blind, then read odds;
   - Duration: score V/Q/H/T, lock F, then read line/odds.
6. TAKE CANDIDATE only if family threshold clears; accepted Position only after exact live confirmation before material state change.
7. No rescue, chase, martingale, averaging down or stake escalation.

## Bootstrap next continuation

Every new continuation must:

1. fetch default `models/lol/CURRENT_MODEL.md`;
2. immediately load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch mutable `models/lol/session/CURRENT_SESSION_LOCK.md`;
4. verify lock `LOL-2026-08-30-V13-DK-KT-1612-UTC7` and authority `083a7a97c04e9fb4fd40b74c3dd931643539aaa0`;
5. load the exact v1.3 authority stack in locked order;
6. use Airtable only as ledger/history authority;
7. load this or a newer DK-KT handoff last.
