# Pattern — Breadcrumbs

> Breadcrumbs show the user's current location within a hierarchical structure. Required on any page 3+ levels deep. Secondary to the primary heading — never the dominant UI element.

---

## When to Use

```
Use breadcrumbs when:                  Do NOT use:
  Page is 3+ levels deep                On flat sites (home → page)
  Hierarchy is meaningful to user       When all pages are siblings
  Users arrive via deep link often      In modals or drawers
  Admin/product UI with nested sections As a replacement for good navigation
```

---

## Pattern 1 — Standard Breadcrumb

```html
<nav aria-label="Breadcrumb" class="breadcrumbs">
  <ol class="breadcrumbs__list">
    <li class="breadcrumbs__item">
      <a href="/" class="breadcrumbs__link">Home</a>
    </li>
    <li class="breadcrumbs__item breadcrumbs__item--sep" aria-hidden="true">
      <svg class="breadcrumbs__chevron" width="12" height="12" viewBox="0 0 16 16" fill="none"
        stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
        <path d="M6 3l5 5-5 5"/>
      </svg>
    </li>
    <li class="breadcrumbs__item">
      <a href="/projects" class="breadcrumbs__link">Projects</a>
    </li>
    <li class="breadcrumbs__item breadcrumbs__item--sep" aria-hidden="true">
      <svg class="breadcrumbs__chevron" width="12" height="12" viewBox="0 0 16 16" fill="none"
        stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
        <path d="M6 3l5 5-5 5"/>
      </svg>
    </li>
    <li class="breadcrumbs__item">
      <a href="/projects/alpha" class="breadcrumbs__link">Alpha</a>
    </li>
    <li class="breadcrumbs__item breadcrumbs__item--sep" aria-hidden="true">
      <svg class="breadcrumbs__chevron" width="12" height="12" viewBox="0 0 16 16" fill="none"
        stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
        <path d="M6 3l5 5-5 5"/>
      </svg>
    </li>
    <li class="breadcrumbs__item">
      <span class="breadcrumbs__current" aria-current="page">Pipeline — Production</span>
    </li>
  </ol>
</nav>
```

```css
.breadcrumbs { margin-bottom: var(--space-6); }

.breadcrumbs__list {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: var(--space-1);
  list-style: none;
  margin: 0; padding: 0;
  font-size: var(--text-sm);
}

.breadcrumbs__item {
  display: flex;
  align-items: center;
  gap: var(--space-1);
}

.breadcrumbs__link {
  color: var(--color-text-secondary);
  text-decoration: none;
  transition: color var(--duration-fast) var(--ease-smooth);
}

.breadcrumbs__link:hover {
  color: var(--color-text-primary);
  text-decoration: underline;
}

.breadcrumbs__link:focus-visible {
  outline: 2px solid var(--color-border-focus);
  outline-offset: 2px;
  border-radius: var(--radius-sm);
}

.breadcrumbs__chevron {
  color: var(--color-text-muted);
  flex-shrink: 0;
}

.breadcrumbs__current {
  color: var(--color-text-primary);
  font-weight: var(--font-weight-medium);
}
```

---

## Pattern 2 — Collapsed Breadcrumb (Long Paths)

When the path is 5+ levels deep, collapse middle items behind an expandable ellipsis.

```html
<nav aria-label="Breadcrumb" class="breadcrumbs breadcrumbs--collapsible">
  <ol class="breadcrumbs__list" id="breadcrumb-list">
    <!-- Always visible: first + last 2 items -->
    <li class="breadcrumbs__item">
      <a href="/" class="breadcrumbs__link">Home</a>
    </li>
    <li class="breadcrumbs__item breadcrumbs__item--sep" aria-hidden="true">
      <svg class="breadcrumbs__chevron" ...><path d="M6 3l5 5-5 5"/></svg>
    </li>

    <!-- Hidden middle items -->
    <li class="breadcrumbs__item breadcrumbs__item--collapsed" id="crumb-collapsed">
      <button
        class="breadcrumbs__expand"
        aria-label="Show full breadcrumb path"
        aria-expanded="false"
        onclick="expandBreadcrumbs()"
      >
        <span aria-hidden="true">···</span>
      </button>
    </li>
    <li class="breadcrumbs__item breadcrumbs__item--sep" aria-hidden="true">
      <svg class="breadcrumbs__chevron" ...><path d="M6 3l5 5-5 5"/></svg>
    </li>

    <!-- Hidden items (shown on expand) -->
    <li class="breadcrumbs__item breadcrumbs__item--hidden" hidden>
      <a href="/org" class="breadcrumbs__link">Organisation</a>
    </li>
    <li class="breadcrumbs__item breadcrumbs__item--sep breadcrumbs__item--hidden" aria-hidden="true" hidden>
      <svg class="breadcrumbs__chevron" ...><path d="M6 3l5 5-5 5"/></svg>
    </li>
    <li class="breadcrumbs__item breadcrumbs__item--hidden" hidden>
      <a href="/org/team" class="breadcrumbs__link">Team</a>
    </li>
    <li class="breadcrumbs__item breadcrumbs__item--sep breadcrumbs__item--hidden" aria-hidden="true" hidden>
      <svg class="breadcrumbs__chevron" ...><path d="M6 3l5 5-5 5"/></svg>
    </li>
    <li class="breadcrumbs__item breadcrumbs__item--hidden" hidden>
      <a href="/org/team/projects" class="breadcrumbs__link">Projects</a>
    </li>
    <li class="breadcrumbs__item breadcrumbs__item--sep breadcrumbs__item--hidden" aria-hidden="true" hidden>
      <svg class="breadcrumbs__chevron" ...><path d="M6 3l5 5-5 5"/></svg>
    </li>

    <!-- Always visible: parent -->
    <li class="breadcrumbs__item">
      <a href="/org/team/projects/alpha" class="breadcrumbs__link">Alpha</a>
    </li>
    <li class="breadcrumbs__item breadcrumbs__item--sep" aria-hidden="true">
      <svg class="breadcrumbs__chevron" ...><path d="M6 3l5 5-5 5"/></svg>
    </li>

    <!-- Current page — always visible -->
    <li class="breadcrumbs__item">
      <span class="breadcrumbs__current" aria-current="page">Pipeline</span>
    </li>
  </ol>
</nav>
```

```css
.breadcrumbs__expand {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0 var(--space-2);
  height: 24px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--color-border);
  background: var(--color-surface-2);
  color: var(--color-text-muted);
  font-size: var(--text-sm);
  cursor: pointer;
  letter-spacing: 0.05em;
  transition:
    background var(--duration-fast) var(--ease-smooth),
    color      var(--duration-fast) var(--ease-smooth);
}

.breadcrumbs__expand:hover {
  background: var(--color-surface-3);
  color: var(--color-text-primary);
}
```

```js
function expandBreadcrumbs () {
  document.querySelectorAll('.breadcrumbs__item--hidden').forEach(el => { el.hidden = false })
  document.getElementById('crumb-collapsed').hidden = true
}
```

---

## Pattern 3 — Breadcrumb with Dropdown (Last Ancestor)

When the direct parent has siblings worth navigating to, expose a dropdown on hover.

```html
<nav aria-label="Breadcrumb" class="breadcrumbs">
  <ol class="breadcrumbs__list">
    <li class="breadcrumbs__item">
      <a href="/" class="breadcrumbs__link">Home</a>
    </li>
    <li class="breadcrumbs__item breadcrumbs__item--sep" aria-hidden="true">
      <svg class="breadcrumbs__chevron" ...><path d="M6 3l5 5-5 5"/></svg>
    </li>

    <!-- Parent with sibling dropdown -->
    <li class="breadcrumbs__item breadcrumbs__item--dropdown">
      <button class="breadcrumbs__dropdown-trigger" aria-expanded="false" aria-haspopup="true">
        <a href="/projects/alpha" class="breadcrumbs__link">Alpha</a>
        <svg width="10" height="10" viewBox="0 0 16 16" fill="none"
          stroke="currentColor" stroke-width="1.5">
          <path d="M3 6l5 5 5-5"/>
        </svg>
      </button>
      <ul class="breadcrumbs__dropdown" role="menu" hidden>
        <li><a href="/projects/beta"  class="breadcrumbs__dropdown-item" role="menuitem">Beta</a></li>
        <li><a href="/projects/gamma" class="breadcrumbs__dropdown-item" role="menuitem">Gamma</a></li>
        <li><a href="/projects"       class="breadcrumbs__dropdown-item" role="menuitem">All projects</a></li>
      </ul>
    </li>

    <li class="breadcrumbs__item breadcrumbs__item--sep" aria-hidden="true">
      <svg class="breadcrumbs__chevron" ...><path d="M6 3l5 5-5 5"/></svg>
    </li>
    <li class="breadcrumbs__item">
      <span class="breadcrumbs__current" aria-current="page">Pipeline — Production</span>
    </li>
  </ol>
</nav>
```

```css
.breadcrumbs__item--dropdown { position: relative; }

.breadcrumbs__dropdown-trigger {
  display: inline-flex;
  align-items: center;
  gap: var(--space-1);
  background: transparent;
  border: none;
  padding: 0;
  cursor: pointer;
}

.breadcrumbs__dropdown {
  position: absolute;
  top: calc(100% + var(--space-2));
  left: 0;
  min-width: 160px;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-lg);
  padding: var(--space-1);
  list-style: none;
  z-index: var(--z-dropdown);
}

.breadcrumbs__dropdown-item {
  display: block;
  padding: var(--space-2) var(--space-3);
  border-radius: var(--radius-sm);
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
  text-decoration: none;
  transition: background var(--duration-fast) var(--ease-smooth);
}

.breadcrumbs__dropdown-item:hover {
  background: var(--color-surface-2);
  color: var(--color-text-primary);
}
```

---

## JSON-LD Structured Data

Add to `<head>` for SEO — Google uses BreadcrumbList to generate sitelinks in search results.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://example.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Projects",
      "item": "https://example.com/projects"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Alpha",
      "item": "https://example.com/projects/alpha"
    },
    {
      "@type": "ListItem",
      "position": 4,
      "name": "Pipeline — Production"
    }
  ]
}
</script>
```

---

## Placement and Styling Rules

```
Position:   Directly below the header/nav, above the page title
Font size:  var(--text-sm) — smaller than body, never larger
Color:      text-secondary for links, text-primary for current
Weight:     regular for links, medium for current page
Separator:  > chevron icon (not / slash — more compact, directional)
Max length: truncate item labels at 24 characters with ellipsis if needed
Margin:     margin-bottom: var(--space-6) before page heading
```

---

## Anti-Patterns

```
× Breadcrumbs on a 1-2 level flat site — creates false sense of hierarchy
× Current page as a link (it's already here)
× Using / text separator instead of a directional chevron icon
× Breadcrumbs inside modals or drawers
× Breadcrumbs as the only navigation — pair with sidebar or primary nav
× More than 6 visible items without collapsing (use ellipsis pattern)
```

---

*Pattern version: global-design-skill v1.0 — `patterns/navigation/breadcrumbs.md`*  
*Related: `recipes/improve-navigation.md`, `patterns/navigation/tabs-patterns.md`, `rules/07-accessibility.md`*
