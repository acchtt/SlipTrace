# Current Live Handoff — 2026-08-25 00:37 UTC+7

**State-only handoff. This file does not override CURRENT_MODEL.md or CURRENT_SESSION_LOCK.md.**

## Active session

- Lock ID: `LOL-2026-08-25-E12-G2-GX-0037-UTC7`
- Match scope: `LEC 2026 Summer — GIANTX vs G2 Esports — Game 2 / remaining series`
- Model: `LoL v0.3.58`
- Frozen authority commit: `67ba101919a5b96b0c237dd8abcb0d6a887a6b1d`
- Circuit breaker: `CLEAR`
- PDRL: `ACTIVE`
- KH directional calibration: `ACTIVE`
- Shadow only: `0.25u` default simulated stake, `0u` actual exposure
- Minimum odds: `1.60`
- PRE_TAKE_CERT interlock: `ACTIVE`
- KHMC / side-neutral margin parent: `ACTIVE`
- Same-map policy: maximum one TAKE per market family; ML / KH / TK / Duration are separate families.
- Airtable live-map policy: map-end batching.

## Game 2 prep state

The session is locked for Game 2 preparation, but the exact Game 1 result and Fearless depletion are not yet canonicalized in Airtable or this handoff.

Before final Game 2 draft certification, restore:

1. exact Game 1 winner / series score;
2. all ten Game 1 used champions and exact roles;
3. Game 2 side / first-pick / selection-right state when available;
4. any user-confirmed substitution or role change.

Do not grade Game 2 as an isolated full-pool draft. Fearless/restricted-pool state is mandatory under PDRL.

## Provisional current rosters

Saved LEC roster context:

G2 Esports:
- Top: BrokenBlade
- Jungle: SkewMond
- Mid: Caps
- ADC: Hans Sama
- Support: Labrov

GIANTX:
- Top: Oscarinin
- Jungle: Isma
- Mid: Jackies
- ADC: Flakked
- Support: Jun

These are prep context only. Current lobby/user-confirmed evidence supersedes them.

## Game 2 draft workflow

When the exact Game 2 draft arrives:

1. resolve FDS with series score, Fearless depletion, side and selection rights;
2. run DIM on exact roles;
3. run PDRL: LPM, JSC, TTM, OSP, PFP, EBD, WCSR, SPP, SAP and PAP;
4. preserve separate `DIM_EDGE`, `PRO_MAP_EDGE`, `PRO_EXEC_EDGE`, `SERIES_DRAFT_EDGE`, `FINAL_PRO_DRAFT_EDGE`;
5. use `FINAL_PRO_DRAFT_EDGE` as the original live-ML draft prior;
6. build draft-only underdog +kills proof only if exact DIM/UDKC requirements pass; PDRL may downgrade but cannot replace UDKC/KPA/KMS/RLD/TAM/CAS;
7. immediate-postdraft ML/KH/TK TAKE remains disabled.

## New Kill Handicap workflow

For every live KH candidate, do not inspect +kills first and reason backward.

Mandatory order:

`live state -> KH_MARGIN_CERT side-neutral distribution -> price both sides -> WMS -> preliminary sign -> sign-specific validator -> retained buffer -> PRE_TAKE_CERT -> verdict`

Required parent controls include:

- favorite defined independently of displayed line;
- one signed final-margin distribution;
- final-margin bins locked before line-driven sign selection;
- both-side pricing from the same distribution when both executable prices exist;
- WMS serial favorite cascade included;
- `SIGN_SELECTED_AFTER_DIST = PASS`;
- selected-side lower-bound cover probability above break-even + retained buffer;
- NKB/RNE treated as arithmetic only;
- failure of one sign provides zero evidence for the opposite sign.

For positive handicaps, `LAC_PRESSURE_CLASS` must distinguish real `EXPANSION_OPPORTUNITY_SUPPRESSED` from neutral `NO_EXPANSION_OPPORTUNITY`.

Every KH TAKE must persist:

`KHMC[DIST=P;BOTH=P/N-A;WMS=P;SIGN_AFTER_DIST=P;LB=<x>;BE=<y>;BUF=<z>;EDGE=P;DIRCAL=A]`

plus the complete selected-side gate signature.

## Live execution state

- Pregame/immediate-postdraft ML/KH/TK TAKEs disabled.
- Live ML/KH/TK require at least two usable synchronized snapshots.
- Contrary-draft live ML requires the retained LRO path where applicable.
- Duration Over requires full DOVC.
- Total Kills Under requires FRP PASS.
- Duration Under retains FCR.
- Greyed/stale markets are non-executable.
- Position-blind reassessment mandatory.
- Exact signed kill-margin arithmetic mandatory.
- Full PRE_TAKE_CERT + contradiction scan + mechanical validator required before TAKE.
- Verdict first; no GitHub/Airtable/web calls in the live critical path once bootstrap is loaded.

## Source handling

- No G2–GX clock correction is currently locked.
- Do not inherit NAVI–FNC source-specific clock corrections automatically.
- User clock correction supersedes the displayed clock immediately.
- `Barons X-Y` means historical Baron takes, not necessarily active Baron buff.
- Tower count is not a standalone ML/KH signal.
- `DELAYED DATA / FEED NOT UPDATING` banners alone are not stale signals.

## Next evidence

Preferred next input is either:

- Game 1 final/draft evidence, so Fearless depletion and series score can be canonicalized before Game 2 draft; or
- the complete Game 2 lobby/draft if it also makes the prior Game 1 depletion unambiguous.

If Game 2 draft arrives without exact Game 1 champion depletion, PDRL FDS is unresolved and `CLEAR/STRONG` professional draft labels are forbidden until the missing series-pool state is restored.
