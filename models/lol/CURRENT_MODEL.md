# Current League of Legends Model

**Canonical namespace:** `models/lol/`

- Active model: **LoL v0.3.56**
- Active rules: `models/lol/rules/MODEL_RULES_LOL_V0.3.56.md`
- Prior deltas: v0.3.55 through v0.3.26 under `models/lol/rules/`
- Mandatory live checklist: `models/lol/procedures/LOL_LIVE_VERDICT_EXECUTION_CHECKLIST_2026-08-10.md`
- Latest draft collapse-risk review: `models/lol/reviews/NIP_WBG_G1_DRAFT_COLLAPSE_RISK_REVIEW_2026-08-13.md`
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
2. v0.3.56 through v0.3.26 rule deltas
3. mandatory live checklist
4. latest reviews referenced above
5. item-verification suspension
6. v0.3.25 consolidated rules / probation / calibration handbook
7. live fast path and main betting procedure
8. connected-stack procedure and addenda
9. scoreboard protocol
10. shared stake policy
11. `models/lol/CURRENT_LIVE_HANDOFF_2026-08-13.md` last

Where conflicts exist, **v0.3.56 controls**.

## Operating state

- Official betting remains **paused** until explicit restoration.
- Official probation remains **13/20 settled/completed**, record 7-6, net -0.16425u / -164,250 VND.
- Next official wager after restoration: 14.
- Duration remains official-ineligible through wager 20.
- Default shadow stake: **0.25u**.
- Actual exposure while paused: **0u**.
- Minimum odds: **1.60**.
- Same-game multiple shadow bets are enabled **after live eligibility** when each independently qualifies; correlated positions are grouped as one calibration evidence cluster.
- Pregame and immediate post-draft **ML / Kill Handicap / Total Kills TAKEs remain disabled**. The KT.C-vs-NS.C post-draft ML override idea is review-only and is **not an active exception**.
- Live ML / Kill Handicap / Total Kills require the retained **two-snapshot live gate** plus all v0.3.56 gates.
- Shadow TAKEs that are visibly executable and qualify are **auto-recorded after the user-facing verdict**; no placement confirmation is required in shadow mode.
- Airtable is the canonical position/map ledger; GitHub is the model/rules authority.
- Current shadow validation after NIP vs WBG G1: **6-7, -0.39850u**; open shadow positions: none.

## Mandatory verdict format

First visible line on active maps:

- `TAKE — [selection] @[odds] — shadow 0.25u; actual 0u.`
- `PASS — [selection/market] @[odds] — 0u.`
- `HOLD — [selection/market] @[odds] — 0u.`

Logging/connectors occur after the live verdict and must not delay it.

# v0.3.56 — HARD Draft Collapse Risk / Fallback Floor Veto

## 1. Draft remains primary after lock

Retain v0.3.55 DER/shared-failure enforcement and the v0.3.47 Draft Function Matrix. TEAM/MKT remains the pre-draft strength anchor; draft controls the post-lock mechanism and conversion layer.

Before any live ML / KH / TK TAKE, classify:

- `DER` — Draft Execution Reliability: LOW / MEDIUM / HIGH burden;
- `DCR` — Draft Collapse Risk: LOW / MEDIUM / HIGH;
- `FF` — Fallback Floor: STABLE / FRAGILE / ABSENT.

## 2. Draft Collapse Risk (DCR)

DCR measures the chance that losing first contact or map control produces clustered deaths / repeated forced defenses rather than a bounded loss.

Mandatory checks:

- frontline durability;
- disengage after failed engage;
- protected sustained DPS;
- objective entry without perfect setup;
- waveclear/base defense while behind;
- whether a failed engage exposes one champion or several;
- reset/re-form ability after first spell cycle;
- incompatible spacing requirements between poke/dive/pick/front-to-back plans;
- opponent repeat forcing into the same shared-failure cluster;
- scheduled dragon/Baron/base-pressure interaction.

## 3. Fallback Floor (FF)

`STABLE` = repeatable lower-variance fallback survives opponent-route testing.  
`FRAGILE` = fallback exists only under narrow setup/spacing/tempo conditions.  
`ABSENT` = no credible repeatable fallback once preferred plan fails.

Generic labels such as waveclear, poke, peel, scaling or pick do not count unless matchup-functional.

## 4. HARD DRAFT-COLLAPSE VETO — NO LIVE EXCEPTION

For **underdog +kills**, activate the hard veto when all are true at draft lock / first complete post-draft assessment:

1. side is underdog by pregame/draft `MKT + TEAM` anchor;
2. `DCR = HIGH`;
3. `FF = FRAGILE` or `ABSENT`;
4. opponent has materially lower execution burden and either two independent forcing routes or one highly reliable route plus strong continuation/re-engage;
5. at least one meaningful scheduled objective/base-pressure sequence is expected to matter if the opponent gains control.

When active:

**UNDERDOG +KILLS IS TAKE-INELIGIBLE FOR THE ENTIRE MAP.**

Do not search for an exception.

The hard veto cannot be removed or softened by:

- current kill lead/parity;
- current gold lead/parity;
- tower/dragon parity;
- widened +kills cushion;
- one or multiple return kills;
- two-snapshot eligibility;
- temporary role-gold improvement;
- live odds movement;
- short-term fight success;
- `resilience proven` language;
- mechanism-valid live proof that would previously have downgraded a v0.3.55 draft-burden veto.

**v0.3.56 supersedes the v0.3.55 live-proof override for HIGH DCR + FRAGILE/ABSENT FF underdog +kills cases.**

The only permitted removal is a **draft-input correction** that changes champion identity, role assignment, or the original matchup-functional DCR/FF classification. Ordinary live events never remove it.

## 5. Market temptation cannot change DCR/FF

Classify DCR/FF before using the displayed handicap as evidence. A large +8.5/+10.5/+12.5 line is arithmetic, not a resilience mechanism.

If DCR/FF was not completed before an underdog +kills candidate is evaluated: **PASS/HOLD**.

## 6. RIT only runs when hard veto is inactive

Retain v0.3.55 Resilience Independence Test, but only after checking the hard veto.

Order:

1. MKT/TEAM underdog identity;
2. DER;
3. DCR;
4. FF;
5. shared-failure / forcing independence;
6. objective schedule interaction;
7. HARD DRAFT-COLLAPSE VETO ACTIVE/INACTIVE;
8. if INACTIVE, run RIT;
9. only then price signed margin / NKB / RFI / KCV / Structure Substitution.

If hard veto is ACTIVE, stop. Verdict is PASS/HOLD for that underdog +kills market.

## 7. Favorite -kills remains independent

A blocked underdog +kills bet does not automatically qualify favorite -kills. Favorite handicap must independently clear the retained signed-margin distribution, NKB, RFI, KCV, Structure Substitution and probability gates.

## 8. ML / Total Kills / Duration

- ML: DCR/FF materially affects conversion probability but is not itself a hard ML veto; all retained MKT/TEAM/live/RWE/TEI gates apply.
- TK: HIGH DCR raises clustered-death tails only conditional on contact; CRR/RKS/KPW/Structure Substitution still control. Do not infer Over from collapse risk alone.
- Duration: retained clock/stall/acceleration/dead-zone restrictions remain unchanged.

## 9. Reference correction — NIP vs WBG G1

NIP: Olaf / Qiyana / Ryze / Jhin / Nautilus.  
WBG: Ambessa / Naafiri / Ahri / Xerath / Camille support.

Correct classification:

- NIP: lower DER, LOW DCR, STABLE FF, repeatable independent forcing/continuation.
- WBG: HIGH DER, HIGH DCR, FRAGILE/ABSENT FF, weak conventional frontline/peel, incompatible dive/poke spacing, clustered-death exposure after failed contact.

At 15:05 WBG led 5-3 and WBG +8.5 @1.961 was visible. Under v0.3.56 the hard veto was already active, so the only valid verdict was:

**PASS — WBG +8.5 kills @1.961 — 0u.**

Final user-supplied kill score: NIP 22-10 WBG.

Reference review: `models/lol/reviews/NIP_WBG_G1_DRAFT_COLLAPSE_RISK_REVIEW_2026-08-13.md`.

# Retained v0.3.55 and earlier controls

All non-conflicting controls remain active, including:

- DER and shared-failure clusters;
- Draft Correction Trigger;
- objective-schedule x execution burden;
- RIT when hard veto inactive;
- scoreboard parity is not mechanism proof;
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

Where any earlier language permits live evidence to override a HIGH-DCR/weak-FF underdog +kills veto, **v0.3.56 controls: no exception.**
