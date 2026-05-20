# Pattern — Onboarding Flows

> Onboarding is the fastest path to the aha moment. Every step that doesn't move the user toward first value is friction. Friction is churn.

---

## The Aha Moment First

Define before designing:
```
Aha moment: [the action where the user first experiences core value]
Steps required: [minimum steps to reach it]
Steps to defer: [everything that can happen after the aha moment]
Drop-off threshold: [if user abandons here, what do we learn?]
```

**Maximum steps to aha moment:** 4. Every additional step costs ~10-15% of users.

---

## Pattern A — Linear Progress Wizard

Best for: products requiring setup data before showing value (analytics, integrations, team tools).

```html
<div class="onboarding-wizard">
  <!-- Progress header -->
  <header class="onboarding-wizard__header">
    <a href="/" class="onboarding-wizard__logo">
      <img src="/logo.svg" alt="ProductName" width="120" height="32" />
    </a>
    <nav class="onboarding-progress" aria-label="Setup progress">
      <ol class="onboarding-progress__steps">
        <li class="step step--done" aria-label="Step 1: Account — completed">
          <span class="step__dot" aria-hidden="true">✓</span>
          <span class="step__label">Account</span>
        </li>
        <li class="step step--active" aria-current="step" aria-label="Step 2: Workspace — current">
          <span class="step__dot" aria-hidden="true">2</span>
          <span class="step__label">Workspace</span>
        </li>
        <li class="step" aria-label="Step 3: Invite team — not started">
          <span class="step__dot" aria-hidden="true">3</span>
          <span class="step__label">Invite team</span>
        </li>
        <li class="step" aria-label="Step 4: First project — not started">
          <span class="step__dot" aria-hidden="true">4</span>
          <span class="step__label">First project</span>
        </li>
      </ol>
    </nav>
    <div class="onboarding-wizard__skip">
      <a href="/dashboard">Skip setup →</a>
    </div>
  </header>

  <!-- Step content -->
  <main class="onboarding-wizard__content">
    <div class="onboarding-step">
      <span class="onboarding-step__count">Step 2 of 4</span>
      <h1 class="onboarding-step__title">Name your workspace</h1>
      <p class="onboarding-step__desc">
        Your workspace is where your team's projects live.
        You can change this later.
      </p>

      <form class="onboarding-step__form" action="/onboarding/workspace" method="POST">
        <div class="field">
          <label for="workspace-name">Workspace name</label>
          <input
            id="workspace-name"
            name="workspace_name"
            type="text"
            placeholder="Acme Design Team"
            autocomplete="organization"
            required
            autofocus
          />
        </div>
        <div class="field">
          <label for="workspace-url">Workspace URL</label>
          <div class="input-prefix">
            <span class="input-prefix__label">app.product.com/</span>
            <input
              id="workspace-url"
              name="workspace_url"
              type="text"
              placeholder="acme-design"
              pattern="[a-z0-9\-]+"
            />
          </div>
          <span class="field-hint">Lowercase letters, numbers, and hyphens only</span>
        </div>

        <div class="onboarding-step__actions">
          <button type="submit" class="btn-primary btn-lg">Continue</button>
        </div>
      </form>
    </div>
  </main>

  <!-- Right panel: context / preview (optional) -->
  <aside class="onboarding-wizard__context" aria-label="What to expect">
    <img src="/onboarding-preview-workspace.webp" alt="Workspace dashboard preview" width="480" height="320" />
    <p>Your workspace will look like this once your team is set up.</p>
  </aside>
</div>
```

```css
.onboarding-wizard {
  display: grid;
  grid-template-rows: auto 1fr;
  grid-template-columns: 1fr;
  min-height: 100dvh;
}

@media (min-width: 1024px) {
  .onboarding-wizard {
    grid-template-columns: 1fr 480px;
    grid-template-rows: auto 1fr;
  }
  .onboarding-wizard__header { grid-column: 1 / -1; }
  .onboarding-wizard__context { grid-row: 2; }
}

.onboarding-wizard__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: var(--space-6) var(--space-8);
  border-bottom: 1px solid var(--color-border);
}

.onboarding-progress__steps {
  display: flex;
  gap: var(--space-2);
  list-style: none;
  padding: 0;
}

.step {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  font-size: 0.875rem;
  color: var(--color-text-muted);
}

.step + .step::before {
  content: '—';
  color: var(--color-border);
}

.step--done .step__dot {
  background: var(--color-success);
  color: white;
}

.step--active {
  color: var(--color-text-primary);
  font-weight: 500;
}

.step--active .step__dot {
  background: var(--color-accent);
  color: oklch(10% 0.01 258);
}

.step__dot {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: var(--color-surface-2);
  display: grid;
  place-items: center;
  font-size: 0.75rem;
  font-weight: 600;
  flex-shrink: 0;
}

.onboarding-wizard__content {
  padding: clamp(2rem, 5vw, 4rem) clamp(1.5rem, 5vw, 5rem);
  max-width: 520px;
}

.onboarding-step__count {
  font-size: 0.8125rem;
  color: var(--color-text-muted);
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin-bottom: var(--space-3);
  display: block;
}

.onboarding-step__title {
  font-size: clamp(1.5rem, 2.5vw, 2rem);
  margin-bottom: var(--space-3);
}

.onboarding-step__actions {
  margin-top: var(--space-8);
  display: flex;
  gap: var(--space-4);
  align-items: center;
}

.onboarding-wizard__context {
  background: var(--color-surface);
  border-left: 1px solid var(--color-border);
  padding: clamp(2rem, 4vw, 3rem);
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
}

.onboarding-wizard__context img {
  border-radius: var(--radius-lg);
  width: 100%;
  height: auto;
  border: 1px solid var(--color-border);
}

.onboarding-wizard__skip {
  font-size: 0.875rem;
  color: var(--color-text-muted);
}
```

---

## Pattern B — Checklist Onboarding (in-app, post-signup)

Best for: complex products where users explore at their own pace; keeps them oriented.

```html
<div class="onboarding-checklist">
  <div class="onboarding-checklist__header">
    <h2>Get started with ProductName</h2>
    <p>Complete these steps to unlock the full power of your workspace.</p>
    <div class="checklist-progress" role="progressbar" aria-valuenow="2" aria-valuemin="0" aria-valuemax="5" aria-label="2 of 5 steps completed">
      <div class="checklist-progress__bar" style="width: 40%"></div>
    </div>
    <span class="checklist-progress__label">2 of 5 complete</span>
  </div>

  <ol class="checklist-steps" aria-label="Onboarding checklist">
    <li class="checklist-step checklist-step--done">
      <span class="checklist-step__check" aria-hidden="true">✓</span>
      <div class="checklist-step__content">
        <strong>Create your account</strong>
        <span class="checklist-step__tag">Done</span>
      </div>
    </li>

    <li class="checklist-step checklist-step--active">
      <span class="checklist-step__number" aria-hidden="true">2</span>
      <div class="checklist-step__content">
        <strong>Create your first project</strong>
        <p>Projects organize your work. Start with anything.</p>
        <a href="/projects/new" class="btn-primary btn-sm">Create project</a>
      </div>
    </li>

    <li class="checklist-step checklist-step--locked">
      <span class="checklist-step__number" aria-hidden="true">3</span>
      <div class="checklist-step__content">
        <strong>Invite your team</strong>
        <p>Collaboration is better together.</p>
      </div>
    </li>
  </ol>

  <button class="checklist-dismiss" aria-label="Dismiss onboarding checklist">
    Dismiss checklist
  </button>
</div>
```

```css
.onboarding-checklist {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  padding: var(--space-6);
  max-width: 480px;
}

.checklist-progress {
  height: 4px;
  background: var(--color-surface-2);
  border-radius: 9999px;
  margin-top: var(--space-4);
  overflow: hidden;
}

.checklist-progress__bar {
  height: 100%;
  background: var(--color-accent);
  border-radius: 9999px;
  transition: width 400ms cubic-bezier(0.16, 1, 0.3, 1);
}

.checklist-steps {
  list-style: none;
  padding: 0;
  margin: var(--space-6) 0;
  display: flex;
  flex-direction: column;
  gap: 0;
}

.checklist-step {
  display: flex;
  gap: var(--space-4);
  padding-block: var(--space-4);
  border-top: 1px solid var(--color-border);
  align-items: flex-start;
}

.checklist-step__check {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: var(--color-success);
  color: white;
  display: grid;
  place-items: center;
  font-size: 0.75rem;
  flex-shrink: 0;
}

.checklist-step--done .checklist-step__content strong {
  text-decoration: line-through;
  color: var(--color-text-muted);
}

.checklist-step--active { background: oklch(from var(--color-accent) l c h / 0.04); }
.checklist-step--locked { opacity: 0.5; }

.checklist-dismiss {
  width: 100%;
  background: transparent;
  border: none;
  font-size: 0.8125rem;
  color: var(--color-text-muted);
  cursor: pointer;
  padding-top: var(--space-3);
  border-top: 1px solid var(--color-border);
  text-decoration: underline;
  text-underline-offset: 2px;
}
```

---

## Pattern C — Product Tour (contextual tooltips)

Best for: complex UIs where the value is already visible; guides users to key features.

```tsx
// Use a minimal library: driver.js or Shepherd.js
// Or implement with CSS Anchor Positioning (CSS 2026)

const tourSteps = [
  {
    target: '#create-button',
    title: 'Start here',
    body: 'Create your first project. It takes 30 seconds.',
    position: 'bottom',
  },
  {
    target: '#sidebar-projects',
    title: 'Your projects',
    body: 'All your projects appear here. Click any to open it.',
    position: 'right',
  },
  {
    target: '#invite-button',
    title: 'Invite your team',
    body: 'Collaboration is where the magic happens.',
    position: 'bottom',
  },
]
```

**Rules:**
- Maximum 5 tooltip steps (more and users click "skip" without reading)
- Each tooltip has one action or observation — not a paragraph
- Skippable at any step ("Skip tour" always visible)
- Tour restarts from settings if the user wants to revisit

---

## Onboarding Copy Rules

```
Step title:   Verb + outcome ("Name your workspace", not "Workspace Setup")
Description:  One sentence — why this step matters to the user
CTA:          Specific ("Continue to invites", not "Next")
Skip:         Always available, never shamed ("Skip for now" not "Skip and miss features")
Progress:     "Step 2 of 4" — always absolute, not percentage for ≤ 5 steps
```

---

## Anti-Patterns

- Requiring all information upfront before showing any value
- No skip option (users who skip often activate later)
- Progress bar that shows 0% on the first step (discouraging)
- "Welcome!" email as the first onboarding step (the product should onboard, not email)
- Tutorial video as a gate to using the product
- Asking for billing before the aha moment

## Related Files

- `rules/13-saas-products.md` — R1 (aha moment), R3 (MVS steps), R4 (navigation)
- `blueprints/saas-app-from-scratch.md` — Section 6: Onboarding
- `patterns/product-ui/empty-states.md` — what users see before creating first item
- `agents/ux-architect.md` — onboarding flow review
