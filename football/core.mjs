export const GRADES = ['A1', 'A2', 'B+', 'B', 'PASS'];
export function requireValue(condition, message) { if (!condition) throw new Error(message); }
export const normalize = value => String(value ?? '').normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();
const plain = value => String(value ?? '').replace(/\*\*|__/g, '').trim();

export function kickoffISO(value, date) {
  value = plain(value).replace(/\s*(ICT|UTC\+7)\s*/ig, '').trim();
  if (/^\d{1,2}:\d{2}$/.test(value)) {
    requireValue(/^\d{4}-\d{2}-\d{2}$/.test(date || ''), 'Choose the ICT slate date for time-only kickoffs.');
    value = `${date}T${value.padStart(5, '0')}:00+07:00`;
  }
  requireValue(/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(:\d{2}(\.\d+)?)?(Z|[+-]\d{2}:\d{2})$/.test(value) && Number.isFinite(Date.parse(value)), 'Kickoff must be HH:MM (ICT) or an ISO timestamp with timezone.');
  return new Date(value).toISOString();
}

export function validateMatches(matches, date) {
  requireValue(Array.isArray(matches) && matches.length > 0 && matches.length <= 30, 'Import between 1 and 30 ranked matches.');
  const ranks = new Set(), identities = new Set();
  return matches.map((item, index) => {
    const rank = Number(item.rank), home = plain(item.home), away = plain(item.away);
    const grade = plain(item.grade).toUpperCase().replace('B / PASS', 'B');
    requireValue(Number.isInteger(rank) && rank > 0 && !ranks.has(rank), `Row ${index + 1}: use a unique positive rank.`);
    requireValue(home && away && normalize(home) !== normalize(away), `Row ${index + 1}: provide both different team names.`);
    requireValue(GRADES.includes(grade), `Row ${index + 1}: frozen grade must be A1, A2, B+, B or PASS.`);
    const kickoff = kickoffISO(item.kickoff, date);
    const key = `${normalize(home)}|${normalize(away)}|${kickoff}`;
    requireValue(!identities.has(key), `Row ${index + 1}: duplicate match.`);
    ranks.add(rank); identities.add(key);
    const match = {rank, home, away, kickoff, grade, competition: plain(item.competition), structuralType: plain(item.structuralType), evidence: plain(item.evidence)};
    requireValue(Object.values(match).every(v => typeof v !== 'string' || v.length <= 15000), 'A match field is too long.');
    return match;
  }).sort((a, b) => a.rank - b.rank);
}

export function parseBoard(text, date) {
  text = text.trim().replace(/^```(?:json|markdown)?\s*\n?/, '').replace(/\n?```$/, '');
  if (text.startsWith('{') || text.startsWith('[')) {
    const json = JSON.parse(text);
    return validateMatches(Array.isArray(json) ? json : json.matches, json.date || date);
  }
  const lines = text.split(/\r?\n/).filter(line => line.includes('|') || line.includes('\t'));
  requireValue(lines.length >= 2, 'Paste a Markdown table, a tab-separated table, or a JSON match list.');
  const split = row => row.includes('\t') ? row.split('\t').map(plain) : row.trim().replace(/^\||\|$/g, '').split(/(?<!\\)\|/).map(v => plain(v).replace(/\\\|/g, '|'));
  const headers = split(lines[0]).map(normalize);
  const aliases = {rank:['rank','#','stt'], kickoff:['ict kickoff','kickoff ict','kickoff','time','gio ict'], match:['match','fixture','tran dau'], home:['home','home team'], away:['away','away team'], grade:['frozen grade','grade','band'], competition:['competition','league','giai dau'], structuralType:['structural type','type'], evidence:['evidence','profile','notes','structural evidence']};
  const column = key => headers.findIndex(h => aliases[key].map(normalize).includes(h));
  requireValue(column('rank') >= 0 && column('kickoff') >= 0 && column('grade') >= 0, 'The table needs Rank, ICT kickoff and Frozen grade columns.');
  return validateMatches(lines.slice(1).filter(line => !/^\s*\|?\s*:?-{2,}/.test(line)).map(line => {
    const cells = split(line), get = key => cells[column(key)] || '';
    let home = get('home'), away = get('away');
    if (!home || !away) {
      const parts = get('match').split(/\s+(?:vs\.?|v\.?|–|—|-)\s+/i);
      requireValue(parts.length === 2, 'Separate teams with “vs”, or use Home and Away columns.');
      [home, away] = parts;
    }
    return {rank:get('rank'), kickoff:get('kickoff'), home, away, grade:get('grade'), competition:get('competition'), structuralType:get('structuralType'), evidence:get('evidence')};
  }), date);
}

export function competitionExclusion(league) {
  const name = normalize(league?.name), country = normalize(league?.country);
  if (!name) return 'Competition identity is unavailable.';
  if (/\bk league\b|\bkleague\b/.test(name)) return 'K League is excluded by the active model.';
  if (name === 'leagues cup') return null;
  if (/\bdfb pokal\b/.test(name) && /germany|deutschland/.test(country)) return null;
  if (country === 'england' && /\bcup\b|\bfa trophy\b|\bfa vase\b/.test(name)) return null;
  if (/\bcup\b|\bpokal\b|\bcopa\b|\bcoupe\b|champions league|europa league|conference league|libertadores|sudamericana|nations league/.test(name)) return 'This cup or international competition is outside the active model scope.';
  return null;
}

export function validateOffers(offers) {
  requireValue(Array.isArray(offers) && offers.length > 0 && offers.length <= 20, 'Review between 1 and 20 visible Over lines.');
  const lines = new Set();
  return offers.map(o => {
    requireValue(typeof o.line === 'number' && o.line > 0 && o.line <= 15 && Number.isInteger(o.line * 4), 'Asian totals must use quarter-goal increments.');
    requireValue(typeof o.odds === 'number' && o.odds > 1 && o.odds <= 100, 'Use decimal odds greater than 1.');
    requireValue(!lines.has(o.line), 'Keep one reviewed price for each line.'); lines.add(o.line);
    return {line:o.line, odds:o.odds};
  });
}

export function settlement(line, goals) {
  const quarter = Math.round(line * 4);
  const halves = quarter % 2 ? [line - .25, line + .25] : [line, line];
  const result = halves.reduce((n, x) => n + Math.sign(goals - x), 0) / 2;
  return ({1:'WIN', '0.5':'HALF WIN', 0:'PUSH', '-0.5':'HALF LOSS', '-1':'LOSS'})[String(result)];
}
export function protection(line) {
  const boundary = line % 1 === .75 ? Math.ceil(line) : Math.floor(line);
  return `${Math.floor(line) + (line % 1 === .75 ? 2 : 1)}+ goals: full win; exactly ${boundary}: ${settlement(line, boundary).toLowerCase()}. 90 minutes + stoppage time.`;
}

export function profileFromEvents(events, teamId, cutoff) {
  const rows = events.filter(e => ['finished','aet','penalties'].includes(e.status) && Date.parse(e.event_date) < Date.parse(cutoff) && Number.isInteger(e.home_score) && Number.isInteger(e.away_score) && [e.home_team_id,e.away_team_id].includes(teamId)).sort((a,b) => Date.parse(b.event_date)-Date.parse(a.event_date));
  const summarize = list => list.length ? {
    matches:list.length, gf:list.reduce((s,e)=>s+(e.home_team_id===teamId?e.home_score:e.away_score),0), ga:list.reduce((s,e)=>s+(e.home_team_id===teamId?e.away_score:e.home_score),0),
    scored2:list.filter(e=>(e.home_team_id===teamId?e.home_score:e.away_score)>=2).length, scored3:list.filter(e=>(e.home_team_id===teamId?e.home_score:e.away_score)>=3).length,
    conceded2:list.filter(e=>(e.home_team_id===teamId?e.away_score:e.home_score)>=2).length, conceded3:list.filter(e=>(e.home_team_id===teamId?e.away_score:e.home_score)>=3).length,
    cleanSheets:list.filter(e=>(e.home_team_id===teamId?e.away_score:e.home_score)===0).length
  } : null;
  return {sample:summarize(rows), recent10:summarize(rows.slice(0,10)), home:summarize(rows.filter(e=>e.home_team_id===teamId)), away:summarize(rows.filter(e=>e.away_team_id===teamId)), recentEventIds:rows.slice(0,3).map(e=>e.id)};
}

export function confirmedXI(lineups, event) {
  return lineups?.lineup_status === 'confirmed' && ['home','away'].every(side => {
    const team = lineups.lineups?.[side];
    return team?.team_id === event[`${side}_team_id`] && team.players?.length === 11 && team.players.every(p=>typeof p.name === 'string' && p.name.trim()) && new Set(team.players.map(p=>p.id ?? normalize(p.name))).size === 11;
  });
}
