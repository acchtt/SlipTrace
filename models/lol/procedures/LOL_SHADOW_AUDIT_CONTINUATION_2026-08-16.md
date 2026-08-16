# LoL Shadow Audit Continuation — 2026-08-16

**Status:** ACTIVE operating policy  
**Model under test:** LoL v0.3.60  
**Supersedes for active governance:** `LOL_SHADOW_AUDIT_CONTINUATION_2026-08-15.md`

Active execution addenda remain:

- `models/lol/procedures/LOL_MULTI_TAKE_NO_DUPLICATE_POLICY_2026-08-15.md`
- `models/lol/procedures/LOL_LIVE_EXECUTION_CALIBRATION_2026-08-15.md`
- `models/lol/procedures/LOL_COMPACT_OUTPUT_FULL_ANALYSIS_RULE_2026-08-15.md`

## Revision boundary

On 2026-08-16 the user requested a full audit review, then focused specifically on the seven-loss streak and explicitly authorized: **"Ok implement the correction now"**.

This satisfies the prior freeze policy's batch-review / explicit-authorization requirement.

The authorized v0.3.60 revision is narrow:

1. Total Kills Under adds Forward Regime Persistence (FRP) and Next Compulsory Contact Cycle stress-testing;
2. Duration Under adds Fast-Close Robustness (FCR) and a one-disruption stress test;
3. live ML must decompose Resource Lead from Structural / Objective-Schedule / Compulsory-Fight Control;
4. consecutive same-series repeats of a diagnosed failed mechanism require Same-Mechanism Re-certification (SMR);
5. existing underdog +kills fail-closed draft-lock remains unchanged.

Reference review:
`models/lol/reviews/SEVEN_LOSS_STREAK_REGIME_PERSISTENCE_ML_CONTROL_REVIEW_2026-08-16.md`

Rules:
`models/lol/rules/MODEL_RULES_LOL_V0.3.60.md`

## Continued audit policy

1. **Shadow TAKEs remain enabled.**
   - Continue TAKE / PASS / HOLD normally under v0.3.60.
   - Qualified executable shadow TAKEs auto-record at 0.25u simulated stake.
   - Actual exposure remains 0u while official betting is paused.

2. **Freeze resumes at v0.3.60.**
   - Do not create v0.3.61 from an individual next result.
   - Do not add one-off thresholds after a single map.
   - Further analytical changes require explicit user authorization or a later batch-audit decision.

3. **Audit sample segmentation is mandatory.**
   - Preserve all settled historical positions/P&L.
   - v0.3.57 = pre-v0.3.58 sample.
   - v0.3.58 = favorite-handicap-corrected sample.
   - v0.3.59 = post-Duration-correction / pre-v0.3.60 batch-review sample.
   - New positions after this authorization are recorded under v0.3.60.
   - Diagnostic regrades never change historical P/L.

4. **v0.3.60 review fields are mandatory when relevant.**
   - TK Under: record FRP and next compulsory-contact schedule.
   - Duration Under: record FCR / one-disruption stress result.
   - Live ML: record RL / SL / OSC / CFC decomposition when lead quality is decision-critical.
   - Same-series repeated thesis after diagnosed loss: record SMR pass/fail and what materially changed.

5. **Do not globally suppress TAKE frequency.**
   - v0.3.60 adds named analytical gates, not an unwritten safety margin.
   - If the written gates pass, execute TAKE.
   - Recent losses are not themselves vetoes.
   - Favorite -kills FFD/RNE remains active and should not be over-vetoed.

6. **Multiple same-map TAKEs remain enabled across different market families; one TAKE maximum per family.**
   - Core families: ML, Kill Handicap, Total Kills, Duration/Total Time.
   - Once a family has a TAKE, no second line/reprice/opposite side in that family on the same map.
   - Each cross-family position must independently qualify.
   - Correlated positions remain one calibration evidence cluster.

7. **Pregame / immediate post-draft ML-KH-TK restrictions remain unchanged.**
   - No TAKE for ML/KH/TK immediately after draft.
   - Live ML/KH/TK require two synchronized snapshots plus all market gates.

## Seven-loss audit reference

The streak from the v0.3.59 high-water mark consisted of:

- BFX-DNS G2 Under 34.5 — loss;
- BLG-WE G1 Under 28 min — loss;
- SK-FNC G1 SK +7.5 — loss, execution-invalid TAKE;
- SK-FNC G2 Under 21.5 — loss;
- G2-SHFT G1 Under 26.5 — loss;
- DNS-T1A G2 DNS ML — loss;
- DNS-T1A G3 DNS ML — loss.

Do not interpret this as a blanket anti-Under or anti-ML command. The correction targets the diagnosed mechanisms only.

## Live-output rule

The first visible line on every active-map screenshot remains the verdict. No GitHub/Airtable/tool work before the visible verdict.

For finals, settle every open position first.

## Authority

GitHub remains model/rules authority. Airtable remains the canonical map/position/roster ledger.