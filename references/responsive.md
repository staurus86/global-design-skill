# Reference — Responsive Design

> Mobile-first breakpoints, container queries, fluid sizing, safe areas, and responsive patterns for every layout type. Always min-width. Test at 390px → 768px → 1280px → 1440px.

---

## Core Rules

**Mobile-first:** Base styles target 390px (iPhone 15). Expand with `min-width` queries. Never `max-width` queries.

```css
/* Wrong — desktop-first */
.grid { display: grid; grid-template-columns: repeat(3, 1fr); }
@media (max-width: 768px) { .grid { grid-template-columns: 1fr; } }

/* Correct — mobile-first */
.grid { display: grid; grid-template-columns: 1fr; }
@media (min-width: 768px)  { .grid { grid-template-columns: repeat(2, 1fr); } }
@media (min-width: 1280px) { .grid { grid-template-columns: repeat(3, 1fr); } }
```

---

## Breakpoint System

```css
/* Mobile-first breakpoints */
/* base:   0px–639px    — mobile portrait */
/* sm:     640px+       — large phone landscape, small tablet */
/* md:     768px+       — tablet portrait */
/* lg:     1024px+      — tablet landscape, small laptop */
/* xl:     1280px+      — desktop */
/* 2xl:    1440px+      — wide desktop */
/* 3xl:    1920px+      — ultra-wide */
```

### Tailwind v4 breakpoints

```css
@theme {
  --breakpoint-sm:  640px;
  --breakpoint-md:  768px;
  --breakpoint-lg:  1024px;
  --breakpoint-xl:  1280px;
  --breakpoint-2xl: 1440px;
  --breakpoint-3xl: 1920px;
}
```

---

## Viewport Height — Always `dvh`

```css
/* Wrong — iOS Safari bug: 100vh includes hidden browser chrome */
.hero { min-height: 100vh; }

/* Correct — Dynamic Viewport Height adjusts for mobile browser chrome */
.hero      { min-height: 100dvh; }
.sidebar   { height: 100dvh; }
.full-page { min-height: 100dvh; }

/* Small viewport for fixed/sticky bottom elements */
.sticky-footer { height: 100svh; }
```

---

## Safe Areas (iOS Notch + Home Bar)

Apply `env(safe-area-inset-*)` to all fixed or sticky elements near screen edges.

```css
/* Fixed navigation */
.nav-fixed {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  padding-top: env(safe-area-inset-top);
}

/* Bottom tab bar */
.tab-bar {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  padding-bottom: env(safe-area-inset-bottom);
}

/* Full-screen sections */
.hero-section {
  padding-top: calc(env(safe-area-inset-top) + var(--space-16));
  padding-bottom: env(safe-area-inset-bottom);
}

/* Sidebar drawer */
.sidebar {
  padding-left: env(safe-area-inset-left);
  padding-right: env(safe-area-inset-right);
}
```

---

## Touch Targets

All interactive elements must be ≥ 44×44px on mobile — even if the visible element is smaller.

```css
/* Expand touch area without changing visual size */
.icon-btn {
  width: 24px;
  height: 24px;
  position: relative;
}

/* Invisible tap target extension */
.icon-btn::after {
  content: '';
  position: absolute;
  inset: -10px;    /* extends hit area to 44×44px total */
}

/* Or use padding + negative margin */
.icon-btn-alt {
  padding: 10px;
  margin: -10px;
}

/* Minimum height for buttons and links in lists */
.list-item-link {
  min-height: 44px;
  display: flex;
  align-items: center;
}
```

---

## Hover-Only Interactions

Desktop hover states must not fire on touch devices.

```css
/* Wrong — fires on tap on mobile (sticky hover state) */
.card:hover { transform: translateY(-2px); }

/* Correct — only on pointer devices (mouse, stylus) */
@media (hover: hover) {
  .card:hover { transform: translateY(-2px); }
}

/* Combined with pointer type */
@media (hover: hover) and (pointer: fine) {
  .tooltip-trigger:hover .tooltip { display: block; }
}
```

---

## Fluid Section Spacing

Section padding varies with viewport to maintain comfortable rhythm.

```css
/* Hero — most generous */
.section-hero     { padding-block: clamp(6rem, 14vw, 16rem) clamp(4rem, 10vw, 12rem); }

/* Standard section */
.section-standard { padding-block: clamp(4rem, 10vw, 12rem); }

/* Tight sections (stats bars, logo strips) */
.section-tight    { padding-block: clamp(2rem, 4vw, 3rem); }

/* Final CTA — most expansive */
.section-exit     { padding-block: clamp(8rem, 16vw, 20rem); }
```

---

## Container Max-Width

Content must not be full-bleed at all viewport widths. Set a max-width and center.

```css
.container {
  width: 100%;
  max-width: 1280px;
  margin-inline: auto;
  padding-inline: clamp(var(--space-5), 5vw, var(--space-16));
}

/* Variants */
.container-narrow { max-width: 800px; }   /* articles, blog posts */
.container-wide   { max-width: 1440px; }  /* marketing, dashboards */
.container-full   { max-width: none; }    /* only for full-bleed sections */
```

---

## Container Queries

For components that adapt based on their container's width, not the viewport.

### When to use container queries vs media queries

| Situation | Use |
|---|---|
| Layout changes based on viewport (sections, page) | Media query |
| Component adapts to its parent's size (card, sidebar widget) | Container query |
| Dashboard card in multiple grid sizes | Container query |
| Sidebar-aware component | Container query |

```css
/* Define the containment context on the wrapper */
.card-wrapper {
  container-type: inline-size;
  container-name: feature-card;
}

/* Default (narrow) layout */
.feature-card {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
}

/* When card is wide enough — switch to horizontal */
@container feature-card (min-width: 380px) {
  .feature-card {
    flex-direction: row;
    align-items: center;
  }
}

/* Larger card — increase heading size */
@container feature-card (min-width: 500px) {
  .feature-card-heading {
    font-size: var(--text-h3);
  }
}
```

### Sidebar-aware main content

```css
.app-layout {
  container-type: inline-size;
}

/* When main content area is narrow (sidebar is open) */
@container (max-width: 900px) {
  .data-grid { grid-template-columns: 1fr; }
}

@container (min-width: 900px) {
  .data-grid { grid-template-columns: repeat(3, 1fr); }
}
```

---

## Responsive Typography Rules

```css
/* Never fixed px for display sizes */
h1 { font-size: var(--text-h1); }   /* clamp-based token */

/* Body: always ≥ 16px at all viewports */
body { font-size: 1rem; }           /* = 16px */

/* Paragraph max-width — always constrain */
p { max-width: 72ch; }

/* Text zoom — must work at 200% browser zoom */
/* Test: Chrome → ⋮ → Zoom → 200% → no overflow, no cut-off */
```

---

## Image Responsiveness

```html
<!-- Always set width + height to prevent CLS -->
<img
  src="/hero.webp"
  alt="Description"
  width="1200"
  height="630"
  fetchpriority="high"
/>

<!-- Lazy load everything below the fold -->
<img
  src="/feature.webp"
  alt="Feature preview"
  width="600"
  height="400"
  loading="lazy"
/>

<!-- Responsive image with art direction -->
<picture>
  <source
    media="(min-width: 768px)"
    srcset="/hero-desktop.webp 1440w, /hero-desktop@2x.webp 2880w"
    width="1440" height="810"
  />
  <img
    src="/hero-mobile.webp"
    srcset="/hero-mobile.webp 390w, /hero-mobile@2x.webp 780w"
    sizes="100vw"
    alt="Hero image"
    width="390" height="600"
    fetchpriority="high"
  />
</picture>
```

---

## Horizontal Scroll Prevention

```css
/* Global — prevent horizontal scroll caused by overflow */
html, body {
  overflow-x: hidden;
  max-width: 100%;
}

/* Allow horizontal scroll only in specific containers */
.scroll-x-container {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch; /* momentum scrolling on iOS */
  scrollbar-width: thin;
  scrollbar-color: var(--color-border) transparent;
}

/* Hide native scrollbar but keep functionality */
.scroll-x-hide-bar::-webkit-scrollbar { display: none; }
.scroll-x-hide-bar { scrollbar-width: none; }
```

---

## Text at 200% Zoom

WCAG 1.4.4 requires text to be readable at 200% browser zoom without horizontal scrolling or loss of content.

**Test method:** Chrome → View → Zoom → 200%. Verify no overflow, no clipped text, no broken layouts.

**Common failures:**
- Fixed-width containers: `width: 600px` → use `max-width: 600px; width: 100%`
- Absolute positioned elements overlapping text
- `overflow: hidden` on text containers that contain wrapped text

```css
/* Pattern that survives 200% zoom */
.responsive-text-container {
  width: 100%;
  max-width: 680px;
  overflow-wrap: break-word;
  word-break: break-word;
}
```

---

## Responsive Checklist

```
[ ] Mobile-first: min-width only, no max-width
[ ] Tested at 390px, 768px, 1280px, 1440px
[ ] 100dvh everywhere — never 100vh
[ ] env(safe-area-inset-*) on fixed/sticky elements
[ ] Touch targets ≥ 44×44px on all interactive elements
[ ] Hover states inside @media (hover: hover)
[ ] No horizontal scroll at any viewport
[ ] Body text ≥ 16px at all sizes
[ ] Images have explicit width + height
[ ] Paragraph width constrained to max 72ch
[ ] Text readable at 200% browser zoom
[ ] Container queries used for component-level adaptation
```

---

*Reference version: global-design-skill v1.0 — `references/responsive.md`*
*Related: `rules/07-responsive-design.md`, `checklists/global-design-review.md` §5, `references/tokens.md`*
