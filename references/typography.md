# Reference — Typography

> Typography is the most immediate signal of quality — before layout, before color, before content. A wrong font destroys premium positioning in 200ms. This reference covers font selection, variable font axes, fluid scale, loading strategy, and pairing logic.

---

## Banned Fonts (automatic fail in any design)

Using any of these as a primary typeface is a critical failure in `checklists/global-design-review.md`:

| Font | Why banned |
|---|---|
| Inter | Over-indexed in developer tools — signals "default template" |
| Roboto | Google's utilitarian default — zero brand differentiation |
| Arial / Helvetica | System defaults — no design intent |
| Open Sans | Early 2010s SaaS — dated, no personality |
| Poppins | Overused in "modern startup" templates — signals amateur |

---

## Approved Font Pairs by Archetype

### Ethereal Black (A) — SaaS, AI, developer tools

| Role | Font | Where to load |
|---|---|---|
| Display / Hero H1 | Geist Display | Vercel CDN |
| Body / UI | Geist Mono | Vercel CDN |
| Alternative display | DM Serif Display | Google Fonts |
| Alternative body | DM Sans | Google Fonts |

```css
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:ital,opsz,wght@0,9..40,300..700;1,9..40,300..700&display=optional');

:root {
  --font-display: 'DM Serif Display', Georgia, serif;
  --font-body:    'DM Sans', system-ui, sans-serif;
}
```

---

### Editorial Luxury (B) — agencies, premium SaaS, fashion

| Role | Font | Notes |
|---|---|---|
| Display | PP Editorial New | Licensed — Pangram Pangram |
| Display (free alt) | Playfair Display | Google Fonts |
| Body | Instrument Sans | Google Fonts |
| Alternative display | Cormorant Garamond | Google Fonts — ultra-thin weight |

```css
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Instrument+Sans:ital,wght@0,400..700;1,400..700&display=optional');

:root {
  --font-display: 'Playfair Display', Georgia, serif;
  --font-body:    'Instrument Sans', system-ui, sans-serif;
}
```

---

### Cyberbrutalism (C) — portfolios, experimental startups

| Role | Font | Notes |
|---|---|---|
| Display | Monument Extended | Licensed — Pangram Pangram |
| Display (free alt) | Bebas Neue | Google Fonts |
| Body | Courier Prime | Google Fonts — mono for body |

---

### Organic Softness (D) — health, wellness, consumer

| Role | Font | Notes |
|---|---|---|
| Display | Fraunces | Google Fonts — variable, `opsz` axis |
| Body | Instrument Sans | Google Fonts |
| Alternative | Lora (variable) | Google Fonts — warmer serif |

```css
/* Fraunces variable — using opsz axis for optical warmth */
@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..900;1,9..144,300..900&family=Instrument+Sans:wght@400;500;600&display=optional');

:root {
  --font-display: 'Fraunces', Georgia, serif;
  --font-body:    'Instrument Sans', system-ui, sans-serif;
}

/* Apply optical sizing — critical for Fraunces */
h1, h2 { font-optical-sizing: auto; }
```

---

### Volumetric Glass (E) — fintech, premium tech

| Role | Font | Notes |
|---|---|---|
| Display | Neue Haas Grotesk | Licensed — Monotype |
| Display (free alt) | Plus Jakarta Sans | Google Fonts |
| Body | Inter (only if archetype is E) | Exception to the ban |

---

### Post-Digital Terminal (G) — dev tools, hacker

| Role | Font | Notes |
|---|---|---|
| Everything | Courier Prime | Google Fonts |
| Alt | VT323 | Google Fonts — pixel terminal |
| Alt | Berkeley Mono | Licensed — commercial mono |

---

### Spatial Luxury (H) — hardware, watches, premium products

| Role | Font | Notes |
|---|---|---|
| Display | Cormorant Garamond (thin weight) | Google Fonts |
| Display alt | Cinzel | Google Fonts — classical |
| Body | Cabinet Grotesk | Google Fonts |

---

## Variable Font Axes

Variable fonts contain multiple axes. Using the right axis at each scale = the difference between generic and editorial.

### Key axes and when to use them

| Axis | Tag | What it does | When to use |
|---|---|---|---|
| Weight | `wght` | Bold ↔ thin | All weights in one file |
| Width | `wdth` | Condensed ↔ expanded | Tight hero headlines |
| Optical size | `opsz` | Adjusts letterform for size | Display vs. body from same font |
| Italic | `ital` | Upright ↔ italic | Expressive editorial contrast |
| Slant | `slnt` | Oblique slant | Subtle alternative to full italic |

### `font-optical-sizing`

Always enable for serif display fonts. It adjusts stroke contrast, serif bracketing, and spacing automatically for the rendered size.

```css
/* Enable automatically — browser uses font-size to select axis value */
h1, h2, h3 {
  font-optical-sizing: auto;
}

/* Explicit control — use a large opsz value for hero display */
.hero-display {
  font-variation-settings: 'opsz' 144; /* largest optical variant */
  font-optical-sizing: none; /* disable auto when setting manually */
}
```

### Fraunces axis example (Organic Softness)

```css
/* Small optical size — compact, efficient for body use */
.body-text {
  font-family: 'Fraunces', serif;
  font-variation-settings: 'opsz' 14, 'wght' 400, 'SOFT' 0;
}

/* Large optical size — decorative, warm for display */
.hero-display {
  font-family: 'Fraunces', serif;
  font-variation-settings: 'opsz' 120, 'wght' 700, 'SOFT' 100;
  font-style: italic;
}
```

---

## Fluid Type Scale

All display sizes use `clamp()`. Never fixed `px` for headings. From `tokens/design-tokens.json`:

```css
:root {
  --text-hero:    clamp(3.5rem, 8vw + 1rem, 12rem);     /* Landing H1 */
  --text-display: clamp(2.5rem, 5vw + 0.5rem, 7rem);    /* Section hero */
  --text-h1:      clamp(2rem, 4vw + 0.25rem, 4.5rem);   /* Page H1 */
  --text-h2:      clamp(1.75rem, 3vw + 0.5rem, 4rem);   /* Section heading */
  --text-h3:      clamp(1.25rem, 2vw + 0.25rem, 2rem);  /* Card heading */
  --text-h4:      clamp(1.125rem, 1.5vw + 0.25rem, 1.5rem);
  --text-body:    clamp(1rem, 1.2vw + 0.4rem, 1.2rem);
  --text-sm:      0.9375rem;
  --text-xs:      0.875rem;
}
```

**Letter-spacing rules by size:**

```css
/* Large display — always negative tracking */
.hero-text    { letter-spacing: -0.04em; }   /* > 48px */
.display-text { letter-spacing: -0.03em; }   /* 32–48px */
.heading-text { letter-spacing: -0.02em; }   /* 24–32px */

/* Body and below — normal or positive */
.body-text    { letter-spacing: 0; }
.label-text   { letter-spacing: 0.04em; }    /* uppercase labels */
.eyebrow-text { letter-spacing: 0.12em; text-transform: uppercase; }
```

---

## Font Loading Strategy

Poor font loading causes FOUT (flash of unstyled text) or FOIT (invisible text). Use this strategy to prevent both.

### 1. Use `font-display: optional`

For landing pages where CLS is critical. If the font doesn't load in time, the system font is used permanently (no flash).

```css
@font-face {
  font-family: 'Instrument Sans';
  src: url('/fonts/instrument-sans-variable.woff2') format('woff2-variations');
  font-weight: 400 700;
  font-style: normal;
  font-display: optional;
}
```

### 2. Use `font-display: swap` for product apps

For apps where brand consistency matters more than CLS. Text shows immediately in fallback font, then swaps.

```css
@font-face {
  font-family: 'DM Sans';
  src: url('/fonts/dm-sans-variable.woff2') format('woff2-variations');
  font-weight: 300 700;
  font-display: swap;
}
```

### 3. Size-adjust fallback (eliminates layout shift)

```css
/* Measure your web font vs system font — adjust until CLS ≈ 0 */
@font-face {
  font-family: 'Instrument Sans Fallback';
  src: local('Arial');
  ascent-override: 94%;
  descent-override: 24%;
  line-gap-override: 0%;
  size-adjust: 100.6%;
}

:root {
  --font-body: 'Instrument Sans', 'Instrument Sans Fallback', system-ui, sans-serif;
}
```

### 4. Preload the primary display font

```html
<!-- In <head>, before any stylesheet -->
<link
  rel="preload"
  href="/fonts/playfair-display-variable.woff2"
  as="font"
  type="font/woff2"
  crossorigin
/>
```

### 5. Load only the weights you use

```
❌ Bad:  font-weight: 100 900  (full range — downloads entire variable axis)
✅ Good: font-weight: 400 700  (only needed range)
```

---

## Paragraph Width Constraint

Maximum readable line length is 75 characters (≈ 680px at 1rem base). This is a critical check in `checklists/global-design-review.md`.

```css
/* Apply to all prose containers */
.prose {
  max-width: 65ch;    /* ch = width of the "0" character */
}

/* Hero subtitle — slightly wider for marketing copy */
.hero-sub {
  max-width: 55ch;
}

/* Never let body paragraphs go full-width on desktop */
.article-body p {
  max-width: 72ch;
}
```

---

## Eyebrow Tags

Every H1 and H2 must have an eyebrow tag (per `checklists/global-design-review.md` item 3.7).

```html
<!-- Correct eyebrow structure -->
<div class="section-header">
  <span class="eyebrow">What we build</span>
  <h2>Infrastructure that doesn't get in your way</h2>
</div>
```

```css
.eyebrow {
  display: block;
  font-size: var(--text-3xs);        /* 0.75rem */
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--color-accent);
  margin-bottom: var(--space-3);
}
```

**Banned eyebrow copy:**
- "SECTION 01", "SECTION 02" — meta-labels, not content
- "ABOUT US", "WHAT WE DO", "OUR SERVICES" — state what's there, not the navigation label
- "FEATURES", "PRICING" — already obvious from context

**Good eyebrow examples:**
- "Used by 2,847 teams" — social proof
- "Now with AI" — news hook
- "Release 3.0" — versioning
- "Why [Company] is different" — positioning

---

## Italic as Contrast Tool

Italic weight creates editorial contrast without decoration. Use on one word in a hero headline.

```css
.hero-heading em {
  font-style: italic;
  color: var(--color-accent);
  /* For variable fonts, prefer slnt/ital axes */
  font-variation-settings: 'ital' 1, 'opsz' 120;
}
```

```html
<h1>Ship 4× faster <em>without</em> the chaos</h1>
```

---

## Font Pairing Decision Tree

```
1. What is the product category?
   → B2B SaaS / developer tool → Grotesque display + Mono body (Archetype A)
   → Consumer / lifestyle → Variable serif + Sans body (Archetype D)
   → Agency / luxury → Editorial serif + Humanist sans (Archetype B)
   → Hardware / premium product → Thin classical serif + Geometric sans (Archetype H)

2. Is the primary user on mobile or desktop?
   → Mobile-first → Prefer sans-serif body (better at small sizes)
   → Desktop → Serif body acceptable if line-height ≥ 1.6

3. What is the text density?
   → High density (admin, data) → Monospace or compact grotesque
   → Low density (landing, marketing) → Expressive serif display

4. Does the brand already have a typeface?
   → Yes → Use it for display, pick body to complement
   → No → Pick archetype, use the pair above
```

---

*Reference version: global-design-skill v1.0 — `references/typography.md`*
*Related: `rules/03-typography.md`, `tokens/design-tokens.json`, `references/aesthetic-archetypes.md`*
