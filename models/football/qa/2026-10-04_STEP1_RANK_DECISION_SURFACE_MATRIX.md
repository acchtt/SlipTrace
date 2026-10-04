# Step-1 /rank Decision-Surface QA Matrix — 2026-10-04

**Stage audited:** Step 1 — Football C official board + C2/C3 shadow boards  
**Authority:** `CURRENT_MODEL.md`, `01_WORK_DAILY_SWEEP.md`, Football C/C2/C3 specs, Step-1 procedures, engine core/adapter, Daily Coverage persistence  
**Process repair:** board-triplet reconciliation + required evidence bases  
**Predictive-rule changes:** none

## Result

`QA FAIL — UNDER-SPECIFIED DECISION SURFACE`

The deterministic engine faithfully ranks and allocates lanes once the semantic football grades are frozen. The remaining gap is upstream of that deterministic layer: several material grades/states do not yet have reproducible classification thresholds.

The QA repair in this branch improves traceability and prevents C/C2/C3 research drift, but it does not pretend that an evidence basis is the same thing as a deterministic predictive threshold.

| # | Material input / surface | Current treatment | Deterministic effect after freeze | QA status |
|---:|---|---|---|---|
| 1 | canonical match identity | AiScore / frozen handoff | exact match key | FULLY TRACED |
| 2 | kickoff / exact kickoff block | timezone-aware frozen schedule | same-KO comparison/capacity | FULLY TRACED |
| 3 | required competition coverage | Step-0 manifest | missing protected block blocks Work | FULLY TRACED |
| 4 | women's-top-flight reconciliation | Step-0 manifest/counters | unresolved/missing class blocks Work | FULLY TRACED |
| 5 | operational viability A/B | operational gate + reliability cap | B caps lane at RESERVE; C/D blocked | FULLY TRACED |
| 6 | competition reliability state | operational-only memory | may cap/demote viability; never promote | FULLY TRACED |
| 7 | tournament incentive applicability/resolution | mandatory structured block | unresolved applicable fixture is quarantined | FULLY TRACED |
| 8 | common Step-1 evidence epoch | one research pass + `common_evidence_basis` | C/C2/C3 triplet must match exactly | FULLY TRACED |
| 9 | home route STRONG/USABLE/WEAK | football research + basis | ranking / lane / C2/C3 policy input | UNDER-SPECIFIED DECISION THRESHOLD |
| 10 | away route STRONG/USABLE/WEAK | football research + basis | ranking / lane / C2/C3 policy input | UNDER-SPECIFIED DECISION THRESHOLD |
| 11 | carrier NONE/USABLE/STRONG | football research + basis | ranking / lane / funding | UNDER-SPECIFIED DECISION THRESHOLD |
| 12 | carrier self-fund | explicit boolean + basis | upper-tail / lane / C2/C3 policy | UNDER-SPECIFIED DECISION THRESHOLD |
| 13 | independent upper-tail | explicit boolean + basis | ranking / lane / bridge/funding | UNDER-SPECIFIED DECISION THRESHOLD |
| 14 | route reliability LOW/MEDIUM/HIGH | semantic grade | C/C2/C3 rank + lane | UNDER-SPECIFIED DECISION THRESHOLD |
| 15 | independent-route quality | semantic grade | C/C2 rank | UNDER-SPECIFIED DECISION THRESHOLD |
| 16 | chance quality | semantic grade | C/C2/C3 rank + lane | UNDER-SPECIFIED DECISION THRESHOLD |
| 17 | failure resistance | semantic grade | rank / lane | UNDER-SPECIFIED DECISION THRESHOLD |
| 18 | XI robustness | pre-XI semantic grade | C/C2 rank | UNDER-SPECIFIED DECISION THRESHOLD |
| 19 | evidence confidence | semantic grade | rank / C3 state / lane | UNDER-SPECIFIED DECISION THRESHOLD |
| 20 | burden protection | semantic grade | rank / RESERVE eligibility | UNDER-SPECIFIED DECISION THRESHOLD |
| 21 | main failure text | required descriptive field | no direct numeric engine term by itself | EXPLICITLY NON-MATERIAL BY ITSELF |
| 22 | failure attacks route | boolean + basis | hard C/C2/C3 veto/lane effect | UNDER-SPECIFIED DECISION THRESHOLD |
| 23 | material suppression | boolean + basis | hard C/C2/C3 veto/lane effect | UNDER-SPECIFIED DECISION THRESHOLD |
| 24 | H2H material-use gate | structured effect + transferability + corroboration + basis | material H2H use fails closed unless verified | FULLY TRACED PROCESS GATE |
| 25 | C completion mode | NONE/TWO_SIDED/CARRIER_LED/FORCED_CHAOS/MIXED | C lane and screen logic | UNDER-SPECIFIED DECISION THRESHOLD |
| 26 | C burden-completion quality | LOW/MEDIUM/HIGH | primary C ranking term + lane | UNDER-SPECIFIED DECISION THRESHOLD |
| 27 | C continuation quality | LOW/MEDIUM/HIGH | primary C ranking term + lane | UNDER-SPECIFIED DECISION THRESHOLD |
| 28 | C opponent leakage | LOW/MEDIUM/HIGH | C rank / carrier path | UNDER-SPECIFIED DECISION THRESHOLD |
| 29 | C burden stall risk | LOW/MEDIUM/HIGH | rank; HIGH hard STOP | UNDER-SPECIFIED DECISION THRESHOLD |
| 30 | C supported burden | numeric quarter line + required `supported_line_basis` | ranking comparator / Step-2 max burden | UNDER-SPECIFIED DECISION THRESHOLD |
| 31 | C board state | C-PASS/WATCH/FOCUS + required `board_state_basis` | only FOCUS may receive operational follow lane | UNDER-SPECIFIED DECISION THRESHOLD |
| 32 | C2 supported burden | independently frozen + basis | C2 action/bridge comparison | UNDER-SPECIFIED DECISION THRESHOLD |
| 33 | C2 board state | C2-PASS/WATCH/FOCUS + basis | shadow action eligibility | UNDER-SPECIFIED DECISION THRESHOLD |
| 34 | C2 ranking key | exact lexicographic tuple | deterministic rank once inputs freeze | FULLY TRACED |
| 35 | C2 selection floor | exact route/carrier boolean logic | CLEAR/BORDERLINE/FAIL | FULLY TRACED AFTER SEMANTIC INPUTS |
| 36 | C3 supported burden | independently frozen + basis; funding constraints | C3 rank/action burden | UNDER-SPECIFIED DECISION THRESHOLD |
| 37 | C3 second-route role | four semantic states + required basis | C3 rank/funding | UNDER-SPECIFIED DECISION THRESHOLD |
| 38 | C3 goal-3/goal-4 funding state/source | structured state/source + basis | C3 state/rank/lane | UNDER-SPECIFIED DECISION THRESHOLD |
| 39 | C3 control-endpoint risk | LOW/MEDIUM/HIGH + basis | C3 state/rank/lane | UNDER-SPECIFIED DECISION THRESHOLD |
| 40 | C3 forced-chaos verification | boolean + basis | can escape control-endpoint PASS | UNDER-SPECIFIED DECISION THRESHOLD |
| 41 | C3 board state | deterministic function of frozen funding/control inputs | PASS/WATCH/FOCUS | FULLY TRACED AFTER SEMANTIC INPUTS |
| 42 | C ranking key | exact burden-completion lexicographic tuple | deterministic rank | FULLY TRACED AFTER SEMANTIC INPUTS |
| 43 | C3 ranking key | exact funding/control lexicographic tuple | deterministic shadow rank | FULLY TRACED AFTER SEMANTIC INPUTS |
| 44 | exact-key tie break | canonical `match_id` | deterministic ordering independent of input order | FULLY TRACED |
| 45 | C base FOLLOW/RESERVE/STOP gate | exact engine conditions | deterministic lane before capacity | FULLY TRACED AFTER SEMANTIC INPUTS |
| 46 | grade-B cap | exact operational rule | never routine FOLLOW | FULLY TRACED |
| 47 | global FOLLOW capacity | max 6 | deterministic overflow | FULLY TRACED |
| 48 | RESERVE capacity | max 4 | deterministic overflow | FULLY TRACED |
| 49 | same-kickoff FOLLOW capacity | max 2 per exact minute | deterministic same-KO overflow | FULLY TRACED |
| 50 | three-board common-evidence equality | `board_triplet_cli.py` | mismatch hard-fails comparison | FULLY TRACED |
| 51 | model-policy field isolation | board-triplet allowlist | C completion cannot leak to C2/C3; C3 fields cannot leak to C/C2 | FULLY TRACED |
| 52 | Daily Coverage publication | exact-copy persistence contract | rerank/re-screen forbidden | FULLY TRACED |
| 53 | C2/C3 prospective counter eligibility | complete ranked eligible universe required | contamination holds counter | FULLY TRACED |

## Under-specified-threshold findings

The active model still uses semantic terms that can alter official rank, supported burden, board state or Step-2 workload without a fully reproducible classifier. The important groups are:

1. route/carrier quality;
2. common LOW/MEDIUM/HIGH quality grades;
3. failure/suppression booleans;
4. Football C completion/continuation/leakage/stall grades;
5. C/C2/C3 supported-line derivation;
6. C and C2 board-state boundaries;
7. C3 second-route/funding/control/forced-chaos classification.

Evidence bases now make these decisions auditable, but **auditability is not determinism**.

## Repair boundary

The following changes were safe `PROCESS COMPLIANCE FIX` items and are implemented:

- require `common_evidence_basis`;
- require `supported_line_basis`;
- require C/C2 `board_state_basis`;
- require missing C3 second-route/forced-chaos bases;
- preserve the bases in engine output/persistence;
- reconcile C/C2/C3 ranked universe and common facts with one board-triplet runner;
- reject model-policy field leakage.

The following must **not** be silently added to Football C by QA:

- numeric route-strength cutoffs;
- numeric HIGH/MEDIUM/LOW grade cutoffs;
- a new formula for supported burden;
- a new deterministic C/C2 FOCUS/WATCH/PASS classifier;
- a new C3 funding/control threshold.

Those would change predictive selection and are:

`MODEL CHALLENGER REQUIRED`

## Counts

- material / explicitly classified surfaces: **53**
- fully traced or deterministic after frozen semantic inputs: **30**
- explicitly non-material by itself: **1**
- under-specified material predictive surfaces: **22**
- stale-authority findings: **0 found in this pass**
- common-evidence reconciliation gap: **repaired**
- persistence traceability gap: **repaired**
- predictive thresholds changed by QA: **0**

Because under-specified predictive surfaces remain, Step 1 cannot honestly receive a decision-surface PASS.

**Overall:** `QA FAIL — UNDER-SPECIFIED DECISION SURFACE`
