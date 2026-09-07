# Touchline — football live scores

Replaces the former football-analysis workspace at the same GitHub Pages route, `/SlipTrace/football/`. The old image-reading/model-evaluation app and its undeployed Worker were removed. Repository model documents and the existing SlipTrace journal remain separate and unchanged.

## Use

Open the site, choose **Connect BSD**, and enter your BSD API key. It is sent directly to `sports.bzzoiro.com` in the Authorization header and kept only in JavaScript memory. Re-enter it after a page reload. No OpenAI/Gemini account, Airtable token, database, or Cloudflare deployment is needed.

BSD's preflight response was checked for the actual GitHub Pages origin `https://acchtt.github.io`: it permits cross-origin GET requests and the Authorization header. End-to-end authenticated feed delivery still requires a valid user key; no production key was available during implementation.

This is a personal bring-your-own-key app. Never commit your BSD key to the repository or place it in a URL. Publicly visible code contains no shared credentials.

## Speed choices

- No framework, package dependencies, external fonts, badge-image requests, AI calls or application backend in the critical path.
- The initial connected request uses BSD's compact `/api/v2/events/live/` endpoint. It already includes league/team names, scores and clocks.
- REST refreshes every 10 seconds with no overlapping live-feed requests. BSD documents its own approximately 10–30-second server cache, so faster polling cannot guarantee fresher scores.
- Optional WebSocket push uses BSD's token subprotocol, keeping the key out of URL logs. It subscribes to at most 10 covered live matches, prioritizing the open match and pins. Other matches continue via REST. Subscription failures and unavailable add-ons fall back to REST without purchasing anything.
- Socket heartbeat, reconnect/resubscribe and offline handling are included. Hidden tabs stop scheduling polls and close their socket; foregrounding reconnects and refreshes.
- Score rows are keyed by event ID. Only changed text is written, rows are reused, and updates are batched per animation frame. Offscreen league groups use `content-visibility`.
- The last score snapshot and pinned IDs are stored locally for immediate display on reopening. A saved snapshot is labelled explicitly; no API key is stored. This is not an offline-installable PWA.
- Full-date fixtures are requested only when selecting All matches/Finished; 200-row pages are displayed progressively. Missing league labels are fetched afterwards. Dates use Asia/Ho_Chi_Minh boundaries.
- Lineups/statistics are lazy-loaded only when opened, with a 30-second in-memory detail cache and cancellation on navigation.
- Errors retain the last scores. Rate-limit responses slow polling instead of spinning.

## Score semantics

REST regulation scores and extra-time goals are combined for the displayed match total; shootout scores are displayed separately. Missing values are shown as dashes. Predicted lineups are identified as predicted.

WebSocket event frames supply authoritative display scores. Only final `goal` and `deleted_event` action scores are applied; provisional `temp_goal` and history replays do not increment the score. Late REST snapshots cannot immediately roll back a newer push. A match disappearing from the live feed triggers a detail refresh and displays CHECK until its status is resolved; disappearance is never assumed to mean full time.

No client-side clock is fabricated between provider updates. “Received” means the local receipt time, not guaranteed stadium event time. The interface does not promise a latency BSD cannot provide. Push entitlement and coverage are provider-dependent.

## Verification

```sh
node --test football/tests/core.test.mjs
node --check football/app.mjs
```

Tests use documented sample payloads, including corrections, null scores, extra time, timezone boundaries, REST-vs-push ordering, and the 10-subscription cap. Live key validation and actual network latency need a valid BSD account. Deploy using the repository's existing GitHub Pages workflow.

Sources: [live REST feed](https://goaldir.com/docs/football/events/), [WebSocket connection/authentication](https://goaldir.com/docs/websocket/), [football frames](https://goaldir.com/docs/websocket/football/).
