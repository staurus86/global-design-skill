# Rule 14 — Landing Pages

> A landing page has one job: get the user to take one specific action. Every rule here serves that job.

---

## The Single Metric

Before any design decision: what is the one action this page must produce?

```
Conversion event: [free trial signup / demo request / purchase / email capture / download]
Primary CTA label: [exact text]
Success definition: [measurable metric — not "more conversions"]
```

If the conversion event changes, the page must be re-evaluated from scratch. The action drives the architecture.

---

## Rules

### R1 — One primary CTA per section

Every screen section has at most one filled/primary button. Multiple primary CTAs in the same section create decision paralysis.

**Pattern:**
- Primary: filled, full color, specific label
- Secondary (optional): ghost/outline or text link
- Multiple CTAs at the page level are fine — each section has its own

**Banned:**
```html
<!-- Two filled buttons side by side — decision paralysis -->
<button class="btn-primary">Start Free Trial</button>
<button class="btn-primary">Request Demo</button>

<!-- Fix: one primary, one secondary -->
<button class="btn-primary">Start free trial — no card needed</button>
<a class="btn-ghost" href="/demo">Talk to sales</a>
```

---

### R2 — Value proposition above the fold

The primary value proposition must be visible without scrolling on mobile (390px viewport).

**Test:**
1. Open the page on a 390×844px viewport
2. Without scrolling: can the user answer "What is this?" and "What do I do next?"
3. If no: the above-fold content is failing

**Elements that must fit above the fold on mobile:**
- Headline (H1)
- Subtext (one sentence)
- Primary CTA
- Optional: social proof element (logo bar or one metric)

**What can be below the fold:**
- Features, how-it-works, testimonials, pricing, FAQ

---

### R3 — Headline formula

A landing page headline is not a tagline. It is a value proposition.

**Formula:** `[Outcome] for [Audience] [Without common pain]`

Examples:
- "Close enterprise deals twice as fast" (outcome for sales teams, implied pain)
- "Design production-ready components in an afternoon" (outcome for designers)
- "Ship your SaaS in a week, not a month" (outcome, without the delay pain)

**Rules:**
- Maximum 3 lines at 390px viewport (if it wraps to 4+, cut words)
- Starts with the user's outcome, not the product's feature
- No: "The world's most powerful [X]" — superlatives without evidence are ignored
- No: "Seamless", "Elevate", "Empower", "Next-gen" — any word from the banned list

---

### R4 — Social proof placement

Social proof must appear near the primary CTA — not only at the bottom of the page.

**Minimum placement rules:**
- Section 1 (Hero): social proof element below the CTA (logo bar, metric, or star rating)
- Section 6+ (Testimonials): full testimonials with names, roles, specific results
- Final CTA section: repeat the strongest social proof element

**Testimonial requirements:**
- Name + Role + Company (all three — "John D., CEO" is insufficient)
- Photo (real, not stock)
- Specific outcome ("Reduced onboarding time from 2 weeks to 3 days")
- No generic praise ("Great product!")

---

### R5 — CTA label specificity

CTA label is the most-read copy on the page. It must be specific.

**Formula:** `Verb + Object + Context`

| Bad (generic) | Good (specific) |
|---|---|
| Get started | Start free trial |
| Learn more | See how it works |
| Submit | Send my request |
| Download | Download the free guide |
| Sign up | Create your account — it's free |

**Context modifiers that reduce friction:**
- "— no credit card needed"
- "— free for 14 days"
- "— cancel anytime"
- "— takes 2 minutes"

---

### R6 — AIDA structure (non-negotiable)

Landing pages follow Attention → Interest → Desire → Action. Deviating from this structure requires a reason.

**Section order:**
1. **Hero** — Attention: one sharp hook, value proposition, CTA
2. **Social proof bar** — Trust anchor: logos or metrics immediately after the promise
3. **Problem / value prop** — Interest: make the user feel understood
4. **How it works** — Interest: remove the "but how?" objection (3-4 steps, not more)
5. **Features** — Desire: evidence for the claims made in sections 1-3
6. **Social proof (deep)** — Desire: specific testimonials with results
7. **Pricing** (if conversion = purchase) — Desire → Action
8. **FAQ** — Desire: objection removal
9. **Final CTA** — Action: single, clean close

**What breaks AIDA:**
- Leading with features before the user understands what problem you solve
- Putting testimonials at the top before the user understands the product
- Pricing before value is established
- Multiple "Action" moments competing at the same level

---

### R7 — Friction inventory

Every element between the user's intention and the conversion is friction. Reduce friction; never add it unless it's necessary qualification.

**High-friction elements to minimize:**
- Form fields: every field reduces completion rate ~5%. Use minimum required for delivery.
- Account creation before value: show the product first
- Credit card required for trial: lose 50%+ of signups. "No card needed" if possible.
- Multi-page checkout for simple purchases: collapse to one page
- CAPTCHA on first submission: add only after abuse detected

**Acceptable friction:**
- Qualifying questions for enterprise/demo request (qualifies leads)
- Phone number for high-consideration purchases (users expect this)
- Company size/use case for proper onboarding (if it genuinely personalizes)

---

### R8 — Hero layout rules

The default centered H1 + subtitle + two buttons is banned. Every hero needs a compositional decision.

**Available compositions:**

**Split (text left, visual right):**
```
[Eyebrow tag]          [Product screenshot /
[H1: benefit]           demo / illustration]
[Subtitle]
[CTA button]
[Social proof]
```

**Full-bleed with overlay:**
```
                    [Full-bleed video or image background]
[Eyebrow tag]
[H1: benefit — high contrast against background]
[CTA button]
```

**Asymmetric with large visual:**
```
[H1 — large]      [Screenshot — extends beyond column]
[CTA + proof]
```

**What the visual must be:**
- Product screenshot or demo (shows the actual product)
- Outcome visualization (before/after, result, chart)
- Real customer photo with result context

**Never:**
- Generic stock photography of people working
- CSS/SVG illustrations of abstract "data" or "connection" patterns
- Geometric shapes and gradients as the primary hero visual

---

### R9 — Pricing section rules

Covered fully in `patterns/marketing-blocks/pricing-sections.md`. Critical rules:

- Maximum 3 tiers (Hick's Law)
- One tier labeled "Most popular" (anchors choice)
- Annual billing default (or toggle defaulting to annual)
- Risk reversal on every tier CTA: "Cancel anytime" / "30-day money-back guarantee"
- Enterprise / "Contact us" option if upmarket customers are a target

---

### R10 — Performance rules for landing pages

Landing pages are the first impression. Performance directly affects conversion (100ms delay ≈ 1% conversion decrease).

**Non-negotiable:**
- LCP ≤ 2.5s on mobile throttled (Lighthouse)
- CLS = 0 (all images have explicit dimensions)
- No render-blocking scripts above the fold
- Hero image: WebP/AVIF, `fetchpriority="high"`, not lazy-loaded

**Analytics and tracking:**
- Load analytics scripts with `defer` or after user interaction
- Consent before loading marketing pixels (GDPR)
- No third-party scripts that add > 50ms to First Contentful Paint

---

### R11 — Mobile-specific rules

Landing pages must be designed for mobile first. 60-70% of landing page traffic is mobile.

**Tap target minimum:** 44×44px on all CTAs
**Hero:** headline must not exceed 3 lines at 390px
**Pricing table:** vertical cards on mobile, not horizontal scroll
**FAQ:** accordion, not expanded list
**Images:** `aspect-ratio` on containers, never fixed heights

---

## Landing Page Checklist

```
[ ] Conversion event defined before design begins
[ ] Value proposition above the fold on mobile (390px)
[ ] One primary CTA per section
[ ] CTA label: Verb + Object + Context (not generic)
[ ] Headline ≤ 3 lines at 390px
[ ] Social proof near primary CTA (not only at bottom)
[ ] Testimonials: name + role + company + specific outcome
[ ] AIDA structure followed
[ ] Form: minimum required fields only
[ ] Pricing: ≤ 3 tiers, one recommended, risk reversal
[ ] LCP ≤ 2.5s, CLS = 0
[ ] No banned words in copy
[ ] No stock photography as primary hero visual
```

## Related Files

- `blueprints/landing-page-from-scratch.md` — full build protocol
- `agents/conversion-designer.md` — conversion audit
- `patterns/marketing-blocks/cta-sections.md` — CTA patterns
- `patterns/marketing-blocks/pricing-sections.md` — pricing psychology
- `patterns/marketing-blocks/social-proof.md` — trust signal patterns
- `patterns/marketing-blocks/hero-sections.md` — hero layout patterns
- `checklists/landing-conversion-review.md` — full conversion checklist
- `recipes/improve-hero-section.md` — hero optimization
- `recipes/improve-pricing-page.md` — pricing optimization
