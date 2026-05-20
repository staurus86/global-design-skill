# Blueprint — Pricing Page From Scratch

> A complete reference implementation for a SaaS pricing page. Covers structure, psychology, copy patterns, components, and trust signals — in the order a visitor encounters them.

---

## Page Structure

```
1. Nav (sticky, minimal)
2. Hero — headline + plan toggle (monthly/annual)
3. Pricing card grid (3 tiers)
4. Feature comparison table (expandable)
5. FAQ section
6. Social proof strip (logos or testimonials)
7. Final CTA section
8. Footer
```

---

## Section 1 — Hero

```html
<section class="pricing-hero">
  <div class="container">
    <div class="pricing-hero__inner">
      <span class="eyebrow">Transparent pricing</span>
      <h1 class="pricing-hero__heading">Plans for every stage of growth</h1>
      <p class="pricing-hero__sub">
        Start free, upgrade when you need more. No hidden fees. Cancel anytime.
      </p>

      <!-- Annual / monthly toggle -->
      <div class="billing-toggle" role="group" aria-label="Billing period">
        <span class="billing-toggle__label">Monthly</span>
        <button
          class="toggle-switch"
          type="button"
          role="switch"
          aria-checked="false"
          id="billing-switch"
          aria-label="Switch to annual billing"
        >
          <span class="toggle-switch__thumb"></span>
        </button>
        <span class="billing-toggle__label">
          Annual
          <span class="billing-toggle__save">Save 20%</span>
        </span>
      </div>
    </div>
  </div>
</section>
```

```css
.pricing-hero {
  padding-block: var(--space-20) var(--space-12);
  text-align: center;
  background: var(--color-surface);
}

.pricing-hero__inner {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-5);
}

.pricing-hero__heading {
  font-size: var(--text-h1);
  font-family: var(--font-display);
  font-weight: 700;
  letter-spacing: -0.02em;
  line-height: 1.1;
  color: var(--color-text-primary);
  max-width: 14ch;
}

.pricing-hero__sub {
  font-size: var(--text-body);
  color: var(--color-text-secondary);
  max-width: 44ch;
}

/* Billing toggle */
.billing-toggle {
  display: flex;
  align-items: center;
  gap: var(--space-3);
}

.billing-toggle__label {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-text-secondary);
}

.billing-toggle__save {
  padding: 2px var(--space-2);
  border-radius: var(--radius-full);
  background: var(--color-success-subtle);
  color: var(--color-success);
  font-size: 11px;
  font-weight: var(--font-weight-semibold);
}

.toggle-switch {
  position: relative;
  width: 44px; height: 24px;
  border-radius: var(--radius-full);
  background: var(--color-surface-3);
  border: 1px solid var(--color-border);
  cursor: pointer;
  transition: background var(--duration-fast) var(--ease-smooth);
}

.toggle-switch[aria-checked="true"] {
  background: var(--color-accent);
  border-color: var(--color-accent);
}

.toggle-switch__thumb {
  position: absolute;
  top: 2px; left: 2px;
  width: 18px; height: 18px;
  border-radius: var(--radius-full);
  background: var(--color-surface);
  box-shadow: var(--shadow-sm);
  transition: transform var(--duration-fast) var(--ease-spring);
}

.toggle-switch[aria-checked="true"] .toggle-switch__thumb {
  transform: translateX(20px);
}
```

```js
const billingSwitch = document.getElementById('billing-switch')
const priceEls      = document.querySelectorAll('[data-monthly][data-annual]')

billingSwitch.addEventListener('click', () => {
  const annual = billingSwitch.getAttribute('aria-checked') !== 'true'
  billingSwitch.setAttribute('aria-checked', String(annual))
  billingSwitch.setAttribute('aria-label',
    annual ? 'Switch to monthly billing' : 'Switch to annual billing')

  priceEls.forEach(el => {
    el.textContent = annual ? el.dataset.annual : el.dataset.monthly
  })
})
```

---

## Section 2 — Pricing Cards

See `patterns/marketing-blocks/comparison-sections.md` Pattern 1 for the full card implementation.

**Copy rules for pricing cards:**

```
Plan name:   Single word, no adjectives ("Starter", "Pro", not "Basic Starter")
Tagline:     Who it's for, not what it includes ("For individuals", not "Basic features")
Price:       Show monthly equivalent even when billed annually
CTA text:    Outcome-oriented, differentiated by plan:
               Starter → "Start for free"
               Pro     → "Start 14-day trial"
               Enterprise → "Talk to sales"
```

---

## Section 3 — Feature Comparison Table

See `patterns/marketing-blocks/comparison-sections.md` Pattern 2 for the full table implementation.

**Grouping strategy:**

```
Group features by user goal, not by product area:
  Good grouping:
    "Deployment" — everything needed to ship code
    "Collaboration" — team and permission features
    "Observability" — logs, metrics, alerts
    "Support" — SLAs, channels, response times

  Bad grouping:
    "Core features" (meaningless)
    "Advanced features" (elitist)
    "Enterprise" (discourages mid-market)
```

---

## Section 4 — FAQ

```html
<section class="faq-section" aria-labelledby="faq-heading">
  <div class="container faq-section__container">
    <h2 class="faq-section__heading" id="faq-heading">Common questions</h2>

    <dl class="faq-list">

      <div class="faq-item">
        <dt>
          <button
            class="faq-trigger"
            type="button"
            aria-expanded="false"
            aria-controls="faq-1"
          >
            Can I change plans at any time?
            <svg class="faq-trigger__icon" aria-hidden="true" width="16" height="16"
              viewBox="0 0 16 16" fill="none" stroke="currentColor"
              stroke-width="1.5" stroke-linecap="round">
              <path d="M3 6l5 5 5-5"/>
            </svg>
          </button>
        </dt>
        <dd class="faq-answer" id="faq-1" hidden>
          <div class="faq-answer__inner">
            Yes. Upgrade or downgrade at any time from your billing settings.
            Upgrades take effect immediately. Downgrades take effect at the end of your billing period.
          </div>
        </dd>
      </div>

      <div class="faq-item">
        <dt>
          <button class="faq-trigger" type="button" aria-expanded="false" aria-controls="faq-2">
            What happens when my trial ends?
            <svg class="faq-trigger__icon" aria-hidden="true" width="16" height="16"
              viewBox="0 0 16 16" fill="none" stroke="currentColor"
              stroke-width="1.5" stroke-linecap="round">
              <path d="M3 6l5 5 5-5"/>
            </svg>
          </button>
        </dt>
        <dd class="faq-answer" id="faq-2" hidden>
          <div class="faq-answer__inner">
            At the end of your 14-day trial, your projects remain active on the Starter plan.
            You will not be charged unless you add a payment method and upgrade.
          </div>
        </dd>
      </div>

    </dl>
  </div>
</section>
```

```css
.faq-section { padding-block: var(--space-20); background: var(--color-surface-2); }

.faq-section__container {
  max-width: 680px;
  margin-inline: auto;
  display: flex;
  flex-direction: column;
  gap: var(--space-10);
}

.faq-section__heading {
  font-size: var(--text-h2);
  font-family: var(--font-display);
  font-weight: 700;
  letter-spacing: -0.02em;
  color: var(--color-text-primary);
  text-align: center;
}

.faq-list { display: flex; flex-direction: column; }

.faq-item {
  border-top: 1px solid var(--color-border);
}

.faq-item:last-child { border-bottom: 1px solid var(--color-border); }

.faq-trigger {
  display: flex;
  width: 100%;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-4);
  padding: var(--space-5) 0;
  background: transparent;
  border: none;
  text-align: left;
  font-size: var(--text-body);
  font-weight: var(--font-weight-medium);
  color: var(--color-text-primary);
  cursor: pointer;
}

.faq-trigger:hover { color: var(--color-accent); }

.faq-trigger__icon {
  flex-shrink: 0;
  transition: transform var(--duration-fast) var(--ease-spring);
}

.faq-trigger[aria-expanded="true"] .faq-trigger__icon {
  transform: rotate(180deg);
}

.faq-answer[hidden] { display: none; }

.faq-answer__inner {
  padding-bottom: var(--space-5);
  font-size: var(--text-body);
  color: var(--color-text-secondary);
  line-height: 1.65;
}
```

```js
document.querySelectorAll('.faq-trigger').forEach(trigger => {
  trigger.addEventListener('click', () => {
    const open   = trigger.getAttribute('aria-expanded') === 'true'
    const answer = document.getElementById(trigger.getAttribute('aria-controls'))
    trigger.setAttribute('aria-expanded', String(!open))
    answer.hidden = open
  })
})
```

---

## Section 5 — Trust Signals Strip

```html
<section class="trust-strip" aria-label="Trusted by leading teams">
  <div class="container trust-strip__container">
    <p class="trust-strip__label">Trusted by engineering teams at</p>
    <div class="trust-strip__logos" aria-hidden="true">
      <!-- Use real SVG logos or img with alt="" -->
      <img src="/logos/vercel.svg"   alt="" width="80"  height="24" loading="lazy" />
      <img src="/logos/stripe.svg"   alt="" width="70"  height="24" loading="lazy" />
      <img src="/logos/notion.svg"   alt="" width="80"  height="24" loading="lazy" />
      <img src="/logos/supabase.svg" alt="" width="100" height="24" loading="lazy" />
      <img src="/logos/linear.svg"   alt="" width="70"  height="24" loading="lazy" />
    </div>
  </div>
</section>
```

```css
.trust-strip {
  padding-block: var(--space-12);
  border-block: 1px solid var(--color-border);
  text-align: center;
}

.trust-strip__container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-5);
}

.trust-strip__label {
  font-size: var(--text-sm);
  color: var(--color-text-muted);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-weight: var(--font-weight-medium);
}

.trust-strip__logos {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  gap: var(--space-8);
  filter: grayscale(1);
  opacity: 0.5;
}

.trust-strip__logos img { height: 24px; width: auto; object-fit: contain; }
```

---

## Section 6 — Final CTA

```html
<section class="pricing-cta" aria-labelledby="cta-heading">
  <div class="container pricing-cta__inner">
    <h2 class="pricing-cta__heading" id="cta-heading">
      Ready to deploy 3x faster?
    </h2>
    <p class="pricing-cta__sub">
      Start free, no credit card required. 14-day Pro trial available on signup.
    </p>
    <div class="pricing-cta__actions">
      <a href="/signup" class="btn btn--primary btn--lg">Get started free</a>
      <a href="/demo" class="btn btn--ghost btn--lg">Book a demo</a>
    </div>
  </div>
</section>
```

---

## Pricing Psychology Checklist

```
[ ] Primary CTA on featured (middle) plan — visual center of attention
[ ] Annual discount visible at hero — anchors full price, shows savings
[ ] Free tier exists and is prominent — reduces friction to signup
[ ] "No credit card required" on free/trial CTA
[ ] "Cancel anytime" near paid plan CTAs
[ ] Enterprise plan CTA leads to sales call, not self-serve signup
[ ] Social proof logos are real, high-profile, recognizable
[ ] FAQ answers real objections — not invented edge cases
[ ] Price per month shown even for annual billing
[ ] Downgrade path described — reduces upgrade anxiety
```

---

*Blueprint version: global-design-skill v1.0 — `blueprints/pricing-page-from-scratch.md`*  
*Related: `patterns/marketing-blocks/comparison-sections.md`, `agents/copy-editor.md`, `skills/global-design/operating-principles.md`*
