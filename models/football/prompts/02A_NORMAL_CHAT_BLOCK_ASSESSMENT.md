# /block — Primary Football C kickoff-block assessment

Effective 2026-11-03 ICT.

This is the primary production assessment route. It changes orchestration only.
Football C certificate, supported-burden, XI, H2H, tournament-incentive,
screenshot-only price, persistence and publication rules remain unchanged.

Load:
- `../CURRENT_MODEL.md`
- `COMMAND_ALIASES.md`
- `../procedures/FOOTBALL_ASSESSMENT_DEPTH_AND_BLOCK_COMPARISON.md`
- `02_NORMAL_CHAT_XI_ODDS.md` for runtime/price contracts

## 1. Resolve the complete block before assessing

Accept an explicit kickoff window or a natural request such as "assess the
23:00 block". Resolve all in-scope unstarted fixtures in that requested block
from the current source/date surface. Reuse a current sweep/source snapshot
when available, but do not require /rank before assessment.

Do not pre-filter by:
- Current Rank or Slate Rank;
- FOLLOW / RESERVE / FOCUS_UNFOLLOWED capacity;
- league popularity or prestige;
- whether another fixture already has a cleaner G3 certificate.

User exclusions and production-scope exclusions still apply.

## 2. Equal-depth Football C research

Every credible candidate must reach the same `ASSESSMENT_DEPTH_V1` floor before
the block comparison. Freeze substantive market-independent conclusions for the
fields required by
`FOOTBALL_ASSESSMENT_DEPTH_AND_BLOCK_COMPARISON.md`, including:
primary/reply routes, carrier, current chance creation, G3/G4 mechanisms,
0-0/1-1/2-0 endpoint tests, continuation, leakage, principal failure,
availability/replacements, H2H, tournament incentive/format and match context.

Research incompleteness is not a football PASS.

## 3. Block comparison

After every candidate reaches equal depth, freeze one football-first comparison
for the complete block:
- candidate IDs and kickoff window;
- G3 strength and exact mechanism;
- G4 strength / continuation after goal three;
- carrier/self-funding strength;
- reply dependence;
- endpoint/control exposure;
- tournament incentive;
- supported burden;
- explicit beats-next reasoning.

A one-sided carrier can outrank a balanced two-route candidate. Route count,
league prestige and rank position are not priority bonuses.

Return the complete block in football order, not just the eventual top pick.

## 4. Runtime authority

The user's block request is an explicit user request to assess every candidate
outside rank gating. For each candidate that needs deterministic /xi authority,
use the existing `EXCEPTION` authority contract with:
- `user_requested_exception=true`;
- a unique `exception_reference` prefixed `BLOCK-`;
- fresh full `exception_research`;
- the candidate's own evidence epoch;
- upstream_state reflecting any existing rank state, or NOT_RANKED.

This is not a bypass. The exception research validator, ASSESSMENT_DEPTH_V1,
Football C compiler, screenshot/price policy, persistence/readback and
publication guard all still apply.

Existing rank rows may be displayed as secondary comparison metadata, but do
not inherit their ordering or FOLLOW lane as block football evidence.

## 5. Odds and actions

No odds are required for the football assessment. Always expose the model's
certified supported burden / preferred football line when one exists.

If the user supplied a screenshot, evaluate only the exact visible ladder.
Never search replacement odds or infer unseen current prices.

ACT/BOOK/PASS must come from the deterministic Football C runtime. A PASS on a
higher visible burden must not erase a lower supported visible line.

## 6. Persistence

Persist every block assessment independently to Decision States using its
Assessment ID/evidence epoch, including PASS/REVIEW_ONLY outcomes. Read back
before publishing an official priced verdict.

Do not use a ranked row as a surrogate for an assessment that was actually run
through block mode.

## 7. Role of /rank after this switch

/rank remains a secondary whole-slate comparison, website and audit surface.
It may be run after block assessment to measure selection inversion or compare
global ordering, but it cannot decide which fixtures receive primary
assessment.
