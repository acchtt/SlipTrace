# Touchline for Windows

Native Windows Forms app for Windows 10/11 x64. No browser engine, web server or AI service. The portable build includes .NET so users do not need to install a runtime.

## Download and use

Download `Touchline-Windows-x64` from a successful **Touchline Windows** GitHub Actions run, extract the ZIP, then run `Touchline.exe`. Builds are unsigned. GitHub requires signing in to download workflow artifacts.

1. Enter your BSD key and click **Connect BSD**. The key is kept in memory and sent only to BSD in the Authorization header; enter it again after restarting.
2. Check a match to follow it. Followed IDs are saved under `%LOCALAPPDATA%/Touchline/followed.json`.
3. Goals/score updates, score corrections, half time, full time and shootout updates trigger Windows tray notifications for followed matches. The first snapshot does not trigger alerts.
4. Closing the window hides it to the tray and keeps updates running. Use **App → Exit** or the tray's **Exit** to stop it. It does not auto-start with Windows.
5. Use **Notifications → Test notification** to check Windows notification settings. Windows Do Not Disturb and notification preferences can suppress banners. Notification history in the app retains the latest 200 alerts during the session, including muted alerts.

## Performance and scope

Uses one asynchronous request loop and a persistent HTTP connection, with no overlapping polling. The compact BSD live endpoint is polled every 10 seconds even while hidden. Changed cells are updated in place. Failed requests retain scores and back off; HTTP 429 respects Retry-After. Actual speed depends on BSD's feed/cache and your connection; RAM and latency have not yet been measured on Windows.

This first native version uses REST, not WebSocket push. It displays live matches and retains followed matches through completion. Fixtures, lineup/statistics views and push remain available in the existing web app, but are not yet ported here. The web app remains intact.

A missing followed match is resolved through its detail endpoint; absence is never taken as proof of full time. If refresh fails, the status bar identifies the last complete update. Notifications report observed changes, not every incident during an outage.

## Build and check

With .NET 10 SDK on Windows:

```
dotnet run --project windows/Touchline.Tests -c Release
dotnet publish windows/Touchline -c Release -r win-x64 --self-contained true -p:PublishSingleFile=true -p:IncludeNativeLibrariesForSelfExtract=true -o dist/Touchline
```

The GitHub workflow runs transition checks and produces the portable executable. A real Windows smoke test is still required: connect with a valid key, follow a match, minimize and close to tray, test notifications, mute, reconnect after network loss, and exit from the tray. No BSD credentials are embedded in builds or tests.

BSD reference: https://goaldir.com/docs/football/events/
Windows tray reference: https://learn.microsoft.com/en-us/dotnet/desktop/winforms/controls/notifyicon-component-overview-windows-forms
