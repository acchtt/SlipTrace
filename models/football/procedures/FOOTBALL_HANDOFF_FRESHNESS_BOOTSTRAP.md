# Football New-Chat / Handoff Freshness Bootstrap

**Status:** MANDATORY ROUTER PRECHECK  
**Scope:** any football stage resumed from a handoff, prior-chat summary, copied response, or stale board artifact

## 1. Core rule

A handoff is a **historical state snapshot**, not current model authority.

Before executing /rank, /xi, /live, /audit, /report, or an equivalent natural-language continuation in a new chat:

1. read `models/football/CURRENT_MODEL.md`;
2. read `models/football/prompts/COMMAND_ALIASES.md`;
3. read the current canonical launcher for the requested stage;
4. for execution-required `/rank`, `/xi`, or `/audit`, read `models/football/procedures/FOOTBALL_RUNTIME_EXECUTION_BOOTSTRAP.md`;
5. only then use the handoff as frozen historical context.

If a handoff names an older model roster or older launcher behavior, the current repository authority wins for **current execution semantics**.

Do not silently continue an old model roster after newer shadow challengers become active. C4 is Step-1-only; its activation changes current `/rank` semantics and adds **read-only frozen C4 snapshot visibility** to `/xi`, but it does not create a fourth Step-2 or `/live` action track.

## 2. Preserve historical fidelity

Freshness does **not** permit retrospective rewriting.

Keep immutable:
- historical C/C2/C3/C4 board states actually frozen at the time;
- historical supported lines;
- historical model availability;
- historical actions/exposures;
- timestamps and evidence epochs.

If a historical board predates C3, do not manufacture a historical C3 rank/line for it. If it predates C4, do not manufacture a historical C4 structured compilation for it.

Instead show:
`SHADOW C3: UNAVAILABLE — BOARD PREDATES C3 / NO PROSPECTIVE C3 FREEZE`

Likewise for a missing historical C2 freeze.

## 3. Current-stage roster

For `/rank`, current output must account for:
- **OFFICIAL C**
- **SHADOW C2**
- **SHADOW C3**
- **SHADOW C4 — STEP 1 ONLY**

For `/xi`, visible output must contain:
- **OFFICIAL C**
- **SHADOW C2**
- **SHADOW C3**
- **SHADOW C4 (STEP1) — NO STEP2 ACTION**

For `/live`, the visible execution roster remains:
- **OFFICIAL C**
- **SHADOW C2**
- **SHADOW C3**

C4 must not be synthesized into a Step-2/live action because it has no execution policy. In `/xi`, only retrieve/display its prospectively frozen Step-1 snapshot.

Never omit C2, C3, or the required C4 XI snapshot line merely because:
- the handoff predates the challenger;
- the handoff only mentions older tracks;
- a frozen challenger line is missing;
- the fixture is an exception;
- the match is already live.

If a track cannot legally issue a comparison, print the exact unavailability/incomplete reason instead of omitting the track.

Examples:

`SHADOW C2: UNAVAILABLE — NO PROSPECTIVE C2 FREEZE`

`SHADOW C3: UNAVAILABLE — BOARD PREDATES C3 / NO PROSPECTIVE C3 FREEZE`

`SHADOW C3: COMPARISON INCOMPLETE — BURDEN-FUNDING STATE NOT INDEPENDENTLY FROZEN`

`SHADOW C4 (STEP1): UNAVAILABLE — NO PROSPECTIVE C4 FREEZE`

## 4. Natural-language continuation

The bootstrap applies even when the user does not type a slash command.

Examples:
- "continue from this handoff"
- "assess these"
- "reassess"
- "what about these live matches"
- a copied prior assistant response followed by new XI/odds/live screenshots

If the requested operation is clearly Step 2 or live, load the current Step-2/live launcher first.

## 5. New-chat stale-authority warning

If the handoff's declared authority differs from current `CURRENT_MODEL.md`, record internally:

`HANDOFF AUTHORITY STALE — CURRENT MODEL/LAUNCHER RELOADED`

Do not treat this as contamination of historical frozen data. It is a router/bootstrap correction.

Runtime availability is also never inherited from a handoff. A previous "Python unavailable", "GitHub unavailable", missing-checkout or engine-not-executed note is historical process context only. Re-probe the current turn before making any availability claim.

## 6. Output invariant

For /xi, every material match block must contain all four visible model lines:

- `OFFICIAL C: ...`
- `SHADOW C2: ...`
- `SHADOW C3: ...`
- `SHADOW C4 (STEP1): ... — NO STEP2 ACTION` or an explicit C4 UNAVAILABLE/COMPARISON INCOMPLETE reason.

For /live, every material match block must contain:
- `OFFICIAL C: ...`
- `SHADOW C2: ...`
- `SHADOW C3: ...`

The shadow lines may be BET/WAIT/PASS, UNAVAILABLE, or COMPARISON INCOMPLETE. C4's XI line is read-only frozen Step-1 context.

They may never be silently absent.

## 7. Handoff generation

Any new handoff must:
- identify Football C as official;
- identify C2 and C3 as Step-2-capable shadow challengers;
- identify C4 as a Step-1-only structured-evidence shadow challenger when C4 is active and state that /xi must display its frozen Step-1 snapshot without creating a C4 Step-2 action;
- state that future chats must reload `CURRENT_MODEL.md` and the current stage launcher before execution;
- state that execution-required stages must re-probe Python/repository availability and may not inherit an old runtime-failure claim;
- distinguish frozen historical state from current execution semantics.

Do not embed launcher text as permanent authority.
