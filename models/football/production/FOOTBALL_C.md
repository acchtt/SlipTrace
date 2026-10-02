# Football C — Production Model

**Status:** ACTIVE OFFICIAL MODEL  
**Architecture:** integrated end-to-end football screening, ranking and execution  
**Intake:** RESEARCHABLE_SENIOR_PRODUCTION

## 1. Production flow

`AISCORE SENIOR UNIVERSE -> OPERATIONAL VIABILITY -> RESEARCHABILITY/CAPACITY -> C SCREEN -> C RESEARCH/ASSESS -> C RANK -> C XI CONFIRMATION -> C-BET/C-WAIT/C-PASS -> WAIT RESOLUTION -> AUDIT`

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

A competition must not be excluded merely because it is historically low-scoring, unfamiliar, a lower professional division, a cup, Japanese/Finnish, or women's football. It should reach Football C only when it is both sufficiently researchable **and operationally viable**.

Conversely, a small/obscure competition with inadequate current evidence should be excluded as:

`INSUFFICIENT RESEARCHABILITY — STEP0 EXCLUDED`

Football C still owns **football-quality** rejection and records that as C-PASS.

## 3. Integrated screen

A fixture survives serious consideration when there is at least one credible current scoring route to a useful Over environment and enough evidence to assess it.

C-PASS when dominated by weak/uncertain routes, strong current suppression without a credible carrier, poor evidence quality, matchup/incentive compression, or unsupported burden.

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

Priority:
`CURRENT MECHANISM -> RECENT SAME-VENUE TRANSFERABLE H2H -> RECENT ALL-VENUE TRANSFERABLE H2H -> OLD BACKGROUND`

H2H never creates a route. Suppressive H2H materially downgrades only when transferable and corroborated by current football evidence.

## 5. Supported burden

Choose one protected Asian-total line or narrow range before current price.

Question:
> What is the highest total the football evidence supports without requiring an optimistic tail?

Never raise burden for better price.

For tournament/cup contexts, a post-XI burden increase is allowed only when the XI/mechanism evidence supports it **and** the verified tournament incentive does not materially suppress persistence.

If tournament incentive is LIMITED/UNKNOWN, there is no actionable protected burden. Block the fixture as `INCENTIVE-INCOMPLETE` until the state is resolved; do not carry a provisional burden into Step 2.

## 6. Ranking

Rank survivors by:
1. reliable path to supported total;
2. independent routes/self-funded carrier;
3. current chance quality;
4. failure resistance;
5. XI robustness when known;
6. burden protection;
7. evidence confidence.

States:
- `C-FOCUS`
- `C-WATCH`
- `C-PASS`

Persist every admitted fixture, including C-PASS, so false negatives can be audited.

## 7. XI confirmation

When XI/current odds arrive:
1. verify fixture/status;
2. map XI changes to route functions;
3. run one mandatory fresh fixture-specific public-web football research pass;
4. verify/recheck tournament format and incentive state when applicable;
5. re-check relevant H2H/matchup evidence;
6. classify thesis PRESERVED / DEGRADED / BROKEN;
7. interpret the executable market;
8. issue C-BET / C-WAIT / C-PASS.

Market-history/odds lookup does not satisfy the football-research requirement.

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
`TARGET REACHED + THESIS STILL HEALTHY?`

For scoreless Over waits, no-goal/no-red-card alone is insufficient. Require contemporaneous attacking-quality evidence.

If price improved because attack went stale:
`C-WAIT CANCELLED — THESIS DECAY`

## 12. Live boundary

Normal live use resolves a predeclared C-WAIT. A goal/red card/major injury/material mechanism change invalidates the old quote and creates a new epoch.

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
