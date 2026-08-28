# EDG vs NIP Game 1 — Live ML Structural Context Review — 2026-08-28

**Scope:** LPL 2026 Split 3 / Play-In Knockouts — EDward Gaming vs Ninjas in Pyjamas — Game 1  
**Model at time of live candidate:** LoL v0.3.58 under lock `LOL-2026-08-28-E16-EDG-NIP-1311-UTC7`  
**Historical position status:** no Position existed for the reviewed EDG ML candidate because the user did not confirm the quoted line still existed  
**Purpose:** diagnose a causal classification error without rewriting historical evidence or using the final result as proof

## Sequence

At approximately 19:18:

- EDG 4–6 NIP kills;
- EDG 2–1 towers;
- NIP 3–0 dragons / Soul point;
- EDG retained favorable role economy across several non-support roles;
- NIP retained the easier Cho'Gath/Gnar/Cassiopeia/Ashe/Seraphine compulsory 5v5 and the next-objective schedule.

The correct live verdict was `PASS — EDG ML` because EDG's projected early-control route had repeatedly failed to control objectives and NIP's next compulsory fight geometry remained easier.

At approximately 22:47:

- EDG 5–7 NIP kills;
- EDG 3–1 towers;
- NIP still 3–0 dragons;
- EDG continued to show broad resource advantages in top/jungle/mid/bot;
- EDG ML was displayed at 2.021.

A visible analytical TAKE candidate was issued on EDG ML @2.021. The user never confirmed that exact price still existed, so under the active execution gate there was no Position, no W/L, and no P/L.

## Error

The analytical flip from PASS to TAKE gave excessive causal weight to the improved tower differential and broad economy without proving that those structures repaired the decision-critical cause of the earlier PASS.

The missing checks were:

1. Did the 3–1 tower state create first move or safer vision entry at the next Soul fight?
2. Did it force NIP to answer a side lane strongly enough to change objective numbers/timing?
3. Did it create a credible cross-map terminal trade if NIP took Soul?
4. Did it materially improve EDG's CFC against NIP's easier front-to-back 5v5?
5. Had EDG actually repaired their repeated failure to convert lane/resource control into neutral-objective control?

Those questions were not positively answered by the synchronized state.

The tower lead was therefore **context**, not demonstrated forward control.

## Correct causal classification

At 22:47:

- `PRIOR_PASS_CAUSE = EDG objective-control mechanism failed + NIP easier Soul-point compulsory 5v5`;
- `TOWER_STATE_CLASS = CONTEXT_ONLY` absent proof of a forward map-control consequence;
- `OBJECTIVE_SCHEDULE_OFFSET = FAIL/UNPROVEN` because NIP still owned the 3-dragon/Soul-point schedule;
- `PASS_CAUSE_REPAIR = FAIL` because the exact earlier rejection cause remained active;
- `REGIME_FLIP_DELTA = FAIL` because the new tower differential did not demonstrate repaired CFC/objective control.

Therefore the correct analytical verdict at the displayed 2.021 price was:

`PASS — EDG ML @2.021`.

## Outcome separation

NIP later won Game 1 22–7 with 4–1 dragons, 2 Barons, 10–4 towers and 2 inhibitors.

That outcome is recorded for history but is **not** the evidence used to justify the correction. The correction is supported by information already available at 22:47: the earlier PASS cause remained active and the new tower state lacked a causal map to the next compulsory fight.

## Model action

Canonicalize two controls prospectively:

1. **Structural Context Gate:** towers/structures are context by default and become positive ML evidence only when mapped to a specific forward-control consequence.
2. **Prior-PASS Cause Repair Gate:** a same-side ML cannot flip from PASS to TAKE unless the previous rejection cause is explicitly repaired or a genuinely new causal thesis supersedes it.

Implementation:
`models/lol/procedures/LOL_ML_STRUCTURAL_CONTEXT_AND_REGIME_FLIP_REPAIR_2026-08-28.md`
