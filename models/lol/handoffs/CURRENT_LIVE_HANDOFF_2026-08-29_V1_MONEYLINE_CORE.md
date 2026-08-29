# Current Live Handoff — LoL v1.0 Moneyline Core — 2026-08-29

**State only — not analytical authority**

## Active model state

- Model: `LoL v1.0 — Moneyline Core`
- Active lock: `LOL-2026-08-29-V1-ML-1341-UTC7`
- Frozen authority commit: `1be61970a3b586fd173479a4e591cfe391e03f0f`
- Circuit breaker: `CLEAR`
- Betting market: `Moneyline only`
- Kill Handicap: `RETIRED_FROM_BETTING`
- Total Kills: `RETIRED_FROM_BETTING`
- Duration: `RETIRED_FROM_BETTING`
- Actual exposure: `0u`
- Default shadow stake: `0.25u`
- Minimum odds: `1.60`
- Required edge: `+5.0pp vs raw implied probability`
- User line-existence confirmation: `ACTIVE`
- Initial v1.0 confirmed Position sample: `0` at rebuild completion

No live matchup is selected in this handoff.

## Bootstrap next chat

1. Fetch default-branch `models/lol/CURRENT_MODEL.md`.
2. Immediately load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`.
3. Fetch mutable `models/lol/session/CURRENT_SESSION_LOCK.md`.
4. Verify lock `LOL-2026-08-29-V1-ML-1341-UTC7` and authority commit `1be61970a3b586fd173479a4e591cfe391e03f0f`.
5. Re-fetch locked `CURRENT_MODEL.md` at that commit.
6. Load the exact v1.0 files in locked CURRENT_MODEL load order.
7. Use Airtable as map/snapshot/position ledger only.
8. Load this or a newer applicable handoff last.

## Compact analytical core

From Team A perspective:

- `D = +1 / 0 / -1` draft prior;
- `R/X/O/T = -2..+2`;
- mechanism state = `INTACT / WEAKENING / BROKEN / REPLACED`;
- `S = 1.0*D_eff + 1.5*R + 1.5*X + 1.25*O + 1.0*T`;
- `P(A) = clamp(50% + 3*S pp, 15%, 85%)`;
- `P(B) = 100% - P(A)`;
- probability must be locked before price comparison;
- book implied = `1/odds`;
- TAKE CANDIDATE requires odds >=1.60 and model edge >=+5.0pp.

Structures are context only unless they demonstrably change forward map control.

## Visible live format

`ML — [TEAM A vs TEAM B]`

`Draft: [A / EVEN / B] — [win mechanism]`

`Live: R [score] | X [score] | O [score] | T [score] | Mechanism [state]`

`Model: A [xx]% / B [yy]%`

`Price: [selection] @[odds] -> book [qq.q]% | edge [±e.e]pp`

`Verdict: HOLD / PASS / TAKE CANDIDATE — [short cause]`

For TAKE CANDIDATE:

`USER_LINE_CONFIRMATION=PENDING — confirm exact TEAM ML @ODDS still exists.`

No Position exists until explicit confirmation.

## Validation freeze

Core is frozen for initial user-confirmed executable Moneyline sample:

- 10 Positions: diagnostic only;
- 20: minimum architecture review;
- 30: preferred first full calibration review.

Do not change the core after one normal loss.

Audit taxonomy only:

- DRAFT READ ERROR
- LIVE STATE ERROR
- PROBABILITY/CALIBRATION ERROR
- PRICE/EXECUTION ERROR

## Historical boundary

All v0.3.58 files, procedures, reviews and Airtable records are preserved unchanged as historical/audit/research authority only. Do not load their derivative gate tree into active v1.0 analysis.

Historical evidence used for the rebuild is recorded in:

`models/lol/reviews/LOL_V1.0_CLEAN_REBUILD_AUDIT_2026-08-29.md`.

## Next live match

At the next match:

1. resolve exact pro draft/roles and material Fearless/restricted-pool context;
2. record compact draft prior/mechanisms only;
3. wait for usable synchronized live state + executable ML;
4. score probability price-blind;
5. then compare to price;
6. TAKE CANDIDATE only if all v1.0 execution controls pass;
7. create Position only after explicit user line confirmation.
