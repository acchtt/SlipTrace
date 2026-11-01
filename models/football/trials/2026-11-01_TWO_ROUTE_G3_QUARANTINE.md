# Football C — Two-route G3 overvaluation risk-tightening quarantine

## Identity

- **Experiment ID:** C-RQ-20261101-TWO-ROUTE-G3
- **Created at (ICT):** 2026-11-01 22:42
- **Champion:** Football C pre-quarantine
- **Champion commit/version:** 29f577bf379b48ed0d33e51cb4a0e3c9320e56e8
- **Challenger:** Football C + TWO_ROUTE_G3 authority quarantine
- **Owner:** user-directed production risk tightening
- **Status:** FROZEN / RUNNING

## Rule delta

- **Exact current rule:** TWO_ROUTE has a dedicated mechanism-rank bonus and two independently STRONG routes can corroborate/relax several G4 completion paths.
- **Exact challenger rule:** TWO_ROUTE remains a valid G3 certificate only; it ties genuine distributed G3 for mechanism rank, never corroborates G4, never relaxes carrier route-reliability or distributed failure-resistance requirements, and cannot by route count alone create ROBUST strength.
- **Files touched if promoted:** `models/football/engine/core.py`, active Football C authority docs, deterministic tests.
- **One material change only:** YES — remove route-count authority above G3.

## Hypothesis

- **Observed failure mode:** Football C overvalues the existence of two scoring routes relative to actual multi-goal continuation, allowing balanced but endpoint-prone 1-0/1-1/2-0 shapes to rank too highly or inherit G4 authority.
- **Hypothesis:** Treating TWO_ROUTE as G3-only evidence will reduce false-positive top ranks and unsupported O3.50/G4 certificates without destroying independently funded carrier-led or leakage-led G3 opportunities.
- **Expected benefit:** lower selection inversion and fewer high-burden certificates derived from route count rather than continuation.
- **Expected cost / missed-opportunity risk:** some genuinely explosive two-sided matches may rank lower when their fourth-goal evidence is not independently established.
- **What result would falsify the hypothesis:** prospectively, quarantined two-route rows materially outperform retained carrier/leakage candidates at the same blocks while G4 false-positive frequency does not improve.

## Discovery set

These cases have zero confirmatory weight.

| Fixture / case | Date | Why it motivated the rule |
|---|---|---|
| User-reported Frosinone #1-ranked case, FT 1-0 | 2026-11-01 | High rank despite a controlled one-goal endpoint; prompted inspection of TWO_ROUTE authority. |
| Recent selection-inversion audits | 2026-10-23 to 2026-11-01 | Repeated concern that balanced route documentation outranked stronger carrier-led high-total candidates. |

## Prospective holdout / quarantine review

- **Start timestamp:** effective only after this patch reaches `main`.
- **Mandatory review/expiry:** 2026-11-08 23:00 ICT or after 40 eligible post-patch TWO_ROUTE-involved Football C decisions, whichever occurs first. Do not silently convert the quarantine into a permanent rule.
- **Eligible universe:** all post-patch Football C ranked/exception assessments in which TWO_ROUTE_G3 is funded or both routes are STRONG.
- **Exclusions:** discovery cases above; retrospective decisions; rows lacking frozen pre-outcome evidence.
- **Decision information clock:** same frozen evidence available to production at the original decision epoch.
- **Market/quote epoch rule:** screenshot-only observed odds remain unchanged; market cannot create structure.
- **Minimum eligible decisions:** 40 preferred for review.
- **Minimum settled exposure differences:** 20 preferred when available.

## Frozen metrics

### Primary metric
- paired false-positive high-burden/top-rank rate for TWO_ROUTE-led rows versus the pre-quarantine champion on the same frozen evidence.

### Secondary metrics
- O2.50/3+ capture among quarantined rows;
- 4+ and 5+ rate;
- main-total clear/push/below;
- top-k block capture and rank regret;
- exposure-rate delta;
- maximum drawdown;
- paired champion-vs-quarantine decision table;
- time-block stability.

### Guardrails
- do not lower G3/G4/G5 thresholds;
- do not create new exposure eligibility;
- preserve self-funded carrier authority;
- preserve historical decisions;
- no outcome or market-price input may alter route/certificate classification.

### Predeclared subgroup cuts
- route class: TWO_ROUTE-only / TWO_ROUTE+LEAKAGE / TWO_ROUTE+CARRIER;
- carrier verification: self-funded / not self-funded;
- line/burden: O2.50 / O2.75-O3.25 extension / O3.50+;
- execution strength: FRAGILE / CONDITIONAL / ROBUST;
- kickoff block and competition.

## Governance result

- [ ] PROMOTE
- [x] KEEP SHADOW / ACTIVE RISK-TIGHTENING QUARANTINE
- [ ] NARROW AND RETEST
- [ ] REJECT

### Reason

User directed immediate correction after an identified production failure. QA permits early adoption only as a pure risk-tightening quarantine with expiry and mandatory review. This record freezes the exact delta prospectively and explicitly excludes the motivating outcome from confirmatory evidence.
