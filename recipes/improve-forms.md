# Recipe — Improve Forms

> Every extra field costs you conversions. Every confusing error message costs you trust. Every missing feedback state costs you completion. Forms are the highest-friction surface in any UI — fix them surgically.

---

## When to use

- Form completion rate < 70%
- Users abandon after the first error
- Support tickets about "I don't know what went wrong"
- Forms look fine but feel bad to fill out
- Error messages say "Invalid input" or "Error occurred"

---

## Diagnosis: Form Failure Modes

```
[ ] Placeholder text used as label (label disappears on focus)
[ ] Error messages: "Invalid", "Required", "Error" — no context
[ ] Error messages appear only on final submit (not on field blur)
[ ] Fields reset to empty after failed submission
[ ] Submit button doesn't change during loading
[ ] No keyboard navigation between fields (wrong tabindex)
[ ] Required fields marked only with red border (color alone)
[ ] Password requirements shown only after error
[ ] "Please" prefix on every label (unnecessary)
[ ] Too many fields for the goal (more than 5 fields on sign-up)
[ ] No success feedback after submission
[ ] Mobile: inputs too small (< 44px height)
```

---

## Step 1 — Audit Required Fields

Every field costs conversions. Remove any field that:
- Can be collected after sign-up
- Can be inferred from other data
- Is "nice to have" for marketing, not product necessity

**Sign-up forms: maximum 3 fields**
```
Email + Password + [one more: Name or Company] → that's it
Phone, job title, team size, referral source → collect after activation
```

**Contact forms: maximum 4 fields**
```
Name + Email + Message + [optional: subject or company]
Phone + Fax + Address → remove unless legally required
```

---

## Step 2 — Fix Labels

Labels must always be visible. Placeholder is not a label.

**Before (wrong — placeholder as label):**
```html
<input type="email" placeholder="Email address" />
```

**After (correct — visible label + example placeholder):**
```html
<div class="field">
  <label for="email" class="field__label">
    Email address
    <span class="field__required" aria-hidden="true">*</span>
  </label>
  <input
    type="email"
    id="email"
    name="email"
    class="field__input"
    placeholder="you@company.com"
    autocomplete="email"
    required
    aria-required="true"
    aria-describedby="email-hint"
  />
  <p id="email-hint" class="field__hint">
    We'll send your confirmation here.
  </p>
</div>
```

```css
.field {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}

.field__label {
  font-size: 0.9375rem;
  font-weight: 500;
  color: var(--color-text-primary);
  display: flex;
  align-items: center;
  gap: var(--space-1);
}

.field__required {
  color: var(--color-error);
  font-size: 0.875rem;
}

.field__input {
  height: 44px;           /* minimum touch target */
  padding-inline: var(--space-4);
  background: var(--color-surface-2);
  border: 1.5px solid var(--color-border);
  border-radius: var(--radius-md);
  font-size: 1rem;        /* prevents iOS zoom on focus */
  color: var(--color-text-primary);
  width: 100%;
  outline: none;
  transition: border-color 150ms, background 150ms, box-shadow 150ms;
}

.field__input::placeholder {
  color: var(--color-text-muted);
  opacity: 0.7;
}

.field__input:focus {
  border-color: var(--color-accent);
  background: var(--color-surface);
  box-shadow: 0 0 0 3px oklch(from var(--color-accent) l c h / 0.15);
}

.field__hint {
  font-size: 0.8125rem;
  color: var(--color-text-muted);
  line-height: 1.4;
}
```

---

## Step 3 — Fix Error Messages

**The formula:** `[Field name]: [What's wrong] — [How to fix]`

| Before (bad) | After (specific) |
|---|---|
| "Invalid email" | "Email: this doesn't look like an email address — check for missing @ or .com" |
| "Required field" | "Password: required to create your account" |
| "Password too short" | "Password: must be at least 8 characters — you entered 5" |
| "Error" | "We couldn't save your changes — the server is temporarily unavailable. Try again in 30 seconds." |
| "Invalid input" | "Phone: enter a number with country code, e.g. +1 555 000 0000" |

**Error state implementation:**
```html
<div class="field field--error">
  <label for="email" class="field__label">Email address</label>
  <input
    type="email"
    id="email"
    class="field__input"
    value="user@"
    aria-invalid="true"
    aria-describedby="email-error"
  />
  <p id="email-error" class="field__error" role="alert">
    Email: this doesn't look right — check for missing domain (e.g., .com)
  </p>
</div>
```

```css
.field--error .field__input {
  border-color: var(--color-error);
  background: oklch(from var(--color-error) l c h / 0.04);
}

.field--error .field__input:focus {
  box-shadow: 0 0 0 3px oklch(from var(--color-error) l c h / 0.15);
}

.field__error {
  font-size: 0.8125rem;
  color: var(--color-error);
  display: flex;
  align-items: flex-start;
  gap: var(--space-1);
  line-height: 1.4;

  /* Animate in */
  animation: error-enter 200ms cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes error-enter {
  from { opacity: 0; transform: translateY(-4px); }
  to   { opacity: 1; transform: translateY(0); }
}
```

**Validate on blur (not on every keystroke, not only on submit):**
```js
document.querySelectorAll('.field__input').forEach(input => {
  input.addEventListener('blur', () => validateField(input))
})

function validateField(input) {
  const field = input.closest('.field')
  const errorId = `${input.id}-error`

  const error = getValidationError(input)

  if (error) {
    input.setAttribute('aria-invalid', 'true')
    input.setAttribute('aria-describedby', errorId)
    field.classList.add('field--error')

    let errorEl = document.getElementById(errorId)
    if (!errorEl) {
      errorEl = document.createElement('p')
      errorEl.id = errorId
      errorEl.className = 'field__error'
      errorEl.setAttribute('role', 'alert')
      field.append(errorEl)
    }
    errorEl.textContent = error

  } else {
    input.removeAttribute('aria-invalid')
    field.classList.remove('field--error')
    document.getElementById(errorId)?.remove()
  }
}
```

---

## Step 4 — Loading & Success States on Submit

**Before (nothing happens for 2 seconds):**
```html
<button type="submit">Submit</button>
```

**After (immediate feedback):**
```html
<button type="submit" class="btn-primary btn-submit" id="submit-btn">
  <span class="btn-submit__label">Create account</span>
  <span class="btn-submit__spinner" aria-hidden="true" hidden></span>
</button>
```

```js
form.addEventListener('submit', async (e) => {
  e.preventDefault()

  const btn = document.getElementById('submit-btn')
  const label = btn.querySelector('.btn-submit__label')
  const spinner = btn.querySelector('.btn-submit__spinner')

  // Loading state
  btn.disabled = true
  btn.setAttribute('aria-busy', 'true')
  label.textContent = 'Creating account…'
  spinner.hidden = false

  try {
    await submitForm(new FormData(form))
    // Success state
    label.textContent = 'Account created!'
    btn.classList.add('btn-submit--success')
    // Redirect or show success message
  } catch (error) {
    // Error state: restore button
    btn.disabled = false
    btn.setAttribute('aria-busy', 'false')
    label.textContent = 'Create account'
    spinner.hidden = true
    // Show form-level error
    showFormError(error.message)
  }
})
```

```css
.btn-submit {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-2);
}

.btn-submit__spinner {
  width: 16px;
  height: 16px;
  border: 2px solid currentColor;
  border-top-color: transparent;
  border-radius: 50%;
  animation: spin 600ms linear infinite;
}

@keyframes spin { to { transform: rotate(360deg); } }

.btn-submit--success { background: var(--color-success); }
```

---

## Step 5 — Show Password Requirements Before Error

```html
<div class="field">
  <label for="password" class="field__label">Password</label>
  <div class="field__input-wrap">
    <input
      type="password"
      id="password"
      class="field__input"
      aria-describedby="password-reqs"
    />
    <button type="button" class="field__toggle-pw" aria-label="Show password">
      <!-- Eye icon -->
    </button>
  </div>

  <!-- Requirements: always visible, check off as user types -->
  <ul id="password-reqs" class="pw-requirements">
    <li class="pw-req" data-rule="length">At least 8 characters</li>
    <li class="pw-req" data-rule="uppercase">One uppercase letter</li>
    <li class="pw-req" data-rule="number">One number</li>
  </ul>
</div>
```

```css
.pw-requirements {
  list-style: none;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: var(--space-1);
  font-size: 0.8125rem;
}

.pw-req {
  color: var(--color-text-muted);
  display: flex;
  align-items: center;
  gap: var(--space-2);
  transition: color 200ms;
}

.pw-req::before {
  content: '○';
  font-size: 0.6rem;
  color: var(--color-text-muted);
  transition: color 200ms;
}

.pw-req--met { color: var(--color-success); }
.pw-req--met::before { content: '●'; color: var(--color-success); }
```

---

## Step 6 — Never Reset Fields on Error

```js
// WRONG — resets entire form
form.reset()

// CORRECT — mark error, keep values, focus first error
function handleFormError(errors) {
  const firstError = Object.keys(errors)[0]
  const firstInput = document.getElementById(firstError)

  Object.entries(errors).forEach(([fieldId, message]) => {
    const input = document.getElementById(fieldId)
    markFieldError(input, message)  // show error, keep value
  })

  firstInput?.focus()  // move focus to first error
}
```

---

## Step 7 — Keyboard Navigation

```html
<!-- Correct tabindex order: labels → inputs → submit -->
<!-- Never use positive tabindex values — use DOM order instead -->

<form>
  <div class="field">
    <label for="name">Name</label>
    <input type="text" id="name" name="name" />
  </div>
  <div class="field">
    <label for="email">Email</label>
    <input type="email" id="email" name="email" />
  </div>
  <button type="submit">Create account</button>
</form>
```

**Additional keyboard improvements:**
- `Enter` in any text input should submit single-field forms
- `Tab` from last field should reach the submit button
- No `tabindex="-1"` on form fields (removes them from keyboard navigation)
- No `tabindex="2"` or higher (disrupts natural order)

---

## Complete Field Component — All States

```html
<!-- Idle -->
<div class="field">
  <label for="email" class="field__label">Work email <span aria-hidden="true">*</span></label>
  <input type="email" id="email" class="field__input" placeholder="you@company.com" autocomplete="email" />
  <p class="field__hint">We'll send your confirmation here</p>
</div>

<!-- Focus (via CSS :focus) -->

<!-- Error -->
<div class="field field--error">
  <label for="email" class="field__label">Work email <span aria-hidden="true">*</span></label>
  <input type="email" id="email" class="field__input" aria-invalid="true" aria-describedby="email-error" value="user@" />
  <p id="email-error" class="field__error" role="alert">Email: missing domain — try "user@company.com"</p>
</div>

<!-- Success / valid -->
<div class="field field--valid">
  <label for="email" class="field__label">Work email <span aria-hidden="true">*</span></label>
  <input type="email" id="email" class="field__input" value="user@company.com" />
  <span class="field__valid-icon" aria-hidden="true">✓</span>
</div>
```

---

## Acceptance Criteria

```
[ ] All inputs have visible, persistent labels (no placeholder-as-label)
[ ] Errors validate on blur — not on every keystroke, not only on submit
[ ] Error message follows [Field]: [Problem] — [Fix] formula
[ ] Fields retain their values on failed form submission
[ ] Submit button shows loading state ("Saving…" + spinner) during async
[ ] Submit button disabled during loading, re-enabled on error
[ ] Password requirements visible before first attempt
[ ] Form inputs ≥ 44px height (touch target)
[ ] Font-size ≥ 16px in inputs (prevents iOS zoom)
[ ] Tab order follows visual reading order
[ ] aria-invalid + aria-describedby wired to error messages
[ ] Success state shown after successful submission
[ ] No form fields reset on server error
```

---

*Recipe version: global-design-skill v1.0 — `recipes/improve-forms.md`*
*Related: `rules/06-components.md`, `patterns/product-ui/error-states.md`, `templates/specs/frontend-tz.md`*
