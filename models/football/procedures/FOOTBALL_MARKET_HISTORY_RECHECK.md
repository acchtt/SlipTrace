# Football Step-2 Market-History Recheck

**Status:** MANDATORY STEP-2 EVIDENCE BLOCK  
**Applies to:** Football C official, C2 shadow  
**Authority:** context/reinspection only; market history does not create football structure

## 1. Mandatory attempt

For every Step-2 fixture, attempt a lightweight Asian-total history trace before the final C/C2 action:

`OPEN -> PRE-XI -> POST-XI / CURRENT PREMATCH`

Prefer the same bookmaker/source across snapshots. If same-source history is unavailable, use clearly timestamped comparable sources and mark limitations.

Set exactly one:
- `MARKET HISTORY FOUND`
- `MARKET HISTORY PARTIAL`
- `MARKET HISTORY UNAVAILABLE — ATTEMPTED`

Do not fabricate missing snapshots.

## 2. What to capture

When observable:
- opening/main Asian total;
- latest reliable pre-XI total;
- current/post-XI main market center;
- source and timestamp context;
- movement direction.

Movement:
- `UP_0.50_PLUS`
- `UP_0.25`
- `STABLE`
- `DOWN_0.25`
- `DOWN_0.50_PLUS`
- `MIXED`
- `UNCLEAR`

The user's current executable quote remains execution authority. External current prices are context only.

## 3. Conflict recheck

Market history is a reinspection trigger, not a model.

Recheck football evidence when:
- XI looks damaged but the total strengthens by >=0.25;
- XI looks stronger/intact but the total weakens by >=0.25;
- current market center is >=0.25 below the frozen C supported line;
- current market center is materially above the frozen C supported line;
- sources disagree materially.

Search specifically for:
- late attacking/defensive absences;
- formation/role changes;
- goalkeeper/centre-back changes;
- tactical suppression;
- tournament incentive changes;
- weather/pitch;
- source/time mismatch;
- stale or misidentified fixture data.

Persist one:
- `NOT_REQUIRED`
- `RECHECKED_FOOTBALL_EXPLAINED`
- `RECHECKED_UNEXPLAINED`
- `LIMITED`

## 4. Model boundary

Market movement may:
- expose missing information;
- reduce confidence;
- force a football recheck;
- help explain why a lower protected line is available.

Market movement may not:
- create a scoring route;
- turn TWO_SIDED into burden-completing;
- upgrade C/C2 rank by price alone;
- raise supported burden;
- replace H2H/tournament/XI research.

A lower total is safer mechanically but is not automatically value.

## 5. Research separation

The market-history attempt does **not** satisfy the mandatory fresh post-XI football research gate.

Both must be completed/declaratively attempted:
- `POST-XI RESEARCH = ...`
- `MARKET HISTORY = ...`

## 6. Output

Every /xi match block must show:
- market-history status;
- OPEN / PRE-XI / CURRENT trace when found;
- movement classification;
- conflict-recheck result;
- current executable user quote separately.

If unavailable:
`MARKET HISTORY: UNAVAILABLE — ATTEMPTED`

Do not hide the missing history.
