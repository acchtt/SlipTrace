# MODEL RULES — LEAGUE OF LEGENDS v0.3.50

**Status:** Active delta  
**Effective date:** 2026-08-10 02:36 UTC+7  
**Supersedes:** v0.3.49 only where stated

## Purpose

Correct the Total Kills Over error exposed by FURIA vs Fluxo W7M Game 2.

Confirmed position under v0.3.49:

- Over 24.5 total kills @1.705 — LOSS (-0.25u)

Final: FURIA 14-3 Fluxo W7M at 32:53, 17 total kills.

Review: `models/lol/reviews/FURIA_FLUXO_G2_OVER_CONTACT_REALIZATION_REVIEW_2026-08-10.md`.

The central correction is:

> **Fight tools create conditional lethality, not guaranteed fights. Total Kills must price whether each nominal contact window is actually realized before pricing how lethal that contact will be.**

v0.3.49 OKP / FCI / CL, v0.3.48 Kill Handicap conversion controls, v0.3.47 Draft Primacy, v0.3.45 Duration, v0.3.44 signed-margin symmetry and all retained execution controls remain active unless superseded below.

---

## 1. Contact Realization Rate (CRR) Is Mandatory

Every Total Kills evaluation must now model four separate layers:

1. **Observed Kill Pace (OKP)** — what has happened;
2. **Forward Contact Inventory (FCI)** — which future event windows may create contact;
3. **Contact Realization Rate (CRR)** — probability each nominal window actually becomes meaningful combat;
4. **Contact Lethality (CL)** — expected death production conditional on realized contact.

A nominal fight window with high CL but low CRR is not a strong Over mechanism.

A useful internal decomposition is:

`Expected remaining kills = sum over windows [ P(contact_i) * E(kills_i | contact_i) ] + residual pick/chase kills`.

This is a discipline rule, not a requirement to manufacture false precision. Use ranges and lower bounds where uncertainty is material.

---

## 2. Count Event Windows, Not Engage Champions

Multiple engage champions participating in the same objective setup are **not independent FCI entries**.

Examples:

- Jarvan + Galio + Volibear around one dragon = one dragon contact window with strong forcing/lethality, not three future fights;
- Nautilus + Annie + Gnar around Baron = one Baron setup unless there are distinct reset/re-engage cycles;
- Ahri + Xin + Ambessa threatening one side-lane collapse = one collapse branch unless the map state supports repeatable independent pick cycles.

### FCI de-duplication rule

Before assigning FCI, group tools by the event they can influence.

Only count separate windows when they are temporally or strategically distinct, such as:

- first dragon contest;
- later soul-point contest;
- Baron setup;
- inhibitor defense;
- a repeat-pick cycle after reset;
- terminal base defense.

Champion-level forcing raises **CRR and/or CL of a window**. It does not multiply the number of windows by itself.

---

## 3. Contact Realization Classification

For every meaningful FCI window, classify CRR:

- `HIGH REALIZATION` — meaningful combat is difficult to avoid;
- `MEDIUM REALIZATION` — both contest and concession/trade are plausible;
- `LOW REALIZATION` — objective/pressure is likely to resolve through concession, trade, zoning or delay;
- `CONDITIONAL / STATE-DEPENDENT` — realization depends on a specific prior event such as soul point, Baron spawn, inhibitor exposure or a gold threshold.

CRR must be based on **incentives and geometry**, not merely champion engage availability.

Relevant inputs:

- objective value and whether conceding is terminal or tolerable;
- cross-map trade options;
- side-lane pressure;
- wave state;
- vision control;
- mobility/global response;
- base-state / inhibitor pressure;
- scaling incentives;
- current gold and item concentration;
- whether the trailing team can delay to a later, better fight;
- whether the leader can force contact without the opponent voluntarily entering range.

---

## 4. Contest / Concede / Trade / Delay Tree

Every major objective or pressure window must have an explicit four-branch test:

1. `CONTEST` — both teams enter meaningful combat;
2. `CONCEDE` — weaker side gives the resource and preserves lives;
3. `TRADE` — weaker side takes cross-map farm/structure/objective instead of fighting;
4. `DELAY` — weaker side clears, pokes, resets or waits for a later window.

Do not label a dragon, Baron or inhibitor as `FORCED / HIGH-CONTACT` unless the `CONTEST` branch materially dominates the other branches.

### Contest Compulsion refinement

v0.3.49 Contest Compulsion remains active, but it is now triggered only when concession/trade/delay branches have become strategically unacceptable or mechanically unavailable.

Strong examples:

- soul itself, not merely first or second dragon;
- Baron when base will otherwise collapse and no cross-map trade exists;
- inhibitor/Nexus defense;
- Elder;
- terminal vision choke where retreat loses the map immediately.

Being behind is **not** sufficient to activate Contest Compulsion.

---

## 5. Threat Deterrence / Contact Suppression

Reliable engage can **reduce** realized combat when its threat makes the opponent leave terrain before contact.

Flag **Threat Deterrence (TD)** when the stronger side has enough access/zone control that the weaker side rationally retreats rather than entering a fight.

Common TD structures:

- Jarvan/Galio or similar layered engage protecting a ranged siege shell;
- Caitlyn traps + long-range control around objective chokes;
- strong poke plus hard engage that makes face-checking impossible;
- Baron-empowered siege where the defender cannot safely step forward;
- side-lane pressure forcing retreat before 5v5 contact occurs.

When TD is active:

- reduce CRR for non-terminal objective windows;
- increase Structure Substitution probability;
- do not automatically reduce CL conditional on contact — contact can still be lethal if it happens;
- recognize that a stronger draft can lower Total Kills by winning space without fighting.

This is the Total Kills analogue of v0.3.48 Structure Substitution.

---

## 6. Mutual-Contact Requirement for Overs

Before a pregame or early-live Over TAKE, answer both:

1. **Can Team A force contact if Team B enters the zone?**
2. **Can Team A force Team B to enter the zone?**

The first question measures access/lethality. The second measures realization.

If the answer to (1) is yes but (2) is uncertain, do not treat the window as high-contact.

### One-sided domination caution

When one side has a material draft/map-control edge, Overs need an explicit mechanism for loser deaths **and/or** loser return kills that does not depend on repeated voluntary contests.

Valid mechanisms include:

- repeatable picks in neutral territory;
- unavoidable dives;
- base-defense fights;
- chase/cleanup after structure breaks;
- compulsory soul/Baron/Elder contests;
- high-frequency skirmish pattern already observed live.

Without such a mechanism, strong favorite control can be Under-friendly even with high conditional CL.

---

## 7. Return-Kill Floor Must Be Functional

Do not credit aggressive champions as automatic return-kill production.

For the trailing side, evaluate whether return kills remain functional after opponent-counter testing:

- can they enter range without being zoned/chunked first?;
- can they survive first contact long enough to return damage?;
- do they have target access after peel/disengage?;
- can they continue damage after the first spell cycle?;
- can they prevent the leader from resetting after a pick?;
- does economic asymmetry remove the nominal counterplay?

Set loser return-kill floor:

- `LOW`;
- `MEDIUM`;
- `HIGH`.

A low loser return-kill floor materially weakens Overs even if favorite kill production is strong.

---

## 8. CRR-Weighted Total Kills Projection

Replace the v0.3.49 projection shortcut with:

`Final Total Kills = Current Kills + CRR-weighted kills from remaining FCI windows + residual pick/chase kills`.

For each material window record internally:

- event/window;
- CRR class;
- contest/concede/trade/delay branches;
- CL conditional on contact;
- expected winner/loser death split;
- whether Threat Deterrence or Structure Substitution can resolve the window without combat.

Then produce low / central / high final-kill branches and line-cross probability.

---

## 9. Over-Specific Vetoes and Surcharge

### Engage-only Over veto

A pregame or early-live Over cannot be TAKEN primarily because both drafts contain many engage or skirmish champions.

If the thesis is essentially `many engage tools => many fights`, PASS.

### Control-dominance Over surcharge

For a pregame or early-live Over, add **+2pp** to the normal Total Kills lower-bound requirement when all are true:

- one side has a material draft/team-strength control edge;
- that side can secure objectives/structures through zoning, siege or side-lane pressure;
- at least two major future windows are `MEDIUM` or `LOW` CRR because concession/trade remains viable;
- loser return-kill floor is not clearly HIGH.

The total required cushion remains capped at **+9pp over break-even**.

### Contact-realization veto

If fewer than two future windows are `HIGH REALIZATION` and no repeatable neutral-pick/dive mechanism exists, a pregame Over defaults to PASS unless the line is sufficiently low that the lower-bound probability still clears all gates after explicit CRR weighting.

---

## 10. Under Interpretation

Do not overcorrect toward Unders.

High Threat Deterrence or low CRR supports Under only if:

- the map has enough structure/objective conversion to end without creating later compulsory contests;
- the trailer cannot generate repeatable picks or return-kill skirmishes;
- base-defense contact is unlikely to erase the Under cushion.

v0.3.49 quiet-start non-persistence and hard-access Under surcharge remain active.

---

## 11. FURIA vs Fluxo W7M G2 Calibration

Draft:

FURIA Volibear / Jarvan IV / Galio / Caitlyn / Karma  
Fluxo W7M Ambessa / Xin Zhao / Ahri / Lucian / Milio

Pregame Over 24.5 @1.705 lost. Final was FURIA 14-3 at 32:53, 17 kills.

The old read correctly identified:

- FURIA draft edge;
- strong conditional first contact;
- medium/high lethality if fights occurred.

It incorrectly inferred:

- too many independent FCI windows from multiple engage champions;
- too much Contest Compulsion;
- too high a Fluxo return-kill floor;
- too little concession/trade/zoning probability;
- too little Threat Deterrence from FURIA's engage + Caitlyn/Karma control shell.

Correct v0.3.50 interpretation:

- FCI: medium/high nominal;
- CRR: medium/uncertain;
- CL conditional on contact: medium/high;
- TD / Structure Substitution: material;
- Fluxo return-kill floor: uncertain low-to-medium;
- pregame Over 24.5 @1.705: **PASS**.

---

## 12. Mandatory Total Kills Internals — v0.3.50

Before every Total Kills TAKE, lock:

1. current kills / exact line / line-cross arithmetic;
2. OKP;
3. de-duplicated FCI event list;
4. CRR classification for every material window;
5. Contest / Concede / Trade / Delay tree;
6. Contest Compulsion status and why concession is no longer viable if active;
7. Threat Deterrence / Structure Substitution status;
8. CL conditional on realized contact;
9. winner kill-production mechanism;
10. loser return-kill floor;
11. CRR-weighted low / central / high final-kill branches;
12. break-even and lower-bound probability after all surcharges.

Missing CRR on a material window => widen uncertainty and PASS/HOLD.

---

## 13. Live Confirmation Upgrade

For live Total Kills, synchronized evidence can materially improve CRR estimation.

Across >=2 snapshots, record whether nominal windows actually resolve through:

- fights;
- picks;
- concessions;
- cross-map trades;
- zoning/structure takes;
- repeated disengages.

Observed **contact realization** can upgrade or downgrade a totals thesis independently from observed kill pace.

Examples:

- repeated objective concessions despite high engage inventory => lower CRR, Under-positive;
- repeated forced contests even at low current kill count => higher CRR, Over-positive;
- frequent contact but 0-1 deaths due functioning disengage => high CRR / low CL;
- rare contact but 3-4 deaths whenever contact occurs => low CRR / high CL.

Do not collapse these patterns into one generic pace variable.

---

## 14. Review Window

For the next **10 settled v0.3.50+ Total Kills positions**, record:

- entry clock;
- line and odds;
- OKP;
- FCI event count after de-duplication;
- CRR by material window;
- Contest/Concede/Trade/Delay branches;
- Contest Compulsion;
- Threat Deterrence;
- CL;
- loser return-kill floor;
- low/central/high final-kill projection;
- final total kills;
- realized number of meaningful contact windows;
- number of nominal windows resolved without combat;
- result / ROI.

Audit specifically for:

- engage-source inflation;
- excessive Contest Compulsion;
- underpriced concession/trade branches;
- overstated loser return kills;
- favorite dominance incorrectly treated as Over-positive;
- CRR and CL being conflated.

---

## 15. Retained Controls

- Draft remains the most important post-lock conditional mechanism layer.
- Total Kills now uses **OKP + de-duplicated FCI + CRR + CL**.
- Base Total Kills lower-bound gates remain +5pp pregame, +4pp early live, +3pp mid/late, with applicable v0.3.49/v0.3.50 surcharges capped at +9pp over break-even.
- v0.3.48 Kill Handicap KCV / Structure Substitution / NKB / RFI remains active.
- v0.3.44 signed-margin symmetry and handicap surcharges remain active.
- Duration remains live-only under v0.3.45.
- Minimum odds remain 1.60.
- Default shadow stake remains 0.25u; actual exposure remains 0u while official betting is paused.
- Same-map add-ons remain enabled only when each independently qualifies and joint correlation is explicitly priced.
- No martingale, rescue, loss chasing or stake escalation.
- Missing decision-critical state => PASS/HOLD.

Where this delta conflicts with v0.3.49 Total Kills interpretation, **v0.3.50 controls**.
