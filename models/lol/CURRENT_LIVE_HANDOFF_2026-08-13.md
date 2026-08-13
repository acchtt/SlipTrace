# CURRENT LIVE HANDOFF — 2026-08-13

## Active model

**LoL v0.3.56**

GitHub is model/rules authority. Airtable is canonical map/position ledger.

Official betting remains **paused**. Shadow mode is active.

- Default shadow stake: 0.25u
- Actual exposure: 0u
- Minimum odds: 1.60
- Pregame/immediate post-draft ML/KH/TK TAKEs: disabled
- Live ML/KH/TK: two synchronized live snapshots plus all retained gates
- Shadow TAKEs: auto-record after visible verdict when executable and qualified; no confirmation required
- Duration restrictions unchanged
- Current shadow validation: **6-7, -0.39850u**
- Open shadow positions: none

## Mandatory live output behavior

For every active-map screenshot, the first visible line must be the verdict:

- `TAKE — [selection] @[odds] — shadow 0.25u; actual 0u.`
- `PASS — [selection/market] @[odds] — 0u.`
- `HOLD — [selection/market] @[odds] — 0u.`

Do not delay the visible verdict for Airtable/GitHub/tool work. Logging occurs after the verdict.

## v0.3.56 HARD Draft-Collapse Veto — no exception

Reference rules:
`models/lol/rules/MODEL_RULES_LOL_V0.3.56.md`

Reference review:
`models/lol/reviews/NIP_WBG_G1_DRAFT_COLLAPSE_RISK_REVIEW_2026-08-13.md`

Before every underdog +kills decision, classify:

- MKT/TEAM underdog identity at draft lock;
- DER — Draft Execution Reliability;
- DCR — Draft Collapse Risk: LOW / MEDIUM / HIGH;
- FF — Fallback Floor: STABLE / FRAGILE / ABSENT;
- forcing/shared-failure independence;
- objective-schedule interaction.

### HARD VETO trigger

If the pregame/draft underdog has:

- DCR = HIGH;
- FF = FRAGILE or ABSENT;
- opponent has materially lower execution burden with reliable independent forcing/continuation;
- a meaningful scheduled objective/base-pressure sequence can matter if opponent gains control;

then:

**UNDERDOG +KILLS IS TAKE-INELIGIBLE FOR THE ENTIRE MAP.**

No live exception. Do not override from:

- kill/gold lead or parity;
- objective parity;
- a wider +kills cushion;
- one or multiple return kills;
- two-snapshot eligibility;
- temporary role-gold improvement;
- live odds movement;
- short-term fight success;
- generic resilience language;
- prior v0.3.55 mechanism-proof override.

Only a draft-input correction changing champion identity, role assignment, or the original functional DCR/FF classification can remove the hard veto.

If hard veto ACTIVE, stop the +kills analysis and PASS/HOLD. Do not search for an exception. Favorite -kills still must qualify independently.

## Recent correction history

### KT.C vs NS.EA G1

NS +8.5 @1.943 lost. v0.3.55 promoted DER/shared-failure/RIT enforcement after the model underweighted NS execution burden.

### KT.C vs NS.EA G2

Model correctly identified KT's easier draft and KT rolled the map. KT ML was 2.037 at post-draft odds, but current model did not allow a post-draft TAKE. A possible ML-only post-draft override remains **review-only and NOT active**.

### NIP vs WBG G1

Draft:

NIP:
- Olaf
- Qiyana
- Ryze
- Jhin
- Nautilus

WBG:
- Ambessa
- Naafiri
- Ahri
- Xerath
- Camille support

TEAM anchor leaned NIP.

Correct draft classification in hindsight / v0.3.56:

- NIP: lower DER, LOW DCR, STABLE FF, repeatable forcing/continuation;
- WBG: HIGH DER, HIGH DCR, FRAGILE/ABSENT FF, weak conventional frontline/peel, incompatible dive/poke spacing, clustered-death exposure.

Shadow position:

`LPL-2026-08-13-NIP-WBG-G1-P01`

- WBG +8.5 kills @1.961
- shadow 0.25u
- actual 0u
- entry 15:05
- entry kills: WBG led 5-3
- entry dragons: 1-1
- entry towers: 0-0
- final kill score supplied by user: NIP 22-10 WBG
- result: **LOSS -0.25u**

Correct v0.3.56 verdict at entry would have been:

**PASS — WBG +8.5 kills @1.961 — 0u.**

The error was allowing short-term return-kill evidence to override a fundamentally HIGH-collapse-risk underdog draft.

## Immediate next action

Prepare **NIP vs WBG Game 2** with fresh-map state reset.

Carry forward TEAM/current-series execution evidence, but reset map-state evidence.

Draft must be assessed before live price temptation using:

1. TEAM + MKT anchor;
2. full Draft Function Matrix;
3. DER;
4. DCR;
5. FF;
6. independent forcing / shared-failure clusters;
7. objective-fight execution;
8. carry protection / protected DPS;
9. collapse-tail geometry;
10. market-specific gates.

For any underdog +kills candidate, check HARD DRAFT-COLLAPSE VETO first. If ACTIVE, there is **no exception** for the rest of the map.
