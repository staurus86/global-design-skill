---
version: 1.0.0
last_updated: 2026-05-25
source: manual
stale_after_days: 90
---

# Entertainment & Culture

## Sector Profile
- **Decision pattern:** Emotion + FOMO, often impulse
- **Risk level:** Low — time and affordable spend
- **Key users:** Fan, gamer, viewer, event attendee
- **Overlaps with:** `travel.md` for destination events and festivals

## Sub-Niches

These sub-niches have distinct conversion paths. When `sub_niche` is known,
apply the relevant sub-section rules on top of the universal rules below.

### casual-games
- Conversion: Install free → in-app purchase or subscription
- Trust signals: App store rating, active player count
- Banned: Aggressive monetisation patterns visible on marketing site

### aaa-games
- Conversion: Pre-order or day-one purchase
- Trust signals: Review scores (Metacritic), gameplay trailer, studio reputation
- Required: Gameplay video above the fold, system requirements table

### streaming
- Conversion: Free trial → subscription
- Trust signals: Title catalogue size, original content, device compatibility
- Required: Content preview grid, pricing table, cancel-anytime callout

### live-events
- Conversion: Ticket purchase (often time-pressured)
- Trust signals: Previous event photos, lineup, venue reputation
- Required: Date / time / venue above the fold, ticket CTA sticky

## Mobile-First Rules
- Trailer / preview: autoplay muted on mobile scroll-into-view, tap to unmute
- Ticket purchase: single-page checkout, Apple/Google Pay support
- Content grid: 2 columns on mobile minimum, scroll-linked reveal animation

## Required Elements
- Immersive hero visual or video preview
- Trailer or sample content above the fold
- Schedule, release date, or event calendar
- Ticket purchase or subscription CTA
- Community hub or social links
- Merchandise or store link
- News and updates section
- Accessibility: subtitles, audio description options

## Banned Patterns
- Autoplay video with sound on page load (not on scroll)
- Small text for event dates or ticket prices
- Hidden or non-obvious ticket purchase flow
- No content preview before subscription wall

## Trust Signals
- Review scores and press quotes
- Awards (BAFTA, Grammy, Rotten Tomatoes score)
- Community size (Discord members, social following)
- "Official" badge for licensed properties

## Conversion Path
- **Awareness:** Trailer, algorithm recommendation, word of mouth
- **Consideration:** Preview content, review reading, community check
- **Decision:** Price / value assessment
- **Action:** Buy / install / subscribe

## Typical Page Structure
Hero (trailer / visual) → Key info (date, price) → Preview content → Schedule → Community → Merch → News

## Quick Diagnosis
1. Who pays? → Individual fan or consumer
2. What do they decide? → Watch, play, attend, or subscribe
3. Risk level? → Low
4. Decision type? → Emotional + impulse
5. Primary value? → Enjoyment, belonging, FOMO resolution

## Disambiguation
- Music festival → use `live-events` sub-niche + `travel.md` for accommodation context
- Educational game → `education.md` rules apply for the learning outcomes section

---

## Design System for This Sector

### Color Strategy

Sub-niche drives palette heavily. Games: dark base with saturated neon. Streaming: dark base, brand accent. Live events: editorial bold, photography-driven. All: high visual energy — this is the one sector where "too much" can be appropriate.

```css
/* Entertainment — high energy, immersive */

/* Gaming (dark) */
--color-bg:       oklch(10% 0.02 270);   /* near-black with cool tint */
--color-accent:   oklch(72% 0.32 295);   /* electric purple */
--color-accent-2: oklch(75% 0.28 200);   /* cyan — secondary energy */
--color-text:     oklch(95% 0.004 270);  /* near-white */
--color-glow:     oklch(72% 0.32 295 / 0.4); /* for neon glow effects */

/* Live events / streaming (editorial) */
--color-bg:       oklch(8%  0.01 280);   /* editorial near-black */
--color-accent:   oklch(65% 0.30 48);    /* warm orange — energy, FOMO */
--color-text:     oklch(97% 0.002 280);  /* high-contrast white */
```

### Typography
- Gaming: condensed or bold display fonts — impact weight, uppercase for titles.
- Streaming: editorial-style, varied weight hierarchy.
- Live events: large, bold, dates maximally prominent.
- Ticket price: largest typographic element after event title.

### Motion Budget
High — this sector earns animation. Hero: auto-play video or animated key art. Transitions: bold, theatrical. Hover: pronounced scale or glow. Stagger: entry animations at 60ms intervals standard.

---

## Key Component Patterns

### Trailer / Hero Video
```html
<!-- Autoplay muted on scroll-in-view, tap/click to unmute -->
<section class="hero-video">
  <video autoplay muted loop playsinline poster="thumbnail.jpg">
    <source src="trailer.mp4" type="video/mp4">
  </video>
  <div class="hero-overlay">
    <h1>Game Title</h1>
    <p class="release">Available 15 September 2026</p>
    <a href="/buy" class="btn-cta">Pre-order — £59.99</a>
    <button class="btn-unmute" aria-label="Unmute trailer">🔊</button>
  </div>
</section>
```
Never autoplay with sound. `playsinline` required for iOS.

### Ticket Purchase Widget
```
[Event]  Glastonbury Festival — 25–29 June 2026
[Stage]  ○ General Admission  ● Weekend Pass
[Qty]    [−] 2 [+]
[Total]  £285 per ticket · £570 total

         [Continue to checkout →]
```
Sticky on mobile. Apple Pay / Google Pay as primary payment CTA.

### Countdown Timer (Live Events Only)
```html
<!-- Only appropriate when event date is set and real -->
<div class="countdown" aria-label="Time until event">
  <div><span class="count">12</span><span class="label">days</span></div>
  <div><span class="count">04</span><span class="label">hours</span></div>
  <div><span class="count">22</span><span class="label">min</span></div>
</div>
```

### Content Preview Grid (Streaming)
- Hover reveals play button + short synopsis.
- Badge: "New", "Trending", "Leaving soon".
- Progress bar for in-progress titles.
- Row labels: "Continue watching", "Trending now", "Because you watched [X]".

---

## Copy & Messaging Patterns

| Context | Pattern | Example |
|---|---|---|
| Headline | Title + energy hook | "Realm of Shadows — The fight begins September 15" |
| Ticket CTA | Specific commitment | "Buy ticket — £95" not "Get tickets" |
| Urgency | Real scarcity | "Fewer than 500 general admission tickets remain" |
| Trial | Risk-free framing | "Watch free for 30 days, cancel anytime" |
| Reviews | Authority quotes | "★★★★★ — Kotaku" / "Album of the Year — NME" |

**Never:** autoplay with sound, hidden ticket fees revealed at checkout, fabricated "X people watching" social proof.

---

## Design References
- Steam (store.steampowered.com) — game page, review aggregation, system requirements
- Spotify — editorial content grid, artist pages, playlist covers
- Ticketmaster — event listing, ticket selection flow, mobile checkout
