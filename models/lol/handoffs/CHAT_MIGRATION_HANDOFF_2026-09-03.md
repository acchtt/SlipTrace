# Chat Migration Handoff — LoL Project — 2026-09-03

**Purpose:** preserve decision-critical state and user workflow preferences when moving to a fresh chat. This is state/context only; GitHub current model + fresh session lock remain analytical authority.

## 1. Authority boundary

- Canonical repository: `acchtt/SlipTrace`.
- Current default-branch model: `LoL v1.3 — Hierarchy Moneyline + Duration Core`.
- Last completed lock: `LOL-2026-09-02-V13-HLE-T1-DRAFTONLY-FORCEDCHOICE-1459-UTC7`.
- Last authority commit used: `3e11a3a2b94a710dbc2d9ef16d88c3ac4ea0335c`.
- The HLE vs T1 series is COMPLETE (`HLE 3-2 T1`). Do **not** reuse that lock for a new series.
- A new chat must bootstrap from `models/lol/CURRENT_MODEL.md` -> `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md` -> `models/lol/session/CURRENT_SESSION_LOCK.md`, then establish a **fresh lock for the new current LCK match** before any new forced-choice Positions.
- If the old HLE-T1 lock is still marked ACTIVE, treat it as stale completed-series state and supersede it prospectively with the fresh match lock.

## 2. Pending task at chat migration

The user asked: `Lock current lck match` on 2026-09-03 around 15:53 UTC+7.

That fresh lock was **not completed before the chat migration request**. Therefore the next chat should:
1. identify the current LCK match for 2026-09-03;
2. build a new price-independent Gol.gg league-relative benchmark for the two teams;
3. freeze K/P0 before same-series results/prices;
4. create and verify a fresh `CURRENT_SESSION_LOCK.md` + current live handoff;
5. only then accept new map drafts/boards for forced-choice recording.

Do not infer the new matchup from the previous HLE-T1 lock.

## 3. Standing execution mode / user preferences

Prospectively continue the user-authorized **POSTDRAFT-ONLY / FORCED-CHOICE** experiment unless the user explicitly changes it:

- No live-state predictions.
- Ignore displayed match clock and all in-map gold/kills/objectives for prediction.
- Inputs for prediction: frozen pre-series benchmark + final draft/mechanisms + supplied market board.
- Enabled families: `Moneyline / Kill Handicap / Duration / Total Kills`.
- Exactly **one canonical Position per family per map**.
- If multiple alternate lines exist in a family, evaluate them but log only one best-fit canonical line.
- `PASS` is disabled for executable offered binary markets; choose the better side, or the less-negative side if both are negative EV.
- Price must not alter benchmark, draft classification, ML probability, KH margin distribution, duration F, or total-kill distribution.
- Tag `MODEL_EDGE` and `FORCED_NEG_EV=YES/NO` for every selected side.
- Shadow stake: `0.25u per family`.
- Actual exposure: `0u`.
- Record all takes.
- Airtable writes are deferred until **map end**; then settle map + all canonical Positions in one batch.
- No chasing, rescue, martingale, averaging down, or stake escalation.

### Portfolio-coherence rule added after HLE-T1 G5

For **small kill handicaps below 5 kills** (e.g. `±4.5`):
- the KH side must **align with the selected ML side**;
- do not take the opposite-side +4.5 while taking the other team ML.

For `±5.5` or wider, KH may still be evaluated independently because the cushion is materially different.

This rule applies **prospectively only**; do not rewrite historical G5.

## 4. Speed / output preference

User wants verdicts fast.

For each new draft + board:
1. **first line immediately:** the selected sides for all enabled families, e.g. `G2: Team A ML / Team A -5.5 / Under 32 / Over 29.5 — 1.00u shadow.`
2. then only the shortest necessary draft rationale / probabilities / forced-negative flags;
3. do **not** delay the user-visible verdict for GitHub or Airtable persistence;
4. persistence may follow after the picks are already delivered.

## 5. Post-audit draft discipline

Checkpoint audit file:
`models/lol/reviews/LOL_FORCED_CHOICE_CHECKPOINT_AUDIT_2026-09-02.md`

Standing enforcement:
1. complete the full Draft Interaction Matrix (DIM);
2. certify `D=+1/-1` only when at least **two independent mechanism advantages** survive adversarial failure-path review; otherwise `D=0 / EVEN-STYLE-DEPENDENT`;
3. do not overvalue vague labels such as `cleaner front-to-back` without interaction geometry;
4. KH requires a full signed final kill-margin distribution before price;
5. Total Kills requires a full total-kill distribution before price;
6. Duration F remains locked before line/odds;
7. no structural coefficient changes yet.

## 6. Canonical forced-choice cohort at migration

After HLE vs T1 Game 5:

- `28 canonical Positions / 7 samples per family`
- Record: `13W-15L`
- Shadow P/L: `-0.9980u`
- Actual exposure: `0u`

By family:
- Moneyline: `1-6 / -1.3305u`
- Kill Handicap: `3-4 / -0.3475u`
- Duration: `4-3 / +0.0795u`
- Total Kills: `5-2 / +0.6005u`

Next formal checkpoint:
- `40 canonical forced-choice Positions / 10 samples per family`
- need `3 more maps / 12 more positions`.

Do not make structural coefficient changes before that checkpoint unless a clear implementation bug is found.

## 7. Last completed series reference

HLE vs T1 final:
- HLE won series `3-2`.
- G5 final: HLE won `22-9` in `28:01`.
- G5 positions: HLE ML WIN / T1 +4.5 LOSS / Over 32 LOSS / Over 30.5 kills WIN.
- G5 net: `-0.0870u`.
- HLE-T1 series forced-choice net: `-0.8040u`.
- Full series handoff: `models/lol/handoffs/CURRENT_LIVE_HANDOFF_2026-09-02_HLE_T1.md`.

## 8. New-chat continuation instruction

Use this exact operating principle:

> Continue the LoL project from `acchtt/SlipTrace`. Bootstrap from `models/lol/CURRENT_MODEL.md`, then `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`, then `models/lol/session/CURRENT_SESSION_LOCK.md`. Load `models/lol/handoffs/CHAT_MIGRATION_HANDOFF_2026-09-03.md` as migration state. The previous HLE-T1 series is complete, so do not reuse its lock. The pending task is to identify and lock the current LCK match with a fresh Gol.gg benchmark and fresh session lock. Preserve draft-only forced-choice mode, one canonical line per family, speed-first verdicts, map-end Airtable logging, post-audit DIM discipline, and the new rule that kill handicaps below 5 must align with the selected ML side. Current cohort is 28 positions / 7 per family / -0.9980u; next audit at 40 positions.
