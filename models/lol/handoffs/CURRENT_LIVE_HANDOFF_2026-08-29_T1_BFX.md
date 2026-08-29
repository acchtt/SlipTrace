# Current Live Handoff — T1 vs BNK FEARX — 2026-08-29

**State only — not analytical authority**

## Series

- Competition: `LCK 2026 Playoffs`
- Round: `Upper Bracket Round 1`
- Match: `T1 vs BNK FEARX`
- Format: `Bo5 Fearless Draft`
- Current series score: `T1 2-2 BNK FEARX`
- Game 1: `T1 win, 25-8, 33:09`
- Game 2: `BFX win, 22-4, 29:07`
- Game 3: `BFX win` — final duration/kills not recorded in this handoff; Game 4 scoreboard confirmed BFX led the series 2-1 entering G4.
- Game 4: `T1 win, 16-11, 42:46`
- Game 4 final macro: `T1 10-4 towers, 4-3 dragons; BFX 2-1 barons; T1 4-0 inhibitors`

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

Light baseline:
- T1 `P0=55%`
- BFX `P0=45%`

Moneyline:
`S=1.5*D_eff+1.5*R+1.5*X+1.25*O+1.0*T`

`P(A)=clamp(P0(A)+3*S pp,15%,85%)`

Hierarchy:
`strength = light starting prior; draft = meaningful map correction; live state = dominant as evidence accumulates`.

Duration remains unchanged:
`R0=max(5,31-t)`
`ER=max(2,R0-1.5V+Q+H+0.75T)`
`F=t+ER`
`P(OVER)=clamp(50%+7*(F-L) pp,15%,85%)`

## Fearless consumed through Game 4

### BFX
G1: K'Sante, Jarvan IV, Ryze, Lucian, Milio
G2: Rumble, Pantheon, Ahri, Zeri, Yuumi
G3: Kled, Lee Sin, Annie, Kai'Sa, Shen
G4: Yorick, Maokai, Viktor, Corki, Nami

### T1
G1: Jayce, Vi, Taliyah, Yunara, Lulu
G2: Ornn, Nocturne, Akali, Ezreal, Seraphine
G3: Olaf, Naafiri, Galio, Jhin, Bard
G4: Nasus, Skarner, Anivia, Miss Fortune, Neeko

All forty listed champions are consumed entering Game 5, subject to the tournament's exact Fearless rules.

## Game 4 draft / result record

Draft:
- BFX: `Yorick / Maokai / Viktor / Corki / Nami`
- T1: `Nasus / Skarner / Anivia / Miss Fortune / Neeko`

Draft read under v1.3: `T1 slight` (`D=+1` from T1 perspective), with the cleaner grouped Skarner/Neeko -> Anivia/MF fight mechanism versus BFX Yorick side-pressure and Viktor/Corki zone-control path.

Final:
- T1 won `16-11` in `42:46`.
- Towers `10-4 T1`.
- Dragons `4-3 T1`.
- Barons `2-1 BFX`.
- Inhibitors `4-0 T1`.
- No accepted v1.3 Position was created in Game 4.
- Airtable map record: `LCK-2026-08-29-T1-BFX-G4`.

Process correction during G4:
- sportsbook header icons were briefly misread as a kill-state change;
- corrected immediately: header displayed K/D/A plus towers, not team kill totals;
- corrected state kept BFX at 3-1 kills while T1 had structure/objective control.

## Game 5 preparation

1. Series is tied `2-2` — deciding map.
2. Resolve Game 5 Blue/Red side assignment first.
3. Apply all forty consumed champions from Games 1-4.
4. Resolve exact five and roles from user draft/screenshot.
5. Use frozen series strength tier: T1 `K=+1 / P0=55%`, BFX `K=-1 / P0=45%`.
6. Grade Game 5 draft separately and give draft more weight than team strength, per v1.3.
7. No pregame/immediate-postdraft TAKE.
8. Wait for synchronized live state plus executable Moneyline/Duration market.
9. ML: lock K/P0 + D/R/X/O/T price-blind, then read odds.
10. Duration: score V/Q/H/T, lock F, then read line/odds.
11. TAKE CANDIDATE only if family threshold clears; accepted Position only after exact live confirmation before material state change.

## Historical ledger boundary

G1 v1.1 retro user-designated ledger entries outside validation:
- BFX ML @4.960 LOSS -0.25u
- Over 31 @1.883 WIN +0.22075u
- combined -0.02925u
- actual exposure 0u

G2: no accepted v1.1 Position.
G3: v1.2 historical; not rescored under v1.3.
G4: no accepted v1.3 Position.

## Continuation bootstrap

Every new continuation must bootstrap from default `CURRENT_MODEL.md`, load `LOL_SESSION_BOOTSTRAP.md`, fetch the mutable lock, then re-fetch and load the exact v1.3 authority stack at `083a7a97c04e9fb4fd40b74c3dd931643539aaa0`, use Airtable as ledger/history only, and load this or a newer handoff last.
