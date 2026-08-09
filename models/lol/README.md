# League of Legends Model Namespace

Canonical entry point: `models/lol/CURRENT_MODEL.md`

## Structure

- `rules/` — versioned model rule deltas
- `procedures/` — operational procedures, addenda, and scoreboard-reading protocol
- `context/` — consolidated baseline rules, probation status, calibration handbook, and pre-match/pre-game procedure
- `handoffs/` — current match-state transfers between chats
- `reviews/` — retained model-development evidence and calibration reviews

## Active version

**LoL v0.3.50.** Normal startup loads `CURRENT_MODEL.md`, then v0.3.50 backward through retained rule deltas, the mandatory live checklist, baseline context/procedures, shared stake policy, and the latest relevant handoff.

Where conflicts exist, the newest active delta controls.

## Current v0.3.50 focus

- Draft remains the primary post-lock conditional mechanism layer.
- Kill Handicap separates map dominance from kill-margin conversion via KCV, Structure Substitution, Net-Kill Burden and Remaining Fight Inventory.
- Total Kills now separates **Observed Kill Pace, de-duplicated Forward Contact Inventory, Contact Realization Rate, and Contact Lethality**.
- Major objective windows must test **Contest / Concede / Trade / Delay** before being counted as fights.
- Strong engage/zone control can produce **Threat Deterrence**, lowering realized contact even when conditional fight lethality is high.
- Pregame Overs cannot be justified by engage inventory alone; one-sided control drafts receive extra Over friction when concession/trade remains viable.
- Same-map Total Kills + Kill Handicap add-ons still require separate T/M projections and a four-cell joint outcome matrix.

## Boundaries

- New LoL files must stay inside `models/lol/`.
- Root application files are not LoL model context.
- `models/football/` must not be loaded by a LoL chat.
- Airtable is the canonical live map/snapshot/position tracker for this project; broader repository ledger conventions remain governed by project-level procedures.
