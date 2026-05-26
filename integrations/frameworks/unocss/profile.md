# UnoCSS — Framework Profile

> UnoCSS is an atomic CSS engine — the architecture behind Tailwind but faster, more configurable, and with a richer preset ecosystem. With `presetUno()`, all Tailwind class names work unchanged. Best for teams migrating from Tailwind or building monorepos where build speed matters.

**Auto-detected via:** `"unocss"` in package.json  
**Install:** `npm install -D unocss`

---

## When to Use UnoCSS

- Migrating a Tailwind project to a faster build engine (Tailwind class names work as-is)
- Monorepos where Tailwind's full rebuild is slow
- Projects needing custom atomic class generators (shortcuts, rules)
- Vue/Nuxt projects where UnoCSS has first-class integration
- Teams who want icon sets as CSS classes (`@unocss/preset-icons`)

**Do not choose UnoCSS when:** your team knows only Tailwind and the project is small — Tailwind v4 is fast enough and has wider community resources.

---

## Setup

```typescript
// uno.config.ts
import { defineConfig, presetUno } from 'unocss'

export default defineConfig({
  presets: [
    presetUno(), // Tailwind-compatible class names
  ],
  theme: {
    colors: {
      accent:  'oklch(57% 0.22 258)',
      surface: 'oklch(100% 0.003 258)',
      text:    'oklch(18% 0.02 258)',
      border:  'oklch(88% 0.01 258)',
    },
    borderRadius: {
      sm: '8px',
      md: '12px',
      lg: '16px',
    },
  },
})
```

```typescript
// vite.config.ts / next.config.ts
import UnoCSS from 'unocss/vite'
export default { plugins: [UnoCSS()] }
```

---

## OKLCH Adaptation

UnoCSS resolves colors through its theme config. All OKLCH values defined in `theme.colors` are available as utility classes:

```html
<!-- Uses oklch(57% 0.22 258) defined in theme -->
<div class="bg-accent text-surface">
<button class="bg-accent hover:bg-accent/90 text-surface rounded-md">
```

Arbitrary OKLCH values:
```html
<div class="bg-[oklch(57%_0.22_258)]">
```

**CSS custom properties in UnoCSS:**
```typescript
// uno.config.ts — output CSS variables
shortcuts: {
  'btn-primary': 'bg-accent text-surface rounded-md px-6 py-3 hover:bg-accent/90',
}
```

---

## Typography

UnoCSS supports arbitrary `clamp()` values natively:

```html
<h1 class="text-[clamp(3.5rem,8vw+1rem,12rem)] leading-[1.1]">
```

Or define in theme:
```typescript
theme: {
  fontSize: {
    hero:    ['clamp(3.5rem, 8vw + 1rem, 12rem)',    { lineHeight: '1.1' }],
    section: ['clamp(2rem,   4vw + 1rem, 3.5rem)',   { lineHeight: '1.2' }],
    body:    ['1rem',                                 { lineHeight: '1.65' }],
  },
}
```

Usage: `<h1 class="text-hero">`

---

## Banned Patterns (UnoCSS-Specific)

| Banned | Problem | Replacement |
|---|---|---|
| Dynamic class construction: `"text-" + color` | UnoCSS can't detect at build time | Use full class name `text-accent` |
| Mixing UnoCSS and Tailwind in same project | Class conflicts | Choose one |
| `presetWind()` + `presetUno()` together | Duplicate rules | Use `presetUno()` only for Tailwind compat |
| Inline arbitrary values for every property | Defeats the purpose of a theme | Define tokens in `uno.config.ts` |

---

## Checklist

- [ ] `uno.config.ts` has OKLCH color tokens in `theme.colors`
- [ ] `presetUno()` included for Tailwind class compatibility
- [ ] Hero font sizes defined in `theme.fontSize` with `clamp()`
- [ ] No dynamic class string construction
- [ ] `motion/react` used for animations — not UnoCSS animation utilities for complex interactions
- [ ] No Tailwind installed alongside UnoCSS
