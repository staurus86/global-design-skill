# Rule — Color

> Color is not decoration — it is a communication system. Every color in the UI carries a meaning: hierarchy, state, brand, status. When color is applied without system, the result is visual noise. These rules encode how to build a color system that works at scale, across themes, and in every context.

---

## R1 — OKLCH for all color values. Never hex or rgb() in components.

OKLCH is perceptually uniform: equal numeric changes produce equal perceptual changes. This means:
- Colors at the same `L` value have equal perceived lightness (unlike HSL or hex)
- Adjusting chroma `C` consistently increases/decreases saturation
- Color relationships stay predictable as you build the scale

```css
/* Correct */
--color-accent: oklch(65% 0.22 258);
--color-base:   oklch(10% 0.015 258);
--color-border: oklch(90% 0.008 258);

/* Wrong */
--color-accent: #6366f1;
--color-border: rgba(0, 0, 0, 0.1);
background: rgb(255, 255, 255);
```

**OKLCH anatomy:**
```
oklch( L     C      H    )
       ↑     ↑      ↑
   Lightness Chroma Hue
   0–100%    0–0.4  0–360°

oklch(65% 0.22 258)
      ↑    ↑    ↑
   65%    0.22  258° (blue)
 lightness chroma  hue
```

---

## R2 — Tint all neutrals toward the accent hue.

Pure gray (`oklch(50% 0 0)`) reads as cold and corporate. A tiny chroma tilt (0.005–0.015) toward the brand hue creates cohesion without obvious coloration.

```css
/* Correct — neutral scale with hue 258 (blue) tint */
--color-neutral-50:   oklch(99%  0.005 258);
--color-neutral-100:  oklch(97%  0.007 258);
--color-neutral-500:  oklch(55%  0.010 258);
--color-neutral-900:  oklch(15%  0.013 258);

/* Wrong — pure achromatic gray */
--gray-100: oklch(97% 0 0);  /* no hue tint */
--gray-500: #737373;          /* hex, no tint */
```

**Rule:** Keep chroma between 0.005–0.018 for neutrals. Above 0.02 starts looking obviously tinted. Below 0.004 is effectively achromatic.

---

## R3 — One accent hue. Variations come from L and C, not H.

Multiple accent hues create visual conflict. States, emphasis levels, and context variations are communicated through lightness and chroma changes on the single accent hue.

```css
/* Correct — variations on single hue */
--color-accent:          oklch(65% 0.22 258);   /* base */
--color-accent-light:    oklch(73% 0.18 258);   /* lighter variant */
--color-accent-dark:     oklch(55% 0.22 258);   /* darker variant */
--color-accent-bg:       oklch(95% 0.04 258);   /* tinted background */
--color-accent-border:   oklch(85% 0.10 258);   /* mid-tone border */

/* Wrong — multiple accent hues */
--color-primary: oklch(65% 0.22 258);   /* blue */
--color-secondary: oklch(65% 0.20 120); /* green — second accent */
--color-tertiary: oklch(65% 0.22 30);   /* orange — third accent */
```

**Exception:** Status colors (success/warning/error) are semantic — they communicate specific system states and use different hues by necessity. They are not accent variations.

---

## R4 — Accent occupies ≤ 15% of visible surface area.

Accent color at full coverage loses its signaling power. It stands out because it contrasts with neutral surfaces. Overuse eliminates that contrast.

```
Neutral surfaces (base, surface, surface-2): 75–85% of screen
Text: 10–15%
Accent: ≤ 15% — reserved for interactive elements, active states, CTAs
Status colors: ≤ 5% each — only where that state is relevant
```

**Audit method:** Screenshot the page, desaturate it, then reintroduce only the accent color. If the accent color covers more than ~15% of the screen, reduce it.

---

## R5 — Reduce chroma as lightness approaches extremes.

Very dark or very light OKLCH colors with high chroma look garish because the gamut is smaller at extremes. Reduce chroma proportionally.

```css
/* Correct — chroma decreases toward extremes */
oklch(95% 0.04 258)   /* light tint — low chroma */
oklch(80% 0.12 258)   /* light-mid — moderate chroma */
oklch(65% 0.22 258)   /* mid — full chroma (base accent) */
oklch(45% 0.18 258)   /* dark-mid — reduced chroma */
oklch(20% 0.08 258)   /* dark — low chroma */

/* Wrong — high chroma at extremes */
oklch(95% 0.22 258)   /* oversaturated light — looks neon */
oklch(15% 0.22 258)   /* oversaturated dark — looks harsh */
```

---

## R6 — All color decisions account for WCAG 2.2 AA contrast.

Insufficient contrast reduces readability for users with low vision and is a legal requirement in many jurisdictions.

| Text type | Minimum ratio | Target |
|---|---|---|
| Normal text (< 18px regular, < 14px bold) | 4.5:1 | 7:1 |
| Large text (≥ 18px regular, ≥ 14px bold) | 3:1 | 4.5:1 |
| UI components (borders, icons) | 3:1 | 4.5:1 |
| Decorative (no information) | No requirement | — |

```css
/* Testing contrast in OKLCH: the L value gives a rough guide */
/* Difference of ≥ 50L between text and background ≈ 4.5:1 */

/* Light mode — text on white */
--color-text-primary:  oklch(15% 0.013 258);  /* L 15 on L 99 → 7:1+ */
--color-text-muted:    oklch(52% 0.010 258);  /* L 52 on L 99 → 4.5:1 ≈ */

/* Always verify with a contrast checker — OKLCH approximation is not exact */
```

---

## R7 — Color is never the only differentiator.

Approximately 8% of men and 0.5% of women have color vision deficiency. A UI that uses color alone to communicate state will fail for these users, and may fail WCAG 1.4.1.

**Required secondary signals:**

| State | Color | + secondary signal |
|---|---|---|
| Error | Red border | + error icon + error text |
| Success | Green indicator | + checkmark icon + success label |
| Warning | Yellow/amber | + warning icon + warning text |
| Disabled | Reduced opacity | + `aria-disabled="true"` + cursor:not-allowed |
| Active nav item | Accent color | + font-weight change or background |
| Required field | — | + asterisk (*) + screen reader "required" |

```html
<!-- Wrong: color alone -->
<input class="input-error" />

<!-- Correct: color + icon + text + ARIA -->
<input
  class="input-error"
  aria-invalid="true"
  aria-describedby="email-error"
/>
<p id="email-error" class="field__error">
  <span aria-hidden="true">⚠</span>
  Email: missing @ symbol — try "user@example.com"
</p>
```

---

## R8 — Dark mode is a separate color system, not an inversion.

Inverting light mode colors creates several problems: shadows disappear (black shadow invisible on dark), high-chroma colors become garish, text becomes too bright (pure white on pure black has too much contrast for comfort).

```css
/* Light mode accent — darker than base, pops on white */
--color-accent: oklch(57% 0.22 258);

/* Dark mode accent — lighter, same hue, reduced chroma */
[data-theme="dark"] --color-accent: oklch(73% 0.20 258);

/* Light mode shadows */
--shadow-md: 0 4px 8px oklch(0% 0 0 / 0.06), 0 12px 24px oklch(0% 0 0 / 0.08);

/* Dark mode: shadows invisible on dark backgrounds — use borders instead */
[data-theme="dark"] --shadow-md:
  0 0 0 1px var(--color-border),
  0 4px 24px oklch(0% 0 0 / 0.4);
```

See `recipes/add-dark-mode.md` for the full dark mode implementation.

---

## R9 — Use `color-mix()` for alpha variants. Never hardcode opacity values.

Hardcoded `rgba(hex, 0.1)` breaks dark mode, creates maintenance burden, and doesn't adapt to theme changes.

```css
/* Correct — relative to current token */
background: oklch(from var(--color-accent) l c h / 0.1);
border:     1px solid oklch(from var(--color-error) l c h / 0.4);

/* Or with color-mix() */
background: color-mix(in oklch, var(--color-accent) 10%, transparent);

/* Wrong — hardcoded opacity on specific color */
background: rgba(99, 102, 241, 0.1);    /* breaks in dark mode */
background: oklch(65% 0.22 258 / 0.1); /* not tied to token — won't update */
```

---

## R10 — Define color strategy before picking colors.

Choosing colors without a strategy leads to inconsistent application. Pick one strategy and commit.

| Strategy | Surface share | When |
|---|---|---|
| **Restrained** | Tinted neutrals + accent ≤ 10% | SaaS, B2B, product default |
| **Committed** | One saturated color 30–60% | Identity-led pages, brand heroes |
| **Full palette** | 3–4 color roles, each deliberate | Campaigns, data viz products |
| **Drenched** | Surface IS the color | Campaign heroes, editorial splashes |

**Restrained is not the default for everything.** A consumer product page benefits from Committed. A campaign should be Drenched. Only use Restrained when the content is the product.

---

## Banned Color Patterns

- Purple-to-indigo gradient on white background
- Neon outer glow shadows
- Pure `#000000` or `#ffffff` without hue tint
- Violet hero gradients
- `rgba(purple, 0.2)` blobs as the only decoration
- Gradient text (`background-clip: text`) — see `rules/03-typography.md` R9
- High-chroma colors at extreme lightness (L < 20% or L > 85%) with C > 0.15

---

## Acceptance Criteria

```
[ ] All color values use OKLCH — no hex, no rgb() in component CSS
[ ] All neutral values carry hue tint (chroma 0.005–0.018)
[ ] One accent hue — state variations use L/C changes, not H changes
[ ] Accent area ≤ 15% of visible screen
[ ] Text contrast ≥ 4.5:1 for body, ≥ 3:1 for large text/UI components
[ ] Color is never the only signal — icon/label/ARIA supplement color
[ ] Dark mode uses separate token values — not inversion
[ ] Alpha variants use oklch(from var(--token) l c h / α) pattern
[ ] No banned color patterns present
[ ] Color strategy defined (restrained / committed / full palette / drenched)
```

---

*Rule version: global-design-skill v1.0 — `rules/04-color.md`*
*Related: `tokens/tokens.css` color section, `tokens/tokens-dark.css`, `recipes/add-dark-mode.md`, `references/color-alchemy.md`*
