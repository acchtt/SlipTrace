# Current Live Handoff — Dplus KIA vs KT Rolster — 2026-08-30

**State only — not analytical authority**

## Series
- Competition: `LCK 2026 Playoffs`
- Round: `Round 1`
- Match: `Dplus KIA vs KT Rolster`
- Format: `Bo5 Fearless Draft`
- Current series score: `KT Rolster 2-0 Dplus KIA`
- Current map: `Game 3 — live`
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

## Game 3 — draft complete
Side: `KT BLUE / DK RED`.

Exact user-supplied role-order draft:
- KT: `Gnar / Cho'Gath / Ryze / Ashe / Seraphine`
- DK: `Ambessa / Naafiri / Aurora / Yunara / Lulu`

Game 3 draft prior under v1.3, from DK perspective:
- `D=-1` — KT slight draft edge.
- KT has the cleaner first-contact / front-to-back shell: Ashe arrow and Ryze/Seraphine follow-up can start fights, while Gnar + Cho'Gath provide layered CC, zone denial, objective durability, and anti-dive disruption.
- Cho'Gath silence/knock-up plus Gnar/Seraphine control can punish Ambessa/Naafiri if DK dives predictably.
- DK has stronger backline access and a higher-damage protected carry setup through Ambessa/Naafiri/Aurora reaching KT's immobile Ashe/Seraphine/Ryze while Lulu enables Yunara.
- DK's win condition is more execution- and angle-dependent; KT's is easier to organize in pro play, but Cho'Gath jungle is a real tempo/agency risk and keeps the draft edge only slight.
- Mechanism starts `INTACT`.

With frozen DK `P0=55%`, the immediate draft-adjusted pre-live reference is `DK 50.5% / KT 49.5%`.

No pregame or immediate-postdraft TAKE. No Game 2 clock offset carries into Game 3 unless the user explicitly says so.

### Game 3 live checkpoint — 06:50
User-supplied detailed state and executable market are treated as the same decision window because both show `1-1` kills and no contradictory objective/structure event.

State:
- Clock: `06:50` (no G2 offset carried into G3)
- Kills: `KT 1-1 DK`
- Gold: `KT +643`
- Towers: `0-0`
- Dragons: `0-0`
- Barons: `0-0`
- Role-weighted gold is modestly KT-favored: Gnar, Cho'Gath and especially Ashe are ahead; DK support has the only visible small counter-edge.

Price-blind ML state from DK perspective:
- `K=+1 / P0=55%`
- `D=-1`
- `MC=INTACT`
- `R=-1`
- `X=0`
- `O=0`
- `T=0`
- `S=-3.0`
- Model: `DK 46.0% / KT 54.0%`

Market:
- DK `2.313` -> implied `43.23%`, edge `+2.77pp`
- KT `1.567` -> below `1.60` minimum odds
- Verdict: `ML PASS`

Duration at 06:50:
- `V=0,Q=0,H=+2,T=0`
- `F=33.0m`
- line 32: Over `1.575`, Under `2.297`
- model Over `57.0%`, Under `43.0%`
- Over is below minimum odds; Under has no edge
- Verdict: `Duration PASS`

Airtable snapshot: `LCK-2026-08-30-DK-KT-G3-0650` / record `rec3mTMFoNZRoaTWQ`.

## Next workflow
1. Wait for synchronized Game 3 live state + executable ML/Duration price.
2. Rebuild `R/X/O/T` price-blind before reading ML price.
3. Keep `D=-1` unless the actual roles differ from the supplied role order or the mechanism materially changes.
4. Duration is independent; score `V/Q/H/T`, lock `F`, then read line/odds.
5. TAKE CANDIDATE only if threshold clears; accepted Position requires exact user confirmation before any material state change.
6. No rescue, chase, martingale, averaging down, or stake escalation.

## Bootstrap next continuation
Every new continuation must fetch default `models/lol/CURRENT_MODEL.md`, load `LOL_SESSION_BOOTSTRAP.md`, verify lock `LOL-2026-08-30-V13-DK-KT-1612-UTC7` and authority `083a7a97c04e9fb4fd40b74c3dd931643539aaa0`, load the exact v1.3 authority stack, use Airtable only as ledger/history authority, and load this or a newer DK-KT handoff last.
