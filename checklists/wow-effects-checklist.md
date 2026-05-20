# Checklist — Wow Effects Quality Gate

> Run before shipping any page that uses animations, parallax, 3D, or motion effects. A page fails this checklist if it scores below 80%.

---

## How to Score

Count all items relevant to your implementation. Score = (passed items / relevant items) × 100.

- **≥ 90%** — Ship it
- **70–89%** — Fix critical items, acceptable for beta
- **< 70%** — Do not ship

Mark each item: **[P]** Pass, **[F]** Fail, **[N/A]** Not applicable.

---

## 1. Reduced Motion Compliance

Every single animation must have a fallback. No exceptions.

- [ ] `prefers-reduced-motion: reduce` tested in DevTools (Chrome: Rendering tab → Emulate CSS media feature)
- [ ] All `animation:` declarations wrapped in `@media (prefers-reduced-motion: no-preference)` OR cancelled in reduce block
- [ ] All `transition:` declarations on animated elements use `:reduce { transition: none }` override
- [ ] GSAP: all timelines wrapped in `gsap.matchMedia().add('(prefers-reduced-motion: no-preference)', ...)`
- [ ] Three.js / R3F canvas: replaced with static `<img>` or hidden when reduced motion is set
- [ ] Spline embed: has a `<img>` fallback rendered when `prefers-reduced-motion: reduce`
- [ ] Marquee/ticker: `animation: none` stops the scroll; content remains visible
- [ ] Page is fully readable and usable with all animations disabled

---

## 2. Performance — GPU & Compositing

- [ ] Only `transform` and `opacity` are animated (never `width`, `height`, `top`, `left`, `margin`, `background-color` in animation loops)
- [ ] `will-change: transform` is NOT set permanently — only added immediately before animation starts
- [ ] `will-change: transform` is removed (set to `auto`) when animation completes
- [ ] No more than 4–6 elements have `will-change` active simultaneously
- [ ] `window.addEventListener('scroll')` is NOT used for any animation — replaced with `IntersectionObserver` or `ScrollTrigger`
- [ ] No `setInterval` used for animation — all loops use `requestAnimationFrame`
- [ ] Canvas `devicePixelRatio` capped at 2: `renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))`
- [ ] Three.js / Spline canvas pauses when off-screen (`IntersectionObserver` cancels RAF loop)
- [ ] Lenis smooth scroll is integrated with GSAP ticker (not running two separate RAF loops)

---

## 3. Performance — Bundle & Load

- [ ] GSAP is imported only if animations require it (not as default)
- [ ] Three.js is imported only if CSS 3D can't achieve the effect
- [ ] All heavy libraries (Three.js, R3F, Spline runtime) are dynamically imported / lazy loaded
- [ ] Grain texture uses inline SVG `data:` URI — not an external image file
- [ ] Hero image has `fetchpriority="high"` attribute
- [ ] Hero image has `<link rel="preload" as="image">` in `<head>`
- [ ] LCP candidate identified and not delayed by animations hiding it

---

## 4. Mobile & Touch Graceful Degradation

- [ ] Cursor effects disabled on `pointer: coarse` (touch devices have no hover cursor)
- [ ] 3D tilt disabled on `pointer: coarse` (touch tilt requires explicit touch handler, not mousemove)
- [ ] Mouse-tracking spotlight removed on `pointer: coarse`
- [ ] Parallax intensity reduced on mobile (or fully disabled for `pointer: coarse`)
- [ ] All effects tested at 375px viewport width — page is not broken
- [ ] `min-height: 100dvh` used (not `100vh`) on any full-screen sections
- [ ] Marquee does not cause horizontal scroll on mobile
- [ ] Touch scroll is not blocked by canvas elements (`pointer-events: none` on decorative canvases)

---

## 5. Visual Quality

- [ ] Grain opacity is 0.03–0.06 — visible texture but not visual noise
- [ ] Mesh gradient colors use OKLCH with chroma reduction near extremes (not oversaturated)
- [ ] Glass effects have `backdrop-filter: blur(24px) saturate(180%)` — not just `backdrop-filter: blur()`
- [ ] Spotlight is subtle (opacity 0.05–0.1 on accent) — not a bright disco effect
- [ ] Animation easing uses custom beziers — never `ease-in-out` for UI motion
- [ ] Stagger delays are 60–120ms between elements — not flat (all same) and not too slow (>200ms)
- [ ] All animations feel intentional — no "everything is flying everywhere"
- [ ] There is one hero element pushed to 120% (the standout) — not everything at maximum
- [ ] 3D effects do not distort text readability
- [ ] No element has more than 2 concurrent animations

---

## 6. Entrance Sequence

- [ ] Page is invisible / broken BEFORE `.entered` classes are added (verify by disabling JS)
- [ ] This is fixed: JS fallback ensures content is visible if JS fails or is slow
- [ ] `requestAnimationFrame(() => requestAnimationFrame(...))` double-RAF used before adding `.entered`
- [ ] Above-fold elements (0–3) animate on load, not on scroll
- [ ] Below-fold elements use `IntersectionObserver` with `threshold: 0.1`
- [ ] `rootMargin: '0px 0px -80px 0px'` prevents elements entering only when nearly scrolled past
- [ ] Each element animates in only once (`scrollObserver.unobserve(el)` after trigger)

---

## 7. Banned Patterns Check

Each of these is an automatic fail:

- [ ] NOT using `transition: all` anywhere — too broad, animates non-compositable properties
- [ ] NOT using `animate-pulse` on multiple elements simultaneously
- [ ] NOT using `ease-in-out` as the primary easing for motion
- [ ] NOT using `h-screen` or `100vh` on full-height sections
- [ ] NOT using `window.addEventListener('scroll')` for animation calculations
- [ ] NOT using gradient text (`background-clip: text`) with gradient background — use solid color
- [ ] NOT using side-stripe `border-left/right` accents on cards (rewrite as background tint or full border)
- [ ] NOT placing decorative SVG "people" illustrations — always a real image or honest placeholder
- [ ] NOT auto-playing video without `prefers-reduced-motion` check
- [ ] NOT triggering layout recalculation inside animation frame (no reading `offsetWidth` in RAF loop)

---

## 8. Scroll Experience Integrity

- [ ] Pinned sections do not create unexpected jumps or scroll hijacking on mobile
- [ ] Horizontal scroll gallery has visible scroll indicator or is swipeable on touch
- [ ] Scroll progress indicators match actual scroll position (±5%)
- [ ] GSAP `scrub` value tuned (0.5–2.0 typical) — not `scrub: true` (that = `scrub: 1` but unintentional)
- [ ] Lenis (if used) does not conflict with browser native scroll restoration on route change

---

## 9. Accessibility

- [ ] Decorative canvases have `aria-hidden="true"`
- [ ] Marquee duplicates have `aria-hidden="true"` on the second copy
- [ ] Auto-moving marquee has `pause on focus` or `pause on hover` (WCAG 2.2 — 2.2.2)
- [ ] GSAP `pin` does not trap keyboard focus inside pinned section
- [ ] All interactive elements (magnetic buttons) remain keyboard-operable
- [ ] Focus ring visible on all interactive elements (not hidden by overflow/clip)
- [ ] Color contrast maintained against animated backgrounds (test with animation paused)

---

## Final Gate

Answer these four questions. Any "no" = do not ship.

| Question | Answer |
|---|---|
| Is the page fully usable with all animations disabled? | Yes / No |
| Does the page scroll smoothly at 60fps on a mid-range phone? | Yes / No |
| Does every animation serve a purpose (not just "because I can")? | Yes / No |
| Would the page survive a 3G connection gracefully? | Yes / No |

---

*Checklist version: global-design-skill v1.0 — `checklists/wow-effects-checklist.md`*  
*Updated: 2026-05-20*  
*Related: `rules/05-animation.md`, `rules/08-performance.md`, `rules/07-accessibility.md`, `patterns/effects/`*
