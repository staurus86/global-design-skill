# Pattern — Social Proof

> Social proof reduces doubt. Doubt is the primary reason motivated users don't convert. Proof must be specific, credible, and positioned near the moment of doubt.

---

## Placement Rules (before choosing a pattern)

Social proof is not a section — it's a principle applied throughout the page:

| Position | Pattern | Purpose |
|---|---|---|
| Hero, below CTA | Logo bar or metric strip | Immediate credibility after the promise |
| After problem section | Short quote | Validates the problem statement |
| After feature section | Testimonial with result | Validates the solution claim |
| Section 6 (dedicated) | Full testimonials | Deep evidence before conversion |
| Pricing, near CTA | Star rating or metric | Final trust signal before commitment |
| Final CTA section | Strongest single quote | Last objection removal |

---

## Pattern A — Logo Bar

Best for: B2B products, enterprise software, platforms. Establishes "they trust us" without claims.

```html
<div class="logo-bar">
  <p class="logo-bar__label">Trusted by teams at</p>
  <div class="logo-bar__logos">
    <img src="/logos/airbnb.svg"    alt="Airbnb"    width="80" height="28" />
    <img src="/logos/stripe.svg"    alt="Stripe"    width="60" height="28" />
    <img src="/logos/notion.svg"    alt="Notion"    width="88" height="28" />
    <img src="/logos/linear.svg"    alt="Linear"    width="72" height="28" />
    <img src="/logos/vercel.svg"    alt="Vercel"    width="76" height="28" />
    <img src="/logos/figma.svg"     alt="Figma"     width="52" height="28" />
  </div>
</div>
```

```css
.logo-bar {
  text-align: center;
  padding-block: var(--space-8);
}

.logo-bar__label {
  font-size: 0.8125rem;
  color: var(--color-text-muted);
  text-transform: uppercase;
  letter-spacing: 0.12em;
  margin-bottom: var(--space-6);
}

.logo-bar__logos {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  gap: var(--space-8) var(--space-10);
  opacity: 0.45;
  filter: grayscale(1);
  transition: opacity 300ms;
}

.logo-bar__logos:hover { opacity: 0.7; }

.logo-bar__logos img { height: 24px; width: auto; object-fit: contain; }
```

**Scrolling marquee variant (for many logos):**
```css
.logo-bar__marquee {
  display: flex;
  gap: var(--space-10);
  animation: marquee 30s linear infinite;
  width: max-content;
}

@keyframes marquee {
  from { transform: translateX(0); }
  to   { transform: translateX(-50%); }
}

@media (prefers-reduced-motion: reduce) {
  .logo-bar__marquee { animation: none; flex-wrap: wrap; }
}
```

---

## Pattern B — Metric Strip

Best for: products with strong quantitative results. More powerful than logos if the numbers are real.

```html
<div class="metric-strip">
  <div class="metric">
    <span class="metric__number">10,400+</span>
    <span class="metric__label">teams using daily</span>
  </div>
  <div class="metric-divider" aria-hidden="true"></div>
  <div class="metric">
    <span class="metric__number">98%</span>
    <span class="metric__label">trial-to-paid conversion</span>
  </div>
  <div class="metric-divider" aria-hidden="true"></div>
  <div class="metric">
    <span class="metric__number">4.9 ★</span>
    <span class="metric__label">average on G2 (2,847 reviews)</span>
  </div>
</div>
```

```css
.metric-strip {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: var(--space-6) var(--space-12);
  padding-block: var(--space-10);
  border-top: 1px solid var(--color-border);
  border-bottom: 1px solid var(--color-border);
}

.metric {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-1);
}

.metric__number {
  font-size: clamp(1.75rem, 3vw, 2.5rem);
  font-weight: 700;
  letter-spacing: -0.02em;
}

.metric__label {
  font-size: 0.875rem;
  color: var(--color-text-muted);
}

.metric-divider {
  width: 1px;
  background: var(--color-border);
  align-self: stretch;
}

@media (max-width: 640px) {
  .metric-divider { display: none; }
}
```

**Rules for metrics:**
- Numbers must be real and verifiable — no "50% improvement" without source
- Include context: "10,400 teams" → not just "10,400"
- Round numbers signal fabrication ("10,000 customers") — use actual numbers ("10,427 customers")
- Star ratings: include review count and platform ("4.9/5 on G2 from 2,847 reviews")

---

## Pattern C — Testimonial Card

Best for: dedicated social proof sections, in-line evidence within feature sections.

```html
<article class="testimonial-card">
  <div class="testimonial-card__quote">
    <blockquote>
      "We cut our onboarding time from 3 weeks to 4 days. Every new hire gets
       up to speed before their first week is over."
    </blockquote>
  </div>
  <footer class="testimonial-card__author">
    <img
      src="/avatars/sarah-chen.webp"
      alt="Sarah Chen"
      width="48"
      height="48"
      class="testimonial-card__avatar"
    />
    <div>
      <cite class="testimonial-card__name">Sarah Chen</cite>
      <p class="testimonial-card__role">Head of People, Stripe</p>
    </div>
    <img
      src="/logos/stripe-small.svg"
      alt="Stripe"
      width="52"
      height="20"
      class="testimonial-card__company-logo"
    />
  </footer>
</article>
```

```css
.testimonial-card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  padding: var(--space-8);
  display: flex;
  flex-direction: column;
  gap: var(--space-6);
}

/* Opening quote mark */
.testimonial-card__quote::before {
  content: '\201C';
  font-size: 4rem;
  line-height: 0.8;
  color: var(--color-accent);
  display: block;
  margin-bottom: var(--space-2);
}

blockquote {
  font-size: 1.0625rem;
  line-height: 1.65;
  color: var(--color-text-primary);
  margin: 0;
}

.testimonial-card__author {
  display: flex;
  align-items: center;
  gap: var(--space-3);
}

.testimonial-card__avatar {
  border-radius: 50%;
  object-fit: cover;
}

.testimonial-card__name {
  font-style: normal;
  font-weight: 600;
  font-size: 0.9375rem;
}

.testimonial-card__role {
  font-size: 0.8125rem;
  color: var(--color-text-muted);
}

.testimonial-card__company-logo {
  margin-left: auto;
  opacity: 0.6;
}
```

---

## Pattern D — Full-Width Featured Quote

Best for: a single powerful testimonial in the middle of a marketing page. High impact.

```html
<section class="featured-quote">
  <div class="container">
    <figure>
      <blockquote class="featured-quote__text">
        "This replaced our entire data stack. We went from 6 tools
         to one. Our team actually uses it."
      </blockquote>
      <figcaption class="featured-quote__attribution">
        <img src="/avatars/marcus-r.webp" alt="Marcus R." width="56" height="56" />
        <div>
          <strong>Marcus R.</strong>
          <span>VP Engineering, Linear</span>
        </div>
      </figcaption>
    </figure>
  </div>
</section>
```

```css
.featured-quote {
  padding-block: clamp(5rem, 10vw, 8rem);
  background: var(--color-surface);
}

.featured-quote__text {
  font-size: clamp(1.5rem, 3vw, 2.25rem);
  font-weight: 500;
  line-height: 1.4;
  max-width: 22ch;
  margin: 0 auto var(--space-8);
  text-align: center;
  /* Quotation marks via CSS */
  quotes: '\201C' '\201D';
}

.featured-quote__text::before { content: open-quote; color: var(--color-accent); }
.featured-quote__text::after  { content: close-quote; color: var(--color-accent); }

.featured-quote__attribution {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-4);
}

.featured-quote__attribution img { border-radius: 50%; }
```

---

## Pattern E — Testimonial Grid (dedicated section)

```html
<section class="testimonials">
  <div class="container">
    <h2>Used by teams that ship</h2>
    <div class="testimonials__grid">
      <!-- 3, 6, or 9 testimonial cards -->
      <!-- Use Pattern C for each card -->
    </div>
  </div>
</section>
```

```css
.testimonials__grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--space-4);
  margin-top: var(--space-10);
}

@media (min-width: 640px) {
  .testimonials__grid { grid-template-columns: repeat(2, 1fr); }
}

@media (min-width: 1024px) {
  .testimonials__grid { grid-template-columns: repeat(3, 1fr); }
}
```

**Masonry variant (columns of different heights):**
```css
@media (min-width: 640px) {
  .testimonials__grid {
    columns: 2;
    column-gap: var(--space-4);
  }
  .testimonial-card {
    break-inside: avoid;
    margin-bottom: var(--space-4);
    display: block;
  }
}
```

---

## Testimonial Quality Requirements

Every testimonial must pass all five checks:

```
[ ] Full name — not "J.D." or "CEO at Fortune 500 company"
[ ] Real role + company — not "Marketing professional"
[ ] Photo — real, not stock (check: does the person exist on LinkedIn?)
[ ] Specific result — not "Great tool!" (what changed numerically or behaviorally?)
[ ] Plausible source — don't attribute results to impossible timelines
```

---

## Anti-Patterns

- "John Doe, CEO, Acme Corp" — fake-sounding names destroy credibility
- Testimonials with no result: "Love this product!" is decoration, not proof
- Logo bar with unrecognizable logos or logos of companies in unrelated industries
- Fake metrics: round numbers, unverifiable claims, no source
- Stock photos of diverse people as testimonial avatars
- Carousel for testimonials (hides proof behind a click)
- All testimonials from the same industry (signals narrow applicability)

## Related Files

- `rules/14-landing-pages.md` — R4: Social proof placement, R3: Testimonial requirements
- `patterns/marketing-blocks/cta-sections.md` — placing proof near CTAs
- `agents/conversion-designer.md` — trust signal audit
- `checklists/landing-conversion-review.md`
