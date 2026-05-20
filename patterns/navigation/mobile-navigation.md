# Pattern — Mobile Navigation

> Mobile navigation is not a scaled-down version of desktop navigation. It is a different interaction model: thumb-reachable, touch-friendly, and optimized for one-handed use.

---

## Mobile Navigation Patterns — Choose One

| Pattern | Use when | Primary action |
|---|---|---|
| **Bottom tab bar** | App with 3-5 primary sections, mobile-first | Tap tab |
| **Hamburger drawer** | Marketing site or app with 5+ sections | Tap hamburger → slide drawer |
| **Top sheet** | Simple apps with 3-4 sections | Tap hamburger → sheet drops down |
| **Full-screen overlay** | Editorial sites, portfolios, bold aesthetic | Hamburger → full-screen menu |

**Never combine patterns.** Pick one approach and use it consistently.

---

## Pattern A — Bottom Tab Bar (native-feeling, app-primary)

Best for: mobile-first apps where the bottom of the screen is thumb-reachable.

```html
<nav class="bottom-nav" aria-label="Main navigation">
  <a href="/home"
     class="bottom-nav__item"
     aria-current="page"
     aria-label="Home">
    <span class="bottom-nav__icon" aria-hidden="true">
      <!-- Home SVG icon, filled when active -->
    </span>
    <span class="bottom-nav__label">Home</span>
  </a>

  <a href="/projects"
     class="bottom-nav__item"
     aria-label="Projects">
    <span class="bottom-nav__icon" aria-hidden="true">
      <!-- Projects SVG icon -->
    </span>
    <span class="bottom-nav__label">Projects</span>
  </a>

  <!-- Center action button (optional: primary action) -->
  <a href="/create"
     class="bottom-nav__item bottom-nav__item--action"
     aria-label="Create new project">
    <span class="bottom-nav__action-btn" aria-hidden="true">+</span>
  </a>

  <a href="/inbox"
     class="bottom-nav__item"
     aria-label="Inbox (2 unread)">
    <span class="bottom-nav__icon" aria-hidden="true">
      <!-- Inbox icon with badge -->
    </span>
    <span class="bottom-nav__badge" aria-hidden="true">2</span>
    <span class="bottom-nav__label">Inbox</span>
  </a>

  <a href="/settings"
     class="bottom-nav__item"
     aria-label="Settings">
    <span class="bottom-nav__icon" aria-hidden="true"><!-- SVG --></span>
    <span class="bottom-nav__label">Settings</span>
  </a>
</nav>
```

```css
.bottom-nav {
  /* Only visible on mobile */
  display: flex;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: var(--z-sticky);
  background: var(--color-surface);
  border-top: 1px solid var(--color-border);
  /* iOS safe area — critical */
  padding-bottom: env(safe-area-inset-bottom);
}

@media (min-width: 768px) {
  .bottom-nav { display: none; }
}

.bottom-nav__item {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 3px;
  padding-block: var(--space-2);
  text-decoration: none;
  color: var(--color-text-muted);
  font-size: 0.6875rem;
  font-weight: 500;
  min-height: 56px; /* touch target */
  position: relative;
  transition: color 150ms;
}

.bottom-nav__item[aria-current="page"] {
  color: var(--color-accent);
}

.bottom-nav__icon {
  width: 24px;
  height: 24px;
}

/* Center action button */
.bottom-nav__item--action {
  color: var(--color-accent);
}

.bottom-nav__action-btn {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: var(--color-accent);
  color: oklch(10% 0.01 258);
  display: grid;
  place-items: center;
  font-size: 1.5rem;
  font-weight: 300;
  margin-top: -8px; /* rises above the bar */
  box-shadow: 0 4px 16px oklch(from var(--color-accent) l c h / 0.4);
}

/* Notification badge on icon */
.bottom-nav__badge {
  position: absolute;
  top: 8px;
  left: calc(50% + 6px);
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: var(--color-error);
  color: white;
  font-size: 0.625rem;
  font-weight: 700;
  display: grid;
  place-items: center;
  border: 2px solid var(--color-surface);
}

/* Adjust main content so it's not hidden behind tab bar */
.app-main {
  padding-bottom: calc(56px + env(safe-area-inset-bottom));
}

@media (min-width: 768px) {
  .app-main { padding-bottom: 0; }
}
```

---

## Pattern B — Hamburger Drawer (slide-in)

Best for: marketing sites, apps with many sections.

```html
<!-- Hamburger trigger (in header) -->
<button
  class="hamburger"
  aria-label="Open navigation menu"
  aria-expanded="false"
  aria-controls="mobile-drawer"
>
  <span class="hamburger-bar" aria-hidden="true"></span>
  <span class="hamburger-bar" aria-hidden="true"></span>
  <span class="hamburger-bar" aria-hidden="true"></span>
</button>

<!-- Backdrop -->
<div class="drawer-backdrop" id="drawer-backdrop" aria-hidden="true" hidden></div>

<!-- Drawer -->
<div
  id="mobile-drawer"
  class="mobile-drawer"
  role="dialog"
  aria-modal="true"
  aria-label="Navigation menu"
  hidden
>
  <div class="mobile-drawer__header">
    <img src="/logo.svg" alt="ProductName" width="100" height="28" />
    <button
      class="drawer-close"
      aria-label="Close navigation menu"
      onclick="closeDrawer()"
    >×</button>
  </div>

  <nav class="mobile-drawer__nav" aria-label="Main navigation">
    <ul role="list">
      <li><a href="/product" class="drawer-nav-item">Product</a></li>
      <li><a href="/pricing" class="drawer-nav-item">Pricing</a></li>
      <li><a href="/customers" class="drawer-nav-item">Customers</a></li>
      <li><a href="/blog" class="drawer-nav-item">Blog</a></li>
    </ul>
  </nav>

  <div class="mobile-drawer__actions">
    <a href="/login" class="btn-ghost btn-full">Sign in</a>
    <a href="/signup" class="btn-primary btn-full">Get started free</a>
  </div>
</div>
```

```css
/* Drawer */
.mobile-drawer {
  position: fixed;
  inset: 0;
  right: auto;
  width: min(320px, 85vw);
  z-index: var(--z-drawer);
  background: var(--color-surface);
  display: flex;
  flex-direction: column;
  overflow-y: auto;
  padding: var(--space-6);
  padding-top: calc(var(--space-6) + env(safe-area-inset-top));
  padding-bottom: calc(var(--space-6) + env(safe-area-inset-bottom));

  /* Animation */
  translate: -100% 0;
  transition: translate 300ms cubic-bezier(0.16, 1, 0.3, 1),
              display 300ms allow-discrete;
}

.mobile-drawer:not([hidden]) {
  translate: 0 0;
}

@starting-style {
  .mobile-drawer:not([hidden]) {
    translate: -100% 0;
  }
}

@media (min-width: 768px) {
  .mobile-drawer { display: none !important; }
}

/* Right-side variant */
.mobile-drawer--right {
  right: 0;
  left: auto;
  translate: 100% 0;
}

.mobile-drawer--right:not([hidden]) { translate: 0 0; }

@starting-style {
  .mobile-drawer--right:not([hidden]) { translate: 100% 0; }
}

/* Backdrop */
.drawer-backdrop {
  position: fixed;
  inset: 0;
  background: oklch(0% 0 0 / 0.5);
  z-index: calc(var(--z-drawer) - 1);
  backdrop-filter: blur(2px);
  opacity: 1;
  transition: opacity 300ms, display 300ms allow-discrete;
}

.drawer-backdrop[hidden] { display: none; }

@starting-style {
  .drawer-backdrop:not([hidden]) { opacity: 0; }
}

/* Drawer header */
.mobile-drawer__header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: var(--space-8);
}

.drawer-close {
  background: transparent;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: var(--color-text-muted);
  min-width: 44px;
  min-height: 44px;
  display: grid;
  place-items: center;
  border-radius: var(--radius-md);
  transition: background 120ms;
}

.drawer-close:hover { background: var(--color-surface-2); }

/* Drawer nav */
.mobile-drawer__nav ul {
  list-style: none;
  padding: 0;
}

.drawer-nav-item {
  display: block;
  padding: var(--space-3) var(--space-2);
  font-size: 1.125rem;
  font-weight: 500;
  color: var(--color-text-primary);
  text-decoration: none;
  border-bottom: 1px solid var(--color-border);
  transition: color 120ms;
}

.drawer-nav-item:hover { color: var(--color-accent); }

.mobile-drawer__actions {
  margin-top: auto;
  padding-top: var(--space-8);
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
}
```

```js
function openDrawer() {
  const drawer = document.getElementById('mobile-drawer')
  const backdrop = document.getElementById('drawer-backdrop')
  const hamburger = document.querySelector('.hamburger')

  drawer.hidden = false
  backdrop.hidden = false
  hamburger.setAttribute('aria-expanded', 'true')
  hamburger.setAttribute('aria-label', 'Close navigation menu')

  // Trap focus
  const focusable = drawer.querySelectorAll('a, button, [tabindex]')
  focusable[0]?.focus()

  // Close on backdrop click
  backdrop.addEventListener('click', closeDrawer, { once: true })
}

function closeDrawer() {
  const drawer = document.getElementById('mobile-drawer')
  const backdrop = document.getElementById('drawer-backdrop')
  const hamburger = document.querySelector('.hamburger')

  drawer.hidden = true
  backdrop.hidden = true
  hamburger.setAttribute('aria-expanded', 'false')
  hamburger.setAttribute('aria-label', 'Open navigation menu')
  hamburger.focus() // return focus to trigger
}

// Close on Escape
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') closeDrawer()
})
```

---

## Hamburger Button Styles

```css
.hamburger {
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 5px;
  background: transparent;
  border: none;
  cursor: pointer;
  min-width: 44px;
  min-height: 44px;
  padding: var(--space-2);
  border-radius: var(--radius-md);
}

@media (min-width: 768px) { .hamburger { display: none; } }

.hamburger-bar {
  width: 22px;
  height: 2px;
  background: var(--color-text-primary);
  border-radius: 2px;
  transition: transform 250ms cubic-bezier(0.16, 1, 0.3, 1),
              opacity 200ms;
  transform-origin: center;
}

/* Animate to × when open */
.hamburger[aria-expanded="true"] .hamburger-bar:nth-child(1) {
  transform: translateY(7px) rotate(45deg);
}
.hamburger[aria-expanded="true"] .hamburger-bar:nth-child(2) {
  opacity: 0;
  transform: scaleX(0);
}
.hamburger[aria-expanded="true"] .hamburger-bar:nth-child(3) {
  transform: translateY(-7px) rotate(-45deg);
}
```

---

## Touch Target Requirements

All interactive elements in mobile navigation:
- Minimum touch target: **44×44px**
- Tab bar items: minimum height **56px** (standard iOS/Android target)
- Drawer nav items: minimum height **48px** padding-included
- Close button: minimum **44×44px**

---

## Anti-Patterns

- Drawer that doesn't have a visible close button (users shouldn't have to discover they can swipe)
- Nav items on mobile < 44px touch target
- Bottom tab bar with > 5 items (no room for labels)
- Drawer that doesn't trap focus (keyboard users tab out of the open drawer)
- No backdrop on drawer (no way to close by tapping outside)
- Navigation that doesn't account for iOS safe area bottom inset
- Hamburger icon without `aria-expanded` + label changes

## Related Files

- `patterns/navigation/header-patterns.md` — desktop header with hamburger trigger
- `patterns/navigation/sidebar-patterns.md` — sidebar that converts to drawer
- `rules/02-layout-and-grid.md` — R11: Safe area insets
- `references/accessibility.md` — focus trap, dialog ARIA
