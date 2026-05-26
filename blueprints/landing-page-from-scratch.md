# Landing Page — From Scratch

> Step-by-step build protocol for a conversion-focused landing page. Follows AIDA structure. Every decision point is explicit.

**Load alongside:** `rules/14-landing-pages.md` · `patterns/marketing-blocks/` · `checklists/landing-conversion-review.md`

---

## Before You Start — Resolve These First

Run `agents/ux-architect.md` Gate 1 before any design work:

```
User: [role] using [device] at [moment in their day]
Goal: [one measurable outcome — signups, trials, purchases]
Primary CTA: [exact label + destination]
Offer: [what the user gets + at what cost/commitment]
Differentiator: [one thing this does that alternatives don't]
CSS framework:  [Tailwind / Bootstrap / Bulma / UnoCSS / Panda CSS / Open Props]
```

**Blocked until answered:**
- Who is the primary user? (not "everyone")
- What is the one action this page must produce?
- What objection will kill the conversion if not addressed?

---

## Page Architecture — AIDA

### Section 1: Hero (Attention)

**Purpose:** Stop the scroll. Deliver the core promise in 5 seconds.

**Required elements:**
- Eyebrow tag: category or audience signal ("For B2B sales teams")
- H1: benefit-first statement, ≤ 3 lines on mobile (390px)
- Subtext: one sentence expanding the promise — not repeating it
- Primary CTA: specific label, above the fold on mobile
- Supporting element: product screenshot / demo video / illustration that shows the product in use

**What to decide:**
- Color strategy: Restrained / Committed / Full palette / Drenched
- Aesthetic archetype (from `SKILL.md` Section 3)
- Background: solid color / gradient / image / video / interactive

**What to avoid:**
- H1 that starts with "The" or "A"
- Two CTAs of equal weight
- Stock photography of people smiling at laptops
- Hero metric template (big number + grid of stats)
- Centered layout with H1 + subtitle + two buttons (the default — banned)

---

### Section 2: Social Proof Bar (Interest — trust anchor)

**Purpose:** Establish credibility immediately after the promise.

**Options (pick one):**
- Logo bar: 5-8 recognizable client/partner logos, labeled "Trusted by"
- Metric strip: 3 real, specific numbers with context ("10,400 teams · 98% trial-to-paid · $2.1M saved")
- Quote strip: single strong testimonial with name + role + photo

**Rules:**
- No fictional companies
- No round numbers without source ("50%" needs context)
- Logos must be real, current, and recognized by the target user

---

### Section 3: Problem / Value Proposition (Interest)

**Purpose:** Make the user feel understood before showing the solution.

**Structure:**
```
Before: [what life looks like with the problem]
After:  [what life looks like with the solution]
Bridge: [how this product creates the transformation]
```

**Alternative structure — "3 pains":**
- Pain 1 → how this solves it
- Pain 2 → how this solves it
- Pain 3 → how this solves it

**Layout options:**
- Text-heavy editorial: strong copy, minimal decoration
- Split: pain/before on left, solution/after on right
- Tabbed: user clicks to reveal solution per pain

---

### Section 4: How It Works (Interest → Desire)

**Purpose:** Remove the "but how does it actually work?" objection.

**Structure:**
- 3-4 steps, not more (Miller's Law — working memory holds 7±2 chunks)
- Each step: number + heading (action) + one sentence + visual evidence
- Visual evidence: actual product screenshot, not illustrated icon

**Layout options:**
- Vertical numbered list with screenshots
- Horizontal steps with connecting lines
- Animated walkthrough (step appears as user scrolls)

**What to avoid:**
- Generic icons instead of product screenshots
- Steps that describe internal process, not user experience
- 6+ steps (consolidate)

---

### Section 5: Features / Capabilities (Desire)

**Purpose:** Answer "does it do X?" for the primary use cases.

**Structure:**
- Lead with outcome, not feature name: "Ship in half the time" not "Real-time collaboration"
- 3-6 features maximum on first pass (Hick's Law)
- Each feature: outcome headline + supporting sentence + visual

**Layout options:**
- Bento grid: asymmetric, varied cell sizes, one hero cell
- Alternating split: image left / text right, then flip
- Tab switcher: category tabs with feature detail below

**What to avoid:**
- Identical card grid (same size, icon + heading + text × N)
- Feature names that require domain knowledge to understand
- Listing more than 3 features per screen section

---

### Section 6: Social Proof — Deep (Desire)

**Purpose:** Remove doubt with evidence from real users.

**Required for each testimonial:**
- Name + Role + Company (all three)
- Specific result: "reduced time by 40%" not "saved time"
- Photo (real, not stock)

**Supplementary:**
- Case study teaser: one user story with before/after numbers
- Review aggregate: "4.8 / 5 from 2,400 reviews on G2" (with logo)
- Video testimonial: thumbnail with play button, 60–90 sec

**What to avoid:**
- "John Doe — CEO, Acme Corp" (fake-sounding)
- Testimonials without a concrete result
- Wall of text quotes

---

### Section 7: Pricing (Desire → Action)

**Include only if pricing is the conversion point.**

**Rules:**
- ≤ 3 tiers (decision paralysis above 3)
- One tier visually recommended ("Most popular")
- Annual pricing shown by default (or toggle defaulting to annual)
- Each tier: exact price + billing period + feature list + CTA
- Risk reversal near each CTA: "Cancel anytime" / "30-day money-back"

**Psychological structure:**
- Most expensive tier anchors perception of value
- Middle tier is the target ("Most popular" label)
- Cheapest tier exists to make the middle feel reasonable

---

### Section 8: FAQ (Desire — objection handling)

**Purpose:** Answer the questions that kill conversions.

**Select 5-7 questions from:**
- How does [primary feature] work?
- Is there a free trial?
- What happens after the trial?
- Can I cancel anytime?
- How is this different from [primary competitor]?
- Is my data secure?
- Do you offer support?

**Format:** Accordion. All closed by default. Opening one closes others.

---

### Section 9: Final CTA (Action)

**Purpose:** Close. One action. No distractions.

**Required:**
- Repeat the primary value proposition (one sentence)
- Primary CTA — same label as Section 1
- Risk reversal: no credit card / free trial / money-back
- Optional: secondary path for users not ready to convert ("Talk to sales" as text link)

**Layout:** Full-width section, maximum visual weight, nothing competing with the CTA.

---

## Design System Decisions

Make these before writing a single line of CSS:

```css
/* 1. Color tokens — OKLCH, no raw values */
--color-base:     oklch(/* L C H */);
--color-surface:  oklch(/* L C H */);
--color-accent:   oklch(/* L C H */);
--color-text:     oklch(/* L C H */);
--color-muted:    oklch(/* L C H */);
--color-border:   oklch(/* L C H / alpha */);

/* 2. Type scale — all clamp() */
--text-hero:    clamp(2.75rem, 6vw + 1rem, 7rem);
--text-display: clamp(2rem, 4vw + 0.5rem, 4.5rem);
--text-h2:      clamp(1.5rem, 2.5vw + 0.5rem, 2.5rem);
--text-body:    clamp(1rem, 1.2vw + 0.4rem, 1.125rem);

/* 3. Spacing — 4px grid */
--space-1: 0.25rem;  /* 4px */
--space-2: 0.5rem;   /* 8px */
--space-4: 1rem;     /* 16px */
--space-6: 1.5rem;   /* 24px */
--space-8: 2rem;     /* 32px */
--space-12: 3rem;    /* 48px */
--space-16: 4rem;    /* 64px */
--space-24: 6rem;    /* 96px */
```

---

## Technology Checklist

**Layout:**
- [ ] Mobile-first CSS: base at 390px, expand with `min-width`
- [ ] `min-height: 100dvh` on hero (never `100vh`)
- [ ] Section padding minimum `6rem` block, preferred `10rem`
- [ ] At least one section breaks the grid

**Images:**
- [ ] LCP image: `fetchpriority="high"`, not lazy-loaded
- [ ] All images: explicit `width` and `height` attributes
- [ ] Product screenshots: `aspect-ratio` on containers

**Animation:**
- [ ] Use `@starting-style` for hero element entrances
- [ ] Scroll reveals: `animation-timeline: view()` (CSS) or GSAP ScrollTrigger
- [ ] No `window.addEventListener('scroll')` for animations
- [ ] All animations wrapped in `@media (prefers-reduced-motion: no-preference)`

**Accessibility:**
- [ ] Eyebrow tags are `<span>`, not `<h2>` (decorative)
- [ ] H1 is the only `h1` on the page
- [ ] CTA buttons use `<button>` or `<a>` — not `<div>`
- [ ] Focus-visible ring on all interactive elements
- [ ] Skip navigation link at top of page

---

## Quality Gates

Before declaring done, pass these gates from `quality-gates.md`:
- [ ] Gate 1: Problem Definition
- [ ] Gate 3: Design System (tokens, type, spacing)
- [ ] Gate 4: States (all interactive elements)
- [ ] Gate 5: Responsive (390px, 768px, 1280px)
- [ ] Gate 6: Accessibility
- [ ] Gate 7: Performance (Lighthouse ≥ 88 mobile)
- [ ] Gate 8: Frontend Readiness

Run `agents/conversion-designer.md` before final approval.
