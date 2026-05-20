# Blueprint — Interactive Landing Page (Wow Stack)

> Full-effects landing page assembled from grain + mesh + spotlight + parallax + text reveal + hover effects + page transitions. Use when the goal is maximum visual impact, not just conversion.

---

## When to Use This Blueprint

| Use this | Skip this |
|---|---|
| Product hero with strong visual identity | B2B lead-gen form-first pages |
| Portfolio / agency / creative studio | High-bounce, intent-driven SaaS |
| Premium launch / announcement page | Complex multi-step onboarding |
| When the experience IS the product | Fast-shipping MVP with no design budget |

For standard landing pages: use `blueprints/landing-page-from-scratch.md` instead.

---

## Pre-Build Decisions (Fill These In)

Before writing a line of code, answer:

1. **Archetype:** (pick from A–H in `rules/01-visual-hierarchy.md`) ___
2. **The One Memorable Thing:** (what will visitors remember in 3 days?) ___
3. **Primary accent OKLCH:** `oklch(___ ___ ___)` ___
4. **Background strategy:** dark / light / mid-tone ___
5. **Motion budget:** CSS-only / CSS + GSAP / Three.js ___
6. **Hero visual:** screenshot / 3D / abstract / typographic ___

---

## Architecture

```
Section 1 — Hero              ← [data-enter] sequence + mesh bg + spotlight
Section 2 — Value / Feature   ← scroll reveal, horizontal scroll or pinned stack
Section 3 — Social Proof      ← infinite marquee or grid reveal
Section 4 — Product Demo      ← 3D tilt showcase or scrollytelling
Section 5 — CTA               ← magnetic button + atmospheric glow
```

---

## Step 1 — Token Foundation

```css
/* Set these FIRST — every effect references these variables */
:root {
  /* Palette */
  --color-base:    oklch(8% 0.015 258);
  --color-surface: oklch(13% 0.012 258);
  --color-border:  oklch(100% 0 0 / 0.1);
  --color-text:    oklch(94% 0.005 258);
  --color-muted:   oklch(50% 0.01 258);
  --color-accent:  oklch(65% 0.22 258);

  /* Typography */
  --text-hero:    clamp(3.5rem, 8vw + 1rem, 10rem);
  --text-display: clamp(2.5rem, 5vw + 0.5rem, 6rem);
  --text-h2:      clamp(1.75rem, 3vw + 0.5rem, 3.5rem);
  --text-body:    clamp(1rem, 1.2vw + 0.4rem, 1.2rem);

  /* Motion */
  --ease-smooth: cubic-bezier(0.22, 1, 0.36, 1);
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
  --ease-expo:   cubic-bezier(0.87, 0, 0.13, 1);

  /* Spacing */
  --section-gap: clamp(6rem, 10vw, 12rem);

  /* Z-index stack */
  --z-grain:   9999;
  --z-cursor:  9998;
  --z-nav:     100;
  --z-toast:   200;
}
```

---

## Step 2 — Global Atmosphere

Applied once to `<body>` — active on every section.

```css
/* Grain texture — mandatory base */
body {
  background-color: var(--color-base);
  color: var(--color-text);
  overflow-x: hidden;
}

body::after {
  content: '';
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: var(--z-grain);
  opacity: 0.04;
  mix-blend-mode: overlay;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
  background-size: 256px 256px;
}

/* Spotlight — follows cursor */
body::before {
  content: '';
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 0;
  background: radial-gradient(
    900px circle at var(--cursor-x, 50%) var(--cursor-y, 50%),
    oklch(from var(--color-accent) l c h / 0.06),
    transparent 55%
  );
  transition: background 50ms linear;
}
```

```javascript
// Update spotlight position
document.addEventListener('mousemove', (e) => {
  document.documentElement.style.setProperty('--cursor-x', `${e.clientX}px`);
  document.documentElement.style.setProperty('--cursor-y', `${e.clientY}px`);
});
```

---

## Step 3 — Hero Section

```html
<section class="hero" data-section="hero">
  <div class="hero-bg mesh-bg"></div>

  <nav class="site-nav" data-enter="0">
    <a href="/" class="nav-logo">Logo</a>
    <ul class="nav-links">
      <li><a href="#features">Features</a></li>
      <li><a href="#pricing">Pricing</a></li>
    </ul>
    <a href="/signup" class="btn-primary" data-magnetic>Get access</a>
  </nav>

  <div class="hero-content">
    <span class="eyebrow" data-enter="1">Now in public beta</span>

    <h1 class="hero-heading" data-enter="2">
      <span class="split-line" data-split>Ship faster.</span>
      <span class="split-line split-line--accent" data-split>Stay proud.</span>
    </h1>

    <p class="hero-subtext" data-enter="3">
      Design-to-code in minutes, not hours.
      The component library for teams who care.
    </p>

    <div class="hero-actions" data-enter="4">
      <a href="/signup" class="btn-primary btn-magnetic" data-magnetic>
        Start for free
      </a>
      <a href="/demo" class="btn-ghost">Watch demo →</a>
    </div>

    <p class="hero-trust" data-enter="5">
      No credit card required. Ships with 200+ components.
    </p>
  </div>

  <div class="hero-visual" data-enter="6" data-tilt>
    <div class="tilt-inner">
      <div class="tilt-layer" data-depth="0.1">
        <div class="product-glow"></div>
      </div>
      <div class="tilt-layer" data-depth="0.3">
        <img
          class="product-screenshot"
          src="/product-preview.png"
          alt="Product UI preview"
          fetchpriority="high"
          width="1200"
          height="800"
        >
      </div>
    </div>
  </div>
</section>
```

```css
.hero {
  position: relative;
  min-height: 100dvh;
  display: grid;
  grid-template-rows: auto 1fr;
  padding-inline: var(--space-8);
  overflow: hidden;
}

.hero-bg {
  position: absolute;
  inset: 0;
  z-index: 0;
}

.mesh-bg {
  background:
    radial-gradient(ellipse 60% 50% at 20% 60%, oklch(55% 0.22 280 / 0.3) 0%, transparent 70%),
    radial-gradient(ellipse 50% 40% at 80% 20%, oklch(65% 0.18 200 / 0.2) 0%, transparent 60%),
    var(--color-base);
}

.hero-content {
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: var(--space-6);
  padding-block: var(--section-gap);
  max-width: 680px;
}

.hero-heading {
  font-size: var(--text-hero);
  font-weight: 900;
  line-height: 0.95;
  letter-spacing: -0.04em;
}

.split-line--accent {
  color: var(--color-accent);
}

.hero-subtext {
  font-size: var(--text-body);
  color: var(--color-muted);
  max-width: 44ch;
  line-height: 1.6;
}

.hero-trust {
  font-size: 0.8rem;
  color: oklch(45% 0.01 258);
}

.hero-visual {
  position: absolute;
  right: -5%;
  top: 50%;
  transform: translateY(-50%);
  width: 55%;
  z-index: 1;
}

@media (max-width: 900px) {
  .hero-visual { display: none; }
  .hero-content { max-width: 100%; }
}
```

---

## Step 4 — Entrance Sequence

```css
/* All [data-enter] elements start invisible */
[data-enter] {
  opacity: 0;
  transform: translateY(16px);
  filter: blur(4px);
}

[data-enter].entered {
  opacity: 1;
  transform: translateY(0);
  filter: blur(0);
  transition:
    opacity 700ms var(--ease-smooth),
    transform 700ms var(--ease-spring),
    filter 700ms var(--ease-smooth);
}

[data-enter="0"].entered { transition-delay: 0ms; }
[data-enter="1"].entered { transition-delay: 80ms; }
[data-enter="2"].entered { transition-delay: 140ms; }
[data-enter="3"].entered { transition-delay: 220ms; }
[data-enter="4"].entered { transition-delay: 300ms; }
[data-enter="5"].entered { transition-delay: 380ms; }
[data-enter="6"].entered { transition-delay: 200ms; }

@media (prefers-reduced-motion: reduce) {
  [data-enter] { opacity: 1; transform: none; filter: none; transition: none; }
}
```

```javascript
document.addEventListener('DOMContentLoaded', () => {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  requestAnimationFrame(() => {
    requestAnimationFrame(() => {
      document.querySelectorAll('[data-enter]').forEach(el => el.classList.add('entered'));
    });
  });
});
```

---

## Step 5 — Scroll Reveal Sections

All sections below the fold use `data-scroll-enter` instead of `data-enter`.

```css
[data-scroll-enter] {
  opacity: 0;
  transform: translateY(32px);
  transition: opacity 600ms var(--ease-smooth), transform 600ms var(--ease-spring);
}

[data-scroll-enter].entered {
  opacity: 1;
  transform: translateY(0);
}

@media (prefers-reduced-motion: reduce) {
  [data-scroll-enter] { opacity: 1; transform: none; transition: none; }
}
```

```javascript
const scrollObserver = new IntersectionObserver(
  (entries) => entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('entered');
      scrollObserver.unobserve(entry.target);
    }
  }),
  { threshold: 0.1, rootMargin: '0px 0px -80px 0px' }
);

document.querySelectorAll('[data-scroll-enter]').forEach(el => scrollObserver.observe(el));
```

---

## Step 6 — Features Section (Pinned Stack)

```html
<section class="features" id="features">
  <div class="features-sticky-container" data-pin-stack>
    <div class="feature-card" data-scroll-enter>
      <div class="feature-tag">01 — Speed</div>
      <h2>Design that ships in hours</h2>
      <p>...</p>
    </div>
    <div class="feature-card" data-scroll-enter>
      <div class="feature-tag">02 — Quality</div>
      <h2>Built to last, not to demo</h2>
      <p>...</p>
    </div>
    <div class="feature-card" data-scroll-enter>
      <div class="feature-tag">03 — System</div>
      <h2>One source. Every platform.</h2>
      <p>...</p>
    </div>
  </div>
</section>
```

```javascript
// GSAP stacking cards — see patterns/effects/scroll-experiences.md
import gsap from 'gsap';
import ScrollTrigger from 'gsap/ScrollTrigger';
gsap.registerPlugin(ScrollTrigger);

gsap.matchMedia().add('(prefers-reduced-motion: no-preference)', () => {
  const cards = gsap.utils.toArray('.feature-card');
  cards.forEach((card, i) => {
    ScrollTrigger.create({
      trigger: card,
      start: 'top top+=80',
      pin: true,
      pinSpacing: false,
    });
    gsap.to(card, {
      scale: 1 - (cards.length - i) * 0.025,
      transformOrigin: 'top center',
      ease: 'none',
      scrollTrigger: {
        trigger: card,
        start: 'top top+=80',
        end: 'bottom top+=80',
        scrub: true,
      }
    });
  });
});
```

---

## Step 7 — Social Proof Marquee

```html
<section class="logos" aria-label="Used by teams at" data-scroll-enter>
  <p class="logos-label">Trusted by teams at</p>
  <div class="marquee" role="marquee" aria-live="off">
    <div class="marquee-track">
      <span class="logo-item">Vercel</span>
      <span class="logo-item">Linear</span>
      <span class="logo-item">Notion</span>
      <span class="logo-item">Railway</span>
      <span class="logo-item">Resend</span>
      <!-- Duplicate for seamless loop -->
      <span class="logo-item" aria-hidden="true">Vercel</span>
      <span class="logo-item" aria-hidden="true">Linear</span>
      <!-- ... -->
    </div>
  </div>
</section>
```

```css
.marquee {
  overflow: hidden;
  mask-image: linear-gradient(to right, transparent, black 15%, black 85%, transparent);
}

.marquee-track {
  display: flex;
  gap: var(--space-12);
  width: max-content;
  animation: marquee-scroll 24s linear infinite;
}

.logo-item {
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--color-muted);
  white-space: nowrap;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

@keyframes marquee-scroll {
  from { transform: translateX(0); }
  to   { transform: translateX(-50%); }
}

@media (prefers-reduced-motion: reduce) {
  .marquee-track { animation: none; }
}
```

---

## Step 8 — CTA Section

```html
<section class="cta-section" data-scroll-enter>
  <div class="cta-glow"></div>

  <span class="eyebrow">Start today</span>
  <h2 class="cta-heading">Ready to ship better?</h2>
  <p class="cta-subtext">Join 2,000+ teams already using the system.</p>

  <a href="/signup" class="btn-primary btn-magnetic btn-lg" data-magnetic>
    Get started free
  </a>
</section>
```

```css
.cta-section {
  position: relative;
  text-align: center;
  padding-block: var(--section-gap);
  overflow: hidden;
}

.cta-glow {
  position: absolute;
  top: -40%;
  left: 50%;
  translate: -50% 0;
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, oklch(from var(--color-accent) l c h / 0.15), transparent 65%);
  pointer-events: none;
  filter: blur(60px);
}

.cta-heading {
  font-size: var(--text-display);
  font-weight: 900;
  letter-spacing: -0.04em;
  margin-block: var(--space-4) var(--space-6);
}
```

---

## Step 9 — Button Components

```css
.btn-primary {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  padding: 0.875rem 2rem;
  background: var(--color-accent);
  color: oklch(98% 0.005 258);
  border-radius: var(--radius-full);
  font-weight: 600;
  font-size: 0.9375rem;
  text-decoration: none;
  transition: transform 200ms var(--ease-spring), box-shadow 200ms var(--ease-smooth);
  position: relative;
  overflow: hidden;
}

.btn-primary::after {
  content: '';
  position: absolute;
  inset: 0;
  background: oklch(100% 0 0 / 0.15);
  opacity: 0;
  transition: opacity 200ms;
}

.btn-primary:hover::after { opacity: 1; }

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 32px oklch(from var(--color-accent) l c h / 0.4);
}

.btn-primary:active { transform: translateY(0); }

.btn-ghost {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  padding: 0.875rem 1.5rem;
  color: var(--color-muted);
  text-decoration: none;
  font-weight: 500;
  transition: color 200ms;
}
.btn-ghost:hover { color: var(--color-text); }

.btn-lg { padding: 1.125rem 2.5rem; font-size: 1.0625rem; }

/* Magnetic button — uses MagneticButton class from hover-effects.md */
```

---

## Step 10 — View Transitions

```css
/* globals.css */
@view-transition {
  navigation: auto;
}

::view-transition-old(root) {
  animation: 250ms var(--ease-expo) both page-exit;
}

::view-transition-new(root) {
  animation: 350ms var(--ease-spring) both page-enter;
}

@keyframes page-exit {
  to { opacity: 0; transform: translateY(-12px); filter: blur(4px); }
}

@keyframes page-enter {
  from { opacity: 0; transform: translateY(12px); filter: blur(4px); }
}

@media (prefers-reduced-motion: reduce) {
  ::view-transition-old(root),
  ::view-transition-new(root) { animation: none; }
}
```

---

## Assembly Checklist

Before calling the page done:

**Atmosphere**
- [ ] Grain texture active on `body::after`
- [ ] Mesh gradient on hero background
- [ ] Spotlight cursor effect enabled (remove on `pointer: coarse`)
- [ ] All background layers don't interfere with text contrast

**Entrance**
- [ ] `[data-enter]` on all above-fold elements in correct order
- [ ] Stagger delays feel natural (80–100ms between groups)
- [ ] `[data-scroll-enter]` on all below-fold sections

**Effects**
- [ ] Tilt effect on product visual (desktop only)
- [ ] Magnetic button on primary CTAs
- [ ] Marquee logo strip (if social proof section exists)
- [ ] GSAP ScrollTrigger import only if JS budget allows

**Transitions**
- [ ] `@view-transition { navigation: auto }` in global CSS
- [ ] Custom enter/exit animations defined

**Accessibility**
- [ ] `prefers-reduced-motion` disables ALL animations/transitions
- [ ] `aria-hidden="true"` on decorative canvases and marquee duplicates
- [ ] Focus order follows visual reading order
- [ ] CTA link text is descriptive (not "Get Started" — add context)

**Performance**
- [ ] Hero image: `fetchpriority="high"` + `<link rel="preload">`
- [ ] Three.js / Spline loaded only if not `prefers-reduced-motion`
- [ ] `will-change: transform` removed after animations complete
- [ ] No `transition: all` anywhere

**Mobile**
- [ ] Tilt / cursor effects disabled on `pointer: coarse`
- [ ] Hero layout switches to single column
- [ ] `min-height: 100dvh` (not `100vh`)
- [ ] Font sizes readable at 375px width

---

## Archetype-Specific Starters

### Archetype A — Ethereal Black (SaaS / AI)
```css
:root {
  --color-base:   oklch(6% 0.01 258);
  --color-accent: oklch(70% 0.25 258); /* electric blue */
}
/* Fonts: Geist Display (headings) + Geist Mono (code/data) */
```

### Archetype B — Editorial Luxury (Agency)
```css
:root {
  --color-base:   oklch(97% 0.008 80); /* warm cream */
  --color-accent: oklch(35% 0.05 55);  /* deep espresso */
}
/* Fonts: Playfair Display Variable + DM Sans */
/* Motion: slow parallax, mask reveals, no blur effects */
```

### Archetype C — Cyberbrutalism (Portfolio / Studio)
```css
:root {
  --color-base:   oklch(100% 0 0);    /* pure white */
  --color-accent: oklch(70% 0.35 95); /* neon yellow */
  --radius-base: 0;                   /* no radius anywhere */
}
/* Fonts: Monument Extended + JetBrains Mono */
/* Layout: raw borders, no shadows */
```

### Archetype E — Volumetric Glass (Premium SaaS)
```css
:root {
  --color-base:    oklch(10% 0.02 265); /* midnight */
  --color-surface: oklch(14% 0.018 265);
  --color-accent:  oklch(75% 0.18 200); /* teal */
}
/* Fonts: Cabinet Grotesk + JetBrains Mono */
/* Glass cards with backdrop-filter throughout */
```

---

*Blueprint version: global-design-skill v1.0 — `blueprints/interactive-landing-page.md`*  
*Updated: 2026-05-20*  
*Required: `tokens/tokens.css`, `rules/05-animation.md`, `rules/14-landing-pages.md`*  
*Related: `patterns/effects/` (all), `recipes/create-wow-hero.md`, `checklists/wow-effects-checklist.md`*
