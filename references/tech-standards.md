# Technology Standards (2025–2026)

> Full code reference for the stack standards summarized in `SKILL.md` → "Technology Standards". Use these — not legacy alternatives.

### CSS

```css
/* File: app/globals.css (or styles/tokens.css) */

/* OKLCH for all colors */
--color-accent: oklch(65% 0.22 258);
--color-base:   oklch(9%  0.012 258);

/* Animate custom properties via @property */
@property --gradient-angle {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}

/* Native nesting */
.card {
  background: var(--color-surface);
  &:hover { background: var(--color-surface-2); }
  @media (min-width: 768px) { display: flex; }
}

/* Popover API — no JS needed for basic dropdowns */
[popover] {
  opacity: 0; transform: scale(0.95);
  transition: opacity 0.2s, transform 0.2s,
              display 0.2s allow-discrete,
              overlay 0.2s allow-discrete;
}
[popover]:popover-open { opacity: 1; transform: scale(1); }
@starting-style { [popover]:popover-open { opacity: 0; transform: scale(0.95); } }

/* Scroll-driven animations — no JS for simple reveals */
@keyframes reveal {
  from { opacity: 0; transform: translateY(1.5rem); }
  to   { opacity: 1; transform: none; }
}
.card {
  animation: reveal linear both;
  animation-timeline: view();
  animation-range: entry 0% entry 40%;
}

/* Dialog native transition */
dialog:open { opacity: 1; transform: scaleY(1); }
dialog {
  opacity: 0; transform: scaleY(0);
  transition: opacity 0.2s, transform 0.2s,
              overlay 0.2s allow-discrete, display 0.2s allow-discrete;
}
@starting-style { dialog:open { opacity: 0; transform: scaleY(0); } }
```

### Tailwind v4

```css
/* File: app/globals.css */

/* No tailwind.config.js — everything in CSS */
@import "tailwindcss";

@theme {
  --color-brand:    oklch(65% 0.22 258);
  --font-display:   "Syne", "sans-serif";
  --breakpoint-3xl: 1920px;
}

/* Dark mode */
@custom-variant dark (&:is(.dark *));

/* shadcn/Radix theming layer */
@theme inline {
  --color-background: var(--background);
  --color-foreground: var(--foreground);
}
```

### React 19

```tsx
/* File: components/Input.tsx (any component file) */

/* ref as regular prop — no forwardRef needed */
function Input({ ref, ...props }: Props & { ref?: Ref<HTMLInputElement> }) {
  return <input ref={ref} {...props} />
}

/* Form state management */
const [state, action, isPending] = useActionState(serverAction, null)

/* Optimistic UI */
const [optimisticItems, addOptimistic] = useOptimistic(items)

/* Form status */
function Submit() {
  const { pending } = useFormStatus()
  return <button disabled={pending}>{pending ? 'Saving...' : 'Save'}</button>
}

/* Async form actions */
<form action={async (formData) => {
  addOptimistic(newItem)
  await createItem(formData)
}}>
```

### Next.js 15

```tsx
/* File: app/[id]/page.tsx (Server Component) */

/* Async APIs — must await (breaking change from v14) */
const cookieStore = await cookies()
const headersList = await headers()
const { id } = await params
const { q } = await searchParams

/* fetch: no-store by default (breaking — v14 was force-cache) */
fetch(url, { next: { revalidate: 3600 } })  /* explicit cache */

/* New "use cache" directive */
async function getData() {
  "use cache"
  cacheLife('minutes')
  return db.query(...)
}
```

### Motion (`motion/react`)

```tsx
/* File: components/Section.tsx */

import { motion, AnimatePresence, useScroll, useAnimate, useInView } from 'motion/react'
import { animate, spring } from 'motion'

/* Scroll-triggered with useInView */
function Section() {
  const [scope, animate] = useAnimate()
  const isInView = useInView(scope, { once: true })

  useEffect(() => {
    if (isInView) animate('li', { opacity: 1, y: 0 }, { delay: stagger(0.08) })
  }, [isInView])

  return <ul ref={scope}><li /><li /></ul>
}

/* View Transitions */
import { animateView } from 'motion'
```

### GSAP

```tsx
/* File: components/Hero.tsx */

import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import { useGSAP } from '@gsap/react'

gsap.registerPlugin(ScrollTrigger, useGSAP)

function Hero() {
  const container = useRef(null)

  const { contextSafe } = useGSAP(() => {
    gsap.from('.title', { y: 50, autoAlpha: 0, duration: 0.8, ease: 'power3.out' })
    gsap.to('.bg', {
      xPercent: -10,
      scrollTrigger: { trigger: container.current, start: 'top top', end: 'bottom top', scrub: 1 }
    })
  }, { scope: container })

  const handleClick = contextSafe(() => gsap.to('.cta', { scale: 1.05, yoyo: true, repeat: 1 }))

  return <section ref={container}>...</section>
}
```

### TypeScript 5

```typescript
/* File: lib/tokens.ts (or any .ts / .tsx file) */

/* satisfies — validate without widening */
const tokens = {
  accent: 'oklch(65% 0.22 258)',
  muted:  'oklch(55% 0.01 258)',
} satisfies Record<string, string>

/* const type params — literal inference */
function variants<const T extends string[]>(v: T): T { return v }
const v = variants(['primary', 'ghost'])  /* → readonly ["primary", "ghost"] */

/* Template literal types for tokens */
type SpaceToken  = `--space-${1|2|3|4|5|6|8|10|12|16|20|24|32}`
type ColorToken  = `--color-${string}`
```
