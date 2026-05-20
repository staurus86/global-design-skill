# Recipe — Add Animations

> **Trigger:** Page feels flat and dead — elements appear statically on load, there are no micro-interactions, and the product feels inert. Or: animations were added hastily and now feel wrong.

---

## Diagnosis Checklist

```
[ ] All elements appear instantly at full opacity on load (no entrance animations)
[ ] Scroll sections appear without any reveal
[ ] Hover states: abrupt color changes with no transition
[ ] transition: all used anywhere
[ ] ease-in-out used anywhere
[ ] window.addEventListener('scroll') for animations
[ ] framer-motion (not motion/react) imported anywhere
[ ] Multiple pulse animations on the same page
[ ] No prefers-reduced-motion override
[ ] Modals/drawers appear without enter/exit transitions
[ ] Page feels uniformly paced — all sections same intensity
```

---

## Step 1 — Set the Motion Budget

Before any CSS, decide on the intensity level per section. Motion contrast creates rhythm.

```
Budget (1–10 scale per section):
  Hero:              6–7   (entrance sequence, stagger)
  Feature sections:  4–5   (scroll reveal, subtle hover)
  Stats/social:      3–4   (counter animation, fade-in)
  Data tables:       2–3   (hover state only)
  Footer:            1–2   (static or single fade)

Target motion intensity by page type:
  Marketing landing: max 7   SaaS product: max 5
  Admin / data:      max 3   Onboarding: max 6
  Error / 404:       max 2
```

---

## Step 2 — Set the Easing and Duration Tokens

These should already be in `tokens.css`. If not, add them:

```css
:root {
  /* Easing */
  --ease-spring: cubic-bezier(0.16, 1, 0.3, 1);      /* entering */
  --ease-smooth: cubic-bezier(0.25, 0.46, 0.45, 0.94); /* hover */
  --ease-exit:   cubic-bezier(0.4, 0, 1, 1);           /* closing */
  --ease-snappy: cubic-bezier(0.4, 0, 0, 1);           /* click feedback */

  /* Duration */
  --duration-instant: 80ms;   /* icon swap, badge */
  --duration-fast:    150ms;  /* hover, small state change */
  --duration-normal:  250ms;  /* enter/exit component */
  --duration-slow:    400ms;  /* modal, drawer */
  --duration-hero:    600ms;  /* hero entrance */
}
```

---

## Step 3 — Fix All Hover Transitions

Audit every interactive element. Replace `transition: all` and `ease-in-out`.

```css
/* Before — common antipatterns */
.btn:hover { transition: all 0.3s ease-in-out; }
.card:hover { transition: all 0.2s; }

/* After — specific properties, correct easing */
.btn {
  transition:
    background   var(--duration-fast)   var(--ease-smooth),
    box-shadow   var(--duration-normal) var(--ease-smooth),
    color        var(--duration-fast)   var(--ease-smooth);
}

.card {
  transition:
    transform  var(--duration-normal) var(--ease-spring),
    box-shadow var(--duration-normal) var(--ease-smooth);
}

.card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}

/* Navigation items */
.nav-item {
  transition:
    background var(--duration-fast) var(--ease-smooth),
    color      var(--duration-fast) var(--ease-smooth);
}

/* Icon buttons */
.icon-btn {
  transition:
    background  var(--duration-fast)    var(--ease-smooth),
    transform   var(--duration-instant) var(--ease-snappy),
    color       var(--duration-fast)    var(--ease-smooth);
}

.icon-btn:active { transform: scale(0.92); }
```

---

## Step 4 — Add Scroll Reveal

Replace any `window.addEventListener('scroll')` with `IntersectionObserver`.

```css
/* Elements start hidden */
.reveal {
  opacity: 0;
  transform: translateY(24px);
  transition:
    opacity   var(--duration-hero) var(--ease-spring),
    transform var(--duration-hero) var(--ease-spring);
}

.reveal.is-visible {
  opacity: 1;
  transform: translateY(0);
}

/* Stagger for lists */
.reveal-stagger > *:nth-child(1) { transition-delay: 0ms; }
.reveal-stagger > *:nth-child(2) { transition-delay: 80ms; }
.reveal-stagger > *:nth-child(3) { transition-delay: 160ms; }
.reveal-stagger > *:nth-child(4) { transition-delay: 240ms; }
.reveal-stagger > *:nth-child(5) { transition-delay: 320ms; }

@media (prefers-reduced-motion: reduce) {
  .reveal {
    opacity: 1;
    transform: none;
    transition: none;
  }
}
```

```js
// Single IntersectionObserver for all reveal elements
const revealObserver = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('is-visible')
      revealObserver.unobserve(entry.target)
    }
  })
}, { threshold: 0.1, rootMargin: '0px 0px -48px 0px' })

document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el))
```

**HTML usage:**

```html
<!-- Section with staggered reveal -->
<section>
  <h2 class="reveal">Why teams choose us</h2>
  <div class="feature-grid reveal-stagger">
    <div class="feature-card reveal">...</div>
    <div class="feature-card reveal">...</div>
    <div class="feature-card reveal">...</div>
  </div>
</section>
```

---

## Step 5 — Hero Entrance Sequence

The hero should feel like a curtain rising, not a page reload.

```css
@keyframes fade-up {
  from { opacity: 0; transform: translateY(16px); }
  to   { opacity: 1; transform: translateY(0); }
}

@keyframes fade-in {
  from { opacity: 0; }
  to   { opacity: 1; }
}

.hero-eyebrow  { animation: fade-up  var(--duration-hero) var(--ease-spring) 0ms   both; }
.hero-heading  { animation: fade-up  var(--duration-hero) var(--ease-spring) 80ms  both; }
.hero-sub      { animation: fade-up  var(--duration-hero) var(--ease-spring) 160ms both; }
.hero-cta      { animation: fade-up  var(--duration-hero) var(--ease-spring) 240ms both; }
.hero-media    { animation: fade-in  800ms             var(--ease-smooth) 100ms both; }

@media (prefers-reduced-motion: reduce) {
  .hero-eyebrow,
  .hero-heading,
  .hero-sub,
  .hero-cta,
  .hero-media {
    animation: none;
    opacity: 1;
    transform: none;
  }
}
```

---

## Step 6 — Fix Skeleton / Loading States

Replace multiple pulsing elements with a single shimmer on the container.

```css
/* Before — each skeleton pulses independently */
.skeleton { animation: pulse 1.5s infinite; }

/* After — single shimmer on the parent */
@keyframes shimmer {
  from { background-position: 200% 0; }
  to   { background-position: -200% 0; }
}

.skeleton-container {
  position: relative;
  overflow: hidden;
}

.skeleton-container::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(
    90deg,
    transparent 0%,
    oklch(from var(--color-surface) l c h / 0.06) 50%,
    transparent 100%
  );
  background-size: 200% 100%;
  animation: shimmer 1.8s linear infinite;
  pointer-events: none;
}

@media (prefers-reduced-motion: reduce) {
  .skeleton-container::after { animation: none; }
}
```

---

## Step 7 — Replace `framer-motion` with `motion/react`

```tsx
/* Before */
import { motion, AnimatePresence } from 'framer-motion'

/* After */
import { motion, AnimatePresence } from 'motion/react'
```

No other changes needed — the API is identical. `motion/react` is the current canonical package.

---

## Step 8 — Modal / Drawer Enter + Exit

Use `@starting-style` for CSS-native enter animations (Baseline 2024, Chrome 117+, Firefox 129+, Safari 17.4+).

```css
.modal {
  /* Exit state */
  @starting-style {
    opacity: 0;
    transform: translateY(-8px) scale(0.97);
  }

  /* Enter state */
  opacity: 1;
  transform: translateY(0) scale(1);
  transition:
    opacity   var(--duration-slow) var(--ease-spring),
    transform var(--duration-slow) var(--ease-spring),
    display   var(--duration-slow) allow-discrete,
    overlay   var(--duration-slow) allow-discrete;
}

/* Remove when hidden — transition-behavior handles the animation */
.modal[hidden] {
  opacity: 0;
  transform: translateY(-8px) scale(0.97);
}

@media (prefers-reduced-motion: reduce) {
  .modal { transition: none; }
  @starting-style { .modal { opacity: 0; transform: none; } }
}
```

---

## Before/After Summary

| Problem | Fix |
|---|---|
| `transition: all` | Specific properties: `background`, `transform`, `color` |
| `ease-in-out` | Context-appropriate: `--ease-spring` / `--ease-smooth` / `--ease-exit` |
| `window.addEventListener('scroll')` | `IntersectionObserver` with `unobserve` |
| `framer-motion` | `motion/react` |
| Multiple pulse animations | Single shimmer on parent container |
| No hero entrance | Staggered `fade-up` keyframe with delay cascade |
| Elements appear instantly | `.reveal` + `IntersectionObserver` |
| No `prefers-reduced-motion` | Every animation has a `@media (prefers-reduced-motion: reduce)` block |
| Modals appear/disappear abruptly | `@starting-style` + `transition-behavior: allow-discrete` |

---

## Verification

```
[ ] No transition: all in codebase (grep: "transition: all")
[ ] No ease-in-out in codebase (grep: "ease-in-out")
[ ] No window.addEventListener('scroll') for animations
[ ] import from 'motion/react' not 'framer-motion'
[ ] Only 1 shimmer per skeleton group (not per item)
[ ] Hero elements stagger — eyebrow first, CTA last
[ ] Scroll reveals use IntersectionObserver with unobserve
[ ] prefers-reduced-motion tested: Chrome DevTools → Rendering → Emulate
[ ] Motion intensity varies per section (not uniform across page)
```

---

*Recipe version: global-design-skill v1.0 — `recipes/add-animations.md`*  
*Related: `rules/05-animation.md`, `tokens/tokens.css` animation section, `agents/motion-designer.md`*
