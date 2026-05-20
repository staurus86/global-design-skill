# Example 03 — Form Accessibility Audit

> **Rules applied:** accessibility R1–R6, R8, R10 · typography R2 · color R7 · performance R8

**Scenario:** A signup form that looks fine visually but fails a basic keyboard-and-screen-reader audit. The UX team ran an automated axe scan: 9 violations, severity: critical. Manual keyboard test: not completable.

---

## Before — The Broken Form

```html
<div class="signup-form">
  <div class="form-title">Create your account</div>

  <div class="field">
    <input type="text" placeholder="Full name" class="input" />
  </div>

  <div class="field">
    <input type="email" placeholder="Work email" class="input" />
  </div>

  <div class="field">
    <input type="password" placeholder="Password" class="input" />
    <div class="hint">Must be at least 8 characters</div>
  </div>

  <div class="field">
    <div class="checkbox-row">
      <div class="checkbox" onclick="toggleCheckbox(this)"></div>
      <span>I agree to the <span style="color:#6366f1">Terms of Service</span></span>
    </div>
  </div>

  <div class="btn-primary" onclick="submitForm()">Create account</div>

  <div class="error-msg" id="error" style="display:none; color:red;">
    Please fix the errors above.
  </div>
</div>
```

```css
.input {
  width: 100%;
  border: 1px solid #d1d5db;
  border-radius: 6px;
  padding: 8px 12px;
  font-size: 13px;      /* iOS zoom trigger */
  outline: none;        /* focus ring removed globally */
}

.input.error { border-color: red; }

.checkbox {
  width: 18px;
  height: 18px;         /* below 44px — untappable on mobile */
  border: 2px solid #d1d5db;
  border-radius: 3px;
  cursor: pointer;
}

.checkbox.checked { background: #6366f1; }

.btn-primary {
  background: #6366f1;
  color: white;
  text-align: center;
  padding: 10px;        /* not a button element */
  border-radius: 6px;
  cursor: pointer;
}

.error-msg { font-size: 13px; margin-top: 8px; }
```

---

## Diagnosis — 9 Violations

| # | Violation | Rule |
|---|---|---|
| 1 | Inputs have no `<label>` — placeholder is the only label | accessibility R3 |
| 2 | `outline: none` on `.input` — focus ring removed globally | accessibility R2 |
| 3 | Custom `<div class="checkbox">` — not keyboard operable | accessibility R1 |
| 4 | Checkbox has no ARIA role, state, or keyboard handler | accessibility R5 |
| 5 | Submit is a `<div>`, not a `<button>` — Tab-skipped, not Enter-activatable | accessibility R1, R10 |
| 6 | Error message only shows by JS `style.display` — `aria-live` not wired | accessibility R6 |
| 7 | Error state: red border only — color as the sole signal | color R7 |
| 8 | `font-size: 13px` — triggers iOS auto-zoom, below minimum | typography R2 |
| 9 | Checkbox touch target: 18×18px — fails 44×44px minimum | accessibility R8 |

---

## After — Corrected Form

```html
<form class="signup-form" novalidate>
  <h2 class="form-title">Create your account</h2>

  <!-- Field: Full name -->
  <div class="field">
    <label for="name" class="field__label">Full name</label>
    <input
      type="text"
      id="name"
      name="name"
      class="input"
      autocomplete="name"
      aria-required="true"
      aria-describedby="name-error"
    />
    <p class="field__error" id="name-error" role="alert" aria-live="assertive"></p>
  </div>

  <!-- Field: Work email -->
  <div class="field">
    <label for="email" class="field__label">Work email</label>
    <input
      type="email"
      id="email"
      name="email"
      class="input"
      autocomplete="email"
      aria-required="true"
      aria-describedby="email-error"
    />
    <p class="field__error" id="email-error" role="alert" aria-live="assertive"></p>
  </div>

  <!-- Field: Password -->
  <div class="field">
    <label for="password" class="field__label">Password</label>
    <div class="input-wrapper">
      <input
        type="password"
        id="password"
        name="password"
        class="input"
        autocomplete="new-password"
        aria-required="true"
        aria-describedby="password-hint password-error"
      />
      <button
        type="button"
        class="input-toggle"
        aria-label="Show password"
        data-target="password"
      >
        <!-- icon -->
        <svg aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z"/>
          <circle cx="12" cy="12" r="3"/>
        </svg>
      </button>
    </div>
    <p class="field__hint" id="password-hint">At least 8 characters, one uppercase, one number.</p>
    <p class="field__error" id="password-error" role="alert" aria-live="assertive"></p>
  </div>

  <!-- Checkbox: Terms -->
  <div class="field">
    <label class="checkbox-label">
      <input
        type="checkbox"
        name="terms"
        class="checkbox-native"
        aria-required="true"
        aria-describedby="terms-error"
      />
      <span class="checkbox-custom" aria-hidden="true"></span>
      I agree to the
      <a href="/terms" class="link">Terms of Service</a>
      and
      <a href="/privacy" class="link">Privacy Policy</a>
    </label>
    <p class="field__error" id="terms-error" role="alert" aria-live="assertive"></p>
  </div>

  <!-- Submit -->
  <button type="submit" class="btn-primary" id="submit-btn">
    Create account
  </button>

  <!-- Global form error — wired to aria-live -->
  <div
    class="form-error"
    id="form-error"
    role="alert"
    aria-live="assertive"
    aria-atomic="true"
  >
    <!-- Error injected here by JS -->
  </div>
</form>
```

```css
/* ── Global focus ring from tokens.css ── */
:focus-visible {
  outline: var(--focus-ring);
  outline-offset: var(--focus-ring-offset);
  border-radius: var(--focus-ring-radius);
}

/* ── Form layout ── */
.signup-form {
  display: flex;
  flex-direction: column;
  gap: var(--space-5);
  max-width: 480px;
}

.form-title {
  font-family: var(--font-display);
  font-size: var(--text-h2);
  font-weight: 700;
  line-height: var(--line-height-tight);
  color: var(--color-text-primary);
  margin-bottom: var(--space-2);
}

/* ── Field ── */
.field {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}

.field__label {
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-text-primary);
}

/* ── Input ── */
.input {
  width: 100%;
  height: var(--input-height);           /* 44px — touch target */
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  background: var(--color-surface);
  color: var(--color-text-primary);
  font-size: var(--text-body);           /* 1rem — prevents iOS zoom */
  padding-inline: var(--space-4);
  transition: border-color var(--duration-fast) var(--ease-smooth);
}

/* Error state: color + icon (not color alone) */
.input[aria-invalid="true"] {
  border-color: var(--color-error-text);
  background: var(--color-error-bg);
  /* Background-image icon provides non-color signal */
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='%23dc2626' stroke-width='2'%3E%3Ccircle cx='12' cy='12' r='10'/%3E%3Cline x1='12' y1='8' x2='12' y2='12'/%3E%3Cline x1='12' y1='16' x2='12.01' y2='16'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right var(--space-3) center;
  padding-inline-end: var(--space-10);
}

/* ── Error and hint text ── */
.field__error {
  font-size: var(--text-sm);
  color: var(--color-error-text);
  min-height: 1.5em;   /* reserve space — prevents CLS on error appear */
  display: flex;
  align-items: center;
  gap: var(--space-2);
}

.field__error:empty { display: none; }

.field__hint {
  font-size: var(--text-sm);
  color: var(--color-text-muted);
}

/* ── Checkbox ── */
.checkbox-label {
  display: flex;
  align-items: flex-start;
  gap: var(--space-3);
  font-size: var(--text-body);
  color: var(--color-text-primary);
  cursor: pointer;
  min-height: 44px;    /* touch target via label */
}

/* Visually hide native checkbox, keep it accessible */
.checkbox-native {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.checkbox-custom {
  flex-shrink: 0;
  width: 20px;
  height: 20px;
  border: 2px solid var(--color-border);
  border-radius: var(--radius-sm);
  background: var(--color-surface);
  transition:
    background     var(--duration-fast) var(--ease-smooth),
    border-color   var(--duration-fast) var(--ease-smooth);
  margin-top: 2px;
}

.checkbox-native:checked + .checkbox-custom {
  background: var(--color-accent);
  border-color: var(--color-accent);
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='14' height='14' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='3'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: center;
}

.checkbox-native:focus-visible + .checkbox-custom {
  outline: var(--focus-ring);
  outline-offset: var(--focus-ring-offset);
  border-radius: var(--radius-sm);
}

/* ── Submit button ── */
.btn-primary {
  width: 100%;
  height: var(--btn-height-md);          /* 44px */
  background: var(--color-accent);
  color: oklch(98% 0.005 258);
  border: none;
  border-radius: var(--radius-md);
  font-weight: var(--font-weight-semibold);
  font-size: var(--text-sm);
  cursor: pointer;
  transition:
    background  var(--duration-fast) var(--ease-smooth),
    opacity     var(--duration-fast) var(--ease-smooth);
}

.btn-primary:hover { background: var(--color-accent-dark); }

.btn-primary[aria-busy="true"] {
  opacity: 0.7;
  cursor: wait;
}

/* ── Link inside form ── */
.link {
  color: var(--color-accent);
  text-decoration: underline;
  text-decoration-color: oklch(from var(--color-accent) l c h / 0.4);
  text-underline-offset: 2px;
  transition: text-decoration-color var(--duration-fast) var(--ease-smooth);
}

.link:hover { text-decoration-color: var(--color-accent); }
```

```js
// form-validation.js
const form = document.querySelector('.signup-form')

function showError(input, message) {
  const errorEl = document.getElementById(input.getAttribute('aria-describedby').split(' ').find(id => id.endsWith('-error')))
  if (!errorEl) return
  input.setAttribute('aria-invalid', 'true')
  errorEl.textContent = message  // aria-live="assertive" announces this
}

function clearError(input) {
  const errorId = input.getAttribute('aria-describedby')?.split(' ').find(id => id.endsWith('-error'))
  const errorEl = errorId ? document.getElementById(errorId) : null
  input.removeAttribute('aria-invalid')
  if (errorEl) errorEl.textContent = ''
}

// Validate on blur — not on every keystroke
form.querySelectorAll('input:not([type="checkbox"])').forEach(input => {
  input.addEventListener('blur', () => {
    if (!input.value.trim()) {
      const label = form.querySelector(`label[for="${input.id}"]`)?.textContent
      showError(input, `${label || 'This field'} is required.`)
    } else {
      clearError(input)
    }
  })
})

form.addEventListener('submit', async (e) => {
  e.preventDefault()

  const btn = document.getElementById('submit-btn')
  btn.setAttribute('aria-busy', 'true')
  btn.textContent = 'Creating account...'

  try {
    // await submitToAPI(new FormData(form))
    btn.textContent = 'Account created!'
  } catch (err) {
    const formError = document.getElementById('form-error')
    formError.textContent = 'Something went wrong. Please try again.'  // aria-live announces
    btn.removeAttribute('aria-busy')
    btn.textContent = 'Create account'
  }
})
```

---

## What Changed and Why

**`<div>` submit → `<button type="submit">`**
A `<div>` is not in the tab order, doesn't respond to Enter/Space, and has no implicit role. `<button>` provides all of that by default. The first rule of ARIA: use a native element if one exists.

**Placeholder → persistent `<label>`**
Placeholder text disappears on focus. Users who return to a partially-filled form have no way to know what a field is for. Each `<label>` is connected via `for`/`id` — screen readers announce the label when the input receives focus.

**`outline: none` → `:focus-visible` global rule**
Removing focus outlines globally is the single most common accessibility violation in production code. `:focus-visible` preserves keyboard navigation rings while suppressing them for mouse clicks.

**Custom `<div>` checkbox → native `<input type="checkbox">` + CSS overlay**
A native checkbox is keyboard-operable, has the correct implicit role, toggles on Space, participates in form submission, and works with `<label>`. The CSS overlay technique gives full visual control without losing any of that behavior.

**`color: red` error → border-color + background + icon + `aria-live`**
Red alone is invisible to ~8% of men with color blindness. Three non-color signals are added: border color, background tint, and an inline SVG icon. The `aria-live="assertive"` region announces the error to screen reader users immediately when it appears.

**`font-size: 13px` → `var(--text-body)` (1rem)**
iOS Safari auto-zooms any focused input with font-size below 16px. This breaks the page layout and disorients the user. 1rem respects the user's browser default and prevents the zoom.

**CLS on error appearance → `min-height: 1.5em` on error container**
When an error message appears below a field, it pushes content down — that's CLS. Reserving the space before the error loads prevents the shift.

---

*Example 03 — `examples/03-form-accessibility.md`*
*Related: `rules/07-accessibility.md`, `recipes/improve-forms.md`, `rules/04-color.md` R7, `checklists/ui-review.md` §2*
