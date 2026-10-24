# Football C — Distributed-G3 floor rollback replay

**Date:** 2026-10-24 ICT  
**Base failed replay:** `2026-10-24_SECOND_STAGE_SELECTION_INVERSION_REPLAY.md`  
**Policy under validation:** preserve mechanism/clearability ranking, restore funded distributed-G3 O2.50 floor  
**Outcome authority:** audit only; no outcome field enters ranking or execution compilation.

## Change under test

The failed second-stage rule denied the direct O2.50 execution floor to a
funded distributed-only G3 unless at least one predictive dimension was HIGH.

The same-information replay showed that this removed 18 ACT-capable FOCUS
fixture-epochs and that 14/18 later cleared O2.50.

This rollback removes only that blanket execution veto.

Preserved:
- evidence_confidence remains excluded as a predictive HIGH dimension for active
  C robustness;
- mechanism/clearability-first ranking remains active;
- self-funded carrier > two-route > leakage > distributed-only in mechanism rank;
- intermediate O2.75/O3.00 burden logic remains;
- O3.25 remains G4-required;
- PHANTOM_FLOOR / actual-entry feasibility remains;
- manufactured lower BOOK targets more than 0.25 below the visible line remain
  blocked.

## Frozen replay delta

Same retained cohort as the failed replay:

- 10 sealed boards;
- 89 fixture-epochs;
- 50 compiled FOCUS fixture-epochs.

| Metric | Failed second stage | Floor rollback |
|---|---:|---:|
| Compiled FOCUS | 50 | 50 |
| ACT-capable FOCUS | 28 | 46 |
| ACT-capable share of FOCUS | 56.0% | 92.0% |
| Distributed rows restored | — | 18 |
| New rows beyond the pre-veto cohort | — | 0 |

The 18 restored rows are exactly the cohort previously removed by the blanket
distributed-G3 veto. Their settled O2.50 audit remains 14/18 clear (77.8%) and
4/18 fail (22.2%). That settlement information validates removal of the blanket
veto but does not create a new threshold or discriminator.

## Latest 10:46–12:00 control board

Because all four funded G3 controls now retain the floor, the first ranking
field no longer separates them. The next active ranking field is mechanism
strength, so the carrier controls stay above the distributed controls:

1. Sanfrecce Hiroshima–Shimizu S-Pulse — CARRIER
2. Jeonnam Dragons–Daegu FC — CARRIER
3. Mynavi Sendai–Nojima Stella — DISTRIBUTED
4. Urawa–INAC Kobe — DISTRIBUTED

Thus the useful ranking repair survives the floor rollback.

Important limitation: Mynavi and Urawa regain direct O2.50 capability when
their exact frozen floor checks clear. This repair deliberately does not claim
a prospective feature discriminator that can identify those two losses without
also suppressing the 14 winning distributed controls. Their protection is
therefore ranking/workload demotion, not a hindsight-fitted execution ban.

## Promotion decision

**ROLLBACK ACCEPTED.**

Keep:
- ranking/mechanism demotion;
- evidence-confidence semantic repair;
- entry-feasibility diagnostics;
- middle-burden execution;
- realistic target reachability.

Reject:
- blanket distributed-only G3 execution veto.

No numeric goal-signal threshold is changed from settled outcomes.
