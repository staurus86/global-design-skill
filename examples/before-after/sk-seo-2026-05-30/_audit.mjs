// Empirical a11y + responsive audit via CDP + axe-core. Node 25 built-in WebSocket.
// Usage: node _audit.mjs <pagesfile.json> <outfile.json>
import { readFileSync, writeFileSync } from 'node:fs';

const pages = JSON.parse(readFileSync(process.argv[2], 'utf8'));
const outFile = process.argv[3];
const axeSrc = readFileSync(new URL('./axe.min.js', import.meta.url), 'utf8');

const ver = await (await fetch('http://127.0.0.1:9222/json/version')).json();
const ws = new WebSocket(ver.webSocketDebuggerUrl);
await new Promise((res, rej) => { ws.onopen = res; ws.onerror = rej; });

let _id = 0;
const pending = new Map();
const loadWaiters = new Map();
ws.onmessage = (ev) => {
  const m = JSON.parse(ev.data);
  if (m.id && pending.has(m.id)) {
    const { resolve, reject } = pending.get(m.id); pending.delete(m.id);
    m.error ? reject(new Error(JSON.stringify(m.error))) : resolve(m.result);
  } else if (m.method === 'Page.loadEventFired' && m.sessionId && loadWaiters.has(m.sessionId)) {
    loadWaiters.get(m.sessionId)();
  }
};
const send = (method, params = {}, sessionId) => new Promise((resolve, reject) => {
  const id = ++_id; pending.set(id, { resolve, reject });
  ws.send(JSON.stringify(sessionId ? { id, method, params, sessionId } : { id, method, params }));
});
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
const runJS = async (sid, expr, awaitPromise = false) => {
  const r = await send('Runtime.evaluate', { expression: expr, awaitPromise, returnByValue: true }, sid);
  return r.result && r.result.value;
};

const VPS = [{ w: 390, mobile: true }, { w: 768, mobile: false }, { w: 1280, mobile: false }, { w: 1440, mobile: false }];
const report = [];

for (const page of pages) {
  const entry = { name: page.name, url: page.url, axe: {}, overflow: {} };
  const { targetId } = await send('Target.createTarget', { url: 'about:blank' });
  const { sessionId } = await send('Target.attachToTarget', { targetId, flatten: true });
  await send('Page.enable', {}, sessionId);
  await send('Runtime.enable', {}, sessionId);
  await send('Network.enable', {}, sessionId);
  await send('Network.setCacheDisabled', { cacheDisabled: true }, sessionId);

  for (const vp of [{ w: 390, mobile: true, key: 'mobile390' }, { w: 1280, mobile: false, key: 'desktop1280' }]) {
    await send('Emulation.setDeviceMetricsOverride', { width: vp.w, height: 900, deviceScaleFactor: 1, mobile: vp.mobile }, sessionId);
    await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: 'reduce' }] }, sessionId);
    const loaded = new Promise(r => loadWaiters.set(sessionId, r));
    await send('Page.navigate', { url: page.url }, sessionId);
    await Promise.race([loaded, sleep(8000)]); loadWaiters.delete(sessionId);
    await sleep(1800);
    await runJS(sessionId, axeSrc + ';0');
    const raw = await runJS(sessionId,
      "axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa']}})" +
      ".then(r=>JSON.stringify(r.violations.map(x=>({id:x.id,impact:x.impact,help:x.help,n:x.nodes.length,ex:x.nodes.slice(0,4).map(z=>({t:(z.target||[]).join(' '),s:(z.failureSummary||'').replace(/\\n/g,' ').slice(0,180)}))}))))" +
      ".catch(e=>JSON.stringify([{id:'AXE_ERROR',impact:'err',help:e.message,n:0,ex:[]}]))",
      true);
    entry.axe[vp.key] = raw ? JSON.parse(raw) : [];
  }

  for (const vp of VPS) {
    await send('Emulation.setDeviceMetricsOverride', { width: vp.w, height: 900, deviceScaleFactor: 1, mobile: vp.mobile }, sessionId);
    await sleep(300);
    const o = await runJS(sessionId,
      "JSON.stringify((function(){var iw=window.innerWidth;var de=document.documentElement;" +
      "var over=[].slice.call(document.querySelectorAll('body *')).filter(function(e){var r=e.getBoundingClientRect();return r.width>0&&r.right>iw+1;})" +
      ".map(function(e){return e.tagName.toLowerCase()+(e.className&&e.className.toString?('.'+e.className.toString().trim().split(/\\s+/)[0]):'')+' ('+Math.round(e.getBoundingClientRect().right)+'px)';});" +
      "return {sw:de.scrollWidth,iw:iw,horiz:de.scrollWidth>iw+1,over:over.slice(0,8),overCount:over.length};})())");
    entry.overflow['vw' + vp.w] = o ? JSON.parse(o) : null;
  }

  await send('Target.closeTarget', { targetId });
  const m = entry.axe.mobile390 || [], d = entry.axe.desktop1280 || [];
  const horiz = VPS.filter(v => entry.overflow['vw' + v.w] && entry.overflow['vw' + v.w].horiz).map(v => v.w);
  console.log(`[${page.name}] axe nodes mobile=${m.reduce((a, x) => a + x.n, 0)} desktop=${d.reduce((a, x) => a + x.n, 0)} | horiz-overflow: ${horiz.join(',') || 'none'}`);
  report.push(entry);
}

writeFileSync(outFile, JSON.stringify(report, null, 2));
ws.close();
console.log('DONE', report.length, '->', outFile);
