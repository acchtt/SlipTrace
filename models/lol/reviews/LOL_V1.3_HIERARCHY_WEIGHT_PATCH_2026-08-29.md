# LoL v1.3 Hierarchy Weight Patch — 2026-08-29

## Trigger

During T1 vs BNK FEARX Game 3, the user clarified that persistent team strength should matter as a starting prior, but draft and especially realized in-game advantage should matter more.

The user explicitly authorized the revised weighting for the next game onward and instructed that canonical model files be updated after Game 3 ended.

Game 3 therefore remains v1.2 historical evidence and is not rescored under v1.3.

## Repair

Retain the independent strength tier `K=-2..+2`, but reduce its baseline weight:

`P0=50%+5*K pp`

Increase intact draft weight:

`S=1.5*D_eff+1.5*R+1.5*X+1.25*O+1.0*T`

Final probability:

`P=clamp(P0+3*S pp,15%,85%)`

Thus one K tier is 5pp, one intact draft step is 4.5pp, and accumulated live evidence can dominate quickly through multiple variables at ±2.

## T1 vs BNK FEARX series prior

Keep the previously reconstructed pre-series tier itself unchanged:

- T1 `K=+1`
- BFX `K=-1`

Only the weight changes prospectively:

- T1 `P0=55%`
- BFX `P0=45%`

The tier remains based only on pre-Game-1 non-price evidence; same-series results do not alter it.

## Boundaries

- v1.3 activates prospectively from Game 4 after a fresh authority lock.
- v1.2 Game 3 remains historical.
- Duration remains unchanged.
- ML odds floor remains 1.60 and edge threshold remains +5.0pp.
- exact user confirmation, synchronization, position-blindness and 0u actual exposure remain unchanged.
