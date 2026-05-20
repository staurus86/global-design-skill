# Recipe — Create a Wow Hero Section

> The step-by-step process for building a hero section that makes people stop scrolling. Not "make it look nice" — a specific sequence with specific techniques. Takes a functional hero from 0 to unforgettable in 9 steps.

---

## Before You Start

**Decision checkpoint:**
1. Which aesthetic archetype? (see `references/aesthetic-archetypes.md`) — commit before step 1
2. What is the ONE memorable thing? Write it in one sentence: "The one thing people remember 3 days later is ___"
3. What is the product's best proof? A number, a visual, a demo, a quote?

**Time estimates:** 2–3 hours for a complete wow hero from scratch

---

## Step 1 — Lock the Headline Formula

The headline is 80% of the hero. Everything else is context for it.

**Formula:** `[Specific result] + [Timeframe or context]`

| Before (generic) | After (specific) |
|---|---|
| "Ship faster" | "Deploy in 23 seconds" |
| "Manage your team" | "Cut standups from 45 minutes to 8" |
| "Scale with confidence" | "From 0 to 1M users — without rewriting your stack" |
| "The all-in-one platform" | "One command. 40 regions. Zero config." |

**Headline constraints:**
- Maximum 2 lines on desktop (test at 1280px)
- Maximum 3 words per line on mobile (test at 390px)
- Must work without the subtitle (if you remove the subtitle, the headline should still make sense)
- No banned words: "seamless", "elevate", "unleash", "empower", "revolutionize", "next-gen"

**Add the eyebrow first:**
```html
<span class="eyebrow">Now in public beta</span>
<!-- or: -->
<span class="eyebrow">Used by 18,000 teams</span>
<!-- or: -->
<span class="eyebrow">YC S24 · #1 on Product Hunt</span>
```

---

## Step 2 — Choose the Layout

Never center. Choose from three layouts — each serves a different story.

**Layout A — Editorial Split (default for SaaS)**
```
┌─────────────────────────────────────────────────┐
│  [Eyebrow]                                       │
│                                                  │
│  Deploy in 23 seconds,      ┌───────────────┐   │
│  roll back in 10.           │               │   │
│                             │  Product      │   │
│  Push to GitHub and         │  Screenshot   │   │
│  your changes are live.     │               │   │
│                             └───────────────┘   │
│  [CTA] [secondary link]                          │
│  Trust signal                                    │
└─────────────────────────────────────────────────┘
```

**Layout B — Full-Bleed with Overlay (for experiences/narrative)**
```
┌─────────────────────────────────────────────────┐
│  ████████████████████████████████████████████   │
│  ██  Background: video / gradient / 3D  █████   │
│  ██                                     █████   │
│  ██  [Eyebrow]                          █████   │
│  ██  The headline here.                 █████   │
│  ██  Subtitle text.                     █████   │
│  ██  [CTA]                              █████   │
│  ████████████████████████████████████████████   │
└─────────────────────────────────────────────────┘
```

**Layout C — Asymmetric (for bold/editorial positioning)**
```
┌─────────────────────────────────────────────────┐
│                              [Eyebrow]           │
│  ████████████████████        [H1 large]          │
│  ████████████████████        [H1 continued]      │
│  ██ Product visual  ██                           │
│  ████████████████████        [Subtitle]          │
│  ████████████████████                            │
│                              [CTA] [Link]        │
└─────────────────────────────────────────────────┘
```

---

## Step 3 — Build the Background (The Atmosphere)

This is where wow starts. The background should communicate the archetype before a word is read.

**For Ethereal Black (archetype A):**
```css
.hero {
  background:
    /* Mesh gradient blobs */
    radial-gradient(ellipse 50% 60% at 15% 70%, oklch(55% 0.22 280 / 0.3) 0%, transparent 65%),
    radial-gradient(ellipse 40% 50% at 85% 20%, oklch(65% 0.18 200 / 0.2) 0%, transparent 55%),
    /* Dot grid */
    radial-gradient(circle, oklch(100% 0 0 / 0.05) 1px, transparent 1px),
    /* Base */
    oklch(8% 0.01 260);
  background-size: auto, auto, 24px 24px, auto;
}

/* Spotlight layer */
.hero::after {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(
    800px at var(--cursor-x, 50%) var(--cursor-y, 50%),
    oklch(55% 0.15 258 / 0.08),
    transparent 50%
  );
  pointer-events: none;
}
```

**For Editorial Luxury (archetype B):**
```css
.hero {
  background: oklch(97% 0.008 80); /* Warm cream */
  position: relative;
}

/* Subtle bottom gradient fade */
.hero::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 40%;
  background: linear-gradient(to bottom, transparent, oklch(95% 0.01 80));
  pointer-events: none;
}
```

**For Organic Softness (archetype D):**
```css
.hero {
  background:
    radial-gradient(ellipse 60% 80% at 10% 50%, oklch(80% 0.08 155 / 0.4) 0%, transparent 60%),
    radial-gradient(ellipse 50% 60% at 90% 80%, oklch(75% 0.1 40 / 0.3) 0%, transparent 50%),
    oklch(97% 0.008 80);
}
```

Add grain on top of everything (applies to all archetypes):
```css
body::after {
  content: '';
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 9999;
  opacity: 0.035;
  mix-blend-mode: overlay;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 512 512' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
  background-size: 256px 256px;
}
```

---

## Step 4 — Typography: The Display Face

Never use only one font. The display/body split is mandatory.

```css
/* Import in <head> */
/* Ethereal Black: Geist Display + Geist Mono */
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@300..900&family=Geist+Mono:wght@400;500&display=swap');

/* Editorial: Fraunces + Instrument Sans */
@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..900;1,9..144,300..900&family=Instrument+Sans:wght@400;500;600&display=swap');

/* Bold/confident: Syne + DM Sans */
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400..800&family=DM+Sans:wght@400;500;600&display=swap');
```

```css
:root {
  --font-display: 'Fraunces', Georgia, serif;
  --font-body:    'Instrument Sans', system-ui, sans-serif;
  --text-hero:    clamp(3rem, 6vw + 1rem, 8rem);
  --text-h1:      clamp(2.5rem, 5vw + 0.5rem, 6rem);
}

.hero-heading {
  font-family: var(--font-display);
  font-size: var(--text-h1);
  line-height: 1.05;
  letter-spacing: -0.03em;
  font-weight: 700;
}

/* Italic accent on key word */
.hero-heading em {
  font-style: italic;
  color: var(--color-accent);
}
```

---

## Step 5 — The Product Visual

The right side of the split hero needs a visual that proves the headline claim.

**Option A — Product screenshot with perspective tilt:**
```html
<div class="hero-visual">
  <div class="bezel-outer">
    <div class="bezel-inner">
      <img
        src="/product-screenshot.png"
        alt="[Describe what the screenshot shows — the specific feature being claimed]"
        width="1200"
        height="800"
        loading="eager"
        fetchpriority="high"
      >
    </div>
  </div>
</div>
```

```css
.bezel-outer {
  padding: 5px;
  border-radius: 14px;
  background: linear-gradient(145deg, oklch(100% 0 0 / 0.12), oklch(100% 0 0 / 0.04));
  border: 1px solid oklch(100% 0 0 / 0.12);
  box-shadow:
    inset 0 1px 0 oklch(100% 0 0 / 0.2),
    0 32px 80px oklch(0% 0 0 / 0.6);
  transform: perspective(1200px) rotateY(-6deg) rotateX(2deg);
  transition: transform 600ms var(--ease-smooth);
}

.bezel-outer:hover {
  transform: perspective(1200px) rotateY(-2deg) rotateX(0.5deg);
}

.bezel-inner {
  border-radius: 10px;
  overflow: hidden;
  background: oklch(12% 0.02 260);
  border: 1px solid oklch(0% 0 0 / 0.4);
}
```

**Option B — Animated terminal / code block:**
```html
<div class="hero-terminal">
  <div class="terminal-bar">
    <span class="terminal-dot terminal-dot--red"></span>
    <span class="terminal-dot terminal-dot--yellow"></span>
    <span class="terminal-dot terminal-dot--green"></span>
  </div>
  <pre class="terminal-code"><code data-typewriter="$ poolr deploy --prod

✓ Connected to postgres://...
✓ Pool configured: 5 connections
✓ Deployed to 40 edge regions
✓ Live: https://your-app.poolr.io

Deploy time: 23.4s ⚡"></code></pre>
</div>
```

**Option C — Floating UI elements (No actual screenshot):**
```html
<div class="hero-visual hero-visual--floating" data-mouse-parallax>
  <div class="float-card float-card--main" data-depth="0.05">
    <!-- Main metric or feature -->
    <span class="float-value">23s</span>
    <span class="float-label">Deploy time</span>
  </div>
  <div class="float-card float-card--secondary" data-depth="0.1">
    <!-- Supporting stat -->
    <span class="float-value">✓</span>
    <span class="float-label">Production live</span>
  </div>
</div>
```

---

## Step 6 — CTA Hierarchy

One primary CTA. One optional secondary. Never equal weight.

```html
<div class="hero-actions">
  <!-- Primary: verb + object + context -->
  <a href="/signup" class="btn btn--primary btn--lg" data-magnetic>
    Deploy your first app free
  </a>

  <!-- Secondary: text link with arrow, never a button -->
  <a href="/demo" class="hero-demo-link">
    Watch 2-min demo
    <svg aria-hidden="true" width="16" height="16" viewBox="0 0 16 16"
      fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round">
      <path d="M3 8h10M8 3l5 5-5 5"/>
    </svg>
  </a>
</div>
```

```css
.btn--primary {
  background: var(--color-accent);
  color: oklch(97% 0.005 258);
  padding: var(--space-4) var(--space-8);
  border-radius: var(--radius-full);
  font-weight: var(--font-weight-semibold);
  font-size: var(--text-body);
  border: none;
  box-shadow:
    0 4px 20px oklch(from var(--color-accent) l c h / 0.4),
    inset 0 1px 0 oklch(100% 0 0 / 0.2);
  transition:
    transform 200ms var(--ease-spring),
    box-shadow 200ms var(--ease-smooth);
}

.btn--primary:hover {
  transform: translateY(-2px);
  box-shadow:
    0 8px 30px oklch(from var(--color-accent) l c h / 0.5),
    inset 0 1px 0 oklch(100% 0 0 / 0.2);
}

.hero-demo-link {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
  text-decoration: none;
  transition: color 200ms var(--ease-smooth), gap 200ms var(--ease-spring);
}

.hero-demo-link:hover {
  color: var(--color-text-primary);
  gap: var(--space-3);
}
```

---

## Step 7 — Trust Signal

One line below the CTA. Reduces the #1 conversion barrier (commitment anxiety).

```html
<p class="hero-trust">
  Trusted by 18,000 teams · No credit card required · Cancel anytime
</p>
```

```css
.hero-trust {
  font-size: var(--text-xs);
  color: var(--color-text-muted);
  display: flex;
  align-items: center;
  gap: var(--space-3);
  flex-wrap: wrap;
}

/* Dot separator */
.hero-trust > span::before {
  content: '·';
  margin-right: var(--space-3);
  opacity: 0.4;
}
.hero-trust > span:first-child::before { display: none; }
```

---

## Step 8 — Entrance Animation (The Sequence)

Every element must enter. The order is: eyebrow → headline → subtitle → CTA → trust → visual.

```css
/* Shared animation */
@keyframes hero-enter {
  from {
    opacity: 0;
    transform: translateY(16px);
    filter: blur(4px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
    filter: blur(0);
  }
}

/* Sequential stagger */
.hero-eyebrow  { animation: hero-enter 600ms var(--ease-smooth) 0ms   both; }
.hero-heading  { animation: hero-enter 800ms var(--ease-spring)  100ms both; }
.hero-subtitle { animation: hero-enter 600ms var(--ease-smooth)  300ms both; }
.hero-actions  { animation: hero-enter 500ms var(--ease-smooth)  500ms both; }
.hero-trust    { animation: hero-enter 400ms var(--ease-smooth)  650ms both; }
.hero-visual   { animation: hero-enter 900ms var(--ease-spring)  200ms both; }

@media (prefers-reduced-motion: reduce) {
  .hero-eyebrow, .hero-heading, .hero-subtitle,
  .hero-actions, .hero-trust, .hero-visual {
    animation: none;
    opacity: 1;
    transform: none;
    filter: none;
  }
}
```

---

## Step 9 — LCP Optimization

The hero image is the LCP element. It must load fast.

```html
<!-- In <head> — preload the hero image -->
<link rel="preload" as="image" href="/hero-product.png" fetchpriority="high">

<!-- The image itself -->
<img
  src="/hero-product.png"
  alt="[Descriptive alt — not 'hero image']"
  width="1200"
  height="800"
  loading="eager"
  fetchpriority="high"
  decoding="async"
>

<!-- Hero font preload -->
<link rel="preload" as="font"
  href="/fonts/fraunces-variable.woff2"
  type="font/woff2"
  crossorigin>
```

**LCP targets:**
- Hero image loads in < 2.5s on 4G
- First Contentful Paint < 1.8s
- CLS = 0 (image has explicit width/height, font uses `font-display: optional`)

---

## Complete Hero Template

```html
<section class="hero" aria-label="Hero">
  <div class="container hero-container">

    <!-- Left: Text column -->
    <div class="hero-text">
      <span class="eyebrow hero-eyebrow">Now in public beta</span>

      <h1 class="hero-heading">
        Deploy in 23&nbsp;seconds,<br>
        roll back in&nbsp;<em>10.</em>
      </h1>

      <p class="hero-subtitle">
        Push to GitHub and your changes are live — globally, on the edge,
        zero config. Your team ships. Infrastructure waits.
      </p>

      <div class="hero-actions">
        <a href="/signup" class="btn btn--primary btn--lg" data-magnetic>
          Start deploying free
        </a>
        <a href="/demo" class="hero-demo-link">
          Watch 2-min demo
          <svg aria-hidden="true" width="16" height="16" viewBox="0 0 16 16"
            fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round">
            <path d="M3 8h10M8 3l5 5-5 5"/>
          </svg>
        </a>
      </div>

      <p class="hero-trust">
        Trusted by 18,000 teams · No credit card required
      </p>
    </div>

    <!-- Right: Product visual -->
    <div class="hero-visual" data-tilt>
      <div class="bezel-outer">
        <div class="bezel-inner">
          <img
            src="/hero-dashboard.png"
            alt="Acme dashboard showing a 23-second deployment timeline"
            width="1200"
            height="800"
            loading="eager"
            fetchpriority="high"
          >
        </div>
      </div>
    </div>

  </div>
</section>
```

---

## Hero Quality Checklist

Before shipping:
- [ ] Headline answers "what + for whom + why now" in under 3 seconds
- [ ] Headline ≤ 2 lines at 1280px, ≤ 3 lines at 390px
- [ ] Zero banned words in all text
- [ ] One primary CTA (verb + object + context), one secondary text link
- [ ] Product visual has `fetchpriority="high"` and explicit dimensions
- [ ] Entrance animation has `prefers-reduced-motion` fallback
- [ ] Background uses OKLCH tokens, no hardcoded hex
- [ ] Eyebrow tag present above H1
- [ ] Trust signal below CTA
- [ ] Grain texture applied (body::after)

---

*Recipe version: global-design-skill v1.0 — `recipes/create-wow-hero.md`*  
*Updated: 2026-05-20*  
*Related: `patterns/marketing-blocks/hero-sections.md`, `patterns/effects/visual-effects.md`, `patterns/effects/hover-effects.md`, `examples/landing-pages/01-saas-hero-redesign.md`*
