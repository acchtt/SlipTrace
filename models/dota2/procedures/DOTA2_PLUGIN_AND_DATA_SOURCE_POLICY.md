# Dota 2 Plugin / Connector / Data-Source Policy

**Status:** ACTIVE GOVERNANCE  
**Authority:** `models/dota2/CURRENT_MODEL.md`

## Purpose

Use connected tools deliberately without letting external data sources override model authority or delay time-sensitive live decisions.

## 1. GitHub — authority layer

Use the GitHub connector for:

- `CURRENT_MODEL.md` bootstrap;
- active rules and procedures;
- session authority lock;
- patch/context notes saved into the project;
- handoffs and postgame reviews;
- controlled model amendments with auditable commits.

GitHub is authoritative for analytical rules. Never infer the active version from chat memory or Airtable.

On active live evidence, the Dota verdict-first rule still applies. If bootstrap was not completed before live evidence arrived, visibly output `MODEL NOT LOADED — HOLD` before any connector call.

## 2. Airtable — canonical mutable live ledger

Canonical base:

- **SlipTrace Dota 2 Live Tracker**
- Base ID: `appoyQ7VAvJcUVJo2`

Tables:

- `Maps`
- `Snapshots`
- `Positions`
- `Rosters`

Use Airtable for mutable operational state only. Airtable does not define analytical rules or silently override GitHub authority.

For active maps:

1. verdict first;
2. write map/snapshot immediately after;
3. create Position only for an executable TAKE;
4. read back and verify exact expected fields before claiming success.

## 3. Web research — context and verification, not authority

Use web research only when it materially improves the decision or fills missing context, for example:

- official Dota 2 patch notes / changed mechanics;
- current tournament schedule or format;
- current roster/substitution verification when saved/user evidence is missing or contradictory;
- recent team context when required by the active rules;
- public match statistics for calibration/review.

Priority:

1. official Valve/Dota 2 or tournament-organizer source where available;
2. official team/player source for roster announcements;
3. reputable structured Dota data providers;
4. reputable secondary esports sources;
5. generic search snippets last.

Do not use web lookup to duplicate-confirm readable current sportsbook odds or a user-confirmed lineup unless there is a concrete conflict.

## 4. Structured Dota data providers

No dedicated Dota/OpenDota/STRATZ installable ChatGPT plugin was available when this policy was initialized. Therefore, third-party Dota data should enter through web/API-accessible research or user-provided evidence unless a future connector is installed.

When using public providers such as OpenDota, STRATZ, Liquipedia, tournament sites, or similar sources:

- treat them as evidence sources, not model authority;
- record source and retrieval date when saving durable context;
- do not assume real-time freshness without checking timestamps;
- do not combine unsynchronized live feeds into one synthetic snapshot;
- prefer official match pages for final results when provider states conflict.

## 5. Google Calendar — optional schedule layer

If the user wants a slate calendar, the Calendar connector may be used to create or inspect tournament/match reminders. Calendar data is scheduling context only and never a substitute for match-state evidence.

## 6. Automations — optional monitoring layer

Native scheduled/conditional tasks may be used for non-urgent workflow support such as:

- daily patch-note checks;
- roster-change checks;
- tournament slate reminders;
- periodic calibration/review reminders.

Do not use hourly automation polling as a substitute for synchronized live betting evidence. Live decisions remain user-triggered from current state/price unless a future approved real-time feed workflow is explicitly added.

## 7. Tool-order discipline on live maps

When already bootstrapped and a synchronized live state is supplied:

1. internally run the active Dota rules;
2. output verdict;
3. log/verify Airtable;
4. perform nonessential web/context work only afterward.

If a decision-critical fact is missing, HOLD/PASS. Do not delay a qualified live verdict for optional research, and do not manufacture missing data from external stale feeds.