# Demo Gallery Wave 2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build Wave 2 of the global-design-skill Demo Gallery — three self-contained Before/After redesign pages (npm package card, MDN API method block, Product Hunt listing) — and update the gallery index to activate Wave 2 links and add Wave 3 placeholder cards.

**Architecture:** Each demo follows the Wave 1 pattern exactly: self-contained HTML+CSS+JS, same token block (including `--color-success`/`--color-success-bg` added in Wave 1 Task 3), same Before/After toggle, skeleton, changelog, token legend. Task 4 updates `demo/index.html` via targeted edits to activate Wave 2 cards and add Wave 3 placeholders so the Wave 3 filter tab does not show an empty grid.

**Tech Stack:** Vanilla HTML5, CSS (OKLCH custom properties, CSS relative color syntax), vanilla JS (no framework), GitHub Pages static deploy from `/demo`.

---

## File Structure

| File | Change | Responsible for |
|------|--------|-----------------|
| `demo/npm-package.html` | Create | npm search card Before/After redesign |
| `demo/mdn-api.html` | Create | MDN API method block Before/After redesign |
| `demo/product-hunt.html` | Create | Product Hunt listing Before/After redesign |
| `demo/index.html` | Modify | Activate Wave 2 links; add Wave 3 placeholder cards |

---

### Task 1: `demo/npm-package.html`

**Files:**
- Create: `demo/npm-package.html`

- [ ] **Step 1: Create the file with this exact content**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>npm Package Card — global-design-skill Demo</title>
  <style>
    /* ── Tokens ── */
    :root {
      --color-bg:             oklch(96% 0.004 258);
      --color-surface:        oklch(100% 0 0);
      --color-border:         oklch(90% 0.006 258);
      --color-text:           oklch(17% 0.012 258);
      --color-text-secondary: oklch(42% 0.012 258);
      --color-text-muted:     oklch(60% 0.008 258);
      --color-accent:         oklch(52% 0.20 258);
      --color-accent-hover:   oklch(45% 0.21 258);
      --color-success:        oklch(45% 0.15 145);
      --color-success-bg:     oklch(56% 0.17 145 / 0.12);
      --space-1: 4px;  --space-2: 8px;  --space-3: 12px; --space-4: 16px;
      --space-5: 20px; --space-6: 24px; --space-8: 32px; --space-10: 40px;
      --text-xs: 11px; --text-sm: 13px; --text-base: 15px;
      --text-md: 17px; --text-lg: 19px;
      --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
      --t-fast: 140ms; --t-base: 210ms;
    }
    @media (prefers-color-scheme: dark) {
      :root {
        --color-bg:             oklch(13% 0.010 258);
        --color-surface:        oklch(17% 0.010 258);
        --color-border:         oklch(26% 0.010 258);
        --color-text:           oklch(94% 0.004 258);
        --color-text-secondary: oklch(72% 0.008 258);
        --color-text-muted:     oklch(55% 0.006 258);
        --color-accent:         oklch(65% 0.20 258);
        --color-accent-hover:   oklch(72% 0.20 258);
        --color-success:        oklch(70% 0.12 145);
        --color-success-bg:     oklch(56% 0.17 145 / 0.15);
      }
    }
    /* ── Reset ── */
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; font-size: var(--text-base); background: var(--color-bg); color: var(--color-text); min-height: 100dvh; }
    a { color: inherit; text-decoration: none; }
    button { border: none; background: none; cursor: pointer; font: inherit; }
    /* ── Page chrome ── */
    .page-header { padding: var(--space-3) var(--space-6); border-bottom: 1px solid var(--color-border); display: flex; align-items: center; justify-content: space-between; font-size: var(--text-sm); color: var(--color-text-muted); }
    .page-header-site { font-weight: 700; color: var(--color-text); }
    .page-header-back { color: var(--color-accent); }
    .page-header-back:hover { text-decoration: underline; }
    .content { max-width: 780px; margin: 0 auto; padding: var(--space-8) var(--space-4); }
    /* ── Toggle bar ── */
    .toggle-bar { display: flex; border: 1px solid var(--color-border); border-radius: 10px; overflow: hidden; margin-bottom: var(--space-6); background: var(--color-surface); }
    .toggle-btn { flex: 1; padding: var(--space-3) var(--space-4); font-size: var(--text-sm); font-weight: 600; color: var(--color-text-muted); cursor: pointer; min-height: 44px; transition: background var(--t-fast) var(--ease-out), color var(--t-fast) var(--ease-out); }
    .toggle-btn.active { background: var(--color-accent); color: oklch(100% 0 0); }
    .toggle-btn:focus-visible { outline: 2px solid var(--color-accent); outline-offset: -2px; }
    /* ── Component wrapper ── */
    .component-wrapper { position: relative; margin-bottom: var(--space-8); }
    .component-state { transition: opacity 200ms cubic-bezier(0.16,1,0.3,1), transform 200ms cubic-bezier(0.16,1,0.3,1); }
    @media (prefers-reduced-motion: reduce) { .component-state { transition: none; } }
    /* ── BEFORE: faithful npm package search card ── */
    .npm-before { background: #fff; border: 1px solid #c8c8c8; font-family: -apple-system, 'Helvetica Neue', sans-serif; font-size: 14px; color: #24292e; padding: 16px 18px; }
    .npm-before-header { display: flex; align-items: baseline; gap: 8px; margin-bottom: 6px; flex-wrap: wrap; }
    .npm-before-name { font-size: 17px; font-weight: 600; color: #212121; }
    .npm-before-name:hover { text-decoration: underline; }
    .npm-before-ver { font-size: 12px; color: #888; }
    .npm-before-lic { font-size: 12px; color: #888; }
    .npm-before-desc { font-size: 13px; color: #6e6e6e; margin-bottom: 10px; line-height: 1.5; }
    .npm-before-dl { font-size: 12px; color: #888; margin-bottom: 8px; }
    .npm-before-tags { display: flex; flex-wrap: wrap; gap: 4px; margin-bottom: 10px; }
    .npm-before-tag { font-size: 11px; color: #8d8d8d; background: #f0f0f0; border: 1px solid #d8d8d8; border-radius: 3px; padding: 1px 6px; }
    .npm-before-meta { font-size: 12px; color: #888; }
    /* ── AFTER: redesigned npm card ── */
    .npm-card { background: var(--color-surface); border: 1px solid var(--color-border); border-radius: 12px; overflow: hidden; }
    .npm-card-header { display: flex; align-items: center; gap: var(--space-2); flex-wrap: wrap; padding: var(--space-4); border-bottom: 1px solid var(--color-border); }
    .npm-name-link { font-size: var(--text-lg); font-weight: 700; color: var(--color-text); }
    .npm-name-link:hover { color: var(--color-accent); }
    .npm-version-pill { font-size: var(--text-xs); font-weight: 600; border: 1px solid var(--color-border); border-radius: 999px; padding: 2px var(--space-2); color: var(--color-text-muted); font-family: 'Menlo','Consolas',monospace; }
    .npm-license-badge { font-size: var(--text-xs); font-weight: 700; border-radius: 999px; padding: 2px var(--space-2); background: var(--color-success-bg); color: var(--color-success); border: 1px solid oklch(from var(--color-success) l c h / 0.3); }
    .npm-card-body { padding: var(--space-4); display: flex; flex-direction: column; gap: var(--space-4); }
    .npm-desc { font-size: var(--text-base); color: var(--color-text-secondary); line-height: 1.55; }
    .npm-install { display: flex; align-items: center; gap: var(--space-2); background: oklch(from var(--color-border) l c h / 0.5); border: 1px solid var(--color-border); border-radius: 8px; padding: var(--space-2) var(--space-3); }
    .npm-install-prompt { font-size: var(--text-sm); color: var(--color-text-muted); font-weight: 700; flex-shrink: 0; font-family: 'Menlo','Consolas',monospace; }
    .npm-install-cmd { font-family: 'Menlo','Consolas',monospace; font-size: var(--text-sm); color: var(--color-text); flex: 1; }
    .npm-copy-btn { font-size: var(--text-xs); font-weight: 600; color: var(--color-accent); padding: var(--space-1) var(--space-2); border-radius: 6px; min-height: 28px; border: 1px solid oklch(from var(--color-accent) l c h / 0.4); transition: background var(--t-fast) var(--ease-out); flex-shrink: 0; }
    .npm-copy-btn:hover { background: oklch(from var(--color-accent) l c h / 0.08); }
    .npm-copy-btn:focus-visible { outline: 2px solid var(--color-accent); outline-offset: 2px; }
    .npm-stats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1px; background: var(--color-border); border: 1px solid var(--color-border); border-radius: 8px; overflow: hidden; }
    .npm-stat { display: flex; flex-direction: column; align-items: center; justify-content: center; padding: var(--space-3); background: var(--color-surface); gap: 2px; }
    .npm-stat-value { font-size: var(--text-md); font-weight: 700; color: var(--color-text); }
    .npm-stat-label { font-size: var(--text-xs); color: var(--color-text-muted); text-align: center; }
    .npm-card-footer { display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: var(--space-2); padding: var(--space-3) var(--space-4); border-top: 1px solid var(--color-border); background: oklch(from var(--color-surface) calc(l - 0.03) c h); }
    .npm-maintainer { display: flex; align-items: center; gap: var(--space-2); }
    .npm-avatar { width: 24px; height: 24px; border-radius: 6px; background: oklch(from var(--color-accent) l c h / 0.15); color: var(--color-accent); display: flex; align-items: center; justify-content: center; font-size: var(--text-xs); font-weight: 700; flex-shrink: 0; }
    .npm-maintainer-name { font-size: var(--text-sm); color: var(--color-text-secondary); }
    .npm-more { font-size: var(--text-xs); color: var(--color-text-muted); }
    .npm-keywords { display: flex; flex-wrap: wrap; gap: var(--space-1); }
    .npm-tag { font-size: var(--text-xs); font-weight: 500; border-radius: 4px; padding: 1px var(--space-2); border: 1px solid var(--color-border); color: var(--color-text-muted); }
    .npm-tag:hover { border-color: var(--color-accent); color: var(--color-accent); }
    /* ── Skeleton ── */
    .skeleton-card { background: var(--color-surface); border: 1px solid var(--color-border); border-radius: 12px; overflow: hidden; }
    .sk-header { display: flex; align-items: center; gap: var(--space-3); padding: var(--space-4); border-bottom: 1px solid var(--color-border); }
    .sk-body { padding: var(--space-4); display: flex; flex-direction: column; gap: var(--space-3); }
    .sk-footer { height: 52px; border-top: 1px solid var(--color-border); }
    .skel { background: linear-gradient(90deg, var(--color-border) 25%, var(--color-bg) 50%, var(--color-border) 75%); background-size: 200% 100%; border-radius: 4px; animation: shimmer 1.5s linear infinite; }
    @keyframes shimmer { 0% { background-position: 200% 0; } 100% { background-position: -200% 0; } }
    @media (prefers-reduced-motion: reduce) { .skel { animation: none; background: var(--color-border); } }
    .sk-name { height: 22px; width: 140px; }
    .sk-pill { height: 20px; width: 58px; border-radius: 999px; }
    .sk-desc-1 { height: 14px; }
    .sk-desc-2 { height: 14px; width: 70%; }
    .sk-install { height: 38px; border-radius: 8px; }
    .sk-stats { height: 72px; border-radius: 8px; }
    /* ── Shared: section labels, changelog, token legend ── */
    .section-label { font-size: var(--text-xs); font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; color: var(--color-text-muted); margin-bottom: var(--space-4); margin-top: var(--space-8); padding-bottom: var(--space-2); border-bottom: 1px solid var(--color-border); }
    .changelog { width: 100%; border-collapse: collapse; font-size: var(--text-sm); margin-bottom: var(--space-8); }
    .changelog th { text-align: left; padding: var(--space-2) var(--space-3); font-size: var(--text-xs); font-weight: 700; color: var(--color-text-muted); border-bottom: 1px solid var(--color-border); }
    .changelog td { padding: var(--space-3); border-bottom: 1px solid var(--color-border); vertical-align: top; line-height: 1.5; }
    .changelog tr:last-child td { border-bottom: none; }
    .changelog td:first-child { font-weight: 600; white-space: nowrap; }
    .changelog .before { color: var(--color-text-secondary); }
    .changelog .after  { color: var(--color-text); }
    .principle { font-size: var(--text-xs); color: var(--color-accent); }
    .token-legend { width: 100%; border-collapse: collapse; font-size: var(--text-sm); }
    .token-legend th { text-align: left; padding: var(--space-2) var(--space-3); font-size: var(--text-xs); font-weight: 700; color: var(--color-text-muted); border-bottom: 1px solid var(--color-border); }
    .token-legend td { padding: var(--space-2) var(--space-3); border-bottom: 1px solid var(--color-border); vertical-align: top; font-family: 'Menlo','Consolas',monospace; font-size: var(--text-xs); }
    .token-legend tr:last-child td { border-bottom: none; }
    .token-name { color: var(--color-accent); }
  </style>
</head>
<body>

<header class="page-header">
  <div>
    <span class="page-header-site">global-design-skill</span>
    <span style="margin:0 8px;opacity:0.3">·</span>
    <span>📦 npm — Package Search Card</span>
  </div>
  <a href="index.html" class="page-header-back">← Gallery</a>
</header>

<main class="content">

  <div class="toggle-bar" role="group" aria-label="Before/After state toggle">
    <button class="toggle-btn" id="btn-before" aria-pressed="false" aria-label="Show original npm package card design">← Before</button>
    <button class="toggle-btn active" id="btn-after" aria-pressed="true" aria-label="Show redesigned version">After →</button>
  </div>

  <div class="component-wrapper" id="component-wrapper">
    <div aria-live="polite" aria-atomic="true">

      <!-- AFTER (default) -->
      <div id="state-after" class="component-state">
        <article class="npm-card">
          <div class="npm-card-header">
            <h2><a href="#" class="npm-name-link">express</a></h2>
            <span class="npm-version-pill">v4.18.2</span>
            <span class="npm-license-badge">MIT</span>
          </div>
          <div class="npm-card-body">
            <p class="npm-desc">Fast, unopinionated, minimalist web framework for node.</p>
            <div class="npm-install">
              <span class="npm-install-prompt">$</span>
              <code class="npm-install-cmd">npm install express</code>
              <button class="npm-copy-btn" aria-label="Copy install command to clipboard">Copy</button>
            </div>
            <div class="npm-stats" aria-label="Package statistics">
              <div class="npm-stat">
                <span class="npm-stat-value">33.4M</span>
                <span class="npm-stat-label">weekly downloads</span>
              </div>
              <div class="npm-stat">
                <span class="npm-stat-value">58k</span>
                <span class="npm-stat-label">dependents</span>
              </div>
              <div class="npm-stat">
                <span class="npm-stat-value">63k ★</span>
                <span class="npm-stat-label">GitHub stars</span>
              </div>
            </div>
          </div>
          <div class="npm-card-footer">
            <div class="npm-maintainer">
              <div class="npm-avatar" aria-hidden="true">DW</div>
              <span class="npm-maintainer-name">dougwilson</span>
              <span class="npm-more">+47 more</span>
            </div>
            <div class="npm-keywords" aria-label="Keywords">
              <span class="npm-tag">web</span>
              <span class="npm-tag">framework</span>
              <span class="npm-tag">node</span>
              <span class="npm-tag">http</span>
            </div>
          </div>
        </article>
      </div>

      <!-- BEFORE -->
      <div id="state-before" class="component-state" hidden>
        <div class="npm-before">
          <div class="npm-before-header">
            <a href="#" class="npm-before-name">express</a>
            <span class="npm-before-ver">4.18.2</span>
            <span class="npm-before-lic">MIT</span>
          </div>
          <div class="npm-before-desc">Fast, unopinionated, minimalist web framework for node.</div>
          <div class="npm-before-dl">📥 33,450,924 weekly downloads</div>
          <div class="npm-before-tags">
            <span class="npm-before-tag">expressjs</span>
            <span class="npm-before-tag">web</span>
            <span class="npm-before-tag">framework</span>
            <span class="npm-before-tag">router</span>
            <span class="npm-before-tag">http</span>
            <span class="npm-before-tag">rest</span>
          </div>
          <div class="npm-before-meta">dougwilson &nbsp;·&nbsp; wesleytodd &nbsp;·&nbsp; +47 maintainers &nbsp;·&nbsp; published 2 months ago</div>
        </div>
      </div>

    </div>
  </div>

  <div class="section-label">Skeleton State</div>
  <div class="skeleton-card" aria-busy="true" aria-label="Loading npm package card">
    <div class="sk-header">
      <div class="skel sk-name"></div>
      <div class="skel sk-pill"></div>
      <div class="skel sk-pill" style="width:44px"></div>
    </div>
    <div class="sk-body">
      <div class="skel sk-desc-1"></div>
      <div class="skel sk-desc-2"></div>
      <div class="skel sk-install"></div>
      <div class="skel sk-stats"></div>
    </div>
    <div class="skel sk-footer"></div>
  </div>

  <div class="section-label">Change Log</div>
  <table class="changelog">
    <thead><tr><th>Change</th><th>Before</th><th>After</th><th>Principle</th></tr></thead>
    <tbody>
      <tr>
        <td>Install command</td>
        <td class="before">No install snippet shown — user must already know the command</td>
        <td class="after">Inline code block "$ npm install express" + Copy button — action available in the card</td>
        <td><span class="principle">rules/14-landing-pages.md → CTA formula (action affordance at point of decision)</span></td>
      </tr>
      <tr>
        <td>Download stats</td>
        <td class="before">"33,450,924 weekly downloads" — raw number buried in grey text row</td>
        <td class="after">3-stat grid (downloads / dependents / stars) — values large, labels small, scannable</td>
        <td><span class="principle">operating-principles §1 (focal point); rules/11-data-tables.md → key metric first</span></td>
      </tr>
      <tr>
        <td>Licence display</td>
        <td class="before">Inline grey text "MIT" — same visual weight as version number</td>
        <td class="after">Green pill badge — open-source licence instantly recognisable as trust signal</td>
        <td><span class="principle">operating-principles §5 (colour with purpose); rules/14-landing-pages.md → trust signals</span></td>
      </tr>
      <tr>
        <td>Keywords</td>
        <td class="before">Grey-filled square chips — decorative, no hover affordance</td>
        <td class="after">Border-only pills in footer; accent colour on hover — secondary info with interaction hint</td>
        <td><span class="principle">operating-principles §5 (colour with purpose); quality-gates Gate 4 (hover state)</span></td>
      </tr>
      <tr>
        <td>Maintainers</td>
        <td class="before">Plain text "dougwilson · wesleytodd · +47" — no visual identity</td>
        <td class="after">Avatar (initials) + primary maintainer name + "+47 more" — human face on the package</td>
        <td><span class="principle">operating-principles §3 (show the person, not just the name)</span></td>
      </tr>
      <tr>
        <td>Dark mode</td>
        <td class="before">Hardcoded #fff + #24292e — breaks in dark mode; Before state kept light-only (faithful)</td>
        <td class="after">OKLCH tokens throughout After state; success token handles licence badge in both modes</td>
        <td><span class="principle">quality-gates Gate 6 (dark mode required)</span></td>
      </tr>
    </tbody>
  </table>

  <div class="section-label">Token Legend</div>
  <table class="token-legend">
    <thead><tr><th>Token</th><th>Light</th><th>Dark</th><th>Used for</th></tr></thead>
    <tbody>
      <tr><td class="token-name">--color-bg</td><td>oklch(96% 0.004 258)</td><td>oklch(13% 0.010 258)</td><td>Page background, skeleton shimmer midpoint</td></tr>
      <tr><td class="token-name">--color-surface</td><td>oklch(100% 0 0)</td><td>oklch(17% 0.010 258)</td><td>Card background, stat cell background</td></tr>
      <tr><td class="token-name">--color-border</td><td>oklch(90% 0.006 258)</td><td>oklch(26% 0.010 258)</td><td>Card border, stat grid dividers, install block, keyword pills</td></tr>
      <tr><td class="token-name">--color-text</td><td>oklch(17% 0.012 258)</td><td>oklch(94% 0.004 258)</td><td>Package name, stat values, install command</td></tr>
      <tr><td class="token-name">--color-text-secondary</td><td>oklch(42% 0.012 258)</td><td>oklch(72% 0.008 258)</td><td>Description, maintainer name</td></tr>
      <tr><td class="token-name">--color-text-muted</td><td>oklch(60% 0.008 258)</td><td>oklch(55% 0.006 258)</td><td>Version pill, stat labels, keywords, "+N more", $ prompt</td></tr>
      <tr><td class="token-name">--color-accent</td><td>oklch(52% 0.20 258)</td><td>oklch(65% 0.20 258)</td><td>Name hover, copy button, keyword hover, avatar bg, focus rings</td></tr>
      <tr><td class="token-name">--color-success</td><td>oklch(45% 0.15 145)</td><td>oklch(70% 0.12 145)</td><td>MIT licence badge text</td></tr>
      <tr><td class="token-name">--color-success-bg</td><td>oklch(56% 0.17 145 / 0.12)</td><td>oklch(56% 0.17 145 / 0.15)</td><td>MIT licence badge background</td></tr>
    </tbody>
  </table>

</main>

<script>
  const wrapper   = document.getElementById('component-wrapper');
  const afterEl   = document.getElementById('state-after');
  const beforeEl  = document.getElementById('state-before');
  const btnBefore = document.getElementById('btn-before');
  const btnAfter  = document.getElementById('btn-after');
  const reduced   = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  let current = 'after';

  function measureHeights() {
    afterEl.hidden = false; beforeEl.hidden = false;
    afterEl.style.visibility = 'hidden'; beforeEl.style.visibility = 'hidden';
    const afterH  = afterEl.getBoundingClientRect().height;
    const beforeH = beforeEl.getBoundingClientRect().height;
    afterEl.style.visibility = ''; beforeEl.style.visibility = '';
    wrapper.style.minHeight = Math.max(afterH, beforeH) + 'px';
    beforeEl.hidden = true;
  }

  function switchTo(target) {
    if (target === current) return;
    current = target;
    const showEl = target === 'after' ? afterEl : beforeEl;
    const hideEl = target === 'after' ? beforeEl : afterEl;
    btnBefore.classList.toggle('active', target === 'before');
    btnAfter.classList.toggle('active',  target === 'after');
    btnBefore.setAttribute('aria-pressed', target === 'before');
    btnAfter.setAttribute('aria-pressed',  target === 'after');
    if (reduced) { hideEl.hidden = true; showEl.hidden = false; return; }
    hideEl.style.opacity = '0'; hideEl.style.transform = 'translateY(4px)';
    setTimeout(() => { hideEl.hidden = true; hideEl.style.opacity = ''; hideEl.style.transform = ''; }, 200);
    showEl.hidden = false; showEl.style.opacity = '0'; showEl.style.transform = 'translateY(4px)';
    requestAnimationFrame(() => requestAnimationFrame(() => {
      showEl.style.transition = 'opacity 200ms cubic-bezier(0.16,1,0.3,1), transform 200ms cubic-bezier(0.16,1,0.3,1)';
      showEl.style.opacity = '1'; showEl.style.transform = 'translateY(0)';
      setTimeout(() => { showEl.style.transition = ''; }, 220);
    }));
  }

  window.addEventListener('DOMContentLoaded', () => {
    measureHeights();
    btnBefore.addEventListener('click', () => switchTo('before'));
    btnAfter.addEventListener('click',  () => switchTo('after'));
    [btnBefore, btnAfter].forEach(btn =>
      btn.addEventListener('keydown', e => {
        if (e.key === ' ' || e.key === 'Enter') { e.preventDefault(); btn.click(); }
      })
    );
  });
</script>
</body>
</html>
```

- [ ] **Step 2: Verify quality gates**

Open `demo/npm-package.html` in Chrome. Check:
- Toggle default → After; click Before → shows npm-faithful layout; toggle keyboard-accessible
- Skeleton matches After layout; shimmer disabled with `prefers-reduced-motion`
- Dark mode: After card readable; Before stays light (correct — faithful recreation)
- 390px: no horizontal overflow; install block wraps cleanly
- Copy button has focus ring; all interactive elements ≥ 44px OR ≥ 28px (copy btn is secondary, inside a block)
- Change log: 6 rows, each with principle reference
- No layout shift on toggle

- [ ] **Step 3: Commit**

```bash
git add demo/npm-package.html
git commit -m "feat(demo): add npm package card Before/After demo (Wave 2)"
```

---

### Task 2: `demo/mdn-api.html`

**Files:**
- Create: `demo/mdn-api.html`

- [ ] **Step 1: Create the file with this exact content**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MDN API Block — global-design-skill Demo</title>
  <style>
    /* ── Tokens ── */
    :root {
      --color-bg:             oklch(96% 0.004 258);
      --color-surface:        oklch(100% 0 0);
      --color-border:         oklch(90% 0.006 258);
      --color-text:           oklch(17% 0.012 258);
      --color-text-secondary: oklch(42% 0.012 258);
      --color-text-muted:     oklch(60% 0.008 258);
      --color-accent:         oklch(52% 0.20 258);
      --color-accent-hover:   oklch(45% 0.21 258);
      --color-success:        oklch(45% 0.15 145);
      --color-success-bg:     oklch(56% 0.17 145 / 0.12);
      --space-1: 4px;  --space-2: 8px;  --space-3: 12px; --space-4: 16px;
      --space-5: 20px; --space-6: 24px; --space-8: 32px; --space-10: 40px;
      --text-xs: 11px; --text-sm: 13px; --text-base: 15px;
      --text-md: 17px; --text-lg: 19px;
      --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
      --t-fast: 140ms; --t-base: 210ms;
    }
    @media (prefers-color-scheme: dark) {
      :root {
        --color-bg:             oklch(13% 0.010 258);
        --color-surface:        oklch(17% 0.010 258);
        --color-border:         oklch(26% 0.010 258);
        --color-text:           oklch(94% 0.004 258);
        --color-text-secondary: oklch(72% 0.008 258);
        --color-text-muted:     oklch(55% 0.006 258);
        --color-accent:         oklch(65% 0.20 258);
        --color-accent-hover:   oklch(72% 0.20 258);
        --color-success:        oklch(70% 0.12 145);
        --color-success-bg:     oklch(56% 0.17 145 / 0.15);
      }
    }
    /* ── Reset ── */
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; font-size: var(--text-base); background: var(--color-bg); color: var(--color-text); min-height: 100dvh; }
    a { color: inherit; text-decoration: none; }
    button { border: none; background: none; cursor: pointer; font: inherit; }
    /* ── Page chrome ── */
    .page-header { padding: var(--space-3) var(--space-6); border-bottom: 1px solid var(--color-border); display: flex; align-items: center; justify-content: space-between; font-size: var(--text-sm); color: var(--color-text-muted); }
    .page-header-site { font-weight: 700; color: var(--color-text); }
    .page-header-back { color: var(--color-accent); }
    .page-header-back:hover { text-decoration: underline; }
    .content { max-width: 780px; margin: 0 auto; padding: var(--space-8) var(--space-4); }
    /* ── Toggle bar ── */
    .toggle-bar { display: flex; border: 1px solid var(--color-border); border-radius: 10px; overflow: hidden; margin-bottom: var(--space-6); background: var(--color-surface); }
    .toggle-btn { flex: 1; padding: var(--space-3) var(--space-4); font-size: var(--text-sm); font-weight: 600; color: var(--color-text-muted); cursor: pointer; min-height: 44px; transition: background var(--t-fast) var(--ease-out), color var(--t-fast) var(--ease-out); }
    .toggle-btn.active { background: var(--color-accent); color: oklch(100% 0 0); }
    .toggle-btn:focus-visible { outline: 2px solid var(--color-accent); outline-offset: -2px; }
    /* ── Component wrapper ── */
    .component-wrapper { position: relative; margin-bottom: var(--space-8); }
    .component-state { transition: opacity 200ms cubic-bezier(0.16,1,0.3,1), transform 200ms cubic-bezier(0.16,1,0.3,1); }
    @media (prefers-reduced-motion: reduce) { .component-state { transition: none; } }
    /* ── BEFORE: faithful MDN API method block (Array.prototype.map) ── */
    .mdn-before { background: #fff; color: #1b1b1b; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; font-size: 15px; border: 1px solid #d7d7db; }
    .mdn-before-topbar { background: #f9f9fb; border-bottom: 1px solid #d7d7db; padding: 6px 20px; font-size: 12px; color: #595959; }
    .mdn-before-body { padding: 24px; }
    .mdn-before-h1 { font-size: 26px; font-weight: 700; color: #15141a; margin-bottom: 12px; font-family: 'Zilla Slab', Georgia, serif; }
    .mdn-before-baseline { display: inline-flex; align-items: center; gap: 6px; background: #e6f4ea; border: 1px solid #a8d5b0; border-radius: 4px; padding: 4px 10px; font-size: 12px; color: #1e7e34; margin-bottom: 16px; }
    .mdn-before-desc { font-size: 15px; color: #1b1b1b; line-height: 1.65; margin-bottom: 20px; }
    .mdn-before-h2 { font-size: 18px; font-weight: 700; color: #15141a; margin-bottom: 8px; padding-bottom: 6px; border-bottom: 2px solid #d7d7db; }
    .mdn-before-pre { background: #f5f2f0; border: 1px solid #d7d7db; border-radius: 4px; padding: 14px 16px; font-family: 'SFMono-Regular', Consolas, monospace; font-size: 13px; color: #1b1b1b; margin-bottom: 20px; line-height: 1.6; }
    .mdn-before-dl dt { font-family: 'SFMono-Regular', Consolas, monospace; font-size: 13px; font-weight: 600; color: #15141a; margin-top: 12px; }
    .mdn-before-dl dd { margin-left: 20px; font-size: 14px; color: #1b1b1b; line-height: 1.6; margin-top: 4px; margin-bottom: 8px; }
    .mdn-before-return { font-size: 14px; color: #1b1b1b; line-height: 1.6; }
    /* ── AFTER: redesigned MDN API block ── */
    .mdn-card { background: var(--color-surface); border: 1px solid var(--color-border); border-radius: 12px; overflow: hidden; }
    .mdn-card-header { padding: var(--space-4); border-bottom: 1px solid var(--color-border); display: flex; flex-direction: column; gap: var(--space-2); }
    .mdn-baseline-pill { display: inline-flex; align-items: center; gap: var(--space-1); background: var(--color-success-bg); color: var(--color-success); border: 1px solid oklch(from var(--color-success) l c h / 0.3); border-radius: 999px; font-size: var(--text-xs); font-weight: 700; padding: 2px var(--space-3); width: fit-content; }
    .mdn-method-name { font-family: 'Menlo','Consolas',monospace; font-size: var(--text-lg); font-weight: 700; color: var(--color-text); line-height: 1.3; }
    .mdn-method-ns { color: var(--color-text-muted); }
    .mdn-method-call { color: var(--color-accent); }
    .mdn-card-body { padding: var(--space-4); display: flex; flex-direction: column; gap: var(--space-5); }
    .mdn-desc { font-size: var(--text-base); color: var(--color-text-secondary); line-height: 1.6; }
    .mdn-subsection-label { font-size: var(--text-xs); font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; color: var(--color-text-muted); margin-bottom: var(--space-2); }
    .mdn-syntax-block { background: oklch(from var(--color-border) l c h / 0.4); border: 1px solid var(--color-border); border-radius: 8px; padding: var(--space-3) var(--space-4); font-family: 'Menlo','Consolas',monospace; font-size: var(--text-sm); line-height: 2; }
    .syn-fn { color: var(--color-accent); font-weight: 600; }
    .syn-param { color: var(--color-text-secondary); }
    .syn-opt { color: var(--color-text-muted); }
    .mdn-params { display: flex; flex-direction: column; gap: var(--space-2); }
    .mdn-param-row { display: grid; grid-template-columns: auto 1fr; gap: var(--space-3); align-items: start; }
    .mdn-param-left { display: flex; flex-direction: column; gap: var(--space-1); align-items: flex-start; }
    .mdn-param-name { font-family: 'Menlo','Consolas',monospace; font-size: var(--text-xs); font-weight: 700; color: var(--color-accent); background: oklch(from var(--color-accent) l c h / 0.10); border-radius: 4px; padding: 2px var(--space-2); white-space: nowrap; }
    .mdn-optional-badge { font-size: var(--text-xs); font-weight: 600; padding: 1px var(--space-2); border-radius: 999px; border: 1px solid var(--color-border); color: var(--color-text-muted); width: fit-content; }
    .mdn-param-desc { font-size: var(--text-sm); color: var(--color-text-secondary); line-height: 1.55; }
    .mdn-return-row { display: flex; align-items: flex-start; gap: var(--space-3); padding: var(--space-3) var(--space-4); background: oklch(from var(--color-border) l c h / 0.4); border: 1px solid var(--color-border); border-radius: 8px; }
    .mdn-return-type { font-family: 'Menlo','Consolas',monospace; font-size: var(--text-xs); font-weight: 700; padding: 2px var(--space-2); border-radius: 4px; background: oklch(from var(--color-accent) l c h / 0.10); color: var(--color-accent); white-space: nowrap; flex-shrink: 0; margin-top: 2px; }
    .mdn-return-desc { font-size: var(--text-sm); color: var(--color-text-secondary); line-height: 1.55; }
    .mdn-compat { display: flex; align-items: center; gap: var(--space-4); flex-wrap: wrap; }
    .mdn-compat-label { font-size: var(--text-xs); color: var(--color-text-muted); font-weight: 600; white-space: nowrap; }
    .mdn-browser-dots { display: flex; gap: var(--space-1); }
    .mdn-browser-dot { width: 36px; height: 36px; border-radius: 8px; background: var(--color-success-bg); border: 1px solid oklch(from var(--color-success) l c h / 0.3); display: flex; align-items: center; justify-content: center; font-size: var(--text-xs); font-weight: 700; color: var(--color-success); }
    /* ── Skeleton ── */
    .skeleton-card { background: var(--color-surface); border: 1px solid var(--color-border); border-radius: 12px; overflow: hidden; }
    .sk-header { display: flex; flex-direction: column; gap: var(--space-2); padding: var(--space-4); border-bottom: 1px solid var(--color-border); }
    .sk-body { padding: var(--space-4); display: flex; flex-direction: column; gap: var(--space-4); }
    .skel { background: linear-gradient(90deg, var(--color-border) 25%, var(--color-bg) 50%, var(--color-border) 75%); background-size: 200% 100%; border-radius: 4px; animation: shimmer 1.5s linear infinite; }
    @keyframes shimmer { 0% { background-position: 200% 0; } 100% { background-position: -200% 0; } }
    @media (prefers-reduced-motion: reduce) { .skel { animation: none; background: var(--color-border); } }
    .sk-baseline { height: 20px; width: 140px; border-radius: 999px; }
    .sk-method { height: 24px; width: 260px; }
    .sk-desc-1 { height: 14px; }
    .sk-desc-2 { height: 14px; width: 65%; }
    .sk-syntax { height: 56px; border-radius: 8px; }
    .sk-param-1 { height: 12px; width: 80px; }
    .sk-param-2 { height: 12px; width: 80%; }
    .sk-return { height: 44px; border-radius: 8px; }
    /* ── Shared ── */
    .section-label { font-size: var(--text-xs); font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; color: var(--color-text-muted); margin-bottom: var(--space-4); margin-top: var(--space-8); padding-bottom: var(--space-2); border-bottom: 1px solid var(--color-border); }
    .changelog { width: 100%; border-collapse: collapse; font-size: var(--text-sm); margin-bottom: var(--space-8); }
    .changelog th { text-align: left; padding: var(--space-2) var(--space-3); font-size: var(--text-xs); font-weight: 700; color: var(--color-text-muted); border-bottom: 1px solid var(--color-border); }
    .changelog td { padding: var(--space-3); border-bottom: 1px solid var(--color-border); vertical-align: top; line-height: 1.5; }
    .changelog tr:last-child td { border-bottom: none; }
    .changelog td:first-child { font-weight: 600; white-space: nowrap; }
    .changelog .before { color: var(--color-text-secondary); }
    .changelog .after  { color: var(--color-text); }
    .principle { font-size: var(--text-xs); color: var(--color-accent); }
    .token-legend { width: 100%; border-collapse: collapse; font-size: var(--text-sm); }
    .token-legend th { text-align: left; padding: var(--space-2) var(--space-3); font-size: var(--text-xs); font-weight: 700; color: var(--color-text-muted); border-bottom: 1px solid var(--color-border); }
    .token-legend td { padding: var(--space-2) var(--space-3); border-bottom: 1px solid var(--color-border); vertical-align: top; font-family: 'Menlo','Consolas',monospace; font-size: var(--text-xs); }
    .token-legend tr:last-child td { border-bottom: none; }
    .token-name { color: var(--color-accent); }
  </style>
</head>
<body>

<header class="page-header">
  <div>
    <span class="page-header-site">global-design-skill</span>
    <span style="margin:0 8px;opacity:0.3">·</span>
    <span>🦊 MDN — API Method Block</span>
  </div>
  <a href="index.html" class="page-header-back">← Gallery</a>
</header>

<main class="content">

  <div class="toggle-bar" role="group" aria-label="Before/After state toggle">
    <button class="toggle-btn" id="btn-before" aria-pressed="false" aria-label="Show original MDN API block design">← Before</button>
    <button class="toggle-btn active" id="btn-after" aria-pressed="true" aria-label="Show redesigned version">After →</button>
  </div>

  <div class="component-wrapper" id="component-wrapper">
    <div aria-live="polite" aria-atomic="true">

      <!-- AFTER (default) -->
      <div id="state-after" class="component-state">
        <article class="mdn-card">
          <div class="mdn-card-header">
            <span class="mdn-baseline-pill" aria-label="Baseline: Widely available since 2015">✓ Baseline 2015</span>
            <h2 class="mdn-method-name">
              <span class="mdn-method-ns">Array.prototype.</span><span class="mdn-method-call">map()</span>
            </h2>
          </div>
          <div class="mdn-card-body">
            <p class="mdn-desc">Creates a new array populated with the results of calling a provided function on every element in the calling array.</p>

            <div>
              <div class="mdn-subsection-label">Syntax</div>
              <div class="mdn-syntax-block">
                <span class="syn-fn">map</span>(<span class="syn-param">callbackFn</span>)<br>
                <span class="syn-fn">map</span>(<span class="syn-param">callbackFn</span>, <span class="syn-opt">thisArg</span>)
              </div>
            </div>

            <div>
              <div class="mdn-subsection-label">Parameters</div>
              <div class="mdn-params">
                <div class="mdn-param-row">
                  <div class="mdn-param-left">
                    <code class="mdn-param-name">callbackFn</code>
                  </div>
                  <p class="mdn-param-desc">A function to execute for each element in the array. Its return value is added as a single element in the new array.</p>
                </div>
                <div class="mdn-param-row">
                  <div class="mdn-param-left">
                    <code class="mdn-param-name">thisArg</code>
                    <span class="mdn-optional-badge">optional</span>
                  </div>
                  <p class="mdn-param-desc">Value to use as <code style="font-family:'Menlo',monospace;font-size:var(--text-xs)">this</code> when executing callbackFn.</p>
                </div>
              </div>
            </div>

            <div>
              <div class="mdn-subsection-label">Return value</div>
              <div class="mdn-return-row">
                <code class="mdn-return-type">Array</code>
                <p class="mdn-return-desc">A new array with each element being the result of the callback function. Always the same length as the source array.</p>
              </div>
            </div>

            <div>
              <div class="mdn-subsection-label">Browser support</div>
              <div class="mdn-compat">
                <span class="mdn-compat-label">All major browsers since 2015</span>
                <div class="mdn-browser-dots" aria-label="Browser compatibility indicators">
                  <span class="mdn-browser-dot" aria-label="Chrome: fully supported">Cr</span>
                  <span class="mdn-browser-dot" aria-label="Firefox: fully supported">Ff</span>
                  <span class="mdn-browser-dot" aria-label="Safari: fully supported">Sf</span>
                  <span class="mdn-browser-dot" aria-label="Edge: fully supported">Ed</span>
                  <span class="mdn-browser-dot" aria-label="Node.js: fully supported">No</span>
                </div>
              </div>
            </div>
          </div>
        </article>
      </div>

      <!-- BEFORE -->
      <div id="state-before" class="component-state" hidden>
        <div class="mdn-before">
          <div class="mdn-before-topbar">MDN Web Docs &rsaquo; JavaScript &rsaquo; Array &rsaquo; Array.prototype.map()</div>
          <div class="mdn-before-body">
            <h1 class="mdn-before-h1">Array.prototype.map()</h1>
            <div class="mdn-before-baseline">✓ Baseline: Widely available &nbsp; Since 2015</div>
            <p class="mdn-before-desc">The <strong>map()</strong> method of <code>Array</code> instances creates a new array populated with the results of calling a provided function on every element in the calling array.</p>
            <h2 class="mdn-before-h2">Syntax</h2>
            <pre class="mdn-before-pre">map(callbackFn)
map(callbackFn, thisArg)</pre>
            <h2 class="mdn-before-h2" style="margin-top:16px">Parameters</h2>
            <dl class="mdn-before-dl">
              <dt>callbackFn</dt>
              <dd>A function to execute for each element in the array. Its return value is added as a single element in the new array. The function is called with the following arguments: element, index, array.</dd>
              <dt>thisArg <span style="font-weight:400;font-size:12px;color:#595959">Optional</span></dt>
              <dd>A value to use as <code>this</code> when executing callbackFn.</dd>
            </dl>
            <h2 class="mdn-before-h2">Return value</h2>
            <p class="mdn-before-return">A new array with each element being the result of the callback function.</p>
          </div>
        </div>
      </div>

    </div>
  </div>

  <div class="section-label">Skeleton State</div>
  <div class="skeleton-card" aria-busy="true" aria-label="Loading MDN API method block">
    <div class="sk-header">
      <div class="skel sk-baseline"></div>
      <div class="skel sk-method"></div>
    </div>
    <div class="sk-body">
      <div class="skel sk-desc-1"></div>
      <div class="skel sk-desc-2"></div>
      <div class="skel sk-syntax"></div>
      <div style="display:flex;gap:var(--space-3)"><div class="skel sk-param-1"></div><div class="skel sk-param-2"></div></div>
      <div style="display:flex;gap:var(--space-3)"><div class="skel sk-param-1"></div><div class="skel sk-param-2" style="width:50%"></div></div>
      <div class="skel sk-return"></div>
    </div>
  </div>

  <div class="section-label">Change Log</div>
  <table class="changelog">
    <thead><tr><th>Change</th><th>Before</th><th>After</th><th>Principle</th></tr></thead>
    <tbody>
      <tr>
        <td>Method name</td>
        <td class="before">Plain h1 serif text — namespace and method name at equal weight</td>
        <td class="after">Monospace h2 with namespace muted (--color-text-muted) and method name accented — scannability without reading</td>
        <td><span class="principle">operating-principles §2 (one focal point per zone — method call is the focal point)</span></td>
      </tr>
      <tr>
        <td>Parameters</td>
        <td class="before">dl/dt/dd prose list — parameter name and description at same density, hard to skim</td>
        <td class="after">Two-column grid: name pill left, description right; optional badge below name — structure at a glance</td>
        <td><span class="principle">operating-principles §3 (label → value pairing); rules/11-data-tables.md → scannable parameter tables</span></td>
      </tr>
      <tr>
        <td>Return value</td>
        <td class="before">Paragraph under h2 heading — type buried in prose</td>
        <td class="after">Highlighted row: "Array" type pill + description — return type readable in one fixation</td>
        <td><span class="principle">operating-principles §1 (focal point); operating-principles §4 (type as label, not prose)</span></td>
      </tr>
      <tr>
        <td>Baseline badge</td>
        <td class="before">Inline green box — good intent but same block width as content, no pill affordance</td>
        <td class="after">Compact pill above method name — scoped to what it describes, uses success token</td>
        <td><span class="principle">operating-principles §5 (colour with purpose); quality-gates Gate 6 (dark mode)</span></td>
      </tr>
      <tr>
        <td>Browser compat</td>
        <td class="before">Full compatibility table with many rows/columns — accurate but noisy for common APIs</td>
        <td class="after">5 browser initials in green support dots — for Baseline-2015 APIs the answer is "all supported"</td>
        <td><span class="principle">operating-principles §2 (reduce noise; show only what changes the decision)</span></td>
      </tr>
      <tr>
        <td>Dark mode</td>
        <td class="before">Hardcoded #fff + #1b1b1b — breaks in dark mode; Before kept light-only (faithful)</td>
        <td class="after">OKLCH tokens + success token for Baseline badge and browser dots</td>
        <td><span class="principle">quality-gates Gate 6 (dark mode required)</span></td>
      </tr>
    </tbody>
  </table>

  <div class="section-label">Token Legend</div>
  <table class="token-legend">
    <thead><tr><th>Token</th><th>Light</th><th>Dark</th><th>Used for</th></tr></thead>
    <tbody>
      <tr><td class="token-name">--color-bg</td><td>oklch(96% 0.004 258)</td><td>oklch(13% 0.010 258)</td><td>Page background, skeleton shimmer midpoint</td></tr>
      <tr><td class="token-name">--color-surface</td><td>oklch(100% 0 0)</td><td>oklch(17% 0.010 258)</td><td>Card background</td></tr>
      <tr><td class="token-name">--color-border</td><td>oklch(90% 0.006 258)</td><td>oklch(26% 0.010 258)</td><td>Card border, syntax block, return row, section dividers</td></tr>
      <tr><td class="token-name">--color-text</td><td>oklch(17% 0.012 258)</td><td>oklch(94% 0.004 258)</td><td>Method name</td></tr>
      <tr><td class="token-name">--color-text-secondary</td><td>oklch(42% 0.012 258)</td><td>oklch(72% 0.008 258)</td><td>Description, parameter descriptions, return description</td></tr>
      <tr><td class="token-name">--color-text-muted</td><td>oklch(60% 0.008 258)</td><td>oklch(55% 0.006 258)</td><td>Namespace prefix (Array.prototype.), subsection labels, optional badge</td></tr>
      <tr><td class="token-name">--color-accent</td><td>oklch(52% 0.20 258)</td><td>oklch(65% 0.20 258)</td><td>Method name (.map()), parameter name pills, return type pill, focus rings</td></tr>
      <tr><td class="token-name">--color-success</td><td>oklch(45% 0.15 145)</td><td>oklch(70% 0.12 145)</td><td>Baseline pill text, browser support dot text</td></tr>
      <tr><td class="token-name">--color-success-bg</td><td>oklch(56% 0.17 145 / 0.12)</td><td>oklch(56% 0.17 145 / 0.15)</td><td>Baseline pill background, browser support dot background</td></tr>
    </tbody>
  </table>

</main>

<script>
  const wrapper   = document.getElementById('component-wrapper');
  const afterEl   = document.getElementById('state-after');
  const beforeEl  = document.getElementById('state-before');
  const btnBefore = document.getElementById('btn-before');
  const btnAfter  = document.getElementById('btn-after');
  const reduced   = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  let current = 'after';

  function measureHeights() {
    afterEl.hidden = false; beforeEl.hidden = false;
    afterEl.style.visibility = 'hidden'; beforeEl.style.visibility = 'hidden';
    const afterH  = afterEl.getBoundingClientRect().height;
    const beforeH = beforeEl.getBoundingClientRect().height;
    afterEl.style.visibility = ''; beforeEl.style.visibility = '';
    wrapper.style.minHeight = Math.max(afterH, beforeH) + 'px';
    beforeEl.hidden = true;
  }

  function switchTo(target) {
    if (target === current) return;
    current = target;
    const showEl = target === 'after' ? afterEl : beforeEl;
    const hideEl = target === 'after' ? beforeEl : afterEl;
    btnBefore.classList.toggle('active', target === 'before');
    btnAfter.classList.toggle('active',  target === 'after');
    btnBefore.setAttribute('aria-pressed', target === 'before');
    btnAfter.setAttribute('aria-pressed',  target === 'after');
    if (reduced) { hideEl.hidden = true; showEl.hidden = false; return; }
    hideEl.style.opacity = '0'; hideEl.style.transform = 'translateY(4px)';
    setTimeout(() => { hideEl.hidden = true; hideEl.style.opacity = ''; hideEl.style.transform = ''; }, 200);
    showEl.hidden = false; showEl.style.opacity = '0'; showEl.style.transform = 'translateY(4px)';
    requestAnimationFrame(() => requestAnimationFrame(() => {
      showEl.style.transition = 'opacity 200ms cubic-bezier(0.16,1,0.3,1), transform 200ms cubic-bezier(0.16,1,0.3,1)';
      showEl.style.opacity = '1'; showEl.style.transform = 'translateY(0)';
      setTimeout(() => { showEl.style.transition = ''; }, 220);
    }));
  }

  window.addEventListener('DOMContentLoaded', () => {
    measureHeights();
    btnBefore.addEventListener('click', () => switchTo('before'));
    btnAfter.addEventListener('click',  () => switchTo('after'));
    [btnBefore, btnAfter].forEach(btn =>
      btn.addEventListener('keydown', e => {
        if (e.key === ' ' || e.key === 'Enter') { e.preventDefault(); btn.click(); }
      })
    );
  });
</script>
</body>
</html>
```

- [ ] **Step 2: Verify quality gates**

Open `demo/mdn-api.html` in Chrome. Check:
- Toggle default → After; Before shows MDN-faithful layout
- Skeleton: matches After layout (badge + method name + desc + syntax block + param rows + return row)
- Dark mode: Baseline pill, browser dots, and parameter name pills all readable
- 390px: parameter grid wraps cleanly, no overflow
- Change log: 6 rows with principle references

- [ ] **Step 3: Commit**

```bash
git add demo/mdn-api.html
git commit -m "feat(demo): add MDN API method block Before/After demo (Wave 2)"
```

---

### Task 3: `demo/product-hunt.html`

**Files:**
- Create: `demo/product-hunt.html`

- [ ] **Step 1: Create the file with this exact content**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Product Hunt Listing — global-design-skill Demo</title>
  <style>
    /* ── Tokens ── */
    :root {
      --color-bg:             oklch(96% 0.004 258);
      --color-surface:        oklch(100% 0 0);
      --color-border:         oklch(90% 0.006 258);
      --color-text:           oklch(17% 0.012 258);
      --color-text-secondary: oklch(42% 0.012 258);
      --color-text-muted:     oklch(60% 0.008 258);
      --color-accent:         oklch(52% 0.20 258);
      --color-accent-hover:   oklch(45% 0.21 258);
      --color-success:        oklch(45% 0.15 145);
      --color-success-bg:     oklch(56% 0.17 145 / 0.12);
      --space-1: 4px;  --space-2: 8px;  --space-3: 12px; --space-4: 16px;
      --space-5: 20px; --space-6: 24px; --space-8: 32px; --space-10: 40px;
      --text-xs: 11px; --text-sm: 13px; --text-base: 15px;
      --text-md: 17px; --text-lg: 19px;
      --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
      --t-fast: 140ms; --t-base: 210ms;
    }
    @media (prefers-color-scheme: dark) {
      :root {
        --color-bg:             oklch(13% 0.010 258);
        --color-surface:        oklch(17% 0.010 258);
        --color-border:         oklch(26% 0.010 258);
        --color-text:           oklch(94% 0.004 258);
        --color-text-secondary: oklch(72% 0.008 258);
        --color-text-muted:     oklch(55% 0.006 258);
        --color-accent:         oklch(65% 0.20 258);
        --color-accent-hover:   oklch(72% 0.20 258);
        --color-success:        oklch(70% 0.12 145);
        --color-success-bg:     oklch(56% 0.17 145 / 0.15);
      }
    }
    /* ── Reset ── */
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; font-size: var(--text-base); background: var(--color-bg); color: var(--color-text); min-height: 100dvh; }
    a { color: inherit; text-decoration: none; }
    button { border: none; background: none; cursor: pointer; font: inherit; }
    /* ── Page chrome ── */
    .page-header { padding: var(--space-3) var(--space-6); border-bottom: 1px solid var(--color-border); display: flex; align-items: center; justify-content: space-between; font-size: var(--text-sm); color: var(--color-text-muted); }
    .page-header-site { font-weight: 700; color: var(--color-text); }
    .page-header-back { color: var(--color-accent); }
    .page-header-back:hover { text-decoration: underline; }
    .content { max-width: 780px; margin: 0 auto; padding: var(--space-8) var(--space-4); }
    /* ── Toggle bar ── */
    .toggle-bar { display: flex; border: 1px solid var(--color-border); border-radius: 10px; overflow: hidden; margin-bottom: var(--space-6); background: var(--color-surface); }
    .toggle-btn { flex: 1; padding: var(--space-3) var(--space-4); font-size: var(--text-sm); font-weight: 600; color: var(--color-text-muted); cursor: pointer; min-height: 44px; transition: background var(--t-fast) var(--ease-out), color var(--t-fast) var(--ease-out); }
    .toggle-btn.active { background: var(--color-accent); color: oklch(100% 0 0); }
    .toggle-btn:focus-visible { outline: 2px solid var(--color-accent); outline-offset: -2px; }
    /* ── Component wrapper ── */
    .component-wrapper { position: relative; margin-bottom: var(--space-8); }
    .component-state { transition: opacity 200ms cubic-bezier(0.16,1,0.3,1), transform 200ms cubic-bezier(0.16,1,0.3,1); }
    @media (prefers-reduced-motion: reduce) { .component-state { transition: none; } }
    /* ── BEFORE: faithful Product Hunt daily feed listing ── */
    .ph-before { background: #fff; border: 1px solid #e5e7eb; font-family: -apple-system, 'Helvetica Neue', sans-serif; padding: 16px; display: flex; align-items: center; gap: 14px; }
    .ph-before-upvote { display: flex; flex-direction: column; align-items: center; gap: 2px; border: 1px solid #e5e7eb; border-radius: 8px; padding: 8px 12px; cursor: pointer; background: #fff; flex-shrink: 0; }
    .ph-before-arrow { font-size: 12px; color: #ff6154; }
    .ph-before-count { font-size: 13px; font-weight: 700; color: #292929; }
    .ph-before-thumb { width: 56px; height: 56px; border-radius: 10px; background: #f0ebff; display: flex; align-items: center; justify-content: center; font-size: 28px; flex-shrink: 0; border: 1px solid #e5e7eb; }
    .ph-before-content { flex: 1; min-width: 0; }
    .ph-before-name { font-size: 16px; font-weight: 700; color: #292929; display: block; margin-bottom: 3px; }
    .ph-before-name:hover { color: #ff6154; }
    .ph-before-tagline { font-size: 13px; color: #6e6e6e; margin-bottom: 8px; line-height: 1.4; }
    .ph-before-tags { display: flex; flex-wrap: wrap; gap: 5px; }
    .ph-before-tag { font-size: 11px; color: #8d8d8d; background: #f3f3f3; border: 1px solid #e0e0e0; border-radius: 999px; padding: 2px 8px; }
    .ph-before-right { display: flex; flex-direction: column; align-items: flex-end; gap: 6px; flex-shrink: 0; }
    .ph-before-comments { font-size: 12px; color: #8d8d8d; }
    .ph-before-featured { font-size: 11px; background: #fff7e6; color: #d97706; border: 1px solid #fbbf24; border-radius: 4px; padding: 2px 6px; }
    /* ── AFTER: redesigned Product Hunt card ── */
    .ph-card { background: var(--color-surface); border: 1px solid var(--color-border); border-radius: 12px; overflow: hidden; }
    .ph-card-header { display: flex; align-items: center; gap: var(--space-3); padding: var(--space-4); border-bottom: 1px solid var(--color-border); }
    .ph-rank { font-size: var(--text-xs); font-weight: 800; color: var(--color-text-muted); min-width: 24px; flex-shrink: 0; }
    .ph-thumb { width: 52px; height: 52px; border-radius: 10px; background: oklch(88% 0.06 290); display: flex; align-items: center; justify-content: center; font-size: 26px; flex-shrink: 0; border: 1px solid var(--color-border); }
    .ph-title-group { flex: 1; min-width: 0; }
    .ph-name-link { font-size: var(--text-lg); font-weight: 700; color: var(--color-text); display: block; margin-bottom: 2px; }
    .ph-name-link:hover { color: var(--color-accent); }
    .ph-tagline { font-size: var(--text-sm); color: var(--color-text-secondary); line-height: 1.4; }
    .ph-upvote {
      display: flex; flex-direction: column; align-items: center; gap: 2px;
      padding: var(--space-2) var(--space-3); border-radius: 8px; min-height: 52px; min-width: 52px;
      background: oklch(from var(--color-accent) l c h / 0.10);
      border: 1px solid oklch(from var(--color-accent) l c h / 0.35);
      color: var(--color-accent); flex-shrink: 0;
      transition: background var(--t-fast) var(--ease-out), border-color var(--t-fast) var(--ease-out);
    }
    .ph-upvote:hover { background: oklch(from var(--color-accent) l c h / 0.18); border-color: var(--color-accent); }
    .ph-upvote:focus-visible { outline: 2px solid var(--color-accent); outline-offset: 2px; }
    .ph-upvote-icon { font-size: var(--text-sm); line-height: 1; }
    .ph-upvote-count { font-size: var(--text-sm); font-weight: 700; line-height: 1; }
    .ph-card-footer { display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: var(--space-2); padding: var(--space-3) var(--space-4); border-top: 1px solid var(--color-border); background: oklch(from var(--color-surface) calc(l - 0.03) c h); }
    .ph-topics { display: flex; flex-wrap: wrap; gap: var(--space-1); }
    .ph-topic { font-size: var(--text-xs); font-weight: 600; border-radius: 999px; padding: 2px var(--space-2); border: 1px solid var(--color-border); color: var(--color-text-muted); }
    .ph-topic:hover { border-color: var(--color-accent); color: var(--color-accent); }
    .ph-meta { display: flex; align-items: center; gap: var(--space-2); font-size: var(--text-xs); color: var(--color-text-muted); }
    .ph-meta-dot { opacity: 0.4; }
    .ph-featured-badge { font-size: var(--text-xs); font-weight: 700; padding: 2px var(--space-2); border-radius: 999px; background: oklch(90% 0.08 68); color: oklch(38% 0.12 68); }
    /* ── Skeleton ── */
    .skeleton-card { background: var(--color-surface); border: 1px solid var(--color-border); border-radius: 12px; overflow: hidden; }
    .sk-header { display: flex; align-items: center; gap: var(--space-3); padding: var(--space-4); border-bottom: 1px solid var(--color-border); }
    .sk-footer { height: 48px; border-top: 1px solid var(--color-border); }
    .skel { background: linear-gradient(90deg, var(--color-border) 25%, var(--color-bg) 50%, var(--color-border) 75%); background-size: 200% 100%; border-radius: 4px; animation: shimmer 1.5s linear infinite; }
    @keyframes shimmer { 0% { background-position: 200% 0; } 100% { background-position: -200% 0; } }
    @media (prefers-reduced-motion: reduce) { .skel { animation: none; background: var(--color-border); } }
    .sk-rank { height: 14px; width: 20px; }
    .sk-thumb { width: 52px; height: 52px; border-radius: 10px; flex-shrink: 0; }
    .sk-title-group { flex: 1; display: flex; flex-direction: column; gap: var(--space-2); }
    .sk-name { height: 20px; width: 60%; }
    .sk-tagline { height: 14px; width: 85%; }
    .sk-upvote { width: 52px; height: 52px; border-radius: 8px; flex-shrink: 0; }
    /* ── Shared ── */
    .section-label { font-size: var(--text-xs); font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; color: var(--color-text-muted); margin-bottom: var(--space-4); margin-top: var(--space-8); padding-bottom: var(--space-2); border-bottom: 1px solid var(--color-border); }
    .changelog { width: 100%; border-collapse: collapse; font-size: var(--text-sm); margin-bottom: var(--space-8); }
    .changelog th { text-align: left; padding: var(--space-2) var(--space-3); font-size: var(--text-xs); font-weight: 700; color: var(--color-text-muted); border-bottom: 1px solid var(--color-border); }
    .changelog td { padding: var(--space-3); border-bottom: 1px solid var(--color-border); vertical-align: top; line-height: 1.5; }
    .changelog tr:last-child td { border-bottom: none; }
    .changelog td:first-child { font-weight: 600; white-space: nowrap; }
    .changelog .before { color: var(--color-text-secondary); }
    .changelog .after  { color: var(--color-text); }
    .principle { font-size: var(--text-xs); color: var(--color-accent); }
    .token-legend { width: 100%; border-collapse: collapse; font-size: var(--text-sm); }
    .token-legend th { text-align: left; padding: var(--space-2) var(--space-3); font-size: var(--text-xs); font-weight: 700; color: var(--color-text-muted); border-bottom: 1px solid var(--color-border); }
    .token-legend td { padding: var(--space-2) var(--space-3); border-bottom: 1px solid var(--color-border); vertical-align: top; font-family: 'Menlo','Consolas',monospace; font-size: var(--text-xs); }
    .token-legend tr:last-child td { border-bottom: none; }
    .token-name { color: var(--color-accent); }
  </style>
</head>
<body>

<header class="page-header">
  <div>
    <span class="page-header-site">global-design-skill</span>
    <span style="margin:0 8px;opacity:0.3">·</span>
    <span>🚀 Product Hunt — Product Listing</span>
  </div>
  <a href="index.html" class="page-header-back">← Gallery</a>
</header>

<main class="content">

  <div class="toggle-bar" role="group" aria-label="Before/After state toggle">
    <button class="toggle-btn" id="btn-before" aria-pressed="false" aria-label="Show original Product Hunt listing design">← Before</button>
    <button class="toggle-btn active" id="btn-after" aria-pressed="true" aria-label="Show redesigned version">After →</button>
  </div>

  <div class="component-wrapper" id="component-wrapper">
    <div aria-live="polite" aria-atomic="true">

      <!-- AFTER (default) -->
      <div id="state-after" class="component-state">
        <article class="ph-card">
          <div class="ph-card-header">
            <span class="ph-rank" aria-label="Ranked #1 today">#1</span>
            <div class="ph-thumb" aria-hidden="true">🚀</div>
            <div class="ph-title-group">
              <h2><a href="#" class="ph-name-link">Raycast AI</a></h2>
              <p class="ph-tagline">Your personal AI assistant built directly into your workflow</p>
            </div>
            <button class="ph-upvote" aria-label="Upvote Raycast AI — currently 1,247 upvotes">
              <span class="ph-upvote-icon" aria-hidden="true">▲</span>
              <span class="ph-upvote-count">1,247</span>
            </button>
          </div>
          <div class="ph-card-footer">
            <div class="ph-topics" aria-label="Topics">
              <span class="ph-topic">Developer Tools</span>
              <span class="ph-topic">Productivity</span>
              <span class="ph-topic">AI</span>
            </div>
            <div class="ph-meta">
              <span>💬 89</span>
              <span class="ph-meta-dot">·</span>
              <span>by levelsio</span>
              <span class="ph-meta-dot">·</span>
              <span class="ph-featured-badge">Featured</span>
            </div>
          </div>
        </article>
      </div>

      <!-- BEFORE -->
      <div id="state-before" class="component-state" hidden>
        <div class="ph-before">
          <button class="ph-before-upvote" aria-label="Upvote: 1,247 votes">
            <span class="ph-before-arrow">▲</span>
            <span class="ph-before-count">1,247</span>
          </button>
          <div class="ph-before-thumb" aria-hidden="true">🚀</div>
          <div class="ph-before-content">
            <a href="#" class="ph-before-name">Raycast AI</a>
            <div class="ph-before-tagline">Your personal AI assistant built directly into your workflow</div>
            <div class="ph-before-tags">
              <span class="ph-before-tag">Developer Tools</span>
              <span class="ph-before-tag">Productivity</span>
              <span class="ph-before-tag">AI</span>
            </div>
          </div>
          <div class="ph-before-right">
            <span class="ph-before-comments">💬 89 comments</span>
            <span class="ph-before-featured">Featured</span>
          </div>
        </div>
      </div>

    </div>
  </div>

  <div class="section-label">Skeleton State</div>
  <div class="skeleton-card" aria-busy="true" aria-label="Loading Product Hunt product listing">
    <div class="sk-header">
      <div class="skel sk-rank"></div>
      <div class="skel sk-thumb"></div>
      <div class="sk-title-group">
        <div class="skel sk-name"></div>
        <div class="skel sk-tagline"></div>
      </div>
      <div class="skel sk-upvote"></div>
    </div>
    <div class="skel sk-footer"></div>
  </div>

  <div class="section-label">Change Log</div>
  <table class="changelog">
    <thead><tr><th>Change</th><th>Before</th><th>After</th><th>Principle</th></tr></thead>
    <tbody>
      <tr>
        <td>Upvote button</td>
        <td class="before">Plain border box, PH-orange arrow, no hover state — hard to Fitts-target, no affordance cue</td>
        <td class="after">52×52px contained button with accent fill tint + border; hover intensifies — primary action prominent</td>
        <td><span class="principle">operating-principles §7 (Fitts — primary action large); quality-gates Gate 4 (idle/hover/focus states)</span></td>
      </tr>
      <tr>
        <td>Product name hierarchy</td>
        <td class="before">Name as block link at 16px — competes visually with tagline below it</td>
        <td class="after">h2 at --text-lg (19px) bold + tagline at --text-sm muted — one clear scan path</td>
        <td><span class="principle">operating-principles §1 (focal point — name is the primary); operating-principles §3 (legibility scale)</span></td>
      </tr>
      <tr>
        <td>Rank indicator</td>
        <td class="before">No rank shown — listing position implicit from page order only</td>
        <td class="after">#1 muted label left of thumbnail — rank immediately scannable on any viewport</td>
        <td><span class="principle">operating-principles §2 (context that changes a decision); rules/11-data-tables.md → rank column first</span></td>
      </tr>
      <tr>
        <td>Topics</td>
        <td class="before">Grey filled pills — no hover, decorative weight equal to comments count</td>
        <td class="after">Border-only pills in footer; accent hover — clear secondary zone, interaction hint</td>
        <td><span class="principle">operating-principles §5 (colour with purpose); quality-gates Gate 4 (hover state)</span></td>
      </tr>
      <tr>
        <td>Meta row</td>
        <td class="before">Comments count and Featured badge in right column — disconnected from content</td>
        <td class="after">Footer row: topics left, meta (comments · by · badge) right — one coherent secondary band</td>
        <td><span class="principle">operating-principles §2 (one focal point per zone — footer = all meta)</span></td>
      </tr>
      <tr>
        <td>Dark mode</td>
        <td class="before">Hardcoded #fff + #292929 + #ff6154 — breaks in dark mode; Before kept light-only (faithful)</td>
        <td class="after">OKLCH tokens throughout; upvote uses relative color syntax from --color-accent</td>
        <td><span class="principle">quality-gates Gate 6 (dark mode required)</span></td>
      </tr>
    </tbody>
  </table>

  <div class="section-label">Token Legend</div>
  <table class="token-legend">
    <thead><tr><th>Token</th><th>Light</th><th>Dark</th><th>Used for</th></tr></thead>
    <tbody>
      <tr><td class="token-name">--color-bg</td><td>oklch(96% 0.004 258)</td><td>oklch(13% 0.010 258)</td><td>Page background, skeleton shimmer midpoint</td></tr>
      <tr><td class="token-name">--color-surface</td><td>oklch(100% 0 0)</td><td>oklch(17% 0.010 258)</td><td>Card background</td></tr>
      <tr><td class="token-name">--color-border</td><td>oklch(90% 0.006 258)</td><td>oklch(26% 0.010 258)</td><td>Card border, topic pills, thumbnail border</td></tr>
      <tr><td class="token-name">--color-text</td><td>oklch(17% 0.012 258)</td><td>oklch(94% 0.004 258)</td><td>Product name</td></tr>
      <tr><td class="token-name">--color-text-secondary</td><td>oklch(42% 0.012 258)</td><td>oklch(72% 0.008 258)</td><td>Tagline</td></tr>
      <tr><td class="token-name">--color-text-muted</td><td>oklch(60% 0.008 258)</td><td>oklch(55% 0.006 258)</td><td>Rank number, topic pill text, meta row (comments, by)</td></tr>
      <tr><td class="token-name">--color-accent</td><td>oklch(52% 0.20 258)</td><td>oklch(65% 0.20 258)</td><td>Upvote button (fill/border/text), name hover, topic hover, focus rings</td></tr>
    </tbody>
  </table>

</main>

<script>
  const wrapper   = document.getElementById('component-wrapper');
  const afterEl   = document.getElementById('state-after');
  const beforeEl  = document.getElementById('state-before');
  const btnBefore = document.getElementById('btn-before');
  const btnAfter  = document.getElementById('btn-after');
  const reduced   = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  let current = 'after';

  function measureHeights() {
    afterEl.hidden = false; beforeEl.hidden = false;
    afterEl.style.visibility = 'hidden'; beforeEl.style.visibility = 'hidden';
    const afterH  = afterEl.getBoundingClientRect().height;
    const beforeH = beforeEl.getBoundingClientRect().height;
    afterEl.style.visibility = ''; beforeEl.style.visibility = '';
    wrapper.style.minHeight = Math.max(afterH, beforeH) + 'px';
    beforeEl.hidden = true;
  }

  function switchTo(target) {
    if (target === current) return;
    current = target;
    const showEl = target === 'after' ? afterEl : beforeEl;
    const hideEl = target === 'after' ? beforeEl : afterEl;
    btnBefore.classList.toggle('active', target === 'before');
    btnAfter.classList.toggle('active',  target === 'after');
    btnBefore.setAttribute('aria-pressed', target === 'before');
    btnAfter.setAttribute('aria-pressed',  target === 'after');
    if (reduced) { hideEl.hidden = true; showEl.hidden = false; return; }
    hideEl.style.opacity = '0'; hideEl.style.transform = 'translateY(4px)';
    setTimeout(() => { hideEl.hidden = true; hideEl.style.opacity = ''; hideEl.style.transform = ''; }, 200);
    showEl.hidden = false; showEl.style.opacity = '0'; showEl.style.transform = 'translateY(4px)';
    requestAnimationFrame(() => requestAnimationFrame(() => {
      showEl.style.transition = 'opacity 200ms cubic-bezier(0.16,1,0.3,1), transform 200ms cubic-bezier(0.16,1,0.3,1)';
      showEl.style.opacity = '1'; showEl.style.transform = 'translateY(0)';
      setTimeout(() => { showEl.style.transition = ''; }, 220);
    }));
  }

  window.addEventListener('DOMContentLoaded', () => {
    measureHeights();
    btnBefore.addEventListener('click', () => switchTo('before'));
    btnAfter.addEventListener('click',  () => switchTo('after'));
    [btnBefore, btnAfter].forEach(btn =>
      btn.addEventListener('keydown', e => {
        if (e.key === ' ' || e.key === 'Enter') { e.preventDefault(); btn.click(); }
      })
    );
  });
</script>
</body>
</html>
```

- [ ] **Step 2: Verify quality gates**

Open `demo/product-hunt.html` in Chrome. Check:
- Toggle default → After; Before shows PH-faithful row layout with orange upvote
- Upvote button: 52×52px, hover state visible, focus ring with Tab key
- Dark mode: upvote button, topic pills all render without broken contrast
- 390px: header row wraps cleanly (rank + thumb + title stack if needed); no overflow
- Change log: 6 rows, each with principle reference

- [ ] **Step 3: Commit**

```bash
git add demo/product-hunt.html
git commit -m "feat(demo): add Product Hunt listing Before/After demo (Wave 2)"
```

---

### Task 4: Update `demo/index.html`

**Files:**
- Modify: `demo/index.html`

Make two targeted edits:
1. Activate the three Wave 2 cards (remove disabled styles, replace "Coming soon" spans with real links)
2. Add Wave 3 placeholder section (fixes the empty grid when "Wave 3" filter is clicked)

- [ ] **Step 1: Activate Wave 2 npm card**

Find this block in `demo/index.html`:
```html
    <div class="demo-card" data-wave="wave-2" style="opacity:0.5;pointer-events:none">
      <div class="card-thumb">
        <div class="card-thumb-half before"><span class="card-thumb-emoji">📦</span><span class="card-thumb-label">Before</span></div>
        <div class="card-thumb-half after"><span class="card-thumb-emoji">📦</span><span class="card-thumb-label">After</span></div>
      </div>
      <div class="card-info">
        <div class="card-site">📦 npm</div>
        <div class="card-component">Package Search Card</div>
        <div class="card-footer"><span class="card-badge badge-high">High</span><span class="card-link" style="color:var(--color-text-muted)">Coming soon</span></div>
      </div>
    </div>
```

Replace with:
```html
    <div class="demo-card" data-wave="wave-2">
      <div class="card-thumb">
        <div class="card-thumb-half before"><span class="card-thumb-emoji">📦</span><span class="card-thumb-label">Before</span></div>
        <div class="card-thumb-half after"><span class="card-thumb-emoji">📦</span><span class="card-thumb-label">After</span></div>
      </div>
      <div class="card-info">
        <div class="card-site">📦 npm</div>
        <div class="card-component">Package Search Card</div>
        <div class="card-footer"><span class="card-badge badge-high">High</span><a href="npm-package.html" class="card-link">View demo →</a></div>
      </div>
    </div>
```

- [ ] **Step 2: Activate Wave 2 MDN card**

Find:
```html
    <div class="demo-card" data-wave="wave-2" style="opacity:0.5;pointer-events:none">
      <div class="card-thumb">
        <div class="card-thumb-half before"><span class="card-thumb-emoji">🦊</span><span class="card-thumb-label">Before</span></div>
        <div class="card-thumb-half after"><span class="card-thumb-emoji">🦊</span><span class="card-thumb-label">After</span></div>
      </div>
      <div class="card-info">
        <div class="card-site">🦊 MDN</div>
        <div class="card-component">API Method Block</div>
        <div class="card-footer"><span class="card-badge badge-deep">Deep</span><span class="card-link" style="color:var(--color-text-muted)">Coming soon</span></div>
      </div>
    </div>
```

Replace with:
```html
    <div class="demo-card" data-wave="wave-2">
      <div class="card-thumb">
        <div class="card-thumb-half before"><span class="card-thumb-emoji">🦊</span><span class="card-thumb-label">Before</span></div>
        <div class="card-thumb-half after"><span class="card-thumb-emoji">🦊</span><span class="card-thumb-label">After</span></div>
      </div>
      <div class="card-info">
        <div class="card-site">🦊 MDN</div>
        <div class="card-component">API Method Block</div>
        <div class="card-footer"><span class="card-badge badge-deep">Deep</span><a href="mdn-api.html" class="card-link">View demo →</a></div>
      </div>
    </div>
```

- [ ] **Step 3: Activate Wave 2 Product Hunt card**

Find:
```html
    <div class="demo-card" data-wave="wave-2" style="opacity:0.5;pointer-events:none">
      <div class="card-thumb">
        <div class="card-thumb-half before"><span class="card-thumb-emoji">🚀</span><span class="card-thumb-label">Before</span></div>
        <div class="card-thumb-half after"><span class="card-thumb-emoji">🚀</span><span class="card-thumb-label">After</span></div>
      </div>
      <div class="card-info">
        <div class="card-site">🚀 Product Hunt</div>
        <div class="card-component">Product Listing</div>
        <div class="card-footer"><span class="card-badge badge-high">High</span><span class="card-link" style="color:var(--color-text-muted)">Coming soon</span></div>
      </div>
    </div>
```

Replace with:
```html
    <div class="demo-card" data-wave="wave-2">
      <div class="card-thumb">
        <div class="card-thumb-half before"><span class="card-thumb-emoji">🚀</span><span class="card-thumb-label">Before</span></div>
        <div class="card-thumb-half after"><span class="card-thumb-emoji">🚀</span><span class="card-thumb-label">After</span></div>
      </div>
      <div class="card-info">
        <div class="card-site">🚀 Product Hunt</div>
        <div class="card-component">Product Listing</div>
        <div class="card-footer"><span class="card-badge badge-high">High</span><a href="product-hunt.html" class="card-link">View demo →</a></div>
      </div>
    </div>
```

- [ ] **Step 4: Update Wave 2 section label and add Wave 3 placeholder section**

Find this line in `demo/index.html`:
```html
  <div class="wave-label" style="margin-top:var(--space-10)">Wave 2 — Depth &amp; variety <span style="font-weight:400;font-style:italic;text-transform:none;letter-spacing:0">(coming soon)</span></div>
```

Replace with:
```html
  <div class="wave-label" style="margin-top:var(--space-10)">Wave 2 — Depth &amp; variety</div>
```

Then find the closing `</main>` tag and insert the Wave 3 section immediately before it:
```html

  <div class="wave-label" style="margin-top:var(--space-10)">Wave 3 — Specialist depth <span style="font-weight:400;font-style:italic;text-transform:none;letter-spacing:0">(coming soon)</span></div>
  <div class="grid">

    <div class="demo-card" data-wave="wave-3" style="opacity:0.5;pointer-events:none">
      <div class="card-thumb">
        <div class="card-thumb-half before"><span class="card-thumb-emoji">📊</span><span class="card-thumb-label">Before</span></div>
        <div class="card-thumb-half after"><span class="card-thumb-emoji">📊</span><span class="card-thumb-label">After</span></div>
      </div>
      <div class="card-info">
        <div class="card-site">📊 Can I Use</div>
        <div class="card-component">Browser Compatibility Table</div>
        <div class="card-footer"><span class="card-badge badge-deep">Deep</span><span class="card-link" style="color:var(--color-text-muted)">Coming soon</span></div>
      </div>
    </div>

    <div class="demo-card" data-wave="wave-3" style="opacity:0.5;pointer-events:none">
      <div class="card-thumb">
        <div class="card-thumb-half before"><span class="card-thumb-emoji">✍️</span><span class="card-thumb-label">Before</span></div>
        <div class="card-thumb-half after"><span class="card-thumb-emoji">✍️</span><span class="card-thumb-label">After</span></div>
      </div>
      <div class="card-info">
        <div class="card-site">✍️ Dev.to</div>
        <div class="card-component">Article Card</div>
        <div class="card-footer"><span class="card-badge badge-deep">Deep</span><span class="card-link" style="color:var(--color-text-muted)">Coming soon</span></div>
      </div>
    </div>

  </div>

```

- [ ] **Step 5: Verify the gallery**

Open `demo/index.html` in Chrome. Check:
- All 6 Wave 1+2 cards show "View demo →" links that work
- Filter "Wave 2": Wave 1 and Wave 3 cards hide; Wave 2 cards visible and clickable
- Filter "Wave 3": Wave 1 and Wave 2 cards hide; 2 Wave 3 placeholder cards shown (greyed out)
- Filter "All": all 8 cards visible (6 active + 2 greyed Wave 3)
- No JS errors in DevTools

- [ ] **Step 6: Commit**

```bash
git add demo/index.html
git commit -m "feat(demo): activate Wave 2 card links and add Wave 3 placeholder cards to gallery"
```

---

### Task 5: Push and verify live

- [ ] **Step 1: Push to master**

```bash
git push origin master
```

- [ ] **Step 2: Wait for GitHub Actions Pages deploy (~30s)**

Watch: `gh run list --limit 3`

Expected: `Deploy Demo Gallery to GitHub Pages` → `completed success`

- [ ] **Step 3: Smoke check all Wave 2 demos**

Open in browser:
- `https://staurus86.github.io/global-design-skill/` — confirm 6 active cards + 2 Wave 3 placeholders
- `https://staurus86.github.io/global-design-skill/npm-package.html` — toggle, dark mode, 390px
- `https://staurus86.github.io/global-design-skill/mdn-api.html` — toggle, dark mode, 390px
- `https://staurus86.github.io/global-design-skill/product-hunt.html` — toggle, upvote hover, 390px

---

## Self-Review

**1. Spec coverage:**

| Spec requirement | Task |
|-----------------|------|
| `npm-package.html` Before/After + skeleton + changelog + token legend | Task 1 |
| `mdn-api.html` Before/After + skeleton + changelog + token legend | Task 2 |
| `product-hunt.html` Before/After + skeleton + changelog + token legend | Task 3 |
| Gallery Wave 2 cards activated | Task 4 |
| Wave 3 placeholder cards (fixes empty filter) | Task 4 |
| Pushed and smoke-checked on live site | Task 5 |

**2. Placeholder scan:** All steps contain complete code. No TBD, no "similar to Task N", no empty steps.

**3. Pattern consistency across all 3 files:**
- Same token block (including `--color-success`/`--color-success-bg`) ✓
- Same JS (`measureHeights`, `switchTo`, `DOMContentLoaded`) ✓
- Same toggle bar, `aria-live`, `aria-pressed` ✓
- Same skeleton pattern (`.skel` + `shimmer` keyframe + reduced-motion guard) ✓
- Same section labels, changelog, token legend CSS ✓
- `<main class="content">` landmark ✓
- `100dvh` on body ✓
- Footer background: `oklch(from var(--color-surface) calc(l - 0.03) c h)` ✓
- Hover tints: `oklch(from var(--color-accent) l c h / ...)` relative color syntax ✓
- Before states: hardcoded hex/colours permitted (faithful recreation) ✓
- After states: OKLCH tokens only ✓
