# Reference — GSAP Patterns

> GSAP is the third choice, not the first. CSS handles hovers, reveals, and scroll-linked transforms natively (`references/motion-systems.md`); `motion/react` handles component state, layout, and exit animations (`rules/17`). GSAP earns its ~25kb when you need a **timeline** — sequenced beats with a position parameter — or **ScrollTrigger** — pinning, scrubbing, and horizontal scroll. Reaching for it to fade in a card is a bundle you pay for and a dependency you maintain.

---

## Choosing the tool

| Need | Use | Cost |
|---|---|---|
| Hover, focus, simple enter/exit | CSS transition + `@starting-style` | 0kb |
| Scroll reveal, parallax, progress bar | CSS `animation-timeline` (`rules/05` R11) | 0kb |
| Component state, layout shift, `AnimatePresence` | `motion/react` (`rules/17`) | ~30kb |
| Sequenced multi-beat timeline | **GSAP core** | ~25kb |
| Pin, scrub, horizontal scroll, batch reveal | **GSAP + ScrollTrigger** | +~15kb |
| Text split by char/word/line | **GSAP + SplitText** | +~7kb |
| Layout-to-layout morph (FLIP) | **GSAP + Flip** | +~5kb |

Mixing `motion/react` and GSAP in one project is fine. Mixing them **on the same element** is not — two libraries writing the same transform fight each other every frame.

---

## Licensing — current status

GSAP is at **3.15.0** and the entire toolset is free, including for commercial use. The plugins that used to require a Club GreenSock membership — SplitText, MorphSVG, DrawSVG, ScrollSmoother, Inertia, CustomBounce, GSDevTools — now ship in the public package under the standard no-charge license. Webflow funded the change.

Practical consequence: text-splitting and SVG-morph animations no longer need a paid workaround or a hand-rolled substitute. Recommend `SplitText` directly.

*(Verified against `package.json` `"version": "3.15.0"` and the license field in the GreenSock repository. Re-check before quoting to a client — licensing terms are the kind of fact that changes.)*

---

## Setup

```js
import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import { SplitText } from 'gsap/SplitText'

gsap.registerPlugin(ScrollTrigger, SplitText)   // register once, at module top level
```

### React — `useGSAP()`, never bare `useEffect`

The `@gsap/react` package exposes `useGSAP()`, a drop-in replacement for `useEffect` / `useLayoutEffect` that reverts every animation and ScrollTrigger created inside it on unmount. Manual cleanup in `useEffect` is the single most common source of leaked ScrollTriggers in React builds — they survive route changes and stack up until scroll behaviour breaks.

```tsx
import { useGSAP } from '@gsap/react'

const container = useRef<HTMLDivElement>(null)

useGSAP(() => {
  gsap.from('.card', { y: 40, opacity: 0, stagger: 0.1 })
}, { scope: container })   // selectors resolve inside container; auto-reverts on unmount
```

`scope` also means you can use plain string selectors instead of a ref per element, without leaking into other components.

---

## Core patterns

### `defaults` on the timeline

```js
const tl = gsap.timeline({ defaults: { duration: 0.8, ease: 'power2.out' } })

tl.to('.a', { y: -20 })
  .to('.b', { y: -20 }, '<0.1')   // 0.1s after the previous tween starts
  .to('.c', { y: -20 }, '<0.1')
```

The position parameter is the reason to use a timeline at all. `'<'` starts with the previous tween, `'>'` after it ends, `'<0.1'` offsets from its start, `'-=0.2'` overlaps the end. Chaining `delay` values instead produces a sequence you cannot re-time without recalculating every step.

### Stagger with distribution

```js
gsap.to('.grid-item', {
  y: 0,
  opacity: 1,
  stagger: {
    each: 0.05,
    from: 'center',   // 'start' | 'end' | 'center' | 'edges' | 'random' | index
    grid: 'auto',     // reads the rendered grid, staggers in 2D
    axis: 'x',        // 'x' | 'y' | null for both
  },
})
```

`grid: 'auto'` is what CSS stagger (`sibling-index()`) cannot do — it staggers by visual position rather than DOM order. Keep the total under 500ms regardless of item count (`rules/05` R9): with 40 items, `each: 0.05` is already 2s and reads as a loading bug.

---

## ScrollTrigger

### Batch reveal — the right tool for a long list

```js
ScrollTrigger.batch('.card', {
  onEnter: els => gsap.to(els, { opacity: 1, y: 0, stagger: 0.1, overwrite: true }),
  start: 'top 85%',
  once: true,
})
```

`batch` groups elements that cross the trigger in the same frame into one call, instead of creating one ScrollTrigger per card. On a 60-item grid that is 1 handler rather than 60.

For a plain fade-up reveal with no stagger, CSS scroll-driven animation does the same job at 0kb. Use `batch` when the stagger has to respond to what actually entered together.

### Pin and scrub

```js
gsap.to('.panel', {
  x: '-300%',
  ease: 'none',                       // required — see mistake 1
  scrollTrigger: {
    trigger: '.container',
    pin: true,
    scrub: 1,                         // 1s catch-up smoothing; `true` = locked to scroll
    end: () => '+=' + document.querySelector('.container').scrollWidth,
  },
})
```

### Horizontal scroll with `containerAnimation`

Animating elements *inside* a horizontally scrolling track needs `containerAnimation` — a normal ScrollTrigger measures against the viewport and never fires for content parked off-screen.

```js
const track = gsap.to('.panels', {
  x: () => -(document.querySelector('.panels').scrollWidth - window.innerWidth),
  ease: 'none',
  scrollTrigger: { trigger: '.wrapper', pin: true, scrub: 1 },
})

gsap.to('.panel-content', {
  scale: 1.2,
  scrollTrigger: {
    trigger: '.panel-content',
    containerAnimation: track,        // measure against the track, not the viewport
    start: 'left center',             // horizontal keywords, not 'top'
    end: 'right center',
    scrub: true,
  },
})
```

---

## SplitText — current API

The old `new SplitText(el, { type })` pattern still works but leaves you to handle font loading and resize yourself: lines split before a webfont lands are split at the wrong widths, and they stay wrong until reload.

```js
const split = SplitText.create('.headline', {
  type: 'lines,words',
  mask: 'lines',            // wraps each line in an overflow-hidden mask — clean reveal, no extra markup
  autoSplit: true,          // re-splits on resize and after fonts finish loading
  aria: 'auto',             // default — keeps the original text readable to screen readers
  onSplit: self => gsap.from(self.lines, { yPercent: 100, stagger: 0.08, ease: 'power3.out' }),
})
```

Return the tween from `onSplit` so GSAP can kill the old one when it re-splits. Without that, every resize stacks another animation on the same nodes.

`aria` defaults to `'auto'`, which restores the original string for assistive tech — splitting a heading into 60 `<span>`s otherwise makes it unreadable letter-by-letter in a screen reader. Do not set `aria: 'none'` on real content.

---

## Reduced motion — `gsap.matchMedia()`

`matchMedia` reverts everything created inside a non-matching context, which is exactly what a `prefers-reduced-motion` switch needs — not a skipped animation, but the end state applied and the ScrollTriggers removed.

```js
const mm = gsap.matchMedia()

mm.add('(prefers-reduced-motion: no-preference)', () => {
  gsap.from('.hero-title', { y: 40, opacity: 0, duration: 0.6 })
  ScrollTrigger.batch('.card', { onEnter: els => gsap.to(els, { opacity: 1, y: 0, stagger: 0.1 }) })
  // everything here is reverted automatically if the preference changes
})

mm.add('(prefers-reduced-motion: reduce)', () => {
  gsap.set('.hero-title, .card', { opacity: 1, y: 0 })   // final state, no motion
})
```

An `if (prefersReduced) return` guard runs once on load and ignores the user changing the setting mid-session. `matchMedia` responds live.

---

## Five mistakes that produce working-but-broken scroll animations

**1. Easing on a scrubbed tween.** `scrub` maps scroll position to animation progress. An ease remaps it again, so the element lags behind the cursor and overshoots on stop.

```js
// Wrong
gsap.to('.panels', { x: -2000, ease: 'power2.out', scrollTrigger: { scrub: 1 } })
// Right
gsap.to('.panels', { x: -2000, ease: 'none', scrollTrigger: { scrub: 1 } })
```

**2. A ScrollTrigger on a child tween of a timeline that already has one.** Silently ignored — no error, no animation.

```js
// Wrong
const tl = gsap.timeline({ scrollTrigger: { trigger: '.section' } })
tl.to('.box', { x: 100, scrollTrigger: { trigger: '.box' } })

// Right — one ScrollTrigger per timeline, or standalone tweens
gsap.to('.box', { x: 100, scrollTrigger: { trigger: '.box' } })
```

**3. `setState` inside `onUpdate`.** Fires up to 60 times a second; every call re-renders the subtree that owns the animation.

```js
// Wrong
scrollTrigger: { onUpdate: self => setProgress(self.progress) }

// Right — write to the DOM directly, outside React's render cycle
const setWidth = gsap.quickSetter('.progress-bar', 'scaleX')
scrollTrigger: { onUpdate: self => setWidth(self.progress) }
```

**4. `from()` following another tween in a timeline.** `from()` has `immediateRender: true`, so it applies its start values at build time and the element visibly jumps before its turn.

```js
tl.to('.box', { x: 100 })
tl.from('.box', { y: 50, immediateRender: false })   // required
```

**5. Animating layout properties.** `width`, `height`, `top`, `left` force a layout pass every frame. Use transforms; when the real layout must change, use the Flip plugin to animate the transform equivalent of the layout delta.

```js
// Wrong
gsap.to('.box', { width: 200, height: 200 })
// Right
gsap.to('.box', { scaleX: 1.5, scaleY: 1.5 })
```

---

## Acceptance criteria

```
[ ] GSAP justified — timeline, pin, scrub, split, or FLIP; not a fade CSS could do
[ ] Plugins registered once at module top level
[ ] React: useGSAP() with a scope — no manual useEffect cleanup
[ ] Every scrubbed tween uses ease: 'none'
[ ] One ScrollTrigger per timeline — no child-tween triggers
[ ] onUpdate writes to the DOM (quickSetter / ref), never setState
[ ] from() after another tween sets immediateRender: false
[ ] Only transform and opacity animated — Flip for real layout changes
[ ] gsap.matchMedia() gates all motion; reduced-motion branch sets the end state
[ ] SplitText uses autoSplit + onSplit; aria left at 'auto'
[ ] ScrollTrigger.refresh() called after async content changes page height
```

---

*Reference version: global-design-skill v2.7.0 — `references/gsap-patterns.md`*
*Related: `rules/05-animation.md` (timing, personality, amplitude limits), `rules/17-motion-react.md` (motion/react — the default for React), `references/motion-systems.md` (CSS-native motion, easing and duration tokens), `patterns/effects/scroll-experiences.md` and `patterns/effects/parallax-system.md` (built scroll patterns)*
