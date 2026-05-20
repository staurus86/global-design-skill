# Pattern — Bento Grid

> A bento grid is an asymmetric card layout where cards have varying column and row spans, creating visual hierarchy through size. It replaces the "identical card grid" banned pattern. Named after Japanese bento boxes.

---

## When to Use

- Feature sections where some features deserve more visual weight
- "How it works" sequences with a lead feature
- Dashboard-style landing pages (Raycast, Linear, Vercel aesthetic)
- When you have 4–8 features and want to avoid the 3-equal-column grid

## When NOT to Use

- Lists of equal-weight items (testimonials, team members, logos) — use a uniform grid
- More than 12 items — bento loses meaning at scale
- Mobile-only designs where all cards stack to full-width anyway

---

## The 12-Column Bento System

All cards live on a 12-column grid with auto rows. Card spans create the visual hierarchy.

### Span patterns (6 features)

```
Layout A — Hero left:
┌─────────────────┬────────┬────────┐
│                 │        │        │
│   HERO (8col)   │  sm    │  sm    │
│                 │ (4col) │ (4col) │
├────────┬────────┴────────┴────────┤
│  med   │        wide (8col)       │
│ (4col) │                          │
└────────┴──────────────────────────┘

Layout B — Hero top:
┌──────────────────────────────────┐
│          HERO (12col)            │
├──────────┬──────────┬────────────┤
│ md(4col) │ md(4col) │  md(4col)  │
└──────────┴──────────┴────────────┘

Layout C — Split:
┌────────────┬──────┬──────┐
│ tall(4col) │ sm   │ sm   │
│ 2 rows     │(4col)│(4col)│
│            ├──────┴──────┤
│            │  wide(8col) │
└────────────┴─────────────┘
```

---

## Implementation

### CSS Grid (no library)

```css
.bento {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-auto-rows: 80px;
  gap: var(--space-4);
}

/* Responsive: stack to 2-col on tablet, 1-col on mobile */
@media (max-width: 768px) {
  .bento {
    grid-template-columns: repeat(2, 1fr);
    grid-auto-rows: auto;
  }
}

@media (max-width: 480px) {
  .bento {
    grid-template-columns: 1fr;
  }
}

/* Card span presets */
.bento-hero   { grid-column: span 8; grid-row: span 5; }
.bento-tall   { grid-column: span 4; grid-row: span 5; }
.bento-wide   { grid-column: span 8; grid-row: span 3; }
.bento-full   { grid-column: span 12; grid-row: span 3; }
.bento-medium { grid-column: span 6; grid-row: span 4; }
.bento-small  { grid-column: span 4; grid-row: span 3; }
.bento-slim   { grid-column: span 4; grid-row: span 2; }

/* Mobile override — all cards full-width */
@media (max-width: 768px) {
  .bento-hero,
  .bento-tall,
  .bento-wide,
  .bento-full,
  .bento-medium,
  .bento-small,
  .bento-slim {
    grid-column: 1 / -1;
    grid-row: span 1;
    min-height: 200px;
  }
}
```

### Tailwind v4 (utility classes)

```html
<div class="grid grid-cols-12 auto-rows-[80px] gap-4">
  <!-- Hero card — 8 columns, 5 rows -->
  <div class="col-span-8 row-span-5 bg-surface rounded-2xl p-8">
    <span class="eyebrow">Core feature</span>
    <h3>The thing that matters most</h3>
    <!-- Rich visual: screenshot, diagram, animation -->
    <img src="/feature-hero.webp" alt="..." class="mt-6 w-full rounded-xl" />
  </div>

  <!-- Small top-right — 4 columns, 2 rows -->
  <div class="col-span-4 row-span-2 bg-surface rounded-2xl p-6">
    <h3>Quick insight</h3>
    <p class="text-muted">Short supporting point</p>
  </div>

  <!-- Small bottom-right — 4 columns, 3 rows -->
  <div class="col-span-4 row-span-3 bg-surface-2 rounded-2xl p-6">
    <div class="stat-display">
      <span class="text-5xl font-bold">4×</span>
      <span class="text-muted">faster deployment</span>
    </div>
  </div>

  <!-- Wide bottom — 8 columns, 3 rows -->
  <div class="col-span-8 row-span-3 bg-surface rounded-2xl p-8">
    <h3>Supporting feature</h3>
    <p>Longer description here — this card has room for it</p>
  </div>

  <!-- Slim full-width — accent highlight -->
  <div class="col-span-12 row-span-2 bg-accent-bg border border-accent/20 rounded-2xl p-6 flex items-center justify-between">
    <p class="font-medium">Used by 2,847 engineering teams worldwide</p>
    <a href="/customers" class="btn-ghost">See case studies →</a>
  </div>
</div>
```

---

## Card Content by Size

Match content to card size. Mismatched content breaks the hierarchy.

| Card size | Content type | Visual element |
|---|---|---|
| Hero (8col × 5row) | Primary feature, longest copy | Product screenshot, diagram, animation |
| Medium (6col × 4row) | Secondary feature | Icon + chart, short demo |
| Wide (8col × 3row) | Supporting claim | Testimonial, metrics bar, code snippet |
| Small (4col × 3row) | Stat, quick benefit | Large number + label, single icon |
| Slim (4col × 2row) | Label, tag, simple claim | Icon + one line |
| Full (12col × 2row) | Social proof bar, CTA accent | Logo strip, trust signal |

---

## Card Anatomy

Each bento card is a surface — not a nested card. Use only one level of depth.

```html
<div class="bento-card bento-hero">
  <!-- Optional: eyebrow tag -->
  <span class="eyebrow">Most-used feature</span>

  <!-- Heading — size matches card span -->
  <h3 class="card-heading">Real-time collaboration</h3>

  <!-- Body — only in medium+ cards -->
  <p class="card-body text-muted">
    See changes from every teammate as they happen.
    No refresh. No merge conflicts.
  </p>

  <!-- Visual — the differentiator -->
  <div class="card-visual mt-auto">
    <img src="/collab-demo.webp" alt="..." width="600" height="360" loading="lazy" />
  </div>
</div>
```

```css
.bento-card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-2xl);
  padding: var(--space-8);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  position: relative;
  transition:
    transform  var(--duration-normal) var(--ease-spring),
    box-shadow var(--duration-normal) var(--ease-smooth);
}

.bento-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

/* Hero card gets more padding, larger heading */
.bento-hero .card-heading {
  font-size: var(--text-h2);
  font-family: var(--font-display);
}

/* Small cards: tighter padding, icon-first */
.bento-small {
  padding: var(--space-6);
}
```

---

## Visual Variety Between Cards

Bento grids feel dull when all cards have the same background. Vary surface treatment:

```css
/* Default — clean surface */
.bento-card { background: var(--color-surface); }

/* Accent tint — for featured/highlighted cards */
.bento-card.variant-accent {
  background: var(--color-accent-bg);
  border-color: oklch(from var(--color-accent) l c h / 0.2);
}

/* Dark invert — for contrast (dark mode: surface-2) */
.bento-card.variant-dark {
  background: var(--color-text);
  color: var(--color-base);
}

/* Transparent + border — ghost cards */
.bento-card.variant-ghost {
  background: transparent;
  border-style: dashed;
}

/* Surface-2 — subtle depth */
.bento-card.variant-raised {
  background: var(--color-surface-2);
  box-shadow: var(--shadow-sm);
}
```

---

## Scroll Reveal for Bento

```ts
const observer = new IntersectionObserver(
  entries => entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('is-visible')
      observer.unobserve(e.target)
    }
  }),
  { threshold: 0.1 }
)

document.querySelectorAll('.bento-card').forEach((card, i) => {
  ;(card as HTMLElement).style.transitionDelay = `${i * 60}ms`
  observer.observe(card)
})
```

```css
.bento-card {
  opacity: 0;
  transform: translateY(16px);
  transition:
    opacity   var(--duration-entrance) var(--ease-spring),
    transform var(--duration-entrance) var(--ease-spring);
}

.bento-card.is-visible {
  opacity: 1;
  transform: translateY(0);
}

@media (prefers-reduced-motion: reduce) {
  .bento-card {
    opacity: 1;
    transform: none;
    transition: none;
  }
}
```

---

## Checklist

```
[ ] No two adjacent cards have identical size (span combo)
[ ] Hero card is visually distinct: larger heading, richer visual
[ ] Total column spans per row = 12 (verify no gaps or overflows)
[ ] Cards do not have nested cards inside them
[ ] Mobile: all cards stack to 1-column with auto height
[ ] Card content matches card size — hero has rich visual, slim has one stat
[ ] At least one card breaks the surface pattern (accent, dark, or ghost variant)
[ ] Hover state: subtle lift + shadow on each card
[ ] No raw px gap values — uses var(--space-4) or var(--space-6)
[ ] Images inside cards have width + height attributes set
```

---

*Pattern version: global-design-skill v1.0 — `patterns/marketing-blocks/bento-grid.md`*
*Related: `rules/02-layout-and-grid.md`, `checklists/global-design-review.md` §4.10, `patterns/marketing-blocks/feature-sections.md`*
