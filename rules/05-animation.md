# Rule — Animation

> Animation communicates state changes, guides attention, and signals system responsiveness. Done wrong, it obscures information and irritates users. Done right, it makes the interface feel alive and trustworthy. Every animation must earn its place by communicating something that static design cannot.

---

## R1 — Every element must enter. Nothing appears statically.

A page where elements already exist at full opacity and position when the user arrives has no energy. Every element should have an entry moment — even if it's only 200ms of opacity fade.

```css
/* Correct — element enters from @starting-style */
.card {
  transition: opacity 300ms var(--ease-spring),
              transform 300ms var(--ease-spring);
}

@starting-style {
  .card {
    opacity: 0;
    transform: translateY(12px);
  }
}

/* For scroll-triggered entries — IntersectionObserver */
.reveal {
  opacity: 0;
  transform: translateY(16px);
  transition: opacity 400ms var(--ease-spring),
              transform 400ms var(--ease-spring);
}

.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}
```

```js
const observer = new IntersectionObserver(
  entries => entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('visible')
      observer.unobserve(e.target)  // animate once, not repeatedly
    }
  }),
  { threshold: 0.1 }
)

document.querySelectorAll('.reveal').forEach(el => observer.observe(el))
```

---

## R2 — Never use `ease-in-out`. Use specific `cubic-bezier()` values.

`ease-in-out` is a CSS default that signals no thought was given to timing. Every animation should use a purpose-built easing that matches its mechanical feel.

```css
/* Correct — named, purpose-built easings */
var(--ease-spring)   /* cubic-bezier(0.16, 1, 0.3, 1) — spring into place */
var(--ease-smooth)   /* cubic-bezier(0.25, 0.46, 0.45, 0.94) — settling */
var(--ease-enter)    /* cubic-bezier(0, 0, 0.2, 1) — crisp entry */
var(--ease-exit)     /* cubic-bezier(0.4, 0, 1, 1) — fast leave */
var(--ease-snappy)   /* cubic-bezier(0.4, 0, 0, 1) — micro-interactions */

/* Wrong */
transition: all 0.3s ease-in-out;
transition: transform 300ms ease;
animation: fade 0.5s linear;
```

**Easing guide by context:**

| Context | Easing | Reason |
|---|---|---|
| Element entering screen | `--ease-spring` | Overshoots slightly — feels physical |
| Hover state change | `--ease-smooth` | Gentle, comfortable |
| Menu/modal opening | `--ease-spring` | Decisive and alive |
| Menu/modal closing | `--ease-exit` | Fast — exits shouldn't linger |
| Button click | `--ease-snappy` | Instant response |
| Color/background | `--ease-smooth` | No mechanical feel needed |
| Spinner | `var(--ease-linear)` | Continuous rotation must be uniform |

---

## R3 — Never use `transition: all`.

`transition: all` transitions every CSS property, including properties that should never transition (display, position, font-family). It causes unexpected behavior, performance issues, and prevents discrete property transitions.

```css
/* Wrong */
.card { transition: all 0.3s ease-in-out; }

/* Correct — explicit property list */
.card {
  transition:
    background-color var(--duration-fast)   var(--ease-smooth),
    border-color     var(--duration-fast)   var(--ease-smooth),
    box-shadow       var(--duration-normal) var(--ease-smooth),
    transform        var(--duration-normal) var(--ease-spring);
}
```

---

## R4 — Duration matches the scale of the change.

Micro-interactions (hover states, icon swaps) must feel instant. Large structural changes (modals, page transitions) need more time to feel purposeful.

```
< 80ms  — imperceptible — not worth animating
80–150ms — instant — icon swap, badge update, color change on hover
150–300ms — fast — component enter/exit, dropdown
300–500ms — standard — modal, drawer, page element
500–800ms — slow — hero entrance, large reveal
> 800ms — very slow — background, parallax, ambient
```

```css
/* Correct durations per context */
.btn:hover { transition: background var(--duration-fast) var(--ease-smooth); }     /* 150ms */
.dropdown  { transition: opacity var(--duration-moderate) var(--ease-spring); }    /* 300ms */
.modal     { transition: transform var(--duration-slow) var(--ease-spring); }      /* 400ms */
.hero-text { animation: hero-enter var(--duration-entrance) var(--ease-spring); }  /* 600ms */

/* Wrong — same duration for everything */
* { transition: all 300ms ease-in-out; }
```

**Distance scales the duration.** The table above assumes a short travel. An element crossing the viewport at the same 300ms reads as a teleport, because the eye tracks distance, not milliseconds. Take the element-type duration as the base at ~100px and multiply:

| Travel | Multiplier |
|---|---|
| 50px | 0.8× |
| 100px | 1.0× (base) |
| 200px | 1.3× |
| 400px | 1.6× |
| Full viewport | 1.8–2.0× |

**Exits run at 65–75% of the matching entrance.** An entrance introduces something the user needs to read; an exit removes something they are already done with. A modal that fades in over 400ms should leave in 260–300ms. Exits that match their entrance feel like the interface is stalling.

**The more often it plays, the shorter it gets.** A hover that fires a thousand times a day and an onboarding reveal seen once are not the same animation, even on the same component. Hover: 100–150ms, opacity or color only. Once-in-a-lifetime reveal: 600ms+ with full choreography. When a duration feels right in isolation but wrong in the build, check how many times a session it actually runs.

---

## R5 — `@starting-style` for elements transitioning from `display: none`.

CSS cannot normally animate from `display: none` — elements appear and disappear without transition. `@starting-style` + `transition-behavior: allow-discrete` enables smooth enter/exit on popovers, modals, dropdowns, and drawers without JavaScript.

```css
/* Dropdown that animates in when shown */
.dropdown-panel {
  opacity: 1;
  transform: translateY(0) scale(1);
  transition:
    opacity    var(--duration-moderate) var(--ease-spring),
    transform  var(--duration-moderate) var(--ease-spring),
    display    var(--duration-moderate) allow-discrete;
}

.dropdown-panel[hidden] {
  display: none;
  opacity: 0;
  transform: translateY(-8px) scale(0.97);
}

/* Entry animation — where the element starts when shown */
@starting-style {
  .dropdown-panel:not([hidden]) {
    opacity: 0;
    transform: translateY(-8px) scale(0.97);
  }
}
```

**Browser support:** `@starting-style` + `allow-discrete` is Baseline 2024. For older browsers, use the JavaScript class-toggle fallback.

---

## R6 — `prefers-reduced-motion` is mandatory for every animation.

Users with vestibular disorders, epilepsy, or motion sensitivity may configure their OS to reduce motion. Ignoring this preference causes physical discomfort and is a WCAG 2.3 Level A violation.

```css
/* Standard pattern — collapse animation to opacity only */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}

/* More nuanced — keep opacity, remove motion */
@media (prefers-reduced-motion: reduce) {
  .hero-text {
    animation: fade-in 200ms forwards;
    transform: none;
  }

  .parallax { transform: none !important; }
  .floating-element { animation: none; }
  .scroll-trigger { transition: opacity 200ms; transform: none !important; }
}

@keyframes fade-in { to { opacity: 1; } }
```

```js
// Check in JS before running complex animations
const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches

if (!reduced) {
  gsap.from('.hero-heading', { y: 40, opacity: 0, duration: 0.8, ease: 'power3.out' })
} else {
  gsap.from('.hero-heading', { opacity: 0, duration: 0.3 })
}
```

---

## R7 — Use `IntersectionObserver`, not `window.addEventListener('scroll')`.

Scroll event listeners run on the main thread and cause reflows/repaints on every scroll position change. `IntersectionObserver` is passive, runs off the main thread, and fires only when the observed threshold is crossed.

```js
/* Wrong — scroll listener */
window.addEventListener('scroll', () => {
  const element = document.querySelector('.animate')
  const rect = element.getBoundingClientRect()
  if (rect.top < window.innerHeight) {
    element.classList.add('visible')  // triggers layout on every frame
  }
})

/* Correct — IntersectionObserver */
const observer = new IntersectionObserver(
  entries => entries.forEach(entry => {
    entry.target.classList.toggle('visible', entry.isIntersecting)
  }),
  { threshold: 0.15, rootMargin: '0px 0px -50px 0px' }
)

document.querySelectorAll('[data-reveal]').forEach(el => observer.observe(el))
```

---

## R8 — Never `animate-pulse` on multiple elements simultaneously.

Multiple pulsing elements create an overwhelming, seizure-risk visual environment. Skeleton loading states should use a single shimmer sweep, not pulsing on each element independently.

```css
/* Wrong — multiple independent pulses */
.skeleton-text   { animation: pulse 1.5s infinite; }
.skeleton-image  { animation: pulse 1.5s infinite; }
.skeleton-button { animation: pulse 1.5s infinite; }

/* Correct — single directional shimmer across the whole skeleton */
.skeleton-container {
  overflow: hidden;
  position: relative;
}

.skeleton-container::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(
    90deg,
    transparent 0%,
    oklch(100% 0 0 / 0.06) 50%,
    transparent 100%
  );
  background-size: 200% 100%;
  animation: shimmer 1.8s var(--ease-linear) infinite;
}

@keyframes shimmer {
  from { background-position: 200% 0; }
  to   { background-position: -200% 0; }
}
```

---

## R9 — Stagger sequential elements. Avoid simultaneous entrances.

When multiple elements enter at the same time, none stands out. Staggered delays create a reading sequence and make the page feel composed.

```css
/* CSS stagger with animation-delay */
.feature-card:nth-child(1) { animation-delay: 0ms; }
.feature-card:nth-child(2) { animation-delay: 80ms; }
.feature-card:nth-child(3) { animation-delay: 160ms; }
.feature-card:nth-child(4) { animation-delay: 240ms; }

/* GSAP stagger */
gsap.from('.feature-card', {
  y: 24,
  opacity: 0,
  duration: 0.6,
  stagger: 0.08,
  ease: 'power3.out'
})

/* Motion/React stagger */
import { motion } from 'motion/react'

const container = { hidden: {}, visible: { transition: { staggerChildren: 0.08 } } }
const item = { hidden: { y: 24, opacity: 0 }, visible: { y: 0, opacity: 1 } }
```

---

## R10 — Use `motion/react`. Never `framer-motion`.

`framer-motion` was renamed to `motion/react` (the `motion` package). The old package name is deprecated.

```tsx
/* Wrong */
import { motion } from 'framer-motion'
import { AnimatePresence } from 'framer-motion'

/* Correct */
import { motion, AnimatePresence } from 'motion/react'
import { useAnimate, useInView, animateView } from 'motion/react'
```

---

## Motion Personality — turn the dial into numbers

`MOTION_INTENSITY: 1–10` (`rules/00`) says how much motion the project gets. It does not say what that motion feels like, so two builds at 6/10 can move like a bank and like a toy. Pick one archetype per project and hold it: the same easing on 80% of animations is what makes motion read as one product rather than one developer's mood per component.

| Archetype | Duration band | Easing | Overshoot | Fits |
|---|---|---|---|---|
| **Premium** | 350–600ms | `--ease-smooth` / `cubic-bezier(0.4, 0, 0.2, 1)` | 0% | Luxury, editorial, spatial, portfolio |
| **Corporate** | 200–400ms | `--ease-snappy` / `cubic-bezier(0.2, 0, 0, 1)` | 0–3% | SaaS, dashboards, admin, fintech |
| **Playful** | 150–300ms | `--ease-spring` (back-out family) | 10–20% | Consumer apps, education, illustration |
| **Energetic** | 100–250ms | expo-out | 15–30% | Gaming, sports, launches, campaigns |

**Default:** Corporate for product UI, Playful for decorative and illustrative elements. Record the pick in the MASTER (`templates/specs/design-system-master.md` §6) as three constants — signature easing, three durations (quick / standard / slow), one entrance pattern. Everything else inherits them.

Overshoot is context-sensitive regardless of archetype: success 5–10%, generic feedback 2–5%, celebration 15–25%, **errors 0%**. An error that bounces reads as cheerful about the failure.

---

## Motion has three layers. Flat animation is missing two of them.

Motion that technically works but feels cheap is almost always a single layer moving alone. Real movement carries supporting motion:

| Layer | What moves | Example |
|---|---|---|
| **Primary** | The thing the eye follows | Card slides up into place |
| **Secondary** | What the primary action disturbs | Its shadow lands 50ms later; the icon inside shifts 2px |
| **Ambient** | Background life, independent of interaction | Gradient drifts, grain shimmers, a slow float |

The check when a build feels flat: name all three layers. If only the primary exists, the interface animates without moving. Ambient is optional on admin and data screens — secondary is not, on any page where motion is meant to be noticed.

Counter-motion is the cheapest secondary layer there is: when the hero moves right, drift the background left at 20–30% of its speed. Depth for one line of CSS.

---

## Motion Budget by Page Type

| Page type | Motion intensity | Primary animations |
|---|---|---|
| Marketing / landing | High (5–7/10) | Hero entrance, scroll reveals, hover states |
| SaaS product | Medium (3–5/10) | Component enter/exit, skeleton, optimistic updates |
| Admin / data | Low (2–3/10) | Table sort, skeleton, toast notifications |
| Onboarding | Medium-high (4–6/10) | Step transitions, progress, celebrates completion |
| Error / 404 | Low (1–2/10) | Simple fade in, no distraction |

---

## Acceptance Criteria

```
[ ] All elements have entry animation (minimum opacity fade)
[ ] No ease-in-out or ease named easings — all cubic-bezier
[ ] No transition: all — explicit property list
[ ] Duration matches scale: micro < 150ms, standard 200–400ms
[ ] @starting-style used for elements transitioning from display:none
[ ] prefers-reduced-motion: all animations collapse or reduce
[ ] IntersectionObserver used — no scroll event listeners for animation
[ ] No multiple simultaneous pulse animations — shimmer pattern used
[ ] Sequential elements stagger by 60–120ms
[ ] motion/react import — not framer-motion
[ ] One motion archetype picked and recorded in the MASTER — not per-component easing
[ ] Long travel scaled by distance; exits at 65–75% of their entrance
[ ] Frequently repeated animations (hover, toggle) kept at 100–150ms
[ ] Noticed motion carries a secondary layer — not primary alone
[ ] No scale(0) on enter or exit — 0.95 minimum
[ ] Errors animate with 0% overshoot
```

---

## R11 — Use scroll-driven animations for simple reveals. Use `IntersectionObserver` as fallback.

CSS scroll-driven animations (Baseline 2024) replace `IntersectionObserver` for visual reveals and parallax — no JavaScript.

```css
/* Simple scroll reveal — no JS needed */
@keyframes reveal {
  from { opacity: 0; transform: translateY(20px); }
  to   { opacity: 1; transform: none; }
}

.scroll-reveal {
  animation: reveal linear both;
  animation-timeline: view();
  animation-range: entry 0% entry 40%;
}

@media (prefers-reduced-motion: reduce) {
  .scroll-reveal { animation: none; opacity: 1; transform: none; }
}
```

**When to use `IntersectionObserver` instead:** When you need class-toggling, complex stagger via JavaScript, or must support browsers without scroll-driven animation support.

---

## R12 — View Transitions for same-document navigation.

Use the View Transitions API for page and component transitions. CSS-native, no library required.

```css
/* Enable for all navigations */
@view-transition {
  navigation: auto;
}

/* Customize transitions */
::view-transition-old(root) {
  animation: 250ms var(--ease-exit) both fade-out;
}
::view-transition-new(root) {
  animation: 300ms var(--ease-spring) both fade-in;
}

/* Named element — animates between matched elements across pages */
.product-card-image {
  view-transition-name: product-image;
  contain: layout;
}
```

```ts
/* JS-triggered view transition (SPA routing) */
async function navigate(url: string) {
  if (!document.startViewTransition) {
    window.location.href = url
    return
  }
  await document.startViewTransition(() => {
    window.location.href = url
  }).finished
}
```

---

## R13 — Never scale to `0`. Never travel more than a third of the screen unbroken.

Two amplitude limits that static review never catches, because both look correct in the CSS.

**`scale(0)` collapses an element into a point** and reads as a glitch, not a dismissal. The last frames shrink past any legible size while the shadow and border collapse with them.

```css
/* Wrong — vanishes into nothing */
.modal-exit { transform: scale(0); }

/* Correct — recedes and fades */
.modal-exit { transform: scale(0.95); opacity: 0; }
```

The same applies to entrances: start at `0.95`, not `0`. Anything below `0.9` looks like a zoom effect rather than an arrival.

**Motion crossing more than a third of the viewport needs an intermediate keyframe** — a curve, a scale change, a speed change. A straight linear slide across the full screen has nothing for the eye to hold on to, and the duration required to make it comfortable (1.8–2.0× base, per R4) makes the wait obvious. Either shorten the travel or break it.

Related limit for multi-element scenes: with three or more elements, keep no more than a third of them in active motion at once. Everything moving at once produces noise, not choreography.

---

## Troubleshooting — the animation works but feels wrong

Motion failures rarely show up as bugs. They show up as a build that technically animates and still feels cheap. Symptom to cause:

| Symptom | Likely cause | Fix |
|---|---|---|
| Feels robotic | Linear easing, or straight-line paths only | Purpose-built `cubic-bezier` (R2); add arc or counter-motion |
| Feels cheap or flat | Only the primary layer moves | Add secondary (shadow, inner icon) and ambient |
| Feels sluggish, though durations match the table | Duration ignores travel distance | Apply the R4 distance multiplier, or shorten the travel |
| Feels twitchy on a familiar control | Same duration for a hover as for a first-run reveal | Apply the frequency rule (R4) |
| Distracting | Too many elements in motion at once | Enforce the third-of-elements limit (R13); cut amplitude |
| No personality — "generic AI page" | Different easing per component | Lock one archetype and one signature easing |
| Element seems to disappear rather than close | `scale(0)`, or opacity alone on a spatial change | `scale(0.95)` + opacity; pair opacity with movement |
| Reads as stalling on close | Exit as long as entrance | Exit at 65–75% |

---

## CSS 2026 — Stagger Without JavaScript

`sibling-index()` and `sibling-count()` are now Baseline (Chrome + Safari stable). Use them to stagger list animations purely in CSS — no `motion/react` needed for simple sequential reveals.

```css
/* CSS stagger — no JS required */
li {
  transition: opacity 0.3s ease, transform 0.3s ease;
  transition-delay: calc((sibling-index() - 1) * 80ms);

  @starting-style {
    opacity: 0;
    transform: translateY(12px);
  }
}
```

**When to use CSS stagger vs motion/react:**

| Scenario | Use |
|---|---|
| Static list, no interaction | CSS `sibling-index()` |
| Interactive list (drag, filter, sort) | `motion/react` variants |
| List exits / removes items | `motion/react` + `AnimatePresence` |
| Scroll-triggered with complex easing | `motion/react` `whileInView` |

---

*Rule version: global-design-skill v2.7.0 — `rules/05-animation.md`*
*Related: `references/motion-systems.md` (tokens, springs, overshoot), `references/gsap-patterns.md` (timeline + ScrollTrigger), `rules/17-motion-react.md` (React), `templates/specs/design-system-master.md` §6 (where the archetype is recorded)*
*Related: `rules/17-motion-react.md`, `references/motion-systems.md`, `references/motion-dev.md`, `tokens/tokens.css`, `patterns/product-ui/loading-states.md`*
