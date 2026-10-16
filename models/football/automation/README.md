# Football v2 — Free GitHub Actions control plane

This layer orchestrates deterministic Football v2 execution on GitHub-hosted
runners without calling any paid AI API.

## Authority split

- ChatGPT Work / GPT-6.1 Sol: fixture research, football evidence gathering,
  screenshot interpretation and structured Football C input preparation.
- Football C: sole football prediction authority.
- GitHub Actions: deterministic execution, validation, CI and artifact transport.
- Google Sheets: active operational persistence/readback authority.

GitHub Actions does **not** replace football research and does not infer missing
C evidence.

## Workflow

Use **Football v2 free control plane** in GitHub Actions.

Operations:

- `health`: run V4 stage tests, control-plane boundary tests, authority checks
  and the XI runtime self-check.
- `sweep`: execute native V4 sweep from a current source JSON.
- `rank`: execute native V4 rank from a frozen sweep/source plus current
  status refresh, Football C payload and explicit unranked reasons.
- `verify-rank`: verify a provided independent Google Sheets readback against
  the immutable rank receipt.
- `xi-self-check`: verify the thin Football C XI runtime only.

Every run uploads a `football-control-<run-id>` artifact containing
`summary.json` and, where applicable, the native V4 receipt.

No OpenAI/API secret is required.

## Request file

Non-health operations use a repository-relative JSON request:

```json
{
  "schema_version": "football-actions-control-v1",
  "operation": "rank",
  "paths": {
    "sweep": "path/to/V4-run-v4_sweep_ready.json",
    "source": "path/to/V4-run-source.json",
    "status_refresh": "path/to/status_refresh.json",
    "c": "path/to/c.json",
    "unranked": "path/to/unranked.json"
  }
}
```

All paths are bound to files inside the checked-out repository. Absolute paths,
missing files and repository traversal are rejected.

### Sweep request

```json
{
  "schema_version": "football-actions-control-v1",
  "operation": "sweep",
  "paths": {
    "source": "path/to/source.json"
  }
}
```

### Rank verification request

```json
{
  "schema_version": "football-actions-control-v1",
  "operation": "verify-rank",
  "paths": {
    "rank": "path/to/v4_rank.json",
    "readback": "path/to/google_sheets_readback.json"
  }
}
```

The readback must already be a **real independent Google Sheets refetch**.
This workflow does not manufacture or self-assert readback evidence.

## Recommended Work usage

Keep GPT-6.1 Sol as the normal Work executor.

1. `/sweep`: Work acquires/researches the source and prepares the source JSON.
2. GitHub Action `sweep`: native V4 validates and emits the immutable receipt.
3. `/rank`: Work researches the full eligible cohort and prepares C,
   status-refresh and unranked JSON.
4. GitHub Action `rank`: native V4 + Football C execute deterministically and
   emit the rank receipt.
5. Work writes/reads active Google Sheets through the connector.
6. GitHub Action `verify-rank`: verifies the independently fetched readback.
7. `/xi` and `/live`: continue using the verified C receipt and the thin
   Football C runtime.

This removes model switching from routine execution while keeping AI research
separate from deterministic model execution.
