# Football workspace

The interface is served by **GitHub Pages** at `/SlipTrace/football/`. A separate Cloudflare Worker handles private API calls and D1 stores immutable board freezes, evidence and assessments. No Sites service is used.

## Deployment status and prerequisites

The source is complete enough to configure and test; it is **not connected to live services merely by publishing the HTML**. Deploy the Worker, create its D1 database and configure secrets before live lineup retrieval or image analysis can run. Integration tests use mocked provider responses and real SQLite; they do not establish live BSD coverage, AI quality or Airtable account access.

Required server secrets:

| Secret | Purpose |
| --- | --- |
| `BSD_API_KEY` | Bzzoiro Sports Data football v2 API token |
| `OPENAI_API_KEY` | Image extraction and application of the written football rules; API usage is billed by OpenAI |
| `APP_TOKEN` | A private random access key of at least 32 characters for this personal workspace |
| `AIRTABLE_TOKEN` | Personal access token with record read/write access to the model's Decision States base; required for official locks |

The browser receives only `APP_TOKEN`, entered by the owner each session. It never receives the three provider tokens. It remembers only the backend URL. This is a **single-owner application**, not a multi-user service. Anyone holding its access key can read its boards and spend its API quota. CORS is not the authentication mechanism; every private endpoint verifies the bearer key.

## Deploy the backend

Run these commands from `football-api/` on a machine authenticated to your Cloudflare account:

```sh
npx wrangler@4 login
npx wrangler@4 d1 create sliptrace-football
```

Replace `REPLACE_WITH_CREATED_D1_DATABASE_ID` in `wrangler.jsonc` with the returned ID. Keep the binding name `DB`. Then:

```sh
npx wrangler@4 d1 migrations apply sliptrace-football --remote
npx wrangler@4 secret put BSD_API_KEY
npx wrangler@4 secret put OPENAI_API_KEY
npx wrangler@4 secret put APP_TOKEN
npx wrangler@4 secret put AIRTABLE_TOKEN
npx wrangler@4 deploy
```

Each secret command prompts privately. Never paste provider keys into repository files, GitHub Pages JavaScript, a chat table or an issue. A template with empty values is included as `.dev.vars.example`. Local `.dev.vars` is ignored by git.

`OPENAI_MODEL` is configurable; the initial value is `gpt-5.4-mini`, which supports image input and structured responses. Verify that the deployment account can use it. Evaluate real extraction and decision examples before relying on a different model.

The allowed browser origin is `https://acchtt.github.io` (an origin has no `/SlipTrace` path). Change it for a custom domain. For local development, temporarily set it to the exact local frontend origin and use local D1 migrations with `wrangler dev`.

In the website choose **Connect workspace**, enter the deployed Worker URL and the owner access key, then check that BSD, AI, database and audit are configured. A missing audit connection allows evidence collection and HOLD assessments but does not issue official locks.

## GitHub Pages

The existing repository workflow `.github/workflows/pages.yml` deploys the repository on pushes to `main`. The new frontend requires no bundler and uses relative asset paths, including the shared module `football/core.mjs`. Keep `football/` and the existing `assets/` directory in the Pages artifact.

Cloudflare hosts only the private API and database. It does not replace GitHub Pages as the website host.

## Receive a ranked table from ChatGPT

### Ordinary chat: paste or import

Ask ChatGPT for this format:

```text
| Rank | ICT kickoff | Match | Frozen grade | Structural type | Competition |
| --- | --- | --- | --- | --- | --- |
| 1 | 20:00 | Home FC vs Away FC | A2 | Two-Sided | League name |
```

The row above is a formatting example, not a real fixture or recommendation. Choose the correct ICT slate date. ISO kickoffs must include a timezone. Include the supporting structural analysis in the expandable context box: scoring profiles, sources and timestamps, carrier routes, expected personnel and failure modes. A ranked table alone is not proof that the model's evidence requirements are met.

Use separate Home and Away columns for team names containing ambiguous match separators. JSON supports `title`, `context`, `date` and `matches`; each match has `rank`, `home`, `away`, `kickoff`, `grade`, `competition`, `structuralType` and `evidence`. Optional descriptive fields can be blank; missing material evidence leads to HOLD.

### Direct handoff: a configured Custom GPT action

An ordinary chat is not automatically connected to this website. `chatgpt-action.openapi.json` supplies a narrowly scoped action that creates a frozen board and reads it back. Replace its example server URL with the deployed Worker URL, import the schema into a Custom GPT, and configure API-key authentication with Bearer `APP_TOKEN` in the GPT's private action settings. Do not publish a GPT that contains your personal workspace key.

Tell the GPT to send the user's reviewed ranked table and supporting analysis to `createRankedFootballBoard`. It must preserve ranks/grades and use explicit kickoff timezones. The action freezes a board; it does not authorize a wager. The user refreshes the website's saved-board list or opens `/football/#board=<returned board ID>`. No background scraping of chats, chat-history access, or automatic ordinary-chat synchronization is implemented.

## Decision behavior

1. Table review is available without a backend. Freezing requires a connection and an upcoming kickoff. Server timestamps and the original ranking cannot be edited in place. A correction creates another board.
2. Search BSD fixtures, inspect the actual home/away teams and kickoff, then explicitly bind the right event. Manual event IDs receive the same identity-preview step. A match cannot later be rebound to another event.
3. Fetch lineups and historical GF/GA profiles from BSD. The documented `lineup_status` remains `confirmed`, `predicted` or `unavailable`; predicted XIs never become confirmed by inference. Player IDs/teams and both eleven-player sheets are checked. The team profile is labelled partial when a complete season cannot be established. Missing chance data stays missing.
4. Select up to three odds images. Images are sent to OpenAI via the Worker for extraction and are not written to D1 or Airtable. The extraction text is retained. Review identity, decimal prices, 90-minute market scope and the real screenshot capture time. Other periods or unclear scope require clearer screenshots.
5. Before evaluation the server fetches current BSD evidence again and loads the **pinned canonical model documents**, in their declared order. The LLM interprets a qualitative rules framework; this is not a trained numerical prediction model and no invented probability or EV formula is added.
6. Server checks enforce confirmed XI, competition exclusions, required profiles, prematch timing, exact reviewed line/price, normal XI-promotion limits and the narrow recent-total/leakage confirmation rule. The inactive Sep 1 hardening regime is not revived: no youth cap, A2 burden prohibition or O3.75 ban.
7. A current 15-minute image/price freshness limit is an application safeguard, **not an asserted statistical rule from the model**. It is rechecked after AI completes. This first implementation evaluates prematch only; live validation, manual live override, just-kicked grace and settlement are not exposed.
8. Every material freeze, lineup state and verdict is appended to D1 and queued for Airtable. Audit retries upsert the same Assessment ID. Earlier audit states must sync before an official selection. If delivery of the final lock is uncertain, the UI displays `AUDIT PENDING` and withholds the action until retry succeeds; it does not silently rerun or rewrite that assessment. Repeated requests for the same odds extraction return the existing decision.

An official lock is a **selection**, not confirmation that the user placed a bet. This application never submits wagers, updates `ledger.json`, changes official P/L, or modifies the existing journal data.

## Model revision

`model.mjs` embeds exactly the four canonical documents from commit `979c955667d63e913cb7eb2ecff915fc1f83920b`:

- `models/football/CURRENT_MODEL.md`
- `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.47-R.md`
- `models/football/procedures/FOOTBALL_BETTING_PROCEDURE.md`
- `models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md`

The version and commit are stored in each board and assessment. Rule updates require a reviewed backend revision, updating the embedded documents and UI source link together. Do not silently apply new rules to old boards. There is no auto-update from `main` at request time.

## Verification

From the repository root, with Node 24:

```sh
node --test football-api/tests/workflow.test.mjs
node --check football/app.mjs
node --check football-api/worker.mjs
```

The tests cover imports/timezones, Asian quarter-line protection, exclusions and named exceptions, profile filtering, authentication, wrong-match evidence, confirmed XI, stale images, non-full-match markets, unlisted AI selections, narrow chance-confirmation logic, audit failures and idempotent decisions. They execute the migration and Worker routes against an in-memory SQLite D1 adapter.

Before treating the live integration as verified, configure the deployment and exercise a covered upcoming fixture end-to-end with real credentials and a clear screenshot. Confirm the exact Airtable field types and token permissions. Unsupported leagues or incomplete evidence should remain HOLD, not synthetic success.

## References

- [BSD football events and lineups](https://goaldir.com/docs/football/events/)
- [BSD authentication](https://goaldir.com/docs/authentication/)
- [BSD OpenAPI schema](https://sports.bzzoiro.com/api/schema/)
- [OpenAI image inputs](https://developers.openai.com/api/docs/guides/images-vision)
- [OpenAI structured outputs](https://developers.openai.com/api/docs/guides/structured-outputs)
- [Cloudflare D1 setup](https://developers.cloudflare.com/d1/get-started/)
- [Cloudflare Worker secrets](https://developers.cloudflare.com/workers/configuration/secrets/)
