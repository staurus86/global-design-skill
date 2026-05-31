# Reference — Live Audit Snippets

> Browser-console scripts to verify a **rendered** page — paste into DevTools (or run via Playwright `evaluate`). Built from real redesign failures where screenshotting the default state passed but the live UI was broken. Static review is not enough: a page can have a "correct" `color` and still render invisible text; a view toggle can silently break; a badge can hide behind another. **Run these against the real DOM, in every theme and every view mode.**

Each snippet returns data — it does not change the page (except the exercise protocol, which toggles state).

---

## Why these exist (real failure modes they catch)

| Failure | What looked fine | What was actually wrong |
|---|---|---|
| Invisible heading in dark mode | `color` was light (passed a naive contrast check) | `-webkit-text-fill-color: transparent` (leftover gradient-text) overrode `color` → text invisible |
| Contrast "failures" that weren't | DOM-walk contrast script flagged white-on-dark hero | Hero/cards/footer use **gradient** backgrounds (`background-color: transparent`) → script read the wrong layer |
| Hidden paid badge | `$` element existed in the DOM | On featured cards, `$` and the "Топ" badge were both absolute top-right → `$` sat under "Топ" |
| Broken list view | Grid view screenshot looked great | View toggle put the class on the grid itself; the `.list-view .cards-grid` (descendant) rule never matched |
| Filters/search visually dead | `card.hidden = true` was set; an attribute-level test (`:not([hidden])`) passed | `.card{display:flex}` overrode the UA `[hidden]{display:none}` → every card stayed visible. Toggling `[hidden]` only hides if the element's own `display` rule doesn't win |
| Active category "ran back and forth" | The scroll-spy code read correct | It compared scroll vs **cached** `offsetTop`; lazy-loaded images grow page height → cached offsets go stale → highlight jumps non-monotonically. Read live `getBoundingClientRect()` |
| Junk in the text / SR layer | Looked clean visually | Lone `$` status glyphs + decorative list numbers (duplicating the `<ol>`) leaked into `innerText` / screen-reader output — invisible on screen, dirty for bots & a11y |

The pattern: **measure the rendered result, not the source intent — and exercise interactive state.**

---

## A. Gradient-aware contrast audit

Naive contrast scripts walk the DOM for a solid `background-color`. Hero/card/footer surfaces are gradients (transparent `background-color`), so the walk hits the wrong layer and reports nonsense. This version also reads the **rendered fill** (`-webkit-text-fill-color`), which overrides `color` for gradient text.

```js
(() => {
  const cv = document.createElement('canvas'); cv.width = cv.height = 1;
  const cx = cv.getContext('2d', { willReadFrequently: true });
  const rgba = s => { if (!s) return null; cx.clearRect(0,0,1,1); cx.fillStyle='rgba(0,0,0,0)'; try{cx.fillStyle=s;}catch(e){return null;} cx.fillRect(0,0,1,1); const d=cx.getImageData(0,0,1,1).data; return [d[0],d[1],d[2],d[3]/255]; };
  const stops = s => (!s||s==='none') ? [] : (s.match(/(rgba?\([^)]*\)|oklch\([^)]*\)|oklab\([^)]*\)|#[0-9a-f]{3,8})/gi)||[]).map(rgba).filter(c=>c&&c[3]>0.3);
  const lum = ([r,g,b]) => { const f=c=>{c/=255;return c<=0.03928?c/12.92:Math.pow((c+0.055)/1.055,2.4);}; return 0.2126*f(r)+0.7152*f(g)+0.0722*f(b); };
  const ratio = (a,b) => { const x=Math.max(lum(a),lum(b)), y=Math.min(lum(a),lum(b)); return (x+0.05)/(y+0.05); };
  const bg = el => { let n=el; while(n&&n.nodeType===1){ const cs=getComputedStyle(n); const c=rgba(cs.backgroundColor); if(c&&c[3]>0.5) return c; const g=stops(cs.backgroundImage); if(g.length){ return [...[0,1,2].map(i=>Math.round(g.reduce((s,c)=>s+c[i],0)/g.length)),1]; } n=n.parentElement; } return [15,23,42,1]; };
  const seen = new Map();
  for (const el of document.querySelectorAll('h1,h2,h3,h4,p,a,span,strong,li,button')) {
    if (!el.offsetParent) continue;
    if (![...el.childNodes].some(n=>n.nodeType===3&&n.textContent.trim().length>1)) continue;
    const sig = el.tagName+'.'+([...el.classList].slice(0,2).join('.'));
    if (seen.has(sig)) continue;
    const cs = getComputedStyle(el);
    // rendered fill wins over color (gradient text / -webkit-text-fill-color)
    const fill = cs.webkitTextFillColor && cs.webkitTextFillColor !== 'currentcolor' ? rgba(cs.webkitTextFillColor) : rgba(cs.color);
    const fg = (fill && fill[3] > 0.05) ? fill : rgba(cs.color);
    const px = parseFloat(cs.fontSize), bold = parseInt(cs.fontWeight)>=700, large = px>=24 || (bold&&px>=18.66);
    seen.set(sig, { sig, ratio: +ratio(fg, bg(el)).toFixed(2), need: large?3:4.5, sample: el.textContent.trim().slice(0,24) });
  }
  const all = [...seen.values()].sort((a,b)=>a.ratio-b.ratio);
  console.table(all);
  return { fails: all.filter(x=>x.ratio < x.need), lowest: all.slice(0,5) };
})();
```

**Read it right:** a `fail` with ratio ≈ 1.0 on a gradient surface may still be a false positive — confirm visually. But ratio ≈ 1.0 where the fill is **transparent** is a real invisible-text bug (see B).

---

## B. Invisible-text scanner (transparent `-webkit-text-fill-color`)

Gradient text (`background-clip: text; -webkit-text-fill-color: transparent`) is a banned pattern (`rules/03-typography.md` R9). When it is half-removed — neutralised in one theme but not the other — the text goes **invisible** in the un-fixed theme while `color` still looks correct. This finds every such element.

```js
(() => {
  const bad = [], seen = new Set();
  document.querySelectorAll('*').forEach(el => {
    if (!el.offsetParent) return;
    if (![...el.childNodes].some(n=>n.nodeType===3&&n.textContent.trim().length>1)) return;
    const tf = getComputedStyle(el).webkitTextFillColor;
    if (tf === 'rgba(0, 0, 0, 0)' || tf === 'transparent' || /\/\s*0\s*\)/.test(tf)) {
      const sig = el.tagName+'.'+([...el.classList].slice(0,2).join('.'));
      if (seen.has(sig)) return; seen.add(sig);
      bad.push({ sig, textFill: tf, color: getComputedStyle(el).color, sample: el.textContent.trim().slice(0,30) });
    }
  });
  console.table(bad);
  return { invisibleTextTypes: bad.length, items: bad };
})();
```

Run in **both** themes. Any hit with no clipped gradient behind it = invisible text. Fix: reset `-webkit-text-fill-color: currentColor` in that theme (match the specificity of the rule that set it transparent), or remove the gradient-text rule entirely.

---

## C. Corner-badge overlap detector

Absolutely-positioned corner badges (`$`, "Топ", "New", status dots) collide when two land in the same corner of the same card — one hides the other. This flags overlapping pairs.

```js
(() => {
  const hits = [];
  document.querySelectorAll('.card, [data-card], article').forEach(card => {
    const badges = [...card.children, ...card.querySelectorAll(':scope > * > .card-badge')]
      .filter(el => el.nodeType===1 && getComputedStyle(el).position==='absolute');
    // include ::after/::before corner pseudo badges by checking computed content
    const boxes = badges.map(b => ({ el:b, r:b.getBoundingClientRect() })).filter(x=>x.r.width>0);
    for (let i=0;i<boxes.length;i++) for (let j=i+1;j<boxes.length;j++) {
      const a=boxes[i].r, b=boxes[j].r;
      const overlap = !(a.right<b.left||a.left>b.right||a.bottom<b.top||a.top>b.bottom);
      if (overlap) hits.push({ card: card.querySelector('.card-title,h2,h3')?.textContent.trim().slice(0,24), a: boxes[i].el.className, b: boxes[j].el.className });
    }
  });
  console.table(hits);
  return { overlappingBadgePairs: hits.length, hits };
})();
```

Note: CSS `::before`/`::after` pseudo badges (e.g. a `content:'Топ'` ribbon) are not in the DOM — also check them by reading `getComputedStyle(card, '::after').content` and comparing its `top`/`right` to the real badge's box.

---

## D. State exercise protocol (don't trust the default screenshot)

A redesign is not verified until every interactive mode is exercised. Toggle each, then re-run A, B, C. **The combinatorial matrix is mandatory** — bugs hide at intersections (featured × paid, dark × list-view, empty × filtered).

```js
// 1. THEME — toggle and re-audit
document.documentElement.classList.toggle('dark');   // or the project's theme mechanism

// 2. VIEW MODE — exercise every layout toggle
document.getElementById('listViewHeader')?.click();  // grid → list (and back)

// 3. EMPTY / NO-RESULTS — type a query that matches nothing
const q = document.querySelector('input[type="text"], input[type="search"]');
if (q) { q.value = 'zzqx-no-match'; q.dispatchEvent(new Event('input',{bubbles:true})); }

// 4. FILTERS — activate each filter, check counts + empty state
document.querySelectorAll('.quick-filter-btn,[data-filter]').forEach(b => { /* click, observe */ });

// 5. KEYBOARD FOCUS — Tab through; every interactive element must show a visible ring
//    (manual: press Tab; or check :focus-visible styles exist for buttons/links/cards)
```

**The required matrix for a redesign:**

```
themes:      light, dark
view modes:  grid, list (and any others)
states:      default, filtered, empty/no-results, loading, error
card tiers:  normal, featured, paid, featured+paid
viewports:   390, 768, 1280
```

Run A (contrast) and B (invisible text) in **every theme**. Run C (badge overlap) on **featured+paid** cards. Exercise D for **every** toggle. Screenshot the intersections, not just the homepage hero.

---

## E. Filter / visibility parity — does `[hidden]` actually hide?

A filter or search that sets `el.hidden = true` (or toggles the `hidden` attribute) only hides if no CSS `display` rule on the element wins over the UA `[hidden]{display:none}`. `.card{display:flex}` (common) **defeats it** — the attribute is set, the card stays on screen. An attribute-level test (`querySelectorAll(':not([hidden])').length`) passes while the page is visually broken. **Apply a filter first, then run this:**

```js
(() => {
  const cards = [...document.querySelectorAll('.card,[data-card],.cards-grid > *')];
  const attrHidden  = cards.filter(c => c.hidden || c.hasAttribute('hidden')).length;
  const reallyShown = cards.filter(c => c.offsetParent !== null).length;
  const attrShown   = cards.length - attrHidden;
  return { total: cards.length, attrShown, reallyShown,
    BUG: attrShown !== reallyShown
      ? 'a display rule defeats [hidden] — add `.card[hidden]{display:none!important}`'
      : 'ok' };
})();
```

Rule of thumb: any element you hide via the `hidden` attribute needs `[hidden]{display:none!important}` if it also has an explicit `display`.

---

## F. Accessible-text / bot layer — what Googlebot, a screen-reader and `innerText` actually get

The rendered pixels can be perfect while the **text layer** is full of junk: lone status glyphs (`$`), decorative numbers that duplicate an `<ol>`'s own numbering ("1, 1 …" to a screen-reader), category labels mangled by abbreviation. Audit it directly:

```js
(() => {
  const txt = document.body.innerText;
  // stray status glyphs sitting on their own line (a decorative $ leaking into text)
  const loneGlyphs = (txt.match(/(?:^|\n)\s*[$€₽]\s*(?=\n|$)/g) || []).length;
  // decorative numbers NOT hidden from the a11y tree (list ranks, plot/radar nodes, count badges)
  const decoNums = [...document.querySelectorAll('span,div,b,strong')].filter(e =>
    e.children.length === 0 && /^\d{1,3}$/.test((e.textContent || '').trim())
    && /rank|num|node|badge|count/i.test(e.className)
    && e.getAttribute('aria-hidden') !== 'true'
    && !e.closest('[role="img"]')
  ).map(e => e.className);
  return { loneStatusGlyphsInText: loneGlyphs, decorativeNumbersExposed: decoNums };
})();
```

Fixes: decorative glyphs/numbers → `aria-hidden="true"` (or wrap a visual plot in `role="img"` with an `aria-label`); a status symbol that must stay a JS data hook → hide it visually *and* from text (`display:none`) and read its value via `textContent`. Re-check that `innerText` contains zero lone glyphs and that ordered lists aren't double-numbered.

---

## G. Count / version parity — no-JS fallback and cache desync

For SEO, the no-JS HTML and every cached/CDN snapshot must agree with the live JS-rendered page.

```js
// static fallbacks must equal the JS-computed values (no "—" placeholders for crawlers)
[...document.querySelectorAll('[id$="Count"],[data-count]')].map(e => ({ id: e.id, shown: e.textContent.trim() }));
// then compare to raw HTML: view-source should show the SAME numbers, not "—" or a stale count
```

If different bots get 396 vs 450, suspect: CDN/edge cache, `Cache-Control` on the HTML, a Service Worker, or a stale uploaded file. Counters rendered only by JS should ship with a **real** static fallback in the markup, not a placeholder.

---

## H. JS-injected layout integrity — one throw blanks half the page

A single uncaught JS error stops **all** subsequent script: tool cards never inject, `IntersectionObserver` reveals never fire, and `.reveal{opacity:0}` elements stay invisible. The page looks like a "broken empty middle" while the hero, static labels and footer render fine — a misleading signal that hides the real cause (the console error).

```js
page.on('pageerror', e => { throw new Error('JS threw, layout will be partial: ' + e.message); });
// after load, prove the JS actually ran:
const ran = await page.evaluate(() => ({
  injected: document.querySelectorAll('[data-injected],.tool,.card').length,
  revealed: document.querySelectorAll('.reveal.in,.is-in').length,
  revealTotal: document.querySelectorAll('.reveal,[class*="reveal"]').length,
}));
if (ran.revealTotal && ran.revealed === 0) throw new Error('No reveals fired — suspect a JS throw before IO setup');
```

**Real miss (chexter.ru pilot 2026-05-31):** `id="g-seo"` referenced in JS as a bare global `g_seo` → `g_seo is not defined`. A hyphenated `id` does **not** create a usable named global; the throw killed card injection *and* every scroll reveal. Always `document.getElementById('g-seo')`, never rely on named-element globals.

---

## I. Mobile overflow — trust `scrollWidth`, and `min-width:0` on track children

`getBoundingClientRect().right > viewport` flags **clipped** absolute children (a sweep line inside `overflow:hidden`) that don't actually extend the page. The source of truth for horizontal overflow is `document.documentElement.scrollWidth`.

```js
const ov = await page.evaluate(() => ({ sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth }));
if (ov.sw > ov.cw) {/* find the real culprit */
  const wide = await page.evaluate(() => [...document.querySelectorAll('*')]
    .filter(el => el.getBoundingClientRect().right > innerWidth + 1 && getComputedStyle(el).position !== 'absolute')
    .map(el => el.tagName + '.' + (el.className||'').toString().split(' ')[0]).slice(0,8));
}
```

**Real miss (chexter.ru pilot):** 451px > 390px viewport. Cause: CSS Grid/Flex children default to `min-width:auto`, so a `1fr` track can't shrink below its content's min-content. Fix: `min-width:0` on grid/flex track children (and on flex `input`s). Absolute children inside `overflow:hidden` were a red herring — `scrollWidth` was the real signal.

---

## J. Reveal-on-scroll + local render of a deployed app

**Screenshots:** a `fullPage` shot does **not** trigger `IntersectionObserver` for below-the-fold elements — they stay at `opacity:0`. Scroll through first, then capture.

```js
const h = await page.evaluate(() => document.body.scrollHeight);
for (let y = 0; y <= h; y += 500) { await page.evaluate(yy => scrollTo(0, yy), y); await page.waitForTimeout(160); }
await page.evaluate(() => scrollTo(0, 0)); await page.waitForTimeout(800);
await page.screenshot({ fullPage: true, path });
```

**Local render when the entry point hardcodes a prod base path:** some apps `define()` an absolute server path in `public/index.php` (e.g. `/var/www/.../app`), so `php -S` 500s locally — and "PHP doesn't run here" gets mistaken for an environment limit. Don't edit the committed entry. Serve a **local-only router shim** that overrides the constant, returns `false` for real static files, then includes the app's autoload + bootstrap:

```php
// router.local.php — php -S 127.0.0.1:8130 -t public router.local.php   (never deploy)
$base = __DIR__ . '/..';                      // local project root
$uri = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);
if ($uri !== '/' && is_file($base.'/public'.$uri)) return false;   // let the server serve assets
define('CHEXTER_BASE_PATH', $base);           // the constant the prod index.php hardcodes
require $base.'/app/Core/Autoloader.php'; App\Core\Autoloader::register($base.'/app');
($app = require $base.'/config/bootstrap.php')->run();
```

This unblocked true before/after verification on chexter.ru (HTTP 200 + axe 0 locally) without touching the deploy entry.

---

## How to use in a Playwright/agent workflow

```js
// pattern: navigate → set state → evaluate(snippet) → assert
await page.emulateMedia({ colorScheme: 'dark' });           // or add the theme class
await page.evaluate(() => document.documentElement.classList.add('dark'));
const invisible = await page.evaluate(/* snippet B */);
if (invisible.invisibleTextTypes > 0) throw new Error('Invisible text in dark: ' + JSON.stringify(invisible.items));
```

---

*Reference version: global-design-skill v1.9.10 — `references/live-audit-snippets.md`*
*Related: `rules/19-contrast-standards.md` (R14 text-fill traps), `checklists/global-design-review.md` (Live Verification), `blueprints/redesign-existing-page.md` (Phase 6), `references/sources.md` (validation tools)*
