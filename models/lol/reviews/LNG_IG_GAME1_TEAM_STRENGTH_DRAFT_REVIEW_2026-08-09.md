# LNG vs IG Game 1 — Team-Strength and Draft Review

**Date:** 2026-08-09  
**Model at entry:** LoL v0.3.41  
**Resulting patch:** LoL v0.3.42

## Recorded shadow position

- LNG +9.5 kills @1.970
- Stake: 0.25u shadow
- Actual exposure: 0u
- Final: IG 26-13 LNG
- Result: LOSS, -0.25u shadow

## Verified lineups supplied by user

LNG:
- sheer
- Weiwei
- Nia
- 1xn
- Missing

IG:
- TheShy
- Wei
- Rookie
- Assum
- Meiko

## Draft

LNG:
- K'Sante
- Naafiri
- Akali
- Corki
- Nautilus

IG:
- Olaf
- Jarvan IV
- Ryze
- Kai'Sa
- Poppy

## Failure 1 — unstable team-strength prior

The team-strength assessment moved too aggressively across successive roster assumptions and market observations. Stale roster/team-level statistics were allowed to influence the prior before the actual current five was locked.

Once the user supplied the correct lineups, the model still moved too far away from a heavily IG-favored market without enough independent current-lineup evidence.

Correction: v0.3.42 requires verified current lineup, roster-discontinuity downweighting, role matrix, representative current-lineup form, de-vigged market anchor and explicit divergence reasons.

## Failure 2 — additive draft-tool counting

The LNG +9.5 thesis counted Corki range/waveclear, K'Sante frontline, Nautilus pick and Akali/Naafiri counter-access as separate resilience positives.

That was too additive. The correct analysis is interaction-based:

- IG's Poppy reduced multiple dash/engage/access functions simultaneously;
- Jarvan + Ryze + Kai'Sa provided reliable target access and layered follow-up;
- Olaf increased run-through pressure and reduced the reliability of conventional control as a stop mechanism;
- LNG's Akali/Naafiri damage had meaningful access burden into IG's control structure;
- the stronger team also had the simpler engage-to-follow-up sequence.

Correction: v0.3.42 applies matchup-adjusted draft function, functional counter tax, execution-burden adjustment and damage-access mapping.

## Failure 3 — unsupported dog-cover probability

The recommendation estimated LNG +9.5 cover too highly without explicitly decomposing:

P(LNG +9.5 covers) = P(LNG wins) + P(IG wins by <=9)

With IG already a large map favorite, the model needed strong evidence that an IG win would usually stay within nine kills. The exact composition instead supported a meaningful IG high-margin branch.

Correction: v0.3.42 requires conditional winner/margin decomposition for every positive kill handicap.

## Counterfactual verdict under v0.3.42

LNG +9.5 @1.970: **PASS** absent a supportable conditional close-loss distribution that clears the pregame +5pp lower-bound edge gate.

## Forward rule

Do not repair this by automatically favoring favorites or negative handicaps. The correction is procedural:

1. stabilize team-strength prior first;
2. test draft tools against opposing answers;
3. account for execution asymmetry;
4. build market-specific conditional distributions;
5. fail closed when divergence or cover probability is unsupported.
