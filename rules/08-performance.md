# Rule — Performance

> Performance is a design decision. Every render-blocking resource, uncompressed image, and layout-shifting element is a choice the designer made — or failed to make. These rules connect design decisions to the Core Web Vitals that determine search ranking, conversion rate, and user trust.

---

## Core Web Vitals Targets

| Metric | Good | Needs improvement | Poor |
|---|---|---|---|
| **LCP** Largest Contentful Paint | ≤ 2.5s | 2.5–4s | > 4s |
| **INP** Interaction to Next Paint | ≤ 200ms | 200–500ms | > 500ms |
| **CLS** Cumulative Layout Shift | ≤ 0.1 | 0.1–0.25 | > 0.25 |

These are Google's thresholds. Pages below "Good" lose SEO ranking and convert at lower rates.

---

## R1 — Identify the LCP element. Prioritize it.

LCP measures how long until the largest visible element is painted. For most landing pages this is the hero image or hero headline. It must load with highest priority.

```html
<!-- LCP is an image: eager + high priority + preload link -->
<link rel="preload" as="image" href="/hero.webp" fetchpriority="high" />

<img
  src="/hero.webp"
  alt="Product dashboard screenshot"
  width="1200"
  height="800"
  loading="eager"
  fetchpriority="high"
  decoding="async"
/>

<!-- LCP is text: no extra steps needed, but ensure font is preloaded -->
<link rel="preload" as="font" href="/fonts/fraunces-var.woff2"
      type="font/woff2" crossorigin />

<!-- Wrong: LCP image treated as lazy -->
<img src="/hero.webp" loading="lazy" />  <!-- delays LCP by seconds -->
```

**How to identify the LCP element:**
1. Open Chrome DevTools → Performance tab
2. Record a page load
3. Look for "LCP" marker in the timeline
4. Or: `web-vitals` library: `import { onLCP } from 'web-vitals'`

---

## R2 — All images have explicit width and height. No CLS from images.

Without `width` and `height`, the browser allocates no space for an image until it loads. When the image arrives, content shifts down — that's CLS.

```html
<!-- Correct: explicit dimensions reserve space before load -->
<img
  src="/product.webp"
  alt="..."
  width="720"
  height="480"
  loading="lazy"
/>

<!-- Correct: responsive images preserve aspect ratio via CSS -->
<img
  src="/product.webp"
  alt="..."
  width="720"
  height="480"
  style="width: 100%; height: auto;"
/>

<!-- Wrong: no dimensions — browser doesn't know the height until load -->
<img src="/product.webp" alt="..." />

<!-- Wrong: only CSS, no HTML attributes — still causes CLS -->
<img src="/product.webp" style="width: 100%;" />
```

---

## R3 — Modern image formats only: WebP or AVIF.

JPEG is 2–5× larger than WebP at equivalent quality. PNG is even larger. AVIF is 30–50% smaller than WebP but with slightly longer encoding time.

```html
<!-- AVIF with WebP fallback -->
<picture>
  <source type="image/avif" srcset="/hero.avif" />
  <source type="image/webp" srcset="/hero.webp" />
  <img src="/hero.jpg" alt="..." width="1200" height="800" />
</picture>

<!-- Responsive: different sizes for different viewports -->
<picture>
  <source
    media="(max-width: 767px)"
    type="image/webp"
    srcset="/hero-mobile.webp 390w, /hero-mobile@2x.webp 780w"
    sizes="100vw"
  />
  <source
    media="(min-width: 768px)"
    type="image/webp"
    srcset="/hero-desktop.webp 1200w, /hero-desktop@2x.webp 2400w"
    sizes="50vw"
  />
  <img src="/hero-desktop.jpg" alt="..." width="1200" height="800" loading="eager" fetchpriority="high" />
</picture>
```

**Compression targets:**
- Hero/LCP image: < 200KB
- Card thumbnails: < 50KB each
- Blog post images: < 150KB
- Icons/SVGs: inline or < 5KB

---

## R4 — Below-fold images are lazy. Above-fold images are eager.

`loading="lazy"` defers image loading until the image is about to enter the viewport. Above-fold images must load immediately — never lazy-load the LCP element.

```html
<!-- Above fold — eager (default) -->
<img src="/hero.webp" loading="eager" fetchpriority="high" />

<!-- Navigation/header logo -->
<img src="/logo.svg" loading="eager" />

<!-- Below fold — lazy -->
<img src="/feature-screenshot.webp" loading="lazy" width="640" height="400" />

<!-- Blog post images — lazy -->
<img src="/post-image.webp" loading="lazy" width="800" height="500" />
```

---

## R5 — Font loading: display=swap, preload critical fonts, load only used weights.

Fonts block text rendering by default. `display=swap` shows fallback text immediately, then swaps to the custom font when it loads.

```html
<!-- Preload critical display font (used in hero) -->
<link rel="preload" as="font" href="/fonts/fraunces-var.woff2"
      type="font/woff2" crossorigin />

<!-- Google Fonts: add display=swap -->
<link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600&display=swap"
      rel="stylesheet" />
```

```css
/* Self-hosted fonts: same display: swap */
@font-face {
  font-family: 'Fraunces';
  src: url('/fonts/fraunces-var.woff2') format('woff2');
  font-weight: 100 900;
  font-style: normal;
  font-display: swap;     /* shows fallback, swaps on load */
}

/* Font subsetting: only load characters you use */
/* For Latin-only content, add &subset=latin to Google Fonts URL */
```

**Load only what you use:**
```
Bad:  font-weight: 100 900;  (loads full variable range — 300KB)
Good: font-weight: 300 700;  (loads only used range — lighter)
Bad:  load Regular + Medium + SemiBold + Bold separately — 4 requests
Good: load one variable font covering the range — 1 request
```

---

## R6 — Third-party scripts load async or defer. Never in `<head>` without async.

Synchronous scripts in `<head>` block HTML parsing and delay LCP by the script's load + execution time.

```html
<!-- Wrong: blocking script -->
<head>
  <script src="https://analytics.example.com/tracker.js"></script>
</head>

<!-- Correct: async (loads in parallel, executes when ready) -->
<script async src="https://analytics.example.com/tracker.js"></script>

<!-- Correct: defer (loads in parallel, executes after HTML parsed) -->
<script defer src="https://cdn.example.com/library.js"></script>

<!-- Best: load analytics after page is interactive -->
<script>
  window.addEventListener('load', () => {
    const script = document.createElement('script')
    script.src = 'https://analytics.example.com/tracker.js'
    document.head.append(script)
  })
</script>
```

---

## R7 — No layout shift from dynamic content insertion.

Content injected above existing content pushes everything down — CLS. Reserve space for dynamic content before it loads.

```css
/* Reserve space for content that loads dynamically */

/* Banner that may appear at top */
.notification-slot {
  min-height: 0;
  overflow: hidden;
  transition: min-height var(--duration-normal) var(--ease-spring);
}

.notification-slot:has(.notification) {
  min-height: 56px;   /* known height — avoids shift */
}

/* Skeleton: same height as the loaded content */
.user-card-skeleton {
  height: 72px;       /* must match the real card height */
  border-radius: var(--radius-lg);
}

/* Wrong: skeleton smaller than the real component */
.user-card-skeleton { height: 40px; }  /* shifts when real card loads at 72px */
```

---

## R8 — Doherty Threshold: every interaction responds within 400ms.

The Doherty Threshold is 400ms — the point where waiting becomes perceptible as a delay and interrupts focus. Any action slower than 400ms must show a loading indicator.

```
< 100ms  → No indicator needed (feels instant)
100–400ms → No indicator for simple operations; skeleton for data
400ms–1s → Show loading state on the triggering element
1–10s    → Show progress indicator
> 10s    → Break into chunks; "continue in background"
```

```tsx
// React 19: useOptimistic for sub-400ms perceived response
const [optimisticLikes, addOptimisticLike] = useOptimistic(likes, (state) => state + 1)

async function handleLike() {
  addOptimisticLike()                // immediate UI update
  await saveLike()                   // actual server call
}

// useActionState: button shows loading without extra state
const [state, action, isPending] = useActionState(saveProfile, null)
```

---

## R9 — Virtualize long lists (> 200 rows).

Rendering 1,000+ DOM elements causes jank, long paint times, and high memory usage. Virtual lists render only the visible rows.

```tsx
// TanStack Virtual (React)
import { useVirtualizer } from '@tanstack/react-virtual'

function VirtualList({ items }) {
  const parentRef = useRef(null)

  const virtualizer = useVirtualizer({
    count: items.length,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 48,     // row height in px
    overscan: 5,                // extra rows above/below viewport
  })

  return (
    <div ref={parentRef} style={{ height: '600px', overflow: 'auto' }}>
      <div style={{ height: virtualizer.getTotalSize() }}>
        {virtualizer.getVirtualItems().map(virtualItem => (
          <div
            key={virtualItem.key}
            style={{
              position: 'absolute',
              top: 0,
              left: 0,
              width: '100%',
              height: `${virtualItem.size}px`,
              transform: `translateY(${virtualItem.start}px)`,
            }}
          >
            {items[virtualItem.index].name}
          </div>
        ))}
      </div>
    </div>
  )
}
```

---

## R10 — Next.js 15: use `"use cache"` for slow data fetches.

The default `fetch()` behavior in Next.js 15 is `no-store` — all data fetches are uncached. Slow API calls on every request destroy performance. Cache data that doesn't change on every request.

```tsx
// Next.js 15 caching
import { unstable_cacheLife as cacheLife } from 'next/cache'

async function getProductList() {
  'use cache'
  cacheLife('hours')    // cache for hours
  return await db.products.findMany()
}

async function getUserProfile(id: string) {
  'use cache'
  cacheLife('minutes')  // cache for minutes
  return await db.users.findUnique({ where: { id } })
}

// For real-time data — no cache
async function getActiveDeployments() {
  // no 'use cache' — fetches fresh on every request
  return await api.deployments.list()
}
```

---

## Performance Audit Checklist

```
[ ] LCP element identified and has fetchpriority="high" + loading="eager"
[ ] LCP measured with PageSpeed Insights: score ≥ 90 mobile, ≥ 95 desktop
[ ] All images have explicit width + height attributes
[ ] All images are WebP or AVIF
[ ] All above-fold images: loading="eager"; below-fold: loading="lazy"
[ ] Critical fonts preloaded with <link rel="preload">
[ ] Third-party scripts load async or defer
[ ] No render-blocking resources in <head>
[ ] Skeleton heights match loaded component heights (no CLS on data load)
[ ] Lists > 200 rows: virtualized
[ ] INP tested: all interactions respond within 400ms
[ ] CLS score ≤ 0.1 (verify with Chrome DevTools Performance tab)
[ ] Next.js: appropriate cacheLife() on all data fetches
```

---

*Rule version: global-design-skill v1.0 — `rules/08-performance.md`*
*Related: `rules/16-design-for-seo.md` R3 (Core Web Vitals), `patterns/product-ui/loading-states.md`, `checklists/global-design-review.md` §9*
