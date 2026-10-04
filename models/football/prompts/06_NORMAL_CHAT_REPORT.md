# 06 — Normal Chat: Football State Report

**Command alias:** `/report`  
**Purpose:** summarize current persisted football state without rerunning predictive stages.

Read first:
- `models/football/CURRENT_MODEL.md`
- `models/football/prompts/COMMAND_ALIASES.md`
- the relevant Airtable contracts when persistence is queried.

## Authority

This is a read/report launcher only.

It may retrieve and summarize:
- current/latest Football C board;
- FOLLOW / RESERVE / STOP queue;
- next scheduled matches;
- current Decision States;
- current Website Picks, including direct C-BET and assumed/reconciled C-WAIT operational exposure;
- current C-WAIT plans and exposure basis;
- current all-model accounting for C/C2/C3/C4, including WATCH/WAIT precedence;
- C2/C3 shadow waits when they exist on the same fixtures;
- C2 shadow state when useful;
- C3 burden-funding shadow state/rank/lane and Board N/5 when useful;
- C4 Step-1 structured shadow state/rank/line and Board N/5 when useful;
- Step-0 coverage/disposition summaries.

It must not:
- run a new AiScore sweep;
- rerank fixtures;
- perform a new Step-1 football assessment;
- perform a new XI/odds decision;
- create an opportunistic live decision;
- alter Airtable/model state merely to make the report cleaner.

## Source priority

For persisted current state use:
1. current conversation evidence when it is newer and explicit;
2. official Football C persisted board / Daily Coverage state;
3. Decision States for material Step-2/live decisions;
4. Website Picks for official published exposure;
5. current authoritative fixture/status verification when the request is about what is upcoming/live/finished now.

Do not present stale stored kickoff/status as current when a schedule/status revalidation is required.

## Default `/report`

When no scope is supplied, return a compact operational report containing:
- active/latest board window;
- FOLLOW matches;
- RESERVE count/list when relevant;
- next upcoming matches in ICT;
- active C-WAIT / official C-BET states;
- C2/C3/C4 prospective board counters when relevant;
- unresolved process faults, if any.

Do not rerun model research.

## Scoped examples

### `/report current board`
Show the latest frozen official Football C board and operational lanes. When a prospective C4 freeze exists, show the compact C-vs-C4 Step-1 delta separately; never merge C4 state into the official queue.

### `/report next matches`
Show upcoming Football C FOLLOW schedule first, then RESERVE if useful. Revalidate current fixture time/status before calling a match upcoming.

### `/report latest decisions`
Show the latest material Football C Decision States and official Website Pick state. Also show the all-model accounting row for C/C2/C3/C4 when available.

For WATCH show `WATCH_ASSUMED O<supported line> @1.65 1u` (shadow equivalent for C2/C3/C4). For WAIT show model-specific target/minimum odds. Keep operational C-WAIT exposure separate from model-accounting precedence.

### `/report coverage`
Show latest Step-0 funnel, including women's top-flight coverage counts/disposition integrity.

### `/report waits`
Show C/C2/C3 WAIT plans with target, minimum odds, accounting basis and current status if known. Default unresolved WAIT accounting is assumed; do not label a WAIT "not reached" unless the user explicitly said so. When a WAIT is not reached and that model had frozen WATCH, show the surviving WATCH accounting bet.

## Refresh modifier

If the user writes `/report ... refresh`, refresh only factual current status needed for reporting, such as fixture time/status or currently persisted rows.

Do not interpret `refresh` as permission to rerun:
- `/sweep`;
- `/rank`;
- `/xi`;
- `/live`.

## Output

Keep reports operational and concise unless the user asks for detail.

Never invent missing state. If a requested report item has no persisted/current evidence, label it unavailable rather than reconstructing a new prediction.
