# Pattern — Sidebar Navigation

> The sidebar is the primary navigation for complex applications. It must reflect the user's current context, support deep hierarchy without overwhelming, and stay efficient for daily use.

---

## When to Use a Sidebar

Use a sidebar when:
- The app has 5+ primary sections
- Users frequently switch between sections
- There is meaningful hierarchy (sections → subsections → items)
- The app is desktop-primary

Use top navigation instead when:
- The app has ≤ 5 sections
- The product is mobile-first
- The UI is content-heavy (documentation, blog)

---

## Pattern A — Standard App Sidebar

Best for: SaaS apps, project tools, analytics dashboards.

```html
<aside class="sidebar" aria-label="Application navigation">
  <!-- Workspace / org switcher -->
  <div class="sidebar__workspace">
    <button class="workspace-switcher" aria-haspopup="true" aria-expanded="false">
      <span class="workspace-avatar" aria-hidden="true">A</span>
      <span class="workspace-name">Acme Design</span>
      <span class="workspace-chevron" aria-hidden="true">⌄</span>
    </button>
  </div>

  <!-- Primary navigation -->
  <nav aria-label="Main navigation">
    <ul class="sidebar-nav" role="list">
      <!-- Section with no children -->
      <li>
        <a
          href="/dashboard"
          class="sidebar-nav__item"
          aria-current="page"
        >
          <span class="sidebar-nav__icon" aria-hidden="true">
            <!-- SVG icon -->
          </span>
          <span class="sidebar-nav__label">Dashboard</span>
        </a>
      </li>

      <!-- Section with children (collapsible) -->
      <li class="sidebar-nav__group">
        <button
          class="sidebar-nav__item sidebar-nav__item--expandable"
          aria-expanded="true"
          aria-controls="projects-submenu"
        >
          <span class="sidebar-nav__icon" aria-hidden="true"><!-- SVG --></span>
          <span class="sidebar-nav__label">Projects</span>
          <span class="sidebar-nav__count" aria-label="14 projects">14</span>
          <span class="sidebar-nav__chevron" aria-hidden="true"></span>
        </button>
        <ul id="projects-submenu" class="sidebar-subnav" role="list">
          <li>
            <a href="/projects/alpha" class="sidebar-subnav__item">
              <span class="sidebar-subnav__dot" aria-hidden="true"></span>
              Alpha redesign
            </a>
          </li>
          <li>
            <a href="/projects/beta" class="sidebar-subnav__item">
              <span class="sidebar-subnav__dot" aria-hidden="true"></span>
              Beta launch
            </a>
          </li>
          <li>
            <a href="/projects" class="sidebar-subnav__item sidebar-subnav__item--more">
              View all projects →
            </a>
          </li>
        </ul>
      </li>

      <li>
        <a href="/team" class="sidebar-nav__item">
          <span class="sidebar-nav__icon" aria-hidden="true"><!-- SVG --></span>
          <span class="sidebar-nav__label">Team</span>
        </a>
      </li>

      <li>
        <a href="/analytics" class="sidebar-nav__item">
          <span class="sidebar-nav__icon" aria-hidden="true"><!-- SVG --></span>
          <span class="sidebar-nav__label">Analytics</span>
          <span class="sidebar-nav__badge" aria-label="New">New</span>
        </a>
      </li>
    </ul>
  </nav>

  <!-- Divider -->
  <div class="sidebar__divider" role="separator"></div>

  <!-- Secondary navigation (settings, help, etc.) -->
  <nav aria-label="Secondary navigation">
    <ul class="sidebar-nav" role="list">
      <li>
        <a href="/settings" class="sidebar-nav__item">
          <span class="sidebar-nav__icon" aria-hidden="true"><!-- SVG --></span>
          <span class="sidebar-nav__label">Settings</span>
        </a>
      </li>
    </ul>
  </nav>

  <!-- User footer -->
  <div class="sidebar__footer">
    <button class="sidebar-user" aria-haspopup="true">
      <img src="/avatars/sarah.webp" alt="Sarah Chen" width="32" height="32" class="sidebar-user__avatar" />
      <div class="sidebar-user__info">
        <span class="sidebar-user__name">Sarah Chen</span>
        <span class="sidebar-user__role">Admin</span>
      </div>
    </button>
  </div>
</aside>
```

```css
.sidebar {
  width: var(--sidebar-width, 240px);
  height: 100dvh;
  position: sticky;
  top: 0;
  display: flex;
  flex-direction: column;
  background: var(--color-surface);
  border-right: 1px solid var(--color-border);
  overflow-y: auto;
  overflow-x: hidden;
  scrollbar-width: thin;
  transition: width 200ms cubic-bezier(0.16, 1, 0.3, 1);
}

/* Collapsed state */
.sidebar.collapsed {
  width: var(--sidebar-width-collapsed, 64px);
}

.sidebar.collapsed .sidebar-nav__label,
.sidebar.collapsed .sidebar-nav__count,
.sidebar.collapsed .sidebar-nav__badge,
.sidebar.collapsed .workspace-name,
.sidebar.collapsed .sidebar-user__info {
  opacity: 0;
  pointer-events: none;
  width: 0;
  overflow: hidden;
}

/* Workspace switcher */
.sidebar__workspace {
  padding: var(--space-4);
  border-bottom: 1px solid var(--color-border);
}

.workspace-switcher {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  width: 100%;
  background: transparent;
  border: none;
  padding: var(--space-2) var(--space-3);
  border-radius: var(--radius-lg);
  cursor: pointer;
  transition: background 120ms;
  text-align: left;
}

.workspace-switcher:hover { background: var(--color-surface-2); }

.workspace-avatar {
  width: 28px;
  height: 28px;
  border-radius: var(--radius-sm);
  background: var(--color-accent);
  color: oklch(10% 0.01 258);
  display: grid;
  place-items: center;
  font-weight: 700;
  font-size: 0.875rem;
  flex-shrink: 0;
}

.workspace-name {
  font-weight: 500;
  font-size: 0.9375rem;
  flex: 1;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  transition: opacity 200ms, width 200ms;
}

/* Navigation items */
.sidebar-nav {
  list-style: none;
  padding: var(--space-2) var(--space-3);
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: var(--space-1);
  flex: 1;
}

.sidebar-nav__item {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  padding: var(--space-2) var(--space-3);
  border-radius: var(--radius-md);
  font-size: 0.9375rem;
  color: var(--color-text-secondary);
  text-decoration: none;
  transition: background 120ms, color 120ms;
  cursor: pointer;
  background: transparent;
  border: none;
  width: 100%;
  text-align: left;
  font-family: inherit;
  white-space: nowrap;
  min-height: 36px;
}

.sidebar-nav__item:hover {
  background: var(--color-surface-2);
  color: var(--color-text-primary);
}

.sidebar-nav__item[aria-current="page"],
.sidebar-nav__item.active {
  background: oklch(from var(--color-accent) l c h / 0.1);
  color: var(--color-accent);
  font-weight: 500;
}

.sidebar-nav__icon {
  width: 18px;
  height: 18px;
  flex-shrink: 0;
  opacity: 0.7;
}

.sidebar-nav__item[aria-current="page"] .sidebar-nav__icon,
.sidebar-nav__item.active .sidebar-nav__icon { opacity: 1; }

.sidebar-nav__label {
  flex: 1;
  transition: opacity 200ms;
}

.sidebar-nav__count {
  font-size: 0.75rem;
  color: var(--color-text-muted);
  background: var(--color-surface-2);
  padding: 0.1em 0.5em;
  border-radius: 9999px;
}

.sidebar-nav__badge {
  font-size: 0.625rem;
  font-weight: 600;
  background: var(--color-accent);
  color: oklch(10% 0.01 258);
  padding: 0.15em 0.5em;
  border-radius: 9999px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.sidebar-nav__chevron {
  width: 12px;
  height: 12px;
  border-right: 1.5px solid currentColor;
  border-bottom: 1.5px solid currentColor;
  transform: rotate(45deg);
  transition: transform 200ms;
  opacity: 0.5;
}

.sidebar-nav__item--expandable[aria-expanded="true"] .sidebar-nav__chevron {
  transform: rotate(-135deg);
}

/* Subnav */
.sidebar-subnav {
  list-style: none;
  padding: var(--space-1) 0 var(--space-1) calc(var(--space-3) + 18px + var(--space-3));
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.sidebar-subnav__item {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  padding: var(--space-1) var(--space-3);
  border-radius: var(--radius-md);
  font-size: 0.875rem;
  color: var(--color-text-muted);
  text-decoration: none;
  transition: background 120ms, color 120ms;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.sidebar-subnav__item:hover {
  background: var(--color-surface-2);
  color: var(--color-text-primary);
}

.sidebar-subnav__item[aria-current="page"] {
  color: var(--color-text-primary);
  font-weight: 500;
}

.sidebar-subnav__dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: currentColor;
  flex-shrink: 0;
  opacity: 0.4;
}

.sidebar-subnav__item[aria-current="page"] .sidebar-subnav__dot { opacity: 1; }

.sidebar-subnav__item--more {
  font-size: 0.8125rem;
  opacity: 0.6;
}

/* Divider */
.sidebar__divider {
  height: 1px;
  background: var(--color-border);
  margin: var(--space-2) var(--space-4);
}

/* User footer */
.sidebar__footer {
  padding: var(--space-3) var(--space-4);
  border-top: 1px solid var(--color-border);
  margin-top: auto;
}

.sidebar-user {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  width: 100%;
  background: transparent;
  border: none;
  padding: var(--space-2) var(--space-3);
  border-radius: var(--radius-lg);
  cursor: pointer;
  text-align: left;
  transition: background 120ms;
}

.sidebar-user:hover { background: var(--color-surface-2); }

.sidebar-user__avatar { border-radius: 50%; object-fit: cover; flex-shrink: 0; }

.sidebar-user__name {
  display: block;
  font-size: 0.875rem;
  font-weight: 500;
  white-space: nowrap;
}

.sidebar-user__role {
  display: block;
  font-size: 0.75rem;
  color: var(--color-text-muted);
}
```

---

## Pattern B — Icon-Only Collapsed Sidebar

When sidebar is collapsed, show only icons. Expand on hover or via toggle button.

```css
/* Collapsed: tooltips replace labels */
.sidebar.collapsed .sidebar-nav__item {
  justify-content: center;
  position: relative;
}

/* Tooltip on hover when collapsed */
.sidebar.collapsed .sidebar-nav__item::after {
  content: attr(data-label);
  position: absolute;
  left: calc(100% + var(--space-3));
  top: 50%;
  translate: 0 -50%;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  padding: var(--space-2) var(--space-3);
  font-size: 0.875rem;
  white-space: nowrap;
  opacity: 0;
  pointer-events: none;
  box-shadow: 0 4px 16px oklch(0% 0 0 / 0.2);
  transition: opacity 150ms 200ms; /* delay prevents flash on quick hover-through */
}

.sidebar.collapsed .sidebar-nav__item:hover::after { opacity: 1; }
```

Add `data-label="Dashboard"` to each nav item for the tooltip content.

---

## Collapse Toggle Button

```html
<button
  class="sidebar-toggle"
  aria-label="Collapse navigation sidebar"
  aria-controls="sidebar"
  aria-expanded="true"
  onclick="toggleSidebar()"
>
  <span aria-hidden="true">«</span>
</button>
```

```css
.sidebar-toggle {
  position: absolute;
  right: -12px;
  top: 72px;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  cursor: pointer;
  display: grid;
  place-items: center;
  font-size: 0.75rem;
  transition: background 120ms;
  z-index: 1;
}

.sidebar-toggle:hover { background: var(--color-surface-2); }

.sidebar.collapsed .sidebar-toggle { transform: rotate(180deg); }
```

---

## Anti-Patterns

- More than 7 primary nav items (Hick's Law)
- Nesting deeper than 2 levels (section → subsection is enough)
- Active state via color alone (add background or weight)
- Icon-only sidebar without tooltips (inaccessible, especially for non-standard icons)
- Sidebar that doesn't scroll when content overflows (nav items get cut off)
- Collapsible groups that don't respect `prefers-reduced-motion`
- Workspace switcher that has no loading state

## Related Files

- `patterns/navigation/header-patterns.md` — top navigation
- `patterns/navigation/mobile-navigation.md` — sidebar on mobile
- `blueprints/saas-app-from-scratch.md` — Shell Option A
- `blueprints/admin-panel-from-scratch.md` — Admin shell
- `references/accessibility.md` — ARIA for nav, current page, expanded
