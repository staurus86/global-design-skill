# Pattern — Bulk Actions

> Bulk actions let users operate on multiple selected rows simultaneously. They appear only when a selection exists and disappear when the selection is cleared. Never show bulk action controls when nothing is selected.

---

## Interaction Model

```
1. User checks a row checkbox         → Selection counter appears
2. User checks more rows             → Counter updates
3. User opens action menu / toolbar  → Bulk actions revealed
4. User confirms a destructive action → Confirmation required
5. Action completes                  → Selection cleared, rows update
6. User unchecks all / clicks X     → Selection counter disappears
```

---

## Pattern 1 — Inline Toolbar (Recommended)

A toolbar that slides in above the table when rows are selected. Replaces or overlays the table header.

```html
<!-- Table section with bulk toolbar -->
<section class="data-table-section">

  <!-- Bulk action bar — hidden until rows selected -->
  <div
    class="bulk-bar"
    id="bulk-bar"
    role="toolbar"
    aria-label="Bulk actions"
    aria-live="polite"
    hidden
  >
    <div class="bulk-bar__left">
      <button class="bulk-bar__deselect" type="button" aria-label="Clear selection">
        <svg aria-hidden="true" width="14" height="14" viewBox="0 0 16 16" fill="none"
          stroke="currentColor" stroke-width="1.5" stroke-linecap="round">
          <path d="M4 4l8 8M12 4l-8 8"/>
        </svg>
      </button>
      <span class="bulk-bar__count" id="bulk-count">3 selected</span>
    </div>

    <div class="bulk-bar__actions">
      <button class="btn btn--ghost btn--sm" type="button" data-bulk-action="archive">
        Archive
      </button>
      <button class="btn btn--ghost btn--sm" type="button" data-bulk-action="export">
        Export
      </button>
      <button class="btn btn--ghost btn--sm btn--danger" type="button" data-bulk-action="delete">
        Delete
      </button>
    </div>
  </div>

  <!-- Table -->
  <div class="table-wrapper" role="region" aria-label="Projects" tabindex="0">
    <table class="data-table" aria-label="Projects list" aria-multiselectable="true">
      <thead>
        <tr>
          <th class="table-th table-th--check" scope="col">
            <input
              type="checkbox"
              class="checkbox"
              id="select-all"
              aria-label="Select all rows"
              aria-controls="table-body"
            />
          </th>
          <th class="table-th" scope="col">Name</th>
          <th class="table-th" scope="col">Status</th>
          <th class="table-th" scope="col">Updated</th>
          <th class="table-th table-th--action" scope="col">
            <span class="sr-only">Actions</span>
          </th>
        </tr>
      </thead>
      <tbody id="table-body">
        <tr class="table-row" aria-selected="false">
          <td class="table-td table-td--check">
            <input type="checkbox" class="checkbox row-checkbox" aria-label="Select Alpha" />
          </td>
          <td class="table-td table-td--primary">Alpha</td>
          <td class="table-td"><span class="badge badge--success">Active</span></td>
          <td class="table-td">2 hours ago</td>
          <td class="table-td table-td--action">
            <button class="icon-btn" type="button" aria-label="More options for Alpha"
              aria-haspopup="true">
              <svg aria-hidden="true" width="16" height="16" viewBox="0 0 16 16" fill="none"
                stroke="currentColor" stroke-width="1.5">
                <circle cx="8" cy="4" r="1" fill="currentColor" stroke="none"/>
                <circle cx="8" cy="8" r="1" fill="currentColor" stroke="none"/>
                <circle cx="8" cy="12" r="1" fill="currentColor" stroke="none"/>
              </svg>
            </button>
          </td>
        </tr>
        <!-- more rows -->
      </tbody>
    </table>
  </div>

</section>
```

```css
.bulk-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: var(--space-3) var(--space-4);
  background: var(--color-accent-subtle);
  border: 1px solid oklch(from var(--color-accent) l c h / 0.2);
  border-radius: var(--radius-lg);
  margin-bottom: var(--space-3);

  /* Animate in */
  @starting-style { opacity: 0; transform: translateY(-4px); }
  opacity: 1;
  transform: translateY(0);
  transition:
    opacity   var(--duration-fast) var(--ease-spring),
    transform var(--duration-fast) var(--ease-spring);
}

.bulk-bar[hidden] { display: none; }

.bulk-bar__left {
  display: flex;
  align-items: center;
  gap: var(--space-3);
}

.bulk-bar__deselect {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 24px; height: 24px;
  border-radius: var(--radius-sm);
  background: transparent;
  border: none;
  color: var(--color-accent-text);
  cursor: pointer;
  transition: background var(--duration-fast) var(--ease-smooth);
}

.bulk-bar__deselect:hover {
  background: oklch(from var(--color-accent) l c h / 0.12);
}

.bulk-bar__count {
  font-size: var(--text-sm);
  font-weight: var(--font-weight-semibold);
  color: var(--color-accent-text);
}

.bulk-bar__actions {
  display: flex;
  align-items: center;
  gap: var(--space-2);
}

/* Row selected state */
.table-row[aria-selected="true"] {
  background: oklch(from var(--color-accent) l c h / 0.05);
}

/* Indeterminate state on select-all */
#select-all:indeterminate { opacity: 0.6; }

@media (max-width: 640px) {
  .bulk-bar { flex-direction: column; align-items: flex-start; gap: var(--space-3); }
  .bulk-bar__actions { flex-wrap: wrap; }
}

@media (prefers-reduced-motion: reduce) {
  .bulk-bar { transition: none; }
}
```

```js
class BulkSelection {
  constructor (section) {
    this.section    = section
    this.selectAll  = section.querySelector('#select-all')
    this.checkboxes = section.querySelectorAll('.row-checkbox')
    this.bulkBar    = section.querySelector('#bulk-bar')
    this.countEl    = section.querySelector('#bulk-count')
    this.rows       = section.querySelectorAll('.table-row')

    this.selectAll.addEventListener('change', () => this.toggleAll())
    this.checkboxes.forEach(cb => cb.addEventListener('change', () => this.update()))

    // Bulk actions
    section.querySelectorAll('[data-bulk-action]').forEach(btn => {
      btn.addEventListener('click', () => this.handleAction(btn.dataset.bulkAction))
    })

    // Clear selection
    section.querySelector('.bulk-bar__deselect')?.addEventListener('click', () => this.clear())
  }

  selected () {
    return [...this.checkboxes].filter(cb => cb.checked)
  }

  update () {
    const sel   = this.selected()
    const count = sel.length
    const total = this.checkboxes.length

    // Update rows aria-selected
    this.rows.forEach((row, i) => {
      row.setAttribute('aria-selected', String(this.checkboxes[i].checked))
    })

    // Indeterminate state
    this.selectAll.indeterminate = count > 0 && count < total
    this.selectAll.checked       = count === total

    // Show/hide bulk bar
    if (count > 0) {
      this.bulkBar.hidden = false
      this.countEl.textContent = `${count} selected`
    } else {
      this.bulkBar.hidden = true
    }
  }

  toggleAll () {
    this.checkboxes.forEach(cb => { cb.checked = this.selectAll.checked })
    this.update()
  }

  clear () {
    this.checkboxes.forEach(cb => { cb.checked = false })
    this.selectAll.checked = false
    this.selectAll.indeterminate = false
    this.update()
  }

  async handleAction (action) {
    const ids = this.selected().map(cb => cb.closest('.table-row')?.dataset.id)

    // Destructive actions require confirmation
    if (action === 'delete') {
      const confirmed = await this.confirm(`Delete ${ids.length} items permanently?`)
      if (!confirmed) return
    }

    try {
      await fetch(`/api/bulk/${action}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ids })
      })
      // Optimistic: remove rows immediately
      this.selected().forEach(cb => cb.closest('.table-row')?.remove())
      this.clear()
    } catch (err) {
      console.error(err)
    }
  }

  confirm (message) {
    return new Promise(resolve => {
      // Use your modal pattern — not window.confirm
      // Dispatch a confirm event and wait for user response
      resolve(window.confirm(message)) // Replace with modal
    })
  }
}

document.querySelectorAll('.data-table-section').forEach(el => new BulkSelection(el))
```

---

## Pattern 2 — Sticky Bottom Action Bar (Mobile)

On mobile, the toolbar pins to the bottom of the viewport instead of floating above the table.

```html
<div class="bulk-bar-bottom" id="bulk-bar-bottom" hidden>
  <div class="bulk-bar-bottom__count">
    <span id="bulk-count-bottom">3 selected</span>
    <button class="bulk-bar__deselect" type="button" aria-label="Clear selection">✕</button>
  </div>
  <div class="bulk-bar-bottom__actions">
    <button class="btn btn--ghost btn--sm" type="button">Archive</button>
    <button class="btn btn--danger btn--sm" type="button">Delete</button>
  </div>
</div>
```

```css
.bulk-bar-bottom {
  position: fixed;
  bottom: 0;
  left: 0; right: 0;
  background: var(--color-surface);
  border-top: 1px solid var(--color-border);
  padding: var(--space-4) var(--space-4) calc(var(--space-4) + env(safe-area-inset-bottom));
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-4);
  box-shadow: var(--shadow-lg);
  z-index: var(--z-sticky);

  @starting-style { transform: translateY(100%); }
  transform: translateY(0);
  transition: transform var(--duration-fast) var(--ease-spring);
}

.bulk-bar-bottom[hidden] {
  display: none;
}

/* Show inline bar on desktop, bottom bar on mobile */
@media (min-width: 640px) {
  .bulk-bar-bottom { display: none !important; }
}

@media (max-width: 639px) {
  .bulk-bar { display: none !important; }
}
```

---

## Confirmation for Destructive Actions

Never execute a destructive bulk action without explicit confirmation. Use the modal pattern:

```html
<!-- Reuse patterns/product-ui/modals.md — confirmation dialog -->
<dialog class="modal modal--sm" id="bulk-delete-confirm" aria-labelledby="delete-title">
  <div class="modal__header">
    <h2 class="modal__title" id="delete-title">Delete 3 projects?</h2>
  </div>
  <div class="modal__body">
    <p>This will permanently delete the selected projects and all associated data.
    This action cannot be undone.</p>
  </div>
  <div class="modal__footer">
    <button class="btn btn--secondary" type="button" data-modal-close>Cancel</button>
    <button class="btn btn--danger" type="button" id="confirm-delete">Delete permanently</button>
  </div>
</dialog>
```

---

## Anti-Patterns

```
× Bulk action toolbar visible when nothing is selected
× Executing destructive actions without confirmation
× No feedback after bulk action (rows don't update, no toast)
× Clearing selection before showing success state
× Select-all that only selects the current page with no indication
× Bulk actions with no way to undo (implement toast with undo for non-destructive)
× More than 5 bulk actions — group or hide rarely-used actions in overflow menu
```

---

*Pattern version: global-design-skill v1.0 — `patterns/admin-ui/bulk-actions.md`*  
*Related: `patterns/admin-ui/charts.md`, `rules/11-data-tables.md`, `patterns/product-ui/notifications.md`*
