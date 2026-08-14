# LoL Shadow Audit Continuation — 2026-08-15

**Status:** ACTIVE operating policy  
**Model under test:** LoL v0.3.59  
**Supersedes for active governance:** `LOL_SHADOW_AUDIT_CONTINUATION_2026-08-14.md`

## Revision boundary

The user explicitly authorized a narrow model update on 2026-08-15 after a recurring Duration audit showed that 0-0 tower states were still being treated as positive Over/stall evidence despite the earlier v0.3.45 rebuild warning.

The authorized revision is **v0.3.59 only**:

- make 0-0 towers neutral by default for Duration;
- distinguish absent conversion from observed failed conversion;
- add mandatory Latent Conversion Hazard (LCH) assessment before Duration Over;
- add a pre-first-tower cascade check;
- preserve all non-conflicting v0.3.58 and earlier rules.

Reference review:
`models/lol/reviews/DURATION_0_0_TOWER_RECURRENCE_REVIEW_2026-08-15.md`

This authorization does **not** reopen unrestricted map-by-map patching.

## Continued audit policy

1. **Shadow TAKEs remain enabled.**
   - Continue issuing TAKE / PASS / HOLD normally under v0.3.59.
   - Qualified executable shadow TAKEs auto-record at 0.25u simulated stake.
   - Actual exposure remains 0u while official betting is paused.

2. **Freeze resumes at v0.3.59.**
   - Do not create v0.3.60 from an individual subsequent result.
   - Do not add one-off exceptions or thresholds after a single map.
   - Further model changes require explicit user authorization or a later batch-audit decision.

3. **Audit sample segmentation is mandatory.**
   - Preserve v0.3.57 results as the pre-v0.3.58 sample.
   - Preserve v0.3.58 results as the favorite-handicap-corrected / pre-v0.3.59 Duration sample.
   - Record all new selections under v0.3.59 as a distinct post-Duration-correction sample.
   - Do not retroactively change settled picks or P/L.
   - Reference regrades are diagnostic only.

4. **Post-map analysis remains mandatory.**
   - Settle every shadow position.
   - Record model-rule error, execution error, data-quality error or variance separately.
   - For Duration, explicitly record whether structural evidence was ABSENT conversion or FAILED conversion at entry.
   - Record LCH at every future Duration Over TAKE.

5. **Draft primacy and market independence remain intact.**
   - Underdog +kills still requires full fallback certification and the v0.3.56 hard veto.
   - Favorite -kills still uses v0.3.58 FFD/RNE.
   - v0.3.59 changes Duration interpretation only.
   - HIGH LCH does not automatically create an Under TAKE.

## Live-output rule

The first visible line on every active-map screenshot remains the verdict. Connector/logging work occurs after the verdict and must not delay it.

## Authority

GitHub remains model/rules authority. Airtable remains the canonical map/position ledger.
