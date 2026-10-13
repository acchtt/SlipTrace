# Football v2 — Decision States

Decision States stores the current /xi or /live assessment epoch.

Active base/table routing comes from ACTIVE_MODEL_ROUTING.json.

## 1. Identity

Every row must identify:

- Assessment ID;
- canonical match / fixture ID;
- competition;
- assessment time;
- evidence epoch;
- current fixture status;
- score/minute for started fixtures.

Never update an unrelated old-base record because names happen to match.

## 2. Frozen Step-1 reference

For a routine V4 match retain the verified Step-1 identity:

- Run/Coverage identity;
- C board state/rank/supported line/lane;
- C2 board state/rank/supported line;
- model_evidence_sha256 or equivalent verified rank reference.

Do not replay or rewrite the Step-1 board inside Decision States.

## 3. Football assessment

Persist the exact current C and C2 football result JSON.

Football C and C2 share the factual evidence epoch but own policy fields
independently.

C owns its completion/continuation/leakage/stall diagnostics and official
action.

C2 owns its route-quality state, supported line, optional independent
c2_opponent_leakage + c2_opponent_leakage_basis and shadow action.

Never reconstruct missing C2 model fields from C.

## 4. Assessment execution status

Use XI Assessment Execution Status.

Active values:

- EXECUTED_C_C2_FOOTBALL_ONLY
- EXECUTED_C_C2_FOOTBALL_AND_PRICE
- ENGINE_FAILED_AFTER_ATTEMPT

If football assessment succeeded but an optional strict price gate failed,
store EXECUTED_C_C2_FOOTBALL_ONLY and the price blocker in normal notes.
Do not falsely label the model engine failed.

## 5. Observed price / screenshot

An observed user screenshot is normal quote evidence, not an executable offer.

Persist where available:

- evaluated line;
- evaluated odds;
- bookmaker/source label;
- original attachment/capture reference;
- original capture time if known.

Do not use a special USER_SCREENSHOT_ONLY_JSON marker in Evidence Summary.

Observed quote ACT/WAIT/PASS remains conditional and non-executable.

## 6. WAIT

Persist model WAIT target/minimum and its current reachability basis when the
model actually returns WAIT.

WAIT is not exposure merely because it exists in Decision States.

Do not write WAIT_ASSUMED or SHADOW_WAIT_ASSUMED for new assessments.

## 7. Strict executable price decision

A strict prematch C/C2 decision requires real current execution evidence.

Persist:

- exact current quote;
- C strict result;
- C2 strict shadow result;
- C action;
- C2 shadow action;
- engine source revision;
- evidence epoch.

After write, independently refetch once. The final publication guard compares
that readback to the already executed pair and confirms quote/fixture/evidence
freshness. It does not rerun C/C2.

## 8. Publication

Only Football C may create an official Website Pick.

C2 remains shadow-only.

Observed/screenshot comparisons never publish.

WATCH and unresolved WAIT never create synthetic Website Pick exposure.

## 9. Actual user bets

Decision States is not the user's betting ledger.

Only explicit user-confirmed slips belong in Actual Bets — Current. Do not
interpret C-BET, C-WAIT, Website Pick or screenshot evidence as proof that the
user placed a wager.

## 10. Readback

One assessment write -> one independent readback.

Verify:

- active base;
- exact Assessment ID / match identity;
- XI Assessment Execution Status;
- exact C/C2 football result JSON;
- evaluated line/odds when a quote comparison was persisted;
- strict pair result when a strict executable decision was persisted.

If any required field differs, report PERSISTENCE_UNVERIFIED.
