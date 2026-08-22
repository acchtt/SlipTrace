# Current Live Handoff — 2026-08-22 21:00 UTC+7

**State-only handoff. This file does not override CURRENT_MODEL.md or CURRENT_SESSION_LOCK.md.**

## Active session

- Lock ID: `LOL-2026-08-22-E5-2100-UTC7`
- Match scope: `SHFT vs FNC — LEC 2026 Summer Week 5 BO3`
- Model: `LoL v0.3.58`
- Frozen authority commit: `d53a9809df5bead5eb78a283a727a19d9651f474`
- Circuit breaker: `CLEAR`
- Shadow only: `0.25u` default simulated stake, `0u` actual exposure
- Minimum odds: `1.60`
- PRE_TAKE_CERT interlock: ACTIVE
- Same-map policy: maximum one TAKE per market family; ML / KH / TK / Duration are separate families.

## Match schedule / readiness

The first scheduled LEC match on 2026-08-22 is Shifters vs Fnatic, LEC Summer Week 5, BO3. Expected start is 17:00 CEST / 22:00 UTC+7.

No 2026-08-22 SHFT-FNC map, snapshot, or position exists in Airtable at handoff creation, so Game 1 begins fresh.

## Canonical roster prep

Airtable roster records are provisional and must yield to user-confirmed or live-scoreboard evidence.

SHFT provisional:
- Top: Rooster
- Jungle: Sheo
- Mid: nuc
- ADC: Paduck
- Support: Stend
- Subs listed: Boukada (Jungle), Trymbi (Support)

FNC provisional:
- Top: Soboro
- Jungle: Razork
- Mid: Vladi
- ADC: Upset
- Support: Lospa

Do not use roster status as draft proof. Exact Game 1 roles/champions must come from the locked draft/live evidence.

## Execution state

- No Game 1 draft has been supplied yet.
- No Game 1 draft edge has been certified.
- Pregame/immediate-postdraft ML/KH/TK TAKEs remain disabled.
- Live ML/KH/TK require at least two usable synchronized live snapshots.
- Underdog +kills requires complete draft-only DIM + UDKC plus downstream live preservation/UCS/exact margin arithmetic.
- Greyed/stale markets are non-executable.
- Position-blind reassessment is mandatory.
- Verdict first; Airtable write and exact verification only after the visible verdict.

## Prior ledger cleanup

Historical position `LPL-2026-08-13-NIP-WBG-G3-P01` (WBG +8.5 kills @1.951, 0.25u shadow) was user-confirmed Loss and reconciled in Airtable to Result=Loss, Thesis State=Settled, P/L=-0.25u, actual exposure=0u.

## Next evidence

When the user supplies SHFT-FNC Game 1 draft or live screenshots:

1. confirm exact teams/game/roles and sportsbook frame;
2. if immediate postdraft, run draft analysis but ML/KH/TK verdict remains HOLD unless a separate eligible Duration setup exists;
3. initialize Airtable Game 1 map/snapshot only after the visible verdict;
4. after two usable synchronized live snapshots, evaluate all executable market families with full PRE_TAKE_CERT before any TAKE.
