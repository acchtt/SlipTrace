# Current Live Handoff — 2026-08-26 18:39 UTC+7

## Series
LCK 2026 Play-In — KT Rolster vs HANJIN BRION
Series score: 2-2 after Game 4.

## Authority
Active lock remains `LOL-2026-08-26-E14R1-KT-BRO-1754-UTC7` at frozen authority commit `0424b09b9a435411fc1c3fb1dc91c2235f31b7bb`.
LoL v0.3.58. Circuit breaker CLEAR. PDRL/PML active. KH directional calibration and dog probation active under the frozen authority.

Default-branch review `models/lol/reviews/E14R1_GAME4_STRICTNESS_REVIEW_2026-08-26.md` is REVIEW ONLY and does not override the frozen lock. No procedure change is active unless user explicitly authorizes another relock/new epoch.

## Game 4 final
User-authoritative final supplied state: KT won, 33:28, KT 17-8 BRO, KT +6.7k, towers 7-3, dragons 3-2, Barons 1-0, inhibitors 1-0.
No shadow position. P/L 0u. Airtable map-end batch complete: one Map row, seven meaningful snapshots, zero Position rows. Review complete.

Data correction: at 9:18 and 11:48 dragons were BRO 0-KT 1. Earlier commentary incorrectly read BRO 1-KT 0.

## Game 4 strictness finding
Zero TAKEs was mixed, not uniformly wrong. Correct passes included BRO -3.5 at 18:28/21:58 and Total Kills Over candidates; BRO ML 1.598 at 11:48 was below floor and lost.

Prospective review concern:
- dog KH `LARGE-only` plus binary 1/2-cycle threshold-crossability is too restrictive and effectively bans many +3.5 states;
- two mechanism-matched suppression windows are difficult to prove from screenshot-only evidence;
- snapshot-compatible COUNTER_EXPANSION / BOUNDED_EXPANSION evidence should be considered in a future relock;
- live ML should strengthen lead-concentration discount when one role holds most enemy gold while the other team has objective/fight-mechanism offsets;
- keep global 1.60 minimum odds floor pending broader evidence.

Key audit examples, not backfilled positions:
- 18:28 KT +3.5 @1.806, KT ML 2.008;
- 21:58 KT +3.5 @1.879, KT ML 2.025.
Historical verdicts remain HOLD/PASS.

## Fearless depletion entering Game 5
KT used:
G1 Olaf / Nocturne / Ryze / Miss Fortune / Nautilus
G2 Ornn / Naafiri / Syndra / Yunara / Lulu
G3 Yorick / Wukong / Zoe / Sivir / Bard
G4 Ambessa / Lee Sin / Lissandra / Ashe / Seraphine

BRO used:
G1 Kled / Jarvan IV / Anivia / Lucian / Milio
G2 Rumble / Vi / Ahri / Kalista / Renata Glasc
G3 Jayce / Xin Zhao / LeBlanc / Ezreal / Elise
G4 Gnar / Pantheon / Locke / Jhin / Camille

Game 5 is deciding map. Fearless archetype-inventory tracking remains mandatory.

## Operating rules
- Same-message user scoreboard + bookmaker screenshots are synchronized by default unless actual state contradicts.
- No Airtable logging mid-map; batch at map end.
- Actual exposure 0u; default shadow stake 0.25u; minimum odds 1.60.
- Under current frozen E14R1, TAKE execution remains enabled, but the Game 4 review has not altered any gate.
