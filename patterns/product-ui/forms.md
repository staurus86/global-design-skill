# Pattern — Forms

> Complete UI patterns for every form context: sign-in, sign-up, settings, checkout, multi-step. Each pattern includes full HTML, CSS via tokens, and the specific rationale behind every structural decision.

---

## Pattern 1 — Sign-in Form

**Context:** Auth page, modal, or inline panel. Maximum friction reduction — users who reach this form already decided to use the product.

```html
<div class="auth-card">
  <div class="auth-card__header">
    <h1 class="auth-card__title">Sign in</h1>
    <p class="auth-card__sub">
      New here? <a href="/signup" class="link">Create an account</a>
    </p>
  </div>

  <form class="auth-form" novalidate>
    <!-- SSO first — reduces password friction -->
    <div class="sso-buttons">
      <button type="button" class="btn-sso">
        <svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24"><!-- Google icon --></svg>
        Continue with Google
      </button>
      <button type="button" class="btn-sso">
        <svg aria-hidden="true" width="18" height="18"><!-- GitHub icon --></svg>
        Continue with GitHub
      </button>
    </div>

    <div class="divider" role="separator">
      <span>or continue with email</span>
    </div>

    <div class="field">
      <label for="signin-email" class="field__label">Email</label>
      <input
        type="email"
        id="signin-email"
        name="email"
        class="input"
        autocomplete="email"
        inputmode="email"
        aria-required="true"
        aria-describedby="signin-email-error"
        autofocus
      />
      <p class="field__error" id="signin-email-error" role="alert" aria-live="assertive"></p>
    </div>

    <div class="field">
      <div class="field__label-row">
        <label for="signin-password" class="field__label">Password</label>
        <a href="/forgot-password" class="link link--sm">Forgot password?</a>
      </div>
      <div class="input-group">
        <input
          type="password"
          id="signin-password"
          name="password"
          class="input"
          autocomplete="current-password"
          aria-required="true"
          aria-describedby="signin-password-error"
        />
        <button type="button" class="input-toggle" aria-label="Show password" aria-pressed="false">
          <svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z"/><circle cx="12" cy="12" r="3"/></svg>
        </button>
      </div>
      <p class="field__error" id="signin-password-error" role="alert" aria-live="assertive"></p>
    </div>

    <button type="submit" class="btn-primary btn--full" id="signin-submit">
      Sign in
    </button>

    <!-- Form-level error (wrong credentials) -->
    <div class="form-error" id="signin-error" role="alert" aria-live="assertive" aria-atomic="true"></div>
  </form>
</div>
```

```css
.auth-card {
  width: min(420px, 100%);
  margin-inline: auto;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  padding: var(--space-10);
  box-shadow: var(--shadow-lg);
}

.auth-card__title {
  font-family: var(--font-display);
  font-size: var(--text-h2);
  font-weight: 700;
  line-height: var(--line-height-tight);
  color: var(--color-text-primary);
  margin-bottom: var(--space-2);
}

.auth-card__sub { color: var(--color-text-secondary); font-size: var(--text-sm); }

.sso-buttons {
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
}

.btn-sso {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-3);
  height: var(--btn-height-md);
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-text-primary);
  cursor: pointer;
  transition: background var(--duration-fast) var(--ease-smooth),
              border-color var(--duration-fast) var(--ease-smooth);
}
.btn-sso:hover { background: var(--color-surface-2); border-color: var(--color-text-muted); }

.divider {
  display: flex;
  align-items: center;
  gap: var(--space-4);
  margin-block: var(--space-5);
  color: var(--color-text-muted);
  font-size: var(--text-xs);
}
.divider::before,
.divider::after {
  content: '';
  flex: 1;
  height: 1px;
  background: var(--color-border);
}

.field__label-row {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: var(--space-2);
}
```

---

## Pattern 2 — Settings Form (Edit Profile)

**Context:** Account settings, preferences. User can save individual sections independently — not one giant submit for the whole page.

```html
<main class="settings-layout">
  <!-- Settings nav (sidebar) handled by sidebar-patterns.md -->
  <div class="settings-content">

    <section class="settings-section" aria-labelledby="profile-heading">
      <div class="settings-section__header">
        <h2 id="profile-heading" class="settings-section__title">Profile</h2>
        <p class="settings-section__desc">Your name and avatar visible to your team.</p>
      </div>

      <form class="settings-form" novalidate>
        <!-- Avatar upload -->
        <div class="field field--avatar">
          <label class="field__label">Profile photo</label>
          <div class="avatar-field">
            <div class="avatar avatar--lg" aria-hidden="true">
              <img src="{{ user.avatar }}" alt="" width="64" height="64" />
            </div>
            <div class="avatar-actions">
              <label for="avatar-upload" class="btn-ghost btn--sm" role="button" tabindex="0">
                Upload photo
                <input
                  type="file"
                  id="avatar-upload"
                  name="avatar"
                  accept="image/png,image/jpeg,image/webp"
                  class="sr-only"
                  aria-describedby="avatar-hint"
                />
              </label>
              <p class="field__hint" id="avatar-hint">JPG, PNG or WebP. Max 2MB.</p>
            </div>
          </div>
        </div>

        <!-- Name fields side by side -->
        <div class="field-group">
          <div class="field">
            <label for="first-name" class="field__label">First name</label>
            <input
              type="text" id="first-name" name="first_name"
              class="input" autocomplete="given-name"
              value="{{ user.first_name }}"
              aria-required="true"
            />
          </div>
          <div class="field">
            <label for="last-name" class="field__label">Last name</label>
            <input
              type="text" id="last-name" name="last_name"
              class="input" autocomplete="family-name"
              value="{{ user.last_name }}"
            />
          </div>
        </div>

        <div class="field">
          <label for="email" class="field__label">Email address</label>
          <input
            type="email" id="email" name="email"
            class="input" autocomplete="email"
            value="{{ user.email }}"
            aria-required="true"
            aria-describedby="email-hint"
          />
          <p class="field__hint" id="email-hint">
            Changing your email requires re-verification.
          </p>
        </div>

        <!-- Section save: sticks to section, not whole page -->
        <div class="settings-form__actions">
          <button type="submit" class="btn-primary btn--sm" id="profile-save">
            Save changes
          </button>
          <!-- Success: inline, replaces button text momentarily -->
          <span class="save-status" id="profile-save-status" aria-live="polite"></span>
        </div>
      </form>
    </section>

    <!-- Divider between settings sections -->
    <hr class="settings-divider" />

    <!-- Another section: Notifications, Password, Danger zone, etc. -->
  </div>
</main>
```

```css
.settings-layout {
  display: grid;
  grid-template-columns: 240px 1fr;
  gap: var(--space-12);
  max-width: var(--container-lg);
  margin-inline: auto;
  padding: var(--space-10) var(--space-8);
}

@media (max-width: 768px) {
  .settings-layout { grid-template-columns: 1fr; }
}

.settings-section {
  display: grid;
  grid-template-columns: 280px 1fr;
  gap: var(--space-8);
  padding-block: var(--space-8);
}

@media (max-width: 960px) {
  .settings-section { grid-template-columns: 1fr; gap: var(--space-5); }
}

.settings-section__title {
  font-size: var(--text-lg);
  font-weight: var(--font-weight-semibold);
  color: var(--color-text-primary);
  margin-bottom: var(--space-2);
}
.settings-section__desc { font-size: var(--text-sm); color: var(--color-text-secondary); }

.settings-form { display: flex; flex-direction: column; gap: var(--space-5); }

.field-group { display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-4); }
@media (max-width: 480px) { .field-group { grid-template-columns: 1fr; } }

.settings-form__actions {
  display: flex;
  align-items: center;
  gap: var(--space-4);
  padding-top: var(--space-2);
}

.save-status { font-size: var(--text-sm); color: var(--color-success-text); }

.settings-divider {
  border: none;
  border-top: 1px solid var(--color-border);
  margin-block: 0;
}
```

---

## Pattern 3 — Multi-Step Form (Checkout / Onboarding)

**Context:** 3–5 step process where each step has one clear purpose. Full pattern including progress, navigation, and step transition.

```html
<div class="multistep-form">
  <!-- Progress indicator -->
  <nav class="form-stepper" aria-label="Checkout steps">
    <ol class="form-stepper__list">
      <li class="stepper-step stepper-step--done" aria-label="Step 1: Account — completed">
        <span class="stepper-step__dot" aria-hidden="true">
          <svg width="12" height="12" viewBox="0 0 12 12"><path d="M2 6l3 3 5-5" stroke="currentColor" stroke-width="1.5" fill="none"/></svg>
        </span>
        <span class="stepper-step__label">Account</span>
      </li>
      <span class="stepper-connector" aria-hidden="true"></span>

      <li class="stepper-step stepper-step--active" aria-current="step" aria-label="Step 2: Details — current">
        <span class="stepper-step__dot" aria-hidden="true">2</span>
        <span class="stepper-step__label">Details</span>
      </li>
      <span class="stepper-connector" aria-hidden="true"></span>

      <li class="stepper-step" aria-label="Step 3: Payment — not yet reached">
        <span class="stepper-step__dot" aria-hidden="true">3</span>
        <span class="stepper-step__label">Payment</span>
      </li>
    </ol>
  </nav>

  <!-- Step panel -->
  <div class="step-panel" role="group" aria-labelledby="step-heading">
    <h2 id="step-heading" class="step-heading">Your details</h2>
    <p class="step-sub">Tell us about yourself so we can personalize your experience.</p>

    <form class="step-form" novalidate>
      <!-- step-specific fields -->
      <div class="field">
        <label for="role" class="field__label">Your role</label>
        <select id="role" name="role" class="input" autocomplete="organization-title">
          <option value="">Select a role</option>
          <option value="engineer">Software Engineer</option>
          <option value="lead">Tech Lead</option>
          <option value="manager">Engineering Manager</option>
          <option value="founder">Founder / CTO</option>
          <option value="other">Other</option>
        </select>
      </div>

      <!-- Step navigation -->
      <div class="step-nav">
        <button type="button" class="btn-ghost" id="step-back">← Back</button>
        <button type="submit" class="btn-primary" id="step-next">Continue →</button>
      </div>
    </form>
  </div>
</div>
```

```css
.multistep-form {
  max-width: 560px;
  margin-inline: auto;
}

/* Stepper */
.form-stepper__list {
  display: flex;
  align-items: center;
  gap: 0;
  list-style: none;
  padding: 0;
  margin-bottom: var(--space-10);
}

.stepper-step {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  font-size: var(--text-sm);
  color: var(--color-text-muted);
}

.stepper-step__dot {
  width: 28px;
  height: 28px;
  border-radius: var(--radius-full);
  border: 2px solid var(--color-border);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: var(--text-xs);
  font-weight: var(--font-weight-bold);
  flex-shrink: 0;
}

.stepper-step--done .stepper-step__dot {
  background: var(--color-success-text);
  border-color: var(--color-success-text);
  color: white;
}

.stepper-step--active {
  color: var(--color-text-primary);
  font-weight: var(--font-weight-medium);
}
.stepper-step--active .stepper-step__dot {
  border-color: var(--color-accent);
  color: var(--color-accent);
}

.stepper-connector {
  flex: 1;
  height: 2px;
  background: var(--color-border);
  margin-inline: var(--space-2);
}

/* Step panel */
.step-heading {
  font-family: var(--font-display);
  font-size: var(--text-h2);
  font-weight: 700;
  line-height: var(--line-height-tight);
  margin-bottom: var(--space-2);
}
.step-sub { color: var(--color-text-secondary); margin-bottom: var(--space-8); }

.step-form { display: flex; flex-direction: column; gap: var(--space-5); }

.step-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: var(--space-4);
}
```

---

## Common Form Elements

```css
/* ── Shared across all form patterns ── */

/* Field */
.field { display: flex; flex-direction: column; gap: var(--space-2); }
.field__label { font-size: var(--text-sm); font-weight: var(--font-weight-medium); color: var(--color-text-primary); }
.field__hint  { font-size: var(--text-sm); color: var(--color-text-muted); }
.field__error { font-size: var(--text-sm); color: var(--color-error-text); min-height: 1.5em; }
.field__error:empty { display: none; }

/* Input */
.input {
  width: 100%;
  height: var(--input-height);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  background: var(--color-surface);
  color: var(--color-text-primary);
  font-size: var(--text-body);
  padding-inline: var(--space-4);
  outline: none;
  transition: border-color var(--duration-fast) var(--ease-smooth);
}
.input:focus-visible {
  border-color: var(--color-accent);
  box-shadow: 0 0 0 3px oklch(from var(--color-accent) l c h / 0.15);
}
.input[aria-invalid="true"] { border-color: var(--color-error-text); background: var(--color-error-bg); }
.input::placeholder { color: var(--color-text-muted); }

/* Textarea */
textarea.input {
  height: auto;
  min-height: calc(var(--input-height) * 3);
  padding-block: var(--space-3);
  resize: vertical;
  line-height: var(--line-height-relaxed);
}

/* Input group (input + inline button) */
.input-group { position: relative; display: flex; align-items: center; }
.input-group .input { padding-inline-end: var(--space-12); }
.input-toggle {
  position: absolute;
  right: var(--space-3);
  width: 32px; height: 32px;
  display: flex; align-items: center; justify-content: center;
  background: transparent; border: none; cursor: pointer;
  color: var(--color-text-muted);
  border-radius: var(--radius-sm);
}
.input-toggle:hover { color: var(--color-text-primary); }

/* Select */
select.input {
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23999' stroke-width='1.5'%3E%3Cpath d='m6 9 6 6 6-6'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right var(--space-3) center;
  padding-inline-end: var(--space-10);
  cursor: pointer;
}

/* Form error (global / server-level) */
.form-error {
  padding: var(--space-3) var(--space-4);
  background: var(--color-error-bg);
  border: 1px solid oklch(from var(--color-error-text) l c h / 0.3);
  border-radius: var(--radius-md);
  color: var(--color-error-text);
  font-size: var(--text-sm);
}
.form-error:empty { display: none; }

/* Link inside forms */
.link { color: var(--color-accent); text-decoration: underline; text-underline-offset: 2px; }
.link--sm { font-size: var(--text-sm); }

/* Full-width button */
.btn--full { width: 100%; }
```

---

*Pattern version: global-design-skill v1.0 — `patterns/product-ui/forms.md`*
*Related: `rules/10-forms.md`, `rules/07-accessibility.md` R3, `examples/03-form-accessibility.md`, `checklists/ui-review.md` §2*
