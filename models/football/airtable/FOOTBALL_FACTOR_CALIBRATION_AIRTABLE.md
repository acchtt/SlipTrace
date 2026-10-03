# Football Factor Calibration — Airtable Contract

**Status:** ACTIVE OBSERVER PERSISTENCE  
**Base:** `SlipTrace Football Decision Control` (`appWyZJjitSBATXAU`)  
**Table:** `Factor Calibration Observations`  
**Table ID:** `tblz2s2KR4BRyAaVo`  
**Authority:** diagnostic only; zero Football C/C2 production authority

## 1. Record identity

One row per frozen Football C fixture per board.

`Observation ID = <Board ID>:<canonical match id/key>`

Do not create duplicate rows for the same frozen board state.

## 2. Freeze-time write

After the Football C board is prospectively frozen, write the immutable factor vector:
- Board ID;
- Match / Competition / Kickoff ICT;
- C Rank / Lane / Supported Line;
- Home Route / Away Route / Carrier;
- Carrier Self Fund;
- Independent Upper Tail;
- Route Reliability;
- Independent Route Quality;
- Chance Quality;
- Failure Resistance;
- XI Robustness;
- Evidence Confidence;
- Burden Protection;
- Completion Mode;
- Burden Completion Quality;
- Continuation Quality;
- Opponent Leakage;
- Burden Stall Risk;
- Failure Attacks Route;
- Material Suppression;
- Calibration Eligible;
- Contamination Reason when not eligible.

Outcome fields remain blank before FT.

## 3. Post-FT append

Audit may later append only:
- Total Goals;
- Support Settlement;
- Support Value;
- Completion Materialized;
- Continuation Materialized;
- Stall Endpoint Observed;
- Trace Score;
- Calibration Notes.

Do not modify the frozen vector after FT.

## 4. Eligibility

`Calibration Eligible = true` only when every factor used by the requested diagnostic was prospectively frozen and recoverable without inference.

If an older board lacks a factor:
- keep the row absent; or
- write an explicitly ineligible row only when useful for audit indexing;
- set a precise Contamination Reason.

Never manufacture new burden-completion grades from FT.

## 5. Trace score

Trace Score is produced by `models/football/engine/factor_calibration.py`.

It is diagnostic only and must never be read by:
- Football C ranking;
- C/C2 board state;
- supported burden construction;
- FOLLOW/RESERVE/STOP;
- Step-2 BET/WAIT/PASS;
- Website Picks.

## 6. Promotion boundary

No Airtable aggregate or trace score directly changes Football C.

A stable overweight/underweight signal must first satisfy `FOOTBALL_FACTOR_CALIBRATION_OBSERVER.md`, then be encoded into a separately versioned challenger for prospective comparison.
