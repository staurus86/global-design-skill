# Blueprint — Onboarding Flow From Scratch

> A complete reference for building a new-user onboarding flow: from the signup form to the aha moment. Covers multi-step wizard, email verification, empty state, and the getting-started checklist.

---

## Flow Architecture

```
[Signup form]
     ↓
[Email verification] (optional — delay until after aha moment)
     ↓
[Wizard: 3–4 steps max]
  Step 1 — What will you use this for? (goal-based routing)
  Step 2 — Core configuration (1–2 inputs, minimum viable)
  Step 3 — Invite team (optional, skippable)
     ↓
[Aha moment — first real value action]
     ↓
[Success state + getting-started checklist on dashboard]
```

---

## Decision: When to Verify Email

```
Verify email BEFORE first use:
  Medical / financial products (compliance)
  Any product where abuse costs money immediately

Verify email AFTER aha moment (preferred):
  All other products — verification before value costs ~30% of signups
  Pattern: complete signup → onboard → use product → reminder email
  User verifies after they've already seen value
```

---

## Page 1 — Signup Form

```html
<div class="auth-page">
  <div class="auth-card">
    <div class="auth-card__header">
      <img src="/logo.svg" alt="Acme" class="auth-logo" width="80" height="24" />
      <h1 class="auth-heading">Create your account</h1>
      <p class="auth-sub">Free forever. No credit card required.</p>
    </div>

    <!-- OAuth first — reduces friction -->
    <div class="auth-oauth">
      <button class="btn btn--oauth" type="button">
        <svg class="btn__icon" aria-hidden="true" width="18" height="18" viewBox="0 0 24 24">
          <!-- GitHub icon -->
          <path fill="currentColor" d="M12 .3a12 12 0 0 0-3.79 23.4c.6.1.8-.26.8-.58v-2.03c-3.33.72-4.03-1.61-4.03-1.61-.55-1.39-1.34-1.76-1.34-1.76-1.08-.74.08-.73.08-.73 1.2.09 1.83 1.24 1.83 1.24 1.07 1.83 2.81 1.3 3.5 1 .1-.78.42-1.31.76-1.61-2.66-.3-5.46-1.33-5.46-5.93 0-1.31.47-2.38 1.24-3.22-.14-.3-.54-1.52.12-3.17 0 0 1.01-.32 3.3 1.23a11.5 11.5 0 0 1 6 0c2.29-1.55 3.3-1.23 3.3-1.23.66 1.65.26 2.87.12 3.17.78.84 1.24 1.91 1.24 3.22 0 4.61-2.8 5.63-5.48 5.92.43.37.81 1.1.81 2.22v3.29c0 .32.19.7.8.58A12 12 0 0 0 12 .3z"/>
        </svg>
        Continue with GitHub
      </button>
      <button class="btn btn--oauth" type="button">
        <svg class="btn__icon" aria-hidden="true" width="18" height="18" viewBox="0 0 24 24">
          <!-- Google icon -->
          <path fill="currentColor" d="M12.5 10.5v3h5.1c-.2 1.1-1.4 3.2-5.1 3.2a5.7 5.7 0 0 1 0-11.4c1.6 0 2.7.7 3.3 1.3l2.2-2.1C16.4 3 14.6 2 12.5 2a8.5 8.5 0 1 0 0 17c4.9 0 8.2-3.4 8.2-8.3 0-.6 0-1-.1-1.4H12.5z"/>
        </svg>
        Continue with Google
      </button>
    </div>

    <div class="auth-divider" aria-hidden="true">
      <span>or</span>
    </div>

    <!-- Email form -->
    <form class="auth-form" novalidate>
      <div class="field">
        <label class="field-label" for="email">Work email</label>
        <input
          class="field-input"
          type="email"
          id="email"
          name="email"
          autocomplete="email"
          placeholder="alex@company.com"
          required
        />
      </div>
      <div class="field">
        <label class="field-label" for="password">Password</label>
        <input
          class="field-input"
          type="password"
          id="password"
          name="password"
          autocomplete="new-password"
          placeholder="At least 8 characters"
          required
          minlength="8"
        />
      </div>
      <button class="btn btn--primary btn--full" type="submit">
        Create account
      </button>
      <p class="auth-terms">
        By signing up, you agree to the
        <a href="/terms">Terms</a> and <a href="/privacy">Privacy Policy</a>.
      </p>
    </form>

    <p class="auth-switch">
      Already have an account? <a href="/login">Sign in</a>
    </p>
  </div>
</div>
```

```css
.auth-page {
  min-height: 100dvh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-6);
  background: var(--color-surface);
}

.auth-card {
  width: 100%;
  max-width: 400px;
  display: flex;
  flex-direction: column;
  gap: var(--space-6);
}

.auth-card__header { text-align: center; display: flex; flex-direction: column; gap: var(--space-3); }
.auth-logo { margin-inline: auto; }

.auth-heading {
  font-size: var(--text-h2);
  font-family: var(--font-display);
  font-weight: 700;
  letter-spacing: -0.02em;
  color: var(--color-text-primary);
}

.auth-sub { font-size: var(--text-sm); color: var(--color-text-secondary); }

.auth-oauth { display: flex; flex-direction: column; gap: var(--space-3); }

.btn--oauth {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-3);
  padding: var(--space-3) var(--space-4);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  background: var(--color-surface);
  color: var(--color-text-primary);
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
  cursor: pointer;
  transition:
    background var(--duration-fast) var(--ease-smooth),
    border-color var(--duration-fast) var(--ease-smooth);
}

.btn--oauth:hover { background: var(--color-surface-2); border-color: var(--color-border-strong); }

.auth-divider {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  color: var(--color-text-muted);
  font-size: var(--text-sm);
}

.auth-divider::before, .auth-divider::after {
  content: '';
  flex: 1;
  height: 1px;
  background: var(--color-border);
}

.auth-form { display: flex; flex-direction: column; gap: var(--space-4); }

.auth-terms {
  font-size: 12px;
  color: var(--color-text-muted);
  text-align: center;
}

.auth-terms a { color: var(--color-text-secondary); }

.auth-switch { text-align: center; font-size: var(--text-sm); color: var(--color-text-secondary); }
.auth-switch a { color: var(--color-accent); font-weight: var(--font-weight-medium); }
```

---

## Pages 2–4 — Onboarding Wizard

See `recipes/improve-onboarding.md` for the full wizard component (HTML, CSS, JS).

**Step content guidelines:**

```
Step 1 — Goal selection (1 question only):
  "What will you primarily use Acme for?"
    ○ Deploy web apps
    ○ Host APIs and services
    ○ Automate CI/CD pipelines
  → Route to different default configs based on answer

Step 2 — Core setup:
  Only the 1–2 fields absolutely required for the aha moment.
  Skip anything that can default to a sensible value.
  Example: team name + first project name only.

Step 3 — Invite team (optional):
  "Invite teammates (optional)"
  Email input for comma-separated addresses.
  Prominent "Skip for now" link.
  Copy: "You can always invite people later from Settings."
```

---

## Page 5 — Aha Moment

Design for the specific aha moment in your product. Example: first deployment.

```html
<div class="aha-moment" role="status" aria-live="polite">
  <div class="aha-moment__animation" aria-hidden="true">
    <!-- Confetti or check animation -->
    <svg class="aha-check" viewBox="0 0 80 80" width="80" height="80">
      <circle class="aha-check__circle" cx="40" cy="40" r="36"
        fill="none" stroke="var(--color-success)" stroke-width="4"
        stroke-dasharray="226" stroke-dashoffset="226"/>
      <path class="aha-check__tick" d="M24 40l12 12 20-24"
        fill="none" stroke="var(--color-success)" stroke-width="4"
        stroke-linecap="round" stroke-dasharray="50" stroke-dashoffset="50"/>
    </svg>
  </div>

  <h1 class="aha-moment__heading">Your first deploy is live.</h1>
  <p class="aha-moment__url">
    <a href="https://alpha.acme.app" target="_blank" rel="noopener">
      alpha.acme.app
    </a>
  </p>
  <p class="aha-moment__sub">Deployed to 24 edge regions in 18 seconds.</p>

  <a href="/dashboard" class="btn btn--primary btn--lg">
    Go to dashboard
  </a>
</div>
```

```css
.aha-moment {
  min-height: 100dvh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  gap: var(--space-6);
  padding: var(--space-8);
}

.aha-moment__heading {
  font-size: var(--text-h1);
  font-family: var(--font-display);
  font-weight: 700;
  letter-spacing: -0.02em;
  color: var(--color-text-primary);
}

.aha-moment__url a {
  font-size: var(--text-h3);
  font-family: var(--font-mono);
  color: var(--color-accent);
  text-decoration: underline;
}

.aha-moment__sub { font-size: var(--text-sm); color: var(--color-text-muted); }

/* Animate the check */
.aha-check__circle { animation: draw-circle 600ms var(--ease-spring) 100ms both; }
.aha-check__tick   { animation: draw-tick   400ms var(--ease-spring) 600ms both; }

@keyframes draw-circle {
  to { stroke-dashoffset: 0; }
}
@keyframes draw-tick {
  to { stroke-dashoffset: 0; }
}

@media (prefers-reduced-motion: reduce) {
  .aha-check__circle, .aha-check__tick { animation: none; stroke-dashoffset: 0; }
}
```

---

## Getting-Started Checklist (Dashboard)

See `recipes/improve-onboarding.md` for the full checklist component with progress bar.

---

## Onboarding Metrics to Track

```
Track these from day one — they tell you where people drop out:

  Signup → wizard start:        target > 85%
  Wizard step 1 → step 2:       target > 90%
  Wizard → aha moment:          target > 60%
  Aha moment → day 7 retention: target > 40%

Drop below target: investigate that specific step.
Add console logs, session replay, or user interviews before changing UI.
```

---

*Blueprint version: global-design-skill v1.0 — `blueprints/onboarding-flow-from-scratch.md`*  
*Related: `recipes/improve-onboarding.md`, `patterns/product-ui/forms.md`, `rules/10-forms.md`*
