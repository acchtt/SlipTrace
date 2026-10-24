# Football C — execution/burden/selection diagnostic flags

**Date flagged:** 2026-10-25 ICT  
**Evidence surface:** V4-20261024-1800-20261025-0000-PRIORITYFIX  
**Authority:** Football C only  
**Selection authority:** ZERO  
**Backfill prohibited:** YES  
**Severity:** HIGH diagnostic

## Flag 1 — custom-line reachability / execution-path defect

Mainz 05 — Werder Bremen and RB Leipzig — Elversberg were assessed with `wait_reachable=false` because the desired target was not visible in the submitted screenshot. That assumption was operationally wrong for this user/bookmaker context: custom total line + odds orders are available and do not require the target to be visible in the screenshot.

Required audit label:

`CUSTOM_LINE_REACHABILITY_FALSE_NEGATIVE_20261024_SLATE`

Audit requirement: custom-line capability must be persistent execution context. Screenshot visibility governs observed odds only; it must not determine whether a football-authorized custom BOOK target is reachable.

## Flag 2 — certificate-to-execution burden gap

A large share of strong C selections in the 18:00-00:00 slate carried only a compiled O2.50 burden while the tradable prematch market was already commonly O3.25 or higher. Waiting for O2.50 or a low O2.75/O3.00 bridge can therefore leave the strongest fast-scoring trajectories non-executable until after the opportunity is gone.

This is not permission to let market lines create football authority. The audit must determine whether Football C needs a settlement-aware execution ceiling/band for O2.75 / O3.00 / O3.25 derived only from frozen football evidence, distinct from the minimum protected certificate.

Required audit label:

`CERTIFICATE_TO_EXECUTION_BURDEN_GAP_O325_20261024_SLATE`

## Flag 3 — G3 rejection versus G4 promotion asymmetry

Willem II — Cambuur was researcher-declared FOCUS with a strong frozen goal signal, but the deterministic compiler rejected every G3 mechanism and converted it to WATCH/STOP with no supported burden.

HamKam — Rosenborg, on the same frozen slate, was promoted to funded G4 / O3.50 despite several supporting dimensions remaining MEDIUM/MIXED. The comparison raises a prospective calibration question: whether G3 admission is too binary for high-signal two-USABLE-route cases while the carrier-led G4 branch is comparatively permissive.

Required audit label:

`G3_REJECTION_G4_PROMOTION_ASYMMETRY_20261024_SLATE`

## Guardrails

- Do not use eventual match outcomes to manufacture retrospective ACTs or change frozen evidence.
- Replays must use the exact pre-kickoff evidence epochs and then compare resulting board/execution states.
- Keep selection recall, certified burden, execution ceiling, market price, and realized exposure as separate audit layers.
- A repair is acceptable only if frozen replay controls improve without broadly promoting weak/high-risk matches.

## Required follow-up

Run one coordinated frozen replay evaluating:
1. persistent custom-line reachability;
2. a football-only intermediate execution burden policy including O3.25;
3. symmetric G3/G4 mechanism calibration using same-slate controls.

No production threshold change is authorized by this flag alone.


## Flag 4 — overlapping G3 extension policies / Chelsea BOOK path conflict

Chelsea — Tottenham (match 1793619) exposed two active Football C extension policies with different robustness standards.

The evaluated Chelsea state was:
- compiled certificate O2.50 / G3 funded;
- G4 rejected;
- certificate robustness CONDITIONAL;
- credible tail NEAR_FUNDED;
- STRONG self-funded carrier;
- chance quality HIGH;
- continuation MEDIUM;
- upper-tail control pressure MODERATE.

`c_intermediate_burden_profile()` accepts CONDITIONAL-or-better rows and authorized O2.75 plus O3.00 for this profile. `evaluate_c_quote()` evaluates that intermediate profile first, so visible O3.00 @1.80 became BOOK O3.00 @1.90+.

However, `c_g3_book_extension_profile()` separately states that FRAGILE and CONDITIONAL G3 rows may not extend above O2.50 and requires ROBUST football. Because the intermediate branch returns first, the stricter ROBUST-only branch never governs Chelsea.

Required audit label:

`OVERLAPPING_G3_EXTENSION_POLICY_CHELSEA_20261024`

Audit requirement: collapse these overlapping extension authorities into one settlement-aware policy with one explicit robustness standard. Preserve the distinction between O3.00 push-at-three and O3.25 half-loss-at-three, but do not allow branch ordering to decide which risk standard applies.

No retrospective settlement or exposure rewrite is authorized by this flag.
