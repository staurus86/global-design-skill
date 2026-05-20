# Example — Agency Portfolio Site (Cyberbrutalism Archetype)

> Full implementation walkthrough: a creative studio portfolio with the Cyberbrutalism archetype (C). Max contrast, raw borders, kinetic type, no visual comfort zones. Target: agency pitching to startup clients.

---

## Project Brief

**Client:** Motion & Type Studio — a 4-person creative studio specializing in brand identity and motion design.

**Goal:** Win project inquiries from funded tech startups. Signal: "We are not a vendor. We are taste-makers."

**The One Memorable Thing:** The typography IS the design — every heading is a piece of work.

**Archetype: C — Cyberbrutalism**
- Base: pure white `oklch(100% 0 0)` with raw black borders
- Accent: neon yellow `oklch(88% 0.2 96)`
- Typography: Monument Extended (display) + JetBrains Mono (data/labels)
- Motion: snap scroll, ASCII reveals, glitch effects
- No border-radius. No shadows. No gradients.

---

## Token Foundation

```css
:root {
  /* Cyberbrutalism palette */
  --color-base:    oklch(100% 0 0);         /* white canvas */
  --color-ink:     oklch(5% 0 0);           /* near-black text */
  --color-accent:  oklch(88% 0.2 96);       /* neon yellow */
  --color-muted:   oklch(45% 0 0);          /* mid gray */
  --color-border:  oklch(0% 0 0);           /* raw black */
  --color-surface: oklch(96% 0 0);          /* off-white cards */

  /* No radius anywhere */
  --radius-base: 0;
  --radius-card: 0;

  /* Borders are statements */
  --border-raw: 2px solid var(--color-border);
  --border-accent: 3px solid var(--color-accent);

  /* Typography */
  --text-hero:    clamp(5rem, 14vw + 1rem, 18rem);
  --text-display: clamp(3rem, 7vw + 0.5rem, 10rem);
  --text-h2:      clamp(1.75rem, 3vw + 0.5rem, 4rem);
  --text-mono:    clamp(0.75rem, 1vw + 0.25rem, 0.9rem);
  --text-body:    clamp(1rem, 1.2vw + 0.4rem, 1.15rem);

  /* Motion */
  --ease-brutal: cubic-bezier(0.9, 0, 0.1, 1);
  --ease-snap:   cubic-bezier(1, 0, 0, 1);

  /* Spacing */
  --section-gap: clamp(6rem, 10vw, 12rem);
}
```

---

## Site Architecture

```
/                  Landing + reel loop
/work              Project grid
/work/[slug]       Case study
/studio            Team + process
/contact           Single form
```

**IA decisions:**
- No "About" page — studio story lives on the home page as a manifesto section
- No "Services" page — described via the Work grid tags
- Contact is a separate page (not a modal) — inquiries deserve weight
- Case study URL structure: `/work/[client-name]` not `/projects/[id]`

---

## Page 1 — Home

### Nav

```html
<nav class="nav-brutal" role="navigation" aria-label="Main">
  <a href="/" class="nav-logo">
    <span class="logo-m">M</span><span class="logo-t">T</span>
  </a>

  <ul class="nav-links" role="list">
    <li><a href="/work" class="nav-link">Work</a></li>
    <li><a href="/studio" class="nav-link">Studio</a></li>
    <li><a href="/contact" class="nav-link nav-link--cta">Start a project</a></li>
  </ul>

  <!-- Mobile: hamburger -->
  <button class="nav-toggle" aria-expanded="false" aria-controls="nav-mobile" aria-label="Open menu">
    <span></span><span></span>
  </button>
</nav>
```

```css
.nav-brutal {
  position: fixed;
  top: 0;
  inset-inline: 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.25rem var(--space-8);
  background: var(--color-base);
  border-bottom: var(--border-raw);
  z-index: 100;
  mix-blend-mode: normal;
}

.nav-logo {
  font-family: 'Monument Extended', sans-serif;
  font-size: 1.25rem;
  font-weight: 800;
  text-decoration: none;
  color: var(--color-ink);
  letter-spacing: -0.02em;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: var(--space-8);
  list-style: none;
  margin: 0; padding: 0;
}

.nav-link {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.8125rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--color-ink);
  text-decoration: none;
  position: relative;
}

/* Brutal underline — full-width on hover */
.nav-link::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 0;
  right: 0;
  height: 2px;
  background: var(--color-accent);
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 200ms var(--ease-brutal);
}
.nav-link:hover::after { transform: scaleX(1); }

.nav-link--cta {
  padding: 0.5rem 1.25rem;
  background: var(--color-accent);
  color: var(--color-ink);
  border: var(--border-raw);
  font-weight: 700;
}
.nav-link--cta::after { display: none; }
.nav-link--cta:hover { background: var(--color-ink); color: var(--color-accent); }
```

### Hero

The hero IS the typography. The name is the headline. No hero image.

```html
<section class="hero-brutal" data-section="hero">
  <!-- Marquee at the very top -->
  <div class="hero-ticker" aria-hidden="true">
    <div class="ticker-track">
      <span>Brand Identity</span>
      <span>★</span>
      <span>Motion Design</span>
      <span>★</span>
      <span>Digital Experiences</span>
      <span>★</span>
      <span>Brand Identity</span>
      <span>★</span>
      <span>Motion Design</span>
      <span>★</span>
      <span>Digital Experiences</span>
      <span>★</span>
    </div>
  </div>

  <div class="hero-main">
    <!-- Counter — signals prestige without fake stats -->
    <div class="hero-meta" data-enter="0">
      <span class="meta-label">Est.</span>
      <span class="meta-value">2019</span>
      <span class="meta-sep">/</span>
      <span class="meta-label">Projects</span>
      <span class="meta-value">47</span>
    </div>

    <!-- The hero heading IS the statement -->
    <h1 class="hero-headline" data-enter="1">
      <span class="hl-line hl-line--1" data-scramble>Motion</span>
      <span class="hl-line hl-line--2" data-scramble>
        <span class="hl-accent">&</span>
        <span>Type</span>
      </span>
      <span class="hl-line hl-line--3" data-scramble>Studio</span>
    </h1>

    <p class="hero-descriptor" data-enter="2">
      Brand identity and motion design for companies<br>
      that refuse to look like everyone else.
    </p>

    <div class="hero-actions" data-enter="3">
      <a href="/work" class="btn-brutal btn-primary">View work →</a>
      <a href="/contact" class="btn-brutal btn-ghost">Start a project</a>
    </div>
  </div>

  <!-- Bold decorative element — the number -->
  <div class="hero-number" aria-hidden="true">04</div>
</section>
```

```css
.hero-brutal {
  min-height: 100dvh;
  display: grid;
  grid-template-rows: auto 1fr;
  padding-top: 80px; /* nav height */
  overflow: hidden;
  position: relative;
}

.hero-ticker {
  border-bottom: var(--border-raw);
  padding: 0.75rem 0;
  overflow: hidden;
  background: var(--color-accent);
}

.ticker-track {
  display: flex;
  gap: var(--space-8);
  width: max-content;
  animation: ticker 20s linear infinite;
  font-family: 'Monument Extended', sans-serif;
  font-size: 0.75rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.15em;
  color: var(--color-ink);
}

@keyframes ticker { from { transform: translateX(0); } to { transform: translateX(-50%); } }

@media (prefers-reduced-motion: reduce) {
  .ticker-track { animation: none; }
}

.hero-main {
  padding: var(--space-12) var(--space-8);
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: var(--space-8);
  position: relative;
  z-index: 1;
}

.hero-meta {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.75rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--color-muted);
  border-left: var(--border-accent);
  padding-left: var(--space-4);
}

.hero-headline {
  font-family: 'Monument Extended', sans-serif;
  font-size: var(--text-hero);
  font-weight: 800;
  line-height: 0.88;
  letter-spacing: -0.04em;
  text-transform: uppercase;
  color: var(--color-ink);
}

.hl-line { display: block; }

.hl-line--2 {
  display: flex;
  align-items: center;
  gap: 0.15em;
}

.hl-accent { color: var(--color-accent); }

.hero-descriptor {
  font-size: var(--text-body);
  color: var(--color-muted);
  max-width: 48ch;
  line-height: 1.5;
  border-left: var(--border-raw);
  padding-left: var(--space-4);
}

/* The giant decorative number */
.hero-number {
  position: absolute;
  right: -0.05em;
  bottom: -0.1em;
  font-family: 'Monument Extended', sans-serif;
  font-size: clamp(12rem, 28vw, 32rem);
  font-weight: 800;
  line-height: 1;
  color: var(--color-surface);
  user-select: none;
  pointer-events: none;
  z-index: 0;
}
```

### Buttons

```css
.btn-brutal {
  display: inline-flex;
  align-items: center;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.875rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  padding: 0.875rem 1.75rem;
  text-decoration: none;
  border: var(--border-raw);
  transition: background 120ms var(--ease-brutal), color 120ms var(--ease-brutal),
              transform 80ms var(--ease-brutal);
  position: relative;
}

/* Brutal shadow — offset block */
.btn-brutal::after {
  content: '';
  position: absolute;
  inset: 0;
  translate: 4px 4px;
  background: var(--color-border);
  z-index: -1;
  transition: translate 80ms var(--ease-brutal);
}

.btn-brutal:hover::after { translate: 2px 2px; }
.btn-brutal:active::after { translate: 0px 0px; }
.btn-brutal:hover { transform: translate(-2px, -2px); }
.btn-brutal:active { transform: translate(0, 0); }

.btn-primary { background: var(--color-accent); color: var(--color-ink); }
.btn-primary:hover { background: var(--color-ink); color: var(--color-accent); }

.btn-ghost { background: transparent; color: var(--color-ink); }
.btn-ghost:hover { background: var(--color-ink); color: var(--color-base); }
```

### Work Grid Section

```html
<section class="work-section" id="work" data-scroll-enter>
  <div class="work-header">
    <h2 class="work-heading">Selected Work</h2>
    <a href="/work" class="work-see-all">All projects (47) →</a>
  </div>

  <div class="work-grid">
    <a href="/work/vanta" class="work-item" data-work-item>
      <div class="work-img-wrap">
        <img src="/work/vanta-thumb.jpg" alt="Vanta brand identity" loading="lazy" width="800" height="600">
        <div class="work-overlay">
          <span class="work-cta">View project →</span>
        </div>
      </div>
      <div class="work-meta">
        <div class="work-tags">
          <span class="tag">Brand Identity</span>
          <span class="tag">Motion</span>
        </div>
        <h3 class="work-title">Vanta</h3>
        <span class="work-year">2025</span>
      </div>
    </a>

    <!-- More items... -->
  </div>
</section>
```

```css
.work-section {
  padding-block: var(--section-gap);
  padding-inline: var(--space-8);
  border-top: var(--border-raw);
}

.work-header {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  margin-bottom: var(--space-12);
  border-bottom: var(--border-raw);
  padding-bottom: var(--space-6);
}

.work-heading {
  font-family: 'Monument Extended', sans-serif;
  font-size: var(--text-h2);
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: -0.02em;
}

.work-see-all {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.8125rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--color-muted);
  text-decoration: none;
}
.work-see-all:hover { color: var(--color-ink); }

/* Asymmetric grid — NOT equal columns */
.work-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0;
}

.work-item:nth-child(1) { grid-column: span 2; border: var(--border-raw); }
.work-item:nth-child(2) { border: var(--border-raw); border-top: none; }
.work-item:nth-child(3) { border: var(--border-raw); border-top: none; border-left: none; }
.work-item:nth-child(4) { grid-column: span 2; border: var(--border-raw); border-top: none; }

.work-item { text-decoration: none; color: inherit; display: block; overflow: hidden; }

.work-img-wrap {
  position: relative;
  overflow: hidden;
  aspect-ratio: 16 / 9;
}

.work-img-wrap img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 500ms var(--ease-brutal);
}

.work-item:hover .work-img-wrap img { transform: scale(1.04); }

.work-overlay {
  position: absolute;
  inset: 0;
  background: var(--color-accent);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 200ms;
}
.work-item:hover .work-overlay { opacity: 0.85; }

.work-cta {
  font-family: 'Monument Extended', sans-serif;
  font-size: 1.25rem;
  font-weight: 800;
  text-transform: uppercase;
  color: var(--color-ink);
}

.work-meta {
  display: flex;
  align-items: center;
  gap: var(--space-4);
  padding: var(--space-4) var(--space-6);
  border-top: var(--border-raw);
}

.work-tags { display: flex; gap: var(--space-2); flex: 1; }

.tag {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.625rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  padding: 0.2rem 0.6rem;
  border: 1px solid var(--color-border);
  color: var(--color-muted);
}

.work-title {
  font-family: 'Monument Extended', sans-serif;
  font-size: 1rem;
  font-weight: 800;
  text-transform: uppercase;
}

.work-year {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.75rem;
  color: var(--color-muted);
}

@media (max-width: 768px) {
  .work-grid { grid-template-columns: 1fr; }
  .work-item:nth-child(n) { grid-column: span 1; }
  .work-item + .work-item { border-top: none; border-left: var(--border-raw); }
}
```

### Manifesto Section

```html
<section class="manifesto" data-scroll-enter>
  <div class="manifesto-number" aria-hidden="true">01</div>
  <div class="manifesto-content">
    <h2 class="manifesto-heading">
      We make things that don't look like<br>
      <span class="mf-accent">other things.</span>
    </h2>
    <div class="manifesto-body">
      <p>Most agencies give you what you expect. A safe gradient. A clean serif. A hero that could belong to any company.</p>
      <p>We do the opposite. Every project starts with a question: what would make this unmistakably yours? What's the visual gesture that no one else would make?</p>
    </div>
  </div>
</section>
```

```css
.manifesto {
  padding-block: var(--section-gap);
  padding-inline: var(--space-8);
  border-top: var(--border-raw);
  display: grid;
  grid-template-columns: auto 1fr;
  gap: var(--space-12);
  align-items: start;
  position: relative;
  overflow: hidden;
}

.manifesto-number {
  font-family: 'Monument Extended', sans-serif;
  font-size: clamp(4rem, 10vw, 12rem);
  font-weight: 800;
  line-height: 1;
  color: var(--color-surface);
  user-select: none;
  position: absolute;
  top: var(--space-8);
  left: var(--space-8);
  z-index: 0;
}

.manifesto-content { position: relative; z-index: 1; }

.manifesto-heading {
  font-family: 'Monument Extended', sans-serif;
  font-size: var(--text-display);
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: -0.03em;
  line-height: 0.9;
  margin-bottom: var(--space-8);
}

.mf-accent {
  color: var(--color-accent);
  -webkit-text-stroke: 2px var(--color-ink);
  text-stroke: 2px var(--color-ink);
}

.manifesto-body {
  max-width: 56ch;
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
  color: var(--color-muted);
  line-height: 1.65;
  border-left: var(--border-accent);
  padding-left: var(--space-6);
}
```

---

## Page 2 — Case Study Layout

```html
<!-- Case study detail page -->
<main class="case-study">
  <header class="case-header">
    <div class="case-tags" data-enter="0">
      <span class="tag">Brand Identity</span>
      <span class="tag">Motion Design</span>
    </div>
    <h1 class="case-title" data-enter="1">Vanta</h1>
    <p class="case-descriptor" data-enter="2">
      Security compliance doesn't have to look like fear.
    </p>
    <div class="case-meta" data-enter="3">
      <div class="meta-item">
        <span class="meta-label">Year</span>
        <span class="meta-value">2025</span>
      </div>
      <div class="meta-item">
        <span class="meta-label">Scope</span>
        <span class="meta-value">Brand / Motion / Web</span>
      </div>
      <div class="meta-item">
        <span class="meta-label">Duration</span>
        <span class="meta-value">8 weeks</span>
      </div>
    </div>
  </header>

  <!-- Hero image — full width -->
  <figure class="case-hero-img" data-enter="4">
    <img src="/work/vanta-hero.jpg" alt="Vanta brand system overview" fetchpriority="high" width="2400" height="1350">
  </figure>

  <!-- Content sections with variable layout -->
  <section class="case-section" data-scroll-enter>
    <h2>The Challenge</h2>
    <p>...</p>
  </section>

  <!-- Image pair — intentional asymmetry -->
  <div class="case-media-pair" data-scroll-enter>
    <figure class="media-large">
      <img src="/work/vanta-01.jpg" alt="..." loading="lazy" width="1200" height="900">
    </figure>
    <figure class="media-small">
      <img src="/work/vanta-02.jpg" alt="..." loading="lazy" width="800" height="1200">
    </figure>
  </div>

  <!-- Navigation to next project -->
  <nav class="case-nav" aria-label="Project navigation" data-scroll-enter>
    <a href="/work/railway" class="case-nav-next">
      <span class="nav-label">Next project</span>
      <span class="nav-title">Railway</span>
      <span class="nav-arrow">→</span>
    </a>
  </nav>
</main>
```

```css
.case-header {
  padding: calc(80px + var(--space-12)) var(--space-8) var(--space-12);
  border-bottom: var(--border-raw);
  display: flex;
  flex-direction: column;
  gap: var(--space-6);
}

.case-title {
  font-family: 'Monument Extended', sans-serif;
  font-size: var(--text-display);
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: -0.04em;
  line-height: 0.9;
}

.case-meta {
  display: flex;
  gap: var(--space-8);
  padding-top: var(--space-6);
  border-top: var(--border-raw);
}

.meta-item {
  display: flex;
  flex-direction: column;
  gap: var(--space-1);
}

.meta-label {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.625rem;
  text-transform: uppercase;
  letter-spacing: 0.15em;
  color: var(--color-muted);
}

.meta-value {
  font-family: 'Monument Extended', sans-serif;
  font-size: 1rem;
  font-weight: 800;
  text-transform: uppercase;
}

.case-hero-img {
  width: 100%;
  margin: 0;
  border-bottom: var(--border-raw);
}

.case-hero-img img {
  width: 100%;
  height: auto;
  display: block;
}

.case-section {
  max-width: 72ch;
  margin-inline: auto;
  padding: var(--section-gap) var(--space-8);
}

.case-section h2 {
  font-family: 'Monument Extended', sans-serif;
  font-size: var(--text-h2);
  font-weight: 800;
  text-transform: uppercase;
  margin-bottom: var(--space-6);
  border-left: var(--border-accent);
  padding-left: var(--space-4);
}

/* Asymmetric image pair */
.case-media-pair {
  display: grid;
  grid-template-columns: 2fr 1fr;
  border-top: var(--border-raw);
  border-bottom: var(--border-raw);
}

.media-large, .media-small { margin: 0; overflow: hidden; }
.media-small { border-left: var(--border-raw); }

.case-media-pair img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

/* Case study footer nav */
.case-nav {
  border-top: var(--border-raw);
  padding: var(--space-8);
}

.case-nav-next {
  display: flex;
  align-items: center;
  gap: var(--space-4);
  text-decoration: none;
  color: var(--color-ink);
  transition: gap 200ms var(--ease-brutal);
}
.case-nav-next:hover { gap: var(--space-8); }

.nav-label {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--color-muted);
}

.nav-title {
  font-family: 'Monument Extended', sans-serif;
  font-size: var(--text-h2);
  font-weight: 800;
  text-transform: uppercase;
  line-height: 1;
}

.nav-arrow {
  font-size: 2rem;
  margin-left: auto;
  transition: transform 200ms var(--ease-brutal);
}
.case-nav-next:hover .nav-arrow { transform: translateX(8px); }
```

---

## Character Scramble Effect

Applied to `data-scramble` elements on load.

```javascript
class CharScramble {
  constructor(el) {
    this.el = el;
    this.original = el.textContent;
    this.chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%';
    this.iteration = 0;
  }

  scramble() {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    clearInterval(this.interval);

    this.interval = setInterval(() => {
      this.el.textContent = this.original
        .split('')
        .map((char, i) => {
          if (char === ' ') return ' ';
          if (i < this.iteration) return this.original[i];
          return this.chars[Math.floor(Math.random() * this.chars.length)];
        })
        .join('');

      if (this.iteration >= this.original.length) {
        clearInterval(this.interval);
      }
      this.iteration += 0.5;
    }, 30);
  }
}

// Fire on page load for hero elements
document.addEventListener('DOMContentLoaded', () => {
  const delay = window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 0 : 200;

  document.querySelectorAll('[data-scramble]').forEach((el, i) => {
    const scrambler = new CharScramble(el);
    setTimeout(() => scrambler.scramble(), delay + i * 150);
  });

  // Also fire on hover for nav links
  document.querySelectorAll('.work-title').forEach(el => {
    const scrambler = new CharScramble(el);
    el.closest('.work-item').addEventListener('mouseenter', () => scrambler.scramble());
  });
});
```

---

## View Transitions for Case Study

```css
/* globals.css */
@view-transition { navigation: auto; }

/* Project title morphs between grid and case study */
.work-title { view-transition-name: none; }  /* default: no transition name */

.work-item[data-project="vanta"] .work-title {
  view-transition-name: project-title-vanta;
}
.case-study[data-project="vanta"] .case-title {
  view-transition-name: project-title-vanta;
}

::view-transition-old(project-title-vanta),
::view-transition-new(project-title-vanta) {
  animation-duration: 500ms;
  animation-timing-function: var(--ease-brutal);
}

/* Page transition: brutal slide */
::view-transition-old(root) {
  animation: 300ms var(--ease-brutal) both slide-out-brutal;
}
::view-transition-new(root) {
  animation: 300ms var(--ease-brutal) 200ms both slide-in-brutal;
}

@keyframes slide-out-brutal {
  to { opacity: 0; transform: translateY(-40px); }
}
@keyframes slide-in-brutal {
  from { opacity: 0; transform: translateY(40px); }
}

@media (prefers-reduced-motion: reduce) {
  ::view-transition-old(root), ::view-transition-new(root) { animation: none; }
}
```

---

## Accessibility Notes

| Element | Implementation |
|---|---|
| Nav toggle | `aria-expanded` toggled by JS, `aria-controls` wired to mobile menu id |
| Work grid | Each `<a>` wraps the full card — one focus target, descriptive link text |
| Case meta labels | `<dt>`/`<dd>` semantics ideal; here implemented with spans + visual label pattern |
| Marquee ticker | `aria-hidden="true"` on ticker — redundant with nav links |
| Decorative numbers | `aria-hidden="true"` on giant background numbers |
| Image pairs | Each `<figure>` has descriptive `alt` text on `<img>` |
| Video reel (if added) | `autoplay muted loop playsinline` + fallback poster image |

---

## Performance Notes

- Monument Extended: `font-display: swap` + preload the 800 weight only
- JetBrains Mono: variable font — single file covers all weights
- Work grid images: `loading="lazy"` except first item (`loading="eager"`)
- Case study hero: `fetchpriority="high"` + preload in `<head>`
- Scramble effect: zero dependencies, ~30 lines of JS

---

*Example version: global-design-skill v1.0 — `examples/websites/02-agency-portfolio.md`*  
*Updated: 2026-05-20*  
*Archetype: C — Cyberbrutalism*  
*Related: `blueprints/portfolio-from-scratch.md`, `references/portfolios.md`, `patterns/effects/text-animations.md`*
