# BFX vs NS G1 PRE_TAKE_CERT Execution Failure Review — 2026-08-23

**Model:** LoL v0.3.58  
**Market:** NS +5.5 kills @1.869  
**Historical result:** LOSS  
**Classification:** procedural execution failure; existing-rule enforcement failure, not missing analytical logic.

## What failed

The model already required DIM, UDKC, KPA/KMS, RLD, False-Stable controls, live preservation, LAC, UCS, signed-margin arithmetic and NKB before an underdog +kills TAKE.

At 14:55, the decision over-weighted:

- the favorite kill margin remaining only +1;
- 0–0 towers;
- a displayed +5.5 cushion;
- the fact that additional kills had occurred without immediate margin expansion.

That evidence was allowed to stand in for the full live preservation / RLD / LAC proof burden.

## Contradictory evidence that should have blocked TAKE

BFX had a meaningful overall economy lead with favorite-side carry leverage, including material Caitlyn and Ryze economy. The BFX draft also had repeatable kill-generation and continuation routes through Jarvan IV, Rumble, Bard, Ryze movement and Caitlyn follow-up.

Existing RLD governance explicitly required the live economy distribution to preserve or downgrade the draft fallback. Carry-centered favorite economy plus cleaner grouped control was a downgrade risk that was not mechanically forced to a terminal value before the visible TAKE.

Existing KMS/LAC governance also required a concrete explanation for how NS would suppress those repeatable routes in the current live regime. Stable margin alone was not sufficient proof.

## Correct retrospective execution verdict

Historical TAKE remains historical and the loss remains -0.25u.

The correct model-certified verdict, had all existing gates been mechanically enforced, was **HOLD/PASS** because the candidate could not establish contradiction-free `LIVE_RLD`, `LIVE_PRESERVATION`, `KMS`, and `LAC` PASS from the available evidence.

## Repair

User instructed **“Do it now”** after asking why rules were repeatedly skipped.

Repair is execution hardening, not new betting logic:

`models/lol/procedures/LOL_PRE_TAKE_CERT_MECHANICAL_VALIDATOR_2026-08-23.md`

The validator protects the visible token `TAKE` and requires:

- an explicit applicability manifest;
- terminal values for every mandatory field;
- a separate contradiction scan;
- explicit split of draft RLD and live RLD for underdog +kills enforcement;
- zero failed/unresolved fields;
- final synchronized state/price recheck;
- circuit-breaker trip on any skipped mandatory gate.

No historical outcome is rewritten.