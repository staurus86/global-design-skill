# Example 04 — Card Grid Cleanup

> **Rules applied:** SKILL.md §7 (layout banned patterns) · color R3, R4 · animation R1, R9 · typography R3, R4 · components (rules/06-components.md)

**Scenario:** A SaaS features section. The team built it in 2 hours following the first Google result for "features section." It has four of the most common design clichés in the industry. The redesign takes the same content and produces something that looks like a deliberate design decision.

---

## Before — The Cliché Grid

```html
<section class="features">
  <div class="container">
    <h2>Everything you need to ship faster</h2>
    <p>Our platform gives your team all the tools to build, deploy, and monitor with confidence.</p>

    <div class="features-grid">

      <div class="feature-card">
        <div class="icon-wrapper">
          <!-- Thick default Lucide icon -->
          <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#6366f1" stroke-width="2.5">
            <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/>
          </svg>
        </div>
        <h3>Lightning Fast</h3>
        <p>Deploy in seconds with our optimized pipeline. No more waiting around.</p>
      </div>

      <div class="feature-card">
        <div class="icon-wrapper">
          <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#6366f1" stroke-width="2.5">
            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
          </svg>
        </div>
        <h3>Enterprise Security</h3>
        <p>Bank-grade encryption keeps your data safe and your team compliant.</p>
      </div>

      <div class="feature-card">
        <div class="icon-wrapper">
          <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#6366f1" stroke-width="2.5">
            <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/>
            <path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>
          </svg>
        </div>
        <h3>Team Collaboration</h3>
        <p>Work together seamlessly with real-time collaboration tools for your whole team.</p>
      </div>

      <div class="feature-card">
        <div class="icon-wrapper">
          <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#6366f1" stroke-width="2.5">
            <line x1="18" y1="20" x2="18" y2="10"/>
            <line x1="12" y1="20" x2="12" y2="4"/>
            <line x1="6"  y1="20" x2="6"  y2="14"/>
          </svg>
        </div>
        <h3>Advanced Analytics</h3>
        <p>Get deep insights into your team's performance with powerful analytics and reporting.</p>
      </div>

    </div>
  </div>
</section>
```

```css
.features {
  padding: 60px 0;    /* below 80px minimum */
  background: #f9fafb;
}

.features h2 {
  font-size: 36px;    /* fixed px */
  text-align: center;
  color: #111827;
  margin-bottom: 16px;
}

.features > .container > p {
  text-align: center;
  color: #6b7280;
  font-size: 18px;
  margin-bottom: 48px;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);  /* always 4 equal columns */
  gap: 24px;
}

.feature-card {
  background: #ffffff;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  padding: 24px;
  text-align: center;   /* centered card content */
}

.icon-wrapper {
  width: 64px;
  height: 64px;
  background: rgba(99, 102, 241, 0.1);   /* hardcoded rgba */
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 16px;
}

.feature-card h3 {
  font-size: 18px;
  font-weight: 600;
  color: #111827;
  margin-bottom: 8px;
}

.feature-card p {
  font-size: 14px;    /* below 16px minimum */
  color: #6b7280;
  line-height: 1.5;
}
```

---

## Diagnosis — 11 Violations

| # | Violation | Rule |
|---|---|---|
| 1 | 4-equal-column icon feature grid (banned pattern) | SKILL.md §2 |
| 2 | Centered card content — all 4 cards identical layout | SKILL.md §7 |
| 3 | `padding: 60px` — below 80px minimum | SKILL.md §7 |
| 4 | `font-size: 36px` — fixed px on heading | typography R1 |
| 5 | `font-size: 14px` on card body text | typography R2 |
| 6 | `rgba(99,102,241,0.1)` — hardcoded opacity, not token | color R9 |
| 7 | Thick default Lucide stroke-width 2.5 (banned) | SKILL.md §2 |
| 8 | No entry animation — cards appear statically | animation R1 |
| 9 | No stagger between cards | animation R9 |
| 10 | Icon on every heading (iconography slop) | SKILL.md §2 |
| 11 | "Seamlessly" in copy | SKILL.md §2 |

**Core problem:** This section announces "I followed a tutorial." The 4-equal-column icon grid with centered content is the single most recognizable SaaS cliché. It signals a product where no designer was involved.

---

## After — Asymmetric Feature Layout

```html
<section class="features">
  <div class="features__inner">

    <!-- Section header: left-aligned, not centered -->
    <div class="features__header">
      <span class="eyebrow">Built for engineering teams</span>
      <h2 class="features__title">One platform. No more context switching.</h2>
    </div>

    <!-- Asymmetric bento: one large card + three small -->
    <div class="features__grid" role="list">

      <!-- Hero feature card: spans 2 rows -->
      <article class="feature-card feature-card--hero" role="listitem" data-reveal>
        <div class="feature-card__content">
          <h3 class="feature-card__title">Deploy in 30 seconds, roll back in 10</h3>
          <p class="feature-card__desc">
            Push to your branch. Pipeline detects the change, runs your test suite,
            and deploys to staging automatically. One click to production. One click back.
          </p>
          <a href="/deploy" class="feature-card__link">
            See how it works
            <svg aria-hidden="true" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </a>
        </div>
        <!-- Actual product screenshot as visual — not an icon -->
        <div class="feature-card__visual">
          <img
            src="/features/deploy-flow.webp"
            alt="Deploy pipeline showing 3 stages: test (32s), build (18s), deploy (11s), with a green success indicator"
            width="600"
            height="400"
            loading="lazy"
            class="feature-card__screenshot"
          />
        </div>
      </article>

      <!-- Supporting features: left-aligned, no icon -->
      <article class="feature-card feature-card--sm" role="listitem" data-reveal>
        <p class="feature-card__stat">99.97%</p>
        <h3 class="feature-card__title">Uptime SLA</h3>
        <p class="feature-card__desc">
          Multi-region deployments with automatic failover.
          Your users don't notice when a server goes down.
        </p>
      </article>

      <article class="feature-card feature-card--sm" role="listitem" data-reveal>
        <p class="feature-card__stat">SOC 2</p>
        <h3 class="feature-card__title">Type II certified</h3>
        <p class="feature-card__desc">
          Annual third-party audits. SSO, audit logs, role-based access.
          Passes most enterprise procurement reviews on first submission.
        </p>
      </article>

      <article class="feature-card feature-card--sm" role="listitem" data-reveal>
        <p class="feature-card__stat">40+</p>
        <h3 class="feature-card__title">Integrations</h3>
        <p class="feature-card__desc">
          GitHub, GitLab, Bitbucket, Slack, PagerDuty, Datadog.
          Webhooks for everything else.
        </p>
      </article>

    </div>
  </div>
</section>
```

```css
/* ── Section ── */
.features {
  padding-block: var(--space-24);        /* 96px — above minimum */
  background: var(--color-base);
}

.features__inner {
  max-width: var(--container-xl);
  margin-inline: auto;
  padding-inline: var(--space-8);
  display: flex;
  flex-direction: column;
  gap: var(--space-12);
}

/* ── Header: left-aligned ── */
.features__header {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: var(--space-4);
  max-width: 640px;
}

.features__title {
  font-family: var(--font-display);
  font-size: var(--text-h2);             /* clamp(1.75rem, 3vw + 0.5rem, 4rem) */
  font-weight: 700;
  line-height: var(--line-height-tight); /* 1.1 */
  letter-spacing: var(--tracking-snug);  /* -0.02em */
  color: var(--color-text-primary);
}

/* ── Asymmetric bento grid ── */
.features__grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto auto;
  gap: var(--space-5);
}

/* Hero card: 8 columns, 2 rows */
.feature-card--hero {
  grid-column: 1 / span 8;
  grid-row: 1 / span 2;
}

/* Three small cards: 4 columns each, stacked */
.feature-card--sm:nth-child(2) { grid-column: 9 / span 4; grid-row: 1; }
.feature-card--sm:nth-child(3) { grid-column: 9 / span 4; grid-row: 2; }
.feature-card--sm:nth-child(4) {
  grid-column: 1 / span 12;    /* full width below at some breakpoints */
  grid-row: 3;
  display: none;                /* hide 4th on large viewport — show on mobile */
}

@media (max-width: 1024px) {
  .features__grid { grid-template-columns: 1fr; }
  .feature-card--hero,
  .feature-card--sm:nth-child(2),
  .feature-card--sm:nth-child(3),
  .feature-card--sm:nth-child(4) {
    grid-column: 1 / -1;
    grid-row: auto;
    display: block;
  }
}

/* ── Cards ── */
.feature-card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  overflow: hidden;
}

/* Hero card: split layout */
.feature-card--hero {
  display: grid;
  grid-template-columns: 1fr 1fr;
  align-items: center;
}

.feature-card--hero .feature-card__content {
  padding: var(--space-10);
}

.feature-card--hero .feature-card__visual {
  height: 100%;
  overflow: hidden;
  border-left: 1px solid var(--color-border);
}

.feature-card__screenshot {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: left top;
}

/* Small cards: left-aligned, stat-led */
.feature-card--sm {
  padding: var(--space-8);
}

/* ── Card content ── */
.feature-card__stat {
  font-family: var(--font-display);
  font-size: var(--text-display);
  font-weight: 700;
  line-height: 1;
  color: var(--color-accent);
  letter-spacing: var(--tracking-tighter);
  margin-bottom: var(--space-3);
}

.feature-card__title {
  font-size: var(--text-h3);
  font-weight: var(--font-weight-semibold);
  line-height: var(--line-height-snug);
  color: var(--color-text-primary);
  margin-bottom: var(--space-3);
}

.feature-card__desc {
  font-size: var(--text-body);            /* 1rem */
  line-height: var(--line-height-relaxed);
  color: var(--color-text-secondary);
}

.feature-card__link {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  margin-top: var(--space-5);
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-accent);
  text-decoration: none;
  transition: gap var(--duration-fast) var(--ease-smooth);
}

.feature-card__link:hover { gap: var(--space-3); }

/* ── Entry animation with stagger ── */
[data-reveal] {
  opacity: 0;
  transform: translateY(20px);
  transition:
    opacity   var(--duration-slow)  var(--ease-spring),
    transform var(--duration-slow)  var(--ease-spring);
}

[data-reveal].visible {
  opacity: 1;
  transform: none;
}

/* Stagger: hero 0ms, small cards 100/200/300ms */
.feature-card--hero       { transition-delay: 0ms;   }
.feature-card--sm:nth-child(2) { transition-delay: 100ms; }
.feature-card--sm:nth-child(3) { transition-delay: 200ms; }
.feature-card--sm:nth-child(4) { transition-delay: 300ms; }

@media (prefers-reduced-motion: reduce) {
  [data-reveal] {
    opacity: 1;
    transform: none;
    transition: none;
  }
}
```

```js
// Scroll-triggered reveal via IntersectionObserver
const observer = new IntersectionObserver(
  entries => entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('visible')
      observer.unobserve(e.target)    // animate once
    }
  }),
  { threshold: 0.1 }
)

document.querySelectorAll('[data-reveal]').forEach(el => observer.observe(el))
```

---

## What Changed and Why

**4-equal-column icon grid → asymmetric bento**
The asymmetric layout immediately signals intentionality. One dominant card (hero feature) and three supporting cards creates visual hierarchy. The grid columns (8 + 4) are not equal — the difference in size communicates importance.

**Centered card content → left-aligned**
Left alignment matches the natural reading direction and creates a consistent left edge. Centering card content looks amateurish in dense grids — it's a pattern borrowed from isolated call-to-action blocks, not information grids.

**Icons on every heading → stat-led cards + product screenshot**
Icons on SaaS feature cards convey nothing — every tool has a "fast" icon, a "secure" icon, a "team" icon. Numbers convey specifics: "99.97% uptime" is a concrete claim. The hero card uses a real product screenshot, not a CSS illustration.

**`padding: 60px` → `var(--space-24)` (96px)**
Sections need breathing room. Tight padding makes the page feel cramped and information-dense without being genuinely information-dense.

**"Seamlessly" → removed**
Banned. Replaced with specific copy that names what the product actually does ("Push to your branch. Pipeline detects the change...").

**No animation → staggered `IntersectionObserver` reveals**
Cards enter with a 20px translateY as they scroll into view. The hero card leads at 0ms, supporting cards follow at 100ms intervals. `IntersectionObserver` replaces `window.addEventListener('scroll')` — no main-thread reflow on every scroll position.

---

*Example 04 — `examples/04-card-grid-cleanup.md`*
*Related: `SKILL.md` §7 banned patterns, `rules/05-animation.md`, `rules/03-typography.md`, `patterns/marketing-blocks/feature-sections.md`*
