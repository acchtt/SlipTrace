# SlipTrace

**Track every slip.**

SlipTrace is a local-first betting journal designed for GitHub Pages. It tracks units, exposure, results, profit/loss, bankroll cash flow, betting metadata, reports, and configurable risk limits while keeping manual browser entries local.

## Features

- [Touchline live football](football/): lightweight BSD live scores, optional WebSocket push, fixtures, results, lineups and statistics. Connect your BSD key directly; no AI service or backend deployment is required. See [setup and speed details](football/README.md).

- Parses pasted Vietnamese and English betslip text.
- Reads betslip screenshots with browser-based OCR.
- Provides an editable import-review screen before saving a detected bet.
- Detects event, league, market, odds, stake, event date, status, result, payout, bookmaker, timing, and strategy tags.
- Converts VND stakes to units using a configurable unit value; the default is 500,000 VND.
- Calculates win, half-win, loss, half-loss, void, pending exposure, and total net P/L.
- Tracks starting bankroll, deposits, withdrawals, current balance, available balance, and an optional bankroll goal.
- Displays cumulative profit and bankroll curves plus breakdowns by sport, odds range, market, timing, bookmaker, and strategy tag.
- Provides weekly and monthly reports, a settled-results calendar, and period comparisons.
- Includes configurable warnings for maximum stake, pending exposure, and daily settled loss.
- Detects possible duplicate entries before saving.
- Supports manual add, edit, delete, bulk actions, and one-click settlement.
- Saves data locally using `localStorage`.
- Synchronizes confirmed ChatGPT-tracked entries from `ledger.json` while preserving local edits.
- Exports full JSON backups and detailed CSV files.
- Installs as a Progressive Web App and caches the application shell for offline access.

## Data model and synchronization

`ledger.json` is the canonical feed for entries added or updated through ChatGPT. An official wager should only be written to the ledger after placement is confirmed.

For each synchronized change:

1. Add or update the bet using a stable `syncId`.
2. Update the top-level `version` timestamp.
3. Commit the file to `main`.
4. Allow GitHub Pages to deploy the updated feed.

The browser checks for updates while the page is open and refreshes when the tab regains focus or connectivity returns.

## Bankroll and guardrails

Current bankroll is calculated from:

`starting bankroll + deposits - withdrawals + settled betting P/L`

Guardrails are warnings rather than automatic blocks. Limits can be configured for:

- maximum stake per pending bet, measured in units
- maximum total pending exposure as a percentage of current bankroll
- maximum daily settled loss, measured in units

## Backup and restore

The Settings page exports a versioned SlipTrace JSON backup containing:

- bets and betting metadata
- unit size, starting bankroll, bankroll goal, and risk settings
- deposits and withdrawals
- theme preference
- locally hidden synchronized bet IDs

Imports support current backups, older `{ settings, bets }` backups, and legacy backups containing only a bets array. Existing browser storage keys remain compatible with previous EdgeLog builds so current users do not lose local data during the rebrand.

## Privacy

Manual entries, edits, settings, bankroll values, cash-ledger entries, table preferences, and risk limits remain in browser `localStorage` unless exported.

Entries intentionally synchronized through ChatGPT are stored in the public repository's `ledger.json`. Do not place private account details, personal identifiers, or sportsbook credentials in synchronized notes.

## Brand

- Product name: **SlipTrace**
- Tagline: **Track every slip.**
- Primary colors: violet, electric blue, and cyan on a deep navy foundation
- Sidebar symbol: `assets/sliptrace-mark.svg`
- App icon: `assets/sliptrace-app-icon.svg`
- Horizontal lockup: `assets/sliptrace-horizontal-dark.svg`
- Brand guide: `brand/SLIPTRACE-BRAND-GUIDE.md`

## Repository and GitHub Pages

- Repository: `https://github.com/acchtt/SlipTrace`
- Live site: `https://acchtt.github.io/SlipTrace/`

The repository slug, displayed product, and installed PWA all use the SlipTrace name.

## Supported Vietnamese labels

The parser recognizes common labels including:

- `Tỷ lệ cược`
- `Loại cược`
- `Sự kiện`
- `Ngày sự kiện`
- `Giải đấu`
- `Tiền cược`
- `Tiền trả về`
- `Trạng thái`
- `Kết quả`

The **thousands of VND** switch is enabled by default, so a displayed stake of `773.00 VND` is interpreted as `773,000 VND`.
