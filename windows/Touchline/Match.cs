using System.Text.Json;
namespace Touchline;

public record Match(long Id, string Home, string Away, string League, int? HomeScore,
    int? AwayScore, string Status, string Period, int? Minute, string Penalties)
{
    public bool Finished => Status is "finished" or "aet" or "ft" || Period is "ft" or "finished";
    public string Clock => Finished ? "FT" : Status == "halftime" || Period == "halftime" ? "HT" : Minute is int m ? $"{m}′" : Status;
    public string Score => $"{HomeScore?.ToString() ?? "—"} – {AwayScore?.ToString() ?? "—"}";
    public static string Text(JsonElement e, string key) => e.TryGetProperty(key, out var v) && v.ValueKind == JsonValueKind.String ? v.GetString()! : "";
    public static int? Number(JsonElement e, string key) => e.ValueKind == JsonValueKind.Object && e.TryGetProperty(key, out var v) && v.TryGetInt32Safe(out int n) ? n : null;
    public static Match Parse(JsonElement e)
    {
        long id = e.GetProperty("id").GetInt64();
        if (id <= 0) throw new JsonException("Invalid match ID");
        int? Total(string side) => Number(e, side + "_score") is int n
            ? n + (e.TryGetProperty("extra_time_score", out var extra) ? Number(extra, side) ?? 0 : 0) : null;
        string pens = e.TryGetProperty("penalty_shootout", out var p) && p.ValueKind == JsonValueKind.Object
            ? $"Pens {Number(p, "home")?.ToString() ?? "—"} – {Number(p, "away")?.ToString() ?? "—"}" : "";
        return new(id, Text(e,"home_team"), Text(e,"away_team"), Text(e,"league_name"), Total("home"), Total("away"), Text(e,"status").ToLowerInvariant(), Text(e,"period").ToLowerInvariant(), Number(e,"current_minute"), pens);
    }
    public static Match[] List(JsonElement root)
    {
        if (root.ValueKind == JsonValueKind.Object)
            foreach (var key in new[] { "events", "results", "data" })
                if (root.TryGetProperty(key, out var list) && list.ValueKind == JsonValueKind.Array) return list.EnumerateArray().Select(Parse).ToArray();
        if (root.ValueKind != JsonValueKind.Array) throw new JsonException("Unexpected match list");
        return root.EnumerateArray().Select(Parse).ToArray();
    }
    public static string? Change(Match? old, Match next)
    {
        if (old is null) return null; // A first snapshot is never a goal alert.
        var changes = new List<string>();
        if (old.HomeScore is int h && old.AwayScore is int a && next.HomeScore is int nh && next.AwayScore is int na && (h != nh || a != na))
            changes.Add(nh < h || na < a ? "Score correction" : "Goal / score update");
        if (!old.Finished && next.Finished) changes.Add("Full time");
        if (old.Clock != "HT" && next.Clock == "HT") changes.Add("Half time");
        if (old.Penalties != next.Penalties && next.Penalties.Length > 0) changes.Add("Shootout update");
        return changes.Count == 0 ? null : string.Join(" · ", changes);
    }
}
static class JsonNumbers
{
    public static bool TryGetInt32Safe(this JsonElement e, out int value) { value = 0; return e.ValueKind == JsonValueKind.Number && e.TryGetInt32(out value); }
}
