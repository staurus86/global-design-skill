# Pattern — Pagination

> Pagination divides a large dataset across multiple pages. Use it when the total count is meaningful, users need to reference specific page numbers, or when infinite scroll would harm orientation.

---

## Pagination vs Infinite Scroll Decision

```
Use pagination when:                     Use infinite scroll when:
  User needs to find item on page N       Content is feed-like (social, news)
  Total count is meaningful info          Users rarely need to go back
  Items need to be compared across pages  Mobile-first, thumb-scroll experience
  SEO requires distinct page URLs         Page position is not a user concern
  Admin tables, data grids                Content is homogeneous, endless
```

Never use infinite scroll for: search results, data tables, e-commerce with filters, account management pages.

---

## Pattern 1 — Standard Pagination

```html
<nav class="pagination" aria-label="Results pagination">
  <!-- Previous -->
  <a href="?page=2" class="pagination__btn" rel="prev" aria-label="Previous page">
    <svg width="16" height="16" viewBox="0 0 16 16" fill="none"
      stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <path d="M10 3L5 8l5 5"/>
    </svg>
  </a>

  <!-- Pages -->
  <ol class="pagination__pages" role="list">
    <li>
      <a href="?page=1" class="pagination__page" aria-label="Page 1">1</a>
    </li>
    <li>
      <a href="?page=2" class="pagination__page" aria-label="Page 2">2</a>
    </li>
    <li>
      <a href="?page=3" class="pagination__page pagination__page--current"
        aria-current="page" aria-label="Page 3, current">3</a>
    </li>
    <li aria-hidden="true">
      <span class="pagination__ellipsis">···</span>
    </li>
    <li>
      <a href="?page=8" class="pagination__page" aria-label="Page 8">8</a>
    </li>
    <li>
      <a href="?page=9" class="pagination__page" aria-label="Page 9">9</a>
    </li>
    <li>
      <a href="?page=10" class="pagination__page" aria-label="Page 10">10</a>
    </li>
  </ol>

  <!-- Next -->
  <a href="?page=4" class="pagination__btn" rel="next" aria-label="Next page">
    <svg width="16" height="16" viewBox="0 0 16 16" fill="none"
      stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <path d="M6 3l5 5-5 5"/>
    </svg>
  </a>
</nav>
```

```css
.pagination {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  justify-content: center;
  padding: var(--space-6) 0;
}

.pagination__pages {
  display: flex;
  align-items: center;
  gap: var(--space-1);
  list-style: none;
  margin: 0; padding: 0;
}

.pagination__btn,
.pagination__page {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 36px;
  height: 36px;
  padding: 0 var(--space-2);
  border-radius: var(--radius-md);
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-text-secondary);
  text-decoration: none;
  border: 1px solid transparent;
  transition:
    background    var(--duration-fast) var(--ease-smooth),
    color         var(--duration-fast) var(--ease-smooth),
    border-color  var(--duration-fast) var(--ease-smooth);
}

.pagination__btn:hover,
.pagination__page:hover {
  background: var(--color-surface-2);
  color: var(--color-text-primary);
}

.pagination__page--current {
  background: var(--color-accent);
  color: var(--color-text-inverse);
  border-color: var(--color-accent);
  pointer-events: none;
}

.pagination__page--current:hover {
  background: var(--color-accent);
  color: var(--color-text-inverse);
}

.pagination__btn[aria-disabled="true"] {
  color: var(--color-text-disabled);
  pointer-events: none;
  cursor: not-allowed;
}

.pagination__ellipsis {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 36px;
  height: 36px;
  color: var(--color-text-muted);
  font-size: var(--text-sm);
  letter-spacing: 0.05em;
}

.pagination__btn:focus-visible,
.pagination__page:focus-visible {
  outline: 2px solid var(--color-border-focus);
  outline-offset: 2px;
}
```

---

## Pattern 2 — Compact Pagination (Mobile / Dense Tables)

When space is limited — show only previous, current/total indicator, and next.

```html
<nav class="pagination-compact" aria-label="Results pagination">
  <a href="?page=2" class="pagination__btn pagination__btn--prev" rel="prev"
    aria-label="Previous page">
    <svg width="16" height="16" viewBox="0 0 16 16" fill="none"
      stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <path d="M10 3L5 8l5 5"/>
    </svg>
    Previous
  </a>

  <span class="pagination-compact__indicator" aria-live="polite">
    Page <strong>3</strong> of 10
  </span>

  <a href="?page=4" class="pagination__btn pagination__btn--next" rel="next"
    aria-label="Next page">
    Next
    <svg width="16" height="16" viewBox="0 0 16 16" fill="none"
      stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <path d="M6 3l5 5-5 5"/>
    </svg>
  </a>
</nav>
```

```css
.pagination-compact {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-4);
  padding: var(--space-4) 0;
}

.pagination__btn--prev,
.pagination__btn--next {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  padding: var(--space-2) var(--space-3);
  border-radius: var(--radius-md);
  border: 1px solid var(--color-border);
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-text-secondary);
  text-decoration: none;
  transition:
    background   var(--duration-fast) var(--ease-smooth),
    color        var(--duration-fast) var(--ease-smooth);
}

.pagination__btn--prev:hover,
.pagination__btn--next:hover {
  background: var(--color-surface-2);
  color: var(--color-text-primary);
}

.pagination-compact__indicator {
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
}
```

---

## Pattern 3 — Rows-Per-Page Control + Pagination

For data tables where users need to control how many rows appear.

```html
<div class="table-footer">
  <div class="table-footer__rows">
    <label class="table-footer__label" for="rows-per-page">Rows per page:</label>
    <select class="table-footer__select" id="rows-per-page" aria-label="Rows per page">
      <option value="10" selected>10</option>
      <option value="25">25</option>
      <option value="50">50</option>
      <option value="100">100</option>
    </select>
  </div>

  <span class="table-footer__count" aria-live="polite">
    21–30 of 847 results
  </span>

  <nav class="pagination-compact" aria-label="Table pagination">
    <button class="pagination__btn" aria-label="First page" title="First page" aria-disabled="false">
      <svg width="16" height="16" viewBox="0 0 16 16" fill="none"
        stroke="currentColor" stroke-width="1.5" stroke-linecap="round">
        <path d="M3 3v10M7 8l5-5m-5 5l5 5"/>
      </svg>
    </button>
    <button class="pagination__btn" aria-label="Previous page" rel="prev">
      <svg width="16" height="16" viewBox="0 0 16 16" fill="none"
        stroke="currentColor" stroke-width="1.5" stroke-linecap="round">
        <path d="M10 3L5 8l5 5"/>
      </svg>
    </button>
    <span class="pagination-compact__indicator" aria-live="polite">
      3 / 85
    </span>
    <button class="pagination__btn" aria-label="Next page" rel="next">
      <svg width="16" height="16" viewBox="0 0 16 16" fill="none"
        stroke="currentColor" stroke-width="1.5" stroke-linecap="round">
        <path d="M6 3l5 5-5 5"/>
      </svg>
    </button>
    <button class="pagination__btn" aria-label="Last page" title="Last page">
      <svg width="16" height="16" viewBox="0 0 16 16" fill="none"
        stroke="currentColor" stroke-width="1.5" stroke-linecap="round">
        <path d="M9 8L4 3m5 5L4 13m9-10v10"/>
      </svg>
    </button>
  </nav>
</div>
```

```css
.table-footer {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: var(--space-6);
  padding: var(--space-3) var(--space-4);
  border-top: 1px solid var(--color-border);
  font-size: var(--text-sm);
}

.table-footer__rows {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  color: var(--color-text-secondary);
}

.table-footer__select {
  padding: var(--space-1) var(--space-2);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-sm);
  background: var(--color-surface);
  color: var(--color-text-primary);
  font-size: var(--text-sm);
  cursor: pointer;
}

.table-footer__count {
  color: var(--color-text-secondary);
  white-space: nowrap;
}

@media (max-width: 640px) {
  .table-footer {
    flex-wrap: wrap;
    justify-content: center;
    gap: var(--space-3);
  }
  .table-footer__rows { display: none; }
}
```

---

## Ellipsis Logic

Show at most 7 page numbers + 2 ellipsis indicators. Algorithm:

```js
function getPages(current, total) {
  if (total <= 7) return Array.from({ length: total }, (_, i) => i + 1)

  const delta = 2
  const left  = current - delta
  const right = current + delta

  const pages = new Set([1, total])
  for (let i = Math.max(2, left); i <= Math.min(total - 1, right); i++) pages.add(i)

  return [...pages].sort((a, b) => a - b).reduce((acc, page, i, arr) => {
    if (i > 0 && arr[i - 1] < page - 1) acc.push('...')
    acc.push(page)
    return acc
  }, [])
}

// getPages(3, 10) → [1, 2, 3, 4, 5, '...', 10]
// getPages(6, 10) → [1, '...', 4, 5, 6, 7, 8, '...', 10]
// getPages(9, 10) → [1, '...', 7, 8, 9, 10]
```

---

## SEO: `rel="prev"` / `rel="next"`

Add to `<head>` or directly on links for paginated content:

```html
<head>
  <link rel="prev" href="https://example.com/articles?page=2" />
  <link rel="next" href="https://example.com/articles?page=4" />
</head>
```

For the first page: only `rel="next"`. For the last page: only `rel="prev"`.

---

## Anti-Patterns

```
× Pagination on a list with fewer than 20 items — no need
× Not preserving URL state — breaks browser back and sharing
× Pagination without total count visible — user can't orient
× Infinite scroll on search results — harms recall and position orientation
× "Load more" replacing pagination on data tables — makes row count unclear
× No keyboard support on custom button-based pagination
× Previous/Next without current page indicator
```

---

*Pattern version: global-design-skill v1.0 — `patterns/navigation/pagination.md`*  
*Related: `rules/11-data-tables.md`, `patterns/navigation/breadcrumbs.md`, `patterns/navigation/tabs-patterns.md`*
