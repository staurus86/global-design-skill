# E-Commerce Store — From Scratch

> Build protocol for an online store: category listing (PLP), product page (PDP), cart, checkout, order confirmation. The highest-stakes flow in web design: average cart abandonment is ~70% (Baymard 2026 meta-analysis), and roughly half of it is UX-caused — unexpected costs (48%), forced account creation (26%), checkout complexity (18%). Every section below exists to attack one of those numbers.

**Load alongside:** `rules/14-landing-pages.md` (homepage) · `rules/10-forms.md` (checkout) · `patterns/product-ui/forms.md` · `patterns/navigation/` · `industries/b2c-products.md` · `checklists/global-design-review.md`

---

## Before You Start — Resolve These First

```
Store model: [D2C single brand / multi-brand retail / marketplace / digital goods]
Catalog size: [<50 SKUs / 50-500 / 500+ — changes PLP and search strategy]
Average order value: [low <$50 / mid / high $500+ — changes trust requirements]
Variants: [none / simple (size, color) / complex (configurator)]
Payment region: [cards + wallets / region-specific (SBP, iDEAL, BNPL...)]
Fulfillment: [physical shipping / digital delivery / local pickup]
Platform: [headless + custom front / Shopify / WooCommerce / custom]
```

**Blocked until answered:**
- What does shipping cost and when does the visitor learn it? (Hidden costs = #1 abandonment driver)
- Can a visitor buy without creating an account? (If no — fight for guest checkout before designing anything)
- What is the return policy and where is it visible? (High-AOV stores live or die by this)

---

## Site Architecture — IA First

```
/                     Homepage (merchandising, not a brochure)
/c/[category]         Category listing (PLP)
  /c/[cat]/[subcat]   Subcategory
/p/[product-slug]     Product page (PDP)
/cart                 Cart page
/checkout             Checkout (minimal chrome — see Checkout section)
/order/[id]           Confirmation + tracking
/search?q=            Search results (PLP layout + query handling)
/account              Orders, returns, addresses (post-purchase)
/help                 Shipping, returns, sizing, contact
```

**Navigation rules:**
- Mega-menu only for 500+ SKU catalogs; ≤ 7 top-level categories (Hick's Law)
- Search visible (not icon-only) for catalogs over ~50 SKUs — on mobile too
- Cart icon: always visible, with item-count badge and accessible label ("Cart, 3 items")
- Breadcrumbs on PLP and PDP — they are navigation *and* `BreadcrumbList` schema

---

## Category Page (PLP)

### Layout

```
[Breadcrumb]
[H1 category name + item count]
[Filter bar / sidebar]  [Sort control]
[Product grid: 2 col @390px, 3-4 col @1280px]
[Pagination]
```

### Product card — the unit of the store

- Image (primary; hover swaps to second image on desktop)
- Product name (full, wraps — never truncate the only identifier)
- Price (+ compare-at price if discounted; discount must be real, see Banned Patterns)
- Variant hint (color swatches if variants exist)
- Rating + review count (only if reviews exist — never fabricate)
- Availability state on the card if relevant ("3 left", "Out of stock")
- Entire card is one link; quick-add button is a separate focusable control

### Filters

- Desktop: sidebar with grouped checkboxes; Mobile: full-screen drawer with "Show N results" apply button
- Show applied filters as removable chips above the grid
- Every filter change updates the URL (sharable, back-button-safe)
- Show result counts per option; never let a filter combination reach a dead end silently — show "0 results" with one-tap reset

### Pagination vs infinite scroll

| Catalog | Use |
|---|---|
| < 100 items per category | "Load more" button (footer stays reachable) |
| 100+ items, browsing-led | "Load more" + URL pages for SEO |
| Comparison shopping (specs) | Classic pagination — users return to specific pages |

Never pure infinite scroll: it kills the footer and back-button position.

---

## Product Page (PDP)

The PDP is two columns on desktop, one on mobile: **gallery left, buy box right.**

### Gallery

- First image = LCP element: `fetchpriority="high"`, explicit `width`/`height`, never lazy
- 3-7 images: in context, detail, scale reference; zoom on tap/click
- Video where motion sells the product (autoplay muted, `prefers-reduced-motion` respected)
- Thumbnails are buttons with `aria-label`, not divs

### Buy box (order is fixed)

```
1. Product name (H1)
2. Rating + review count → anchor link to reviews
3. Price — current, compare-at, per-unit if relevant. Large, near the CTA
4. Variant selectors (see below)
5. Shipping answer: cost + ETA ("Free over $50 · arrives Thu, Jun 18")
6. [Add to cart] — full-width on mobile, highest contrast on page
7. Express pay (Apple Pay / Google Pay) directly below — wallets are
   the majority of mobile transactions
8. Trust row: returns window · warranty · secure payment
```

**Variant selectors:**
- Swatches/buttons, not `<select>`, for ≤ 8 options; label shows the chosen value ("Color: Navy")
- Unavailable combinations: disabled with reason, never hidden
- Selected variant updates price, gallery, and availability — and the URL (`?variant=`)

**Sticky add-to-cart (mobile):** once the buy box scrolls away, pin a bar: name + price + [Add to cart]. The single highest-leverage mobile PDP pattern.

### Below the fold

1. Description — scannable: short paragraphs, real specs table, no marketing slop
2. Reviews — distribution bars + photos first + "verified purchase"; sort by recent/helpful
3. Cross-sell ("goes well with") — 4 items max, after the product content, never inside the buy box

### PDP states

| State | Treatment |
|---|---|
| In stock | Default |
| Low stock | Honest count if true ("2 left") — fabricated scarcity is a banned dark pattern |
| Out of stock | Keep page live (SEO), CTA → "Notify me" email capture, show alternatives |
| Backorder / preorder | Explicit ship date promise on the CTA ("Ships Jul 10") |
| Added to cart | Confirmation with mini-cart slide-in + "View cart / Continue shopping" — never a dead-end redirect |

---

## Cart

- **Mini-cart** (slide-in panel) for add-to-cart confirmation and quick review; **cart page** for editing — both exist
- Each line: thumbnail, name + variant (link back to PDP), unit price, quantity stepper (44×44px targets), line total, remove
- Remove is one click + brief undo — not a confirm modal
- **Order summary shows the real total**: subtotal, shipping (calculated or estimator by region/zip), tax, total. Surprise costs at checkout are the #1 abandonment cause — kill them here
- Promo-code field: collapsed behind a link ("Have a code?") — an open field sends users hunting for coupons off-site
- Free-shipping progress if a threshold exists ("$12 away from free shipping" + progress bar) — honest and high-converting
- Express pay buttons at the top of the cart
- **Empty cart**: not a dead end — message + link to bestsellers/categories, and persist cart contents across sessions (localStorage or account)

---

## Checkout

The checkout is a different *mode*, not another page of the site.

### Structural rules

- **Minimal chrome:** logo (links home), step indicator, secure badge. No site nav, no footer links, no cross-sell — every exit link is a leak
- **Guest checkout is the primary path**, visually first; account creation is a one-checkbox offer *after* payment info or on the confirmation page. Forced registration = 26% of abandonment
- One column. Multi-column checkout forms measurably increase errors
- Steps: `Contact → Shipping → Payment → Review` — as one accordion page or 3-4 separate steps; either works, mixing both does not
- Show a cart summary (collapsible on mobile) with the final total visible at every step

### Form fields — the 12-element budget

An ideal checkout has 12-14 form elements total (Baymard). Cut ruthlessly:

- Single "Full name" field, not First/Last
- Address autocomplete (one line + suggestions); "Address line 2" collapsed behind a link
- Email, not phone, as the primary contact (ask phone only if delivery genuinely needs it, and say why)
- Billing address = shipping address by default (pre-checked); reveal billing form only when unchecked
- **`autocomplete` attributes on every field** — this is the difference between a 3-minute and a 30-second checkout:

```html
<input name="name"        autocomplete="name">
<input name="email"       autocomplete="email" inputmode="email">
<input name="address"     autocomplete="street-address">
<input name="postal"      autocomplete="postal-code">
<input name="cc-number"   autocomplete="cc-number" inputmode="numeric">
<input name="cc-exp"      autocomplete="cc-exp"    inputmode="numeric">
<input name="cc-csc"      autocomplete="cc-csc"    inputmode="numeric">
```

### Payment

- Express wallets (Apple Pay / Google Pay / regional) above the card form
- Card form: number with live brand icon + spacing-as-you-type, expiry `MM/YY`, CVC with a "what is this" hint
- Inline validation on blur (not on every keystroke, never only on submit); errors per `rules/10-forms.md`: neutral tone, name the fix
- **Payment error state is mandatory design work:** keep all entered data, name the problem ("card declined — try another card"), never clear the form, never bounce to step 1

### Order confirmation

- Order number, what was bought, where it ships, when it arrives, total paid
- "Track your order" path that works without an account (email link)
- *This* is where the account-creation offer belongs ("Save your details for next time — set a password")

---

## Trust & Ethics

E-commerce inherits SKILL.md Banned Patterns — these dark patterns convert short-term and destroy the brand:

- No fake countdown timers, no fabricated "N people are viewing this", no false stock counts
- No drip pricing — the cart total is the checkout total
- No preselected paid add-ons (gift wrap, insurance, "priority processing")
- No confirm-shaming on cart abandonment popups
- Real urgency (true stock, real sale end date) is fine — and must be true

Trust signals that actually work: visible return policy near the CTA, real contact channel, recognizable payment logos, honest review distribution (a 4.6 with critical reviews converts better than a suspicious 5.0).

---

## Performance & SEO

Image-heavy + revenue-critical — Gate 7 is **Required** here, not recommended:

- LCP = PDP/PLP first image: AVIF/WebP, `fetchpriority="high"`, sized, CDN
- Gallery and grid images: explicit dimensions (zero CLS), lazy-load below fold only
- Variant switches must not reflow the buy box (reserve space for price/availability changes)
- `Product` schema with `offers` (price, availability, currency), `AggregateRating` if reviews exist, `BreadcrumbList` on PLP/PDP — this is what wins shopping-rich results
- Out-of-stock PDPs: keep 200 + schema `availability: OutOfStock`, never 404 a product that may return

---

## Quality Gates

- [ ] Gate 1: Problem Definition (store model, AOV, region resolved)
- [ ] Gate 2: IA (catalog → PLP → PDP → cart → checkout mapped; search strategy)
- [ ] Gate 3: Design System (tokens; price/discount/availability styles are tokens too)
- [ ] Gate 4: States (out-of-stock, low stock, empty cart, payment error, added-to-cart)
- [ ] Gate 5: Responsive (sticky add-to-cart at 390px; filter drawer; checkout one-column)
- [ ] Gate 6: Accessibility (variant swatches keyboard-operable, cart badge announced, form labels + autocomplete)
- [ ] Gate 7: Performance — Required (LCP image discipline, zero CLS on variant switch)
- [ ] Gate 8: Frontend Readiness (every state specced; `autocomplete` map included)

Run `agents/conversion-designer.md` on PDP and checkout — with the dark-pattern boundary explicitly in scope.
Verify rendered per `rules/20-rendered-verification.md`: the checkout must be walked end-to-end at 390px, including the payment-error state.
