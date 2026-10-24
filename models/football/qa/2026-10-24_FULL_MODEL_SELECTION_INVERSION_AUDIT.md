# Football C — Whole-model selection-inversion audit

**Date:** 2026-10-24 ICT  
**Authority:** Football C only  
**Scope:** /sweep -> /rank -> /xi -> execution/persistence -> audit calibration  
**Predictive production changes in this audit:** NONE

## Executive finding

The model is not statistically proven to be globally inverted, but the current
architecture contains multiple mechanisms capable of producing the user's
observed pattern: reject many eventual high-goal matches while exposing a
smaller set of fragile or over-burdened ACTs.

The strongest signal is not that Football C has no useful football edge. The
historical frozen audit showed O2.50 certificates reaching 8/11 (72.7%), while
O3.50 certificates reached only 2/8 (25.0%). The main failures are therefore
selection recall, burden calibration and execution mapping.

Recent settled priced PASS controls from the 23 Oct 06:00 ICT operating day
through the 24 Oct morning slate contain 9 actual prematch PASS decisions:
5 subsequently cleared the evaluated Over burden and 4 did not. This is a
diagnostic sample, not a calibrated population estimate. Several of those PASS
decisions were produced before the 24 Oct endpoint-control repair and must not
be attributed to the repaired code.

The old deterministically replayable ACT cohort was 2 wins, 3 full losses and
1 half-loss. All six paths are changed/removed by later repairs, so that cohort
diagnoses legacy execution rather than current post-repair ACT precision.

## Severity matrix

### CRITICAL — screening is a terminal predictor despite being described as research admission

`discovery_goal_gate.py` uses four-to-ten-match team histories and hard
thresholds for priority/Over rates/draw traps. `goals_first_intake.py` turns a
fully quantified `WATCH_GOAL_SIGNAL` into a terminal intake state rather than
sending it through full Football C research.

This means a lightweight statistical prescreen can permanently suppress a
fixture before current routes, carrier, leakage, XI and tournament context are
researched by C. Puebla-Monterrey and the previously repaired Viborg threshold
cliff are concrete controls for this defect class.

Across six retained rank bundles examined here, the underlying sweep ledgers
contained 68 terminal `WATCH_GOAL_SIGNAL` rows, 25 qualified rows and 20 review
rows among rows with a completed goal screen. Outcome coverage is not complete
enough to retune these thresholds from hindsight, but the architecture is
clearly a predictive gate rather than merely a priority layer.

**Required repair:** preserve the screen as workload priority, not final football
authority. Add a bounded low-priority/control research path rather than treating
a negative screen as equivalent to a Football C rejection.

### HIGH — Football C board state is externally supplied rather than compiled

`schema.json` requires `board_state` as input. `adapter.run_board()` sorts
Football C by that supplied FOCUS/WATCH/PASS state before the deterministic
ranking key. `validate_c_screen_state()` blocks only a narrow subset of
contradictions.

Retained-board replay shows this has not yet caused the historical split:
33/33 FOCUS rows had funded G3 and 22/22 WATCH rows had no funded G3. Therefore
this is an authority/integrity defect, not the demonstrated historical root
cause of inversion.

**Required repair:** deterministically compile C board state from the same
frozen evidence/certificates, retain researcher-declared state as audit metadata
only, and fail closed on disagreement.

### HIGH — official ranking rewards certificate depth before burden-normalized clearability

The official C ranking key places certificate robustness first and funded
certificate depth second. The code already computes a market-independent,
burden-normalized `follow_clearability_score`, but uses it only to allocate
FOLLOW workload after FOCUS has been selected.

Historical frozen audit:
- FOCUS 3+ reach: 11/19 = 57.9%
- WATCH 3+ reach: 9/18 = 50.0%
- FOCUS 4+ reach: 5/19 = 26.3%
- WATCH 4+ reach: 8/18 = 44.4%
- O2.50 certificate reach: 8/11 = 72.7%
- O3.50 certificate reach: 2/8 = 25.0%

The upper-tail layer is much weaker than the protected G3 floor. Ranking deeper
certificates ahead of shallower clearable burdens can therefore over-prioritize
fragile high lines.

**Required repair:** frozen challenger only. Reuse the existing clearability
profile in official rank before certificate depth, or demote depth to a later
tie-breaker. Merge only if replay improves separation without collapsing useful
coverage.

### HIGH — execution can reject a funded lower burden because the evaluated screenshot line is higher

Several recent false-negative PASSes were C-FOCUS with funded O2.50, while the
single evaluated screenshot quote was O2.75/O3.00/O3.25. Current policy judges
that observed line; it does not clearly require evaluation of every visible
Asian-total line in the screenshot.

The 24 Oct endpoint repair correctly removed synthetic HIGH pressure caused by
stacked MEDIUM/MIXED cautions, but a higher screenshot line can still be
unsupported even when the lower funded C burden remains sound.

**Required repair:** remain screenshot-only, but when multiple totals are
actually visible, parse the visible ladder and deterministically choose the
highest current line at/below C's direct ACT ceiling that clears the price
floor. Never infer a line or price that is not visible.

### MEDIUM-HIGH — one endpoint label mixes G3-floor risk with G4+ tail risk

Current endpoint pressure is shared across execution. A genuine tail-control
concern can therefore erase lower-burden authority unless the repaired G3 floor
path survives it.

**Required repair:** distinguish a route-specific G3 endpoint veto from a G4+
tail-control veto. Hard G3 veto requires evidence that attacks the third-goal
route itself; upper-tail control must not automatically destroy an otherwise
funded G3 floor. Do not change the current numeric low-draw threshold until a
frozen challenger is validated.

### MEDIUM — G4 contract is internally inconsistent

Runtime allows `G4_RESEARCH_COMPLETE_MIXED`, while the canonical RANK procedure
states that a completed G4 investigation must finish FUNDED or REJECTED.
Production receipts currently use MIXED.

**Required repair:** choose one authority. Either formally define MIXED as a
completed non-funded diagnostic state everywhere, or collapse it into
COMPLETE_REJECTED plus separate path diagnostics.

### MEDIUM — G3 BOOK O3.25 authority drift

The active XI prompt and execution repair cap G3-only BOOK at O3.00, while
`production/FOOTBALL_C.md`, `CURRENT_MODEL.md` and the core min-odds helper
still retain O3.25 language/data.

**Required repair:** remove O3.25 from active G3 BOOK authority and constants, or
explicitly mark historical-only. One runtime policy must exist.

### MEDIUM — current model authority still contains a stale partial-rank rule

`CURRENT_MODEL.md` still says a partial verified sweep subset may be handed to
rank if both sides label it PARTIAL. The repaired V4 RANK authority now correctly
fails closed until upstream sweep intake is complete.

**Required repair:** align CURRENT_MODEL with the new fail-closed upstream
completeness boundary.

### MEDIUM — calibration coverage is incomplete

Exceptions, terminal screen rejections and all no-action rows are not stored in
one enumerable outcome ledger. CI proves deterministic contracts, not predictive
quality. This makes it easy to optimize from visible wins/losses while missing
the denominator.

**Required repair:** prospective zero-authority calibration ledger for every
frozen prematch row:
source-visible state, screen state, board state, certificate, robustness,
endpoint pressure, evaluated line/action, final goals, G3/G4/quoted-burden
settlement. Outcomes may update audit/calibration only and never rewrite the
prematch decision.

## What is currently worth preserving

1. Complete date-surface acquisition and the newly repaired inclusive end-time
   boundary.
2. Tournament-incentive verification.
3. Screenshot-only market authority.
4. Deterministic G3/G4 certificate compiler as a base architecture.
5. O2.50/G3 protected burden: this is the strongest retained historical signal.
6. Distributed-G3 hardening that removes weak all-MEDIUM/two-USABLE shapes.
7. BOOK as zero exposure until independently filled.
8. Separation of model decisions from Actual Bets.

## What should not be changed from outcomes alone

- Do not globally relax PASS because several recent PASSes won.
- Do not globally tighten ACT because the old ACT cohort lost.
- Do not raise/lower the low-draw threshold from individual final scores.
- Do not restore old permissive O3.25/O3.50 execution.
- Do not use Auckland City or any other unassessed fixture as a model PASS.

## Coordinated repair order

1. Make sweep negative screens non-terminal for a bounded control/research lane.
2. Compile C board state deterministically; supplied state becomes audit-only.
3. Run a burden-normalized official-rank challenger using existing clearability.
4. Split G3 endpoint authority from upper-tail endpoint authority.
5. Evaluate all actually visible screenshot totals, never only an arbitrarily
   selected quote when a lower funded line is present.
6. Reconcile G4 MIXED and O3.25 BOOK authority drift.
7. Add universal prospective decision/outcome calibration and report:
   ACT hit rate, PASS false-negative rate, execution coverage, FOCUS/WATCH G3
   and G4 reach, and certificate-specific settlement.

## Current decision

**DEEP REPAIR REQUIRED.**

Do not interpret this as proof that every PASS should become ACT. The present
evidence says the model has useful lower-burden football signal but loses much
of it through prescreen recall, upper-tail prioritization and execution mapping.
Architecture should be repaired before another result-driven threshold change.
