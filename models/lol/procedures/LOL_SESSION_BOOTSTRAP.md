# LoL Session Bootstrap — Mandatory New-Chat Guardrail

**Status:** ACTIVE GOVERNANCE  
**Effective:** 2026-08-18 UTC+7  
**Amended:** 2026-08-20 UTC+7  
**Authority:** `models/lol/CURRENT_MODEL.md`

## Purpose

Prevent authority drift, stale-version blending, skipped market gates, false logging claims, unnecessary external roster lookup, missing persistence, outcome-driven mid-slate model changes, and execution drift when a LoL audit continues in a new chat or after context compression.

This procedure is governance/execution control. It does not create a new analytical model version.

## 1. GitHub authority bootstrap

At the start of every new chat/session for the LoL project:

1. Fetch `models/lol/CURRENT_MODEL.md` first from the repository default branch.
2. Immediately load this file: `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`.
3. Immediately fetch `models/lol/session/CURRENT_SESSION_LOCK.md` if it exists.
4. Load `models/lol/procedures/LOL_SESSION_AUTHORITY_LOCK_TAKE_SIGNATURE_AND_CIRCUIT_BREAKER_2026-08-20.md`.
5. If the session lock is `ACTIVE`, re-fetch `CURRENT_MODEL.md` at the lock's `authority_commit` and treat that locked copy as the effective authority for the slate.
6. Load all analytical/procedural files for the slate from the same locked authority commit unless a file is explicitly a mutable state ledger such as the session lock or Airtable live ledger.
7. Follow the exact required load order in the locked `CURRENT_MODEL.md`.
8. Load the latest applicable live handoff last. Handoffs carry state only; where a handoff conflicts with locked authority, locked authority wins.
9. Do not trust a model version stated in conversation memory, project context, pasted transfer prompts, older handoffs, or prior assistant output when it conflicts with locked GitHub authority.
10. Do not load, blend, or revive a retired analytical version merely because it has a higher version number or appears in historical records.

### Session-lock fail closed

If an `ACTIVE` lock exists but its authority commit cannot be fetched, the active model cannot be matched, or the loaded files come from a different analytical commit, model-certified analysis is blocked.

Visible status when a live verdict is required:

`MODEL LOCK MISMATCH — HOLD`

Do not silently fall back to the default branch.

### No active lock

If no active lock exists for the current UTC+7 slate, complete bootstrap from current authority and establish a lock before the first TAKE-eligible decision.

Match prep and HOLD analysis may continue while a lock is being established, but no TAKE may be issued without a valid lock.

Default slate boundary is the UTC+7 calendar day. An explicit user instruction may authorize an immediate relock/new epoch.

Mandatory lock procedure:
`models/lol/procedures/LOL_SESSION_AUTHORITY_LOCK_TAKE_SIGNATURE_AND_CIRCUIT_BREAKER_2026-08-20.md`

## 2. Fail-closed bootstrap rule

No model-certified match analysis may begin until the authority bootstrap and mandatory load sequence are complete.

If live evidence arrives before bootstrap is complete, the visible verdict must be:

`MODEL NOT LOADED — HOLD`

No connector/tool call may precede that visible HOLD. After the visible HOLD, complete bootstrap immediately, then reassess the same evidence if still usable.

This preserves the live rule: **verdict first; no connector/logging work before the visible live verdict.**

## 3. Mandatory model-lock assertion

Before the first model-certified live verdict of a session, internally verify all of the following:

- active model exactly matches the locked `CURRENT_MODEL.md`;
- active `authority_commit` is known when a lock is active;
- retired versions are identified and excluded;
- mandatory procedures/reviews required by the locked load order were loaded;
- `LOL_UNDERDOG_PLUSKILLS_DRAFT_LOCK_GUARD_2026-08-19.md` is loaded;
- `LOL_UNDERDOG_CUSHION_SUFFICIENCY_2026-08-20.md` is loaded;
- `LOL_FRP_POSITIVE_EVIDENCE_EXECUTION_CALIBRATION_2026-08-20.md` is loaded;
- `LOL_SESSION_AUTHORITY_LOCK_TAKE_SIGNATURE_AND_CIRCUIT_BREAKER_2026-08-20.md` is loaded;
- latest handoff was loaded last;
- shadow stake, minimum odds, market-family limits, and live-snapshot eligibility rules are known;
- Airtable post-verdict logging procedure is loaded;
- procedural circuit-breaker state is known.

If any item is unresolved, fail closed to `MODEL NOT LOADED — HOLD`.

If circuit-breaker state is active, analysis may continue but TAKE issuance is blocked with:

`TAKE SUSPENDED — PROCEDURAL CIRCUIT BREAKER`

## 4. Saved lineup / roster context priority

For named-team match prep, use saved project lineup context before external web roster lookup.

- Search `models/lol/context/lineups/` for the teams/league first.
- A dated official match-specific lineup card saved there is the preferred starting lineup source.
- Treat saved lineups as dated evidence, not permanent roster locks; newer official match-specific lineup evidence supersedes older saved entries.
- If a current lineup is already present in saved project data, do not replace it with generic web roster pages merely because they are easier to find.
- External web lookup is a fallback for missing/uncertain lineup context or for checking whether a newer official lineup has superseded the saved one.
- Before applying a numeric team-strength prior, verify the current five-player lineup and any material substitutions/role swaps.

Current saved lineup index:
`models/lol/context/lineups/LCK_CL_2026_STARTING_LINEUPS.md`

## 5. Market-family hard gates

Compact output is allowed, but full underlying analysis is mandatory.

Before every TAKE, the mandatory TAKE gate signature from the session-lock procedure must be fully resolved. A narrative summary is never a substitute for the signature.

### Total Kills Under

- full retained TK framework applies;
- `FRP = PASS` is mandatory;
- passive quiet / low historical kill pace cannot by itself satisfy FRP;
- next compulsory-contact cycle must be identified;
- **FRP is not a default HOLD gate**: once two-snapshot eligibility is satisfied, positively adjudicate PASS / FAIL / UNCERTAIN rather than asking for discretionary extra confirmation;
- repeated bounded kill recurrence across real objective/contact cycles is positive FRP evidence;
- a completed objective cycle can count as **suppressed compulsory contact** when the map progresses through concession, zoning, cross-map play, ranged defense, or low-risk objective control with bounded kills;
- Structure Substitution can support TK Under only when it removes future fight requirements, not merely because objectives replaced past fights;
- engage champions/buttons do not by themselves make next-cycle contact pressure HIGH — test whether the opponent actually must contest and whether re-engage/chase is required;
- after two distinct meaningful objective/contact cycles with bounded recurrence, explicitly test whether the regime should persist; do not automatically demand a third cycle;
- if future suppression is not positively demonstrated, `FRP = FAIL/UNCERTAIN -> PASS/HOLD`;
- if FRP and every other retained TK/pricing gate pass, do not add another unwritten confirmation layer.

Mandatory execution calibration:
`models/lol/procedures/LOL_FRP_POSITIVE_EVIDENCE_EXECUTION_CALIBRATION_2026-08-20.md`

Reference review:
`models/lol/reviews/TT_JDG_G2_TOTAL_KILLS_FRP_EXECUTION_REVIEW_2026-08-20.md`

### Duration Under

- shortest realistic close route must be tested;
- `FCR = ROBUST` is mandatory except an explicitly retained terminal exception;
- one ordinary disruption must not destroy the Under thesis.

### Duration Over

- low kills are not positive stall evidence by themselves;
- 0-0 towers / low tower count are neutral by default;
- at least two independent positive clock-consuming mechanisms are required;
- at least one must be observed `FAILED CONVERSION` or equivalent repeated denial/reset;
- Structure Substitution is mandatory;
- shortest plausible compulsory fight/objective -> structures -> base -> Nexus cascade must be tested.

### Live Moneyline

- two usable live snapshots required;
- position-blind reassessment required;
- Lead Decomposition (`RL / SL / OSC / CFC`) required;
- neutral-setup compulsory-fight stress test required;
- same-series SMR applies where the thesis relies on a previously failed mechanism;
- team strength and current gold are modifiers/context, not standalone TAKE authorization.

### Favorite -kills

- two usable live snapshots required;
- exact signed kill margin required;
- exact cover threshold and `RNE` required;
- `FFD` and remaining forced-fight schedule required;
- Structure Substitution / NKB / KCV / safe-concede routes must be tested;
- team strength or gold lead alone cannot authorize TAKE.

### Underdog +kills

- two usable live snapshots required;
- exact signed kill-margin arithmetic required;
- draft-locked fallback certification is fail-closed;
- a complete **UDKC — Underdog +Kills Draft Certificate** must exist before any underdog +kills TAKE;
- the UDKC must resolve DER / FRI / SRI / FER / PDC / PST / ARI / KPA / KMS / RLD / False-Stable Guard / DCR / FF / hard Draft-Collapse Veto;
- every mandatory PASS field must actually pass, False-Stable Guard must be INACTIVE, FF must be STABLE, and hard veto must be INACTIVE;
- omitted, implied, narrative-only, or `UNRESOLVED` certification fields force `PASS/HOLD`;
- UDKC is **draft-only, not timestamp-locked**: if the exact locked draft is first received after live play begins or a new chat starts mid-map, run the mandatory Draft-Isolation Pass before using the live state for +kills analysis;
- Draft Isolation must exclude current kills, gold, objectives, structures, current odds, current handicap size, and current margin from the certificate;
- if one screenshot contains both draft and live state, process **Phase A: draft-only UDKC**, then **Phase B: live reassessment**;
- missing persisted UDKC alone is not a veto when the exact draft can be recovered and fully certified; missing/ambiguous draft or incomplete UDKC remains fail-closed;
- live evidence may preserve or downgrade a draft-certified STABLE UDKC, but may never supply missing draft proof or upgrade a genuinely FRAGILE/ABSENT draft;
- `KPA` and `KMS` must both pass, in addition to retained FER/PDC/PST/ARI requirements;
- RLD is mandatory before KMS may pass;
- False-Stable Guard applies;
- theoretical engage, scaling, waveclear, peel/utility, safe ADC play, small current kill margin, or a large displayed +kills buffer cannot substitute for KMS;
- exact NKB / additional-net-kill arithmetic describes the hurdle only; it is never draft certification evidence;
- after STABLE UDKC, **UCS — Underdog Cushion Sufficiency** is mandatory as a separate live gate;
- `NKB <= 4` is `THIN` and defaults HOLD; it may pass only under the observed anti-cascade requirements in the UCS procedure;
- if one ordinary adverse fight + continuation can plausibly cross the failure threshold, `UCS` cannot pass;
- UDKC STABLE never substitutes for UCS.

Mandatory draft guard:
`models/lol/procedures/LOL_UNDERDOG_PLUSKILLS_DRAFT_LOCK_GUARD_2026-08-19.md`

Mandatory cushion guard:
`models/lol/procedures/LOL_UNDERDOG_CUSHION_SUFFICIENCY_2026-08-20.md`

Reference amendment:
`models/lol/reviews/UDKC_DRAFT_ISOLATION_AMENDMENT_2026-08-20.md`

### Missing gate

If any decision-critical gate or any required gate-signature field is missing, ambiguous, or not actually evaluated, the market is **not TAKE-eligible**. Use `PASS/HOLD`.

## 6. Mandatory TAKE gate signature

Before every TAKE, execute the family-specific `GATE_SIG[...]` defined in:

`models/lol/procedures/LOL_SESSION_AUTHORITY_LOCK_TAKE_SIGNATURE_AND_CIRCUIT_BREAKER_2026-08-20.md`

Hard rules:

- every required field must be explicit PASS or valid N/A;
- missing or unresolved field -> HOLD/PASS;
- compact visible commentary does not relax this requirement;
- the position `Entry Evidence` must persist the compact `GATE_SIG[...]` block after the verdict;
- failure to produce the signature is a procedural circuit-breaker trigger if a TAKE was visibly issued.

## 7. Procedural circuit breaker

The circuit breaker triggers on execution failure, not on a normal losing result.

Trigger conditions include:

- a TAKE later found to violate an active hard gate;
- a TAKE without a complete mandatory gate signature;
- authority/model mismatch;
- live evidence used to create prohibited draft proof;
- skipped/substituted family-specific gate.

When active:

- no new position may be created;
- analysis and HOLD snapshot logging may continue;
- proposed fixes may be written but remain pending under the current lock;
- resume only on next valid slate lock or explicit user authorization to relock now;
- circuit-breaker state must be persisted in `CURRENT_SESSION_LOCK.md`.

A fully canonical loss does not trigger it.

## 8. Version-vocabulary tripwire

If an assistant begins citing a retired model/version as active, or uses a later-version-only concept that is not explicitly incorporated into locked canonical authority:

1. stop model-certified analysis;
2. visible status becomes `MODEL AUTHORITY MISMATCH — HOLD` if an active live verdict is required;
3. reload locked `CURRENT_MODEL.md` and this bootstrap;
4. resume only after the model-lock assertion passes.

Do not silently blend conflicting material.

## 9. Airtable logging truthfulness

For every valid visible live verdict, follow the canonical post-verdict logging procedure.

- `PASS/HOLD`: write the exact live snapshot after the visible verdict; no position record.
- executable `TAKE`: write the snapshot and exact shadow position after the visible verdict.
- for new TAKES after 2026-08-20 governance activation, position Entry Evidence must include `GATE_SIG[...]`.
- verify the expected record exists after the write.
- never say `logged`, `settled`, or equivalent unless the corresponding Airtable mutation actually succeeded and the expected record was verified.
- if logging fails, state: `VERDICT VALID — LOGGING FAILED` and repair the ledger without altering the analytical verdict.
- a missing historical write may be backfilled only from original evidence and the original visible verdict.

## 10. No retrospective upgrade / no outcome patching

A later outcome cannot turn an earlier `PASS/HOLD` into a position.

A procedural-error TAKE may be recorded as the position that was visibly issued, but its audit must clearly state the correct canonical verdict when applicable.

A retrospective review may identify a missed qualifying TAKE window for calibration, but that does not create a historical position or rewrite the original visible verdict.

A valid loss does not authorize an analytical rule change by itself. Mechanism-level batch review is required. During an active session lock, changes remain pending unless the user explicitly authorizes a relock.

## 11. Durable-fix verification

Never claim a fix is durable because it was merely discussed in chat.

Before saying `fixed`, `canonical`, `saved`, or `future chats will inherit this`, require:

1. canonical GitHub write succeeded;
2. written file fetched back;
3. exact new requirement verified in fetched content;
4. change included in the applicable authority lock, or explicitly marked pending for the next slate.

## 12. New-chat prompt rule

Future transfer prompts must not hardcode a model version as independent authority. They should instruct the next chat to fetch `CURRENT_MODEL.md`, this bootstrap, and the session lock.

Minimum transfer instruction:

> Continue the LoL shadow-audit from `acchtt/SlipTrace`. Fetch `models/lol/CURRENT_MODEL.md` first, then `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`, then `models/lol/session/CURRENT_SESSION_LOCK.md`. If the lock is ACTIVE, use its authority commit for the analytical stack and do not silently use newer default-branch edits. Load the session authority-lock/TAKE-signature/circuit-breaker procedure, the FRP calibration, the UDKC draft guard, and UCS. Latest handoff loads last and carries state only. If bootstrap is incomplete, fail closed to `MODEL NOT LOADED — HOLD`; if lock authority mismatches, `MODEL LOCK MISMATCH — HOLD`; if the procedural circuit breaker is active, issue no new TAKES. Every TAKE requires a complete market-family `GATE_SIG[...]` and post-verdict Airtable verification.
