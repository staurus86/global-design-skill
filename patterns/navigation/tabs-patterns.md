# Pattern — Tabs

> Tabs switch between sibling views of the same content type. They are for navigation within a context — not for multi-step flows, not for filtering, not as primary page navigation.

---

## When to Use Tabs

```
Use tabs when:                         Do NOT use tabs when:
  Views are peer alternatives            Steps are sequential (use wizard)
  User needs to compare views            Content is filtered (use filter bar)
  Views share the same page context      >7 options exist (use select or nav)
  Content is always present              Content loads progressively (use accordion)
```

---

## Pattern 1 — Horizontal Tabs (Default)

The standard tab pattern for 2–6 options within a section.

```html
<div class="tabs" role="tablist" aria-label="Project views">
  <button
    class="tab"
    role="tab"
    aria-selected="true"
    aria-controls="panel-overview"
    id="tab-overview"
  >Overview</button>
  <button
    class="tab"
    role="tab"
    aria-selected="false"
    aria-controls="panel-activity"
    id="tab-activity"
    tabindex="-1"
  >Activity</button>
  <button
    class="tab"
    role="tab"
    aria-selected="false"
    aria-controls="panel-settings"
    id="tab-settings"
    tabindex="-1"
  >Settings</button>
</div>

<div
  class="tab-panel"
  role="tabpanel"
  id="panel-overview"
  aria-labelledby="tab-overview"
>
  Overview content
</div>
<div
  class="tab-panel"
  role="tabpanel"
  id="panel-activity"
  aria-labelledby="tab-activity"
  hidden
>
  Activity content
</div>
<div
  class="tab-panel"
  role="tabpanel"
  id="panel-settings"
  aria-labelledby="tab-settings"
  hidden
>
  Settings content
</div>
```

```css
.tabs {
  display: flex;
  border-bottom: 1px solid var(--color-border);
  gap: 0;
  padding: 0;
  overflow-x: auto;
  scrollbar-width: none;
}

.tab {
  position: relative;
  padding: var(--space-3) var(--space-4);
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-text-secondary);
  background: transparent;
  border: none;
  cursor: pointer;
  white-space: nowrap;
  transition:
    color var(--duration-fast) var(--ease-smooth);
}

.tab::after {
  content: '';
  position: absolute;
  bottom: -1px;
  left: 0; right: 0;
  height: 2px;
  background: var(--color-accent);
  transform: scaleX(0);
  transition: transform var(--duration-fast) var(--ease-spring);
}

.tab:hover { color: var(--color-text-primary); }

.tab[aria-selected="true"] {
  color: var(--color-accent);
  font-weight: var(--font-weight-semibold);
}

.tab[aria-selected="true"]::after { transform: scaleX(1); }

.tab:focus-visible {
  outline: 2px solid var(--color-border-focus);
  outline-offset: -2px;
  border-radius: var(--radius-sm);
}

.tab-panel { padding: var(--space-6) 0; }
.tab-panel[hidden] { display: none; }
```

```js
class TabGroup {
  constructor (el) {
    this.tabs   = [...el.querySelectorAll('[role="tab"]')]
    this.panels = [...el.parentElement.querySelectorAll('[role="tabpanel"]')]

    this.tabs.forEach((tab, i) => {
      tab.addEventListener('click',   () => this.select(i))
      tab.addEventListener('keydown', e  => this.onKey(e, i))
    })
  }

  select (index) {
    this.tabs.forEach((t, i) => {
      const active = i === index
      t.setAttribute('aria-selected', String(active))
      t.tabIndex = active ? 0 : -1
      this.panels[i].hidden = !active
    })
    this.tabs[index].focus()
  }

  onKey (e, i) {
    const map = {
      ArrowRight: (i + 1) % this.tabs.length,
      ArrowLeft:  (i - 1 + this.tabs.length) % this.tabs.length,
      Home:       0,
      End:        this.tabs.length - 1,
    }
    if (map[e.key] !== undefined) {
      e.preventDefault()
      this.select(map[e.key])
    }
  }
}

document.querySelectorAll('[role="tablist"]').forEach(el => new TabGroup(el))
```

---

## Pattern 2 — Pill Tabs (Compact)

For smaller surface areas — settings panels, cards, filter groups with tab semantics.

```html
<div class="tabs-pills" role="tablist" aria-label="View mode">
  <button class="tab-pill" role="tab" aria-selected="true"  aria-controls="panel-grid" id="tab-grid">Grid</button>
  <button class="tab-pill" role="tab" aria-selected="false" aria-controls="panel-list" id="tab-list" tabindex="-1">List</button>
  <button class="tab-pill" role="tab" aria-selected="false" aria-controls="panel-map"  id="tab-map"  tabindex="-1">Map</button>
</div>
```

```css
.tabs-pills {
  display: inline-flex;
  padding: var(--space-1);
  background: var(--color-surface-2);
  border-radius: var(--radius-lg);
  gap: var(--space-1);
}

.tab-pill {
  padding: var(--space-2) var(--space-4);
  border-radius: var(--radius-md);
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-text-secondary);
  background: transparent;
  border: none;
  cursor: pointer;
  transition:
    background var(--duration-fast) var(--ease-smooth),
    color      var(--duration-fast) var(--ease-smooth),
    box-shadow var(--duration-fast) var(--ease-smooth);
}

.tab-pill:hover { color: var(--color-text-primary); }

.tab-pill[aria-selected="true"] {
  background: var(--color-surface);
  color: var(--color-text-primary);
  box-shadow: var(--shadow-sm);
}

.tab-pill:focus-visible {
  outline: 2px solid var(--color-border-focus);
  outline-offset: 2px;
}
```

---

## Pattern 3 — Vertical Tabs (Sidebar Navigation)

For settings pages or dashboards where content is detailed and nav is persistent.

```html
<div class="tabs-vertical">
  <div class="tabs-vertical__nav" role="tablist" aria-label="Settings" aria-orientation="vertical">
    <button class="tab-vertical" role="tab" aria-selected="true"  aria-controls="panel-profile"  id="tab-profile">Profile</button>
    <button class="tab-vertical" role="tab" aria-selected="false" aria-controls="panel-security" id="tab-security" tabindex="-1">Security</button>
    <button class="tab-vertical" role="tab" aria-selected="false" aria-controls="panel-billing"  id="tab-billing"  tabindex="-1">Billing</button>
    <button class="tab-vertical" role="tab" aria-selected="false" aria-controls="panel-api"      id="tab-api"      tabindex="-1">API Keys</button>
  </div>

  <div class="tabs-vertical__panels">
    <div class="tab-panel" role="tabpanel" id="panel-profile"  aria-labelledby="tab-profile">...</div>
    <div class="tab-panel" role="tabpanel" id="panel-security" aria-labelledby="tab-security" hidden>...</div>
    <div class="tab-panel" role="tabpanel" id="panel-billing"  aria-labelledby="tab-billing"  hidden>...</div>
    <div class="tab-panel" role="tabpanel" id="panel-api"      aria-labelledby="tab-api"      hidden>...</div>
  </div>
</div>
```

```css
.tabs-vertical {
  display: grid;
  grid-template-columns: 200px 1fr;
  gap: var(--space-8);
  align-items: start;
}

.tabs-vertical__nav {
  display: flex;
  flex-direction: column;
  gap: var(--space-1);
  position: sticky;
  top: var(--space-6);
}

.tab-vertical {
  display: flex;
  align-items: center;
  padding: var(--space-2) var(--space-3);
  border-radius: var(--radius-md);
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-text-secondary);
  background: transparent;
  border: none;
  cursor: pointer;
  text-align: left;
  transition:
    background var(--duration-fast) var(--ease-smooth),
    color      var(--duration-fast) var(--ease-smooth);
}

.tab-vertical:hover {
  background: var(--color-surface-2);
  color: var(--color-text-primary);
}

.tab-vertical[aria-selected="true"] {
  background: var(--color-accent-subtle);
  color: var(--color-accent-text);
  font-weight: var(--font-weight-semibold);
}

@media (max-width: 640px) {
  .tabs-vertical {
    grid-template-columns: 1fr;
  }
  .tabs-vertical__nav {
    flex-direction: row;
    overflow-x: auto;
    position: static;
    scrollbar-width: none;
  }
}
```

For vertical tabs, change ArrowRight/ArrowLeft to ArrowDown/ArrowUp in the keyboard handler, and add `aria-orientation="vertical"` to the tablist (already shown in HTML above).

---

## Keyboard Behavior

| Key | Action |
|---|---|
| `Tab` | Move focus to active tab, then to tab panel |
| `ArrowRight` / `ArrowDown` | Next tab (wraps) |
| `ArrowLeft` / `ArrowUp` | Previous tab (wraps) |
| `Home` | First tab |
| `End` | Last tab |
| `Enter` / `Space` | Activates focused tab (if using manual activation) |

**Activation model:** The examples above use automatic activation (selection follows focus). For tabs with slow-loading panels, use manual activation (Enter/Space required after focusing).

---

## Anti-Patterns

```
× Tabs for a 2-step checkout — use a wizard/stepper
× Tabs with 10+ items — use a select dropdown or sub-navigation
× Tabs that change the URL without routing logic — breaks browser back
× Nested tabs — maximum 1 tab level
× Tabs used as filters — use a FilterBar component
× Tab labels > 3 words — truncate or reconsider structure
```

---

*Pattern version: global-design-skill v1.0 — `patterns/navigation/tabs-patterns.md`*  
*Related: `patterns/navigation/breadcrumbs.md`, `patterns/navigation/pagination.md`, `rules/07-accessibility.md`*
