# Rule 16 — Design for SEO

> Design decisions directly affect search ranking. Semantic structure, Core Web Vitals, and content architecture are design problems — not developer afterthoughts.

---

## SEO is a Design Problem

Most SEO guides address content strategy. This rule addresses the design decisions that affect ranking:

1. **Semantic HTML structure** — how headings, links, and landmarks signal meaning to crawlers
2. **Core Web Vitals** — LCP, CLS, INP are design decisions, not just implementation details
3. **Content architecture** — how information is organized affects crawlability and topical authority
4. **Internal linking** — link placement and anchor text are design choices
5. **Schema markup** — structured data communicates directly to search engines and AI models

---

## Rules

### R1 — One H1 per page, always

The H1 is the primary topic signal for the page. One per page. Always the main page headline.

**Banned:**
- Site name as H1 on every page
- Multiple H1s (one for mobile hero, one for desktop — use CSS, not duplicate HTML)
- No H1 (implicit topic = no topic signal)
- H1 hidden via `display: none` or `visibility: hidden` (crawlers see it; Google penalizes hidden content)

**Correct heading hierarchy:**
```html
<h1>Primary topic of the page</h1>
  <h2>Major section 1</h2>
    <h3>Subsection</h3>
  <h2>Major section 2</h2>
    <h3>Subsection</h3>
```

**Never skip levels:** H1 → H3 (skipping H2) creates ambiguous hierarchy for crawlers.

---

### R2 — Semantic HTML is not optional

Semantic elements communicate structure to crawlers, screen readers, and AI models parsing your content.

**Required landmarks:**
```html
<header>       <!-- site header + navigation -->
<nav>          <!-- navigation landmark -->
<main>         <!-- primary page content -->
  <article>    <!-- self-contained content (blog post, case study) -->
  <section>    <!-- thematic grouping within main -->
  <aside>      <!-- supplementary content -->
<footer>       <!-- site footer -->
```

**Content elements:**
```html
<p>           <!-- paragraph — never use div for paragraph text -->
<ul> <ol>     <!-- lists — not <div> with manual bullets -->
<figure>      <!-- image with caption -->
  <figcaption>
<blockquote>  <!-- quoted content, with cite attribute -->
<time datetime="2026-05-20">May 20, 2026</time>  <!-- dates -->
<address>     <!-- contact information -->
```

**Banned patterns:**
```html
<div class="heading">  <!-- use h1-h6 -->
<div class="paragraph"> <!-- use p -->
<div class="list">  <!-- use ul/ol -->
<span onClick="">  <!-- use button -->
<div onClick="">   <!-- use a or button -->
```

---

### R3 — Core Web Vitals are design decisions

LCP, CLS, and INP are determined partly by design choices, not only by code.

**Largest Contentful Paint (LCP) — target ≤ 2.5s:**
- Design decision: what is the LCP element? (Usually the hero image or H1)
- Design implication: the LCP element must not be lazy-loaded, hidden behind CSS, or loaded in a carousel
- Required: `fetchpriority="high"` on the hero image; `<link rel="preload">` for critical fonts

**Cumulative Layout Shift (CLS) — target = 0:**
- Design decision: every image must have known dimensions at design time
- Required: `width` + `height` attributes on all `<img>` elements
- Required: `aspect-ratio` on all media containers (prevents jump when image loads)
- Banned: injecting content above existing content (pushes content down = CLS)
- Banned: web fonts that cause FOIT (Flash of Invisible Text) — use `font-display: optional` or `swap`

**Interaction to Next Paint (INP) — target ≤ 200ms:**
- Design decision: every interactive element must respond within 200ms visually
- Implementation: Doherty Threshold (400ms for full response; 16ms for visual feedback)
- Banned: heavy click handlers that block the main thread (use `startTransition` or `requestIdleCallback`)

---

### R4 — Internal linking is a design pattern

Links between pages signal topical relationships to crawlers and distribute ranking authority.

**Design rules:**
- Every page must have at least 3 internal links to related content
- Link placement: in-text links (inside `<p>`) carry more weight than sidebar links
- Anchor text must be descriptive: "See our pricing plans" not "click here"
- Related content sections (blog post recommendations, feature cross-links) are SEO features

**Banned anchor text:**
- "Click here"
- "Read more"
- "Learn more" (without context)
- "Here" (as the only linked word)

**Link architecture:**
- Important pages (features, pricing, case studies) → linked from homepage
- Blog posts → link to the product/feature page they're about
- Case studies → link to the relevant use case or industry page
- Documentation → links back to the marketing page for the feature

---

### R5 — Schema markup is always present

Schema markup communicates structured data directly to Google, Bing, and AI crawlers (ChatGPT, Perplexity, Gemini). It is a design decision because it requires knowing the content type and structure of each page.

**Required schema by page type:**

**Homepage:**
```json
{
  "@type": "Organization",
  "name": "Company Name",
  "url": "https://example.com",
  "logo": "https://example.com/logo.png",
  "sameAs": ["https://twitter.com/...", "https://linkedin.com/..."]
}
```

**Product/Feature page:**
```json
{
  "@type": "SoftwareApplication",
  "name": "Product Name",
  "applicationCategory": "BusinessApplication",
  "offers": { "@type": "Offer", "price": "29", "priceCurrency": "USD" }
}
```

**Blog post:**
```json
{
  "@type": "Article",
  "headline": "Post Title",
  "author": { "@type": "Person", "name": "Author Name" },
  "datePublished": "2026-05-20",
  "dateModified": "2026-05-20"
}
```

**FAQ section:**
```json
{
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "Question text",
    "acceptedAnswer": { "@type": "Answer", "text": "Answer text" }
  }]
}
```

**Pricing page:**
```json
{
  "@type": "Product",
  "offers": [
    { "@type": "Offer", "name": "Starter", "price": "29", "priceCurrency": "USD" },
    { "@type": "Offer", "name": "Growth", "price": "99", "priceCurrency": "USD" }
  ]
}
```

---

### R6 — Meta structure per page

Meta title and description are design copy, not developer boilerplate.

**Title formula:** `[Primary keyword] — [Brand name]` or `[Outcome] | [Brand name]`
**Length:** 50-60 characters (longer gets truncated in SERPs)

**Description formula:** Value proposition in 1-2 sentences, 140-160 characters.
**Include:** what the page is about + why the user should click

**Open Graph (for social sharing):**
```html
<meta property="og:title" content="[Page title]" />
<meta property="og:description" content="[Page description]" />
<meta property="og:image" content="https://example.com/og-image.jpg" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
```

**OG image design standards:**
- 1200×630px
- Brand logo visible
- Page title or key message
- No text smaller than 28px (will be illegible in small previews)

---

### R7 — URL structure is a design decision

URL structure affects both user understanding and crawlability.

**Rules:**
- URLs are human-readable: `/features/analytics` not `/features?id=4821`
- Hierarchy matches content hierarchy: `/blog/category/post-slug`
- No unnecessary words: `/blog/post/how-to-use-analytics` → `/blog/how-to-use-analytics`
- Lowercase, hyphens, no underscores or spaces
- No trailing slashes (or always trailing slashes — pick one and be consistent)
- Canonical URL defined to prevent duplicate content

---

### R8 — Images are content, not decoration

Search image results, Google Discover, and AI models parse image context.

**Alt text rules:**
- Descriptive: `alt="Dashboard showing monthly revenue chart with 32% growth"` not `alt="chart"`
- Decorative images: `alt=""` (empty, not absent) — tells crawlers to skip
- Never: `alt="image"`, `alt="photo"`, `alt="icon"`, or filename as alt text
- Product screenshots: describe what the screenshot shows, not that it is a screenshot

**Image file names:**
- Descriptive: `analytics-dashboard-overview.webp` not `img-021.webp`
- Lowercase, hyphens
- Include primary keyword where natural

---

### R9 — Page speed as SEO signal

Google uses Core Web Vitals as a ranking factor. Performance = ranking.

**Design decisions that affect speed:**

| Design decision | Impact | Fix |
|---|---|---|
| Large hero image | LCP, load time | WebP/AVIF, explicit dimensions, `fetchpriority="high"` |
| Multiple heavy fonts | FCP, LCP | Variable font (one file), `font-display: optional` |
| Render-blocking scripts | FCP, LCP | `defer`, `type="module"`, or move below fold |
| Animations above fold | INP, LCP | CSS animations only above fold; GSAP/Motion below |
| Third-party embeds (video, maps) | Load time | Facade pattern (load on click) |
| Too many font weights | Load time | Use variable fonts; load only used weights |

---

### R10 — Crawl budget and content architecture

For large sites (> 100 pages), every page must earn its crawl.

**Rules:**
- Don't index pages that have no unique content (filtered views, search result pages)
- `noindex` on: thank-you pages, confirmation pages, admin pages, staging environments
- `canonical` on: pages with similar content (product variants, date-filtered URLs)
- Sitemap: include only indexable pages; update automatically on publish

**Content depth over breadth:**
- 5 deep, authoritative posts on related topics outperform 50 thin posts
- Each post should be the best answer on the internet for its specific question
- Internal links between related posts create topical clusters (better than isolated posts)

---

## SEO Design Checklist

```
[ ] One H1 per page — specific, includes primary keyword
[ ] Semantic HTML: nav, main, article, section, aside, footer
[ ] All images: explicit width + height, descriptive alt text
[ ] LCP element: fetchpriority="high", not lazy-loaded
[ ] CLS = 0: aspect-ratio on media containers, font-display set
[ ] Schema markup: Organization / Article / FAQPage / Product as applicable
[ ] Meta title: 50-60 chars, primary keyword
[ ] Meta description: 140-160 chars, value proposition
[ ] OG image: 1200×630px, readable text, brand logo
[ ] Internal links: ≥ 3 per page, descriptive anchor text
[ ] URL: human-readable, lowercase, hyphens, no unnecessary words
[ ] Canonical URL defined on all pages
[ ] Core Web Vitals: LCP ≤ 2.5s, CLS = 0, INP ≤ 200ms
```

## Related Files

- `rules/07-responsive-design.md` — mobile-first (Google mobile-first indexing)
- `references/performance.md` — Core Web Vitals implementation
- `blueprints/landing-page-from-scratch.md` — landing page performance requirements
- `blueprints/website-from-scratch.md` — multi-page SEO architecture
