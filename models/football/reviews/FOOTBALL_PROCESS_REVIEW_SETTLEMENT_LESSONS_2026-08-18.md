# Football Process Review — Settlement Lessons: Copenhagen, San Diego, Gnistan

**Date:** 2026-08-18  
**Status:** Active process review / enforcement clarification  
**Active model:** Football v0.2.47 — AUDIT MODE  
**Version action:** No model-version bump. These are enforcement clarifications and evidence-weighting lessons under existing rules.

## Scope

This review consolidates three newly settled shadow decisions and the adjacent Nõmme process audit:

- FC Copenhagen vs Debreceni — Under 4 @1.77 at 67:26, score 2-1 — **LOSS**, final 5-1.
- San Diego FC vs Puebla — Over 2.75 @1.85 at 66:31, score 1-1 — **FULL WIN**, final 3-2.
- IF Gnistan vs Ilves — Over 3.75 @1.83 at 33:06, score 1-1 — **FULL WIN**, final 3-2.
- Nõmme United U21 vs Nõmme Kalju U21 — Over 4 @1.83 at 10:37, score 0-0 — **LOSS, PROCESS INVALID** under existing Gate 5.

The purpose is not outcome-fitting. Historical selections remain exactly as issued. The objective is to improve enforcement of already active concepts: independence, persistence, remaining-goal burden, halftime compression, and actual regime change.

## 1. Gnistan confirms the value of separating first-half selection from second-half re-entry

The original Gnistan Over 3.75 was issued at 33:06 with the score 1-1 after a score-stable interval showed fresh threat: new attempts, Gnistan's first SOT, and Ilves' second big chance. The match reached 2-2 by halftime and finished 3-2.

The first-half shadow therefore settled as a full win. More importantly, the **second half produced only one goal despite a 2-2 halftime**.

This supports the v0.2.47 process distinction:

- a valid first-half Over can remain valid historically;
- a 3+ goal halftime creates a new scoring-regime problem;
- the prior first-half openness cannot justify a fresh post-HT Over;
- a high-scoring first half is not evidence that second-half scoring hazard will remain equally high.

This is supportive process evidence for the HT-compression gate, not proof of a universal statistical law.

## 2. San Diego shows what a stronger late Over signal looks like

At 66:31, San Diego vs Puebla was 1-1. The Over 2.75 promotion was supported by more than the score:

- both teams had demonstrated an independent scoring route;
- attacking output had expanded materially from the earlier checkpoint;
- San Diego retained sustained box/chance pressure;
- Puebla remained capable of contributing rather than becoming a passive non-participant;
- the protected quarter-line reduced dependence on an exact multi-goal finish.

The final 3-2 result is consistent with the process thesis, but the key lesson is **prospective**: repeated two-sided threat across comparable windows is materially stronger than an isolated burst of efficiency.

## 3. Copenhagen exposes a distinct Under failure mode

At 67:26 Copenhagen led Debreceni 2-1 in the match and 5-1 on aggregate. Under 4 @1.77 was promoted partly because the aggregate state appeared to support conservation.

The final was 5-1. Copenhagen scored three additional goals after the shadow entry.

The process error was not simply 'bad luck'. The model over-weighted **incentive-to-conserve** relative to evidence of **actual deceleration**.

Going forward:

- a large aggregate lead, comfortable table position, qualification security, or lack of need for another goal is **context only** for an Under;
- these incentives cannot independently establish a closed/decaying goal regime;
- an Under needs affirmative current evidence that the match is actually throttling down, such as reduced high-value entries, lower transition frequency, fewer bodies committed, attack-dampening substitutions, repeated harmless possession, opponent suppression, or comparable score-stable windows showing threat decay;
- if the leader retains repeatable chance creation, attacking depth, or a credible multi-goal route, conservation language must not override that evidence.

In short: **'they do not need to score' is not equivalent to 'they have stopped creating'.**

## 4. Nõmme remains the warning against manufacturing independent evidence

The Nõmme Over 4 loss remains process-invalid because the promotion used one early SOT cluster as if it supplied both shot-quality and persistence channels.

This review reinforces the existing correction:

- raw SOT is not shot-location/chance-structure evidence;
- one event cluster cannot count twice under different labels;
- kickoff-to-one-cumulative-snapshot is not persistence;
- shallow provider data increases uncertainty rather than lowering the evidence bar.

## 5. Enforcement clarifications active immediately

Without changing the model version, apply these rules to all live totals:

1. **Independent-channel deduplication:** each primary channel must be supported by genuinely distinct evidence. If two labels depend on the same event cluster, count one channel, not two.
2. **Persistence proof:** `Tempo/Persistence` requires comparable score-stable snapshots or a clearly timestamped repeated sequence. A single cumulative snapshot cannot prove persistence.
3. **Goal-budget proportionality:** the evidence burden must rise with the exact full-win goal requirement. A total needing four or five additional goals cannot be justified by one efficient early burst.
4. **Under deceleration proof:** conservation incentives are context only. A live Under requires affirmative evidence of actual threat decay or suppression in the current regime.
5. **Protected-line preference remains valid:** when the thesis clears all gates, prefer the lowest eligible protected boundary that preserves price quality and reduces unnecessary goal-count burden.
6. **High-scoring HT reset remains hard:** after 3+ first-half goals, no post-HT Over may inherit first-half evidence as fresh proof.

## 6. What not to do

Do not respond to these outcomes by:

- adding a blanket Over bias because San Diego and Gnistan won;
- adding a blanket Under bias after high-scoring first halves;
- banning early Overs entirely because Nõmme failed;
- assuming large aggregate leads always produce Unders;
- inventing fixed waiting-minute rules without a larger audited sample.

The correct adjustment is **evidence quality and independence**, not directional superstition.

## Operating principle

**For Overs, demand repeated independent threat that supports the exact remaining-goal budget. For Unders, demand demonstrated deceleration rather than inferred lack of motivation. After high-scoring halftime states, reset the scoring process completely.**
