# Football C2 — independent O2.25 opponent leakage calibration (2026-10-13)

**Status:** ACTIVE, prospective, C2 shadow only. User-authorized follow-on to PR #157.
The C-owned PR #157 completion/stall counterweight is not copied into C2.

## Observed failure and narrowly defined remedy

In the Oct-12 results/selection audit, several O2.25 rejections had a
STRONG scoring route facing a HIGH-leakage opponent. C2's independent
clearing-goal rule could require a separate upper-tail flag despite current
matchup leakage offering a credible third-goal path.

At **O2.25 only**, `c2_low_burden_leakage_goal3_funded` certifies that
independently evidenced opponent leakage supplies third-goal proof if:

- `c2_opponent_leakage` is HIGH, with a **non-empty C2-specific basis**
  documenting current opponent-specific defensive leakage;
- at least one scoring route is STRONG; carrier is at least USABLE;
- route reliability is HIGH;
- independent route quality, chance quality, failure resistance,
  evidence confidence and burden protection are all >= MEDIUM;
- independent upper-tail proof is absent (the specific C2 gate in question);
- no failure directly attacks the scoring route, and no material suppression.

The C2-owned signal is optional in older/missing-input payloads; absence
**never grants** a rescue. An isolated `c2_opponent_leakage` grade without
basis, or vice versa, fails schema validation. Shared matchup facts can
inform both models but C2's grade and basis must be independently authored,
not copied from C's `opponent_leakage` or completion/stall policy labels.

## Selection and execution

- Qualifying evidence can clear the **C2** selection-quality floor and
  third-goal certification at O2.25. C2-WATCH/PASS contradicting a fully
  qualified O2.25 route is sent back for C2-FOCUS review.
- O2.0 still means a two-goal push. O2.5/O2.75 are *not* rescued.
- A higher quoted line cannot use the O2.25 counterweight as a market-gap
  bridge. Only a genuinely reachable O2.25 target can be considered under
  unchanged independent C2 price, Step-2, XI and tournament rules.
- This rule creates **no fourth-goal certification** or generic relaxation.
- C2 cannot authorize a Website Pick, physical bet or official C action;
  screenshot-only evidence remains conditional and non-executable.

## Preservation and QA

No frozen Oct-12 C or C2 board, exception, price snapshot, actual bet or
Airtable record may be rewritten. Future C2 football evidence must populate
both C2-specific fields when asserting this path. Test independently for
O2.25 approval, missing/bad basis, MEDIUM leakage, weak routes, low-quality
or vetoed signals, O2.5+, bridge protection, C2 board-state contradiction,
and strict separation from C-owned fields.
