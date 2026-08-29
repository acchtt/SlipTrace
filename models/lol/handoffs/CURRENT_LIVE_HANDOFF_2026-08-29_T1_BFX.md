# Current Live Handoff — T1 vs BNK FEARX — 2026-08-29

**State only — not analytical authority**

## Series

- Competition: `LCK 2026 Playoffs`
- Round: `Upper Bracket Round 1`
- Match: `T1 vs BNK FEARX`
- Format: `Bo5 Fearless Draft`
- Current series score: `T1 1-1 BNK FEARX`
- Game 1: `T1 win, 25-8, 33:09`
- Game 2: `BNK FEARX win, 22-4, 29:07`
- Game 2 macro: `BFX 9-1 towers, 3-1 dragons, 1-0 barons, 1-0 inhibitors`

## Active model state — prospective from Game 3

- Model: `LoL v1.2 — Strength-Prior Moneyline + Duration Core`
- Active lock: `LOL-2026-08-29-V12-T1-BFX-G3-1650-UTC7`
- Frozen authority commit: `18a5c9c6e6e2a7efe820b6da3f0269d2e8e1e18f`
- Circuit breaker: `CLEAR`
- Active markets: `Moneyline + Duration Over/Under`
- Kill Handicap: `RETIRED_FROM_BETTING`
- Total Kills: `RETIRED_FROM_BETTING`
- Actual exposure: `0u`
- Shadow stake: `0.25u`
- Minimum odds: `1.60`
- ML edge: `+5.0pp`
- Duration edge: `+7.5pp`
- Exact live confirmation gate: `ACTIVE`
- v1.2 accepted samples: `ML_SAMPLE_N=0; DURATION_SAMPLE_N=0`

## v1.2 Moneyline strength prior for this series

Reconstructed only from evidence available before Game 1; sportsbook price and Games 1-2 results were excluded.

From BFX perspective:

`K=-1`
`P0(BFX)=40%`

From T1 perspective:

`K=+1`
`P0(T1)=60%`

Basis: T1 had the stronger established top-level baseline/direct playoff path; BFX had enough recent official same-league wins and successful Play-In form that the gap is meaningful but not the maximum tier.

Freeze this `K/P0` for the remainder of the series unless a genuine roster/availability change occurs.

Moneyline probability from Team A perspective:

`S=1.0*D_eff+1.5*R+1.5*X+1.25*O+1.0*T`

`P(A)=clamp(P0(A)+3*S pp,15%,85%)`

Price may not choose or modify `K`.

## Duration

Duration is unchanged from v1.1:

`R0=max(5.0,31.0-t)`

`ER=max(2.0,R0-1.5*V+1.0*Q+1.0*H+0.75*T)`

`F=t+ER`

`P(OVER)=clamp(50%+7*(F-L) pp,15%,85%)`

Absent conversion opportunity remains neutral.

## Fearless consumption through Game 2

### BNK FEARX consumed
Game 1:
- `K'Sante`
- `Jarvan IV`
- `Ryze`
- `Lucian`
- `Milio`

Game 2:
- `Rumble`
- `Pantheon`
- `Ahri`
- `Zeri`
- `Yuumi`

### T1 consumed
Game 1:
- `Jayce`
- `Vi`
- `Taliyah`
- `Yunara`
- `Lulu`

Game 2:
- `Ornn`
- `Nocturne`
- `Akali`
- `Ezreal`
- `Seraphine`

Treat all twenty champions as consumed for Game 3 draft analysis subject to the exact tournament Fearless rules.

## Game 1 ledger boundary

At the synchronized 11:32 v1.1 window:

1. `BFX ML @4.960` — v1.1 candidate, final LOSS.
2. `Over 31 @1.883` — v1.1 candidate, final WIN at 33:09.

The user forgot live confirmation. After the result, both were saved as retroactive user-designated Airtable ledger Positions outside validation:

- BFX ML: `-0.25u`
- Over 31: `+0.22075u`
- combined retro ledger: `-0.02925u`
- actual exposure: `0u`

They do not increment any accepted validation sample.

## Game 2 model boundary

Draft:
- BFX: `Rumble / Pantheon / Ahri / Zeri / Yuumi`
- T1: `Ornn / Nocturne / Akali / Ezreal / Seraphine`

Draft prior: `T1 slight`.

The missing team-strength prior was identified during Game 2 and ML certification was withheld rather than silently mutating v1.1. No accepted Game 2 Position was created. Game 2 remains historical v1.1 evidence and is not relabeled v1.2.

## Game 3 preparation

1. Series tied `1-1`.
2. Resolve Game 3 Blue/Red side.
3. Apply all twenty consumed champions.
4. Resolve exact five/roles if lineup changes appear.
5. Use frozen series strength prior: `BFX K=-1 / P0=40%`, `T1 K=+1 / P0=60%`.
6. Grade compact map-specific draft prior separately from team strength.
7. No pregame/immediate-postdraft betting TAKE.
8. Wait for synchronized live state + executable ML/Duration market.
9. ML: lock `K/P0`, then score `D/R/X/O/T` price-blind, calculate probability, then read price.
10. Duration: score `V/Q/H/T`, lock `F`, then read line/price.
11. TAKE CANDIDATE only through its family threshold; accepted Position only after exact live user confirmation before material state change.

## Bootstrap next continuation

Every new continuation must:

1. Fetch default-branch `models/lol/CURRENT_MODEL.md`.
2. Immediately load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`.
3. Fetch mutable `models/lol/session/CURRENT_SESSION_LOCK.md`.
4. Verify lock `LOL-2026-08-29-V12-T1-BFX-G3-1650-UTC7` and authority `18a5c9c6e6e2a7efe820b6da3f0269d2e8e1e18f`.
5. Re-fetch locked `CURRENT_MODEL.md` at that authority commit.
6. Load the exact v1.2 stack in locked CURRENT_MODEL order.
7. Use Airtable only as canonical map/snapshot/position ledger.
8. Load this or a newer T1-BFX handoff last.
