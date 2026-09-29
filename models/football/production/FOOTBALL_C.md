# Football C — Production Model

**Status:** ACTIVE OFFICIAL MODEL  
**Architecture:** integrated end-to-end football screening, ranking and execution  
**Intake:** BROAD_SENIOR_PRODUCTION

## 1. Production flow

`AISCORE BROAD SENIOR UNIVERSE -> C SCREEN -> C RESEARCH/ASSESS -> C RANK -> C XI CONFIRMATION -> C-BET/C-WAIT/C-PASS -> WAIT RESOLUTION -> AUDIT`

Football C is deliberately integrated. Do not rebuild Football A's multi-gate architecture inside C.

## 2. Broad-senior intake

Step 0 must send every reasonable senior first-team fixture in the requested window to Football C after only hard scope/identity/time exclusions.

Legacy league registries, LOW-GOAL exclusions, country-wide exclusions, professional-lower-division exclusions and small-cup filters may not remove an otherwise reasonable senior fixture before C sees it.

Professional lower divisions, senior cup blocks, senior women's first-team blocks and unfamiliar senior competitions are C-screenable unless they fail a hard scope/identity rule.

Football C owns football-quality rejection and records it as C-PASS.

## 3. Integrated screen

A fixture survives serious consideration when there is at least one credible current scoring route to a useful Over environment and enough evidence to assess it.

C-PASS when dominated by weak/uncertain routes, strong current suppression without a credible carrier, poor evidence quality, matchup/incentive compression, or unsupported burden.

Do not keep weak fixtures merely to fill a board. No target board size.

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
4. re-check relevant H2H/matchup evidence;
5. classify thesis PRESERVED / DEGRADED / BROKEN;
6. interpret the executable market;
7. issue C-BET / C-WAIT / C-PASS.

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

## 13. Persistence

Model identifier: `Football C`.

Daily Coverage Ledger must retain the full C funnel, including C-PASS.

Decision States store material Step-2/live decisions.

Website Picks store official C-BET exposure.

User bet slip remains physical execution truth.

Never overwrite historical Football A records.

## 14. Audit

Audit:
`RAW SENIOR -> HARD EXCLUDED -> ADMITTED TO C -> C-PASS -> C-WATCH -> C-FOCUS -> C-BET/C-WAIT`

A missing reasonable senior fixture is a coverage failure. A high-scoring C-PASS is a model-screen false negative. Keep those categories separate.

Never retro-change states from FT.
