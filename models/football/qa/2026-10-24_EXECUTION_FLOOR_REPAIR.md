# Football C — Execution Floor / Endpoint-Control Repair

**Date:** 2026-10-24 ICT  
**Authority:** Football C only  
**Operating-day audit window:** 2026-10-23 06:00 ICT -> 2026-10-24 03:00 ICT  
**Change class:** risk-tightening correction / execution-authority repair

## Defect

The 2026-10-23 ACT-strength quarantine created two structural overblocks:

1. `endpoint_control_pressure=HIGH` could be synthesized by accumulating ordinary
   MEDIUM completion/continuation/stall grades plus MIXED historical/context
   evidence, even when no direct hard-control signal existed.
2. `execution_strength=FRAGILE` erased all direct ACT authority, including an
   already-funded G3/O2.50 burden when the fragility belonged to the upper tail.

The corrected 06:00->03:00 audit showed useful protection remained necessary
(HAGL distributed-G3 rejection; Teleoptik high-tail rejection), but the late
board also demonstrated that the execution layer could suppress a large share
of already-funded lower burdens. Outcomes are audit evidence only; they do not
set any new numerical threshold.

## Repair

### Endpoint pressure

`HIGH` is now reserved for an existing direct hard-control trigger:

- effective burden stall risk HIGH;
- frozen low-draw-trap rate >= 0.25;
- suppressive H2H with VERIFIED transferability and VERIFIED current corroboration.

Any number of ordinary MEDIUM grades and/or MIXED contextual signals remain
`MODERATE`. They are cautions, not a synthetic hard veto.

### Funded G3 execution floor

A new deterministic `c_goal3_execution_floor_authorized()` gate preserves
O2.50 direct-ACT authority only when:

- C already funds G3 under the existing certificate compiler;
- endpoint pressure is not HIGH;
- burden completion and effective continuation are at least MEDIUM;
- effective stall is no worse than MEDIUM;
- route reliability, chance quality, failure resistance, evidence confidence
  and burden protection are at least MEDIUM;
- no material suppression or route-destroying failure exists.

No new result-derived goal-rate threshold is introduced.

### Execution-strength semantics

- **FRAGILE:** no upper-tail ACT and no BOOK. May retain only the funded O2.50
  G3 floor when the execution-floor gate clears.
- **CONDITIONAL:** a funded O2.50 G3 may ACT at O2.50 when the floor gate clears
  and endpoint pressure is not HIGH. Deeper certificates remain protected by
  0.25 goals below the certified burden. No BOOK.
- **ROBUST:** unchanged; may ACT at/below certificate subject to ordinary gates.
- **BOOK:** unchanged as ROBUST-only. G3 BOOK remains capped at O3.00; G3-only
  O3.25/O3.50 are not re-opened.

## Frozen controls

### HAGL – SLNA

The hardened distributed-G3 rule remains unchanged. The frozen all-MEDIUM,
two-USABLE-route shape still does not fund G3, so no execution floor exists.

### Teleoptik – TSC Backa Topola

The frozen low-draw-trap rate is 0.30, which remains a direct HIGH endpoint
trigger. The FRAGILE O3.50 certificate therefore has no direct ACT ceiling.
The old O3.25 ACT path is not restored.

### Upper-tail fragility

A FRAGILE G4/G5 certificate with a separately valid G3 floor may execute only
at O2.50. It cannot use the deeper certificate to authorize O2.75/O3.00/O3.25/
O3.50.

## Regression coverage

`models/football/engine/tests/test_core.py` now locks:

- stacked MEDIUM/MIXED cautions -> MODERATE, not HIGH;
- low-draw trap 0.25 -> HIGH;
- FRAGILE funded G3 floor may ACT O2.50 when no hard control exists;
- FRAGILE deeper certificate may retain O2.50 but not its upper tail;
- CONDITIONAL G3 may retain O2.50 under MODERATE pressure;
- HAGL still lacks G3 funding;
- Teleoptik remains HIGH/FRAGILE with no direct ACT ceiling.

## Invariants preserved

- football thesis before market;
- screenshot-only odds authority;
- tournament-incentive verification;
- no hindsight/backfill after kickoff;
- no result-derived threshold tuning;
- rank/FOCUS/FOLLOW remain workload priority, not execution authority;
- actual bets remain separate accounting;
- BOOK remains zero exposure until independently confirmed filled.
