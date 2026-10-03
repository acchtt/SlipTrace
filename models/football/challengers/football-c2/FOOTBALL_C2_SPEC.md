# Football C2 — Selection-First Challenger Specification

**Status:** PROSPECTIVE SHADOW CHALLENGER — ACTIVE AFTER FOOTBALL C1 STOP
**Champion:** Football C
**Parent:** Football C production
**Purpose:** preserve Football C's compact architecture while fixing the observed selection-inversion failure: marginal protected-line matches were promoted into bets while stronger football environments were left unexposed because the market sat modestly above the initial supported burden.

Football C2 is shadow-only. It may never create an official Website Pick or authorize real exposure.

## 1. Design principle

C2 owns the full decision from common fixture handoff onward:

`COMMON AISCORE FIXTURE UNIVERSE -> C2 SCREEN -> C2 RESEARCH/RANK -> XI CONFIRMATION -> SELECTION GATE -> BET / WAIT / PASS -> SETTLEMENT`

The architecture remains integrated and simple. Do not recreate Football A's multi-gate stack.

## 2. Fair-comparison boundary

- fixture discovery remains common and AiScore-authoritative;
- C2 receives the same broad-senior fixture universe as Football C;
- one common semantic research state is frozen before C or C2 applies policy;
- C2 must not read Football C's rank/verdict/result before freezing its own policy output;
- C2 uses the same contemporaneous XI, odds and public web evidence epoch as Football C;
- historical C1 cases may motivate this design but have zero C2 validation weight.

## 3. C2 screen

Apply shared hard scope/identity rules first.

A fixture survives when current football supports at least one credible Over route and the evidence is strong enough to research further.

PASS early when dominated by:
- weak/uncertain routes on both sides;
- strong current suppression with no credible carrier;
- unusable evidence;
- matchup/incentive conditions that materially reduce the goal path;
- unsupported burden with no realistic protected expression.

Do not fill a board quota.

## 4. Integrated football assessment

For every survivor assess:

### 4.1 Routes
For each team classify:
- `STRONG`
- `USABLE`
- `WEAK`

Use creation, finishing, service, transition, set-piece, territorial pressure and repeatable opponent leakage in proper context. Scorelines support a route but do not create one.

### 4.2 Carrier
Classify:
- `STRONG CARRIER`
- `USABLE CARRIER`
- `NO RELIABLE CARRIER`

Carrier status must come from football evidence, never market magnitude alone.

### 4.3 Chance quality
Prefer big chances, dangerous box/central access, quality SOT/keeper work, xG/xGOT in context, repeatable high-value transitions, or credible data-poor equivalents.

### 4.4 Failure mode
State the single most important way the Over can fail.

### 4.5 H2H
Priority:
`CURRENT MECHANISM -> RECENT SAME-VENUE TRANSFERABLE H2H -> RECENT ALL-VENUE TRANSFERABLE H2H -> OLD BACKGROUND`

Suppressive H2H matters only when reasonably transferable and corroborated by current football. Open H2H supports but never rescues weak current evidence.

## 5. Initial supported burden

**C2 owns this field independently.** Shared football evidence does not mean shared model burden.

Choose one protected Asian-total line or narrow range before looking at price.

Question:
> What is the highest total current football supports without requiring an optimistic tail?

Record:
- `SUPPORTED LINE`
- optional `CEILING`
- one-sentence basis.

This is the initial football burden, not an immutable execution line.

Hard comparison rule:
- do not read/copy Football C's supported line while freezing C2's line;
- persist the C2 line separately;
- if an independent C2 line is unavailable, mark the paired comparison incomplete rather than substituting C's line.

## 6. Selection quality and ranking

Rank survivors directly by:
1. route reliability;
2. independent route quality / self-funded carrier;
3. current chance quality;
4. failure-mode resistance;
5. XI robustness when known;
6. evidence confidence;
7. burden protection.

Price does not create rank.

Board states:
- `C2-FOCUS`
- `C2-WATCH`
- `C2-PASS`

### 6.1 Selection-quality floor

A direct C2-BET requires one of:

**Two-route floor**
- both routes at least USABLE;
- at least one route STRONG;
- no unresolved failure mode directly attacks either route.

**Carrier floor**
- one STRONG CARRIER;
- independent current upper-tail evidence;
- opponent route may be WEAK, but the carrier must plausibly self-fund the selected burden.

A low line does not waive this floor.

### 6.2 Protected-line inversion guard

A C2-WATCH may not become a direct BET merely because O2.0/O2.25 is available at an attractive price.

If the main failure mode still directly attacks the scoring mechanism after XI/research, the match remains WATCH/PASS even when:
- the market is below supported burden;
- the lower line offers push protection;
- the price is >=1.65.

This explicitly prevents:
`weaker match + comfortable line -> exposure`
from outranking
`stronger match + slightly difficult line -> no exposure`.

### 6.3 Exposure monotonicity check

Before finalizing any C2-BET slate, compare all serious candidates.

If a lower-ranked WATCH is being promoted while a higher-ranked FOCUS is unexposed solely because of a modest market-gap problem, re-screen both under Section 9. Do not automatically suppress the WATCH; instead verify that its football quality independently clears the selection floor.

## 7. XI confirmation — one pass

When confirmed XI arrives:
- map absences/changes to route functions;
- run one fresh fixture-specific public-web research pass;
- re-check current H2H/matchup only if mechanism-relevant;
- classify thesis `PRESERVED / DEGRADED / BROKEN`.

Fresh post-XI research is mandatory before a final prematch C2-BET.

## 8. Market interpretation

The bookmaker is evidence, not authority.

### 8.1 Market below initial C2 burden

A lower line is useful protection only if the selection-quality floor is already cleared.

If current football explains the market pessimism and attacks the mechanism, downgrade/PASS.

A cheap protected line cannot rescue a marginal match.

### 8.2 Market aligned

At/below supported burden with acceptable price and no material football veto -> normal C2-BET eligibility.

### 8.3 Market above initial C2 burden

Do not mechanically buy the higher line.

First distinguish:
- `MARGINAL MATCH / HIGH LINE` -> WAIT or PASS;
- `HIGH-QUALITY FOCUS / MARKET GAP` -> apply Section 9.

## 9. C2 Focus Market-Gap Bridge

This is the targeted fix for C1's unreachable-WAIT selection inversion.

It applies only to a **C2-FOCUS** candidate.

A market line above the initial supported line may become executable up to **+0.50 goals** only when ALL are true:

1. XI thesis is PRESERVED, or DEGRADED without damage to the primary scoring mechanisms;
2. the selection-quality floor clears strongly;
3. at least one of:
   - two STRONG routes; or
   - one STRONG route + one USABLE route + STRONG CARRIER;
4. independent **non-market** upper-tail evidence exists, such as:
   - repeated current 3+ match environments driven by the same mechanisms;
   - repeated current 3+ carrier outputs;
   - strong current opponent leakage plus preserved carrier;
   - transferable open H2H that corroborates current football, but H2H may not be the sole proof;
5. no material current suppression veto remains;
6. price >=1.65;
7. the selected line is no more than +0.50 above the initial supported burden.

If these conditions clear:
- +0.25 may be executed normally;
- +0.50 requires explicit note `FOCUS MARKET-GAP BRIDGE +0.50`.

The market itself never proves upper tail. This prevents the Morocco/Monterrey-style circularity where a huge total/handicap manufactures its own justification.

If the independent football proof does not clear, keep the original supported burden and use WAIT/PASS.

## 10. Price

- >=1.65 normal acceptable;
- 1.60-1.64 soft zone only for top-ranked C2-FOCUS at/below supported burden;
- <1.60 normally WAIT/PASS.

Soft-zone pricing may never rescue an above-burden line.

## 11. Final action

### C2-BET — SHADOW
Use when:
- selection-quality floor clears;
- selected line is at/below supported burden OR valid Section-9 bridge;
- price clears;
- no material suppression/failure veto remains.

### C2-WAIT — SHADOW
Use only when:
- football thesis is already bet-quality;
- current line/price is the only blocker;
- target is realistically reachable;
- waiting is not expected to require negative football information.

A WAIT must declare:
- target;
- minimum odds;
- cancellation condition;
- thesis-health requirement.

### C2-PASS
Use when football quality is inadequate, failure risk remains mechanism-level, burden is unsupported, or WAIT is structurally unrealistic.

## 12. Unreachable-WAIT check

Before declaring WAIT, estimate whether the target can realistically appear before normal scoring events invalidate the epoch.

If the gap is **0.50 goals or greater** in a high-tempo C2-FOCUS environment:
- run the Section-9 Focus Market-Gap Bridge first;
- if bridge clears, prefer direct exposure over an unreachable WAIT;
- if bridge fails, WAIT is allowed only with a documented reason the target is realistically reachable pre-event.

Do not create a nominal WAIT whose target is expected to appear only after the match has already scored.

## 13. Decay integrity

A WAIT never auto-executes merely because the number appears.

When target is reached:
`TARGET REACHED + THESIS STILL HEALTHY?`

For scoreless Overs, require at least one live attacking-quality indicator. If decay reflects stale attack, cancel:
`C2-WAIT CANCELLED — THESIS DECAY`.

## 14. Live handling

C2 is not a general live-betting model.

It may act live only to resolve a predeclared C2-WAIT. Any goal, red card, major injury, or material mechanism change creates a new epoch and voids the old quote.

## 15. Required board output

| Rank | Match | C2 state | Routes | Carrier | Supported line | Main failure | Initial action |

## 16. Required XI/odds output

`#rank MATCH — C2-BET / C2-WAIT / C2-PASS`

Then:
- XI state
- Fresh research status
- H2H state if material
- Initial supported line
- selected/executable line
- selection-floor result
- Focus Market-Gap Bridge result if applicable
- one integrated reason
- WAIT target/cancel conditions if needed

## 17. Persistence

Model identifier:
`Football C2 — SHADOW`

Never create an official Website Pick.

Record enough information for rank/state, routes/carrier, supported line, selection-floor result, bridge result, XI state, current quote, action, wait resolution, final score and counterfactual settlement.

## 18. Trial integrity

- Football C1 is frozen and stops prospectively at the C2 activation commit.
- C1 history remains untouched.
- C2 starts a fresh prospective window.
- No C2 edits after its first eligible result; any further predictive rule change requires C3.
- Historical cases that motivated C2 have zero validation weight.

## 19. What C2 is testing

> A compact football model performs better when exposure is selected primarily by match quality, with protected burden as risk control rather than a promotion mechanism, while top-quality FOCUS matches receive a narrowly bounded football-proven bridge when the market is modestly above the initial burden.


## 20. Dual-track operational boundary

Effective from the QA authority/C2 validation repair:

- Football C is the production champion.
- C2 is a shadow policy challenger.
- C and C2 consume the same frozen semantic football evidence at board and XI epochs.
- Football C fields remain canonical production fields.
- C2 shadow persistence must never overwrite C.
- C2 may not create Website Picks or real exposure.
- Python validates both tracks from the same factual evidence but uses model-specific policy: Football C burden-completion ranking for C, frozen route-quality ranking for C2.
- C2 independently freezes its supported burden; C's line is never substituted.
- all earlier C2 results before the QA authority/C2 validation repair are excluded from the restarted confirmatory window because comparison plumbing was contaminated.

This section changes experiment plumbing/authority, not C2's predictive selection thresholds.


## Tournament-incentive evidence completeness

C2 consumes the same mandatory tournament-format/incentive block as Football C.

For every fixture the common evidence must explicitly declare `tournament_incentive_required`. If true, the complete tournament block must exist before C2 board state is assigned, and Step 2 must record `tournament_incentive_rechecked=true` before any C2 shadow action.

This is an evidence-completeness guard only. It does not alter the frozen C2 selection floor, bridge cap, price rules, or shadow-only authority.


### Incentive resolution gate

LIMITED/UNKNOWN tournament evidence is not a C2 policy input. It is an incomplete common-evidence state.

An applicable fixture receives no C2-PASS/WATCH/FOCUS, selection floor, bridge readiness, or shadow action until qualification/tiebreak/margin/simultaneous-result consequences are resolved and VERIFIED.

A user-declared exception does not waive this common-evidence gate.
