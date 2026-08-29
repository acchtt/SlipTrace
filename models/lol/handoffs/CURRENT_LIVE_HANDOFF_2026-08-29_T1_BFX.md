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

Freeze this `K/P0` for the remainder of Game 3 under v1.2 unless a genuine roster/availability change occurs.

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

## Game 3 state

Series entering map: `1-1`.

Exact user-supplied draft:
- T1: `Olaf / Naafiri / Galio / Jhin / Bard`
- BNK FEARX: `Kled / Lee Sin / Annie / Kai'Sa / Shen`

Expected roles from listed order:
- T1: `Olaf top / Naafiri jungle / Galio mid / Jhin bot / Bard support`
- BFX: `Kled top / Lee Sin jungle / Annie mid / Kai'Sa bot / Shen support`

Game 3 Blue/Red assignment has not yet been explicitly confirmed by the user in the handoff. Do not infer side from sportsbook display colors alone.

Post-draft executable market shown at 00:00:
- T1 ML `1.475`
- BFX ML `2.549`
- Duration Over 31 `1.692`
- Duration Under 31 `2.086`
- Total Kills and Kill Handicap are visible but retired from betting.

Draft-only read under v1.2: `BFX slight` (`D=-1` from T1 perspective) because BFX has the cleaner layered hard-engage/global follow-up path through Kled/Lee/Annie/Shen into Kai'Sa, while T1's counter-engage/dive shell through Galio/Olaf/Naafiri/Bard can punish a failed first commit. Team strength remains separate and frozen at T1 `K=+1 / P0=60%`, BFX `K=-1 / P0=40%`.

No immediate-postdraft betting TAKE. Wait for synchronized live state plus executable ML/Duration market.

## Game 3 live workflow

1. Use frozen series strength prior: `T1 K=+1 / P0=60%`, `BFX K=-1 / P0=40%`.
2. Use Game 3 draft prior separately: BFX slight unless later exact role/side information materially changes the mechanism read.
3. ML: score `R/X/O/T` and mechanism price-blind, then calculate from `P0`, then read odds.
4. Duration: score `V/Q/H/T`, lock `F`, then read line/price.
5. No pregame/immediate-postdraft TAKE.
6. A TAKE CANDIDATE becomes an accepted Position only after exact user confirmation before material state change.

## User-authorized next-game Moneyline patch — NOT ACTIVE IN GAME 3

During Game 3 the user explicitly stated the intended causal hierarchy:

`TEAM STRENGTH = STARTING PRIOR`
`DRAFT = MORE IMPORTANT MAP-SPECIFIC CORRECTION`
`LIVE STATE = DOMINANT ONCE REAL EVIDENCE EXISTS`

The user explicitly authorized applying this revised weighting **from the next game onward**, while also instructing that the canonical GitHub model/lock update should be performed **after Game 3 ends**.

Therefore:

- Game 3 remains fully governed by active v1.2 authority and must not be silently rescored under the future patch.
- After Game 3 final, before any Game 4 model-certified betting analysis, create/activate the next model generation and fresh session lock.
- Planned Moneyline repair for that generation:
  - retain `K=-2..+2` as the independent team-strength tier;
  - reduce strength baseline to `P0(A)=50%+5*K pp`;
  - increase draft weight so `D` is a meaningful map-specific correction;
  - planned score: `S=1.5*D_eff+1.5*R+1.5*X+1.25*O+1.0*T`;
  - planned probability: `P(A)=clamp(P0(A)+3*S pp,15%,85%)`;
  - retain ML minimum odds `1.60` and edge threshold `+5.0pp` unless the user separately authorizes a change;
  - retain price-blind probability locking, synchronization, position-blind execution and exact user confirmation controls.
- Duration remains unchanged unless separately authorized.
- Preserve the same pre-series non-price `K` tier evidence logic; only its probability weight changes prospectively.

Until the post-Game-3 GitHub activation and fresh lock are complete, the future patch is **authorized/planned state only**, not active analytical authority.

## Bootstrap next continuation

Every new continuation must:

1. Fetch default-branch `models/lol/CURRENT_MODEL.md`.
2. Immediately load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`.
3. Fetch mutable `models/lol/session/CURRENT_SESSION_LOCK.md`.
4. Verify the current active lock and authority.
5. Re-fetch locked `CURRENT_MODEL.md` at that authority commit.
6. Load the exact active stack in locked CURRENT_MODEL order.
7. Use Airtable only as canonical map/snapshot/position ledger.
8. Load this or a newer T1-BFX handoff last.

If Game 3 has ended and the authorized next-game patch has not yet been canonically activated with a fresh lock, do not issue Game 4 TAKE CANDIDATEs; first complete the model update and lock transition.