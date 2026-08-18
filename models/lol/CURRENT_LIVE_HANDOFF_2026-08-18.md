# Current Live Handoff — 2026-08-18 UTC+7

## Authority

GitHub is model/rules authority. Airtable is canonical live map/snapshot/position ledger.

**Before using this handoff, load `models/lol/CURRENT_MODEL.md` first and obey `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`.**

If this handoff conflicts with `CURRENT_MODEL.md`, `CURRENT_MODEL.md` wins.

## Active model

**LoL v0.3.58** is canonical.

- v0.3.59 and v0.3.60 are retired from active analytical use.
- Do not load/blend them.
- FRP/FCR/CFC/SMR are active only because they are incorporated into canonical v0.3.58.
- KPA/KMS + False-Stable amendment is active inside the v0.3.58 fallback procedure.

## New mandatory session guardrail

`models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`

Key points:

- new chat: fetch `CURRENT_MODEL.md` first;
- stale memory/project context/pasted prompts do not override GitHub;
- latest handoff loads last;
- if a live state arrives before bootstrap, visible verdict is `MODEL NOT LOADED — HOLD` before any tool call;
- every market-family TAKE must clear its exact canonical hard gates;
- never say `logged` unless Airtable write + verification actually succeeded.

Reference review:
`models/lol/reviews/DNS_NS_G3_SESSION_BOOTSTRAP_AND_FRP_EXECUTION_REVIEW_2026-08-18.md`

## Current LCK CL series

DNS Challengers vs NS Challengers, series was 1-1 entering Game 3.

### Game 2

NS won 21-12 in 34:26. No position taken. Early DNS +4.5 watch never became a TAKE.

### Game 3 draft

DNS: Rumble / Trundle / Mel / Caitlyn / Bard  
NS: Gnar / Wukong / Aurora / Ezreal / Seraphine

Valid logged snapshots before the procedure error:

- 4:51 — 0-0 kills, DNS +159g, 0-0 towers, 0-0 dragons — HOLD.
- 8:51 — NS 1-0 kills, NS +487g, 0-0 towers, 0-0 dragons — HOLD.
- 11:50 — NS 2-0 kills, NS +1.4k, 0-0 towers, NS 1-0 dragons — HOLD.

At approximately 13:40:

- NS 4-0 kills;
- NS about +3.0k gold;
- towers 0-0;
- NS 1-0 dragons;
- Total Kills Under 26.5 @1.839 was visibly issued as a 0.25u shadow TAKE.

This TAKE was a **procedure/execution error**. Correct canonical v0.3.58 verdict was PASS/HOLD because `FRP` was not established as PASS. The game later reached at least 14-14 kills, so Under 26.5 was mathematically lost.

Canonical audit label:

`EXECUTION / PROCEDURE ERROR — correct v0.3.58 verdict PASS/HOLD; FRP FAIL/UNCERTAIN.`

Do not use this loss to create a new model version.

## Live workflow to preserve

- verdict first;
- no connector/logging call before visible verdict;
- post-draft ML/KH/TK TAKE disabled;
- live ML/KH/TK require two synchronized snapshots;
- position-blind reassessment;
- exact signed kill-margin arithmetic;
- favorite -kills: FFD + RNE + Structure Substitution / safe-concede tests;
- underdog +kills: fail-closed fallback + KPA/KMS + False-Stable Guard;
- TK Under: `FRP = PASS` mandatory;
- Duration Under: `FCR = ROBUST` mandatory except retained terminal exceptions;
- live ML: Lead Decomposition + CFC stress test;
- minimum odds 1.60;
- shadow only, default 0.25u, actual 0u;
- maximum one TAKE per family per map;
- no chasing/rescue/martingale/stake escalation;
- every valid verdict followed by actual Airtable snapshot write + verification.
