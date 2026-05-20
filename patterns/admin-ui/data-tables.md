# Pattern — Data Tables

> The data table is the primary UI component in admin panels and data-heavy SaaS apps. Every decision here — column order, row height, sort behavior, selection model — directly affects operator efficiency.

---

## Table Architecture Decision

Before building, decide:
```
Data volume:      [< 100 / < 1000 / 10,000+ rows]
Primary action:   [view / edit / delete / export / bulk-operate]
Key identifiers:  [what uniquely identifies a row to the user?]
Density:          [comfortable (48px) / standard (40px) / compact (32px)]
Selection model:  [single / multi / none]
Column visibility: [fixed / user-configurable]
```

---

## Full Table Anatomy

```html
<div class="table-container">
  <!-- Table toolbar: above the table -->
  <div class="table-toolbar">
    <div class="table-toolbar__left">
      <h2 class="table-title">Projects <span class="table-count">4,832</span></h2>
    </div>
    <div class="table-toolbar__right">
      <button class="btn-ghost btn-sm" onclick="exportData()">Export CSV</button>
      <a href="/projects/new" class="btn-primary btn-sm">New project</a>
    </div>
  </div>

  <!-- Filter bar: below title, above table -->
  <!-- See filters.md for full pattern -->
  <div class="table-filters">
    <!-- ... -->
  </div>

  <!-- Bulk action bar: appears when rows are selected -->
  <div class="bulk-bar" id="bulk-bar" hidden aria-live="polite">
    <span class="bulk-bar__count" id="selection-count">0 selected</span>
    <div class="bulk-bar__actions">
      <button class="btn-ghost btn-sm">Archive</button>
      <button class="btn-ghost btn-sm">Export</button>
      <button class="btn-destructive btn-sm" onclick="confirmBulkDelete()">Delete</button>
    </div>
    <button class="btn-ghost btn-sm bulk-bar__clear" onclick="clearSelection()">Deselect all</button>
  </div>

  <!-- Scroll wrapper -->
  <div class="table-scroll" tabindex="0" role="region" aria-label="Projects table, scrollable">
    <table class="data-table" aria-label="Projects">
      <thead>
        <tr>
          <!-- Select all checkbox -->
          <th scope="col" class="col-check">
            <input
              type="checkbox"
              id="select-all"
              aria-label="Select all projects"
              onclick="toggleSelectAll(this)"
            />
          </th>

          <!-- Sortable column -->
          <th scope="col" class="col-name">
            <button
              class="col-sort"
              aria-label="Sort by Name, ascending"
              data-sort="name"
              data-direction="asc"
            >
              Name
              <span class="sort-icon sort-icon--asc" aria-hidden="true"></span>
            </button>
          </th>

          <th scope="col" class="col-status">Status</th>

          <th scope="col" class="col-members">
            <button class="col-sort" aria-label="Sort by Members" data-sort="members">
              Members
              <span class="sort-icon" aria-hidden="true"></span>
            </button>
          </th>

          <th scope="col" class="col-updated">
            <button class="col-sort" aria-label="Sort by Updated date" data-sort="updated_at">
              Updated
              <span class="sort-icon" aria-hidden="true"></span>
            </button>
          </th>

          <!-- Actions column: no header text -->
          <th scope="col" class="col-actions">
            <span class="sr-only">Row actions</span>
          </th>
        </tr>
      </thead>

      <tbody>
        <!-- Standard row -->
        <tr class="data-row" data-id="proj-1">
          <td class="col-check">
            <input
              type="checkbox"
              aria-label="Select Alpha redesign"
              class="row-checkbox"
              onchange="handleRowSelect(this)"
            />
          </td>
          <td class="col-name">
            <a href="/projects/alpha" class="row-primary-link">Alpha redesign</a>
            <span class="row-sub">Created by Sarah Chen</span>
          </td>
          <td class="col-status">
            <span class="badge badge-active">Active</span>
          </td>
          <td class="col-members">
            <div class="avatar-stack">
              <img src="/a1.webp" alt="Sarah" title="Sarah Chen" width="24" height="24" />
              <img src="/a2.webp" alt="Marcus" title="Marcus Rivera" width="24" height="24" />
              <span class="avatar-count" title="3 more members">+3</span>
            </div>
          </td>
          <td class="col-updated">
            <time datetime="2026-05-18">2 days ago</time>
          </td>
          <td class="col-actions">
            <div class="row-actions">
              <a href="/projects/alpha/edit" class="row-action" aria-label="Edit Alpha redesign">
                <!-- Edit icon -->
              </a>
              <button
                class="row-action row-action--danger"
                aria-label="Delete Alpha redesign"
                onclick="confirmDelete('proj-1', 'Alpha redesign')"
              >
                <!-- Delete icon -->
              </button>
            </div>
          </td>
        </tr>

        <!-- Error row state -->
        <tr class="data-row data-row--error" data-id="proj-err">
          <td colspan="6" class="row-error-cell">
            <span class="row-error-icon" aria-hidden="true">⚠</span>
            Failed to load this row. <button class="link-btn" onclick="retryRow('proj-err')">Retry</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- Pagination -->
  <div class="table-pagination" aria-label="Pagination">
    <span class="pagination-info">Showing 201–225 of 4,832 results</span>
    <div class="pagination-controls">
      <select
        class="pagination-size"
        aria-label="Rows per page"
        onchange="setPageSize(this.value)"
      >
        <option value="25" selected>25 per page</option>
        <option value="50">50 per page</option>
        <option value="100">100 per page</option>
      </select>
      <nav aria-label="Page navigation">
        <button class="page-btn" aria-label="Previous page" onclick="prevPage()">‹</button>
        <button class="page-btn" aria-label="Page 1" onclick="goToPage(1)">1</button>
        <button class="page-btn page-btn--active" aria-current="page" aria-label="Page 9, current">9</button>
        <button class="page-btn" aria-label="Page 10" onclick="goToPage(10)">10</button>
        <span class="page-ellipsis" aria-hidden="true">…</span>
        <button class="page-btn" aria-label="Page 194" onclick="goToPage(194)">194</button>
        <button class="page-btn" aria-label="Next page" onclick="nextPage()">›</button>
      </nav>
    </div>
  </div>
</div>
```

```css
/* Table container */
.table-container {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  overflow: hidden;
}

/* Toolbar */
.table-toolbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: var(--space-5) var(--space-6);
  border-bottom: 1px solid var(--color-border);
  gap: var(--space-4);
}

.table-title {
  font-size: 1rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: var(--space-2);
}

.table-count {
  font-size: 0.8125rem;
  color: var(--color-text-muted);
  background: var(--color-surface-2);
  padding: 0.1em 0.5em;
  border-radius: 9999px;
  font-weight: 400;
}

.table-toolbar__right { display: flex; gap: var(--space-2); }

/* Bulk action bar */
.bulk-bar {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  padding: var(--space-3) var(--space-6);
  background: oklch(from var(--color-accent) l c h / 0.08);
  border-bottom: 1px solid var(--color-border);
  flex-wrap: wrap;
}

.bulk-bar[hidden] { display: none; }

.bulk-bar__count {
  font-weight: 500;
  font-size: 0.9375rem;
  margin-right: var(--space-2);
}

.bulk-bar__clear { margin-left: auto; }

/* Scroll wrapper */
.table-scroll {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}

/* Table */
.data-table {
  width: 100%;
  border-collapse: collapse;
  min-width: 600px;
}

.data-table th {
  text-align: left;
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--color-text-muted);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  padding: var(--space-3) var(--space-4);
  border-bottom: 1px solid var(--color-border);
  white-space: nowrap;
  background: var(--color-surface);
  position: sticky;
  top: 0;
}

.data-table td {
  padding: var(--space-3) var(--space-4);
  border-bottom: 1px solid var(--color-border);
  font-size: 0.9375rem;
  vertical-align: middle;
}

/* Row states */
.data-row { transition: background 120ms; }
.data-row:hover { background: var(--color-surface-2); }
.data-row:hover .row-actions { opacity: 1; }
.data-row.selected { background: oklch(from var(--color-accent) l c h / 0.06); }
.data-row--error { background: oklch(from var(--color-error) l c h / 0.04); }
.data-row:last-child td { border-bottom: none; }

/* Column types */
.col-check { width: 40px; padding-inline: var(--space-4) var(--space-2); }
.col-name  { min-width: 200px; }
.col-status { width: 100px; }
.col-actions { width: 80px; text-align: right; }

/* Primary link */
.row-primary-link {
  font-weight: 500;
  color: var(--color-text-primary);
  text-decoration: none;
}

.row-primary-link:hover {
  color: var(--color-accent);
  text-decoration: underline;
  text-underline-offset: 2px;
}

.row-sub {
  display: block;
  font-size: 0.8125rem;
  color: var(--color-text-muted);
  margin-top: 2px;
}

/* Sort button */
.col-sort {
  background: transparent;
  border: none;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  font-size: inherit;
  font-weight: inherit;
  color: inherit;
  letter-spacing: inherit;
  text-transform: inherit;
  padding: 0;
  font-family: inherit;
}

.sort-icon {
  width: 10px;
  height: 10px;
  opacity: 0.3;
  border-left: 1.5px solid currentColor;
  border-bottom: 1.5px solid currentColor;
  transform: rotate(-45deg);
}

.sort-icon--asc { opacity: 1; transform: rotate(-45deg); }
.sort-icon--desc { opacity: 1; transform: rotate(135deg); }

/* Row actions */
.row-actions {
  display: flex;
  gap: var(--space-1);
  justify-content: flex-end;
  opacity: 0;
  transition: opacity 120ms;
}

.row-action {
  width: 32px;
  height: 32px;
  display: grid;
  place-items: center;
  border-radius: var(--radius-md);
  color: var(--color-text-muted);
  background: transparent;
  border: none;
  cursor: pointer;
  text-decoration: none;
  transition: background 120ms, color 120ms;
}

.row-action:hover {
  background: var(--color-surface-2);
  color: var(--color-text-primary);
}

.row-action--danger:hover {
  background: oklch(from var(--color-error) l c h / 0.1);
  color: var(--color-error);
}

/* Avatar stack */
.avatar-stack {
  display: flex;
  align-items: center;
}

.avatar-stack img {
  border-radius: 50%;
  border: 2px solid var(--color-surface);
  margin-left: -8px;
  object-fit: cover;
}

.avatar-stack img:first-child { margin-left: 0; }

.avatar-count {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: var(--color-surface-2);
  border: 2px solid var(--color-surface);
  margin-left: -8px;
  display: grid;
  place-items: center;
  font-size: 0.625rem;
  font-weight: 600;
  color: var(--color-text-muted);
}

/* Pagination */
.table-pagination {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: var(--space-4) var(--space-6);
  border-top: 1px solid var(--color-border);
  gap: var(--space-4);
  flex-wrap: wrap;
}

.pagination-info {
  font-size: 0.875rem;
  color: var(--color-text-muted);
}

.pagination-controls {
  display: flex;
  align-items: center;
  gap: var(--space-3);
}

.pagination-size {
  font-size: 0.875rem;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  padding: var(--space-1) var(--space-2);
  color: var(--color-text-primary);
}

.page-btn {
  min-width: 32px;
  height: 32px;
  border-radius: var(--radius-md);
  background: transparent;
  border: 1px solid transparent;
  cursor: pointer;
  font-size: 0.875rem;
  color: var(--color-text-secondary);
  display: grid;
  place-items: center;
  transition: background 120ms, border-color 120ms;
}

.page-btn:hover {
  background: var(--color-surface-2);
  border-color: var(--color-border);
}

.page-btn--active {
  background: var(--color-accent);
  color: oklch(10% 0.01 258);
  border-color: var(--color-accent);
  font-weight: 600;
}

.page-ellipsis {
  color: var(--color-text-muted);
  font-size: 0.875rem;
}
```

---

## Empty Table State

```html
<tbody>
  <tr>
    <td colspan="6" class="table-empty">
      <div class="empty-state-compact">
        <p>No projects found.</p>
        <a href="/projects/new" class="btn-primary btn-sm">Create your first project</a>
      </div>
    </td>
  </tr>
</tbody>
```

```css
.table-empty { padding: var(--space-16); text-align: center; }
```

---

## Loading Table State

```html
<!-- Skeleton rows: same structure as real rows, aria-busy on table -->
<table class="data-table" aria-busy="true" aria-label="Loading projects">
  <tbody>
    <tr class="data-row" aria-hidden="true">
      <td class="col-check"><div class="skeleton skeleton--circle" style="width:16px;height:16px;"></div></td>
      <td><div class="skeleton skeleton--text" style="width:65%;"></div></td>
      <td><div class="skeleton skeleton--text" style="width:50%;"></div></td>
      <td><div class="skeleton skeleton--text" style="width:40%;"></div></td>
      <td><div class="skeleton skeleton--text" style="width:55%;"></div></td>
      <td></td>
    </tr>
    <!-- Repeat 8 rows -->
  </tbody>
</table>
```

---

## TanStack Table v8 (React)

```tsx
import { useReactTable, getCoreRowModel, getSortedRowModel, flexRender } from '@tanstack/react-table'

const table = useReactTable({
  data,
  columns,
  getCoreRowModel: getCoreRowModel(),
  getSortedRowModel: getSortedRowModel(),
  state: { sorting, rowSelection },
  onSortingChange: setSorting,
  onRowSelectionChange: setRowSelection,
  enableRowSelection: true,
})
```

---

## Anti-Patterns

- Infinite scroll in admin tables (operators need to navigate to specific page numbers)
- Row actions always visible (clutters the table — show on hover desktop, always on mobile)
- Sorting without visual indicator (user doesn't know current sort state)
- Bulk operations without count in the confirmation ("Delete items?" → "Delete 24 items?")
- No sticky header when table is scrollable (column context lost)
- Showing all rows without pagination for > 50 rows (performance and usability)

## Related Files

- `patterns/admin-ui/filters.md` — filter bar that sits above the table
- `rules/12-admin-panels.md` — R3: Table as primary component
- `blueprints/admin-panel-from-scratch.md` — Core screen 1: Data table
- `references/data-viz.md` — charts and KPI cards for data dashboards
