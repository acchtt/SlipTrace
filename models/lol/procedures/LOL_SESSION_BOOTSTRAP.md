# LoL Session Bootstrap — Mandatory New-Chat Guardrail

**Status:** ACTIVE GOVERNANCE  
**Effective:** 2026-08-18 UTC+7  
**Amended:** 2026-08-20 UTC+7  
**Authority:** `models/lol/CURRENT_MODEL.md`

## Purpose

Prevent authority drift, stale-version blending, skipped market gates, false logging claims, unnecessary external roster lookup, and execution drift that turns named gates into generic HOLD bias when a LoL audit continues in a new chat or after context compression.

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
- `LOL_UNDERDOG_PLUSKILLS_DRAFT_LOCK_GUARD_2026-08-19.md` is loaded;
- `LOL_FRP_POSITIVE_EVIDENCE_EXECUTION_CALIBRATION_2026-08-20.md` is loaded;
- latest handoff was loaded last;
- shadow stake, minimum odds, market-family limits, and live-snapshot eligibility rules are known;
- Airtable post-verdict logging procedure is loaded.

If any item is unresolved, fail closed to `MODEL NOT LOADED — HOLD`.

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

Compact output is allowed, but the underlying market-specific gate must be explicitly resolved before TAKE.

### Total Kills Under

- full retained TK framework applies;
- `FRP = PASS` is mandatory;
- passive quiet / low historical kill pace cannot by itself satisfy FRP;
- next compulsory-contact cycle must be identified;
- **FRP is not a default HOLD gate**: once two-snapshot eligibility is satisfied, positively adjudicate PASS / FAIL / UNCERTAIN rather than asking for discretionary extra confirmation;
- repeated bounded kill recurrence across real objective/contact cycles is positive FRP evidence;
- a completed objective cycle can count as **suppressed compulsory contact** when the map progresses through concession, zoning, cross-map play, ranged defense, or low-risk objective control with bounded kills;
- Structure Substitution can support TK Under only when it **removes future fight requirements**, not merely because objectives replaced past fights;
- engage champions/buttons do not by themselves make next-cycle contact pressure HIGH — test whether the opponent actually must contest and whether re-engage/chase is required;
- after two distinct meaningful objective/contact cycles with bounded recurrence, explicitly test whether the regime should persist; do not automatically demand a third cycle;
- if future suppression is not positively demonstrated, `FRP = FAIL/UNCERTAIN` -> `PASS/HOLD`;
- if `FRP = PASS` and every other retained TK/pricing gate passes, do not add another unwritten confirmation layer.

Mandatory execution calibration:
`models/lol/procedures/LOL_FRP_POSITIVE_EVIDENCE_EXECUTION_CALIBRATION_2026-08-20.md`

Reference review:
`models/lol/reviews/TT_JDG_G2_TOTAL_KILLS_FRP_EXECUTION_REVIEW_2026-08-20.md`

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
- False-Stable Guard applies;
- theoretical engage, scaling, waveclear, peel/utility, safe ADC play, small current kill margin, or a large displayed +kills buffer cannot substitute for KMS;
- exact NKB / additional-net-kill arithmetic describes the hurdle only; it is never certification evidence.

Mandatory guard:
`models/lol/procedures/LOL_UNDERDOG_PLUSKILLS_DRAFT_LOCK_GUARD_2026-08-19.md`

Reference amendment:
`models/lol/reviews/UDKC_DRAFT_ISOLATION_AMENDMENT_2026-08-20.md`

### Missing gate

If any decision-critical gate is missing, ambiguous, or not actually evaluated, the market is **not TAKE-eligible**. Use `PASS/HOLD`.

## 6. Version-vocabulary tripwire

If an assistant begins citing a retired model/version as active, or uses a later-version-only concept that is not explicitly incorporated into the current canonical model:

1. stop model-certified analysis;
2. visible status becomes `MODEL AUTHORITY MISMATCH — HOLD` if an active live verdict is required;
3. reload `CURRENT_MODEL.md` and this bootstrap;
4. resume only after the model-lock assertion passes.

Do not silently blend the conflicting material.

## 7. Airtable logging truthfulness

For every valid visible live verdict, follow the canonical post-verdict logging procedure.

- `PASS/HOLD`: write the exact synchronized snapshot after the visible verdict; no position record.
- executable `TAKE`: write the snapshot and exact shadow position after the visible verdict.
- verify the expected record exists after the write.
- never say `logged`, `settled`, or equivalent unless the corresponding Airtable mutation actually succeeded and the expected record was verified.
- if logging fails, state: `VERDICT VALID — LOGGING FAILED` and repair the ledger without altering the analytical verdict.
- a missing historical write may be backfilled only from the original synchronized evidence and original visible verdict.

## 8. No retrospective upgrade

A later outcome cannot turn an earlier `PASS/HOLD` into a position. A procedural-error TAKE may be recorded as the position that was visibly issued, but its audit must clearly state that the correct canonical-model verdict was PASS/HOLD when applicable.

A retrospective review may identify a **missed qualifying TAKE window** for calibration, but that does not create a historical position or rewrite the original visible verdict.

## 9. New-chat prompt rule

Future transfer prompts must not hardcode a model version as independent authority. They should instruct the next chat to fetch `CURRENT_MODEL.md` first and obey this bootstrap.

The minimum transfer instruction is:

> Continue the LoL shadow-audit from `acchtt/SlipTrace`. Fetch `models/lol/CURRENT_MODEL.md` first, then load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md` and follow the exact required load order. GitHub is model authority; latest handoff loads last. Use saved lineup context under `models/lol/context/lineups/` before external roster lookup. If bootstrap is incomplete, fail closed to `MODEL NOT LOADED — HOLD`. Load the FRP positive-evidence execution calibration so Total Kills FRP is positively adjudicated rather than used as a generic HOLD veto. For underdog +kills, require a complete draft-only UDKC; if none is persisted but the exact locked draft is available, reconstruct it with Draft Isolation before applying live state. Missing/ambiguous draft or incomplete mechanism certification remains HOLD/PASS.
