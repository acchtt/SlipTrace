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

## ASSESSMENT_DEPTH_V3

Effective for new assessment epochs from 2026-11-05 08:15 UTC.

V3 retains every V2 conclusion and closes two observed failure modes.

**Ignition calibration:** HIGH activation must be supported by structured
current-from-0-0 evidence. Freeze current attack structure, early chance
creation, early concession/opening behavior, game-state forcing pressure and
the weaker side's ability to change state. HIGH requires at least two HIGH
signals, one of which must be early chance creation or early concession/opening,
plus at least MEDIUM current attack structure. Full-match over rates, historical
scorelines and generic table urgency are corroboration only.

**Tournament structure proof:** any fixture requiring tournament incentive must
freeze the actual structure kind (regular league, group stage, knockout first
leg, knockout second leg, single elimination, final or other verified), a
substantive basis, and at least one official-competition or primary-organizer
format source. Stage and aggregate state must be internally consistent.
Unknown/secondary-only structure evidence blocks normal production assessment.

These fields are prospective evidence only. They do not use odds or outcomes
and do not rewrite historical V1/V2 epochs.

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

## BLOCK_DISCRIMINATION_V3 — lightweight selection mode

Effective for new /block calls from 2026-11-07.

The previous production rule requiring every block candidate to complete
ASSESSMENT_DEPTH_V2/V3 before comparison is retired because it duplicates /xi
work and consumes excessive research/usage.

New /block is a two-stage selector:

1. **block sweep:** resolve the entire unstarted cohort and freeze lightweight
   goals-first intake evidence for every fixture;
2. **block rank:** compare only qualified survivors, select **3–5 PRIMARY**
   candidates, then retain the strongest remaining professional candidates in a
   **HIGH_SIGNAL_RESERVE** lane up to **10 total visible rows**.

Active deterministic comparison invariant: **BLOCK_PRIORITY_V1**. Lightweight
/block does not run full depth on the entire cohort, but its declared football
order must not contradict the goal-first principles of BLOCK_PRIORITY_V1.

Band A and Band B form one football-first professional pool. Competition band or
observability is not an early ranking bonus and cannot hide a materially stronger
goal signal. Band C remains constrained by the active 15-point plus verified-
researchability safeguard.

Every completed block freezes an `omission_audit`. A qualified A/B candidate
hidden solely because the 10-row display cap was reached is retained in that
audit with `omission_reason=DISPLAY_CAP_ONLY`.

The lightweight comparison may use current scoring-route signal, opponent
leakage, recent comparable 3+/4+ signal, game-state/incentive pressure,
endpoint/control risk and observability/XI readiness.

It MUST NOT claim a Football C G3/G4 certificate, supported burden,
ASSESSMENT_DEPTH_V3 completion, ACT/BOOK/PASS, or Decision States execution for
a fixture that has only passed the lightweight block selector.

A selected fixture receives full ASSESSMENT_DEPTH_V3 only when /xi is invoked
(or when another explicit deep-assessment command requires it). /xi then owns
H2H materiality, detailed failure mechanisms, G4 research, certificate
compilation, screenshot price evaluation and persistence/readback.

Historical equal-depth block receipts remain immutable/readable. This change is
prospective and exists specifically to keep block selection materially cheaper
than deep assessment of the entire cohort.

