# Dota 2 Session Bootstrap — Mandatory New-Chat Guardrail

**Status:** ACTIVE GOVERNANCE  
**Authority:** `models/dota2/CURRENT_MODEL.md`

## Purpose

Prevent authority drift, accidental LoL-rule carryover, stale patch assumptions, skipped Dota-specific gates, false logging claims, and live-decision drift after a new chat or context compression.

## 1. Mandatory bootstrap

At the start of every Dota 2 project chat/session:

1. Fetch `models/dota2/CURRENT_MODEL.md` first.
2. Immediately load this file.
3. Fetch `models/dota2/session/CURRENT_SESSION_LOCK.md`.
4. If the lock is ACTIVE, re-fetch `CURRENT_MODEL.md` at the lock's `authority_commit` and load the remaining analytical stack from that same commit.
5. Follow the exact load order in the effective `CURRENT_MODEL.md`.
6. Load the latest applicable handoff last.
7. Treat handoffs as state transfer only; authority files win on conflict.
8. Do not use LoL rules, abbreviations, thresholds, or prior conclusions unless the Dota 2 authority explicitly imports them.

If an ACTIVE lock cannot be resolved to one coherent authority commit, model-certified analysis is blocked with:

`MODEL LOCK MISMATCH — HOLD`

## 2. Live-evidence fail closed

If live evidence arrives before bootstrap is complete, output first:

`MODEL NOT LOADED — HOLD`

No GitHub, Airtable, web, or other connector call may precede that visible HOLD. Complete bootstrap immediately afterward and reassess only if the evidence/price is still usable.

## 3. First-slate lock

If no active lock exists, shadow prep may continue, but no TAKE may be issued until an authority commit has been frozen for the slate. Default slate boundary is the UTC+7 calendar day unless the user explicitly defines another boundary.

## 4. Minimum state required for live certification

A synchronized live snapshot should capture as much of the following as the evidence supports:

- map clock;
- Radiant/Dire orientation;
- kills;
- total net-worth lead and, when decision-critical, core-by-core net-worth distribution;
- tower and barracks state;
- Roshan status/cycle and Aegis/major-drop ownership;
- meaningful buyback availability/cooldowns/cost pressure;
- death timers when near a decisive fight or high-ground push;
- high-ground breach/defense state, glyph when material;
- next compulsory objective/contact window;
- live market line and price used for the verdict.

Unknown values must remain unknown. Do not infer hidden buyback, cooldown, item, ward, vision, Roshan-drop, or patch-state facts from narrative convenience.

## 5. Snapshot synchronization

Two screenshots or observations count as two usable snapshots only if each is internally coherent and the state progression is temporally plausible. A stale market quote combined with a newer scoreboard is not one synchronized snapshot.

If a material fight, Roshan event, barracks loss, buyback cascade, or major price move occurs while a verdict is being formed, discard the old candidate and request/use a fresh synchronized state before any TAKE.

## 6. Position-blind reassessment

Every new live assessment is made from the current state as if there were no existing position. Existing exposure may affect whether a duplicate market-family position is allowed, but never the analytical verdict itself.

## 7. Patch and roster context

- Treat patch assumptions as dated evidence, not timeless mechanics.
- Prefer official patch notes for changed mechanics when verification is necessary.
- Prefer saved/user-confirmed current rosters over generic web roster pages.
- Do not delay a live verdict with duplicate roster/odds lookup when the user already supplied readable current evidence.

## 8. TAKE preconditions

Before any TAKE, all of the following must be true:

- bootstrap complete;
- active authority lock valid;
- required synchronized snapshot count satisfied;
- market-family hard gates in the active rules explicitly resolved;
- exact line/price is still executable;
- no same-map duplicate TAKE already exists in that market family;
- shadow stake and actual exposure policy known;
- no unresolved decision-critical fact is being silently guessed.

Missing required proof => `HOLD/PASS`, not a narrative exception.