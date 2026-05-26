# Open Props — Framework Profile

> Open Props (by Adam Argyle, Google Chrome DevRel) is a CSS custom properties token library — not a component framework. It ships 300+ design tokens including OKLCH-native color palettes, fluid typography, easing functions, and animation keyframes. Works with any stack as a token foundation layer.

**Auto-detected via:** `"open-props"` in package.json  
**Install:** `npm install open-props`  
**CDN:** `@import "https://unpkg.com/open-props"`

---

## When to Use Open Props

- Building a custom design system from tokens up (no component opinions)
- Augmenting any other framework with a consistent token layer
- Projects where Tailwind/Bootstrap feel like too much framework opinion
- Designers who want OKLCH colors, fluid type, and spring easings ready-made
- Vanilla CSS projects that want a professional token system without a build step

**Do not choose Open Props as your only tool when:** you need pre-built interactive components — pair it with a component library or build your own.

---

## OKLCH Adaptation

Open Props already ships OKLCH color tokens (`--pink-5`, `--blue-7`, etc.). Layer your project tokens on top:

```css
@import "open-props/style";      /* core tokens */
@import "open-props/colors";     /* oklch() color palette */
@import "open-props/sizes";      /* spacing scale */
@import "open-props/fonts";      /* fluid font sizes */
@import "open-props/easings";    /* spring and easing functions */

:root {
  /* Override or extend with project-specific tokens */
  --color-accent:   oklch(57% 0.22 258);
  --color-surface:  oklch(100% 0.003 258);
  --color-text:     oklch(18% 0.02 258);

  /* Map Open Props easings to global-design-skill tokens */
  --ease-smooth:  var(--ease-3);
  --ease-spring:  var(--ease-spring-3);
  --ease-bounce:  var(--ease-elastic-3);
}
```

**Never use Open Props color tokens directly in components** — always map through your project tokens first. This ensures your OKLCH values stay consistent even if Open Props changes.

---

## Typography

Open Props ships fluid font sizes that already use `clamp()`:

```css
/* Open Props fluid scale — already clamp() */
--font-size-0:  clamp(.75rem, 2vw, 1rem);
--font-size-1:  clamp(1rem,   2vw, 1.1rem);
--font-size-6:  clamp(2.5rem, 6vw, 4rem);
--font-size-7:  clamp(3rem,   7vw, 5rem);
--font-size-8:  clamp(3.75rem, 8vw, 6.5rem);
```

Map to global-design-skill typography tokens:
```css
:root {
  --text-hero:    var(--font-size-8);   /* clamp(3.75rem, 8vw, 6.5rem) */
  --text-section: var(--font-size-6);   /* clamp(2.5rem, 6vw, 4rem) */
  --text-body:    var(--font-size-1);   /* 1rem min */
}
```

---

## Animation

Open Props ships animation keyframes and easing tokens — combine with `motion/react`:

```css
/* Use Open Props keyframes in CSS */
.card {
  animation: var(--animation-fade-in);
  animation-duration: 0.4s;
  animation-timing-function: var(--ease-3);
}
```

```tsx
// Use Open Props easing in motion/react
import { motion } from 'motion/react'

<motion.div
  initial={{ opacity: 0, y: 16 }}
  animate={{ opacity: 1, y: 0 }}
  transition={{
    duration: 0.4,
    ease: [0.25, 0.1, 0.25, 1] // var(--ease-3) value
  }}
/>
```

---

## Banned Patterns (Open Props-Specific)

| Banned | Problem | Replacement |
|---|---|---|
| Using `--pink-5` directly in components | Breaks token abstraction | Map to `--color-accent` first |
| Importing all of Open Props | Unused tokens add weight | Import only needed modules |
| Mixing Open Props font scale with Tailwind font scale | Conflicting values | Use one scale only |

---

## Checklist

- [ ] Open Props imported modularly (only needed files)
- [ ] Project tokens defined that map from Open Props tokens
- [ ] `--ease-smooth` and `--ease-spring` mapped to Open Props equivalents
- [ ] Fluid font sizes mapped to global-design-skill typography tokens
- [ ] No Open Props color tokens used directly in components (mapped through project tokens)
