# LoL Multi-TAKE / No-Duplicate Policy — 2026-08-15

**Status:** ACTIVE governance addendum  
**Applies to:** LoL v0.3.59 shadow audit and future live execution unless superseded

## User authorization

The user explicitly authorized multiple qualified TAKEs within the same match/map, while prohibiting duplicate position entries.

## Operating rule

1. **Multiple TAKEs in one match/map are allowed.**
   - There is no one-bet-per-map restriction.
   - Each position must independently satisfy every applicable analytical, live-eligibility, execution, pricing, stale-line and veto gate.
   - A prior TAKE on the map does not lower the threshold for a later TAKE.

2. **Duplicate position entries are forbidden.**
   - A duplicate is the same map + same market family + same exact selection/line, regardless of a later odds change.
   - Example: `Under 25.5 kills` already taken on the map cannot be taken again later merely because the odds changed.
   - A materially different line is a distinct proposition (for example `Under 25.5` versus `Under 23.5`) and may qualify separately.
   - A different market family or opposite side is also a distinct proposition and may qualify separately.

3. **Correlation handling remains mandatory.**
   - Distinct same-map positions can still be highly correlated.
   - Correlation must be assessed explicitly; correlated positions remain grouped as one calibration evidence cluster.
   - No duplicate rule may be bypassed by labeling a repeated position an add-on, re-entry, top-up or reprice.

4. **No rescue / chase behavior.**
   - Multiple TAKE permission does not authorize martingale, loss chasing, rescue entries or stake escalation.
   - Default shadow stake remains 0.25u per independently qualified position; actual exposure remains 0u while official betting is paused.

5. **Ledger check.**
   - Before auto-recording a TAKE after the visible verdict, check the current map's position ledger for an existing identical selection/line.
   - If an identical position already exists, do not create a second position record.

This is an execution/governance change only. It does not create LoL v0.3.60 and does not alter analytical gates or thresholds.
