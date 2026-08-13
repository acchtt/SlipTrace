# Current League of Legends Model

**Canonical namespace:** `models/lol/`

- Active model: **LoL v0.3.57**
- Active rules: `models/lol/rules/MODEL_RULES_LOL_V0.3.57.md`
- Prior deltas: v0.3.56 through v0.3.26 under `models/lol/rules/`
- Mandatory fallback certification: `models/lol/procedures/LOL_FALLBACK_FLOOR_CERTIFICATION_2026-08-13.md`
- Mandatory live checklist: `models/lol/procedures/LOL_LIVE_VERDICT_EXECUTION_CHECKLIST_2026-08-10.md`
- Latest fallback-floor review: `models/lol/reviews/NIP_WBG_G3_FALLBACK_FLOOR_MISCLASSIFICATION_REVIEW_2026-08-13.md`
- Prior draft collapse-risk review: `models/lol/reviews/NIP_WBG_G1_DRAFT_COLLAPSE_RISK_REVIEW_2026-08-13.md`
- Prior draft execution-burden review: `models/lol/reviews/KT_NS_G1_DRAFT_EXECUTION_BURDEN_REVIEW_2026-08-13.md`
- Latest role-weighted economy review: `models/lol/reviews/HLE_BRO_G1_ROLE_WEIGHTED_ECONOMY_REVIEW_2026-08-12.md`
- Latest aggregate bias/fade review: `models/lol/reviews/AGGREGATE_ANTI_FAVORITE_FADE_BIAS_REVIEW_2026-08-11.md`
- Latest live-ML terminal-threat review: `models/lol/reviews/SK_VIT_G1_TERMINAL_THREAT_ANSWERABILITY_REVIEW_2026-08-10.md`
- Latest Total Kills recurrence review: `models/lol/reviews/HLE_GGA_G2_UNDER_SKIRMISH_RECURRENCE_REVIEW_2026-08-10.md`
- Prior Total Kills contact-realization review: `models/lol/reviews/FURIA_FLUXO_G2_OVER_CONTACT_REALIZATION_REVIEW_2026-08-10.md`
- Prior Total Kills / add-on correlation review: `models/lol/reviews/KC_FNC_GAME2_TOTAL_KILLS_CORRELATION_REVIEW_2026-08-10.md`
- Latest handicap conversion review: `models/lol/reviews/G2_TH_KILL_HANDICAP_CONVERSION_REVIEW_2026-08-09.md`
- Draft primacy review: `models/lol/reviews/JDG_WE_GAME2_DRAFT_PRIMACY_REVIEW_2026-08-09.md`
- Duration review: `models/lol/reviews/DURATION_MARKET_REBUILD_REVIEW_2026-08-09.md`
- Handicap directional review: `models/lol/reviews/KILL_HANDICAP_DIRECTIONAL_BIAS_REVIEW_2026-08-09.md`
- Latest handoff: `models/lol/CURRENT_LIVE_HANDOFF_2026-08-13.md`
- Portable baseline context: `models/lol/context/lol-v0.3.25/`
- Shared stake policy: `shared/STAKE_POLICY_V2.json`

## Required load order

1. `models/lol/CURRENT_MODEL.md`
2. v0.3.57 through v0.3.26 rule deltas
3. mandatory fallback-floor certification procedure
4. mandatory live checklist
5. latest reviews referenced above
6. item-verification suspension
7. v0.3.25 consolidated rules / probation / calibration handbook
8. live fast path and main betting procedure
9. connected-stack procedure and addenda
10. scoreboard protocol
11. shared stake policy
12. `models/lol/CURRENT_LIVE_HANDOFF_2026-08-13.md` last

Where conflicts exist, **v0.3.57 controls**.

## Operating state

- Official betting remains **paused** until explicit restoration.
- Official probation remains **13/20 settled/completed**, record 7-6, net -0.16425u / -164,250 VND.
- Next official wager after restoration: 14.
- Duration remains official-ineligible through wager 20.
- Default shadow stake: **0.25u**.
- Actual exposure while paused: **0u**.
- Minimum odds: **1.60**.
- Same-game multiple shadow bets are enabled **after live eligibility** when each independently qualifies; correlated positions are grouped as one calibration evidence cluster.
- Pregame and immediate post-draft **ML / Kill Handicap / Total Kills TAKEs remain disabled**. The KT.C-vs-NS.C post-draft ML override idea remains review-only and is not active.
- Live ML / Kill Handicap / Total Kills require the retained **two-snapshot live gate** plus all v0.3.57 gates.
- Shadow TAKEs that are visibly executable and qualify are **auto-recorded after the user-facing verdict**; no placement confirmation is required in shadow mode.
- Airtable is the canonical position/map ledger; GitHub is the model/rules authority.
- Current settled shadow validation after NIP vs WBG G2: **6-8, -0.64850u**.
- Open shadow position: `LPL-2026-08-13-NIP-WBG-G3-P01` — WBG +8.5 kills @1.951, 0.25u shadow, actual 0u; result pending. Under v0.3.57 the entry thesis is process-invalidated but the recorded position is not deleted or retroactively regraded.

## Mandatory verdict format

First visible line on active maps:

- `TAKE — [selection] @[odds] — shadow 0.25u; actual 0u.`
- `PASS — [selection/market] @[odds] — 0u.`
- `HOLD — [selection/market] @[odds] — 0u.`

Logging/connectors occur after the live verdict and must not delay it.

# v0.3.57 — Fallback Floor Certification / False-Stable Guard

## 1. STABLE is no longer a descriptive label

For underdog +kills, `FF = STABLE` is a **positive certification**. It requires matchup-relative PASS results on all four critical tests:

1. `FER` — Failed-Engage Reset;
2. `PDC` — Protected-DPS Continuation;
3. `PST` — Pressured Space: objective entry or base/wave defense while behind;
4. `ARI` — Alternative Route Independence.

Any FAIL or UNRESOLVED blocks STABLE.

## 2. Forcing redundancy and survival redundancy are separate

Mandatory separate scores:

- `FRI` — Forcing Route Independence;
- `SRI` — Survival Route Independence.

Multiple engage, CC, pick, flank or re-engage tools may raise FRI while SRI remains LOW. **Engage count is never fallback proof.**

## 3. False-Stable Guard

STABLE is forbidden when the fallback is materially another version of the same forward-commit plan, when peel competes with initiation, when carry protection disappears during engage, when behind-state objective entry requires the same all-in, or when opponent range/pick/disengage/re-engage can punish failed contact without a demonstrated reset route.

If the guard is ACTIVE, FF is `FRAGILE` or `ABSENT`.

## 4. Fail closed

For underdog +kills:

- incomplete certification => PASS/HOLD;
- ambiguous certification => PASS/HOLD;
- DCR ambiguity between MEDIUM/HIGH is resolved to HIGH when failed contact can expose multiple members and the opponent has at least two repeatable punish/continuation routes;
- ordinary live success cannot upgrade `FRAGILE`, `ABSENT` or `UNCERTIFIED` to STABLE;
- handicap size/odds cannot influence DCR/FF certification.

Only a genuine draft-input correction may reopen certification.

## 5. v0.3.56 hard veto remains controlling after certification

Mandatory order before underdog +kills pricing:

1. MKT + TEAM underdog identity;
2. DER;
3. FRI;
4. SRI;
5. FER;
6. PDC;
7. PST;
8. ARI;
9. False-Stable Guard;
10. DCR;
11. FF certification;
12. v0.3.56 HARD Draft-Collapse Veto;
13. RIT only if veto inactive;
14. signed-margin / NKB / RFI / KCV / Structure Substitution pricing.

If the hard veto is ACTIVE, stop. Do not search for an exception.

## 6. Reference correction — NIP vs WBG G3

WBG: Gnar / Lee Sin / Annie / Mel / Rell.  
NIP: Tristana / Xin Zhao / Twisted Fate / Ashe / Seraphine.

The erroneous v0.3.56 classification credited WBG with STABLE fallback because of multiple engage/peel branches.

Correct v0.3.57 classification for underdog +kills:

- WBG FRI: meaningful;
- WBG SRI: insufficient;
- WBG critical fallback certification: not all PASS;
- False-Stable Guard: ACTIVE;
- WBG DCR: HIGH for handicap eligibility;
- WBG FF: FRAGILE;
- hard draft-collapse veto: ACTIVE.

Therefore WBG +8.5 kills @1.951 at 20:12 was TAKE-ineligible. Correct verdict:

**PASS — WBG +8.5 kills @1.951 — 0u.**

Reference review: `models/lol/reviews/NIP_WBG_G3_FALLBACK_FLOOR_MISCLASSIFICATION_REVIEW_2026-08-13.md`.

# Retained controls

All non-conflicting v0.3.56 and earlier controls remain active, including:

- strict HIGH-DCR + weak-FF underdog +kills hard veto with no live exception;
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

Favorite -kills remains independent. Blocking underdog +kills never creates an automatic reverse bet.
