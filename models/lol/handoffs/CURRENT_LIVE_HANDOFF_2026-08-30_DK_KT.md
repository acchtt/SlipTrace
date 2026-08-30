# Current Live Handoff — Dplus KIA vs KT Rolster — 2026-08-30

**State only — not analytical authority**

## Series

- Competition: `LCK 2026 Playoffs`
- Round: `Round 1`
- Match: `Dplus KIA vs KT Rolster`
- Format: `Bo5 Fearless Draft`
- Scheduled: `2026-08-30 15:00 UTC+7 / 17:00 KST`
- Current series score: `KT Rolster 1-0 Dplus KIA`
- Current map: `Game 2 — live`

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

This is a meaningful but not maximum strength tier. Freeze it for the series absent genuine roster/availability change. Game 1 result does not modify K/P0.

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

## Game 2 — current

User screenshot at ~3:15 confirms exact five/roles:

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

Game 2 live state at screenshot:
- Clock `3:15`
- Kills `0-0`
- Gold lead `KT +22`
- Towers `0-0`
- Dragons `0-0`
- Barons `0-0`
- Inhibitors `0-0`

Blue/Red side assignment has not been explicitly supplied; do not infer from display placement alone.

Fearless consumed entering Game 2:
- KT: `Trundle, Jarvan IV, Syndra, Ezreal, Nautilus`
- DK: `Olaf, Xin Zhao, Orianna, Caitlyn, Bard`

Game 2 draft read under v1.3 should be kept separate from the frozen series strength prior. No pregame/immediate-postdraft TAKE. No executable ML/Duration price has yet been supplied for Game 2, so no betting verdict/Position exists for this map under the current lock.

## Next workflow

1. Resolve Game 2 Blue/Red side when user supplies it.
2. Keep strength frozen: DK `55%` / KT `45%` before draft/live correction.
3. Grade Game 2 draft separately and track Fearless consumption.
4. On synchronized live state + executable market:
   - ML: lock K/P0 + D/R/X/O/T price-blind, then read odds;
   - Duration: score V/Q/H/T, lock F, then read line/odds.
5. TAKE CANDIDATE only if family threshold clears.
6. Accepted Position only after exact live user confirmation before material state change.

## Bootstrap next continuation

Every new continuation must:

1. fetch default `models/lol/CURRENT_MODEL.md`;
2. immediately load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch mutable `models/lol/session/CURRENT_SESSION_LOCK.md`;
4. verify lock `LOL-2026-08-30-V13-DK-KT-1612-UTC7` and authority `083a7a97c04e9fb4fd40b74c3dd931643539aaa0`;
5. load the exact v1.3 authority stack in locked order;
6. use Airtable only as ledger/history authority;
7. load this or a newer DK-KT handoff last.
