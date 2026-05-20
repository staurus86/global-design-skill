# Pattern — FAQ Sections

> FAQs are objection handlers, not a support knowledge base. Every question in a marketing FAQ is a conversion blocker that needs to be removed.

---

## FAQ vs. Support Docs

**Marketing FAQ:** Questions that prevent conversion. Answers are conversion copy.
**Support docs:** How-to guides, troubleshooting, detailed instructions.

**Rule:** If the answer to a FAQ question is longer than 3 sentences, it belongs in documentation — not on the marketing page.

---

## Selecting Questions

Before writing layout, select questions from this checklist:

**Objections that kill conversion:**
- [ ] How much does it cost? (if pricing is not fully clear)
- [ ] Is there a free trial?
- [ ] Do I need a credit card to start?
- [ ] Can I cancel anytime?
- [ ] How is this different from [primary competitor]?

**Trust questions:**
- [ ] Is my data secure?
- [ ] Do you comply with GDPR / SOC 2 / HIPAA? (if relevant)
- [ ] What happens to my data if I cancel?
- [ ] Who owns my content / work?

**Commitment questions:**
- [ ] How long does setup take?
- [ ] Do I need to install anything?
- [ ] Can I import from [common alternative]?
- [ ] What kind of support do you offer?

**Target:** 5-8 questions. More than 10 signals indecision about what the product is.

---

## Pattern A — Accordion (default, most pages)

Best for: most landing pages, pricing pages, product pages.

```html
<section class="faq">
  <div class="container">
    <div class="faq__header">
      <h2>Frequently asked questions</h2>
      <p>Still have questions? <a href="/contact">Talk to us</a></p>
    </div>

    <div class="faq__list" role="list">
      <div class="faq-item" role="listitem">
        <button
          class="faq-item__question"
          aria-expanded="false"
          aria-controls="faq-1-answer"
          id="faq-1-trigger"
        >
          Is there a free trial?
          <span class="faq-item__icon" aria-hidden="true"></span>
        </button>
        <div
          class="faq-item__answer"
          id="faq-1-answer"
          role="region"
          aria-labelledby="faq-1-trigger"
          hidden
        >
          <p>
            Yes — all plans start with a 14-day free trial. No credit card required.
            You get full access to every feature in the Growth plan during your trial.
            After 14 days, choose the plan that fits your team or cancel with one click.
          </p>
        </div>
      </div>

      <!-- Additional FAQ items follow the same pattern -->
    </div>
  </div>
</section>
```

```css
.faq { padding-block: clamp(5rem, 10vw, 8rem); }

.faq__header {
  text-align: center;
  margin-bottom: var(--space-12);
}

.faq__header p {
  color: var(--color-text-muted);
  margin-top: var(--space-3);
}

.faq__list {
  max-width: 720px;
  margin-inline: auto;
  display: flex;
  flex-direction: column;
}

.faq-item {
  border-bottom: 1px solid var(--color-border);
}

.faq-item:first-child { border-top: 1px solid var(--color-border); }

.faq-item__question {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-4);
  background: transparent;
  border: none;
  padding-block: var(--space-5);
  text-align: left;
  font-size: 1rem;
  font-weight: 500;
  color: var(--color-text-primary);
  cursor: pointer;
  line-height: 1.4;
}

.faq-item__question:hover { color: var(--color-accent); }

.faq-item__question:focus-visible {
  outline: 2px solid var(--color-accent);
  outline-offset: 2px;
  border-radius: var(--radius-sm);
}

/* The +/× icon via CSS */
.faq-item__icon {
  flex-shrink: 0;
  width: 20px;
  height: 20px;
  position: relative;
}

.faq-item__icon::before,
.faq-item__icon::after {
  content: '';
  position: absolute;
  background: currentColor;
  border-radius: 2px;
  transition: transform 250ms cubic-bezier(0.16, 1, 0.3, 1),
              opacity 200ms;
}

/* Horizontal bar */
.faq-item__icon::before {
  width: 14px;
  height: 2px;
  top: 50%;
  left: 50%;
  translate: -50% -50%;
}

/* Vertical bar */
.faq-item__icon::after {
  width: 2px;
  height: 14px;
  top: 50%;
  left: 50%;
  translate: -50% -50%;
}

/* Rotate to × when open */
[aria-expanded="true"] .faq-item__icon::after {
  transform: rotate(90deg);
  opacity: 0;
}

/* Answer panel */
.faq-item__answer {
  overflow: hidden;
  padding-bottom: var(--space-5);
}

.faq-item__answer[hidden] { display: none; }

.faq-item__answer p {
  color: var(--color-text-secondary);
  line-height: 1.7;
  max-width: 65ch;
}

/* Animate open/close */
.faq-item__answer:not([hidden]) {
  animation: faq-open 250ms cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes faq-open {
  from { opacity: 0; transform: translateY(-8px); }
  to   { opacity: 1; transform: translateY(0); }
}

@media (prefers-reduced-motion: reduce) {
  .faq-item__answer:not([hidden]) { animation: none; }
}
```

**JavaScript (minimal, vanilla):**
```js
document.querySelectorAll('.faq-item__question').forEach(btn => {
  btn.addEventListener('click', () => {
    const expanded = btn.getAttribute('aria-expanded') === 'true'
    const answerId = btn.getAttribute('aria-controls')
    const answer = document.getElementById(answerId)

    btn.setAttribute('aria-expanded', String(!expanded))
    answer.hidden = expanded
  })
})
```

**React version:**
```tsx
function FAQItem({ question, answer }: { question: string; answer: string }) {
  const [open, setOpen] = useState(false)
  const id = useId()

  return (
    <div className="faq-item">
      <button
        className="faq-item__question"
        aria-expanded={open}
        aria-controls={`${id}-answer`}
        onClick={() => setOpen(prev => !prev)}
      >
        {question}
        <span className="faq-item__icon" aria-hidden="true" />
      </button>
      <div
        id={`${id}-answer`}
        className="faq-item__answer"
        hidden={!open}
      >
        <p>{answer}</p>
      </div>
    </div>
  )
}
```

---

## Pattern B — Two-Column FAQ Grid

Best for: pages with 8-12 questions, when the FAQ section needs more visual weight.

```html
<div class="faq-grid">
  <div class="faq-col">
    <!-- Left column: first half of questions -->
    <!-- Use Pattern A faq-item for each -->
  </div>
  <div class="faq-col">
    <!-- Right column: second half of questions -->
  </div>
</div>
```

```css
.faq-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 0 var(--space-12);
}

@media (min-width: 768px) {
  .faq-grid {
    grid-template-columns: 1fr 1fr;
    align-items: start;
  }
}
```

---

## Pattern C — Inline FAQ (below pricing)

Best for: pricing-specific objections immediately below the pricing tiers.

```html
<div class="faq-inline">
  <h3 class="faq-inline__title">Common questions about pricing</h3>
  <dl class="faq-inline__list">
    <div class="faq-inline__item">
      <dt>Can I change plans later?</dt>
      <dd>Yes — upgrade or downgrade anytime. Changes take effect on your next billing cycle. No penalties.</dd>
    </div>
    <div class="faq-inline__item">
      <dt>What payment methods do you accept?</dt>
      <dd>All major credit cards (Visa, Mastercard, Amex), and bank transfers for annual plans over $1,000/year.</dd>
    </div>
    <div class="faq-inline__item">
      <dt>Do you offer refunds?</dt>
      <dd>Yes — 30-day money-back guarantee on all plans. No questions asked.</dd>
    </div>
  </dl>
</div>
```

```css
.faq-inline {
  margin-top: var(--space-12);
  padding-top: var(--space-10);
  border-top: 1px solid var(--color-border);
}

.faq-inline__title {
  font-size: 1.125rem;
  font-weight: 600;
  margin-bottom: var(--space-6);
}

.faq-inline__list {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--space-6);
}

@media (min-width: 640px) {
  .faq-inline__list { grid-template-columns: 1fr 1fr; }
}

.faq-inline__item dt {
  font-weight: 600;
  margin-bottom: var(--space-2);
}

.faq-inline__item dd {
  color: var(--color-text-secondary);
  line-height: 1.65;
  margin: 0;
}
```

---

## Schema Markup (required for FAQ on marketing pages)

FAQPage schema enables rich results in Google Search (FAQ accordion in SERPs) and feeds AI answer engines.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is there a free trial?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes — all plans start with a 14-day free trial. No credit card required. You get full access to every feature in the Growth plan during your trial."
      }
    },
    {
      "@type": "Question",
      "name": "Can I cancel anytime?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Cancel your subscription anytime from your account settings. No penalties, no lock-in periods."
      }
    }
  ]
}
</script>
```

---

## Anti-Patterns

- Questions that have answers longer than 3 sentences (move to documentation)
- Questions the company would prefer not to answer ("How does it compare to [competitor]?") — omitting obvious comparisons is a trust signal problem
- FAQ as a design element only — questions that no real user would ever ask
- All-expanded (non-accordion) layout for 8+ questions (creates an overwhelming wall of text)
- No link to support or contact at the end of the FAQ section
- FAQ without FAQPage schema markup (missed rich result opportunity)

## Related Files

- `rules/14-landing-pages.md` — R: AIDA structure, FAQ position
- `rules/16-design-for-seo.md` — R5: Schema markup
- `patterns/marketing-blocks/pricing-sections.md` — pricing FAQ (Pattern C)
- `references/accessibility.md` — accordion ARIA patterns
