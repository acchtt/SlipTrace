# Current Live Handoff — T1 vs BNK FEARX — 2026-08-29

**State only — not analytical authority**

## Series

- Competition: `LCK 2026 Playoffs`
- Round: `Upper Bracket Round 1`
- Match: `T1 vs BNK FEARX`
- Format: `Bo5 Fearless Draft`
- Game 1: `T1 win, 25-8, 33:09`
- Game 2: `BFX win, 22-4, 29:07`
- Game 3: completed before Game 4; final result not yet supplied/recorded in this handoff.
- Game 4 is live.

## Active model — Game 4 onward

- Model: `LoL v1.3 — Hierarchy Moneyline + Duration Core`
- Active lock: `LOL-2026-08-29-V13-T1-BFX-G4-1757-UTC7`
- Authority: `083a7a97c04e9fb4fd40b74c3dd931643539aaa0`
- Circuit breaker: CLEAR
- Markets: Moneyline + Duration
- KH/TK: retired
- Actual exposure: 0u
- Shadow stake: 0.25u
- Minimum odds: 1.60
- ML edge: +5.0pp
- Duration edge: +7.5pp
- v1.3 ML sample: 0
- Duration sample: 0

## v1.3 hierarchy

Series strength tier remains reconstructed from pre-Game-1 non-price evidence only:
- T1 `K=+1`
- BFX `K=-1`

New light baseline:
- T1 `P0=55%`
- BFX `P0=45%`

Moneyline:
`S=1.5*D_eff+1.5*R+1.5*X+1.25*O+1.0*T`

`P(A)=clamp(P0(A)+3*S pp,15%,85%)`

Hierarchy:
`strength = light starting prior; draft = meaningful map correction; live state = dominant as evidence accumulates`.

Game 3 remains v1.2 historical evidence and is not rescored under v1.3.

Duration remains unchanged:
`R0=max(5,31-t)`
`ER=max(2,R0-1.5V+Q+H+0.75T)`
`F=t+ER`
`P(OVER)=clamp(50%+7*(F-L) pp,15%,85%)`

## Fearless consumed through Game 3

### BFX
G1: K'Sante, Jarvan IV, Ryze, Lucian, Milio
G2: Rumble, Pantheon, Ahri, Zeri, Yuumi
G3: Kled, Lee Sin, Annie, Kai'Sa, Shen

### T1
G1: Jayce, Vi, Taliyah, Yunara, Lulu
G2: Ornn, Nocturne, Akali, Ezreal, Seraphine
G3: Olaf, Naafiri, Galio, Jhin, Bard

All thirty are consumed for Game 4 subject to tournament Fearless rules.

## Game 4 supplied draft

Screenshot at ~1:50 confirms:

- BFX: `Yorick / Maokai / Viktor / Corki / Nami`
- T1: `Nasus / Skarner / Anivia / Miss Fortune / Neeko`

Expected roles:
- BFX: Yorick top / Maokai jungle / Viktor mid / Corki bot / Nami support
- T1: Nasus top / Skarner jungle / Anivia mid / Miss Fortune bot / Neeko support

Blue/Red side has not been explicitly confirmed; do not infer it from display placement alone.

Game 4 at screenshot state: ~1:50, 0-0 kills, 0-0 objectives/structures, BFX about +128g. This is too early for any betting verdict without synchronized executable ML/Duration prices and no immediate-postdraft TAKE is allowed.

## Historical ledger boundary

G1 v1.1 retro user-designated ledger entries outside validation:
- BFX ML @4.960 LOSS -0.25u
- Over 31 @1.883 WIN +0.22075u
- combined -0.02925u
- actual exposure 0u

G2: no accepted v1.1 Position.
G3: v1.2; no v1.3 rescore.

## Continuation

For Game 4:
1. use v1.3 K/P0 and draft prior separately;
2. no immediate-postdraft TAKE;
3. on synchronized live state + executable market, score ML price-blind then price;
4. score Duration V/Q/H/T, lock F, then line/odds;
5. candidate requires family threshold and timely exact user confirmation.

Every new continuation must bootstrap from default CURRENT_MODEL, load bootstrap procedure, mutable lock, then exact authority stack at `083a7a97c04e9fb4fd40b74c3dd931643539aaa0`, Airtable ledger only, handoff last.
