# Football New-Chat / Handoff Freshness Bootstrap

**Status:** MANDATORY ROUTER PRECHECK  
**Scope:** any football stage resumed from a handoff, prior-chat summary, copied response, or stale board artifact  
**Active roster:** Football C official + Football C2 shadow

## 1. Core rule

A handoff is a **historical state snapshot**, not current model authority.

Before executing /rank, /xi, /live, /audit, /report, or an equivalent natural-language continuation in a new chat:

1. read `models/football/CURRENT_MODEL.md`;
2. read `models/football/procedures/FOOTBALL_C_C2_ACTIVE_PAIR.md`;
3. read `models/football/prompts/COMMAND_ALIASES.md`;
4. read the current canonical launcher for the requested stage;
5. for execution-required /rank, /xi, or /audit, read `models/football/procedures/FOOTBALL_RUNTIME_EXECUTION_BOOTSTRAP.md`;
6. only then use the handoff as frozen historical context.

If a handoff names an older roster or launcher behavior, current repository authority wins for **current execution semantics**.

Record internally when needed:

`HANDOFF AUTHORITY STALE — CURRENT MODEL/LAUNCHER RELOADED`

## 2. Active roster

For new/current execution:

- **OFFICIAL C**
- **SHADOW C2**

C3 and C4 are retired. They must not be executed, required, displayed as current tracks, or reconstructed for a new decision.

"all models" means the active roster: C + C2.

## 3. Preserve historical fidelity

Freshness does **not** permit retrospective rewriting.

Historical C3/C4 records remain immutable when they were genuinely frozen at the time. Preserve:
- historical C/C2/C3/C4 board states actually frozen;
- historical supported lines;
- historical model availability;
- historical actions/exposures/accounting;
- timestamps and evidence epochs.

Do not manufacture a missing historical challenger after kickoff or FT.

Historical visibility is audit context only and never reactivates a retired model.

## 4. Current-stage behavior

For `/rank`:
- produce Football C official board;
- produce Football C2 shadow board;
- reconcile the same ranked eligible universe and frozen common evidence through the active C+C2 board pair.

For `/xi`:
- freeze one common current evidence epoch;
- freeze C and C2 model-owned inputs independently;
- execute the atomic C+C2 pair;
- a C-only completed exception is forbidden.

For `/live`:
- resolve Football C official live/WAIT state;
- resolve C2 shadow live/WAIT state when a prospective C2 state exists;
- C2 never creates official exposure.

For `/audit`:
- current forward metrics use C+C2 only;
- historical C3/C4 rows may be reported only as historical records from their original epochs.

## 5. Natural-language continuation

This bootstrap applies even when the user does not type a slash command, including:
- "continue from this handoff";
- "assess these";
- "reassess";
- "what about these live matches";
- a copied prior response followed by new XI/odds/live screenshots.

Runtime availability is also never inherited from a handoff. Re-probe the current turn before making any availability claim.
