# Rule — Forms

> Forms are the highest-stakes UI component. They are where users give you their data, their money, and their trust. A form that's confusing, unreliable, or inaccessible destroys conversion and credibility simultaneously. These rules encode the gap between a form that looks correct and a form that actually works.

---

## R1 — Minimum viable field count. Ask only what you need right now.

Every additional field reduces completion rate. Research consistently shows that reducing from 11 fields to 4 improves signup conversion by 120%. Ask the minimum required to complete the current step. Get the rest later, when the user is invested.

```
Sign-up: Email + Password only (name, phone, company → after they're in)
Checkout step 1: Email only (shipping, billing → next step)
Profile: Required fields only with "Add later" links for optional

Never ask for:
  - Phone number unless you will call/text them
  - Company name unless B2B and required for billing
  - "How did you hear about us" on the sign-up form (use analytics)
  - Date of birth unless legally required
  - Gender unless essential to the product
```

**The audit question:** "If a user refuses to fill this field, do we block them?" If no — remove it from the required set.

---

## R2 — Validate on blur, not on change. Never on submit alone.

Validating on every keystroke (change) interrupts typing and shows errors before the user has finished. Validating only on submit leaves the user with a list of errors to hunt through. Blur-on-exit is the correct moment — the user has finished with that field.

```js
// Correct — validate when user leaves the field
input.addEventListener('blur', () => validateField(input))

// Correct — clear error when user starts fixing it
input.addEventListener('input', () => {
  if (input.getAttribute('aria-invalid') === 'true') {
    clearError(input)
  }
})

// Wrong — validates on every keystroke
input.addEventListener('input', () => validateField(input))

// Wrong — only validates on submit (user fills whole form before seeing errors)
form.addEventListener('submit', () => validateAll())
```

```js
function validateField(input) {
  const value = input.value.trim()
  const type = input.type
  let error = ''

  if (input.required && !value) {
    const label = document.querySelector(`label[for="${input.id}"]`)?.textContent ?? 'This field'
    error = `${label} is required.`
  } else if (type === 'email' && value && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)) {
    error = `Enter a valid email address — for example, name@company.com`
  }

  if (error) {
    showError(input, error)
  } else {
    clearError(input)
  }
}
```

---

## R3 — Error messages: say what happened and what to do. Never blame.

Generic errors ("Invalid input") tell the user nothing. The error message must answer two questions: what's wrong, and how to fix it.

**The formula:** [What the system detected] — [what to do instead]

```
Wrong:  "Invalid email"
Wrong:  "Please enter a valid email address"
Wrong:  "Email is incorrect"
Correct: "Email is missing the @ symbol — try name@company.com"

Wrong:  "Password is too weak"
Correct: "Password needs at least one number — try adding 1 to the end"

Wrong:  "Error processing payment"
Correct: "Card declined — check the card number and try again, or use a different card"

Wrong:  "Invalid date"
Correct: "Enter a date in MM/DD/YYYY format — for example, 03/15/1990"

Wrong:  "This field is required"
Correct: "Email address is required to create your account"
```

**Never use:** "Invalid", "Incorrect", "Wrong", "Bad", "Error" as standalone messages. Always say what specifically failed.

---

## R4 — Never reset field values on failed submission.

When a form fails (validation error, network error, server error), keep the user's input. Re-filling a form after losing progress is the highest-friction experience in web UI. Users abandon rather than retype.

```js
// Wrong — clears form on error
async function handleSubmit(e) {
  e.preventDefault()
  try {
    await api.submit(formData)
  } catch (err) {
    form.reset()  // destroys all user input
    showError(err.message)
  }
}

// Correct — preserve input, show error in place
async function handleSubmit(e) {
  e.preventDefault()
  const btn = form.querySelector('[type="submit"]')
  btn.setAttribute('aria-busy', 'true')
  btn.textContent = 'Saving...'

  try {
    await api.submit(new FormData(form))
    showSuccess()
  } catch (err) {
    // Input is preserved — only the error message updates
    document.getElementById('form-error').textContent =
      'Could not save your changes. Check your connection and try again.'
    btn.removeAttribute('aria-busy')
    btn.textContent = 'Save changes'
  }
}
```

---

## R5 — Multi-step forms: show progress, allow back navigation, validate per step.

Long forms broken into steps complete at higher rates than single long forms. Each step should have one clear goal and never ask for data used in a previous step again.

```html
<!-- Progress indicator -->
<nav class="form-progress" aria-label="Form progress">
  <ol class="form-progress__steps">
    <li class="form-progress__step form-progress__step--done"  aria-label="Step 1: Account — completed">
      <span class="step-dot" aria-hidden="true">✓</span>
      <span>Account</span>
    </li>
    <li class="form-progress__step form-progress__step--active" aria-current="step" aria-label="Step 2: Details — current">
      <span class="step-dot" aria-hidden="true">2</span>
      <span>Details</span>
    </li>
    <li class="form-progress__step" aria-label="Step 3: Payment — not started">
      <span class="step-dot" aria-hidden="true">3</span>
      <span>Payment</span>
    </li>
  </ol>
</nav>
```

```css
.form-progress__steps {
  display: flex;
  align-items: center;
  gap: var(--space-4);
  list-style: none;
  padding: 0;
}

.form-progress__step {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  font-size: var(--text-sm);
  color: var(--color-text-muted);
}

.form-progress__step--done  { color: var(--color-success-text); }
.form-progress__step--active { color: var(--color-text-primary); font-weight: var(--font-weight-medium); }

.step-dot {
  width: 24px;
  height: 24px;
  border-radius: var(--radius-full);
  border: 2px solid currentColor;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: var(--text-3xs);
  font-weight: var(--font-weight-bold);
}

.form-progress__step--done .step-dot {
  background: var(--color-success-text);
  border-color: var(--color-success-text);
  color: var(--color-success-bg);
}
```

**Back navigation rules:**
- Always show a "Back" button on steps 2+
- Back must not lose data from the current step
- Back should not re-validate the current step on exit
- URL should update per step so browser Back button works

---

## R6 — `autocomplete` attributes on every relevant input.

Browsers and password managers autofill inputs when `autocomplete` is set correctly. Missing it forces users to manually type common information — name, address, card number — every time.

```html
<!-- Sign in -->
<input type="email"    autocomplete="email" />
<input type="password" autocomplete="current-password" />

<!-- Sign up -->
<input type="text"     autocomplete="name" />
<input type="email"    autocomplete="email" />
<input type="password" autocomplete="new-password" />

<!-- Checkout / billing -->
<input type="text"   autocomplete="cc-name" />
<input type="text"   autocomplete="cc-number" />
<input type="text"   autocomplete="cc-exp" />
<input type="text"   autocomplete="cc-csc" />

<!-- Shipping address -->
<input type="text"   autocomplete="shipping address-line1" />
<input type="text"   autocomplete="shipping address-line2" />
<input type="text"   autocomplete="shipping address-level2" />  <!-- city -->
<input type="text"   autocomplete="shipping postal-code" />
<select              autocomplete="shipping country" ></select>

<!-- Disable autofill for specific fields (OTP, security codes) -->
<input type="text" autocomplete="one-time-code" inputmode="numeric" pattern="[0-9]*" />
```

---

## R7 — `inputmode` for the right keyboard on mobile.

`type="text"` always shows the alphabetic keyboard. `inputmode` tells the OS which keyboard to display without changing validation behavior.

```html
<!-- Shows numeric keypad -->
<input type="text" inputmode="numeric"  pattern="[0-9]*"    placeholder="ZIP code" />
<input type="text" inputmode="numeric"  pattern="[0-9]*"    placeholder="PIN" />

<!-- Shows telephone keypad -->
<input type="tel"  inputmode="tel"                          placeholder="+1 (555) 000-0000" />

<!-- Shows email keyboard (@ key prominent) -->
<input type="email" inputmode="email"                       placeholder="name@company.com" />

<!-- Shows URL keyboard (. / keys prominent) -->
<input type="url"   inputmode="url"                         placeholder="https://" />

<!-- Shows decimal keyboard (. key) -->
<input type="text"  inputmode="decimal"                     placeholder="0.00" />
```

---

## R8 — Conditional fields: show/hide with transition, never collapse to 0 height instantly.

Fields that appear or disappear based on previous answers must animate smoothly. Instant appearance causes CLS and disorientation.

```html
<div class="field">
  <label class="checkbox-label">
    <input type="checkbox" id="has-company" name="has_company" />
    <span>I'm signing up for a company</span>
  </label>
</div>

<!-- Conditional field: shown when checkbox checked -->
<div class="conditional-field" id="company-fields" hidden>
  <div class="field">
    <label for="company-name">Company name</label>
    <input type="text" id="company-name" name="company_name" autocomplete="organization" />
  </div>
</div>
```

```css
.conditional-field {
  display: grid;
  grid-template-rows: 0fr;
  opacity: 0;
  transition:
    grid-template-rows var(--duration-moderate) var(--ease-spring),
    opacity            var(--duration-moderate) var(--ease-spring);
}

.conditional-field > * {
  overflow: hidden;
}

.conditional-field:not([hidden]) {
  grid-template-rows: 1fr;
  opacity: 1;
}

/* prefers-reduced-motion */
@media (prefers-reduced-motion: reduce) {
  .conditional-field { transition: opacity var(--duration-fast); }
}
```

```js
document.getElementById('has-company').addEventListener('change', e => {
  const fields = document.getElementById('company-fields')
  if (e.target.checked) {
    fields.removeAttribute('hidden')
    // Focus first field in the revealed section
    fields.querySelector('input')?.focus()
  } else {
    fields.setAttribute('hidden', '')
    // Clear values when hiding — don't submit hidden data
    fields.querySelectorAll('input, select, textarea').forEach(el => el.value = '')
  }
})
```

---

## R9 — Password fields: always show/hide toggle. Show requirements inline.

Users make fewer password errors when they can verify what they typed. Requirement checklists that update in real time prevent submit-and-fail cycles.

```html
<div class="field">
  <label for="password">Password</label>
  <div class="input-group">
    <input
      type="password"
      id="password"
      autocomplete="new-password"
      aria-describedby="password-requirements"
    />
    <button type="button" class="input-toggle" aria-label="Show password" aria-pressed="false">
      <svg class="icon-eye" aria-hidden="true" ...></svg>
      <svg class="icon-eye-off" aria-hidden="true" ...></svg>
    </button>
  </div>

  <ul class="password-requirements" id="password-requirements" aria-live="polite">
    <li class="req" data-req="length">At least 8 characters</li>
    <li class="req" data-req="uppercase">One uppercase letter</li>
    <li class="req" data-req="number">One number</li>
  </ul>
</div>
```

```css
.req { color: var(--color-text-muted); font-size: var(--text-sm); }
.req::before { content: '○ '; }
.req.met { color: var(--color-success-text); }
.req.met::before { content: '● '; }
```

```js
const toggle = document.querySelector('.input-toggle')
const input  = document.getElementById('password')
const reqs   = { length: v => v.length >= 8, uppercase: v => /[A-Z]/.test(v), number: v => /\d/.test(v) }

toggle.addEventListener('click', () => {
  const showing = input.type === 'text'
  input.type = showing ? 'password' : 'text'
  toggle.setAttribute('aria-pressed', String(!showing))
  toggle.setAttribute('aria-label', showing ? 'Show password' : 'Hide password')
})

input.addEventListener('input', () => {
  Object.entries(reqs).forEach(([key, test]) => {
    document.querySelector(`[data-req="${key}"]`)?.classList.toggle('met', test(input.value))
  })
})
```

---

## R10 — Success state is a destination, not a toast.

After a successful form submission, the page must clearly communicate completion. A small toast that disappears in 3 seconds is not enough for high-stakes actions (order placed, account created, payment processed).

```
Low stakes (feedback form, newsletter):    Toast notification — "Message sent"
Medium stakes (profile update, settings):  Inline confirmation replacing the form
High stakes (order, payment, signup):      Dedicated success state or page

Success state must:
  - Confirm exactly what was done (not just "Success!")
  - Tell the user what happens next
  - Provide a clear path forward (CTA or navigation)
  - Be accessible — not only visual
```

```html
<!-- High-stakes success: replaces the form -->
<div class="success-state" role="status" aria-live="polite">
  <div class="success-icon" aria-hidden="true">
    <svg ...><!-- checkmark --></svg>
  </div>
  <h2>Account created</h2>
  <p>
    We sent a confirmation to <strong>{{ email }}</strong>.
    Check your inbox to activate your account.
  </p>
  <p class="success-next">Didn't receive it? <button type="button" class="link">Resend email</button></p>
</div>
```

---

## Form Acceptance Criteria

```
[ ] Field count: only required fields present — optional fields deferred
[ ] Validation: fires on blur, clears on input (if field was invalid)
[ ] Error messages: specify what failed and what to do
[ ] Field values preserved on failed submission
[ ] autocomplete attributes on every relevant input
[ ] inputmode set for numeric, phone, email, URL inputs
[ ] Mobile: virtual keyboard doesn't cover active input
[ ] Multi-step: progress indicator + back navigation works
[ ] Conditional fields: animate in/out, hidden fields cleared on hide
[ ] Password: show/hide toggle + live requirements checklist
[ ] Submit button: shows loading state + prevents double-submit
[ ] Success: dedicated state for high-stakes submissions
[ ] All inputs: <label> with for/id, aria-describedby for hints/errors
[ ] All inputs: ≥ 1rem font-size (prevents iOS zoom)
[ ] All interactive elements: keyboard accessible
```

---

*Rule version: global-design-skill v1.0 — `rules/10-forms.md`*
*Related: `rules/07-accessibility.md` R3, `rules/04-color.md` R7, `recipes/improve-forms.md`, `examples/03-form-accessibility.md`, `checklists/ui-review.md` §2*
