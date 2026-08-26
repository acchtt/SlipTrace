# E14R1 Game 4 Strictness Review — 2026-08-26

Status: REVIEW ONLY — does not modify frozen E14R1 authority.

Series: KT Rolster vs HANJIN BRION, Game 4. Final user-authoritative state: KT won 17-8 at 33:28 supplied state. No shadow position; P/L 0u.

## What the zero-TAKE map actually showed

Zero TAKEs alone does not prove blanket conservatism. Several passes were correct:
- BRO -3.5 at 18:28 and 21:58 would have lost.
- Total Kills Overs shown at 15:18/18:28 would have lost against final 25 kills.
- BRO ML 1.598 at 11:48 was below the global floor and ultimately lost.

However, two active controls are now too restrictive for the actual screenshot-driven evidence stream.

### 1. Dog KH probation is effectively a small-handicap ban

Current E14R1 requires DOG_CUSHION_CLASS=LARGE and automatically fails when a MATERIAL/HIGH one- or two-cycle WMS branch can cross the dog failure threshold. In LoL, a +3.5 failure threshold is almost always crossable by one ordinary 4-0 fight, so this binary rule makes +3.5 structurally unavailable even when the underdog has independent map-win equity.

Key prospective audit examples:
- 18:28: KT +3.5 @1.806; kills 4-4, KT down 1.6k and one tower, but up 2-1 dragons, better 5v5 draft, and had already produced a 3-kill counter-expansion.
- 21:58: KT +3.5 @1.879; KT down 1 kill and 1.8k, towers tied 2-2, up 2-1 dragons, same independent 5v5 win path.

The final KT win is supporting evidence only; the pre-result criticism is that the rule never allowed these candidates to reach pricing certification.

Recommended prospective adjustment:
- permit MATERIAL dog cushions when the dog has independent ML support and strong live resilience/counter-expansion evidence;
- retain THIN as presumptive PASS;
- replace binary cycle-crossability veto with probability-weighted hazard: HIGH + imminent forced cycle can veto; MATERIAL should increase buffer/tail weight rather than auto-fail.

### 2. Two video-style suppression windows are incompatible with screenshot evidence

The user supplies synchronized scoreboard + market screenshots, not continuous video. Requiring two mechanism-matched observed suppression windows often asks for evidence the interface cannot provide.

Recommended screenshot-compatible evidence classes:
- COUNTER_EXPANSION: underdog materially reverses favorite kill/economy/objective pressure across synchronized snapshots.
- BOUNDED_EXPANSION: favorite has pressure and compulsory-cycle access but margin expansion remains bounded while the underdog preserves/recovers structures or objectives.

One strong COUNTER_EXPANSION plus one BOUNDED_EXPANSION interval should be eligible to substitute for two video-observed suppression windows, subject to WMS and pricing.

### 3. Live ML underweighted lead concentration

At 18:28 and 21:58 BRO's gold edge was heavily concentrated in Gnar while KT held the dragon edge, had already demonstrated a 3-kill counter-expansion, and retained the cleaner 5v5 control shell. KT ML was 2.008 and 2.025 respectively. The live ML process should more explicitly discount concentrated single-role gold when the opposing team has objective parity/advantage and a demonstrated teamfight mechanism.

Recommended prospective adjustment:
- strengthen LEAD_CONCENTRATION_DISCOUNT inside Lead Decomposition;
- allow a close-state underdog ML to certify when concentrated enemy gold is offset by objective control + demonstrated fight mechanism + favorable draft execution shape.

### 4. Keep the global 1.60 floor

Do not lower the 1.60 minimum from this map. KT 1.592 at 9:18 ultimately won, but BRO 1.598 at 11:48 ultimately lost. One near-floor winner is not enough evidence to weaken the global price floor.

## Data correction

At 9:18 and 11:48 the scoreboard showed dragons BRO 0-KT 1. Earlier live commentary misread this as BRO 1-KT 0, overstating BRO control. Airtable Game 4 records have been corrected to the actual objective state.

## Governance

Historical HOLD/PASS verdicts remain unchanged and are not backfilled. This review is prospective only. E14R1 remains frozen until the user explicitly authorizes another relock/new authority epoch.
