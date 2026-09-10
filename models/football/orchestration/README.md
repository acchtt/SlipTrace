# Football Multi-Agent Orchestration

**Status:** EXPERIMENTAL workflow layer  
**Model impact:** NONE — this does not change the football model, grades, execution policy, competition policy, or official P/L semantics.  
**Authority:** `models/football/CURRENT_MODEL.md` always wins.

This directory adapts the football workflow to a Codex-style orchestrated route: cheap workers collect, normalize, verify, and persist evidence while one authoritative Main Agent performs the actual football judgment.

The purpose is to reduce high-tier reasoning usage without weakening structural research quality.

## Golden rule

**Workers produce evidence. The Main Agent produces football decisions.**

No worker may independently create or alter any of the following unless the Main Agent explicitly delegates a purely mechanical copy of an already-finalized state:

- PRE grade;
- structural archetype / type;
- FOCUS / WATCHLIST / PASS / UNRESOLVED;
- official rank;
- EGE / goal-burden classification;
- executable line choice;
- LOCK / HOLD / PASS;
- model-rule changes.

Worker disagreement is evidence for the Main Agent to resolve, not a vote.

## Dynamic authority load

At the start of every substantive run, the Main Agent must read `CURRENT_MODEL.md` and follow the load order declared there. Never hard-code an old model version into orchestration behavior.

Current orchestration must preserve these production invariants from the active football stack:

1. AiScore remains the sole fixture-discovery authority.
2. Time is normalized to `Asia/Ho_Chi_Minh` exactly once.
3. Scope filtering occurs before deep research.
4. Price and confirmed XI do not influence frozen PRE.
5. Every Work-admitted fixture is structurally judged exactly once before the visible board is shortened.
6. Frozen PRE is historical state and is not rebuilt at XI/market time.
7. The user normally supplies confirmed XI and current Asian-total odds later.
8. Airtable remains the shared state bridge.
9. Official picks/results remain separate from HOLD/PASS and shadow/counterfactual states.
10. Model changes require repeated evidence and explicit user approval when the active audit procedure requires it.

## Role map

### Main Agent — authoritative football judge

Recommended: strongest available reasoning model for Daily Sweep and Post-Slate Audit.

Owns:

- current-model interpretation;
- structural synthesis;
- PRE grade/type/board state;
- cross-match ranking;
- post-XI regime/burden judgment;
- final LOCK/HOLD/PASS decision;
- audit learning judgment.

The Main Agent should avoid spending its context on repetitive fixture parsing, basic historical collection, duplicated source reading, and mechanical reconciliation when those can be delegated safely.

### Companion — context/state assistant

Fact-only support role. It should:

- load the active model manifest and relevant procedure paths;
- maintain the run manifest and task ledger;
- consolidate worker reports;
- flag missing evidence or contradictory worker findings;
- preserve compact handoff context.

It must not grade or rank matches.

### Investigator — football research worker

Researches assigned fixtures or one narrow evidence lane. Suitable lanes include:

- season/recent GF-GA profile;
- scoring 2+ / conceding 2+ frequency;
- home/away profile;
- chance quality / creation evidence;
- tactical / incentive context;
- historical high-line environment;
- explicit UYL trial research when the user invoked that trial.

Investigators return sourced facts, uncertainty, and plausible failure evidence. They must not see bookmaker price during PRE and must not output a betting verdict.

### Default Executor — deterministic / low-judgment worker

Suitable work:

- parse and validate the AiScore handoff;
- apply explicit scope/registry rules mechanically;
- normalize fixture identity and time;
- build compact evidence packets;
- reconcile coverage counts;
- construct Airtable payloads from Main-Agent-finalized states;
- perform routine result/settlement calculations during audit.

It must not reinterpret the football model.

### Senior Executor — disabled for routine football judgment

Do not use a second high-tier agent as an independent picker. A Senior Executor may be used only for an unusually difficult technical/research synthesis requested by the Main Agent. Its output is advisory; the Main Agent still owns the official football decision.

### Tester — independent verification

Verifies process, not football opinion:

- every admitted fixture accounted for exactly once;
- exclusion/registry rules respected;
- no odds/XI leaked into PRE;
- worker packets satisfy the required contract;
- coverage equations reconcile;
- Airtable persistence matches the frozen Main Agent artifact;
- settlement math is correct.

A Tester must never promote/demote a match.

### Archivist — durable context

Maintains project/session documentation and compact handoffs. It may record orchestration observations and audit summaries, but must not edit `CURRENT_MODEL.md`, active rules, competition registry, or trial rules unless the user explicitly requests a model/workflow change.

## Route policy

- **Light:** simple factual question or tiny maintenance task; no swarm.
- **Medium:** targeted research/support around one match or a bounded workflow task. Main Agent still judges.
- **Heavy:** daily structural sweep, large historical research, league-level audit, or post-slate audit.

Daily Sweep and Post-Slate Audit are the primary Heavy-route use cases.

## Daily data flow

`AISCORE HANDOFF -> MECHANICAL VALIDATION/SCOPE -> PARALLEL FACT RESEARCH -> MAIN-AGENT PRE JUDGMENT -> MAIN-AGENT RANKING -> TESTER RECONCILIATION -> AIRTABLE PERSISTENCE`

At XI/market time:

`FROZEN PRE -> USER XI -> MAIN-AGENT XI RERANK -> MAIN-AGENT REGIME/BURDEN -> USER ODDS -> MAIN-AGENT FINAL ACTION -> PERSISTENCE`

At audit time:

`STORED PRE/DECISIONS/PICKS -> ROUTINE RESULT/SETTLEMENT WORKERS -> ANOMALY RESEARCH -> MAIN-AGENT LEARNING REVIEW -> TESTER -> ARCHIVE`

## Token-control rules

1. Batch independent fixtures rather than spawning one worker per fixture when a worker can safely handle a small group.
2. Give each worker only the authority files and fixture evidence needed for its lane.
3. Require compact structured returns; do not return long narrative unless the Main Agent requests it.
4. Do not make multiple workers re-research the same fact by default.
5. Escalate ambiguity to the Main Agent rather than repeatedly expanding cheap-worker context.
6. Preserve deep research for plausible candidates; do not weaken the active scope gate merely to keep workers busy.

## Production safety

This orchestration is initially a **workflow trial**, not a model revision. Compare its board completeness, ranking fidelity, research depth, Airtable persistence, and usage against the existing workflow before making it the only production route.

Use:

- `DAILY_SWEEP_HEAVY_ROUTE.md` for the orchestrated price/XI-blind daily board;
- `WORKER_CONTRACTS.md` for worker input/output rules;
- `POST_SLATE_AUDIT_HEAVY_ROUTE.md` for orchestrated audits.
