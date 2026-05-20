# Pattern — Comparison Sections

> Comparison sections help users make a decision: pricing tiers, plan features, before/after states, or product vs. competitors. The goal is to reduce perceived risk and accelerate commitment.

---

## Decision: What Type of Comparison?

```
Pricing tiers (2–4 plans)        → Pricing card grid (Pattern 1)
Feature matrix (5+ features)     → Feature comparison table (Pattern 2)
Before / After state              → Split comparison (Pattern 3)
Product vs. competitors           → Competitor matrix (Pattern 4, variant of 2)
```

---

## Pattern 1 — Pricing Card Grid

Standard 3-tier layout with a recommended/popular plan highlighted.

```html
<section class="pricing-section">
  <div class="pricing-section__eyebrow-wrap">
    <span class="eyebrow">Simple pricing</span>
  </div>
  <h2 class="pricing-section__heading">Plans that scale with your team</h2>
  <p class="pricing-section__sub">Start free. Upgrade when you need more.</p>

  <div class="pricing-grid">

    <!-- Starter -->
    <div class="pricing-card">
      <div class="pricing-card__header">
        <p class="pricing-card__name">Starter</p>
        <div class="pricing-card__price">
          <span class="pricing-card__amount">$0</span>
          <span class="pricing-card__period">/month</span>
        </div>
        <p class="pricing-card__desc">For individuals and small projects.</p>
      </div>
      <ul class="pricing-card__features">
        <li class="pricing-card__feature pricing-card__feature--yes">5 projects</li>
        <li class="pricing-card__feature pricing-card__feature--yes">1 GB storage</li>
        <li class="pricing-card__feature pricing-card__feature--yes">Community support</li>
        <li class="pricing-card__feature pricing-card__feature--no">Custom domains</li>
        <li class="pricing-card__feature pricing-card__feature--no">Team collaboration</li>
        <li class="pricing-card__feature pricing-card__feature--no">Analytics</li>
      </ul>
      <a href="/signup" class="btn btn--secondary btn--full">Get started free</a>
    </div>

    <!-- Pro — highlighted -->
    <div class="pricing-card pricing-card--featured" aria-label="Recommended plan">
      <div class="pricing-card__badge">Most popular</div>
      <div class="pricing-card__header">
        <p class="pricing-card__name">Pro</p>
        <div class="pricing-card__price">
          <span class="pricing-card__amount">$29</span>
          <span class="pricing-card__period">/month</span>
        </div>
        <p class="pricing-card__desc">For growing teams that need more control.</p>
      </div>
      <ul class="pricing-card__features">
        <li class="pricing-card__feature pricing-card__feature--yes">Unlimited projects</li>
        <li class="pricing-card__feature pricing-card__feature--yes">50 GB storage</li>
        <li class="pricing-card__feature pricing-card__feature--yes">Priority support</li>
        <li class="pricing-card__feature pricing-card__feature--yes">Custom domains</li>
        <li class="pricing-card__feature pricing-card__feature--yes">Team collaboration (up to 10)</li>
        <li class="pricing-card__feature pricing-card__feature--no">Analytics</li>
      </ul>
      <a href="/signup?plan=pro" class="btn btn--primary btn--full">Start 14-day trial</a>
    </div>

    <!-- Enterprise -->
    <div class="pricing-card">
      <div class="pricing-card__header">
        <p class="pricing-card__name">Enterprise</p>
        <div class="pricing-card__price">
          <span class="pricing-card__amount">Custom</span>
        </div>
        <p class="pricing-card__desc">For large teams with advanced needs.</p>
      </div>
      <ul class="pricing-card__features">
        <li class="pricing-card__feature pricing-card__feature--yes">Unlimited projects</li>
        <li class="pricing-card__feature pricing-card__feature--yes">Unlimited storage</li>
        <li class="pricing-card__feature pricing-card__feature--yes">Dedicated support</li>
        <li class="pricing-card__feature pricing-card__feature--yes">Custom domains</li>
        <li class="pricing-card__feature pricing-card__feature--yes">Unlimited team members</li>
        <li class="pricing-card__feature pricing-card__feature--yes">Advanced analytics + SSO</li>
      </ul>
      <a href="/contact" class="btn btn--secondary btn--full">Contact sales</a>
    </div>

  </div>
</section>
```

```css
.pricing-section {
  padding-block: var(--space-24);
  text-align: center;
}

.pricing-section__eyebrow-wrap { margin-bottom: var(--space-5); }
.pricing-section__heading {
  font-size: var(--text-h1);
  font-family: var(--font-display);
  font-weight: 700;
  color: var(--color-text-primary);
  line-height: 1.1;
  letter-spacing: -0.02em;
  margin-bottom: var(--space-4);
}
.pricing-section__sub {
  font-size: var(--text-body);
  color: var(--color-text-secondary);
  margin-bottom: var(--space-12);
  max-width: 44ch;
  margin-inline: auto;
}

.pricing-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--space-6);
  align-items: start;
  max-width: 960px;
  margin-inline: auto;
}

.pricing-card {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: var(--space-6);
  padding: var(--space-8);
  background: var(--color-surface-2);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  text-align: left;
}

.pricing-card--featured {
  background: var(--color-surface);
  border-color: var(--color-accent);
  box-shadow: 0 0 0 3px oklch(from var(--color-accent) l c h / 0.15), var(--shadow-lg);
  transform: scale(1.02);
  z-index: 1;
}

.pricing-card__badge {
  position: absolute;
  top: calc(-1px - var(--space-3));
  left: 50%;
  transform: translateX(-50%);
  padding: var(--space-1) var(--space-3);
  border-radius: var(--radius-full);
  background: var(--color-accent);
  color: var(--color-text-inverse);
  font-size: 12px;
  font-weight: var(--font-weight-semibold);
  letter-spacing: 0.04em;
  white-space: nowrap;
}

.pricing-card__name {
  font-size: var(--text-sm);
  font-weight: var(--font-weight-semibold);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--color-text-secondary);
}

.pricing-card__price {
  display: flex;
  align-items: baseline;
  gap: var(--space-1);
  margin-block: var(--space-2);
}

.pricing-card__amount {
  font-size: var(--text-display);
  font-family: var(--font-display);
  font-weight: 700;
  letter-spacing: -0.03em;
  color: var(--color-text-primary);
}

.pricing-card__period {
  font-size: var(--text-sm);
  color: var(--color-text-muted);
}

.pricing-card__desc {
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
  line-height: 1.5;
}

.pricing-card__features {
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
  flex: 1;
  list-style: none;
  padding: 0;
  margin: 0;
}

.pricing-card__feature {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
}

.pricing-card__feature::before {
  content: '';
  display: block;
  width: 16px; height: 16px;
  border-radius: var(--radius-full);
  flex-shrink: 0;
  background-size: contain;
  background-repeat: no-repeat;
}

.pricing-card__feature--yes::before {
  background-color: var(--color-success-subtle);
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='10' viewBox='0 0 24 24' fill='none' stroke='%2322c55e' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6L9 17l-5-5'/%3E%3C/svg%3E");
  background-position: center;
}

.pricing-card__feature--no {
  color: var(--color-text-disabled);
}

.pricing-card__feature--no::before {
  background-color: var(--color-surface-3);
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='8' height='8' viewBox='0 0 24 24' fill='none' stroke='%236b7280' stroke-width='2' stroke-linecap='round'%3E%3Cpath d='M5 12h14'/%3E%3C/svg%3E");
  background-position: center;
}

.btn--full { width: 100%; justify-content: center; }

@media (max-width: 900px) {
  .pricing-grid { grid-template-columns: 1fr; max-width: 400px; }
  .pricing-card--featured { transform: none; }
}
```

---

## Pattern 2 — Feature Comparison Table

For 5+ features with fine-grained tier differences.

```html
<div class="comparison-table-wrap" role="region" aria-label="Feature comparison" tabindex="0">
  <table class="comparison-table">
    <caption class="sr-only">Feature comparison across Starter, Pro, and Enterprise plans</caption>
    <thead>
      <tr>
        <th class="comparison-table__label-col" scope="col"></th>
        <th scope="col">
          <div class="comparison-table__plan">Starter</div>
          <div class="comparison-table__plan-price">Free</div>
        </th>
        <th scope="col" class="comparison-table__plan-col--featured">
          <div class="comparison-table__plan">Pro</div>
          <div class="comparison-table__plan-price">$29/mo</div>
        </th>
        <th scope="col">
          <div class="comparison-table__plan">Enterprise</div>
          <div class="comparison-table__plan-price">Custom</div>
        </th>
      </tr>
    </thead>
    <tbody>
      <tr class="comparison-table__section-row">
        <td colspan="4" class="comparison-table__section">Deployment</td>
      </tr>
      <tr>
        <td class="comparison-table__feature">Projects</td>
        <td>5</td>
        <td class="comparison-table__plan-col--featured">Unlimited</td>
        <td>Unlimited</td>
      </tr>
      <tr>
        <td class="comparison-table__feature">Custom domains</td>
        <td><span class="check check--no" aria-label="Not included">—</span></td>
        <td class="comparison-table__plan-col--featured"><span class="check check--yes" aria-label="Included">✓</span></td>
        <td><span class="check check--yes" aria-label="Included">✓</span></td>
      </tr>
      <tr>
        <td class="comparison-table__feature">Build minutes</td>
        <td>300 min/mo</td>
        <td class="comparison-table__plan-col--featured">6,000 min/mo</td>
        <td>Unlimited</td>
      </tr>
    </tbody>
    <tfoot>
      <tr>
        <td></td>
        <td><a href="/signup" class="btn btn--secondary btn--sm">Get started</a></td>
        <td class="comparison-table__plan-col--featured">
          <a href="/signup?plan=pro" class="btn btn--primary btn--sm">Start trial</a>
        </td>
        <td><a href="/contact" class="btn btn--secondary btn--sm">Contact sales</a></td>
      </tr>
    </tfoot>
  </table>
</div>
```

```css
.comparison-table-wrap {
  overflow-x: auto;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  max-width: 900px;
  margin-inline: auto;
}

.comparison-table {
  width: 100%;
  border-collapse: collapse;
  font-size: var(--text-sm);
}

.comparison-table thead th {
  padding: var(--space-5) var(--space-6);
  text-align: center;
  border-bottom: 1px solid var(--color-border);
  background: var(--color-surface-2);
}

.comparison-table__label-col { width: 40%; text-align: left; }

.comparison-table__plan {
  font-size: var(--text-body);
  font-weight: var(--font-weight-semibold);
  color: var(--color-text-primary);
}

.comparison-table__plan-price {
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
  margin-top: var(--space-1);
}

.comparison-table__plan-col--featured {
  background: oklch(from var(--color-accent) l c h / 0.04);
  border-inline: 1px solid oklch(from var(--color-accent) l c h / 0.2);
}

.comparison-table tbody td {
  padding: var(--space-4) var(--space-6);
  text-align: center;
  border-bottom: 1px solid var(--color-border);
  color: var(--color-text-secondary);
}

.comparison-table__feature {
  text-align: left;
  color: var(--color-text-primary);
}

.comparison-table__section-row td {
  background: var(--color-surface-3);
  padding: var(--space-2) var(--space-6);
}

.comparison-table__section {
  font-size: 11px;
  font-weight: var(--font-weight-semibold);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--color-text-muted);
}

.comparison-table tfoot td {
  padding: var(--space-5) var(--space-6);
  text-align: center;
}

.check--yes { color: var(--color-success); font-size: 16px; }
.check--no  { color: var(--color-text-muted); }

.sr-only {
  position: absolute; width: 1px; height: 1px;
  padding: 0; margin: -1px; overflow: hidden;
  clip: rect(0,0,0,0); white-space: nowrap; border: 0;
}
```

---

## Anti-Patterns

```
× More than 4 pricing tiers — too many options cause decision paralysis
× No recommended/popular plan — users don't know where to start
× Hiding price — "Contact sales" on all plans signals opacity
× CTA text identical on all plans ("Get started") — differentiate by plan goal
× Comparison table without sticky column headers on mobile
× Features listed as product names, not user outcomes
× Showing 20+ features in pricing cards — use table for detail, cards for overview
```

---

*Pattern version: global-design-skill v1.0 — `patterns/marketing-blocks/comparison-sections.md`*  
*Related: `patterns/marketing-blocks/feature-sections.md`, `patterns/marketing-blocks/stats-sections.md`, `skills/global-design/operating-principles.md`*
