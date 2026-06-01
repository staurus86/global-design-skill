# Recipe — Improve Onboarding

> **Trigger:** New user activation rate is low. Users sign up, look around, and leave. They never reach the "aha moment" — the first action that demonstrates product value.

---

## Diagnosis Checklist

```
[ ] User lands on an empty dashboard with no guidance
[ ] No progress indicator during onboarding steps
[ ] Onboarding asks for optional information before showing value
[ ] "Complete your profile" is the first ask (not value delivery)
[ ] No sample data / demo state to show what the product looks like
[ ] Multiple email verification walls before the aha moment
[ ] Users must read documentation to get started
[ ] No way to skip steps and return later
[ ] Mobile onboarding is not tested
[ ] No success state — completion not celebrated
```

---

## The Three Principles

```
1. Value before friction
   Show the product working before asking for credit card, phone,
   or company size. Every field before the aha moment costs 10% of users.

2. One action per screen
   A setup wizard with 8 inputs on one screen fails. One decision at a time.

3. Progress is motivating
   Show users how far they've come and what remains.
   A half-filled progress bar is more motivating than an empty checklist.
```

---

## Step 1 — Define the Aha Moment

Before designing any onboarding, write down the exact aha moment:

```
For a deployment platform:   First successful deploy completes
For a project management:    First task assigned to a real teammate
For an analytics tool:       First data point plotted on a real chart
For a communication tool:    First real message received

Everything in onboarding should get the user to this moment faster.
```

Remove any step that doesn't contribute to reaching the aha moment.

---

## Step 2 — Multi-Step Wizard Component

```html
<div class="onboarding-wizard" aria-label="Account setup">

  <!-- Progress indicator -->
  <nav class="wizard-progress" aria-label="Setup progress">
    <ol class="wizard-progress__steps">
      <li class="wizard-step wizard-step--complete" aria-label="Create account, completed">
        <span class="wizard-step__indicator">
          <svg aria-hidden="true" width="12" height="12" viewBox="0 0 16 16" fill="none"
            stroke="currentColor" stroke-width="2" stroke-linecap="round">
            <path d="M3 8l4 4 6-6"/>
          </svg>
        </span>
        <span class="wizard-step__label">Account</span>
      </li>
      <span class="wizard-step__line" aria-hidden="true"></span>
      <li class="wizard-step wizard-step--active" aria-current="step"
        aria-label="Set up your workspace, current step">
        <span class="wizard-step__indicator">2</span>
        <span class="wizard-step__label">Workspace</span>
      </li>
      <span class="wizard-step__line" aria-hidden="true"></span>
      <li class="wizard-step" aria-label="Invite your team, upcoming">
        <span class="wizard-step__indicator">3</span>
        <span class="wizard-step__label">Invite team</span>
      </li>
      <span class="wizard-step__line" aria-hidden="true"></span>
      <li class="wizard-step" aria-label="First deploy, upcoming">
        <span class="wizard-step__indicator">4</span>
        <span class="wizard-step__label">Deploy</span>
      </li>
    </ol>
    <p class="wizard-progress__sub" aria-live="polite">Step 2 of 4</p>
  </nav>

  <!-- Step content -->
  <div class="wizard-body" role="region" aria-labelledby="step-heading">
    <div class="wizard-body__inner">
      <h1 class="wizard-heading" id="step-heading">Set up your workspace</h1>
      <p class="wizard-sub">Give your workspace a name. You can change this later.</p>

      <form class="wizard-form" id="workspace-form" novalidate>
        <div class="field">
          <label class="field-label" for="workspace-name">Workspace name</label>
          <input
            class="field-input"
            type="text"
            id="workspace-name"
            name="workspace_name"
            placeholder="Acme Engineering"
            autocomplete="organization"
            required
            minlength="2"
          />
        </div>
      </form>
    </div>

    <div class="wizard-footer">
      <button class="btn btn--ghost" type="button" data-wizard-back>Back</button>
      <div class="wizard-footer__right">
        <button class="btn btn--ghost btn--sm" type="button" data-wizard-skip>Skip for now</button>
        <button class="btn btn--primary" type="submit" form="workspace-form">
          Continue
        </button>
      </div>
    </div>
  </div>

</div>
```

```css
.onboarding-wizard {
  max-width: 520px;
  margin-inline: auto;
  padding: var(--space-8);
  display: flex;
  flex-direction: column;
  gap: var(--space-10);
  min-height: 100dvh;
  justify-content: center;
}

/* Progress steps */
.wizard-progress__steps {
  display: flex;
  align-items: center;
  list-style: none;
  padding: 0; margin: 0;
  gap: 0;
}

.wizard-step {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-2);
}

.wizard-step__indicator {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 32px; height: 32px;
  border-radius: var(--radius-full);
  font-size: 13px;
  font-weight: var(--font-weight-semibold);
  background: var(--color-surface-3);
  color: var(--color-text-muted);
  border: 2px solid transparent;
  transition:
    background var(--duration-normal) var(--ease-smooth),
    color      var(--duration-normal) var(--ease-smooth),
    border-color var(--duration-normal) var(--ease-smooth);
}

.wizard-step--complete .wizard-step__indicator {
  background: var(--color-success-subtle);
  color: var(--color-success);
  border-color: var(--color-success);
}

.wizard-step--active .wizard-step__indicator {
  background: var(--color-accent-subtle);
  color: var(--color-accent);
  border-color: var(--color-accent);
}

.wizard-step__label {
  font-size: 11px;
  font-weight: var(--font-weight-medium);
  color: var(--color-text-muted);
  white-space: nowrap;
}

.wizard-step--active .wizard-step__label,
.wizard-step--complete .wizard-step__label {
  color: var(--color-text-secondary);
}

.wizard-step__line {
  flex: 1;
  height: 2px;
  background: var(--color-border);
  margin-bottom: calc(16px + var(--space-2)); /* align with indicator center */
}

.wizard-progress__sub {
  text-align: center;
  font-size: var(--text-sm);
  color: var(--color-text-muted);
  margin-top: var(--space-3);
}

/* Body */
.wizard-body {
  display: flex;
  flex-direction: column;
  gap: var(--space-8);
}

.wizard-heading {
  font-size: var(--text-h2);
  font-family: var(--font-display);
  font-weight: 700;
  color: var(--color-text-primary);
  letter-spacing: -0.02em;
  line-height: 1.1;
  margin-bottom: var(--space-3);
}

.wizard-sub {
  font-size: var(--text-body);
  color: var(--color-text-secondary);
  line-height: 1.65;
}

.wizard-form { margin-top: var(--space-6); }

/* Footer */
.wizard-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-4);
  padding-top: var(--space-6);
  border-top: 1px solid var(--color-border);
}

.wizard-footer__right {
  display: flex;
  align-items: center;
  gap: var(--space-3);
}

@media (max-width: 480px) {
  .onboarding-wizard { padding: var(--space-6) var(--space-4); }
  .wizard-step__label { display: none; }
  .wizard-footer { flex-direction: column; align-items: stretch; }
  .wizard-footer__right { flex-direction: column; }
}
```

---

## Step 3 — Empty Dashboard with Checklist

After onboarding completion, the user lands on a dashboard with a getting-started checklist. Shows value with sample data.

```html
<div class="onboarding-checklist" aria-labelledby="checklist-heading">
  <div class="onboarding-checklist__header">
    <h2 class="onboarding-checklist__heading" id="checklist-heading">
      Get started with 4 quick steps
    </h2>
    <div class="onboarding-checklist__progress">
      <div class="progress-bar">
        <div class="progress-bar__fill" style="width: 25%" role="progressbar"
          aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"
          aria-label="25% complete">
        </div>
      </div>
      <span class="progress-bar__label">1 of 4 complete</span>
    </div>
  </div>

  <ul class="onboarding-tasks">
    <li class="onboarding-task onboarding-task--done">
      <span class="onboarding-task__check" aria-hidden="true">
        <svg width="14" height="14" viewBox="0 0 16 16" fill="none"
          stroke="currentColor" stroke-width="2" stroke-linecap="round">
          <path d="M3 8l4 4 6-6"/>
        </svg>
      </span>
      <div class="onboarding-task__body">
        <p class="onboarding-task__title">Create your account</p>
      </div>
      <span class="badge badge--success">Done</span>
    </li>

    <li class="onboarding-task">
      <span class="onboarding-task__check onboarding-task__check--empty" aria-hidden="true"></span>
      <div class="onboarding-task__body">
        <p class="onboarding-task__title">Connect your repository</p>
        <p class="onboarding-task__desc">Link a GitHub, GitLab, or Bitbucket repo to get started.</p>
      </div>
      <a href="/connect" class="btn btn--primary btn--sm">Connect</a>
    </li>

    <li class="onboarding-task">
      <span class="onboarding-task__check onboarding-task__check--empty" aria-hidden="true"></span>
      <div class="onboarding-task__body">
        <p class="onboarding-task__title">Deploy your first project</p>
        <p class="onboarding-task__desc">Run a deploy in under 2 minutes.</p>
      </div>
      <a href="/projects/new" class="btn btn--ghost btn--sm">Start</a>
    </li>

    <li class="onboarding-task">
      <span class="onboarding-task__check onboarding-task__check--empty" aria-hidden="true"></span>
      <div class="onboarding-task__body">
        <p class="onboarding-task__title">Invite your team</p>
        <p class="onboarding-task__desc">Collaborate with up to 10 teammates for free.</p>
      </div>
      <a href="/team/invite" class="btn btn--ghost btn--sm">Invite</a>
    </li>
  </ul>

  <button class="onboarding-checklist__dismiss" type="button">
    Dismiss — I know my way around
  </button>
</div>
```

```css
.onboarding-checklist {
  background: var(--color-surface-2);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  padding: var(--space-6);
  display: flex;
  flex-direction: column;
  gap: var(--space-5);
  margin-bottom: var(--space-8);
}

.onboarding-checklist__header { display: flex; flex-direction: column; gap: var(--space-3); }

.onboarding-checklist__heading {
  font-size: var(--text-h3);
  font-weight: var(--font-weight-semibold);
  color: var(--color-text-primary);
}

.progress-bar {
  height: 6px;
  background: var(--color-surface-3);
  border-radius: var(--radius-full);
  overflow: hidden;
}

.progress-bar__fill {
  height: 100%;
  background: var(--color-accent);
  border-radius: var(--radius-full);
  transition: width var(--duration-slow) var(--ease-spring);
}

.progress-bar__label {
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
}

.onboarding-tasks {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
  list-style: none;
  padding: 0; margin: 0;
}

.onboarding-task {
  display: flex;
  align-items: center;
  gap: var(--space-4);
  padding: var(--space-4);
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
}

.onboarding-task--done { opacity: 0.6; }

.onboarding-task__check {
  width: 24px; height: 24px;
  border-radius: var(--radius-full);
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--color-success-subtle);
  color: var(--color-success);
}

.onboarding-task__check--empty {
  background: var(--color-surface-3);
  border: 2px dashed var(--color-border-strong);
}

.onboarding-task__body { flex: 1; min-width: 0; }

.onboarding-task__title {
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-text-primary);
}

.onboarding-task--done .onboarding-task__title {
  text-decoration: line-through;
  color: var(--color-text-secondary);
}

.onboarding-task__desc {
  font-size: 12px;
  color: var(--color-text-muted);
  margin-top: var(--space-1);
  line-height: 1.5;
}

.onboarding-checklist__dismiss {
  background: none;
  border: none;
  padding: 0;
  font-size: var(--text-sm);
  color: var(--color-text-muted);
  cursor: pointer;
  text-align: center;
  align-self: center;
  text-decoration: underline;
}

.onboarding-checklist__dismiss:hover { color: var(--color-text-secondary); }
```

---

## Before/After Summary

| Problem | Fix |
|---|---|
| Empty dashboard, no guidance | Checklist with sample data visible behind |
| Many fields before aha moment | Remove every field not needed for first value |
| No progress indication | Wizard progress bar + step counter |
| No way to skip | "Skip for now" link on every non-critical step |
| Success not celebrated | Completion screen with confetti / clear summary |
| Mobile onboarding untested | Wizard tested at 390px, footer button stacks |

---

## Verification

```
[ ] Time to aha moment measured — target < 5 minutes from signup
[ ] Steps not required for aha moment removed or marked optional
[ ] Mobile tested: all steps work at 390px width
[ ] Progress indicator visible and updates on each step
[ ] "Skip" available on every optional step
[ ] Checklist visible on empty dashboard
[ ] Checklist dismissable (persists in localStorage/DB)
[ ] Sample data shown so dashboard isn't completely empty
[ ] Completion celebrated (success screen, checkmarks, progress fills)
```

---

*Recipe version: global-design-skill v1.0 — `recipes/improve-onboarding.md`*  
*Related: `patterns/product-ui/forms.md`, `patterns/product-ui/notifications.md`, `operating-principles.md`*
