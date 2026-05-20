# Pattern — Error States

> Errors are inevitable. How the product handles them determines whether users trust it. Every error state has three jobs: explain what failed, tell the user why, and give them exactly one recovery action.

---

## Error Taxonomy

| Type | Cause | Location | Recovery |
|---|---|---|---|
| **Field validation** | User input doesn't match requirements | Below input field | User corrects field |
| **Form submission** | Server rejected the form | Above submit button | User corrects and resubmits |
| **Network / timeout** | Connection dropped, request timed out | Inline or toast | Retry button |
| **Server error (5xx)** | Internal failure, not user's fault | Inline or full page | Contact support or retry later |
| **Not found (404)** | URL doesn't exist or resource deleted | Full page | Navigate elsewhere |
| **Permission denied (403)** | User lacks access | Inline or full page | Request access |
| **Session expired** | Auth token expired | Modal (blocking) | Re-login |
| **Rate limited** | Too many requests | Toast + inline | Wait and retry |
| **Conflict** | Data changed while user was editing | Inline | Resolve or reload |

---

## Pattern A — Field Validation Error

Trigger: user blurs a field with invalid input, or submits a form with validation errors.

```html
<div class="field field--error">
  <label for="email">
    Email <span aria-hidden="true">*</span>
  </label>
  <input
    id="email"
    type="email"
    name="email"
    value="notanemail"
    aria-invalid="true"
    aria-describedby="email-error"
  />
  <span
    id="email-error"
    class="field-error"
    role="alert"
  >
    Enter a valid email address — for example, name@company.com
  </span>
</div>
```

```css
.field--error input,
.field--error textarea,
.field--error select {
  border-color: var(--color-error);
  background: oklch(from var(--color-error) l c h / 0.04);
}

.field--error input:focus-visible {
  outline-color: var(--color-error);
}

.field-error {
  display: block;
  margin-top: var(--space-2);
  font-size: 0.875rem;
  color: var(--color-error);
  line-height: 1.4;
}

/* Animate in — subtle, not distracting */
.field-error {
  animation: error-in 150ms ease-out;
}

@keyframes error-in {
  from { opacity: 0; transform: translateY(-4px); }
  to   { opacity: 1; transform: translateY(0); }
}
```

**Validation timing:**
- Validate on blur (field loses focus), not on every keystroke
- Show errors on submit for required fields not yet touched
- Clear errors as user corrects the field (validate on input after first blur)

---

## Pattern B — Form Submission Error

Trigger: form submit fails — server rejects, network drops, conflict occurs.

```html
<form action="/signup" method="POST">
  <!-- Server error banner: above fields, below the form title -->
  <div class="form-error-banner" role="alert" aria-live="assertive">
    <span class="form-error-banner__icon" aria-hidden="true">⚠</span>
    <div>
      <strong>Couldn't create your account</strong>
      <p>This email is already registered. <a href="/login">Sign in instead</a> or use a different email.</p>
    </div>
  </div>

  <!-- Fields remain filled — don't reset on error -->
  <div class="field">
    <label for="email">Email</label>
    <input id="email" type="email" value="user@example.com" aria-invalid="true" aria-describedby="email-server-error" />
    <span id="email-server-error" class="field-error">This email is already in use.</span>
  </div>

  <button type="submit" class="btn-primary">Create account</button>
</form>
```

```css
.form-error-banner {
  display: flex;
  gap: var(--space-3);
  align-items: flex-start;
  background: oklch(from var(--color-error) l c h / 0.08);
  border: 1px solid oklch(from var(--color-error) l c h / 0.3);
  border-radius: var(--radius-lg);
  padding: var(--space-4);
  margin-bottom: var(--space-6);
  font-size: 0.9375rem;
}

.form-error-banner__icon {
  color: var(--color-error);
  font-size: 1.125rem;
  flex-shrink: 0;
  margin-top: 1px;
}

.form-error-banner p {
  margin-top: var(--space-1);
  color: var(--color-text-secondary);
}
```

**Rules:**
- Never reset form fields on submit error
- Scroll to the error banner on server error
- Never lose user's input — if the server errors, the form should stay filled

```tsx
// React: focus the error banner on appearance
useEffect(() => {
  if (serverError) {
    errorBannerRef.current?.focus()
  }
}, [serverError])
```

---

## Pattern C — Network / Retry Error

Trigger: network connection dropped, request timed out, service temporarily unavailable.

```html
<!-- Inline variant — for data-fetching sections -->
<div class="error-inline" role="alert">
  <span class="error-inline__icon" aria-hidden="true">⚡</span>
  <div class="error-inline__content">
    <strong>Couldn't load your projects</strong>
    <p>Check your internet connection and try again.</p>
    <button class="btn-ghost btn-sm" onclick="retryLoad()">
      Try again
    </button>
  </div>
</div>
```

```css
.error-inline {
  display: flex;
  gap: var(--space-4);
  align-items: flex-start;
  padding: var(--space-5);
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  border-left: 3px solid var(--color-error);
}

.error-inline__icon {
  font-size: 1.25rem;
  color: var(--color-error);
  flex-shrink: 0;
}

.error-inline__content strong {
  display: block;
  margin-bottom: var(--space-1);
}

.error-inline__content p {
  font-size: 0.9375rem;
  color: var(--color-text-secondary);
  margin-bottom: var(--space-4);
}
```

---

## Pattern D — Toast Error (non-blocking, transient)

Trigger: action failed but user can continue (save failed, export failed, non-critical operation).

```html
<div
  class="toast toast--error"
  role="alert"
  aria-live="assertive"
  aria-atomic="true"
>
  <span class="toast__icon" aria-hidden="true">✕</span>
  <div class="toast__content">
    <strong>Export failed</strong>
    <p>The selected date range exceeds 90 days. Select a shorter range.</p>
  </div>
  <button
    class="toast__close"
    aria-label="Dismiss notification"
    onclick="this.closest('.toast').remove()"
  >×</button>
</div>
```

```css
.toast {
  position: fixed;
  top: var(--space-4);
  right: var(--space-4);
  z-index: var(--z-toast);
  display: flex;
  align-items: flex-start;
  gap: var(--space-3);
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: var(--space-4) var(--space-5);
  max-width: 380px;
  box-shadow: 0 8px 32px oklch(0% 0 0 / 0.25);

  /* Animate in */
  animation: toast-in 250ms cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes toast-in {
  from { opacity: 0; transform: translateY(-12px) scale(0.96); }
  to   { opacity: 1; transform: translateY(0) scale(1); }
}

.toast--error { border-left: 3px solid var(--color-error); }

.toast__icon {
  color: var(--color-error);
  font-size: 1.125rem;
  flex-shrink: 0;
}

.toast__content strong { display: block; margin-bottom: var(--space-1); }
.toast__content p { font-size: 0.875rem; color: var(--color-text-secondary); }

.toast__close {
  background: transparent;
  border: none;
  color: var(--color-text-muted);
  cursor: pointer;
  font-size: 1.125rem;
  line-height: 1;
  padding: var(--space-1);
  margin-left: auto;
  flex-shrink: 0;
  min-width: 32px;
  min-height: 32px;
}
```

**Toast error: persist until dismissed** — never auto-dismiss error toasts. Users need to read them.

---

## Pattern E — Full-Page Error (404 / 500)

```html
<main class="error-page">
  <div class="container">
    <span class="error-page__code" aria-hidden="true">404</span>
    <h1 class="error-page__title">Page not found</h1>
    <p class="error-page__desc">
      This page doesn't exist or was moved.
      Check the URL or go back to the dashboard.
    </p>
    <div class="error-page__actions">
      <a href="/dashboard" class="btn-primary">Go to dashboard</a>
      <button onclick="history.back()" class="btn-ghost">Go back</button>
    </div>
  </div>
</main>
```

```css
.error-page {
  min-height: 100dvh;
  display: flex;
  align-items: center;
  text-align: center;
}

.error-page__code {
  font-size: clamp(4rem, 12vw, 8rem);
  font-weight: 800;
  color: var(--color-text-muted);
  opacity: 0.2;
  display: block;
  line-height: 1;
  letter-spacing: -0.04em;
}

.error-page__title {
  font-size: clamp(1.5rem, 3vw, 2.5rem);
  margin-bottom: var(--space-4);
}

.error-page__desc {
  max-width: 44ch;
  margin-inline: auto;
  color: var(--color-text-secondary);
  margin-bottom: var(--space-8);
}

.error-page__actions {
  display: flex;
  gap: var(--space-3);
  justify-content: center;
  flex-wrap: wrap;
}
```

---

## Error Copy Formula

```
[What failed] + [Why it failed] + [One specific recovery action]

❌ "Error"
❌ "Something went wrong"
❌ "Invalid input"
❌ "Action failed. Please try again."

✅ "Couldn't save changes — your session expired. Sign in again to continue."
✅ "Password must be at least 8 characters — include one number or symbol."
✅ "Export failed — the date range exceeds 90 days. Select a shorter range."
✅ "Couldn't delete this project — it has 3 active billing subscriptions. Cancel billing first."
```

**Tone rules:**
- Neutral, not apologetic ("Couldn't load" not "Sorry, we couldn't load")
- Specific, not systemic ("Your connection dropped" not "There was a problem")
- Actionable ("Try again" → "Retry upload" is better)
- Never blame the user ("Invalid input" → "Enter a valid email address")

---

## Accessibility Requirements

```html
<!-- Field errors: aria-invalid + aria-describedby -->
<input aria-invalid="true" aria-describedby="field-error-id" />
<span id="field-error-id" role="alert">Error message</span>

<!-- Non-blocking errors: role="alert" + aria-live="polite" -->
<!-- Blocking errors: role="alert" + aria-live="assertive" -->

<!-- Form errors: scroll to and focus error summary on submit -->
```

---

## Anti-Patterns

- Auto-dismissing error toasts (users need time to read errors)
- Clearing form fields on server error (forces user to re-type everything)
- Generic "Something went wrong" — tells the user nothing
- Error toast that appears in bottom-left (opposite of reading direction)
- Red color as the only indicator (must have icon + text for colorblind users)
- Showing a skeleton loader when the data actually errored (use error state instead)
- Stack trace or technical error codes exposed to end users

## Related Files

- `rules/06-components.md` — R4: Form input anatomy, error placement
- `rules/13-saas-products.md` — R9: Error recovery as product feature
- `patterns/product-ui/loading-states.md` — skeleton vs. error distinction
- `references/accessibility.md` — aria-live regions, focus management
- `references/forms.md` — full form validation patterns
