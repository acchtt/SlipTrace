# Current Live Handoff — T1 vs BNK FEARX — 2026-08-29

**State only — not analytical authority**

## Series

- Competition: `LCK 2026 Playoffs`
- Round: `Upper Bracket Round 1`
- Match: `T1 vs BNK FEARX`
- Format: `Bo5 Fearless Draft`
- Scheduled start: `2026-08-29 15:00 UTC+7 / 17:00 KST`
- Series state at v1.1 handoff update: `not started / no live evidence supplied in this chat`

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
- v1.1 samples: `ML_SAMPLE_N=0; DURATION_SAMPLE_N=0`

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

Score:

- `V` net conversion velocity;
- `Q` compulsory-cycle spacing;
- `H` terminal path depth;
- `T` terminal trajectory;

all on `-2..+2`.

Then:

`ER = max(2.0, R0 - 1.5*V + 1.0*Q + 1.0*H + 0.75*T)`

`F = t + ER`

Lock `F` before the offered Duration line/odds are used as analytical evidence.

For line `L`:

`P(OVER) = clamp(50% + 7*(F-L) pp, 15%, 85%)`

`P(UNDER) = 100% - P(OVER)` when settlement semantics are clear.

Duration TAKE CANDIDATE requires odds >=1.60 and selected-side edge >=+7.5pp.

Absent conversion opportunity is neutral: low kills, close gold or low towers alone do not prove a slow game.

## Series-specific preparation

Before Game 1 draft analysis:

- use canonical saved T1 and BNK FEARX roster context first;
- reliable user-supplied exact lineup/card overrides generic roster sources;
- resolve exact five and roles before using player fit materially;
- resolve current professional patch and applicable Fearless champion-reuse rules.

For each map:

1. resolve compact draft prior `T1 / EVEN / BFX` and concrete win mechanisms;
2. Games 2+ incorporate actual champions consumed earlier in the Fearless series;
3. no pregame/immediate-postdraft betting TAKE;
4. wait for usable synchronized live state plus executable active-family market;
5. ML: score `R/X/O/T` + mechanism contradiction price-blind, calculate probability, then price;
6. Duration: score `V/Q/H/T`, lock `F`, then use offered line to calculate Over/Under probability and price;
7. a family qualifies only through its own threshold;
8. create a Position only after explicit confirmation of the exact quoted market/line/odds.

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

No live betting verdict or Position has been issued for T1–BFX under v1.1 at this handoff update.
