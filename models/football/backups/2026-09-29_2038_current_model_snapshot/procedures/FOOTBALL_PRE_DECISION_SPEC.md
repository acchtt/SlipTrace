# Football A — Compiled PRE Decision Specification

**Status:** ACTIVE OPERATIONAL COMPILER  
**Stage:** Step 1 / Work structural PRE only  
**Model:** Football A current official stack  
**Purpose:** make repeated PRE assessments deterministic without changing the football model.  
**Price policy:** PRICE-BLIND  
**Confirmed-XI policy:** CONFIRMED-XI-BLIND  
**Authority:** final operational authority for Step-1 PRE classification, board tier, supported-burden construction discipline, PASS rescue, and PRE Structural Rank where older active files overlap or use ambiguous ordering.

This file **compiles** the active rules. It is not a new predictive patch and does not retroactively change any frozen historical PRE state, rank, verdict, exposure, or P/L.

If this file conflicts with older Step-1 wording about route-symmetry priority, carrier ranking, PRE use of confirmed XI, PASS rescue, or the order of PRE judgment, use this file for Step 1. Later Step-2 XI/market execution rules remain governed by their own active authorities.

---

## 1. Fixed Step-1 decision order

Every Work-admitted fixture must execute this exact order:

`SCOPE/HANDOFF PASS -> EVIDENCE PACKET -> HOME ROUTE -> AWAY ROUTE -> SECOND-ROUTE INDEPENDENCE -> PRACTICAL CARRIER -> FAILURE/VETO -> STRUCTURAL GRADE -> BOARD TIER -> PASS RESCUE IF NEEDED -> SUPPORTED BURDEN -> PRE RANK FACTORS -> CROSS-MATCH RANK -> FREEZE`

Do not:
- rank before every fixture has a frozen PRE state;
- use price, Asian total, 1X2, handicap, market movement, or confirmed XI to improve PRE;
- let a later positive compensate for an earlier hard failure;
- infer missing evidence as positive evidence;
- change an earlier route state merely to make the final grade/rank look coherent.

---

## 2. Mandatory evidence packet

Each team route is evaluated from the same evidence-channel schema. Investigators may return `UNKNOWN`; they must not substitute a different easier metric just because one source is missing.

### Positive route-owned channels

- **CQ — Chance quality / creation:** current big chances, xG/xGOT, high-value shots, central/box access, quality SOT, sustained dangerous creation, or a documented equivalent.
- **REP — Repeatability:** repeated current scoring/creation against relevant resistance in the relevant home/away/competition context. One isolated high score is not repeatability.
- **MECH — Independent mechanism:** a football mechanism by which the team itself can create goals without requiring opponent collapse first: press/territory, transition, wide overload, central combinations, set pieces, class-gap pressure, etc.
- **CTX — Relevant-context support:** home/away split, competition level, opponent class, incentive/format, and schedule context showing that CQ/REP/MECH is applicable to this match.

### Supporting-only channels

These may support a route but cannot independently create SUPPORTED/PROVEN status:

- **OPP — Opponent leakage/failure compatibility**
- **FORM — raw GF/GA, recent scorelines, Over/BTTS frequency**
- **NAME — reputation, player names, expected attacking talent**
- **H2H — historical scorelines without a current mechanism match**
- **STATE — hypothetical chase/game-state assumption**

### Negative channels

- **SUPPRESS — current chance-quality suppression / repeated low-urgency control**
- **MECH_BREAK — opponent specifically removes the required mechanism**
- **ROLE_RISK — known pre-XI structural dependency on uncertain personnel/role**
- **FATIGUE_ROTATION — known schedule/rotation context materially lowering the route**
- **DATA_CONFLICT — credible sources materially disagree on the route evidence**

### No double counting

One underlying fact can support only one primary channel. Example: five recent 3-2 scorelines cannot be counted separately as REP, CQ, and MECH unless independent evidence actually establishes those channels.

---

## 3. Deterministic route-state compiler

Grade HOME and AWAY separately.

### PROVEN

A route is `PROVEN` only when:

1. **CQ = PASS**, and
2. **REP = PASS**, and
3. CTX does not make those signals materially irrelevant to the current fixture, and
4. there is no HARD VETO against that route.

MECH should normally be identifiable; if CQ + REP are strong but MECH is unclear, cap evidence confidence rather than inventing a mechanism.

### SUPPORTED

A route is `SUPPORTED` when PROVEN does not clear, but:

1. at least **two independent route-owned positive channels** among CQ / REP / MECH clear at usable strength; and
2. at least one of those channels is CQ or MECH; and
3. the route is not supported mainly by OPP / FORM / NAME / H2H / STATE; and
4. there is no HARD VETO.

### NOMINAL

A route is `NOMINAL` when a plausible contribution exists but SUPPORTED does not clear, including when the case relies mainly on:

- opponent leakage;
- raw GF/GA or score-form;
- BTTS/Over frequency;
- names/reputation;
- H2H;
- isolated high scores;
- lineup-preservation assumptions;
- hypothetical chase/game state.

### FAILED

A route is `FAILED` when:

- a HARD VETO directly defeats the route; or
- current evidence shows the route is materially absent/suppressed; or
- the required mechanism is contradicted rather than merely unknown.

### Data-poor substitute

When detailed CQ data is genuinely unavailable, a route may use a data-poor substitute only if all are present:

1. REP = strong and repeated;
2. MECH = identifiable from credible football evidence;
3. OPP or class-gap compatibility = strong;
4. source quality is adequate and internally consistent.

Any fixture using a data-poor substitute is capped at **A2 maximum** and must persist `DATA-POOR SUBSTITUTE = YES`.

Missing CQ data by itself is not evidence of failure.

---

## 4. Second-route independence compiler

For every A2 two-route candidate, classify the weaker route:

### INDEPENDENT SECOND ROUTE

Requires:

- route state is at least SUPPORTED;
- CQ or MECH is directly owned by that team;
- the route does not materially require opponent collapse, a red card, a chase script, or the stronger team scoring first;
- FORM/BTTS/H2H/leakage are supporting context, not the main proof.

### CONDITIONAL SECOND ROUTE

Use when the weaker route depends materially on leakage, score-form proxy, H2H, venue-only contribution, uncertain personnel, or game-state assumptions.

Confirmed XI is not available in Step 1. Therefore:

- **PROVEN + SUPPORTED:** A2 FOCUS remains possible at PRE only when the SUPPORTED route is INDEPENDENT, has direct route-owned chance/mechanism proof, is not materially XI-sensitive, and the failure/burden gates clear.
- **SUPPORTED + SUPPORTED:** Step-1 maximum is **A2 WATCHLIST**. Promotion to FOCUS may occur only in Step 2 if the active XI-stage rules establish both mechanisms strongly enough and confirmed XI preserves them.
- XI names may never be imagined or assumed at PRE to clear this cap.

---

## 5. Practical carrier compiler

For each team, classify the self-funded 3+ path exactly once:

### PRACTICAL CARRIER CEILING — VERIFIED

All of the following must clear:

1. **Repeatability:** at least two recent 3+ team-goal demonstrations, or one 3+ demonstration plus repeated strong underlying creation compatible with another 3+ output.
2. **Mechanism proof:** a current, repeatable football mechanism is identified.
3. **Independence:** the 3+ route does not require the opponent to score or an abnormal state first.
4. **Compatibility:** either the opponent repeatedly permits the same mechanism **or** the carrier's own current chance-quality evidence is strong enough to make the route substantially opponent-independent.
5. **Integrity:** no known current PRE-stage structural damage or HARD VETO materially breaks the mechanism.
6. **XI sensitivity:** the route is not so dependent on uncertain personnel that confirmed XI is required to know whether the mechanism exists.

Only VERIFIED receives first-order practical-ceiling rank credit or cross-grade B+ > A2 authority.

### PRACTICAL CARRIER CEILING — CANDIDATE

Use when a plausible self-funded 3+ path exists but exactly one or more VERIFIED requirements remain unresolved, especially material XI sensitivity or incomplete chance-quality proof.

CANDIDATE:
- may preserve a later Step-2 reopen;
- may improve monitoring/evidence confidence;
- may not create cross-grade carrier priority at PRE.

### PRACTICAL CARRIER CEILING — UNVERIFIED

Use when the 3+ case rests mainly on favorite status, market reputation, one scoreline, generic opponent leakage, or unsupported projection.

---

## 6. Failure-mode severity compiler

Every fixture gets one dominant failure mode and one severity:

### HARD VETO

A negative is a HARD VETO only when it is:

1. current/relevant;
2. mechanism-compatible with the route/burden being evaluated; and
3. supported by either:
   - two independent negative evidence channels; or
   - one decisive current football fact that directly removes the required mechanism.

Examples may include repeated current control/suppression plus weak CQ, a known tactical/availability fact that removes the sole route, or repeated mechanism-specific matchup suppression.

Historical H2H alone, generic cup caution, generic away risk, or one low-scoring result is never a HARD VETO.

### SOFT PENALTY

Use when the concern is relevant but does not satisfy HARD VETO. It may lower tier, burden, failure resistance, or evidence confidence; it cannot be silently upgraded into a hard block.

### NONE / UNRESOLVED

- `NONE` when no material negative mechanism is identified.
- `UNRESOLVED` when sources conflict or required evidence is missing.

A material unresolved failure question prevents FOCUS.

---

## 7. Structural grade and board-tier matrix

Apply after route states, second-route state, carrier state, and veto state are frozen.

| Route pair | Structural result | Step-1 board rule |
|---|---|---|
| PROVEN + PROVEN | A1 | FOCUS if no HARD VETO, burden path is clear, and evidence confidence is not LOW; otherwise WATCHLIST |
| PROVEN + SUPPORTED | A2 | FOCUS only if weaker route = INDEPENDENT, route-owned CQ/MECH is present, no HARD VETO, burden path clear, and material XI sensitivity is absent; otherwise WATCHLIST |
| SUPPORTED + SUPPORTED | A2 | WATCHLIST maximum at Step 1; Step 2 may promote only under active XI hardening rules |
| PROVEN + NOMINAL | B+ candidate lane | WATCHLIST only when VERIFIED carrier/pass-rescue conditions establish a practical 3+ path; otherwise provisional PASS -> mandatory PASS Rescue Screen |
| SUPPORTED + NOMINAL | B+ | WATCHLIST only when supported burden is constructible and no HARD VETO; otherwise PASS |
| NOMINAL + NOMINAL | B / PASS | PASS |
| any FAILED route | PASS by default | WATCHLIST/B+ only if the opposite route has a VERIFIED self-funded carrier that survives the failed-route branch and supports the total independently |
| material unresolved evidence | UNRESOLVED | never FOCUS |

Grades are ceilings, not positive points. A lower grade may rank above a higher grade only under the active Practical Ceiling Ranking rules after both are legitimately on the FOCUS/WATCHLIST board.

---

## 8. Mandatory PASS Rescue Screen

Before finalizing any provisional B/PASS where:

- either route is PROVEN/SUPPORTED; or
- a plausible carrier/class-gap route exists; or
- weak secondary-route quality is the main reason for PASS,

run exactly one PASS Rescue Screen.

### Rescue to B+ WATCHLIST

Requires:

- at least one PROVEN/SUPPORTED route;
- PRACTICAL CARRIER CEILING = VERIFIED;
- opponent failure compatibility or sufficiently strong own CQ;
- no HARD VETO;
- a supported burden can be constructed.

Persist:

`PASS RESCUE — B+ WATCHLIST — VERIFIED CARRIER`

### Keep PASS — CARRIER CANDIDATE

If carrier = CANDIDATE rather than VERIFIED:

`PASS — CARRIER CANDIDATE / RE-SCREEN ELIGIBLE`

### Keep PASS — STRONG SUPPRESSION VETO

If a HARD VETO is present:

`PASS — STRONG SUPPRESSION VETO`

### Keep PASS — NO PRACTICAL CEILING

If no VERIFIED carrier / supported burden exists:

`PASS — NO PRACTICAL 3+ CEILING`

Run the screen once. Do not recursively rescue a rescue.

---

## 9. Supported-burden compiler

Supported burden is football structure, not price.

Mandatory rules:

1. Build burden from the **reliable 3+ mechanism**, not by adding two weak one-goal routes.
2. A CONDITIONAL second route cannot raise burden by itself.
3. Route symmetry or grade label alone cannot justify O2.75/O3.0.
4. A newly PASS-rescued B+ defaults to **O2.5 maximum** unless an existing active rule independently proves a higher burden.
5. O3.0+ requires the active upper-tail / 4+ path standard.
6. If two active burden interpretations are both plausible from the same evidence, choose the **lower protected burden** and persist `BURDEN AMBIGUITY — LOWER PROTECTED BURDEN USED`.
7. PRE burden is frozen before current market price.

Persist:
- supported burden or range;
- exact football mechanism funding it;
- whether a fourth-goal / upper-tail path is proven;
- whether any part of the burden depends on a conditional second route;
- burden confidence HIGH / MEDIUM / LOW.

LOW burden confidence prevents FOCUS.

---

## 10. Deterministic PRE Structural Rank

Rank only after every FOCUS/WATCHLIST fixture is frozen.

Use the final Practical Ceiling hierarchy **lexicographically**, not as an improvised weighted score:

1. practical self-funded 3+ ceiling;
2. opponent defensive-failure/leakage compatibility with that mechanism;
3. current chance quality + scoring urgency/repeatability;
4. failure-mode resistance at supported burden;
5. secondary-route quality;
6. route symmetry / structural grade as a tie-breaker;
7. supported-burden fit/protection;
8. evidence confidence.

Rules:

- VERIFIED carrier receives first-order self-funded-ceiling credit; CANDIDATE does not.
- A2 FOCUS does not automatically outrank B+ WATCHLIST.
- A B+ VERIFIED carrier may outrank an ordinary A2 when the practical 3+ path is stronger.
- Structural grade is not a monotonic ranking score.
- Price/market data never changes PRE rank.
- When all football rank factors are materially tied, use lower supported burden, then higher evidence confidence, then canonical AiScore fixture ID as a deterministic stable tie-breaker.

Persist the reason for every cross-grade inversion.

---

## 11. Evidence confidence

Assign:

- **HIGH:** required positive/negative channels are current, source-consistent, and include direct football/chance evidence.
- **MEDIUM:** decision clears but one non-critical channel uses a data-poor substitute or has limited sample depth.
- **LOW:** key route, failure, carrier, or burden conclusion depends on incomplete/conflicting evidence.

LOW confidence:
- prevents FOCUS;
- prevents VERIFIED carrier;
- may still allow WATCHLIST when the structural state is otherwise valid;
- becomes UNRESOLVED when the missing item can change grade/tier rather than merely confidence.

Do not turn UNKNOWN into LOW-confidence positive evidence.

---

## 12. Required PRE decision trace

Every Work-admitted fixture must freeze this trace before cross-match ranking:

```yaml
pre_compiler: FOOTBALL_PRE_DECISION_SPEC_V1
fixture_id: <AiScore id>
evidence_epoch: <timestamp>
home_route:
  cq: PASS|PARTIAL|FAIL|UNKNOWN
  rep: PASS|PARTIAL|FAIL|UNKNOWN
  mech: PASS|PARTIAL|FAIL|UNKNOWN
  ctx: PASS|PARTIAL|FAIL|UNKNOWN
  state: PROVEN|SUPPORTED|NOMINAL|FAILED
away_route: <same>
data_poor_substitute: YES|NO
weaker_route: INDEPENDENT|CONDITIONAL|NA
carrier:
  home: VERIFIED|CANDIDATE|UNVERIFIED
  away: VERIFIED|CANDIDATE|UNVERIFIED
dominant_failure:
  label: <text>
  severity: HARD_VETO|SOFT_PENALTY|NONE|UNRESOLVED
pass_rescue: RESCUED_BPLUS|CANDIDATE_PASS|SUPPRESSION_PASS|NO_CEILING_PASS|NA
structural_grade: A1|A2|B+|B|UNRESOLVED
board_tier: FOCUS|WATCHLIST|PASS|UNRESOLVED
tier_cap_reason: <exact reason or NONE>
supported_burden: <value/range or NONE>
burden_basis: <mechanism>
upper_tail_4plus: PROVEN|NOT_PROVEN|NA
burden_confidence: HIGH|MEDIUM|LOW
evidence_confidence: HIGH|MEDIUM|LOW
rank_factors:
  practical_3plus: <state>
  opponent_compatibility: HIGH|MEDIUM|LOW|NA
  chance_quality_urgency: HIGH|MEDIUM|LOW
  failure_resistance: HIGH|MEDIUM|LOW
  secondary_route_quality: HIGH|MEDIUM|LOW|NA
  route_symmetry: HIGH|MEDIUM|LOW
unresolved_items:
  - <item or NONE>
```

The frozen artifact is invalid if this trace is absent for an actionable fixture.

---

## 13. Step-2 boundary

Step 1 never uses confirmed XI or current market price to manufacture a stronger PRE state.

At Step 2:
- confirmed XI may damage or, where an active rule explicitly permits, create a fresh football re-screen epoch;
- SUPPORTED+SUPPORTED A2 WATCHLIST may be reconsidered for FOCUS only under the active two-route XI hardening requirements;
- a CARRIER CANDIDATE may become VERIFIED only with fresh football evidence under the active Step-2 rules;
- market evidence may trigger market-alignment/carrier-decomposition rules but may not retroactively rewrite the frozen Step-1 PRE.

Preserve both frozen PRE and any later current state separately.

---

## 14. Authority

This compiled specification is the final Step-1 operational authority for:

- route-state assignment;
- second-route independence;
- PRE practical-carrier state;
- hard-veto vs soft-penalty classification;
- grade/tier caps;
- PASS rescue;
- supported-burden discipline;
- PRE Structural Rank ordering;
- PRE decision-trace completeness.

It compiles and resolves overlapping Step-1 wording from:
- `MODEL_RULES_FOOTBALL_V0.2.52.md`;
- `MODEL_RULES_FOOTBALL_V0.2.53.md`;
- `MODEL_RULES_FOOTBALL_A.md`;
- `MODEL_RULES_FOOTBALL_A_PRACTICAL_CEILING_RANKING.md`;
- `MODEL_RULES_FOOTBALL_A_PASS_RESCUE.md`;
- `MODEL_RULES_FOOTBALL_A_TWO_ROUTE_HARDENING.md`;
- `FOOTBALL_MATCH_SWEEP_AND_RESEARCH_PROCEDURE.md`;
- `01_WORK_DAILY_SWEEP.md`.

It does **not** replace Step-2 market alignment, XI review, carrier-market decomposition, HMA, decay-first, B+ protected-line execution, exposure, settlement, or post-slate audit authorities.
