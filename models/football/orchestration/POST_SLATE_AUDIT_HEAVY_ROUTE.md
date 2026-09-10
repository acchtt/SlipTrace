# Orchestrated Post-Slate Audit — Heavy Route

**Status:** EXPERIMENTAL workflow trial  
**Purpose:** move routine result/settlement/evidence collection to workers while reserving model-learning judgment for one authoritative Main Agent.  
**Authority:** read `models/football/CURRENT_MODEL.md` and the active audit/persistence procedures first.

## Invocation

```text
use heavy route. Run the football orchestrated post-slate audit using models/football/orchestration/POST_SLATE_AUDIT_HEAVY_ROUTE.md for the requested slate. Preserve historical model/version fidelity. Workers collect evidence and settlement facts only; the Main Agent alone decides audit classifications and lessons.
```

## 0. Main-Agent authority load

Read:

1. `models/football/CURRENT_MODEL.md`;
2. the current post-slate audit prompt/procedure and active model rules it requires;
3. the current Airtable coverage and Decision State contracts;
4. `models/football/orchestration/README.md`;
5. `models/football/orchestration/WORKER_CONTRACTS.md`.

Record the model version that actually produced each historical decision. Do not relabel older exposure as the current model.

## 1. Companion — reconstruct audit manifest

Spawn one Companion to assemble a compact index for the requested slate:

- fixture identity;
- frozen PRE state/version;
- material Decision States;
- official exposure from Website Picks where applicable;
- current settlement state;
- candidates for anomaly review.

The Companion must not decide whether a past decision was good or bad.

## 2. Routine Result / Settlement Executors

Spawn Default Executors using Contract F for routine results and settlement math.

They should:

- verify final score/status;
- settle only actual official exposure;
- apply the active Asian-total settlement rules;
- return P/L math;
- identify missing or conflicting result data.

Do not spend Main-Agent reasoning on routine arithmetic.

## 3. Main Agent — select anomaly set

From stored state + settlement facts, identify which fixtures deserve deeper investigation.

Prioritize:

- losing official selections;
- repeated false-negative HOLD/PASS patterns;
- ranking misses;
- burden/regime errors;
- fixture-filter/time-integrity faults;
- persistence/sync faults;
- repeated structural failure modes;
- meaningful missed opportunities.

Routine wins and correctly handled routine non-exposure states should remain compact.

A high-scoring final after HOLD/PASS is not automatically an anomaly requiring model change.

## 4. Parallel Audit Anomaly Investigators

Spawn Investigators only for the selected anomaly set, using Contract G.

Batch similar anomalies when useful, but keep historical evidence separated by fixture/model version.

Investigators must distinguish:

- facts available at decision time;
- facts only known afterward;
- observed match outcome evidence;
- plausible process/model/information/execution/variance/fixture-filter/price-regime/persistence lanes.

They must not propose a final audit classification or model change.

## 5. Tester — audit integrity

Spawn one Tester to verify:

- official exposure totals match Website Picks;
- settlement math is correct;
- HOLD/PASS/shadow/counterfactual states did not enter official P/L;
- frozen PRE was not rewritten with hindsight;
- historical version labels remain correct;
- every anomaly has sufficient evidence to support Main-Agent review.

Return PASS/FAIL plus exact faults.

## 6. MAIN AGENT — authoritative audit judgment

Only the Main Agent may decide:

- what worked;
- which misses were genuine;
- final error taxonomy;
- whether an outcome was variance versus model/process failure;
- whether a repeated pattern justifies TEST / KEEP / MODIFY / REJECT;
- whether a proposed rule/workflow change deserves user consideration.

Apply the current audit semantics exactly, including any active STANDARD/EGE/direct/decay/non-decay/goal-expansion labels declared by the model.

### Learning guard

Do not recommend model change from one outcome.

For every proposed change, state:

- exact rule/workflow affected;
- repeated evidence pattern;
- expected benefit;
- downside/risk;
- TEST / KEEP / MODIFY / REJECT.

Do not edit model/rule/registry/trial files automatically unless the user explicitly asks.

## 7. Archivist — compact durable record

After Main-Agent judgment, the Archivist may update orchestration/session documentation with:

- audit period;
- verified official record/P&L;
- meaningful error counts;
- accepted no-change conclusions;
- unresolved research questions;
- proposed tests awaiting user approval;
- orchestration token/agent usage report where available.

Do not let the Archivist convert a proposed test into an active model rule.

## 8. Final output

Return a compact audit:

- historical model versions audited;
- official W/L/push/units summary;
- what worked;
- meaningful misses only;
- final error taxonomy;
- repeated structural patterns;
- burden/regime/price/schedule/persistence issues;
- TEST / KEEP / MODIFY / REJECT recommendations;
- no-change areas;
- tester PASS/FAIL;
- orchestration usage summary if available.

## Success criterion

The orchestrated audit should use high-tier reasoning primarily for causal interpretation and model-learning judgment, not result retrieval, arithmetic, duplicate source reading, or routine state reconstruction.
