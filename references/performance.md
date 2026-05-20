# Reference — Performance

> Core Web Vitals targets, LCP optimization, CLS prevention, INP patterns, image strategy, font loading, and bundle size control. Performance is a design requirement, not a post-launch task.

---

## Core Web Vitals Targets

| Metric | Good | Needs work | Poor | Measure |
|---|---|---|---|---|
| **LCP** (Largest Contentful Paint) | ≤ 2.5s | 2.5–4s | > 4s | First load, mobile |
| **CLS** (Cumulative Layout Shift) | ≤ 0.1 | 0.1–0.25 | > 0.25 | All loads |
| **INP** (Interaction to Next Paint) | ≤ 200ms | 200–500ms | > 500ms | All interactions |

**Target from global-design-skill:** Lighthouse Performance ≥ 88 on mobile throttled (4G, 4× CPU slowdown).

---

## LCP — Largest Contentful Paint

LCP is almost always the hero image or hero text.

### Identify the LCP element

```html
<!-- The LCP element is usually the first large image -->
<img
  src="/hero.webp"
  alt="Hero"
  width="1440"
  height="810"
  fetchpriority="high"    <!-- CRITICAL: tells browser to load immediately -->
  decoding="async"
  loading="eager"         <!-- NOT lazy — LCP must not be lazy-loaded -->
/>
```

### Hero image optimization

```html
<!-- Responsive LCP with art direction -->
<picture>
  <!-- WebP for modern browsers -->
  <source
    type="image/webp"
    media="(min-width: 768px)"
    srcset="/hero-desktop.webp 1440w, /hero-desktop@2x.webp 2880w"
    sizes="100vw"
  />
  <source
    type="image/webp"
    srcset="/hero-mobile.webp 390w, /hero-mobile@2x.webp 780w"
    sizes="100vw"
  />
  <!-- AVIF fallback for maximum compression -->
  <img
    src="/hero.jpg"
    alt="Hero"
    width="1440"
    height="810"
    fetchpriority="high"
    decoding="async"
  />
</picture>
```

### Preload LCP image (Next.js 15)

```tsx
import Image from 'next/image'

// Next.js Image component handles LCP optimization automatically
<Image
  src="/hero.webp"
  alt="Hero image"
  width={1440}
  height={810}
  priority           // sets fetchpriority="high" + preload link
  quality={85}
/>
```

---

## CLS — Cumulative Layout Shift

CLS is caused by elements changing size after the page loads. Common culprits: images without dimensions, web fonts, dynamic content injection.

### Always set image dimensions

```html
<!-- Every img must have width + height -->
<img src="/card.webp" alt="..." width="600" height="400" />

<!-- Or use aspect-ratio in CSS -->
<div style="aspect-ratio: 16/9">
  <img src="/card.webp" alt="..." style="width: 100%; height: 100%; object-fit: cover;" />
</div>
```

```css
/* Reserve space for images before they load */
.image-container {
  aspect-ratio: 16 / 9;
  background: var(--color-surface-2);
  overflow: hidden;
}

.image-container img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```

### Font CLS prevention

See `references/typography.md` — use `size-adjust` fallback + `font-display: optional`.

```css
@font-face {
  font-family: 'Instrument Sans Fallback';
  src: local('Arial');
  ascent-override: 94%;
  descent-override: 24%;
  line-gap-override: 0%;
  size-adjust: 100.6%;  /* measured against actual loaded font */
}
```

### Dynamic content — reserve space

```css
/* Skeleton preserves layout space before data loads */
.user-card-skeleton {
  height: 96px;           /* matches loaded state */
  border-radius: var(--radius-lg);
  background: var(--color-surface-2);
}

/* Tab panel — don't shift layout when tab changes */
.tab-panel {
  min-height: 400px;      /* minimum prevents sudden collapse */
}
```

---

## INP — Interaction to Next Paint

INP measures time from user interaction to next frame paint. Kept ≤ 200ms by:

1. **Avoid long tasks** — code that runs > 50ms on main thread
2. **Defer non-critical JS** — use `setTimeout(fn, 0)` or `requestIdleCallback`
3. **Use CSS transitions** — not JS-driven style changes
4. **Optimistic updates** — update UI immediately, confirm later

```tsx
/* React 19 — optimistic update for instant feedback */
import { useOptimistic } from 'react'

function LikeButton({ post }: { post: Post }) {
  const [count, addOptimistic] = useOptimistic(post.likes)

  async function handleLike() {
    addOptimistic(count + 1)       // UI updates instantly
    await likePost(post.id)        // server confirms async
  }

  return <button onClick={handleLike}>{count} likes</button>
}
```

```ts
/* Defer non-critical work */
button.addEventListener('click', () => {
  updateUI()  // synchronous — immediate visual feedback

  // Defer analytics, logging, non-visual work
  requestIdleCallback(() => {
    trackEvent('button_clicked')
    syncToServer()
  })
})
```

---

## Image Optimization

### Format selection

| Format | Use when | Support |
|---|---|---|
| WebP | Default for photos, screenshots | Universal modern |
| AVIF | Maximum compression (30–50% smaller than WebP) | Chrome 85+, Firefox 93+, Safari 16+ |
| SVG | Icons, logos, diagrams (vector) | Universal |
| PNG | Transparency with sharp edges | Universal |
| JPEG | Legacy fallback only | Universal |

### Lazy loading

```html
<!-- Lazy load everything below the fold -->
<img src="/feature.webp" alt="..." width="600" height="400" loading="lazy" />

<!-- Never lazy-load above-fold / LCP images -->
<img src="/hero.webp" alt="..." width="1440" height="810" fetchpriority="high" />
```

### Blur placeholder (low-quality image placeholder)

```tsx
/* Next.js Image with blur placeholder */
<Image
  src="/feature.webp"
  alt="Feature preview"
  width={600}
  height={400}
  placeholder="blur"
  blurDataURL="data:image/webp;base64,..."   /* tiny base64 */
  loading="lazy"
/>
```

---

## Font Performance

```html
<!-- 1. Preload the primary display font only -->
<link rel="preload" href="/fonts/playfair-display-variable.woff2" as="font" type="font/woff2" crossorigin />

<!-- 2. Load only needed weight range -->
<!-- Bad: font-weight: 100 900 (full axis) -->
<!-- Good: font-weight: 400 700 (only what you use) -->
```

```css
/* 3. Self-host variable fonts — eliminates Google Fonts round-trip */
@font-face {
  font-family: 'Instrument Sans';
  src: url('/fonts/instrument-sans-variable.woff2') format('woff2-variations');
  font-weight: 400 700;
  font-style: normal;
  font-display: optional;
}
```

---

## JavaScript Bundle

### Lazy-load heavy components (Next.js 15)

```tsx
import dynamic from 'next/dynamic'
import { Suspense } from 'react'

/* Below-fold 3D scene — don't include in initial bundle */
const Scene3D = dynamic(() => import('@/components/Scene3D'), {
  ssr: false,
  loading: () => <div className="skeleton-container" style={{ height: 400 }} />,
})

/* Rich text editor — only load when user clicks "edit" */
const RichEditor = dynamic(() => import('@/components/RichEditor'), {
  ssr: false,
})
```

### Tree-shaking — import only what you use

```tsx
/* Wrong — imports entire library */
import * as motion from 'motion/react'

/* Correct — named imports only */
import { motion, AnimatePresence } from 'motion/react'
```

---

## Next.js 15 Performance Patterns

```tsx
/* No-store by default (changed from v14) — be explicit */
const data = await fetch('/api/data', {
  next: { revalidate: 3600 }  // cache 1 hour
})

/* New "use cache" directive */
async function getExpensiveData() {
  'use cache'
  cacheLife('hours')
  return db.query(...)
}

/* Streaming — show UI progressively */
import { Suspense } from 'react'

export default function Page() {
  return (
    <main>
      <HeroSection />        {/* immediate — static */}
      <Suspense fallback={<StatsSkeleton />}>
        <LiveStats />          {/* streamed — async data */}
      </Suspense>
      <Suspense fallback={<FeedSkeleton />}>
        <ActivityFeed />       {/* streamed — slower query */}
      </Suspense>
    </main>
  )
}
```

---

## Performance Checklist

```
[ ] LCP element identified — hero image or H1
[ ] fetchpriority="high" on LCP image
[ ] LCP image NOT lazy-loaded
[ ] All images have width + height attributes (CLS = 0)
[ ] All non-LCP images have loading="lazy"
[ ] Images in WebP or AVIF format
[ ] Display font preloaded in <head>
[ ] Only needed font weights loaded (not full axis)
[ ] font-display: optional or swap
[ ] Heavy components lazy-loaded with dynamic()
[ ] No window.addEventListener('scroll') for animations
[ ] Optimistic updates for user interactions
[ ] Lighthouse mobile score ≥ 88
[ ] No third-party scripts blocking <head>
[ ] Third-party scripts use async or defer
```

---

*Reference version: global-design-skill v1.0 — `references/performance.md`*
*Related: `checklists/global-design-review.md` §9, `rules/08-performance.md`, `references/responsive.md`*
