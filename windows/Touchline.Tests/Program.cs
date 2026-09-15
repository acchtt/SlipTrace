using System.Text.Json;
using Touchline;
int count = 0;
void Check(bool ok, string name) { if (!ok) throw new Exception(name); Console.WriteLine("PASS " + name); count++; }
Match Read(string json) { using var d = JsonDocument.Parse(json); return Match.Parse(d.RootElement); }
var first = Read("""{"id":1,"home_team":"A","away_team":"B","status":"live","home_score":0,"away_score":0}""");
Check(Match.Change(null, first) is null, "First snapshot is silent");
Check(Match.Change(first, first) is null, "Identical snapshot is silent");
var goal = first with { HomeScore = 1 };
Check(Match.Change(first, goal) == "Goal / score update", "Goal detected");
Check(Match.Change(goal, first) == "Score correction", "Goal correction detected");
Check(Match.Change(first, first with { Status = "finished" }) == "Full time", "Confirmed full time");
Check(Match.Change(first, first with { Period = "halftime" }) == "Half time", "Half time");
Check(Match.Change(first with { HomeScore = null }, goal) is null, "Unknown score creates no goal alert");
var extra = Read("""{"id":1,"home_score":1,"away_score":1,"extra_time_score":{"home":2,"away":0},"penalty_shootout":{"home":4,"away":3}}""");
Check(extra.HomeScore == 3 && extra.AwayScore == 1, "Extra time added once");
Check(extra.Penalties == "Pens 4 – 3", "Shootout kept separate");
using (var list = JsonDocument.Parse("""{"results":[{"id":1,"home_score":null,"away_score":null}]}""")) Check(Match.List(list.RootElement)[0].Score == "— – —", "Null scores and list envelope");
Check(Match.Change(goal, goal with { HomeScore = 2, Status = "finished" }) == "Goal / score update · Full time", "Final goal and full time combined");
Console.WriteLine($"{count} checks passed.");
