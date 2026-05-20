# Pattern — Stats Sections

> Stats sections prove claims with numbers. They only work when the numbers are real, sourced, and specific. A generic "50% faster" with no context is decoration, not evidence — and undermines trust.

---

## The Evidence Test

Before designing the section, run every number through this test:

```
1. Is this number real? (not estimated, not rounded to "nice" values)
2. Can we cite the source? (internal data, third-party study, user survey)
3. Is the timeframe relevant? (not a record from 5 years ago)
4. Does the number answer a user concern? (speed, reliability, scale, cost)
5. Will this number still be true in 3 months? (avoid numbers that drift)
```

Fail any test: remove the stat. Use a testimonial or case study instead.

---

## Pattern 1 — Horizontal Stats Bar

Four key metrics in a horizontal strip. Works as a trust band between hero and features.

```html
<section class="stats-bar" aria-label="Product metrics">
  <div class="container">
    <dl class="stats-bar__list">

      <div class="stats-bar__item">
        <dt class="stats-bar__label">Deployments per day</dt>
        <dd class="stats-bar__value">
          <span class="stats-bar__number">2.4M</span>
        </dd>
      </div>

      <div class="stats-bar__item" aria-hidden="true">
        <span class="stats-bar__sep"></span>
      </div>

      <div class="stats-bar__item">
        <dt class="stats-bar__label">Uptime SLA</dt>
        <dd class="stats-bar__value">
          <span class="stats-bar__number">99.99%</span>
        </dd>
      </div>

      <div class="stats-bar__item" aria-hidden="true">
        <span class="stats-bar__sep"></span>
      </div>

      <div class="stats-bar__item">
        <dt class="stats-bar__label">Average deploy time</dt>
        <dd class="stats-bar__value">
          <span class="stats-bar__number">23</span>
          <span class="stats-bar__unit">sec</span>
        </dd>
      </div>

      <div class="stats-bar__item" aria-hidden="true">
        <span class="stats-bar__sep"></span>
      </div>

      <div class="stats-bar__item">
        <dt class="stats-bar__label">Teams using global edge</dt>
        <dd class="stats-bar__value">
          <span class="stats-bar__number">18K</span>
          <span class="stats-bar__unit">+</span>
        </dd>
      </div>

    </dl>
  </div>
</section>
```

```css
.stats-bar {
  padding-block: var(--space-12);
  border-block: 1px solid var(--color-border);
  background: var(--color-surface-2);
}

.stats-bar__list {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0;
  flex-wrap: wrap;
  margin: 0; padding: 0;
}

.stats-bar__item {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: var(--space-4) var(--space-10);
}

.stats-bar__sep {
  display: block;
  width: 1px;
  height: 48px;
  background: var(--color-border);
}

.stats-bar__value {
  display: flex;
  align-items: baseline;
  gap: var(--space-1);
  margin-bottom: var(--space-2);
}

.stats-bar__number {
  font-size: var(--text-display);
  font-family: var(--font-display);
  font-weight: 700;
  letter-spacing: -0.03em;
  color: var(--color-text-primary);
  line-height: 1;
}

.stats-bar__unit {
  font-size: var(--text-h3);
  font-family: var(--font-display);
  font-weight: 600;
  color: var(--color-accent);
  line-height: 1;
}

.stats-bar__label {
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
  max-width: 16ch;
  line-height: 1.4;
}

@media (max-width: 768px) {
  .stats-bar__list {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: var(--space-1);
  }
  .stats-bar__sep { display: none; }
  .stats-bar__item { padding: var(--space-6) var(--space-4); }
}
```

---

## Pattern 2 — Stats with Context

Numbers alone don't persuade. Pair each stat with a one-line source or context string.

```html
<section class="stats-context" aria-label="Impact metrics">
  <div class="container stats-context__container">

    <div class="stats-context__intro">
      <span class="eyebrow">Measured impact</span>
      <h2 class="stats-context__heading">Built for teams that ship daily</h2>
      <p class="stats-context__body">
        Numbers from our infrastructure, measured across production deployments in Q1 2025.
      </p>
    </div>

    <dl class="stats-context__grid">

      <div class="stats-context__item">
        <dd class="stats-context__value">
          <span class="stats-context__number">3.2x</span>
        </dd>
        <dt class="stats-context__label">Faster deploy cycle</dt>
        <p class="stats-context__source">vs. self-hosted CI, median across 2,000 teams</p>
      </div>

      <div class="stats-context__item">
        <dd class="stats-context__value">
          <span class="stats-context__number">$14K</span>
        </dd>
        <dt class="stats-context__label">Saved per year in infra</dt>
        <p class="stats-context__source">median savings, Pro plan customers, 2024 survey</p>
      </div>

      <div class="stats-context__item">
        <dd class="stats-context__value">
          <span class="stats-context__number">8 min</span>
        </dd>
        <dt class="stats-context__label">Time to first deployment</dt>
        <p class="stats-context__source">median new user, measured product telemetry</p>
      </div>

      <div class="stats-context__item">
        <dd class="stats-context__value">
          <span class="stats-context__number">99.97%</span>
        </dd>
        <dt class="stats-context__label">Platform uptime</dt>
        <p class="stats-context__source">12-month rolling average, all regions</p>
      </div>

    </dl>
  </div>
</section>
```

```css
.stats-context { padding-block: var(--space-24); }

.stats-context__container {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: var(--space-16);
  align-items: start;
}

.stats-context__intro { position: sticky; top: var(--space-8); }

.stats-context__heading {
  font-size: var(--text-h2);
  font-family: var(--font-display);
  font-weight: 700;
  color: var(--color-text-primary);
  letter-spacing: -0.02em;
  line-height: 1.1;
  margin-block: var(--space-4);
}

.stats-context__body {
  font-size: var(--text-body);
  color: var(--color-text-secondary);
  line-height: 1.65;
  max-width: 36ch;
}

.stats-context__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-1);
  margin: 0; padding: 0;
}

.stats-context__item {
  padding: var(--space-8);
  background: var(--color-surface-2);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}

.stats-context__value { margin: 0; }

.stats-context__number {
  display: block;
  font-size: var(--text-display);
  font-family: var(--font-display);
  font-weight: 700;
  letter-spacing: -0.03em;
  color: var(--color-text-primary);
  line-height: 1;
}

.stats-context__label {
  font-size: var(--text-body);
  font-weight: var(--font-weight-semibold);
  color: var(--color-text-primary);
}

.stats-context__source {
  font-size: 12px;
  color: var(--color-text-muted);
  line-height: 1.5;
  margin: 0;
}

@media (max-width: 900px) {
  .stats-context__container { grid-template-columns: 1fr; gap: var(--space-10); }
  .stats-context__intro { position: static; }
}

@media (max-width: 600px) {
  .stats-context__grid { grid-template-columns: 1fr; }
}
```

---

## Pattern 3 — Animated Counter (with IntersectionObserver)

Numbers that count up when the section enters viewport. Use sparingly — once per page.

```js
function animateCounter (el, from, to, duration = 1200) {
  const start = performance.now()
  const isDecimal = String(to).includes('.')
  const decimals  = isDecimal ? String(to).split('.')[1].length : 0

  function update (now) {
    const elapsed  = now - start
    const progress = Math.min(elapsed / duration, 1)
    // Ease out cubic
    const eased    = 1 - Math.pow(1 - progress, 3)
    const current  = from + (to - from) * eased
    el.textContent = isDecimal
      ? current.toFixed(decimals)
      : Math.floor(current).toLocaleString()
    if (progress < 1) requestAnimationFrame(update)
  }

  requestAnimationFrame(update)
}

// Trigger on viewport entry
new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (!entry.isIntersecting) return
    const el = entry.target
    const to = parseFloat(el.dataset.to)
    const from = parseFloat(el.dataset.from || 0)
    animateCounter(el, from, to)
    observer.unobserve(el)
  })
}, { threshold: 0.5 }).observe(document.querySelectorAll('[data-counter]'))

// prefers-reduced-motion: show final value immediately
if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  document.querySelectorAll('[data-counter]').forEach(el => {
    el.textContent = el.dataset.to
  })
}
```

```html
<!-- Usage: data-to is the target number, data-from optional -->
<span class="stats-bar__number" data-counter data-to="2400000" data-from="0">2,400,000</span>
```

The element's initial text content is shown before JS runs (SSR-safe). The counter animates from `data-from` to `data-to` when the element enters the viewport.

---

## Anti-Patterns

```
× Round numbers with no source ("10,000+ customers", "50% faster")
× Stats that change quarterly but are hardcoded — will become stale
× More than 4–6 stats — diminishing returns; each extra number dilutes attention
× All stats about the same thing (all speed metrics, or all scale metrics)
× Animating every number simultaneously — animation loses meaning
× Counter animation on desktop but not mobile — inconsistent
× No unit labels — "2.4M what?" needs context
× Hero-metric template (big number + gradient + small label) — banned cliché
```

---

*Pattern version: global-design-skill v1.0 — `patterns/marketing-blocks/stats-sections.md`*  
*Related: `patterns/marketing-blocks/comparison-sections.md`, `patterns/marketing-blocks/feature-sections.md`, `agents/copy-editor.md`*
