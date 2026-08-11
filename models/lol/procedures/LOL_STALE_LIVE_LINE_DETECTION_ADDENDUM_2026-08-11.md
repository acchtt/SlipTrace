# LoL Stale Live Line Detection Addendum — 2026-08-11

**Status:** Mandatory execution/data-integrity gate  
**Applies to:** all live LoL markets under v0.3.53 and later unless superseded  
**Trigger:** KRX Challengers vs BNK FEARX Youth Game 2, where BFX +3.5 @1.815 and Over 33 @1.747 remained visually frozen across material game-state changes and were mistakenly treated as executable prices.

## 1. Core rule
A visible live line is not automatically an executable live line.

Before any `TAKE`, classify each candidate market as:
- `FRESH / EXECUTABLE`
- `SUSPECT STALE`
- `LOCKED / SUSPENDED`
- `EXPIRED`

Only `FRESH / EXECUTABLE` can be recommended as a TAKE.

## 2. Stale-line fingerprints
Treat a market as `SUSPECT STALE` when any of the following occurs:

1. the exact line and both odds remain unchanged across >=2 synchronized snapshots despite a material state change;
2. the exact line/odds remain unchanged for roughly >=90 seconds while adjacent markets materially reprice;
3. ML reprices materially while duration / total kills / kill handicap remain numerically identical through changing clock, kills, gold, objectives, or structures;
4. a line is visually greyed, disabled, delayed, or otherwise not clearly selectable;
5. the same old line persists after the underlying state has moved far enough that a normal live market should have repriced;
6. user identifies the line as expired, frozen, unavailable, or non-clickable.

Any one strong fingerprint is sufficient to fail closed.

## 3. Mandatory pre-TAKE freshness check
Before outputting `TAKE — selection @odds`:

- compare the candidate line/odds against the immediately prior sportsbook snapshot;
- compare current game clock/state against that prior snapshot;
- verify that the candidate market has refreshed consistently with the new state or is visibly selectable;
- if freshness cannot be established, output `HOLD/PASS — stale-line risk — 0u` and request/await a refreshed board.

Do not use a frozen number merely because it would be attractive if executable.

## 4. Cross-market stale detection
If one market reprices while another remains exactly frozen across a material state move, do not assume the frozen market is live. Treat the unchanged market as stale until a new quote or explicit user confirmation of clickability appears.

## 5. Confirmation rule retained
User confirmation still must match the same executable line/price. A stale/expired line cannot become a recorded position through confirmation after the fact.

## 6. Calibration handling
Stale/expired recommendations are execution-layer errors, not settled model positions.

- no grading;
- no P/L;
- no fade benchmark grading;
- do not count toward v0.3.53 10/20 validation windows;
- log the incident as data-integrity/process evidence.

## 7. KRX-BFX G2 correction
At 23:23 the displayed BFX +3.5 @1.815 and Over 33 @1.747 appeared attractive. At 25:32 those exact numbers were still displayed despite material game-state movement; later they continued to appear frozen while ML and other live prices changed. User then confirmed those were expired/frozen lines.

Correct handling under this addendum: **do not issue TAKE on either frozen market.** They are `EXPIRED / STALE`, not missed bets.
