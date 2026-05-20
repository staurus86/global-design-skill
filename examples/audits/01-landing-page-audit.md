# Example — Landing Page Audit

> **Scenario:** Generic B2B SaaS landing page submitted for design review before launch. Score: 34/100 → redesign recommended before shipping.

---

## Audit Metadata

| Field | Value |
|---|---|
| **Product** | Hypothetical project management SaaS |
| **Review type** | Pre-ship audit |
| **Overall score** | 34/100 → REVISE |
| **Gates passed** | 2 of 8 |

---

## The Page Under Review

```html
<!-- Representative structure of the audited page -->
<section style="text-align: center; padding: 80px 20px; background: linear-gradient(135deg, #6366f1, #8b5cf6);">
  <h1 style="font-size: 48px; color: white; font-family: Roboto, sans-serif;">
    Manage your projects seamlessly
  </h1>
  <p style="color: rgba(255,255,255,0.8); font-size: 18px; margin: 20px auto; max-width: 500px;">
    The all-in-one platform that helps teams collaborate, track progress, and ship faster.
    Seamless integration with all your tools.
  </p>
  <div style="display: flex; gap: 16px; justify-content: center; margin-top: 32px;">
    <button style="background: white; color: #6366f1; padding: 14px 28px; border-radius: 8px; font-weight: 600; border: none;">
      Get Started
    </button>
    <button style="background: transparent; border: 2px solid white; color: white; padding: 14px 28px; border-radius: 8px; font-weight: 600;">
      Learn More
    </button>
  </div>
</section>

<!-- Feature grid -->
<section style="padding: 80px 20px; background: white;">
  <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; max-width: 1000px; margin: 0 auto;">
    <div style="border: 1px solid #e5e7eb; padding: 24px; border-radius: 8px; border-left: 4px solid #6366f1;">
      <h3>Collaboration</h3>
      <p>Work together with your team in real-time.</p>
    </div>
    <div style="border: 1px solid #e5e7eb; padding: 24px; border-radius: 8px; border-left: 4px solid #6366f1;">
      <h3>Tracking</h3>
      <p>Keep track of all your projects and tasks.</p>
    </div>
    <div style="border: 1px solid #e5e7eb; padding: 24px; border-radius: 8px; border-left: 4px solid #6366f1;">
      <h3>Integrations</h3>
      <p>Connect with all your favorite tools seamlessly.</p>
    </div>
  </div>
</section>
```

---

## Quality Gate Status

| Gate | Status | Notes |
|---|---|---|
| Gate 1 — Problem defined | ❌ | "Manage your projects seamlessly" — not a problem, a generic claim |
| Gate 2 — User identified | ❌ | No specific user persona evident from any copy |
| Gate 3 — Metric set | ❌ | No conversion goal specified or implied |
| Gate 4 — All states designed | ❌ | Buttons have no hover/focus/active states |
| Gate 5 — Responsive behavior | ❌ | 3-column grid breaks below 768px — no mobile layout |
| Gate 6 — ARIA specified | ❌ | No alt text, no button types, no landmark roles |
| Gate 7 — Tokens used | ❌ | 100% inline styles with hardcoded hex values |
| Gate 8 — Developer can implement | ✅ | Simple enough to implement as-is |

**Gates passed: 2/8 — REVISE**

---

## Dimension Scores

| Dimension | Score | Finding |
|---|---|---|
| Visual hierarchy | 6/20 | Centered layout with two equal-weight CTAs — no clear focal point |
| Typography | 4/20 | Roboto (banned font), fixed 48px (not fluid), no display/body split |
| Color | 3/20 | Purple-to-indigo gradient (banned), pure white text, no hue-tinted neutrals |
| Motion | 9/20 | No animation at all — everything static on load |
| Accessibility | 12/20 | HTML is semantic; but focus styles are absent, no labels on form elements |
| **Total** | **34/100** | |

---

## Banned Patterns Found

| Pattern | Location | Severity | Fix |
|---|---|---|---|
| Purple-to-indigo gradient | Hero background | Critical | Replace with solid `oklch(12% 0.02 260)` dark or `oklch(97% 0.008 80)` light |
| Centered hero + H1 + subtitle + two equal buttons | Hero section | Critical | Convert to left-aligned split layout per `patterns/marketing-blocks/hero-sections.md` Pattern 1 |
| Side-stripe `border-left: 4px solid` | All 3 feature cards | Critical | Remove — replace with full border or background tint |
| Roboto as body font | `font-family: Roboto` in hero | Major | Replace with Instrument Sans + a display face |
| "Seamless" in copy | Hero subtitle ("seamless integration") | Major | Banned copy — replace with specific capability |
| "Get Started" CTA | Hero primary button | Major | Apply Verb + Object + Context formula |
| `transition: all` not present but zero transitions | All interactive elements | Minor | Add specific transitions per `rules/05-animation.md` |
| No `prefers-reduced-motion` media query | Page-level CSS | Minor | Required for any animations added |

---

## Critical Issues

### 1. Centered hero with equal-weight CTAs
- **Location:** Hero section
- **Problem:** The banned default SaaS hero. Interchangeable with thousands of other products. Zero brand differentiation. Two equal buttons create CTA paralysis.
- **Fix:** Redesign as left-aligned split hero per `patterns/marketing-blocks/hero-sections.md`. Replace "Get Started" + "Learn More" with one primary (action + context) + one ghost text link.
- **Reference:** `rules/14-landing-pages.md` R2, `examples/landing-pages/01-saas-hero-redesign.md`

### 2. Purple-to-indigo gradient background
- **Location:** Hero `background: linear-gradient(135deg, #6366f1, #8b5cf6)`
- **Problem:** Banned color pattern. Signals genericness. Removes all possibility of brand distinctiveness.
- **Fix:** Remove gradient entirely. Use a dark surface color from the token system: `var(--color-surface)` or `oklch(10% 0.015 258)` for dark-mode hero.
- **Reference:** `rules/04-color.md` R1, `checklists/global-design-review.md` banned patterns

### 3. Side-stripe border-left accent on feature cards
- **Location:** All 3 feature cards (`border-left: 4px solid #6366f1`)
- **Problem:** Banned structural pattern. Conveys no meaning, just decoration that signals "I ran out of ideas."
- **Fix:** Remove the border-left entirely. If visual grouping is needed, use a subtle background tint: `background: oklch(from var(--color-accent) l c h / 0.05)`.
- **Reference:** `checklists/global-design-review.md` banned patterns — "Side-stripe borders"

---

## Major Issues

### 4. Generic copy throughout
- **Location:** All text
- **Problem:** "Manage your projects seamlessly", "all-in-one platform", "seamless integration" — zero differentiation. Any PM tool could copy this verbatim.
- **Fix:** Apply `agents/copy-editor.md`. Start with the headline formula: `[Result] in [timeframe/context]` or `[Verb] [specific outcome]`.
- **Example fix:** "Manage your projects seamlessly" → "Ship projects 30% faster — without the status meeting"

### 5. No responsive mobile layout
- **Location:** 3-column feature grid
- **Problem:** At 390px, 3 columns at 250px each would require horizontal scrolling. No mobile breakpoint defined.
- **Fix:** Add media query: `@media (max-width: 768px) { .feature-grid { grid-template-columns: 1fr; } }`. Consider single column on mobile, 2-column on tablet.
- **Reference:** `rules/09-responsive.md` R1

### 6. Roboto as font choice
- **Location:** `font-family: Roboto, sans-serif` throughout
- **Problem:** Roboto is a banned font — generic, associated with Android/Material, provides zero brand signal.
- **Fix:** Replace with font pairing. For this product context (productivity SaaS): Inter (body) + Syne (display) or Instrument Sans (body) + Plus Jakarta Sans (headings).
- **Reference:** `rules/03-typography.md` R6

---

## Minor Issues

### 7. Static on load — no entrance animation
- **Location:** Page-wide
- **Problem:** "Everything must enter" — a page that snaps in without animation feels like a static file, not a product.
- **Fix:** Add minimal staggered entrance to hero: `@starting-style` on hero elements with 150ms stagger. Scroll-triggered fade-up on feature cards.
- **Reference:** `rules/05-animation.md` R1

### 8. Missing `fetchpriority="high"` preparation
- **Location:** No images currently — but when product screenshot is added to hero
- **Problem:** Future LCP element should have `fetchpriority="high"` from day one.
- **Fix:** When adding product screenshot: `<img fetchpriority="high" loading="eager" ...>`
- **Reference:** `rules/08-performance.md` R1

---

## Strengths

1. **HTML is semantically correct.** `<h1>`, `<h3>`, `<section>` tags are used appropriately. No `<div>` replacing semantic elements.
2. **Feature cards have visible text contrast.** The dark text on white cards passes WCAG 4.5:1 contrast for the text color used.
3. **Page structure follows AIDA.** Hero → Features is the correct page flow, even if execution is flawed.

---

## Recommended Fixes (Priority Order)

### Priority 1 — Required before implementation
- [ ] Replace gradient hero with dark/light solid surface
- [ ] Redesign hero as left-aligned split layout
- [ ] Remove side-stripe borders from feature cards
- [ ] Replace "Get Started" / "Learn More" CTAs with specific copy

### Priority 2 — Required before handoff
- [ ] Replace Roboto with approved font pairing
- [ ] Rewrite hero headline with specificity and outcome
- [ ] Add responsive breakpoints to feature grid
- [ ] Migrate all inline styles to CSS custom properties

### Priority 3 — Required before ship
- [ ] Add entrance animations (hero stagger + scroll-triggered reveals)
- [ ] Add hover/focus/active states to all interactive elements
- [ ] Add ARIA attributes (landmark roles, button types, alt text)

---

## What a Passing Version Looks Like

After all Priority 1–3 fixes, the page should score 75–85/100 and pass Gates 1–7. Gate 8 requires the developer handoff template to be completed per `templates/specs/frontend-tz.md`.

See `examples/landing-pages/01-saas-hero-redesign.md` for the hero section transformation applied to a similar starting point.

---

*Example version: global-design-skill v1.0 — `examples/audits/01-landing-page-audit.md`*  
*Related: `templates/specs/design-review-report.md`, `checklists/global-design-review.md`, `agents/design-critic.md`*
