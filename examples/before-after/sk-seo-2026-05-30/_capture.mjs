// CDP full-page screenshot driver (Node 25 built-in WebSocket).
// Usage: node _capture.mjs <jobsfile.json>
// job: { url, out, width, mobile }
import { writeFileSync, readFileSync } from 'node:fs';

const jobsFile = process.argv[2];
const jobs = JSON.parse(readFileSync(jobsFile, 'utf8'));

const ver = await (await fetch('http://127.0.0.1:9222/json/version')).json();
const ws = new WebSocket(ver.webSocketDebuggerUrl);
await new Promise((res, rej) => { ws.onopen = res; ws.onerror = rej; });

let _id = 0;
const pending = new Map();
const loadWaiters = new Map(); // sessionId -> resolve
ws.onmessage = (ev) => {
  const m = JSON.parse(ev.data);
  if (m.id && pending.has(m.id)) {
    const { resolve, reject } = pending.get(m.id);
    pending.delete(m.id);
    m.error ? reject(new Error(JSON.stringify(m.error))) : resolve(m.result);
  } else if (m.method === 'Page.loadEventFired' && m.sessionId && loadWaiters.has(m.sessionId)) {
    loadWaiters.get(m.sessionId)();
  }
};
const send = (method, params = {}, sessionId) => new Promise((resolve, reject) => {
  const id = ++_id;
  pending.set(id, { resolve, reject });
  ws.send(JSON.stringify(sessionId ? { id, method, params, sessionId } : { id, method, params }));
});
const sleep = (ms) => new Promise(r => setTimeout(r, ms));

for (const job of jobs) {
  const { targetId } = await send('Target.createTarget', { url: 'about:blank' });
  const { sessionId } = await send('Target.attachToTarget', { targetId, flatten: true });
  await send('Page.enable', {}, sessionId);
  await send('Network.enable', {}, sessionId);
  await send('Network.setCacheDisabled', { cacheDisabled: true }, sessionId);
  await send('Emulation.setEmulatedMedia',
    { features: [{ name: 'prefers-reduced-motion', value: 'reduce' }] }, sessionId);
  await send('Emulation.setDeviceMetricsOverride',
    { width: job.width, height: 900, deviceScaleFactor: job.mobile ? 2 : 1, mobile: !!job.mobile }, sessionId);
  const loaded = new Promise(r => loadWaiters.set(sessionId, r));
  await send('Page.navigate', { url: job.url }, sessionId);
  await Promise.race([loaded, sleep(8000)]);
  loadWaiters.delete(sessionId);
  await sleep(2000); // partials fetch + fonts + layout settle
  const { data } = await send('Page.captureScreenshot',
    { format: 'png', captureBeyondViewport: true, fromSurface: true }, sessionId);
  writeFileSync(job.out, Buffer.from(data, 'base64'));
  await send('Target.closeTarget', { targetId });
  console.log('OK', job.out);
}
ws.close();
console.log('DONE', jobs.length);
