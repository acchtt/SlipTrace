# Football C Elite Upper-Tail Observer

**Status:** PROSPECTIVE OBSERVER ONLY — NO PRODUCTION AUTHORITY  
**Opened:** 2026-10-01 ICT  
**Parent:** Football C production  
**Purpose:** test whether Football C's supported-burden ceiling is systematically too conservative in a narrow elite-carrier class.

## Why this observer exists

The 2026-09-30 evening slate produced a clear missed opportunity:

- AS Roma Women vs Barcelona Women
- frozen Football C support: O3.0
- market at Step 2: lowest shown O4.25 @1.67
- Football C: PASS
- Football C2: PASS because +1.25 exceeded the +0.50 bridge cap
- FT: 0-6

This is not enough to justify a predictive rule change.

The same board also contained counterexamples where strong-carrier / independent-upper-tail evidence did **not** support buying extra burden.

## Retrospective diagnostic — 2026-09-30 board

Broad upper-tail carrier cohort definition:

- carrier = STRONG
- carrier_self_fund = true
- independent_upper_tail = true
- route_reliability = HIGH
- chance_quality = HIGH
- evidence_confidence = HIGH

There were 14 such C-FOCUS fixtures on the frozen board.

Diagnostic outcome:
- 6 finished above frozen supported line
- 1 finished exactly on frozen supported line
- 7 finished below frozen supported line
- average frozen supported line: 3.04
- average actual goals: 2.64

Therefore there is no evidence from this slate that Football C is generally under-supporting strong upper-tail carriers.

### Large market-gap cases actually assessed

1. OL Lyonnes Women vs Chelsea Women
   - support O2.75
   - market O3.25 @1.90 (+0.50)
   - C WAIT
   - C2 bridge BET shadow
   - FT 0-0
   - extra-burden bridge lost

2. SL Benfica Women vs Bayern Munchen Women
   - support O2.75
   - market O3.5 @1.92 (+0.75)
   - C PASS
   - C2 PASS
   - FT 0-3
   - buying O3.5 would have lost

3. AS Roma Women vs Barcelona Women
   - support O3.0
   - market O4.25 @1.67 (+1.25)
   - C PASS
   - C2 PASS
   - FT 0-6
   - buying O4.25 would have won

A generic extension of the C2 bridge from +0.50 to +1.25 would therefore have produced 1 win and 2 losses on these three observed gap cases, approximately -1.33u flat-stake at the recorded quotes.

Do not expand the bridge globally from this evidence.

## Narrow elite profile hypothesis

A much narrower frozen profile existed on only three matches:

- both routes at least USABLE
- carrier = STRONG
- carrier_self_fund = true
- independent_upper_tail = true
- route_reliability = HIGH
- independent_route_quality = HIGH
- chance_quality = HIGH
- failure_resistance = HIGH
- evidence_confidence = HIGH
- burden_protection = HIGH
- failure_attacks_route = false
- material_suppression = false

The three qualifying 2026-09-30 matches were:

- Farul Constanta Women vs Sparta Praha Women — support O3.0, FT 0-4
- SK Brann Women vs HJK Helsinki Women — support O2.75, FT 4-0
- AS Roma Women vs Barcelona Women — support O3.0, FT 0-6

All three finished above frozen support, but this is a tiny retrospective sample and must carry zero predictive-rule weight.

Only Roma-Barca was a valid observed large market-gap case in this exact elite profile. Farul was a schedule-integrity miss and Brann was available at exact support.

## Prospective observer trigger

Tag a fixture `ELITE_UPPER_TAIL_OBSERVER` only when all are true **before outcome**:

- official C state = C-FOCUS
- home_route >= USABLE
- away_route >= USABLE
- carrier = STRONG
- carrier_self_fund = true
- independent_upper_tail = true
- route_reliability = HIGH
- independent_route_quality = HIGH
- chance_quality = HIGH
- failure_resistance = HIGH
- evidence_confidence = HIGH
- burden_protection = HIGH
- failure_attacks_route = false
- material_suppression = false

Record but do not act on:

- frozen supported line
- current executable main/alternate totals and odds
- gap from support
- XI thesis state
- exact non-market upper-tail evidence
- main failure mode
- FT total goals
- settlement of frozen support
- hypothetical settlement of each recorded above-support quote

## Non-negotiable authority

This observer:

- does not change Football C supported burden
- does not extend the C2 bridge
- does not authorize BET/WAIT
- does not create Website Picks
- does not modify frozen evidence after result
- does not use market magnitude as proof of upper tail

Any future promotion requires a materially larger **prospective** sample and evidence that the narrow class improves out-of-sample exposure quality, not merely that selected FT results were high.

## Process case kept separate

Farul Constanta Women vs Sparta Praha Women is classified primarily as:

`MISSED OPPORTUNITY — PROCESS / SCHEDULE INTEGRITY`

The wrong kickoff prevented normal prematch Step 2. Its FT result must not be used as proof that a higher burden should have been bought.

Roma Women vs Barcelona Women is classified as:

`MISSED OPPORTUNITY — MODEL BURDEN / UPPER-TAIL CEILING`

and is the motivating observation for this prospective observer.
