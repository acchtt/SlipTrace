# Football C — Production Model

**Status:** ACTIVE OFFICIAL MODEL  
**Effective:** 2026-09-29 ICT by explicit user directive  
**Predecessor:** Football A  
**Architecture:** integrated end-to-end football screening, ranking and execution

Football C is the production football model. It replaces Football A for all new boards and new decision epochs after activation.

This activation is **user-directed before completion of the planned prospective shadow test**. It is not represented as a statistically validated QA promotion. Historical Football A decisions remain historically valid and must never be relabelled as Football C.

## 1. Production flow

`AISCORE FIXTURE UNIVERSE -> C SCREEN -> C RESEARCH/ASSESS -> C RANK -> C XI CONFIRMATION -> C BET / WAIT / PASS -> LIVE WAIT RESOLUTION -> SETTLEMENT/AUDIT`

Football C is deliberately integrated. Do not rebuild Football A's multi-gate architecture inside C.

There is no independent:
- HMA gate;
- carrier-market-decomposition gate;
- priority-inversion gate;
- market-undercut veto;
- execution-class compiler;
- upper-tail committee;
- separate PRE-vs-Step-2 model hierarchy.

Those concepts may be considered as evidence where relevant, but the final decision is one integrated football judgment.

## 2. Fixture and scope authority

AiScore remains the fixture-discovery authority.

Apply the shared production identity/time/scope protections:
- verify fixture identity, home/away, kickoff and status;
- preserve source time and convert exactly once to ICT;
- senior first-team football only unless an explicit current exception exists;
- exclude youth/Uxx, academy, reserves/B/development, amateur/semi-pro, regional/state/provincial and currently excluded low-quality scope families;
- do not create fixtures from secondary research sources.

Step 0 remains responsible for the complete actionable handoff.

## 3. Integrated screen

A fixture survives when there is at least one credible current scoring route to a useful Over environment and enough evidence to research it confidently.

PASS early when dominated by:
- weak/uncertain scoring routes on both sides;
- strong current suppression with no credible carrier;
- poor evidence quality;
- matchup/incentive conditions that materially reduce the goal path;
- a required burden that lacks a realistic protected expression.

Do not keep weak fixtures merely to fill a board. There is no target board size.

## 4. Football assessment

For every researched fixture determine:

### Routes
Per team:
- `STRONG`
- `USABLE`
- `WEAK`

Use mechanisms: creation, finishing, service, transition, set pieces, territorial/box pressure, and repeatable opponent leakage. Scorelines support a route but never create one by themselves.

### Carrier
- `STRONG CARRIER`
- `USABLE CARRIER`
- `NO RELIABLE CARRIER`

A carrier is a football conclusion, not a market-derived label.

### Chance quality
Prefer high-value chances, box/central access, quality SOT, xG/xGOT in context, repeatable dangerous transitions, or credible data-poor equivalents. Raw possession/corners/shot counts cannot substitute for chance quality.

### Main failure mode
State the single most important way the Over thesis can fail: tactical compression, opponent resistance, route disappearance, class-gap control, first-leg/final incentive, venue-specific suppression, or current finishing/creation weakness.

### H2H
H2H is mandatory context when usable.

Priority:
`CURRENT MECHANISM -> RECENT SAME-VENUE TRANSFERABLE H2H -> RECENT ALL-VENUE TRANSFERABLE H2H -> OLD BACKGROUND`

H2H never creates a route. Suppressive H2H materially downgrades only when reasonably transferable and corroborated by current football evidence.

## 5. Supported burden

Choose a protected Asian-total line or narrow range **before current price**.

Question:

> What is the highest total supported by the football evidence without requiring an optimistic tail?

Prefer useful quarter/whole-line protection. Never raise burden just to obtain a better price.

Persist:
- supported line;
- optional ceiling;
- concise football basis.

## 6. Ranking

Rank survivors directly against each other using:

1. reliable path to supported total;
2. independent route quality / self-funded carrier;
3. current chance quality;
4. failure-mode resistance;
5. XI robustness when known;
6. burden protection;
7. evidence confidence.

Price does not create structural rank.

Board states:
- `C-FOCUS`
- `C-WATCH`
- `C-PASS`

Persist ordinal rank plus board state. Map C-FOCUS/WATCH/PASS to the existing Coverage Board Tier field where needed; preserve C terminology in Frozen PRE Summary.

## 7. XI + current evidence — one confirmation pass

When confirmed XI and current odds arrive:

1. verify fixture/status;
2. map XI changes to route functions;
3. run **one mandatory fresh fixture-specific public-web football research pass**;
4. re-check H2H/matchup when material;
5. classify the original thesis as `PRESERVED`, `DEGRADED`, or `BROKEN`;
6. interpret the supplied executable market;
7. issue one final action.

Do not split these into separate veto committees.

A final prematch `C-BET` is forbidden if fresh post-XI football research was skipped. Market-history/odds lookup does not satisfy the football-research requirement.

## 8. Market interpretation

The bookmaker is evidence, not authority.

### Market above supported burden
Do not buy unsupported extra burden.

WAIT only when the supported target is realistically reachable **without requiring the football thesis to deteriorate**. Otherwise PASS.

### Market below supported burden
Treat the undercut as a warning, not an automatic veto.

Ask:
> Is there current football evidence explaining why the market is more pessimistic?

If the answer is YES and it attacks the mechanism, downgrade/PASS.

If NO and the football thesis remains intact, the lower line may be valuable protection.

Do not create a standalone market-undercut HOLD state.

## 9. Price

Production price policy:
- `>=1.65`: normal acceptable zone;
- `1.60–1.64`: soft zone, eligible only for a top-ranked C-FOCUS candidate at/below supported burden with no material football veto;
- `<1.60`: normally WAIT or PASS.

Price cannot create football quality and cannot justify higher burden.

## 10. Final action

Football C has only three decision states.

### C-BET
Use when:
- football thesis survives;
- selected line is at/below supported burden;
- price clears Section 9;
- no material current football veto remains.

Record exact line, odds, timestamp and evidence epoch.

### C-WAIT
Use only when:
- thesis is already strong enough;
- current line/price is the blocker;
- a specific protected target is realistically reachable;
- waiting is not expected to require negative football information.

Predeclare:
- target line;
- minimum odds;
- cancellation event;
- thesis-health evidence required when target appears.

### C-PASS
Use when the football thesis is not good enough, available burden is unsupported, price is unacceptable without a healthy wait path, or the wait would depend on thesis deterioration.

## 11. Decay integrity

`PRICE DECAY != THESIS DECAY`

A WAIT never auto-executes because the number appears.

At target:

`TARGET REACHED + THESIS STILL HEALTHY?`

For scoreless Over waits, no-goal/no-red-card is insufficient. Require contemporaneous evidence that the scoring mechanism still functions, such as:
- credible high-value chances;
- repeated dangerous central/box entries;
- threatening keeper work / quality SOT;
- dangerous transitions producing quality final actions;
- another fixture-specific mechanism identified in the original C thesis.

If the price improved because attacking quality has gone stale:

`C-WAIT CANCELLED — THESIS DECAY`

Do not keep chasing progressively lower lines without a genuinely new positive scoring epoch.

## 12. Live boundary

Football C is not an opportunistic live-selection model.

Normal live use is only:
- resolve a predeclared C-WAIT;
- re-evaluate after a material event when the user explicitly asks.

A goal, red card, major injury, or material mechanism change invalidates the old quote. Reassess the football thesis; never mechanically carry the old decision through the event.

## 13. Required board output

| Rank | Match | C state | Routes | Carrier | Supported line | Main failure | Initial action |
|---|---|---|---|---|---|---|---|

Keep explanations compact and integrated.

## 14. Required XI/odds output

`#rank MATCH — C-BET / C-WAIT / C-PASS`

Then:
- XI: PRESERVED / DEGRADED / BROKEN
- Fresh research: FOUND / LIMITED / UNAVAILABLE-ATTEMPTED
- H2H: compact state when material
- Supported line
- Current executable line/odds
- Integrated reason
- WAIT target/cancellation/thesis-health requirement when applicable

## 15. Persistence

Model identifier:
`Football C`

For every material Step-2 decision, persist a Decision State with the current action and evidence.

For every official C-BET:
1. persist Decision State;
2. create/update the corresponding Website Pick;
3. reconcile fixture/model/line/odds/stake/evidence epoch/timestamps;
4. prevent duplicate active official picks.

Airtable Decision State = model decision history.  
Website Pick = model official exposure record.  
User bet slip = physical execution truth and supersedes model records when auditing what was actually placed.

Do not overwrite historical Football A records.

## 16. Audit rules

Audit C using exact historical C states.

Separate:
- C-BET direct;
- C-WAIT reached and executed;
- C-WAIT cancelled for thesis decay;
- C-WAIT never reached;
- C-PASS;
- actual user execution deviations.

Never award hypothetical P/L to a C-WAIT/C-PASS unless an exact contemporaneous executable quote was actually frozen as a shadow/counterfactual audit state. Never rewrite a decision because of FT.

## 17. Football A status

Football A is retired from new production decisions as of Football C activation.

Football A files remain in the repository for historical audit and rollback only. They are not part of the Football C load order.

Restore point:
- branch `archive/pre-football-c-active-2026-09-29`
- snapshot `models/football/backups/2026-09-29_2038_current_model_snapshot/`
