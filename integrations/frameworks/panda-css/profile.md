# Panda CSS — Framework Profile

> Panda CSS (by the Chakra UI team) is a type-safe, zero-runtime CSS-in-JS framework for React and Next.js. Styles are co-located with components, tokens are fully typed with TypeScript autocomplete, and the output is static CSS — no runtime overhead. Best for teams building design systems where token contracts must be enforced at compile time.

**Auto-detected via:** `"@pandacss/dev"` in package.json  
**Install:** `npm install -D @pandacss/dev && npx panda init --postcss`

---

## When to Use Panda CSS

- TypeScript-first React/Next.js projects requiring type-safe design tokens
- Teams building a component library where token misuse should be a compile error
- Projects moving away from runtime CSS-in-JS (Styled Components, Emotion) for performance
- Design systems where token contracts between design and dev must be machine-enforced

**Do not choose Panda CSS when:** the team is not using TypeScript, the project is vanilla HTML, or fast setup is more important than type safety.

---

## Setup

```typescript
// panda.config.ts
import { defineConfig } from '@pandacss/dev'

export default defineConfig({
  preflight: true,
  include: ['./src/**/*.{ts,tsx}'],
  exclude: [],
  outdir: 'styled-system',
  theme: {
    tokens: {
      colors: {
        accent:      { value: 'oklch(57% 0.22 258)' },
        surface:     { value: 'oklch(100% 0.003 258)' },
        textPrimary: { value: 'oklch(18% 0.02 258)' },
        textMuted:   { value: 'oklch(45% 0.02 258)' },
        border:      { value: 'oklch(88% 0.01 258)' },
      },
      fontSizes: {
        hero:    { value: 'clamp(3.5rem, 8vw + 1rem, 12rem)' },
        section: { value: 'clamp(2rem, 4vw + 1rem, 3.5rem)' },
        body:    { value: '1rem' },
      },
      radii: {
        sm: { value: '8px' },
        md: { value: '12px' },
        lg: { value: '16px' },
      },
      easings: {
        smooth: { value: 'cubic-bezier(0.25, 0.1, 0.25, 1)' },
        spring: { value: 'cubic-bezier(0.16, 1, 0.3, 1)' },
      },
    },
  },
})
```

```json
// package.json — add prepare script
{
  "scripts": {
    "prepare": "panda codegen"
  }
}
```

---

## OKLCH Adaptation

All OKLCH values are defined once in `panda.config.ts`. Components reference tokens by name — no raw values in component code:

```tsx
import { css } from '../styled-system/css'

// Type-safe — 'accent' autocompletes from your token definition
const heroStyle = css({
  fontSize: 'hero',
  color: 'textPrimary',
  background: 'surface',
  borderRadius: 'md',
})

// Semantic recipes for repeated patterns
import { cva } from '../styled-system/css'

const button = cva({
  base: {
    borderRadius: 'md',
    fontSize: 'body',
    cursor: 'pointer',
  },
  variants: {
    intent: {
      primary:   { background: 'accent', color: 'surface' },
      secondary: { border: '2px solid token(colors.accent)', color: 'accent' },
    },
  },
})
```

---

## Typography

Font sizes are type-checked through the token system. `clamp()` is defined once in the config, used everywhere via token name:

```tsx
// hero, section, body are token names — TypeScript autocompletes them
<h1 className={css({ fontSize: 'hero', lineHeight: '1.1' })}>
<h2 className={css({ fontSize: 'section', lineHeight: '1.2' })}>
<p  className={css({ fontSize: 'body', lineHeight: '1.65' })}>
```

---

## Animation with motion/react

Panda CSS handles static styles. Use `motion/react` for all animations — the two systems are fully compatible:

```tsx
import { motion } from 'motion/react'
import { css } from '../styled-system/css'

const cardStyle = css({
  borderRadius: 'lg',
  background: 'surface',
  border: '1px solid token(colors.border)',
})

<motion.div
  className={cardStyle}
  initial={{ opacity: 0, y: 16 }}
  whileInView={{ opacity: 1, y: 0 }}
  viewport={{ once: true }}
  transition={{ duration: 0.4, ease: 'easeOut' }}
>
```

---

## Banned Patterns (Panda CSS-Specific)

| Banned | Problem | Replacement |
|---|---|---|
| Raw OKLCH in `css()` calls: `{ color: 'oklch(57% 0.22 258)' }` | Bypasses token system | Use `{ color: 'accent' }` |
| Dynamic template literal class generation | Panda can't statically analyze | Use `cva` recipes with explicit variants |
| Mixing Panda CSS with Tailwind | Class conflicts, bloated output | Choose one |
| Skipping `panda codegen` after token changes | Type definitions go stale | Run `panda codegen` in `prepare` script |

---

## Checklist

- [ ] `panda.config.ts` has all OKLCH colors as named tokens
- [ ] `clamp()` font sizes defined as tokens, not inline values
- [ ] `prepare` script runs `panda codegen`
- [ ] No raw OKLCH values in component `css()` calls — all through token names
- [ ] `motion/react` used for animations
- [ ] No Tailwind installed alongside Panda CSS
- [ ] TypeScript autocomplete working for token names in `css()` calls
