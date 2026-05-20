# Pattern — Modals and Dialogs

> A modal interrupts everything. It pauses the user's task and demands their attention. Used correctly, a modal is the right tool for decisions and confirmations that require full focus. Used incorrectly, it's the product equivalent of a telemarketer calling during dinner. These patterns encode when to use modals and how to build them correctly.

---

## When to use a modal

```
USE a modal for:
  ✓ Destructive confirmation — "Delete this project?" (irreversible, requires attention)
  ✓ Complex input — add a new item when the form doesn't belong inline
  ✓ Blocking decision — user must choose before continuing
  ✓ Preview — image lightbox, document preview, video player

DO NOT use a modal for:
  ✗ Information the user didn't ask for (use toast or banner)
  ✗ Error messages (use inline error or notification)
  ✗ First-page marketing overlays (interrupt the primary task)
  ✗ Anything with more than 2 form sections (use a page or drawer instead)
  ✗ Nested modals (a modal triggered from another modal — redesign the flow)
```

---

## Pattern 1 — Confirmation Dialog

**Context:** Destructive or irreversible action. Short, clear, one decision.

```html
<!-- Trigger: the button that opens the modal -->
<button
  type="button"
  class="btn-ghost btn--danger"
  id="delete-trigger"
  aria-haspopup="dialog"
>
  Delete project
</button>

<!-- Dialog: native <dialog> element for built-in focus trap -->
<dialog
  class="modal"
  id="delete-modal"
  aria-modal="true"
  aria-labelledby="delete-modal-title"
  aria-describedby="delete-modal-desc"
>
  <div class="modal__inner">
    <div class="modal__header">
      <!-- Warning icon — reinforces severity -->
      <div class="modal__icon modal__icon--danger" aria-hidden="true">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/>
          <line x1="12" y1="9" x2="12" y2="13"/>
          <line x1="12" y1="17" x2="12.01" y2="17"/>
        </svg>
      </div>
      <button
        type="button"
        class="modal__close"
        aria-label="Close dialog"
      >
        <svg aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M18 6 6 18M6 6l12 12"/>
        </svg>
      </button>
    </div>

    <div class="modal__body">
      <h2 id="delete-modal-title" class="modal__title">Delete "Pipeline — Production"?</h2>
      <p id="delete-modal-desc" class="modal__desc">
        This will permanently delete the project and all its deployments.
        You cannot undo this action.
      </p>

      <!-- Confirmation input for high-stakes destructive actions -->
      <div class="field">
        <label for="confirm-delete" class="field__label">
          Type <strong>pipeline-production</strong> to confirm
        </label>
        <input
          type="text"
          id="confirm-delete"
          class="input"
          autocomplete="off"
          autocorrect="off"
          spellcheck="false"
          aria-describedby="confirm-delete-desc"
        />
        <p class="sr-only" id="confirm-delete-desc">
          Type the project name exactly as shown above to enable the delete button.
        </p>
      </div>
    </div>

    <div class="modal__footer">
      <button type="button" class="btn-ghost" id="delete-cancel">Cancel</button>
      <button type="button" class="btn-primary btn--danger" id="delete-confirm" disabled>
        Delete project
      </button>
    </div>
  </div>
</dialog>
```

```js
const trigger = document.getElementById('delete-trigger')
const modal   = document.getElementById('delete-modal')
const cancel  = document.getElementById('delete-cancel')
const confirm = document.getElementById('delete-confirm')
const input   = document.getElementById('confirm-delete')

// Open
trigger.addEventListener('click', () => {
  modal.showModal()
  // Focus the input (not the destructive button)
  input.focus()
})

// Close — returns focus to trigger
function closeModal() {
  modal.close()
  trigger.focus()
  input.value = ''
  confirm.disabled = true
}

cancel.addEventListener('click', closeModal)
modal.addEventListener('click', e => {
  // Close on backdrop click
  if (e.target === modal) closeModal()
})
modal.addEventListener('keydown', e => {
  if (e.key === 'Escape') closeModal()
})

// Enable confirm only when text matches
input.addEventListener('input', () => {
  confirm.disabled = input.value !== 'pipeline-production'
})

// Confirm action
confirm.addEventListener('click', async () => {
  confirm.setAttribute('aria-busy', 'true')
  confirm.textContent = 'Deleting...'
  try {
    await api.deleteProject('pipeline-production')
    closeModal()
    // Navigate away or update list
  } catch {
    confirm.removeAttribute('aria-busy')
    confirm.textContent = 'Delete project'
  }
})
```

---

## Pattern 2 — Form Modal (Add / Edit)

**Context:** Creating or editing a record without leaving the current page. Short form — if it needs more than 6 fields, use a drawer or page instead.

```html
<button type="button" class="btn-primary" id="add-member-trigger" aria-haspopup="dialog">
  Add team member
</button>

<dialog class="modal modal--form" id="add-member-modal" aria-modal="true"
        aria-labelledby="add-member-title">
  <div class="modal__inner">
    <div class="modal__header">
      <h2 id="add-member-title" class="modal__title">Add team member</h2>
      <button type="button" class="modal__close" aria-label="Close">
        <svg aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M18 6 6 18M6 6l12 12"/></svg>
      </button>
    </div>

    <form class="modal__body modal__form" id="add-member-form" novalidate>
      <div class="field">
        <label for="member-email" class="field__label">Email address</label>
        <input
          type="email" id="member-email" name="email"
          class="input" inputmode="email" autocomplete="off"
          aria-required="true" aria-describedby="member-email-error"
        />
        <p class="field__error" id="member-email-error" role="alert" aria-live="assertive"></p>
      </div>

      <div class="field">
        <label for="member-role" class="field__label">Role</label>
        <select id="member-role" name="role" class="input" aria-required="true">
          <option value="">Select a role</option>
          <option value="viewer">Viewer — read access</option>
          <option value="editor">Editor — can deploy</option>
          <option value="admin">Admin — full access</option>
        </select>
      </div>
    </form>

    <div class="modal__footer">
      <button type="button" class="btn-ghost" id="add-member-cancel">Cancel</button>
      <button type="submit" form="add-member-form" class="btn-primary" id="add-member-submit">
        Send invite
      </button>
    </div>
  </div>
</dialog>
```

---

## Pattern 3 — Drawer (Side Panel)

**Context:** More space needed than a modal offers. Settings panel, filter panel, detail view. Slides in from the right. Does not cover the full viewport — content remains visible behind it.

```html
<button type="button" class="btn-ghost btn--sm" id="filters-trigger" aria-expanded="false"
        aria-controls="filters-drawer">
  Filters
</button>

<!-- Drawer -->
<div
  class="drawer"
  id="filters-drawer"
  role="dialog"
  aria-modal="true"
  aria-labelledby="drawer-title"
  aria-hidden="true"
>
  <div class="drawer__backdrop" id="drawer-backdrop"></div>
  <div class="drawer__panel">
    <div class="drawer__header">
      <h2 id="drawer-title" class="drawer__title">Filters</h2>
      <button type="button" class="modal__close" id="drawer-close" aria-label="Close filters">
        <svg aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M18 6 6 18M6 6l12 12"/></svg>
      </button>
    </div>

    <div class="drawer__body">
      <!-- filter controls -->
    </div>

    <div class="drawer__footer">
      <button type="button" class="btn-ghost" id="clear-filters">Clear all</button>
      <button type="button" class="btn-primary" id="apply-filters">Apply filters</button>
    </div>
  </div>
</div>
```

```css
/* ── Modal core ── */
.modal {
  position: fixed;
  inset: 0;
  width: min(560px, calc(100vw - var(--space-8)));
  max-height: calc(100dvh - var(--space-16));
  margin: auto;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-2xl);
  padding: 0;
  overflow: hidden;

  /* Entry animation */
  transition:
    opacity    var(--duration-moderate) var(--ease-spring),
    transform  var(--duration-moderate) var(--ease-spring),
    display    var(--duration-moderate) allow-discrete;
}

.modal:not([open]) {
  opacity: 0;
  transform: scale(0.96) translateY(8px);
  display: none;
  pointer-events: none;
}

@starting-style {
  .modal[open] {
    opacity: 0;
    transform: scale(0.96) translateY(8px);
  }
}

/* Backdrop */
.modal::backdrop {
  background: oklch(0% 0 0 / 0.5);
  backdrop-filter: blur(4px);

  transition:
    opacity var(--duration-moderate) var(--ease-smooth),
    display var(--duration-moderate) allow-discrete;
}

@starting-style {
  .modal[open]::backdrop { opacity: 0; }
}

/* Modal layout */
.modal__inner { display: flex; flex-direction: column; height: 100%; }

.modal__header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: var(--space-4);
  padding: var(--space-6) var(--space-6) var(--space-4);
  border-bottom: 1px solid var(--color-border);
}

.modal__icon {
  width: 40px; height: 40px;
  border-radius: var(--radius-md);
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0;
}
.modal__icon--danger { background: var(--color-error-bg); color: var(--color-error-text); }

.modal__title {
  font-size: var(--text-lg);
  font-weight: var(--font-weight-semibold);
  line-height: var(--line-height-snug);
  color: var(--color-text-primary);
}
.modal__desc { font-size: var(--text-body); color: var(--color-text-secondary); margin-top: var(--space-2); }

.modal__close {
  width: 32px; height: 32px;
  display: flex; align-items: center; justify-content: center;
  background: transparent; border: none;
  border-radius: var(--radius-md);
  color: var(--color-text-muted); cursor: pointer;
  flex-shrink: 0;
  transition: background var(--duration-fast) var(--ease-smooth),
              color    var(--duration-fast) var(--ease-smooth);
}
.modal__close:hover { background: var(--color-surface-2); color: var(--color-text-primary); }

.modal__body { padding: var(--space-6); flex: 1; overflow-y: auto; }
.modal__form { display: flex; flex-direction: column; gap: var(--space-5); }

.modal__footer {
  display: flex;
  justify-content: flex-end;
  gap: var(--space-3);
  padding: var(--space-4) var(--space-6);
  border-top: 1px solid var(--color-border);
}

/* Danger button variant */
.btn--danger {
  background: var(--color-error-text);
  color: white;
}
.btn--danger:hover { background: oklch(from var(--color-error-text) calc(l - 0.08) c h); }
.btn--danger:disabled { opacity: 0.4; pointer-events: none; }

/* ── Drawer ── */
.drawer {
  position: fixed;
  inset: 0;
  z-index: var(--z-modal);
  pointer-events: none;
}
.drawer[aria-hidden="false"] { pointer-events: auto; }

.drawer__backdrop {
  position: absolute;
  inset: 0;
  background: oklch(0% 0 0 / 0.5);
  opacity: 0;
  transition: opacity var(--duration-moderate) var(--ease-smooth);
}
.drawer[aria-hidden="false"] .drawer__backdrop { opacity: 1; }

.drawer__panel {
  position: absolute;
  top: 0; right: 0; bottom: 0;
  width: min(400px, 90vw);
  background: var(--color-surface);
  border-left: 1px solid var(--color-border);
  box-shadow: var(--shadow-2xl);
  display: flex; flex-direction: column;
  transform: translateX(100%);
  transition: transform var(--duration-moderate) var(--ease-spring);
}
.drawer[aria-hidden="false"] .drawer__panel { transform: translateX(0); }

.drawer__header {
  display: flex; justify-content: space-between; align-items: center;
  padding: var(--space-5) var(--space-6);
  border-bottom: 1px solid var(--color-border);
}
.drawer__title { font-size: var(--text-lg); font-weight: var(--font-weight-semibold); }
.drawer__body  { flex: 1; overflow-y: auto; padding: var(--space-6); }
.drawer__footer {
  display: flex; justify-content: flex-end; gap: var(--space-3);
  padding: var(--space-4) var(--space-6);
  border-top: 1px solid var(--color-border);
}

/* prefers-reduced-motion */
@media (prefers-reduced-motion: reduce) {
  .modal,
  .drawer__panel {
    transition: opacity var(--duration-fast);
    transform: none !important;
  }
}
```

---

## Accessibility Requirements (All Modals)

```
[ ] Native <dialog> element with showModal() — or role="dialog" aria-modal="true"
[ ] aria-labelledby pointing to the modal title
[ ] aria-describedby pointing to supporting description
[ ] Focus moves to first interactive element on open (input > heading > primary action)
[ ] Focus trapped inside — Tab cycles within modal only
[ ] Escape key closes modal
[ ] Click on backdrop closes modal (where appropriate)
[ ] Focus returns to the trigger element on close
[ ] Scroll locked on body while modal is open (native <dialog> does this)
[ ] Backdrop: semi-transparent, communicates content is behind
```

---

*Pattern version: global-design-skill v1.0 — `patterns/product-ui/modals.md`*
*Related: `rules/07-accessibility.md` R7, `rules/05-animation.md` R5, `checklists/ui-review.md` §6*
