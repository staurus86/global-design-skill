# Rule 02 — Layout and Grid

> Grid gives structure. Breaking the grid creates emphasis. Both are intentional. Neither is optional.

---

## Grid Fundamentals

### The default grid

```css
.container {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: clamp(1rem, 2vw, 1.5rem);
  max-width: 1280px;
  margin-inline: auto;
  padding-inline: clamp(1rem, 4vw, 2rem);
}
```

**12 columns** because it divides cleanly into 1, 2, 3, 4, 6 column layouts.

**Gap:** fluid between `1rem` and `1.5rem` — not a fixed value.

**Max-width:** `1280px` for marketing. `1440px` for dashboards with dense data. Never unconstrained.

---

## Rules

### R1 — Mobile-first, always

Base styles target `390px`. Expand with `min-width` queries. Never shrink from desktop.

```css
/* Correct */
.grid { grid-template-columns: 1fr; }
@media (min-width: 768px) { .grid { grid-template-columns: repeat(2, 1fr); } }
@media (min-width: 1280px) { .grid { grid-template-columns: repeat(3, 1fr); } }

/* Banned */
.grid { grid-template-columns: repeat(3, 1fr); }
@media (max-width: 768px) { .grid { grid-template-columns: 1fr; } }
```

---

### R2 — Break the grid intentionally

At least one section per page must deviate from the column grid. Pure symmetry is monotony.

**Methods:**
- Overlap elements across grid boundaries with negative margins
- Extend a section element to full bleed while keeping content constrained
- Offset a cell: `margin-top: -3rem` to break the horizontal rhythm
- Rotate an element 1–3deg for editorial tension
- Let one image bleed beyond the container

**Rule:** Grid breaks are compositional decisions, not accidents. Every deviation is intentional and has a reason.

---

### R3 — Never nest cards inside cards

Nested containers create visual noise and false hierarchy. Cards are a leaf-level pattern.

**Banned:**
```html
<div class="card">
  <div class="card"> <!-- Never -->
    content
  </div>
</div>
```

**Fix:** If you need inner grouping within a card, use whitespace and dividers — not nested card components.

---

### R4 — Section padding minimum

Section padding below `6rem` creates compressed layouts that remove breathing room from content.

```css
/* Minimum */
.section { padding-block: 6rem; }

/* Preferred for marketing */
.section { padding-block: clamp(5rem, 10vw, 10rem); }

/* For dense admin UI */
.section { padding-block: 2rem; }
```

**Exception:** Admin panels, dashboards, and data-heavy interfaces — use `2-4rem` padding. Density is a feature there.

---

### R5 — Bento grid for asymmetric layouts

When equal columns create monotony, use bento grids with varied cell sizes.

```css
.bento {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: clamp(0.75rem, 1.5vw, 1.25rem);
  grid-auto-flow: dense; /* packs cells to fill gaps */
}

.cell-hero   { grid-column: span 8; grid-row: span 2; }
.cell-stat   { grid-column: span 4; }
.cell-wide   { grid-column: span 12; }
.cell-third  { grid-column: span 4; }
.cell-half   { grid-column: span 6; }

@media (max-width: 768px) {
  [class^="cell-"] { grid-column: span 12; }
}
```

**Arithmetic rule:** Verify that spans sum to multiples of 12 per visual row. Mismatched spans create unintended whitespace.

---

### R6 — Sidebar layouts

Sidebar + content is the standard SaaS app shell. Define widths as CSS custom properties.

```css
.layout-sidebar {
  display: grid;
  grid-template-columns: var(--sidebar-width, 240px) 1fr;
  min-height: 100dvh;
}

/* Collapsed state */
.layout-sidebar.collapsed {
  grid-template-columns: var(--sidebar-width-collapsed, 64px) 1fr;
}

/* Mobile: sidebar becomes drawer, content is full width */
@media (max-width: 768px) {
  .layout-sidebar { grid-template-columns: 1fr; }
  .sidebar { position: fixed; inset: 0; z-index: var(--z-drawer); }
}
```

---

### R7 — Editorial split layout

For alternating content sections (text left, image right — then flip):

```css
.split {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: clamp(2rem, 4vw, 5rem);
  align-items: center;
}

.split.flip { direction: rtl; } /* reverses column order */
.split.flip > * { direction: ltr; } /* restores text direction inside */

@media (max-width: 768px) {
  .split { grid-template-columns: 1fr; }
  .split.flip { direction: ltr; }
}
```

**Rhythm rule:** If using alternating splits, vary the content proportion — not always 50/50. Try 40/60, then 60/40. Identical proportions throughout = monotony.

---

### R8 — Z-axis is intentional depth

Overlapping elements creates depth. Unintentional overlap is a bug. Intentional overlap is a design decision.

**z-index naming system (define once, use everywhere):**
```css
:root {
  --z-below:    -1;   /* background elements */
  --z-base:      0;   /* normal document flow */
  --z-raised:   10;   /* cards, slight elevation */
  --z-dropdown: 100;  /* dropdowns, tooltips */
  --z-sticky:   200;  /* sticky headers */
  --z-drawer:   300;  /* mobile drawers */
  --z-modal:    400;  /* modal overlays */
  --z-toast:    500;  /* notifications */
  --z-cursor:  1000;  /* custom cursor */
}
```

**Banned:** Raw z-index values in components (`z-index: 9999`). Every z-index is a named layer.

---

### R9 — Container queries over breakpoints for components

Components define their own layout based on available space, not viewport width.

```css
.card-container { container-type: inline-size; }

.card { /* base: narrow container */ }

@container (min-width: 400px) {
  .card {
    display: grid;
    grid-template-columns: 120px 1fr;
  }
}
```

**When to use container queries:** reusable components that appear in sidebars, modals, and main content at different widths.

**When to use viewport breakpoints:** page-level layout changes (sidebar collapses, nav reflows, section reflows).

---

### R10 — Full-bleed vs. contained sections

Content is always contained. Backgrounds can be full-bleed.

```html
<!-- Correct: background is full-bleed, content is contained -->
<section class="section-bleed">
  <div class="container">
    content here
  </div>
</section>
```

```css
.section-bleed {
  background: var(--color-surface);
  /* no max-width here — this is full bleed */
}
.container {
  max-width: 1280px;
  margin-inline: auto;
  padding-inline: clamp(1rem, 4vw, 2rem);
}
```

**Banned:** Content lines wider than 75-80 characters. Add `max-width: 65ch` to body text columns.

---

### R11 — Sticky elements need safe areas

Fixed and sticky elements on mobile must account for iOS safe areas (notch, home indicator).

```css
.header-sticky {
  position: sticky;
  top: 0;
  padding-top: env(safe-area-inset-top);
}

.footer-fixed {
  position: fixed;
  bottom: 0;
  padding-bottom: env(safe-area-inset-bottom);
}
```

---

### R12 — Images don't cause layout shift

All images must have explicit dimensions to prevent Cumulative Layout Shift (CLS).

```html
<img
  src="hero.webp"
  width="1280"
  height="720"
  alt="Product dashboard overview"
  fetchpriority="high"
/>
```

For fluid images:
```css
img { width: 100%; height: auto; aspect-ratio: attr(width) / attr(height); }
```

For media containers before image loads:
```css
.media-container { aspect-ratio: 16 / 9; background: var(--color-surface); }
```

---

## Layout Audit Checklist

```
[ ] Mobile-first: base at 390px, expand with min-width
[ ] At least one section breaks the grid (intentionally)
[ ] No nested cards
[ ] Section padding minimum 6rem (or 2rem for dense admin)
[ ] Bento cells sum to multiples of 12 per row
[ ] All z-index values use named CSS custom properties
[ ] Images have explicit width + height attributes
[ ] Safe area insets on fixed/sticky elements
[ ] Body text columns max-width: 65ch
[ ] No content wider than its container
```

## Related Files

- `rules/01-visual-hierarchy.md` — visual rank within layouts
- `rules/05-spacing-and-density.md` — spacing tokens, gap scales
- `rules/07-responsive-design.md` → `references/responsive.md` — breakpoints, container queries
- `references/tokens.md` — spacing token system
- `patterns/navigation/` — header and sidebar layout patterns
