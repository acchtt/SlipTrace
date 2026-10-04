# Football C3 — Burden-Funding Challenger Specification

**Status:** PROSPECTIVE SHADOW CHALLENGER  
**Champion:** Football C  
**Parallel challenger:** Football C2 remains frozen and unchanged  
**Purpose:** test whether Football C/C2 overvalue the existence of two scoring routes when those routes do not reliably fund the goal that clears the supported Asian total.

Football C3 is shadow-only. It may never create an official Website Pick or authorize real exposure.

## 1. Design principle

C3 asks:

> Who prospectively funds the goal that actually clears this supported burden?

For O2.0/O2.25/O2.5/O2.75, C3 must identify the mechanism funding **goal 3**.

For O3.0 and above, C3 must identify the mechanism funding **goal 4** as well as the path through goal 3.

Having two plausible scoring routes is descriptive only. It is not a positive ranking factor by itself.

## 2. Fair-comparison boundary

- fixture discovery is common and AiScore-authoritative;
- operational viability/researchability are common;
- one common football-fact evidence object is frozen before C/C2/C3 apply policy;
- C3 must not read C rank/state/lane or C2 rank/state before freezing its own fields;
- C3 uses the same current XI, odds, H2H, tournament and public-web evidence epoch as C/C2;
- C3 owns its supported line independently;
- C3 never changes C/C2 frozen outputs.

## 3. Second-route role

Classify the weaker/secondary scoring route as exactly one and persist a non-empty `c3_second_route_role_basis` explaining why the current route belongs in that class:

- `BURDEN_CONTRIBUTING` — prospectively helps fund the goal that clears the line;
- `EXCHANGE_ONLY` — can plausibly contribute one goal / 1-1 exchange but does not materially fund the clearing goal;
- `STATE_DEPENDENT` — becomes credible only if a particular open-game/deficit state occurs;
- `NONE` — no meaningful second scoring route.

Only `BURDEN_CONTRIBUTING` receives any positive C3 selection value.

`EXCHANGE_ONLY` and `STATE_DEPENDENT` must never be treated as equivalent to an independent burden-completing route.

## 4. Funding state

For each relevant clearing goal classify:

- `VERIFIED` — current football evidence gives a concrete, repeatable mechanism;
- `PARTIAL` — plausible but materially dependent on optimistic tail / unresolved state;
- `NONE` — no credible prospective funding;
- `NOT_REQUIRED` — only when the supported line does not require that goal.

Funding source:

- `CARRIER`;
- `SECOND_ROUTE`;
- `FORCED_CHAOS`;
- `MIXED`;
- `NONE`.

Every funding state must include a short evidence basis.

### Goal 3

For any supported line >= O2.0:
- goal3 funding must not be `NOT_REQUIRED`.

### Goal 4

For supported line >= O3.0:
- goal4 funding must not be `NOT_REQUIRED`.

For supported line < O3.0:
- goal4 funding = `NOT_REQUIRED`;
- goal4 funding source = `NONE`.

## 5. Funding-source integrity

### CARRIER

A VERIFIED carrier-funded clearing goal requires:
- STRONG carrier;
- carrier_self_fund = true;
- independent_upper_tail = true;
- no material suppression attacking the carrier.

### SECOND_ROUTE

A VERIFIED second-route-funded clearing goal requires:
- second_route_role = BURDEN_CONTRIBUTING;
- weaker route at least USABLE;
- no unresolved failure mode directly attacking that route.

### FORCED_CHAOS

C3 independently freezes `c3_forced_chaos_verified = true/false` plus a non-empty `c3_forced_chaos_basis`.

A VERIFIED forced-chaos clearing goal requires:
- `c3_forced_chaos_verified = true`;
- tournament/game-state mechanism prospectively verified from the common factual evidence;
- no unresolved incentive-integrity state.

Do not inherit Football C's `completion_mode` or `continuation_quality` labels to satisfy this rule.

### MIXED

A VERIFIED mixed source requires at least two independently credible funding contributors. Do not use MIXED merely because both teams can score once.

## 6. Control-endpoint risk

Classify:

- `LOW`;
- `MEDIUM`;
- `HIGH`.

Question:

> Is 1-1, 2-0 or 0-2 a natural endpoint from which the match can settle/control without a verified reason to produce the clearing goal?

Evidence can include:
- score-control behavior;
- failure mode;
- tactical asymmetry;
- opponent suppression;
- draw utility / table utility;
- recent repeatable two-goal endpoints;
- H2H only when transferable.

A scoreline pattern alone does not prove causality, but prospectively corroborated control behavior may raise risk.

C3-FOCUS requires LOW control-endpoint risk.

MEDIUM caps at C3-WATCH / C3-RESERVE.

HIGH is C3-PASS / C3-STOP unless a separately verified forced-chaos state explicitly invalidates the control endpoint.

## 7. C3 screen / board state

### C3-FOCUS

Requires:
- required clearing-goal funding = VERIFIED;
- control-endpoint risk = LOW;
- no material suppression;
- failure mode does not directly attack the clearing-goal mechanism;
- route reliability >= MEDIUM;
- evidence confidence = HIGH.

Two routes are not required.

### C3-WATCH

Use when:
- required funding = PARTIAL; or
- control endpoint = MEDIUM; or
- evidence confidence = MEDIUM; or
- mechanism is credible but one material uncertainty remains.

### C3-PASS

Use when:
- required funding = NONE; or
- control endpoint = HIGH without verified forced-chaos escape; or
- material suppression attacks the clearing-goal mechanism; or
- evidence is insufficient to specify a funding source.

## 8. Supported burden

C3 independently freezes `c3_supported_line` before price and persists a non-empty `supported_line_basis`.

The line must be consistent with the funding proof:

- O2.0–O2.75 requires a credible goal-3 path;
- O3.0+ requires goal-3 and goal-4 paths.

Do not copy C or C2 supported line.

If independent C3 line cannot be frozen:

`C3 COMPARISON INCOMPLETE — SUPPORTED BURDEN NOT INDEPENDENTLY FROZEN`

## 9. Ranking

Rank C3 survivors by:

1. required clearing-goal funding state;
2. lower control-endpoint risk;
3. verified funding-source independence;
4. carrier self-fund / independent upper tail;
5. BURDEN_CONTRIBUTING second route only;
6. failure resistance;
7. route reliability;
8. chance quality;
9. evidence confidence;
10. burden protection;
11. lower supported burden as a late comparator.

No positive term exists for TWO_SIDED or "two usable routes" by itself.

## 10. Shadow lane

C3-FOLLOW — SHADOW requires:
- C3-FOCUS;
- required funding VERIFIED;
- control endpoint LOW;
- failure resistance HIGH;
- evidence confidence HIGH;
- supported line <= O3.0.

C3-RESERVE — SHADOW:
- C3-WATCH with PARTIAL funding or MEDIUM control risk; or
- C3-FOCUS with one MEDIUM non-core quality dimension.

C3-STOP — SHADOW otherwise.

C3 shadow lane never changes Football C operational FOLLOW/RESERVE/STOP.

## 11. Step-2 action

C3 uses the same confirmed XI/current quote epoch as C/C2 when that fixture is already being assessed.

Recheck:
- second-route role;
- goal3 funding/source;
- goal4 funding/source when required;
- control-endpoint risk;
- funding mechanism integrity.

C3 direct shadow BET requires:
- frozen/current C3-FOCUS;
- current required funding VERIFIED;
- current control endpoint LOW;
- primary mechanism intact;
- no material veto;
- quote at/below C3 supported line;
- normal price >=1.65, or the same 1.60–1.64 top-focus soft-zone rule used by Football C.

C3 has no C2-style market-gap bridge.

If the current quote is above C3 supported burden, C3 may WAIT — SHADOW only when the original funding mechanism remains intact and a realistic target is reachable.

## 12. Live

C3 live handling is comparison-only and only for a predeclared C3-WAIT on a fixture already in the normal live workflow.

A goal/red/material incentive change creates a new C3 funding/control epoch.

C3 live resolution does not require shots, xG, big chances, dangerous attacks, possession, corners, box entries or other provider live-stat telemetry. The absence of positive live stats cannot downgrade funding/control by itself.

No opportunistic C3-only live exposure.

## 13. Primary experiment

The primary C3 endpoint is **selection quality**, not extra exposure.

Measure:
- two-goal endpoint rate;
- supported-line settlement;
- same-kickoff priority inversions;
- how often C/C2 promote TWO_SIDED/MIXED while C3 classifies the second route EXCHANGE_ONLY/STATE_DEPENDENT;
- carrier-led clears that C3 preserves;
- false negatives caused by C3 being too strict.

C3 must be judged against C on the same prospectively frozen boards.

## 14. No hindsight tuning

The recent two-goal cluster motivates C3 but has zero confirmatory C3 weight.

Do not import Leyton, Fiorentina, Reading, Bosnia-Sweden, Faroe-Slovakia or other historical outcomes into C3 thresholds.

They are design motivation only.

## 15. Promotion boundary

C3 cannot replace C from a handful of examples.

Any promotion requires:
- predeclared prospective board window;
- complete paired C vs C3 board records;
- no material process contamination;
- better selection quality without unacceptable false-negative inflation;
- separate review of C2 results.

Until then:

`FOOTBALL C3 — SHADOW ONLY`
