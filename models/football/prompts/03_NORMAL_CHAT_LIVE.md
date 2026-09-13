# 03 — Normal Chat: Live Review

Use Normal Chat with medium or high reasoning.

## Authority
Read `models/football/CURRENT_MODEL.md` first and use its active official model/load order. Never infer the current version from this prompt.

Load the current stage-relevant files for live execution: time/schedule integrity, betting/live procedure, active official rules, and Decision States contract. Preserve frozen PRE history.

## Airtable
Base ID `appWyZJjitSBATXAU`.
Daily Coverage Ledger `tblcl1UAyMqZT6Ub0`.
Decision States `tblQmUpd5WjBLQ38X`.
Website Picks `tblg3J5sbJYbzuTYD`.

Read only the requested fixture's frozen PRE plus the latest material Decision State unless the user explicitly asks for broader comparison. Do not read Website Picks by default unless existing exposure is necessary to answer the current live question.

## User-supplied live state
Use the user's current score, minute, live Asian-total line/price, and any supplied stats/cards/substitutions/injuries. Do not automatically fetch bookmaker markets unless explicitly asked.

If no current line/price is supplied, give game-state OPEN/WATCH/CLOSED only; do not invent an executable market.

## Live evaluation
Validate or invalidate the frozen thesis; do not rewrite PRE.

Assess current route survival, carrier ceiling, opponent contribution, failure-mode evolution, conversion quality/current scoring hazard, exact remaining-goal burden, and the current model's price rules.

If the active model contains an EGE/high-environment regime, preserve the already-documented pre-goal/post-XI supported burden. A quiet opening may corroborate an already-established high-line calibration if the current rules allow it, but a goal-driven line expansion must never create or raise the supported burden. After an early goal, follow the current no-chase/post-goal-normalization rule and use the model's corresponding audit label.

Apply any inherited halftime compression/saturation gate when the current model says it remains active. Do not project a high-scoring first half forward automatically.

## Logging
Do not create a Decision State for routine commentary or every minute update. Persist only genuinely material live states required by the current Decision States contract, such as a new executable action, a material closure/invalidation, or an explicitly requested checkpoint.

## v0.2.54 quarantine
All new live/relative-decay Over entries are shadow-only. With synchronized evidence record `SHADOW LIVE/DECAY — NO OFFICIAL EXPOSURE`; without it use `LIVE CHANCE QUALITY UNAVAILABLE — HOLD`. Do not write Website Picks or official P/L for either state.

## Output
Very compact: LIVE STATUS, best supplied/supported line, price class, confidence, action, and a short reason. Do not repeat the entire PRE research.