# Current League of Legends Model

**Canonical namespace:** `models/lol/`

- Active model: **LoL v0.3.58**
- Active rules: `models/lol/rules/MODEL_RULES_LOL_V0.3.58.md`
- Prior deltas: v0.3.57 through v0.3.26 under `models/lol/rules/`
- **Active audit governance:** `models/lol/procedures/LOL_SHADOW_AUDIT_CONTINUATION_2026-08-14.md`
- Prior freeze procedure: `models/lol/procedures/LOL_SHADOW_AUDIT_FREEZE_2026-08-13.md`
- Mandatory fallback certification: `models/lol/procedures/LOL_FALLBACK_FLOOR_CERTIFICATION_2026-08-13.md`
- Mandatory live checklist: `models/lol/procedures/LOL_LIVE_VERDICT_EXECUTION_CHECKLIST_2026-08-10.md`
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
- Duration review: `models/lol/reviews/DURATION_MARKET_REBUILD_REVIEW_2026-08-09.md`
- Handicap directional review: `models/lol/reviews/KILL_HANDICAP_DIRECTIONAL_BIAS_REVIEW_2026-08-09.md`
- Latest handoff: `models/lol/CURRENT_LIVE_HANDOFF_2026-08-14.md`
- Portable baseline context: `models/lol/context/lol-v0.3.25/`
- Shared stake policy: `shared/STAKE_POLICY_V2.json`

## Required load order

1. `models/lol/CURRENT_MODEL.md`
2. `models/lol/procedures/LOL_SHADOW_AUDIT_CONTINUATION_2026-08-14.md`
3. v0.3.58 through v0.3.26 rule deltas
4. mandatory fallback-floor certification procedure
5. mandatory live checklist
6. latest reviews referenced above
7. item-verification suspension
8. v0.3.25 consolidated rules / probation / calibration handbook
9. live fast path and main betting procedure
10. connected-stack procedure and addenda
11. scoreboard protocol
12. shared stake policy
13. `models/lol/CURRENT_LIVE_HANDOFF_2026-08-14.md` last

Where conflicts exist, **v0.3.58 controls analytically and the active audit-continuation policy controls governance**.

## Operating state

- Official betting remains **paused** until explicit restoration.
- Official probation remains **13/20 settled/completed**, record 7-6, net -0.16425u / -164,250 VND.
- Next official wager after restoration: 14.
- Duration remains official-ineligible through wager 20.
- Default shadow stake: **0.25u**.
- Actual exposure while paused: **0u**.
- Minimum odds: **1.60**.
- Same-game multiple shadow bets are enabled **after live eligibility** when each independently qualifies; correlated positions are grouped as one calibration evidence cluster.
- Pregame and immediate post-draft **ML / Kill Handicap / Total Kills TAKEs remain disabled**.
- Live ML / Kill Handicap / Total Kills require the retained **two-snapshot live gate** plus all active gates.
- **Shadow TAKEs remain active and are auto-recorded after the user-facing verdict when visibly executable and qualified.**
- v0.3.57 results remain the pre-revision audit sample. New selections are recorded under v0.3.58 as the post-revision sample.
- The user explicitly authorized the v0.3.58 batch revision on 2026-08-14. **Do not create v0.3.59 or patch v0.3.58 from an individual next map** without further explicit authorization or a later batch-audit decision.
- Airtable is the canonical position/map ledger; GitHub is the model/rules authority.

## Mandatory verdict format

First visible line on active maps:

- `TAKE — [selection] @[odds] — shadow 0.25u; actual 0u.`
- `PASS — [selection/market] @[odds] — 0u.`
- `HOLD — [selection/market] @[odds] — 0u.`

Logging/connectors occur after the live verdict and must not delay it.

# v0.3.58 — Favorite -kills Forced-Fight Density

## 1. Baron / inhibitor requirement removed

For favorite -kills, existing Baron ownership and existing inhibitor destruction are **supporting evidence, not mandatory prerequisites**.

Absence of Baron/inhibitor cannot by itself force PASS/HOLD.

## 2. Forced-Fight Density (FFD)

Before favorite -kills pricing, classify expected remaining **Forced-Fight Density**:

- `LOW`
- `MEDIUM`
- `HIGH`

FFD is HIGH only when multiple scheduled windows are materially difficult for the underdog to avoid and the favorite has reliable access/continuation to translate those windows into net kill-margin expansion.

Mandatory inputs:

1. current signed kill margin;
2. `RNE` — Required Net Expansion to cover the line;
3. Role-Weighted Economy / TEI and lead quality;
4. dragon/Soul schedule;
5. Baron availability or imminent Baron window, without requiring ownership;
6. tower/base-pressure schedule;
7. favorite initiation/access reliability and continuation;
8. underdog ability to cross-map, waveclear, disengage, trade or safely concede;
9. underdog reset/survival under pressured entry;
10. Structure Substitution — whether the favorite can close while deleting the fights needed for the handicap.

## 3. Pre-Baron favorite -kills eligibility

Favorite -kills can qualify before Baron/inhibitor when:

- two-snapshot live gate is satisfied;
- favorite economy/role distribution and lead quality are materially positive;
- FFD = HIGH;
- RNE is supportable by expected remaining fight count and signed-margin distribution;
- NKB / RFI / KCV / Structure Substitution do not negate the cover branch;
- exact executable odds are >=1.60.

This is not an automatic TAKE. Do not infer HIGH FFD from 3–0 dragons, a large gold lead, TEAM edge, strong engage or imminent Baron by itself.

## 4. T1 vs DK G1 reference correction

At 20:27 T1 led 16–8 kills, approximately +5.4k gold, towers 3–1 and dragons 3–0. Baron and inhibitors were still 0–0. T1 -15.5 @1.617 required `RNE = +8` additional net kills.

The Soul + imminent Baron schedule, T1 access/continuation, large economy edge and limited DK ability to avoid future contests created HIGH FFD.

v0.3.58 reference verdict:

**TAKE — T1 -15.5 kills @1.617 — shadow 0.25u; actual 0u.**

Final was T1 30–11 DK. This is a diagnostic regrade only; no historical v0.3.57 P/L is altered.

Reference review: `models/lol/reviews/T1_DK_G1_FAVORITE_HANDICAP_FORCED_FIGHT_DENSITY_REVIEW_2026-08-14.md`.

# v0.3.57 — Fallback Floor Certification / False-Stable Guard

For underdog +kills, `FF = STABLE` remains a positive matchup-relative certification requiring PASS on:

1. `FER` — Failed-Engage Reset;
2. `PDC` — Protected-DPS Continuation;
3. `PST` — Pressured Space;
4. `ARI` — Alternative Route Independence.

Separate `FRI` — Forcing Route Independence from `SRI` — Survival Route Independence. Engage count is never fallback proof.

False-Stable Guard remains active when fallback is another version of the same forward-commit plan, peel competes with initiation, carry protection disappears during engage, behind-state objective entry repeats the same all-in dependency, or opponent range/pick/disengage/re-engage can punish failed contact without a demonstrated reset.

Incomplete or ambiguous certification => PASS/HOLD. Ordinary live events cannot upgrade `FRAGILE`, `ABSENT` or `UNCERTIFIED` to STABLE.

# v0.3.56 — Hard Draft-Collapse Veto

For underdog +kills, after v0.3.57 certification, if:

- DCR = HIGH;
- FF = FRAGILE or ABSENT;
- opponent has materially easier repeat forcing/continuation;
- scheduled objective/base pressure can matter;

then:

**UNDERDOG +KILLS IS TAKE-INELIGIBLE FOR THE ENTIRE MAP. NO LIVE EXCEPTION.**

Favorite -kills remains independent and now uses the v0.3.58 FFD/RNE correction where applicable.

# Retained controls

All non-conflicting v0.3.57 and earlier controls remain active, including:

- DER and shared-failure clusters;
- Draft Correction Trigger;
- objective-schedule x execution burden;
- RIT only when the hard veto is inactive;
- Role-Weighted Economy / TEI;
- two-snapshot live eligibility;
- MKT + TEAM anchoring;
- anti-favorite guard;
- Draft Primacy 14-function matrix;
- TTA / EBG / lead quality;
- side-neutral signed kill-margin distribution;
- NKB / RFI / KCV / Structure Substitution;
- Handicap Buffer Retention;
- OKP / FCI / CRR / SRR / BF / CL / RKS / KPW;
- position-blind reassessment;
- stale-line gate;
- same-game correlation decomposition;
- Duration restrictions;
- no rescue/martingale/loss chasing.

Blocking underdog +kills never creates an automatic reverse favorite -kills TAKE.
