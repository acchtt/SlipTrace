# Football C — Assessment Depth and Block Comparison

Effective for new assessment epochs from 2026-11-02 08:45 ICT.

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

## BLOCK_DISCRIMINATION_V2

The prior BLOCK_COMPARISON_V1 prose requirement is now fail-closed for
production rank. Deterministic Grade-A candidate blocks are formed from nearby
kickoffs (adjacent gap no more than 60 minutes, total block span no more than 90
minutes) when the block contains at least one FOCUS row.

Each candidate freezes a `block_comparison` object with equal-depth completion,
candidate IDs, block rank, market independence, at least two football evidence
references, and substantive bases for G3, G4, carrier/self-funding, reply
dependence, endpoint exposure, continuation, tournament incentive, supported
burden and beats-next reasoning.

The comparison does not override Football C. Its relative order must reconcile
with the deterministic engine inputs. A disagreement means the grades/research
are not yet internally coherent; the whole block checkpoints as
`BLOCK_COMPARISON_PENDING` until the factual grades and football comparison
agree.

This is deliberately a research-completeness repair rather than a result-fitted
new scoring threshold.
