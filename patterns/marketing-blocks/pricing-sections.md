# Pattern — Pricing Sections

> Pricing is a conversion decision, not a layout decision. The design must eliminate confusion and guide the user to the right tier without decision paralysis.

---

## Decision Framework

Before designing:
```
Tiers: [how many? maximum 3 for consumer/SMB; unlimited for enterprise list]
Billing toggle: [monthly/annual? default to annual if you want to show it]
Target tier: [which tier do you want most users to choose?]
Enterprise path: [contact form / Calendly / chat?]
Risk reversal: [free trial? money-back guarantee? cancel anytime?]
```

---

## Pattern A — Three-Tier Cards (standard)

Best for: SaaS with clear tier progression, B2B tools, subscription products.

```html
<section class="pricing">
  <div class="container">
    <div class="pricing__header">
      <span class="eyebrow">Pricing</span>
      <h2>Simple, transparent pricing</h2>
      <p>Start free. Upgrade when you're ready.</p>

      <!-- Billing toggle -->
      <div class="pricing__toggle" role="group" aria-label="Billing period">
        <button
          class="toggle-btn"
          aria-pressed="false"
          data-period="monthly"
        >Monthly</button>
        <button
          class="toggle-btn toggle-btn--active"
          aria-pressed="true"
          data-period="annual"
        >Annual <span class="save-badge">Save 20%</span></button>
      </div>
    </div>

    <div class="pricing__grid">
      <!-- Tier 1: Starter -->
      <div class="pricing-card">
        <div class="pricing-card__header">
          <h3 class="pricing-card__name">Starter</h3>
          <p class="pricing-card__desc">For individuals and small projects</p>
        </div>
        <div class="pricing-card__price">
          <span class="price-amount" data-monthly="29" data-annual="23">$23</span>
          <span class="price-period">/month</span>
        </div>
        <p class="price-billing">Billed $276/year</p>
        <a href="/signup?plan=starter" class="btn-ghost btn-full">Get started</a>
        <ul class="pricing-card__features">
          <li><span aria-hidden="true">✓</span> 5 projects</li>
          <li><span aria-hidden="true">✓</span> 10GB storage</li>
          <li><span aria-hidden="true">✓</span> Email support</li>
        </ul>
      </div>

      <!-- Tier 2: Growth (recommended) -->
      <div class="pricing-card pricing-card--featured">
        <div class="pricing-card__badge">Most popular</div>
        <div class="pricing-card__header">
          <h3 class="pricing-card__name">Growth</h3>
          <p class="pricing-card__desc">For growing teams that need more</p>
        </div>
        <div class="pricing-card__price">
          <span class="price-amount" data-monthly="79" data-annual="63">$63</span>
          <span class="price-period">/month</span>
        </div>
        <p class="price-billing">Billed $756/year</p>
        <a href="/signup?plan=growth" class="btn-primary btn-full">Start 14-day trial</a>
        <ul class="pricing-card__features">
          <li><span aria-hidden="true">✓</span> Unlimited projects</li>
          <li><span aria-hidden="true">✓</span> 100GB storage</li>
          <li><span aria-hidden="true">✓</span> Priority support</li>
          <li><span aria-hidden="true">✓</span> Team collaboration</li>
          <li><span aria-hidden="true">✓</span> Advanced analytics</li>
        </ul>
      </div>

      <!-- Tier 3: Enterprise -->
      <div class="pricing-card">
        <div class="pricing-card__header">
          <h3 class="pricing-card__name">Enterprise</h3>
          <p class="pricing-card__desc">Custom pricing for large teams</p>
        </div>
        <div class="pricing-card__price">
          <span class="price-custom">Custom</span>
        </div>
        <p class="price-billing">Volume discounts available</p>
        <a href="/contact-sales" class="btn-ghost btn-full">Talk to sales</a>
        <ul class="pricing-card__features">
          <li><span aria-hidden="true">✓</span> Everything in Growth</li>
          <li><span aria-hidden="true">✓</span> SSO / SAML</li>
          <li><span aria-hidden="true">✓</span> SLA guarantee</li>
          <li><span aria-hidden="true">✓</span> Dedicated CSM</li>
          <li><span aria-hidden="true">✓</span> Custom contracts</li>
        </ul>
      </div>
    </div>

    <!-- Risk reversal below the grid -->
    <p class="pricing__guarantee">
      All plans include a 30-day money-back guarantee. No questions asked.
    </p>
  </div>
</section>
```

```css
.pricing__grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--space-4);
  margin-top: var(--space-12);
}

@media (min-width: 768px) {
  .pricing__grid {
    grid-template-columns: repeat(3, 1fr);
    align-items: start;
  }
}

.pricing-card {
  position: relative;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  padding: var(--space-8);
}

.pricing-card--featured {
  background: var(--color-base);
  border-color: var(--color-accent);
  /* Scale up to visually emphasize */
  transform: scale(1.04);
  box-shadow: 0 8px 40px oklch(0% 0 0 / 0.2);
}

.pricing-card__badge {
  position: absolute;
  top: -14px;
  left: 50%;
  translate: -50% 0;
  background: var(--color-accent);
  color: oklch(10% 0.01 258);
  font-size: 0.75rem;
  font-weight: 600;
  padding: 0.25rem 0.875rem;
  border-radius: 9999px;
  white-space: nowrap;
}

.price-amount {
  font-size: clamp(2rem, 3vw, 3rem);
  font-weight: 700;
  letter-spacing: -0.02em;
}

.btn-full { width: 100%; justify-content: center; margin-block: var(--space-6); }

.pricing-card__features {
  list-style: none;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
  font-size: 0.9375rem;
}
```

**Billing toggle behavior:**
```tsx
const [period, setPeriod] = useState<'monthly' | 'annual'>('annual')

// Update all prices on toggle
const prices = { monthly: { starter: 29, growth: 79 }, annual: { starter: 23, growth: 63 } }
```

---

## Pattern B — Horizontal Comparison Table

Best for: products with many features, when users need detailed feature comparison.

```html
<div class="pricing-table">
  <table>
    <thead>
      <tr>
        <th scope="col">Feature</th>
        <th scope="col">Starter <span>$23/mo</span></th>
        <th scope="col" class="col-featured">Growth <span>$63/mo</span></th>
        <th scope="col">Enterprise <span>Custom</span></th>
      </tr>
    </thead>
    <tbody>
      <tr class="pricing-table__group">
        <td colspan="4">Core features</td>
      </tr>
      <tr>
        <th scope="row">Projects</th>
        <td>5</td>
        <td class="col-featured">Unlimited</td>
        <td>Unlimited</td>
      </tr>
      <tr>
        <th scope="row">Team members</th>
        <td>1</td>
        <td class="col-featured">Up to 25</td>
        <td>Unlimited</td>
      </tr>
      <tr>
        <th scope="row">SSO / SAML</th>
        <td><span class="check-no" aria-label="Not included">—</span></td>
        <td class="col-featured"><span class="check-no" aria-label="Not included">—</span></td>
        <td><span class="check-yes" aria-label="Included">✓</span></td>
      </tr>
    </tbody>
  </table>
</div>
```

```css
.pricing-table { overflow-x: auto; }

.pricing-table table {
  width: 100%;
  border-collapse: collapse;
  min-width: 600px;
}

.pricing-table th, .pricing-table td {
  padding: var(--space-3) var(--space-4);
  border-bottom: 1px solid var(--color-border);
  text-align: center;
}

.pricing-table th[scope="row"] { text-align: left; font-weight: 400; }

.col-featured { background: oklch(from var(--color-accent) l c h / 0.06); }

.pricing-table__group td {
  font-weight: 600;
  font-size: 0.875rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  padding-top: var(--space-6);
  color: var(--color-text-muted);
}

.check-yes { color: var(--color-success); }
.check-no  { color: var(--color-text-muted); }
```

---

## Pattern C — Freemium + Upgrade CTA

Best for: products with a free tier, usage-based pricing, developer tools.

```html
<section class="pricing-freemium">
  <div class="container">
    <div class="pricing-freemium__grid">
      <!-- Free tier -->
      <div class="freemium-card freemium-card--free">
        <h3>Free</h3>
        <p class="freemium-price">$0 <span>forever</span></p>
        <p>Everything you need to get started.</p>
        <a href="/signup" class="btn-ghost btn-full">Create free account</a>
        <ul>
          <li>3 projects</li>
          <li>1 team member</li>
          <li>Community support</li>
        </ul>
      </div>

      <!-- Paid tiers (compact) -->
      <div class="freemium-card freemium-card--paid">
        <div class="freemium-upgrade">
          <h3>Pro — $29/month</h3>
          <p>Unlimited projects. Priority support. Team features.</p>
          <a href="/upgrade" class="btn-primary">Upgrade to Pro</a>
        </div>
        <div class="freemium-upgrade freemium-upgrade--enterprise">
          <h3>Enterprise — Custom</h3>
          <p>SSO, SLA, dedicated support, custom contracts.</p>
          <a href="/sales" class="btn-ghost">Talk to sales</a>
        </div>
      </div>
    </div>
  </div>
</section>
```

---

## Psychological Principles

**Price anchoring:** Show the most expensive option first (left to right on desktop) so the middle tier feels reasonable.

**Decoy effect:** The middle tier (Growth) is priced to make the value gap between Starter and Growth feel large, and between Growth and Enterprise feel small.

**Default annual:** Users who see annual pricing first spend more. Default the toggle to annual. Show monthly as the alternative.

**Risk reversal placement:** Must appear immediately below the CTA button or the tier grid — not only in the footer.

```html
<!-- After each CTA -->
<p class="risk-reversal">No credit card required · Cancel anytime</p>
```

---

## Anti-Patterns

- More than 3 tiers without a clear differentiation rationale (Hick's Law)
- No "Most popular" or recommended tier — all tiers look equal
- Hiding the price ("Contact us for pricing" on the main tier)
- Comparing to competitors in a way that's dishonest or unverifiable
- Feature list with 20+ items per tier (users stop reading after 5-7)
- Price toggle defaulting to monthly (trains users to pay monthly, lower LTV)
- Risk reversal buried in fine print at the bottom of the page

## Related Files

- `rules/14-landing-pages.md` — R9: Pricing section rules
- `patterns/marketing-blocks/cta-sections.md` — CTA button patterns
- `patterns/marketing-blocks/faq-sections.md` — pricing FAQ patterns
- `agents/conversion-designer.md` — pricing conversion audit
- `checklists/landing-conversion-review.md`
