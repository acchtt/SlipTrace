# Current League of Legends Model

**Canonical namespace:** `models/lol/`

- Active model: **LoL v0.3.54**
- Active rules: `models/lol/rules/MODEL_RULES_LOL_V0.3.54.md`
- Prior deltas: v0.3.53 through v0.3.26 under `models/lol/rules/`
- Mandatory live checklist: `models/lol/procedures/LOL_LIVE_VERDICT_EXECUTION_CHECKLIST_2026-08-10.md`
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
- Latest handoff: `models/lol/CURRENT_LIVE_HANDOFF_2026-08-12.md`
- Portable baseline context: `models/lol/context/lol-v0.3.25/`
- Shared stake policy: `shared/STAKE_POLICY_V2.json`

## Required load order

1. `models/lol/CURRENT_MODEL.md`
2. v0.3.54 through v0.3.26 rule deltas
3. mandatory live checklist
4. latest reviews referenced above
5. item-verification suspension
6. v0.3.25 consolidated rules / probation / calibration handbook
7. live fast path and main betting procedure
8. connected-stack procedure and addenda
9. scoreboard protocol
10. shared stake policy
11. `models/lol/CURRENT_LIVE_HANDOFF_2026-08-12.md` last

Where conflicts exist, **v0.3.54 controls**.

## Operating state

- Official betting remains **paused** until explicit restoration.
- Official probation remains **13/20 settled/completed**, record 7-6, net -0.16425u / -164,250 VND.
- Next official wager after restoration: 14.
- Duration remains official-ineligible through wager 20.
- Default shadow stake: **0.25u**.
- Actual exposure while paused: **0u**.
- Minimum odds: **1.60**.
- Same-game multiple shadow bets are enabled **after live eligibility** when each independently qualifies; correlated positions are grouped as one calibration evidence cluster.
- Pregame and immediate post-draft **ML / Kill Handicap / Total Kills TAKEs are disabled**.
- Airtable is the canonical position/map ledger; GitHub is the model/rules authority.

## Mandatory verdict format

First visible line on active maps:

- `TAKE — [selection] @[odds] — shadow 0.25u; actual 0u.`
- `PASS — [selection/market] @[odds] — 0u.`
- `HOLD — [selection/market] @[odds] — 0u.`

Logging/connectors occur after the live verdict and must not delay it.

# v0.3.54 — Role-Weighted Economy / Terminal Economy Interaction

## 1. Role-Weighted Economy (RWE)

When role-level gold is visible, live ML analysis may not collapse economy to raw team gold alone.

Mandatory fields:

- `RGV` — Role Gold Vector by champion/role pair;
- `GLC` — Gold Leverage Class (`HIGH / MEDIUM / LOW`) based on current champion function, not rigid role labels;
- `GCQ` — Gold Concentration Quality (`A FAVORED / B FAVORED / NEUTRAL-MIXED`).

Near-even team gold is **not** economic neutrality when GCQ is materially asymmetric.

If role-level gold is visible but not parsed, ML TAKE is ineligible. If unavailable, do not invent it; apply an uncertainty penalty.

## 2. Terminal Economy Interaction (TEI)

After 30:00, combine RWE with objective terminality.

A comeback ML against a side with both:

- `HIGH TERMINALITY` objective control (e.g. soul/four dragons, Baron with map access, inhibitor/base access, stacked terminal objectives), and
- favorable GCQ concentrated on HIGH-leverage champions,

receives a major probability downgrade.

Kill lead or superficially near-even raw gold cannot independently override this combination. Require repeated observed proof that those terminal threats are being suppressed; otherwise PASS/HOLD.

## 3. Reference correction

HLE-BRO G1 at 36:09 exposed the deterministic representation bug: BRO's large visible economy advantages on K'Sante/Corki plus four dragons and Baron were more terminal than the raw near-even team-gold summary implied, while HLE's largest economy advantage sat on Vi/utility-side resources.

Reference review: `models/lol/reviews/HLE_BRO_G1_ROLE_WEIGHTED_ECONOMY_REVIEW_2026-08-12.md`.

# v0.3.53 — Aggregate Bias / Market Anchor / Shared-Failure Correction

## 1. Live eligibility

ML, Kill Handicap and Total Kills require at least **two synchronized live snapshots**, preferably >=90 seconds apart, before any TAKE. Pregame and immediate post-draft are analysis-only.

Duration retains its stricter existing clock gates.

## 2. Market + TEAM anchor

Every probability estimate begins with:

- `MKT`: current market anchor, conceptually de-vigged;
- `TEAM`: persistent team-strength / execution prior.

Fearless Draft changes champion mechanisms but does **not** reset TEAM to neutral. Same-series execution evidence persists across maps.

Draft theory alone may not create a large departure from MKT/TEAM. A large disagreement requires repeated live proof.

## 3. Anti-favorite bias guard

Before underdog ML or +kills against a clear favorite, prove with observed live evidence that the favorite's baseline skill/conversion edge is actually being suppressed. Attractive underdog tools or price alone are insufficient.

## 4. Mechanism Independence / Shared-Failure Penalty

Classify major survival/forcing tools as:

- `INDEPENDENT`
- `PARTIALLY COUPLED`
- `COUPLED`

Several champion abilities depending on the same tempo, angle, fog access, first-spell success or economy state count as one shared failure cluster, not several independent answers.

Coupled mechanisms widen favorite blowout tails and reduce underdog +kills/comeback lower bounds.

## 5. Handicap Buffer Retention

When the thesis is "underdog can lose but keep the margin bounded," do not chase a heavily compressed live +H merely because the underdog temporarily leads.

If most protective buffer has disappeared and the favorite's latent skill/range/control edge remains, default PASS unless repeated live evidence proves the wide-margin tail has materially collapsed.

## 6. Structure Substitution — two-sided

Classify structure conversion:

- `MARGIN-COMPRESSING`
- `MARGIN-EXPANDING`
- `MIXED/NEUTRAL`

Structure dominance can compress kill margin when the favorite can close without combat, but can expand it when towers/base pressure forces repeated losing defense.

## 7. Total Kills — RKS + KPW

Retain OKP / FCI / CRR / SRR / BF / CL, and add:

- `RKS` — Return-Kill Suppression;
- `KPW` — Kills Per Realized Window;
- future-window deletion after structure/Baron/inhibitor acceleration.

High BF/SRR means many contact opportunities, not automatically many kills. Strong-team clean 2-0/3-0 fights plus rapid structures can create a low-kill stomp.

## 8. Fade benchmark audit

For each confirmed shadow TAKE, when the opposite-side price is visible, record it in the position notes as a counterfactual fade benchmark. Do not create a second shadow position from the benchmark.

Track model ROI versus fade ROI by market, phase and favorite/underdog direction.

## 9. Change control

Do not promote a new model from one ordinary settled map. Performance-driven promotion requires at least **5 settled positions across at least 3 maps** showing the same mechanism, or a broader aggregate review. Deterministic correctness/state-representation bugs are the exception; v0.3.54 uses this exception.

# Retained v0.3.52 controls

- Terminal Threat Answerability (TTA)
- Execution Burden Gradient (EBG)
- terminal vs non-terminal lead quality
- early-live ML hard veto
- live ML lower-bound buffers
- Comeback Conversion Reserve
- Draft Primacy functional matrix

Under v0.3.54, all of these must also pass MKT/TEAM anchoring, shared-failure testing, and RWE/TEI when applicable.

# Retained Kill Handicap controls

- side-neutral signed kill-margin distribution
- NKB / RFI / KCV
- position-blind repricing
- handicap lower-bound buffers
- map dominance != margin dominance
- Buffer Retention and two-sided Structure Substitution now control when they conflict with older interpretation
- apply RWE/TEI late-game when gold concentration changes fight cleanliness or closing tails

# Retained Total Kills controls

- OKP / FCI / CRR / SRR / BF / CL
- event-window de-duplication
- Contest / Concede / Trade / Delay
- Threat Deterrence GLOBAL / LOCAL / NONE
- quiet-start non-persistence
- Total Kills lower-bound buffers
- v0.3.53 RKS / KPW / window-deletion overlay is mandatory
- apply RWE/TEI late-game when gold concentration changes return-kill probability or closing speed

# Retained Duration controls

- no pregame TAKE
- no TAKE before 12:00
- 12:00-13:59 requires two synchronized snapshots >=90 sec apart showing the same mechanism
- 14:00+ still requires observed stall/acceleration
- reprice after first tower / Baron / inhibitor / major acceleration

# Same-game shadow testing

Multiple same-map shadow positions are allowed after eligibility when each independently qualifies. Correlated positions are separate P/L entries but one calibration cluster. Do not add positions merely to increase sample size.

# Execution / settlement

- A TAKE is conditional/unrecorded until explicit confirmation of the exact same executable line/price.
- Disappeared/locked/deteriorated before confirmation => NO BET / 0u.
- User correction overrides visual scoreboard bugs.
- User statement `Final`, `final score`, or `X won` controls settlement when grading data are sufficient.
- Unconfirmed recommendations are never graded.
- No martingale, rescue or loss chasing.
- Missing decision-critical information => PASS/HOLD.
