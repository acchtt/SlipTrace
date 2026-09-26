# Football A — Mandatory Post-XI Football Web-Research Gate

**Status:** ACTIVE PROCESS-COMPLIANCE GATE  
**Effective:** 2026-09-26 ICT  
**Scope:** Step 2 XI + odds review, including prematch and just-started/live screenshots  
**Model effect:** none. This does not change predictive thresholds, supported burden, carrier triggers, price floors, ranking, or exposure eligibility. It enforces the intended evidence workflow.

## 1. Purpose

A confirmed XI changes the information state. The model must not jump directly from:

`FROZEN PRE → XI SCREENSHOT → ODDS / MARKET DECOMPOSITION → VERDICT`

without making a fresh fixture-specific football research attempt.

Market-history research and football research are separate obligations. Finding opening/current odds does **not** satisfy this gate.

## 2. Prematch hard gate

For every normal prematch Step-2 fixture, use:

`FROZEN PRE → IDENTITY GATE → FIRST-PASS XI → POST-XI FOOTBALL WEB RESEARCH → MARKET-HISTORY ATTEMPT → XI/RESEARCH/MARKET CONFLICT CHECK → FINAL XI → CHANCE QUALITY / BURDEN → MARKET CENTER / CARRIER → EXECUTION`

Before a final prematch LOCK / HOLD / PASS / WAIT is issued, perform a targeted web search for current fixture-specific football evidence after the supplied XI has been read.

Set exactly one status:

- `POST-XI RESEARCH = FOUND`
- `POST-XI RESEARCH = LIMITED`
- `POST-XI RESEARCH = UNAVAILABLE — ATTEMPTED`
- `POST-XI RESEARCH = SKIPPED — EXPLICIT USER WAIVER`

`NOT CHECKED`, a missing status, or silently relying only on frozen PRE/Airtable/GitHub/model files is a **PROCESS COMPLIANCE FAILURE**.

An ordinary official prematch lock may not be published with `NOT CHECKED` or missing research status.

## 3. Required research targets

Search only for evidence that can change or harden the post-XI football thesis. Target, where available:

- confirmed starter roles and likely shape;
- important attacking creators/finishers and whether their route survives;
- late injuries, suspensions, illness, rotation, or unexpected omissions;
- defensive absences that change opponent leakage;
- recent chance creation / high-value chance production and chance concession;
- recent relevant home/away or venue-specific performance;
- competition incentives, qualification state, first-leg/second-leg context, or rotation incentives;
- current manager/team news with tactical relevance;
- same-venue H2H / matchup-compression evidence when the active burden rule requires it;
- football-led explanations for a material disagreement between frozen PRE and the current market.

Do not perform broad generic browsing merely to create volume. The search must be targeted to the actual XI, route construction, failure mode, chance quality, and market conflict.

## 4. Source quality

After AiScore establishes fixture identity, post-XI research is source-flexible.

Prefer:

1. official competition, federation, club, or team sources;
2. reputable match reporting / team news;
3. reputable statistics providers with current match/team data;
4. credible specialist sources.

Generic prediction pages, scraped previews, or unsourced summaries may supplement but must not be the sole basis for a material upgrade.

The user's supplied current executable odds remain execution-price authority. External odds may be used only for context/history unless the user explicitly requests price verification.

## 5. Evidence semantics

Fresh research may:

- validate or downgrade the first-pass XI interpretation;
- identify a late absence or tactical issue;
- harden or weaken chance-quality confidence;
- explain a market undercut/high-market conflict;
- support a carrier reopen when the active football rules independently permit it;
- close an execution lane when current football evidence invalidates the frozen thesis.

Fresh research may **not**:

- rewrite frozen PRE history;
- let market price create structure;
- fabricate missing chance-quality evidence;
- bypass the price floor, burden protection, upper-tail gate, scope gate, or identity gate.

## 6. Just-started / live latency interaction

`LIVE VERDICT-FIRST` changes ordering only. It does **not** waive this research gate.

When a Step-2 screenshot arrives after kickoff or in a just-started live window and the quote is time-sensitive:

1. read the minimum confirmed state;
2. surface the actionable provisional verdict immediately;
3. in the **same assessment**, perform the targeted post-XI football web-research attempt unless it was already completed for this fixture at the current XI epoch;
4. record the research status;
5. if material contradictory evidence is found while the quoted state remains current, issue the corrected verdict immediately;
6. if a goal/red card/material state change occurs first, void the old quote and reprice the new epoch.

Do not let “verdict first” become “research never.”

## 7. Market-history separation

The following are independent fields:

- `POST-XI FOOTBALL RESEARCH STATUS`
- `MARKET HISTORY STATUS`

A completed market-history watch cannot substitute for football web research, and vice versa.

The conflict review should compare:

`FROZEN PRE + FIRST-PASS XI + FRESH FOOTBALL RESEARCH + MARKET HISTORY + CURRENT MARKET`

before the final prematch interpretation.

## 8. Persistence

For every material Step-2 assessment, persist or include in the Decision State evidence:

- post-XI research status;
- concise summary of material fresh findings;
- source quality / source limitation where relevant;
- whether the fresh research changed the first-pass XI interpretation;
- market-history status separately.

If research is `LIMITED` or `UNAVAILABLE — ATTEMPTED`, state the limitation explicitly rather than filling the gap with inference.

## 9. Regression guard

This gate is canonical workflow authority.

Any future edit to `CURRENT_MODEL.md`, `02_NORMAL_CHAT_XI_ODDS.md`, or `FOOTBALL_BETTING_PROCEDURE.md` that:

- removes the mandatory post-XI football research attempt;
- merges it into market-history research;
- changes prematch `must` to optional `may`;
- allows ordinary official prematch publication with missing/`NOT CHECKED` status;
- interprets live verdict-first as permission to omit the same-assessment research attempt;

is a **WORKFLOW REGRESSION** and must fail deterministic operational QA unless the user explicitly authorizes a new canonical workflow.

## 10. Audit label

This is a:

`PROCESS COMPLIANCE FIX — POST-XI RESEARCH GATE`

It must not be described as a predictive model promotion or used to rewrite historical decisions.
