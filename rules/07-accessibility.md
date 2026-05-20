# Rule — Accessibility

> Accessibility is not a feature — it is correctness. An interface that cannot be used with a keyboard, screen reader, or at low vision is broken for a specific population. WCAG 2.2 AA is the minimum, not the ceiling. These rules encode the decisions that separate a functional interface from a usable one.

---

## R1 — Every interactive element is reachable and operable by keyboard.

Approximately 26% of US adults have some disability. Keyboard-only operation is required by users who cannot use a mouse (motor disabilities, tremors, broken mice) and by screen reader users.

```html
<!-- Correct: native interactive elements receive focus by default -->
<button>Save changes</button>
<a href="/settings">Settings</a>
<input type="text" />
<select>...</select>

<!-- Correct: custom interactive element with tabindex -->
<div
  role="button"
  tabindex="0"
  onclick="handleClick()"
  onkeydown="if (e.key === 'Enter' || e.key === ' ') handleClick()"
>
  Custom button
</div>

<!-- Wrong: div with click handler but no keyboard access -->
<div onclick="handleClick()">Click me</div>
```

**Tab order rules:**
- Never use `tabindex > 0` (positive values disrupt natural order)
- Use DOM order to control focus sequence
- `tabindex="0"` adds element to natural tab order
- `tabindex="-1"` removes from tab order but allows programmatic focus

---

## R2 — Focus-visible ring on every interactive element.

The `:focus-visible` ring tells keyboard users where they are. Never remove it — hiding the ring is like removing a mouse cursor.

```css
/* Global focus ring */
:focus-visible {
  outline: var(--focus-ring);          /* 2px solid var(--color-accent) */
  outline-offset: var(--focus-ring-offset);  /* 2px */
  border-radius: var(--focus-ring-radius);   /* var(--radius-md) */
}

/* Remove only the pointer focus ring — keep keyboard ring */
:focus:not(:focus-visible) {
  outline: none;
}

/* Never */
*:focus { outline: none; }
button:focus { outline: 0; }
```

**Context-specific overrides:**
```css
/* Circular elements (avatars, icon buttons) */
.btn-icon:focus-visible {
  border-radius: var(--radius-full);
}

/* Inset focus ring (when outline would be clipped) */
.panel-item:focus-visible {
  outline-offset: -2px;
  border-radius: 0;
}
```

---

## R3 — Every form input has a visible, persistent label.

Placeholder text disappears on focus and is not a label. Users with cognitive disabilities and users who return to a partially-filled form need to see labels at all times.

```html
<!-- Correct -->
<div class="field">
  <label for="email">Email address</label>
  <input type="email" id="email" placeholder="you@company.com" />
</div>

<!-- Correct: visually hidden label (when visual space is constrained) -->
<label for="search" class="sr-only">Search</label>
<input type="search" id="search" placeholder="Search projects…" />

<!-- Wrong: placeholder as label -->
<input type="email" placeholder="Email address" />

<!-- Wrong: implicit label without for/id -->
<label>Email <input type="email" /></label>
<!-- (implicit labels fail in some screen readers) -->
```

---

## R4 — Images have descriptive alt text. Decorative images use alt="".

Screen readers announce image content. An image without alt text is announced as the filename. A decorative image with a description interrupts the reading flow.

```html
<!-- Informative image: describe the content -->
<img
  src="/dashboard-screenshot.webp"
  alt="The Pipeline dashboard showing 4 active deployments and 2 failed builds"
  width="720"
  height="480"
/>

<!-- Chart/graph: describe the data it shows -->
<img
  src="/revenue-chart.png"
  alt="Bar chart showing monthly revenue increasing from $61,200 in May 2025 to $84,210 in May 2026"
/>

<!-- Decorative (icon next to labeled text, background texture): empty alt -->
<img src="/decorative-wave.svg" alt="" aria-hidden="true" />

<!-- Wrong: filename as alt -->
<img src="/hero.jpg" alt="hero.jpg" />

<!-- Wrong: "image of" prefix (redundant — screen reader already says "image") -->
<img src="/team.jpg" alt="Image of the team at the office" />
```

---

## R5 — ARIA roles, states, and properties for all custom components.

The ARIA authoring practices cover every common UI pattern. When you build a custom component, every interactive state must be communicated via ARIA attributes.

**Most commonly missed ARIA attributes:**

```html
<!-- Accordion / disclosure -->
<button
  aria-expanded="false"
  aria-controls="section-content"
>
  Section title
</button>
<div id="section-content" hidden>...</div>

<!-- Dropdown / combobox -->
<button
  aria-haspopup="listbox"
  aria-expanded="false"
  aria-controls="dropdown-list"
>
  Filter by status
</button>
<ul id="dropdown-list" role="listbox" aria-label="Status options">
  <li role="option" aria-selected="true">Active</li>
  <li role="option" aria-selected="false">Inactive</li>
</ul>

<!-- Tab panel -->
<div role="tablist" aria-label="Settings sections">
  <button role="tab" aria-selected="true" aria-controls="panel-profile" id="tab-profile">Profile</button>
  <button role="tab" aria-selected="false" aria-controls="panel-security" id="tab-security">Security</button>
</div>
<div role="tabpanel" id="panel-profile" aria-labelledby="tab-profile">...</div>

<!-- Modal / dialog -->
<dialog
  aria-modal="true"
  aria-labelledby="modal-title"
  aria-describedby="modal-description"
>
  <h2 id="modal-title">Delete project</h2>
  <p id="modal-description">This action cannot be undone.</p>
</dialog>

<!-- Loading state -->
<div aria-busy="true" aria-live="polite">
  Loading your projects…
</div>

<!-- Sorted table column -->
<th aria-sort="ascending">Name</th>
<th aria-sort="none">Updated</th>
```

---

## R6 — Dynamic content changes are announced via `aria-live`.

Screen readers only read what's in the document when the user navigates to it — they don't re-read content that changes dynamically. `aria-live` regions announce changes as they happen.

```html
<!-- Error that appears after form submit -->
<div
  role="alert"
  aria-live="assertive"
  aria-atomic="true"
>
  <!-- Error message injected here by JS -->
</div>

<!-- Success toast -->
<div
  role="status"
  aria-live="polite"
  aria-atomic="true"
>
  <!-- Toast message injected here -->
</div>

<!-- Live search results count -->
<p
  aria-live="polite"
  aria-atomic="true"
>
  <!-- "12 results for 'deploy'" — updates as user types -->
</p>
```

**`aria-live` values:**
- `"assertive"` — interrupts immediately (use for errors, critical alerts)
- `"polite"` — waits for user pause (use for success, status, counts)
- `aria-atomic="true"` — reads the entire region, not just changed parts

---

## R7 — Modal dialogs have focus trap and return focus on close.

When a modal opens, keyboard focus must stay within it. When it closes, focus must return to the element that triggered it. Neither is automatic.

```js
function openModal(modal, trigger) {
  modal.showModal()  // native dialog: auto-blocks background interaction

  // Focus first interactive element in modal
  const firstFocusable = modal.querySelector('button, [href], input, select, textarea, [tabindex="0"]')
  firstFocusable?.focus()
}

function closeModal(modal, trigger) {
  modal.close()
  trigger?.focus()  // return focus to the element that opened the modal
}

// Focus trap — keep Tab within the modal
modal.addEventListener('keydown', e => {
  if (e.key !== 'Tab') return

  const focusable = [...modal.querySelectorAll('button, [href], input, select, textarea, [tabindex="0"]')]
  const first = focusable[0]
  const last = focusable[focusable.length - 1]

  if (e.shiftKey && document.activeElement === first) {
    e.preventDefault()
    last.focus()
  } else if (!e.shiftKey && document.activeElement === last) {
    e.preventDefault()
    first.focus()
  }
})

// Close on Escape
modal.addEventListener('keydown', e => {
  if (e.key === 'Escape') closeModal(modal, trigger)
})
```

---

## R8 — All touch targets are minimum 44×44px.

This is Apple's Human Interface Guidelines minimum, Google's Material Design minimum, and WCAG 2.5.5 (AA). Users with motor disabilities and users in motion (commuting, walking) need larger targets.

```css
/* Correct: element itself is 44px */
.btn { min-height: 44px; min-width: 44px; }

/* Correct: visual element smaller, hit area extended with pseudo-element */
.icon-btn {
  width: 24px;
  height: 24px;
  position: relative;
}
.icon-btn::after {
  content: '';
  position: absolute;
  inset: -10px;  /* extends hit area to 44×44 */
}

/* Wrong: 28px button */
.btn-xs { height: 28px; padding-inline: 8px; }  /* too small */

/* Exception: links within text (constrained by line-height context) */
```

---

## R9 — Skip navigation link at the top of every page.

Keyboard users must tab through all navigation items to reach the main content on every page load. A skip link jumps directly to `<main>`.

```html
<!-- First element in <body>, visually hidden until focused -->
<a href="#main-content" class="skip-link">Skip to main content</a>

<!-- Must be present on the target element -->
<main id="main-content" tabindex="-1">
  <!-- tabindex="-1" allows programmatic focus via the skip link href -->
</main>
```

```css
.skip-link {
  position: absolute;
  top: var(--space-4);
  left: var(--space-4);
  z-index: var(--z-max);
  background: var(--color-surface);
  color: var(--color-text-primary);
  border: 2px solid var(--color-accent);
  border-radius: var(--radius-md);
  padding: var(--space-3) var(--space-5);
  font-weight: var(--font-weight-medium);
  text-decoration: none;

  /* Hidden until focused */
  transform: translateY(-200%);
  transition: transform var(--duration-fast) var(--ease-spring);
}

.skip-link:focus-visible {
  transform: translateY(0);
}
```

---

## R10 — Use semantic HTML. ARIA supplements — it does not replace.

Native HTML elements carry built-in accessibility semantics. A `<button>` is keyboard-operable, focusable, and has a role of "button" by default. A `<div role="button" tabindex="0">` requires you to reimplement all of that manually.

```html
<!-- Correct: semantic elements -->
<nav aria-label="Main navigation">...</nav>
<main>...</main>
<article>...</article>
<aside aria-label="Related links">...</aside>
<header>...</header>
<footer>...</footer>
<h1>Page title</h1>
<button>Action</button>
<a href="/page">Link</a>
<ul><li>...</li></ul>
<table><caption>...</caption>...</table>

<!-- Wrong: div soup with ARIA bolted on -->
<div role="navigation" aria-label="Main navigation">...</div>
<div role="main">...</div>
<div role="button" tabindex="0">Action</div>
```

**First rule of ARIA:** If you can use a native HTML element with the required semantics, use it. Only use ARIA when native semantics are insufficient.

---

## Keyboard Navigation Reference

| Component | Enter | Space | Escape | Arrow keys | Tab |
|---|---|---|---|---|---|
| Button | Activate | Activate | — | — | Next focusable |
| Link | Follow | — | — | — | Next focusable |
| Checkbox | Toggle | Toggle | — | — | Next focusable |
| Radio group | Select | Select | — | ↑↓ move selection | Next group |
| Dropdown/listbox | Select option | — | Close | ↑↓ navigate options | Close + next |
| Accordion | Toggle | Toggle | — | — | Next accordion |
| Modal | — | — | Close | — | Next in modal (trapped) |
| Tabs | — | — | — | ←→ switch tabs | Exit tablist |
| Combobox | Select | — | Clear/close | ↑↓ navigate options | Next focusable |
| Date picker | Select date | — | Close | ←→↑↓ navigate | Close + next |

---

## Acceptance Criteria

```
[ ] All interactive elements reachable via Tab in logical order
[ ] Focus-visible ring: 2px solid accent, correct offset, visible in both themes
[ ] Skip navigation link at page top, activates on focus
[ ] All form inputs have visible, persistent <label> with for/id wiring
[ ] All images: descriptive alt text or alt="" for decorative
[ ] All custom components: correct ARIA role + state attributes
[ ] Modal: focus trap + Escape closes + focus returns to trigger
[ ] Dynamic content (errors, toasts, counts): aria-live regions wired
[ ] All touch targets ≥ 44×44px
[ ] Semantic HTML used — ARIA added where native semantics insufficient
[ ] Color contrast ≥ 4.5:1 body text, ≥ 3:1 large text and UI components
[ ] Tested: keyboard-only navigation, screen reader (VoiceOver/NVDA), 200% zoom
```

---

*Rule version: global-design-skill v1.0 — `rules/07-accessibility.md`*
*Related: `templates/specs/frontend-tz.md` ARIA section, `checklists/ui-review.md` accessibility section, `rules/06-components.md`*
