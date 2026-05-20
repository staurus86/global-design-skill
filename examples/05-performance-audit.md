# Example 05 — Performance Audit and Fix

> **Rules applied:** performance R1–R10 · animation R6, R7 · accessibility R2

**Scenario:** A marketing landing page scoring 34 on PageSpeed Insights mobile. The team is confused — "the site looks fine." This example walks through a full performance audit, identifies the root causes, and shows the fixes. After applying them: 91 mobile, 97 desktop.

---

## PageSpeed Report — Before

```
Mobile score:  34 / 100
Desktop score: 71 / 100

LCP:  6.8s  ❌ (target: ≤ 2.5s)
INP:  680ms ❌ (target: ≤ 200ms)
CLS:  0.41  ❌ (target: ≤ 0.1)

Opportunities:
  - Serve images in next-gen formats (saves 2.4MB)
  - Properly size images (saves 1.1MB)
  - Eliminate render-blocking resources (saves 1.8s)
  - Reduce unused JavaScript (saves 0.9s)
  - Image elements do not have explicit width and height
  - Avoid enormous network payloads (3.7MB total)
```

---

## Before — The Problem Code

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Acme — Build faster</title>

  <!-- PROBLEM 1: Blocking fonts in <head> — no preload, no display=swap -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&family=Roboto:wght@300;400;500;700&display=block" rel="stylesheet" />

  <!-- PROBLEM 2: Blocking analytics script -->
  <script src="https://analytics.example.com/tracker.js"></script>

  <!-- PROBLEM 3: Blocking A/B testing script -->
  <script src="https://ab-testing.example.com/optimize.js"></script>

  <link rel="stylesheet" href="/styles.css" />
</head>
<body>

  <!-- PROBLEM 4: LCP image with no priority signals, lazy loaded -->
  <section class="hero">
    <img
      src="/hero.png"
      alt="Hero"
      class="hero-img"
      loading="lazy"
    />
    <h1>Build faster products</h1>
    <p>Ship 4x faster with our platform</p>
  </section>

  <!-- PROBLEM 5: Images with no dimensions — CLS source -->
  <section class="features">
    <img src="/feature-1.jpg" alt="Feature 1" />
    <img src="/feature-2.jpg" alt="Feature 2" />
    <img src="/feature-3.jpg" alt="Feature 3" />
  </section>

  <!-- PROBLEM 6: Dynamic banner injected above content — CLS -->
  <div id="promo-banner"></div>

  <!-- PROBLEM 7: 800-row table, all DOM rendered -->
  <section class="data-section">
    <table class="deployments-table">
      <!-- 800 <tr> rows rendered at once -->
    </table>
  </section>

  <!-- PROBLEM 8: scroll listener for animation -->
  <script>
    window.addEventListener('scroll', () => {
      document.querySelectorAll('.feature-card').forEach(card => {
        const rect = card.getBoundingClientRect()
        if (rect.top < window.innerHeight) {
          card.classList.add('visible')
        }
      })
    })
  </script>

  <!-- PROBLEM 9: Multiple chat/support scripts at end of body — still blocking -->
  <script src="https://widget.intercom.io/widget/abc123"></script>
  <script src="https://cdn.segment.com/analytics.js/v1/abc/analytics.min.js"></script>
</body>
</html>
```

```css
/* PROBLEM 10: hero image — no size constraints, loads PNG */
.hero-img {
  width: 100%;
  max-width: 1200px;
  /* no height — browser allocates 0px until image loads */
}

/* PROBLEM 11: scroll animations cause reflow on main thread */
.feature-card { opacity: 0; transform: translateY(20px); transition: all 0.5s ease; }
.feature-card.visible { opacity: 1; transform: translateY(0); }
```

---

## Root Cause Analysis

| Problem | Impact | Fix |
|---|---|---|
| LCP image is `loading="lazy"` and PNG format | +3.2s LCP | `eager` + preload + convert to WebP |
| 9-weight Inter + Roboto, `display=block` | +1.8s blocked render | Single variable font, `display=swap` |
| 2 blocking scripts in `<head>` | +1.4s blocked parse | `async` or post-load |
| Feature images have no `width`/`height` | CLS 0.31 | Add dimensions |
| Dynamic promo banner injects above content | CLS +0.10 | Reserve slot height |
| 800-row table in DOM | INP 680ms (scroll jank) | Virtualize |
| `window.scroll` listener for animations | INP spikes | Replace with IntersectionObserver |
| Chat/analytics scripts blocking | +0.4s | `defer` + post-load |

---

## After — Fixed Code

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Acme — Build faster</title>

  <!-- FIX 1: Preload LCP image — must come first in <head> -->
  <link rel="preload" as="image" href="/hero.webp" fetchpriority="high" />

  <!-- FIX 2: Preload only the critical font weight used in hero -->
  <link rel="preload" as="font"
    href="https://fonts.gstatic.com/s/instrumentsans/v1/pxicypckl_A_Mq_U_pWvQg.woff2"
    type="font/woff2" crossorigin />

  <!-- FIX 3: Load only 2 weights of 1 font, display=swap -->
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;600&display=swap"
        rel="stylesheet" />

  <link rel="stylesheet" href="/styles.css" />

  <!-- Anti-flash theme script (inline, no network request) -->
  <script>
    const t = localStorage.getItem('theme') || (matchMedia('(prefers-color-scheme:dark)').matches ? 'dark' : 'light')
    document.documentElement.setAttribute('data-theme', t)
  </script>
</head>
<body>

  <!-- FIX 4: LCP image — eager, fetchpriority high, WebP, explicit dimensions -->
  <section class="hero">
    <picture>
      <source type="image/avif" srcset="/hero.avif 1x, /hero@2x.avif 2x" />
      <source type="image/webp" srcset="/hero.webp 1x, /hero@2x.webp 2x" />
      <img
        src="/hero.webp"
        alt="Pipeline dashboard showing real-time deployment status for 3 services"
        width="1200"
        height="800"
        loading="eager"
        fetchpriority="high"
        decoding="async"
        class="hero-img"
      />
    </picture>
    <h1>Build faster products</h1>
    <p>Ship in hours, not days. Automatic deploys, instant rollbacks.</p>
  </section>

  <!-- FIX 5: Feature images — explicit dimensions, lazy, WebP -->
  <section class="features">
    <img src="/feature-1.webp" alt="Auto-deploy workflow: commit triggers build in 18 seconds" width="480" height="320" loading="lazy" />
    <img src="/feature-2.webp" alt="Rollback interface showing previous 5 deploys with one-click restore" width="480" height="320" loading="lazy" />
    <img src="/feature-3.webp" alt="Team alerts screen showing Slack and PagerDuty integration status" width="480" height="320" loading="lazy" />
  </section>

  <!-- FIX 6: Promo banner — space reserved before JS injects content -->
  <div id="promo-banner" class="promo-slot" aria-live="polite">
    <!-- Banner injected by JS after load — space reserved in CSS -->
  </div>

  <!-- FIX 7: Virtualized table — renders only visible rows -->
  <section class="data-section">
    <div id="virtual-table-container" style="height: 600px; overflow-y: auto;">
      <!-- TanStack Virtual renders rows here -->
    </div>
  </section>

  <!-- FIX 8: Analytics — deferred to after page load -->
  <script>
    window.addEventListener('load', () => {
      // Analytics
      const analytics = document.createElement('script')
      analytics.src = 'https://cdn.segment.com/analytics.js/v1/abc/analytics.min.js'
      analytics.defer = true
      document.head.append(analytics)

      // Chat widget — only if user interacts first
      let chatLoaded = false
      const loadChat = () => {
        if (chatLoaded) return
        chatLoaded = true
        const chat = document.createElement('script')
        chat.src = 'https://widget.intercom.io/widget/abc123'
        document.head.append(chat)
      }
      document.addEventListener('mousemove', loadChat, { once: true })
      document.addEventListener('touchstart', loadChat, { once: true })
    })
  </script>

  <!-- FIX 9: A/B test script — async, loaded after render -->
  <script async src="https://ab-testing.example.com/optimize.js"></script>

  <!-- FIX 10: IntersectionObserver for scroll animations -->
  <script type="module">
    // FIX: IntersectionObserver instead of scroll listener
    const observer = new IntersectionObserver(
      entries => entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.classList.add('visible')
          observer.unobserve(e.target)
        }
      }),
      { threshold: 0.1 }
    )
    document.querySelectorAll('[data-reveal]').forEach(el => observer.observe(el))

    // FIX: Virtual table with TanStack Virtual
    import { Virtualizer } from '@tanstack/virtual-core'

    const container = document.getElementById('virtual-table-container')
    const data = window.__DEPLOYMENTS__ // server-rendered JSON

    const virtualizer = new Virtualizer({
      count: data.length,
      getScrollElement: () => container,
      estimateSize: () => 52,
      overscan: 5,
      onChange: instance => renderVirtualRows(instance, data)
    })

    function renderVirtualRows(v, items) {
      const totalHeight = v.getTotalSize()
      container.style.height = totalHeight + 'px'
      container.style.position = 'relative'

      container.innerHTML = v.getVirtualItems().map(row => `
        <div style="position:absolute;top:0;left:0;width:100%;height:${row.size}px;transform:translateY(${row.start}px)">
          <div class="table-row">
            <span>${items[row.index].name}</span>
            <span>${items[row.index].status}</span>
            <span>${items[row.index].time}</span>
          </div>
        </div>
      `).join('')
    }
  </script>
</body>
</html>
```

```css
/* FIX 10a: hero image explicit dimensions */
.hero-img {
  width: 100%;
  height: auto;       /* preserves aspect ratio from width/height HTML attributes */
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-xl);
}

/* FIX 6: reserve banner slot — prevents CLS */
.promo-slot {
  overflow: hidden;
  min-height: 0;
  transition: min-height var(--duration-normal) var(--ease-spring);
}

.promo-slot:has(.promo-banner) {
  min-height: 52px;   /* matches actual banner height */
}

/* FIX 11: replace transition:all and ease-in-out */
[data-reveal] {
  opacity: 0;
  transform: translateY(16px);
  transition:
    opacity   var(--duration-slow) var(--ease-spring),
    transform var(--duration-slow) var(--ease-spring);
}

[data-reveal].visible {
  opacity: 1;
  transform: none;
}

/* prefers-reduced-motion: keep fade, remove translate */
@media (prefers-reduced-motion: reduce) {
  [data-reveal] {
    transform: none;
    transition-duration: var(--duration-fast);
  }
}
```

---

## Results

```
Mobile score:  91 / 100  (was 34)
Desktop score: 97 / 100  (was 71)

LCP:  1.9s  ✓ (was 6.8s — 3.6× faster)
INP:  85ms  ✓ (was 680ms — 8× faster)
CLS:  0.02  ✓ (was 0.41 — 20× better)

Page weight: 410KB  (was 3.7MB — 9× smaller)
```

---

## Fix Impact Breakdown

| Fix | LCP delta | INP delta | CLS delta |
|---|---|---|---|
| LCP image: PNG → WebP + preload + eager | -2.8s | — | — |
| Font loading: 9 weights → 1 variable + swap | -1.4s | — | — |
| Analytics/chat scripts: blocking → post-load | -0.6s | -120ms | — |
| Image dimensions added | — | — | -0.31 |
| Promo banner slot reserved | — | — | -0.08 |
| Table virtualized (800→20 DOM rows) | — | -480ms | — |
| `scroll` listener → IntersectionObserver | — | -75ms | — |

The biggest single win: the LCP image was JPEG, lazy-loaded, with no explicit dimensions, no preload. Converting it to WebP and adding `fetchpriority="high"` + `loading="eager"` saved 2.8 seconds of LCP alone.

---

## Performance Checklist for This Page

```
[x] LCP element identified (hero image) + fetchpriority="high" + preload link
[x] LCP measured with PageSpeed Insights: 91 mobile
[x] All images have explicit width + height
[x] All images are WebP with AVIF fallback via <picture>
[x] Above-fold images: loading="eager"; below-fold: loading="lazy"
[x] Critical font preloaded (hero display font)
[x] Google Fonts: display=swap, minimal weights (400;600 only)
[x] Third-party scripts: async or deferred post-load
[x] No render-blocking resources in <head>
[x] Skeleton/slot heights match loaded content (no CLS on data load)
[x] Table (800 rows) virtualized with TanStack Virtual
[x] All interactions respond within 400ms (INP: 85ms)
[x] CLS ≤ 0.1 (measured: 0.02)
```

---

*Example 05 — `examples/05-performance-audit.md`*
*Related: `rules/08-performance.md`, `rules/05-animation.md`, `checklists/global-design-review.md` §9, `recipes/improve-mobile-version.md`*
