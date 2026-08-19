# DNS vs BRO Game 1 — Underdog +Kills Role-Leverage and Duration Execution Review

**Date:** 2026-08-19 UTC+7  
**Model:** LoL v0.3.58 canonical  
**Status:** Retained in-place clarification review; no version bump

## Scope

Review the two visible Game 1 TAKEs and determine whether the failure requires a new model version or enforcement/clarification inside canonical v0.3.58.

Draft:

- DNS blue: Ambessa / Qiyana / Orianna / Jhin / Bard
- BRO red: Olaf / Jarvan IV / Cassiopeia / Corki / Neeko

Final:

- BRO won
- duration 33:14
- kills 17-7 BRO
- final signed BRO kill margin: +10

Visible positions:

1. DNS +8.5 kills @2.014 at 9:44 — LOSS, -0.25u shadow.
2. Over 33 minutes @1.666 at 18:54 — WIN, +0.1665u shadow.

Historical results remain unchanged. This review evaluates whether the TAKEs were eligible under the already-written canonical rules.

---

## 1. Primary finding — no v0.3.59 is warranted

The key failure was not absence of a model concept. Canonical v0.3.58 already contained the controls needed to reject the DNS +8.5 position:

- underdog +kills fallback is draft-locked and fail-closed;
- STABLE requires FER/PDC/PST/ARI plus KPA and KMS;
- False-Stable Guard activates when the favorite has repeatable range/zone/siege/continuation routes and the underdog repeatedly enters the same controlled space;
- ordinary live evidence cannot upgrade FRAGILE / ABSENT / UNCERTIFIED fallback to STABLE;
- role-weighted economy / TEI and lead quality are already required concepts in the model.

Therefore this incident is classified primarily as an **execution/enforcement miss**, with one narrow procedural clarification added below so role-location evidence cannot be misread as generic resistance.

Canonical model remains **LoL v0.3.58**.

---

## 2. Draft interaction should have blocked DNS underdog +kills certification

Before live play, the correct draft read already identified BRO as the cleaner grouped-execution draft.

The relevant mechanism cluster:

1. Cassiopeia Miasma directly constrains Ambessa/Qiyana forward-entry paths.
2. Jarvan IV + Neeko provide layered first contact and continuation around the same entry space.
3. Olaf provides an independent anti-CC damage route and does not share BRO's control dependency.
4. Corki supplies protected ranged damage and objective-zone pressure behind that shell.
5. DNS kill production depends heavily on Ambessa/Qiyana access, terrain/flank quality and Orianna follow-up.
6. If DNS first contact fails, several members can be exposed together and Jhin/Bard do not independently repair the shared front-entry failure cluster.

Retrospective certification:

- FER: FAIL / at best UNRESOLVED
- PDC: UNRESOLVED
- PST: FAIL / UNRESOLVED
- ARI: FAIL
- KPA: PASS but conditional
- KMS: FAIL / UNRESOLVED
- False-Stable Guard: ACTIVE
- fallback floor: FRAGILE / UNCERTIFIED

Under the existing lock rule, that classification means ordinary live evidence cannot later upgrade DNS to STABLE.

---

## 3. 9:44 DNS +8.5 TAKE — procedural error

Synchronized 9:44 state:

- DNS 0-1 BRO kills
- BRO approximately +1.0k gold
- towers 0-0
- dragons 0-0
- barons 0-0
- DNS 3 grubs
- DNS +8.5 kills @2.014

Exact signed arithmetic was correct:

- current BRO margin = +1
- DNS +8.5 loses only if BRO finishes +9 or better
- BRO therefore needed +8 additional net kills from 9:44

The arithmetic did **not** certify the position. It only described the hurdle.

The visible TAKE incorrectly treated the following as positive margin-resistance evidence:

- small current kill margin;
- DNS 3 grubs;
- lack of early structural separation;
- localized DNS map/economy resistance.

But the draft fallback had not passed KMS and was not live-upgradable. Therefore the correct canonical verdict at 9:44 was:

**HOLD/PASS — DNS +8.5 kills @2.014 — 0u.**

The final +10 BRO margin confirms the mechanism failure, but the correction does not depend on the result.

---

## 4. Role-leverage error — top/grub resistance was overweighted

The live analysis treated a top-side advantage and 3 grubs too similarly to generic team-wide resistance.

That is too coarse.

Gold and objective assets must be interpreted through **where the leverage sits and how it converts into the relevant market distribution**.

For grouped midgame kill-margin suppression:

- mid/ADC economy often has more immediate protected-DPS, objective-zone and siege leverage;
- a top-lane lead can be highly valuable, but only if it creates an independent suppressive route such as side-lane inevitability, reliable flank access, durable frontline control, or a repeatable way to survive/deny the favorite's grouped conversion;
- grubs are structural/tempo assets, not automatic kill-margin suppression;
- an isolated top lead does not offset favorite carry concentration when the favorite also owns the easier grouped fight architecture.

At 18:54 the role distribution made the point clearly:

- DNS Ambessa held a large top-side advantage over Olaf;
- BRO's meaningful economy was concentrated in Corki and Cassiopeia;
- BRO also held 2 dragons and the easier neutral-objective 5v5 structure.

Calling that state "distributed economy resistance" was incorrect. The resistance was **localized**, while BRO held the higher-leverage grouped carry economy.

No fixed numeric lane multiplier is introduced. This is a mechanism check, not a rigid top<mid<ADC formula.

---

## 5. New in-place clarification — Role-Leverage Decomposition (RLD)

For every underdog +kills certification/reassessment, canonical v0.3.58 now requires **RLD — Role-Leverage Decomposition** before KMS may pass.

RLD must answer:

1. Where is each side's meaningful gold/level advantage concentrated: top, jungle, mid, ADC, support?
2. Which pockets convert directly into the next compulsory grouped fights, protected DPS, objective turn, siege or re-engage?
3. Does an underdog top-side lead create an **independent margin-suppression route**, or is it only isolated lane value?
4. Are grubs/towers/objective assets creating real kill-margin suppression, or only structure/tempo leverage?
5. Does the favorite hold carry-centered economy plus cleaner grouped access/control while the underdog's resistance is localized elsewhere?

Hard interpretation:

- If favorite carry leverage + grouped control is materially stronger and the underdog's resistance is mainly isolated top/grubs without an independent suppressive route, `KMS = PASS` is forbidden.
- RLD `UNRESOLVED` means fallback STABLE is forbidden.
- RLD does not automatically make top gold low-value. A fed top champion can pass RLD when its lead genuinely converts into side-lane inevitability, reliable flank/access, frontline durability or another independent KMS mechanism.

This clarification is added to the mandatory fallback-floor procedure, not a new analytical version.

---

## 6. Separate audit — Over 33 at 18:54 was also not canonical TAKE-eligible

The Over 33 position won by 14 seconds, but outcome must not hide the procedure.

18:54 state:

- DNS 0-2 BRO kills
- BRO +818 gold
- towers 1-1
- dragons 0-2 BRO
- barons 0-0
- Over 33 @1.666

The visible thesis relied on:

- only one additional kill from 9:44 to 18:54;
- only two total towers;
- "low conversion";
- balanced structures;
- supposed distributed DNS economy resistance.

Canonical Duration Over rules already say:

- low kills are neutral by themselves;
- low tower count is neutral by itself;
- conversion must be classified `ABSENT CONVERSION` vs `FAILED CONVERSION`;
- at least one positive Over mechanism must be observed failed conversion or equivalent repeated defense/reset;
- objective progress can be Structure Substitution and compress the clock.

At 18:54 there was no documented observed FAILED CONVERSION mechanism. BRO had also progressed to two dragons while the game stayed low-kill, which is compatible with Structure Substitution rather than positive stall evidence.

Therefore the correct canonical verdict was:

**HOLD/PASS — Over 33 minutes @1.666 — 0u.**

The historical Win and +0.1665u shadow P/L remain recorded, but the thesis state should be audit-labeled INVALIDATED.

---

## 7. Historical ledger corroboration — objective tokens can bias +kills reads

Airtable contains prior underdog +kills theses where 3 grubs / shallow structural separation were used as resistance evidence. Outcomes are mixed, including losses.

This review does not retroactively invalidate every such position. It establishes a narrower rule:

**grubs and isolated lane economy must never substitute for KMS or RLD.**

A future audit may review older positions individually if needed.

---

## 8. Operational correction

For underdog +kills, the internal certification output must now include:

- MKT/TEAM underdog
- DER
- FRI
- SRI
- FER
- PDC
- PST
- ARI
- KPA
- KMS
- **RLD**
- False-Stable Guard
- DCR
- FF
- hard Draft-Collapse Veto

Missing/unresolved RLD => PASS/HOLD.

The lock rule remains unchanged: ordinary live evidence cannot upgrade a draft-locked non-STABLE fallback.

For Duration Over, no new rule is added. The existing FAILED-CONVERSION / Structure Substitution hard gate simply must be enforced.

---

## 9. Model decision

**Decision: keep LoL v0.3.58. Do not create v0.3.59.**

Reason:

- DNS +8.5 was already blocked by existing draft-lock + KMS/False-Stable controls;
- Over 33 was already blocked by existing Duration Over FAILED-CONVERSION controls;
- the only genuine clarification needed is to make role-location leverage mechanically explicit inside underdog +kills certification so isolated top/grub resistance cannot be treated as equivalent to carry-centered grouped leverage.

This is an in-place canonical v0.3.58 procedural clarification.
