# Current League of Legends Model

**Canonical namespace:** `models/lol/`

## ACTIVE MODEL

- Active analytical model: **LoL v0.3.58**
- Active rules: `models/lol/rules/MODEL_RULES_LOL_V0.3.58.md`
- Canonical reset authority: `models/lol/procedures/LOL_V0.3.58_CANONICAL_RESET_2026-08-16.md`
- Mandatory new-chat bootstrap: `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`
- **LoL v0.3.59 and v0.3.60 are retired/discarded from the active analytical hierarchy.**
- Their files may remain only as historical/audit artifacts. Do not load, blend, or auto-restore them.

User instruction on 2026-08-16 UTC+7: **"Discard newer versions, update this version accordingly".**

The prior temporary v0.3.58 override is ended. v0.3.58 is now the canonical model, not a temporary rollback.

## Mandatory session bootstrap / authority-drift guard

Every new chat/session must fetch this `CURRENT_MODEL.md` first, then immediately load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md` before continuing the remaining load order.

Conversation memory, project context, pasted transfer prompts, older handoffs, historical model labels, and prior assistant output are never allowed to override this file's active/retired model hierarchy.

If live evidence arrives before bootstrap is complete, the only valid visible verdict is:

`MODEL NOT LOADED — HOLD`

No tool call may precede that visible HOLD. Bootstrap then completes and the same synchronized evidence may be reassessed if still valid.

A model/version vocabulary mismatch is a hard tripwire: stop model-certified analysis, reload this file + the bootstrap, and fail closed until the authority lock passes.

Reference incident review:
`models/lol/reviews/DNS_NS_G3_SESSION_BOOTSTRAP_AND_FRP_EXECUTION_REVIEW_2026-08-18.md`

## Canonical v0.3.58 in-place amendments

### Duration Over — Structure Substitution / real stall evidence

The active v0.3.58 file includes the KRX vs BRO Game 2 correction:

- low kills are not positive Duration stall evidence by themselves;
- 0-0 towers / no first tower / low absolute tower count are neutral state descriptors by default;
- conversion evidence must be classified as `ABSENT CONVERSION` or `FAILED CONVERSION`;
- only actual failed conversion or another clearly observed clock-consuming defense/reset mechanism may support the structure portion of an Over thesis;
- Structure Substitution is mandatory — objective/tower progress can compress clock even while kills remain low;
- a Duration Over requires two independent positive clock-consuming mechanisms, with at least one grounded in observed failed conversion or equivalent repeated denial;
- every Duration Over must test the shortest plausible next compulsory fight/objective -> serial structures -> base -> Nexus cascade.

Reference:
`models/lol/reviews/KRX_BRO_G2_DURATION_STRUCTURE_SUBSTITUTION_REVIEW_2026-08-16.md`

### Daily-audit gap fix — active inside v0.3.58

On 2026-08-16 the user instructed: **"Fix whats lacking and prepare for lec".** The following narrow controls were therefore incorporated directly into canonical v0.3.58:

- **FRP — Forward Regime Persistence** for every Total Kills Under;
- **FCR — Fast-Close Robustness** / one-disruption stress test for every normal Duration Under;
- **Lead Decomposition + CFC — Compulsory Fight Control** for every live Moneyline;
- **SMR — Same-Mechanism Re-certification** when a later same-series TAKE relies on a previously diagnosed failed mechanism.

Reference:
`models/lol/reviews/V0.3.58_CANONICAL_GAP_FIX_2026-08-16.md`

These controls are active because they are now written into `MODEL_RULES_LOL_V0.3.58.md`. Do not load v0.3.59/v0.3.60 to obtain them.

### Underdog +kills — Kill Production vs Kill-Margin Suppression

After KC vs GIANTX Game 1 on 2026-08-18 UTC+7, the fallback-floor procedure was amended in place to correct a false-`STABLE` underdog +kills certification.

Mandatory distinction:

- **KPA — Kill Production Ability:** can the underdog still generate kills while behind?
- **KMS — Kill-Margin Suppression:** can the underdog plausibly prevent the favorite from repeatedly converting advantages into net kill-margin expansion?

`STABLE` now requires both KPA and KMS to pass, in addition to the existing FER/PDC/PST/ARI requirements. Engage, scaling, waveclear, safe marksman play or theoretical return-kill tools cannot by themselves prove KMS.

The False-Stable Guard must activate when the favorite has repeatable range/zone/siege/continuation routes and the underdog's kill routes depend on entering the same controlled space without an independent reset/survival route.

Team strength remains a modifier, not a standalone veto. A materially stronger favorite plus superior repeatable control routes increases the proof burden for KMS but does not automatically authorize favorite -kills.

`0-0 towers` remains neutral and must not be used as an implicit anti-control signal. Strong favorite control can exist before structural conversion when multiple mechanism signals jointly support it.

References:
- `models/lol/reviews/KC_GX_G1_UNDERDOG_KILLS_FALSE_STABLE_REVIEW_2026-08-18.md`
- `models/lol/procedures/LOL_FALLBACK_FLOOR_CERTIFICATION_2026-08-13.md`

This is an in-place v0.3.58 procedural amendment. Do not create or load v0.3.59/v0.3.60 for it.

### Underdog +kills — Role-Leverage Decomposition

After DNS vs BRO Game 1 on 2026-08-19 UTC+7, the fallback-floor procedure was clarified in place to prevent isolated top-side economy or grubs from being treated as generic kill-margin resistance.

Mandatory **RLD — Role-Leverage Decomposition** now asks where meaningful economy is concentrated and whether that location actually converts into the relevant grouped-fight / kill-margin-suppression mechanism.

- mid/ADC carry-centered economy can have higher immediate grouped-fight leverage when paired with protected DPS, objective control and cleaner access;
- top-side economy is not intrinsically low-value, but it must create an independent suppressive route such as side-lane inevitability, reliable flank/access, durable frontline control or another real KMS mechanism;
- grubs are structure/tempo assets and are never automatic KMS evidence;
- if favorite carry leverage + grouped control is materially stronger while the underdog's resistance is mainly isolated top/grubs, `KMS = PASS` is forbidden;
- `RLD = UNRESOLVED` forbids fallback `STABLE`.

The same incident review also found that the historical Over 33 TAKE was not canonical-eligible: low kills and low tower count were used as stall evidence without documented `FAILED CONVERSION`. The existing Duration Over gate already covered this, so no new Duration rule was required.

Reference:
`models/lol/reviews/DNS_BRO_G1_UNDERDOG_KILLS_ROLE_LEVERAGE_AND_DURATION_EXECUTION_REVIEW_2026-08-19.md`

This is an in-place v0.3.58 procedural clarification. Do not create v0.3.59 for it.

### Underdog +kills — UDKC draft-isolation hard guard

After DNS vs BRO Game 2 on 2026-08-19 UTC+7, a second procedural error showed that merely writing draft-lock rules was not enough: live evidence was used to assert KMS/RLD even though a complete draft-only fallback certificate had not been established.

Canonical v0.3.58 enforces a mandatory **UDKC — Underdog +Kills Draft Certificate**:

- UDKC must explicitly resolve DER / FRI / SRI / FER / PDC / PST / ARI / KPA / KMS / RLD / False-Stable Guard / DCR / FF / hard Draft-Collapse Veto;
- omitted, implied, narrative-only, or unresolved fields mean `UNCERTIFIED`;
- UDKC is **draft-only, not timestamp-locked**;
- if the exact locked draft is first received after live play has started, including inside a live screenshot or when a new chat starts mid-map, the analyst may reconstruct UDKC using a strict **Draft-Isolation Pass** before any +kills TAKE;
- Draft Isolation must use champion/team inputs only and must exclude current kills, gold, objectives, structures, odds movement, current handicap size, and current kill margin;
- if one screenshot contains both draft and live state, process **Phase A: draft-only UDKC**, then **Phase B: live reassessment**;
- the completed certificate should be persisted as soon as it is available so later chats can reuse it;
- missing persistence alone is not a map-long veto when the exact draft can be recovered and fully certified; missing/ambiguous draft or incomplete mechanism proof remains fail-closed;
- live evidence may preserve or downgrade a draft-certified STABLE certificate, but can never supply missing draft proof or upgrade a genuinely FRAGILE/ABSENT draft;
- exact kill-margin / NKB arithmetic is downstream hurdle math only and is never certification evidence;
- safe ADC play, peel, waveclear, scaling, small current kill margin, 0-0 towers, grubs, isolated lane gold, or a large displayed +kills buffer cannot substitute for KMS.

Mandatory guard:
`models/lol/procedures/LOL_UNDERDOG_PLUSKILLS_DRAFT_LOCK_GUARD_2026-08-19.md`

References:
- `models/lol/reviews/DNS_BRO_G2_UNDERDOG_PLUSKILLS_DRAFT_LOCK_EXECUTION_REVIEW_2026-08-19.md`
- `models/lol/reviews/UDKC_DRAFT_ISOLATION_AMENDMENT_2026-08-20.md`

This is an in-place v0.3.58 governance/enforcement amendment. Do not create v0.3.59 for it.

### Draft reading — Draft Interaction Matrix (DIM)

After BLG vs LGD Game 3 on 2026-08-20 UTC+7, the draft process was amended to prevent generic champion utility from being credited as if it directly answered the opponent's actual kill mechanism.

Before any model-certified draft edge or draft-derived fallback classification, complete the mandatory **DIM — Draft Interaction Matrix**:

- exact role assignments first;
- primary and secondary kill mechanisms for both teams;
- **TAM — Threat-Answer Matching**: each claimed defensive/reset tool must be mapped to the opponent mechanism it actually answers;
- **OSG — Objective-Setup Geometry**: range, choke control, vision-entry safety, first move, globals, flank/access and objective-turn geometry;
- **DAU — Damage Access & Uptime**: realistic target access and protected damage continuation, not theoretical DPS;
- **SLI — Side-Lane Independence**: split/side routes count only if they survive matchup, globals, catch, waveclear, objective timing and four-man-survival tests;
- **FNF — Frontline Necessity Fit**: lack of a traditional tank is not a generic weakness when a composition wins pre-contact space and does not require sustained front-to-back;
- **CAS — Collapse Asymmetry**: after one ordinary favorite advantage, can the underdog actually break repeated kill-margin expansion?
- **ETS — Execution & Team-Strength modifier** only after interaction geometry is established;
- mandatory **AFP — Adversarial Favorite Pass** before finalizing the draft edge.

For underdog +kills, DIM is a hard prerequisite to UDKC. `TAM = FAIL/UNRESOLVED` or `CAS = FAIL/UNRESOLVED` forbids `KMS = PASS` and therefore forbids UDKC `STABLE`.

Draft Edge and Underdog +Kills Stability must be output separately. A playable draft can still be a bad +kills draft.

Mandatory procedure:
`models/lol/procedures/LOL_DRAFT_INTERACTION_MATRIX_2026-08-20.md`

Reference review:
`models/lol/reviews/BLG_LGD_G3_DRAFT_INTERACTION_REVIEW_2026-08-20.md`

This is an in-place v0.3.58 analytical/procedural amendment. Under an already-frozen Session Authority Lock, it activates only when included in the applicable authority commit; otherwise it is pending for the next slate unless the user explicitly authorizes an immediate relock.

### Live Moneyline — Draft Prior Degradation & Live Regime Override (LRO)

After NS vs T1A Game 1 on 2026-08-21 UTC+7, the Live ML process was amended to prevent a CLEAR/STRONG post-draft read from becoming a hidden permanent veto after repeated coherent live evidence shows that the original mechanism is no longer functioning at the current role/economy state.

Mandatory rules:

- draft remains a prior for Live ML, not a permanent veto;
- classify `DPS — Draft Prior State` as `INTACT / DEGRADED / BROKEN`;
- the neutral-setup fight stress test uses current live items, levels, role-weighted economy and objective schedule; `neutral` means positioning/entry, not equalized economy or a reset to post-draft;
- standard Live ML remains two-snapshot eligible when aligned with a CLEAR/STRONG draft prior or when the draft edge was only SLIGHT/EVEN/UNCLEAR;
- an ML TAKE **against** a CLEAR/STRONG draft prior requires mandatory `LRO = PASS`;
- that contrary-draft LRO path requires three usable snapshots, at least two meaningful contact/objective cycles, regime persistence, multi-role leverage, `DPS = BROKEN`, `CFC_CURRENT = PASS`, next-cycle stress PASS and `DRP — Draft Recovery Path = PASS`;
- one fight, one dragon, one gold number, market movement, team reputation or the eventual result cannot satisfy LRO by itself;
- once `DPS=BROKEN` and `LRO=PASS`, the original draft edge may not remain an unwritten Live ML veto;
- LRO applies to Moneyline only and cannot upgrade UDKC, create missing draft proof, or bypass another market family's gates.

Mandatory procedure:
`models/lol/procedures/LOL_LIVE_ML_DRAFT_PRIOR_DEGRADATION_AND_REGIME_OVERRIDE_2026-08-21.md`

Reference review:
`models/lol/reviews/NS_T1A_G1_LIVE_ML_DRAFT_PRIOR_ANCHORING_REVIEW_2026-08-21.md`

This is an in-place v0.3.58 analytical/procedural amendment. It may activate mid-slate only under an explicit user-authorized relock/new epoch.

## Active operational governance

- Official betting remains paused; shadow only.
- Default shadow stake: **0.25u**; actual exposure: **0u**.
- Minimum odds: **1.60**.
- Every new chat/session must complete `LOL_SESSION_BOOTSTRAP.md`; incomplete bootstrap is fail-closed.
- Verdict first; no connector/logging work before the visible live verdict.
- **Immediately after every valid visible live verdict, Airtable map/snapshot logging is mandatory and the expected record must be verified to exist.**
- `PASS` / `HOLD` still require a snapshot log but never create a position; a qualified executable `TAKE` requires snapshot + exact shadow-position logging after the verdict, subject to the one-TAKE-per-family ledger check.
- If a map/snapshot/position write is discovered missing, backfill only from the original synchronized evidence and original visible verdict; never invent or upgrade a `PASS`/`HOLD` into a position. Fight-mid-verdict discarded decisions remain unlogged/void.
- Airtable logging failure is a data-integrity issue only: it must not delay the visible verdict, change analytical gates, or create an extra confirmation requirement.
- Never claim `logged` or `settled` unless the actual Airtable write succeeded and the expected record was verified.
- Compact output still requires full underlying analysis.
- Pregame/immediate post-draft ML/KH/TK TAKEs remain disabled.
- Live ML/KH/TK retain the two-snapshot eligibility gate; Live ML against a CLEAR/STRONG draft prior additionally requires the LRO three-snapshot override certificate.
- Same-map multiple TAKEs may occur across different market families, maximum one TAKE per family: ML / Kill Handicap / Total Kills / Duration.
- Greyed/stale markets are non-executable.
- Position-blind reassessment remains mandatory.
- Exact signed kill-margin arithmetic remains mandatory.
- Draft Interaction Matrix is mandatory before any model-certified draft edge/draft-derived fallback classification when the exact draft is available.
- Draft-locked underdog +kills fallback certification remains fail-closed, including DIM, KPA/KMS separation, mandatory RLD, and mandatory complete draft-only UDKC.
- Missing persisted UDKC is not itself a veto when the exact locked draft can be recovered; run Draft Isolation before using live state for the market. Missing/ambiguous draft or incomplete UDKC remains HOLD/PASS.
- Live evidence cannot create draft proof and ordinary live evidence cannot re-upgrade a genuinely FRAGILE/ABSENT or already downgraded fallback.
- Live ML must assess Draft Prior State and use current-state CFC; a passing LRO can override the weight of a broken draft prior for ML only.
- Total Kills Under is never TAKE-eligible unless `FRP = PASS` is actually established; passive quiet alone is insufficient.
- No rescue, martingale, chasing, or stake escalation.
- The FRP/FCR/CFC/LRO/SMR/UDKC/DIM gates are mechanism/execution checks, **not** a blanket increase in conservatism. If all written gates pass, default posture remains TAKE.

Mandatory draft interaction procedure:
`models/lol/procedures/LOL_DRAFT_INTERACTION_MATRIX_2026-08-20.md`

Mandatory Live ML regime procedure:
`models/lol/procedures/LOL_LIVE_ML_DRAFT_PRIOR_DEGRADATION_AND_REGIME_OVERRIDE_2026-08-21.md`

Mandatory underdog +kills guard:
`models/lol/procedures/LOL_UNDERDOG_PLUSKILLS_DRAFT_LOCK_GUARD_2026-08-19.md`

Mandatory logging procedure:
`models/lol/procedures/LOL_AIRTABLE_POST_VERDICT_LOGGING_INTEGRITY_2026-08-16.md`

Mandatory session bootstrap:
`models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`

## Retired newer analytical versions

Do **not** apply v0.3.59 or v0.3.60 as model layers merely because their version numbers are higher.

Later-version-only concepts remain inactive unless they have been explicitly incorporated into the amended v0.3.58 file or the user separately re-authorizes them. FRP/FCR/CFC/SMR remain active through canonical v0.3.58 rules; LRO is active through the explicit v0.3.58 Live ML procedure when included in the Session Authority Lock.

Historical positions and P/L remain unchanged and keep their original model labels.

## Required load order

1. `models/lol/CURRENT_MODEL.md`
2. `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`
3. `models/lol/procedures/LOL_V0.3.58_CANONICAL_RESET_2026-08-16.md`
4. `models/lol/rules/MODEL_RULES_LOL_V0.3.58.md`
5. v0.3.57 through v0.3.26 rule deltas
6. mandatory fallback-floor certification procedure, including active KPA/KMS + RLD amendments
7. `models/lol/procedures/LOL_DRAFT_INTERACTION_MATRIX_2026-08-20.md`
8. `models/lol/procedures/LOL_UNDERDOG_PLUSKILLS_DRAFT_LOCK_GUARD_2026-08-19.md`
9. `models/lol/procedures/LOL_LIVE_ML_DRAFT_PRIOR_DEGRADATION_AND_REGIME_OVERRIDE_2026-08-21.md`
10. mandatory live verdict checklist
11. `models/lol/procedures/LOL_AIRTABLE_POST_VERDICT_LOGGING_INTEGRITY_2026-08-16.md`
12. retained pre-v0.3.59 reviews/procedures relevant to v0.3.58 plus the explicit v0.3.58 amendment reviews above, the 2026-08-18 session-bootstrap/FRP execution review, the 2026-08-19 DNS-BRO G2 draft-lock execution review, the 2026-08-20 UDKC Draft-Isolation amendment, `models/lol/reviews/BLG_LGD_G3_DRAFT_INTERACTION_REVIEW_2026-08-20.md`, and `models/lol/reviews/NS_T1A_G1_LIVE_ML_DRAFT_PRIOR_ANCHORING_REVIEW_2026-08-21.md`
13. item-verification suspension
14. v0.3.25 consolidated rules / probation / calibration handbook
15. live fast path and main betting procedure
16. connected-stack procedure and addenda
17. scoreboard protocol
18. shared stake policy
19. latest live handoff last, applying this CURRENT_MODEL authority where conflicts exist

**Do not load v0.3.59 or v0.3.60 rule files in the active stack.**

## Recording

- New positions are recorded as **LoL v0.3.58**.
- Every valid live verdict must be followed by an Airtable snapshot write and verification; `PASS` / `HOLD` produce no position record, while `TAKE` produces the exact shadow position after the verdict when executable.
- Missing logs must be repaired faithfully from original evidence without creating retrospective decisions.
- A visibly issued procedural-error TAKE may be backfilled faithfully but must be audit-labeled with the correct canonical verdict; do not rewrite history by pretending it was a PASS.
- Do not append `temporary override` to new records.
- Prior v0.3.59/v0.3.60 positions remain labeled historically as they were.
- Do not create or auto-promote a newer model from an individual outcome unless the user explicitly requests another model change.
