# Rule — Typography

> Typography is not decoration — it is the primary carrier of meaning, hierarchy, and tone. Every typographic decision affects legibility, scanning behavior, and perceived brand quality. These rules encode what separates professional typography from default font stacks.

---

## R1 — All display type is fluid. No fixed px for headings.

Fixed headline sizes break at unexpected viewports. Fluid type with `clamp()` works correctly on every screen without media query overrides.

```css
/* Correct */
--text-hero:    clamp(3.5rem, 8vw + 1rem, 12rem);
--text-display: clamp(2.5rem, 5vw + 0.5rem, 7rem);
--text-h1:      clamp(2rem, 4vw + 0.25rem, 4.5rem);
--text-h2:      clamp(1.75rem, 3vw + 0.5rem, 4rem);
--text-h3:      clamp(1.25rem, 2vw + 0.25rem, 2rem);

/* Wrong — fixed pixel sizes */
h1 { font-size: 48px; }
h2 { font-size: 36px; }
```

**`clamp()` anatomy:** `clamp(minimum, preferred, maximum)`
- Minimum: smallest size — never go below this even on tiny screens
- Preferred: `Nvw + Xrem` — scales with viewport width
- Maximum: cap — won't get absurdly large on ultra-wide displays

---

## R2 — Body text minimum 16px (1rem) everywhere.

iOS Safari auto-zooms inputs with font-size < 16px. Users with vision impairment rely on browser default (16px). Smaller body text increases error rates in reading comprehension.

```css
/* Correct */
body { font-size: 1rem; }          /* 16px — user's base */
p    { font-size: var(--text-body); }  /* clamp(1rem, 1.2vw + 0.4rem, 1.2rem) */

/* Wrong */
body { font-size: 14px; }
.description { font-size: 13px; }

/* Exception: UI micro-labels (timestamps, badge counts) may be smaller
   but must never be interactive or primary reading content */
.timestamp { font-size: var(--text-2xs); }  /* 13px — OK for non-reading UI */
```

---

## R3 — Letter spacing tracks with size. Tighten large, widen small uppercase.

Optical spacing: large type has too much inter-letter space at default tracking; uppercase small labels need extra air to read as words.

```css
/* Large display type — tighten */
.hero-heading  { letter-spacing: var(--tracking-tighter); }  /* -0.04em */
.display-text  { letter-spacing: var(--tracking-tight); }    /* -0.03em */
.section-h2    { letter-spacing: var(--tracking-snug); }     /* -0.02em */

/* Body — neutral */
p { letter-spacing: var(--tracking-normal); }  /* 0 */

/* Uppercase labels — widen */
.table-header  {
  text-transform: uppercase;
  letter-spacing: var(--tracking-wider);   /* 0.06em */
}
.eyebrow {
  text-transform: uppercase;
  letter-spacing: var(--tracking-widest);  /* 0.12em */
}

/* Wrong — tracking uniform regardless of size */
h1 { letter-spacing: 0; }
.eyebrow { letter-spacing: 0; }
```

---

## R4 — Line height matches context: tight for headlines, relaxed for prose.

Headlines at 1.65 line-height look balloon-like and amateurish. Body at 1.1 is unreadable. Each has a correct range.

```css
/* Correct */
.display-heading { line-height: var(--line-height-tight);   }  /* 1.1 */
.section-heading { line-height: var(--line-height-snug);    }  /* 1.3 */
.ui-label        { line-height: var(--line-height-normal);  }  /* 1.5 */
.body-text       { line-height: var(--line-height-relaxed); }  /* 1.65 */
.small-dense     { line-height: var(--line-height-loose);   }  /* 1.8 */

/* Wrong */
h1 { line-height: 1.5; }    /* too loose — floaty headline */
p  { line-height: 1.2; }    /* too tight — exhausting to read */
```

---

## R5 — Maximum line length 75 characters (≈ 680px at 16px).

Lines longer than 75 characters cause the eye to lose its place when scanning to the next line. Use `max-width` on prose containers — not on UI components.

```css
/* Prose containers */
.prose { max-width: var(--container-prose); }  /* 680px */
article p { max-width: 65ch; }

/* UI components: no max-width constraint — fill their container */
.card-description { max-width: none; }  /* card width handles this */

/* Wrong — too wide */
.blog-content { max-width: 1200px; }  /* line length > 120 chars */
```

---

## R6 — Font pairing: one expressive display, one functional body, one mono.

Using only one font is bland. Using more than three creates chaos.

**The three slots:**

| Slot | Purpose | Example choices |
|---|---|---|
| Display | Headings, heroes, pull quotes | Fraunces, PP Editorial New, Cormorant, Clash Display, Syne |
| Body | Paragraphs, UI labels, body copy | Instrument Sans, DM Sans, Cabinet Grotesk, Outfit |
| Mono | Code, data, timestamps | JetBrains Mono, Berkeley Mono, Commit Mono |

**Banned as primary display fonts:** Inter, Roboto, Arial, Open Sans, Helvetica, Poppins (as default), Space Grotesk (as "premium" signal).

```css
/* Font loading — only required weights */
@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..900;1,9..144,300..900&family=Instrument+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
  --font-display: 'Fraunces', Georgia, serif;
  --font-body:    'Instrument Sans', system-ui, sans-serif;
  --font-mono:    'JetBrains Mono', 'Courier New', monospace;
}

h1, h2, h3     { font-family: var(--font-display); }
body           { font-family: var(--font-body); }
code, pre, kbd { font-family: var(--font-mono); }
```

---

## R7 — Eyebrow tag precedes every hero H1 and section H2.

The eyebrow provides context before the headline, creates visual breathing room, and adds a second entry point for scanning readers.

```html
<!-- Correct -->
<span class="eyebrow">New → Version 3.0</span>
<h1>Ship 4× faster without the chaos</h1>

<!-- Wrong — headline with no context -->
<h1>Ship 4× faster without the chaos</h1>
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
  font-size: var(--text-3xs);     /* 12px */
  font-weight: var(--font-weight-medium);
  letter-spacing: var(--tracking-widest);  /* 0.12em */
  text-transform: uppercase;
  color: var(--color-accent);
  margin-bottom: var(--space-5);
}
```

---

## R8 — Hero headlines are ≤ 3 lines on the smallest target viewport.

A headline wrapping to 4+ lines on mobile breaks scanning. Cut words, not the `clamp()` scale.

**Test process:**
1. Chrome DevTools → device: iPhone 14 Pro (390×844)
2. Count headline lines
3. If > 3: shorten the headline — never reduce font size to compensate

```css
/* The clamp scale controls size — headline must be short enough */
.hero-heading {
  font-size: var(--text-display);
  max-width: 14ch;          /* force natural break point */
}

/* Wrong — reducing font size to make long headline fit */
@media (max-width: 768px) {
  .hero-heading { font-size: 1.5rem; }  /* never compensate for verbosity */
}
```

---

## R9 — Gradient text is banned.

`background-clip: text` with a gradient kills text accessibility (color contrast checks fail because the color varies), breaks on some browsers, and reads as a dated design trend.

```css
/* Banned */
.gradient-text {
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

/* Correct alternatives */
.accent-word   { color: var(--color-accent); }         /* solid accent */
.italic-word   { font-style: italic; }                 /* typographic contrast */
.weight-word   { font-weight: var(--font-weight-bold); }  /* weight contrast */
```

---

## R10 — Variable fonts: animate weight and width on scroll for editorial impact.

Variable fonts allow smooth transitions between weights. Used deliberately, this creates kinetic hierarchy.

```css
/* Load variable font with axis ranges */
@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,100..900&display=swap');

/* Weight morphing on scroll */
@property --font-weight-morph {
  syntax: '<number>';
  inherits: false;
  initial-value: 300;
}

.kinetic-heading {
  font-variation-settings: 'wght' var(--font-weight-morph);
  transition: --font-weight-morph 400ms var(--ease-smooth);
}

/* Trigger via IntersectionObserver */
.kinetic-heading.in-view {
  --font-weight-morph: 800;
}

/* prefers-reduced-motion: skip the transition */
@media (prefers-reduced-motion: reduce) {
  .kinetic-heading { transition: none; --font-weight-morph: 700; }
}
```

---

## Typography Anti-Patterns

- Paragraph width > 80ch (eyes lose line when scanning)
- `font-size: 14px` on body text (too small for comfortable reading)
- All-caps paragraphs (slows reading speed by 25%)
- Mixing more than 3 typeface families
- Decorative fonts at small sizes (< 24px) — they become illegible
- Line-height < 1.4 for body text
- `letter-spacing: -0.05em` on body text (negative tracking works only for large display)
- `text-transform: uppercase` on long sentences (should only be used on labels ≤ 5 words)

---

## Acceptance Criteria

```
[ ] All headings use clamp() fluid scale — no fixed px
[ ] Body text ≥ 16px on all viewports (inputs too — prevents iOS zoom)
[ ] Hero H1 ≤ 3 lines on 390px viewport
[ ] Line heights correct: 1.1 headlines / 1.65 body
[ ] Letter spacing: tighter on large type, wider on uppercase labels
[ ] Font pairing: expressive display + functional body
[ ] No banned fonts as primary: Inter, Roboto, Arial, Helvetica, Poppins
[ ] Eyebrow tag present on hero H1 and major section H2s
[ ] No gradient text
[ ] Prose max-width ≤ 680px (65–75ch)
```

---

*Rule version: global-design-skill v1.0 — `rules/03-typography.md`*
*Related: `references/typography.md`, `tokens/tokens.css` typography section, `patterns/marketing-blocks/hero-sections.md`*
