---
version: 1.0.0
last_updated: 2026-05-25
source: manual
stale_after_days: 90
---

# Travel & Hospitality

## Sector Profile
- **Decision pattern:** Emotional desire + urgency, often impulse or comparison
- **Risk level:** Medium — money, time, expectations
- **Key users:** Traveller, guest, event attendee
- **Overlaps with:** `entertainment.md` for live events and festivals

## Mobile-First Rules
- Availability / date picker: large tap targets, month view default, sticky on mobile
- Price: visible on mobile without scrolling past gallery
- Book CTA: sticky bottom bar on mobile with price + "Book Now"

## Required Elements
- Stunning photography (destination, property, food, activities)
- Availability calendar with real-time pricing
- Price breakdown (base rate, taxes, fees) before final checkout
- Verified reviews with date and stay type
- Location map with distance to key attractions
- Amenities list with icons
- Cancellation policy prominently displayed
- Local guide or neighbourhood information
- Booking engine with confirmation flow

## Banned Patterns
- Hidden fees revealed only at payment step
- Fake "only 2 rooms left" urgency when availability is high
- Small or dark photography
- Cancellation policy buried in footer or terms
- Complex multi-page booking flow on mobile

## Trust Signals
- Review platform badges (TripAdvisor, Google, Booking.com) with score
- Number of guests hosted
- Response rate and response time for hosts / hotels
- Verified listing badge
- Awards (hotel stars, Michelin, travel press recognition)

## Conversion Path
- **Awareness:** Search, social inspiration, travel blog
- **Consideration:** Gallery, reviews, price comparison, location
- **Decision:** Availability + cancellation policy check
- **Action:** Book + payment

## Typical Page Structure
Hero gallery → Availability + price → Reviews → Amenities → Location map → Cancellation policy → Similar options → Book CTA

## Quick Diagnosis
1. Who pays? → Individual traveller or group
2. What do they decide? → Where to stay or what experience to book
3. Risk level? → Medium
4. Decision type? → Emotional desire + practical validation
5. Primary value? → Experience, convenience, value for money

## Disambiguation
- Restaurant without accommodation → strip property sections, keep gallery + booking + reviews
- Live event or festival → use `entertainment.md`

---

## Design System for This Sector

### Color Strategy

Destination-driven — palette should evoke the experience. Beach: warm sandy whites + ocean blues. Mountain: deep greens + stone grays. City: editorial darks. Use imagery as the primary color source — UI chrome stays neutral.

```css
/* Travel — imagery-first, escape feeling */
--color-bg:         oklch(99% 0.003 75);  /* warm near-white */
--color-accent:     oklch(55% 0.20 225); /* ocean blue — booking actions */
--color-accent-2:   oklch(68% 0.18 75);  /* warm orange — urgency, deals */
--color-text:       oklch(16% 0.008 240);/* near-black */
--color-price:      oklch(28% 0.005 240);/* heavy for price prominence */
--color-deal:       oklch(52% 0.22 145); /* green — available / good deal */
--color-scarce:     oklch(62% 0.18 48);  /* orange — limited availability */
--color-border:     oklch(90% 0.005 75); /* warm light border */
```

### Typography
- Destination names: expressive, slightly larger — this is the emotional hook.
- Price: bold, prominent — `font-weight: 700`, clearly separated from taxes/fees.
- Reviews: slightly smaller, high density — travellers read many reviews quickly.
- Dates: monospaced or tabular for aligned calendar grids.

### Spacing & Density
Gallery-forward above the fold — full-viewport hero photo standard. Booking section needs tight, scannable layout (date + price + CTA visible together). Review section: compact, scrollable.

---

## Key Component Patterns

### Date Picker / Availability Calendar
- Mobile: full-screen overlay with month view, large 44px day cells.
- Desktop: inline dual-month calendar.
- Colour coding: available (white), selected (accent), unavailable (strikethrough + muted), price shown on each available date.
- Sticky on mobile: date + price + "Book" always visible at bottom.

### Price Breakdown Panel
Show full cost before final payment step — hidden fees are a banned pattern.
```
Base rate:        £120/night × 3 nights    £360
Cleaning fee:                               £45
Service fee (12%):                          £49
Tourist tax:                                £18
──────────────────────────────────────────────
Total:                                    £472
[Confirm and pay]
```

### Review Display
```
[★★★★☆ 4.7 · 284 reviews]

"[Quote — 1-2 sentences, specific detail]"
— [First name], [Stay type], [Month Year]

[Room comfort ████ 4.8] [Cleanliness ████ 4.9] [Location ███ 4.2]
```
Sub-category scores help travellers prioritise by what matters to them.

### Availability Urgency (Real Data Only)
```html
<!-- Only show when actually true, based on live data -->
<p class="scarcity-notice" aria-live="polite">
  Only 2 rooms available for your dates
</p>
```
Never fabricate. Use `aria-live="polite"` for accessibility.

### Sticky Mobile Booking Bar
```
[Check in: Jun 14] [Check out: Jun 17]   £157/night
                                         [Book now]
```
Always visible on mobile property page — survives gallery scroll.

---

## Copy & Messaging Patterns

| Context | Pattern | Example |
|---|---|---|
| Headline | Experience + place | "Cliffside villa with private pool, Santorini" |
| Price | Nightly rate first | "From £157/night · taxes included" |
| CTA | Clear commitment | "Book now" / "Reserve your dates" |
| Urgency | Real scarcity | "2 rooms left for Jun 14–17" — not "Hurry!" |
| Reviews | Specific + dated | "Stunning views, perfect host — Ana, Jul 2025" |
| Cancellation | Prominent | "Free cancellation until Jun 12" |

**Never:** hidden fees at checkout, fabricated "9 people viewing this" notices, stock photography without real location shots.

---

## Design References
- Airbnb (airbnb.com) — gallery UX, trust system, booking flow, mobile sticky bar
- Booking.com — availability calendar, price transparency, scarcity signals
- Mr & Mrs Smith — luxury hotel editorial design, photography-first layout
