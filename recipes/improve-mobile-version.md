# Recipe — Improve the Mobile Version

> Mobile is not a smaller desktop. It has different physics (touch), different posture (one hand, varying light), different intent (faster, more task-focused), and different technical constraints (OS chrome, safe areas, viewport units). Fix the mobile version by treating it as a distinct design problem.

---

## When to use

- Mobile bounce rate significantly higher than desktop
- Users complain about the mobile experience
- Desktop → responsive shrink created the mobile version (not designed for mobile)
- CTA not visible without scrolling on 390px
- Touch targets too small (common complaint: "hard to tap")
- iOS Safari has layout bugs (safe areas, 100vh, etc.)

---

## Diagnosis: Mobile Failure Modes

```
[ ] Using 100vh (breaks on iOS Safari — use 100dvh)
[ ] Interactive elements < 44px touch target
[ ] Text < 16px in form inputs (triggers iOS auto-zoom)
[ ] Hover states fire on tap (show on hover: hover rule missing)
[ ] Navigation is desktop nav scaled down (not mobile pattern)
[ ] Bottom of content hidden behind iOS home bar
[ ] Horizontal scroll from element wider than viewport
[ ] Fixed elements overlap content (nav, banners)
[ ] Images don't have explicit dimensions (CLS)
[ ] Font too small: < 15px body text on mobile
[ ] Tap targets too close together (< 8px gap between them)
[ ] Forms require landscape mode to see all fields
```

---

## Step 1 — Fix Viewport Height

**The most common iOS Safari bug. Fix this first.**

```css
/* WRONG: breaks on iOS Safari */
.hero { min-height: 100vh; }
.modal { height: 100vh; }
.full-screen { height: 100vh; }

/* CORRECT: uses dynamic viewport height */
.hero { min-height: 100dvh; }
.modal { height: 100dvh; }
.full-screen { height: 100dvh; }

/* For backwards compatibility with older browsers */
.hero {
  min-height: 100vh;              /* fallback */
  min-height: 100dvh;             /* override if supported */
}
```

---

## Step 2 — Fix Touch Targets

Every interactive element must be ≥ 44×44px. This is Apple's HIG and Google's Material Design minimum.

**Before:**
```css
.btn-sm   { height: 28px; padding-inline: 12px; }
.nav-link { padding: 4px 8px; font-size: 14px; }
.close-btn { width: 24px; height: 24px; }
```

**After — visual size unchanged, tap area expanded:**
```css
/* Option A: expand the element itself */
.btn-sm {
  height: 44px;
  padding-inline: var(--space-4);
  min-width: 44px;
}

/* Option B: expand tap area without visual change */
.close-btn {
  width: 24px;
  height: 24px;
  position: relative;
}
.close-btn::after {
  content: '';
  position: absolute;
  inset: -10px;  /* extends hit area by 10px on all sides = 44×44 */
}

/* Option C: use padding on links */
.nav-link {
  display: flex;
  align-items: center;
  min-height: 44px;
  padding-inline: var(--space-3);
}
```

---

## Step 3 — Prevent iOS Auto-Zoom on Inputs

iOS Safari zooms in when a form input has `font-size < 16px`. This is extremely jarring.

```css
/* All form inputs must be at least 16px on mobile */
input, select, textarea {
  font-size: 1rem;   /* 16px — prevents iOS zoom */
}

/* Or specifically on mobile */
@media (max-width: 767px) {
  input, select, textarea {
    font-size: 1rem;
  }
}
```

---

## Step 4 — Fix the Navigation

Desktop nav scaled to mobile = unreadable. Implement a proper mobile pattern.

**Mobile pattern decision:**

| Situation | Pattern |
|---|---|
| App with 3-5 sections | Bottom tab bar (see `patterns/navigation/mobile-navigation.md`) |
| Marketing site / app with 5+ sections | Hamburger → slide drawer |
| Simple 3-4 section site | Hamburger → dropdown sheet |

**Minimum implementation — hamburger drawer:**
```html
<!-- Hide desktop nav on mobile -->
<nav class="desktop-nav">...</nav>

<!-- Mobile: hamburger trigger -->
<button
  class="hamburger"
  aria-label="Open navigation menu"
  aria-expanded="false"
  aria-controls="mobile-drawer"
>
  <span class="hamburger-bar" aria-hidden="true"></span>
  <span class="hamburger-bar" aria-hidden="true"></span>
  <span class="hamburger-bar" aria-hidden="true"></span>
</button>
```

```css
/* Desktop nav: hide on mobile */
.desktop-nav  { display: flex; }
.hamburger    { display: none; }

@media (max-width: 767px) {
  .desktop-nav { display: none; }
  .hamburger   { display: flex; }
}
```

---

## Step 5 — Safe Area Insets

iPhones have a notch / Dynamic Island at top and a home indicator bar at bottom. Content behind these areas is unreachable.

```css
/* Page layout */
body {
  padding-top:    env(safe-area-inset-top);
  padding-bottom: env(safe-area-inset-bottom);
  padding-left:   env(safe-area-inset-left);
  padding-right:  env(safe-area-inset-right);
}

/* Fixed header */
.header {
  padding-top: max(var(--space-4), env(safe-area-inset-top));
}

/* Bottom tab bar */
.bottom-nav {
  padding-bottom: env(safe-area-inset-bottom);
}

/* The main content padding when bottom nav is present */
.app-main {
  padding-bottom: calc(56px + env(safe-area-inset-bottom));
}
```

**In `<head>` — required for safe area to work:**
```html
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
```

---

## Step 6 — Fix Horizontal Scroll

Any element wider than the viewport causes horizontal scroll on the entire page.

**Finding the culprit:**
```css
/* Debug: temporarily outline all elements wider than viewport */
* {
  outline: 1px solid red;
  max-width: 100%;
}
```

**Common causes and fixes:**
```css
/* Long words / URLs that don't wrap */
p, li, td {
  overflow-wrap: break-word;
  word-break: break-word;
}

/* Fixed-width elements */
.sidebar { width: 300px; }
/* Fix: */
.sidebar { width: min(300px, 100%); }

/* Tables wider than viewport */
.table-container {
  overflow-x: auto;       /* scroll the table, not the page */
  -webkit-overflow-scrolling: touch;
}

/* Images without max-width */
img { max-width: 100%; height: auto; }

/* Negative margins */
.section { margin-inline: -20px; }  /* causes overflow */
/* Fix: */
.section { padding-inline: 20px; }  /* use padding instead */
```

---

## Step 7 — Mobile Typography

```css
/* Mobile-specific adjustments */
@media (max-width: 767px) {
  /* Tighter hero headline on mobile */
  .hero-heading {
    font-size: clamp(2rem, 8vw, 3.5rem);
    letter-spacing: -0.02em;
    line-height: 1.1;
  }

  /* Increased line-height for body (easier to read on small screen) */
  body {
    font-size: 1rem;
    line-height: 1.7;
  }

  /* Reduce section padding on mobile */
  .section {
    padding-block: clamp(3rem, 8vw, 6rem);
    padding-inline: var(--space-5);
  }
}
```

---

## Step 8 — Hover States Only on Pointer Devices

Hover states fire on tap on touch devices, causing stuck states.

```css
/* WRONG: hover state fires on tap, gets stuck */
.card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-md);
}

/* CORRECT: only applies where hover is possible */
@media (hover: hover) and (pointer: fine) {
  .card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-md);
  }
}
```

---

## Step 9 — CTAs Above Fold on Mobile

On 390px, the hero CTA must be visible without scrolling.

**Audit process:**
1. Open Chrome DevTools → device: iPhone 14 Pro (390×844)
2. Can you see the primary CTA without scrolling?
3. If not: reduce hero image size, shorten headline, reduce subheadline

**Quick fix:**
```css
@media (max-width: 767px) {
  .hero-split {
    grid-template-columns: 1fr;
  }

  /* Move visual below text on mobile */
  .hero-visual { order: 2; }
  .hero-text    { order: 1; }

  /* Limit visual height so CTA stays above fold */
  .hero-visual img {
    max-height: 280px;
    object-fit: cover;
    object-position: top;
  }
}
```

---

## Step 10 — Performance on Mobile Networks

Mobile users are often on slower connections. Performance IS the mobile experience.

```html
<!-- Responsive images: smaller on mobile -->
<picture>
  <source
    media="(max-width: 767px)"
    srcset="/hero-mobile.webp 390w, /hero-mobile@2x.webp 780w"
    sizes="100vw"
  />
  <source
    media="(min-width: 768px)"
    srcset="/hero-desktop.webp 1200w, /hero-desktop@2x.webp 2400w"
    sizes="50vw"
  />
  <img
    src="/hero-desktop.webp"
    alt="..."
    width="1200"
    height="800"
    fetchpriority="high"
  />
</picture>
```

---

## Mobile Audit Checklist

Run on real device + Chrome DevTools (390px iPhone 14 Pro):

```
[ ] 100dvh used everywhere 100vh was used
[ ] All tap targets ≥ 44×44px (verified in accessibility inspector)
[ ] Form inputs: font-size ≥ 16px (no zoom on tap)
[ ] Mobile navigation pattern implemented (not desktop nav)
[ ] Safe area insets applied (header, bottom nav, fixed elements)
[ ] No horizontal scroll on any page
[ ] Hero CTA visible without scrolling on 390px
[ ] Hover states wrapped in @media (hover: hover)
[ ] PageSpeed Insights mobile score ≥ 80
[ ] Tested on real iOS device (Safari) and Android (Chrome)
[ ] viewport-fit=cover in meta viewport tag
[ ] Content not hidden behind fixed bottom nav
```

---

*Recipe version: global-design-skill v1.0 — `recipes/improve-mobile-version.md`*
*Related: `rules/02-layout-and-grid.md`, `patterns/navigation/mobile-navigation.md`, `templates/specs/frontend-tz.md`*
