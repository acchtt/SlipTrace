# Current Live Handoff — T1 vs BNK FEARX — 2026-08-29

**State only — not analytical authority**

## Series

- Competition: `LCK 2026 Playoffs`
- Round: `Upper Bracket Round 1`
- Match: `T1 vs BNK FEARX`
- Format: `Bo5 Fearless Draft`
- Scheduled start: `2026-08-29 15:00 UTC+7 / 17:00 KST`
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
- Actual exposure: `0u`
- Default shadow stake: `0.25u`
- Minimum odds: `1.60`
- ML required edge: `+5.0pp vs raw implied probability`
- Duration required edge: `+7.5pp vs raw implied probability`
- User line-existence confirmation: `ACTIVE`
- v1.1 accepted samples after Game 1: `ML_SAMPLE_N=0; DURATION_SAMPLE_N=0`

## Game 1 draft / Fearless consumption

BNK FEARX Blue:
- Top: `K'Sante`
- Jungle: `Jarvan IV`
- Mid: `Ryze`
- ADC: `Lucian`
- Support: `Milio`

T1 Red:
- Top: `Jayce`
- Jungle: `Vi`
- Mid: `Taliyah`
- ADC: `Yunara`
- Support: `Lulu`

Treat all ten Game 1 champions as consumed for later Fearless-draft analysis subject to the exact tournament reuse rules already resolved for this series.

## Game 1 v1.1 decision record

At the synchronized 11:32 decision window, two TAKE CANDIDATEs were issued:

1. `BFX Moneyline @4.960`
   - model BFX probability: `35%`
   - raw implied probability: `20.2%`
   - model edge: `+14.8pp`
   - final outcome: `LOSS` because T1 won.

2. `Over 31.0 @1.883`
   - locked central final estimate: `F = 33.0m`
   - model Over probability: `64.0%`
   - raw implied probability: `53.1%`
   - model edge: `+10.9pp`
   - final outcome: `WIN` because map ended `33:09`.

However, exact user line confirmation arrived only after material state changes and after the final result. Under v1.1 governance the candidates had expired, so **no retroactive Position was created**, no v1.1 accepted sample increment occurred, and no shadow or actual P/L is booked from these candidates.

Airtable Maps record logged:
- `LCK-2026-08-29-T1-BFX-G1`
- winner `T1`
- duration `33:09`
- final kills `33`
- no accepted Position.

## Bootstrap next continuation

1. Fetch default-branch `models/lol/CURRENT_MODEL.md`.
2. Immediately load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`.
3. Fetch mutable `models/lol/session/CURRENT_SESSION_LOCK.md`.
4. Verify lock `LOL-2026-08-29-V11-T1-BFX-1429-UTC7` and authority commit `f2ee41755508a9286c9a6cb45acacf57dcbe974e`.
5. Re-fetch locked `CURRENT_MODEL.md` at that commit.
6. Load the exact v1.1 stack in locked CURRENT_MODEL order.
7. Use Airtable as map/snapshot/position ledger only.
8. Load this or a newer T1–BFX handoff last.

## Moneyline core

From Team A perspective:

- `D = +1 / 0 / -1` draft prior;
- `R/X/O/T = -2..+2`;
- mechanism state `INTACT / WEAKENING / BROKEN / REPLACED`;
- `S = 1.0*D_eff + 1.5*R + 1.5*X + 1.25*O + 1.0*T`;
- `P(A) = clamp(50% + 3*S pp, 15%, 85%)`;
- raw book implied `1/odds`;
- ML TAKE CANDIDATE requires odds >=1.60 and edge >=+5.0pp.

ML probability is locked before price evidence. Structures are context unless they change forward control.

## Duration core

At current clock `t` in decimal minutes:

`R0 = max(5.0, 31.0 - t)`

Score `V/Q/H/T` on `-2..+2`, then:

`ER = max(2.0, R0 - 1.5*V + 1.0*Q + 1.0*H + 0.75*T)`

`F = t + ER`

Lock `F` before the offered Duration line/odds are used as analytical evidence.

For line `L`:

`P(OVER) = clamp(50% + 7*(F-L) pp, 15%, 85%)`

`P(UNDER) = 100% - P(OVER)` when settlement semantics are clear.

Duration TAKE CANDIDATE requires odds >=1.60 and selected-side edge >=+7.5pp.

Absent conversion opportunity is neutral: low kills, close gold or low towers alone do not prove a slow game.

## Game 2+ execution

1. Incorporate Game 1 consumed champions into Fearless draft reading.
2. Resolve compact draft prior `T1 / EVEN / BFX` and concrete win mechanisms.
3. No pregame/immediate-postdraft betting TAKE.
4. Wait for usable synchronized live state plus executable active-family market.
5. ML: score `R/X/O/T` + mechanism contradiction price-blind, calculate probability, then price.
6. Duration: score `V/Q/H/T`, lock `F`, then use offered line to calculate Over/Under probability and price.
7. Each family qualifies only through its own threshold.
8. Create a Position only after explicit confirmation of the exact quoted market/line/odds **before** a material live event invalidates the candidate.

## Validation freeze

Track ML and Duration independently:

- 10 accepted Positions per family: diagnostic only;
- 20: minimum architecture review;
- 30: preferred first full calibration review.

Audit taxonomy only:

- DRAFT READ ERROR
- LIVE STATE ERROR
- PROBABILITY/CALIBRATION ERROR
- PRICE/EXECUTION ERROR

Do not mutate either family after one ordinary result.

## Historical boundary

All v0.x files/procedures/reviews/Airtable records remain historical/audit/research authority only. Historical Duration DOVC/FCR/FRP is not active. v1.0 is also historical generation authority; its ML formula is carried forward unchanged in v1.1.
