# Recipe — Improve Navigation

> **Trigger:** Navigation feels confusing, users complain about "getting lost", analytics show high drop-off on interior pages, or the nav has grown organically into a mess of 12+ items.

---

## Diagnosis Checklist

Before applying fixes, identify which problems are present:

```
[ ] More than 7 items in the top nav (Hick's Law violation)
[ ] Nav items are feature names, not user goals ("Dashboard", "Reports", "Tools")
[ ] Active state is invisible or ambiguous
[ ] No visual hierarchy between primary and secondary nav items
[ ] Mobile nav: hamburger with no visible state indicator
[ ] Breadcrumbs missing on pages 3+ levels deep
[ ] Back navigation impossible without browser back button
[ ] Current page not highlighted in sidebar
[ ] Search is buried or missing
[ ] Nav covers useful content on scroll (sticky nav too tall)
[ ] No skip navigation link (keyboard users)
[ ] Logo doesn't link to home
```

---

## Step 1 — Audit and reduce nav items (Hick's Law)

More than 7 navigation items creates decision paralysis. Every item above 7 increases time-to-decision and increases the chance of clicking nothing.

**Reduction process:**

```
1. List all current nav items
2. Group them by user goal, not product feature:
   "Pipeline", "Deploys", "Builds", "Environments" → all serve "Ship code"
   Collapse to "Deployments" with sub-navigation
3. Move low-frequency items to profile menu or settings
4. Move utility items (Help, Docs, Status) to footer or secondary nav
5. Target: 5–7 items maximum in primary nav
```

```
Before (12 items): Dashboard / Projects / Pipelines / Deploys / Builds / Environments / Domains / Team / Billing / Settings / Documentation / Status

After (6 items): Overview / Deployments / Projects / Team / Settings / [Help icon]
```

---

## Step 2 — Rename items to user goals, not feature names

Navigation labels should answer "what will I do here?" not "what is this section called in the codebase?"

```
Before → After:

"Dashboard"        → "Overview" (or the actual value: "Activity")
"Analytics"        → "Usage & performance"  
"Reports"          → "Insights" or remove if rarely used
"Tools"            → Split into specific items or remove
"Resources"        → "Documentation" (specific)
"Administration"   → "Settings"
"My Account"       → avatar/profile menu (doesn't need a nav slot)
```

---

## Step 3 — Clear active state

The active state tells the user "you are here." It must be impossible to miss.

```css
/* Correct: strong active state — background + color + weight */
.nav-item {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  padding: var(--space-2) var(--space-3);
  border-radius: var(--radius-md);
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-text-secondary);
  text-decoration: none;
  transition: background var(--duration-fast) var(--ease-smooth),
              color     var(--duration-fast) var(--ease-smooth);
}

.nav-item:hover {
  background: var(--color-surface-2);
  color: var(--color-text-primary);
}

.nav-item[aria-current="page"],
.nav-item.active {
  background: oklch(from var(--color-accent) l c h / 0.10);
  color: var(--color-accent);
  font-weight: var(--font-weight-semibold);
}

/* Wrong: only color change — too subtle */
.nav-item.active { color: var(--color-accent); }

/* Wrong: underline only — looks like a link, not a location indicator */
.nav-item.active { text-decoration: underline; }
```

```html
<!-- Always use aria-current="page" on the current page's nav link -->
<a href="/deployments" class="nav-item" aria-current="page">Deployments</a>
<a href="/projects"    class="nav-item">Projects</a>
```

---

## Step 4 — Establish visual hierarchy between primary and secondary nav

Not all nav items are equal. Primary items (used daily) should be visually louder than secondary items (used monthly).

```html
<!-- Header nav: primary items full, secondary items as icons or text-only -->
<header class="site-header">
  <nav class="header-nav" aria-label="Main navigation">
    <!-- Primary: icon + label -->
    <a href="/overview"     class="nav-item nav-item--primary" aria-current="page">
      <svg aria-hidden="true" class="icon" ...></svg> Overview
    </a>
    <a href="/deployments"  class="nav-item nav-item--primary">
      <svg aria-hidden="true" class="icon" ...></svg> Deployments
    </a>

    <!-- Secondary: text only, muted -->
    <a href="/docs"     class="nav-item nav-item--secondary">Docs</a>
    <a href="/status"   class="nav-item nav-item--secondary">Status</a>
  </nav>

  <!-- Utility: avatar, notifications -->
  <div class="header-utils">
    <button class="icon-btn" aria-label="Notifications">...</button>
    <button class="avatar-btn" aria-label="Account menu">...</button>
  </div>
</header>
```

```css
.nav-item--primary  { font-weight: var(--font-weight-medium); }
.nav-item--secondary {
  font-size: var(--text-sm);
  color: var(--color-text-muted);
}
.nav-item--secondary:hover { color: var(--color-text-secondary); }
```

---

## Step 5 — Fix the mobile navigation

Mobile nav must communicate its state and be easy to open and close.

```html
<!-- Mobile: hamburger with clear open/closed state -->
<button
  type="button"
  class="nav-toggle"
  aria-expanded="false"
  aria-controls="mobile-menu"
  aria-label="Open navigation menu"
>
  <!-- Hamburger icon — animates to X when open -->
  <span class="hamburger-line"></span>
  <span class="hamburger-line"></span>
  <span class="hamburger-line"></span>
</button>

<nav
  class="mobile-menu"
  id="mobile-menu"
  aria-label="Mobile navigation"
  hidden
>
  <a href="/overview"    class="mobile-nav-item" aria-current="page">Overview</a>
  <a href="/deployments" class="mobile-nav-item">Deployments</a>
  <a href="/projects"    class="mobile-nav-item">Projects</a>
  <a href="/team"        class="mobile-nav-item">Team</a>
  <a href="/settings"    class="mobile-nav-item">Settings</a>
</nav>
```

```css
.nav-toggle {
  display: none;
  flex-direction: column;
  gap: 5px;
  padding: var(--space-2);
  background: transparent;
  border: none;
  cursor: pointer;
  width: 44px; height: 44px;
  align-items: center;
  justify-content: center;
  border-radius: var(--radius-md);
}

@media (max-width: 768px) { .nav-toggle { display: flex; } }

.hamburger-line {
  display: block;
  width: 20px; height: 2px;
  background: var(--color-text-primary);
  border-radius: 2px;
  transition: transform var(--duration-fast) var(--ease-spring),
              opacity  var(--duration-fast) var(--ease-smooth);
}

.nav-toggle[aria-expanded="true"] .hamburger-line:nth-child(1) { transform: translateY(7px) rotate(45deg); }
.nav-toggle[aria-expanded="true"] .hamburger-line:nth-child(2) { opacity: 0; }
.nav-toggle[aria-expanded="true"] .hamburger-line:nth-child(3) { transform: translateY(-7px) rotate(-45deg); }

.mobile-menu {
  position: fixed;
  top: var(--header-height);
  left: 0; right: 0;
  background: var(--color-surface);
  border-bottom: 1px solid var(--color-border);
  padding: var(--space-4);
  display: flex;
  flex-direction: column;
  gap: var(--space-1);
  z-index: var(--z-sticky);
  box-shadow: var(--shadow-lg);
}

.mobile-nav-item {
  display: flex;
  align-items: center;
  padding: var(--space-3) var(--space-4);
  border-radius: var(--radius-md);
  font-size: var(--text-body);
  font-weight: var(--font-weight-medium);
  color: var(--color-text-secondary);
  text-decoration: none;
  min-height: 44px;
}
.mobile-nav-item[aria-current="page"] {
  background: var(--color-surface-2);
  color: var(--color-text-primary);
}
```

```js
const toggle = document.querySelector('.nav-toggle')
const menu   = document.getElementById('mobile-menu')

toggle.addEventListener('click', () => {
  const open = toggle.getAttribute('aria-expanded') === 'true'
  toggle.setAttribute('aria-expanded', String(!open))
  toggle.setAttribute('aria-label', open ? 'Open navigation menu' : 'Close navigation menu')
  menu.hidden = open
})

// Close on Escape
document.addEventListener('keydown', e => {
  if (e.key === 'Escape' && !menu.hidden) {
    menu.hidden = true
    toggle.setAttribute('aria-expanded', 'false')
    toggle.focus()
  }
})
```

---

## Step 6 — Add breadcrumbs on deep pages

Any page more than 2 levels deep needs breadcrumbs. Users should always be able to answer "where am I?"

```html
<!-- Appears below the header, above page title -->
<nav aria-label="Breadcrumb" class="breadcrumbs">
  <ol class="breadcrumbs__list">
    <li class="breadcrumbs__item">
      <a href="/" class="breadcrumbs__link">Home</a>
    </li>
    <li class="breadcrumbs__item" aria-hidden="true">
      <span class="breadcrumbs__sep">/</span>
    </li>
    <li class="breadcrumbs__item">
      <a href="/projects" class="breadcrumbs__link">Projects</a>
    </li>
    <li class="breadcrumbs__item" aria-hidden="true">
      <span class="breadcrumbs__sep">/</span>
    </li>
    <li class="breadcrumbs__item">
      <span aria-current="page" class="breadcrumbs__current">Pipeline — Production</span>
    </li>
  </ol>
</nav>
```

```css
.breadcrumbs__list {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: var(--space-2);
  list-style: none;
  padding: 0;
  font-size: var(--text-sm);
}
.breadcrumbs__link { color: var(--color-text-secondary); text-decoration: none; }
.breadcrumbs__link:hover { color: var(--color-text-primary); text-decoration: underline; }
.breadcrumbs__sep { color: var(--color-text-muted); }
.breadcrumbs__current { color: var(--color-text-primary); font-weight: var(--font-weight-medium); }
```

---

## Result Verification

```
[ ] Nav items ≤ 7 in primary nav
[ ] Items named for user goals, not feature/section names
[ ] Active state: background + color change, clearly visible
[ ] Visual hierarchy: primary items louder than secondary
[ ] Mobile: hamburger animates to X, menu opens correctly
[ ] Escape closes mobile menu, focus returns to toggle
[ ] Breadcrumbs on all pages 3+ levels deep
[ ] Logo links to home
[ ] Skip navigation link at top of page
[ ] aria-current="page" on active nav item
[ ] All nav items keyboard accessible (Tab + Enter)
```

---

*Recipe version: global-design-skill v1.0 — `recipes/improve-navigation.md`*
*Related: `rules/02-cognitive-laws.md` R1 (Hick's Law), `rules/07-accessibility.md`, `patterns/navigation/header-patterns.md`, `patterns/navigation/mobile-navigation.md`*
