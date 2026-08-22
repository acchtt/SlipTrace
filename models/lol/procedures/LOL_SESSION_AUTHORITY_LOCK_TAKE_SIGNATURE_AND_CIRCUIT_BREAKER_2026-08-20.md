# LoL Session Authority Lock, TAKE Gate Signature & Procedural Circuit Breaker — 2026-08-20

**Status:** ACTIVE GOVERNANCE  
**Effective:** 2026-08-20 UTC+7  
**Amended:** 2026-08-22 UTC+7  
**Analytical model:** unchanged; canonical remains LoL v0.3.58  
**Purpose:** prevent new-chat execution drift, silent mid-slate rule mutation, missing-gate TAKES, outcome-driven patching, and post-outcome hindsight from substituting for pre-entry validation.

This procedure changes governance/execution only. It does not create a new analytical model version.

## 1. Session authority lock

A live shadow-audit slate must run against one frozen analytical authority snapshot.

Canonical lock ledger:
`models/lol/session/CURRENT_SESSION_LOCK.md`

Each active lock must record:

- Lock ID;
- status `ACTIVE` / `CLOSED` / `CIRCUIT_BREAKER`;
- effective time in UTC+7;
- authority commit SHA;
- active analytical model;
- reason / authorization for the lock;
- circuit-breaker state.

### New-chat behavior

Every new chat must still fetch `models/lol/CURRENT_MODEL.md` first and then `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`.

The bootstrap must then fetch `models/lol/session/CURRENT_SESSION_LOCK.md`.

If an `ACTIVE` lock exists:

1. use its `authority_commit` as the frozen source for all analytical/procedural files for that slate;
2. re-fetch `CURRENT_MODEL.md` at that commit and use that locked copy as the effective authority;
3. follow the locked `CURRENT_MODEL.md` load order at the same commit;
4. do not allow later default-branch edits to alter live decisions in the locked slate;
5. if the lock cannot be read, the commit cannot be fetched, or the locked model conflicts with the expected model hierarchy, fail closed to `MODEL LOCK MISMATCH — HOLD`.

Default slate boundary is the UTC+7 calendar day. A user may explicitly authorize an immediate relock/new epoch before the day ends. A normal win or loss never authorizes a relock.

If no active lock exists for the current slate, create one from the fully bootstrapped current authority before the first TAKE-eligible live decision. Match prep and HOLD analysis may occur while the lock is being established, but no TAKE may be issued until the lock is valid.

## 2. No silent mid-slate analytical mutation

Once the slate is locked:

- ordinary match outcomes do not change the active stack;
- a valid model loss does not trigger a rule amendment;
- reviews and proposed fixes may be written during the slate, but they are `PENDING_NEXT_SLATE` unless the user explicitly authorizes an immediate relock;
- a newer default-branch file or later commit is not active merely because it exists;
- a new chat must inherit the lock, not reconstruct the model from conversation memory.

This prevents the sequence: lose -> patch -> continue under a different hidden model.

## 3. Mandatory TAKE gate signature

Before every visible `TAKE`, resolve a machine-like gate signature internally. Compact visible output is allowed, but every required field must be explicitly `PASS` or valid `N/A` before TAKE.

If any required field is missing, implied, contradictory, `FAIL`, or `UNRESOLVED`, verdict is `HOLD/PASS`.

### Common TAKE signature

Every market family must resolve:

- `LOCK` — active session authority lock matches the loaded stack;
- `MODEL` — active model/version exact match;
- `EXEC` — displayed market executable, not greyed/stale;
- `ODDS` — price meets canonical minimum;
- `FAMILY` — no prior TAKE in the same map/market family;
- `POSBLIND` — position-blind reassessment completed;
- `STATE` — current evidence/state is usable under the scoreboard protocol;
- `MARKET_GATE` — all family-specific gates below resolved.

### Live Moneyline signature

Required:

`LOCK | MODEL | EXEC | ODDS | FAMILY | POSBLIND | 2SNAP | LD | DRAFT_PRIOR_STATE | CFC_CURRENT | NEUTRAL_FIGHT_STRESS_CURRENT | LRO/N-A | SMR/N-A`

Lead Decomposition must include the retained role/structure/objective-control decomposition. `CFC_CURRENT = PASS` cannot be inferred from gold lead alone.

The neutral-fight stress test uses current live items/levels/role economy and treats `neutral` as approximately neutral positioning/entry, not equalized economy or a reset to the post-draft state.

If the contemplated ML selection opposes an original `CLEAR` or `STRONG` draft edge, `LRO = PASS` is mandatory under:

`models/lol/procedures/LOL_LIVE_ML_DRAFT_PRIOR_DEGRADATION_AND_REGIME_OVERRIDE_2026-08-21.md`

That path requires a compact sub-signature:

`LRO[3SNAP | 2CYCLE | REGIME_PERSISTENCE | MULTI_ROLE_LEVERAGE | DPS=BROKEN | CFC_CURRENT | NEXT_CYCLE_STRESS | DRP]`

All fields must PASS. If the ML aligns with the original CLEAR/STRONG draft edge, or the draft edge was only SLIGHT/EVEN/UNCLEAR, `LRO=N/A` is valid and the retained two-snapshot Live ML path applies.

A draft prior cannot remain a hidden permanent ML veto after `DPS=BROKEN` and `LRO=PASS` are established. Conversely, live ML regime override never creates or upgrades draft-only proof for underdog +kills.

### Favorite -kills signature

Required:

`LOCK | MODEL | EXEC | ODDS | FAMILY | POSBLIND | 2SNAP | SIGNED_MARGIN | COVER_THRESHOLD | RNE | FFD | REMAINING_FORCED_FIGHTS | STRUCTURE_SUBSTITUTION | SAFE_CONCEDE_TEST | KCV/NKB retained checks`

Exact arithmetic describes the required expansion; it does not itself certify the bet.

### Underdog +kills signature

Required:

`LOCK | MODEL | EXEC | ODDS | FAMILY | POSBLIND | 2SNAP | DIM | TAM | CAS | UDKC_STABLE | KPA | KMS | RLD | FALSE_STABLE_INACTIVE | UCS | SIGNED_MARGIN | EXACT_NKB | LIVE_PRESERVATION`

`DIM` is the mandatory draft interaction layer from `LOL_DRAFT_INTERACTION_MATRIX_2026-08-20.md`. `DIM = PASS` requires exact-role resolution and completion of the mechanism map, including `TAM — Threat-Answer Matching` and `CAS — Collapse Asymmetry`. `TAM` or `CAS` `FAIL/UNRESOLVED` forbids `KMS = PASS` and therefore forbids UDKC `STABLE`.

`UDKC_STABLE` is draft-only. `UCS` is a separate downstream live cushion gate and cannot be satisfied by UDKC alone.

### Total Kills Under signature

Required:

`LOCK | MODEL | EXEC | ODDS | FAMILY | POSBLIND | 2SNAP | TK_FRAMEWORK | FRP | NEXT_COMPULSORY_CYCLE | PRICE`

`FRP` must be positively adjudicated. Passive quiet is not enough.

### Total Kills Over signature

Required:

`LOCK | MODEL | EXEC | ODDS | FAMILY | POSBLIND | 2SNAP | RETAINED_TK_OVER_FRAMEWORK | RECURRENCE/CONTACT_PRESSURE | PRICE`

Do not import the Under FRP gate as a generic veto for Over.

### Duration Under signature

Required:

`LOCK | MODEL | EXEC | ODDS | FAMILY | POSBLIND | SHORTEST_CLOSE_ROUTE | FCR_ROBUST | STRUCTURE_STATE | PRICE`

### Duration Over signature

Required:

`LOCK | MODEL | EXEC | ODDS | FAMILY | POSBLIND | POSITIVE_CLOCK_MECH_1 | POSITIVE_CLOCK_MECH_2 | FAILED_CONVERSION_OR_EQUIVALENT | STRUCTURE_SUBSTITUTION | SHORTEST_CASCADE_TEST | PRICE`

Low kills and low tower count are not positive clock mechanisms by themselves.

## 4. Mechanical pre-TAKE interlock

This is a hard execution barrier. It exists specifically so a future real-money workflow cannot depend on the analyst remembering to apply prose rules correctly.

### 4.1 Certificate must exist before the verdict

Before the word `TAKE` may be emitted, construct a complete **PRE_TAKE_CERT** for the contemplated selection from the currently locked authority and the synchronized state/price pair.

The certificate must contain:

- exact map identifier;
- exact market family and selection;
- exact displayed odds/line;
- evidence clock/state identifier;
- active Lock ID and authority commit;
- every common and family-specific required gate field;
- every exact arithmetic field required by that family.

The certificate is pre-entry evidence. It may not be completed from a later fight, later price, result, or postgame interpretation.

### 4.2 Mechanical schema validation

Run a fail-closed validation of PRE_TAKE_CERT before the visible verdict.

Validation passes only when:

1. every required field for that family is present exactly once;
2. every categorical gate is an allowed terminal value: `PASS` or an explicitly permitted `N/A`;
3. `FAIL`, `UNRESOLVED`, `UNKNOWN`, omitted, blank, implied, or narrative-only fields fail validation;
4. exact numeric fields such as signed margin, failure/cover threshold, NKB/RNE, odds and line are actually populated where required;
5. the Lock ID/model/authority commit match the currently loaded locked stack;
6. the market family is unused for the map;
7. the executable price and assessed live state belong to the same usable decision window.

There is no analyst override for a failed certificate.

**Mechanical result:**

- `PRE_TAKE_CERT = PASS` -> the candidate may proceed to a visible TAKE;
- anything else -> `HOLD/PASS`, with no position created.

### 4.3 State-change expiry

A PRE_TAKE_CERT expires immediately if a material state change occurs before entry, including a fight, meaningful kill change, objective capture, structure change, or other decision-critical live transition.

If the state changes during the decision/entry window:

- `STATE/EXEC = FAIL` for the old certificate;
- the old certificate cannot be reused;
- obtain a fresh synchronized state/price pair;
- rebuild and revalidate PRE_TAKE_CERT from zero before any TAKE.

A stale certificate may never be repaired by editing only the changed fields.

### 4.4 Visible verdict and ledger ordering

The operational order is fixed:

`evidence -> PRE_TAKE_CERT build -> mechanical validation -> visible verdict -> Airtable position write -> exact record verification`

Never use:

`visible TAKE -> fill missing gates afterward`.

If the persisted Airtable `GATE_SIG[...]` does not exactly reflect the already-passed PRE_TAKE_CERT, treat that as an execution failure and trigger the circuit breaker.

### 4.5 Anti-hindsight accounting

Postgame review may diagnose a prediction but cannot rewrite what the model predicted.

Hard rules:

- a settled TAKE remains a recorded model prediction with its actual Win/Loss result and P/L;
- a later analytical re-read may be labeled `POSTGAME DIAGNOSTIC`, but it cannot convert the historical prediction into a fictional pre-entry HOLD;
- an audit may classify a TAKE as procedurally invalid only when contemporaneous entry evidence proves that an active pre-entry hard gate or execution rule was actually violated;
- the final game result by itself is never evidence of a pre-entry gate failure;
- procedural invalidation does not erase the prediction result from performance accounting; keep prediction outcome/P&L and process-validity as separate dimensions;
- performance summaries must not improve win rate or model accuracy by removing losing predictions merely because a later review says the analysis should have been different.

Therefore every reviewed TAKE has two independent labels:

1. `PREDICTION_RESULT = WIN / LOSS / PUSH / VOID`; and
2. `PROCESS_VALIDITY = VALID / INVALIDATED`.

A valid loss is a model miss/variance event. An invalidated loss is still a historical losing prediction plus an execution failure. Neither may be presented as though the model correctly predicted HOLD before the event.

### 4.6 Real-money readiness consequence

The mechanical interlock is mandatory before any future policy could permit actual exposure above `0u`.

No discussion of real-money readiness may treat prose compliance as sufficient. A prerequisite is demonstrated shadow operation with the interlock producing **zero missing-gate, stale-certificate, or post-TAKE certificate-completion violations** over the evaluation sample.

This section does not itself authorize real-money betting or change the current `0u` actual-exposure policy.

## 5. Gate-signature persistence

For every TAKE position, Airtable `Entry Evidence` must include a compact `GATE_SIG[...]` block containing the resolved family signature.

Example:

`GATE_SIG[LOCK=P;MODEL=P;2SNAP=P;DIM=P;TAM=P;CAS=P;UDKC=P;KMS=P;RLD=P;UCS=P;NKB=7;...]`

For a Live ML TAKE against a CLEAR/STRONG draft prior, also persist the compact LRO sub-signature, for example:

`LRO[3SNAP=P;2CYCLE=P;REGIME=P;MULTI_ROLE=P;DPS=BROKEN;CFC_CURRENT=P;NEXT_CYCLE=P;DRP=P]`

The visible verdict remains first. Logging happens after the verdict under the existing Airtable integrity procedure.

A missing historical `GATE_SIG` does not retroactively void old records, but all new TAKES after this governance activation require it.

## 6. Procedural circuit breaker

The circuit breaker is triggered by an execution failure, not by ordinary variance.

Trigger immediately if any of the following occurs:

- a visible TAKE is later found to have violated an active hard gate;
- a TAKE was issued without a complete mandatory gate signature;
- `PRE_TAKE_CERT` was missing, failed, incomplete, or completed after the visible TAKE;
- an expired pre-state-change certificate was reused after a material live transition;
- the wrong model/version or unlocked authority was used;
- draft-only proof was supplied by live state where prohibited;
- a market-family hard gate was skipped or substituted by narrative confidence;
- under an authority commit containing DIM, an underdog +kills TAKE was issued without resolving `DIM/TAM/CAS` as required;
- under an authority commit containing the Live ML regime override, an ML TAKE against a CLEAR/STRONG draft prior was issued without resolving the required `LRO[...]` fields.

When triggered:

1. status becomes `TAKE SUSPENDED — PROCEDURAL CIRCUIT BREAKER`;
2. continue analysis/HOLD logging if useful, but create no new positions;
3. audit the exact failure and write any proposed fix;
4. do not activate the fix inside the locked slate automatically;
5. resume TAKES only at the next valid slate lock or after explicit user authorization to relock now;
6. update `CURRENT_SESSION_LOCK.md` so the breaker state persists across chats.

A fully canonical bet that simply loses does **not** trigger the circuit breaker.

## 7. Outcome-driven change prohibition

Do not change the active analytical model because one bet or one short losing run failed.

A valid loss should be classified as one of:

- expected variance;
- mechanism miss under otherwise valid certification;
- calibration candidate requiring batch evidence.

A rule change requires a mechanism-level review, not the result alone. New safeguards that correct a proven procedural omission may be written, but the active slate remains frozen unless explicitly relocked.

Post-outcome analytical diagnosis must not be used to relabel a historical losing prediction as though the model had issued HOLD before entry. Process validity and prediction result are separate audit dimensions under Section 4.5.

## 8. Fix verification standard

Never say a governance/model fix is durable merely because it was discussed in chat.

A claimed durable fix requires:

1. write to the canonical GitHub file(s);
2. fetch the written file(s) back;
3. verify the exact new requirement exists;
4. include the resulting change in the next authority lock;
5. if the current slate is already locked, keep the change pending unless explicit relock authorization was given.

This is mandatory for any future statement such as `fixed`, `canonical`, `saved`, or `future chats will inherit this`.

## 9. Handoff rule

Handoffs carry state, not authority.

They may include:

- current map/series;
- exact drafts/roles;
- persisted UDKC state;
- snapshots;
- open/settled positions;
- circuit-breaker state;
- Session Lock ID and authority commit.

They must not override the lock, `CURRENT_MODEL.md`, or bootstrap.

## 10. Reference incidents

This guard was introduced after the 2026-08-19/20 chat-transition audit found several visible TAKES that were later audit-invalidated and found that a previously discussed underdog-cushion safeguard had not actually been persisted into canonical authority.

The DIM extension was added after BLG vs LGD Game 3 showed that a full-looking UDKC could still be wrong when generic defensive utility was not matched against the favorite's actual kill mechanism.

The Live ML regime-override extension was added after NS vs T1A Game 1 showed that a CLEAR draft prior could remain an unintended live veto even after repeated current-state role/objective evidence had degraded the mechanisms supporting that prior.

The mechanical PRE_TAKE_CERT interlock and anti-hindsight accounting were added after DK vs GEN Game 3 exposed that a visible TAKE could be emitted even though required DIM/TAM/CAS fields were absent, followed by a postgame temptation to describe the loss as something the model 'should have held.' The correction is procedural: block incomplete TAKES before money could be committed, and preserve the actual prediction result afterward.

References:
- `models/lol/reviews/CHAT_TRANSITION_EXECUTION_DRIFT_AND_SESSION_LOCK_REVIEW_2026-08-20.md`
- `models/lol/reviews/BLG_LGD_G3_DRAFT_INTERACTION_REVIEW_2026-08-20.md`
- `models/lol/reviews/NS_T1A_G1_LIVE_ML_DRAFT_PRIOR_ANCHORING_REVIEW_2026-08-21.md`
- `models/lol/reviews/DK_GEN_G3_GEN_PLUSKILLS_DIM_EXECUTION_REVIEW_2026-08-22.md`
