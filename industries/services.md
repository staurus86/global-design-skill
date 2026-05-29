---
version: 1.0.0
last_updated: 2026-05-25
source: manual
stale_after_days: 90
---

# B2C Services

## Sector Profile
- **Decision pattern:** Trust + emotional connection, personal choice
- **Risk level:** Medium — money, time, intangible result
- **Key users:** Individual client, sometimes referral from friend
- **Overlaps with:** `health.md` for medical/clinical services

## Mobile-First Rules
- Booking calendar: full-width, large tap targets (44px minimum per slot)
- Service packages: stacked cards on mobile, price prominent
- Testimonials: carousel with swipe, photo + first name + service type visible

## Required Elements
- Personal story or credentials (who you are, why you do this)
- Before/after or transformation examples where applicable
- Video or photo testimonials with full name and service received
- Booking calendar or scheduling widget
- Service packages with clear pricing tiers
- Process explanation (what happens step by step)
- FAQ about process, results, and refund policy
- Guarantee or satisfaction policy
- Consultation CTA (lower commitment than "Book Now")

## Banned Patterns
- Anonymous testimonials ("— Happy Client")
- Pricing hidden behind "contact for quote" for standard services
- No description of the process or what to expect
- Generic stock photography of the service category
- Overpromising outcomes ("Guaranteed results in 7 days")
- No cancellation or refund policy visible

## Trust Signals
- Real photo of the practitioner or team
- Credentials, certifications, years of experience
- Named testimonials with photo and service received
- Media mentions or press features
- Number of clients served or sessions completed
- Money-back or satisfaction guarantee badge

## Conversion Path
- **Awareness:** Word of mouth, search, social media
- **Consideration:** Bio reading, testimonial review, FAQ scan
- **Decision:** Process review, pricing check, availability check
- **Action:** Book consultation or first session

## Typical Page Structure
Hero (practitioner photo + value proposition) → Story / credentials → Problem statement → Service packages → Process → Testimonials → FAQ → Booking CTA

## Quick Diagnosis
1. Who pays? → Individual consumer
2. What do they decide? → Book a service with a person
3. Risk level? → Medium (trust in the provider matters most)
4. Decision type? → Emotional + trust-based
5. Primary value? → Transformation, relief, learning, connection

## Disambiguation
- Medical or clinical services → use `health.md`
- Educational courses with curriculum → use `education.md`
- Service delivered by a software product → use `tech-saas.md`

---

## Design System for This Sector

### Color Strategy

Personal brand palette — driven by the practitioner's photography and personality. Avoid generic "professional" blues unless they match the person's brand. Photography warmth should dictate the palette. Soft, approachable, never corporate.

```css
/* B2C Services — personal brand, warm */
--color-bg:         oklch(99% 0.005 80);  /* warm near-white */
--color-accent:     oklch(52% 0.18 55);  /* warm amber — energy, CTA */
--color-accent-2:   oklch(62% 0.14 145); /* soft green — growth, calm */
--color-text:       oklch(18% 0.010 60); /* warm near-black */
--color-muted:      oklch(55% 0.012 65); /* secondary text */
--color-quote:      oklch(35% 0.008 65); /* testimonial text — slightly muted */
--color-border:     oklch(88% 0.010 75); /* warm light border */
```

Photography note: use real photos of the actual practitioner — stock photography is a banned pattern in this sector. Lighting: soft, approachable. Background: clean, consistent with brand palette.

### Typography
- Practitioner name: bold, prominent — this is the brand.
- Service name: clear, outcome-oriented — not jargon.
- Testimonials: slightly larger than body, italic or visually distinct.
- Price: visible and honest — "Contact for quote" is a conversion killer for standard services.

### Spacing & Density
Personal and spacious — this is a relationship business. Generous section spacing signals thoughtfulness. Photography should breathe. Don't cram the page.

---

## Key Component Patterns

### Practitioner Hero
```html
<section class="practitioner-hero">
  <div class="hero-photo">
    <img src="sarah-real-photo.jpg" alt="Sarah Williams, life coach"
         width="480" height="600" fetchpriority="high">
  </div>
  <div class="hero-content">
    <span class="eyebrow">Life & Career Coach · 8 years · 300+ clients</span>
    <h1>I help ambitious professionals stop overthinking and start moving</h1>
    <p class="sub">6-week 1:1 coaching for career transitions and confidence</p>
    <a href="/consult" class="btn-primary">Book a free 30-min call</a>
    <p class="trust-note">No commitment — just a conversation</p>
  </div>
</section>
```
Free consultation CTA lower barrier than "Book session". Photo must be genuine — real setting, natural lighting.

### Service Tier Cards
```html
<div class="service-tiers">
  <article class="tier">
    <h3>Discovery Session</h3>
    <p class="price">£95 · single session</p>
    <p class="description">60-min intensive for a specific challenge or decision</p>
    <ul class="includes">
      <li>Pre-session questionnaire</li>
      <li>60-min 1:1 video call</li>
      <li>Action plan document</li>
    </ul>
    <a href="/book/discovery">Book session</a>
  </article>
  <article class="tier tier-featured">
    <span class="badge">Most popular</span>
    <h3>6-Week Programme</h3>
    <p class="price">£1,200 · payment plan available</p>
    <!-- ... -->
  </article>
</div>
```

### Process / What to Expect
Reduces anxiety about "what actually happens".
```
1. [Free call]     30-min discovery — no commitment, no sales pressure
2. [Intake]        Complete a brief questionnaire before Session 1
3. [Sessions]      6 × 60-min video calls, weekly
4. [Support]       WhatsApp between sessions for quick questions
5. [Completion]    Personalised action plan + 30-day check-in
```

### Testimonial Card
```html
<blockquote class="testimonial">
  <p>"[Specific, named outcome — not vague praise. 
      What changed? What was the result?]"</p>
  <footer>
    <img src="client-photo.jpg" alt="James T." width="48" height="48">
    <div>
      <strong>James T.</strong>
      <span class="service-received">6-Week Programme · Career Transition</span>
    </div>
  </footer>
</blockquote>
```
Photo required (with consent). Never "— Happy Client". Service type shown for specificity.

### Booking Calendar Widget
- Show available slots for next 2 weeks by default.
- Time zone: auto-detect + allow manual override (international clients).
- Confirmation: immediate email with calendar `.ics` attachment.
- Cancellation: policy visible before confirming.

---

## Copy & Messaging Patterns

| Context | Pattern | Example |
|---|---|---|
| Headline | Problem + who | "Stop procrastinating on the career move you've been planning for 2 years" |
| Sub-headline | Outcome + timeframe | "6-week 1:1 coaching that gets you unstuck and moving" |
| CTA | Low-commitment | "Book a free call" before "Buy a session" |
| Testimonial | Specific result | "I got the promotion I'd been avoiding asking for — within 6 weeks" |
| Process | Anxiety-reducer | "Session 1: we map where you are. Session 2: we identify what's blocking you." |
| Guarantee | Concrete | "If you don't feel it was worth your time after Session 1, I'll refund you." |

**Never:** anonymous testimonials, hidden pricing for standard services, stock photos, outcome guarantees without evidence.

---

## Design References
- Marie Forleo (marieforleo.com) — personal brand design, conversion structure
- Jenna Kutcher — photography-led personal brand, tier pricing
- Tony Robbins (tonyrobbins.com) — trust hierarchy, proof elements, high-ticket conversion
