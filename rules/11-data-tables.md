# Rule — Data Tables

> Tables are not grids. They communicate relationships between structured data across two axes. A table without clear column hierarchy, consistent alignment, and appropriate density is a spreadsheet with styling — not a UI component. These rules separate readable data from visual noise.

---

## R1 — Numeric columns right-aligned. Text columns left-aligned. Booleans centered.

Alignment is not aesthetic — it's how data is compared. Right-aligned numbers let the eye scan down the decimal points. Left-aligned text follows the natural reading start. Centered checkboxes sit in their column without creating ragged edges.

```css
/* Column alignment by data type */
.col-text    { text-align: left; }
.col-numeric { text-align: right; font-variant-numeric: tabular-nums; }
.col-boolean { text-align: center; }
.col-status  { text-align: left; }    /* status badges are text-adjacent */
.col-actions { text-align: right; }   /* actions align with right edge */

/* font-variant-numeric: tabular-nums — monospace number widths */
/* ensures 1,234 and 9,876 take the same horizontal space for alignment */
.col-numeric, .col-date {
  font-variant-numeric: tabular-nums;
  font-family: var(--font-mono);      /* or tabular-nums alone if body font supports it */
}
```

```html
<!-- Column header alignment matches data alignment -->
<thead>
  <tr>
    <th scope="col" class="col-text">Name</th>
    <th scope="col" class="col-text">Status</th>
    <th scope="col" class="col-numeric" aria-sort="descending">Amount</th>
    <th scope="col" class="col-text">Date</th>
    <th scope="col" class="col-actions">
      <span class="sr-only">Actions</span>
    </th>
  </tr>
</thead>
```

---

## R2 — Row height defines density mode. Two modes: comfortable (48px) and compact (36px).

There is no universal correct row height. Comfortable density works for records users read and act on (CRM, order management). Compact density works for monitoring dashboards and log viewers where volume matters.

```css
/* ── Comfortable (default) — 48px rows ── */
.table--comfortable tbody td {
  padding-block: var(--space-3);   /* ~12px, giving ~48px total with line-height */
  padding-inline: var(--space-4);
}

/* ── Compact — 36px rows ── */
.table--compact tbody td {
  padding-block: var(--space-2);   /* ~8px */
  padding-inline: var(--space-3);
  font-size: var(--text-sm);
}

/* ── Header row is always 40px regardless of mode ── */
.table thead th {
  height: 40px;
  padding-inline: var(--space-4);
  font-size: var(--text-xs);
  font-weight: var(--font-weight-medium);
  color: var(--color-text-muted);
  text-transform: uppercase;
  letter-spacing: var(--tracking-wider);
  border-bottom: 1px solid var(--color-border);
  white-space: nowrap;
}
```

---

## R3 — Sortable columns: visual indicator on current sort, clickable header, ARIA sort attribute.

Users expect to sort by clicking a column header. The current sort state must be visually indicated on the column header — not just via ARIA.

```html
<th
  scope="col"
  class="col-numeric col-sortable col-sorted-desc"
  aria-sort="descending"
  tabindex="0"
  role="columnheader"
>
  Amount
  <span class="sort-indicator" aria-hidden="true">↓</span>
</th>
```

```css
.col-sortable {
  cursor: pointer;
  user-select: none;
  position: relative;
}

.col-sortable:hover {
  color: var(--color-text-primary);
  background: var(--color-surface-2);
}

.col-sortable:focus-visible {
  outline: var(--focus-ring);
  outline-offset: -2px;
}

.sort-indicator {
  opacity: 0;
  margin-inline-start: var(--space-2);
  transition: opacity var(--duration-fast) var(--ease-smooth);
  display: inline-block;
  width: 12px;
}

.col-sortable:hover .sort-indicator { opacity: 0.4; }
.col-sorted-asc  .sort-indicator,
.col-sorted-desc .sort-indicator    { opacity: 1; }

.col-sorted-asc  .sort-indicator::before { content: '↑'; }
.col-sorted-desc .sort-indicator::before { content: '↓'; }
```

```js
// Keyboard sort — Enter or Space on sortable header
document.querySelectorAll('.col-sortable').forEach(th => {
  th.addEventListener('keydown', e => {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault()
      th.click()
    }
  })
})
```

**`aria-sort` values:** `ascending`, `descending`, `none`, `other`.
The unsorted state uses `aria-sort="none"`. Only the active column has `ascending` or `descending`.

---

## R4 — Row selection: checkbox column, select-all in header, clear visual state for selected rows.

```html
<table class="data-table" aria-multiselectable="true">
  <thead>
    <tr>
      <th scope="col" class="col-select">
        <label class="sr-only" for="select-all">Select all rows</label>
        <input
          type="checkbox"
          id="select-all"
          aria-label="Select all rows"
          class="checkbox-native"
        />
        <span class="checkbox-custom" aria-hidden="true"></span>
      </th>
      <th scope="col">Name</th>
      <!-- ... -->
    </tr>
  </thead>
  <tbody>
    <tr aria-selected="false">
      <td class="col-select">
        <input type="checkbox" aria-label="Select Acme Corp row" class="checkbox-native" />
        <span class="checkbox-custom" aria-hidden="true"></span>
      </td>
      <td>Acme Corp</td>
    </tr>
  </tbody>
</table>
```

```css
/* Selected row — background tint, not border */
tr[aria-selected="true"] td {
  background: oklch(from var(--color-accent) l c h / 0.06);
}

/* Bulk action bar: appears when 1+ rows selected */
.bulk-actions {
  display: none;
  position: sticky;
  bottom: 0;
  background: var(--color-surface);
  border-top: 1px solid var(--color-border);
  padding: var(--space-3) var(--space-4);
  align-items: center;
  gap: var(--space-3);
}

.bulk-actions.visible { display: flex; }
```

---

## R5 — Empty state for zero-result tables. Skeleton for loading tables.

A blank table body with no explanation looks like a bug.

```html
<!-- Empty state: no data at all -->
<tbody>
  <tr>
    <td colspan="5" class="table-empty">
      <div class="empty-state">
        <p class="empty-state__title">No deployments yet</p>
        <p class="empty-state__desc">Deployments appear here when you push to a branch with CI enabled.</p>
        <a href="/docs/setup" class="btn-ghost btn--sm">Set up CI pipeline</a>
      </div>
    </td>
  </tr>
</tbody>

<!-- Empty search: filtered to zero results -->
<tbody>
  <tr>
    <td colspan="5" class="table-empty">
      <p>No results for "<strong>{{ query }}</strong>"</p>
      <button type="button" class="link">Clear filters</button>
    </td>
  </tr>
</tbody>
```

```css
/* ── Loading skeleton rows ── */
.table-skeleton tbody tr td {
  padding-block: var(--space-3);
}

.skeleton-cell {
  height: 14px;
  border-radius: var(--radius-sm);
  background: var(--color-surface-2);
  position: relative;
  overflow: hidden;
}

/* Shimmer sweeps across the whole skeleton container */
.table-skeleton tbody::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg, transparent 0%, oklch(100% 0 0 / 0.06) 50%, transparent 100%);
  background-size: 200% 100%;
  animation: shimmer 1.8s linear infinite;
  pointer-events: none;
}

@keyframes shimmer {
  from { background-position: 200% 0; }
  to   { background-position: -200% 0; }
}

@media (prefers-reduced-motion: reduce) {
  .table-skeleton tbody::after { animation: none; }
}
```

---

## R6 — Sticky header for tables taller than the viewport.

When a table scrolls vertically, the header must stay visible. Without it, users lose column context.

```css
.table-container {
  overflow-y: auto;
  max-height: 600px;    /* or calc(100dvh - header-height) */
  position: relative;
}

.data-table thead th {
  position: sticky;
  top: 0;
  z-index: var(--z-sticky);
  background: var(--color-base);
  /* Border-bottom disappears under sticky — use box-shadow instead */
  box-shadow: 0 1px 0 var(--color-border);
}
```

---

## R7 — Row actions: use icon buttons in an actions column. Reveal on hover/focus.

Action buttons for every row (Edit, Delete, View) should be visually quiet until the row is active. Showing them at full opacity on every row creates visual noise.

```html
<td class="col-actions">
  <div class="row-actions">
    <button type="button" class="icon-btn" aria-label="Edit Acme Corp">
      <svg aria-hidden="true" ...><!-- edit icon --></svg>
    </button>
    <button type="button" class="icon-btn" aria-label="Delete Acme Corp">
      <svg aria-hidden="true" ...><!-- trash icon --></svg>
    </button>
  </div>
</td>
```

```css
.row-actions {
  display: flex;
  justify-content: flex-end;
  gap: var(--space-1);
  opacity: 0;
  transition: opacity var(--duration-fast) var(--ease-smooth);
}

/* Show on row hover OR when any action is focused */
tr:hover .row-actions,
tr:focus-within .row-actions {
  opacity: 1;
}

.icon-btn {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: var(--radius-md);
  border: none;
  background: transparent;
  color: var(--color-text-muted);
  cursor: pointer;
  transition: background var(--duration-fast) var(--ease-smooth),
              color    var(--duration-fast) var(--ease-smooth);
}

.icon-btn:hover { background: var(--color-surface-2); color: var(--color-text-primary); }
```

---

## R8 — Pagination vs. infinite scroll: choose based on task type.

```
Pagination:      User navigates to a specific page, needs to return to same position,
                 compares records across pages, exports or shares a filtered view.
                 Use for: admin tables, order lists, user management.

Infinite scroll: User browses continuously, position doesn't need to be bookmarked,
                 content is feed-like.
                 Use for: activity feeds, image galleries, content discovery.

Load more:       Compromise — shows first N rows, button reveals more.
                 Preserves position (unlike infinite scroll) without forced pagination.
                 Use for: tables where most users find what they need in first page.
```

```html
<!-- Pagination: accessible, keyboard-navigable -->
<nav aria-label="Table pagination" class="pagination">
  <button class="pagination__btn" aria-label="Previous page" disabled>←</button>

  <span class="pagination__info" aria-live="polite" aria-atomic="true">
    Page 3 of 24 — 235 results
  </span>

  <button class="pagination__btn" aria-label="Next page">→</button>

  <!-- Optional: page size selector -->
  <label class="pagination__size">
    Rows per page:
    <select aria-label="Rows per page">
      <option value="25">25</option>
      <option value="50" selected>50</option>
      <option value="100">100</option>
    </select>
  </label>
</nav>
```

---

## R9 — Frozen first column for wide tables that scroll horizontally.

Wide tables with many columns must scroll horizontally. Without a frozen first column, users lose track of which row they're on.

```css
.table-container {
  overflow-x: auto;
}

/* Freeze first column */
.data-table th:first-child,
.data-table td:first-child {
  position: sticky;
  left: 0;
  z-index: 1;
  background: var(--color-base);
}

/* Shadow to indicate frozen column */
.data-table th:first-child::after,
.data-table td:first-child::after {
  content: '';
  position: absolute;
  top: 0;
  right: -12px;
  bottom: 0;
  width: 12px;
  background: linear-gradient(to right, oklch(0% 0 0 / 0.06), transparent);
  pointer-events: none;
}
```

---

## R10 — Responsive tables: priority columns on mobile, full table on desktop.

A 12-column table cannot fit on 390px. Decide which columns are essential and hide the rest at small viewports.

```css
/* Hide lower-priority columns on mobile */
@media (max-width: 767px) {
  .col-secondary  { display: none; }
  .col-optional   { display: none; }

  /* Compact on mobile: 2 critical columns */
  .data-table td,
  .data-table th {
    padding-inline: var(--space-3);
  }
}

/* Alternative: stack key-value on mobile */
@media (max-width: 480px) {
  .data-table thead { display: none; }  /* hide headers */

  .data-table tr {
    display: block;
    border: 1px solid var(--color-border);
    border-radius: var(--radius-md);
    margin-bottom: var(--space-3);
    padding: var(--space-4);
  }

  .data-table td {
    display: flex;
    justify-content: space-between;
    border: none;
    padding: var(--space-1) 0;
  }

  .data-table td::before {
    content: attr(data-label);
    font-weight: var(--font-weight-medium);
    color: var(--color-text-muted);
  }
}
```

---

## Data Table Acceptance Criteria

```
[ ] Numeric columns right-aligned with tabular-nums
[ ] Text columns left-aligned
[ ] Density mode appropriate for content type (comfortable vs. compact)
[ ] Sortable columns: aria-sort, keyboard activation, visible sort direction
[ ] Row selection: checkboxes + aria-selected + bulk action bar
[ ] Empty state: explains why and what to do
[ ] Loading: skeleton rows with shimmer (not multiple pulse)
[ ] Header sticky when table exceeds viewport height
[ ] Row actions: icon buttons, visible on hover/focus-within
[ ] Pagination or load-more: page state announced via aria-live
[ ] Horizontal scroll: first column frozen with shadow
[ ] Mobile: non-essential columns hidden or table reflows to card layout
[ ] All interactive elements keyboard accessible
```

---

*Rule version: global-design-skill v1.0 — `rules/11-data-tables.md`*
*Related: `rules/07-accessibility.md`, `rules/09-responsive.md`, `patterns/product-ui/data-tables.md`, `checklists/ui-review.md` §3*
