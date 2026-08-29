# Current Live Handoff — T1 vs BNK FEARX — 2026-08-29

**State only — not analytical authority**

## Series

- Competition: `LCK 2026 Playoffs`
- Round: `Upper Bracket Round 1`
- Match: `T1 vs BNK FEARX`
- Format: `Bo5 Fearless Draft`
- Scheduled start: `2026-08-29 15:00 UTC+7 / 17:00 KST`
- Series state at handoff creation: `not started`

## Active model state

- Model: `LoL v1.0 — Moneyline Core`
- Active lock: `LOL-2026-08-29-V1-T1-BFX-1352-UTC7`
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
- Initial v1.0 confirmed Position sample: `0` at series-lock creation

## Bootstrap next continuation

1. Fetch default-branch `models/lol/CURRENT_MODEL.md`.
2. Immediately load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`.
3. Fetch mutable `models/lol/session/CURRENT_SESSION_LOCK.md`.
4. Verify lock `LOL-2026-08-29-V1-T1-BFX-1352-UTC7` and authority commit `1be61970a3b586fd173479a4e591cfe391e03f0f`.
5. Re-fetch locked `CURRENT_MODEL.md` at that commit.
6. Load the exact v1.0 files in locked CURRENT_MODEL load order.
7. Use Airtable as map/snapshot/position ledger only.
8. Load this or a newer T1–BFX handoff last.

## Analytical core

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

## Series-specific preparation

Before Game 1 draft analysis:

- use canonical saved T1 and BNK FEARX roster context first;
- user-supplied exact lineup/card overrides generic roster sources when reliable;
- resolve exact five and roles before using player fit materially;
- identify the current professional patch and any competition-specific Fearless implementation details that affect legal champion reuse.

For each map:

1. resolve compact draft prior `T1 / EVEN / BFX` and concrete win mechanisms;
2. for Games 2+ incorporate the actual champions consumed earlier in the series;
3. no pregame/immediate-postdraft TAKE;
4. wait for usable synchronized live state plus executable Moneyline;
5. score `R/X/O/T` and mechanism contradiction price-blind;
6. calculate model probability;
7. only then compare against the offered Moneyline;
8. TAKE CANDIDATE only if all v1.0 execution controls pass;
9. create a Position only after explicit user confirmation that the exact quoted ML/odds still exist.

## Validation freeze

Core remains frozen:

- 10 Positions: diagnostic only;
- 20: minimum architecture review;
- 30: preferred first full calibration review.

Audit taxonomy only:

- DRAFT READ ERROR
- LIVE STATE ERROR
- PROBABILITY/CALIBRATION ERROR
- PRICE/EXECUTION ERROR

## Historical boundary

All v0.3.58 files, procedures, reviews and Airtable records remain historical/audit/research authority only. Do not load their gate tree into active T1–BFX analysis.

No live betting verdict has been issued for this series at handoff creation.
