# Pattern — Auth Screens

> The auth flow beyond sign-in: sign-up, forgot/reset password, magic link, and OTP/2FA. Sign-in itself (SSO buttons, password toggle, error placement, full CSS) lives in `patterns/product-ui/forms.md` Pattern 1 — these screens reuse its `auth-card` shell and tokens. Auth screens are the first product UI a user touches; they set the quality expectation for everything behind them.

**Shared rules for every screen here:**
- One `auth-card` (≤ 420px), one task per screen, no marketing sidebar competing for attention
- SSO options first when they exist — every password not created is a support ticket avoided
- `autocomplete` attributes always (`email`, `new-password`, `current-password`, `one-time-code`)
- Errors per `rules/10-forms.md`: inline, neutral tone, name the fix; form-level error for credential failures
- All states designed: idle, loading (button spinner, fields stay enabled-looking but inert), error, success

---

## Pattern 1 — Sign-up Form

**Context:** Friction here is paid for twice — in lost signups and in fake-data accounts. Ask for the minimum the product needs on day one; everything else belongs in onboarding (`patterns/product-ui/onboarding.md`).

```html
<form class="auth-form" novalidate>
  <!-- SSO first, divider, then: -->
  <div class="field">
    <label for="su-email" class="field__label">Email</label>
    <input type="email" id="su-email" name="email" class="input"
           autocomplete="email" inputmode="email" aria-required="true" />
  </div>

  <div class="field">
    <label for="su-password" class="field__label">Password</label>
    <div class="input-group">
      <input type="password" id="su-password" name="new-password" class="input"
             autocomplete="new-password" aria-required="true"
             aria-describedby="pw-rules" minlength="8" />
      <button type="button" class="input-toggle" aria-label="Show password" aria-pressed="false">…</button>
    </div>
    <!-- Live requirement list: checks tick as the user types -->
    <ul class="pw-rules" id="pw-rules" aria-live="polite">
      <li class="pw-rule" data-met="false">At least 8 characters</li>
      <li class="pw-rule" data-met="false">One number or symbol</li>
    </ul>
  </div>

  <button type="submit" class="btn-primary btn--full">Create account</button>

  <p class="auth-legal">
    By continuing you agree to the <a href="/terms">Terms</a> and <a href="/privacy">Privacy Policy</a>.
  </p>
</form>
```

```css
.pw-rules { display: grid; gap: var(--space-1); margin-top: var(--space-2); }
.pw-rule {
  font-size: var(--text-xs);
  color: var(--color-text-muted);
  display: flex; align-items: center; gap: var(--space-2);
}
.pw-rule::before { content: '○'; }
.pw-rule[data-met="true"] { color: var(--color-success); }
.pw-rule[data-met="true"]::before { content: '✓'; }

.auth-legal {
  margin-top: var(--space-4);
  font-size: var(--text-xs);
  color: var(--color-text-muted);
  text-align: center;
}
```

**Decisions that matter:**
- **No "confirm password" field.** Show/hide toggle + `autocomplete="new-password"` made it obsolete; it only doubles typos and friction
- **Live requirement checklist, not a strength meter.** "Weak/medium/strong" is judgment without instruction; "✓ At least 8 characters" tells the user exactly what's left
- Name, company, role — not here. Day-one minimum is email + password (or just email for magic-link products)
- Legal consent as a sentence, not a checkbox, unless the jurisdiction requires explicit opt-in (then an unchecked checkbox — never pre-checked)
- Email verification: let the user into the product immediately if at all possible; gate sensitive actions on verification instead of gating everything

---

## Pattern 2 — Forgot / Reset Password

**Context:** The user is already frustrated. Two screens, zero surprises.

**Screen A — request (`/forgot-password`):**
- One email field + "Send reset link". That's the whole screen
- Success state replaces the form: "If an account exists for **name@example.com**, a reset link is on its way. Check spam too." — same message whether the account exists or not (prevents account enumeration)
- "Back to sign in" link

**Screen B — reset (from the email link):**
- One new-password field with the same live requirement checklist as sign-up + `autocomplete="new-password"`
- On success: sign the user in directly and redirect into the product — forcing a fresh manual sign-in after a successful reset is pure punishment
- Expired/used link state: say it plainly and offer one button — "Request a new link" — not an error code

---

## Pattern 3 — Magic Link

**Context:** Passwordless email sign-in. The design work is in the *waiting* state, not the form.

**Sent state (replaces the form):**

```html
<div class="auth-card auth-card--status" role="status">
  <div class="auth-status-icon" aria-hidden="true"><!-- mail icon --></div>
  <h1 class="auth-card__title">Check your email</h1>
  <p class="auth-card__sub">
    We sent a sign-in link to <strong>name@example.com</strong>.
    It expires in 15 minutes.
  </p>
  <button type="button" class="btn-ghost" data-cooldown="30">Resend link</button>
  <a href="/login" class="link link--sm">Use a different email</a>
</div>
```

**Decisions that matter:**
- Echo the exact email back — typos are the #1 magic-link failure, and showing the address is the diagnostic
- Resend button with a visible cooldown ("Resend (24s)") — prevents rage-clicking and rate-limit errors
- State the expiry. An expired link opens Screen B-style recovery: "This link expired — enter your email and we'll send a fresh one"
- The link must work on a *different device* than the one that requested it (user requests on desktop, opens mail on phone) — design the "confirmed, return to your other device" state

---

## Pattern 4 — OTP / 2FA Code Entry

**Context:** Six-digit code from email, SMS, or authenticator app.

```html
<form class="auth-form" novalidate>
  <label for="otp" class="field__label">Enter the 6-digit code</label>
  <input
    type="text" id="otp" name="otp" class="input input--otp"
    inputmode="numeric" pattern="[0-9]*" maxlength="6"
    autocomplete="one-time-code" autofocus
    aria-describedby="otp-hint otp-error"
  />
  <p class="field__hint" id="otp-hint">Sent to ···· ··· 4821 · <button type="button" class="link link--sm" data-cooldown="30">Resend</button></p>
  <p class="field__error" id="otp-error" role="alert" aria-live="assertive"></p>
  <button type="submit" class="btn-primary btn--full">Verify</button>
</form>
```

```css
.input--otp {
  font-family: var(--font-mono);
  font-size: var(--text-xl);
  letter-spacing: 0.5em;
  text-align: center;
}
```

**Decisions that matter:**
- **One input, not six boxes.** `autocomplete="one-time-code"` gives OS-level autofill from SMS/mail; six separate inputs break paste, autofill, and screen readers. The spaced monospace styling gives the six-box look without the damage
- `inputmode="numeric"` opens the number pad on mobile
- Auto-submit on the 6th digit is acceptable *only* with a visible loading state and an error path that clears the field and refocuses
- Wrong code: "That code didn't match — check the newest message" (codes stack up; the user often types an old one)
- Always offer the fallback path: "Use a backup code" / "Try another method"

---

## Anti-Patterns

| Anti-pattern | Why it fails | Instead |
|---|---|---|
| Confirm-password field | Doubles typos, adds nothing with show/hide toggle | One field + toggle + live rules |
| Strength meter ("weak/strong") | Judges without instructing | Requirement checklist with live ✓ |
| Six separate OTP boxes | Breaks paste, autofill, screen readers | One input, `one-time-code`, spaced mono |
| "Email not found" on forgot-password | Account enumeration vulnerability | Same neutral success message either way |
| Forcing sign-in after password reset | Punishes a user who just recovered | Sign in directly on success |
| Pre-checked marketing consent | Dark pattern; illegal in GDPR scope | Unchecked, or a plain sentence for ToS |
| CAPTCHA before first error | Friction tax on every legitimate user | Invisible/risk-based, or after N failures |
| Auth card competing with split-screen brand panel | The task is signing in, not re-reading the pitch | Brand panel is fine — keep it static, no CTAs |
