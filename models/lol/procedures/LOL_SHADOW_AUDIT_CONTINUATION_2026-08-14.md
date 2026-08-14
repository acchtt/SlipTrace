# LoL Shadow Audit Continuation — 2026-08-14

**Status:** ACTIVE operating policy  
**Model under test:** LoL v0.3.58  
**Supersedes for active governance:** `LOL_SHADOW_AUDIT_FREEZE_2026-08-13.md`

## Revision boundary

The user explicitly authorized a narrow model update on 2026-08-14 after accumulated audit evidence showed a repeated favorite-handicap confirmation problem.

The authorized revision is v0.3.58 only: remove Baron/inhibitor as mandatory favorite -kills prerequisites and add Forced-Fight Density / Required Net Expansion assessment.

This authorization does **not** reopen unrestricted map-by-map patching.

## Continued audit policy

1. **Shadow TAKEs remain enabled.**
   - Continue issuing TAKE / PASS / HOLD normally under v0.3.58.
   - Qualified executable shadow TAKEs are auto-recorded at 0.25u simulated stake.
   - Actual exposure remains 0u while official betting is paused.

2. **Freeze resumes at v0.3.58.**
   - Do not create v0.3.59 from an individual subsequent result.
   - Do not add one-off exceptions or thresholds after a single map.
   - Further model changes require explicit user authorization or a later batch-audit decision.

3. **Audit sample segmentation is mandatory.**
   - Preserve v0.3.57 results as the pre-revision sample.
   - Record all new selections under v0.3.58 as a distinct post-revision sample.
   - Do not retroactively change settled v0.3.57 positions to v0.3.58 picks.
   - Reference regrades are diagnostic only and do not alter historical P/L.

4. **Post-map analysis remains mandatory.**
   - Settle every shadow position.
   - Record model-rule error, execution error, data-quality error or variance separately.
   - Record notable false PASS/HOLD cases when the market outcome is useful for calibration, without treating untaken bets as P/L.

5. **Draft primacy remains intact.**
   - Underdog +kills still requires DER, FRI, SRI, FER, PDC, PST, ARI, False-Stable Guard, DCR and FF certification before pricing.
   - v0.3.56 hard draft-collapse veto remains non-overridable.
   - v0.3.58 changes favorite -kills terminal-confirmation logic only.

## Live-output rule

The first visible line on every active-map screenshot remains the verdict. Connector/logging work occurs after the verdict and must not delay it.

## Authority

GitHub remains model/rules authority. Airtable remains the canonical map/position ledger.
