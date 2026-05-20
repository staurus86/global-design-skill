# Reference — Accessibility

> WCAG 2.2 AA implementation guide. Contrast, keyboard navigation, focus management, ARIA roles, screen readers, and reduced motion. Accessibility is structural — it cannot be added after the fact.

---

## Core Requirement

**WCAG 2.2 Level AA** is the minimum. It is a legal requirement in the EU (EAA 2025), USA (ADA), UK (PSBAR), and most jurisdictions.

**Contrast ratios:**
- Normal text (< 18px / < 14px bold): **4.5:1**
- Large text (≥ 18px / ≥ 14px bold): **3:1**
- UI components (buttons, inputs, focus rings): **3:1**
- Decorative elements: no requirement

---

## Focus States

Every interactive element must have a visible focus state. Never `outline: none` without replacement.

```css
/* Global focus ring — overrides browser default */
:focus-visible {
  outline: 2px solid var(--color-accent);
  outline-offset: 2px;
  border-radius: var(--radius-sm);
}

/* Remove on mouse click (not keyboard) */
:focus:not(:focus-visible) {
  outline: none;
}

/* Component-specific focus ring */
.btn:focus-visible {
  outline: 2px solid var(--color-accent);
  outline-offset: 3px;
  box-shadow: 0 0 0 4px oklch(from var(--color-accent) l c h / 0.15);
}

/* Input focus */
.input:focus-visible {
  outline: 2px solid var(--color-accent);
  outline-offset: 0;
  border-color: var(--color-accent);
}

/* Dark background — white focus ring */
.dark-section *:focus-visible {
  outline-color: oklch(95% 0.005 258);
}
```

---

## Skip Navigation

Must appear as the first interactive element on every page with navigation.

```html
<!-- First element in <body> -->
<a href="#main-content" class="skip-nav">
  Skip to main content
</a>

<nav>...</nav>

<main id="main-content" tabindex="-1">
  <!-- main content -->
</main>
```

```css
.skip-nav {
  position: absolute;
  top: -100%;
  left: var(--space-4);
  padding: var(--space-2) var(--space-4);
  background: var(--color-surface);
  border: 2px solid var(--color-accent);
  border-radius: var(--radius-md);
  color: var(--color-text);
  font-weight: 600;
  z-index: var(--z-max);
  text-decoration: none;
  transition: top var(--duration-fast) var(--ease-smooth);
}

.skip-nav:focus {
  top: var(--space-4);
}
```

---

## Form Accessibility

Every input must have a visible, linked label.

```html
<!-- Correct: visible label linked to input -->
<div class="field">
  <label for="email">Email address</label>
  <input
    type="email"
    id="email"
    name="email"
    autocomplete="email"
    aria-describedby="email-hint email-error"
    aria-required="true"
  />
  <p id="email-hint" class="field-hint">
    We'll only use this to send your receipts.
  </p>
  <p id="email-error" class="field-error" role="alert" aria-live="polite">
    <!-- populated by JS on validation error -->
  </p>
</div>

<!-- Wrong: placeholder only -->
<input type="email" placeholder="Email address" />
```

```css
/* Label always visible */
label {
  display: block;
  font-size: var(--text-xs);
  font-weight: 500;
  color: var(--color-text-2);
  margin-bottom: var(--space-2);
}

/* Error state */
.field[data-error] label { color: var(--color-error); }
.field[data-error] input {
  border-color: var(--color-error);
  box-shadow: 0 0 0 3px oklch(from var(--color-error) l c h / 0.15);
}

.field-error {
  color: var(--color-error);
  font-size: var(--text-xs);
  margin-top: var(--space-1);
}
```

---

## Modal / Dialog

Focus must be trapped inside the modal while open. Returns to trigger on close.

```html
<dialog
  id="confirm-dialog"
  aria-labelledby="dialog-title"
  aria-describedby="dialog-desc"
  aria-modal="true"
>
  <h2 id="dialog-title">Delete this item?</h2>
  <p id="dialog-desc">This action cannot be undone.</p>

  <div class="dialog-actions">
    <button autofocus>Cancel</button>
    <button class="btn-danger">Delete</button>
  </div>
</dialog>
```

```ts
class AccessibleDialog {
  private trigger: HTMLElement | null = null

  open(dialog: HTMLDialogElement, triggerEl: HTMLElement) {
    this.trigger = triggerEl
    dialog.showModal()

    /* Trap focus — browser handles this natively with <dialog> */
    /* Escape key: browser closes dialog natively */

    dialog.addEventListener('close', () => this.close(), { once: true })
  }

  close() {
    /* Return focus to the element that opened the modal */
    this.trigger?.focus()
  }
}
```

---

## Images

```html
<!-- Informative image: describe what the image communicates -->
<img
  src="/dashboard-screenshot.webp"
  alt="Dashboard showing 4 active deployments and a 99.8% uptime metric for the past 30 days"
  width="1200"
  height="675"
/>

<!-- Decorative image: empty alt, no role -->
<img src="/abstract-bg.webp" alt="" width="1920" height="1080" />

<!-- Icon with text label: icon is decorative -->
<button>
  <svg aria-hidden="true" focusable="false"><!-- ... --></svg>
  Download report
</button>

<!-- Icon without text: needs aria-label -->
<button aria-label="Download report as PDF">
  <svg aria-hidden="true" focusable="false"><!-- ... --></svg>
</button>
```

---

## ARIA Roles and States

### Interactive elements

```html
<!-- Accordion -->
<button
  aria-expanded="false"
  aria-controls="accordion-panel-1"
  id="accordion-trigger-1"
>
  How does billing work?
</button>
<div
  id="accordion-panel-1"
  role="region"
  aria-labelledby="accordion-trigger-1"
  hidden
>
  <!-- content -->
</div>

<!-- Tabs -->
<div role="tablist" aria-label="Account settings">
  <button role="tab" aria-selected="true"  aria-controls="panel-profile" id="tab-profile">Profile</button>
  <button role="tab" aria-selected="false" aria-controls="panel-billing" id="tab-billing">Billing</button>
</div>
<div role="tabpanel" id="panel-profile" aria-labelledby="tab-profile">...</div>
<div role="tabpanel" id="panel-billing" aria-labelledby="tab-billing" hidden>...</div>

<!-- Combobox -->
<label for="search">Search</label>
<input
  type="text"
  id="search"
  role="combobox"
  aria-expanded="false"
  aria-autocomplete="list"
  aria-controls="search-listbox"
  aria-activedescendant=""
/>
<ul role="listbox" id="search-listbox">
  <li role="option" id="opt-1" aria-selected="false">Result 1</li>
</ul>
```

### Dynamic content

```html
<!-- Toast / notification -->
<div role="alert" aria-live="assertive" aria-atomic="true">
  <!-- Populated by JS -->
</div>

<!-- Status update (non-urgent) -->
<div role="status" aria-live="polite">
  <!-- Populated by JS — "3 items saved" etc. -->
</div>

<!-- Loading state -->
<div aria-live="polite" aria-busy="true">
  <span class="sr-only">Loading results...</span>
</div>
```

---

## Keyboard Navigation

All interactive elements must be keyboard-accessible.

```ts
/* Keyboard pattern for custom components */

/* Dropdown */
trigger.addEventListener('keydown', (e: KeyboardEvent) => {
  if (e.key === 'Enter' || e.key === ' ') {
    e.preventDefault()
    openDropdown()
  }
  if (e.key === 'Escape') closeDropdown()
})

/* Tab list */
tabList.addEventListener('keydown', (e: KeyboardEvent) => {
  const tabs = [...tabList.querySelectorAll<HTMLElement>('[role="tab"]')]
  const currentIndex = tabs.indexOf(document.activeElement as HTMLElement)

  if (e.key === 'ArrowRight') {
    e.preventDefault()
    tabs[(currentIndex + 1) % tabs.length].focus()
  }
  if (e.key === 'ArrowLeft') {
    e.preventDefault()
    tabs[(currentIndex - 1 + tabs.length) % tabs.length].focus()
  }
  if (e.key === 'Home') { e.preventDefault(); tabs[0].focus() }
  if (e.key === 'End')  { e.preventDefault(); tabs[tabs.length - 1].focus() }
})
```

---

## Screen Reader Utilities

```css
/* Visually hidden but accessible to screen readers */
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}

/* Becomes visible on focus (for skip links) */
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  padding: inherit;
  margin: inherit;
  overflow: visible;
  clip: auto;
  white-space: normal;
}
```

---

## Reduced Motion

All animations must respect `prefers-reduced-motion`. This is a WCAG 2.3 Level A requirement.

```css
/* Global reset — safest approach for complex animation systems */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}

/* Nuanced — preserve opacity, remove motion */
@media (prefers-reduced-motion: reduce) {
  .hero-heading {
    animation: fade-in 200ms forwards;
    transform: none;
  }
  .parallax    { transform: none !important; }
  .floating-el { animation: none; }
}

@keyframes fade-in { to { opacity: 1; } }
```

```ts
/* JS check before running GSAP / motion/react */
const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches

if (!reduced) {
  gsap.from('.hero-heading', { y: 40, opacity: 0, duration: 0.8 })
} else {
  gsap.from('.hero-heading', { opacity: 0, duration: 0.2 })
}
```

---

## Color Accessibility

```css
/* Color must never be the ONLY differentiator */

/* Wrong — error state indicated by color alone */
.input-error { border-color: var(--color-error); }

/* Correct — color + icon + label + border */
.input-error {
  border-color: var(--color-error);
  background-image: url("data:image/svg+xml,..."); /* error icon */
  padding-right: var(--space-10);
}

.field-error-label {
  color: var(--color-error);
  display: flex;
  align-items: center;
  gap: var(--space-1);
}

.field-error-label::before {
  content: '⚠';
  aria-hidden: 'true';
}
```

---

## Accessibility Checklist

```
[ ] Contrast: 4.5:1 normal text, 3:1 large text and UI components
[ ] Skip navigation link at page top
[ ] All form inputs: visible <label> linked with for/id
[ ] Error messages: aria-live="polite" + descriptive text
[ ] All images: descriptive alt (or alt="" for decorative)
[ ] Modal: focus trap + aria-modal + focus returns on close
[ ] All interactive elements keyboard-accessible
[ ] Tab order matches visual reading order
[ ] No outline: none without visible replacement
[ ] aria-expanded on all toggles (accordion, dropdown, combobox)
[ ] prefers-reduced-motion: all animations conditional
[ ] Color is not the only differentiator
[ ] Charts have data table alternative (for screen readers)
```

---

*Reference version: global-design-skill v1.0 — `references/accessibility.md`*
*Related: `rules/08-accessibility.md`, `checklists/global-design-review.md` §7, `references/forms.md`*
