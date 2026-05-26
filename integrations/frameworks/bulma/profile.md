# Bulma 1.0 — Framework Profile

> Bulma is a modern CSS-only framework — zero JavaScript. Version 1.0 (released March 2025) rewrote the entire variable system to CSS custom properties. Best for vanilla HTML projects, static sites, and projects where JS bundle size is constrained.

**Auto-detected via:** `"bulma"` in package.json  
**Install:** `npm install bulma`  
**CDN:** `<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@1.0/css/bulma.min.css">`

---

## When to Use Bulma

- Vanilla HTML/CSS projects with no framework or build step
- Static site generators (Hugo, Jekyll, Eleventy)
- Developers who want readable, English-like class names over utility classes
- Projects where zero JavaScript dependency is a hard requirement
- Landing pages and marketing sites that don't need React

**Do not choose Bulma when:** you need interactive JS components (modals, dropdowns), you're in a React/Next.js project, or you need a large component library.

---

## OKLCH Adaptation

Bulma 1.0 uses CSS custom properties throughout. Override in `:root`:

```css
@import 'bulma/css/bulma.css';

:root {
  --bulma-primary:        oklch(57% 0.22 258);
  --bulma-primary-light:  oklch(92% 0.06 258);
  --bulma-primary-dark:   oklch(38% 0.20 258);
  --bulma-background:     oklch(100% 0.003 258);
  --bulma-text:           oklch(18% 0.02 258);
  --bulma-text-light:     oklch(45% 0.02 258);
  --bulma-border:         oklch(88% 0.01 258);
  --bulma-radius:         var(--radius-md, 12px);
  --bulma-radius-large:   var(--radius-lg, 16px);
  --bulma-radius-small:   var(--radius-sm, 8px);
}
```

---

## Typography

Bulma uses `em` units. Override hero `.title` sizes with `clamp()`:

```css
.hero .title.is-1 {
  font-size: clamp(2.5rem, 6vw + 1rem, 5rem);
  line-height: 1.1;
}
.hero .title.is-2 {
  font-size: clamp(2rem, 4vw + 1rem, 4rem);
  line-height: 1.15;
}
/* Body text — Bulma default is 1em = 16px — acceptable */
/* Ensure inputs don't trigger iOS zoom */
.input, .textarea, .select select {
  font-size: 1rem;
}
```

---

## Animation

Bulma has zero built-in JavaScript animations. Use `motion/react` for interactive states, or CSS `@starting-style` for pure CSS entry animations:

```css
/* Pure CSS entry — no JS needed */
.card {
  transition: opacity 0.3s ease, transform 0.3s ease;

  @starting-style {
    opacity: 0;
    transform: translateY(12px);
  }
}
```

For interactive React components using Bulma classes with motion/react:
```tsx
import { motion } from 'motion/react'

<motion.div
  className="card"
  initial={{ opacity: 0, y: 16 }}
  whileInView={{ opacity: 1, y: 0 }}
  viewport={{ once: true }}
  transition={{ duration: 0.4, ease: 'easeOut' }}
>
```

---

## Banned Patterns (Bulma-Specific)

| Banned | Problem | Replacement |
|---|---|---|
| `.is-primary` without OKLCH override | Default blue | Set `--bulma-primary` first |
| `.has-text-grey-light` | Often fails contrast | Explicit OKLCH value |
| `.has-background-light` | Hex default | Override `--bulma-background` |
| Bulma's default font stack (BlinkMacSystemFont) | Generic | Set `--bulma-family-primary` to your font |
| Nested `.columns` more than 2 levels | Layout confusion | Flatten structure |

---

## Checklist

- [ ] `--bulma-primary` overridden with OKLCH token
- [ ] `--bulma-background` and `--bulma-text` use OKLCH
- [ ] `.title.is-1` / `.is-2` use `clamp()`
- [ ] No `.has-text-grey-light` — replaced with OKLCH value
- [ ] Inputs have `font-size: 1rem` (iOS zoom prevention)
- [ ] CSS `@starting-style` used for entry animations (no JS needed)
- [ ] motion/react used only when React is in the stack
