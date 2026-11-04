# Football C — Assessment Depth and Block Comparison

ASSESSMENT_DEPTH_V1 remains frozen-history compatible from 2026-11-02. ASSESSMENT_DEPTH_V2 is effective for new assessment epochs from 2026-11-04 07:00 ICT.

## ASSESSMENT_DEPTH_V1

A new Football C assessment is incomplete until it freezes substantive, market-independent conclusions for:

- primary scoring route;
- secondary or reply route;
- carrier capacity;
- current chance creation;
- explicit goal-three mechanism;
- independent goal-four mechanism or an explicit football rejection;
- 0-0 stall;
- 1-1 stall;
- continuation from 2-0;
- opponent leakage;
- named principal failure mechanism;
- availability and replacements;
- H2H transferability;
- tournament incentive and format;
- rivalry/rest/travel/fatigue context;
- supported-burden basis.

The manifest must match the evidence epoch and assessment timestamp and contain at least two football evidence references.

Bare labels such as CHECKED, MEDIUM, HIGH, LOW, UNKNOWN or TBD do not satisfy the contract. Missing or thin conclusions must stop with ASSESSMENT_RESEARCH_INCOMPLETE. Do not convert research incompleteness into a football-quality rejection.

Ranked fixtures reuse unchanged frozen rank evidence and refresh only changed availability, incentive, status and unresolved football facts. This contract must not cause a second full-slate research pass.

Explicit exceptions still require the separate fresh-full-research exception contract.

## ASSESSMENT_DEPTH_V2

V2 retains every V1 conclusion and adds one block-selection-only activation
assessment to the frozen match evidence:

- `activation_quality = LOW | MEDIUM | HIGH`;
- `activation_basis` with a substantive prospective explanation; and
- `activation_evidence_refs` containing at least two distinct football sources.

Activation evaluates how readily the current match can become goal-active:
current attacking availability/structure, early chance creation, opponent early
concessions/opening behaviour, whether recent comparable matches become
competitive early, and whether the weaker side can force a game-state change.

Activation is **selection evidence only**. It cannot fund G3/G4/G5/G6, change
the supported burden, authorize ACT/BOOK, or use bookmaker prices/results.

## BLOCK_COMPARISON_V1

When several credible fixtures share one kickoff window, assess them as one comparison block after each candidate reaches the same ASSESSMENT_DEPTH_V1 floor.

Freeze:

- block ID and window;
- candidate match IDs;
- same-depth-completed=true;
- block rank;
- G3 strength;
- G4 strength;
- carrier/self-funding strength;
- reply dependence;
- 0-0 / 1-1 / 2-0 endpoint exposure;
- continuation strength;
- tournament incentive;
- supported burden;
- beats-next basis explaining why each higher candidate outranks the next credible candidate.

Comparison is football-first. League prestige, popularity and the mere existence of two scoring routes cannot substitute for stronger completion and continuation evidence. A one-sided carrier may outrank a balanced two-route match when its third/fourth-goal path is stronger.

## Non-goals

This contract does not change Football C certificate thresholds, G3/G4/G5 funding rules, the two-route quarantine, or historical decisions. It is an orchestration and evidence-completeness repair only.


## G3_BORDERLINE_DISCRIMINATION_V2

The 44-match same-information replay showed that the prior Pareto guard could
not recover false negatives after research compressed them into generic MEDIUM
grades. For new rank epochs, a REVIEW_ONLY row with a STRONG primary route,
USABLE reply, at-least-MEDIUM carrier and core G3 axes, no high stall and no
hard veto is therefore **research-incomplete** until one bounded second pass is
frozen.

The `selection_recheck` object must use
`contract=G3_BORDERLINE_DISCRIMINATION_V2`, be market-independent, contain at
least two football references, name the exact missing G3 requirement, and give
substantive conclusions for primary goal-three path, reply/independent
completion, 0-0/1-1/2-0 stop risk, continuation after goal two, principal
failure, and grade reconciliation.

This contract never upgrades a certificate. If the second pass finds stronger
facts, update the ordinary Football C evidence fields and rerun the unchanged
compiler. Otherwise freeze `CONFIRMED_REVIEW_ONLY`. Missing proof becomes
`G3_BORDERLINE_RESEARCH_PENDING`, not a negative football verdict.

## BLOCK_DISCRIMINATION_V3

For new production blocks from the V3 activation boundary, the old requirement
to reconcile with global Football C /rank is retired. Global rank remains
secondary audit metadata only.

Each credible Grade-A/B block candidate must satisfy ASSESSMENT_DEPTH_V2,
including source-backed activation evidence, and freeze a `block_comparison`
object with equal-depth completion, candidate IDs, block rank, market
independence, at least two football evidence references, and substantive bases
for G3, G4, carrier/self-funding, reply dependence, endpoint exposure,
continuation, tournament incentive, supported burden and beats-next reasoning.

The declared block order must reconcile with the deterministic
`BLOCK_PRIORITY_V1` runtime order. That comparator uses only frozen prematch
football evidence in this order:

1. hard football viability / funded G3 accessibility;
2. activation quality;
3. opponent leakage / game-opening potential;
4. continuation after goals;
5. credible G4 / upper-tail state;
6. 0-0 / 1-1 / 2-0 endpoint resistance;
7. current chance quality;
8. burden-completion quality;
9. frozen 3+/4+ goal signal;
10. protected-burden clearability;
11. certificate robustness/depth; and
12. G3 mechanism class as a late tiebreaker only.

Thus a carrier certificate cannot automatically defeat materially stronger
activation, leakage, continuation and upper-tail evidence. Conversely, HIGH
leakage alone cannot rescue LOW chance quality, a broken route or material
suppression.

BLOCK_PRIORITY_V1 is a selection comparator only. It changes no Football C
certificate threshold and has no price/exposure authority. Screenshot
ACT/BOOK/PASS still requires the existing XI deterministic runtime, Decision
States persistence, independent readback and Step2 publication guard.
