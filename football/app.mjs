import {parseBoard,validateOffers,kickoffISO,protection} from './core.mjs';
const $ = selector => document.querySelector(selector);
const esc = value => String(value ?? '').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const ict = value => new Intl.DateTimeFormat('en-GB',{timeZone:'Asia/Ho_Chi_Minh',day:'2-digit',month:'short',hour:'2-digit',minute:'2-digit',hour12:false}).format(new Date(value));
const localICT = value => new Date(new Date(value).getTime()+7*3600000).toISOString().slice(0,16);
const state = {url:'',token:'',board:null,selected:null,draft:null,images:[],previewURLs:[],busy:false};
try {state.url=localStorage.getItem('sliptrace-football-api') || '';} catch {}
$('#slate-date').value=localICT(new Date()).slice(0,10); $('#api-url').value=state.url;
function notice(message,error=false) { const node=$('#notice');node.hidden=!message;node.textContent=message;node.classList.toggle('error',error); }
function current() {return state.board?.matches.find(m=>m.id===state.selected);}
function field(name) {return $(`[data-field="${name}"]`);}
function cleanupImages() {state.previewURLs.forEach(URL.revokeObjectURL);state.previewURLs=[];state.images=[];}
async function task(fn) {
  if(state.busy)return; state.busy=true;document.body.classList.add('busy');
  const buttons=[...document.querySelectorAll('button')].filter(b=>!b.disabled && !b.closest('dialog'));buttons.forEach(b=>b.disabled=true);
  try {await fn();} catch(error){notice(error.message,true);} finally {state.busy=false;document.body.classList.remove('busy');buttons.filter(b=>b.isConnected).forEach(b=>b.disabled=false);}
}
async function api(path,body) {
  if(!state.url || !state.token) throw new Error('Connect your private workspace first. Table review works without a connection.');
  let response;
  try {response=await fetch(state.url+path,{method:body===undefined?'GET':'POST',headers:{Authorization:`Bearer ${state.token}`,...(body===undefined?{}:{'Content-Type':'application/json'})},...(body===undefined?{}:{body:JSON.stringify(body)}),signal:AbortSignal.timeout(180000)});}
  catch {throw new Error('The workspace could not be reached. Check its URL and connection. If a verdict timed out, refresh the board before retrying.');}
  let result;try{result=await response.json();}catch{throw new Error('The backend did not return a readable response.');}
  if(!response.ok)throw new Error(result.error || `Request failed (${response.status}).`);return result;
}
function table(matches){return `<div class="table-wrap"><table><thead><tr><th>Rank</th><th>Kickoff · ICT</th><th>Match</th><th>Grade</th><th>Type</th></tr></thead><tbody>${matches.map(m=>`<tr><td>${m.rank}</td><td>${esc(ict(m.kickoff))}</td><td>${esc(m.home)} vs ${esc(m.away)}</td><td><span class="grade">${esc(m.grade)}</span></td><td>${esc(m.structuralType || 'Not supplied')}</td></tr>`).join('')}</tbody></table></div>`;}
function previewImport(){state.draft=parseBoard($('#table-input').value,$('#slate-date').value);$('#import-preview').innerHTML=table(state.draft)+`<p class="hint">Review the teams and date. Freezing saves the original ranks and grades permanently for this board.</p><button id="freeze-board" class="primary">Freeze ${state.draft.length} matches</button>`;$('#import-preview').hidden=false;notice('Review the parsed matches, then freeze the board.');}
$('#preview-import').addEventListener('click',()=>task(previewImport));
$('#table-input').addEventListener('input',()=>{state.draft=null;$('#import-preview').hidden=true;});
$('#slate-date').addEventListener('change',()=>{state.draft=null;$('#import-preview').hidden=true;});
$('#json-file').addEventListener('change',event=>task(async()=>{const file=event.target.files[0];if(!file)return;if(file.size>150000)throw new Error('The import file must be smaller than 150 KB.');const text=await file.text();$('#table-input').value=text;try{const parsed=JSON.parse(text);if(parsed.context)$('#context-input').value=String(parsed.context).slice(0,60000);if(parsed.title)$('#board-title').value=String(parsed.title).slice(0,120);}catch{}previewImport();}));
$('#template').addEventListener('click',()=>task(async()=>{const text='| Rank | ICT kickoff | Match | Frozen grade | Structural type | Competition |\n| --- | --- | --- | --- | --- | --- |\n| 1 | 20:00 | Home FC vs Away FC | A2 | Two-Sided | League name |';try{await navigator.clipboard.writeText(text);notice('Table format copied. Ask ChatGPT to use this format and include its supporting analysis.');}catch{$('#table-input').value=text;notice('The example format is in the import box. Replace its example teams with your shortlist.');}}));
$('#import-preview').addEventListener('click',event=>{if(event.target.id==='freeze-board')task(async()=>{
  if(!state.draft)throw new Error('Review the table again before freezing.');
  const board=await api('/boards',{matches:state.draft,title:$('#board-title').value || `${$('#slate-date').value} shortlist`,context:$('#context-input').value});
  state.board=board;state.selected=board.matches[0]?.id;location.hash=`board=${board.id}`;await loadBoards();renderBoard();$('#import-preview').hidden=true;notice('Shortlist frozen. Select each match to confirm its BSD fixture.');
});});

$('#connection-open').addEventListener('click',()=>$('#connection-dialog').showModal());
$('#connection-close').addEventListener('click',()=>$('#connection-dialog').close());
$('#connection-form').addEventListener('submit',async event=>{
  event.preventDefault();const button=event.submitter;button.disabled=true;$('#connection-error').textContent='';
  try {
    const url=new URL($('#api-url').value);if(url.username || url.password || url.search || url.hash || (url.protocol!=='https:' && !(['localhost','127.0.0.1'].includes(url.hostname) && url.protocol==='http:')))throw new Error('Use an HTTPS backend URL. HTTP is supported only for localhost.');
    state.url=url.href.replace(/\/$/,'');state.token=$('#access-key').value;
    if(state.token.length<32)throw new Error('The workspace access key must have at least 32 characters.');
    const health=await api('/health');await loadBoards();
    try{localStorage.setItem('sliptrace-football-api',state.url);}catch{}
    $('#connection-state').textContent='Connected';$('#connection-state').className='pill good';$('#connection-open').textContent='Connection';$('#connection-dialog').close();$('#access-key').value='';
    const missing=Object.entries(health.configured || {}).filter(([,v])=>!v).map(([k])=>k);
    notice(missing.length?`Connected. Backend setup still needed: ${missing.join(', ')}.`:'Workspace connected.');
    const boardId=new URLSearchParams(location.hash.slice(1)).get('board');if(boardId)await loadBoard(boardId);
  }catch(error){state.token='';$('#connection-state').textContent='Not connected';$('#connection-state').className='pill';$('#connection-error').textContent=error.message;}
  finally{button.disabled=false;}
});
$('#disconnect').addEventListener('click',()=>{state.token='';state.board=null;state.selected=null;$('#access-key').value='';$('#connection-state').textContent='Not connected';$('#connection-state').className='pill';$('#connection-open').textContent='Connect workspace';$('#board-select').innerHTML='<option value="">Saved boards</option>';cleanupImages();renderBoard();$('#connection-dialog').close();notice('Disconnected. Your saved boards remain on your private backend.');});
async function loadBoards(){const boards=await api('/boards');$('#board-select').innerHTML='<option value="">Saved boards</option>'+boards.map(b=>`<option value="${esc(b.id)}">${esc(b.title)}</option>`).join('');if(state.board)$('#board-select').value=state.board.id;}
async function loadBoard(boardId){const board=await api(`/boards/${encodeURIComponent(boardId)}`);state.board=board;if(!board.matches.some(m=>m.id===state.selected))state.selected=board.matches[0]?.id;$('#board-select').value=board.id;location.hash=`board=${board.id}`;renderBoard();}
$('#board-select').addEventListener('change',event=>{if(event.target.value)task(()=>loadBoard(event.target.value));});
$('#refresh-board').addEventListener('click',()=>task(async()=>{await loadBoards();if(state.board)await loadBoard(state.board.id);notice('Saved boards refreshed. ChatGPT action imports appear in the board selector.');}));
function renderBoard(){
  $('#board-heading').textContent=state.board?.title || 'Match board';$('#board-empty').hidden=!!state.board;
  $('#match-list').innerHTML=state.board?.matches.map(m=>{const latest=m.assessments.filter(a=>a.oddsEvidenceId).at(-1);return `<button class="match-card ${m.id===state.selected?'active':''}" data-match="${esc(m.id)}" aria-pressed="${m.id===state.selected}"><span class="rank">${String(m.rank).padStart(2,'0')}</span><span><strong>${esc(m.home)}<br><span class="hint">vs</span> ${esc(m.away)}</strong><span class="match-meta"><span class="grade">${esc(m.grade)}</span><span>${esc(ict(m.kickoff))}</span></span><span class="match-meta">${esc(latest?.verdict || (m.eventId?'Fixture linked':'Awaiting fixture'))}</span></span></button>`;}).join('') || '';
  renderDetail();
}
$('#match-list').addEventListener('click',event=>{const button=event.target.closest('[data-match]');if(button && !state.busy){state.selected=button.dataset.match;renderBoard();}});
function renderDetail(){
  cleanupImages();const m=current();if(!m){$('#match-detail').innerHTML='<div class="empty"><span class="empty-mark">02—04</span><h3>Keep every decision connected</h3><p>Select a saved match to see lineups, odds and its verdict.</p></div>';return;}
  $('#match-detail').replaceChildren($('#detail-template').content.cloneNode(true));field('competition').textContent=m.competition || 'Competition to verify';field('match-name').textContent=`${m.home} vs ${m.away}`;field('kickoff').textContent=`${ict(m.kickoff)} ICT · Frozen ${ict(state.board.created_at)} ICT`;
  field('grades').innerHTML=`<span class="grade">Frozen ${esc(m.grade)}</span> <span class="pill">${esc(m.structuralType || 'Structural type not supplied')}</span>`;
  if(m.eventId){field('fixture').innerHTML=`<p class="hint">BSD fixture #${m.eventId}</p><button data-action="lineups" class="secondary">Fetch latest lineups</button>`;$('[data-action="find"]').hidden=true;}
  const snapshot=m.evidence.filter(e=>e.kind==='lineups').at(-1);if(snapshot)renderLineups(snapshot);
  const odds=m.evidence.filter(e=>e.kind==='odds').at(-1);if(odds)renderOdds(odds);
  const verdict=m.assessments.filter(a=>a.oddsEvidenceId).at(-1);if(verdict)renderVerdict(verdict);
  field('history').innerHTML=[...m.assessments].reverse().map(a=>`<article><time>${esc(ict(a.createdAt))} ICT · ${esc(a.period)} · ${esc(a.auditStatus==='synced'?'Airtable synced':'Audit pending')}</time><strong>${esc(a.verdict)}</strong><p>${esc(a.summary)}</p></article>`).join('');
  if(m.assessments.some(a=>a.auditStatus==='pending'))field('history').insertAdjacentHTML('beforeend','<button data-action="audit" class="secondary">Retry Airtable sync</button>');
}
function renderLineups(snapshot){
  const {lineups,profiles,league}=snapshot;field('competition').textContent=league?.name || 'Competition unavailable';
  const players=list=>(list || []).map(p=>`<li><span class="jersey">${esc(p.jersey_number ?? '—')}</span>${esc(p.name)}${p.captain?' (C)':''}</li>`).join('');
  field('lineups').innerHTML=`<p class="hint">Fetched ${esc(ict(snapshot.fetchedAt))} ICT <span class="pill ${lineups.lineup_status==='confirmed'?'good':'warn'}">${esc(lineups.lineup_status)}</span></p>${lineups.lineup_status!=='confirmed'?'<p class="audit-warning">Only confirmed starting XIs can clear the lineup check.</p>':''}<div class="lineup-grid">${['home','away'].map(side=>{const team=lineups.lineups?.[side];if(!team)return `<div class="lineup-team"><h3>${esc(snapshot.event[`${side}_team`])}</h3><p class="hint">No lineup published.</p></div>`;return `<div class="lineup-team"><h3>${esc(team.team_name)}</h3><p class="hint">${esc(team.formation || 'Formation unavailable')}</p><ol>${players(team.players)}</ol><details><summary>Bench · ${team.substitutes?.length || 0}</summary><ol>${players(team.substitutes)}</ol></details></div>`;}).join('')}</div><details class="context"><summary>Team profiles & source evidence</summary>${['home','away'].map(side=>{const p=profiles[side],s=p?.sample;return `<h3>${esc(snapshot.event[`${side}_team`])}</h3><p class="hint">${s?`${s.matches} matches · GF ${s.gf} / GA ${s.ga} · Scored 2+: ${s.scored2}/${s.matches} · Conceded 2+: ${s.conceded2}/${s.matches} · ${p.seasonComplete?'Complete available season':'Partial sample'}`:'Profile unavailable'}</p>`;}).join('')}<pre class="evidence-text hint">${esc(JSON.stringify({warnings:snapshot.warnings,profiles,absences:lineups.unavailable_players},null,2))}</pre></details>`;
}
function renderOdds(odds){
  const e=odds.extracted;const already=current().assessments.some(a=>a.oddsEvidenceId===odds.id);
  field('odds-review').innerHTML=`<div class="odds-review" data-odds-id="${esc(odds.id)}"><h3>Review the image reading</h3><p>${esc(e.home || 'Home unreadable')} vs ${esc(e.away || 'Away unreadable')}</p><p class="hint">${esc(e.bookmaker || 'Bookmaker not visible')} · ${esc(e.period)} · ${esc(e.oddsFormat)} odds</p>${(e.warnings || []).map(w=>`<p class="audit-warning">${esc(w)}</p>`).join('')}<div class="offer-row"><span class="hint">Over line</span><span class="hint">Decimal odds</span><span></span></div><div id="offer-rows">${e.offers.map(o=>offerRow(o)).join('')}</div><button data-action="add-offer" class="text-button">+ Add a visible line</button><label for="captured-at">Screenshot captured at · ICT</label><input id="captured-at" type="datetime-local" value="${localICT(odds.createdAt)}"><p class="hint">Set the actual capture time. Fresh uploads do not make old prices current. The workspace asks for a new image after 15 minutes.</p><label class="checkbox"><input id="identity-confirm" type="checkbox"><span>I checked the image: it is this exact fixture, the prices above are correct, and this is the full-match 90-minute Over market.</span></label><button data-action="verdict" class="primary" ${already?'disabled':''}>${already?'Assessed · Upload a new image to reassess':'Run football model'}</button></div>`;
}
function offerRow(o={}){return `<div class="offer-row"><input type="number" min="0.25" max="15" step="0.25" aria-label="Over goal line" class="offer-line" value="${esc(o.line ?? '')}"><input type="number" min="1.001" max="100" step="any" aria-label="Decimal odds" class="offer-odds" value="${esc(o.odds ?? '')}"><button type="button" class="icon-button" data-action="remove-offer" aria-label="Remove line">×</button></div>`;}
function renderVerdict(a){
  field('verdict').innerHTML=`<article class="verdict ${a.verdict==='OFFICIAL LOCK'?'lock':''}"><p class="eyebrow">${esc(a.modelVersion)} · ${esc(a.modelSha?.slice(0,7))} · ${esc(ict(a.createdAt))} ICT</p><h4>${esc(a.verdict)}${a.verdict==='OFFICIAL LOCK'?` — O${a.selectedLine} @ ${a.selectedOdds}`:''}</h4><p>${esc(a.summary)}</p>${a.protection?`<p class="hint">${esc(a.protection)}</p>`:''}${a.postXIGrade?`<p class="hint">Frozen ${esc(current().grade)} → Post-XI ${esc(a.postXIGrade)}</p>`:''}${['primaryRoute','profileAssessment','chanceQualityAssessment','lineupAssessment'].filter(k=>a[k]).map(k=>`<p class="hint">${esc(a[k])}</p>`).join('')}${['failureModes','missingEvidence','lineComparisons'].filter(k=>a[k]?.length).map(k=>`<h3>${({failureModes:'Failure modes',missingEvidence:'Unresolved evidence',lineComparisons:'Line comparison'})[k]}</h3><ul>${a[k].map(item=>`<li>${esc(item)}</li>`).join('')}</ul>`).join('')}<p class="hint">${a.auditStatus==='synced'?'Recorded in Airtable.':'Saved on your backend. Airtable sync pending.'}</p></article>`;
}
$('#match-detail').addEventListener('change',event=>{
  if(event.target.id!=='odds-images')return;
  task(async()=>{cleanupImages();const files=[...event.target.files];if(files.length>3)throw new Error('Choose up to three images.');if(files.some(f=>f.size>2*1024*1024 || !['image/png','image/jpeg','image/webp'].includes(f.type)))throw new Error('Each image must be PNG, JPEG or WebP and no larger than 2 MB.');
    state.images=await Promise.all(files.map(file=>new Promise((resolve,reject)=>{const reader=new FileReader();reader.onload=()=>resolve(reader.result);reader.onerror=()=>reject(new Error('An image could not be read.'));reader.readAsDataURL(file);})));state.previewURLs=files.map(URL.createObjectURL);field('image-preview').innerHTML=state.previewURLs.map((url,i)=>`<a href="${url}" target="_blank" rel="noreferrer"><img src="${url}" alt="Odds screenshot ${i+1}"></a>`).join('');$('[data-action="extract"]').disabled=!files.length;
  });
});
$('#match-detail').addEventListener('click',event=>{
  const button=event.target.closest('[data-action]');if(!button || button.disabled)return;const action=button.dataset.action;
  if(action==='add-offer'){$('#offer-rows').insertAdjacentHTML('beforeend',offerRow());return;}
  if(action==='remove-offer'){button.closest('.offer-row').remove();return;}
  task(async()=>{
    const m=current(),path=`/matches/${m.id}`;
    if(action==='find'){
      const fixtures=await api(path+'/fixtures');field('fixture').innerHTML=`<p class="hint">Choose the exact fixture. Check home/away order and kickoff before confirming.</p>${fixtures.length?fixtures.map(e=>`<label class="fixture-option"><input type="radio" name="bsd-fixture" value="${e.id}">${esc(e.home_team)} vs ${esc(e.away_team)}<small>${esc(ict(e.event_date))} ICT · ${esc(e.status)} · BSD #${e.id}</small></label>`).join(''):'<p class="audit-warning">No matching fixture found. It may be outside BSD coverage or listed under another team name.</p>'}<div class="fixture-actions"><label>Or enter its BSD event ID<input id="manual-event-id" inputmode="numeric" placeholder="Event ID"></label><button data-action="bind" class="secondary">Review fixture identity</button></div>`;
    }
    if(action==='bind'){
      const eventId=Number($('#manual-event-id').value || $('input[name="bsd-fixture"]:checked')?.value);if(!Number.isSafeInteger(eventId) || eventId<=0)throw new Error('Select a fixture or enter a valid BSD event ID.');
      // The server returns identity before binding, including manually entered IDs.
      const preview=await api(path+'/fixture-preview',{eventId});field('fixture').innerHTML=`<div class="fixture-option"><strong>${esc(preview.home_team)} vs ${esc(preview.away_team)}</strong><p class="hint">${esc(ict(preview.event_date))} ICT · ${esc(preview.status)} · BSD #${eventId}</p><p class="hint">Frozen match: ${esc(m.home)} vs ${esc(m.away)}. Confirm only if these identify the same fixture.</p><button data-action="confirm-bind" data-event-id="${eventId}" class="primary">Confirm this exact fixture</button></div>`;
    }
    if(action==='confirm-bind'){await api(path+'/bind',{eventId:Number(button.dataset.eventId),identityConfirmed:true});notice('Fixture confirmed. Fetching its lineups and team profiles…');await api(path+'/lineups',{});await loadBoard(state.board.id);notice('BSD evidence loaded. Predicted lineups remain provisional.');}
    if(action==='lineups'){notice('Fetching lineups and team profiles…');await api(path+'/lineups',{});await loadBoard(state.board.id);notice('Latest BSD evidence saved.');}
    if(action==='extract'){if(!state.images.length)throw new Error('Choose an odds image first.');notice('Reading the odds images…');const odds=await api(path+'/odds',{images:state.images});m.evidence.push(odds);renderOdds(odds);notice('Check the extracted identity, market and prices against your screenshots.');}
    if(action==='verdict'){
      const offers=validateOffers([...document.querySelectorAll('#offer-rows .offer-row')].map(row=>({line:Number(row.querySelector('.offer-line').value),odds:Number(row.querySelector('.offer-odds').value)})));
      if(!$('#identity-confirm').checked)throw new Error('Review the image and confirm its identity and 90-minute market before analysis.');
      const capture=$('#captured-at').value;if(!capture)throw new Error('Enter the screenshot capture time.');
      notice('Refreshing lineups and evaluating the frozen thesis against the reviewed market…');await api(path+'/verdict',{oddsEvidenceId:$('.odds-review').dataset.oddsId,offers,capturedAt:kickoffISO(capture+':00+07:00'),identityConfirmed:true});await loadBoard(state.board.id);notice('Assessment saved. Read its verdict and unresolved evidence below.');
    }
    if(action==='audit'){await api(path+'/audit',{});await loadBoard(state.board.id);notice('Decision history synced to Airtable.');}
  });
});
window.addEventListener('beforeunload',cleanupImages);
