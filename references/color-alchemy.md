# Reference — Color Alchemy

> OKLCH science, perceptual palettes, dark mode, multi-accent systems, P3 wide-gamut, and data visualization color. The "why" behind `tokens/design-tokens.json`.

---

## Why OKLCH

OKLCH (Oklab Lightness-Chroma-Hue) solves the core problem with HSL and hex: equal numeric steps produce unequal perceived changes.

| Color space | Perceptual uniformity | CSS support | Dark mode predictability |
|---|---|---|---|
| Hex / RGB | ❌ No | ✅ Universal | ❌ Unpredictable |
| HSL | ⚠️ Partial | ✅ Universal | ⚠️ Lightness unreliable |
| **OKLCH** | **✅ Yes** | **✅ Baseline 2023** | **✅ Predictable** |
| Lab / LCH | ✅ Yes | ✅ Baseline 2023 | ✅ Predictable |

**Practical consequence:** When you set `L = 65%` for two different hues in OKLCH, they appear equally bright. In HSL, they would not — yellow at `hsl(60, 100%, 50%)` appears much lighter than blue at `hsl(240, 100%, 50%)`.

---

## Anatomy of an OKLCH Token

```css
--color-accent: oklch( 65%   0.22   258 );
/*                     ^^^   ^^^^   ^^^
                        L     C      H
                     Lightness  Chroma  Hue angle
                     0-100%     0-0.4   0-360      */
```

**Lightness (L):**
- 0% = absolute black, 100% = absolute white
- Human perception maps to this linearly
- Use as the primary lever for light/dark mode variants

**Chroma (C):**
- 0 = gray (no saturation), 0.4 = maximum (not all hues reach 0.4)
- Max gamut-safe chroma for sRGB display: ~0.25 (hue-dependent)
- P3 display allows ~0.33
- Rule: if it looks oversaturated on a standard monitor, drop C

**Hue (H):**
- 0/360 = red, 90 = yellow, 180 = cyan, 258 = blue-violet, 295 = purple

---

## Building the Neutral Scale

Neutrals must carry the accent hue — never pure gray. This creates visual coherence across the entire design.

```css
/* Hue = 258 (blue-violet) — adjust to match your accent */
:root {
  --neutral-0:    oklch(100% 0.002 258);  /* near white, barely tinted */
  --neutral-50:   oklch(99%  0.005 258);
  --neutral-100:  oklch(97%  0.007 258);
  --neutral-200:  oklch(93%  0.008 258);
  --neutral-300:  oklch(87%  0.010 258);
  --neutral-400:  oklch(72%  0.010 258);
  --neutral-500:  oklch(55%  0.010 258);
  --neutral-600:  oklch(42%  0.012 258);
  --neutral-700:  oklch(32%  0.012 258);
  --neutral-800:  oklch(22%  0.012 258);
  --neutral-900:  oklch(15%  0.013 258);
  --neutral-950:  oklch(11%  0.014 258);
  --neutral-1000: oklch(8%   0.015 258);
}
```

**Rule:** Chroma of neutrals should be 10–15% of the accent chroma. If accent C = 0.22, neutral C = 0.010–0.015.

---

## Semantic Token Layer

Never use primitive tokens in components. Always map through a semantic layer.

```css
/* Light mode defaults */
:root {
  --color-base:          var(--neutral-50);
  --color-surface:       var(--neutral-0);
  --color-surface-2:     var(--neutral-100);
  --color-border:        var(--neutral-200);
  --color-text:          var(--neutral-950);
  --color-text-2:        var(--neutral-700);
  --color-text-muted:    var(--neutral-500);
  --color-accent:        oklch(57% 0.22 258);   /* accent-600 — darker for light bg */
  --color-accent-bg:     oklch(97% 0.04 258);   /* accent-50 */
}

/* Dark mode */
.dark {
  --color-base:          var(--neutral-1000);
  --color-surface:       var(--neutral-950);
  --color-surface-2:     var(--neutral-900);
  --color-border:        oklch(26% 0.012 258 / 0.7);
  --color-text:          var(--neutral-50);
  --color-text-2:        var(--neutral-300);
  --color-text-muted:    var(--neutral-500);
  --color-accent:        oklch(73% 0.18 258);   /* accent-400 — lighter for dark bg */
  --color-accent-bg:     oklch(20% 0.06 258);
}
```

**Dark mode accent rule:** Increase L by ~10–15%, decrease C slightly. The accent must pass 3:1 contrast on `--color-surface` in both modes.

---

## Generating the Accent Scale

From a single brand hue, generate the full 10-step scale:

```css
/* Given accent hue = 258, target base lightness = 65% */
:root {
  --accent-50:  oklch(97% 0.04 258);
  --accent-100: oklch(93% 0.07 258);
  --accent-200: oklch(87% 0.11 258);
  --accent-300: oklch(80% 0.15 258);
  --accent-400: oklch(73% 0.18 258);  /* dark mode interactive */
  --accent-500: oklch(65% 0.22 258);  /* base (reference) */
  --accent-600: oklch(57% 0.22 258);  /* light mode interactive */
  --accent-700: oklch(48% 0.20 258);
  --accent-800: oklch(38% 0.17 258);
  --accent-900: oklch(28% 0.12 258);
}
```

**Pattern:** L decreases 7–10 points per step. C increases through the midrange, then decreases toward the dark end (dark colors can't hold high chroma on most displays).

---

## Multi-Accent Palettes

For products with multiple accent colors (status, data categories, UI zones):

### Complementary pair (high contrast, brand primary + action)

```css
/* Primary accent: blue-violet */
--color-accent-primary: oklch(65% 0.22 258);
/* Secondary accent: 180° opposite = warm orange */
--color-accent-secondary: oklch(65% 0.22 78);
```

### Split-complementary (softer, for marketing sections)

```css
/* Primary: blue-violet (258) */
--color-accent-a: oklch(65% 0.22 258);
/* Split left: cyan (210) */
--color-accent-b: oklch(65% 0.20 210);
/* Split right: magenta (310) */
--color-accent-c: oklch(65% 0.18 310);
```

### Analogous (for dashboard data series, 6 series)

Keep hues within a 60° arc, vary lightness for distinction:

```css
--data-1: oklch(58% 0.22 258);   /* blue-violet */
--data-2: oklch(62% 0.20 230);   /* blue */
--data-3: oklch(55% 0.22 285);   /* purple */
--data-4: oklch(65% 0.18 200);   /* teal */
--data-5: oklch(52% 0.20 310);   /* magenta */
--data-6: oklch(68% 0.15 170);   /* green */
```

---

## Color for Data Visualization

Chart color series must satisfy two constraints simultaneously:
1. Distinguishable by hue for color-sighted users
2. Distinguishable by lightness for color-blind users

```css
/* 8-color accessible data palette */
:root {
  /* Spread hue by ~40–50° increments, vary L for grayscale distinction */
  --chart-1: oklch(55% 0.22 258);   /* blue — L55 */
  --chart-2: oklch(62% 0.20 25);    /* red-orange — L62 */
  --chart-3: oklch(68% 0.18 145);   /* green — L68 */
  --chart-4: oklch(50% 0.22 300);   /* purple — L50 */
  --chart-5: oklch(72% 0.16 75);    /* amber — L72 */
  --chart-6: oklch(45% 0.20 195);   /* teal-dark — L45 */
  --chart-7: oklch(78% 0.14 330);   /* pink-light — L78 */
  --chart-8: oklch(40% 0.18 258);   /* navy — L40 */
}
```

**Grayscale test:** Convert to grayscale — each color should appear as a distinct shade of gray. If two look identical, adjust L.

**Dark mode chart colors:** Increase L by ~8–12% for all chart series. Dark backgrounds need lighter colors to maintain contrast.

---

## WCAG Contrast Requirements

From `checklists/global-design-review.md`:
- Normal text (< 18px regular, < 14px bold): **4.5:1** against background
- Large text (≥ 18px regular, ≥ 14px bold): **3:1**
- UI components and focus rings: **3:1**

### Quick contrast check in OKLCH

Approximate contrast ratio from lightness values (not exact, but useful for quick checks):

```
L difference for ~4.5:1: ≈ 60 points
L difference for ~3:1:   ≈ 45 points

Example:
Text L=10% on background L=97%  → difference=87 → passes 4.5:1 ✅
Text L=55% on background L=97%  → difference=42 → fails 4.5:1 ❌
Text L=42% on background L=97%  → difference=55 → passes 4.5:1 ✅
```

For precise values, use a contrast checker that supports OKLCH (polypane.app, colorsandfonts.com).

---

## P3 Wide-Gamut Colors

Display P3 allows more vivid colors — particularly greens, reds, and deep blues — than sRGB. Supported on Apple devices (iPhone 7+, MacBook Pro 2016+) and most modern monitors.

**Strategy:** Define P3 colors as a progressive enhancement. sRGB fallback first.

```css
/* Start with sRGB-safe OKLCH */
:root {
  --color-accent: oklch(65% 0.22 258);
}

/* P3 enhancement — only on capable displays */
@media (color-gamut: p3) {
  :root {
    --color-accent: oklch(65% 0.28 258);   /* higher chroma, stays in P3 gamut */
  }
}
```

**Max P3-safe chroma by hue region:**

| Hue range | Max sRGB C | Max P3 C |
|---|---|---|
| Red (0–30°, 330–360°) | 0.25 | 0.33 |
| Yellow-green (70–130°) | 0.22 | 0.30 |
| Green (130–170°) | 0.25 | 0.36 |
| Cyan (170–220°) | 0.20 | 0.28 |
| Blue (220–280°) | 0.22 | 0.28 |
| Purple (280–330°) | 0.22 | 0.30 |

---

## Color Strategy by Page Type

### "Restrained" — admin panels, dashboards

```css
/* Two accents max, one primary + one status */
--color-accent:   oklch(57% 0.22 258);
--color-success:  oklch(55% 0.18 145);
--color-warning:  oklch(65% 0.18 75);
--color-error:    oklch(52% 0.22 25);
/* Everything else: neutrals */
```

### "Committed" — SaaS marketing, landing pages

```css
/* One accent used deliberately throughout */
--color-accent:    oklch(65% 0.22 258);
--color-accent-bg: oklch(97% 0.04 258);   /* sections, badges */
/* One supporting accent for hover/focus */
--color-accent-2:  oklch(65% 0.18 295);
```

### "Full palette" — consumer apps, dashboards with data viz

```css
/* Multiple semantic colors + chart series */
/* Follow multi-accent palette rules above */
```

### "Drenched" — Neo-Maximalism, event sites

```css
/* Color IS the surface */
--color-base: oklch(65% 0.30 75);   /* saturated amber as page background */
/* Typography in high-contrast dark or white against it */
```

---

## Opacity Tokens for Layering

Use relative color syntax to generate opacity variants from tokens:

```css
/* Relative color syntax — CSS 2023, Baseline 2024 */
.surface-accent-tint {
  background: oklch(from var(--color-accent) l c h / 0.08);
}

.border-accent-subtle {
  border-color: oklch(from var(--color-accent) l c h / 0.20);
}

/* Darker variant of surface (without separate token) */
.surface-elevated {
  background: oklch(from var(--color-surface) calc(l - 2%) c h);
}
```

---

## Palette Tools

- **Coolors** (coolors.co) — fast palette generator with export, accessibility/contrast check, and color extraction from an image. Use it to *explore*, then convert the chosen hues to OKLCH tokens (this skill ships OKLCH, never raw hex — see R1 in `rules/04-color.md`).
- **OKLCH Color Picker** (oklch.com, Evil Martians) — pick and tune directly in OKLCH; the right final step after Coolors exploration.

Workflow: explore in Coolors → lock the hue family → rebuild the scale in OKLCH (`oklch.com`) → tokenize per `Generating the Accent Scale` above. Never ship a Coolors hex palette directly.

---

## Banned Color Patterns

These are explicit fails in `checklists/global-design-review.md`:

```
❌ Purple-to-indigo gradient on white background
❌ Neon outer glow box-shadows
❌ Pure #000000 or #ffffff (no hue tint)
❌ Violet hero gradients
❌ rgba(purple, 0.2) blobs as the only decoration
❌ Hex colors in any component (use OKLCH tokens)
❌ Gradient text (background-clip: text)
```

---

*Reference version: global-design-skill v1.9.5 — `references/color-alchemy.md`*
*Related: `rules/04-color.md`, `tokens/design-tokens.json`, `references/visual-effects.md`, `references/component-libraries.md`*
