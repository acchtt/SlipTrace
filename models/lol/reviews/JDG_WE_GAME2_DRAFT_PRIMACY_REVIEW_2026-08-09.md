# JDG vs WE Game 2 — Draft Primacy Calibration Review

**Date:** 2026-08-09  
**Model at time of miss:** LoL v0.3.46  
**Resulting model:** LoL v0.3.47

## Missed market

At 11:46, JDG led WE 6-4 with +2.9k gold, towers 0-0 and WE holding the first dragon.

Live handicap:

- JDG -9.5 kills @1.844
- WE +9.5 kills @1.912

The model passed both sides. Final was JDG 19-5 WE at 25:18, a +14 kill margin.

The final outcome is not used to justify the corrected recommendation. The review asks whether the 11:46 state already contained enough evidence for JDG -9.5 to qualify.

## Draft

JDG:

- Olaf
- Jarvan IV
- Syndra
- Ezreal
- Nautilus

WE:

- Dr. Mundo
- Xin Zhao
- Viktor
- Lucian
- Milio

## What the old read missed

The v0.3.46 live handicap read treated WE's Mundo/Viktor/Milio package as meaningful generic resilience. That was too coarse.

WE's tools did not solve the actual matchup:

- Mundo supplied durability but little proactive hard control;
- Xin Zhao's main hard control required close access and setup;
- Viktor's control was zoning/delayed rather than reliable first contact;
- Milio primarily supplied defensive peel and range support;
- Lucian had no hard control.

JDG had multiple independent, reliable ways to start and continue fights:

- Nautilus first contact;
- Jarvan initiation and displacement;
- Syndra burst/control follow-up;
- Olaf run-through pressure into limited stop tools;
- Ezreal safe ranged damage and cleanup.

The trailing composition's lack of reliable proactive CC materially reduced its ability to choose fights, contest objectives from losing vision, interrupt JDG's first successful sequence or generate comeback states.

## Economic distribution mattered

The +2.9k team lead was not concentrated in one fragile carry. Role-level gold showed JDG ahead in four of five positions, with especially large jungle and mid advantages.

That distribution made the draft edge more dangerous:

- engage/control roles were economically strong;
- primary damage roles were not starved;
- future objective setups favored JDG across multiple lanes;
- WE could not simply neutralize one fed champion to reset the map.

The model should have treated this as Distributed Economic Dominance combined with a Draft-Dominance Cascade state.

## Corrected margin logic

At 11:46, JDG were already +2 kills. Covering -9.5 required a final margin of +10 or more, so JDG needed at least +8 additional net kills.

The old analysis overweighted that arithmetic as a burden.

Under the corrected framework, the key question is:

`P(final JDG margin >=10 | current synchronized state and draft interaction)`

A defensible reconstructed range is approximately 60-67%.

Break-even at 1.844 is 54.23%. The v0.3.44 early-live handicap surcharge requires a lower-bound edge of +6pp, or roughly 60.23%.

With the lower bound around 60% and multiple independent draft/lead mechanisms supporting the wide-margin branch, JDG -9.5 was at or just through the qualifying gate.

## Corrected process verdict

**TAKE — JDG -9.5 kills @1.844 — shadow 0.25u; actual 0u.**

The position was not actually recommended or confirmed at the time, so it remains an untaken calibration miss and contributes 0u to the ledger.

## Model changes caused by this review

v0.3.47 introduces:

1. Draft Primacy after draft lock: draft is the primary conditional engine for state conversion.
2. Mandatory Draft Function Matrix.
3. CC Scarcity / Proactivity Tax.
4. Distributed Economic Dominance (DED).
5. Draft-Dominance Cascade (DDC).
6. Explicit conditional favorite wide-margin sanity check.
7. Early Favorite Handicap Fast Path.
8. Mechanistic rather than nominal underdog resilience.
9. Mandatory draft reassessment after material live state changes.

## Anti-overfit guardrail

This review does not create a blanket favorite bias.

Favorite -kills must still clear the symmetric v0.3.44 probability surcharge. DED without a conversion-capable draft is insufficient. A strong draft without a live lead is not automatically a wide-margin state. The correction is to condition the margin distribution correctly when **draft structure and live state align**.
