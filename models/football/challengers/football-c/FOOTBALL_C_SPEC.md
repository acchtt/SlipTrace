# Football C — Integrated Challenger Specification

**Status:** PROSPECTIVE SHADOW CHALLENGER  
**Champion:** Football A  
**Purpose:** test whether a simpler, integrated v0.2.47-style decision architecture can match or improve Football A while materially reducing stages, latency, and execution-selection failure points.

Football C is not an official betting model. During the trial it may create only shadow decisions and counterfactual settlements. It must never publish an official Website Pick or authorize real exposure.

## 1. Design principle

Football C owns the full football decision from the common raw fixture handoff onward:

`COMMON AISCORE FIXTURE UNIVERSE -> C SCREEN -> C RESEARCH/ASSESS -> C RANK -> C XI CONFIRMATION -> C BET / WAIT / PASS -> C SETTLEMENT`

There is no separate Football-A PRE compiler, execution-class compiler, HMA layer, carrier-market-decomposition layer, priority-inversion layer, or market-alignment gate inside C.

Those ideas may be used as football/market evidence, but they do not exist as independent veto machines.

Football C must be understandable from this file plus its launcher. Do not import Football A's 31-file execution stack into C.

## 2. Fair-comparison boundary

For the A-vs-C trial:

- fixture discovery remains common and AiScore-authoritative;
- C receives the same fixture universe that A receives;
- C must not read A's frozen grades, ranks, Step-2 verdicts, Website Picks, or final result before freezing its own corresponding state;
- C may use the same contemporaneous XI, odds screenshot/text, and public web evidence available to A at that epoch;
- C may use Airtable only to persist/recover its own C states during the prospective run, not to copy A's judgment.

This keeps the comparison about decision architecture rather than fixture discovery.

## 3. C screen

Apply the shared hard identity/scope rules first:

- senior first-team football only unless an explicit prospective trial exception exists;
- exclude youth/Uxx, academy, reserves/B/development, amateur/semi-pro, regional/state/provincial and other currently excluded scope families;
- verify fixture identity, home/away, kickoff and status;
- preserve time-zone integrity.

Then C itself screens the remaining fixtures.

A fixture survives when there is at least one credible current route to a useful Over environment and the evidence is strong enough to research further.

PASS early when the fixture is dominated by:
- weak/uncertain scoring routes on both sides;
- strong current suppression with no credible carrier;
- unusable evidence quality;
- matchup/incentive conditions that materially reduce the expected goal path;
- unsupported high burden with no realistic protected expression.

Do not keep weak fixtures merely to fill a board. Do not impose a fixed board-size target.

## 4. Integrated football assessment

For every surviving fixture, answer five questions.

### 4.1 Scoring routes
For each team classify its current scoring route:
- `STRONG` — repeatable current creation/finishing route;
- `USABLE` — credible route but less robust or more conditional;
- `WEAK` — contribution relies mainly on opponent failure, score proxy, or uncertain personnel.

Use actual mechanisms: creation, finishing, service, transition, set piece, territorial pressure, or repeatable opponent leakage.

Recent scorelines support a route but do not create one by themselves.

### 4.2 Self-funded carrier
Classify whether either side can plausibly produce most or all of the target total itself:
- `STRONG CARRIER`;
- `USABLE CARRIER`;
- `NO RELIABLE CARRIER`.

A carrier is football evidence, not a market-derived label.

### 4.3 Chance quality
Prefer current chance-quality evidence when available: big chances, central/box access, quality shots/SOT, xG/xGOT used in proper context, repeatable high-value transitions, or a credible data-poor equivalent.

Do not allow raw possession, corners, or generic shot counts to substitute for finishing-quality evidence.

### 4.4 Suppression / failure mode
State the single most important way the Over thesis can fail.

Check tactical control/compression, opponent resistance, one route disappearing, class-gap game-state control, first-leg/final/incentive effects, venue-specific matchup suppression, and current finishing/creation weakness.

### 4.5 H2H
H2H is mandatory context when usable.

Priority:
`CURRENT MECHANISM -> RECENT SAME-VENUE TRANSFERABLE H2H -> RECENT ALL-VENUE TRANSFERABLE H2H -> OLD BACKGROUND`

H2H never creates a scoring route.

Suppressive H2H can materially downgrade/pass only when it is reasonably transferable and current football evidence corroborates the same mechanism. Open H2H can support but never rescue weak current football evidence.

## 5. C supported burden

Choose one protected Asian-total burden or a narrow range before considering price.

The burden must answer:

> What is the highest total this football evidence supports without requiring an optimistic tail?

Prefer quarter/whole-line protection when adjacent lines are otherwise similar.

Do not raise burden merely because a higher line pays more.

C records:
- `SUPPORTED LINE`;
- optional `CEILING`;
- one-sentence basis.

## 6. C ranking

Rank survivors directly against each other. No grade-first or price-first ordering.

Use this priority:
1. reliable path to the supported total;
2. independent route quality / self-funded carrier;
3. current chance quality;
4. failure-mode resistance;
5. XI robustness when known;
6. burden protection;
7. evidence confidence.

Market price does not create rank.

Output one ordinal rank plus one board state:
- `C-FOCUS`;
- `C-WATCH`;
- `C-PASS`.

Use C-PASS for researched fixtures that should not proceed to serious execution review.

## 7. XI confirmation — one pass

When confirmed XI arrives, do exactly one football confirmation pass.

Required:
- map missing/changed personnel to actual route functions;
- run one fresh fixture-specific public-web football research pass;
- re-check current H2H/matchup only where it can alter the mechanism;
- state whether the original thesis is `PRESERVED`, `DEGRADED`, or `BROKEN`.

Do not create separate XI, research, H2H, market-alignment and carrier committees. They are evidence inside one decision.

Fresh post-XI web research remains mandatory before a final prematch C-BET.

## 8. Market interpretation

The bookmaker is evidence, not authority.

### 8.1 Market above C burden
If the available main/lowest useful line is above C's supported burden:
- do not buy the extra burden merely for price;
- use WAIT only when the supported target is realistically reachable without requiring the football thesis to deteriorate;
- otherwise PASS.

### 8.2 Market below C burden
A lower market center is a warning, not an automatic veto.

Ask:
> Is there current football evidence explaining why the market is more pessimistic?

If YES and the explanation attacks C's mechanism, downgrade or PASS.

If NO and C's football thesis remains intact, the lower line may be treated as useful protection. Do not force a separate market-undercut hold merely because the book is lower.

### 8.3 Price
For the shadow trial:
- `>=1.65` is normal acceptable pricing;
- `1.60–1.64` is a SOFT ZONE, not an automatic rejection. It may be C-BET only for a top-ranked C-FOCUS candidate at/below supported burden with no material football veto;
- `<1.60` is normally PASS/WAIT.

This is frozen for the trial and must not be adjusted from early results.

## 9. Final action: only BET / WAIT / PASS

### C-BET — SHADOW
Use when:
- football thesis survives;
- selected line is at/below C-supported burden; no above-burden exception is granted during this initial trial;
- price is acceptable under Section 8.3;
- no material current suppression/failure veto remains.

Record exact line, odds and timestamp.

### C-WAIT — SHADOW
WAIT is allowed only when:
- football thesis is already good enough;
- the current line/price is the blocker;
- a specific protected target is realistically reachable;
- waiting is not expected to require the match to demonstrate negative information.

A WAIT must predeclare:
- target line;
- minimum odds;
- cancellation condition;
- what football evidence must still be true when the target appears.

### C-PASS
Use when the football thesis is not good enough, the only available line requires unsupported burden, the price is unacceptable without a healthy wait path, or the planned wait would depend on thesis deterioration.

## 10. Decay integrity: price decay != thesis decay

A predeclared WAIT never auto-executes merely because the number appears.

When the target is reached, ask only:

`TARGET REACHED + THESIS STILL HEALTHY?`

For a scoreless Over wait, no goal/no red card alone is insufficient.

At least one current attacking-quality indicator must show the original scoring route is still functioning, such as:
- credible high-value chance(s);
- repeated dangerous box/central entries;
- meaningful threatening SOT/keeper work;
- clear transition/territorial pressure that is producing quality final actions;
- another fixture-specific mechanism originally identified by C.

If the price improved because the attack has gone stale, cancel the plan:

`C-WAIT CANCELLED — THESIS DECAY`

Do not chase a later lower line after cancellation unless a genuinely new scoring epoch forms.

## 11. Live handling

C is not a general live-betting model during this test.

It may act live only to resolve a predeclared C-WAIT using Section 10. No opportunistic new live bets.

A goal, red card, major injury, or material mechanism change creates a new epoch and voids the old quote. The predeclared concept may be reassessed, but it is never mechanically carried across the event.

## 12. Required C board output

For every researched actionable fixture:

| Rank | Match | C state | Routes | Carrier | Supported line | Main failure | Initial action |
|---|---|---|---|---|---|---|---|

Keep the board compact. Explanation belongs in a short evidence note, not a chain of sub-verdicts.

## 13. Required C XI/odds output

For each supplied match:

`#rank MATCH — C-BET / C-WAIT / C-PASS`

Then:
- XI: PRESERVED / DEGRADED / BROKEN
- Fresh research: FOUND / LIMITED / UNAVAILABLE-ATTEMPTED
- H2H: one compact state if material
- Supported line
- Current line/odds
- One integrated reason
- If WAIT: target + cancellation condition + thesis-health requirement

## 14. Persistence during shadow

Use model identifier:
`Football C — SHADOW`

C must not write an official Website Pick.

For every material C-BET/C-WAIT/C-PASS comparison case, preserve enough information for frozen C rank/state, route/carrier description, supported line, XI state, current quote, C action, WAIT target/reach/cancel state, final score, and counterfactual settlement.

If Airtable schema cannot express a C-specific field cleanly, preserve the exact C state in Evidence Summary/Fail Reasons without altering Football A fields.

## 15. Non-negotiable trial rules

- No Football C rule edits after the prospective test starts.
- Discovery matches do not count as holdout evidence.
- C remains shadow-only.
- C cannot consult A's decision before freezing its own decision for that epoch.
- No retrospective rank/line changes after FT.
- No result-based exceptions.
- No hidden score when researching a historical state.
- Operational simplicity is part of the hypothesis; do not recreate Football A's stage count inside C.

## 16. What Football C is testing

Football C is an architectural challenger, not a claim that one particular Football A rule is wrong.

It tests this bundled hypothesis:

> A compact end-to-end football judgment with protected-line discipline, mandatory XI/web/H2H confirmation, soft market interpretation, and thesis-aware waiting can produce equal or better decisions with fewer operational failure points than Football A's multi-gate pipeline.

Because the bundle is inseparable by construction, a successful C trial would justify a later narrower decomposition test before any component-level causal claims.
