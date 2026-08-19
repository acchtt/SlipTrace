# DNS vs BRO Game 2 — Underdog +Kills Draft-Lock Execution Review

**Date:** 2026-08-19 UTC+7  
**Model:** canonical LoL v0.3.58  
**Status:** PROCEDURAL ERROR CONFIRMED; no model-version bump

## Incident

Draft:

- BRO blue: Yorick / Pantheon / Syndra / Caitlyn / Karma
- DNS red: Jayce / Skarner / Galio / Ezreal / Seraphine

Visible live TAKE:

- 5:48 — DNS +7.5 kills @2.072, 0.25u shadow / 0u actual.
- State: BRO 2-1 DNS, BRO +111g, 0-0 towers, 0-0 dragons, 0-0 barons.
- User later reported the position lost.

The result is not needed to establish the procedural failure.

## Finding

The TAKE was not canonical-eligible.

The assistant had not completed and persisted the mandatory draft-locked fallback certification before live play. At 5:48 it then used live evidence to assert that KMS/RLD passed.

That violates the existing fallback-floor lock rule:

- missing or unresolved certification fields require HOLD/PASS;
- ordinary live evidence cannot upgrade UNCERTIFIED/FRAGILE/ABSENT to STABLE;
- safe marksman play, peel, waveclear, engage/counter-engage and theoretical return-kill tools cannot by themselves prove Kill-Margin Suppression.

Correct canonical verdict at 5:48:

**HOLD/PASS — DNS +7.5 kills @2.072 — 0u.**

## What went wrong

The reasoning over-weighted:

- the small current BRO kill margin (+1);
- the fact BRO needed +7 additional net kills to beat DNS +7.5;
- DNS's Skarner/Galio/Seraphine defensive shell;
- Ezreal's safety and ranged continuation;
- the small live gold lead.

Those facts can affect live preservation or pricing **after** a valid STABLE draft certificate exists. They cannot create that certificate.

The reasoning also under-tested BRO's independent repeatable routes:

- Caitlyn/Karma range and siege;
- Syndra pick/zone control;
- Pantheon first-contact/global acceleration;
- Yorick side-lane/structure pressure that can force defensive entries and map compression.

A valid KMS PASS required a concrete explanation for how DNS would suppress repeated BRO **net kill-margin expansion** across those routes. That proof was never completed.

## Permanent execution fix

A new mandatory procedure is added:

`models/lol/procedures/LOL_UNDERDOG_PLUSKILLS_DRAFT_LOCK_GUARD_2026-08-19.md`

It introduces UDKC — Underdog +Kills Draft Certificate.

Hard requirements:

1. UDKC must be complete after draft lock and before any live state is used for underdog +kills analysis.
2. Every mandatory fallback field must be resolved; omitted/UNRESOLVED fields fail closed.
3. UDKC must be persisted in the map audit trail or handoff so a new chat can verify it.
4. Missing persisted UDKC in a new/mid-map chat => underdog +kills HOLD/PASS for that map.
5. Live evidence can preserve or downgrade a STABLE certificate but can never create or upgrade one.
6. Exact net-kill burden is downstream arithmetic, never certification evidence.
7. A same-series prior invalidation triggers SMR: the next map requires a fresh complete UDKC before live.

## Model decision

**Keep LoL v0.3.58.**

This was an enforcement failure of rules that already existed. The fix is a hard governance/execution guard designed to make the failure mechanically difficult to repeat, especially across new chats or context compression.

## Ledger treatment

The historical position remains recorded as the visibly issued shadow position. Its result/P&L should remain historically accurate, while Thesis State is audit-labeled `Invalidated` and Entry Evidence states that the correct canonical verdict was HOLD/PASS.
