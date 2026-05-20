# Example — Multi-Page Website (Full Build)

> **Scenario:** Build a multi-page marketing website for a developer tool from scratch, applying `blueprints/website-from-scratch.md`. This example shows the complete IA decision-making process, the navigation system, and the CSS Anchor Positioning implementation.

---

## Context

**Product:** A database connection pooler for serverless applications  
**Audience:** Backend developers and DevOps engineers  
**Archetype:** A — Ethereal Black  
**Aesthetic one thing:** "A terminal that disappears when you don't need it"

---

## Information Architecture

```
/                    Home (marketing landing)
/docs                Documentation root
/docs/quickstart     Getting started guide
/pricing             Pricing page
/changelog           Product changelog
/blog                Engineering blog
/blog/[slug]         Individual post
/about               Team + mission
```

**IA decisions:**

- **No `/features` page.** Features are demonstrated on the homepage, not on a separate page. A separate features page is a second chance to sell what the homepage already sold.
- **`/docs` is its own navigation context.** Docs switch to a two-column sidebar layout with its own nav tree. The marketing nav disappears.
- **`/changelog` not hidden in docs.** Developer tools earn trust through public shipping velocity. The changelog is a top-level page.
- **`/about` without a `/team` sub-page.** For a small team, combining mission + team into one page is correct. Separate pages for small teams signal padding.

---

## Navigation System

### Marketing nav (top, transparent → sticky)

```html
<header class="site-header" role="banner">
  <div class="container header__container">

    <!-- Logo -->
    <a href="/" class="header__logo" aria-label="Poolr home">
      <svg class="logo-mark" aria-hidden="true" ...></svg>
      <span class="logo-text">Poolr</span>
    </a>

    <!-- Skip navigation — required per rules/07-accessibility.md -->
    <a href="#main-content" class="skip-nav">Skip to main content</a>

    <!-- Main navigation -->
    <nav aria-label="Main navigation">
      <ul class="nav__list" role="list">
        <li><a href="/docs" class="nav__link">Docs</a></li>
        <li><a href="/pricing" class="nav__link">Pricing</a></li>
        <li><a href="/changelog" class="nav__link">Changelog</a></li>
        <li><a href="/blog" class="nav__link">Blog</a></li>
      </ul>
    </nav>

    <!-- CTAs -->
    <div class="header__actions">
      <a href="/login" class="btn btn--ghost btn--sm">Sign in</a>
      <a href="/signup" class="btn btn--primary btn--sm">Start free</a>
    </div>

  </div>
</header>
```

```css
.site-header {
  position: sticky;
  top: 0;
  z-index: var(--z-sticky);
  background: oklch(from var(--color-surface) l c h / 0);
  backdrop-filter: blur(0px);
  border-bottom: 1px solid transparent;
  transition:
    background var(--duration-normal) var(--ease-smooth),
    backdrop-filter var(--duration-normal) var(--ease-smooth),
    border-color var(--duration-normal) var(--ease-smooth);
}

.site-header.scrolled {
  background: oklch(from var(--color-surface) l c h / 0.9);
  backdrop-filter: blur(12px);
  border-bottom-color: var(--color-border);
}
```

```javascript
// Transparent → opaque on scroll
const header = document.querySelector('.site-header');
const heroHeight = document.querySelector('.hero').offsetHeight;

const observer = new IntersectionObserver(
  ([entry]) => header.classList.toggle('scrolled', !entry.isIntersecting),
  { threshold: 0 }
);
observer.observe(document.querySelector('.hero'));
```

---

### Docs nav (sidebar, two-column layout)

When user navigates to `/docs`, the entire layout switches:

```html
<div class="docs-layout">

  <!-- Sidebar nav -->
  <nav class="docs-nav" aria-label="Documentation navigation">
    <div class="docs-nav__section">
      <span class="docs-nav__section-title">Getting Started</span>
      <ul role="list">
        <li><a href="/docs/quickstart" class="docs-nav__link docs-nav__link--active" aria-current="page">Quickstart</a></li>
        <li><a href="/docs/install" class="docs-nav__link">Installation</a></li>
        <li><a href="/docs/configuration" class="docs-nav__link">Configuration</a></li>
      </ul>
    </div>
    <div class="docs-nav__section">
      <span class="docs-nav__section-title">Reference</span>
      <ul role="list">
        <li><a href="/docs/api" class="docs-nav__link">API</a></li>
        <li><a href="/docs/cli" class="docs-nav__link">CLI</a></li>
        <li><a href="/docs/config-file" class="docs-nav__link">Config file</a></li>
      </ul>
    </div>
  </nav>

  <!-- Docs content -->
  <main class="docs-content" id="main-content">
    ...
  </main>

</div>
```

```css
.docs-layout {
  display: grid;
  grid-template-columns: 240px 1fr;
  gap: 0;
  min-height: 100dvh;
  align-items: start;
}

.docs-nav {
  position: sticky;
  top: var(--header-height, 64px);
  height: calc(100dvh - var(--header-height, 64px));
  overflow-y: auto;
  padding: var(--space-6) var(--space-4);
  border-right: 1px solid var(--color-border);
  scrollbar-width: thin;
}

.docs-content {
  max-width: 720px;
  padding: var(--space-10) var(--space-8);
}
```

---

## Schema Markup

Applied per `rules/16-design-for-seo.md`:

```html
<!-- Organization schema on every page -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Poolr",
  "url": "https://poolr.dev",
  "logo": "https://poolr.dev/logo.png",
  "description": "Database connection pooler for serverless applications",
  "sameAs": ["https://github.com/poolr", "https://twitter.com/poolrdev"]
}
</script>

<!-- SoftwareApplication schema on homepage -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Poolr",
  "applicationCategory": "DeveloperApplication",
  "operatingSystem": "All",
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "USD"
  }
}
</script>

<!-- Article schema on each blog post -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "TechArticle",
  "headline": "How Poolr handles connection limits in serverless",
  "author": {
    "@type": "Person",
    "name": "Alex Kim"
  },
  "datePublished": "2026-03-15",
  "publisher": {
    "@type": "Organization",
    "name": "Poolr"
  }
}
</script>
```

---

## CSS Anchor Positioning (Baseline 2024)

Used for the docs nav table of contents — a right-sidebar that anchors to the current section heading:

```css
/* Section headings become anchors */
.docs-content h2 {
  anchor-name: --section-heading;
}

/* TOC item follows the active heading */
.toc-active-indicator {
  position: absolute;
  position-anchor: --section-heading;
  top: anchor(top);
  left: anchor(right);
  transition: top 150ms var(--ease-smooth);
}
```

For the popover tooltips on docs code examples (using Popover API):

```html
<button
  popovertarget="explain-pool-size"
  class="code-explain-btn"
  aria-label="Explain pool_size parameter">
  ?
</button>

<div id="explain-pool-size" popover>
  <p>The maximum number of connections to maintain in the pool.
  For serverless, keep this low (2–5) to avoid overwhelming your database.</p>
</div>
```

---

## View Transitions (Level 2)

Page transitions between marketing and docs:

```css
/* Each named element transitions smoothly between pages */
.site-logo {
  view-transition-name: site-logo;
}

.page-title {
  view-transition-name: page-title;
}

::view-transition-old(site-logo),
::view-transition-new(site-logo) {
  animation-duration: 250ms;
  animation-timing-function: var(--ease-smooth);
}

/* Docs sidebar: enter from left */
::view-transition-new(docs-sidebar) {
  animation: slide-from-left 300ms var(--ease-spring);
}

@keyframes slide-from-left {
  from { transform: translateX(-100%); opacity: 0; }
}
```

---

## Mobile Navigation

At 768px and below:

```html
<!-- Mobile header -->
<header class="site-header" role="banner">
  <div class="container header__container">
    <a href="/" class="header__logo" aria-label="Poolr home">...</a>

    <button
      class="hamburger"
      aria-expanded="false"
      aria-controls="mobile-nav"
      aria-label="Open navigation"
      type="button">
      <span class="hamburger__bar"></span>
      <span class="hamburger__bar"></span>
      <span class="hamburger__bar"></span>
    </button>
  </div>
</header>

<nav id="mobile-nav" class="mobile-nav" aria-label="Mobile navigation" hidden>
  <ul role="list">
    <li><a href="/docs">Docs</a></li>
    <li><a href="/pricing">Pricing</a></li>
    <li><a href="/changelog">Changelog</a></li>
    <li><a href="/blog">Blog</a></li>
    <li class="mobile-nav__ctas">
      <a href="/login" class="btn btn--ghost">Sign in</a>
      <a href="/signup" class="btn btn--primary">Start free</a>
    </li>
  </ul>
</nav>
```

```css
.mobile-nav {
  position: fixed;
  inset: 0;
  background: var(--color-surface);
  z-index: var(--z-modal);
  padding: var(--space-20) var(--space-6) var(--space-8);
  display: flex;
  flex-direction: column;
  gap: var(--space-2);

  /* Entry animation with @starting-style */
  transition:
    opacity var(--duration-normal) var(--ease-smooth),
    transform var(--duration-normal) var(--ease-spring),
    display var(--duration-normal) var(--ease-smooth) allow-discrete;

  @starting-style {
    opacity: 0;
    transform: translateY(-8px);
  }
}

.mobile-nav[hidden] {
  opacity: 0;
  transform: translateY(-8px);
  display: none;
}
```

---

## Meta Tags

Applied per `rules/16-design-for-seo.md`:

```html
<!-- All pages -->
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#0a0b0f">

<!-- Homepage -->
<title>Poolr — Database connection pooling for serverless</title>
<meta name="description" content="Add connection pooling to any Postgres database in 30 seconds. Built for serverless functions, edge workers, and CI environments.">
<meta property="og:title" content="Poolr — Database connection pooling for serverless">
<meta property="og:description" content="Add connection pooling to any Postgres database in 30 seconds.">
<meta property="og:image" content="https://poolr.dev/og.png">
<link rel="canonical" href="https://poolr.dev/">

<!-- Blog post -->
<title>How Poolr handles connection limits | Poolr Blog</title>
<meta name="description" content="[First 160 characters of article introduction]">
<link rel="canonical" href="https://poolr.dev/blog/connection-limits">
```

---

## What This Example Demonstrates

| Decision | Pattern applied | Reference |
|---|---|---|
| Transparent → sticky nav transition | `IntersectionObserver` on hero | `patterns/navigation/header-patterns.md` |
| Docs sidebar with sticky position | `position: sticky` + `height: 100dvh` | `patterns/navigation/sidebar-patterns.md` |
| `@starting-style` mobile drawer | Display:none transition via allow-discrete | `rules/05-animation.md` R5 |
| CSS Anchor Positioning for TOC | `anchor-name` + `position-anchor` | `rules/02-layout-and-grid.md` |
| View Transitions between pages | `view-transition-name` + `::view-transition-*` | `rules/05-animation.md` |
| Schema markup per page type | JSON-LD Organization + Article | `rules/16-design-for-seo.md` |
| `aria-current="page"` on active nav | WCAG 2.2 navigation landmark | `rules/07-accessibility.md` |
| Skip navigation link | First focusable element on every page | `rules/07-accessibility.md` R9 |

---

*Example version: global-design-skill v1.0 — `examples/websites/01-multi-page-site.md`*  
*Related: `blueprints/website-from-scratch.md`, `patterns/navigation/`, `rules/16-design-for-seo.md`*
