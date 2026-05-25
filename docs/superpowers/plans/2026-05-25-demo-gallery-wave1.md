# Demo Gallery Wave 1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build Wave 1 of the global-design-skill Demo Gallery: three self-contained Before/After redesign pages (Hacker News, Stack Overflow, GitHub PR) plus a gallery index page, deployed to GitHub Pages from the `demo/` folder on `master`.

**Architecture:** Each demo file is a self-contained HTML+CSS+JS file with no external dependencies. Before and After states are live HTML toggled by a keyboard-accessible bar. A shared token block is copy-pasted into each file; `demo/tokens.css` is the update source of truth. The gallery page (`demo/index.html`) shows all demos in a filterable 3-column card grid with two-phase JS hide/show.

**Tech Stack:** Vanilla HTML5, CSS (OKLCH custom properties, Grid), vanilla JS (no framework), GitHub Pages (static deploy from `/demo` folder, `master` branch).

---

### Task 1: Foundation — `demo/tokens.css` + `demo/README.md`

**Files:**
- Create: `demo/tokens.css`
- Create: `demo/README.md`

- [ ] **Step 1: Create `demo/tokens.css`**

```css
/* demo/tokens.css — single source of truth for demo design tokens.
   NOT loaded by browsers. Exists for reference and sed-based sync only.
   Update protocol: sed -i'' 's/--color-accent: oklch(52% 0.20 258)/--color-accent: oklch(NEW)/g' demo/*.html
*/
:root {
  --color-bg:             oklch(96% 0.004 258);
  --color-surface:        oklch(100% 0 0);
  --color-border:         oklch(90% 0.006 258);
  --color-text:           oklch(17% 0.012 258);
  --color-text-secondary: oklch(42% 0.012 258);
  --color-text-muted:     oklch(60% 0.008 258);
  --color-accent:         oklch(52% 0.20 258);
  --color-accent-hover:   oklch(45% 0.21 258);

  --space-1: 4px;  --space-2: 8px;  --space-3: 12px; --space-4: 16px;
  --space-5: 20px; --space-6: 24px; --space-8: 32px; --space-10: 40px;

  --text-xs: 11px; --text-sm: 13px; --text-base: 15px;
  --text-md: 17px; --text-lg: 19px;
  --text-xl:  clamp(20px, 2.3vw + 0.5rem, 26px);
  --text-2xl: clamp(26px, 3.5vw + 0.5rem, 36px);

  --ease-out:    cubic-bezier(0.16, 1, 0.3, 1);
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
  --t-fast: 140ms; --t-base: 210ms; --t-slow: 320ms;
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
  }
}
```

- [ ] **Step 2: Create `demo/README.md`**

```markdown
# Demo Gallery

Eight self-contained Before/After redesign demos using global-design-skill.

## Token Update Protocol

`demo/tokens.css` is the single source of truth for design tokens. Tokens are
duplicated into each demo file for self-containment (no build step, GitHub Pages ready).

To update a token value across all demo files, run from the repo root:

```bash
# Portable — works on macOS and Linux
sed -i'' 's/--color-accent: oklch(52% 0.20 258)/--color-accent: oklch(NEW_VALUE)/g' demo/*.html
```

Never edit token values in individual demo files directly.

## Files

| File | Wave | Component |
|------|------|-----------|
| `index.html` | — | Gallery page |
| `hacker-news.html` | 1 | HN Story List Item |
| `stack-overflow.html` | 1 | SO Question Card |
| `github-pr.html` | 1 | GitHub PR Card |
| `npm-package.html` | 2 | npm Package Card |
| `mdn-api.html` | 2 | MDN API Method Block |
| `product-hunt.html` | 2 | Product Hunt Listing |
| `caniuse-table.html` | 3 | Can I Use Browser Table |
| `devto-card.html` | 3 | Dev.to Article Card |
```

- [ ] **Step 3: Verify directory**

Run: `ls demo/`
Expected: `README.md  tokens.css`

- [ ] **Step 4: Commit**

```bash
git add demo/tokens.css demo/README.md
git commit -m "feat(demo): add token source-of-truth and README"
```

---

### Task 2: `demo/hacker-news.html`

**Files:**
- Create: `demo/hacker-news.html`

- [ ] **Step 1: Create the file with this exact content**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hacker News Story Item — global-design-skill Demo</title>
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
      }
    }

    /* ── Reset ── */
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      font-size: var(--text-base);
      background: var(--color-bg);
      color: var(--color-text);
      min-height: 100dvh;
    }
    a { color: inherit; text-decoration: none; }
    button { border: none; background: none; cursor: pointer; font: inherit; }

    /* ── Page chrome ── */
    .page-header {
      padding: var(--space-3) var(--space-6);
      border-bottom: 1px solid var(--color-border);
      display: flex; align-items: center; justify-content: space-between;
      font-size: var(--text-sm); color: var(--color-text-muted);
    }
    .page-header-site { font-weight: 700; color: var(--color-text); }
    .page-header-back { color: var(--color-accent); }
    .page-header-back:hover { text-decoration: underline; }
    .content { max-width: 720px; margin: 0 auto; padding: var(--space-8) var(--space-4); }

    /* ── Toggle bar ── */
    .toggle-bar {
      display: flex; border: 1px solid var(--color-border); border-radius: 10px;
      overflow: hidden; margin-bottom: var(--space-6); background: var(--color-surface);
    }
    .toggle-btn {
      flex: 1; padding: var(--space-3) var(--space-4); font-size: var(--text-sm);
      font-weight: 600; color: var(--color-text-muted); cursor: pointer; min-height: 44px;
      transition: background var(--t-fast) var(--ease-out), color var(--t-fast) var(--ease-out);
    }
    .toggle-btn.active { background: var(--color-accent); color: oklch(100% 0 0); }
    .toggle-btn:focus-visible { outline: 2px solid var(--color-accent); outline-offset: -2px; }

    /* ── Component wrapper ── */
    .component-wrapper { position: relative; margin-bottom: var(--space-8); }
    .component-state {
      transition: opacity 200ms cubic-bezier(0.16,1,0.3,1),
                  transform 200ms cubic-bezier(0.16,1,0.3,1);
    }
    @media (prefers-reduced-motion: reduce) { .component-state { transition: none; } }

    /* ── BEFORE: faithful HN snapshot 2026-05-25 ── */
    .hn-before {
      font-family: 'Times New Roman', Times, serif;
      font-size: 10pt; background: #f6f6ef; border-top: 2px solid #ff6600; padding: 8px;
    }
    .hn-before-table { border-collapse: collapse; width: 100%; }
    .hn-before-table td { vertical-align: top; padding: 2px 4px; }
    .hn-before-rank { color: #828282; width: 22px; }
    .hn-before-arrow { color: #9a9a9a; font-size: 14px; width: 14px; cursor: pointer; }
    .hn-before-title a { color: #000; font-size: 10pt; }
    .hn-before-title a:visited { color: #828282; }
    .hn-before-domain { font-size: 8pt; color: #828282; }
    .hn-before-domain a { color: #828282; }
    .hn-before-sub { font-size: 7pt; color: #828282; }
    .hn-before-sub a { color: #828282; }
    .hn-before-user { color: #3c963c; }

    /* ── AFTER: redesigned card ── */
    .hn-card {
      display: flex; gap: var(--space-4);
      background: var(--color-surface); border: 1px solid var(--color-border);
      border-radius: 12px; padding: var(--space-4);
    }
    .hn-vote {
      display: flex; flex-direction: column; align-items: center; gap: var(--space-1);
      border: 1px solid var(--color-border); border-radius: 8px;
      padding: var(--space-2) var(--space-3); flex-shrink: 0;
    }
    .hn-vote-btn {
      width: 32px; height: 44px; display: flex; align-items: center; justify-content: center;
      border-radius: 6px; color: var(--color-text-muted); font-size: var(--text-sm);
      transition: background var(--t-fast) var(--ease-out), color var(--t-fast) var(--ease-out);
    }
    .hn-vote-btn:hover { background: oklch(52% 0.20 258 / 0.1); color: var(--color-accent); }
    .hn-vote-btn:focus-visible { outline: 2px solid var(--color-accent); outline-offset: 1px; }
    .hn-score { font-size: var(--text-sm); font-weight: 700; color: var(--color-text-secondary); }
    .hn-body { flex: 1; min-width: 0; }
    .hn-meta-top { display: flex; align-items: center; gap: var(--space-2); margin-bottom: var(--space-2); }
    .hn-domain {
      font-size: var(--text-xs); font-weight: 600; color: var(--color-text-muted);
      border: 1px solid var(--color-border); border-radius: 999px; padding: 2px var(--space-2);
    }
    .hn-title { margin-bottom: var(--space-3); }
    .hn-title-link { font-size: var(--text-lg); font-weight: 600; color: var(--color-text); line-height: 1.35; }
    .hn-title-link:hover { color: var(--color-accent); }
    .hn-title-link:visited { color: var(--color-text-secondary); }
    .hn-meta {
      display: flex; align-items: center; flex-wrap: wrap;
      gap: var(--space-2); font-size: var(--text-sm); color: var(--color-text-muted);
    }
    .hn-meta-author { color: var(--color-text-secondary); font-weight: 500; }
    .hn-meta-dot { opacity: 0.4; }
    .hn-comments { color: var(--color-accent); }
    .hn-comments:hover { text-decoration: underline; }
    .hn-share-btn {
      color: var(--color-text-muted); font-size: var(--text-sm);
      padding: 2px var(--space-2); border-radius: 4px; min-height: 44px;
      display: inline-flex; align-items: center;
      transition: color var(--t-fast) var(--ease-out);
    }
    .hn-share-btn:hover { color: var(--color-accent); }
    .hn-share-btn:focus-visible { outline: 2px solid var(--color-accent); outline-offset: 1px; }

    /* ── Skeleton ── */
    .skeleton-card {
      display: flex; gap: var(--space-4);
      background: var(--color-surface); border: 1px solid var(--color-border);
      border-radius: 12px; padding: var(--space-4);
    }
    .skel {
      background: linear-gradient(90deg, var(--color-border) 25%, var(--color-bg) 50%, var(--color-border) 75%);
      background-size: 200% 100%; border-radius: 4px;
      animation: shimmer 1.5s linear infinite;
    }
    @keyframes shimmer { 0% { background-position: 200% 0; } 100% { background-position: -200% 0; } }
    @media (prefers-reduced-motion: reduce) { .skel { animation: none; background: var(--color-border); } }
    .skel-vote { width: 52px; border-radius: 8px; flex-shrink: 0; min-height: 80px; }
    .skel-body { flex: 1; display: flex; flex-direction: column; gap: var(--space-2); }
    .skel-pill { height: 18px; width: 80px; border-radius: 999px; }
    .skel-title { height: 22px; }
    .skel-title-short { height: 22px; width: 65%; }
    .skel-meta { height: 14px; width: 55%; }

    /* ── Section labels ── */
    .section-label {
      font-size: var(--text-xs); font-weight: 700; letter-spacing: 0.08em;
      text-transform: uppercase; color: var(--color-text-muted);
      margin-bottom: var(--space-4); margin-top: var(--space-8);
      padding-bottom: var(--space-2); border-bottom: 1px solid var(--color-border);
    }

    /* ── Change log ── */
    .changelog { width: 100%; border-collapse: collapse; font-size: var(--text-sm); margin-bottom: var(--space-8); }
    .changelog th {
      text-align: left; padding: var(--space-2) var(--space-3);
      font-size: var(--text-xs); font-weight: 700; color: var(--color-text-muted);
      border-bottom: 1px solid var(--color-border);
    }
    .changelog td {
      padding: var(--space-3); border-bottom: 1px solid var(--color-border);
      vertical-align: top; line-height: 1.5;
    }
    .changelog tr:last-child td { border-bottom: none; }
    .changelog td:first-child { font-weight: 600; white-space: nowrap; }
    .changelog .before { color: var(--color-text-secondary); }
    .changelog .after { color: var(--color-text); }
    .principle { font-size: var(--text-xs); color: var(--color-accent); }

    /* ── Token legend ── */
    .token-legend { width: 100%; border-collapse: collapse; font-size: var(--text-sm); }
    .token-legend th {
      text-align: left; padding: var(--space-2) var(--space-3);
      font-size: var(--text-xs); font-weight: 700; color: var(--color-text-muted);
      border-bottom: 1px solid var(--color-border);
    }
    .token-legend td {
      padding: var(--space-2) var(--space-3); border-bottom: 1px solid var(--color-border);
      vertical-align: top; font-family: 'Menlo', 'Consolas', monospace; font-size: var(--text-xs);
    }
    .token-legend tr:last-child td { border-bottom: none; }
    .token-name { color: var(--color-accent); }
  </style>
</head>
<body>

<header class="page-header">
  <div>
    <span class="page-header-site">global-design-skill</span>
    <span style="margin:0 8px;opacity:0.3">·</span>
    <span>🟠 Hacker News — Story List Item</span>
  </div>
  <a href="index.html" class="page-header-back">← Gallery</a>
</header>

<div class="content">

  <div class="toggle-bar" role="group" aria-label="Before/After state toggle">
    <button class="toggle-btn" id="btn-before" aria-pressed="false" aria-label="Show original Hacker News design">← Before</button>
    <button class="toggle-btn active" id="btn-after" aria-pressed="true" aria-label="Show redesigned version">After →</button>
  </div>

  <div class="component-wrapper" id="component-wrapper">
    <div aria-live="polite" aria-atomic="true">

      <!-- AFTER (default) -->
      <div id="state-after" class="component-state">
        <article class="hn-card">
          <div class="hn-vote">
            <button class="hn-vote-btn" aria-label="Upvote this story">▲</button>
            <span class="hn-score">847</span>
            <button class="hn-vote-btn" aria-label="Downvote this story">▼</button>
          </div>
          <div class="hn-body">
            <div class="hn-meta-top">
              <span class="hn-domain">github.com</span>
            </div>
            <h2 class="hn-title">
              <a href="#" class="hn-title-link">Show HN: I built a tool that turns any terminal command into a web UI</a>
            </h2>
            <div class="hn-meta">
              <span class="hn-meta-author">devmaker42</span>
              <span class="hn-meta-dot">·</span>
              <span>3h ago</span>
              <span class="hn-meta-dot">·</span>
              <a href="#" class="hn-comments">213 comments</a>
              <span class="hn-meta-dot">·</span>
              <button class="hn-share-btn" aria-label="Share this story">Share</button>
            </div>
          </div>
        </article>
      </div>

      <!-- BEFORE -->
      <div id="state-before" class="component-state" hidden>
        <div class="hn-before">
          <table class="hn-before-table">
            <tbody>
              <tr>
                <td class="hn-before-rank">1.</td>
                <td class="hn-before-arrow">&#9650;</td>
                <td class="hn-before-title">
                  <a href="#">Show HN: I built a tool that turns any terminal command into a web UI</a>
                  <span class="hn-before-domain"> (<a href="#">github.com</a>)</span>
                </td>
              </tr>
              <tr>
                <td colspan="2"></td>
                <td class="hn-before-sub">
                  847 points by <a href="#" class="hn-before-user">devmaker42</a>
                  <a href="#"> 3 hours ago</a>
                  | <a href="#">hide</a>
                  | <a href="#">213&nbsp;comments</a>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

    </div>
  </div>

  <div class="section-label">Skeleton State</div>
  <div class="skeleton-card" aria-busy="true" aria-label="Loading Hacker News story item">
    <div class="skel skel-vote"></div>
    <div class="skel-body">
      <div class="skel skel-pill"></div>
      <div class="skel skel-title"></div>
      <div class="skel skel-title-short"></div>
      <div class="skel skel-meta"></div>
    </div>
  </div>

  <div class="section-label">Change Log</div>
  <table class="changelog">
    <thead>
      <tr><th>Change</th><th>Before</th><th>After</th><th>Principle</th></tr>
    </thead>
    <tbody>
      <tr>
        <td>Layout</td>
        <td class="before">HTML &lt;table&gt; with colspan rows; no semantic structure</td>
        <td class="after">Flexbox &lt;article&gt;, semantic &lt;h2&gt; for title</td>
        <td><span class="principle">operating-principles §1 (semantic structure first)</span></td>
      </tr>
      <tr>
        <td>Typography</td>
        <td class="before">Times New Roman 10pt on #f6f6ef; rank, title, meta at same visual weight</td>
        <td class="after">System sans-serif; title at --text-lg (19px) bold, meta at --text-sm (13px) muted</td>
        <td><span class="principle">operating-principles §3 (legibility scale)</span></td>
      </tr>
      <tr>
        <td>Vote widget</td>
        <td class="before">Single grey ▲ triangle; score buried in 7pt meta text row below title</td>
        <td class="after">[▲ score ▼] contained group, left-aligned, 44px touch targets each</td>
        <td><span class="principle">operating-principles §7 (Fitts — primary action large); quality-gates Gate 4 (all interactive states: idle/hover/focus)</span></td>
      </tr>
      <tr>
        <td>Domain display</td>
        <td class="before">Plain "(github.com)" in parentheses, 8pt grey — source unclear until you read it</td>
        <td class="after">Domain pill above title — source credibility established before reading</td>
        <td><span class="principle">operating-principles §2 (one focal point per zone)</span></td>
      </tr>
      <tr>
        <td>Colour system</td>
        <td class="before">Raw hex (#f6f6ef, #ff6600, #828282) — not themeable</td>
        <td class="after">OKLCH custom properties; dark mode via @media (prefers-color-scheme: dark)</td>
        <td><span class="principle">operating-principles §5 (colour system with purpose); quality-gates Gate 6 (dark mode)</span></td>
      </tr>
      <tr>
        <td>Share action</td>
        <td class="before">No share affordance</td>
        <td class="after">Share button in meta row, min-height 44px, focus ring</td>
        <td><span class="principle">rules/14-landing-pages.md → action affordance in every card</span></td>
      </tr>
    </tbody>
  </table>

  <div class="section-label">Token Legend</div>
  <table class="token-legend">
    <thead>
      <tr><th>Token</th><th>Light</th><th>Dark</th><th>Used for</th></tr>
    </thead>
    <tbody>
      <tr><td class="token-name">--color-bg</td><td>oklch(96% 0.004 258)</td><td>oklch(13% 0.010 258)</td><td>Page background</td></tr>
      <tr><td class="token-name">--color-surface</td><td>oklch(100% 0 0)</td><td>oklch(17% 0.010 258)</td><td>Card background</td></tr>
      <tr><td class="token-name">--color-border</td><td>oklch(90% 0.006 258)</td><td>oklch(26% 0.010 258)</td><td>Card border, vote widget border, dividers</td></tr>
      <tr><td class="token-name">--color-text</td><td>oklch(17% 0.012 258)</td><td>oklch(94% 0.004 258)</td><td>Title text</td></tr>
      <tr><td class="token-name">--color-text-secondary</td><td>oklch(42% 0.012 258)</td><td>oklch(72% 0.008 258)</td><td>Score, author name</td></tr>
      <tr><td class="token-name">--color-text-muted</td><td>oklch(60% 0.008 258)</td><td>oklch(55% 0.006 258)</td><td>Vote arrows, time, separator dots, header</td></tr>
      <tr><td class="token-name">--color-accent</td><td>oklch(52% 0.20 258)</td><td>oklch(65% 0.20 258)</td><td>Toggle active, comment link, focus rings, domain pill border</td></tr>
    </tbody>
  </table>

</div>

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

- [ ] **Step 2: Open in browser — verify quality gates**

Open `demo/hacker-news.html` in Chrome. Check all 7 gates:

| Gate | What to check |
|------|---------------|
| Toggle | Default shows After (redesigned). Click Before → original HN layout. Click After → redesign returns. |
| Keyboard | Tab to both toggle buttons; Space/Enter switches state; focus ring visible on each. |
| Skeleton | Shimmer visible below component; no animation in `prefers-reduced-motion` mode (DevTools → Rendering). |
| Dark mode | Enable dark OS theme or DevTools → Rendering → prefers-color-scheme: dark; both states render without broken contrast. |
| Responsive | DevTools responsive view at 390px — no horizontal scroll; card reflows cleanly. |
| No layout shift | Toggle Before↔After — wrapper height stays stable (no jump). |
| Change log | 6 rows visible with principle references. |

- [ ] **Step 3: Commit**

```bash
git add demo/hacker-news.html
git commit -m "feat(demo): add Hacker News story item Before/After demo (Wave 1)"
```

---

### Task 3: `demo/stack-overflow.html`

**Files:**
- Create: `demo/stack-overflow.html`

- [ ] **Step 1: Create the file with this exact content**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Stack Overflow Question Card — global-design-skill Demo</title>
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
      }
    }

    /* ── Reset ── */
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      font-size: var(--text-base); background: var(--color-bg);
      color: var(--color-text); min-height: 100dvh;
    }
    a { color: inherit; text-decoration: none; }
    button { border: none; background: none; cursor: pointer; font: inherit; }

    /* ── Page chrome ── */
    .page-header {
      padding: var(--space-3) var(--space-6); border-bottom: 1px solid var(--color-border);
      display: flex; align-items: center; justify-content: space-between;
      font-size: var(--text-sm); color: var(--color-text-muted);
    }
    .page-header-site { font-weight: 700; color: var(--color-text); }
    .page-header-back { color: var(--color-accent); }
    .page-header-back:hover { text-decoration: underline; }
    .content { max-width: 780px; margin: 0 auto; padding: var(--space-8) var(--space-4); }

    /* ── Toggle bar ── */
    .toggle-bar {
      display: flex; border: 1px solid var(--color-border); border-radius: 10px;
      overflow: hidden; margin-bottom: var(--space-6); background: var(--color-surface);
    }
    .toggle-btn {
      flex: 1; padding: var(--space-3) var(--space-4); font-size: var(--text-sm);
      font-weight: 600; color: var(--color-text-muted); cursor: pointer; min-height: 44px;
      transition: background var(--t-fast) var(--ease-out), color var(--t-fast) var(--ease-out);
    }
    .toggle-btn.active { background: var(--color-accent); color: oklch(100% 0 0); }
    .toggle-btn:focus-visible { outline: 2px solid var(--color-accent); outline-offset: -2px; }

    /* ── Component wrapper ── */
    .component-wrapper { position: relative; margin-bottom: var(--space-8); }
    .component-state {
      transition: opacity 200ms cubic-bezier(0.16,1,0.3,1), transform 200ms cubic-bezier(0.16,1,0.3,1);
    }
    @media (prefers-reduced-motion: reduce) { .component-state { transition: none; } }

    /* ── BEFORE: faithful SO question card ── */
    .so-before {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
      font-size: 13px; background: #fff; border: 1px solid #d6d9dc; color: #3b4045;
    }
    .so-before-item { display: flex; gap: 0; padding: 0; border-bottom: 1px solid #e3e6e8; }
    .so-before-stats {
      display: flex; flex-direction: column; align-items: flex-end; justify-content: flex-start;
      gap: 6px; min-width: 108px; padding: 16px 8px 16px 16px; flex-shrink: 0;
    }
    .so-before-stat { font-size: 11px; color: #6a737c; text-align: right; }
    .so-before-stat-num { display: block; font-size: 17px; font-weight: 400; color: #6a737c; }
    .so-before-stat-num.strong { color: #0c0d0e; font-weight: 700; }
    .so-before-answered-badge {
      border: 1px solid #5eba7d; border-radius: 3px; padding: 4px 7px; text-align: center;
    }
    .so-before-answered-badge .so-before-stat-num { color: #2d6a4f; font-size: 17px; }
    .so-before-content { flex: 1; padding: 16px 16px 16px 0; min-width: 0; }
    .so-before-title { margin-bottom: 6px; }
    .so-before-title a { color: #0074cc; font-size: 17px; line-height: 1.3; }
    .so-before-title a:visited { color: #0074cc; }
    .so-before-excerpt { color: #3b4045; font-size: 13px; line-height: 1.5; margin-bottom: 8px; }
    .so-before-excerpt code { font-family: monospace; background: #eff0f1; padding: 1px 4px; border-radius: 2px; }
    .so-before-tags { display: flex; flex-wrap: wrap; gap: 4px; margin-bottom: 10px; }
    .so-before-tag {
      font-size: 12px; color: #39739d; background: #e1ecf4;
      border: 1px solid #9fc2d0; border-radius: 3px; padding: 2px 6px;
    }
    .so-before-footer { display: flex; align-items: center; justify-content: space-between; }
    .so-before-footer-time { color: #6a737c; font-size: 12px; }
    .so-before-user { display: flex; gap: 6px; align-items: center; }
    .so-before-avatar {
      width: 32px; height: 32px; border-radius: 3px; flex-shrink: 0;
      background: #e1ecf4; display: flex; align-items: center; justify-content: center;
      font-size: 11px; color: #39739d; font-weight: 700;
    }
    .so-before-username { color: #0074cc; font-size: 13px; display: block; }
    .so-before-rep { color: #6a737c; font-size: 12px; }

    /* ── AFTER: redesigned card ── */
    .so-card {
      background: var(--color-surface); border: 1px solid var(--color-border);
      border-radius: 12px; overflow: hidden;
    }
    .so-card-inner { display: flex; gap: var(--space-4); padding: var(--space-4); }
    .so-vote {
      display: flex; flex-direction: column; align-items: center; gap: var(--space-1);
      border: 1px solid var(--color-border); border-radius: 8px;
      padding: var(--space-2) var(--space-3); flex-shrink: 0; align-self: flex-start;
    }
    .so-vote-btn {
      width: 32px; height: 44px; display: flex; align-items: center; justify-content: center;
      border-radius: 6px; color: var(--color-text-muted); font-size: var(--text-sm);
      transition: background var(--t-fast) var(--ease-out), color var(--t-fast) var(--ease-out);
    }
    .so-vote-btn:hover { background: oklch(52% 0.20 258 / 0.1); color: var(--color-accent); }
    .so-vote-btn:focus-visible { outline: 2px solid var(--color-accent); outline-offset: 1px; }
    .so-score { font-size: var(--text-sm); font-weight: 700; color: var(--color-text-secondary); }
    .so-body { flex: 1; min-width: 0; display: flex; flex-direction: column; gap: var(--space-3); }
    .so-title-link {
      font-size: var(--text-lg); font-weight: 600; color: var(--color-text); line-height: 1.35;
    }
    .so-title-link:hover { color: var(--color-accent); }
    .so-excerpt { font-size: var(--text-sm); color: var(--color-text-secondary); line-height: 1.6; }
    .so-excerpt code {
      font-family: 'Menlo', 'Consolas', monospace; font-size: var(--text-xs);
      background: oklch(from var(--color-border) l c h / 0.5); border-radius: 4px; padding: 1px 4px;
    }
    .so-tags { display: flex; flex-wrap: wrap; gap: var(--space-1); }
    .so-tag {
      font-size: var(--text-xs); font-weight: 600; color: var(--color-accent);
      border: 1px solid oklch(52% 0.20 258 / 0.3); border-radius: 4px; padding: 2px var(--space-2);
      transition: background var(--t-fast) var(--ease-out);
    }
    .so-tag:hover { background: oklch(52% 0.20 258 / 0.08); }
    .so-footer {
      display: flex; align-items: center; justify-content: space-between;
      padding: var(--space-3) var(--space-4); border-top: 1px solid var(--color-border);
      background: oklch(from var(--color-bg) l c h / 0.6);
    }
    .so-meta { display: flex; align-items: center; gap: var(--space-2); font-size: var(--text-sm); }
    .so-avatar {
      width: 28px; height: 28px; border-radius: 6px; flex-shrink: 0;
      background: oklch(52% 0.20 258 / 0.15); display: flex; align-items: center;
      justify-content: center; font-size: var(--text-xs); font-weight: 700; color: var(--color-accent);
    }
    .so-author { color: var(--color-text-secondary); font-weight: 500; }
    .so-meta-dot { opacity: 0.35; color: var(--color-text-muted); }
    .so-time { color: var(--color-text-muted); }
    .so-views { color: var(--color-text-muted); }
    .so-answers-badge {
      display: flex; align-items: center; gap: var(--space-1);
      background: oklch(56% 0.17 145 / 0.12); border: 1px solid oklch(56% 0.17 145 / 0.4);
      color: oklch(35% 0.12 145); border-radius: 6px; padding: var(--space-1) var(--space-3);
      font-size: var(--text-sm); font-weight: 600;
    }
    .so-answers-icon { font-size: var(--text-md); }

    /* ── Skeleton ── */
    .skeleton-card {
      background: var(--color-surface); border: 1px solid var(--color-border);
      border-radius: 12px; overflow: hidden;
    }
    .sk-inner { display: flex; gap: var(--space-4); padding: var(--space-4); }
    .skel {
      background: linear-gradient(90deg, var(--color-border) 25%, var(--color-bg) 50%, var(--color-border) 75%);
      background-size: 200% 100%; border-radius: 4px; animation: shimmer 1.5s linear infinite;
    }
    @keyframes shimmer { 0% { background-position: 200% 0; } 100% { background-position: -200% 0; } }
    @media (prefers-reduced-motion: reduce) { .skel { animation: none; background: var(--color-border); } }
    .sk-vote { width: 52px; min-height: 96px; border-radius: 8px; flex-shrink: 0; }
    .sk-body { flex: 1; display: flex; flex-direction: column; gap: var(--space-2); }
    .sk-title-1 { height: 22px; }
    .sk-title-2 { height: 22px; width: 75%; }
    .sk-text { height: 14px; }
    .sk-text-short { height: 14px; width: 60%; }
    .sk-tags { display: flex; gap: var(--space-2); margin-top: var(--space-1); }
    .sk-tag { height: 20px; width: 52px; border-radius: 4px; }
    .sk-footer { height: 44px; border-top: 1px solid var(--color-border); }

    /* ── Section labels, changelog, token legend — same as hacker-news.html ── */
    .section-label {
      font-size: var(--text-xs); font-weight: 700; letter-spacing: 0.08em;
      text-transform: uppercase; color: var(--color-text-muted);
      margin-bottom: var(--space-4); margin-top: var(--space-8);
      padding-bottom: var(--space-2); border-bottom: 1px solid var(--color-border);
    }
    .changelog { width: 100%; border-collapse: collapse; font-size: var(--text-sm); margin-bottom: var(--space-8); }
    .changelog th {
      text-align: left; padding: var(--space-2) var(--space-3);
      font-size: var(--text-xs); font-weight: 700; color: var(--color-text-muted);
      border-bottom: 1px solid var(--color-border);
    }
    .changelog td { padding: var(--space-3); border-bottom: 1px solid var(--color-border); vertical-align: top; line-height: 1.5; }
    .changelog tr:last-child td { border-bottom: none; }
    .changelog td:first-child { font-weight: 600; white-space: nowrap; }
    .changelog .before { color: var(--color-text-secondary); }
    .changelog .after  { color: var(--color-text); }
    .principle { font-size: var(--text-xs); color: var(--color-accent); }
    .token-legend { width: 100%; border-collapse: collapse; font-size: var(--text-sm); }
    .token-legend th {
      text-align: left; padding: var(--space-2) var(--space-3);
      font-size: var(--text-xs); font-weight: 700; color: var(--color-text-muted);
      border-bottom: 1px solid var(--color-border);
    }
    .token-legend td {
      padding: var(--space-2) var(--space-3); border-bottom: 1px solid var(--color-border);
      vertical-align: top; font-family: 'Menlo','Consolas',monospace; font-size: var(--text-xs);
    }
    .token-legend tr:last-child td { border-bottom: none; }
    .token-name { color: var(--color-accent); }
  </style>
</head>
<body>

<header class="page-header">
  <div>
    <span class="page-header-site">global-design-skill</span>
    <span style="margin:0 8px;opacity:0.3">·</span>
    <span>📚 Stack Overflow — Question Card</span>
  </div>
  <a href="index.html" class="page-header-back">← Gallery</a>
</header>

<div class="content">

  <div class="toggle-bar" role="group" aria-label="Before/After state toggle">
    <button class="toggle-btn" id="btn-before" aria-pressed="false" aria-label="Show original Stack Overflow design">← Before</button>
    <button class="toggle-btn active" id="btn-after" aria-pressed="true" aria-label="Show redesigned version">After →</button>
  </div>

  <div class="component-wrapper" id="component-wrapper">
    <div aria-live="polite" aria-atomic="true">

      <!-- AFTER (default) -->
      <div id="state-after" class="component-state">
        <article class="so-card">
          <div class="so-card-inner">
            <div class="so-vote">
              <button class="so-vote-btn" aria-label="Upvote question">▲</button>
              <span class="so-score">47</span>
              <button class="so-vote-btn" aria-label="Downvote question">▼</button>
            </div>
            <div class="so-body">
              <h2><a href="#" class="so-title-link">Why does CSS Grid auto-fill create extra columns when using minmax with fr units?</a></h2>
              <p class="so-excerpt">I'm trying to create a responsive grid using <code>auto-fill</code> and <code>minmax()</code> but keep getting unexpected extra columns at certain viewport widths...</p>
              <div class="so-tags">
                <a href="#" class="so-tag">css</a>
                <a href="#" class="so-tag">css-grid</a>
                <a href="#" class="so-tag">flexbox</a>
                <a href="#" class="so-tag">responsive-design</a>
              </div>
            </div>
          </div>
          <div class="so-footer">
            <div class="so-meta">
              <div class="so-avatar" aria-hidden="true">cL</div>
              <span class="so-author">csslearner99</span>
              <span class="so-meta-dot">·</span>
              <span class="so-time">2h ago</span>
              <span class="so-meta-dot">·</span>
              <span class="so-views">2.8k views</span>
            </div>
            <div class="so-answers-badge" aria-label="3 answers">
              <span class="so-answers-icon">✓</span>
              <span>3 answers</span>
            </div>
          </div>
        </article>
      </div>

      <!-- BEFORE -->
      <div id="state-before" class="component-state" hidden>
        <div class="so-before">
          <div class="so-before-item">
            <div class="so-before-stats">
              <div class="so-before-stat">
                <span class="so-before-stat-num strong">47</span>
                <span>votes</span>
              </div>
              <div class="so-before-stat so-before-answered-badge">
                <span class="so-before-stat-num">3</span>
                <span>answers</span>
              </div>
              <div class="so-before-stat">
                <span class="so-before-stat-num">2,841</span>
                <span>views</span>
              </div>
            </div>
            <div class="so-before-content">
              <h3 class="so-before-title"><a href="#">Why does CSS Grid auto-fill create extra columns when using minmax with fr units?</a></h3>
              <p class="so-before-excerpt">I'm trying to create a responsive grid using <code>auto-fill</code> and <code>minmax()</code> but keep getting unexpected extra columns at certain viewport widths...</p>
              <div class="so-before-tags">
                <a href="#" class="so-before-tag">css</a>
                <a href="#" class="so-before-tag">css-grid</a>
                <a href="#" class="so-before-tag">flexbox</a>
                <a href="#" class="so-before-tag">responsive-design</a>
              </div>
              <div class="so-before-footer">
                <span class="so-before-footer-time">asked 2 hours ago</span>
                <div class="so-before-user">
                  <div class="so-before-avatar" aria-hidden="true">cL</div>
                  <div>
                    <a href="#" class="so-before-username">csslearner99</a>
                    <span class="so-before-rep">234</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>

  <div class="section-label">Skeleton State</div>
  <div class="skeleton-card" aria-busy="true" aria-label="Loading Stack Overflow question card">
    <div class="sk-inner">
      <div class="skel sk-vote"></div>
      <div class="sk-body">
        <div class="skel sk-title-1"></div>
        <div class="skel sk-title-2"></div>
        <div class="skel sk-text" style="margin-top:4px"></div>
        <div class="skel sk-text-short"></div>
        <div class="sk-tags">
          <div class="skel sk-tag"></div>
          <div class="skel sk-tag"></div>
          <div class="skel sk-tag"></div>
        </div>
      </div>
    </div>
    <div class="skel sk-footer"></div>
  </div>

  <div class="section-label">Change Log</div>
  <table class="changelog">
    <thead><tr><th>Change</th><th>Before</th><th>After</th><th>Principle</th></tr></thead>
    <tbody>
      <tr>
        <td>Information hierarchy</td>
        <td class="before">Votes / answers / views in a sidebar column; title at same visual weight as stats</td>
        <td class="after">Title is dominant (--text-lg); stats demoted to footer — read title first, then decide</td>
        <td><span class="principle">operating-principles §2 (one focal point: the question title)</span></td>
      </tr>
      <tr>
        <td>Vote widget</td>
        <td class="before">Score number only in stats sidebar; no interactive affordance visible</td>
        <td class="after">[▲ score ▼] group with 44px touch targets, hover and focus states</td>
        <td><span class="principle">operating-principles §7 (Fitts); quality-gates Gate 4 (all interactive states)</span></td>
      </tr>
      <tr>
        <td>Answer badge</td>
        <td class="before">Green border box in stats sidebar — same weight as vote count and views</td>
        <td class="after">Isolated badge in card footer — visually distinct, reads as a status not a metric</td>
        <td><span class="principle">operating-principles §4 (status vs. metric distinction)</span></td>
      </tr>
      <tr>
        <td>Tags</td>
        <td class="before">#e1ecf4 background pills with blue border — colour-heavy, competes with title link</td>
        <td class="after">Accent-tinted border only, no fill — tags present without dominating</td>
        <td><span class="principle">operating-principles §5 (colour with purpose — accent reserved for primary actions)</span></td>
      </tr>
      <tr>
        <td>User meta</td>
        <td class="before">32px avatar + username + rep scattered below tags; "asked X ago" left-aligned opposite</td>
        <td class="after">Avatar + author + dot + time + dot + views in a single inline meta row in the footer</td>
        <td><span class="principle">operating-principles §3 (group related information spatially)</span></td>
      </tr>
      <tr>
        <td>Dark mode</td>
        <td class="before">None — hardcoded #fff, #0074cc, #e1ecf4</td>
        <td class="after">Full dark mode via OKLCH tokens + @media (prefers-color-scheme: dark)</td>
        <td><span class="principle">quality-gates Gate 6 (dark mode required)</span></td>
      </tr>
    </tbody>
  </table>

  <div class="section-label">Token Legend</div>
  <table class="token-legend">
    <thead><tr><th>Token</th><th>Light</th><th>Dark</th><th>Used for</th></tr></thead>
    <tbody>
      <tr><td class="token-name">--color-bg</td><td>oklch(96% 0.004 258)</td><td>oklch(13% 0.010 258)</td><td>Page background, card footer tint</td></tr>
      <tr><td class="token-name">--color-surface</td><td>oklch(100% 0 0)</td><td>oklch(17% 0.010 258)</td><td>Card background</td></tr>
      <tr><td class="token-name">--color-border</td><td>oklch(90% 0.006 258)</td><td>oklch(26% 0.010 258)</td><td>Card border, footer divider, vote widget border, skeleton base</td></tr>
      <tr><td class="token-name">--color-text</td><td>oklch(17% 0.012 258)</td><td>oklch(94% 0.004 258)</td><td>Question title</td></tr>
      <tr><td class="token-name">--color-text-secondary</td><td>oklch(42% 0.012 258)</td><td>oklch(72% 0.008 258)</td><td>Score, author name, excerpt text</td></tr>
      <tr><td class="token-name">--color-text-muted</td><td>oklch(60% 0.008 258)</td><td>oklch(55% 0.006 258)</td><td>Vote arrows, time, views, separator dots</td></tr>
      <tr><td class="token-name">--color-accent</td><td>oklch(52% 0.20 258)</td><td>oklch(65% 0.20 258)</td><td>Toggle active, tag borders, tag text, focus rings, avatar background</td></tr>
    </tbody>
  </table>

</div>

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

Open `demo/stack-overflow.html` in Chrome. Same 7-gate checklist as Task 2:
toggle default → After; keyboard accessible; skeleton shimmer visible; dark mode OK; no horizontal overflow at 390px; no layout shift on toggle; change log has 6 rows with principle references.

- [ ] **Step 3: Commit**

```bash
git add demo/stack-overflow.html
git commit -m "feat(demo): add Stack Overflow question card Before/After demo (Wave 1)"
```

---

### Task 4: `demo/github-pr.html`

**Files:**
- Create: `demo/github-pr.html`

- [ ] **Step 1: Create the file with this exact content**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GitHub PR Card — global-design-skill Demo</title>
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
      }
    }

    /* ── Reset ── */
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      font-size: var(--text-base); background: var(--color-bg);
      color: var(--color-text); min-height: 100dvh;
    }
    a { color: inherit; text-decoration: none; }
    button { border: none; background: none; cursor: pointer; font: inherit; }

    /* ── Page chrome ── */
    .page-header {
      padding: var(--space-3) var(--space-6); border-bottom: 1px solid var(--color-border);
      display: flex; align-items: center; justify-content: space-between;
      font-size: var(--text-sm); color: var(--color-text-muted);
    }
    .page-header-site { font-weight: 700; color: var(--color-text); }
    .page-header-back { color: var(--color-accent); }
    .page-header-back:hover { text-decoration: underline; }
    .content { max-width: 780px; margin: 0 auto; padding: var(--space-8) var(--space-4); }

    /* ── Toggle bar ── */
    .toggle-bar {
      display: flex; border: 1px solid var(--color-border); border-radius: 10px;
      overflow: hidden; margin-bottom: var(--space-6); background: var(--color-surface);
    }
    .toggle-btn {
      flex: 1; padding: var(--space-3) var(--space-4); font-size: var(--text-sm);
      font-weight: 600; color: var(--color-text-muted); cursor: pointer; min-height: 44px;
      transition: background var(--t-fast) var(--ease-out), color var(--t-fast) var(--ease-out);
    }
    .toggle-btn.active { background: var(--color-accent); color: oklch(100% 0 0); }
    .toggle-btn:focus-visible { outline: 2px solid var(--color-accent); outline-offset: -2px; }

    /* ── Component wrapper ── */
    .component-wrapper { position: relative; margin-bottom: var(--space-8); }
    .component-state {
      transition: opacity 200ms cubic-bezier(0.16,1,0.3,1), transform 200ms cubic-bezier(0.16,1,0.3,1);
    }
    @media (prefers-reduced-motion: reduce) { .component-state { transition: none; } }

    /* ── BEFORE: faithful GitHub PR list item ── */
    .gh-before {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      font-size: 14px; background: #fff; border: 1px solid #d0d7de; color: #24292f;
    }
    .gh-before-item {
      display: flex; align-items: flex-start; gap: 8px;
      padding: 12px 16px; border-bottom: 1px solid #d0d7de;
    }
    .gh-before-icon { flex-shrink: 0; margin-top: 2px; }
    .gh-before-content { flex: 1; min-width: 0; }
    .gh-before-title-row { display: flex; align-items: baseline; flex-wrap: wrap; gap: 6px; margin-bottom: 4px; }
    .gh-before-pr-title { font-size: 14px; font-weight: 600; color: #0969da; }
    .gh-before-pr-title:hover { text-decoration: underline; }
    .gh-before-label {
      font-size: 11px; font-weight: 500; border: 1px solid; border-radius: 999px;
      padding: 0 6px; white-space: nowrap;
    }
    .gh-before-meta { font-size: 12px; color: #57606a; line-height: 1.5; }
    .gh-before-meta a { color: #0969da; }
    .gh-before-meta code {
      font-family: 'SFMono-Regular', Consolas, monospace; font-size: 11px;
      background: rgba(175,184,193,0.2); border-radius: 6px; padding: 1px 4px;
    }
    .gh-before-right {
      flex-shrink: 0; display: flex; flex-direction: column;
      align-items: flex-end; gap: 8px; padding-top: 2px;
    }
    .gh-before-avatars { display: flex; }
    .gh-before-avatar {
      width: 20px; height: 20px; border-radius: 50%; border: 1px solid #fff;
      background: #e1e4e8; display: flex; align-items: center; justify-content: center;
      font-size: 8px; font-weight: 700; color: #57606a; margin-left: -4px;
    }
    .gh-before-avatar:first-child { margin-left: 0; }
    .gh-before-checks { display: flex; align-items: center; gap: 3px; color: #57606a; font-size: 12px; }

    /* ── AFTER: redesigned PR card ── */
    .gh-card {
      background: var(--color-surface); border: 1px solid var(--color-border); border-radius: 12px; overflow: hidden;
    }
    .gh-card-header {
      display: flex; align-items: center; gap: var(--space-3);
      padding: var(--space-4); border-bottom: 1px solid var(--color-border);
    }
    .gh-status {
      display: inline-flex; align-items: center; gap: var(--space-1);
      font-size: var(--text-xs); font-weight: 700; padding: var(--space-1) var(--space-3);
      border-radius: 999px; flex-shrink: 0;
      background: oklch(45% 0.15 145 / 0.12);
      border: 1px solid oklch(45% 0.15 145 / 0.4);
      color: oklch(32% 0.12 145);
    }
    @media (prefers-color-scheme: dark) {
      .gh-status {
        background: oklch(65% 0.15 145 / 0.15);
        border-color: oklch(65% 0.15 145 / 0.4);
        color: oklch(78% 0.12 145);
      }
    }
    .gh-pr-num { font-size: var(--text-sm); color: var(--color-text-muted); flex-shrink: 0; }
    .gh-branch-row {
      display: flex; align-items: center; gap: var(--space-2);
      font-size: var(--text-xs); color: var(--color-text-muted); margin-left: auto;
    }
    .gh-branch {
      font-family: 'Menlo','Consolas',monospace; font-size: var(--text-xs);
      background: oklch(from var(--color-border) l c h / 0.7);
      border: 1px solid var(--color-border); border-radius: 4px;
      padding: 1px var(--space-2);
    }
    .gh-branch-arrow { opacity: 0.4; }
    .gh-card-body { padding: var(--space-4); display: flex; flex-direction: column; gap: var(--space-3); }
    .gh-title-link {
      font-size: var(--text-lg); font-weight: 600; color: var(--color-text); line-height: 1.35;
    }
    .gh-title-link:hover { color: var(--color-accent); }
    .gh-labels { display: flex; flex-wrap: wrap; gap: var(--space-1); }
    .gh-label {
      font-size: var(--text-xs); font-weight: 600; border-radius: 999px;
      padding: 2px var(--space-2); border: 1px solid;
    }
    .gh-label-bug    { color: oklch(35% 0.18 25);  background: oklch(35% 0.18 25 / 0.10);  border-color: oklch(35% 0.18 25 / 0.35); }
    .gh-label-feat   { color: oklch(32% 0.12 258); background: oklch(32% 0.12 258 / 0.10); border-color: oklch(32% 0.12 258 / 0.35); }
    .gh-label-review { color: oklch(42% 0.14 68);  background: oklch(42% 0.14 68 / 0.10);  border-color: oklch(42% 0.14 68 / 0.35); }
    @media (prefers-color-scheme: dark) {
      .gh-label-bug    { color: oklch(72% 0.18 25);  background: oklch(72% 0.18 25 / 0.12);  border-color: oklch(72% 0.18 25 / 0.35); }
      .gh-label-feat   { color: oklch(70% 0.14 258); background: oklch(70% 0.14 258 / 0.12); border-color: oklch(70% 0.14 258 / 0.35); }
      .gh-label-review { color: oklch(75% 0.14 68);  background: oklch(75% 0.14 68 / 0.12);  border-color: oklch(75% 0.14 68 / 0.35); }
    }
    .gh-card-footer {
      display: flex; align-items: center; justify-content: space-between;
      padding: var(--space-3) var(--space-4); border-top: 1px solid var(--color-border);
      background: oklch(from var(--color-bg) l c h / 0.6);
    }
    .gh-meta { display: flex; align-items: center; gap: var(--space-2); font-size: var(--text-sm); color: var(--color-text-muted); }
    .gh-meta-dot { opacity: 0.35; }
    .gh-assignees { display: flex; align-items: center; gap: var(--space-2); }
    .gh-assignee {
      display: flex; align-items: center; gap: var(--space-1);
      font-size: var(--text-xs); color: var(--color-text-secondary);
    }
    .gh-avatar {
      width: 24px; height: 24px; border-radius: 6px; flex-shrink: 0;
      display: flex; align-items: center; justify-content: center;
      font-size: var(--text-xs); font-weight: 700;
    }
    .gh-avatar-1 { background: oklch(52% 0.20 258 / 0.15); color: var(--color-accent); }
    .gh-avatar-2 { background: oklch(56% 0.17 145 / 0.15); color: oklch(35% 0.12 145); }
    .gh-review-btn {
      display: inline-flex; align-items: center; gap: var(--space-1);
      font-size: var(--text-sm); font-weight: 600; color: var(--color-accent);
      padding: var(--space-2) var(--space-4); border-radius: 8px; min-height: 44px;
      border: 1px solid oklch(52% 0.20 258 / 0.4);
      transition: background var(--t-fast) var(--ease-out), border-color var(--t-fast) var(--ease-out);
    }
    .gh-review-btn:hover { background: oklch(52% 0.20 258 / 0.08); border-color: var(--color-accent); }
    .gh-review-btn:focus-visible { outline: 2px solid var(--color-accent); outline-offset: 2px; }
    .gh-ci-check {
      display: flex; align-items: center; gap: var(--space-1);
      font-size: var(--text-xs); color: oklch(35% 0.12 145);
    }
    @media (prefers-color-scheme: dark) {
      .gh-ci-check { color: oklch(70% 0.12 145); }
      .gh-avatar-2 { color: oklch(65% 0.12 145); }
    }

    /* ── Skeleton ── */
    .skeleton-card { background: var(--color-surface); border: 1px solid var(--color-border); border-radius: 12px; overflow: hidden; }
    .sk-header { display: flex; align-items: center; gap: var(--space-3); padding: var(--space-4); border-bottom: 1px solid var(--color-border); }
    .sk-body { padding: var(--space-4); display: flex; flex-direction: column; gap: var(--space-2); }
    .sk-footer { height: 56px; border-top: 1px solid var(--color-border); }
    .skel {
      background: linear-gradient(90deg, var(--color-border) 25%, var(--color-bg) 50%, var(--color-border) 75%);
      background-size: 200% 100%; border-radius: 4px; animation: shimmer 1.5s linear infinite;
    }
    @keyframes shimmer { 0% { background-position: 200% 0; } 100% { background-position: -200% 0; } }
    @media (prefers-reduced-motion: reduce) { .skel { animation: none; background: var(--color-border); } }
    .sk-badge  { height: 22px; width: 64px; border-radius: 999px; }
    .sk-prnum  { height: 16px; width: 36px; }
    .sk-branch { height: 16px; width: 140px; border-radius: 4px; margin-left: auto; }
    .sk-title-1 { height: 22px; }
    .sk-title-2 { height: 22px; width: 60%; }
    .sk-labels { display: flex; gap: var(--space-2); }
    .sk-label { height: 20px; width: 60px; border-radius: 999px; }

    /* ── Shared: section labels, changelog, token legend ── */
    .section-label {
      font-size: var(--text-xs); font-weight: 700; letter-spacing: 0.08em;
      text-transform: uppercase; color: var(--color-text-muted);
      margin-bottom: var(--space-4); margin-top: var(--space-8);
      padding-bottom: var(--space-2); border-bottom: 1px solid var(--color-border);
    }
    .changelog { width: 100%; border-collapse: collapse; font-size: var(--text-sm); margin-bottom: var(--space-8); }
    .changelog th {
      text-align: left; padding: var(--space-2) var(--space-3);
      font-size: var(--text-xs); font-weight: 700; color: var(--color-text-muted);
      border-bottom: 1px solid var(--color-border);
    }
    .changelog td { padding: var(--space-3); border-bottom: 1px solid var(--color-border); vertical-align: top; line-height: 1.5; }
    .changelog tr:last-child td { border-bottom: none; }
    .changelog td:first-child { font-weight: 600; white-space: nowrap; }
    .changelog .before { color: var(--color-text-secondary); }
    .changelog .after  { color: var(--color-text); }
    .principle { font-size: var(--text-xs); color: var(--color-accent); }
    .token-legend { width: 100%; border-collapse: collapse; font-size: var(--text-sm); }
    .token-legend th {
      text-align: left; padding: var(--space-2) var(--space-3);
      font-size: var(--text-xs); font-weight: 700; color: var(--color-text-muted);
      border-bottom: 1px solid var(--color-border);
    }
    .token-legend td {
      padding: var(--space-2) var(--space-3); border-bottom: 1px solid var(--color-border);
      vertical-align: top; font-family: 'Menlo','Consolas',monospace; font-size: var(--text-xs);
    }
    .token-legend tr:last-child td { border-bottom: none; }
    .token-name { color: var(--color-accent); }
  </style>
</head>
<body>

<header class="page-header">
  <div>
    <span class="page-header-site">global-design-skill</span>
    <span style="margin:0 8px;opacity:0.3">·</span>
    <span>🐙 GitHub — PR / Issue Card</span>
  </div>
  <a href="index.html" class="page-header-back">← Gallery</a>
</header>

<div class="content">

  <div class="toggle-bar" role="group" aria-label="Before/After state toggle">
    <button class="toggle-btn" id="btn-before" aria-pressed="false" aria-label="Show original GitHub PR design">← Before</button>
    <button class="toggle-btn active" id="btn-after" aria-pressed="true" aria-label="Show redesigned version">After →</button>
  </div>

  <div class="component-wrapper" id="component-wrapper">
    <div aria-live="polite" aria-atomic="true">

      <!-- AFTER (default) -->
      <div id="state-after" class="component-state">
        <article class="gh-card">
          <div class="gh-card-header">
            <span class="gh-status" aria-label="Status: Open">● Open</span>
            <span class="gh-pr-num">#847</span>
            <div class="gh-branch-row" aria-label="Branch: feat/sidebar into main">
              <span class="gh-branch">feat/sidebar</span>
              <span class="gh-branch-arrow">→</span>
              <span class="gh-branch">main</span>
            </div>
          </div>
          <div class="gh-card-body">
            <h2><a href="#" class="gh-title-link">feat: add responsive sidebar with collapsible navigation</a></h2>
            <div class="gh-labels">
              <span class="gh-label gh-label-feat">enhancement</span>
              <span class="gh-label gh-label-bug">accessibility</span>
              <span class="gh-label gh-label-review">needs review</span>
            </div>
          </div>
          <div class="gh-card-footer">
            <div class="gh-meta">
              <div class="gh-assignees">
                <div class="gh-assignee">
                  <div class="gh-avatar gh-avatar-1" aria-hidden="true">JD</div>
                  <span>sarah-dev</span>
                </div>
                <div class="gh-assignee">
                  <div class="gh-avatar gh-avatar-2" aria-hidden="true">MR</div>
                  <span>mike-r</span>
                </div>
              </div>
              <span class="gh-meta-dot">·</span>
              <span>opened 2 days ago</span>
              <span class="gh-meta-dot">·</span>
              <div class="gh-ci-check" aria-label="CI checks passed">✓ 2/2</div>
            </div>
            <button class="gh-review-btn" aria-label="Review changes for this pull request">Review →</button>
          </div>
        </article>
      </div>

      <!-- BEFORE -->
      <div id="state-before" class="component-state" hidden>
        <div class="gh-before">
          <div class="gh-before-item">
            <div class="gh-before-icon" aria-label="Open pull request">
              <svg width="16" height="16" viewBox="0 0 16 16" fill="#1a7f37">
                <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354Z"/>
              </svg>
            </div>
            <div class="gh-before-content">
              <div class="gh-before-title-row">
                <a href="#" class="gh-before-pr-title">feat: add responsive sidebar with collapsible navigation</a>
                <span class="gh-before-label" style="border-color:#d93f0b;color:#d93f0b;background:#ffebe9">accessibility</span>
                <span class="gh-before-label" style="border-color:#0075ca;color:#0075ca;background:#ddf4ff">enhancement</span>
                <span class="gh-before-label" style="border-color:#e4e669;color:#7a6800;background:#fafa6e22">needs review</span>
              </div>
              <div class="gh-before-meta">
                #847 opened 2 days ago by <a href="#">sarah-dev</a>
                &nbsp;·&nbsp;
                <code>feat/sidebar</code> → <code>main</code>
              </div>
            </div>
            <div class="gh-before-right">
              <div class="gh-before-avatars">
                <div class="gh-before-avatar" aria-label="Assignee JD">JD</div>
                <div class="gh-before-avatar" style="background:#ddf4ff;color:#0075ca" aria-label="Assignee MR">MR</div>
              </div>
              <div class="gh-before-checks" aria-label="CI: 2 of 2 checks passed">
                <svg width="14" height="14" viewBox="0 0 16 16" fill="#2da44e"><path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.75.75 0 0 1 1.06-1.06L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"/></svg>
                2 / 2
              </div>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>

  <div class="section-label">Skeleton State</div>
  <div class="skeleton-card" aria-busy="true" aria-label="Loading GitHub pull request card">
    <div class="sk-header">
      <div class="skel sk-badge"></div>
      <div class="skel sk-prnum"></div>
      <div class="skel sk-branch"></div>
    </div>
    <div class="sk-body">
      <div class="skel sk-title-1"></div>
      <div class="skel sk-title-2"></div>
      <div class="sk-labels">
        <div class="skel sk-label"></div>
        <div class="skel sk-label"></div>
        <div class="skel sk-label" style="width:80px"></div>
      </div>
    </div>
    <div class="skel sk-footer"></div>
  </div>

  <div class="section-label">Change Log</div>
  <table class="changelog">
    <thead><tr><th>Change</th><th>Before</th><th>After</th><th>Principle</th></tr></thead>
    <tbody>
      <tr>
        <td>Status visibility</td>
        <td class="before">Status conveyed by a green SVG icon only — icon meaning requires prior knowledge of GitHub</td>
        <td class="after">"● Open" pill with text label + colour — status legible without context</td>
        <td><span class="principle">operating-principles §4 (status must be text, not icon alone)</span></td>
      </tr>
      <tr>
        <td>Branch info</td>
        <td class="before">Inline in meta row as monospace code segments — easy to miss, buried after PR number and author</td>
        <td class="after">Isolated branch row in card header: feat/sidebar → main — reads as a navigation path</td>
        <td><span class="principle">operating-principles §2 (one focal point per zone — header = status + routing)</span></td>
      </tr>
      <tr>
        <td>Labels</td>
        <td class="before">Raw hex colours in HTML style attributes — no token system; all labels same visual weight</td>
        <td class="after">OKLCH semantic colours by label type (bug/feature/review); pill border-only — hierarchy by type</td>
        <td><span class="principle">operating-principles §5 (colour with purpose); rules/labels.md → semantic label colours</span></td>
      </tr>
      <tr>
        <td>Assignees</td>
        <td class="before">20px avatar thumbnails stacked right — identity visible only on hover; no names</td>
        <td class="after">Avatar (24px) + name inline — identity readable at a glance</td>
        <td><span class="principle">operating-principles §3 (show the person, not just the icon)</span></td>
      </tr>
      <tr>
        <td>Action affordance</td>
        <td class="before">No action in list item — must navigate to the PR page to begin review</td>
        <td class="after">"Review →" button in footer — primary action reachable from the list</td>
        <td><span class="principle">rules/14-landing-pages.md → CTA formula (specific label, primary visual weight)</span></td>
      </tr>
      <tr>
        <td>Dark mode</td>
        <td class="before">None — raw hex colours (#24292f, #0969da, #d0d7de) not themeable</td>
        <td class="after">OKLCH tokens + dark-mode overrides for all status colours and label variants</td>
        <td><span class="principle">quality-gates Gate 6 (dark mode required)</span></td>
      </tr>
    </tbody>
  </table>

  <div class="section-label">Token Legend</div>
  <table class="token-legend">
    <thead><tr><th>Token</th><th>Light</th><th>Dark</th><th>Used for</th></tr></thead>
    <tbody>
      <tr><td class="token-name">--color-bg</td><td>oklch(96% 0.004 258)</td><td>oklch(13% 0.010 258)</td><td>Page background, card footer tint</td></tr>
      <tr><td class="token-name">--color-surface</td><td>oklch(100% 0 0)</td><td>oklch(17% 0.010 258)</td><td>Card background</td></tr>
      <tr><td class="token-name">--color-border</td><td>oklch(90% 0.006 258)</td><td>oklch(26% 0.010 258)</td><td>Card border, header/footer dividers, branch pill border</td></tr>
      <tr><td class="token-name">--color-text</td><td>oklch(17% 0.012 258)</td><td>oklch(94% 0.004 258)</td><td>PR title</td></tr>
      <tr><td class="token-name">--color-text-secondary</td><td>oklch(42% 0.012 258)</td><td>oklch(72% 0.008 258)</td><td>Assignee names</td></tr>
      <tr><td class="token-name">--color-text-muted</td><td>oklch(60% 0.008 258)</td><td>oklch(55% 0.006 258)</td><td>PR number, branch text, time, separator dots</td></tr>
      <tr><td class="token-name">--color-accent</td><td>oklch(52% 0.20 258)</td><td>oklch(65% 0.20 258)</td><td>Toggle active, Review button, focus rings, enhancement label</td></tr>
    </tbody>
  </table>

</div>

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

Open `demo/github-pr.html` in Chrome. Check all 7 gates (same checklist as Tasks 2 and 3):
toggle default → After; keyboard; skeleton; dark mode; 390px; no layout shift; change log.

Additionally for this component: verify the green "Open" status pill, both label colour variants (light/dark mode), and the "Review →" button focus ring at 44px touch target.

- [ ] **Step 3: Commit**

```bash
git add demo/github-pr.html
git commit -m "feat(demo): add GitHub PR card Before/After demo (Wave 1)"
```

---

### Task 5: `demo/index.html`

**Files:**
- Create: `demo/index.html`

- [ ] **Step 1: Create the file with this exact content**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Demo Gallery — global-design-skill</title>
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
      --space-1: 4px;  --space-2: 8px;  --space-3: 12px; --space-4: 16px;
      --space-5: 20px; --space-6: 24px; --space-8: 32px; --space-10: 40px;
      --text-xs: 11px; --text-sm: 13px; --text-base: 15px;
      --text-md: 17px; --text-lg: 19px;
      --text-xl:  clamp(20px, 2.3vw + 0.5rem, 26px);
      --text-2xl: clamp(26px, 3.5vw + 0.5rem, 36px);
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
      }
    }

    /* ── Reset ── */
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      font-size: var(--text-base); background: var(--color-bg);
      color: var(--color-text); min-height: 100dvh;
    }
    a { color: inherit; text-decoration: none; }
    button { border: none; background: none; cursor: pointer; font: inherit; }

    /* ── Nav ── */
    .nav {
      padding: var(--space-3) var(--space-6);
      border-bottom: 1px solid var(--color-border);
      display: flex; align-items: center; justify-content: space-between;
      background: var(--color-surface);
      position: sticky; top: 0; z-index: 10;
    }
    .nav-logo {
      font-size: var(--text-sm); font-weight: 800; color: var(--color-accent);
      letter-spacing: -0.02em;
    }
    .nav-filters { display: flex; gap: var(--space-1); }
    .filter-btn {
      font-size: var(--text-sm); font-weight: 600; padding: var(--space-1) var(--space-3);
      border-radius: 999px; color: var(--color-text-muted); min-height: 36px;
      transition: background var(--t-fast) var(--ease-out), color var(--t-fast) var(--ease-out);
    }
    .filter-btn:hover { background: oklch(from var(--color-border) l c h / 0.7); color: var(--color-text); }
    .filter-btn.active { background: var(--color-accent); color: oklch(100% 0 0); }
    .filter-btn:focus-visible { outline: 2px solid var(--color-accent); outline-offset: 2px; }

    /* ── Hero ── */
    .hero {
      background: oklch(13% 0.010 258);
      padding: var(--space-10) var(--space-6);
      text-align: center;
    }
    .hero-title {
      font-size: var(--text-2xl); font-weight: 800;
      color: oklch(94% 0.004 258); letter-spacing: -0.03em; margin-bottom: var(--space-3);
    }
    .hero-sub {
      font-size: var(--text-sm); color: oklch(55% 0.006 258); max-width: 480px; margin: 0 auto;
      line-height: 1.6;
    }
    .hero-pills {
      display: flex; justify-content: center; gap: var(--space-2); margin-top: var(--space-5); flex-wrap: wrap;
    }
    .hero-pill {
      font-size: var(--text-xs); font-weight: 600; padding: var(--space-1) var(--space-3);
      border-radius: 999px; border: 1px solid oklch(30% 0.010 258);
      color: oklch(60% 0.008 258);
    }

    /* ── Grid ── */
    .grid-section { max-width: 1200px; margin: 0 auto; padding: var(--space-8) var(--space-6); }
    .grid {
      display: grid;
      grid-template-columns: repeat(1, 1fr);
      gap: clamp(16px, 2vw, 24px);
    }
    @media (min-width: 640px)  { .grid { grid-template-columns: repeat(2, 1fr); } }
    @media (min-width: 1024px) { .grid { grid-template-columns: repeat(3, 1fr); } }

    /* ── Demo card ── */
    .demo-card {
      background: var(--color-surface); border: 1px solid var(--color-border);
      border-radius: 16px; overflow: hidden;
      transition: transform var(--t-fast) var(--ease-out), box-shadow var(--t-fast) var(--ease-out),
                  opacity 150ms var(--ease-out);
    }
    .demo-card:hover { transform: translateY(-2px); box-shadow: 0 8px 24px oklch(17% 0.012 258 / 0.10); }
    .demo-card.card--hidden {
      opacity: 0; transform: scale(0.96); pointer-events: none; transition: opacity 150ms var(--ease-out), transform 150ms var(--ease-out);
    }

    /* Thumbnail: 50/50 split — Before (red tint) | After (green tint) */
    .card-thumb { display: grid; grid-template-columns: 1fr 1fr; height: 80px; }
    .card-thumb-half {
      display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 4px;
    }
    .card-thumb-half.before { background: oklch(88% 0.05 25); }
    .card-thumb-half.after  { background: oklch(90% 0.05 145); }
    .card-thumb-emoji { font-size: 24px; line-height: 1; }
    .card-thumb-label {
      font-size: 9px; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase;
    }
    .card-thumb-half.before .card-thumb-label { color: oklch(40% 0.12 25); }
    .card-thumb-half.after  .card-thumb-label { color: oklch(30% 0.12 145); }
    .card-thumb-divider {
      width: 1px; height: 80px; background: oklch(100% 0 0 / 0.4); align-self: center;
    }

    .card-info { padding: var(--space-4); }
    .card-site { font-size: var(--text-base); font-weight: 700; color: var(--color-text); margin-bottom: var(--space-1); }
    .card-component { font-size: var(--text-sm); color: var(--color-accent); margin-bottom: var(--space-3); }
    .card-footer { display: flex; align-items: center; justify-content: space-between; }
    .card-badge {
      font-size: var(--text-xs); font-weight: 700; padding: 2px var(--space-2); border-radius: 999px;
    }
    .badge-wow  { background: oklch(90% 0.08 68);  color: oklch(38% 0.12 68); }
    .badge-high { background: oklch(90% 0.06 145); color: oklch(30% 0.10 145); }
    .badge-deep { background: oklch(88% 0.06 258); color: oklch(35% 0.14 258); }
    .card-link {
      font-size: var(--text-sm); font-weight: 600; color: var(--color-accent);
      display: inline-flex; align-items: center; gap: var(--space-1); padding: var(--space-1) 0;
      min-height: 44px;
    }
    .card-link:hover { text-decoration: underline; }
    .card-link:focus-visible { outline: 2px solid var(--color-accent); outline-offset: 2px; border-radius: 4px; }

    /* Wave label above grid */
    .wave-label {
      font-size: var(--text-xs); font-weight: 800; letter-spacing: 0.08em; text-transform: uppercase;
      color: var(--color-text-muted); margin-bottom: var(--space-4); margin-top: var(--space-8);
    }
    .wave-label:first-child { margin-top: 0; }

    /* ── Footer ── */
    .site-footer {
      border-top: 1px solid var(--color-border); padding: var(--space-8) var(--space-6);
      text-align: center; font-size: var(--text-sm); color: var(--color-text-muted);
      display: flex; align-items: center; justify-content: center; gap: var(--space-4); flex-wrap: wrap;
    }
    .site-footer a { color: var(--color-accent); }
    .site-footer a:hover { text-decoration: underline; }
  </style>
</head>
<body>

<nav class="nav" aria-label="Site navigation">
  <span class="nav-logo">global-design-skill</span>
  <div class="nav-filters" role="group" aria-label="Filter demos by wave">
    <button class="filter-btn active" data-wave="all"    aria-pressed="true">All</button>
    <button class="filter-btn"        data-wave="wave-1" aria-pressed="false">Wave 1</button>
    <button class="filter-btn"        data-wave="wave-2" aria-pressed="false">Wave 2</button>
    <button class="filter-btn"        data-wave="wave-3" aria-pressed="false">Wave 3</button>
  </div>
</nav>

<section class="hero">
  <h1 class="hero-title">Demo Gallery</h1>
  <p class="hero-sub">Real redesigns of developer tools using global-design-skill. Every component: Before and After, live HTML, OKLCH tokens, WCAG 2.2 AA.</p>
  <div class="hero-pills">
    <span class="hero-pill">8 redesigns</span>
    <span class="hero-pill">OKLCH tokens</span>
    <span class="hero-pill">Dark mode</span>
    <span class="hero-pill">All states</span>
  </div>
</section>

<main class="grid-section">

  <div class="wave-label">Wave 1 — Maximum contrast</div>
  <div class="grid" id="demo-grid">

    <div class="demo-card" data-wave="wave-1">
      <div class="card-thumb">
        <div class="card-thumb-half before">
          <span class="card-thumb-emoji">🟠</span>
          <span class="card-thumb-label">Before</span>
        </div>
        <div class="card-thumb-half after">
          <span class="card-thumb-emoji">🟠</span>
          <span class="card-thumb-label">After</span>
        </div>
      </div>
      <div class="card-info">
        <div class="card-site">🟠 Hacker News</div>
        <div class="card-component">Story List Item</div>
        <div class="card-footer">
          <span class="card-badge badge-wow">WOW</span>
          <a href="hacker-news.html" class="card-link">View demo →</a>
        </div>
      </div>
    </div>

    <div class="demo-card" data-wave="wave-1">
      <div class="card-thumb">
        <div class="card-thumb-half before">
          <span class="card-thumb-emoji">📚</span>
          <span class="card-thumb-label">Before</span>
        </div>
        <div class="card-thumb-half after">
          <span class="card-thumb-emoji">📚</span>
          <span class="card-thumb-label">After</span>
        </div>
      </div>
      <div class="card-info">
        <div class="card-site">📚 Stack Overflow</div>
        <div class="card-component">Question Card</div>
        <div class="card-footer">
          <span class="card-badge badge-wow">WOW</span>
          <a href="stack-overflow.html" class="card-link">View demo →</a>
        </div>
      </div>
    </div>

    <div class="demo-card" data-wave="wave-1">
      <div class="card-thumb">
        <div class="card-thumb-half before">
          <span class="card-thumb-emoji">🐙</span>
          <span class="card-thumb-label">Before</span>
        </div>
        <div class="card-thumb-half after">
          <span class="card-thumb-emoji">🐙</span>
          <span class="card-thumb-label">After</span>
        </div>
      </div>
      <div class="card-info">
        <div class="card-site">🐙 GitHub</div>
        <div class="card-component">PR / Issue Card</div>
        <div class="card-footer">
          <span class="card-badge badge-high">High</span>
          <a href="github-pr.html" class="card-link">View demo →</a>
        </div>
      </div>
    </div>

  </div><!-- #demo-grid -->

  <div class="wave-label" style="margin-top:var(--space-10)">Wave 2 — Depth &amp; variety <span style="font-weight:400;font-style:italic;text-transform:none;letter-spacing:0">(coming soon)</span></div>
  <div class="grid">

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

  </div>

</main>

<footer class="site-footer">
  <a href="https://github.com/staurus86/global-design-skill" aria-label="View global-design-skill on GitHub">GitHub repo</a>
  <span style="opacity:0.3">·</span>
  <span>MIT licence</span>
  <span style="opacity:0.3">·</span>
  <span>OKLCH · No build step · GitHub Pages</span>
</footer>

<script>
  const filterBtns = document.querySelectorAll('.filter-btn');
  const allCards   = document.querySelectorAll('.demo-card');

  function hideCard(card) {
    card.classList.add('card--hidden');
    card.addEventListener('transitionend', () => { card.style.display = 'none'; }, { once: true });
  }
  function showCard(card) {
    card.style.display = '';
    requestAnimationFrame(() => requestAnimationFrame(() => card.classList.remove('card--hidden')));
  }

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const wave = btn.dataset.wave;
      filterBtns.forEach(b => { b.classList.remove('active'); b.setAttribute('aria-pressed', 'false'); });
      btn.classList.add('active'); btn.setAttribute('aria-pressed', 'true');
      allCards.forEach(card => {
        const matches = wave === 'all' || card.dataset.wave === wave;
        if (matches) showCard(card); else hideCard(card);
      });
    });
    btn.addEventListener('keydown', e => {
      if (e.key === ' ' || e.key === 'Enter') { e.preventDefault(); btn.click(); }
    });
  });
</script>

</body>
</html>
```

- [ ] **Step 2: Verify quality gates**

Open `demo/index.html` in Chrome. Check:

| Check | What to verify |
|-------|----------------|
| Cards visible | All 3 Wave 1 cards render with emoji thumbnails; Wave 2 cards shown as greyed-out "Coming soon" |
| Filter — Wave 1 | Click "Wave 1" → Wave 2 cards fade out + disappear; Wave 1 cards remain |
| Filter — All | Click "All" → Wave 2 cards fade back in; no empty grid holes during transition |
| Keyboard filter | Tab to filter buttons; Space/Enter triggers filter; aria-pressed updates |
| Card CTA | "View demo →" links open correct demo files |
| Dark mode | Hero, nav, cards all render without broken contrast |
| 390px | 1-column grid, hero text clamps down, no horizontal overflow |
| 768px | 2-column grid |
| 1024px | 3-column grid |
| No JS errors | Open DevTools Console — no errors during filter transitions |

- [ ] **Step 3: Commit**

```bash
git add demo/index.html
git commit -m "feat(demo): add gallery index page with wave filter and card grid"
```

---

### Task 6: GitHub Pages Setup

**Files:**
- Modify: `README.md` (repo root) — add Pages URL after it's confirmed live

- [ ] **Step 1: Enable GitHub Pages in repo settings**

In browser:
1. Go to `https://github.com/staurus86/global-design-skill/settings/pages`
2. Under **Source**, select: **Deploy from a branch**
3. Branch: `master` · Folder: `/demo`
4. Click **Save**
5. Wait ~60 seconds for the first deploy

- [ ] **Step 2: Verify the site is live**

Open: `https://staurus86.github.io/global-design-skill/`

Expected: gallery `index.html` loads. All 3 Wave 1 demo links work.

If the URL returns 404, wait another 60 seconds and refresh — first deploy can take up to 3 minutes.

- [ ] **Step 3: Add the Pages URL to `README.md`**

In the repo root `README.md`, add the following line under the existing description (after the first paragraph, before any existing sections):

```markdown
**Live demos:** https://staurus86.github.io/global-design-skill/
```

- [ ] **Step 4: Commit and push**

```bash
git add README.md
git commit -m "docs: add GitHub Pages live demo URL to README"
git push origin master
```

- [ ] **Step 5: Smoke check after push**

Reload `https://staurus86.github.io/global-design-skill/` — confirm it still renders. Open one demo (e.g., `hacker-news.html`) and toggle Before/After — confirm both states work on the live site.

---

## Self-Review

**Spec coverage check:**

| Spec requirement | Task that covers it |
|------------------|---------------------|
| `demo/tokens.css` as source of truth | Task 1 |
| `demo/README.md` with sed update protocol | Task 1 |
| `hacker-news.html` Before + After + skeleton + changelog + token legend | Task 2 |
| `stack-overflow.html` same format | Task 3 |
| `github-pr.html` same format | Task 4 |
| `demo/index.html` gallery page | Task 5 |
| Filter tabs with two-phase JS (hideCard/showCard) | Task 5 |
| Difficulty badges (WOW/High/Deep) | Task 5 |
| Responsive grid (390px/768px/1024px) | Task 5 |
| GitHub Pages setup from `master` `/demo` | Task 6 |
| README with Pages URL | Task 6 |
| Toggle default = After | Tasks 2-4 (btn-after has class `active` on load) |
| `aria-live="polite"` on component wrapper | Tasks 2-4 |
| JS-measured `minHeight` (no `aspect-ratio`) | Tasks 2-4 (measureHeights function) |
| `prefers-reduced-motion` instant swap | Tasks 2-4 (reduced const) |
| Skeleton shimmer `linear` easing | Tasks 2-4 (`animation: shimmer 1.5s linear`) |
| No `ease-in-out`, no `100vh`, no raw hex, no external CSS | All tasks — OKLCH tokens only, `100dvh` used |

**Placeholder scan:** No TBD, no TODO, no "similar to Task N" — all tasks contain complete code.

**Type consistency:** `switchTo`, `measureHeights`, `btnBefore`, `btnAfter`, `hideCard`, `showCard` — names consistent across Tasks 2-5.
