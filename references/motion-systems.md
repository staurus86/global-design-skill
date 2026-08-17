# Reference — Motion Systems

> CSS-native animation techniques: scroll-driven animations, View Transitions API, `@starting-style`, `@property` animation, and the full motion toolkit without JavaScript. For the React/JS animation layer, see `references/motion-dev.md`.

---

## Motion Budget by Page Type

Before writing any animation, set the intensity ceiling for each section.

| Page type | Max intensity | Primary techniques |
|---|---|---|
| Marketing landing | 7/10 | Hero entrance, scroll reveals, hover states |
| SaaS product | 5/10 | Component enter/exit, optimistic updates |
| Admin / data | 3/10 | Table sort, skeleton, toast |
| Onboarding | 6/10 | Step transitions, progress, celebrations |
| Error / 404 | 2/10 | Simple fade — no distraction |
| **Section within page** | Varies | Hero: 6–7, Features: 4–5, Footer: 1–2 |

**Motion contrast creates rhythm.** A page where all sections have the same animation intensity feels monotonous. The hero should feel more alive than the footer.

---

## Easing Reference

Never use named easings (`ease`, `ease-in`, `ease-in-out`, `ease-out`). These are browser defaults with no design intent.

```css
:root {
  --ease-spring:  cubic-bezier(0.16, 1, 0.3, 1);        /* entering — overshoots slightly */
  --ease-smooth:  cubic-bezier(0.25, 0.46, 0.45, 0.94); /* hover — gentle decelerate */
  --ease-enter:   cubic-bezier(0, 0, 0.2, 1);           /* crisp entry — fast then settle */
  --ease-exit:    cubic-bezier(0.4, 0, 1, 1);           /* fast exit — don't linger */
  --ease-snappy:  cubic-bezier(0.4, 0, 0, 1);           /* click feedback */
  --ease-linear:  cubic-bezier(0, 0, 1, 1);             /* spinners only */
}
```

| Context | Easing | Reason |
|---|---|---|
| Element entering | `--ease-spring` | Physical, overshoots into place |
| Hover state | `--ease-smooth` | Comfortable, not mechanical |
| Menu / modal open | `--ease-spring` | Decisive — communicates system response |
| Menu / modal close | `--ease-exit` | Exits must be fast — don't compete with new content |
| Button click | `--ease-snappy` | Instant confirmation |
| Color / background | `--ease-smooth` | No mechanical feel needed |
| Spinner / marquee | `--ease-linear` | Continuous — must be uniform |

---

## Duration Reference

```css
:root {
  --duration-instant:  80ms;   /* icon swap, badge counter update */
  --duration-micro:   120ms;   /* hover color change */
  --duration-fast:    150ms;   /* hover state, border, small component */
  --duration-normal:  200ms;   /* component enter/exit */
  --duration-moderate:300ms;   /* dropdown, drawer, sheet */
  --duration-slow:    400ms;   /* modal, page element */
  --duration-entrance:600ms;   /* hero H1, large reveal */
  --duration-relaxed: 800ms;   /* parallax, background shift */
}
```

**Rule:** Duration scales with visual weight. A 4px icon swap: 80ms. A full-screen modal: 400ms. If it feels fast, it's probably right.

---

## Springs — stiffness and damping

Springs have no duration. They settle when the physics says so, which is why they beat fixed timing on anything the user drives directly — drag, tabs, toggles, layout shifts. For anything the user only watches, a `cubic-bezier` with a known duration is easier to choreograph against.

```tsx
transition={{ type: 'spring', stiffness: 400, damping: 30 }}
```

| Feel | Stiffness | Damping | Use |
|---|---|---|---|
| Very stiff | 400+ | 25–30 | Buttons, toggles, tabs — near-instant settle |
| Standard | 250–350 | 18–24 | Modals, drawers, layout animations |
| Gentle | 100–150 | 20–25 | Large surfaces, ambient movement |
| Bouncy | 150–250 | 10–15 | Playful archetype only |
| Very bouncy | 100–200 | 5–10 | Celebration moments — one per page at most |

Damping ratio decides the character: below 1.0 the spring oscillates, 1.0 is the fastest settle without overshoot, above 1.0 it crawls in. Damping under 15 on a Corporate or Premium build will look like a bug, not a flourish.

**Never spring an error state.** Oscillation reads as playful, and a failed payment is not.

---

## Overshoot budget

Overshoot is how far past the target the element travels before settling. It is the single strongest signal of motion personality — and the easiest to apply where it does harm.

| Context | Overshoot | Why |
|---|---|---|
| Success confirmation | 5–10% | Enough lift to register as positive |
| Generic feedback (press, toggle) | 2–5% | Physical, not decorative |
| Celebration (onboarding complete, first win) | 15–25% | Once per flow, never repeated |
| Premium / editorial builds | 0% | Overshoot reads as cheap on a luxury surface |
| **Errors, warnings, destructive confirms** | **0%** | A bouncing error is cheerful about the failure |

---

## `@starting-style` — CSS-Native Enter Animations

`@starting-style` enables CSS transitions from `display: none` without JavaScript. Baseline 2024. (Chrome 117+, Firefox 129+, Safari 17.4+)

**Without `@starting-style`:** Elements transitioning from `display: none` appear instantly — no entrance animation.

**With `@starting-style`:** Define the initial state before the element becomes visible.

```css
/* Dropdown / popover */
.dropdown {
  opacity: 1;
  transform: translateY(0) scale(1);
  transition:
    opacity   var(--duration-moderate) var(--ease-spring),
    transform var(--duration-moderate) var(--ease-spring),
    display   var(--duration-moderate) allow-discrete,
    overlay   var(--duration-moderate) allow-discrete;
}

.dropdown[hidden] {
  display: none;
  opacity: 0;
  transform: translateY(-8px) scale(0.97);
}

@starting-style {
  .dropdown:not([hidden]) {
    opacity: 0;
    transform: translateY(-8px) scale(0.97);
  }
}
```

```css
/* Native <dialog> enter/exit */
dialog {
  opacity: 1;
  transform: scale(1);
  transition:
    opacity   var(--duration-slow) var(--ease-spring),
    transform var(--duration-slow) var(--ease-spring),
    overlay   var(--duration-slow) allow-discrete,
    display   var(--duration-slow) allow-discrete;
}

dialog:not([open]) {
  opacity: 0;
  transform: scale(0.95);
  pointer-events: none;
}

@starting-style {
  dialog[open] {
    opacity: 0;
    transform: scale(0.95);
  }
}
```

```css
/* Native [popover] API */
[popover] {
  opacity: 0;
  transform: translateY(-4px) scale(0.97);
  transition:
    opacity   var(--duration-normal) var(--ease-spring),
    transform var(--duration-normal) var(--ease-spring),
    display   var(--duration-normal) allow-discrete,
    overlay   var(--duration-normal) allow-discrete;
}

[popover]:popover-open {
  opacity: 1;
  transform: translateY(0) scale(1);
}

@starting-style {
  [popover]:popover-open {
    opacity: 0;
    transform: translateY(-4px) scale(0.97);
  }
}
```

---

## `@property` — Animating Custom Properties

`@property` registers a CSS custom property with a type, enabling transitions between values. Without registration, custom properties change instantly (cannot be interpolated).

```css
/* Register the property */
@property --card-glow {
  syntax: "<number>";
  inherits: false;
  initial-value: 0;
}

/* Now it transitions */
.card {
  box-shadow: 0 0 calc(var(--card-glow) * 1px) oklch(from var(--color-accent) l c h / 0.3);
  transition: --card-glow var(--duration-normal) var(--ease-smooth);
}

.card:hover {
  --card-glow: 24;
}
```

```css
/* Animated gradient angle */
@property --gradient-angle {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}

.animated-gradient {
  background: conic-gradient(
    from var(--gradient-angle),
    oklch(65% 0.22 258),
    oklch(65% 0.18 310),
    oklch(65% 0.22 258)
  );
  animation: spin-gradient 6s linear infinite;
}

@keyframes spin-gradient {
  to { --gradient-angle: 360deg; }
}
```

```css
/* Hue animation */
@property --hue {
  syntax: "<number>";
  inherits: false;
  initial-value: 258;
}

.hue-accent {
  color: oklch(65% 0.22 var(--hue));
  animation: drift-hue 10s linear infinite;
}

@keyframes drift-hue {
  to { --hue: 318; }
}

@media (prefers-reduced-motion: reduce) {
  .hue-accent { animation: none; }
}
```

---

## Scroll-Driven Animations (CSS Native)

CSS scroll-driven animations replace `IntersectionObserver` for visual reveals and parallax. No JavaScript. Baseline 2024 (Chrome 115+, Firefox 132+, Safari 26).

### Scroll-linked (scrubs with scroll position)

```css
@keyframes reveal-from-bottom {
  from { opacity: 0; transform: translateY(24px); }
  to   { opacity: 1; transform: translateY(0); }
}

.scroll-reveal {
  animation: reveal-from-bottom linear both;
  animation-timeline: view();
  animation-range: entry 0% entry 40%;
}
```

### Parallax (element moves slower than scroll)

```css
@keyframes parallax-up {
  from { transform: translateY(0); }
  to   { transform: translateY(-15%); }
}

.parallax-slow {
  animation: parallax-up linear both;
  animation-timeline: scroll(root block);
  animation-range: 0% 100%;
}
```

### Progress bar (tied to page scroll)

```css
.scroll-progress {
  position: fixed;
  top: 0;
  left: 0;
  height: 3px;
  background: var(--color-accent);
  transform-origin: left;
  animation: grow-width linear both;
  animation-timeline: scroll(root);
}

@keyframes grow-width {
  from { transform: scaleX(0); }
  to   { transform: scaleX(1); }
}
```

### Stagger via `animation-range` offset

```css
.feature-grid .card:nth-child(1) { animation-range: entry 0% entry 35%; }
.feature-grid .card:nth-child(2) { animation-range: entry 10% entry 45%; }
.feature-grid .card:nth-child(3) { animation-range: entry 20% entry 55%; }

.feature-grid .card {
  animation: reveal-from-bottom linear both;
  animation-timeline: view();
}
```

### `prefers-reduced-motion` for scroll-driven

```css
@media (prefers-reduced-motion: reduce) {
  .scroll-reveal {
    animation: none;
    opacity: 1;
    transform: none;
  }
  .parallax-slow {
    animation: none;
    transform: none;
  }
}
```

---

## View Transitions API

CSS-powered page transitions and component-level crossfades. No JavaScript required for same-page transitions.

### Same-document view transitions (CSS only)

```css
/* Opt-in for the entire document */
@view-transition {
  navigation: auto;
}

/* Customize the transition */
::view-transition-old(root) {
  animation: 300ms var(--ease-exit) both fade-out;
}

::view-transition-new(root) {
  animation: 300ms var(--ease-spring) both fade-in;
}

@keyframes fade-out { to { opacity: 0; } }
@keyframes fade-in  { from { opacity: 0; } }
```

### Named view transition elements (hero animation between pages)

```css
/* On the source page */
.product-card {
  view-transition-name: product-hero;
  contain: layout;
}

/* On the target page */
.product-hero-image {
  view-transition-name: product-hero;
  contain: layout;
}

/* The browser automatically animates between matching names */
```

### JavaScript-triggered view transitions (for SPA)

```ts
import { animateView } from 'motion'

async function navigateTo(url: string) {
  await animateView(() => {
    window.location.href = url
  })
}

// Or with the native API
async function updateDOM(newContent: string) {
  if (!document.startViewTransition) {
    document.body.innerHTML = newContent
    return
  }

  await document.startViewTransition(() => {
    document.body.innerHTML = newContent
  }).finished
}
```

---

## Hero Entrance Sequence

The hero is the first thing the user sees. It must feel composed, not accidental.

```css
@keyframes fade-up {
  from { opacity: 0; transform: translateY(16px); }
  to   { opacity: 1; transform: translateY(0); }
}

@keyframes fade-in {
  from { opacity: 0; }
  to   { opacity: 1; }
}

/* Stagger: eyebrow → H1 → subtitle → CTA → media */
.hero-eyebrow { animation: fade-up var(--duration-entrance) var(--ease-spring) 0ms   both; }
.hero-heading { animation: fade-up var(--duration-entrance) var(--ease-spring) 80ms  both; }
.hero-sub     { animation: fade-up var(--duration-entrance) var(--ease-spring) 160ms both; }
.hero-cta     { animation: fade-up var(--duration-entrance) var(--ease-spring) 240ms both; }
.hero-media   { animation: fade-in 800ms              var(--ease-smooth) 100ms both; }

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

## Scroll Reveal (IntersectionObserver — for browsers without scroll-driven support)

```css
.reveal {
  opacity: 0;
  transform: translateY(20px);
  transition:
    opacity   var(--duration-entrance) var(--ease-spring),
    transform var(--duration-entrance) var(--ease-spring);
}

.reveal.is-visible {
  opacity: 1;
  transform: translateY(0);
}

/* Stagger for lists */
.reveal-stagger .reveal:nth-child(1) { transition-delay: 0ms; }
.reveal-stagger .reveal:nth-child(2) { transition-delay: 80ms; }
.reveal-stagger .reveal:nth-child(3) { transition-delay: 160ms; }
.reveal-stagger .reveal:nth-child(4) { transition-delay: 240ms; }
.reveal-stagger .reveal:nth-child(5) { transition-delay: 320ms; }

@media (prefers-reduced-motion: reduce) {
  .reveal {
    opacity: 1;
    transform: none;
    transition: none;
  }
}
```

```ts
const observer = new IntersectionObserver(
  entries => entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('is-visible')
      observer.unobserve(e.target)   // animate once — do not re-trigger
    }
  }),
  { threshold: 0.1, rootMargin: '0px 0px -48px 0px' }
)

document.querySelectorAll('.reveal').forEach(el => observer.observe(el))
```

---

## Hover State Rules

Every interactive element must have smooth hover transitions. Never `transition: all`.

```css
/* Button */
.btn {
  transition:
    background-color var(--duration-fast)   var(--ease-smooth),
    box-shadow       var(--duration-normal) var(--ease-smooth),
    color            var(--duration-fast)   var(--ease-smooth),
    transform        var(--duration-fast)   var(--ease-snappy);
}

.btn:active {
  transform: scale(0.97);
}

/* Card */
.card {
  transition:
    transform  var(--duration-normal) var(--ease-spring),
    box-shadow var(--duration-normal) var(--ease-smooth);
}

.card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

/* Link */
.link {
  text-decoration-color: transparent;
  transition: text-decoration-color var(--duration-fast) var(--ease-smooth);
}

.link:hover {
  text-decoration-color: currentColor;
}

/* Icon button */
.icon-btn {
  transition:
    background var(--duration-fast)    var(--ease-smooth),
    transform  var(--duration-instant) var(--ease-snappy),
    color      var(--duration-fast)    var(--ease-smooth);
}

.icon-btn:active {
  transform: scale(0.88);
}
```

---

## Skeleton / Loading State

One shimmer sweep — not individual pulses. See `rules/05-animation.md` R8.

```css
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
    oklch(from var(--color-surface-2) l c h / 0.07) 50%,
    transparent 100%
  );
  background-size: 200% 100%;
  animation: shimmer 1.8s var(--ease-linear) infinite;
  pointer-events: none;
}

@media (prefers-reduced-motion: reduce) {
  .skeleton-container::after { animation: none; }
}
```

---

## Animation Acceptance Criteria

```
[ ] No transition: all anywhere in codebase
[ ] No ease-in-out or named easings — all cubic-bezier
[ ] Duration matched to visual weight — micro < 150ms, modal ≤ 400ms
[ ] @starting-style for elements that transition from display: none
[ ] prefers-reduced-motion: all animations either collapse or disable
[ ] IntersectionObserver for scroll reveals — no scroll event listeners
[ ] One shimmer sweep per skeleton group (not per item)
[ ] Hero elements stagger 60–100ms per element
[ ] motion/react import — not framer-motion
[ ] View Transitions used for same-document navigation (if applicable)
[ ] Scroll-driven animations preferred over JS for simple reveals (if browser support sufficient)
```

---

*Reference version: global-design-skill v1.0 — `references/motion-systems.md`*
*Related: `rules/05-animation.md`, `references/motion-dev.md`, `references/visual-effects.md`*
