# Current Live Handoff — Dplus KIA vs KT Rolster — 2026-08-30

**State only — not analytical authority**

## Series
- Competition: `LCK 2026 Playoffs`
- Round: `Round 1`
- Match: `Dplus KIA vs KT Rolster`
- Format: `Bo5 Fearless Draft`
- Current series score: `KT Rolster 2-0 Dplus KIA`
- Current map: `Game 3 — prep`
- Game 3 side assignment: `KT Rolster BLUE / Dplus KIA RED` (explicitly supplied by user)

## Active model
- Model: `LoL v1.3 — Hierarchy Moneyline + Duration Core`
- Active lock: `LOL-2026-08-30-V13-DK-KT-1612-UTC7`
- Frozen authority commit: `083a7a97c04e9fb4fd40b74c3dd931643539aaa0`
- Circuit breaker: `CLEAR`
- Active markets: `Moneyline + Duration Over/Under`
- Kill Handicap / Total Kills: `RETIRED_FROM_BETTING`
- Actual exposure: `0u`
- Shadow stake: `0.25u`
- Minimum odds: `1.60`
- ML edge threshold: `+5.0pp`
- Duration edge threshold: `+7.5pp`
- Accepted v1.3 samples: `ML_SAMPLE_N=1; DURATION_SAMPLE_N=0`

## Series-frozen Moneyline strength prior
Price-independent, same-series results excluded:
- Dplus KIA: `K=+1 / P0=55%`
- KT Rolster: `K=-1 / P0=45%`

Do not change K/P0 because KT leads 2-0.

## Core formulas
Moneyline:
`S=1.5*D_eff+1.5*R+1.5*X+1.25*O+1.0*T`
`P(A)=clamp(P0(A)+3*S pp,15%,85%)`

Duration:
`R0=max(5.0,31.0-t)`
`ER=max(2.0,R0-1.5*V+Q+H+0.75*T)`
`F=t+ER`
`P(OVER)=clamp(50%+7*(F-L) pp,15%,85%)`

## Game 1 — completed before relock
KT won `15-11` in `38:44`.
- KT: `Trundle / Jarvan IV / Syndra / Ezreal / Nautilus`
- DK: `Olaf / Xin Zhao / Orianna / Caitlyn / Bard`
Historical context only; not a certified DK-KT sample under this relock.

## Game 2 — completed
Draft:
- KT: `Rumble / Skarner / Ahri / Kalista / Renata Glasc`
- DK: `Jayce / Vi / Annie / Taliyah / Alistar`
Draft prior from DK perspective: `D=-1` (KT slight).

User-specified Game 2 clock correction was `displayed -1:10`; this correction was Game-2-specific unless user extends it.

Confirmed v1.3 Position at displayed `14:46` / effective `13:36`:
- State from DK perspective: `K=+1;P0=55%;D=-1;MC=INTACT;R=+2;X=+1;O=0;T=+1;S=4.0`
- Model: `DK 67.0% / KT 33.0%`
- Market: `KT ML @4.259` (book implied `23.48%`)
- Edge: `+9.52pp`
- User confirmed exact line before reported material state change
- Position ID: `LCK-2026-08-30-DK-KT-G2-ML-KT-1356`
- Shadow stake: `0.25u`; actual exposure `0u`
- Result: `WIN`; shadow P/L `+0.81475u`
- Airtable record: `recjcpAqK1BGgDCT7`

Game 2 final:
- KT won `15-13`
- Displayed `43:11`; effective under G2 correction `42:01`
- Towers `KT 6-9 DK`
- Dragons `3-3`
- Barons `KT 1-2 DK`
- Inhibitors `1-1`

## Fearless consumed entering Game 3
KT consumed:
- G1: `Trundle, Jarvan IV, Syndra, Ezreal, Nautilus`
- G2: `Rumble, Skarner, Ahri, Kalista, Renata Glasc`

DK consumed:
- G1: `Olaf, Xin Zhao, Orianna, Caitlyn, Bard`
- G2: `Jayce, Vi, Annie, Taliyah, Alistar`

All 20 champions above are consumed entering Game 3 subject to tournament Fearless rules.

## Game 3 prep
- Side: `KT BLUE / DK RED`.
- Keep frozen strength prior: `DK 55% / KT 45%` before draft/live correction.
- Deep-pool draft emphasis: identify forced/comfortable role picks, engage/disengage balance, protected damage, waveclear, side-lane pressure, objective setup, and whether either team is pushed onto low-agency or off-role-looking combinations.
- KT is on series point, but series score is not allowed to modify K/P0.
- No pregame or immediate-postdraft TAKE.
- Once full draft is supplied, lock `D` price-blind.
- On synchronized live state + executable market, rebuild `R/X/O/T` price-blind before pricing.
- Duration is independent; do not infer slow pace from low early kills alone.
- No Game 2 clock offset carries into Game 3 unless the user explicitly says so.

## Next workflow
1. Receive exact Game 3 five champions/roles.
2. Lock Game 3 draft prior under v1.3.
3. Wait for synchronized live state + executable ML/Duration price.
4. TAKE CANDIDATE only if threshold clears; accepted Position requires exact user confirmation before any material state change.
5. No rescue, chase, martingale, averaging down, or stake escalation.

## Bootstrap next continuation
Every new continuation must fetch default `models/lol/CURRENT_MODEL.md`, load `LOL_SESSION_BOOTSTRAP.md`, verify lock `LOL-2026-08-30-V13-DK-KT-1612-UTC7` and authority `083a7a97c04e9fb4fd40b74c3dd931643539aaa0`, load the exact v1.3 authority stack, use Airtable only as ledger/history authority, and load this or a newer DK-KT handoff last.
