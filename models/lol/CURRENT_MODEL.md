# Current League of Legends Model

**Canonical namespace:** `models/lol/`

- Active model: **LoL v0.3.60**
- Active rules: `models/lol/rules/MODEL_RULES_LOL_V0.3.60.md`
- Prior deltas: v0.3.59 through v0.3.26 under `models/lol/rules/`
- **Active audit governance:** `models/lol/procedures/LOL_SHADOW_AUDIT_CONTINUATION_2026-08-16.md`
- **Mandatory live execution calibration:** `models/lol/procedures/LOL_LIVE_EXECUTION_CALIBRATION_2026-08-15.md`
- **Mandatory compact-output/full-analysis addendum:** `models/lol/procedures/LOL_COMPACT_OUTPUT_FULL_ANALYSIS_RULE_2026-08-15.md`
- **Active no-duplicate multi-TAKE policy:** `models/lol/procedures/LOL_MULTI_TAKE_NO_DUPLICATE_POLICY_2026-08-15.md`
- Mandatory fallback certification: `models/lol/procedures/LOL_FALLBACK_FLOOR_CERTIFICATION_2026-08-13.md`
- Mandatory live checklist: `models/lol/procedures/LOL_LIVE_VERDICT_EXECUTION_CHECKLIST_2026-08-10.md`
- **Latest batch review:** `models/lol/reviews/SEVEN_LOSS_STREAK_REGIME_PERSISTENCE_ML_CONTROL_REVIEW_2026-08-16.md`
- Latest Duration recurrence review: `models/lol/reviews/DURATION_0_0_TOWER_RECURRENCE_REVIEW_2026-08-15.md`
- Latest favorite-handicap review: `models/lol/reviews/T1_DK_G1_FAVORITE_HANDICAP_FORCED_FIGHT_DENSITY_REVIEW_2026-08-14.md`
- Latest fallback-floor review: `models/lol/reviews/NIP_WBG_G3_FALLBACK_FLOOR_MISCLASSIFICATION_REVIEW_2026-08-13.md`
- Prior draft collapse-risk review: `models/lol/reviews/NIP_WBG_G1_DRAFT_COLLAPSE_RISK_REVIEW_2026-08-13.md`
- Prior draft execution-burden review: `models/lol/reviews/KT_NS_G1_DRAFT_EXECUTION_BURDEN_REVIEW_2026-08-13.md`
- Latest role-weighted economy review: `models/lol/reviews/HLE_BRO_G1_ROLE_WEIGHTED_ECONOMY_REVIEW_2026-08-12.md`
- Latest aggregate bias/fade review: `models/lol/reviews/AGGREGATE_ANTI_FAVORITE_FADE_BIAS_REVIEW_2026-08-11.md`
- Latest live-ML terminal-threat review: `models/lol/reviews/SK_VIT_G1_TERMINAL_THREAT_ANSWERABILITY_REVIEW_2026-08-10.md`
- Latest Total Kills recurrence review: `models/lol/reviews/HLE_GGA_G2_UNDER_SKIRMISH_RECURRENCE_REVIEW_2026-08-10.md`
- Prior Total Kills contact-realization review: `models/lol/reviews/FURIA_FLUXO_G2_OVER_CONTACT_REALIZATION_REVIEW_2026-08-10.md`
- Prior Total Kills / add-on correlation review: `models/lol/reviews/KC_FNC_GAME2_TOTAL_KILLS_CORRELATION_REVIEW_2026-08-10.md`
- Prior handicap conversion review: `models/lol/reviews/G2_TH_KILL_HANDICAP_CONVERSION_REVIEW_2026-08-09.md`
- Draft primacy review: `models/lol/reviews/JDG_WE_GAME2_DRAFT_PRIMACY_REVIEW_2026-08-09.md`
- Handicap directional review: `models/lol/reviews/KILL_HANDICAP_DIRECTIONAL_BIAS_REVIEW_2026-08-09.md`
- Latest handoff: `models/lol/CURRENT_LIVE_HANDOFF_2026-08-16.md`
- Portable baseline context: `models/lol/context/lol-v0.3.25/`
- Shared stake policy: `shared/STAKE_POLICY_V2.json`

## Required load order

1. `models/lol/CURRENT_MODEL.md`
2. `models/lol/procedures/LOL_SHADOW_AUDIT_CONTINUATION_2026-08-16.md`
3. `models/lol/procedures/LOL_LIVE_EXECUTION_CALIBRATION_2026-08-15.md`
4. `models/lol/procedures/LOL_COMPACT_OUTPUT_FULL_ANALYSIS_RULE_2026-08-15.md`
5. v0.3.60 through v0.3.26 rule deltas
6. mandatory fallback-floor certification procedure
7. mandatory live checklist
8. latest reviews referenced above, with the 2026-08-16 seven-loss review first
9. item-verification suspension
10. v0.3.25 consolidated rules / probation / calibration handbook
11. live fast path and main betting procedure
12. connected-stack procedure and addenda
13. scoreboard protocol
14. shared stake policy
15. `models/lol/CURRENT_LIVE_HANDOFF_2026-08-16.md` last

Where conflicts exist, **v0.3.60 controls analytically, the active 2026-08-16 audit-continuation policy controls governance, and the live execution calibration controls TAKE/PASS/HOLD posture without adding unwritten gates**.

## Operating state

- Official betting remains **paused** until explicit restoration.
- Official probation remains **13/20 settled/completed**, record 7-6, net -0.16425u / -164,250 VND.
- Next official wager after restoration: 14.
- Duration remains official-ineligible through wager 20.
- Default shadow stake: **0.25u**.
- Actual exposure while paused: **0u**.
- Minimum odds: **1.60**.
- Same-map multiple shadow bets are enabled across different market families when each independently qualifies.
- Maximum one TAKE per map in each core family: **ML / Kill Handicap / Total Kills / Duration**.
- Pregame and immediate post-draft **ML / Kill Handicap / Total Kills TAKEs remain disabled**.
- Live ML / Kill Handicap / Total Kills require the retained **two-snapshot live gate** plus all active gates.
- Shadow TAKEs auto-record after the user-facing verdict when visibly executable and qualified.
- **No unwritten extra safety margin:** when every written gate, veto, re-certification check and pricing requirement passes, execute TAKE.
- HOLD/PASS after eligibility must identify a specific active gate, veto, pricing failure, stale line, no-duplicate rule or correlation reason.
- v0.3.57 remains the pre-v0.3.58 audit sample.
- v0.3.58 remains the favorite-handicap-corrected sample.
- v0.3.59 remains the post-Duration-correction / pre-v0.3.60 batch-review sample.
- New selections are recorded under **v0.3.60**.
- The user explicitly authorized v0.3.60 on 2026-08-16 after a batch review of the seven-loss streak. **Do not create v0.3.61 from an individual next result** without further explicit authorization or later batch review.
- Airtable is canonical position/map/roster ledger; GitHub is model/rules authority.

## Mandatory verdict format

First visible line on active maps:

- `TAKE — [selection] @[odds] — shadow 0.25u; actual 0u.`
- `PASS — [selection/market] @[odds] — 0u.`
- `HOLD — [selection/market] @[odds] — 0u.`

Logging/connectors occur after the live verdict and must not delay it.

# v0.3.60 — Forward Regime Persistence / Control-Lead Correction

Reference review:
`models/lol/reviews/SEVEN_LOSS_STREAK_REGIME_PERSISTENCE_ML_CONTROL_REVIEW_2026-08-16.md`

## A. Total Kills Under — Forward Regime Persistence (FRP)

A quiet current game is not enough for a TK Under.

Retain OKP / FCI / CRR / SRR / BF / CL / RKS / KPW, then classify:

- next compulsory-contact cycle pressure = LOW / MEDIUM / HIGH;
- `FRP = PASS / FAIL / UNCERTAIN`.

Only FRP PASS is TAKE-eligible.

Passive quiet between objectives has reduced evidentiary weight. Suppression of an actual compulsory contact window is materially stronger evidence.

Mandatory question:

**“Why should the next compulsory objective/contact cycle be at least as kill-suppressive as the interval already observed?”**

After a material recurrence burst, a later quiet patch does not restore FRP without mechanism-relevant evidence.

## B. Duration Under — Fast-Close Robustness (FCR)

Retain all v0.3.45 Duration timing/acceleration/persistence/dead-zone/buffer gates and v0.3.59 LCH/conversion controls.

Classify `FCR = ROBUST / FRAGILE / UNCERTAIN`.

Only ROBUST is normally TAKE-eligible outside the retained terminal-state exception.

Mandatory one-disruption question:

**“If the fastest close route suffers one normal disruption, does the Under thesis still remain materially viable?”**

A shortest plausible route is not enough if one ordinary reset/partial conversion/delayed structure breaks the Under.

## C. Live ML — Resource Lead vs Control Lead

Before every live ML TAKE, decompose:

- `RL` — Resource Lead;
- `SL` — Structural Lead;
- `OSC` — Objective-Schedule Control;
- `CFC` — Compulsory Fight Control.

Mandatory question:

**“If the next two major compulsory fights begin from approximately neutral setup, which side has the easier first contact, re-engage, carry access and reset?”**

A candidate can be richer without controlling the next fights. A resource lead with little/no structural separation must be discounted when the opponent owns materially easier first contact/re-engage.

If RL is positive but CFC materially favors the opponent and independent control evidence is absent, ML is PASS/HOLD.

## D. Same-Mechanism Re-certification (SMR)

A previous loss is never a blanket veto.

But once a same-series loss has a diagnosed mechanism, a later TAKE relying on the same structural thesis must explicitly re-certify that mechanism.

Material re-certification can come from a changed draft, changed first-contact relationship, stronger structural control, changed objective schedule, demonstrated answer to the prior forcing route, or materially different price after the failed branch is included.

Repeating a similar +1k lead / low-kill state / 0-0 tower state is not enough.

If the prior mechanism remains active and the new TAKE depends on the same assumption, SMR fails.

## E. No blanket conservatism

v0.3.60 is not a command to avoid Unders, ML, or repeated series positions.

It adds named gates. If they pass alongside all retained gates at qualifying executable odds, default verdict remains TAKE.

Favorite -kills FFD/RNE remains fully active; the seven-loss streak contained no favorite -kills loss.

# v0.3.59 retained — Duration 0-0 Tower Neutralization / LCH

- 0-0 towers/no first tower = neutral by default.
- Distinguish `ABSENT CONVERSION` from `FAILED CONVERSION`.
- Only FAILED CONVERSION can satisfy the structure-related stall component of a Duration Over.
- LCH LOW/MEDIUM/HIGH mandatory before Duration Over.
- If LCH HIGH, Over is TAKE-ineligible unless high-leverage conversion has already failed after LCH became high and two independent stall mechanisms plus survival/dead-zone gates still pass.
- Ask: **“What happens if the next compulsory fight is lost?”**
- HIGH LCH does not automatically create an Under.

# v0.3.58 retained — Favorite -kills Forced-Fight Density

- Baron ownership and inhibitor destruction are supporting evidence, not prerequisites.
- Compute exact signed margin and RNE.
- Classify FFD LOW/MEDIUM/HIGH.
- Pre-Baron favorite -kills can qualify when FFD HIGH, RNE supportable and NKB/RFI/KCV/Structure Substitution do not negate the cover branch.
- Do not infer FFD HIGH from a large lead/3-0 dragons/strong engage alone.

# v0.3.57 / v0.3.56 retained — Underdog +kills

Underdog +kills requires draft-time positive certification:

1. FER PASS
2. PDC PASS
3. PST PASS
4. ARI PASS
5. False-Stable Guard INACTIVE
6. FF STABLE
7. hard Draft-Collapse Veto INACTIVE

Ordinary live evidence cannot upgrade an uncertified fallback. Missing/ambiguous certification = TAKE-INELIGIBLE for the map unless the underlying draft input itself is corrected.

SK +7.5 vs FNC G1 remains the reference execution-invalid TAKE; correct historical verdict was PASS.

# Retained controls

All non-conflicting v0.3.59 and earlier controls remain active, including:

- DER / shared-failure clusters;
- Draft Correction Trigger;
- objective-schedule x execution burden;
- RIT only when hard veto inactive;
- Role-Weighted Economy / TEI;
- two-snapshot live eligibility;
- MKT + TEAM anchoring;
- anti-favorite guard;
- Draft Primacy 14-function matrix;
- TTA / EBG / lead quality;
- side-neutral signed kill-margin distribution;
- exact kill-handicap arithmetic;
- NKB / RFI / KCV / Structure Substitution;
- Handicap Buffer Retention;
- OKP / FCI / CRR / SRR / BF / CL / RKS / KPW;
- position-blind reassessment;
- stale-line/greyed-market gate;
- same-game correlation decomposition;
- one TAKE maximum per market family per map;
- no rescue/martingale/loss chasing.

Blocking one market or side never creates an automatic reverse TAKE.