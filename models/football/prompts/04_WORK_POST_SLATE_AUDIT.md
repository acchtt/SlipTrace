# 04 — Work High: Post-Slate Audit

Use Work mode with high reasoning.

## Authority

Read `models/football/CURRENT_MODEL.md` first. Use the official model, active patches, time/schedule rules and audit semantics declared there at execution time. Never infer the active version from this prompt.

Load only the current files needed to interpret frozen PRE, later material states, exposure decisions, shadows and settlement. Historical assessments remain tied to the model version that actually produced them.

## Airtable

Base ID `appWyZJjitSBATXAU`.
Daily Coverage Ledger `tblcl1UAyMqZT6Ub0`.
Decision States `tblQmUpd5WjBLQ38X`.
Website Picks `tblg3J5sbJYbzuTYD`.

Read only the requested slate/board and records needed for that audit.

## Audit boundary

Use frozen PRE from Daily Coverage Ledger as historical truth. Use Decision States for later XI/market/execution/live epochs. Use Website Picks only for actual official exposure/results.

Do not rebuild the original PRE with hindsight and do not re-research every routine fixture from scratch.

Spend deep effort on meaningful anomalies:

- losing official selections;
- repeated false-negative waits/holds;
- `DIRECT LOCK ELIGIBLE` candidates suppressed by Model A exposure gates;
- ranking and priority-inversion misses;
- fixture-filter/time-integrity failures;
- missing or skipped mandatory post-XI football web research;
- cases where market-history lookup was incorrectly treated as football research;
- price/burden/regime errors;
- persistence/synchronization faults;
- repeated failure modes;
- missed opportunities where carrier/upper-tail evidence mattered.

Routine wins and correctly handled non-exposures can be summarized from stored evidence.

## Historical/version fidelity

Never relabel an older decision as Football A. A later model may be used only as a clearly labelled counterfactual audit and must not rewrite historical exposure/P&L.

A high-scoring result after a HOLD/WAIT is not automatically a model error. Determine whether the contemporaneous state actually satisfied the then-active rules.

## Football A audit separation

For prospective Football A records, preserve three axes:

1. Structural Rank;
2. Execution Class;
3. Exposure Decision.

Report separately:

- official Football A LOCK exposure and P/L;
- `DIRECT LOCK ELIGIBLE` + `NO BET — EXPOSURE HOLD — UPPER-TAIL INSUFFICIENT` outcomes;
- `DIRECT LOCK ELIGIBLE` + `NO BET — EXPOSURE HOLD — PRIORITY INVERSION GUARD` outcomes;
- QUALIFIED — WAIT FOR DECAY target-burden outcomes;
- STRUCTURAL HOLD outcomes;
- A1/A2 FOCUS +0.25 acceptance-band shadows;
- B+ / CC+ audit-lane outcomes;
- MCE shadows;
- live/relative-decay shadows;
- FOCUS vs WATCHLIST 3+ and 4+ threshold performance.

Counterfactual and shadow lanes never enter official P/L.

### Model A core diagnostics

For every DIRECT candidate, audit whether:

- upper-tail state was correctly classified `PASS / FAIL / NOT REQUIRED`;
- priority-inversion state was correctly classified `CLEAR / BLOCKED / FOOTBALL OVERRIDE`;
- the final Exposure Decision followed the ordering:

`STRUCTURAL RANK → UPPER-TAIL PROOF → ROUTE QUALITY / FAILURE RESISTANCE → BURDEN PROTECTION → PRICE AS TIE-BREAKER`.

Flag:

- `EXPOSURE GATE FALSE POSITIVE` — official lock failed while the contemporaneous upper-tail/priority evidence did not truly justify exposure;
- `EXPOSURE GATE FALSE NEGATIVE` — exposure hold won and contemporaneous evidence shows the Model A gate should have passed;
- `PRIORITY INVERSION BREACH` — materially weaker lower-ranked official exposure was taken ahead of a higher-ranked price-only wait without valid football override;
- `UPPER-TAIL GATE BREACH` — A2 at supported ceiling was officially exposed without required upper-tail proof;
- `STRUCTURAL RANK PRESERVED` — result miss does not invalidate the frozen structural ordering;
- `EXECUTION SELECTION ERROR` — football board was useful but official exposure selection was wrong.

Do not label every losing lock a gate error; distinguish variance, conversion miss and genuine selection fault.

## Existing quarantine checks

Continue to flag official MCE/+0.25 or ordinary new live/decay exposure as a quarantine breach unless an explicit active-model/user exception applied.

The A1/A2 +0.25 acceptance band remains shadow-only until its release gate is explicitly removed by a later approved model.

Keep B+ / CC+ separate from that acceptance-band sample.

## Error taxonomy

Classify meaningful issues with the active model taxonomy where available. Otherwise use:

- PROCESS ERROR
- MODEL ERROR
- INFORMATION ERROR
- EXECUTION ERROR
- VARIANCE
- FIXTURE-FILTER / SCHEDULE-INTEGRITY ERROR
- PRICE / BURDEN / REGIME ERROR
- PERSISTENCE / SYNC ERROR
- POST-XI RESEARCH COMPLIANCE ERROR

## Step-2 post-XI research compliance audit

For every material Step-2 XI+odds assessment in the audited slate, inspect the Decision State evidence for a separate post-XI football research status and market-history status.

A compliant post-XI status is one of:

- `FOUND`;
- `LIMITED`;
- `UNAVAILABLE — ATTEMPTED`;
- `SKIPPED — EXPLICIT USER WAIVER`.

Flag `POST-XI RESEARCH COMPLIANCE ERROR` when:

- status is absent / `NOT CHECKED`;
- no fresh fixture-specific football research was attempted after the XI first pass;
- odds/market-history research was counted as satisfying football research;
- a prematch Website Pick was published before the research gate completed;
- live verdict-first was used as a reason never to perform the same-assessment research attempt.

Do not retroactively change historical P/L solely because of a process-compliance fault. Preserve the original decision and classify the workflow defect separately.

## Learning rule

Do not propose another model change from one outcome. Recommend changes only when repeated prospective evidence supports them.

For each proposed change state:

- exact rule/workflow affected;
- evidence pattern;
- expected benefit;
- downside;
- `TEST / KEEP / MODIFY / REJECT`.

Do not edit model files automatically unless the user explicitly asks.

## Output

Compact audit summary:

- board ID/name when available;
- model versions audited;
- official LOCK results/P&L;
- DIRECT-eligible exposure holds by blocker;
- qualified-wait target outcomes;
- structural holds;
- acceptance-band/B+/MCE/live shadow lanes;
- FOCUS-vs-WATCHLIST 3+/4+ separation;
- priority-inversion compliance;
- upper-tail gate performance;
- meaningful misses and error taxonomy;
- recommended `TEST / KEEP / MODIFY / REJECT` items;
- no-change areas.
