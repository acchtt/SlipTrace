# Current Live Handoff — 2026-08-19 UTC+7

**Authority:** load this handoff last, but `models/lol/CURRENT_MODEL.md` remains superior if anything conflicts.

## Canonical model

- Active model: LoL v0.3.58.
- v0.3.59 / v0.3.60 remain retired.
- Mandatory new-chat bootstrap applies.
- New mandatory underdog +kills guard is active:
  `models/lol/procedures/LOL_UNDERDOG_PLUSKILLS_DRAFT_LOCK_GUARD_2026-08-19.md`.

## Permanent underdog +kills execution rule

A complete pre-live **UDKC — Underdog +Kills Draft Certificate** must exist before any live state is used to evaluate underdog +kills.

UDKC must explicitly resolve:
DER / FRI / SRI / FER / PDC / PST / ARI / KPA / KMS / RLD / False-Stable Guard / DCR / FF / hard Draft-Collapse Veto.

Hard enforcement:

- missing / implied / unresolved field => HOLD/PASS;
- no persisted pre-live UDKC in a new mid-map chat => underdog +kills HOLD/PASS for that map;
- live evidence may preserve or downgrade STABLE, never create or upgrade it;
- exact NKB / additional-net-kill hurdle is arithmetic only, never certification evidence;
- safe ADC, peel, waveclear, scaling, 0-0 towers, grubs, small current margin, isolated lane gold, or a large displayed +kills cushion cannot substitute for KMS.

Reference:
`models/lol/reviews/DNS_BRO_G2_UNDERDOG_PLUSKILLS_DRAFT_LOCK_EXECUTION_REVIEW_2026-08-19.md`

## LCK DNS vs BRO — series state

### Game 1

BRO won 33:14, kills 17-7.

Historical visible positions:

- DNS +8.5 kills @2.014 — Loss -0.25u shadow; audit-invalidated, correct canonical verdict HOLD/PASS.
- Over 33 minutes @1.666 — Win +0.1665u shadow; audit-invalidated, correct canonical verdict HOLD/PASS.

Primary lessons already written into canonical v0.3.58:

- do not treat isolated top/grub advantage as generic kill-margin resistance;
- use RLD;
- Duration Over requires actual FAILED CONVERSION / positive clock-consuming mechanisms, not low kills or low tower count alone.

### Game 2

Draft:

- BRO blue: Yorick / Pantheon / Syndra / Caitlyn / Karma
- DNS red: Jayce / Skarner / Galio / Ezreal / Seraphine

Post-draft baseline odds seen:

- ML DNS 2.132 / BRO 1.663
- Duration 32: Over 1.779 / Under 1.968
- Total Kills 24.5: Over 2.178 / Under 1.636
- active KH DNS +3.5 2.045 / BRO -3.5 1.720

Live snapshots:

- 4:19: BRO 1-0 DNS, BRO +280g, 0-0 towers/dragons/barons; DNS +7.5 @2.023. HOLD as snapshot 1.
- 5:48: BRO 2-1 DNS, BRO +111g, 0-0 towers/dragons/barons; DNS +7.5 @2.072.

A visible TAKE was incorrectly issued at 5:48:

- DNS +7.5 kills @2.072, 0.25u shadow / 0u actual.

User later reported the position lost.

Audit finding:

- the TAKE was procedurally invalid because no complete pre-live UDKC had been recorded;
- live evidence was incorrectly used to assert KMS/RLD;
- correct canonical verdict was HOLD/PASS regardless of outcome.

Airtable Position ID:
`LCK-2026-08-19-DNS-BRO-G2-KH-DNS+7.5-0548`

## User-visible preference

Do not include data-status labels/notes in verdict commentary or Airtable notes. Still enforce synchronization from actual game clock, scoreboard state and odds shown.

## Game 3 / next-map instruction

Start position-blind from the new draft.

For any underdog +kills candidate:

1. complete and persist UDKC immediately after draft lock;
2. if UDKC is not complete before live evidence, lock that family to HOLD/PASS for the entire map;
3. same-series SMR is active because Game 2's underdog +kills mechanism was audit-invalidated;
4. never infer STABLE from a large live handicap buffer.

Official betting remains paused; shadow default 0.25u, actual 0u.
