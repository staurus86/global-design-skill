# Rule — Contrast Standards

> Contrast is not a binary pass/fail — it is a range. Below the floor, text becomes illegible. Above the ceiling, eyes fatigue faster than they would on paper. These rules define the floor, the ceiling, and the optimal band for every layer of a UI: page background → section → block/card → text. Compliance with WCAG 2.2 AA is the legal minimum; comfort-first contrast is the standard.

---

## R1 — The contrast triangle: background, block, text.

Every UI has three contrast relationships to manage simultaneously:

```
Page background
      │ ← surface separation contrast
   Section / Card background
      │ ← text background contrast
   Text / Icon / UI component
```

**Each relationship has a different target:**

| Relationship | Minimum | Target | Upper limit |
|---|---|---|---|
| Text on block background | 4.5:1 | 7:1 | 15:1 |
| Large text (≥ 24px or ≥ 18.7px bold) on block bg | 3:1 | 4.5:1 | 15:1 |
| UI components (borders, icons, inputs) | 3:1 | 4.5:1 | — |
| Block/card on page background | 1.5:1 | 2:1 – 3:1 | — |
| Adjacent sections (no border) | 1.2:1 | 2:1 | — |
| Focus ring on surrounding color | 3:1 | 4.5:1 | — |

**The upper limit matters.** Contrast above 15:1 — especially in dark mode — causes halation (the glowing halo effect around bright text on dark backgrounds) and increases eye fatigue for prolonged reading.

---

## R2 — WCAG 2.2 AA is the legal floor. Know all four tiers.

| Standard | Normal text | Large text | UI components |
|---|---|---|---|
| WCAG 2.2 A | — | — | No requirement |
| **WCAG 2.2 AA (minimum)** | **4.5:1** | **3:1** | **3:1** |
| WCAG 2.2 AAA | 7:1 | 4.5:1 | — |
| Comfort target (this skill) | 7:1 | 4.5:1 | 4.5:1 |

**Large text definition (WCAG):**
- Regular weight: ≥ 18pt (≥ 24px at 96dpi)
- Bold weight: ≥ 14pt (≥ 18.67px at 96dpi)

**Exemptions (WCAG explicitly excludes):**
- Disabled / inactive UI components — no contrast requirement
- Purely decorative elements (`alt=""`, no information)
- Logos and brand wordmarks

**Not exempt — common mistake:**
- Placeholder text → must meet 4.5:1 (it is a visible text instruction)
- Muted/secondary text → must meet 4.5:1 unless it is truly decorative

---

## R3 — OKLCH contrast quick-check. Verify with a tool.

The L channel in OKLCH is perceptually uniform — use it as a fast pre-flight check. Always verify exact ratios with a contrast checker.

```
Approximate L difference → contrast ratio (sRGB background):

ΔL ≥ 70  →  7:1+  ✅ AAA
ΔL ≥ 55  →  4.5:1  ✅ AA
ΔL ≥ 45  →  3:1  ✅ AA large text / UI
ΔL < 45  →  likely failing  ❌

Examples:
Text oklch(15% …) on background oklch(99% …)  → ΔL=84 → passes AAA ✅
Text oklch(52% …) on background oklch(99% …)  → ΔL=47 → passes AA ✅ (borderline)
Text oklch(58% …) on background oklch(99% …)  → ΔL=41 → fails AA ❌
Text oklch(75% …) on background oklch(15% …)  → ΔL=60 → passes AA ✅
```

**OKLCH heuristic is approximate — use for initial decision-making only.**

Precise tools:
- **polypane.app/color-contrast** — supports OKLCH input natively
- **colorsandfonts.com** — OKLCH and APCA support
- **whocanuse.com** — impact estimation across disability types
- **Firefox DevTools** → Accessibility panel → contrast ratio live check

---

## R4 — Surface layer contrast: block-on-background.

Cards, panels, modals, and sections must be visually distinct from the page background — but not violently. Too much surface contrast creates a cluttered, high-noise layout.

```css
/* Light mode surface stack */
:root {
  --color-base:      oklch(99% 0.005 258);   /* page background */
  --color-surface:   oklch(100% 0.002 258);  /* cards (slightly lighter) */
  --color-surface-2: oklch(96% 0.007 258);   /* sections, aside panels */
}

/* Surface ratios (light mode): */
/* base → surface: ~1.1:1 — subtle lift (use shadow to supplement) */
/* base → surface-2: ~1.4:1 — clear section boundary */

/* Dark mode surface stack */
.dark {
  --color-base:      oklch(10% 0.015 258);   /* page background */
  --color-surface:   oklch(13% 0.015 258);   /* cards */
  --color-surface-2: oklch(16% 0.015 258);   /* elevated panels */
}

/* Dark mode surface ratios: ~1.3:1 between layers — visible but not harsh */
```

**Surface separation without sufficient contrast → add a border:**

```css
/* When surface contrast < 1.5:1, use a border to define the boundary */
.card {
  background: var(--color-surface);
  border: 1px solid var(--color-border); /* border carries the separation, not contrast */
}

/* --color-border must have 3:1 ratio against BOTH adjacent surfaces */
--color-border: oklch(87% 0.009 258);  /* visible on L99 base and L100 cards */
```

---

## R5 — Adjacent section contrast. How to separate page sections.

Alternating section backgrounds create rhythm and content grouping. The options — ordered by visual weight:

```css
/* Option A: L±4 alternation + full section padding (most common) */
.section-light { background: oklch(99% 0.005 258); }
.section-alt   { background: oklch(95% 0.008 258); } /* ΔL=4, ratio ~1.1:1 */
/* Works because generous padding (≥ 96px) creates separation even at low contrast */

/* Option B: stronger L difference — visually distinct zones */
.section-base   { background: oklch(99% 0.005 258); }
.section-accent { background: oklch(97% 0.040 258); } /* accent-tinted surface */
/* ΔL=2, but chroma difference makes zones readable */

/* Option C: border-top as separator on identical backgrounds */
.section + .section {
  border-top: 1px solid oklch(90% 0.008 258 / 0.6);
}
/* No contrast difference needed — border carries the division */
```

**Rule:** Either ΔL ≥ 4 (visible without border) OR a 1px divider at 3:1 against both sections.

**Never:** Two adjacent sections at identical background with no border and no padding increase — they merge visually and destroy content grouping.

---

## R6 — Text on colored blocks. Measure against the immediate background.

When text sits inside a colored card, badge, or section, contrast is measured against that element's background — not against the page background.

```css
/* Card with accent-tinted background */
.feature-card {
  background: oklch(95% 0.05 258);   /* L=95 */
}
.feature-card p {
  color: oklch(20% 0.015 258);       /* L=20 — ΔL=75 → well above 4.5:1 ✅ */
}

/* Status badge: green background */
.badge-success {
  background: oklch(92% 0.06 145);   /* light green */
  color: oklch(22% 0.12 145);        /* dark green — ΔL=70 ✅ */
}

/* Status badge: dark background (error) */
.badge-error {
  background: oklch(30% 0.18 25);    /* dark red */
  color: oklch(96% 0.03 25);         /* near-white warm — ΔL=66 ✅ */
}

/* WRONG: using page-level text color on colored block */
.feature-card p {
  color: oklch(52% 0.010 258);  /* passes on white page, fails on L95 accent card */
}
```

**Verify each block separately.** Passing contrast on the page background does not mean the color passes inside a colored container.

---

## R7 — Gradient backgrounds. Measure at the worst point.

Text on gradients must pass at every point where text appears — not at the best point.

```css
/* Gradient background under text */
.hero {
  background: linear-gradient(
    to bottom,
    oklch(20% 0.015 258) 0%,   /* dark — good contrast for white text */
    oklch(50% 0.020 258) 100%  /* medium — potential failure zone */
  );
}
```

**Measurement rule:**
1. If text is light → measure contrast against the lightest point of the gradient under the text area
2. If text is dark → measure against the darkest point
3. If the gradient sweeps across the text area vertically → check at multiple vertical points

```css
/* Safe approach: contain text in the guaranteed high-contrast zone */
.hero__content {
  padding-top: 10%;          /* stays in the dark zone of the gradient */
  padding-bottom: 5%;        /* doesn't reach the fade-out */
}

/* Or: add a scrim overlay to guarantee minimum contrast */
.hero::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(
    to bottom,
    oklch(0% 0 0 / 0.5) 0%,  /* dark scrim strengthens contrast */
    oklch(0% 0 0 / 0) 100%
  );
}
/* Ensure text layer is above scrim (z-index) */
```

---

## R8 — Dark mode: upper contrast limit and halation.

Dark mode introduces a contrast problem that light mode does not have: **too-high contrast causes halation** — the perceived glow/blur around bright text on very dark backgrounds. This increases eye fatigue during prolonged use.

**Cause:** The human eye cannot fully adapt when bright light (text) coexists with very dark context (background). The iris tries to contract for the bright text but needs to dilate for the dark background — it compromises, causing blur and fatigue.

```css
/* Problem: pure white on near-black = 19:1 contrast — too harsh for body text */
.dark body {
  background: oklch(8%  0.015 258);   /* near-black */
  color:      oklch(100% 0 0);        /* pure white — contrast ~19:1 ❌ too high */
}

/* Solution: reduce text lightness in dark mode to comfortable band */
.dark body {
  background: oklch(8%  0.015 258);   /* near-black surface */
  color:      oklch(88% 0.007 258);   /* off-white, tinted — contrast ~12:1 ✅ */
}

/* Dark mode token set — optimal comfort range 10:1 – 15:1 for body text */
.dark {
  --color-text:       oklch(88% 0.007 258);  /* primary text — ~12:1 on dark surface */
  --color-text-2:     oklch(72% 0.008 258);  /* secondary text — ~7:1 */
  --color-text-muted: oklch(55% 0.009 258);  /* muted — ~4.5:1 (floor) */
}
```

**Dark mode contrast targets:**

| Role | Ratio target | OKLCH range |
|---|---|---|
| Primary body text | 10:1 – 15:1 | L 82–90% on L 8–10% bg |
| Secondary text | 7:1 – 10:1 | L 68–80% |
| Muted / meta text | 4.5:1 – 7:1 | L 50–65% |
| Headings (large) | 12:1 – 18:1 | L 90–95% |
| Interactive accent | 3:1 – 7:1 | Varies by hue |

**Never use pure `oklch(100% 0 0)` as body text color in dark mode.** Reduce L to 85–92% and add a slight hue tint.

---

## R9 — Muted, placeholder, and disabled states.

```css
/* Secondary / muted text — must still pass 4.5:1 */
--color-text-muted: oklch(52% 0.010 258);   /* on L99 base: ΔL=47, passes AA ✅ */

/* Placeholder text — MUST pass 4.5:1 (WCAG 2.2, 1.4.3) */
input::placeholder {
  color: oklch(57% 0.009 258);  /* verify against input background specifically */
}

/* Disabled state — WCAG exempts, but use reduced opacity pattern */
.btn:disabled {
  opacity: 0.38;        /* Material Design convention — visually signals disabled */
  cursor: not-allowed;
  /* Do NOT apply to elements that still require 4.5:1 — only truly inactive components */
}

/* Disabled state — alternative: explicit low-contrast without opacity */
.input:disabled {
  color:      oklch(72% 0.008 258);  /* below AA — acceptable for disabled */
  background: oklch(96% 0.006 258);
  /* Announce disabled state via aria-disabled="true" — don't rely on visual alone */
}
```

**Rules:**
- Muted text that conveys information → 4.5:1 required
- Placeholder text → 4.5:1 required (common mistake: treated like disabled)
- Disabled interactive elements → no WCAG contrast requirement, but must have non-color indicator (`aria-disabled`, `cursor: not-allowed`, structural change)

---

## R10 — Focus ring contrast (WCAG 2.2, §2.4.11).

The focus ring must pass 3:1 against **both** the background behind it and the element it surrounds. This is WCAG 2.2 AA (non-optional since WCAG 2.2 became W3C Recommendation).

```css
:root {
  --focus-ring-color:  oklch(57% 0.22 258);   /* accent color */
  --focus-ring-width:  2px;
  --focus-ring-offset: 2px;
}

:focus-visible {
  outline: var(--focus-ring-width) solid var(--focus-ring-color);
  outline-offset: var(--focus-ring-offset);
}

/* Verify:
   - focus ring vs page background: 3:1 minimum
   - focus ring vs focused element background: 3:1 minimum
   - In dark mode: adjust --focus-ring-color (lighter L) to maintain 3:1 on dark surfaces */

.dark :focus-visible {
  outline-color: oklch(73% 0.18 258);  /* lighter accent for dark surfaces */
}
```

**White background on focus ring (anti-pattern):**
```css
/* Wrong: single-color outline may be invisible on white or light surfaces */
:focus-visible { outline: 2px solid white; }  /* fails on light bg */

/* Correct: double ring ensures visibility on any background */
:focus-visible {
  outline: 2px solid var(--focus-ring-color);
  box-shadow: 0 0 0 4px var(--color-surface); /* inner gap ring in surface color */
}
```

---

## R11 — APCA: the next standard (WCAG 3.0).

APCA (Advanced Perceptual Contrast Algorithm) replaces the WCAG 2.x luminance formula with a model based on spatial frequency and reading conditions. It uses Lc (Lightness Contrast) values instead of ratios.

**Why it matters:** WCAG 2.x contrast ratios are flawed — very light colors on white can fail at 4.5:1 even when readable, while some combinations that look difficult can pass. APCA correlates better with actual readability.

**APCA Lc thresholds (informational — not yet a legal requirement):**

| Lc value | Use case |
|---|---|
| Lc 90+ | Body text, fluent reading (recommended) |
| Lc 75 | Large body text, comfortable reading |
| Lc 60 | Minimum body text |
| Lc 45 | Minimum large text (≥ 36px) |
| Lc 30 | Minimum non-text / icons (informational) |
| Lc 15 | Placeholder / disabled (minimum visual) |

**Relationship to WCAG 2.2 AA:**

WCAG 2.2 AA 4.5:1 ≈ APCA Lc 60 for most mid-range colors. For very light or very dark colors, APCA is more accurate.

```
APCA tool: https://www.myndex.com/APCA/
Use alongside WCAG 2.2 — WCAG 2.2 is legally required, APCA is better science.
```

---

## R12 — Fix workflow: correcting a failing contrast.

When a text/background combination fails, adjust in this priority order:

```
1. Darken text (increase L difference) — safest, preserves background design
2. Lighten/darken background — if text color is brand-constrained
3. Add a scrim/overlay behind text — for images and gradients
4. Increase font size to qualify for "large text" 3:1 requirement
5. Increase font weight to bold to qualify at ≤ 18.67px
6. Switch to a different token from the palette that passes
```

**OKLCH fix recipe:**

```css
/* Failing combination */
--color-text-muted: oklch(60% 0.010 258);   /* on L99 background: ΔL=39 → fails */

/* Fix Option A: darken the text */
--color-text-muted: oklch(48% 0.010 258);   /* ΔL=51 → passes AA ✅ */

/* Fix Option B: if 48% looks too dark, increase font size instead */
.hint-text {
  font-size: 1.125rem;   /* 18px — now qualifies as "large" for 3:1 threshold */
  color: oklch(60% 0.010 258);  /* ΔL=39 still fails... */
  /* 3:1 threshold would need ΔL ≈ 45, still need oklch(54% …) */
}
```

**Fast fix matrix for light mode (white/near-white background, L≈97–100):**

| Target ratio | Max text L (on L97 bg) | Min text L (on L10 bg) |
|---|---|---|
| 3:1 (large text) | ≤ 55% | ≥ 65% |
| 4.5:1 (body) | ≤ 47% | ≥ 72% |
| 7:1 (AAA) | ≤ 35% | ≥ 82% |

**Fast fix matrix for dark mode (near-black background, L≈8–12):**

| Target ratio | Min text L (on L10 bg) |
|---|---|
| 4.5:1 (body) | ≥ 55% |
| 7:1 (AAA) | ≥ 67% |
| Comfort max (~15:1) | ≤ 92% |

---

## R13 — Automated contrast checking in the workflow.

**During development — browser:**
```
Firefox DevTools → Accessibility tab → select element → see contrast ratio live
Chrome DevTools → Elements → Computed → Accessibility → Contrast ratio
```

**During design (Figma):**
```
Select text layer → right panel → Contrast checker plugin
Or: Stark plugin → checks WCAG 2.2 and APCA simultaneously
```

**In CI/CD — automated:**
```bash
# axe-core (npm) — runs WCAG 2.2 AA contrast checks
npx axe-cli https://your-staging-url.com --tags wcag2aa
# Reports all contrast failures as violations

# Playwright + axe integration
import { checkA11y } from 'axe-playwright'
await checkA11y(page, undefined, { runOnly: ['color-contrast'] })
```

**In CSS — lint with stylelint:**
```json
{
  "stylelint-a11y/content-property-no-static-value": true
}
```

---

## Eye Comfort: Beyond the Ratio

Contrast ratio alone does not determine reading comfort. These factors interact with contrast:

| Factor | Comfort range | Why |
|---|---|---|
| Line height | 1.5 – 1.8 for body | Space between lines reduces crowding |
| Line length | 55 – 75 characters | Long lines increase tracking distance |
| Letter spacing | 0 – 0.02em for body | Too tight = strain, too loose = fragmented |
| Font weight | 400–500 for body text | Heavy weight at small sizes closes letterforms |
| Background texture | Avoid patterns under text | Reduces effective contrast |
| Anti-aliasing | `-webkit-font-smoothing: antialiased` | Thins strokes — reduce contrast if using |
| Contrast ratio in context | Sweet spot: 7:1 – 12:1 | Both too low and too high cause fatigue |

```css
/* Eye-friendly body text token set (light mode) */
body {
  font-size: 1rem;              /* 16px minimum */
  line-height: 1.6;             /* comfort range */
  color: oklch(18% 0.013 258);  /* 7:1+ contrast — not pure black */
  background: oklch(99% 0.005 258);  /* not pure white */
  max-width: 68ch;              /* line length */
  letter-spacing: 0.01em;       /* slight tracking */
}
```

---

## Acceptance Criteria

```
[ ] Text on block: ≥ 4.5:1 for body (< 24px), ≥ 3:1 for large text (≥ 24px / ≥ 18.7px bold)
[ ] UI components (input borders, icon buttons, state indicators): ≥ 3:1
[ ] Card/block on page background: ≥ 1.5:1 OR a visible border at 3:1
[ ] Adjacent sections: ΔL ≥ 4 OR a 1px border at 3:1 on both sides
[ ] Placeholder text: ≥ 4.5:1 (measured against input background)
[ ] Muted/secondary text: ≥ 4.5:1
[ ] Focus ring: ≥ 3:1 against background AND against focused element
[ ] Dark mode body text: 10:1 – 15:1 (not pure white — L ≤ 92%)
[ ] Gradient text areas: measured at worst-contrast point of the gradient
[ ] Text on colored blocks: measured against the block color, not page background
[ ] Disabled components: non-color indicator present (aria-disabled + cursor)
[ ] All contrast verified with a tool — not estimated from OKLCH L alone
[ ] Automated axe-core check passes for color-contrast violations
[ ] Eye comfort factors: line-height ≥ 1.5, max-width ≤ 75ch, body text not pure black/white
```

---

*Rule version: global-design-skill v1.9.1 — `rules/19-contrast-standards.md`*
*Related: `rules/04-color.md` (OKLCH system), `rules/07-accessibility.md` (ARIA, keyboard), `references/color-alchemy.md` (token building), `checklists/global-design-review.md` section 2*
