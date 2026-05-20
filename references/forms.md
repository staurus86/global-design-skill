# Reference — Forms

> Form anatomy, input states, validation patterns, React 19 form actions, and every edge case. Forms are the highest-stakes UX: errors cost conversions, poor validation causes frustration.

---

## Field Anatomy

Every form field has 5 parts: label + input + hint + error + success.

```html
<div class="field" data-state="idle">
  <!-- 1. Label — always visible, always linked -->
  <label for="email" class="field-label">
    Email address
    <span class="field-required" aria-hidden="true">*</span>
  </label>

  <!-- 2. Input wrapper — contains input + optional icons -->
  <div class="field-input-wrapper">
    <input
      type="email"
      id="email"
      name="email"
      class="field-input"
      autocomplete="email"
      required
      aria-describedby="email-hint email-error"
      aria-invalid="false"
    />
    <!-- Optional: leading icon, trailing action -->
  </div>

  <!-- 3. Hint — always visible when present -->
  <p id="email-hint" class="field-hint">
    We'll send your receipt here.
  </p>

  <!-- 4. Error — shown on validation failure -->
  <p id="email-error" class="field-error" role="alert" aria-live="polite" hidden>
    <!-- populated by JS -->
  </p>

  <!-- 5. Success — shown after validation passes (optional) -->
  <p class="field-success" hidden>
    ✓ Looks good
  </p>
</div>
```

---

## Input States

All five states must be designed. Never ship a form with only the idle state.

```css
/* Base input styles */
.field-input {
  width: 100%;
  padding: var(--space-3) var(--space-4);
  background: var(--color-surface);
  border: 1.5px solid var(--color-border);
  border-radius: var(--radius-md);
  color: var(--color-text);
  font-size: var(--text-body);
  line-height: 1.5;
  transition:
    border-color var(--duration-fast) var(--ease-smooth),
    box-shadow   var(--duration-fast) var(--ease-smooth);
}

/* Placeholder */
.field-input::placeholder { color: var(--color-text-muted); }

/* Hover */
@media (hover: hover) {
  .field-input:hover {
    border-color: var(--color-text-2);
  }
}

/* Focus */
.field-input:focus-visible {
  outline: none;
  border-color: var(--color-accent);
  box-shadow: 0 0 0 3px oklch(from var(--color-accent) l c h / 0.15);
}

/* Error state */
.field[data-state="error"] .field-input {
  border-color: var(--color-error);
}
.field[data-state="error"] .field-input:focus-visible {
  box-shadow: 0 0 0 3px oklch(from var(--color-error) l c h / 0.15);
}

/* Success state */
.field[data-state="success"] .field-input {
  border-color: var(--color-success);
}

/* Disabled */
.field-input:disabled {
  background: var(--color-surface-2);
  color: var(--color-text-muted);
  cursor: not-allowed;
  opacity: 0.6;
}
```

---

## Validation Patterns

### Validate on blur, not on input

```ts
/* Wrong — validates while typing (annoying) */
input.addEventListener('input', validate)

/* Correct — validates after user leaves the field */
input.addEventListener('blur', validate)

/* Also validate on form submit */
form.addEventListener('submit', (e) => {
  e.preventDefault()
  const allValid = validateAll()
  if (allValid) submitForm()
})
```

### Error message formula

```
❌ "Invalid email"
✅ "Enter a valid email address — for example, name@company.com"

❌ "Required"
✅ "Email is required to send your receipt"

❌ "Password too short"
✅ "Password must be at least 8 characters. Try adding a number or symbol."
```

**Formula:** What's wrong + why it matters + how to fix it.

### Inline validation (React)

```tsx
import { useState } from 'react'

function EmailField() {
  const [value, setValue] = useState('')
  const [error, setError] = useState('')
  const [touched, setTouched] = useState(false)

  function validate(val: string) {
    if (!val) return 'Email is required to send your receipt'
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val)) {
      return 'Enter a valid email — for example, name@company.com'
    }
    return ''
  }

  return (
    <div className="field" data-state={touched && error ? 'error' : 'idle'}>
      <label htmlFor="email" className="field-label">Email address</label>
      <input
        type="email"
        id="email"
        value={value}
        onChange={e => setValue(e.target.value)}
        onBlur={() => {
          setTouched(true)
          setError(validate(value))
        }}
        aria-describedby={error ? 'email-error' : undefined}
        aria-invalid={touched && !!error}
        className="field-input"
      />
      {touched && error && (
        <p id="email-error" className="field-error" role="alert">
          {error}
        </p>
      )}
    </div>
  )
}
```

---

## React 19 Form Actions

React 19 introduces server actions and `useActionState` for forms. Use this pattern instead of manual state management.

```tsx
'use server'

async function submitContactForm(prevState: FormState, formData: FormData): Promise<FormState> {
  const email = formData.get('email') as string
  const message = formData.get('message') as string

  if (!email || !email.includes('@')) {
    return { error: 'Enter a valid email address', field: 'email' }
  }

  if (!message || message.length < 20) {
    return { error: 'Message must be at least 20 characters', field: 'message' }
  }

  await sendEmail({ email, message })
  return { success: true }
}
```

```tsx
'use client'

import { useActionState } from 'react'
import { useFormStatus } from 'react-dom'

function SubmitButton() {
  const { pending } = useFormStatus()
  return (
    <button type="submit" disabled={pending} className="btn-primary">
      {pending ? 'Sending...' : 'Send message'}
    </button>
  )
}

type FormState = { error?: string; field?: string; success?: boolean }

function ContactForm() {
  const [state, action] = useActionState(submitContactForm, {})

  if (state.success) {
    return (
      <div role="alert" className="form-success">
        <p>Message sent — we'll reply within 2 business days.</p>
      </div>
    )
  }

  return (
    <form action={action} noValidate>
      <div className="field" data-state={state.field === 'email' ? 'error' : 'idle'}>
        <label htmlFor="email">Email address</label>
        <input
          type="email"
          id="email"
          name="email"
          aria-describedby={state.field === 'email' ? 'email-error' : undefined}
          aria-invalid={state.field === 'email'}
        />
        {state.field === 'email' && (
          <p id="email-error" role="alert" className="field-error">
            {state.error}
          </p>
        )}
      </div>

      <div className="field" data-state={state.field === 'message' ? 'error' : 'idle'}>
        <label htmlFor="message">Message</label>
        <textarea id="message" name="message" rows={5} />
        {state.field === 'message' && (
          <p id="message-error" role="alert" className="field-error">
            {state.error}
          </p>
        )}
      </div>

      <SubmitButton />
    </form>
  )
}
```

---

## Select, Checkbox, Radio

```html
<!-- Select -->
<div class="field">
  <label for="plan" class="field-label">Billing plan</label>
  <div class="field-select-wrapper">
    <select id="plan" name="plan" class="field-select">
      <option value="">Choose a plan</option>
      <option value="starter">Starter — $9/mo</option>
      <option value="pro">Pro — $29/mo</option>
    </select>
    <svg class="field-select-arrow" aria-hidden="true"><!-- chevron --></svg>
  </div>
</div>

<!-- Checkbox group -->
<fieldset class="field-group">
  <legend class="field-group-label">Notify me about</legend>

  <label class="checkbox-label">
    <input type="checkbox" name="notify" value="deploys" class="checkbox" />
    <span class="checkbox-text">Deployments</span>
  </label>

  <label class="checkbox-label">
    <input type="checkbox" name="notify" value="errors" class="checkbox" />
    <span class="checkbox-text">Errors</span>
  </label>
</fieldset>

<!-- Radio group -->
<fieldset class="field-group">
  <legend class="field-group-label">Payment method</legend>

  <label class="radio-label">
    <input type="radio" name="payment" value="card" class="radio" />
    <span class="radio-text">Credit card</span>
  </label>

  <label class="radio-label">
    <input type="radio" name="payment" value="bank" class="radio" />
    <span class="radio-text">Bank transfer</span>
  </label>
</fieldset>
```

---

## Multi-Step Form

```tsx
type StepId = 'account' | 'profile' | 'plan' | 'confirm'

const steps: { id: StepId; label: string }[] = [
  { id: 'account',  label: 'Account' },
  { id: 'profile',  label: 'Profile' },
  { id: 'plan',     label: 'Plan' },
  { id: 'confirm',  label: 'Confirm' },
]

function MultiStepForm() {
  const [currentStep, setCurrentStep] = useState<StepId>('account')
  const currentIndex = steps.findIndex(s => s.id === currentStep)

  return (
    <div>
      {/* Step indicator */}
      <nav aria-label="Form progress">
        <ol className="step-list">
          {steps.map((step, i) => (
            <li
              key={step.id}
              className="step"
              aria-current={step.id === currentStep ? 'step' : undefined}
            >
              <span className={`step-number ${i < currentIndex ? 'complete' : ''}`}>
                {i < currentIndex ? '✓' : i + 1}
              </span>
              <span className="step-label">{step.label}</span>
            </li>
          ))}
        </ol>
      </nav>

      {/* Step content */}
      <div role="region" aria-label={`Step ${currentIndex + 1} of ${steps.length}: ${steps[currentIndex].label}`}>
        {currentStep === 'account'  && <AccountStep />}
        {currentStep === 'profile'  && <ProfileStep />}
        {currentStep === 'plan'     && <PlanStep />}
        {currentStep === 'confirm'  && <ConfirmStep />}
      </div>

      {/* Navigation */}
      <div className="step-nav">
        {currentIndex > 0 && (
          <button type="button" onClick={() => setCurrentStep(steps[currentIndex - 1].id)}>
            Back
          </button>
        )}
        <button type="button" onClick={() => setCurrentStep(steps[currentIndex + 1].id)}>
          {currentIndex < steps.length - 1 ? 'Continue' : 'Finish'}
        </button>
      </div>
    </div>
  )
}
```

---

## Form Checklist

```
[ ] Every input has a visible <label> linked with for/id
[ ] Placeholder is a hint — never a replacement for label
[ ] All 5 states designed: idle, hover, focus, error, disabled
[ ] Errors shown after blur (not while typing)
[ ] Error message formula: what's wrong + why + how to fix
[ ] Error messages have role="alert" and aria-live="polite"
[ ] aria-invalid set to true on fields with errors
[ ] Submit button disabled (with pending state) during submission
[ ] Success state designed — what happens after successful submit
[ ] Autocomplete attributes set (email, name, tel, etc.)
[ ] Radio/checkbox groups wrapped in <fieldset> + <legend>
[ ] Touch targets: inputs ≥ 44px height on mobile
[ ] Keyboard: Tab to move between fields, Enter to submit
```

---

*Reference version: global-design-skill v1.0 — `references/forms.md`*
*Related: `rules/10-forms-and-inputs.md`, `patterns/product-ui/forms.md`, `references/accessibility.md`*
