# Pattern — Header / Top Navigation

> The header is the one UI element present on every page. It must communicate current location, provide access to all sections, and stay out of the way of the content.

---

## Header Anatomy

```
[Logo]  [Primary nav items]  [Secondary actions]  [CTA / User]
```

Every header has four zones. Not all zones are required:

| Zone | Required | Content |
|---|---|---|
| Logo | Always | Links to homepage or dashboard |
| Primary nav | Always | Section links (≤ 7 items) |
| Secondary actions | Optional | Search, notifications, help |
| Right zone | Always | CTA (marketing) or user avatar (app) |

---

## Pattern A — Marketing Header (sticky, transparent → solid)

Best for: marketing websites, landing pages.

```html
<header class="site-header" id="site-header">
  <div class="site-header__inner">
    <!-- Logo -->
    <a href="/" class="site-header__logo" aria-label="ProductName — go to homepage">
      <img src="/logo.svg" alt="ProductName" width="120" height="32" />
    </a>

    <!-- Primary navigation -->
    <nav class="site-header__nav" aria-label="Main navigation">
      <ul class="site-header__nav-list" role="list">
        <li>
          <a href="/product" class="nav-link">Product</a>
        </li>
        <li class="nav-item--dropdown">
          <button
            class="nav-link nav-link--dropdown"
            aria-expanded="false"
            aria-controls="solutions-dropdown"
          >
            Solutions
            <span class="nav-chevron" aria-hidden="true"></span>
          </button>
          <div
            id="solutions-dropdown"
            class="nav-dropdown"
            role="region"
            hidden
          >
            <a href="/for-designers" class="nav-dropdown__item">
              <strong>For designers</strong>
              <span>Design systems and tokens</span>
            </a>
            <a href="/for-developers" class="nav-dropdown__item">
              <strong>For developers</strong>
              <span>Component libraries</span>
            </a>
          </div>
        </li>
        <li><a href="/pricing" class="nav-link">Pricing</a></li>
        <li><a href="/blog" class="nav-link">Blog</a></li>
      </ul>
    </nav>

    <!-- Right zone -->
    <div class="site-header__actions">
      <a href="/login" class="nav-link">Sign in</a>
      <a href="/signup" class="btn-primary btn-sm">Get started free</a>
    </div>

    <!-- Mobile hamburger -->
    <button
      class="site-header__hamburger"
      aria-label="Open navigation menu"
      aria-expanded="false"
      aria-controls="mobile-nav"
    >
      <span class="hamburger-bar" aria-hidden="true"></span>
      <span class="hamburger-bar" aria-hidden="true"></span>
      <span class="hamburger-bar" aria-hidden="true"></span>
    </button>
  </div>
</header>
```

```css
.site-header {
  position: sticky;
  top: 0;
  z-index: var(--z-sticky);
  width: 100%;
  /* Transparent start — transitions to solid on scroll */
  background: transparent;
  transition: background 300ms, border-color 300ms, box-shadow 300ms;
}

.site-header.scrolled {
  background: oklch(from var(--color-base) l c h / 0.92);
  backdrop-filter: blur(16px) saturate(180%);
  border-bottom: 1px solid var(--color-border);
}

.site-header__inner {
  display: flex;
  align-items: center;
  gap: var(--space-8);
  max-width: 1280px;
  margin-inline: auto;
  padding: var(--space-4) clamp(var(--space-4), 4vw, var(--space-8));
  height: 64px;
}

.site-header__nav { flex: 1; }

.site-header__nav-list {
  display: none; /* hidden on mobile — see mobile-navigation.md */
  list-style: none;
  padding: 0;
  margin: 0;
  gap: var(--space-1);
}

@media (min-width: 768px) {
  .site-header__nav-list { display: flex; }
}

.nav-link {
  display: inline-flex;
  align-items: center;
  gap: var(--space-1);
  padding: var(--space-2) var(--space-3);
  border-radius: var(--radius-md);
  font-size: 0.9375rem;
  color: var(--color-text-secondary);
  text-decoration: none;
  transition: color 120ms, background 120ms;
  white-space: nowrap;
  background: transparent;
  border: none;
  cursor: pointer;
  font-family: inherit;
}

.nav-link:hover {
  color: var(--color-text-primary);
  background: oklch(from var(--color-text-primary) l c h / 0.06);
}

.nav-link[aria-current="page"] {
  color: var(--color-text-primary);
  font-weight: 500;
}

.nav-link:focus-visible {
  outline: 2px solid var(--color-accent);
  outline-offset: 2px;
}

/* Dropdown chevron — CSS only */
.nav-chevron {
  width: 12px;
  height: 12px;
  border-right: 1.5px solid currentColor;
  border-bottom: 1.5px solid currentColor;
  transform: rotate(45deg) translateY(-2px);
  transition: transform 200ms;
}

.nav-link--dropdown[aria-expanded="true"] .nav-chevron {
  transform: rotate(-135deg) translateY(-2px);
}

/* Dropdown panel */
.nav-dropdown {
  position: absolute;
  top: calc(100% + var(--space-2));
  left: 0;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  padding: var(--space-2);
  min-width: 240px;
  box-shadow: 0 8px 32px oklch(0% 0 0 / 0.2);
  z-index: var(--z-dropdown);

  /* Animate open */
  opacity: 1;
  transform: translateY(0) scale(1);
  transform-origin: top left;
  transition: opacity 150ms, transform 150ms cubic-bezier(0.16, 1, 0.3, 1),
              display 150ms allow-discrete;
}

.nav-dropdown[hidden] {
  display: none;
}

@starting-style {
  .nav-dropdown:not([hidden]) {
    opacity: 0;
    transform: translateY(-8px) scale(0.97);
  }
}

.nav-item--dropdown { position: relative; }

.nav-dropdown__item {
  display: block;
  padding: var(--space-3) var(--space-4);
  border-radius: var(--radius-lg);
  text-decoration: none;
  color: var(--color-text-primary);
  transition: background 120ms;
}

.nav-dropdown__item:hover { background: var(--color-surface-2); }

.nav-dropdown__item strong {
  display: block;
  font-size: 0.9375rem;
  margin-bottom: 2px;
}

.nav-dropdown__item span {
  font-size: 0.8125rem;
  color: var(--color-text-muted);
}

/* Hamburger */
.site-header__hamburger {
  display: flex;
  flex-direction: column;
  gap: 5px;
  background: transparent;
  border: none;
  cursor: pointer;
  padding: var(--space-2);
  min-width: 44px;
  min-height: 44px;
  justify-content: center;
  align-items: center;
}

@media (min-width: 768px) {
  .site-header__hamburger { display: none; }
}

.hamburger-bar {
  width: 22px;
  height: 2px;
  background: var(--color-text-primary);
  border-radius: 2px;
  transition: transform 200ms, opacity 200ms;
}

/* Scroll behavior via JS */
```

```js
// Transparent → solid on scroll
const header = document.getElementById('site-header')
window.addEventListener('scroll', () => {
  header.classList.toggle('scrolled', window.scrollY > 20)
}, { passive: true })

// Dropdown toggle
document.querySelectorAll('.nav-link--dropdown').forEach(btn => {
  btn.addEventListener('click', () => {
    const expanded = btn.getAttribute('aria-expanded') === 'true'
    const panelId = btn.getAttribute('aria-controls')
    const panel = document.getElementById(panelId)
    btn.setAttribute('aria-expanded', String(!expanded))
    panel.hidden = expanded
  })
})

// Close dropdown on outside click
document.addEventListener('click', e => {
  if (!e.target.closest('.nav-item--dropdown')) {
    document.querySelectorAll('.nav-link--dropdown').forEach(btn => {
      btn.setAttribute('aria-expanded', 'false')
      document.getElementById(btn.getAttribute('aria-controls')).hidden = true
    })
  }
})

// Close on Escape
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') {
    document.querySelectorAll('[aria-expanded="true"]').forEach(el => {
      el.setAttribute('aria-expanded', 'false')
    })
  }
})
```

---

## Pattern B — App Header (authenticated, fixed)

Best for: SaaS apps, dashboards, authenticated product views.

```html
<header class="app-header">
  <a href="/dashboard" class="app-header__logo" aria-label="Go to dashboard">
    <img src="/logo-mark.svg" alt="ProductName" width="32" height="32" />
  </a>

  <!-- Global search -->
  <button
    class="app-header__search"
    aria-label="Search (Ctrl+K)"
    onclick="openCommandPalette()"
  >
    <span class="search-icon" aria-hidden="true">⌕</span>
    <span class="search-placeholder">Search…</span>
    <kbd class="search-kbd">⌘K</kbd>
  </button>

  <!-- Right zone -->
  <div class="app-header__actions">
    <!-- Notifications -->
    <button
      class="app-header__icon-btn"
      aria-label="Notifications (3 unread)"
      aria-haspopup="true"
    >
      <span aria-hidden="true">🔔</span>
      <span class="notification-badge" aria-hidden="true">3</span>
    </button>

    <!-- Help -->
    <a href="/docs" class="app-header__icon-btn" aria-label="Help and documentation">
      <span aria-hidden="true">?</span>
    </a>

    <!-- User avatar -->
    <button
      class="app-header__avatar"
      aria-label="Account menu for Sarah Chen"
      aria-haspopup="true"
      aria-expanded="false"
    >
      <img src="/avatars/sarah.webp" alt="" width="32" height="32" />
    </button>
  </div>
</header>
```

```css
.app-header {
  position: sticky;
  top: 0;
  z-index: var(--z-sticky);
  height: 56px;
  display: flex;
  align-items: center;
  gap: var(--space-4);
  padding-inline: var(--space-4);
  background: var(--color-surface);
  border-bottom: 1px solid var(--color-border);
}

.app-header__search {
  flex: 1;
  max-width: 360px;
  display: flex;
  align-items: center;
  gap: var(--space-2);
  padding: var(--space-2) var(--space-3);
  background: var(--color-surface-2);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  cursor: pointer;
  font-size: 0.875rem;
  color: var(--color-text-muted);
  transition: border-color 150ms, background 150ms;
}

.app-header__search:hover {
  border-color: var(--color-accent);
  background: var(--color-surface);
}

.search-placeholder { flex: 1; text-align: left; }

.search-kbd {
  font-size: 0.75rem;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-sm);
  padding: 0.1em 0.4em;
  font-family: var(--font-mono);
}

.app-header__actions { display: flex; gap: var(--space-1); margin-left: auto; align-items: center; }

.app-header__icon-btn {
  position: relative;
  width: 36px;
  height: 36px;
  display: grid;
  place-items: center;
  border-radius: var(--radius-md);
  background: transparent;
  border: none;
  cursor: pointer;
  color: var(--color-text-muted);
  transition: background 120ms, color 120ms;
  font-size: 1rem;
}

.app-header__icon-btn:hover {
  background: var(--color-surface-2);
  color: var(--color-text-primary);
}

.notification-badge {
  position: absolute;
  top: 4px;
  right: 4px;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: var(--color-error);
  color: white;
  font-size: 0.625rem;
  font-weight: 700;
  display: grid;
  place-items: center;
}

.app-header__avatar {
  border-radius: 50%;
  overflow: hidden;
  width: 32px;
  height: 32px;
  border: 2px solid var(--color-border);
  cursor: pointer;
  transition: border-color 150ms;
  background: transparent;
  padding: 0;
}

.app-header__avatar:hover { border-color: var(--color-accent); }
.app-header__avatar img { width: 100%; height: 100%; object-fit: cover; }
```

---

## Active State Rules

```css
/* Current page link — not just color */
.nav-link[aria-current="page"] {
  color: var(--color-text-primary);
  font-weight: 500;
  /* Additional differentiator: */
  background: oklch(from var(--color-accent) l c h / 0.1);
}
```

Never use color as the only active indicator. Color-blind users cannot distinguish.

---

## Skip Navigation (required on all pages)

```html
<!-- First element in <body> -->
<a href="#main-content" class="skip-nav">Skip to main content</a>

<style>
.skip-nav {
  position: absolute;
  top: -100%;
  left: var(--space-4);
  background: var(--color-accent);
  color: oklch(10% 0.01 258);
  padding: var(--space-3) var(--space-6);
  border-radius: var(--radius-md);
  font-weight: 600;
  z-index: calc(var(--z-toast) + 1);
  text-decoration: none;
  transition: top 150ms;
}
.skip-nav:focus { top: var(--space-4); }
</style>
```

---

## Anti-Patterns

- Nav items > 7 at top level
- Active state via color only (no weight, background, or underline differentiator)
- Dropdown that requires hover to stay open (inaccessible on touch, keyboard)
- Logo with no alt text or linking nowhere
- No skip navigation link
- Header that covers content on scroll (use `position: sticky` not `fixed` without offset)
- `100vh` on full-height pages behind a fixed header — always subtract header height

## Related Files

- `patterns/navigation/mobile-navigation.md` — hamburger and mobile drawer
- `patterns/navigation/sidebar-patterns.md` — sidebar nav for apps
- `rules/02-layout-and-grid.md` — R11: Sticky element safe areas
- `references/accessibility.md` — keyboard nav, skip links, ARIA patterns
