# Pattern — Filters and Search

> Filters help operators find specific records in large datasets. They must be fast to apply, visually clear when active, and easily cleared. Active filters are always visible as dismissible chips.

---

## Filter Architecture Decisions

```
Filter types needed:  [search / select / date range / boolean / number range]
State persistence:    [URL params / session storage / user preferences]
Filter location:      [above table / in sidebar / in header]
Search:               [client-side / server-side / debounced API]
```

**URL params (recommended for most cases):**
- Shareable: send the URL to a colleague and they see the same filtered view
- Refreshable: page reload preserves the filter state
- Bookmarkable: operators can save filtered views

---

## Pattern A — Horizontal Filter Bar (standard)

Best for: tables with 3-6 filter dimensions. Sits directly above the data table.

```html
<div class="filter-bar" role="search" aria-label="Filter projects">
  <!-- Search input -->
  <div class="filter-search">
    <span class="filter-search__icon" aria-hidden="true">⌕</span>
    <input
      type="search"
      class="filter-search__input"
      placeholder="Search projects…"
      aria-label="Search projects by name"
      id="table-search"
      autocomplete="off"
    />
    <!-- Clear search button — appears when input has value -->
    <button
      class="filter-search__clear"
      aria-label="Clear search"
      hidden
    >×</button>
  </div>

  <!-- Filter dropdowns -->
  <div class="filter-controls">
    <button
      class="filter-btn"
      aria-haspopup="listbox"
      aria-expanded="false"
      data-filter="status"
    >
      Status
      <span class="filter-btn__chevron" aria-hidden="true"></span>
    </button>

    <button
      class="filter-btn"
      aria-haspopup="listbox"
      aria-expanded="false"
      data-filter="assigned"
    >
      Assigned to
      <span class="filter-btn__chevron" aria-hidden="true"></span>
    </button>

    <button
      class="filter-btn filter-btn--active"
      aria-haspopup="listbox"
      aria-expanded="false"
      data-filter="created"
      aria-label="Date filter: Last 30 days (active)"
    >
      Created: Last 30 days
      <span class="filter-btn__chevron" aria-hidden="true"></span>
    </button>

    <!-- More filters (collapses less-used filters) -->
    <button class="filter-btn filter-btn--more">
      More filters
    </button>
  </div>

  <!-- Spacer -->
  <div class="filter-bar__spacer"></div>

  <!-- Clear all (only when filters are active) -->
  <button
    class="filter-clear"
    onclick="clearAllFilters()"
    aria-live="polite"
  >
    Clear all filters
  </button>
</div>

<!-- Active filter chips (below filter bar) -->
<div class="active-filters" aria-label="Active filters" aria-live="polite">
  <span class="active-filters__label">Filtered by:</span>

  <div class="filter-chips">
    <div class="filter-chip">
      <span>Status: Active</span>
      <button
        class="filter-chip__remove"
        aria-label="Remove Status filter"
        onclick="removeFilter('status')"
      >×</button>
    </div>

    <div class="filter-chip">
      <span>Assigned: Sarah Chen</span>
      <button
        class="filter-chip__remove"
        aria-label="Remove Assigned to filter"
        onclick="removeFilter('assigned')"
      >×</button>
    </div>
  </div>
</div>
```

```css
/* Filter bar */
.filter-bar {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  padding: var(--space-4) var(--space-6);
  border-bottom: 1px solid var(--color-border);
  flex-wrap: wrap;
}

/* Search input */
.filter-search {
  position: relative;
  flex: 1;
  min-width: 200px;
  max-width: 320px;
}

.filter-search__icon {
  position: absolute;
  left: var(--space-3);
  top: 50%;
  translate: 0 -50%;
  color: var(--color-text-muted);
  font-size: 1rem;
  pointer-events: none;
}

.filter-search__input {
  width: 100%;
  height: 36px;
  padding-left: var(--space-8);
  padding-right: var(--space-8);
  background: var(--color-surface-2);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  font-size: 0.9375rem;
  color: var(--color-text-primary);
  outline: none;
  transition: border-color 150ms, background 150ms;
}

.filter-search__input:focus {
  border-color: var(--color-accent);
  background: var(--color-surface);
}

.filter-search__input::placeholder { color: var(--color-text-muted); }

/* Native search clear button */
.filter-search__input::-webkit-search-cancel-button { display: none; }

.filter-search__clear {
  position: absolute;
  right: var(--space-2);
  top: 50%;
  translate: 0 -50%;
  background: transparent;
  border: none;
  color: var(--color-text-muted);
  cursor: pointer;
  font-size: 1rem;
  width: 24px;
  height: 24px;
  display: grid;
  place-items: center;
  border-radius: var(--radius-sm);
}

/* Filter buttons */
.filter-controls {
  display: flex;
  gap: var(--space-2);
  flex-wrap: wrap;
}

.filter-btn {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  height: 36px;
  padding-inline: var(--space-3);
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  font-size: 0.875rem;
  color: var(--color-text-secondary);
  cursor: pointer;
  white-space: nowrap;
  transition: border-color 150ms, background 150ms, color 150ms;
}

.filter-btn:hover {
  border-color: var(--color-text-muted);
  color: var(--color-text-primary);
}

.filter-btn--active {
  background: oklch(from var(--color-accent) l c h / 0.1);
  border-color: var(--color-accent);
  color: var(--color-text-primary);
  font-weight: 500;
}

.filter-btn__chevron {
  width: 10px;
  height: 10px;
  border-right: 1.5px solid currentColor;
  border-bottom: 1.5px solid currentColor;
  transform: rotate(45deg) translateY(-1px);
  opacity: 0.6;
}

.filter-btn__chevron.open { transform: rotate(-135deg) translateY(1px); }

.filter-bar__spacer { flex: 1; }

.filter-clear {
  font-size: 0.875rem;
  color: var(--color-text-muted);
  background: transparent;
  border: none;
  cursor: pointer;
  text-decoration: underline;
  text-underline-offset: 2px;
  white-space: nowrap;
  padding: 0;
  transition: color 150ms;
}

.filter-clear:hover { color: var(--color-text-primary); }

/* Active filter chips */
.active-filters {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  padding: var(--space-3) var(--space-6);
  border-bottom: 1px solid var(--color-border);
  flex-wrap: wrap;
  background: oklch(from var(--color-accent) l c h / 0.03);
}

.active-filters:empty { display: none; }

.active-filters__label {
  font-size: 0.8125rem;
  color: var(--color-text-muted);
  flex-shrink: 0;
}

.filter-chips {
  display: flex;
  gap: var(--space-2);
  flex-wrap: wrap;
}

.filter-chip {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  height: 28px;
  padding-left: var(--space-3);
  padding-right: var(--space-2);
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: 9999px;
  font-size: 0.8125rem;
}

.filter-chip__remove {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: var(--color-surface-2);
  border: none;
  cursor: pointer;
  display: grid;
  place-items: center;
  font-size: 0.75rem;
  color: var(--color-text-muted);
  transition: background 120ms, color 120ms;
}

.filter-chip__remove:hover {
  background: var(--color-error);
  color: white;
}
```

---

## Pattern B — Filter Dropdown Panel

The dropdown that appears when a filter button is clicked.

```html
<div
  class="filter-panel"
  id="status-filter-panel"
  role="listbox"
  aria-label="Filter by status"
  aria-multiselectable="true"
>
  <div class="filter-panel__search">
    <input
      type="search"
      placeholder="Search statuses…"
      aria-label="Search filter options"
    />
  </div>

  <ul class="filter-panel__options">
    <li
      class="filter-option filter-option--selected"
      role="option"
      aria-selected="true"
      onclick="toggleFilter('status', 'active')"
    >
      <span class="filter-option__check" aria-hidden="true">✓</span>
      <span class="badge badge-active">Active</span>
      <span class="filter-option__count">2,847</span>
    </li>
    <li
      class="filter-option"
      role="option"
      aria-selected="false"
      onclick="toggleFilter('status', 'pending')"
    >
      <span class="filter-option__check" aria-hidden="true"></span>
      <span class="badge badge-pending">Pending</span>
      <span class="filter-option__count">341</span>
    </li>
    <li
      class="filter-option"
      role="option"
      aria-selected="false"
      onclick="toggleFilter('status', 'inactive')"
    >
      <span class="filter-option__check" aria-hidden="true"></span>
      <span class="badge badge-inactive">Inactive</span>
      <span class="filter-option__count">1,644</span>
    </li>
  </ul>

  <div class="filter-panel__footer">
    <button class="btn-ghost btn-sm" onclick="clearFilter('status')">Clear</button>
    <button class="btn-primary btn-sm" onclick="applyFilter('status')">Apply</button>
  </div>
</div>
```

```css
.filter-panel {
  position: absolute;
  top: calc(100% + var(--space-2));
  left: 0;
  z-index: var(--z-dropdown);
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  box-shadow: 0 8px 32px oklch(0% 0 0 / 0.2);
  min-width: 240px;
  overflow: hidden;
}

.filter-panel__search {
  padding: var(--space-3);
  border-bottom: 1px solid var(--color-border);
}

.filter-panel__search input {
  width: 100%;
  padding: var(--space-2) var(--space-3);
  background: var(--color-surface-2);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  font-size: 0.875rem;
}

.filter-panel__options {
  list-style: none;
  padding: var(--space-2);
  margin: 0;
  max-height: 240px;
  overflow-y: auto;
}

.filter-option {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  padding: var(--space-2) var(--space-3);
  border-radius: var(--radius-md);
  cursor: pointer;
  transition: background 120ms;
}

.filter-option:hover { background: var(--color-surface-2); }

.filter-option__check {
  width: 16px;
  height: 16px;
  border: 1.5px solid var(--color-border);
  border-radius: var(--radius-sm);
  display: grid;
  place-items: center;
  font-size: 0.6875rem;
  color: transparent;
  flex-shrink: 0;
  transition: background 120ms, border-color 120ms, color 120ms;
}

.filter-option--selected .filter-option__check {
  background: var(--color-accent);
  border-color: var(--color-accent);
  color: oklch(10% 0.01 258);
}

.filter-option__count {
  margin-left: auto;
  font-size: 0.8125rem;
  color: var(--color-text-muted);
}

.filter-panel__footer {
  display: flex;
  justify-content: space-between;
  padding: var(--space-3);
  border-top: 1px solid var(--color-border);
}
```

---

## Pattern C — Date Range Filter

```html
<div class="date-filter-panel">
  <div class="date-presets">
    <button class="date-preset" onclick="setDateRange('today')">Today</button>
    <button class="date-preset" onclick="setDateRange('7d')">Last 7 days</button>
    <button class="date-preset date-preset--active" onclick="setDateRange('30d')">Last 30 days</button>
    <button class="date-preset" onclick="setDateRange('90d')">Last 90 days</button>
    <button class="date-preset" onclick="setDateRange('custom')">Custom range</button>
  </div>
  <div class="date-custom" hidden id="custom-range">
    <label>From <input type="date" id="date-from" /></label>
    <label>To   <input type="date" id="date-to" /></label>
  </div>
</div>
```

---

## Search Debounce (JS)

```js
// Debounce search: wait 300ms after user stops typing before firing
let searchTimer
document.getElementById('table-search').addEventListener('input', e => {
  clearTimeout(searchTimer)
  searchTimer = setTimeout(() => {
    updateURLParam('q', e.target.value)
    reloadTableData()
  }, 300)
})
```

---

## URL State Management

```js
function updateURLParam(key, value) {
  const url = new URL(window.location)
  if (value) {
    url.searchParams.set(key, value)
  } else {
    url.searchParams.delete(key)
  }
  window.history.replaceState({}, '', url)
}

function clearAllFilters() {
  window.history.replaceState({}, '', window.location.pathname)
  reloadTableData()
}
```

---

## Anti-Patterns

- Filters that apply immediately on every change (should apply on click, or debounce search separately)
- Active filters not shown as visible chips (operators forget what's filtered)
- No "Clear all filters" when multiple filters are active
- Filter state lost on page navigation (use URL params)
- Search that fires on every keystroke without debounce (hammers the API)
- Filter dropdowns wider than the viewport on mobile

## Related Files

- `patterns/admin-ui/data-tables.md` — filter bar appears inside the table container
- `rules/12-admin-panels.md` — R4: Filter and search mandatory at scale
- `blueprints/admin-panel-from-scratch.md` — filter bar anatomy
