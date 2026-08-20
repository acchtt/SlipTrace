# KRX vs NS Game 2 — Underdog +Kills Cushion Sufficiency Review — 2026-08-20

**Model authority:** canonical LoL v0.3.58  
**Incident:** LCK KRX vs NS Game 2  
**Historical visible TAKE:** KRX +3.5 kills @1.909 at 8:41, 0.25u shadow / 0u actual  
**Final:** NS 16-9 KRX; final NS kill margin +7; historical result LOSS -0.25u

## Finding

The draft-only UDKC was not the main failure. KRX could reasonably be classified as having a structurally functional fallback through K'Sante/Shen/Orianna/Jhin/Zaahen. The execution error was treating `UDKC = STABLE` as if it were enough to justify a thin live handicap.

At entry:

- kills were 1-1;
- NS gold lead was only +59;
- KRX led dragons 1-0;
- towers were 0-0;
- KRX +3.5 @1.909 was available;
- current signed NS kill margin was 0;
- NS needed only **+4 additional net kills** from that state to beat KRX +3.5.

That remaining cushion was vulnerable to one ordinary bad compulsory fight plus immediate continuation. No live evidence had yet demonstrated that KRX's draft-certified anti-cascade routes were actually suppressing a normal 3-4 net-kill expansion cycle under pressure.

The correct canonical retrospective verdict is therefore:

`HOLD/PASS KRX +3.5 @1.909 — 0u`

The historical position/result/P&L remain recorded as issued; the thesis should be audit-invalidated rather than rewritten.

## Root cause

The model had strong draft-certification gates but no explicit **post-certification cushion-sufficiency gate**. This allowed the following invalid reasoning chain:

`UDKC STABLE -> current game looks even -> favorite needs +4 net kills -> TAKE`

The exact NKB arithmetic was correct, but the analysis failed to ask whether the remaining NKB could be consumed by a single ordinary adverse cycle.

UDKC answers **whether the underdog possesses structural margin-suppression routes**. It does not answer **whether the offered live cushion is large enough for the current state**.

## Canonical fix — UCS

Add mandatory **UCS — Underdog Cushion Sufficiency** after UDKC/live-preservation checks and before pricing an underdog +kills TAKE.

### 1. Exact remaining cushion

Compute:

- current signed favorite kill margin;
- handicap failure threshold;
- **NKB — Net Kills to Break:** the minimum additional favorite net kills from the current state required to make the underdog handicap lose.

### 2. Single-Cycle Net Expansion stress test

Classify **SCNE — Single-Cycle Net Expansion**: a realistic, ordinary adverse net-kill swing the favorite can produce from the next compulsory contact **plus immediate continuation** (chase, re-engage, objective turn, dive, or base-defense collection).

SCNE is not a catastrophic-tail estimate. It asks what a normal losing cycle can cost this specific underdog given the drafts and current map control.

### 3. Thin-cushion hardening

- If `NKB <= 4`, the cushion is **THIN**.
- A THIN cushion cannot pass UCS from draft theory, even when UDKC is STABLE.
- For THIN cushions, require **observed live suppression proof** that the underdog has already limited a comparable adverse contact through disengage/reform, protected DPS, return kills, or another concrete anti-cascade mechanism.
- If that proof is absent or ambiguous: `UCS = FAIL/UNCERTAIN -> HOLD/PASS`.

This is not a blanket ban on nominal +3.5. If the underdog is already ahead in kills, a +3.5 line may imply a much larger NKB. The gate is based on the **remaining live cushion**, not the printed handicap alone.

### 4. One-cycle vulnerability

If `NKB <= plausible SCNE`, UCS fails unless strong observed live suppression evidence makes that ordinary expansion route materially unlikely.

If SCNE cannot be resolved confidently and the cushion is THIN, fail closed.

### 5. Eligibility relationship

An underdog +kills TAKE now requires both:

- complete UDKC remains STABLE after live reassessment; and
- `UCS = PASS`.

`UDKC = STABLE` means **eligible to inspect the line**, not **line is valuable**.

## Why this is an in-place v0.3.58 fix

This is a narrow execution/governance correction to underdog +kills pricing after certification. It does not change the analytical model family and does not justify creating v0.3.59 or restoring retired versions.

Reference procedure amended by this review:
`models/lol/procedures/LOL_UNDERDOG_PLUSKILLS_DRAFT_LOCK_GUARD_2026-08-19.md`
