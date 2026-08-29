# Current Live Handoff — T1 vs BNK FEARX — 2026-08-29

**State only — not analytical authority**

## Series

- Competition: `LCK 2026 Playoffs`
- Round: `Upper Bracket Round 1`
- Match: `T1 vs BNK FEARX`
- Format: `Bo5 Fearless Draft`
- Current series score: `T1 1-0 BNK FEARX`
- Game 1 winner: `T1`
- Game 1 final duration: `33:09`
- Game 1 final kills: `T1 25-8 BNK FEARX`

## Active model state

- Model: `LoL v1.1 — Moneyline + Duration Core`
- Active lock: `LOL-2026-08-29-V11-T1-BFX-1429-UTC7`
- Frozen authority commit: `f2ee41755508a9286c9a6cb45acacf57dcbe974e`
- Circuit breaker: `CLEAR`
- Active markets: `Moneyline + Duration Over/Under`
- Kill Handicap: `RETIRED_FROM_BETTING`
- Total Kills: `RETIRED_FROM_BETTING`
- Actual exposure policy: `0u`
- Default shadow stake: `0.25u`
- Minimum odds: `1.60`
- ML required edge: `+5.0pp`
- Duration required edge: `+7.5pp`
- Exact live user confirmation gate: `ACTIVE`
- Accepted v1.1 samples after G1: `ML_SAMPLE_N=0; DURATION_SAMPLE_N=0`

## Game 1 Fearless consumption

BNK FEARX consumed:
- `K'Sante`
- `Jarvan IV`
- `Ryze`
- `Lucian`
- `Milio`

T1 consumed:
- `Jayce`
- `Vi`
- `Taliyah`
- `Yunara`
- `Lulu`

Treat all ten as consumed in Game 2 draft analysis subject to the exact tournament Fearless rules already resolved for this series.

## Game 1 decision / ledger state

At the synchronized 11:32 window two live TAKE CANDIDATEs were issued:

1. `BFX ML @4.960`
   - model probability `35.0%`
   - raw implied `20.16%`
   - edge `+14.84pp`
   - final result `LOSS`

2. `Over 31 @1.883`
   - locked `F=33.0m`
   - model Over probability `64.0%`
   - raw implied `53.11%`
   - edge `+10.89pp`
   - final result `WIN` at `33:09`

The user forgot to confirm while the decision window was live. After the final result, the user explicitly requested both be saved in Airtable. They have therefore been stored as **retroactive user-designated ledger Positions outside the v1.1 validation sample** with `0.25u` shadow stake and `0u` actual exposure:

- BFX ML P/L: `-0.25u`
- Over 31 P/L: `+0.22075u`
- combined retro ledger P/L: `-0.02925u`

These records do **not** increment `ML_SAMPLE_N` or `DURATION_SAMPLE_N` and do not alter the frozen v1.1 model.

## Game 2 state

- Side assignment confirmed by user: `BNK FEARX Blue / T1 Red`.
- Series score entering map: `T1 1-0 BNK FEARX`.
- Apply all Game 1 Fearless consumption before grading the Game 2 draft.

## Game 2 preparation

1. Apply Fearless consumption from Game 1.
2. Resolve exact five/roles if any lineup changes appear.
3. Produce only a compact draft prior `T1 / EVEN / BFX` plus concrete mechanisms.
4. No pregame or immediate-postdraft betting TAKE.
5. Wait for synchronized live state plus executable ML/Duration market.
6. ML: score `R/X/O/T` + mechanism contradiction price-blind, calculate probability, then read price.
7. Duration: score `V/Q/H/T`, lock `F`, then read line and price.
8. A TAKE CANDIDATE becomes a Position only after exact user confirmation before a material live event invalidates it.

## Bootstrap next continuation

Every new continuation must:

1. Fetch default-branch `models/lol/CURRENT_MODEL.md`.
2. Immediately load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`.
3. Fetch mutable `models/lol/session/CURRENT_SESSION_LOCK.md`.
4. Verify lock `LOL-2026-08-29-V11-T1-BFX-1429-UTC7` and authority `f2ee41755508a9286c9a6cb45acacf57dcbe974e`.
5. Re-fetch locked `CURRENT_MODEL.md` at that authority commit.
6. Load the exact v1.1 stack in locked CURRENT_MODEL order.
7. Use Airtable only as canonical map/snapshot/position ledger.
8. Load this or a newer T1-BFX handoff last.
