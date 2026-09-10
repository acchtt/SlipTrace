# 04 — Work High: Post-Slate Audit

Use Work mode with high reasoning.

## Authority
Read `models/football/CURRENT_MODEL.md` first. Use the official model, active patches, time/schedule rules, and audit semantics declared there at execution time. Never infer the active version from this prompt.

Load only the current files needed to interpret frozen PRE, later material states, live/audit labels, and settlement. Historical assessments remain tied to the model version that actually produced them.

## Airtable
Base ID `appWyZJjitSBATXAU`.
Daily Coverage Ledger `tblcl1UAyMqZT6Ub0`.
Decision States `tblQmUpd5WjBLQ38X`.
Website Picks `tblg3J5sbJYbzuTYD`.

Read only the requested slate/date and the records needed for that audit.

## Audit boundary
Use frozen PRE from Daily Coverage Ledger as historical truth. Use Decision States for later XI/market/live assessment epochs. Use Website Picks only for actual official exposure/results when needed.

Do not rebuild the original PRE with hindsight and do not re-research every routine fixture from scratch.

Spend deep Work effort on meaningful anomalies:
- losing official selections;
- repeated false-negative HOLD/PASS patterns;
- ranking misses;
- fixture-filter/time-integrity failures;
- price or burden/regime errors;
- persistence/synchronization faults;
- repeated failure modes;
- missed opportunities where the current model's later regime logic is relevant.

For normal wins and correctly handled routine HOLD/PASS states, summarize briefly from stored evidence.

## Historical/version fidelity
Never relabel an older decision as the current model. A later patch can be used for counterfactual audit only if clearly labelled; it must not rewrite historical exposure/P&L.

If the current model defines STANDARD/EGE or similar execution labels, audit them exactly as declared. Distinguish direct execution, relative decay, non-decay holds, and goal-expansion/no-chase holds where applicable.

A high-scoring result after a HOLD is not automatically a model error. Determine whether the evidence available at the time actually satisfied the current/then-active gate.

## Error taxonomy
Classify meaningful issues using the active audit taxonomy where defined. Otherwise use:
- PROCESS ERROR
- MODEL ERROR
- INFORMATION ERROR
- EXECUTION ERROR
- VARIANCE
- FIXTURE-FILTER / SCHEDULE-INTEGRITY ERROR
- PRICE / BURDEN / REGIME ERROR
- PERSISTENCE / SYNC ERROR

## Learning rule
Do not propose a model change because of one outcome. Recommend change only when repeated evidence supports it. For each proposed change state: exact rule/workflow affected, evidence pattern, expected benefit, downside, and TEST / KEEP / MODIFY / REJECT.

Do not edit model files automatically unless the user explicitly asks.

## Output
Compact audit summary: model versions audited, official results/exposure summary, what worked, meaningful misses, error taxonomy, repeated structural patterns, schedule/price/persistence issues, recommended TEST/KEEP/MODIFY items, and no-change areas.