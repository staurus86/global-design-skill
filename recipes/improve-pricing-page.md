# Recipe — Improve a Pricing Page

> Pricing pages have one job: remove the hesitation to click "Buy." Every element either reduces hesitation or adds it. Audit which is which, then remove the friction and amplify the confidence.

---

## When to use

- Pricing page conversion < 5% of visitors
- Users visit pricing and leave without clicking any CTA
- "Which plan should I choose?" is a frequent support question
- Annual plan uptake < 25% (default billing is monthly)
- Too many plans with unclear differentiation

---

## Diagnosis: Pricing Page Failures

```
[ ] Monthly pricing shown by default (annual is better for revenue)
[ ] No recommended plan (users must decide alone)
[ ] Feature table has > 15 rows (cognitive overload)
[ ] Features described by name only — no outcome context
[ ] Free plan hides paid plan value
[ ] No social proof near CTA
[ ] Enterprise plan says "Contact sales" only (no starting price range)
[ ] CTA says "Get Started" or "Subscribe" (generic)
[ ] Annual savings not shown with monthly toggle
[ ] No money-back guarantee or trial length near CTA
[ ] FAQ section missing or generic
[ ] Mobile: plans shown in a scrollable row (invisible)
```

---

## Step 1 — Set Annual as Default

Annual default increases revenue and signals confidence.

```html
<!-- Toggle: annual by default -->
<div class="billing-toggle" role="group" aria-label="Billing period">
  <button
    class="toggle-btn"
    data-period="monthly"
    aria-pressed="false"
  >Monthly</button>

  <button
    class="toggle-btn toggle-btn--active"
    data-period="annual"
    aria-pressed="true"
  >
    Annual
    <span class="toggle-badge">Save 20%</span>
  </button>
</div>
```

```css
.billing-toggle {
  display: inline-flex;
  background: var(--color-surface-2);
  border: 1px solid var(--color-border);
  border-radius: 9999px;
  padding: 4px;
  gap: 2px;
  margin-bottom: var(--space-10);
}

.toggle-btn {
  height: 36px;
  padding-inline: var(--space-5);
  border-radius: 9999px;
  background: transparent;
  border: none;
  cursor: pointer;
  font-size: 0.9375rem;
  font-weight: 500;
  color: var(--color-text-muted);
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  transition: background 150ms, color 150ms;
}

.toggle-btn--active {
  background: var(--color-surface);
  color: var(--color-text-primary);
  box-shadow: 0 1px 4px oklch(0% 0 0 / 0.1);
}

.toggle-badge {
  font-size: 0.6875rem;
  font-weight: 600;
  background: oklch(from var(--color-success) l c h / 0.15);
  color: var(--color-success);
  padding: 0.1em 0.5em;
  border-radius: 9999px;
}
```

```js
// Price switching
const toggle = document.querySelector('.billing-toggle')
toggle.addEventListener('click', e => {
  const btn = e.target.closest('.toggle-btn')
  if (!btn) return
  const period = btn.dataset.period

  // Update toggle state
  toggle.querySelectorAll('.toggle-btn').forEach(b => {
    b.classList.toggle('toggle-btn--active', b === btn)
    b.setAttribute('aria-pressed', b === btn ? 'true' : 'false')
  })

  // Update all prices
  document.querySelectorAll('[data-price-monthly]').forEach(el => {
    el.textContent = period === 'annual'
      ? el.dataset.priceAnnual
      : el.dataset.priceMonthly
  })

  // Update billing note
  document.querySelectorAll('[data-billing-note]').forEach(el => {
    el.textContent = period === 'annual'
      ? 'Billed annually'
      : 'Billed monthly'
  })
})
```

---

## Step 2 — Mark the Recommended Plan

Without a recommendation, the user must make a decision. Remove that burden.

```html
<div class="pricing-grid">

  <!-- Starter -->
  <div class="plan-card">
    <!-- no badge -->
    ...
  </div>

  <!-- Pro — Recommended -->
  <div class="plan-card plan-card--featured" aria-label="Pro plan — most popular">
    <div class="plan-badge">Most popular</div>
    ...
  </div>

  <!-- Enterprise -->
  <div class="plan-card">
    ...
  </div>

</div>
```

```css
.pricing-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--space-5);
  align-items: start;
}

.plan-card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-2xl);
  padding: var(--space-8);
  position: relative;
  transition: box-shadow 200ms;
}

/* Featured card: slightly scaled, different border */
.plan-card--featured {
  border-color: var(--color-accent);
  box-shadow: 0 0 0 1px var(--color-accent),
              0 8px 32px oklch(from var(--color-accent) l c h / 0.15);
  transform: scale(1.03);
  transform-origin: top center;
  z-index: 1;
}

/* Badge positioned above the card */
.plan-badge {
  position: absolute;
  top: -14px;
  left: 50%;
  translate: -50% 0;
  background: var(--color-accent);
  color: oklch(10% 0.01 258);
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  padding: 0.25rem 0.875rem;
  border-radius: 9999px;
  white-space: nowrap;
}

@media (max-width: 768px) {
  .pricing-grid {
    grid-template-columns: 1fr;
    max-width: 420px;
    margin-inline: auto;
  }
  .plan-card--featured { transform: none; }
}
```

---

## Step 3 — Price Anchoring (Show Most Expensive First)

Reading left-to-right, the first price anchors perception. Show the highest price first.

```
[ Enterprise $299 ] [ Pro $79 — featured ] [ Starter $29 ]
```

This makes Pro feel reasonable after seeing Enterprise. If you show Starter first, Pro feels expensive.

**Mobile exception:** On mobile (stacked), show the featured plan first.

---

## Step 4 — Trim the Feature Table

More than 12 features in a comparison table causes abandonment.

**Rules:**
- Show only differentiating features (not things all plans share)
- Group by outcome, not feature category
- Use outcomes, not feature names

| Before (feature-name) | After (outcome-focused) |
|---|---|
| "API rate limit: 100/min" | "API calls: 100/min · 1,000/min · Unlimited" |
| "Webhooks" | "Webhooks ✓" |
| "SSO support" | "Single sign-on (SSO)" |
| "Data export" | "Export to CSV, Excel, JSON" |

```html
<!-- Feature row: three-column diff -->
<tr class="feature-row">
  <td class="feature-name">Team members</td>
  <td class="plan-cell">Up to 3</td>
  <td class="plan-cell plan-cell--featured">Up to 25</td>
  <td class="plan-cell">Unlimited</td>
</tr>

<!-- Section divider in table -->
<tr class="feature-section-header">
  <td colspan="4">Security & Access</td>
</tr>
```

---

## Step 5 — Add Social Proof Next to CTA

The decision moment is at the CTA. That's where proof must be.

```html
<div class="plan-cta">
  <a href="/signup?plan=pro" class="btn-primary btn-lg btn-full">
    Start Pro free for 14 days
  </a>
  <p class="plan-proof">
    No credit card required · Cancel anytime
  </p>
  <div class="plan-rating">
    <!-- Stars -->
    <span class="stars" aria-label="4.9 out of 5">★★★★★</span>
    <span class="rating-text">4.9/5 from 2,847 reviews</span>
  </div>
</div>
```

```css
.plan-cta {
  margin-top: var(--space-8);
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
}

.plan-proof {
  text-align: center;
  font-size: 0.8125rem;
  color: var(--color-text-muted);
}

.plan-rating {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-2);
  font-size: 0.8125rem;
  color: var(--color-text-muted);
}

.stars {
  color: oklch(75% 0.18 85);  /* warm gold */
  font-size: 0.875rem;
  letter-spacing: -0.02em;
}
```

---

## Step 6 — CTA Copy Formula

`[Verb] [plan] [for free/N days]`

| Before (generic) | After (specific) |
|---|---|
| "Get Started" | "Start Pro free for 14 days" |
| "Subscribe" | "Upgrade to Pro" |
| "Choose Plan" | "Start with Starter" |
| "Contact Us" | "Talk to sales — we respond in 2 hours" |

---

## Step 7 — Handle the Enterprise Row

"Contact sales" with no price range creates uncertainty. Give a range or anchor.

```html
<div class="enterprise-section">
  <div class="enterprise-content">
    <h3>Enterprise</h3>
    <p>Custom contracts, SLAs, and dedicated support for teams of 200+.</p>
    <ul class="enterprise-features">
      <li>Custom seat pricing (starts at $199/month)</li>
      <li>99.99% SLA with dedicated support</li>
      <li>SOC 2 Type II, HIPAA, GDPR</li>
      <li>SSO, SAML, custom roles</li>
    </ul>
  </div>
  <div class="enterprise-cta">
    <a href="/enterprise" class="btn-primary">Talk to sales</a>
    <p>We respond within 2 business hours</p>
  </div>
</div>
```

---

## Step 8 — Add an Objection-Handling FAQ

FAQs near pricing answer the hesitation, not the product:

1. "Can I change plans later?" (Yes, upgrade/downgrade anytime)
2. "What happens after my trial?" (You'll be asked to choose a plan; nothing is lost)
3. "Do you offer refunds?" (30-day money-back, no questions asked)
4. "Is my data safe if I cancel?" (30-day export window)
5. "Do you have a free plan?" (Yes / No — be direct)

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can I change plans after signing up?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. You can upgrade or downgrade at any time. Upgrades apply immediately; downgrades apply at the end of your current billing period."
      }
    }
  ]
}
```

---

## Acceptance Criteria

```
[ ] Annual is default billing period
[ ] Annual savings percentage visible on toggle
[ ] One plan is visually recommended (badge, scale, or border)
[ ] Feature table ≤ 12 differentiating rows
[ ] Social proof (rating or testimonial) adjacent to each CTA
[ ] CTA label follows Verb + Plan + Trial formula
[ ] Enterprise section shows price range or anchor
[ ] FAQ section addresses ≥ 5 real hesitations
[ ] FAQPage schema markup present
[ ] Mobile: plans stack vertically, featured plan first
[ ] No plan's CTA uses "Get Started" or "Subscribe"
```

---

*Recipe version: global-design-skill v1.0 — `recipes/improve-pricing-page.md`*
*Related: `rules/14-landing-pages.md`, `patterns/marketing-blocks/pricing-sections.md`, `agents/conversion-designer.md`*
