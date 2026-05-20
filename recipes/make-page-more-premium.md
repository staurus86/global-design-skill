# Recipe — Make a Page Feel More Premium

> "Premium" is not decoration — it is the removal of everything that feels cheap, inconsistent, or effortless. Apply these steps in order. Each one compounds the previous.

---

## When to use

- Client says "it looks cheap / generic / amateur"
- Design uses default fonts, generic shadows, stock photos
- Everything is perfectly centered and symmetrical (= boring)
- The page could belong to any company in any industry

---

## Diagnosis: Premium Killers Checklist

Run this first. Each ✓ is a premium killer to fix.

```
[ ] Using Inter, Roboto, Arial, Open Sans, or Helvetica as primary typeface
[ ] Pure #000 or #fff background with no hue tint
[ ] Symmetric 3-column icon grid as features section
[ ] Centered hero: H1 + subtext + 2 equal buttons
[ ] Stock photography (people in offices, handshakes, laptops)
[ ] Generic hero gradient: purple → indigo on white
[ ] Zero visual texture (flat matte surfaces everywhere)
[ ] Side-stripe colored borders on cards
[ ] "Get Started" / "Learn More" CTAs
[ ] gradient text (background-clip: text)
[ ] Identical card padding throughout (uniform = cheap)
[ ] Neon outer glow box-shadows
[ ] Border-radius too small (< 8px) or too large (pill buttons on non-pill UI)
[ ] Decorative icons on every heading and bullet
```

---

## Step 1 — Replace the Typeface

The single highest-ROI change. An expressive display font elevates everything else.

**Before (banned):**
```css
font-family: 'Inter', sans-serif; /* or Roboto, Arial, Poppins */
```

**After — pick one pair:**

| Aesthetic | Display | Body |
|---|---|---|
| Ethereal / SaaS | Geist Display | Geist Mono |
| Editorial / Luxury | PP Editorial New / Playfair Display | Instrument Sans |
| Confident / B2B | Neue Haas Grotesk / Monument Extended | DM Sans |
| Warm / Consumer | Fraunces (variable, `wdth` axis) | Instrument Sans |
| Authoritative | Cormorant Garamond | Cabinet Grotesk |

```css
/* Load from Google Fonts or self-host */
@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..900;1,9..144,300..900&family=Instrument+Sans:wght@400;500;600&display=swap');

:root {
  --font-display: 'Fraunces', Georgia, serif;
  --font-body:    'Instrument Sans', system-ui, sans-serif;
}

h1, h2, h3 { font-family: var(--font-display); }
body        { font-family: var(--font-body); }
```

---

## Step 2 — Add Hue to Every Neutral

Pure gray is cheap. Tint all neutrals toward the accent hue.

**Before:**
```css
--color-base:    #0a0a0a;
--color-surface: #ffffff;
--color-border:  #e5e5e5;
--color-muted:   #737373;
```

**After:**
```css
/* All neutrals carry the brand hue */
--color-base:    oklch(8%  0.015 258);   /* near-black, blue tinted */
--color-surface: oklch(99% 0.005 258);   /* near-white, blue tinted */
--color-border:  oklch(90% 0.008 258);   /* light border with hue */
--color-muted:   oklch(52% 0.012 258);   /* mid gray with hue */

/* Dark mode */
--color-base:    oklch(10% 0.015 258);
--color-surface: oklch(14% 0.012 258);
--color-border:  oklch(22% 0.015 258 / 0.6);
```

---

## Step 3 — Add Surface Texture

Flat matte = commodity. Noise grain is the fastest premium signal.

```css
/* Add to body or root container */
body::after {
  content: '';
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 9999;
  opacity: 0.04;
  mix-blend-mode: overlay;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
  background-size: 256px;
}
```

---

## Step 4 — Break the Grid in One Section

Every section perfectly centered = corporate template. One section must deviate.

**The asymmetric editorial split:**
```css
.editorial-section {
  display: grid;
  grid-template-columns: 1fr 1.618fr;   /* golden ratio */
  gap: var(--space-16);
  align-items: center;
  padding-block: clamp(6rem, 12vw, 14rem);
}

/* Alternate: offset heading */
.heading-offset {
  position: relative;
  margin-left: -2rem;   /* intentionally breaks the container */
  font-size: var(--text-display);
  line-height: 0.92;
  letter-spacing: -0.04em;
}
```

**Micro-asymmetry on a symmetric layout:**
```css
/* Vary card padding — same grid, different rhythm */
.feature-grid .card:nth-child(3n+1) { padding: var(--space-8) var(--space-6); }
.feature-grid .card:nth-child(3n+2) { padding: var(--space-6) var(--space-8); padding-top: var(--space-10); }
.feature-grid .card:nth-child(3n)   { padding: var(--space-10) var(--space-6) var(--space-6); }
```

---

## Step 5 — Elevate the Hero

**Before (banned centered hero):**
```html
<section style="text-align: center; padding: 120px 24px">
  <h1>Supercharge Your Workflow</h1>
  <p>The all-in-one platform for modern teams.</p>
  <a href="#">Get Started</a>
  <a href="#">Learn More</a>
</section>
```

**After (split hero with perspective product visual):**
```html
<section class="hero-split">
  <div class="hero-split__text">
    <span class="eyebrow">New → Version 3.0</span>
    <h1 class="hero-split__heading">
      Ship 4× faster<br>
      <em>without</em> the chaos
    </h1>
    <p class="hero-split__sub">
      [Company] reduces deployment time from 45 minutes to 11.
      Used by 2,847 engineering teams.
    </p>
    <div class="hero-split__cta">
      <a href="/signup" class="btn-primary">Start free — no card required</a>
      <a href="/demo" class="btn-ghost">Watch 90s demo ↗</a>
    </div>
  </div>
  <div class="hero-split__visual">
    <img
      src="/product-screenshot.webp"
      alt="The [Product] dashboard showing 4 active deployments"
      width="720" height="480"
      fetchpriority="high"
      style="border-radius: var(--radius-xl); transform: perspective(1200px) rotateY(-8deg) rotateX(2deg);"
    />
  </div>
</section>
```

```css
.hero-split {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-16);
  align-items: center;
  min-height: 100dvh;
  padding-inline: var(--space-16);
}

.hero-split__heading {
  font-size: var(--text-display);  /* clamp(2.5rem, 5vw + 0.5rem, 7rem) */
  font-family: var(--font-display);
  font-weight: 700;
  line-height: 0.95;
  letter-spacing: -0.03em;
}

.hero-split__heading em {
  font-style: italic;
  color: var(--color-accent);
}

@media (max-width: 768px) {
  .hero-split { grid-template-columns: 1fr; min-height: auto; }
  .hero-split__visual { order: -1; }
}
```

---

## Step 6 — Fix Shadows

Generic box-shadows look like defaults. Ambient shadows look expensive.

**Before (cheap):**
```css
box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
box-shadow: 0 0 20px rgba(99, 102, 241, 0.5); /* neon glow — banned */
```

**After (premium shadow system):**
```css
/* Subtle ambient — for cards at rest */
--shadow-sm: 0 1px 2px oklch(0% 0 0 / 0.04),
             0 2px 4px oklch(0% 0 0 / 0.04);

/* Medium — for cards on hover, dropdowns */
--shadow-md: 0 4px 8px oklch(0% 0 0 / 0.06),
             0 12px 24px oklch(0% 0 0 / 0.08);

/* Large — for modals, elevated panels */
--shadow-lg: 0 8px 16px oklch(0% 0 0 / 0.08),
             0 24px 48px oklch(0% 0 0 / 0.14);

/* Colored ambient — brand accent tint only */
--shadow-accent: 0 8px 32px oklch(from var(--color-accent) l c h / 0.25);
```

---

## Step 7 — Add the Bezel Container

The double-container is a signature premium detail. Product screenshots feel expensive inside a bezeled frame.

```css
.bezel-outer {
  padding: 0.375rem;
  background: oklch(from var(--color-accent) l c h / 0.08);
  border: 1px solid oklch(from var(--color-accent) l c h / 0.2);
  border-radius: var(--radius-2xl);
  box-shadow: var(--shadow-lg);
}

.bezel-inner {
  border-radius: calc(var(--radius-2xl) - 0.375rem);
  overflow: hidden;
  background: var(--color-surface);
  box-shadow:
    inset 0 1px 0 oklch(100% 0 0 / 0.12),
    inset 0 -1px 0 oklch(0% 0 0 / 0.08);
}
```

---

## Step 8 — Space Generously and Unevenly

**Before:**
```css
section { padding: 80px 24px; } /* all sections identical */
```

**After:**
```css
/* Each section has its own rhythm */
.hero      { padding-block: clamp(6rem,  14vw, 16rem) clamp(4rem, 10vw, 12rem); }
.proof-bar { padding-block: clamp(2rem,  4vw,  3rem); }   /* tight by design */
.features  { padding-block: clamp(8rem,  14vw, 18rem); }
.pricing   { padding-block: clamp(6rem,  10vw, 12rem); }
.cta-final { padding-block: clamp(10rem, 16vw, 20rem); }  /* expansive exit */
```

---

## Step 9 — One Premium Detail at 120%

Pick the element most worth screenshotting. Push it to extraordinary.

**Options:**
- **The headline**: massive weight + tight tracking + italic contrast word
- **The product visual**: deep perspective transform + ambient shadow + bezel
- **A stat**: enormous number + elegant label + thin divider
- **A quote**: full-width, editorial size, CSS `quotes` property
- **A CTA button**: gradient fill + shimmer animation on hover

Everything else: clean and competent at 80%. The contrast makes the signature detail pop.

---

## Result Verification

After applying all steps, the design should pass:

```
[ ] A stranger can identify the industry within 3 seconds
[ ] The font feels distinctive — not a template font
[ ] At least one section breaks the grid
[ ] Shadows have depth — not flat or neon
[ ] Texture is present but subtle
[ ] The "One Memorable Thing" is visually dominant
[ ] No banned patterns from global-design-review.md remain
```

---

*Recipe version: global-design-skill v1.0 — `recipes/make-page-more-premium.md`*
*Related: `skills/hyperdesign/SKILL.md`, `rules/01-visual-hierarchy.md`, `rules/02-layout-and-grid.md`*
