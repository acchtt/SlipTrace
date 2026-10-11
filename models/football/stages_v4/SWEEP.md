# /sweep — Football V4 source-backed fixture intake

This is the only current /sweep launcher. Do not load the retired
`00_NORMAL_CHAT_AISCORE_FETCH.md` or V1–V3 Step0 engines.

Read `league_registry.py` and `README.md`. Interpret the requested
sweep window in ICT; start at the actual current time unless an explicit
future start is given, and never include already-started fixtures.

Fetch one appropriately bounded current fixture feed (AiScore if
available; an independently checkable source otherwise), gather actual
match IDs, teams, source URLs, current kickoff and prematch statuses
within the window. Include the researched country's league tiers,
women's senior top flights and legitimate official competitions.
Do NOT require every women's league worldwide to be enumerated.
Preserve visible out-of-scope fixtures in audit ledger. For conditional
leagues include `researchability_status=VERIFIED` only if the actual
match/season data channels were checked, otherwise show PENDING.
No historical lineup or total-odds proof for routine leagues.

Prepare `football-stages-v4` input and run
`python models/football/stages_v4/stage.py --output v4_sweep.json sweep --source source.json`.
Report the full verified research queue sorted by the source-backed
goal-first signals, all pending-proof fixtures, excluded reasons, and
the actual integrity hash. No 8-match cap, forced ZIP, serial
Work chat, indefinite resume, imaginary fetch or automatically placed bet.
Airtable writes only when a genuine live source/run receipt is available.
