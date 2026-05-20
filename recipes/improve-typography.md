# Recipe — Improve Typography

> **Trigger:** The page "looks fine" but feels cheap, hard to scan, or lacks personality. Usually the culprit is font choice, scale, or density — not color or layout.

---

## Diagnosis Checklist

```
[ ] Using Inter, Roboto, Arial, or Helvetica as the primary display font
[ ] All headings at fixed px sizes (not clamp)
[ ] Hero H1 > 3 lines on mobile (390px)
[ ] Body text < 16px anywhere (especially inputs)
[ ] line-height: 1.5 on headings (too loose)
[ ] line-height: 1.2 on body text (too tight)
[ ] No eyebrow tag before hero H1
[ ] Uppercase labels with no letter-spacing (unreadable)
[ ] Letter-spacing: 0 on display headings (too spacious at large sizes)
[ ] Prose width > 75ch (eye loses the line)
[ ] Gradient text anywhere (background-clip: text)
[ ] Only one typeface — no display/body/mono separation
[ ] Text hierarchy: only weight used, no size difference between levels
```

---

## Step 1 — Replace the font

The single highest-impact change. A page on Inter looks like every SaaS from 2019. A page on Fraunces looks intentional.

**Font loading (head of document):**

```html
<!-- Preload the display font — hero text is likely LCP -->
<link rel="preload" as="font"
  href="https://fonts.gstatic.com/s/fraunces/v31/6NUh8FyLNQOQZAnv9bYEvDiIdE9Eqcbf.woff2"
  type="font/woff2" crossorigin />

<!-- Load the pair: expressive display + functional body -->
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..900;1,9..144,300..900&family=Instrument+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap"
      rel="stylesheet" />
```

```css
:root {
  --font-display: 'Fraunces', Georgia, serif;
  --font-body:    'Instrument Sans', system-ui, sans-serif;
  --font-mono:    'JetBrains Mono', 'Courier New', monospace;
}

/* Apply immediately */
h1, h2, h3, h4 { font-family: var(--font-display); }
body, p, label, input, button { font-family: var(--font-body); }
code, pre, kbd, samp { font-family: var(--font-mono); }
```

**Choosing the right pair:**

| Product type | Display font | Body font |
|---|---|---|
| SaaS / dev tool | Fraunces | Instrument Sans |
| Agency / creative | Syne or Clash Display | DM Sans |
| Finance / legal | Cormorant | Cabinet Grotesk |
| Health / wellness | Fraunces (italic) | Outfit |
| Editorial / blog | PP Editorial New | Instrument Sans |

**Never use as primary display:** Inter, Roboto, Arial, Helvetica, Open Sans, Poppins, Space Grotesk.

---

## Step 2 — Switch to fluid type scale

Replace every fixed `font-size` on headings with `clamp()`. Inputs must be ≥ 1rem.

```css
/* Before */
h1 { font-size: 48px; }
h2 { font-size: 36px; }
h3 { font-size: 24px; }
p  { font-size: 14px; }

/* After */
:root {
  --text-hero:    clamp(3.5rem, 8vw + 1rem, 12rem);
  --text-display: clamp(2.5rem, 5vw + 0.5rem, 7rem);
  --text-h1:      clamp(2rem, 4vw + 0.25rem, 4.5rem);
  --text-h2:      clamp(1.75rem, 3vw + 0.5rem, 4rem);
  --text-h3:      clamp(1.25rem, 2vw + 0.25rem, 2rem);
  --text-body:    clamp(1rem, 1.2vw + 0.4rem, 1.2rem);
  --text-sm:      clamp(0.875rem, 0.8vw + 0.4rem, 1rem);
}

h1 { font-size: var(--text-h1); }
h2 { font-size: var(--text-h2); }
h3 { font-size: var(--text-h3); }
p  { font-size: var(--text-body); }
input, textarea, select { font-size: var(--text-body); } /* prevents iOS zoom */
```

---

## Step 3 — Fix line-height per context

Line-height should feel inevitable — tight headlines, airy body text.

```css
/* Before: same line-height everywhere */
* { line-height: 1.5; }

/* After: context-specific */
h1, h2     { line-height: 1.1;  }  /* tight — headlines need density */
h3, h4     { line-height: 1.3;  }  /* snug */
p, li, td  { line-height: 1.65; }  /* relaxed — reading comfort */
label,
.ui-label  { line-height: 1.5;  }  /* normal — short strings */
```

---

## Step 4 — Fix letter-spacing

Large type at default tracking looks loose and amateurish. Uppercase labels need extra air.

```css
/* Before: tracking never set */
h1 { letter-spacing: 0; }
.label { text-transform: uppercase; letter-spacing: 0; } /* unreadable */

/* After */
.text-hero    { letter-spacing: -0.04em; }  /* tightest */
.text-display { letter-spacing: -0.03em; }
h1, h2        { letter-spacing: -0.02em; }
h3            { letter-spacing: -0.01em; }
p             { letter-spacing: 0; }        /* neutral */

/* Uppercase labels — always wider */
.eyebrow, .table-header, .badge {
  text-transform: uppercase;
  letter-spacing: 0.08em;     /* minimum */
}
.section-label {
  text-transform: uppercase;
  letter-spacing: 0.12em;     /* wider for small labels */
}
```

---

## Step 5 — Add eyebrow tag

Every hero H1 and major section H2 should have an eyebrow — a small caps label that provides context before the headline.

```html
<!-- Before: headline with no context -->
<h1>Deploy in 30 seconds, roll back in 10</h1>

<!-- After: eyebrow + headline -->
<span class="eyebrow">Now in beta</span>
<h1>Deploy in 30 seconds, roll back in 10</h1>
```

```css
.eyebrow {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  padding: 0.25rem 0.875rem;
  border: 1px solid oklch(from var(--color-accent) l c h / 0.4);
  border-radius: var(--radius-full);
  background: oklch(from var(--color-accent) l c h / 0.06);
  font-size: var(--text-3xs);   /* 11–12px */
  font-weight: var(--font-weight-medium);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--color-accent);
  margin-bottom: var(--space-5);
}
```

---

## Step 6 — Constrain prose width

Long lines break reading. Set max-width on content containers.

```css
/* Before: full-width prose */
.blog-post p { max-width: none; }
.feature-desc { max-width: 100%; }

/* After */
article p,
.prose         { max-width: 65ch; }   /* body text: 65–75 chars per line */
.feature-desc  { max-width: 42ch; }   /* short card descriptions */
.hero-sub      { max-width: 48ch; }   /* hero subheadline */
```

---

## Step 7 — Remove gradient text

`background-clip: text` with a gradient fails contrast checks and reads as a dated pattern.

```css
/* Before */
.gradient-text {
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

/* After — pick one replacement */
.accent-word  { color: var(--color-accent); }           /* solid accent color */
.italic-word  { font-style: italic; }                   /* typographic contrast */
.weight-word  { font-weight: 900; }                     /* weight contrast */
```

---

## Before/After Summary

| Problem | Fix |
|---|---|
| Inter as primary font | Fraunces + Instrument Sans |
| Fixed `48px` heading | `clamp(2rem, 4vw + 0.25rem, 4.5rem)` |
| `line-height: 1.5` on H1 | `line-height: 1.1` |
| `line-height: 1.2` on body | `line-height: 1.65` |
| No letter-spacing on large type | `-0.02em` to `-0.04em` |
| Uppercase with no tracking | `letter-spacing: 0.12em` |
| No eyebrow tag | `<span class="eyebrow">` before every H1/H2 |
| Prose full-width | `max-width: 65ch` |
| Gradient text | Solid accent or italic |
| 14px body text | `font-size: var(--text-body)` (1rem min) |

---

## Verification

```
[ ] Font: expressive display + functional body + mono — no Inter/Roboto/Arial
[ ] All headings use clamp() — verify by resizing browser from 390px to 1920px
[ ] Hero H1 ≤ 3 lines at 390px width
[ ] Body text ≥ 16px — check in DevTools Computed styles
[ ] line-height: 1.1 on hero, 1.65 on paragraphs
[ ] Letter-spacing tight on large type, wide on uppercase labels
[ ] Eyebrow present before hero H1 and major section H2s
[ ] Prose containers: max-width 65ch or less
[ ] No gradient text
[ ] Inputs: font-size: 1rem (test on iPhone — no auto-zoom)
```

---

*Recipe version: global-design-skill v1.0 — `recipes/improve-typography.md`*
*Related: `rules/03-typography.md`, `tokens/tokens.css` typography section, `examples/01-hero-redesign.md`*
