import {API,SOCKET,rows,normalize,isLive,statusText,score,mergeRest,applyFrame,ictDate,dayWindow,visibleEvents,subscriptions} from './core.mjs';
const $=s=>document.querySelector(s), esc=v=>String(v??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const state={key:'',events:new Map(),pins:new Set(),tab:'live',date:ictDate(),query:'',session:0,liveBusy:false,failures:0,blockedUntil:0,lastReceived:0,liveTimer:null,socket:null,socketTimer:null,heartbeat:null,wantPush:false,pushUnavailable:false,subscribed:new Set(),rejected:new Set(),selected:null,detailTab:'lineups',dayAbort:null,detailAbort:null,controllers:new Set(),dayLoaded:null,dayLoading:false};
const nodes=new Map(),groups=new Map(),detailCache=new Map();
let renderPending=false,saveTimer=null;
$('#date').value=state.date;
try{state.pins=new Set(JSON.parse(localStorage.getItem('touchline-pins')||'[]').filter(Number.isSafeInteger));const saved=JSON.parse(localStorage.getItem('touchline-scores')||'null');if(saved?.events && Date.now()-saved.at<86400000){state.events=new Map(saved.events.map(e=>[e.id,{...normalize(e),streamScore:e.streamScore,checking:false}]));state.lastReceived=saved.at;}}catch{}
function message(text,error=false){$('#message').hidden=!text;$('#message').textContent=text;$('#message').classList.toggle('error',error);}
function setText(node,value){if(node.textContent!==String(value))node.textContent=String(value);}
function updateConnection(){
  const socketLive=state.socket?.readyState===WebSocket.OPEN;
  setText($('#transport'),!state.key?'Not connected':!navigator.onLine?'Offline':socketLive?`Push · ${state.subscribed.size}/10`:state.pushUnavailable?'REST · 10s':'REST · 10s');
  $('#transport').classList.toggle('live',!!state.key&&navigator.onLine);$('#onboarding').hidden=!!state.key;
  const t=state.lastReceived?new Intl.DateTimeFormat('en-GB',{timeZone:'Asia/Ho_Chi_Minh',hour:'2-digit',minute:'2-digit',second:'2-digit',hour12:false}).format(state.lastReceived):null;
  setText($('#updated'),t?`${state.key?'Received':'Saved snapshot'} ${t} ICT`:'Connect to load the live feed');
  setText($('#feed-note'),socketLive?'Push covers up to 10 live matches; the full feed also refreshes every 10 seconds.':state.pushUnavailable?'WebSocket unavailable on this connection. REST refreshes every 10 seconds.':'REST refreshes every 10 seconds. Push requires BSD’s WebSocket add-on.');
}
function scheduleRender(){if(!renderPending){renderPending=true;requestAnimationFrame(()=>{renderPending=false;render();});}}
function saveSnapshot(){clearTimeout(saveTimer);saveTimer=setTimeout(()=>{try{localStorage.setItem('touchline-scores',JSON.stringify({at:state.lastReceived,events:[...state.events.values()].slice(0,500)}));}catch{}},1200);}
function render(){
  const list=visibleEvents([...state.events.values()],state);setText($('#live-count'),state.key?[...state.events.values()].filter(isLive).length:'—');setText($('#pin-count'),state.pins.size);updateConnection();
  const wanted=new Set(),wantedGroups=new Set(),grouped=new Map();
  for(const e of list){
    const groupId=String(e.league_id??'other');wantedGroups.add(groupId);if(!grouped.has(groupId))grouped.set(groupId,[]);grouped.get(groupId).push(e.id);let g=groups.get(groupId);
    if(!g){const section=document.createElement('section');section.className='league';const heading=document.createElement('div');heading.className='league-heading';const name=document.createElement('strong'),count=document.createElement('span');heading.append(name,count);const body=document.createElement('div');section.append(heading,body);g={section,name,count,body};groups.set(groupId,g);}
    setText(g.name,e.league_name||`Competition ${e.league_id??'unlisted'}`);
    let row=nodes.get(e.id);if(!row){row=$('#row-template').content.firstElementChild.cloneNode(true);row.dataset.id=e.id;nodes.set(e.id,row);}
    const scores=score(e),old=row.querySelector('.scores').textContent;setText(row.querySelector('.home'),e.home_team);setText(row.querySelector('.away'),e.away_team);setText(row.querySelector('.home-score'),scores[0]);setText(row.querySelector('.away-score'),scores[1]);setText(row.querySelector('.minute'),statusText(e));
    row.classList.toggle('playing',isLive(e)&&!!state.key);row.classList.toggle('stale',!state.key||!!e.checking);const pin=row.querySelector('.pin');pin.setAttribute('aria-pressed',String(state.pins.has(e.id)));pin.setAttribute('aria-label',`${state.pins.has(e.id)?'Unpin':'Pin'} ${e.home_team} vs ${e.away_team}`);setText(pin,state.pins.has(e.id)?'★':'☆');
    row.querySelector('.match-open').setAttribute('aria-label',`${e.home_team} ${scores[0]}, ${e.away_team} ${scores[1]}, ${statusText(e)}. Open match details.`);
    setText(row.querySelector('.extra'),e.penalty_shootout?`Pens ${e.penalty_shootout.home??'—'}–${e.penalty_shootout.away??'—'}`:e.checking?'Checking match status':e.extra_time_score?'Includes extra time':state.subscribed.has(e.id)?'PUSH':'');
    if(old&&old!==row.querySelector('.scores').textContent&&state.key){row.classList.remove('changed');requestAnimationFrame(()=>row.classList.add('changed'));}
    if(row.parentNode!==g.body)g.body.append(row);wanted.add(e.id);
  }
  for(const [id,row]of nodes){if(!wanted.has(id))row.remove();}
  // Reorder only when membership/order changes; score ticks keep focused rows intact.
  let groupCursor=$('#leagues').firstElementChild;
  for(const groupId of wantedGroups){const g=groups.get(groupId),order=grouped.get(groupId);let cursor=g.body.firstElementChild;for(const id of order){const row=nodes.get(id);if(row!==cursor)g.body.insertBefore(row,cursor);cursor=row.nextElementSibling;}setText(g.count,`${order.length} match${order.length===1?'':'es'}`);if(g.section!==groupCursor)$('#leagues').insertBefore(g.section,groupCursor);groupCursor=g.section.nextElementSibling;}
  for(const [id,g]of groups)if(!wantedGroups.has(id))g.section.remove();
  $('#empty').hidden=list.length>0;
  if(!list.length){setText($('#empty h2'),state.dayLoading?'Loading fixtures…':!state.key?'Ready for kickoff.':state.query?'No matching teams.':state.tab==='pinned'?'Pin the matches you follow.':state.tab==='live'?'No matches live right now.':'No matches in this view.');setText($('#empty p'),!state.key?'Connect your BSD key to load real scores.':state.dayLoading?'Fixtures appear as each page arrives.':state.tab==='pinned'?'Use the star beside a match to keep it here.':'Try All matches or another date.');}
  if(state.selected)renderDetailScore();
}
async function get(path,params={},signal){
  if(!state.key)throw new Error('Connect your BSD key first.');
  if(Date.now()<state.blockedUntil)throw new Error('BSD rate limit reached. Automatic refresh will resume shortly.');
  const url=new URL(path,API);for(const[k,v]of Object.entries(params))url.searchParams.set(k,v);
  const controller=new AbortController();state.controllers.add(controller);const timeout=setTimeout(()=>controller.abort(),15000);const abort=()=>controller.abort();signal?.addEventListener('abort',abort,{once:true});if(signal?.aborted)controller.abort();
  try{
    const response=await fetch(url,{headers:{Authorization:`Token ${state.key}`,Accept:'application/json'},signal:controller.signal,credentials:'omit',redirect:'error'});
    if(response.status===429){const retry=response.headers.get('Retry-After'),seconds=Number(retry);state.blockedUntil=Date.now()+(Number.isFinite(seconds)&&seconds>0?seconds*1000:60000);throw new Error('BSD rate limit reached. Keeping the last scores and slowing refresh.');}
    if(response.status===401||response.status===403){const error=new Error('BSD rejected this key or its access. Check your BSD account.');error.auth=true;throw error;}
    if(!response.ok)throw new Error(`BSD returned HTTP ${response.status}. Keeping the last scores.`);
    return await response.json();
  }catch(error){if(error.name==='AbortError')throw error;if(error instanceof TypeError)throw new Error('Cannot reach BSD. Check your connection or browser access; the last scores remain visible.');throw error;}
  finally{clearTimeout(timeout);state.controllers.delete(controller);signal?.removeEventListener('abort',abort);}
}
function schedulePoll(delay=10000){clearTimeout(state.liveTimer);if(state.key&&!document.hidden)state.liveTimer=setTimeout(poll,Math.max(delay,state.blockedUntil-Date.now()));}
async function poll(){
  if(!state.key||state.liveBusy||document.hidden||!navigator.onLine)return;
  const session=state.session,start=Date.now();state.liveBusy=true;$('#refresh').disabled=true;
  try{
    const feed=rows(await get('events/live/'));if(session!==state.session)return;
    const seen=new Set();for(const item of feed){const e=mergeRest(state.events.get(item.id),item,start);state.events.set(e.id,e);seen.add(e.id);}
    const disappeared=[...state.events.values()].filter(e=>isLive(e)&&!seen.has(e.id)&&(!e.checking||Date.now()-(e.checkAt||0)>30000));
    for(const e of disappeared){state.events.set(e.id,{...e,checking:true,checkAt:Date.now()});void resolveDisappeared(e.id,session);}
    state.lastReceived=Date.now();state.failures=0;message('');scheduleRender();saveSnapshot();syncSubscriptions();
  }catch(error){if(session!==state.session||error.name==='AbortError')return;state.failures++;message(error.message,true);if(error.auth){stop();updateConnection();}}
  finally{if(session===state.session){state.liveBusy=false;$('#refresh').disabled=false;schedulePoll(Math.min(60000,10000*2**Math.min(state.failures,3)));}}
}
async function resolveDisappeared(id,session){try{const e=normalize(await get(`events/${id}/`));if(session!==state.session)return;state.events.set(id,{...state.events.get(id),...e,streamScore:undefined,pushAt:undefined,checking:isLive(e)});scheduleRender();}catch{/* Keep CHECK rather than inventing a final result. */}}
async function loadDay(){
  if(!state.key)return;state.dayAbort?.abort();const controller=new AbortController();state.dayAbort=controller;const date=state.date,session=state.session;state.dayLoading=true;state.dayLoaded=null;scheduleRender();
  try{
    const range=dayWindow(date);for(let offset=0;offset<10000;offset+=200){const start=Date.now();const feed=rows(await get('events/',{...range,limit:200,offset},controller.signal));if(controller.signal.aborted||session!==state.session)return;for(const raw of feed){const old=state.events.get(raw.id);const e=mergeRest(old,raw,start);state.events.set(e.id,{...e,league_name:raw.league_name||old?.league_name});}scheduleRender();if(feed.length<200){state.dayLoaded=date;break;}if(offset===9800)message('BSD returned more than 10,000 fixtures. This date view is partial.',true);}
    void loadLeagueNames(session);saveSnapshot();
  }catch(error){if(error.name!=='AbortError'&&session===state.session)message(error.message,true);}
  finally{if(state.dayAbort===controller){state.dayLoading=false;scheduleRender();}}
}
async function loadLeagueNames(session){
  const missing=[...new Set([...state.events.values()].filter(e=>!e.league_name&&e.league_id).map(e=>e.league_id))];
  // Lazy and bounded: only name the leagues on the chosen date; never delay scores.
  for(let i=0;i<missing.length;i+=4){if(session!==state.session||document.hidden)return;await Promise.allSettled(missing.slice(i,i+4).map(async id=>{const league=await get(`leagues/${id}/`);if(session!==state.session)return;for(const e of state.events.values())if(e.league_id===id)e.league_name=league.name;scheduleRender();}));}
}
function closeSocket(){clearTimeout(state.socketTimer);clearTimeout(state.heartbeat);const ws=state.socket;state.socket=null;state.subscribed.clear();if(ws){ws.onclose=null;ws.onmessage=null;ws.onerror=null;ws.close();}}
function connectSocket(){
  if(!state.key||!state.wantPush||state.pushUnavailable||document.hidden||!navigator.onLine||state.socket)return;
  const session=state.session;let ws;try{ws=new WebSocket(SOCKET,['token',state.key]);}catch{state.pushUnavailable=true;updateConnection();return;}state.socket=ws;
  ws.onopen=()=>{if(session!==state.session)return;syncSubscriptions();heartbeat();updateConnection();};
  let received=Date.now();
  function heartbeat(){clearTimeout(state.heartbeat);state.heartbeat=setTimeout(()=>{if(state.socket!==ws)return;if(Date.now()-received>60000){ws.close();return;}if(ws.readyState===WebSocket.OPEN)ws.send(JSON.stringify({action:'ping'}));heartbeat();},20000);}
  ws.onmessage=event=>{
    if(session!==state.session||state.socket!==ws)return;received=Date.now();let frame;try{frame=JSON.parse(event.data);}catch{return;}
    if(frame.type==='error'){
      if(['auth_required','subscription_required'].includes(frame.code)){state.pushUnavailable=true;closeSocket();updateConnection();return;}
      if(frame.event_id){state.rejected.add(Number(frame.event_id));state.subscribed.delete(Number(frame.event_id));syncSubscriptions();}return;
    }
    const id=Number(frame.event_id),previous=state.events.get(id);const next=applyFrame(previous,frame);if(next!==previous){state.events.set(id,next);state.lastReceived=Date.now();scheduleRender();saveSnapshot();syncSubscriptions();}
  };
  ws.onerror=()=>{};
  ws.onclose=event=>{if(state.socket!==ws)return;state.socket=null;state.subscribed.clear();clearTimeout(state.heartbeat);if([4401,4402,4404].includes(event.code))state.pushUnavailable=true;updateConnection();if(!state.pushUnavailable&&state.key&&!document.hidden)state.socketTimer=setTimeout(connectSocket,10000);};
}
function syncSubscriptions(){
  if(!state.socket){connectSocket();return;}if(state.socket.readyState!==WebSocket.OPEN)return;
  const wanted=new Set(subscriptions([...state.events.values()].filter(e=>!state.rejected.has(e.id)),state.pins,state.selected));
  for(const id of state.subscribed)if(!wanted.has(id)){state.socket.send(JSON.stringify({action:'unsubscribe',event_id:id}));state.subscribed.delete(id);}
  for(const id of wanted)if(!state.subscribed.has(id)){state.socket.send(JSON.stringify({action:'subscribe',event_id:id}));state.subscribed.add(id);}
  updateConnection();scheduleRender();
}
function stop(){state.session++;state.key='';clearTimeout(state.liveTimer);state.controllers.forEach(c=>c.abort());state.controllers.clear();state.dayAbort?.abort();state.detailAbort?.abort();closeSocket();state.liveBusy=false;state.dayLoading=false;$('#refresh').disabled=false;}
function openSettings(){$('#settings-error').textContent='';$('#settings').showModal();}
$('#connect').onclick=openSettings;$('#start').onclick=openSettings;$('#close-settings').onclick=()=>$('#settings').close();
$('#settings-form').onsubmit=async event=>{
  event.preventDefault();const key=$('#key').value.trim();if(!key)return;stop();state.key=key;state.wantPush=$('#push').checked;state.pushUnavailable=false;state.rejected.clear();state.failures=0;state.blockedUntil=0;$('#key').value='';$('#settings').close();updateConnection();message('Connecting to BSD…');await poll();if(state.key&&state.tab!=='live')void loadDay();
};
$('#disconnect').onclick=()=>{stop();$('#key').value='';$('#settings').close();$('#detail').close();state.selected=null;message('Disconnected. Saved scores remain visible as a snapshot.');render();};
$('#refresh').onclick=()=>{if(!state.key){openSettings();return;}void poll();if(state.tab!=='live'&&state.tab!=='pinned')void loadDay();};
document.querySelectorAll('[data-tab]').forEach(button=>button.onclick=()=>{state.tab=button.dataset.tab;document.querySelectorAll('[data-tab]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));render();if(['today','finished'].includes(state.tab)&&state.dayLoaded!==state.date)void loadDay();});
$('#date').onchange=()=>{if(!$('#date').value)return;state.date=$('#date').value;if(!['today','finished'].includes(state.tab))document.querySelector('[data-tab="today"]').click();else{render();void loadDay();}};
$('#search').oninput=()=>{state.query=$('#search').value;scheduleRender();};
$('#leagues').onclick=event=>{const row=event.target.closest('.match-row');if(!row)return;const id=Number(row.dataset.id);if(event.target.closest('.pin')){state.pins.has(id)?state.pins.delete(id):state.pins.add(id);try{localStorage.setItem('touchline-pins',JSON.stringify([...state.pins]));}catch{}render();syncSubscriptions();}else void openDetail(id);};
function renderDetailScore(){const e=state.events.get(state.selected);if(!e)return;const s=score(e);setText($('#detail-title'),`${e.home_team} vs ${e.away_team}`);setText($('#detail-league'),e.league_name||'Match centre');$('#detail-score').innerHTML=`${esc(s[0])} : ${esc(s[1])}<small>${esc(statusText(e))}${!state.key?' · Saved snapshot':''}${e.penalty_shootout?` · Pens ${esc(e.penalty_shootout.home)}–${esc(e.penalty_shootout.away)}`:''}</small>`;}
async function openDetail(id){state.selected=id;renderDetailScore();$('#detail-content').innerHTML='<div class="detail-tabs"><button data-detail="lineups" aria-pressed="true">Lineups</button><button data-detail="stats" aria-pressed="false">Statistics</button></div><div id="detail-body"></div>';state.detailTab='lineups';$('#detail').showModal();syncSubscriptions();await loadDetail();}
async function loadDetail(){
  state.detailAbort?.abort();const controller=new AbortController();state.detailAbort=controller;const id=state.selected,kind=state.detailTab,key=`${id}:${kind}`,cached=detailCache.get(key),session=state.session;
  if(cached)renderDetailData(kind,cached.data);else $('#detail-body').innerHTML='<p class="detail-empty">Loading match details…</p>';
  if(cached&&Date.now()-cached.at<30000)return;
  try{const data=await get(`events/${id}/${kind}/`,{},controller.signal);if(controller.signal.aborted||session!==state.session||state.selected!==id||state.detailTab!==kind)return;detailCache.set(key,{at:Date.now(),data});renderDetailData(kind,data);}
  catch(error){if(error.name!=='AbortError'&&state.selected===id)$('#detail-body').innerHTML=`<p class="detail-empty">${esc(error.message)}</p><button id="retry-detail">Retry</button>`;}
}
function renderDetailData(kind,data){
  const body=$('#detail-body');if(!body)return;
  if(kind==='lineups'){
    if(!data.lineups){body.innerHTML='<p class="detail-empty">Lineups are not available yet.</p>';return;}
    body.innerHTML=`<p class="hint">${esc(data.lineup_status==='confirmed'?'Confirmed lineups':data.lineup_status==='predicted'?'Predicted lineups — not official':'Lineup status unavailable')}</p><div class="sides">${['home','away'].map(side=>{const team=data.lineups[side];if(!team)return '<p>Unavailable</p>';return `<section><h3>${esc(team.team_name)}</h3><small>${esc(team.formation||'')}</small><ol>${(team.players||[]).map(p=>`<li>${esc(p.jersey_number??'')} ${esc(p.name)}${p.captain?' (C)':''}</li>`).join('')}</ol><details><summary>Bench</summary><ol>${(team.substitutes||[]).map(p=>`<li>${esc(p.name)}</li>`).join('')}</ol></details></section>`;}).join('')}</div>`;
  }else{
    const stats=data.stats||{},h=stats.home||{},a=stats.away||{};
    const keys=[['ball_possession','Possession'],['total_shots','Shots'],['shots_on_target','On target'],['corner_kicks','Corners'],['fouls','Fouls'],['yellow_cards','Yellow cards'],['red_cards','Red cards']];
    body.innerHTML=keys.map(([key,label])=>`<div class="stat"><b>${esc(h[key]??'—')}</b><span>${label}</span><b>${esc(a[key]??'—')}</b></div>`).join('')+'<p class="hint">— means BSD has no reported value.</p>';
  }
}
$('#detail-content').onclick=event=>{const button=event.target.closest('[data-detail]');if(button){state.detailTab=button.dataset.detail;document.querySelectorAll('[data-detail]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));void loadDetail();}if(event.target.id==='retry-detail')void loadDetail();};
$('#close-detail').onclick=()=>$('#detail').close();$('#detail').addEventListener('close',()=>{state.selected=null;state.detailAbort?.abort();syncSubscriptions();});
document.addEventListener('visibilitychange',()=>{if(document.hidden){clearTimeout(state.liveTimer);closeSocket();}else if(state.key){void poll();connectSocket();if(['today','finished'].includes(state.tab))void loadDay();}});
window.addEventListener('online',()=>{if(state.key){void poll();connectSocket();}});window.addEventListener('offline',()=>{clearTimeout(state.liveTimer);closeSocket();message('Offline. Showing the last received scores.',true);updateConnection();});
window.addEventListener('pagehide',()=>{clearTimeout(state.liveTimer);closeSocket();state.controllers.forEach(c=>c.abort());});
render();
