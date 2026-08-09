# FURIA vs Fluxo W7M Game 2 — Total Kills Contact-Realization Review

**Date:** 2026-08-10  
**Model at entry:** LoL v0.3.49  
**Market:** Over 24.5 total kills @1.705  
**Stake:** 0.25u shadow / 0u actual  
**Result:** LOSS (-0.25u)

## Final

FURIA 14-3 Fluxo W7M at 32:53.  
Final total kills: 17.

Draft:

- FURIA: Volibear / Jarvan IV / Galio / Caitlyn / Karma
- Fluxo W7M: Ambessa / Xin Zhao / Ahri / Lucian / Milio

## Entry thesis

The v0.3.49 read correctly identified a material FURIA draft/control edge and substantial hard-access capability on both teams. The Total Kills error was translating that engage inventory into too many future realized fights.

The recommendation treated Volibear, Jarvan, Galio, Ambessa, Xin Zhao and Ahri as multiple fight-creation channels and inferred high Forward Contact Inventory plus medium/high Contact Lethality.

That was not sufficient.

## Primary error — engage-source inflation

Champion-level engage tools are not independent map-level contact windows.

A single dragon setup can contain several champions capable of engaging while still producing:

- one fight;
- a short pick;
- a disengage;
- a cross-map trade;
- or no combat because the weaker side concedes.

The model effectively counted several tools contributing to the same possible event as if they created several independent future fight opportunities.

## Missing variable — Contact Realization Rate

v0.3.49 modeled:

- Observed Kill Pace (OKP);
- Forward Contact Inventory (FCI);
- Contact Lethality (CL).

It did not explicitly model the probability that each nominal contact window would actually become combat.

That missing layer is **Contact Realization Rate (CRR)**.

For every future window, the model must ask:

> If this window exists, what is the probability both teams actually enter meaningful combat before the window resolves?

A nominal dragon, Baron, Herald, side-lane collapse or base-defense window is not a realized fight until contest incentives, pathing, tradeability and control geometry are considered.

## Contact refusal / concession

Fluxo could lose map resources without repeatedly accepting FURIA's preferred engagement geometry.

A trailing team can:

- concede an objective;
- trade cross-map structures/camps;
- clear waves and retreat;
- give vision space;
- delay until a later objective;
- abandon a doomed side of the map.

Contest Compulsion is therefore conditional, not automatic. The option to concede narrows as the map approaches soul, Baron, inhibitors and terminal base pressure, but it does not disappear at every objective.

## Threat deterrence

FURIA's draft had a second mechanism the Over thesis underweighted: **threat can suppress contact**.

Jarvan/Galio/Volibear access plus Caitlyn/Karma range and zone control can make a weaker team leave terrain before initiation occurs. Strong engage is therefore not always kill-positive. It can convert into:

- uncontested objective control;
- zoning;
- tower damage;
- vision denial;
- safe structure progression.

This is **Threat Deterrence / Structure Substitution for Total Kills**.

## Return-kill overestimate

The Over also assumed meaningful Fluxo return-kill production because Ambessa/Xin/Ahri/Lucian could access FURIA carries.

That was too generous. Return-kill capability must be tested against:

- who controls first contact;
- whether the losing side can enter range without being chunked or zoned;
- peel and counter-engage;
- whether the leader can reset after the first target;
- live economic asymmetry.

The final 14-3 score shows the loser-death / return-kill branch was much more one-sided than projected.

## Correct pregame interpretation

The draft should have been classified:

- FURIA map-control/draft edge: material;
- nominal FCI: medium/high;
- CRR: uncertain/medium because many windows were concede/tradeable;
- CL conditional on realized contact: medium/high;
- Threat Deterrence / Structure Substitution: material;
- Fluxo return-kill floor: uncertain/low-to-medium.

At Over 24.5 @1.705, break-even was 58.65%. The model's quoted 65-72% range was overconfident and not supported by realized-contact evidence.

Correct v0.3.50 interpretation: **PASS pregame Over 24.5 unless the CRR-weighted kill projection clears the applicable lower-bound gate after concession and threat-deterrence branches.**

## Calibration lessons

1. Count **event windows**, not engage champions.
2. Add **Contact Realization Rate (CRR)** between FCI and CL.
3. Explicitly model `CONTEST / CONCEDE / TRADE / DELAY` for every major window.
4. Strong engage and zone control can be **fight-deterrent** and structure-positive.
5. Contest Compulsion must be proven by objective state; do not activate it merely because one team is behind.
6. For Overs, distinguish `can force if opponent enters` from `can force opponent to enter`.
7. Return kills require functional access under the actual control geometry, not merely aggressive champions.
8. Pregame Overs need stricter evidence when one side can dominate objectives/structures without mutual combat.

## Model action

Promote these corrections into LoL v0.3.50. Preserve v0.3.49 OKP/FCI/CL and v0.3.48 handicap-conversion controls, but insert CRR and concession/threat-deterrence analysis into every Total Kills projection.
