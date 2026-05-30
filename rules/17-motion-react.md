# Rule 17 — Animation with motion/react

> Motion is now a standalone library (formerly Framer Motion). The package is `motion`, the React import is `motion/react`. All `framer-motion` imports are a banned pattern — the package is deprecated. This rule covers every animation pattern you need for production UI: entry, scroll-triggered, scroll-linked, exit, layout, and stagger.

---

## Import — The Only Correct Form

```tsx
// CORRECT
import { motion, AnimatePresence, useScroll, useTransform,
         useReducedMotion, useInView, stagger, animate } from 'motion/react'

// BANNED — package is deprecated
import { motion } from 'framer-motion'
```

Install:
```bash
npm install motion
```

---

## R1 — Every element must enter. Nothing appears statically.

Use `initial` + `animate` on `motion.*` elements. Entry should be fast (200–400ms) with a spring or ease-out curve.

```tsx
// Basic fade-up entry
<motion.div
  initial={{ opacity: 0, y: 16 }}
  animate={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.35, ease: [0.25, 0.1, 0.25, 1] }}
>
  {children}
</motion.div>
```

---

## R2 — Scroll-triggered: use whileInView

For elements that animate when they enter the viewport. Set `once: true` so the animation only plays once.

```tsx
<motion.section
  initial={{ opacity: 0, y: 24 }}
  whileInView={{ opacity: 1, y: 0 }}
  viewport={{ once: true, margin: '-80px' }}
  transition={{ duration: 0.5, ease: 'easeOut' }}
>
  {children}
</motion.section>
```

**`margin: '-80px'`** fires the animation slightly before the element fully enters — avoids a jarring pop-in at the bottom of the screen.

---

## R3 — Staggered children

Use `variants` + `staggerChildren` to stagger a list. Stagger delay: 60–120ms per item.

```tsx
const containerVariants = {
  hidden: {},
  visible: {
    transition: {
      staggerChildren: 0.08,
    },
  },
}

const itemVariants = {
  hidden: { opacity: 0, y: 16 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.4, ease: 'easeOut' } },
}

// Parent
<motion.ul
  variants={containerVariants}
  initial="hidden"
  whileInView="visible"
  viewport={{ once: true }}
>
  {items.map((item) => (
    <motion.li key={item.id} variants={itemVariants}>
      {item.content}
    </motion.li>
  ))}
</motion.ul>
```

---

## R4 — Scroll-linked animations: useScroll + useTransform

For parallax or progress-linked effects. Only animate `transform` and `opacity` — never width, height, or padding (causes reflow).

```tsx
import { useScroll, useTransform, motion } from 'motion/react'

function ParallaxHero() {
  const { scrollYProgress } = useScroll()
  const y = useTransform(scrollYProgress, [0, 1], ['0%', '30%'])

  return (
    <motion.div style={{ y }}>
      <img src="/hero.webp" alt="Hero" />
    </motion.div>
  )
}
```

**Scoped scroll** (relative to a container, not the page):
```tsx
const ref = useRef(null)
const { scrollYProgress } = useScroll({ target: ref, offset: ['start end', 'end start'] })
```

---

## R5 — Exit animations: AnimatePresence

Wrap conditionally-rendered components in `AnimatePresence`. The `exit` prop defines the out-state.

```tsx
<AnimatePresence>
  {isOpen && (
    <motion.div
      key="modal"
      initial={{ opacity: 0, scale: 0.96 }}
      animate={{ opacity: 1, scale: 1 }}
      exit={{ opacity: 0, scale: 0.96 }}
      transition={{ duration: 0.2, ease: 'easeOut' }}
    >
      <Modal />
    </motion.div>
  )}
</AnimatePresence>
```

**Page transitions** — wrap route output in `AnimatePresence`:
```tsx
<AnimatePresence mode="wait">
  <motion.main
    key={pathname}
    initial={{ opacity: 0, y: 8 }}
    animate={{ opacity: 1, y: 0 }}
    exit={{ opacity: 0, y: -8 }}
    transition={{ duration: 0.25 }}
  >
    {children}
  </motion.main>
</AnimatePresence>
```

`mode="wait"` ensures the exit animation completes before the enter animation starts.

---

## R6 — Layout animations

Add `layout` to animate position/size changes automatically. Use `layoutId` to animate an element between two DOM positions (e.g., a selected tab indicator).

```tsx
// Animated tab underline
{tabs.map((tab) => (
  <button key={tab.id} onClick={() => setActive(tab.id)}>
    {tab.label}
    {active === tab.id && (
      <motion.div layoutId="tab-underline" className="tab-indicator" />
    )}
  </button>
))}
```

---

## R7 — Transitions: springs vs easing

| Use case | Type | Example |
|---|---|---|
| Interactive UI (buttons, modals, tabs, drag) | Spring | `type: 'spring', stiffness: 400, damping: 30` |
| Decorative / sequential (scroll reveals, page transitions) | Easing | `ease: 'easeOut', duration: 0.4` |
| Entry animations | Easing | `ease: [0.25, 0.1, 0.25, 1]` |

```tsx
// Spring — feels physical, responds to interruption
transition={{ type: 'spring', stiffness: 400, damping: 30 }}

// Ease — predictable, controlled
transition={{ duration: 0.35, ease: [0.25, 0.1, 0.25, 1] }}

// Tailwind spring utility (motion v12+)
<div className="transition-transform duration-500 ease-spring-soft">
```

---

## R8 — Accessibility: useReducedMotion

Always respect the OS "Reduce Motion" setting. Wrap all decorative animations.

```tsx
import { useReducedMotion } from 'motion/react'

function AnimatedCard({ children }: { children: React.ReactNode }) {
  const shouldReduceMotion = useReducedMotion()

  return (
    <motion.div
      initial={{ opacity: 0, y: shouldReduceMotion ? 0 : 16 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true }}
      transition={{ duration: shouldReduceMotion ? 0.01 : 0.4 }}
    >
      {children}
    </motion.div>
  )
}
```

Global pattern using CSS (works without JS):
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## R9 — Hover and tap interactions

```tsx
<motion.button
  whileHover={{ scale: 1.03 }}
  whileTap={{ scale: 0.97 }}
  transition={{ type: 'spring', stiffness: 400, damping: 30 }}
>
  Get Started
</motion.button>
```

**Card hover — lift effect:**
```tsx
<motion.div
  whileHover={{ y: -4, boxShadow: '0 12px 40px oklch(0% 0 0 / 0.15)' }}
  transition={{ type: 'spring', stiffness: 300, damping: 25 }}
>
  <Card />
</motion.div>
```

---

## R10 — Performance rules

| Rule | Detail |
|---|---|
| Only animate `transform` + `opacity` in scroll-linked effects | Keeps animation on GPU thread |
| Never animate `width`, `height`, `padding`, `margin` | Triggers layout recalculation |
| Use `will-change: transform` sparingly | Only on elements that animate continuously |
| Stagger max 12 items | Beyond 12, aggregate delay becomes noticeable |
| Test on low-end mobile | Use Chrome DevTools CPU throttle 4x |

---

## R11 — Scroll-spy & sticky nav: read live positions, don't pin tall blocks

Two scroll-driven bugs from a real catalog redesign (`redesigns/bestseotools/CASE-STUDY.md`). Framework-agnostic — applies to vanilla JS and React scroll handlers alike.

**Scroll-spy must read live geometry, not cached offsets.** Highlighting the active section by comparing `scrollY` to a **cached** `offsetTop` breaks the moment page height changes — lazy-loaded images/media push sections down, the cache goes stale, and the active item **jumps back and forth** instead of advancing in order. Read the current position each frame:

```js
// rAF-throttled scroll handler
let current = sections[0];
for (const s of sections) {
  if (s.getBoundingClientRect().top <= navHeight + 24) current = s; else break; // DOM order → early-break is cheap
}
setActive(current.id);
```

`getBoundingClientRect()` is always current; the early `break` keeps it to a few reads per frame. Don't auto-scroll the active item's *page* position from a scroll handler (feedback loop) — only scroll the nav strip horizontally.

**A sticky element can only pin what's slim.** `position: sticky; top: 0` on a *tall* block (e.g. a grouped category nav, ~750px) pins the whole thing and covers the viewport, so it has to collapse the instant it sticks. Delaying the collapse just keeps the tall block pinned. Instead: let the **expanded** block scroll away in flow, and make only the **compact** bar sticky — switch after the expanded block has scrolled past, and compensate the height change with a spacer so content doesn't jump.

```css
/* expanded = in normal flow (scrolls away); only the compact bar sticks */
@media (min-width: 1024px){ .nav:not(.nav-compact){ position: relative } }
.nav.nav-compact{ position: sticky; top: 0 }
```

---

## Banned Patterns

```tsx
// BANNED — deprecated package
import { motion } from 'framer-motion'

// BANNED — animate layout properties
animate={{ width: '100%', height: 'auto' }}

// BANNED — transition: all equivalent
transition={{ duration: 0.3 }} // when applied to layout-triggering properties

// BANNED — multiple simultaneous pulse animations
<motion.div animate={{ scale: [1, 1.05, 1] }} transition={{ repeat: Infinity }} />
<motion.div animate={{ scale: [1, 1.05, 1] }} transition={{ repeat: Infinity }} />

// BANNED — stagger > 120ms on more than 6 items (cumulative delay > 720ms)
staggerChildren: 0.15 // on 10 items = 1.5s before last item enters
```

---

## motion/react v12 — New Features (2026)

- **OKLCH color support** — animate between OKLCH values natively: `animate={{ color: 'oklch(60% 0.2 240)' }}`
- **`layoutAnchor`** — custom anchor point for layout animations
- **`layout="x"` / `layout="y"`** — axis-locked layout animations
- **`skipInitialAnimation`** in `useSpring` — skip the first render animation
- **`scroll()` function** — direct scroll-linked animation without hooks:

```tsx
import { animate, scroll } from 'motion/react'

scroll(
  animate('.progress-bar', { scaleX: [0, 1] }),
  { axis: 'y' }
)
```
