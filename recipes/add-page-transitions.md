# Recipe — Add Page Transitions

> How to make navigating between pages feel like a product, not a browser reload. Two layers: (1) first-load entrance sequence, (2) route-to-route transitions. With View Transitions API (Baseline 2024) and GSAP fallback.

---

## Layer 1 — First-Load Entrance Sequence

The page loads and elements arrive in a choreographed sequence. This is what makes a page feel "built" rather than "rendered".

### Step 1 — Assign `data-enter` roles

```html
<!-- Header arrives first -->
<header class="site-header" data-enter="0">...</header>

<!-- Hero text arrives second -->
<div class="hero-text" data-enter="1">...</div>

<!-- Hero visual arrives third (overlapping with text) -->
<div class="hero-visual" data-enter="2">...</div>

<!-- Below fold: animate on scroll, not on load -->
<section class="features" data-scroll-enter>...</section>
```

### Step 2 — Define the entrance animation

```css
/* Base state — all entered elements start invisible */
[data-enter] {
  opacity: 0;
  transform: translateY(12px);
  filter: blur(4px);
}

/* When JS adds .entered class */
[data-enter].entered {
  opacity: 1;
  transform: translateY(0);
  filter: blur(0);
  transition:
    opacity 700ms var(--ease-smooth),
    transform 700ms var(--ease-spring),
    filter 700ms var(--ease-smooth);
}

/* Stagger per group */
[data-enter="0"].entered { transition-delay: 0ms; }
[data-enter="1"].entered { transition-delay: 80ms; }
[data-enter="2"].entered { transition-delay: 160ms; }
[data-enter="3"].entered { transition-delay: 240ms; }

/* Scroll-triggered sections */
[data-scroll-enter] {
  opacity: 0;
  transform: translateY(24px);
  transition:
    opacity 600ms var(--ease-smooth),
    transform 600ms var(--ease-spring);
}

[data-scroll-enter].entered {
  opacity: 1;
  transform: translateY(0);
}

@media (prefers-reduced-motion: reduce) {
  [data-enter],
  [data-scroll-enter] {
    opacity: 1;
    transform: none;
    filter: none;
    transition: none;
  }
}
```

### Step 3 — Trigger on load

```javascript
// Fire entrance sequence after DOM is ready
document.addEventListener('DOMContentLoaded', () => {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  // Small delay ensures styles are applied before class is added
  requestAnimationFrame(() => {
    requestAnimationFrame(() => {
      document.querySelectorAll('[data-enter]').forEach(el => {
        el.classList.add('entered');
      });
    });
  });

  // Scroll observer for below-fold elements
  const scrollObserver = new IntersectionObserver(
    (entries) => entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('entered');
        scrollObserver.unobserve(entry.target);
      }
    }),
    { threshold: 0.1, rootMargin: '0px 0px -60px 0px' }
  );

  document.querySelectorAll('[data-scroll-enter]').forEach(el => scrollObserver.observe(el));
});
```

---

## Layer 2 — View Transitions API (Baseline 2024)

Native browser API for page transitions. No library needed. Works in Next.js, Astro, Remix, and vanilla.

### Basic setup (MPA / vanilla)

```css
/* Enable view transitions globally */
@view-transition {
  navigation: auto;
}

/* Default transition */
::view-transition-old(root),
::view-transition-new(root) {
  animation-duration: 300ms;
  animation-timing-function: var(--ease-smooth);
}

::view-transition-old(root) {
  animation-name: page-exit;
}

::view-transition-new(root) {
  animation-name: page-enter;
}

@keyframes page-exit {
  from { opacity: 1; transform: translateY(0); filter: blur(0); }
  to   { opacity: 0; transform: translateY(-8px); filter: blur(2px); }
}

@keyframes page-enter {
  from { opacity: 0; transform: translateY(8px); filter: blur(2px); }
  to   { opacity: 1; transform: translateY(0); filter: blur(0); }
}

@media (prefers-reduced-motion: reduce) {
  ::view-transition-old(root),
  ::view-transition-new(root) {
    animation: none;
  }
}
```

### Shared element transitions (hero image → detail page)

```css
/* Portfolio grid: each project card image has a unique name */
.project-card[data-project="alpha"] .project-img {
  view-transition-name: project-img-alpha;
}
.project-card[data-project="beta"] .project-img {
  view-transition-name: project-img-beta;
}

/* Detail page: same name on the hero image */
.project-detail[data-project="alpha"] .hero-img {
  view-transition-name: project-img-alpha;
}

/* Custom animation for the shared element */
::view-transition-old(project-img-alpha),
::view-transition-new(project-img-alpha) {
  animation-duration: 400ms;
  animation-timing-function: var(--ease-spring);
}
```

```html
<!-- Grid card -->
<a href="/projects/alpha" class="project-card" data-project="alpha">
  <img class="project-img" src="/alpha-thumb.jpg" alt="Project Alpha">
</a>

<!-- Detail page hero -->
<section class="project-detail" data-project="alpha">
  <img class="hero-img" src="/alpha-hero.jpg" alt="Project Alpha">
</section>
```

### Named element transitions

```css
/* Site logo slides between pages */
.site-logo { view-transition-name: site-logo; }

/* Page title morphs */
.page-title { view-transition-name: page-title; }

/* Sidebar stays fixed during nav */
.sidebar { view-transition-name: sidebar; }
::view-transition-old(sidebar),
::view-transition-new(sidebar) {
  /* No animation for sidebar — just instant update */
  animation: none;
}
```

---

## Layer 3 — Next.js App Router Transitions

```typescript
// app/layout.tsx
// Wrap page content with a transition provider

'use client';
import { useEffect, useRef } from 'react';
import { usePathname } from 'next/navigation';

export function PageTransition({ children }: { children: React.ReactNode }) {
  const pathname = usePathname();
  const containerRef = useRef<HTMLDivElement>(null);
  const prevPathname = useRef(pathname);

  useEffect(() => {
    if (prevPathname.current === pathname) return;
    prevPathname.current = pathname;

    if (!document.startViewTransition) {
      // Fallback for unsupported browsers
      containerRef.current?.classList.add('page-entering');
      setTimeout(() => {
        containerRef.current?.classList.remove('page-entering');
      }, 400);
      return;
    }

    // View Transitions are handled by the browser automatically
    // with @view-transition { navigation: auto } in CSS
  }, [pathname]);

  return (
    <div ref={containerRef} className="page-transition-wrapper">
      {children}
    </div>
  );
}
```

```css
/* Fallback for browsers without View Transitions API */
.page-transition-wrapper.page-entering {
  animation: page-enter 400ms var(--ease-smooth) both;
}
```

**Next.js CSS for View Transitions:**
```css
/* globals.css */
@view-transition {
  navigation: auto;
}

/* Customize per route type */
::view-transition-old(root) {
  animation: 250ms ease-in both fade-slide-out;
}

::view-transition-new(root) {
  animation: 350ms var(--ease-spring) both fade-slide-in;
}

@keyframes fade-slide-out {
  to { opacity: 0; transform: translateX(-20px); }
}

@keyframes fade-slide-in {
  from { opacity: 0; transform: translateX(20px); }
}
```

---

## Layer 4 — Loading Bar (Navigation Progress)

Shows a progress bar at the top during page navigation. Communicates that something is happening.

```html
<div class="nav-progress" role="progressbar" aria-label="Page loading" aria-hidden="true"></div>
```

```css
.nav-progress {
  position: fixed;
  top: 0;
  left: 0;
  height: 3px;
  background: var(--color-accent);
  z-index: var(--z-toast);
  transition: width 200ms var(--ease-smooth);
  width: 0;
  opacity: 0;
  box-shadow: 0 0 8px oklch(from var(--color-accent) l c h / 0.6);
}

.nav-progress.loading {
  opacity: 1;
}

.nav-progress.complete {
  width: 100% !important;
  opacity: 0;
  transition: width 200ms var(--ease-smooth), opacity 400ms var(--ease-smooth) 200ms;
}
```

```javascript
class NavigationProgress {
  constructor() {
    this.bar = document.querySelector('.nav-progress');
    this.fakeWidth = 0;
    this.interval = null;

    if (!this.bar) return;

    // Listen for navigation events
    document.addEventListener('click', (e) => {
      const link = e.target.closest('a[href]');
      if (!link) return;

      const href = link.getAttribute('href');
      if (href.startsWith('/') || href.startsWith('./')) {
        this.start();
      }
    });
  }

  start() {
    this.fakeWidth = 0;
    this.bar.style.width = '0';
    this.bar.classList.add('loading');
    this.bar.classList.remove('complete');

    // Fake progress until navigation completes
    this.interval = setInterval(() => {
      if (this.fakeWidth < 85) {
        this.fakeWidth += Math.random() * 15;
        this.bar.style.width = `${this.fakeWidth}%`;
      }
    }, 200);
  }

  complete() {
    clearInterval(this.interval);
    this.bar.classList.add('complete');
    setTimeout(() => {
      this.bar.classList.remove('loading', 'complete');
      this.bar.style.width = '0';
    }, 700);
  }
}

const progress = new NavigationProgress();

// Complete when new page loads
document.addEventListener('DOMContentLoaded', () => progress.complete());
```

---

## Complete Transition Setup Checklist

For a fully choreographed site:

- [ ] First-load sequence: `[data-enter]` attributes on all above-fold elements
- [ ] Entrance animation CSS with stagger delays
- [ ] `IntersectionObserver` for below-fold scroll reveals
- [ ] `@view-transition { navigation: auto }` in global CSS
- [ ] Custom `::view-transition-*` animations defined
- [ ] Shared element transitions for navigable content (portfolio, blog)
- [ ] Loading progress bar for navigation feedback
- [ ] `prefers-reduced-motion` fallback on every animation
- [ ] Navigation progress bar initialized
- [ ] Test: reduce motion preference — page must still be fully readable

---

## What Each Pattern Costs

| Pattern | Bundle cost | Render cost | Wow impact |
|---|---|---|---|
| First-load entrance | 0kb (CSS + 20 lines JS) | Minimal | Very high |
| View Transitions API | 0kb (native) | Minimal | Very high |
| Shared element transitions | 0kb | Minimal | Extreme (on portfolio) |
| Navigation progress bar | ~1kb | Minimal | Medium |
| GSAP page transitions | ~30kb | Low | High |
| Lenis smooth scroll | ~8kb | Low | High |

**Recommended minimum stack:**
1. First-load entrance sequence (free)
2. `@view-transition { navigation: auto }` (free)
3. `prefers-reduced-motion` fallback (free)

Everything above 3 is additive — not required for a wow experience.

---

*Recipe version: global-design-skill v1.0 — `recipes/add-page-transitions.md`*  
*Updated: 2026-05-20*  
*Related: `patterns/effects/scroll-experiences.md`, `patterns/effects/text-animations.md`, `rules/05-animation.md`*
