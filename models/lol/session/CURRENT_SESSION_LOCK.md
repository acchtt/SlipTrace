# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-27-E15R1-NS-BFX-G3PLUS-1641-UTC7`  
**Status:** `CLOSED`  
**Effective:** `2026-08-27 16:41 UTC+7`  
**Closed:** `2026-08-27 after Game 4 / series completion`  
**Scope:** `LCK 2026 Play-In — Nongshim RedForce vs BNK FEARX — Games 3–5 only`  
**Superseded lock:** `LOL-2026-08-27-E15-NS-BFX-1547-UTC7`  
**Frozen authority commit:** `d63d372503f3c14ee058464ee77d041399de22ca`  
**Historical analytical model:** `LoL v0.3.58 + E15R1 session speed/decay overlay`  
**Circuit breaker at close:** `CLEAR`  
**Actual exposure:** `0u`

## Final series state

BNK FEARX defeated Nongshim RedForce **3–1**.

- Game 1: NS won 27–8 in 27:53; no position.
- Game 2: BFX won 27–12 in 30:55; confirmed/logged TK Over 39.5 @2.086 lost, -0.25u.
- Game 3: NS lost 10–18; TK Over 29.5 @1.863 was logged under the authority then in force and lost, -0.25u.
- Game 4: BFX won; BFX ML @2.943 was explicitly user-confirmed as still available before acceptance and won, +0.48575u.

Series shadow P/L from the logged positions above: `-0.01425u`. Actual exposure remained `0u`.

## Historical E15R1 authority

Games 3–4 were governed by the frozen authority commit:
`d63d372503f3c14ee058464ee77d041399de22ca`

Historical verdicts and P/L remain frozen under that authority and must not be rewritten by subsequent calibration.

## User line-existence confirmation gate — carried forward

User instruction on 2026-08-27:
**“from now on only log the bet when i confirm it still exists.”**

This execution rule is now canonicalized prospectively in:
`models/lol/procedures/LOL_POST_NS_BFX_MARKET_PRIORITY_AND_EXECUTION_CALIBRATION_2026-08-27.md`

Future session locks must retain it unless explicitly revoked by the user.

## Post-series canonical calibration

After series completion the user instructed:
**“Adjust the model accordingly.”**

The prospective calibration is active on the default branch through:

- `models/lol/CURRENT_MODEL.md`
- `models/lol/procedures/LOL_POST_NS_BFX_MARKET_PRIORITY_AND_EXECUTION_CALIBRATION_2026-08-27.md`
- `models/lol/reviews/NS_BFX_2026-08-27_SERIES_CALIBRATION_REVIEW.md`

Canonical model activation commit containing the new amendment:
`8480902c6b9d664bccfdbd9cc92f242b16c5c6cf`

A future slate must establish a new ACTIVE lock from current default-branch authority before any TAKE-eligible decision.

## Continuation requirement

Because this lock is CLOSED, new sessions must bootstrap from default-branch `CURRENT_MODEL.md`, load the bootstrap procedure, observe this closed historical lock, and create a fresh session lock for the next live slate before issuing a TAKE.

Do not freeze future analysis to this closed lock's historical authority commit.
