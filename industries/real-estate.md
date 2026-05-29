---
version: 1.0.0
last_updated: 2026-05-25
source: manual
stale_after_days: 90
---

# Real Estate

## Sector Profile
- **Decision pattern:** Largest purchase decision, emotional + rational
- **Risk level:** Very high — long-term financial commitment
- **Key users:** Buyer, renter, investor
- **Overlaps with:** `b2b-products.md` for commercial real estate

## Mobile-First Rules
- Property gallery: full-screen swipeable carousel, pinch-to-zoom
- Map: interactive, full-width, loads without requiring JS frameworks
- Contact agent: floating button visible throughout property page on mobile

## Required Elements
- High-quality photos (minimum 10 per property) or virtual tour
- Interactive location map with neighbourhood information
- Price or price range (or clear reason why not shown)
- Floor plans and room dimensions
- Agent or developer details with direct contact
- Similar properties / nearby listings
- Mortgage calculator or affordability estimator
- Legal documents or disclosure information where required
- Viewing booking widget

## Banned Patterns
- Low-resolution or dark property photos
- Price hidden behind "register to see"
- No location information (address or at least neighbourhood + map)
- Fake or inflated availability ("last unit!")
- Complex contact forms when direct phone/email should suffice

## Trust Signals
- Agency licence number
- Agent photo, name, and track record
- Number of properties sold / managed
- Client testimonials with address area and transaction type
- Industry association membership (RICS, NAR, etc.)

## Conversion Path
- **Awareness:** Portal search, agent referral, social media
- **Consideration:** Gallery, location, price, floor plan review
- **Decision:** Viewing booking, comparison with similar
- **Action:** Book viewing or request information

## Typical Page Structure
Gallery → Price + key details → Location map → Floor plan → Agent details → Similar properties → Mortgage calculator → Book viewing CTA

## Quick Diagnosis
1. Who pays? → Buyer, renter, or investor
2. What do they decide? → Where to live or invest
3. Risk level? → Very high (largest financial decision)
4. Decision type? → Emotional desire + rational validation
5. Primary value? → Security, lifestyle, investment return

## Disambiguation
- Commercial real estate sold to businesses → also apply `b2b-products.md`
- Property management software → use `tech-saas.md`

---

## Design System for This Sector

### Color Strategy

Neutral and premium — the property photos are the hero, UI must not compete. Residential: warm whites, warm grays. Luxury: near-blacks with gold accent. Commercial: cool grays, deep blue.

```css
/* Real Estate — premium neutral, photography-forward */
--color-bg:         oklch(98% 0.004 80);   /* warm near-white */
--color-accent:     oklch(42% 0.10 255);  /* classic agency blue */
--color-accent-lux: oklch(72% 0.12 80);   /* gold — luxury segment only */
--color-text:       oklch(16% 0.008 255); /* near-black */
--color-muted:      oklch(50% 0.010 255); /* agent details, secondary */
--color-price:      oklch(22% 0.005 255); /* price — heavier weight than body */
--color-border:     oklch(88% 0.006 255); /* structural only */
```

Luxury segment: invert to dark base `oklch(12% 0.015 260)` with warm gold accent.

### Typography
- Property address: slightly larger, medium weight — it's the primary identifier.
- Price: bold, prominent — `clamp(1.8rem, 2.5vw, 2.4rem)`, never smaller than h3.
- Room specs (3 bed · 2 bath · 120m²): monospaced or tabular for quick scan.
- Agent name: slightly styled — personal trust, not just a data field.

### Spacing & Density
Photography-first. Hero gallery should fill the viewport. Details below the fold use moderate density — buyers need to scan many specs quickly.

---

## Key Component Patterns

### Property Card (Listing Grid)
```html
<article class="property-card">
  <div class="gallery-thumb">
    <img src="main.jpg" alt="3-bed semi in Hackney" loading="lazy">
    <span class="badge-new">New listing</span>
  </div>
  <div class="property-details">
    <p class="price">£485,000</p>
    <h3>Queensbridge Road, E8</h3>
    <ul class="specs">
      <li>3 beds</li><li>2 baths</li><li>112 m²</li>
    </ul>
    <p class="agent-name">Listed by: James Thornton</p>
  </div>
  <a href="/property/123" class="cta-book">Book viewing</a>
</article>
```
Price always visible without hover. No "Register to see price" — banned pattern.

### Full-Screen Gallery
- First image: exterior, daylight, wide-angle.
- Navigation: arrow keys + swipe (mobile), thumbnail strip below on desktop.
- Counter: "4 / 12" — sets expectations.
- Virtual tour button if available: prominent, not buried.

### Interactive Map + Neighbourhood Panel
```
[Map — fullwidth, interactive] [Sidebar: school ratings, transport, shops]
```
- Walking time to station: visible on map pin hover.
- Ofsted/school rating: visible without leaving property page.
- Street view link: opens in lightbox, not new tab.

### Viewing Booking Widget
- Calendar: month view, available slots highlighted, booked slots greyed.
- Time slots: 30-min increments.
- One-step confirmation: name + phone + time = done.
- After booking: add to calendar link (Google, Apple, Outlook).

### Mortgage Estimator
Inputs: price (pre-filled), deposit %, term in years.
Output: monthly payment estimate, total cost, LTV%.
Disclaimer: "This is a guide only. Speak to a mortgage adviser." — visible.

---

## Copy & Messaging Patterns

| Context | Pattern | Example |
|---|---|---|
| Headline | Address + key spec | "3-bed Victorian terrace, 5 min from tube" |
| CTA | Low-commitment first | "Book a viewing" — not "Make an offer" |
| Price | Always explicit | "£485,000 — leasehold · 94 years remaining" |
| Urgency | Real scarcity only | "3 viewings booked this week" if true |
| Agent | Personal, not corporate | "Listed by James — call direct: 07xxx" |

**Never:** "Price on application" without clear reason, "luxury" in copy without evidence, AI-generated property descriptions with generic adjectives.

---

## Design References
- Rightmove (rightmove.co.uk) — gallery UX, map integration, search filters
- Zillow (zillow.com) — mortgage calculator, map overlay pattern
- Knight Frank (knightfrank.com) — luxury segment design, editorial photography layout
