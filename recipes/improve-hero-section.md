# Recipe — Improve a Hero Section

> The hero section is the only design decision most users ever see. If it fails to communicate in 5 seconds, the page fails. Fix the hero, fix conversion.

---

## When to use

- Bounce rate > 60% on the landing page
- Users don't understand what the product does
- Hero looks like every other SaaS homepage
- A/B test showed headline change had no effect (structural problem, not copy)
- "Scroll to see more" is the only way to understand the value

---

## Diagnosis: Hero Failure Modes

| Failure | Symptom | Fix |
|---|---|---|
| **Generic centered layout** | H1 + p + 2 buttons, centered, full-width | Switch to split or asymmetric layout |
| **Vague headline** | "Empower your team", "Next-gen platform" | Outcome + Audience + Without Pain formula |
| **No visual proof** | Text-only hero, or stock photo | Product screenshot with perspective |
| **Too many CTAs** | 3+ buttons with equal weight | One primary, one ghost max |
| **No specificity** | "Used by thousands" without numbers | "2,847 engineering teams" |
| **Hero is an info dump** | Features list, 5 paragraphs in the hero | Move features to section 2; hero = hook only |
| **LCP not prioritized** | Hero image loads after text | `fetchpriority="high"`, preload |

---

## Step 1 — Choose the Right Layout

**Never use the default centered layout unless you have a specific reason.**

### Layout A: Split Hero (most effective for SaaS)
```
┌─────────────────────────────────────────────┐
│  Text (45%)           │  Visual (55%)        │
│                       │                      │
│  [eyebrow]            │  [product screenshot │
│  [H1 headline]        │   with perspective   │
│  [subheadline]        │   transform]         │
│  [CTA] [ghost CTA]    │                      │
└─────────────────────────────────────────────┘
```

### Layout B: Centered with Overflow Visual
```
┌─────────────────────────────────────────────┐
│         [eyebrow tag]                        │
│    [Large H1 — 2 lines max]                  │
│         [subheadline]                        │
│      [CTA]    [ghost CTA]                    │
│                                              │
│  [Product screenshot overflows bottom ↓]     │
└─────────────────────────────────────────────┘
   [Screenshot continues over next section]
```

### Layout C: Asymmetric with Bento (complex products)
```
┌─────────────────────────────────────────────┐
│  [H1 — left, large]   │  [KPI card 1]       │
│                       │  [KPI card 2]       │
│  [subheadline]        ├────────────────────┤
│  [CTA]                │  [Product view     │
│                       │   spans 2 rows]    │
└─────────────────────────────────────────────┘
```

---

## Step 2 — Fix the Headline

**The formula:** `[Specific Outcome] for [Specific Audience] without [Specific Pain]`

All three don't have to appear in the headline — but the thinking must be there.

| Before (banned) | After (specific) |
|---|---|
| "Empower Your Team" | "Ship features in hours, not sprints" |
| "Next-Gen Analytics" | "Know which customers are about to churn — before they do" |
| "Streamline Your Workflow" | "Reduce code review time from 3 days to 4 hours" |
| "The Future of [Industry]" | "The deployment platform 2,847 teams switched to after their last outage" |
| "Seamless Collaboration" | "Your entire team, always looking at the same data" |

**Headline mechanics:**
```css
/* Headline must be tight, confident, large */
.hero-heading {
  font-size: var(--text-display);     /* clamp(2.5rem, 5vw + 0.5rem, 7rem) */
  font-family: var(--font-display);
  font-weight: 700;
  line-height: 0.95;                  /* tight for large display type */
  letter-spacing: -0.03em;           /* optically tighten at large sizes */
  max-width: 12ch;                   /* force natural line breaks */
}

/* Italic or accent word for visual rhythm */
.hero-heading em {
  font-style: italic;
  color: var(--color-accent);        /* or: font-weight: 300 for contrast */
}
```

---

## Step 3 — Add an Eyebrow Tag

An eyebrow tag provides context, creates exclusivity, and draws the eye before the headline.

```html
<span class="eyebrow">New → v3.0 released May 2026</span>
<!-- OR -->
<span class="eyebrow">
  Trusted by 2,847 engineering teams
</span>
<!-- OR -->
<a href="/changelog" class="eyebrow eyebrow--link">
  What's new in v3.0 →
</a>
```

```css
.eyebrow {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  padding: 0.25rem 0.875rem;
  border: 1px solid oklch(from var(--color-accent) l c h / 0.4);
  border-radius: 9999px;
  background: oklch(from var(--color-accent) l c h / 0.06);
  font-size: 0.75rem;
  font-weight: 500;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--color-accent);
  margin-bottom: var(--space-5);
}

.eyebrow--link {
  text-decoration: none;
  cursor: pointer;
  transition: background 150ms, border-color 150ms;
}

.eyebrow--link:hover {
  background: oklch(from var(--color-accent) l c h / 0.12);
  border-color: var(--color-accent);
}
```

---

## Step 4 — Add Product Visual with Depth

A hero without product proof is a promise. A hero with product proof is evidence.

**Perspective transform on screenshot:**
```html
<div class="hero-visual">
  <div class="hero-visual__bezel">
    <img
      class="hero-visual__screenshot"
      src="/product-dashboard.webp"
      alt="The [Product] dashboard showing active deployments and pipeline status"
      width="720"
      height="480"
      fetchpriority="high"
    />
  </div>
</div>
```

```css
.hero-visual {
  position: relative;
  perspective: 1200px;
}

.hero-visual__bezel {
  padding: 0.375rem;
  background: oklch(from var(--color-accent) l c h / 0.08);
  border: 1px solid oklch(from var(--color-accent) l c h / 0.2);
  border-radius: var(--radius-2xl);
  box-shadow:
    0 8px 16px oklch(0% 0 0 / 0.1),
    0 32px 64px oklch(0% 0 0 / 0.2);
  transform: rotateY(-8deg) rotateX(2deg);
  transform-style: preserve-3d;
  transition: transform 600ms cubic-bezier(0.16, 1, 0.3, 1);
}

.hero-visual:hover .hero-visual__bezel {
  transform: rotateY(-4deg) rotateX(1deg);
}

.hero-visual__screenshot {
  display: block;
  border-radius: calc(var(--radius-2xl) - 0.375rem);
  width: 100%;
  height: auto;
}

/* Entry animation */
@starting-style {
  .hero-visual__bezel {
    opacity: 0;
    transform: rotateY(-16deg) rotateX(4deg) translateY(24px);
  }
}
```

---

## Step 5 — CTA Discipline

**Rule: One primary CTA. One ghost CTA. Nothing else.**

```html
<div class="hero-cta">
  <!-- Primary: action + object + context -->
  <a href="/signup" class="btn-primary btn-lg">
    Start free — no card needed
  </a>

  <!-- Ghost: lower commitment alternative -->
  <a href="/demo" class="btn-ghost btn-lg">
    Watch 90s demo
  </a>
</div>

<!-- Risk reducer near CTA -->
<p class="hero-cta__proof">
  Joined by 2,847 teams · Setup in 8 minutes · Cancel anytime
</p>
```

```css
.hero-cta {
  display: flex;
  gap: var(--space-3);
  align-items: center;
  flex-wrap: wrap;
  margin-top: var(--space-8);
}

.hero-cta__proof {
  font-size: 0.8125rem;
  color: var(--color-text-muted);
  margin-top: var(--space-3);
  display: flex;
  gap: var(--space-3);
  align-items: center;
}

/* Dot separator */
.hero-cta__proof span::before {
  content: '·';
  margin-right: var(--space-3);
  opacity: 0.4;
}
.hero-cta__proof span:first-child::before { display: none; }
```

---

## Step 6 — Add Entry Animation

A static hero = no energy. Everything must enter.

```css
/* Stagger all hero elements */
.hero-split__text > * {
  opacity: 0;
  transform: translateY(16px);
  animation: hero-enter 600ms cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

.eyebrow             { animation-delay: 0ms; }
.hero-heading        { animation-delay: 80ms; }
.hero-subheadline    { animation-delay: 160ms; }
.hero-cta            { animation-delay: 240ms; }
.hero-cta__proof     { animation-delay: 300ms; }

@keyframes hero-enter {
  to { opacity: 1; transform: translateY(0); }
}

/* Visual enters separately */
.hero-visual__bezel {
  animation: visual-enter 800ms 200ms cubic-bezier(0.16, 1, 0.3, 1) forwards;
  opacity: 0;
}

@keyframes visual-enter {
  from {
    opacity: 0;
    transform: rotateY(-16deg) rotateX(4deg) translateY(32px);
  }
  to {
    opacity: 1;
    transform: rotateY(-8deg) rotateX(2deg) translateY(0);
  }
}

/* Reduced motion: no transform, only opacity */
@media (prefers-reduced-motion: reduce) {
  .hero-split__text > *,
  .hero-visual__bezel {
    animation: fade-in 400ms forwards;
    transform: none;
  }
  @keyframes fade-in { to { opacity: 1; } }
}
```

---

## Step 7 — Fix Performance

Hero performance is conversion performance.

```html
<!-- LCP optimization: preload the hero image -->
<link rel="preload" as="image" href="/product-dashboard.webp" fetchpriority="high">

<!-- LCP image: always eager, high priority -->
<img
  src="/product-dashboard.webp"
  loading="eager"
  fetchpriority="high"
  decoding="async"
  width="720"
  height="480"
  alt="..."
/>

<!-- Hero background (if image): preload -->
<link rel="preload" as="image" href="/hero-bg.webp">
```

---

## Complete Split Hero — Full Implementation

```html
<section class="hero-split">
  <div class="hero-split__text">
    <span class="eyebrow">New in 2026 → Multi-region deploys</span>

    <h1 class="hero-heading">
      Ship 4× faster<br>
      <em>without</em> the chaos
    </h1>

    <p class="hero-subheadline">
      [Product] cuts average deployment time from 45 minutes to 11.
      Used by 2,847 engineering teams at companies like [Name] and [Name].
    </p>

    <div class="hero-cta">
      <a href="/signup" class="btn-primary btn-lg">Start free — no card needed</a>
      <a href="/demo"   class="btn-ghost  btn-lg">Watch 90s demo</a>
    </div>

    <p class="hero-cta__proof">
      <span>2,847 teams</span>
      <span>Setup in 8 minutes</span>
      <span>Cancel anytime</span>
    </p>
  </div>

  <div class="hero-visual">
    <div class="hero-visual__bezel">
      <img
        src="/product-dashboard.webp"
        alt="The [Product] pipeline view showing 4 active deployments"
        width="720" height="480"
        fetchpriority="high"
        loading="eager"
      />
    </div>
  </div>
</section>
```

---

## Acceptance Criteria

```
[ ] Headline ≤ 3 lines on 390px viewport
[ ] Value proposition clear within 5 seconds to a stranger
[ ] Product visual present (no stock photography)
[ ] One primary CTA, one ghost CTA — no more
[ ] LCP element has fetchpriority="high"
[ ] Entry animation present, respects prefers-reduced-motion
[ ] Hero fails the banned layout test (NOT centered H1 + p + 2 equal buttons)
[ ] Eyebrow tag present
[ ] Risk reducer / specificity near CTA
```

---

*Recipe version: global-design-skill v1.0 — `recipes/improve-hero-section.md`*
*Related: `rules/14-landing-pages.md`, `blueprints/landing-page-from-scratch.md`, `patterns/marketing-blocks/hero-sections.md`*
