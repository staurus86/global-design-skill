# Marketing Website — From Scratch

> Build protocol for a multi-page marketing website: homepage + inner pages, navigation, blog, about, contact. Distinct from a single landing page — covers the full site architecture.

**Load alongside:** `rules/14-landing-pages.md` · `rules/02-layout-and-grid.md` · `patterns/marketing-blocks/` · `patterns/navigation/` · `checklists/global-design-review.md`

---

## Before You Start — Resolve These First

```
Business type: [SaaS / Agency / Product / Service / Content]
Primary visitor intent: [learn / evaluate / contact / buy / read]
Primary conversion goal: [trial / contact / purchase / newsletter / download]
Content volume: [landing-only / 5-10 pages / 20+ pages with blog]
SEO priority: [low / medium / high — determines content architecture]
Brand maturity: [new brand / established brand with guidelines]
```

**Blocked until answered:**
- What is the one thing the homepage must make visitors do?
- Is there a blog or content section? (Changes IA significantly)
- What does the navigation look like at mobile? (Decide before design)

---

## Site Architecture — IA First

Map all pages before designing any of them.

### Minimal viable site (5-7 pages)
```
/                   Homepage
/product            Product overview (or /features, /how-it-works)
/pricing            Pricing
/about              About / Company
/blog               Blog index (if content strategy exists)
/contact            Contact
```

### Standard marketing site (10-15 pages)
```
/                   Homepage
/product
  /features         Features overview
  /use-cases        Use cases by role or industry
  /integrations     Integration partners
/pricing            Pricing
/customers          Customer stories / Case studies
  /[company-slug]   Individual case study
/company
  /about            About
  /team             Team (optional)
  /careers          Careers (if hiring)
/blog               Blog index
  /[slug]           Blog post
/legal
  /privacy          Privacy policy
  /terms            Terms of service
/contact            Contact
```

**Navigation rules:**
- Top-level items: ≤ 7 (Hick's Law)
- Dropdown depth: maximum 2 levels
- Never put legal pages in main navigation

---

## Global Navigation

**Desktop nav structure:**
```
[Logo]  [Product ▼]  [Pricing]  [Customers]  [Blog]      [Sign in]  [CTA button]
```

**Requirements:**
- Logo links to homepage
- Active page indicated (not just color — add weight or underline)
- CTA button: highest contrast, right-aligned
- Dropdown: appears on hover (desktop) + click (keyboard/touch)
- Sticky on scroll: sticky from top, with subtle shadow or border on scroll
- `backdrop-filter: blur()` if header goes transparent over hero

**Mobile nav:**
- Hamburger button: 44×44px minimum, with visible label "Menu" or accessible aria-label
- Drawer: slides from right or top, full-width
- Drawer contains all nav items at larger touch target (48px row height)
- Primary CTA stays sticky or at bottom of drawer
- Escape closes drawer; clicking outside closes drawer
- `aria-expanded` on hamburger button

**CSS anchor positioning for dropdowns (CSS 2026):**
```css
.dropdown-trigger { anchor-name: --nav-dropdown; }
.dropdown-panel {
  position: absolute;
  position-anchor: --nav-dropdown;
  top: anchor(bottom);
  left: anchor(left);
}
```

---

## Homepage Architecture

### Hero
Covered in `blueprints/landing-page-from-scratch.md` Section 1.
Key difference for homepage vs. landing page: homepage hero is broader (product category), landing page hero is specific (one audience + one offer).

### Value proposition section

**Not the same as the hero.** The hero captures attention; this section explains what the product is.

```
[Overarching statement about the product's purpose]

[Capability 1]  [Capability 2]  [Capability 3]
[Short label]   [Short label]   [Short label]
```

Or alternating split layout (one capability per section with screenshot).

### Social proof (after value prop)

Logo bar for enterprise/B2B. Metric strip for consumer/SMB. Testimonial carousel for service business.

### Feature showcase

One section per primary feature, alternating layout. See `patterns/marketing-blocks/hero-sections.md` for split layout code.

### Customer stories / Case studies

3 cards minimum, linking to full case study pages. Include: company name + logo + industry + one-sentence result.

### Blog preview (if blog exists)

3 most recent posts. Title + category + date + read time. "Read all articles" link.

### Final CTA

Same as landing page Section 9: full-width, value restatement, primary CTA + risk reversal.

### Footer

```
[Logo + tagline]
[Nav columns: Product · Company · Resources · Legal]
[Social links]
[© 2026 Company. All rights reserved.]
[Privacy Policy · Terms of Service · Cookie Settings]
```

**Footer rules:**
- Cookie settings link required if using analytics/tracking (GDPR)
- Social icons: aria-label with platform name
- Column grouping: ≤ 6 links per column

---

## Inner Pages

### /product or /features

**Structure:**
1. Hero: what the product does (broader than landing page)
2. Feature breakdown: one section per major capability
3. Integration ecosystem: logos of tools it connects with
4. Pricing CTA: "Start for free" or "See pricing"

### /pricing

Covered fully in `patterns/marketing-blocks/pricing-sections.md`.
**Always required on pricing page:**
- FAQ section below the tiers (handle all pricing objections)
- Enterprise contact option for custom pricing
- Comparison to competitors (optional, but high-converting when done honestly)

### /customers or /case-studies

**Index page:**
- Filter by industry, company size, use case
- Card grid: logo + company + industry + one-line result + "Read story"

**Individual case study:**
```
Customer: [name, role, company, photo]
Challenge: [what problem before the product]
Solution: [how they used the product]
Results: [specific numbers — not "improved efficiency"]
Quote: [pull quote, verbatim]
CTA: [Start your free trial / Contact sales]
```

### /blog

**Index:**
- Featured post (large card, top)
- Recent posts (3-column grid)
- Category filter
- Newsletter signup inline

**Post:**
- Title + author + date + read time + category
- Table of contents (sticky, for posts > 1500 words)
- Social share (native Web Share API on mobile)
- Related posts (3, by category)
- Author bio
- CTA (contextual to post category)

---

## Design System for Multi-Page Sites

### Typography hierarchy

```css
/* Page-level headings */
h1 { font-size: var(--text-display); } /* homepage hero */
h2 { font-size: var(--text-h2); }      /* section headings */
h3 { font-size: var(--text-h3); }      /* card headings */

/* Blog-specific */
.post-title   { font-size: var(--text-h2); }
.post-body    { font-size: var(--text-body); line-height: 1.75; }
.post-body h2 { font-size: var(--text-h3); margin-top: var(--space-12); }
```

### Consistent section spacing

```css
.section { padding-block: clamp(5rem, 10vw, 10rem); }
.section-sm { padding-block: clamp(3rem, 6vw, 6rem); }
```

### Color differentiation between pages

**Homepage:** can use multiple backgrounds for section rhythm (base, surface, accent-tinted)
**Inner pages:** typically consistent background, differentiated by content weight
**Blog:** clean, high-contrast reading surface; accent used only for links and highlights

---

## SEO Architecture (if SEO priority is medium/high)

Load `rules/16-design-for-seo.md` alongside this blueprint.

**Page structure:**
- One `<h1>` per page (the page title, not the site name)
- `<h2>` for major sections, `<h3>` for subsections
- Meta title: ≤ 60 characters, includes primary keyword
- Meta description: ≤ 160 characters, includes CTA

**Schema markup:**
- Homepage: `Organization` + `WebSite` schema
- Product page: `SoftwareApplication` or `Product` schema
- Blog post: `Article` or `BlogPosting` schema
- FAQ sections: `FAQPage` schema
- Pricing page: `PriceSpecification` inside `Offer` schema

**Performance:**
- LCP image: `fetchpriority="high"`, not lazy-loaded
- Critical CSS inline, rest deferred
- Font: `font-display: optional` to prevent invisible text flash
- No JavaScript required for above-the-fold content

---

## Navigation State Machine

| State | Trigger | Appearance |
|---|---|---|
| Transparent | Hero with dark background | No background, white text |
| Solid | Scroll past hero | `--color-surface` background + border-bottom |
| Active item | Current page | Bold weight + underline or background |
| Dropdown open | Hover / click trigger | Panel below trigger, shadow |
| Mobile open | Hamburger click | Drawer slides in |
| Mobile closed | Escape / backdrop click / nav click | Drawer slides out |

---

## Quality Gates

- [ ] Gate 1: Problem Definition (all page goals defined)
- [ ] Gate 2: Information Architecture (all pages mapped, nav ≤ 7)
- [ ] Gate 3: Design System (consistent tokens across all pages)
- [ ] Gate 4: States (nav states, mobile menu, all interactive)
- [ ] Gate 5: Responsive (every page at 390, 768, 1280)
- [ ] Gate 6: Accessibility (skip-nav, ARIA on hamburger/dropdown, keyboard nav)
- [ ] Gate 7: Performance (Core Web Vitals per page)
- [ ] Gate 8: Frontend Readiness

Run `agents/conversion-designer.md` on homepage and pricing page.
Run `agents/design-critic.md` before stakeholder review.
