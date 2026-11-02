# 2026-11-02 Recent 44-Match Selection Repair Replay

## Scope

Same-information replay of the exact 44 unique assessed fixtures from the recent
Decision States cohort, beginning with Yongin FC–Seoul E-Land / Mito–Sanfrecce
and ending with Portland Timbers–Houston Dynamo.

The replay input contains frozen assessment evidence only. Final scores,
bookmaker outcomes and post-match facts are excluded from engine execution.
Fixtures are compared only inside their original assessment batch.

- Audit branch: `audit/replay-44-selection-20261102`
- Replay CI commit: `b8f17c455be1b6c53d6009c2c74acb0bb20f9475`
- Active deterministic CI run: `41393798299` — SUCCESS
- Frozen fixture count: **44**
- Frozen assessment batches: **24**

## Prospective replay result

| Metric | Result |
|---|---:|
| Original compiled states | 29 FOCUS / 15 WATCH |
| Repaired compiled states | 29 FOCUS / 15 WATCH |
| State changes | **0** |
| Repaired FOLLOW | 24 |
| Repaired RESERVE | 5 |
| Repaired REVIEW_ONLY | 15 |
| Rank movements | **9** |
| REVIEW_PARETO_DOMINANCE challengers | **0** |
| FOCUS rows blocked by review challenger | **0** |

The repair therefore changes ordering only. It does not change the qualification
boundary on this cohort, and the new review-dominance guard fires on none of the
44 fixtures.

## The nine rank movements

Outcome overlay is applied only after the same-information replay completed.

| Fixture | Old rank | New rank | FT | Effect |
|---|---:|---:|---:|---|
| Manchester City–Brighton | 3 | **1** | 0–1 | Worse |
| Werder Bremen–Hoffenheim | **1** | 2 | 2–0 | Worse/neutral below G3 |
| Fredrikstad–Rosenborg | 2 | 3 | 0–3 | Worse — only 3+ in block moved down |
| Club América–Toluca | 2 | **1** | 2–2 | Neutral |
| Necaxa W–Santos Laguna W | **1** | 2 | 1–3 | Neutral |
| Yokohama F.Marinos–Kawasaki | 2 | **1** | 4–2 | Better |
| Cerezo Osaka Sakai W–AS Elfen Saitama W | **1** | 2 | 4–0 | Better ordering by total-goal ceiling |
| PSIM Yogyakarta–Borneo | 2 | **1** | 2–1 | Worse at 4+ |
| Persib Bandung–Isenmulang | **1** | 2 | 4–0 | Worse at 4+ |

## Changed-block top-selection separation

Only four frozen assessment blocks changed their #1 fixture.

| Block | Old #1 goals | New #1 goals |
|---|---:|---:|
| 2026-10-31 14:49 UTC | Werder 2 | Man City 1 |
| 2026-11-01 02:54 UTC | Necaxa W 4 | América 4 |
| 2026-11-01 03:43 UTC | Cerezo W 4 | Yokohama 6 |
| 2026-11-01 08:14 UTC | Persib 4 | PSIM 3 |

- Old #1 reached 3+: **3/4**
- New #1 reached 3+: **3/4**
- Old #1 reached 4+: **3/4**
- New #1 reached 4+: **2/4**
- Mean goals of old #1: **3.50**
- Mean goals of new #1: **3.50**

This replay does **not** demonstrate better separation from the 2 November rank
repair. At the 4+ endpoint it is slightly worse in the only blocks where the
top selection actually changed.

## Diagnosis

The 44-match inversion is deeper than the lexicographic rank order.

1. The FOCUS/WATCH boundary remains unchanged on all 44 fixtures.
2. The Pareto review guard finds zero challengers because it uses the same
   clearability/ceiling score family that already rated the poor FOCUS rows
   above many eventual high-total WATCH rows.
3. Therefore the guard is too self-referential to detect the observed
   false-negative class.
4. Restoring mechanism-first ranking fixes a policy inconsistency, but it is not
   sufficient to repair match selection.

The next repair should target the **evidence-to-grade / qualification layer**,
not add another rank-key shuffle. In particular, the replay supports building a
separate block-relative challenger from independent prospective football facts
(goal-three supply, reply independence, continuation after first/second goal,
0-0/1-1/2-0 stall resistance and tournament incentive) rather than reusing the
existing clearability/ceiling outputs as its own validator.

No result-fitted threshold change is authorized by this replay.
