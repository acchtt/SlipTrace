# LoL Live Chat Transfer Handoff — 2026-08-22 19:47 UTC+7

**Purpose:** state-only transfer for the next chat. This file does not override `CURRENT_MODEL.md`, the session bootstrap, or `CURRENT_SESSION_LOCK.md`.

## New-chat bootstrap requirement

The next chat must bootstrap from GitHub before model-certified analysis:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. fetch `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch `models/lol/session/CURRENT_SESSION_LOCK.md`;
4. use the active lock authority commit for the full analytical/procedural stack;
5. load this handoff last as state only.

If live evidence arrives before bootstrap is complete, visible verdict is exactly `MODEL NOT LOADED — HOLD` before any connector/tool call.

## Active session state

- Active lock at transfer: `LOL-2026-08-22-E4-1920-UTC7`.
- Active model: LoL v0.3.58.
- Frozen authority commit: `7f308824e7e31eaaa56c6d53c115ce6d76651faf`.
- Circuit breaker: CLEAR.
- Mechanical `PRE_TAKE_CERT` interlock is ACTIVE.
- Shadow only: default 0.25u; actual exposure 0u.
- Minimum odds 1.60.
- One TAKE per market family per map.

## Current series — TES vs JDG, LPL 2026 Split 3 BO3

Series state at transfer: **JDG lead 1-0**.

### Saved confirmed Game 1 lineups / roles

TES:
- ZUIAN — Olaf top
- Tian — Nocturne jungle
- Creme — Ahri mid
- JackeyLove — Ezreal bot
- Zhuo — Seraphine support

JDG:
- Xiaoxu — Rumble top
- JunJia — Trundle jungle
- HongQ — Viktor mid
- GALA — Jhin bot
- Vampire — Karma support

These five-player lineups were visible in user-supplied live screenshots. Reuse saved lineup context first; do not perform external roster lookup merely to reconfirm them unless later evidence conflicts or the user asks.

### Game 1 state / result

Map ID: `LPL-2026-08-22-TES-JDG-G1`.

Important source correction: the scoreboard incorrectly displayed `Final` while the game was still live at 11:23 and 15:52. The user explicitly confirmed it was live. Do not treat those labels as the match result.

Usable live snapshots:
- 11:23 — TES 3-3 JDG, towers 0-0, JDG dragons 1-0. Odds included TES ML 1.550 / JDG 2.352.
- 15:52 — TES 3-3 JDG, towers 0-0, JDG dragons 2-0. Odds included TES ML 1.664 / JDG 2.131.

At 15:52 a mechanically certified shadow TAKE was issued:
- JDG ML @2.131
- 0.25u shadow / 0u actual
- PRE_TAKE_CERT PASS
- Moneyline family consumed for Game 1

User later confirmed: **JDG won Game 1**. No exact final kill score or duration was supplied; do not invent them.

Airtable position:
- Position ID `LPL-2026-08-22-TES-JDG-G1-ML-JDG-1552`
- Result: Win
- Thesis State: Settled
- Shadow P/L: +0.28275u
- Actual exposure: 0u

Game 1 map winner is logged as JDG.

### Next expected state

Continue TES vs JDG into **Game 2** under the active E4 match-scope lock unless GitHub lock state has changed by the time the new chat starts.

Game 2 market families are fresh. Pregame/immediate-postdraft ML/KH/TK TAKEs remain disabled; live ML/KH/TK need at least two usable live snapshots. Every TAKE must pass complete PRE_TAKE_CERT before the visible verdict.

## Prior important audit context from this chat

- The mechanical PRE_TAKE_CERT hard interlock was added because a prior GEN +9.5 kill-handicap loss exposed that a TAKE could be emitted with missing mandatory gates. The rule now requires complete pre-entry validation before the word TAKE may be emitted.
- Anti-hindsight accounting is mandatory: a losing prediction cannot later be rewritten as though the model had predicted HOLD. Prediction result and process validity remain separate dimensions.
- Historical DK vs GEN Game 2 DK +10.5 was void/invalidated for a fight during the decision/entry window (state/price synchronization failure).
- Historical DK vs GEN Game 3 GEN +9.5 @1.664 was a losing prediction and audit-invalidated for missing mandatory pre-entry gates; the loss remains in prediction-performance accounting.

These items are already governed by GitHub authority/session-lock procedures; this section is only a transfer reminder.

## Workflow preferences to preserve

- Keep visible live replies brief; run the full procedure internally.
- Verdict first during live analysis, then Airtable logging and exact verification.
- No unnecessary commentary about source delay/staleness; enforce synchronization/coherence internally.
- Do not automatically discard sportsbook evidence because source clocks differ.
- Reuse saved confirmed lineups; no unnecessary web lineup lookup.
- User corrections about live state/fight timing/source labels are material evidence and must be reflected exactly.
- Do not chase an ML after the useful value window has passed merely because later state confirms the thesis.

## Non-LoL detour to ignore

The user supplied two Hull City vs Manchester United soccer screenshots during this chat, then explicitly said: `Jdg won abort last screenshots`.

Those soccer screenshots are **aborted/ignored for this LoL audit**. No soccer result or soccer bet was logged to the LoL Airtable ledger.
