# LoL Multi-TAKE / No-Duplicate Policy — 2026-08-15

**Status:** ACTIVE governance addendum  
**Applies to:** LoL v0.3.59 shadow audit and future live execution unless superseded

## User authorization

The user explicitly authorized multiple qualified TAKEs within the same match/map, while prohibiting duplicate use of the same market family.

## Operating rule

1. **Multiple TAKEs in one match/map are allowed across different market families.**
   - There is no one-bet-per-map restriction.
   - Each position must independently satisfy every applicable analytical, live-eligibility, execution, pricing, stale-line and veto gate.
   - A prior TAKE on the map does not lower the threshold for a later TAKE in another family.

2. **Maximum one TAKE per market family per map.**
   - Once a market family has a TAKE on that map, that family is closed for additional TAKEs for the remainder of the map.
   - This applies regardless of later odds changes, line movement, side changes, or a materially different numerical line.
   - Core live families are:
     - `ML` — Moneyline
     - `KH` — Kill Handicap
     - `TK` — Total Kills
     - `TT` / `Duration` — Total Time / Map Duration
   - Example: after `Under 25.5 kills` is taken, no later TK position such as `Under 23.5`, `Over 30.5`, or the same line at a new price may be taken on that map.
   - Example: after `G2 -7.5 kills` is taken, no later KH position on either team or any different handicap line may be taken on that map.
   - Multiple TAKEs remain possible if they are in different families, e.g. one ML + one KH + one TK + one Duration, provided each independently qualifies.

3. **Correlation handling remains mandatory.**
   - Distinct same-map positions across market families can still be highly correlated.
   - Correlation must be assessed explicitly; correlated positions remain grouped as one calibration evidence cluster.
   - The one-per-family rule may not be bypassed by labeling a repeated position an add-on, re-entry, top-up, alternate line, opposite side, or reprice.

4. **No rescue / chase behavior.**
   - Multiple TAKE permission does not authorize martingale, loss chasing, rescue entries or stake escalation.
   - Default shadow stake remains 0.25u per independently qualified position; actual exposure remains 0u while official betting is paused.

5. **Ledger check.**
   - Before auto-recording a TAKE after the visible verdict, check the current map's position ledger for any existing position in that market family.
   - If that family already has a TAKE, do not create another position record in that family on the same map.

This is an execution/governance change only. It does not create LoL v0.3.60 and does not alter analytical gates or thresholds.
