# Football C — coordinated /sweep + /rank repair replay

**Date:** 2026-10-26 ICT  
**Authority:** Football C only  
**Repair target:** /sweep CONTROL_REVIEW authority + /rank FOLLOW global-cap allocation  
**/xi changes:** NONE  
**Replay type:** frozen same-information structural replay; no outcome field enters selection

## Repair under replay

1. CONTROL_REVIEW remains research/calibration-only and is excluded from the
   production `eligible_queue`.
2. FOLLOW keeps at most one primary CLEARABILITY nominee per exact kickoff, but
   the global FOLLOW cap is applied by quality across all primary nominees.
   Kickoff chronology is only a deterministic tie-breaker.

No G3/G4/G5/G6 funding predicate, board-state compiler, ranking key, price rule,
or /xi execution rule is changed by this coordinated repair.

## Exact replay cohort

Only sealed boards that contain the frozen metadata required to replay both
repairs were used. Older rank packages were not backfilled with fields that did
not exist at their evidence epoch.

| Sealed board | Frozen assessed inputs | Old board | Repaired board | CONTROL_REVIEW rows | Controls removed from board |
|---|---:|---:|---:|---:|---:|
| 2026-10-24 07:26–12:00 | 5 | 2 | 2 | 0 | 0 |
| 2026-10-24 10:46–12:00 | 7 | 4 | 4 | 0 | 0 |
| 2026-10-24 18:00–00:00 | 27 | 19 | 18 | 4 | 1 |
| 2026-10-25 09:09–12:00 | 12 | 5 | 2 | 4 | 3 |
| 2026-10-25 main 15:00–03:00 | 54 | 45 | 42 | 4 | 3 |
| **Total** | **105** | **75** | **68** | **12** | **7** |

Seven production board rows existed only because a negative-screen calibration
control was allowed to re-enter production. The repaired sweep removes that
authority path while preserving all CONTROL_REVIEW rows in the research/audit
denominator.

## FOLLOW replay

| Sealed board | Old FOLLOW | Repaired FOLLOW | Membership change |
|---|---:|---:|---|
| 2026-10-24 07:26–12:00 | 2 | 2 | none |
| 2026-10-24 10:46–12:00 | 3 | 3 | none |
| 2026-10-24 18:00–00:00 | 7 | 7 | 1 out / 1 in |
| 2026-10-25 09:09–12:00 | 4 | 2 | 2 zero-authority controls removed |
| 2026-10-25 main 15:00–03:00 | 7 | 7 | 5 out / 5 in |
| **Total** | **23** | **21** | **8 out / 6 in** |

The repaired FOLLOW portfolio improved the frozen workload-quality diagnostics:

| Metric across FOLLOW rows | Old | Repaired |
|---|---:|---:|
| Mean clearability score | 38.26 | **46.76** |
| Mean balanced score | 92.43 | **110.43** |
| Mean upside score | 52.09 | **56.81** |

This improvement is purely prospective/frozen-feature based. No final score,
odds, or post-kickoff field was used to choose the repaired FOLLOW set.

## Notable frozen changes

### 2026-10-25 morning

Removed from production because they were CONTROL_REVIEW:

- Nagoya Grampus Eight–Yokohama F.Marinos — old FOLLOW;
- Oita Trinita–Ventforet Kofu — old RESERVE;
- Kataller Toyama–Consadole Sapporo — old FOLLOW.

The repaired production board retains only the two non-control FOCUS rows.

### 2026-10-25 main slate

Removed from production because they were CONTROL_REVIEW:

- Chindia Targoviste–CSM Olimpia Satu Mare — old FOLLOW;
- FC Midtjylland–Lyngby — old FOCUS_UNFOLLOWED;
- AZ Alkmaar–FC Twente — old FOCUS_UNFOLLOWED.

The fourth control, Helsingborgs IF–Ljungskile, was already outside the
production board.

FOLLOW global-quality reallocation changes the main-slate seven from:

- Norrby–IFK Norrkoeping;
- Cheongju–Yongin;
- Inter–Fiorentina;
- Fortuna Sittard–Excelsior;
- Thun–Lugano;
- Genk–Standard Liege;
- Chindia–Olimpia Satu Mare;

to:

- Inter–Fiorentina;
- PSV Eindhoven–Feyenoord;
- Sparta Rotterdam–Ajax;
- Basel–Grasshopper;
- Thun–Lugano;
- Barcelona–Real Madrid;
- Freiburg–Bayern Munich.

The replay does **not** claim this new seven is predictively superior from one
settled slate. Its purpose is to prove that global capacity now follows the
declared clearability policy rather than accidental kickoff chronology.

## Outcome-overlay warning

The structural replay intentionally reads no outcome fields.

A separate audit overlay on the already reconciled 25-Oct results shows that the
main-slate FOLLOW 3+ reach is **5/7 before and 5/7 after**. Therefore the
allocator repair fixes a real semantics bug but does not, by itself, solve the
selection-inversion problem.

Likewise, CONTROL_REVIEW removal is an authority correction, not a claim that
every negative-screen control is a bad football match. Some controls later
scored highly. The repaired system correctly prevents a calibration lane from
creating production authority; predictive recall must be handled by a separate
G3 mechanism challenger.

## Promotion decision

**PROMOTE the two coordinated authority/allocator repairs.**

They:
- enforce an already-documented zero-authority boundary;
- remove accidental kickoff-first FOLLOW truncation;
- improve frozen FOLLOW workload-quality diagnostics;
- preserve certificates and /xi execution policy;
- do not use outcomes to select rows.

**DO NOT claim the upstream selection problem is solved.**

The replay leaves the next predictive task unchanged: build and test a
same-information G3 mechanism-balance challenger across multiple sealed boards
before modifying carrier/two-route/distributed certificate funding or the
official rank key.
