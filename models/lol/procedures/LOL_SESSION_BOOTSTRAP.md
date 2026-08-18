# LoL Session Bootstrap — Mandatory New-Chat Guardrail

**Status:** ACTIVE GOVERNANCE  
**Effective:** 2026-08-18 UTC+7  
**Authority:** `models/lol/CURRENT_MODEL.md`

## Purpose

Prevent authority drift, stale-version blending, skipped market gates, and false logging claims when a LoL audit continues in a new chat or after context compression.

This procedure is governance/execution control. It does not create a new analytical model version.

## 1. GitHub authority lock

At the start of every new chat/session for the LoL project:

1. Fetch `models/lol/CURRENT_MODEL.md` first.
2. Treat it as the sole authority for the active analytical model, retired versions, required files, and load order.
3. Do not trust a model version stated in conversation memory, project context, a pasted handoff prompt, an older handoff, or prior assistant output when it conflicts with `CURRENT_MODEL.md`.
4. Follow the exact required load order in `CURRENT_MODEL.md`.
5. Load the latest applicable live handoff last. Where the handoff conflicts with `CURRENT_MODEL.md`, `CURRENT_MODEL.md` wins.
6. Do not load, blend, or revive a retired analytical version merely because it has a higher version number or appears in historical records.

## 2. Fail-closed bootstrap rule

No model-certified match analysis may begin until the authority lock and mandatory load sequence are complete.

If a live screenshot/state arrives before bootstrap is complete, the visible verdict must be:

`MODEL NOT LOADED — HOLD`

No connector/tool call may precede that visible verdict. After the visible HOLD, complete the bootstrap immediately, then reassess from the same synchronized evidence if still valid.

This preserves the live rule: **verdict first; no connector/logging work before the visible live verdict.**

## 3. Mandatory model-lock assertion

Before the first model-certified live verdict of a session, internally verify all of the following:

- active model exactly matches `CURRENT_MODEL.md`;
- retired versions are identified and excluded;
- mandatory procedures/reviews required by the current load order were loaded;
- latest handoff was loaded last;
- shadow stake, minimum odds, market-family limits, and live-snapshot eligibility rules are known;
- Airtable post-verdict logging procedure is loaded.

If any item is unresolved, fail closed to `MODEL NOT LOADED — HOLD`.

## 4. Market-family hard gates

Compact output is allowed, but the underlying market-specific gate must be explicitly resolved before TAKE.

### Total Kills Under

- full retained TK framework applies;
- `FRP = PASS` is mandatory;
- passive quiet / low historical kill pace cannot by itself satisfy FRP;
- next compulsory-contact cycle must be identified;
- if future suppression is not positively demonstrated, `FRP = FAIL/UNCERTAIN` -> `PASS/HOLD`.

### Duration Under

- shortest realistic close route must be tested;
- `FCR = ROBUST` is mandatory except an explicitly retained terminal exception;
- one ordinary disruption must not destroy the Under thesis.

### Live Moneyline

- two synchronized snapshots required;
- position-blind reassessment required;
- Lead Decomposition (`RL / SL / OSC / CFC`) required;
- neutral-setup compulsory-fight stress test required.

### Favorite -kills

- two synchronized snapshots required;
- exact signed kill margin required;
- exact cover threshold and `RNE` required;
- `FFD` and remaining forced-fight schedule required;
- Structure Substitution / NKB / KCV / safe-concede routes must be tested;
- team strength or gold lead alone cannot authorize TAKE.

### Underdog +kills

- two synchronized snapshots required;
- exact signed kill-margin arithmetic required;
- draft-locked fallback certification is fail-closed;
- `KPA` and `KMS` must both pass, in addition to retained FER/PDC/PST/ARI requirements;
- False-Stable Guard applies;
- theoretical engage, scaling, waveclear, or safe ADC play cannot substitute for KMS.

### Missing gate

If any decision-critical gate is missing, ambiguous, or not actually evaluated, the market is **not TAKE-eligible**. Use `PASS/HOLD`.

## 5. Version-vocabulary tripwire

If an assistant begins citing a retired model/version as active, or uses a later-version-only concept that is not explicitly incorporated into the current canonical model:

1. stop model-certified analysis;
2. visible status becomes `MODEL AUTHORITY MISMATCH — HOLD` if an active live verdict is required;
3. reload `CURRENT_MODEL.md` and this bootstrap;
4. resume only after the model-lock assertion passes.

Do not silently blend the conflicting material.

## 6. Airtable logging truthfulness

For every valid visible live verdict, follow the canonical post-verdict logging procedure.

- `PASS/HOLD`: write the exact synchronized snapshot after the visible verdict; no position record.
- executable `TAKE`: write the snapshot and exact shadow position after the visible verdict.
- verify the expected record exists after the write.
- never say `logged`, `settled`, or equivalent unless the corresponding Airtable mutation actually succeeded and the expected record was verified.
- if logging fails, state: `VERDICT VALID — LOGGING FAILED` and repair the ledger without altering the analytical verdict.
- a missing historical write may be backfilled only from the original synchronized evidence and original visible verdict.

## 7. No retrospective upgrade

A later outcome cannot turn an earlier `PASS/HOLD` into a position. A procedural-error TAKE may be recorded as the position that was visibly issued, but its audit must clearly state that the correct canonical-model verdict was PASS/HOLD when applicable.

## 8. New-chat prompt rule

Future transfer prompts must not hardcode a model version as independent authority. They should instruct the next chat to fetch `CURRENT_MODEL.md` first and obey this bootstrap.

The minimum transfer instruction is:

> Continue the LoL shadow-audit from `acchtt/SlipTrace`. Fetch `models/lol/CURRENT_MODEL.md` first, then load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md` and follow the exact required load order. GitHub is model authority; latest handoff loads last. If bootstrap is incomplete, fail closed to `MODEL NOT LOADED — HOLD`.
