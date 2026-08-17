# Football Process Review — Nõmme United U21 vs Nõmme Kalju U21: Early SOT Efficiency False-Positive

**Date:** 2026-08-18  
**Status:** Active process review / validator-enforcement clarification  
**Model at original decision:** Football v0.2.47 — AUDIT MODE  
**Resulting amendment:** No model-version bump yet. Existing validator Gate 5 was already sufficient; the failure was an enforcement/deduplication error. Promote a new rule version only if a broader repeated pattern requires behavior beyond the current validator.

## Scope

This review audits the v0.2.47 shadow selection issued in Nõmme United U21 vs Nõmme Kalju U21 at approximately 10:37 with the score 0-0:

`SHADOW LEAN — DO NOT PLACE: Over 4.0 @1.83`

The user later confirmed the final score as **Nõmme United U21 2-0 Nõmme Kalju U21**. The shadow outcome is therefore a full loss at the 0.125u audit convention: **-0.125u simulated P/L**.

The purpose of this review is process validity, not hindsight outcome-fitting. The question is whether the 10:37 state actually satisfied the rules that were already active at the time.

## Original synchronized evidence

At approximately 10:08-10:37:

- score: 0-0;
- possession: 45-55;
- shots: 3-1;
- shots on target: 3-1;
- all four recorded attempts were on target;
- corners: 0-0;
- no supplied big-chance count;
- no supplied box-touch count;
- no supplied shot-location map or inside-box split;
- no supplied dangerous-transition sequence;
- no supplied defensive-degradation sequence.

Market:

- Over 4.0 @1.83;
- Over 4.25 @2.03;
- Over 3.75 @1.66, below the active 1.70 reference floor.

Settlement on Over 4.0 from 0-0:

- 0-3 total goals: loss;
- exactly 4 total goals: push;
- 5+ total goals: full win.

The candidate therefore required **five total goals for a full win** from a 0-0 state after roughly ten minutes.

## Original promotion logic

The Decision State marked two primary channels:

- `Shot Quality/Locations`;
- `Tempo/Persistence`.

The evidence summary supporting those labels was effectively the same early event cluster: four total shots, all four on target, with both teams contributing.

That was the key process error.

## Existing validator requirement

`FOOTBALL_PRE_VERDICT_VALIDATOR.md` Gate 5 already states:

- any live candidate needs at least two **independent** primary forward-looking channels;
- possession, pass volume, raw shots, SOT, xG and xGOT cannot by themselves satisfy the minimum.

Therefore this selection did not require a new result-driven rule to become invalid. It was already invalid under the model that issued it.

## Process violations

### 1. Raw SOT was misclassified as shot-quality/location evidence

A shot being on target does not by itself establish a strong shot location or chance structure.

Without location, inside-box context, clear-chance context, goalkeeper-intervention quality, or equivalent structural detail, the 3-1 SOT count remained a **raw SOT statistic**.

It could not legitimately populate `Shot Quality/Locations` as an independent primary channel.

### 2. The same shot cluster was double-counted

The same four attempts were used to support both:

- direct threat / shot quality; and
- tempo / persistence.

That violates independence. One event cluster cannot become two channels merely by assigning two labels.

### 3. Kickoff-to-10' is not persistence by itself

A kickoff baseline of zero events followed by a cumulative 10-minute snapshot does not prove persistence.

`Tempo/Persistence` requires either:

- at least two comparable score-stable live snapshots showing continuing/repeated threat; or
- a timestamped event sequence clearly showing repeated attacks/chances over the interval.

The Nõmme state had one meaningful cumulative live snapshot, not a demonstrated repeated regime.

### 4. No independent structural channel was supplied

There were no supplied corners, box-touch accumulation, territory progression, repeated entries, defensive errors, big chances, or equivalent structural evidence supporting the Over independently of the raw SOT count.

With corners at 0-0 and no deeper chance-location feed, the second independent primary channel was unresolved.

### 5. The remaining-goal burden was unusually high

Over 4.0 from 0-0 at 10:37 required five total goals for a full win and four merely to push.

The market had already priced the match as an extreme goal environment. A short early burst of efficient SOT was not enough evidence to support that full-win burden.

This is not a new universal numerical threshold. It is a reminder that settlement/event-budget burden must be supported by the **quality and independence** of the evidence, especially at very high live totals.

## Correct counterfactual verdict

At 10:37 under the rules actually active at the time:

- `Primary channel 1:` raw SOT / direct threat — context only unless location/quality is verified;
- `Primary channel 2:` unresolved;
- `Directional persistence:` unresolved;
- `Goal environment:` unresolved-to-open watch, not proven open for O4;
- `Best protected total:` Over 4.0 @1.83;
- `Validator:` HOLD;
- `Verdict:` `NO BET — HOLD`.

The correct unlock condition would have been a later score-stable checkpoint showing a genuinely independent second channel — for example repeated high-value box attempts, big chances, meaningful keeper interventions, dangerous transitions, or sustained structural pressure — while the remaining-goal budget still offered a defensible protected line.

## Audit classification

The historical shadow decision remains preserved exactly as issued in the Decision States table. It must not be rewritten.

For the Circuit Breaker audit, however, process validity is separate from outcome. The Nõmme selection is classified:

- **Outcome:** Loss;
- **Process validity:** Invalid;
- **Reason:** Existing Gate 5 was breached through raw-SOT promotion, evidence double-counting, and unsupported persistence.

The invalid sample remains visible for audit integrity but must not be treated as a valid positive or negative model-performance datapoint when estimating v0.2.47 edge.

## Immediate enforcement clarification — active going forward

Without changing the model version, apply the existing validator as follows:

1. **Raw SOT is never `Shot Quality/Locations` without location/chance-structure context.**
2. **One event cluster cannot satisfy two independent primary channels.**
3. **`Tempo/Persistence` cannot be inferred from kickoff zero to one cumulative snapshot.** Require comparable score-stable snapshots or a clearly repeated event sequence.
4. **When provider depth is shallow, missing chance-location/box-access data increases uncertainty; it does not permit raw SOT to stand in for those channels.**
5. **For very high live totals, explicitly match the evidence to the exact full-win goal burden.** Protection is useful, but a push boundary cannot rescue an unsupported five-goal thesis.

These are enforcement clarifications of existing synchronization, independence, provider-quality and event-budget rules, not a hindsight Under bias.

## v0.2.47 sample status at audit time

Known v0.2.47 shadows in the current run:

- Vasco da Gama vs Santos — Over 2.25 @1.80 prematch — user-confirmed final 0-3, full win under the 0.125u convention (+0.100u simulated).
- Austin FC vs FC Dallas — Over 2.25 @1.84 at 17:00, 0-0 — final verified as Austin 1-2 Dallas, full win (+0.105u simulated).
- IF Gnistan vs Ilves — Over 3.75 @1.83 at 33:06, 1-1 — user-confirmed HT 2-2; exact final not yet verified in this review. At total 4, settlement is half-win/half-push; any fifth goal makes it a full win.
- Nõmme United U21 vs Nõmme Kalju U21 — Over 4.0 @1.83 at 10:37, 0-0 — user-confirmed final 2-0, loss (-0.125u simulated), process validity Invalid.

Do not claim a final v0.2.47 ROI until the Gnistan settlement is confirmed and invalid samples are separated from valid-sample performance.

## Next-step research

Track early live Over candidates where:

- the total is already 3.5 or higher;
- the first 8-15 minutes show unusually high SOT efficiency;
- deeper provider metrics are limited.

Record whether the early SOT cluster broadens into independent box/chance/structural channels by the next score-stable checkpoint. Only after a larger sample should the model add a new empirical high-total penalty or fixed waiting rule.

## Operating principle

**Do not confuse efficiency with persistence, and do not manufacture independence by relabeling the same events.**

The correct response to the Nõmme loss is stricter enforcement of rules already present, not a blanket anti-Over adjustment.