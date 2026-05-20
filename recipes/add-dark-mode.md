# Recipe — Add Dark Mode

> Dark mode is not "invert the colors." It is a separate visual system with different contrast relationships, saturation levels, and surface hierarchy. Done wrong, it looks like a broken site. Done right, it feels like the design was made for dark from the start.

---

## When to use

- Product has user preference for dark/light (developer tools, dashboards, IDEs)
- Users work at night or in low-light environments
- Accessibility requirement (some users require dark mode medically)
- Adding to an existing light-mode product

---

## The Core Rules

1. **Never invert — rebuild.** Dark backgrounds need different lightness, chroma, and opacity values.
2. **Reduce saturation in dark mode.** Colors that look good on white look garish on dark backgrounds. Lower chroma by 20–30%.
3. **Shadows disappear on dark.** Replace shadows with borders + surface layering.
4. **Text contrast is different.** Dark mode text is not `#ffffff` on `#000000`. Both extremes need tinting.
5. **Images need special treatment.** Photos look fine; pure white logos and icons need a tinted container.

---

## Step 1 — Token Architecture (One Source of Truth)

Never write two separate color declarations. Use CSS custom properties that switch at the root.

```css
/* ============================================
   BASE TOKENS — never change these
   ============================================ */
:root {
  /* Brand */
  --brand-accent:  oklch(65% 0.22 258);  /* electric blue */
  --brand-success: oklch(55% 0.18 145);
  --brand-warning: oklch(65% 0.18 75);
  --brand-error:   oklch(52% 0.22 25);

  /* Semantic tokens — assigned from base or theme below */
  /* (set in light mode by default) */
}

/* ============================================
   LIGHT MODE — default
   ============================================ */
:root {
  --color-base:        oklch(99% 0.005 258);  /* page background */
  --color-surface:     oklch(100% 0.003 258); /* card / panel */
  --color-surface-2:   oklch(96%  0.006 258); /* input bg, hover */
  --color-border:      oklch(90%  0.008 258);
  --color-text-primary:  oklch(15% 0.015 258);
  --color-text-secondary:oklch(35% 0.012 258);
  --color-text-muted:    oklch(52% 0.010 258);

  /* Accent at light-mode lightness */
  --color-accent:      oklch(55% 0.22 258);   /* slightly darker on white */
  --color-accent-bg:   oklch(95% 0.04 258);   /* accent tint backgrounds */
}

/* ============================================
   DARK MODE
   ============================================ */
.dark,
[data-theme="dark"] {
  --color-base:        oklch(10%  0.015 258);  /* near-black, blue tinted */
  --color-surface:     oklch(14%  0.012 258);  /* card / panel */
  --color-surface-2:   oklch(19%  0.010 258);  /* input bg, hover */
  --color-border:      oklch(26%  0.012 258 / 0.7);

  --color-text-primary:  oklch(95% 0.005 258);
  --color-text-secondary:oklch(72% 0.008 258);
  --color-text-muted:    oklch(50% 0.008 258);

  /* Accent: lighter on dark background */
  --color-accent:      oklch(70% 0.20 258);   /* brighter to maintain contrast */
  --color-accent-bg:   oklch(20% 0.06 258);   /* accent tint for dark surfaces */
}

/* ============================================
   SYSTEM PREFERENCE (no JS needed)
   ============================================ */
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    /* Same values as .dark above */
    --color-base:        oklch(10%  0.015 258);
    --color-surface:     oklch(14%  0.012 258);
    /* ... (repeat or use a shared @layer) */
  }
}
```

---

## Step 2 — Shadow System for Dark Mode

Shadows are invisible on dark backgrounds. Replace with surface + border layering.

```css
/* Light mode shadows */
:root {
  --shadow-sm: 0 1px 2px oklch(0% 0 0 / 0.05), 0 2px 4px oklch(0% 0 0 / 0.05);
  --shadow-md: 0 4px 8px oklch(0% 0 0 / 0.08), 0 12px 24px oklch(0% 0 0 / 0.1);
  --shadow-lg: 0 8px 16px oklch(0% 0 0 / 0.1), 0 24px 48px oklch(0% 0 0 / 0.15);
}

/* Dark mode: shadows use white light source + surface difference */
.dark {
  --shadow-sm: 0 0 0 1px var(--color-border);
  --shadow-md: 0 0 0 1px var(--color-border),
               0 4px 24px oklch(0% 0 0 / 0.4);
  --shadow-lg: 0 0 0 1px var(--color-border),
               0 8px 48px oklch(0% 0 0 / 0.6);
}
```

---

## Step 3 — Implement the Toggle

**Approach: class on `<html>` + localStorage persistence**

```html
<!-- In <head>, before any content renders — prevents flash -->
<script>
  const theme = localStorage.getItem('theme')
  const system = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
  document.documentElement.setAttribute('data-theme', theme ?? system)
</script>
```

```html
<!-- Toggle button -->
<button
  class="theme-toggle"
  aria-label="Toggle dark mode"
  onclick="toggleTheme()"
>
  <span class="theme-toggle__icon theme-toggle__icon--light" aria-hidden="true">☀</span>
  <span class="theme-toggle__icon theme-toggle__icon--dark"  aria-hidden="true">☽</span>
</button>
```

```js
function toggleTheme() {
  const current = document.documentElement.getAttribute('data-theme')
  const next = current === 'dark' ? 'light' : 'dark'
  document.documentElement.setAttribute('data-theme', next)
  localStorage.setItem('theme', next)
}

// Sync with system preference changes
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
  if (!localStorage.getItem('theme')) {
    // Only follow system if user hasn't made a manual choice
    document.documentElement.setAttribute('data-theme', e.matches ? 'dark' : 'light')
  }
})
```

```css
/* Show correct icon per mode */
[data-theme="light"] .theme-toggle__icon--dark  { display: none; }
[data-theme="dark"]  .theme-toggle__icon--light { display: none; }

/* Animate the toggle */
.theme-toggle {
  width: 40px;
  height: 40px;
  border-radius: var(--radius-md);
  background: transparent;
  border: 1px solid var(--color-border);
  cursor: pointer;
  display: grid;
  place-items: center;
  font-size: 1rem;
  color: var(--color-text-muted);
  transition: background 150ms, color 150ms;
}

.theme-toggle:hover {
  background: var(--color-surface-2);
  color: var(--color-text-primary);
}
```

**React / Next.js:**
```tsx
'use client'
import { useEffect, useState } from 'react'

export function ThemeToggle() {
  const [theme, setTheme] = useState<'light' | 'dark'>('light')

  useEffect(() => {
    const stored = localStorage.getItem('theme') as 'light' | 'dark' | null
    const system = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
    const initial = stored ?? system
    setTheme(initial)
    document.documentElement.setAttribute('data-theme', initial)
  }, [])

  function toggle() {
    const next = theme === 'dark' ? 'light' : 'dark'
    setTheme(next)
    document.documentElement.setAttribute('data-theme', next)
    localStorage.setItem('theme', next)
  }

  return (
    <button onClick={toggle} aria-label="Toggle dark mode" className="theme-toggle">
      {theme === 'dark' ? '☀' : '☽'}
    </button>
  )
}
```

---

## Step 4 — Handle Images and Logos

**Problem:** Dark logos on a dark background disappear. White logos on a light background disappear.

```css
/* Light-mode logo: dark version */
.logo-dark-mode  { display: none; }
.logo-light-mode { display: block; }

[data-theme="dark"] .logo-dark-mode  { display: block; }
[data-theme="dark"] .logo-light-mode { display: none; }
```

**Alternative: CSS filter for simple icons:**
```css
/* Only for monochrome SVG icons — not photos */
[data-theme="dark"] .icon-auto {
  filter: invert(1) hue-rotate(180deg);
}
```

**Photos:** Photos generally look fine in both modes. No treatment needed unless the photo has a white background.

```css
/* Photo with white background: add a subtle inset border */
[data-theme="dark"] .photo-white-bg {
  outline: 1px solid var(--color-border);
  border-radius: var(--radius-md);
}
```

---

## Step 5 — Audit Every Component

Run through all components and verify they use tokens (not hardcoded values):

```bash
# Find any hardcoded color values (should return 0 results after migration)
grep -r "#[0-9a-fA-F]\{3,6\}\|rgb\|rgba\|hsl\|hwb" src/ --include="*.css" --include="*.tsx" --include="*.ts"
```

**Common missed spots:**
- SVG `fill` and `stroke` colors (use `currentColor` or CSS variables)
- `box-shadow` with hardcoded `rgba()` values
- `border` with hardcoded hex
- `background-image: linear-gradient(...)` with hardcoded colors
- Third-party component overrides

```css
/* SVG icons: always use currentColor */
.icon svg { fill: currentColor; }

/* Or directly in SVG */
<svg fill="currentColor" stroke="currentColor">
```

---

## Step 6 — Transition Between Modes

```css
/* Smooth transition when toggling (not on initial load) */
.theme-transition * {
  transition:
    background-color 250ms cubic-bezier(0.4, 0, 0.2, 1),
    border-color     250ms cubic-bezier(0.4, 0, 0.2, 1),
    color            150ms cubic-bezier(0.4, 0, 0.2, 1) !important;
}
```

```js
// Add transition class, remove after animation completes
function toggleTheme() {
  document.documentElement.classList.add('theme-transition')
  // ... toggle logic
  setTimeout(() => {
    document.documentElement.classList.remove('theme-transition')
  }, 300)
}
```

**Note:** Do NOT add `transition` to all CSS properties by default — only add the class during the toggle event.

---

## Step 7 — Dark Mode for Specific Third-Party Libraries

**Charts (Recharts / Nivo):**
```tsx
const chartColors = {
  grid: 'var(--color-border)',
  text: 'var(--color-text-muted)',
  tooltip: {
    background: 'var(--color-surface)',
    border:     'var(--color-border)',
    text:       'var(--color-text-primary)',
  }
}
```

**Code blocks (Prism / Shiki):**
```css
/* Override code block theme variables */
[data-theme="dark"] .code-block {
  --code-bg:      oklch(12% 0.01 258);
  --code-border:  oklch(22% 0.012 258);
  --code-string:  oklch(72% 0.18 145);
  --code-keyword: oklch(72% 0.18 258);
  --code-comment: oklch(45% 0.005 258);
}
```

---

## Acceptance Criteria

```
[ ] No hardcoded color values in CSS/TSX — all use tokens
[ ] All tokens switch correctly in dark mode (visual audit each component)
[ ] Dark mode activates on system preference without JS flash
[ ] Dark mode preference persists across page reloads (localStorage)
[ ] Toggle button shows correct icon per current mode
[ ] Contrast ratios pass WCAG AA in BOTH modes
[ ] Shadows visible in both modes (surface layering for dark)
[ ] Logos/icons have dark-mode variants or use currentColor
[ ] Transition animation smooth (no jarring flash)
[ ] No element becomes invisible in either mode (audit all surfaces)
[ ] Third-party components (charts, code blocks) styled for both modes
[ ] prefers-reduced-motion: no transition animation on toggle
```

---

*Recipe version: global-design-skill v1.0 — `recipes/add-dark-mode.md`*
*Related: `references/color-alchemy.md`, `rules/02-layout-and-grid.md`, `rules/04-color.md`*
