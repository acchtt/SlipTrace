# DNS Challengers vs NS Challengers Game 3 — Session Bootstrap / FRP Execution Review

**Date:** 2026-08-18 UTC+7  
**Canonical model:** LoL v0.3.58  
**Status:** PROCEDURE / EXECUTION ERROR REVIEW

## Incident

During LCK CL DNS Challengers vs NS Challengers Game 3, the session drifted away from the canonical model hierarchy.

The assistant incorrectly operated as if LoL v0.3.59 remained active, despite `models/lol/CURRENT_MODEL.md` explicitly declaring LoL v0.3.58 canonical and v0.3.59/v0.3.60 retired.

At approximately 13:40, with NS leading 4-0 kills, about +3.0k gold, 1-0 dragons and 0-0 towers, the visible verdict was:

`TAKE — UNDER 26.5 kills @1.839 — 0.25u shadow.`

The game later reached at least 14-14 kills, so the Under was mathematically lost.

## Correct canonical-model verdict

**PASS / HOLD — Under 26.5.**

The loss is classified as an **execution/procedure error**, not a clean model-certified analytical miss.

## Why the TAKE was invalid

Canonical v0.3.58 requires **FRP — Forward Regime Persistence** for every Total Kills Under.

Only `FRP = PASS` is TAKE-eligible.

The 13:40 reasoning relied too heavily on elapsed low kill pace and a possible Structure Substitution path. It did not positively establish that the next compulsory-contact cycle would remain kill-suppressive.

At that state:

- NS had Gnar / Wukong / Aurora / Ezreal / Seraphine;
- DNS had Rumble / Trundle / Mel / Caitlyn / Bard;
- multiple future dragon / grouped objective / tower-defense cycles remained;
- NS had strong first-contact, re-engage and layered fight tools;
- the observed quiet history was largely passive quiet rather than demonstrated suppression of compulsory contact;
- no independent repeatable future-suppression mechanism was positively certified.

Therefore FRP should have been `FAIL` or `UNCERTAIN`, forcing `PASS/HOLD`.

## Root causes

1. **Authority inversion:** stale conversation/project context outranked GitHub `CURRENT_MODEL.md`.
2. **Version blending:** retired v0.3.59 vocabulary/concepts were treated as active.
3. **Market-gate shortcut:** FRP was not explicitly resolved before a TK Under TAKE.
4. **Logging truthfulness gap:** prior turns sometimes said `logged` after tool discovery rather than after an actual Airtable write plus verification.

## Corrective controls

A mandatory session bootstrap is added at:

`models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`

It requires:

- `CURRENT_MODEL.md` first in every new chat;
- GitHub authority over memory/project context/handoff prompts;
- fail-closed `MODEL NOT LOADED — HOLD` if live evidence arrives before bootstrap;
- explicit market-family hard gates;
- version-vocabulary tripwire;
- actual Airtable write + verification before claiming `logged`;
- latest handoff loaded last;
- no retrospective upgrade of PASS/HOLD decisions.

## Audit treatment

The visible Under 26.5 TAKE should remain in the shadow ledger as the position that was actually issued, because canonical logging integrity requires faithful backfill of missing writes from the original synchronized evidence and visible verdict.

However, its audit annotation must state:

`EXECUTION / PROCEDURE ERROR — correct canonical v0.3.58 verdict was PASS/HOLD because FRP was not PASS.`

This incident does **not** authorize a new model version. The correction is governance/execution control around canonical v0.3.58.
