# LoL Shadow Audit Freeze — 2026-08-13

**Status:** ACTIVE operating policy
**Model under test:** LoL v0.3.57

## Purpose

Collect an unbiased sample of the current model's actual selections without continuing to patch the rules after individual wins/losses.

## Operating policy

1. **Shadow TAKEs remain enabled.**
   - Continue issuing TAKE / PASS / HOLD normally under the frozen v0.3.57 rules.
   - Qualified executable shadow TAKEs are auto-recorded at the standard 0.25u simulated stake.
   - Actual exposure remains 0u while official betting is paused.

2. **No model patching during the freeze.**
   - Do not create a new LoL model version in response to an individual map.
   - Do not alter v0.3.57 eligibility gates, draft classifications, thresholds, market logic, or procedures based on an isolated result.
   - Do not add one-off exceptions or compensating rules.

3. **Post-map analysis is still mandatory.**
   - Settle every recorded shadow position normally.
   - Record whether the pick won/lost and whether the underlying thesis was correct, partially correct, or wrong.
   - Separate execution error from model-rule error from variance.
   - Reviews during the freeze are observational only and must not change active rules.

4. **Draft evaluation remains mandatory and locked before pricing.**
   - Use TEAM prior, DER, FRI, SRI, FER, PDC, PST, ARI, False-Stable Guard, DCR, FF, and the retained market-specific framework.
   - Market attractiveness must not rewrite the draft classification.
   - Live results may test the classification but do not retroactively redefine it.

5. **Audit sample integrity.**
   - Do not invert the model after losses.
   - Do not skip qualified shadow TAKEs merely because recent picks performed poorly.
   - Do not chase losses or change stake size.
   - Keep the same 0.25u simulated stake so results remain comparable.

6. **When changes are allowed again.**
   - The freeze remains active until the user explicitly ends it or explicitly authorizes a batch audit/model revision.
   - Any future revision must be based on the accumulated audit sample, not a single triggering map.

## Live-output rule

The first visible line on every active-map screenshot remains the verdict. Logging and review work happens after the verdict and must not delay it.

## Authority

This policy changes operating governance only. It does **not** modify LoL v0.3.57's analytical rules. Where this policy conflicts with an impulse to patch the model after a result, **the freeze controls**.
