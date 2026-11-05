# Football C — Assessed Matches Settlement Audit

Date: 2026-11-05 ICT
Status: DEEP AUDIT REQUIRED
Scope: assessed fixtures from Buriram–Kashima through the 03:00 ICT UCL block
Model of record: Football C only

## Scope / integrity

This audit uses frozen prospective Football C assessments plus final results only for settlement classification.
No result is used to rewrite a prior certificate or create retrospective exposure.

Physical P/L remains separate. Several /xi rows were OBSERVED_*_NON_EXECUTABLE or BOOK targets with zero exposure unless the user independently confirmed a fill.

## Final results reconciliation

| Fixture | Frozen final football state | Supported burden | FT | Supported burden reached? | Audit classification |
|---|---|---:|---:|---|---|
| Buriram United–Kashima Antlers | FOCUS, FRAGILE DISTRIBUTED G3 | O2.5 | 0-0 | NO | CERTIFICATE_FALSE_POSITIVE |
| Al Nasr Dubai–Qatar SC | FRAGILE LEAKAGE G3 | O2.5 | 4-1 | YES | certificate clear; G4 opportunity missed |
| Dortmund U19–Real Betis U19 | ROBUST G4 | O3.5 | 2-2 | YES | correct |
| Nasaf W–Beijing W | FOCUS, FRAGILE DISTRIBUTED G3 | O2.5 | 1-2 | YES | G3 clear; initial live 1-1 concern resolved at FT |
| East Bengal W–Hwacheon KSPO W | WATCH, no G3 | none | 1-4 | n/a | CERTIFICATE_FALSE_NEGATIVE |
| Al Rayyan–Al Nahda | FOCUS, FRAGILE G3 | O2.5 | 2-0 | NO | CERTIFICATE_FALSE_POSITIVE; priced O3 PASS was correct |
| Al Wahda–Al Khaldiya | FOCUS, ROBUST G3 | O2.5 | 1-2 | YES | correct; O2.75 BOOK would half-win if filled |
| Rennes–Olympiacos | FOCUS, FRAGILE DISTRIBUTED G3 | O2.5 | 0-0 | NO | CERTIFICATE_FALSE_POSITIVE; observed ACT model verdict lost |
| Kuwait SC–Nasaf | WATCH, no G3 | none | 2-3 | n/a | CERTIFICATE_FALSE_NEGATIVE |
| AEK Athens–Real Madrid | ROBUST G4 after confirmed XI | O3.5 | 2-3 | YES | correct; O3.5 BOOK target would win if filled |
| Fenerbahce–Liverpool | CONDITIONAL G3 after confirmed XI downgrade | O2.5 | 3-2 | YES | correct floor; O2.75 BOOK target would win if filled |
| Lens–Como | FOCUS, ROBUST CARRIER G4 | O3.5 | 1-9 | YES | strong correct |
| Leipzig–Manchester City | FOCUS, ROBUST CARRIER G4 | O3.5 | 2-3 | YES | strong correct |
| Viking–Sabah | FOCUS, CONDITIONAL LEAKAGE G3 | O2.5 | 4-1 | YES | correct |
| Dortmund–Real Betis | FOCUS, CONDITIONAL G4 | O3.5 | 2-1 | NO | G3 clear, G4 overreach |
| Slavia Praha–Arsenal | FOCUS, ROBUST G3 | O2.5 | 1-2 | YES | correct |
| PSV–Club Brugge | FOCUS, FRAGILE G3 with no direct ACT ceiling | O2.5 | 1-2 | YES | football floor cleared; execution veto was conservative |
| Porto–Napoli | WATCH, no G3 | none | 4-1 | n/a | CERTIFICATE_FALSE_NEGATIVE |

## Aggregate football settlement

Final football assessments with a supported burden: 15.

- G3-or-deeper certificate reached 3+ goals: 12/15 = 80.0%.
- Exact supported burden reached: 11/15 = 73.3%.
- Supported-burden failures:
  - Buriram–Kashima, O2.5 -> 0 goals.
  - Al Rayyan–Al Nahda, O2.5 -> 2 goals.
  - Rennes–Olympiacos, O2.5 -> 0 goals.
  - Dortmund–Betis, O3.5 -> 3 goals.
- Final G4 certificates in this scope: 5.
- G4/O3.5 cleared: 4/5 = 80.0%.

Assessed rows with no G3 certificate: 3.

- East Bengal–Hwacheon: 5 goals.
- Kuwait–Nasaf: 5 goals.
- Porto–Napoli: 5 goals.

Therefore no-G3 false-negative rate in this discovery scope is 3/3. This is not a universal performance estimate; the sample is small and not promotion-valid, but all three failures share the same selection-side problem.

## Block-order audit

### AFC Women
1. Nasaf–Beijing: 3 goals, G3 clear.
2. East Bengal–Hwacheon: 5 goals, no G3.

The #1 was not a final false positive, but the #2 no-G3 rejection was a severe false negative.

### 22:30–23:00 block
1. Al Rayyan–Al Nahda: 2 goals.
2. Al Wahda–Al Khaldiya: 3 goals.
3. Rennes–Olympiacos: 0 goals.
4. Kuwait–Nasaf: 5 goals.

The only no-G3 row finished with the highest total. This is direct settlement confirmation of the hard-viability inversion diagnosed on 2026-11-04.

### 00:45 UCL
1. AEK–Real Madrid: 5 goals.
2. Fenerbahce–Liverpool: 5 goals.

No selection inversion. Confirmed-XI adjustments were conservative but safe.

### 03:00 UCL
1. Lens–Como: 10 goals.
2. Leipzig–Manchester City: 5 goals.
3. Viking–Sabah: 5 goals.
4. Dortmund–Betis: 3 goals.
5. Slavia–Arsenal: 3 goals.
6. PSV–Club Brugge: 3 goals.
7. Porto–Napoli: 5 goals.

The top two carrier-led selections were excellent and validate the direction of emphasizing strong carrier structure for selection. However, Porto–Napoli again proves that the tier-2 no-G3 lane can hide a high-total result at the bottom of the block.

## Defect classification

### 1. CERTIFICATE_FALSE_NEGATIVE — confirmed repeated
Three assessed no-G3 rows all produced five goals:
- East Bengal–Hwacheon.
- Kuwait–Nasaf.
- Porto–Napoli.

The common pattern is that current scoring force/leakage exists, but either route-quality/H2H/control logic prevents G3 and BLOCK_PRIORITY_V1 then hard-locks the row below every funded-G3 FOCUS row.

### 2. RANKING_INVERSION — confirmed in the 23:00 block
Kuwait–Nasaf was mathematically unable to outrank the three G3-funded rows because hard viability tier is the first lexicographic key. Final total order exposed the weakness: the #4 row produced five goals while #1/#3 produced two/zero.

### 3. CERTIFICATE_FALSE_POSITIVE — still present, but narrower than first feared
Buriram, Al Rayyan and Rennes failed G3. Buriram and Rennes fit the prior broad-MEDIUM / FRAGILE G3 diagnosis. Al Rayyan was a LEAKAGE G3 and failed at exactly two.

### 4. G4 overreach — one clear case
Dortmund–Betis supported O3.5 and finished 2-1. G3 was correct; the fourth-goal extension was not.

### 5. Tournament incentive failure — not supported
The problematic rows generally carried MIXED incentive rather than an automatic expansive upgrade. Incentive is not the common root cause.

## What improved

The 03:00 UCL block demonstrates that carrier-led, high-chance, high-completion selections can work very well under the existing model:

- Lens–Como: #1, ROBUST CARRIER G4, 10 goals.
- Leipzig–City: #2, ROBUST CARRIER G4, 5 goals.

This matters because it narrows the repair target. The problem is not that carrier-led logic itself is bad; it is that BLOCK_PRIORITY_V1 cannot rescue strong carrier/no-G3 rows once the certificate layer rejects them.

## Root-cause update

The 2026-11-04 architecture audit remains valid, with one important refinement:

- The main current failure is now more strongly evidenced as **false-negative suppression + hard block tiering**.
- FRAGILE distributed G3 still needs safety tightening because Buriram and Rennes both settled 0-0.
- But a blanket tightening of all G3 would be wrong: 12/15 funded G3-or-deeper assessments reached three goals, and the 03:00 carrier-led top selections were strong.
- The permanent repair should target the no-G3 rescue / block-order separation and the broad-MEDIUM FRAGILE exposure lane independently.

## Normal-audit result

The same defect pattern now appears across multiple blocks and a reliable repair requires code modification/regression testing.

status: DEEP AUDIT REQUIRED

defect_class:
- CERTIFICATE_FALSE_NEGATIVE
- RANKING_INVERSION
- CERTIFICATE_FALSE_POSITIVE
- G4_RESEARCH_COMPLETENESS_FAILURE

scope:
- 2026-11-04/05 ICT assessed fixtures listed in this report
- BLOCK-AWCL-2130-20261104-V1
- BLOCK-2230-2300-20261104-V3
- BLOCK-UCL-0045-20261105-V1
- BLOCK-UCL-0300-20261105-V1
- Buriram direct /xi and current XI runtime rows 144-147

frozen_evidence:
- three no-G3 rows were hard tier-2 under BLOCK_PRIORITY_V1;
- all three later produced five goals;
- Buriram and Rennes were FRAGILE broad-MEDIUM G3 constructions and both finished 0-0;
- carrier-led ROBUST UCL #1/#2 both cleared G4 strongly.

observed_failure:
- no-G3 rows cannot challenge funded-G3 rows in block priority even when current carrier/goal signal is stronger;
- FRAGILE broad-MEDIUM G3 can still create direct O2.5 exposure;
- G4 can overreach while G3 remains correct.

suspected_area:
- engine/block_priority.py hard_viability lexicographic tier
- engine/core.py c_verified_current_structure_goal3 / c_distributed_goal3_funded
- c_g3_endpoint_control_pressure
- single-H2H suppressive hard control
- G4 continuation/transferability contract

ruled_out:
- tournament incentive as common cause
- league prestige/popularity
- a blanket failure of carrier-led goal logic
- final-score-only explanation

questions_for_deep_audit:
1. Can block order compare raw carrier force before certificate accessibility without creating exposure authority?
2. Can a no-G3 row enter a non-executable CARRIER_REVIEW tier that can outrank weak FRAGILE G3 selections?
3. Should a single suppressive H2H be capped unless independently corroborated?
4. Should FRAGILE distributed/current-structure G3 with several MEDIUM risk axes be exposure-quarantined?
5. What additional G4 requirement would have rejected Dortmund–Betis O3.5 without damaging Lens–Como / Leipzig–City?

recommended_tests:
- East Bengal–Hwacheon false-negative regression.
- Kuwait–Nasaf false-negative / single-H2H regression.
- Porto–Napoli no-G3 carrier-rescue regression.
- Buriram–Kashima FRAGILE distributed G3 exposure regression.
- Rennes–Olympiacos broad-MEDIUM G3 regression.
- Dortmund–Betis G4 overreach regression.
- Lens–Como and Leipzig–City must remain positive controls.

implementation_requested: false
