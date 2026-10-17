# Ranking research coverage repair — 17 October 2026

Scope: workflow/evidence-accounting repair to SlipTrace Football C. No C
certificate, prediction, ranking-key, price, sweep admission or bet rule changed.

## Discovery evidence

Frozen run `V4-20261017-1200-20261017-1800` contains 39 eligible fixtures:
10 C-assessed (2 FOCUS, 8 WATCH), 24 research-evidence exclusions and 5 closed.
All 24 exclusion notes use the same generic text. The native runtime accepted
reason strings without validating a research-attempt trace. Independent saved
board readback was labelled verified despite incomplete cohort research.
These observations motivate a process repair; they do not prove that additional
fixtures should have received FOCUS or validate any predictive calibration.

## Prospective repair

- Bare evidence-missing/news-unverified/budget reasons remain pending.
- Evidence-limited rows require match identity, exact missing fields, real
  source attempts with timestamps and field-specific findings, and next action.
  Runtime validates structure/time; factual source truth remains the operator's
  responsibility. No artificial minimum search count is introduced.
- Every eligible fixture appears in the coverage manifest. Unresolved rows
  retain sweep facts and research order in a resume queue.
- New native checkpoints retain factual C input, including WATCH/PASS. Resume
  merges only new/updated evidence within the same source/model epoch, preserves
  immutable lineage, refreshes the full cohort status, and removes closed rows.
- An empty assessed cohort can save research progress without fabricating a
  board. Exact board persistence and complete research have distinct statuses.
- XI can use verified FOCUS rows from a partial board while preserving coverage
  labels. It reuses unchanged facts; mandatory current/post-XI football research
  and all existing exposure gates remain in force.
- Canonical launchers resolve the same-run checkpoint and continue unresolved
  work without asking the user to resubmit omitted fixture IDs.

This is a resumable Work procedure, not a background scheduler or an automatic
web researcher. Historical receipts and decisions are not rewritten. The
original 24 research gaps have not been retrospectively assessed by this patch.

## Verification

116 V4 tests and 167 active-engine CI tests passed locally. New regressions
cover the 39/10/24/5 incident shape, trace identity/fields/time validation,
empty research checkpoint, evidence reuse, immutable earlier receipt,
source/model mismatch, newly started fixtures, WATCH retention, exact complete
versus partial readback, and XI transfer of partial coverage.

## Sweep startup follow-up

A user-supplied screenshot shows a separate sweep task stopping because it
reported no local runner and no Actions dispatch capability. This is execution
setup, not a C football rejection. The screenshot does not establish which
tools that task actually had.

The sweep launcher now checks execution capabilities before acquisition,
obtains a missing checkout when execution exists, and identifies the existing
push-triggered recovery workflow (manual dispatch is not necessary). It also
makes the already-authorized independent-provider fallback explicit and retains
acquired source facts as a non-ready checkpoint on genuine execution failure.
Rank receives the same missing-checkout clarification. No source validation
requirement is relaxed and no new workflow or background scheduler is added.
