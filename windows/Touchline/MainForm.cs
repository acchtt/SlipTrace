using System.Net;
using System.Net.Http.Headers;
using System.Text.Json;
namespace Touchline;

public sealed class MainForm : Form
{
    readonly HttpClient http = new(new HttpClientHandler { AllowAutoRedirect = false }) { BaseAddress = new Uri("https://sports.bzzoiro.com/api/v2/"), Timeout = TimeSpan.FromSeconds(15) };
    readonly CancellationTokenSource stop = new();
    readonly System.Windows.Forms.Timer timer = new() { Interval = 10000 };
    readonly NotifyIcon tray = new() { Icon = SystemIcons.Application, Text = "Touchline live scores", Visible = true };
    readonly TextBox key = new() { Width = 280, UseSystemPasswordChar = true, PlaceholderText = "BSD API key (kept in memory)" };
    readonly TextBox search = new() { Width = 220, PlaceholderText = "Search teams or leagues" };
    readonly CheckBox mute = new() { Text = "Mute alerts", AutoSize = true };
    readonly CheckBox onlyFollowed = new() { Text = "Followed only", AutoSize = true };
    readonly Label status = new() { Dock = DockStyle.Bottom, Height = 34, TextAlign = ContentAlignment.MiddleLeft, Text = "Connect BSD to load live matches. Check a match to follow it." };
    readonly ListView board = new() { Dock = DockStyle.Fill, View = View.Details, CheckBoxes = true, FullRowSelect = true, HideSelection = false };
    readonly ListBox history = new() { Dock = DockStyle.Fill, IntegralHeight = false };
    readonly Dictionary<long, Match> matches = new();
    readonly Dictionary<long, ListViewItem> items = new();
    readonly HashSet<long> followed = new();
    readonly string settings = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData), "Touchline", "followed.json");
    bool busy, connected, exiting, painting;
    int failures;
    DateTimeOffset lastSuccess;
    public MainForm()
    {
        Text = "Touchline — live football"; ClientSize = new Size(1000, 650); MinimumSize = new Size(760, 460);
        Font = new Font("Segoe UI", 10); BackColor = Color.FromArgb(245, 247, 249);
        var menu = new MenuStrip();
        var file = new ToolStripMenuItem("App");
        file.DropDownItems.Add("Hide to tray", null, (_, _) => Hide());
        file.DropDownItems.Add("Exit", null, (_, _) => Quit());
        var notifications = new ToolStripMenuItem("Notifications");
        notifications.DropDownItems.Add("Test notification", null, (_, _) => Alert("Test notification", "Touchline notifications are working."));
        notifications.DropDownItems.Add("Mute / unmute", null, (_, _) => mute.Checked = !mute.Checked);
        menu.Items.AddRange([file, notifications]); MainMenuStrip = menu;
        var controls = new FlowLayoutPanel { Dock = DockStyle.Top, Height = 90, Padding = new Padding(10), WrapContents = true };
        var connect = new Button { Text = "Connect BSD", AutoSize = true };
        var refresh = new Button { Text = "Refresh", AutoSize = true };
        connect.Click += async (_, _) => {
            if (busy) return;
            string token = key.Text.Trim();
            if (string.IsNullOrWhiteSpace(token) || token.Any(char.IsWhiteSpace)) { status.Text = "Enter a valid BSD key."; return; }
            http.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Token", token);
            key.Clear(); matches.Clear(); failures = 0; connected = true;
            timer.Stop(); await RefreshScores(); timer.Start();
        };
        refresh.Click += async (_, _) => { if (failures == 0) await RefreshScores(); };
        controls.Controls.AddRange([key, connect, refresh, search, onlyFollowed, mute]);
        foreach (var (title, width) in new[] { ("Follow / League", 200), ("Home", 230), ("Score", 90), ("Away", 230), ("Time", 90), ("Shootout", 130) }) board.Columns.Add(title, width);
        board.ItemChecked += (_, e) => {
            if (painting || e.Item.Tag is not long id) return;
            if (e.Item.Checked) followed.Add(id); else followed.Remove(id);
            SaveFollows(); BeginInvoke((Action)PaintScores);
        };
        search.TextChanged += (_, _) => PaintScores(); onlyFollowed.CheckedChanged += (_, _) => PaintScores();
        var tabs = new TabControl { Dock = DockStyle.Fill };
        var scoresTab = new TabPage("Live scores"); scoresTab.Controls.Add(board);
        var historyTab = new TabPage("Notification history"); historyTab.Controls.Add(history);
        tabs.TabPages.AddRange([scoresTab, historyTab]);
        Controls.Add(tabs); Controls.Add(controls); Controls.Add(menu); Controls.Add(status);
        var trayMenu = new ContextMenuStrip();
        trayMenu.Items.Add("Open Touchline", null, (_, _) => Restore());
        trayMenu.Items.Add("Mute / unmute", null, (_, _) => mute.Checked = !mute.Checked);
        trayMenu.Items.Add("Exit", null, (_, _) => Quit());
        tray.ContextMenuStrip = trayMenu; tray.DoubleClick += (_, _) => Restore(); tray.BalloonTipClicked += (_, _) => Restore();
        timer.Tick += async (_, _) => await RefreshScores();
        FormClosing += (_, e) => { if (!exiting && e.CloseReason == CloseReason.UserClosing) { e.Cancel = true; Hide(); } };
        FormClosed += (_, _) => { stop.Cancel(); timer.Dispose(); tray.Dispose(); http.Dispose(); };
        try { if (File.Exists(settings)) followed.UnionWith(JsonSerializer.Deserialize<long[]>(File.ReadAllText(settings)) ?? []); } catch (Exception ex) when (ex is IOException or JsonException or UnauthorizedAccessException) { status.Text = "Could not read saved follows. You can follow matches again."; }
    }
    void Restore() { Show(); WindowState = FormWindowState.Normal; Activate(); }
    void Quit() { exiting = true; Close(); }
    void SaveFollows()
    {
        try { Directory.CreateDirectory(Path.GetDirectoryName(settings)!); File.WriteAllText(settings + ".tmp", JsonSerializer.Serialize(followed)); File.Move(settings + ".tmp", settings, true); }
        catch (Exception ex) when (ex is IOException or UnauthorizedAccessException) { status.Text = "Follows work this session but could not be saved."; }
    }
    async Task<JsonDocument> Get(string path)
    {
        using var response = await http.GetAsync(path, stop.Token);
        if (response.StatusCode == HttpStatusCode.TooManyRequests)
        {
            var retry = response.Headers.RetryAfter;
            var seconds = retry?.Delta?.TotalSeconds ?? (retry?.Date - DateTimeOffset.UtcNow)?.TotalSeconds ?? 60;
            timer.Interval = (int)Math.Clamp(seconds * 1000, 10000, int.MaxValue);
            throw new HttpRequestException("Rate limited", null, response.StatusCode);
        }
        response.EnsureSuccessStatusCode();
        return JsonDocument.Parse(await response.Content.ReadAsStringAsync(stop.Token));
    }
    async Task RefreshScores()
    {
        if (busy || !connected || stop.IsCancellationRequested) return;
        busy = true; timer.Stop();
        try
        {
            using var doc = await Get("events/live/");
            var current = Match.List(doc.RootElement);
            var present = current.Select(m => m.Id).ToHashSet();
            foreach (var match in current) UpdateMatch(match);
            // Disappearance is not full time. Resolve followed matches with the detail endpoint.
            foreach (long id in matches.Keys.Where(id => !present.Contains(id)).ToArray())
            {
                if (!followed.Contains(id)) { matches.Remove(id); continue; }
                if (matches[id].Finished) continue;
                using var detail = await Get($"events/{id}/");
                var resolved = Match.Parse(detail.RootElement);
                if (resolved.Id != id) throw new JsonException("Mismatched detail ID");
                UpdateMatch(resolved);
            }
            lastSuccess = DateTimeOffset.Now; failures = 0; timer.Interval = 10000;
            status.Text = $"Received {lastSuccess:HH:mm:ss} · {current.Length} live · {followed.Count} followed · Refresh every 10 seconds · Close hides to tray";
            PaintScores();
        }
        catch (OperationCanceledException) when (stop.IsCancellationRequested) { }
        catch (Exception ex) when (ex is HttpRequestException or JsonException or OperationCanceledException or InvalidOperationException or KeyNotFoundException or FormatException)
        {
            failures++;
            if (ex is HttpRequestException { StatusCode: HttpStatusCode.Unauthorized or HttpStatusCode.Forbidden })
            { connected = false; status.Text = "BSD rejected access. Check your key and account, then connect again."; }
            else
            {
                if (ex is not HttpRequestException { StatusCode: HttpStatusCode.TooManyRequests }) timer.Interval = Math.Min(120000, 10000 * (1 << Math.Min(failures, 3)));
                status.Text = $"Feed unavailable · Last complete update: {(lastSuccess == default ? "none" : lastSuccess.ToString("HH:mm:ss"))} · Retry in {timer.Interval / 1000}s";
            }
            PaintScores();
        }
        finally { busy = false; if (connected && !stop.IsCancellationRequested) timer.Start(); }
    }
    void UpdateMatch(Match match)
    {
        matches.TryGetValue(match.Id, out var old);
        string? change = Match.Change(old, match);
        matches[match.Id] = match;
        if (followed.Contains(match.Id) && change is not null)
            Alert(change, $"{match.Home} {match.Score} {match.Away} · {match.Clock} {match.Penalties}");
    }
    void Alert(string title, string body)
    {
        history.Items.Insert(0, $"{DateTime.Now:HH:mm:ss}  {title} — {body}");
        while (history.Items.Count > 200) history.Items.RemoveAt(200);
        if (!mute.Checked) tray.ShowBalloonTip(5000, title, body.Length > 250 ? body[..250] : body, ToolTipIcon.Info);
    }
    void PaintScores()
    {
        if (IsDisposed) return;
        painting = true; board.BeginUpdate();
        try
        {
            var visible = matches.Values.Where(m => (!onlyFollowed.Checked || followed.Contains(m.Id)) &&
                $"{m.Home} {m.Away} {m.League}".Contains(search.Text.Trim(), StringComparison.OrdinalIgnoreCase)).OrderByDescending(m => followed.Contains(m.Id)).ThenBy(m => m.League).ThenBy(m => m.Id).ToArray();
            var ids = visible.Select(m => m.Id).ToHashSet();
            foreach (long id in items.Keys.Where(id => !ids.Contains(id)).ToArray()) { board.Items.Remove(items[id]); items.Remove(id); }
            foreach (var m in visible)
            {
                string[] cells = [m.League, m.Home, m.Score, m.Away, m.Clock, m.Penalties];
                if (!items.TryGetValue(m.Id, out var row)) { row = new ListViewItem(cells) { Tag = m.Id }; items[m.Id] = row; board.Items.Add(row); }
                else for (int i = 0; i < cells.Length; i++) if (row.SubItems[i].Text != cells[i]) row.SubItems[i].Text = cells[i];
                row.Checked = followed.Contains(m.Id);
            }
        }
        finally { board.EndUpdate(); painting = false; }
    }
}
