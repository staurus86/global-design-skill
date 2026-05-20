# Pattern — CTA Sections

> A CTA section has one job: close. It appears after value has been established. It must be the highest-contrast, most visually dominant moment on the page.

---

## When to Use a Dedicated CTA Section

CTA sections appear at:
1. **Hero** — primary CTA (inline, not a standalone section)
2. **After features** — mid-page CTA (users who are already convinced)
3. **Final section** — the close (users who scrolled everything)

A page with one CTA has weak conviction. A page with 4+ competing CTAs creates paralysis. Target: primary CTA in hero + one mid-page + final section.

---

## Pattern A — Centered Close (final section)

Best for: most landing pages. Clean, high-impact, single-focus close.

```html
<section class="cta-close">
  <div class="container">
    <h2 class="cta-close__headline">Start shipping better UI today</h2>
    <p class="cta-close__sub">Join 10,400 teams who stopped wrestling with inconsistent design.</p>
    <div class="cta-close__actions">
      <a href="/signup" class="btn-primary btn-lg">Start free trial</a>
      <p class="cta-close__friction">No credit card · 14-day trial · Cancel anytime</p>
    </div>
  </div>
</section>
```

```css
.cta-close {
  padding-block: clamp(6rem, 12vw, 10rem);
  text-align: center;
  /* Distinct background from previous section */
  background: var(--color-accent);
  color: oklch(10% 0.01 258);
}

.cta-close__headline {
  font-size: clamp(2rem, 4vw, 3.5rem);
  max-width: 18ch;
  margin-inline: auto;
}

.cta-close__sub {
  max-width: 48ch;
  margin-inline: auto;
  margin-block: var(--space-4);
  opacity: 0.8;
}

.cta-close__actions {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-3);
  margin-top: var(--space-8);
}

.cta-close__friction {
  font-size: 0.875rem;
  opacity: 0.65;
}

/* Dark variant */
.cta-close--dark {
  background: var(--color-base);
  color: var(--color-text-primary);
}

/* Surface variant (lighter) */
.cta-close--surface {
  background: var(--color-surface);
  color: var(--color-text-primary);
}
```

---

## Pattern B — Split CTA (with social proof)

Best for: mid-page CTA or final section with a strong testimonial.

```html
<section class="cta-split">
  <div class="container">
    <div class="cta-split__content">
      <h2>Ready to cut onboarding time in half?</h2>
      <p>Start with a 14-day free trial. No card needed.</p>
      <a href="/signup" class="btn-primary btn-lg">Get started free</a>
      <p class="cta-friction">Free forever plan available · No card needed</p>
    </div>
    <div class="cta-split__proof">
      <!-- Featured quote pattern from social-proof.md -->
      <blockquote class="cta-quote">
        "We onboard new engineers 3× faster now. It's the first tool
         the whole team actually uses."
      </blockquote>
      <cite class="cta-quote__author">
        <img src="/avatars/jay-p.webp" alt="Jay P." width="40" height="40" />
        <span>Jay P. — CTO, Vercel</span>
      </cite>
    </div>
  </div>
</section>
```

```css
.cta-split .container {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--space-12);
  align-items: center;
}

@media (min-width: 768px) {
  .cta-split .container {
    grid-template-columns: 1fr 1fr;
  }
}

.cta-split__proof {
  background: oklch(100% 0 0 / 0.05);
  border: 1px solid oklch(100% 0 0 / 0.12);
  border-radius: var(--radius-xl);
  padding: var(--space-8);
}

.cta-quote {
  font-size: 1.125rem;
  line-height: 1.6;
  font-style: italic;
  margin-bottom: var(--space-6);
}

.cta-quote__author {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  font-style: normal;
  font-size: 0.875rem;
}

.cta-quote__author img { border-radius: 50%; }
```

---

## Pattern C — Dual Path CTA

Best for: products with two distinct conversion paths (self-serve vs. sales).

```html
<section class="cta-dual">
  <div class="container">
    <div class="cta-dual__grid">
      <div class="cta-dual__path">
        <div class="cta-dual__icon" aria-hidden="true">⚡</div>
        <h3>Start for free</h3>
        <p>Get full access to all features. No credit card required for the trial.</p>
        <a href="/signup" class="btn-primary">Create free account</a>
        <p class="cta-friction">14-day trial · No card · Cancel anytime</p>
      </div>
      <div class="cta-dual__divider" aria-hidden="true">or</div>
      <div class="cta-dual__path">
        <div class="cta-dual__icon" aria-hidden="true">💬</div>
        <h3>Talk to our team</h3>
        <p>Get a custom demo and discuss pricing for your team's specific needs.</p>
        <a href="/demo" class="btn-ghost">Book a 30-min call</a>
        <p class="cta-friction">Usually responds within 2 hours</p>
      </div>
    </div>
  </div>
</section>
```

```css
.cta-dual__grid {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  gap: var(--space-10);
  align-items: center;
}

@media (max-width: 768px) {
  .cta-dual__grid {
    grid-template-columns: 1fr;
    text-align: center;
  }
}

.cta-dual__path {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  padding: var(--space-8);
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
}

.cta-dual__divider {
  font-size: 1.125rem;
  color: var(--color-text-muted);
  font-weight: 500;
}
```

---

## Pattern D — Banner / Sticky Bar

Best for: time-limited offers, announcement-style CTAs, product launches.

```html
<div class="cta-banner" role="banner" aria-label="Limited offer">
  <p>
    <strong>Spring launch —</strong> First 500 signups get 40% off the first year.
    <a href="/signup?promo=spring" class="cta-banner__link">Claim your spot</a>
  </p>
  <button class="cta-banner__close" aria-label="Dismiss offer">×</button>
</div>
```

```css
.cta-banner {
  position: sticky;
  top: 0;
  z-index: var(--z-sticky);
  background: var(--color-accent);
  color: oklch(10% 0.01 258);
  text-align: center;
  padding: var(--space-3) var(--space-8);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-4);
  font-size: 0.9375rem;
}

.cta-banner__link {
  font-weight: 600;
  text-decoration: underline;
  text-underline-offset: 2px;
}

.cta-banner__close {
  position: absolute;
  right: var(--space-4);
  background: transparent;
  border: none;
  font-size: 1.25rem;
  cursor: pointer;
  color: inherit;
  opacity: 0.7;
  line-height: 1;
  padding: var(--space-2);
  min-width: 44px;
  min-height: 44px;
}
```

---

## Button Design Rules (applied at CTA sections)

```css
/* Primary — the conversion action */
.btn-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  background: var(--color-accent);
  color: oklch(10% 0.01 258);
  font-weight: 600;
  border-radius: var(--radius-full);
  border: none;
  cursor: pointer;
  transition: filter 150ms, transform 100ms;
  white-space: nowrap;
}

.btn-primary:hover { filter: brightness(1.08); }
.btn-primary:active { transform: scale(0.97); }
.btn-primary:focus-visible {
  outline: 2px solid var(--color-accent);
  outline-offset: 3px;
}

/* Sizes */
.btn-md { height: 44px; padding-inline: var(--space-6); font-size: 1rem; }
.btn-lg { height: 52px; padding-inline: var(--space-8); font-size: 1.0625rem; }

/* Ghost variant */
.btn-ghost {
  background: transparent;
  border: 1.5px solid currentColor;
  color: var(--color-text-primary);
  /* all other properties same as .btn-primary */
}
```

---

## CTA Copy Rules

```
Formula: Verb + Object + Context

❌ "Get started"             → ✅ "Start free trial"
❌ "Learn more"              → ✅ "See how it works"
❌ "Sign up"                 → ✅ "Create your account — it's free"
❌ "Submit"                  → ✅ "Send my request"
❌ "Download"                → ✅ "Download the free guide (PDF)"
❌ "Book demo"               → ✅ "Book a 30-min product demo"
```

**Context modifiers (below the button, not in the button):**
- "No credit card required"
- "Free 14-day trial"
- "Cancel anytime"
- "Takes 2 minutes to set up"
- "Join 10,400+ teams"

---

## Anti-Patterns

- Two primary (filled) buttons at the same hierarchy level in one section
- CTA label "Get Started" — too generic, reduce specificity anxiety
- No friction reducer (missing risk reversal near the button)
- CTA on a dark background with insufficient contrast (test: 4.5:1 ratio)
- CTA section that appears before value has been established (AIDA violation)
- Animated CTA button that draws attention before the user finishes reading

## Related Files

- `rules/14-landing-pages.md` — R1 (one CTA per section), R5 (CTA label specificity)
- `patterns/marketing-blocks/hero-sections.md` — hero CTA placement
- `patterns/marketing-blocks/social-proof.md` — proof near CTAs
- `agents/conversion-designer.md` — CTA audit
