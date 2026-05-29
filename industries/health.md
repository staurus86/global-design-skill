---
version: 1.0.0
last_updated: 2026-05-25
source: manual
stale_after_days: 90
---

# Health & Medicine

## Sector Profile
- **Decision pattern:** Trust + fear reduction, high responsibility
- **Risk level:** Very high — health and life involved
- **Key users:** Patient, parent, caregiver
- **Overlaps with:** `services.md` for wellness coaches and non-clinical practitioners

## Mobile-First Rules
- Booking button: visible without scrolling on mobile
- Emergency / urgent care info: top of page, high contrast, always accessible
- Provider credentials: visible in card format on mobile, not hidden behind "More"

## Required Elements
- Practitioner credentials and medical licenses
- Insurance acceptance and out-of-pocket cost transparency
- Services and treatments offered with plain-language descriptions
- HIPAA-compliant or GDPR-compliant patient testimonials
- Online booking / scheduling widget
- Location, hours, and phone number above the fold
- Emergency or urgent contact information prominently placed
- Privacy policy link prominent (not footer-buried)
- Accessibility statement (WCAG AAA target for this sector)

## Banned Patterns
- Unsubstantiated medical claims without disclaimer
- Before/after photos without informed consent disclaimer
- Pricing hidden entirely with no indication of range
- High-pressure booking tactics ("Only 2 slots this week")
- Complex navigation during a stressful health search
- Auto-play audio or video

## Trust Signals
- Medical license numbers or regulatory body membership
- Hospital affiliations
- Named patient testimonials (HIPAA-compliant format)
- Years in practice and number of patients treated
- Awards or recognition from medical organisations
- Secure booking badge

## Conversion Path
- **Awareness:** Search ("doctor near me"), referral, insurance directory
- **Consideration:** Provider bio, credentials, services review
- **Decision:** Insurance check, location/hours verification
- **Action:** Book appointment

## Typical Page Structure
Trust signals → Services → Provider profiles → Location + hours → Booking → Insurance → Emergency info

## Quick Diagnosis
1. Who pays? → Patient or insurance
2. What do they decide? → Choose a healthcare provider
3. Risk level? → Very high
4. Decision type? → Trust-first, risk-reduction dominant
5. Primary value? → Health outcome, safety, professional competence

## Disambiguation
- Wellness coach, yoga studio, or non-clinical practitioner → use `services.md`
- Health insurance product → use `finance.md`
- Medical device or equipment sold B2B → use `b2b-products.md`

---

## Design System for This Sector

### Color Strategy

Calming, clinical, trustworthy. Avoid red (triggers emergency associations), orange (too casual), pure black.

```css
/* Health — clinical calm */
--color-bg:       oklch(99% 0.003 200);   /* near-white with cool tint */
--color-accent:   oklch(55% 0.14 200);   /* calm teal-blue */
--color-accent-2: oklch(68% 0.10 165);   /* soft green — healing */
--color-text:     oklch(18% 0.008 240);  /* near-black, blue undertone */
--color-muted:    oklch(55% 0.010 220);  /* secondary text */
--color-warning:  oklch(62% 0.16 75);    /* amber — never red for health alerts */
--color-border:   oklch(90% 0.006 200);  /* very light, clinical */
```

### Typography
- Headlines: clean, authoritative — DM Sans, Source Sans, Nunito Sans. Never decorative or script.
- Body: min 16px, `line-height: 1.65` — medical text must be easy to re-read under stress.
- Provider names: slightly larger and bolder — patients scan for names first.
- Medical terms: always followed by a plain-language parenthetical on first use.

### Spacing & Density
Open, generous — density signals stress, openness signals calm. Max content width 720px for reading-heavy sections. Card padding minimum `var(--space-6)` on all sides.

---

## Key Component Patterns

### Provider Card
Credentials and license must appear before the booking CTA. Never anonymous.

```html
<div class="provider-card">
  <img src="dr-chen.jpg" alt="Dr. Sarah Chen" width="96" height="96">
  <div class="provider-info">
    <span class="eyebrow">Cardiologist · 18 yrs experience</span>
    <h3>Dr. Sarah Chen</h3>
    <p class="credentials">MD, FRCP · Licensed NY, NJ · Lic. #12345</p>
    <p class="availability">Next available: <strong>Tomorrow, 9 am</strong></p>
    <a href="/book/dr-chen" class="btn-primary">Book appointment</a>
  </div>
</div>
```

### Appointment Booking Flow
Multi-step — never single-page overload for health decisions.
1. Select specialty / service
2. Select provider (or "Any available")
3. Pick date + time (calendar — no dropdowns)
4. Confirm insurance / payment
5. Summary with cancellation policy before final submit

### Emergency Notice — Always Present
```html
<!-- Persistent top-of-page, even on non-emergency pages -->
<aside class="emergency-notice" role="alert">
  <strong>Medical emergency?</strong> Call 911 or go to your nearest ER.
  Do not use this form for urgent conditions.
</aside>
```
Style: amber/teal, not red. `role="alert"` for screen readers.

### Trust Bar (above the fold, before first CTA)
```
[Medical licence] · [X years practice] · [HIPAA / GDPR compliant] · [Insurance accepted] · [Secure booking SSL]
```

---

## Copy & Messaging Patterns

| Context | Pattern | Example |
|---|---|---|
| Headline | `[Outcome] for [patient type]` | "Expert cardiac care for active adults" |
| CTA | Appointment-first | "Book appointment" — not "Claim your slot" |
| Trust | Specific numbers | "Dr. Chen has treated 4 200+ patients" |
| Disclaimer | Always visible | "This is not a substitute for professional medical advice." |
| Error | Empathetic tone | "We couldn't verify your insurance — let's help you check manually." |

**Never:** countdown timers, flash-sale urgency, superlatives without evidence ("world's best").

---

## Design References
- Cleveland Clinic (clevelandclinic.org) — trust hierarchy, provider card layout
- One Medical — clean booking flow, anxiety-free design
- Zocdoc — availability calendar, search-first UX, insurance check pattern
