# Pattern — Scroll Experiences

> Scroll is the primary interaction on the web. These patterns turn passive scrolling into active storytelling. Each pattern includes a working implementation and a judgment guide for when to use it.

---

## Pattern 1 — Smooth Scroll (Lenis)

The invisible foundation. Native browser scroll is jerky — Lenis adds momentum that makes pages feel expensive.

```bash
npm install @studio-freight/lenis
```

```javascript
import Lenis from '@studio-freight/lenis';

const lenis = new Lenis({
  duration: 1.2,          // Scroll inertia (1.0 = default, 1.5 = very smooth)
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),  // Expo out
  orientation: 'vertical',
  smoothWheel: true,
  wheelMultiplier: 1,
  touchMultiplier: 2,
  infinite: false
});

// GSAP ScrollTrigger integration (if using GSAP)
import { ScrollTrigger } from 'gsap/ScrollTrigger';
lenis.on('scroll', ScrollTrigger.update);

// RAF loop
function raf(time) {
  lenis.raf(time);
  requestAnimationFrame(raf);
}
requestAnimationFrame(raf);

// Pause during modals/dialogs
document.addEventListener('dialog-open', () => lenis.stop());
document.addEventListener('dialog-close', () => lenis.start());

// Reduced motion: disable smooth scroll
if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  // Don't initialize Lenis — native scroll is better for reduced-motion users
}
```

**CSS scroll behavior fallback (when not using Lenis):**
```css
@media (prefers-reduced-motion: no-preference) {
  html {
    scroll-behavior: smooth;
  }
}
```

---

## Pattern 2 — Pinned Section (Cards Stack on Scroll)

Section stays pinned while child cards animate in. Creates the impression of cards physically stacking.

```html
<section class="pin-section">
  <div class="pin-container">
    <div class="stack-card stack-card--1">
      <h3>Step 1 — Push to GitHub</h3>
      <p>Connect your repository once. Every push triggers an automatic build.</p>
    </div>
    <div class="stack-card stack-card--2">
      <h3>Step 2 — Global CDN</h3>
      <p>Your build deploys to 40 edge locations simultaneously.</p>
    </div>
    <div class="stack-card stack-card--3">
      <h3>Step 3 — Live in 23 seconds</h3>
      <p>Preview URLs generated instantly. Your team reviews before production.</p>
    </div>
  </div>
</section>
```

```css
.pin-section {
  /* Height = pinned duration — 300vh means 3 viewport heights of scroll distance */
  height: 300vh;
  position: relative;
}

.pin-container {
  position: sticky;
  top: 0;
  height: 100dvh;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.stack-card {
  position: absolute;
  width: min(500px, 90vw);
  padding: var(--space-8);
  background: var(--color-surface-2);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-xl);
}
```

```javascript
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
gsap.registerPlugin(ScrollTrigger);

const mm = gsap.matchMedia();

mm.add('(prefers-reduced-motion: no-preference)', () => {

  const cards = gsap.utils.toArray('.stack-card');

  cards.forEach((card, i) => {
    const isLast = i === cards.length - 1;

    gsap.from(card, {
      yPercent: 100,
      opacity: 0,
      scale: 0.9,
      scrollTrigger: {
        trigger: '.pin-section',
        start: `top+=${i * 100}% top`,
        end: `top+=${(i + 1) * 100}% top`,
        scrub: 0.8
      }
    });

    if (!isLast) {
      // Previous cards scale down as new one arrives
      gsap.to(card, {
        scale: 0.92,
        yPercent: -8 * (cards.length - i - 1),
        scrollTrigger: {
          trigger: '.pin-section',
          start: `top+=${(i + 1) * 100}% top`,
          end: `top+=${(i + 2) * 100}% top`,
          scrub: 0.8
        }
      });
    }
  });

});

// Fallback: show all cards stacked without animation
mm.add('(prefers-reduced-motion: reduce)', () => {
  gsap.utils.toArray('.stack-card').forEach((card, i) => {
    card.style.position = 'relative';
    card.style.transform = `translateY(${i * 20}px)`;
    card.style.marginBottom = `${i < 2 ? -160 : 0}px`;
  });
});
```

---

## Pattern 3 — Horizontal Scroll Gallery

A section where vertical scroll is translated into horizontal movement. Best for portfolios, feature galleries, and timelines.

```html
<section class="h-scroll-section">
  <div class="h-scroll-track">
    <div class="h-scroll-item">
      <img src="/work-1.jpg" alt="Project 1">
      <h3>Project 1</h3>
    </div>
    <div class="h-scroll-item">
      <img src="/work-2.jpg" alt="Project 2">
      <h3>Project 2</h3>
    </div>
    <div class="h-scroll-item">...</div>
    <div class="h-scroll-item">...</div>
    <div class="h-scroll-item">...</div>
  </div>
</section>
```

```css
.h-scroll-section {
  /* Height = how much vertical scroll triggers horizontal movement */
  /* items × 60vw = total horizontal distance to cover */
  height: calc(5 * 60vw);
}

.h-scroll-track {
  position: sticky;
  top: 0;
  height: 100dvh;
  display: flex;
  align-items: center;
  gap: var(--space-8);
  padding-inline: var(--space-10);
  /* Start off-screen right */
  transform: translateX(var(--h-scroll-x, 0));
  will-change: transform;
}

.h-scroll-item {
  flex-shrink: 0;
  width: 55vw;
  max-width: 720px;
}

.h-scroll-item img {
  width: 100%;
  aspect-ratio: 16 / 9;
  object-fit: cover;
  border-radius: var(--radius-xl);
}
```

```javascript
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
gsap.registerPlugin(ScrollTrigger);

const mm = gsap.matchMedia();

mm.add('(prefers-reduced-motion: no-preference)', () => {

  const section = document.querySelector('.h-scroll-section');
  const track = document.querySelector('.h-scroll-track');

  const getScrollAmount = () => {
    return -(track.scrollWidth - window.innerWidth);
  };

  gsap.to(track, {
    x: getScrollAmount,
    ease: 'none',
    scrollTrigger: {
      trigger: section,
      start: 'top top',
      end: () => `+=${track.scrollWidth}`,
      scrub: 1,
      pin: true,
      invalidateOnRefresh: true
    }
  });

});

// Mobile: disable horizontal scroll, use normal vertical flow
mm.add('(max-width: 768px)', () => {
  const section = document.querySelector('.h-scroll-section');
  if (section) {
    section.style.height = 'auto';
    const track = document.querySelector('.h-scroll-track');
    if (track) {
      track.style.position = 'relative';
      track.style.flexWrap = 'wrap';
      track.style.transform = 'none';
    }
  }
});
```

---

## Pattern 4 — Reading Progress Bar

Thin line at the top showing how far through an article the user has scrolled.

```html
<div class="reading-progress" role="progressbar" aria-label="Reading progress" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0"></div>
```

```css
/* CSS-only via scroll-driven animations (Baseline 2024) */
@keyframes progress-grow {
  from { transform: scaleX(0); }
  to   { transform: scaleX(1); }
}

.reading-progress {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: var(--color-accent);
  transform-origin: left center;
  z-index: var(--z-sticky);
  animation: progress-grow linear both;
  animation-timeline: scroll(root block);

  /* Subtle glow */
  box-shadow: 0 0 8px oklch(from var(--color-accent) l c h / 0.6);
}

@media (prefers-reduced-motion: reduce) {
  .reading-progress { display: none; }
}
```

---

## Pattern 5 — Section Reveal Sequence

Every section on the page appears with a staggered entrance. Creates page-level choreography.

```css
/* Each section type has a reveal class */
.reveal {
  opacity: 0;
  transform: translateY(32px);
  transition:
    opacity 600ms var(--ease-smooth),
    transform 600ms var(--ease-spring);
  transition-delay: var(--reveal-delay, 0ms);
}

.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}

/* Stagger children within a section */
.reveal-stagger > * {
  opacity: 0;
  transform: translateY(20px);
  transition:
    opacity 500ms var(--ease-smooth),
    transform 500ms var(--ease-spring);
}

.reveal-stagger.visible > *:nth-child(1) { transition-delay: 0ms; }
.reveal-stagger.visible > *:nth-child(2) { transition-delay: 80ms; }
.reveal-stagger.visible > *:nth-child(3) { transition-delay: 160ms; }
.reveal-stagger.visible > *:nth-child(4) { transition-delay: 240ms; }
.reveal-stagger.visible > *:nth-child(5) { transition-delay: 320ms; }
.reveal-stagger.visible > *:nth-child(6) { transition-delay: 400ms; }

.reveal-stagger.visible > * {
  opacity: 1;
  transform: translateY(0);
}

@media (prefers-reduced-motion: reduce) {
  .reveal,
  .reveal-stagger > * {
    opacity: 1;
    transform: none;
    transition: none;
  }
}
```

```javascript
// Single observer for all reveal elements
const revealObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        revealObserver.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.1, rootMargin: '0px 0px -60px 0px' }
);

document.querySelectorAll('.reveal, .reveal-stagger').forEach(el => {
  revealObserver.observe(el);
});
```

---

## Pattern 6 — Scroll-Linked Opacity Fade

Hero content fades out as user scrolls down — creates depth and "leaving the surface" effect.

```javascript
if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  const hero = document.querySelector('.hero');
  const heroContent = document.querySelector('.hero__content');

  function updateHeroOpacity() {
    const scrollProgress = window.scrollY / window.innerHeight;
    const opacity = Math.max(0, 1 - scrollProgress * 2); // Fades out by 50% scroll
    heroContent.style.opacity = opacity;
    heroContent.style.transform = `translateY(${scrollProgress * 30}px)`;
  }

  // Only when hero is visible
  const observer = new IntersectionObserver(([entry]) => {
    if (entry.isIntersecting) {
      window.addEventListener('scroll', updateHeroOpacity, { passive: true });
    } else {
      window.removeEventListener('scroll', updateHeroOpacity);
    }
  });
  observer.observe(hero);
}
```

**CSS scroll-driven version (Baseline 2024):**
```css
@keyframes hero-fade {
  from { opacity: 1; transform: translateY(0); }
  to   { opacity: 0; transform: translateY(-30px); }
}

.hero__content {
  animation: hero-fade linear both;
  animation-timeline: scroll(root);
  animation-range: 0% 50vh;  /* Fully faded out by 50vh of scroll */
}

@media (prefers-reduced-motion: reduce) {
  .hero__content { animation: none; }
}
```

---

## Pattern 7 — Scroll-Triggered Counter Section

Stats that count up when scrolled into view — see `patterns/effects/text-animations.md` for the CountUp class.

```html
<section class="stats-section reveal-stagger">
  <div class="stat">
    <span class="stat__value" data-count-up data-target="18000" data-suffix="+" data-duration="2500">18,000+</span>
    <span class="stat__label">Teams worldwide</span>
  </div>
  <div class="stat">
    <span class="stat__value" data-count-up data-target="99.9" data-suffix="%" data-decimals="1" data-duration="2000">99.9%</span>
    <span class="stat__label">Uptime SLA</span>
  </div>
  <div class="stat">
    <span class="stat__value" data-count-up data-target="23" data-suffix="s" data-duration="1500">23s</span>
    <span class="stat__label">Average deploy time</span>
  </div>
</section>
```

---

## Pattern 8 — Scroll Snap

Full-page sections that snap between them — creates a slide-like experience.

```css
.snap-container {
  height: 100dvh;
  overflow-y: scroll;
  scroll-snap-type: y mandatory;
  /* Use 'proximity' for soft snapping that doesn't force every section */
}

.snap-section {
  height: 100dvh;
  scroll-snap-align: start;
  scroll-snap-stop: always; /* Forces user to stop at each section */
}

/* Smooth entry animation per section */
.snap-section > .snap-content {
  opacity: 0;
  transform: translateY(20px);
  transition:
    opacity 600ms var(--ease-smooth),
    transform 600ms var(--ease-spring);
}

/* :has() triggers when section is snapped into view */
.snap-section:is(:has(> :target), :snapped) > .snap-content {
  opacity: 1;
  transform: translateY(0);
}

@media (prefers-reduced-motion: reduce) {
  .snap-container { scroll-snap-type: none; }
  .snap-section > .snap-content { opacity: 1; transform: none; }
}
```

---

## When to Use Each Pattern

| Pattern | Use case | Avoid when |
|---|---|---|
| Smooth scroll (Lenis) | Any multi-section site | Accessibility-first — always pair with reduced-motion check |
| Pinned stacking cards | Feature storytelling, step-by-step processes | More than 4–5 cards (gets tedious) |
| Horizontal scroll gallery | Portfolio, product showcase, timeline | Long text content, anything that needs deep scrolling within items |
| Reading progress | Long articles, documentation, blogs | Single-screen pages, marketing pages |
| Section reveal | Any page with multiple sections | Pages where content needs to be indexed by search bots (content exists but is invisible) |
| Scroll-linked opacity | Hero sections with dramatic entrances | Interfaces where content recall matters |
| Scroll snap | Slideshow-style narratives, onboarding | Irregular section heights, content-heavy pages |

---

*Pattern version: global-design-skill v1.0 — `patterns/effects/scroll-experiences.md`*  
*Updated: 2026-05-20*  
*Related: `patterns/effects/parallax-system.md`, `patterns/effects/text-animations.md`, `rules/05-animation.md`*
