# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-25-E13-KRXC-BFXY-1542-UTC7`  
**Status:** `CLOSED`  
**Effective:** `2026-08-25 15:42 UTC+7`  
**Closed:** `2026-08-25 20:05 UTC+7`  
**Scope:** `LCK Challengers League 2026 — KRX Challengers vs BNK FEARX Youth — completed series`  
**Closure reason:** `Series complete; KRX.C won 3-1. User closed/skipped the remaining 2026-08-25 evening slate and authorized prospective model calibration.`  
**Frozen authority used for E13:** `67ba101919a5b96b0c237dd8abcb0d6a887a6b1d`  
**Active analytical model during E13:** `LoL v0.3.58`  
**Circuit breaker at closure:** `CLEAR`  
**Actual exposure:** `0u`  
**Default shadow stake:** `0.25u`  
**Minimum accepted odds:** `1.60`

## Historical lock preservation

E13 remains historically frozen to authority commit:

`67ba101919a5b96b0c237dd8abcb0d6a887a6b1d`

Do not retroactively apply later analytical changes to E13 predictions, positions, settlements or P/L.

## Series final

KRX Challengers defeated BNK FEARX Youth **3-1**.

User-authoritative completed map results captured during the slate:

- Game 1: KRX.C win, 17-10, 42:28.
- Game 2: BFX.Y win, 18-10, 33:22.
- Game 3: KRX.C win, 18-8, 28:03.
- Game 4: KRX.C win, 23-12, 34:36.

The Game 4 Duration Over 32:00 shadow position at 1.886 settled as a win under E13 historical authority.

## Post-E13 canonical change

After the series closed, the user instructed:

**“Ok implement them now.”**

Default-branch `models/lol/CURRENT_MODEL.md` was then prospectively amended to activate the 2026-08-25 afternoon professional-meta / Kill-Handicap asymmetry / screenshot-sync / workload calibration for future authority epochs.

This CLOSED lock does not freeze or activate that amendment for E13.

## Next-session rule

There is **no ACTIVE LoL slate lock** after this closure.

On the next match/slate:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. read this CLOSED lock and treat it as historical only;
4. complete current default-branch bootstrap;
5. establish a new Session Authority Lock before the first TAKE-eligible decision;
6. freeze that new lock to a commit containing all intended current analytical amendments.

Until a new lock exists, match prep/HOLD analysis may continue but TAKE is not authorized.
