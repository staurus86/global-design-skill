# Pattern — Parallax System

> Complete parallax toolkit: CSS-only, JavaScript scroll-based, mouse-tracking, and GSAP ScrollTrigger implementations. Each level has a use case and a performance note. Always include `prefers-reduced-motion` fallback.

---

## Level 1 — CSS Parallax (Zero JS, Best Performance)

Pure CSS parallax using `perspective` and `translateZ` on scroll. Works without any JavaScript.

```html
<div class="parallax-scene">
  <div class="parallax-layer parallax-layer--bg">
    <!-- Slowest: background image or gradient -->
  </div>
  <div class="parallax-layer parallax-layer--mid">
    <!-- Medium: decorative elements -->
  </div>
  <div class="parallax-layer parallax-layer--fg">
    <!-- Fastest: content -->
  </div>
</div>
```

```css
.parallax-scene {
  perspective: 1px;
  height: 100dvh;
  overflow-x: hidden;
  overflow-y: auto;
}

.parallax-layer {
  position: absolute;
  inset: 0;
}

/* Background: 60% scroll speed (moves slower) */
.parallax-layer--bg {
  transform: translateZ(-1px) scale(2);
}

/* Mid: 80% scroll speed */
.parallax-layer--mid {
  transform: translateZ(-0.5px) scale(1.5);
}

/* Foreground: 100% scroll speed (normal) */
.parallax-layer--fg {
  transform: translateZ(0);
}

@media (prefers-reduced-motion: reduce) {
  .parallax-layer {
    transform: none !important;
  }
  .parallax-scene {
    perspective: none;
  }
}
```

**Formula:** `scale = 1 + (abs(translateZ) / perspective)`  
If `perspective: 1px` and `translateZ: -1px`, then `scale = 2`.

**Performance:** 100% GPU-composited, zero JS, zero layout recalc.  
**Limitation:** Requires the container to be the scroll root; doesn't work with sticky headers.

---

## Level 2 — JS Scroll Parallax (IntersectionObserver + CSS variables)

The recommended default for most cases. Uses `IntersectionObserver` for entry, then updates CSS variables on scroll.

```html
<section class="section-parallax" data-parallax-speed="0.3">
  <div class="parallax-bg"></div>
  <div class="parallax-content">
    <h2>Section heading</h2>
  </div>
</section>
```

```css
.section-parallax {
  position: relative;
  overflow: hidden;
  min-height: 600px;
}

.parallax-bg {
  position: absolute;
  inset: -20%;     /* Oversized so parallax doesn't reveal edges */
  background-image: url('/image.jpg');
  background-size: cover;
  background-position: center;
  transform: translateY(var(--parallax-offset, 0));
  will-change: transform;  /* Only set when actively scrolling */
}

@media (prefers-reduced-motion: reduce) {
  .parallax-bg {
    transform: none;
    inset: 0;
  }
}
```

```javascript
class ParallaxSystem {
  constructor() {
    this.elements = [];
    this.ticking = false;

    // Check prefers-reduced-motion
    this.reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (this.reducedMotion) return;

    this.init();
  }

  init() {
    document.querySelectorAll('[data-parallax-speed]').forEach(el => {
      const bg = el.querySelector('.parallax-bg');
      if (!bg) return;

      this.elements.push({
        el,
        bg,
        speed: parseFloat(el.dataset.parallaxSpeed) || 0.3
      });

      // Pre-enable GPU compositing only when in view
      const observer = new IntersectionObserver(([entry]) => {
        bg.style.willChange = entry.isIntersecting ? 'transform' : 'auto';
      }, { rootMargin: '100px' });
      observer.observe(el);
    });

    window.addEventListener('scroll', () => this.requestTick(), { passive: true });
    this.update(); // Initial position
  }

  requestTick() {
    if (!this.ticking) {
      requestAnimationFrame(() => {
        this.update();
        this.ticking = false;
      });
      this.ticking = true;
    }
  }

  update() {
    const scrollY = window.scrollY;

    this.elements.forEach(({ el, bg, speed }) => {
      const rect = el.getBoundingClientRect();
      const elTop = rect.top + scrollY;
      const relativeScroll = scrollY - elTop + window.innerHeight;
      const offset = relativeScroll * speed * -1;

      bg.style.setProperty('--parallax-offset', `${offset}px`);
    });
  }
}

new ParallaxSystem();
```

---

## Level 3 — Multi-Layer Parallax (Different Speeds)

Multiple elements moving at different speeds creates true depth.

```html
<section class="multi-parallax">
  <!-- Layer 1: slowest (deepest) -->
  <div class="mp-layer" data-speed="0.1">
    <img src="/mountains-far.png" alt="" aria-hidden="true" class="layer-img layer-img--far">
  </div>
  <!-- Layer 2: medium -->
  <div class="mp-layer" data-speed="0.25">
    <img src="/mountains-mid.png" alt="" aria-hidden="true" class="layer-img layer-img--mid">
  </div>
  <!-- Layer 3: fast (closest to viewer) -->
  <div class="mp-layer" data-speed="0.4">
    <img src="/mountains-near.png" alt="" aria-hidden="true" class="layer-img layer-img--near">
  </div>
  <!-- Content layer: fixed, no parallax -->
  <div class="mp-content">
    <h1>Heading above all layers</h1>
  </div>
</section>
```

```css
.multi-parallax {
  position: relative;
  height: 100dvh;
  overflow: hidden;
}

.mp-layer {
  position: absolute;
  inset: 0;
  transform: translateY(var(--mp-offset, 0));
  will-change: transform;
}

.layer-img {
  width: 100%;
  height: 120%;         /* Extra height compensates for parallax movement */
  object-fit: cover;
  object-position: center bottom;
}

.mp-content {
  position: relative;
  z-index: 10;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}
```

```javascript
// Multi-layer parallax
const layers = document.querySelectorAll('.mp-layer[data-speed]');

function updateLayers() {
  const scrolled = window.scrollY;
  layers.forEach(layer => {
    const speed = parseFloat(layer.dataset.speed);
    layer.style.setProperty('--mp-offset', `${scrolled * speed}px`);
  });
}

if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  window.addEventListener('scroll', () => requestAnimationFrame(updateLayers), { passive: true });
}
```

---

## Level 4 — Mouse-Tracking Parallax (3D Depth Illusion)

Elements shift based on cursor position, creating a 3D parallax depth effect. Best on hero sections and product screenshots.

```html
<div class="mouse-parallax" data-mouse-parallax>
  <div class="mp-item" data-depth="0.02">
    <img src="/hero-bg.png" alt="" aria-hidden="true">
  </div>
  <div class="mp-item" data-depth="0.05">
    <img src="/hero-mid.png" alt="" aria-hidden="true">
  </div>
  <div class="mp-item" data-depth="0.1">
    <div class="hero-product-screenshot">...</div>
  </div>
</div>
```

```css
.mouse-parallax {
  position: relative;
  overflow: hidden;
  transform-style: preserve-3d;
}

.mp-item {
  position: absolute;
  inset: 0;
  transform: translate(var(--mp-x, 0), var(--mp-y, 0));
  transition: transform 150ms linear;  /* Smooths mouse jitter */
  will-change: transform;
}

/* The slowest transition creates the motion blur feel */
.mp-item[data-depth="0.02"] { transition-duration: 200ms; }
.mp-item[data-depth="0.05"] { transition-duration: 150ms; }
.mp-item[data-depth="0.1"]  { transition-duration: 80ms; }

@media (prefers-reduced-motion: reduce) {
  .mp-item { transform: none !important; transition: none; }
}
```

```javascript
class MouseParallax {
  constructor(el) {
    this.el = el;
    this.items = [...el.querySelectorAll('[data-depth]')];
    this.center = { x: 0, y: 0 };
    this.current = { x: 0, y: 0 };
    this.target = { x: 0, y: 0 };

    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    this.observe();
  }

  observe() {
    this.el.addEventListener('mousemove', (e) => {
      const rect = this.el.getBoundingClientRect();
      // Normalize to -0.5 to +0.5 range
      this.target.x = (e.clientX - rect.left) / rect.width - 0.5;
      this.target.y = (e.clientY - rect.top) / rect.height - 0.5;
    });

    this.el.addEventListener('mouseleave', () => {
      this.target.x = 0;
      this.target.y = 0;
    });

    this.animate();
  }

  animate() {
    // Lerp (linear interpolation) for smooth follow
    this.current.x += (this.target.x - this.current.x) * 0.08;
    this.current.y += (this.target.y - this.current.y) * 0.08;

    this.items.forEach(item => {
      const depth = parseFloat(item.dataset.depth) || 0.05;
      const moveX = this.current.x * depth * 100;
      const moveY = this.current.y * depth * 100;
      item.style.setProperty('--mp-x', `${moveX}px`);
      item.style.setProperty('--mp-y', `${moveY}px`);
    });

    requestAnimationFrame(() => this.animate());
  }
}

document.querySelectorAll('[data-mouse-parallax]').forEach(el => new MouseParallax(el));
```

---

## Level 5 — GSAP ScrollTrigger Parallax

The most powerful option. Use when you need exact control, scrubbing, or pinning.

```bash
npm install gsap
```

```javascript
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
gsap.registerPlugin(ScrollTrigger);

// Check reduced motion first
const mm = gsap.matchMedia();

mm.add('(prefers-reduced-motion: no-preference)', () => {

  // Basic parallax — element moves at 30% of scroll speed
  gsap.to('.parallax-element', {
    yPercent: -30,
    ease: 'none',   // Critical: no easing on scroll-linked animations
    scrollTrigger: {
      trigger: '.parallax-section',
      start: 'top bottom',
      end: 'bottom top',
      scrub: true   // Ties animation to scroll position
    }
  });

  // Hero multi-layer parallax
  const heroTl = gsap.timeline({
    scrollTrigger: {
      trigger: '.hero',
      start: 'top top',
      end: 'bottom top',
      scrub: 1  // Number = seconds of lag behind scroll
    }
  });

  heroTl
    .to('.hero-bg', { yPercent: 20, ease: 'none' }, 0)
    .to('.hero-mid', { yPercent: 10, ease: 'none' }, 0)
    .to('.hero-content', { yPercent: 5, opacity: 0, ease: 'none' }, 0);

  // Section fade-in on scroll (not parallax but always paired with it)
  gsap.utils.toArray('.reveal-section').forEach(section => {
    gsap.fromTo(section,
      { y: 60, opacity: 0 },
      {
        y: 0,
        opacity: 1,
        duration: 1,
        ease: 'power2.out',
        scrollTrigger: {
          trigger: section,
          start: 'top 80%',
          toggleActions: 'play none none reverse'
        }
      }
    );
  });

});
```

**Sticky-pin parallax (cards stack on top of each other):**
```javascript
mm.add('(prefers-reduced-motion: no-preference)', () => {

  const cards = gsap.utils.toArray('.stack-card');
  const totalCards = cards.length;

  cards.forEach((card, i) => {
    gsap.to(card, {
      scale: 1 - (totalCards - i - 1) * 0.05,
      yPercent: -15 * (totalCards - i - 1),
      ease: 'none',
      scrollTrigger: {
        trigger: card,
        start: 'top top+=80',
        end: `+=${totalCards * 100}%`,
        pin: true,
        pinSpacing: false,
        scrub: 0.5
      }
    });
  });

});
```

---

## Level 6 — CSS Scroll-Driven Animations (Baseline 2024, No JS)

Native browser API — no library needed. Animates elements based on scroll position.

```css
/* Reading progress bar */
@keyframes progress {
  from { transform: scaleX(0); }
  to   { transform: scaleX(1); }
}

.progress-bar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: var(--color-accent);
  transform-origin: left;
  animation: progress linear;
  animation-timeline: scroll();
  animation-fill-mode: both;
}

/* Fade-in on scroll (no IntersectionObserver needed) */
@keyframes fade-in-up {
  from { opacity: 0; transform: translateY(40px); }
  to   { opacity: 1; transform: translateY(0); }
}

.scroll-reveal {
  animation: fade-in-up linear both;
  animation-timeline: view();
  animation-range: entry 0% entry 30%;
}

/* Parallax via scroll-driven (most performant possible) */
@keyframes parallax-move {
  from { transform: translateY(0); }
  to   { transform: translateY(-20%); }
}

.scroll-parallax-bg {
  animation: parallax-move linear;
  animation-timeline: scroll(root);
  animation-fill-mode: both;
}

/* Staggered reveal for card grid */
.card:nth-child(1) { animation-delay: 0ms; }
.card:nth-child(2) { animation-delay: 75ms; }
.card:nth-child(3) { animation-delay: 150ms; }
.card:nth-child(4) { animation-delay: 225ms; }

.card {
  animation: fade-in-up 600ms var(--ease-spring) both;
  animation-timeline: view();
  animation-range: entry 0% entry 40%;
}

/* Respect reduced-motion */
@media (prefers-reduced-motion: reduce) {
  .scroll-reveal,
  .scroll-parallax-bg,
  .card {
    animation: none;
    opacity: 1;
    transform: none;
  }
}
```

---

## Parallax Decision Guide

| Scenario | Best approach | Why |
|---|---|---|
| Background image in hero | CSS `perspective` parallax or Scroll-driven | Zero JS, GPU composited |
| Multi-layer scene (3+ layers) | JS scroll with RAF | CSS perspective requires specific DOM structure |
| Hover depth effect | Mouse-tracking parallax | Scroll-based doesn't work on hover |
| Pinned scroll sections | GSAP ScrollTrigger | CSS scroll-driven can't pin |
| Staggered section reveals | CSS scroll-driven `view()` | Baseline 2024, cleanest API |
| Complex scroll choreography | GSAP ScrollTrigger timeline | Full control, scrub, sequencing |
| Reading progress bar | CSS scroll-driven `scroll()` | One line of CSS |

---

*Pattern version: global-design-skill v1.0 — `patterns/effects/parallax-system.md`*  
*Updated: 2026-05-20*  
*Related: `patterns/effects/visual-effects.md`, `patterns/effects/scroll-experiences.md`, `rules/05-animation.md`*
