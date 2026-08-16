# JDG vs LGD Game 1 — v0.3.60 Live ML Application Review

**Date:** 2026-08-16 UTC+7  
**Model:** LoL v0.3.60  
**Position:** LGD ML @4.773, shadow 0.25u  
**Result:** LOSS -0.25u shadow, actual 0u  
**Final:** JDG win, 35:25, kills 14-13, towers 9-2, dragons 2-2, Barons 2-0, inhibitors 2-0

## Review conclusion

**Diagnostic classification: execution/application error under the existing v0.3.60 + retained anti-favorite controls.**

Correct historical verdict at 8:23 should have been:

`PASS — LGD ML @4.773 — 0u.`

Historical ledger P/L remains unchanged.

This review does **not** authorize or require v0.3.61. The active stack already contained the relevant controls; they were misapplied.

## Entry state

Draft:

- JDG: Rumble / Jarvan IV / Syndra / Ezreal / Karma
- LGD: Ambessa / Skarner / Ryze / Lucian / Milio

Draft assessment before live play: slight JDG.

Post-draft market:

- JDG 1.477
- LGD 2.543

Approximate no-vig LGD market probability: 36.7%.

First live snapshot, 5:13:

- kills 0-0
- JDG about +1.0k gold
- towers 0-0
- dragons 0-0
- ML JDG 1.316 / LGD 3.222

Entry snapshot, 8:23:

- JDG 3-2 LGD
- JDG about +1.2k gold
- towers 0-0
- dragons 0-0
- ML JDG 1.162 / LGD 4.773

Approximate no-vig LGD market probability at entry: 19.6%.

The TAKE rationale treated the expanded LGD price plus Skarner/Ambessa fight access as enough to price LGD above the market.

## 1. v0.3.60 RL / SL / OSC / CFC decomposition was misapplied

At entry:

- `RL`: **JDG positive** — about +1.2k and +1 kill.
- `SL`: **neutral** — 0-0 towers.
- `OSC`: **neutral on scoreboard**, but draft setup quality leaned JDG because their range/zone package could control neutral-objective approach.
- `CFC`: should have been classified **JDG-favored or at minimum not LGD-favored**.

The live verdict over-weighted LGD's obvious hard-start buttons. v0.3.60 CFC is not merely “who can engage first.” It also requires survival of first exchange, re-engage, protected DPS continuation, reset/disengage, target access, and objective-turn control.

JDG had:

- Jarvan first contact and peel flexibility;
- Rumble zone denial through choke/objective space;
- Syndra pick plus anti-entry control;
- Ezreal safe long-range continuation;
- Karma shielding, speed and spacing support.

LGD had strong initiation through Skarner/Ambessa, but their damage follow-up was shorter-ranged and more dependent on the same forward-entry geometry.

Therefore the correct neutral-setup stress answer was not “LGD dictate the next fights.” JDG could make LGD enter through layered range/zone while retaining safer DPS and reset options.

## 2. DER / shared-failure penalty was missed

The retained anti-favorite review requires underdog tools to be tested for mechanism independence.

LGD's apparent comeback tools were materially coupled:

- Skarner entry;
- Ambessa follow/dive;
- Ryze/Lucian short-range follow-up;
- Milio protection after the forward commit.

These mechanisms shared the same need to enter JDG's controlled space and survive Rumble/Syndra/Jarvan disruption. They were not independent comeback routes.

The TAKE effectively counted “Skarner engage + Ambessa access + Ryze/Lucian damage” as several reasons for LGD resilience when they were largely one shared forward-contact branch.

## 3. MKT + TEAM anchor was not respected

The retained aggregate anti-favorite correction states that market/team-strength priors cannot be reset toward neutral merely because an underdog draft has visible tools.

Here:

- JDG was the post-draft market favorite;
- the draft assessment already leaned JDG;
- JDG then gained the first two live resource leads;
- LGD had no structural or objective control evidence at the entry snapshot.

The move from about 36.7% no-vig LGD post-draft to about 19.6% no-vig at 8:23 was large, but a large price move is not itself evidence of mispricing.

To TAKE LGD, the model needed an explicit fair-probability case that still exceeded the market after applying the JDG team/draft anchor, current JDG resource lead, JDG CFC advantage, and LGD shared-failure penalty.

That case was not established. The verdict instead reasoned from “LGD still have a path” to “LGD are underpriced.” Those are not equivalent.

## 4. 0-0 structures were incorrectly used as absence of JDG control evidence

At 8:23, 0-0 towers and 0-0 dragons were neutral facts.

They did not supply LGD with independent control evidence, and they did not erase JDG's draft-level range/zone advantage.

The correct interpretation was:

- JDG already held RL;
- SL had not yet separated;
- OSC had not yet separated;
- draft CFC still leaned JDG;
- therefore LGD needed a strong price-only edge after all downside branches, not merely a generic comeback route.

## 5. Later states validate the pre-existing mechanism, but are not used to backfit the verdict

Later snapshots showed exactly the branch that should have been represented at entry:

- around 13:53 LGD led kills 4-3, yet JDG led towers 1-0 and dragons 1-0;
- 21:26 LGD led kills 5-3, yet JDG were still about +1.9k with towers 3-1 and dragons 2-0;
- 31:17 LGD led kills 11-7, yet JDG were about +4.6k with towers 6-2 and Baron 1-0;
- final JDG won 14-13 kills while dominating towers 9-2, Barons 2-0 and inhibitors 2-0.

This was a Structure-Substitution / map-control branch: JDG did not need early kill-margin dominance to retain and expand win probability.

The outcome supports the mechanism diagnosis, but the review classification rests on information and rules available at entry.

## Correct historical decision

`PASS — LGD ML @4.773 — 0u.`

Named failing gates at 8:23:

1. `CFC`: misclassified; full neutral-setup fight control favored JDG or was at least not independently LGD-favored.
2. `DER/shared-failure`: LGD's comeback tools were materially coupled around the same forward-entry route.
3. `MKT + TEAM anchor`: favorite prior plus draft lean plus live resource lead remained intact.
4. `Pricing edge`: no explicit fair-probability case was established after those penalties; high odds alone did not prove edge.

## Governance consequence

- Keep the recorded result and -0.25u P/L in the audit ledger.
- Mark the TAKE diagnostically as execution/application-invalid, analogous in governance treatment to other rule-application errors.
- Do not create v0.3.61 from this single result.
- No new threshold is added.
- Future v0.3.60 ML execution must run the full CFC stress test rather than equating hard engage with fight control, and must explicitly carry the MKT+TEAM anchor plus DER/shared-failure penalty into any price-based underdog reversal.
