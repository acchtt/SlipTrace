# LoL Session Bootstrap — Mandatory New-Chat Guardrail

**Status:** ACTIVE GOVERNANCE  
**Original effective:** 2026-08-18 UTC+7  
**Rebuilt:** 2026-08-29 UTC+7  
**Authority:** `models/lol/CURRENT_MODEL.md`

## Purpose

Prevent authority drift, stale-version blending, false logging claims, unnecessary source lookup, outcome-driven mutation and execution drift across chats.

This bootstrap is deliberately **version-neutral**. It loads exactly the analytical/procedural stack declared by `CURRENT_MODEL.md`; it does not hard-code legacy v0.x market gates.

---

# 1. Mandatory GitHub bootstrap order

At the start of every LoL project chat/session:

1. Fetch `models/lol/CURRENT_MODEL.md` first from the repository default branch.
2. Immediately load this file: `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`.
3. Immediately fetch `models/lol/session/CURRENT_SESSION_LOCK.md` if it exists.
4. If that lock is `ACTIVE`, read its `authority_commit` and re-fetch `models/lol/CURRENT_MODEL.md` at that exact commit.
5. Treat the locked `CURRENT_MODEL.md` as the effective analytical authority for the live epoch.
6. Load every file in the exact required load order declared by the locked `CURRENT_MODEL.md`, from the same authority commit unless the file is explicitly mutable state such as `CURRENT_SESSION_LOCK.md` or Airtable.
7. Load the latest applicable live handoff last. Handoffs carry state, never analytical authority.
8. Conversation memory, project context, prompts, prior assistant output, historical files and old handoffs never override locked/current GitHub authority.
9. Never load or blend a historical model merely because it has a higher version number or familiar gate name.

## Lock mismatch

If an ACTIVE lock cannot be fetched, its authority commit cannot be matched, or the declared active model conflicts with the loaded stack:

`MODEL LOCK MISMATCH — HOLD`

Do not silently fall back to default-branch rules.

## No active lock

If no valid active lock exists, bootstrap the current authority and establish a fresh lock before the first TAKE-eligible live decision.

Draft preparation and non-betting analysis may occur before the lock exists. No TAKE may be issued without a valid lock.

---

# 2. Authorized rebuild state

When the user has explicitly authorized a clean model rebuild and the replacement analytical stack is not yet fully activated by `CURRENT_MODEL.md` plus a fresh Session Authority Lock, no live TAKE is permitted.

Visible status if live betting evidence arrives during that interval:

`MODEL REBUILD IN PROGRESS — HOLD`

This state takes precedence over trying to blend the old and new models.

---

# 3. Model-lock assertion

Before the first model-certified live betting verdict of a session, verify internally:

- active model exactly matches locked `CURRENT_MODEL.md`;
- active authority commit is known and fetchable;
- all mandatory active files in `CURRENT_MODEL.md` were loaded from that commit;
- retired/historical files are excluded from active analytical authority;
- current market scope is known;
- current circuit-breaker state is known;
- current minimum odds / probability-edge / stake / exposure controls are known;
- current user execution-confirmation requirement is known;
- Airtable remains the canonical historical map/snapshot/position ledger;
- latest applicable handoff was loaded last.

If any decision-critical assertion is unresolved:

`MODEL NOT LOADED — HOLD`

If the active governance file declares a procedural circuit breaker:

`TAKE SUSPENDED — PROCEDURAL CIRCUIT BREAKER`

---

# 4. Saved lineup and match-context priority

For named-team professional match prep:

1. use saved project/Airtable roster or lineup context first;
2. use a current user-supplied official lineup/card or exact five-player confirmation over generic roster websites;
3. external roster lookup is needed only when saved/user evidence is missing, contradictory, ambiguous, or the user explicitly requests verification;
4. a dated lineup is evidence for that date, not a permanent roster lock;
5. before using player/team context materially in a draft prior, resolve decision-critical substitutions or role swaps.

Do not spend live decision time duplicate-confirming an already reliable five.

---

# 5. Odds and screenshot fast path

When the user supplies a readable sportsbook screenshot with the relevant active-market price, treat that displayed price as market authority for that decision window unless:

- the market is unclear;
- the screenshot is stale/greyed;
- synchronization is contradicted;
- the requested market is not shown;
- or the user explicitly requests a cross-book check.

When the user explicitly confirms paired scoreboard/market screenshots represent the same live state, device/header/capture-time differences alone do not invalidate synchronization. Internal state contradictions still fail closed.

Do not use bookmaker price movement as evidence for the game-state probability unless the active model explicitly says otherwise.

---

# 6. Active-market scope comes only from CURRENT_MODEL

Never assume legacy market families remain active.

Before betting analysis, read `CURRENT_MODEL.md` for:

- active betting market(s);
- retired/suspended markets;
- active probability procedure;
- active execution controls.

If a screenshot includes a retired market, do not revive its historical gates or issue a betting verdict for it.

---

# 7. Position-blind and anti-chasing controls

Unless explicitly revoked by current authority:

- reassess each live state position-blind;
- do not defend a prior selection because it is already logged;
- no rescue, martingale, chasing, averaging down or stake escalation;
- actual exposure remains whatever the current lock says, with `0u` as the standing shadow-audit policy unless explicitly changed by the user.

---

# 8. User confirmation before Position creation

If current authority requires user line-existence confirmation:

- an analytical TAKE/TAKE CANDIDATE is not a Position;
- `PENDING` creates no W/L or P/L;
- only explicit confirmation that the exact quoted market/price still exists may create an accepted Position;
- if the line materially moves or a material game-state change occurs, reassess under the active model before acceptance;
- never create a retroactive Position because an unconfirmed candidate later won.

---

# 9. Airtable logging truthfulness

GitHub is analytical/governance authority. Airtable is canonical historical map/snapshot/position state.

- Do not delete or rewrite historical records to improve model performance.
- Preserve the model/version actually used for historical positions.
- A successful analytical verdict does not imply a successful Airtable write.
- Never claim a Position was logged/settled unless the write actually succeeded under the available workflow.
- Historical result and process validity remain separate.

Use the current active model's logging instructions rather than legacy family-specific signatures.

---

# 10. Outcome-driven mutation prohibition

A normal win or loss does not authorize an analytical rule change.

Follow the validation/change protocol declared by the active `CURRENT_MODEL.md`.

If a model change is discussed but not committed, fetched back, activated by `CURRENT_MODEL.md` and frozen by the active/new lock, it is not active authority.

---

# 11. Minimum transfer instruction

For a new chat:

> Continue the League of Legends project from `acchtt/SlipTrace`. Fetch `models/lol/CURRENT_MODEL.md` first, immediately load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`, then fetch `models/lol/session/CURRENT_SESSION_LOCK.md`. If the lock is ACTIVE, use its frozen authority commit and follow the exact load order in locked `CURRENT_MODEL.md`. Load the latest applicable handoff last. GitHub is analytical authority; Airtable is the historical map/snapshot/position ledger. Never blend historical model files into active authority. If the stack cannot be matched, fail closed to the status required by the bootstrap/current governance.
