# Football C — O2.25 leakage calibration (2026-10-13)

**Status:** ACTIVE prospective calibration for Football C only.

This repair is based on the Oct-12 result audit. The audit showed a repeated
false-negative shape at the protected O2.25 burden: fixtures with a STRONG
scoring route and HIGH opponent leakage were being left WATCH/STOP or AVOID
because recent 1-1/two-goal stall history dominated the completion read. At
the same time, higher-burden FOLLOW/RESERVE misses at O2.5/O2.75 showed that a
general relaxation would be unsafe.

## Prospective rule

Football C may fund goal three through a narrow **O2.25 leakage route** when:

- the execution/supported burden is O2.25 or lower;
- at least one scoring route is STRONG;
- opponent leakage is HIGH;
- burden-completion quality is at least MEDIUM;
- route reliability is at least MEDIUM;
- chance quality is at least MEDIUM;
- burden-stall risk is HIGH **or** continuation quality is LOW;
- no material suppression remains;
- no failure mode directly attacks the scoring route.

For this narrow route only, HIGH stall risk or LOW continuation is the
specific suppression being counterweighted rather than an automatic PASS.
If stall risk and continuation are both only MEDIUM, this calibration does
not activate; the original goal-three proof remains required. This prevents a
generic upgrade of ordinary mixed/two-route O2.25 profiles.

LOW burden-completion quality is never rescued.

## Hard limits

This calibration:

- does **not** extend to O2.5, O2.75 or higher;
- does **not** manufacture a fourth-goal tail;
- does **not** bypass a broken thesis, material veto, route-attacking failure
  or material suppression;
- does **not** lower the normal price floor;
- does **not** convert screenshot-only evidence into an executable bet;
- does **not** change C2 policy. (This describes PR #157's original C-only scope;
  the separately authorized prospective C2 follow-on is documented in
  `../challengers/football-c2/FOOTBALL_C2_O225_LEAKAGE_CALIBRATION_20261013.md`
  and does not import C completion/stall fields.)

A high-confidence O2.25 leakage-funded fixture cannot remain C-WATCH/STOP when
evidence confidence, failure resistance and burden protection are each at
least MEDIUM; the board must re-evaluate it as C-FOCUS.

## C2 independence

Football C2 retains its frozen route-quality policy. It does not inherit C's
completion/stall diagnostics or this O2.25 leakage counterweight. Shared
opponent-leakage facts may influence C2's independently researched route and
chance grades, but C2 still clears its own selection floor and clearing-goal
rules.

## Historical integrity

Do not rewrite prior boards, decisions, screenshots, Actual Bets, or Oct-12
assessment records. Audit outcomes are evidence for this prospective
calibration only.
