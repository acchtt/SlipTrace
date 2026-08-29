# Current Live Handoff — T1 vs BNK FEARX — 2026-08-29

**State only — not analytical authority**

## Series

- Competition: `LCK 2026 Playoffs`
- Round: `Upper Bracket Round 1`
- Match: `T1 vs BNK FEARX`
- Format: `Bo5 Fearless Draft`
- Current series score: `T1 1-1 BNK FEARX`
- Game 1 winner: `T1`
- Game 1 final duration: `33:09`
- Game 1 final kills: `T1 25-8 BNK FEARX`
- Game 2 winner: `BNK FEARX`
- Game 2 final duration: `29:07`
- Game 2 final kills: `BNK FEARX 22-4 T1`
- Game 2 final macro: `BFX 9-1 towers, 3-1 dragons, 1-0 barons, 1-0 inhibitors`

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
- Accepted v1.1 samples after G2: `ML_SAMPLE_N=0; DURATION_SAMPLE_N=0`

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

Treat all twenty champions as consumed for Game 3 draft analysis subject to the exact tournament Fearless rules already resolved for this series.

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

The user forgot to confirm while the decision window was live. After the final result, the user explicitly requested both be saved in Airtable. They are stored as **retroactive user-designated ledger Positions outside the v1.1 validation sample** with `0.25u` shadow stake and `0u` actual exposure:

- BFX ML P/L: `-0.25u`
- Over 31 P/L: `+0.22075u`
- combined retro ledger P/L: `-0.02925u`

They do **not** increment `ML_SAMPLE_N` or `DURATION_SAMPLE_N`.

## Game 2 draft and decision record

Side assignment:
- `BNK FEARX Blue`
- `T1 Red`

Draft:
- BNK FEARX: `Rumble / Pantheon / Ahri / Zeri / Yuumi`
- T1: `Ornn / Nocturne / Akali / Ezreal / Seraphine`

Draft-only prior issued: `T1 slight`.

Important ML architecture issue identified before later live checkpoints:
- active v1.1 Moneyline has no explicit persistent team-strength prior;
- draft-only probability must not be treated as a full pregame team win probability;
- in T1 vs BFX this omission can mechanically overstate BFX when live state is favorable;
- therefore G2 ML was held rather than certifying a candidate even when the frozen formula mechanically cleared edge;
- this is a mechanical architecture concern for a future revision, not a mid-series silent model mutation.

G2 live checkpoints:
- ~04:15: BFX +932g, 1-0 kills; ML held, Duration pass/hold.
- ~10:05: BFX +828g, 2-0 kills, T1 first dragon; frozen ML formula mechanically favored BFX but certification was withheld due identified team-strength-prior defect; Duration line 32 was PASS.

Final:
- BNK FEARX won `22-4` in `29:07`.
- Towers `9-1`, dragons `3-1`, barons `1-0`, inhibitors `1-0` for BFX.
- No accepted v1.1 Position in Game 2.
- Airtable map record: `LCK-2026-08-29-T1-BFX-G2`.

## Game 3 preparation

1. Series is tied `1-1`.
2. Resolve Game 3 Blue/Red side assignment.
3. Apply all twenty consumed champions from Games 1-2.
4. Resolve exact five/roles if any lineup changes appear.
5. Produce compact draft prior plus concrete win mechanisms only; no immediate-postdraft TAKE.
6. For ML, continue under frozen v1.1 authority; do not silently add a team-strength variable mid-series. Because the missing team-strength prior has been identified as a mechanical defect, fail closed on any ML candidate whose qualification materially depends on treating the draft/live formula as the complete matchup prior.
7. Duration remains active under the frozen v1.1 Duration Core.
8. Wait for synchronized live state plus executable ML/Duration market.
9. A TAKE CANDIDATE becomes a Position only after exact user confirmation before material live state change.

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
