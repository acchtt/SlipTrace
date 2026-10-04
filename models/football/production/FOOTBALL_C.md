# Football C — Production Model

**Status:** ACTIVE OFFICIAL MODEL  
**Architecture:** integrated end-to-end football screening, ranking and execution  
**Intake:** RESEARCHABLE_SENIOR_PRODUCTION

## 1. Production flow

`AISCORE SENIOR UNIVERSE -> OPERATIONAL VIABILITY -> RESEARCHABILITY/CAPACITY -> C SCREEN -> C RESEARCH/ASSESS -> BURDEN-COMPLETION FREEZE -> C RANK -> SAME-KICKOFF COMPARISON -> C XI CONFIRMATION -> C-BET/C-WAIT/C-PASS -> WAIT RESOLUTION -> AUDIT`

Football C is deliberately integrated. Do not rebuild Football A's multi-gate architecture inside C.

## 2. Researchable-senior intake

Step 0 must first discover the senior slate broadly, then apply:

1. hard scope/identity/time exclusions;
2. the mandatory **operational viability gate** in `models/football/procedures/FOOTBALL_OPERATIONAL_VIABILITY_GATE.md`;
3. a cheap **researchability gate**;
4. the 15-fixture normal Work admission cap.

Only operational grade A/B fixtures enter the normal Football C board. A can receive normal FOLLOW/RESERVE treatment. B is conditional and is capped at RESERVE at board time. C/D are excluded before Work unless explicitly reopened by the user.

Protected senior international qualifiers/tournaments and major continental club competitions bypass the ordinary domestic researchability exclusion when identity/time are valid, but they do not bypass the operational viability declaration.

Ordinary domestic/small competition fixtures are admitted only when current evidence is sufficient to support the Football C research schema:

- recent team evidence for both sides;
- meaningful current competition context;
- at least one usable mechanism/stat/news layer beyond bare final scores.

A competition must not be excluded merely because it is historically low-scoring, unfamiliar, a lower professional division, a cup, Japanese/Finnish, or women's football. Senior women's domestic top-flight leagues are a mandatory Step-0 discovery class and use the same viability/researchability standard as men's senior top flights. They should reach Football C only when they are both sufficiently researchable **and operationally viable**.

Conversely, a small/obscure competition with inadequate current evidence should be excluded as:

`INSUFFICIENT RESEARCHABILITY — STEP0 EXCLUDED`

Football C still owns **football-quality** rejection and records that as C-PASS.

## 3. Integrated screen

A fixture survives serious consideration when there is at least one credible current scoring route **and a credible path to completing the protected burden**.

Read and apply `models/football/procedures/FOOTBALL_BURDEN_COMPLETION_SELECTION.md`.

Do not equate "both teams can score" with an Over thesis. Explicitly identify where the goal that clears the supported burden comes from.

A WEAK second scoring route is not automatically suppressive when a STRONG carrier can self-fund and the opponent materially leaks.

C-PASS when dominated by weak/uncertain routes, strong current suppression without a credible carrier, poor evidence quality, matchup/incentive compression, unsupported burden, or LOW burden-completion/continuation quality.

Do not keep weak fixtures merely to fill a board. There is no predictive target board size; the upstream operational handoff is separately capped at 15 to control research workload.

## 4. Football assessment

For each admitted fixture determine:

### Routes
Per team: `STRONG / USABLE / WEAK`.

Use actual scoring mechanisms: creation, finishing, service, transition, set pieces, box/territorial pressure, and repeatable opponent leakage. Scorelines support but do not create a route.

### Carrier
`STRONG CARRIER / USABLE CARRIER / NO RELIABLE CARRIER`.

Carrier is football evidence, not market-derived.

### Chance quality
Prefer high-value chances, box/central access, quality SOT, xG/xGOT in context, dangerous transitions or credible data-poor equivalents. Possession/corners/raw shots do not substitute for chance quality.

### Burden completion / continuation
Freeze:
- completion mode = NONE / TWO_SIDED / CARRIER_LED / FORCED_CHAOS / MIXED;
- burden completion quality = LOW / MEDIUM / HIGH;
- continuation quality = LOW / MEDIUM / HIGH;
- opponent leakage = LOW / MEDIUM / HIGH;
- burden stall risk = LOW / MEDIUM / HIGH.

A plausible 1-1 is not HIGH completion for O2.5+. A carrier-led 3-0/4-0 path may be stronger than a balanced two-route match when the carrier can self-fund and the opponent leaks.

### Main failure
State the primary failure mechanism: compression, resistance, route disappearance, class-gap control, incentive, venue-specific suppression, or creation/finishing weakness.

### Tournament format & incentive
For any cup, tournament, qualifier, two-leg tie, final-round group/league state, or user-declared exception, run:
`models/football/procedures/FOOTBALL_TOURNAMENT_INCENTIVE_INTEGRITY.md`

Explicitly separate route quality from incentive/persistence. Verify draw resolution, aggregate/table state, qualification conditions, tiebreak/margin incentives, and whether a likely score state actually forces either side to chase.

A strong XI does not by itself justify a higher total when parity, aggregate protection, direct penalties, or another control state is strategically acceptable.

For an applicable tournament fixture, `LIMITED` or `UNKNOWN` incentive resolution is a **hard incompleteness state**, not a downgrade. Do not assign C-PASS/WATCH/FOCUS, C2 state, or an official supported burden until the exact qualification/tiebreak/margin/simultaneous-result implications are resolved.

### H2H
H2H is mandatory context when usable.

Read and apply:
`models/football/procedures/FOOTBALL_SEMANTIC_DECISION_BASIS.md`

Priority:
`CURRENT MECHANISM -> RECENT SAME-VENUE TRANSFERABLE H2H -> RECENT ALL-VENUE TRANSFERABLE H2H -> OLD BACKGROUND`

Here, `recent` is a research-priority label, not a hidden numerical pass/fail cutoff. Football C has no active fixed match-count/year recency threshold.

H2H never creates a route. Suppressive H2H materially downgrades only when the researcher records both why it is transferable to the current matchup and which current football evidence independently corroborates the same suppressive mechanism.

Every H2H declaration must carry a non-empty `h2h_basis`. If transferability/current corroboration is not established, H2H may remain LIMITED / NOT_USABLE / not material but may not silently create `material_suppression=true`.

## 5. Supported burden

Choose one protected Asian-total line or narrow range before current price.

Persist a non-empty `supported_line_basis` explaining why this is the highest burden supported without requiring an optimistic tail. The basis is audit evidence only and has no independent ranking weight.

Question:
> What is the highest total the football evidence supports without requiring an optimistic tail?

Never raise burden for better price.

For tournament/cup contexts, a post-XI burden increase is allowed only when the XI/mechanism evidence supports it **and** the verified tournament incentive does not materially suppress persistence.

If tournament incentive is LIMITED/UNKNOWN, there is no actionable protected burden. Block the fixture as `INCENTIVE-INCOMPLETE` until the state is resolved; do not carry a provisional burden into Step 2.

## 6. Ranking

Rank survivors by:
1. burden-completion quality;
2. continuation quality;
3. lower stall risk;
4. self-funded independent upper-tail path;
5. carrier strength;
6. opponent leakage;
7. burden protection;
8. lower supported burden when completion quality is otherwise comparable;
9. route reliability;
10. current chance quality;
11. failure resistance;
12. evidence confidence;
13. XI robustness;
14. independent-route quality.

Two-sidedness is one completion mode, not a ranking advantage by itself.

States:
- `C-FOCUS`
- `C-WATCH`
- `C-PASS`

Persist a non-empty `board_state_basis` for the frozen state. This makes the existing semantic screen auditable; it does not create a new numerical FOCUS/WATCH/PASS threshold.

Persist every admitted fixture, including C-PASS, so false negatives can be audited.

Before finalizing C-PASS, apply the carrier-contradiction check from the burden-completion procedure. A HIGH-completion/HIGH-continuation STRONG self-funded carrier with upper-tail proof and opponent leakage cannot be passed solely because the second scoring route is weak.

After ranking, compare fixtures sharing the exact kickoff minute. At most two may receive routine FOLLOW at that kickoff; otherwise-qualified overflow falls to RESERVE subject to capacity.

## 7. XI confirmation

When XI/current odds arrive:
1. verify fixture/status;
2. map XI changes to route functions;
3. run one mandatory fresh fixture-specific public-web football research pass;
4. run the mandatory Asian-total market-history attempt from `FOOTBALL_MARKET_HISTORY_RECHECK.md`;
5. verify/recheck tournament format and incentive state when applicable;
6. re-check relevant H2H/matchup evidence;
7. recheck completion mode, burden-completion quality, continuation quality, opponent leakage and stall risk;
8. run any market-history conflict reinspection;
9. classify thesis PRESERVED / DEGRADED / BROKEN;
10. interpret the executable market;
11. issue C-BET / C-WAIT / C-PASS.

Market-history/odds lookup does not satisfy the football-research requirement. The market-history attempt is nevertheless mandatory and must be declared FOUND / PARTIAL / UNAVAILABLE-ATTEMPTED.

## 8. Market interpretation

The bookmaker is evidence, not authority.

If market is above supported burden, do not buy unsupported burden. WAIT only when protected target can arrive without expected thesis deterioration.

If market is below supported burden, ask whether current football evidence explains the pessimism. If yes and mechanism is attacked, downgrade/PASS. If no, lower line may be useful protection.

No standalone market-undercut HOLD state.

## 9. Price

- >=1.65 normal acceptable zone.
- 1.60–1.64 soft zone only for top-ranked C-FOCUS at/below supported burden with no material football veto.
- <1.60 normally WAIT/PASS.

## 10. Final action

### C-BET
Football thesis survives; line at/below supported burden; price acceptable; no material football veto.

### C-WAIT
Thesis already good enough; current line/price is blocker; protected target realistically reachable without expected negative football information.

Predeclare target line, minimum odds, cancellation event, and thesis-health evidence required.

### C-PASS
Thesis inadequate, burden unsupported, price unacceptable without healthy wait path, or wait depends on thesis deterioration.

## 11. Decay integrity

`PRICE DECAY != THESIS DECAY`

At target:
`TARGET REACHED + PREMATCH/XI THESIS NOT MATERIALLY INVALIDATED?`

Do **not** require positive live-stat confirmation for a scoreless Over wait. Shots, xG/xGOT, big chances, dangerous attacks, possession, corners, box entries and momentum feeds are not live execution gates.

No-goal clock decay by itself is not thesis decay.

Cancel only when concrete football information materially damages the frozen mechanism or incentive state:
`C-WAIT CANCELLED — THESIS DECAY`

## 12. Live boundary

Normal live use resolves a predeclared C-WAIT; an explicit match-specific exception may reopen a live fixture under the normal exception boundary. A goal/red card/major injury/material mechanism change invalidates the old quote and creates a new epoch.

Live assessment proceeds regardless of provider live stats. Current score/minute/line/odds plus preserved prematch/XI football evidence are sufficient unless a separate integrity gate is unresolved.

For tournament/cup fixtures, every new epoch must also recompute score/aggregate/table incentive: whether a draw is acceptable, whether penalties/extra time are reachable, whether margin is still required, and which side is genuinely forced to chase.

## 13. Persistence

Model identifier: `Football C`.

Daily Coverage Ledger must retain the full C funnel, including C-PASS.

Decision States store material Step-2/live decisions.

Website Picks store official C-BET exposure.

User bet slip remains physical execution truth.

Never overwrite historical Football A records.

## 14. Audit

Audit:
`RAW SENIOR -> HARD EXCLUDED -> OPERATIONAL EXCLUDED -> RESEARCHABILITY EXCLUDED -> CAPACITY DEFERRED -> ADMITTED TO C -> C-PASS -> C-WATCH -> C-FOCUS -> C-BET/C-WAIT`

A skipped visible senior fixture with no disposition is a coverage failure. A documented operational exclusion or capacity deferral is not automatically a model-screen error. A high-scoring admitted C-PASS remains a model-screen false negative. Keep those categories separate.

Never retro-change states from FT.
