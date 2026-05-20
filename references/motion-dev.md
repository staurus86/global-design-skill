# Reference — Motion Dev (React)

> `motion/react` hooks, scroll-triggered animations, AnimatePresence, layout animations, and GSAP integration for React 19 + Next.js 15. For CSS-native animation patterns, see `references/motion-systems.md`.

---

## Import Paths

```tsx
/* CORRECT — always motion/react */
import { motion, AnimatePresence, useScroll, useTransform, useInView, useAnimate, stagger } from 'motion/react'
import { animate, spring } from 'motion'

/* BANNED — old package name */
import { motion } from 'framer-motion'  // ❌
```

---

## Core API

### `motion` component

```tsx
/* Basic entrance animation */
<motion.div
  initial={{ opacity: 0, y: 16 }}
  animate={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
/>

/* Exit animation */
<motion.div
  exit={{ opacity: 0, scale: 0.95 }}
  transition={{ duration: 0.2, ease: [0.4, 0, 1, 1] }}
/>

/* Hover + tap */
<motion.button
  whileHover={{ scale: 1.02 }}
  whileTap={{ scale: 0.97 }}
  transition={{ duration: 0.15, ease: [0.4, 0, 0, 1] }}
/>
```

### Variants for reuse

```tsx
const fadeUp = {
  hidden:  { opacity: 0, y: 16 },
  visible: { opacity: 1, y: 0,  transition: { duration: 0.6, ease: [0.16, 1, 0.3, 1] } },
  exit:    { opacity: 0, y: -8, transition: { duration: 0.2, ease: [0.4, 0, 1, 1] } },
}

const staggerContainer = {
  hidden:  {},
  visible: { transition: { staggerChildren: 0.08, delayChildren: 0 } },
}

<motion.ul variants={staggerContainer} initial="hidden" animate="visible">
  {items.map(item => (
    <motion.li key={item.id} variants={fadeUp}>
      {item.label}
    </motion.li>
  ))}
</motion.ul>
```

---

## AnimatePresence

Use for components that mount/unmount — modals, toasts, route transitions, conditional renders.

```tsx
import { AnimatePresence, motion } from 'motion/react'

function Modal({ isOpen, onClose }: { isOpen: boolean; onClose: () => void }) {
  return (
    <AnimatePresence>
      {isOpen && (
        <motion.div
          key="modal-overlay"
          className="fixed inset-0 bg-black/50"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          transition={{ duration: 0.2 }}
          onClick={onClose}
        >
          <motion.dialog
            open
            className="modal"
            initial={{ opacity: 0, scale: 0.95, y: -8 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.95, y: -8 }}
            transition={{ duration: 0.3, ease: [0.16, 1, 0.3, 1] }}
            onClick={e => e.stopPropagation()}
          >
            {/* modal content */}
          </motion.dialog>
        </motion.div>
      )}
    </AnimatePresence>
  )
}
```

**Important:** `AnimatePresence` requires `key` on the direct child. Without `key`, exit animations don't trigger.

---

## useScroll + useTransform

For scroll-linked animations — progress bars, parallax, fade-on-scroll.

```tsx
import { useScroll, useTransform } from 'motion/react'

function ParallaxHero() {
  const { scrollY } = useScroll()
  const y = useTransform(scrollY, [0, 600], [0, -100])
  const opacity = useTransform(scrollY, [0, 300], [1, 0])

  return (
    <section className="relative">
      <motion.div
        className="hero-bg absolute inset-0"
        style={{ y }}
      />
      <motion.div
        className="hero-content"
        style={{ opacity }}
      >
        <h1>Headline</h1>
      </motion.div>
    </section>
  )
}
```

### Scroll progress for a specific element

```tsx
function FeatureSection({ children }: { children: React.ReactNode }) {
  const ref = useRef<HTMLDivElement>(null)
  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ['start end', 'end start'], // enter from bottom to exit from top
  })

  const opacity = useTransform(scrollYProgress, [0, 0.2, 0.8, 1], [0, 1, 1, 0])
  const scale = useTransform(scrollYProgress, [0, 0.2], [0.95, 1])

  return (
    <motion.section ref={ref} style={{ opacity, scale }}>
      {children}
    </motion.section>
  )
}
```

---

## useInView + useAnimate (stagger on scroll entry)

```tsx
import { useInView, useAnimate, stagger } from 'motion/react'
import { useEffect, useRef } from 'react'

function FeatureGrid({ features }: { features: Feature[] }) {
  const [scope, animate] = useAnimate()
  const isInView = useInView(scope, { once: true, margin: '-48px 0px' })

  useEffect(() => {
    if (isInView) {
      animate(
        '.feature-card',
        { opacity: [0, 1], y: [20, 0] },
        {
          duration: 0.6,
          ease: [0.16, 1, 0.3, 1],
          delay: stagger(0.08),
        }
      )
    }
  }, [isInView, animate])

  return (
    <ul ref={scope} className="feature-grid">
      {features.map(f => (
        <li key={f.id} className="feature-card" style={{ opacity: 0 }}>
          <h3>{f.title}</h3>
          <p>{f.description}</p>
        </li>
      ))}
    </ul>
  )
}
```

---

## Layout Animations

For animating layout changes — items reordering, list item add/remove, tabs switching.

```tsx
import { motion, AnimatePresence } from 'motion/react'

/* Smooth list reorder */
function SortableList({ items }: { items: Item[] }) {
  return (
    <ul>
      <AnimatePresence>
        {items.map(item => (
          <motion.li
            key={item.id}
            layout          /* animates position changes */
            layoutId={item.id}
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: 'auto' }}
            exit={{ opacity: 0, height: 0 }}
            transition={{ duration: 0.3, ease: [0.16, 1, 0.3, 1] }}
          >
            {item.label}
          </motion.li>
        ))}
      </AnimatePresence>
    </ul>
  )
}
```

```tsx
/* Animated tab underline — follows selected tab */
function Tabs({ tabs, selected, onChange }: TabsProps) {
  return (
    <div className="tabs">
      {tabs.map(tab => (
        <button
          key={tab.id}
          onClick={() => onChange(tab.id)}
          className="relative"
        >
          {tab.label}
          {selected === tab.id && (
            <motion.span
              layoutId="tab-underline"
              className="absolute bottom-0 inset-x-0 h-0.5 bg-accent"
              transition={{ duration: 0.25, ease: [0.16, 1, 0.3, 1] }}
            />
          )}
        </button>
      ))}
    </div>
  )
}
```

---

## `prefers-reduced-motion` in React

```tsx
import { useReducedMotion } from 'motion/react'

function AnimatedCard({ children }: { children: React.ReactNode }) {
  const reduced = useReducedMotion()

  return (
    <motion.div
      initial={{ opacity: 0, y: reduced ? 0 : 16 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{
        duration: reduced ? 0.15 : 0.6,
        ease: [0.16, 1, 0.3, 1],
      }}
    >
      {children}
    </motion.div>
  )
}
```

---

## GSAP with React 19 (`useGSAP`)

Use GSAP for complex timeline sequences, physics simulations, and ScrollTrigger. Always use the official `@gsap/react` hook — never manage GSAP instances manually in `useEffect`.

```tsx
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import { useGSAP } from '@gsap/react'
import { useRef } from 'react'

gsap.registerPlugin(ScrollTrigger, useGSAP)

function AnimatedSection() {
  const containerRef = useRef<HTMLDivElement>(null)

  const { contextSafe } = useGSAP(
    () => {
      /* Entrance timeline */
      const tl = gsap.timeline()
      tl.from('.section-eyebrow', { y: 20, opacity: 0, duration: 0.6, ease: 'power3.out' })
        .from('.section-heading', { y: 20, opacity: 0, duration: 0.8, ease: 'power3.out' }, '-=0.4')
        .from('.section-body', { y: 16, opacity: 0, duration: 0.6, ease: 'power3.out' }, '-=0.5')

      /* ScrollTrigger for feature cards */
      gsap.from('.feature-card', {
        y: 30,
        opacity: 0,
        stagger: 0.08,
        duration: 0.6,
        ease: 'power3.out',
        scrollTrigger: {
          trigger: '.feature-grid',
          start: 'top 80%',
          once: true,
        },
      })

      /* Parallax background */
      gsap.to('.section-bg', {
        yPercent: -10,
        ease: 'none',
        scrollTrigger: {
          trigger: containerRef.current,
          start: 'top bottom',
          end: 'bottom top',
          scrub: 1,
        },
      })
    },
    { scope: containerRef }
  )

  /* Safe click handler (GSAP context-aware) */
  const handleCTAClick = contextSafe(() => {
    gsap.to('.cta-btn', {
      scale: 1.05,
      duration: 0.1,
      yoyo: true,
      repeat: 1,
      ease: 'power2.inOut',
    })
  })

  return (
    <section ref={containerRef}>
      <div className="section-bg" />
      <span className="section-eyebrow">What we build</span>
      <h2 className="section-heading">Heading here</h2>
      <p className="section-body">Body text here</p>
      <div className="feature-grid">
        {/* feature cards */}
      </div>
      <button className="cta-btn" onClick={handleCTAClick}>
        Book a demo
      </button>
    </section>
  )
}
```

### GSAP `prefers-reduced-motion`

```tsx
const { contextSafe } = useGSAP(() => {
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches

  gsap.from('.hero-heading', {
    y: reduced ? 0 : 40,
    opacity: 0,
    duration: reduced ? 0.2 : 0.8,
    ease: 'power3.out',
  })
}, { scope: containerRef })
```

---

## React 19 Patterns

### Optimistic updates with animation

```tsx
import { useOptimistic } from 'react'
import { motion, AnimatePresence } from 'motion/react'

function LikeButton({ post }: { post: Post }) {
  const [optimisticLikes, addOptimistic] = useOptimistic(post.likes)

  async function handleLike() {
    addOptimistic(optimisticLikes + 1)
    await likePost(post.id)
  }

  return (
    <button onClick={handleLike}>
      <AnimatePresence mode="popLayout">
        <motion.span
          key={optimisticLikes}
          initial={{ y: -12, opacity: 0 }}
          animate={{ y: 0,  opacity: 1 }}
          exit={{ y: 12, opacity: 0 }}
          transition={{ duration: 0.15, ease: [0.16, 1, 0.3, 1] }}
        >
          {optimisticLikes}
        </motion.span>
      </AnimatePresence>
    </button>
  )
}
```

### Form pending state with animation

```tsx
import { useActionState, useFormStatus } from 'react'
import { motion } from 'motion/react'

function SubmitButton() {
  const { pending } = useFormStatus()

  return (
    <motion.button
      type="submit"
      disabled={pending}
      animate={{ opacity: pending ? 0.6 : 1 }}
      transition={{ duration: 0.15 }}
    >
      {pending ? 'Saving...' : 'Save changes'}
    </motion.button>
  )
}
```

---

## Motion Budget Enforcement in Components

```tsx
/* Design-system-level motion config — one source of truth */
export const motionConfig = {
  spring:   { ease: [0.16, 1, 0.3, 1]   as const, duration: 0.6 },
  smooth:   { ease: [0.25, 0.46, 0.45, 0.94] as const, duration: 0.3 },
  exit:     { ease: [0.4, 0, 1, 1]       as const, duration: 0.2 },
  micro:    { ease: [0.4, 0, 0, 1]       as const, duration: 0.12 },
} as const

export const fadeUp = {
  hidden:  { opacity: 0, y: 16 },
  visible: { opacity: 1, y: 0, transition: motionConfig.spring },
  exit:    { opacity: 0, y: -8, transition: motionConfig.exit },
}

export const fadeIn = {
  hidden:  { opacity: 0 },
  visible: { opacity: 1, transition: motionConfig.smooth },
  exit:    { opacity: 0, transition: motionConfig.exit },
}
```

---

*Reference version: global-design-skill v1.0 — `references/motion-dev.md`*
*Related: `rules/05-animation.md`, `references/motion-systems.md`, `skills/global-design/SKILL.md` §GSAP*
