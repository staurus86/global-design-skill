# Pattern — Hero Sections

> The hero is the first and most important decision on any marketing page. It establishes the aesthetic, communicates the value proposition, and sets the conversion trajectory.

---

## Decision Framework

Before choosing a layout, answer:
1. What is the LCP element? (Determines what gets `fetchpriority="high"`)
2. Is the product visual or abstract? (Determines whether screenshot or illustration makes sense)
3. What is the primary device? (Mobile-first means the mobile layout is designed first)
4. What is the aesthetic archetype? (From `SKILL.md` Section 3 — commit before writing CSS)

---

## Pattern A — Split: Text Left, Visual Right

Best for: SaaS products with a strong UI screenshot, software tools, dashboards.

```html
<section class="hero-split">
  <div class="container">
    <div class="hero-split__content">
      <span class="eyebrow">New — Spring 2026</span>
      <h1 class="hero-split__headline">Ship production UI in half the time</h1>
      <p class="hero-split__sub">The design system that goes from token to component without the ceremony.</p>
      <div class="hero-split__actions">
        <a href="/signup" class="btn-primary">Start free — no card needed</a>
        <a href="/demo" class="btn-ghost">Watch 2-min demo</a>
      </div>
      <div class="hero-split__proof">
        <img src="/logos/company-a.svg" alt="Company A" width="80" height="24" />
        <img src="/logos/company-b.svg" alt="Company B" width="80" height="24" />
        <img src="/logos/company-c.svg" alt="Company C" width="80" height="24" />
      </div>
    </div>

    <div class="hero-split__visual">
      <img
        src="/hero-dashboard.webp"
        alt="Analytics dashboard showing monthly revenue trending up 32%"
        width="720"
        height="480"
        fetchpriority="high"
      />
    </div>
  </div>
</section>
```

```css
.hero-split {
  min-height: 100dvh;
  display: flex;
  align-items: center;
  padding-block: clamp(5rem, 10vw, 8rem);
}

.hero-split .container {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--space-12);
  align-items: center;
}

@media (min-width: 768px) {
  .hero-split .container {
    grid-template-columns: 1fr 1fr;
  }
}

@media (min-width: 1280px) {
  .hero-split .container {
    grid-template-columns: 5fr 6fr; /* slight visual weight toward image */
  }
}

.hero-split__visual img {
  width: 100%;
  height: auto;
  border-radius: var(--radius-xl);
  box-shadow: 0 24px 80px oklch(0% 0 0 / 0.3);
  /* Slight upward float — breaks the flat grid */
  transform: perspective(1200px) rotateY(-4deg) rotateX(2deg);
}

.hero-split__proof {
  display: flex;
  gap: var(--space-6);
  align-items: center;
  margin-top: var(--space-8);
  opacity: 0.5;
  filter: grayscale(1);
}
```

**Entrance animation (CSS @starting-style):**
```css
.hero-split__content {
  opacity: 1;
  transform: translateY(0);
  transition: opacity 500ms, transform 500ms cubic-bezier(0.16, 1, 0.3, 1);
}

@starting-style {
  .hero-split__content {
    opacity: 0;
    transform: translateY(24px);
  }
}
```

---

## Pattern B — Centered: Full Attention on Headline

Best for: editorial brands, agencies, early-stage products, bold aesthetic archetypes.

```html
<section class="hero-centered">
  <div class="container">
    <span class="eyebrow">Design system · v2.0</span>
    <h1 class="hero-centered__headline">
      The last design system<br>you'll ever configure
    </h1>
    <p class="hero-centered__sub">
      Token-first. Component-ready. Ships with dark mode, accessibility, and motion out of the box.
    </p>
    <a href="/start" class="btn-primary btn-lg">Get started free</a>
    <p class="hero-centered__disclaimer">No credit card · Unlimited projects · Cancel anytime</p>

    <div class="hero-centered__visual">
      <img
        src="/product-preview.webp"
        alt="Component library preview showing 120+ production-ready components"
        width="1200"
        height="600"
        fetchpriority="high"
      />
    </div>
  </div>
</section>
```

```css
.hero-centered {
  text-align: center;
  padding-block: clamp(6rem, 12vw, 10rem);
}

.hero-centered__headline {
  font-size: var(--text-display);
  max-width: 16ch;
  margin-inline: auto;
}

.hero-centered__sub {
  max-width: 52ch;
  margin-inline: auto;
  color: var(--color-text-secondary);
  margin-block: var(--space-6);
}

.hero-centered__disclaimer {
  font-size: 0.875rem;
  color: var(--color-text-muted);
  margin-top: var(--space-3);
}

.hero-centered__visual {
  margin-top: var(--space-16);
  /* Image overflows container — intentional grid break */
  margin-inline: clamp(-2rem, -5vw, -6rem);
  border-radius: var(--radius-xl) var(--radius-xl) 0 0;
  overflow: hidden;
}
```

---

## Pattern C — Full-Bleed Video / Image Background

Best for: premium brands, event pages, product launches, high-impact moments.

```html
<section class="hero-fullbleed">
  <!-- Background: video or image -->
  <video
    class="hero-fullbleed__bg"
    src="/hero-bg.mp4"
    autoplay
    muted
    loop
    playsinline
    aria-hidden="true"
  ></video>
  <!-- Overlay for contrast -->
  <div class="hero-fullbleed__overlay" aria-hidden="true"></div>

  <div class="container hero-fullbleed__content">
    <span class="eyebrow" style="color: oklch(100% 0 0 / 0.7)">Now available</span>
    <h1 class="hero-fullbleed__headline">Built for speed.<br>Designed to last.</h1>
    <a href="/get-started" class="btn-primary btn-lg">Start building</a>
  </div>
</section>
```

```css
.hero-fullbleed {
  position: relative;
  min-height: 100dvh;
  display: flex;
  align-items: center;
  color: var(--color-text-inverse);
}

.hero-fullbleed__bg {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: 0;
}

.hero-fullbleed__overlay {
  position: absolute;
  inset: 0;
  background: oklch(5% 0.01 258 / 0.65);
  z-index: 1;
}

.hero-fullbleed__content {
  position: relative;
  z-index: 2;
}

.hero-fullbleed__headline {
  font-size: var(--text-hero);
  max-width: 12ch;
  color: oklch(98% 0 0);
}
```

**Accessibility:** Video background must be pausable. Add a "Pause background video" button for `prefers-reduced-motion`.
```css
@media (prefers-reduced-motion: reduce) {
  .hero-fullbleed__bg { display: none; }
}
```

---

## Pattern D — Asymmetric Bento Hero

Best for: feature-rich products, design tools, analytics platforms.

```html
<section class="hero-bento">
  <div class="container">
    <div class="hero-bento__grid">
      <!-- Main headline cell -->
      <div class="hero-bento__cell hero-bento__cell--headline">
        <span class="eyebrow">Introducing v3</span>
        <h1>Analytics that actually explain why</h1>
        <a href="/trial" class="btn-primary">Start free trial</a>
      </div>

      <!-- Feature preview cell -->
      <div class="hero-bento__cell hero-bento__cell--preview">
        <img src="/chart-preview.webp" alt="Revenue attribution chart" width="480" height="320" fetchpriority="high" />
      </div>

      <!-- Stat cell -->
      <div class="hero-bento__cell hero-bento__cell--stat">
        <span class="stat-number">4.2×</span>
        <span class="stat-label">faster time to insight</span>
      </div>

      <!-- Social proof cell -->
      <div class="hero-bento__cell hero-bento__cell--proof">
        <p>"Replaced 3 tools. Pays for itself in week one."</p>
        <cite>Maria Chen, Head of Growth, Acme</cite>
      </div>
    </div>
  </div>
</section>
```

```css
.hero-bento__grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
  gap: var(--space-4);
}

.hero-bento__cell {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  padding: var(--space-8);
}

.hero-bento__cell--headline {
  grid-column: span 7;
  grid-row: span 2;
  background: var(--color-base);
}

.hero-bento__cell--preview {
  grid-column: span 5;
  grid-row: span 2;
  overflow: hidden;
  padding: 0;
}

.hero-bento__cell--stat    { grid-column: span 4; }
.hero-bento__cell--proof   { grid-column: span 8; }

@media (max-width: 768px) {
  .hero-bento__grid [class^="hero-bento__cell"] {
    grid-column: span 12;
  }
}
```

---

## Eyebrow Tag (required on all hero patterns)

```css
.eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 0.375rem;
  padding: 0.25rem 0.875rem;
  border-radius: 9999px;
  font-size: 0.6875rem;
  font-weight: 500;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  border: 1px solid currentColor;
  opacity: 0.65;
  margin-bottom: var(--space-4);
}
```

---

## Anti-Patterns

- Centered layout with H1 + subtitle + two equal CTA buttons (the default — banned)
- Hero without a visual element (headline + button alone = conversion dead zone)
- Stock photography of people smiling at laptops or handshaking
- CSS/SVG abstract "data flow" animations as the primary hero visual
- `min-height: 100vh` — use `100dvh` (iOS Safari bug)
- Two CTAs of equal visual weight ("Get Started" + "Learn More" both filled)
- Headline exceeding 3 lines at 390px viewport

## Related Files

- `rules/14-landing-pages.md` — R8: Hero layout rules
- `blueprints/landing-page-from-scratch.md` — Section 1: Hero
- `patterns/marketing-blocks/cta-sections.md` — CTA design patterns
- `references/motion-systems.md` — scroll entrance animations
