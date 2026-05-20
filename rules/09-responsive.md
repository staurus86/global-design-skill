# Rule — Responsive Design

> Responsive is not "it shrinks on mobile." Responsive means every layout, interaction, and content decision was made with the smallest screen first. Desktop is an enhancement. Mobile is the product.

---

## R1 — Mobile-first CSS. Write small-screen styles by default; add breakpoints upward.

Mobile-first means the baseline CSS is for mobile. Larger viewports override with `min-width` breakpoints. The reverse — desktop default with `max-width` overrides — consistently produces worse mobile results because you're subtracting features instead of adding them.

```css
/* Correct — mobile first */
.hero {
  display: flex;
  flex-direction: column;
  padding: var(--space-10) var(--space-6);
  gap: var(--space-8);
}

@media (min-width: 768px) {
  .hero {
    flex-direction: row;
    align-items: center;
    padding: var(--space-20) var(--space-10);
  }
}

/* Wrong — desktop first, subtracting on mobile */
.hero {
  display: flex;
  flex-direction: row;
  padding: 80px 40px;
}

@media (max-width: 768px) {
  .hero {
    flex-direction: column;
    padding: 40px 24px;
  }
}
```

---

## R2 — Use `100dvh`, never `100vh`. Use `100svh` for small stable containers.

`100vh` on iOS Safari includes the browser chrome height, causing content to be cut off by the address bar. `100dvh` dynamically tracks the available viewport height.

```css
/* Hero that fills the screen */
.hero   { min-height: 100dvh; }   /* dynamic — adjusts as address bar hides/shows */

/* Fixed bottom sheet: use svh for stable calculation */
.drawer { height: 80svh; }        /* small — stable, excludes dynamic UI chrome */

/* Full-screen modal */
.modal  { height: 100dvh; }

/* Wrong — clips content behind iOS address bar */
.hero   { min-height: 100vh; }
.modal  { height: 100vh; }
```

---

## R3 — The 5 standard breakpoints. Use them consistently.

```css
:root {
  --bp-xs:  390px;   /* iPhone 14 Pro — smallest common target */
  --bp-sm:  640px;   /* large phones, small tablets */
  --bp-md:  768px;   /* tablet portrait */
  --bp-lg:  1024px;  /* tablet landscape, small laptop */
  --bp-xl:  1280px;  /* desktop */
  --bp-2xl: 1536px;  /* large desktop */
}

/* Usage */
@media (min-width: 640px)  { /* sm */ }
@media (min-width: 768px)  { /* md */ }
@media (min-width: 1024px) { /* lg */ }
@media (min-width: 1280px) { /* xl */ }
```

**Tailwind v4 breakpoints — same values:**
```css
@theme {
  --breakpoint-xs:  390px;
  --breakpoint-sm:  640px;
  --breakpoint-md:  768px;
  --breakpoint-lg:  1024px;
  --breakpoint-xl:  1280px;
  --breakpoint-2xl: 1536px;
}
```

**When to add a custom breakpoint:** Only when the content breaks — not to match a specific device. If the layout looks wrong between 900–1000px, add `@media (min-width: 960px)`. Don't add breakpoints preemptively.

---

## R4 — Test on real devices at 390px width first.

The critical mobile viewport is 390×844px (iPhone 14 Pro). If something breaks there, it breaks for the largest segment of mobile users. DevTools responsive mode is not a substitute for testing on a real device — tap targets, scroll inertia, and address bar behavior all differ.

**Mandatory test checklist before ship:**
```
[ ] Hero H1 ≤ 3 lines on 390px
[ ] No horizontal scroll at 390px
[ ] All tap targets ≥ 44×44px
[ ] Text legible — no overflow, no truncation of meaning
[ ] Forms usable — keyboard doesn't cover input fields
[ ] Navigation accessible — menu opens and closes
[ ] Images don't break layout
[ ] CTA above the fold or within first scroll on mobile
```

**DevTools simulation:** Right-click → Inspect → Toggle device toolbar → Select "iPhone 14 Pro" (390×844). Verify at 1× and 2× (Retina) zoom levels.

---

## R5 — Navigation pattern changes at breakpoints.

Desktop navigation rarely works on mobile. Each breakpoint class needs a considered navigation pattern.

```
Mobile (< 768px):   Hamburger menu or bottom tab bar (≤ 5 tabs)
Tablet (768–1024px): Collapsible sidebar or compact header nav
Desktop (> 1024px): Full horizontal nav or persistent sidebar
```

```html
<!-- Bottom tab navigation for mobile apps -->
<nav class="bottom-nav" aria-label="Main navigation">
  <a href="/" class="bottom-nav__item" aria-current="page">
    <svg aria-hidden="true" ...></svg>
    <span>Home</span>
  </a>
  <a href="/explore" class="bottom-nav__item">
    <svg aria-hidden="true" ...></svg>
    <span>Explore</span>
  </a>
  <!-- max 5 items — each needs a label, not icon-only -->
</nav>
```

```css
.bottom-nav {
  display: none;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  height: calc(56px + env(safe-area-inset-bottom));
  padding-bottom: env(safe-area-inset-bottom);
  background: var(--color-surface);
  border-top: 1px solid var(--color-border);
  display: flex;
  z-index: var(--z-sticky);
}

@media (min-width: 768px) {
  .bottom-nav { display: none; }  /* replaced by header nav on tablet+ */
}

.bottom-nav__item {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 4px;
  font-size: var(--text-3xs);
  color: var(--color-text-muted);
  text-decoration: none;
  min-height: 56px;
}

.bottom-nav__item[aria-current="page"] {
  color: var(--color-accent);
}
```

---

## R6 — Safe area insets on all devices with notches or home indicators.

Devices with rounded corners, notches, or gesture navigation areas require padding that accounts for those hardware intrusions.

```html
<!-- Required in <head> -->
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
```

```css
/* Apply to fixed/sticky elements at screen edges */
.header {
  padding-top: env(safe-area-inset-top);
}

.bottom-nav, .floating-cta {
  padding-bottom: env(safe-area-inset-bottom);
}

.side-drawer {
  padding-left: env(safe-area-inset-left);
}

/* Content areas — add safe area on sides for landscape iPhones */
.content-wrapper {
  padding-inline: max(var(--space-6), env(safe-area-inset-left), env(safe-area-inset-right));
}
```

---

## R7 — Responsive images: `srcset` + `sizes` for art direction, `<picture>` for format switching.

Sending a 1200px image to a 390px phone wastes 75% of the data.

```html
<!-- Same image, different sizes (resolution switching) -->
<img
  src="/product.webp"
  srcset="/product-400.webp 400w, /product-800.webp 800w, /product-1200.webp 1200w"
  sizes="(max-width: 768px) 100vw, (max-width: 1024px) 50vw, 33vw"
  alt="..."
  width="1200"
  height="800"
  loading="lazy"
/>

<!-- Different crops for different viewports (art direction) -->
<picture>
  <source
    media="(max-width: 767px)"
    srcset="/hero-portrait.webp 390w, /hero-portrait@2x.webp 780w"
    sizes="100vw"
  />
  <source
    media="(min-width: 768px)"
    srcset="/hero-landscape.webp 1200w, /hero-landscape@2x.webp 2400w"
    sizes="50vw"
  />
  <img src="/hero-landscape.webp" alt="..." width="1200" height="800" loading="eager" fetchpriority="high" />
</picture>
```

**`sizes` attribute:** Tells the browser how wide the image will render before it loads the CSS. Without it, the browser assumes 100vw and downloads the wrong size.

---

## R8 — Hover states only where hover exists.

On touch devices there is no hover state. CSS hover applied unconditionally can get "stuck" on tap — the element appears hovered after a touch interaction until the user taps elsewhere.

```css
/* Wrong — hover on touch devices gets stuck */
.card:hover { transform: translateY(-4px); box-shadow: var(--shadow-lg); }

/* Correct — hover only where pointer is fine (mouse) */
@media (hover: hover) and (pointer: fine) {
  .card:hover { transform: translateY(-4px); box-shadow: var(--shadow-lg); }
}

/* Touch-specific active state (visual feedback on tap) */
@media (hover: none) {
  .card:active { background: var(--color-surface-2); }
}
```

---

## R9 — No fixed pixel widths on containers or columns in the responsive range.

Fixed widths create horizontal scroll. Every layout dimension in the responsive range should be relative or constrained with `max-width`.

```css
/* Correct */
.container {
  width: 100%;
  max-width: var(--container-xl);     /* 1280px */
  margin-inline: auto;
  padding-inline: var(--space-6);     /* gutter */
}

.sidebar { width: min(280px, 100%); }  /* caps at 280px, never overflows */

/* Wrong */
.container { width: 1200px; }         /* horizontal scroll on small screens */
.sidebar   { width: 280px; }          /* overflows at small viewport */
```

---

## R10 — Typography adapts to viewport through `clamp()` — never breakpoint overrides.

Overriding font size inside media queries creates discrete jumps. `clamp()` produces a smooth continuous scale that never needs breakpoint intervention.

```css
/* Correct — continuous fluid scale */
--text-hero:    clamp(2.5rem, 7vw + 0.5rem, 10rem);
--text-display: clamp(2rem, 5vw + 0.5rem, 7rem);
--text-h1:      clamp(1.75rem, 4vw + 0.25rem, 4.5rem);
--text-h2:      clamp(1.5rem, 3vw + 0.5rem, 4rem);
--text-body:    clamp(1rem, 1.2vw + 0.4rem, 1.2rem);

/* Wrong — breakpoint overrides for type */
@media (max-width: 768px) {
  h1 { font-size: 2rem; }
  h2 { font-size: 1.5rem; }
}
```

---

## Responsive Audit Checklist

```
[ ] All layouts built mobile-first (min-width breakpoints)
[ ] min-height: 100dvh used — never 100vh
[ ] Tested on 390px width: no horizontal scroll, H1 ≤ 3 lines
[ ] All tap targets ≥ 44×44px
[ ] Navigation pattern appropriate for each breakpoint
[ ] viewport-fit=cover + safe area insets on fixed elements
[ ] Responsive images: srcset + sizes or <picture>
[ ] Hover states gated with @media (hover: hover) and (pointer: fine)
[ ] No fixed widths on containers in the responsive range
[ ] Typography uses clamp() — no media query font-size overrides
[ ] Forms tested with virtual keyboard open (iOS + Android)
[ ] CTAs visible above fold on 390px
```

---

*Rule version: global-design-skill v1.0 — `rules/09-responsive.md`*
*Related: `rules/07-accessibility.md` R8, `rules/08-performance.md` R3, `recipes/improve-mobile-version.md`, `tokens/tokens.css` breakpoints section*
