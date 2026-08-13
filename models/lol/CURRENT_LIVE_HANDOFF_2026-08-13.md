# CURRENT LIVE HANDOFF — 2026-08-13

## Active model

**LoL v0.3.57 — FROZEN FOR SHADOW AUDIT**

GitHub is model/rules authority. Airtable is canonical map/position ledger.

Official betting remains **paused**. Shadow TAKEs remain active.

### Active audit-freeze governance

Procedure: `models/lol/procedures/LOL_SHADOW_AUDIT_FREEZE_2026-08-13.md`

- Continue issuing TAKE / PASS / HOLD normally under frozen v0.3.57.
- Qualified executable shadow TAKEs remain auto-recorded at 0.25u simulated stake; actual exposure remains 0u.
- **Do not patch, version-bump, add exceptions to, or modify v0.3.57 because of individual map outcomes.**
- Settle and analyze every shadow pick normally.
- Reviews during the freeze are observational only; they do not alter the active model.
- Do not invert the model or skip qualified TAKEs because recent results were poor.
- The freeze ends only when the user explicitly authorizes a batch audit/model revision or explicitly ends the freeze.

## Core operating state

- Default shadow stake: 0.25u
- Actual exposure: 0u
- Minimum odds: 1.60
- Pregame/immediate post-draft ML/KH/TK TAKEs: disabled
- Live ML/KH/TK: two synchronized live snapshots plus all retained gates
- Shadow TAKEs: auto-record after visible verdict when executable and qualified; no confirmation required
- Duration restrictions unchanged

## Current open shadow positions

- `LPL-2026-08-13-NIP-WBG-G3-P01` — WBG +8.5 kills @1.951, 0.25u shadow, actual 0u; result pending in canonical ledger. Entry thesis was later judged process-invalid under v0.3.57; do not delete or retroactively regrade it.
- `LCK-2026-08-13-KRX-BFX-G3-P01` — KRX +7.5 kills @2.047, 0.25u shadow, actual 0u; result pending in canonical ledger. User has already flagged the selection as another bad call; analyze after settlement but **do not patch the model during the freeze**.

## Mandatory live output behavior

For every active-map screenshot, the first visible line must be the verdict:

- `TAKE — [selection] @[odds] — shadow 0.25u; actual 0u.`
- `PASS — [selection/market] @[odds] — 0u.`
- `HOLD — [selection/market] @[odds] — 0u.`

Do not delay the visible verdict for Airtable/GitHub/tool work. Logging occurs after the verdict.

## v0.3.57 Fallback Floor Certification — mandatory

Rules:
`models/lol/rules/MODEL_RULES_LOL_V0.3.57.md`

Procedure:
`models/lol/procedures/LOL_FALLBACK_FLOOR_CERTIFICATION_2026-08-13.md`

Reference review:
`models/lol/reviews/NIP_WBG_G3_FALLBACK_FLOOR_MISCLASSIFICATION_REVIEW_2026-08-13.md`

### Core correction

Do **not** infer fallback resilience from engage redundancy.

Before every underdog +kills decision, separately classify:

- DER;
- FRI — Forcing Route Independence;
- SRI — Survival Route Independence;
- FER — Failed-Engage Reset;
- PDC — Protected-DPS Continuation;
- PST — Pressured Space;
- ARI — Alternative Route Independence;
- False-Stable Guard ACTIVE/INACTIVE;
- DCR;
- FF.

`FF = STABLE` requires PASS on FER + PDC + PST + ARI and False-Stable Guard INACTIVE.

Any FAIL or UNRESOLVED means STABLE is forbidden for underdog +kills.

### False-Stable Guard

Activate when the alleged fallback is materially another version of the same forward-commit plan, when peel competes with initiation, when carry protection disappears during engage, when behind-state objective entry repeats the same all-in dependency, or when opponent range/pick/disengage/re-engage can punish failed contact without a demonstrated reset route.

If active, FF = FRAGILE or ABSENT.

### Conservative DCR tie-break

For underdog +kills, if DCR is materially between MEDIUM and HIGH, use HIGH when failed contact can expose multiple members and the opponent has at least two repeatable punish/continuation routes.

### Fail closed

If certification is incomplete or ambiguous: **PASS/HOLD**.

Ordinary live events cannot upgrade FRAGILE/ABSENT/UNCERTIFIED to STABLE. Kill parity, return kills, temporary role-gold gains, objective parity, bigger cushions and two-snapshot eligibility do not create an exception.

Only a genuine draft-input correction may reopen the certification.

## v0.3.56 hard draft-collapse veto remains active

After v0.3.57 certification, if the underdog is HIGH DCR + FRAGILE/ABSENT FF and the opponent has materially easier repeat forcing/continuation with scheduled objective/base pressure, then:

**UNDERDOG +KILLS IS TAKE-INELIGIBLE FOR THE ENTIRE MAP.**

No live exception. If veto active, stop the handicap analysis. Favorite -kills still must qualify independently.

## Triggering correction — NIP vs WBG G3

WBG:
- Gnar
- Lee Sin
- Annie
- Mel
- Rell

NIP:
- Tristana
- Xin Zhao
- Twisted Fate
- Ashe
- Seraphine

At 20:12:

- NIP led 4-3 kills;
- NIP +2.7k gold;
- NIP led towers 2-1;
- dragons 1-1;
- WBG +8.5 kills @1.951.

The v0.3.56 entry incorrectly called WBG's fallback STABLE because it had multiple engage/peel branches.

Correct v0.3.57 classification:

- WBG FRI meaningful;
- WBG SRI insufficient;
- critical fallback certification not all PASS;
- False-Stable Guard ACTIVE;
- DCR HIGH for handicap eligibility;
- FF FRAGILE;
- hard veto ACTIVE.

Correct verdict at that entry: `PASS — WBG +8.5 kills @1.951 — 0u.`

## Recent settled corrections

### KT.C vs NS.EA G1

NS +8.5 @1.943 lost. Draft execution burden was underweighted.

### NIP vs WBG G1

WBG +8.5 @1.961 lost. v0.3.56 introduced the HIGH-DCR + weak-FF hard veto.

### NIP vs WBG G2

Over 33:00 @1.857 lost when WBG won 16-6 at 30:46. Settled shadow validation became 6-8, -0.64850u.

## Immediate next action

Continue the current live map from fresh synchronized evidence under frozen v0.3.57. Shadow TAKEs remain active and must be logged if qualified. **Do not patch the model from the next result; accumulate audit evidence instead.**
