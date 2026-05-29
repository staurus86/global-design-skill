---
version: 1.0.0
last_updated: 2026-05-25
source: manual
stale_after_days: 90
---

# Non-Profit & Charity

## Sector Profile
- **Decision pattern:** Mission alignment + trust, values-driven
- **Risk level:** Low–medium — money (donation) and time (volunteering)
- **Key users:** Donor, volunteer, grant maker
- **Overlaps with:** `government.md` for organisations with civic mandates

## Mobile-First Rules
- Donate button: visible above the fold on mobile, high contrast
- Impact numbers: large typography, readable without scrolling
- Volunteer signup form: single column, minimal fields on mobile

## Required Elements
- Mission and vision in plain language
- Impact metrics (people served, funds distributed, outcomes achieved)
- Financial transparency (annual report link, charity rating badge)
- Multiple ways to help: donate, volunteer, advocate, share
- Success stories with named beneficiaries (where consent exists)
- Team and board information
- Contact information and registered address
- Accessibility (WCAG AAA — public services obligation)
- Multi-language support if serving diverse communities

## Banned Patterns
- Misleading impact claims without sourcing
- Aggressive donation pressure tactics
- Hidden administrative cost ratio
- Complex or inaccessible navigation
- Outdated news or impact data (more than 12 months old without update)

## Trust Signals
- Charity Navigator, GuideStar, or local equivalent rating badge
- Registered charity number
- Audited accounts or financial summary
- Named board members with credentials
- Media coverage from reputable outlets

## Conversion Path
- **Awareness:** Search, social sharing, personal connection to cause
- **Consideration:** Mission review, impact data, financial transparency check
- **Decision:** Story connection, trust validation
- **Action:** One-time donation → recurring giving → volunteer signup

## Typical Page Structure
Mission + impact numbers → How we help → Stories → Ways to give → Transparency / reports → Team → Contact

## Quick Diagnosis
1. Who pays? → Donor (individual or foundation)
2. What do they decide? → Give money or time to a cause
3. Risk level? → Low–medium
4. Decision type? → Values-driven, trust-dependent
5. Primary value? → Social impact, alignment with personal values

## Disambiguation
- Organisation delivers government contracts or civic services → use `government.md`
- Social enterprise that sells products → split: product pages use `b2c-products.md`

---

## Design System for This Sector

### Color Strategy

Warm and human — avoid cold corporate blues. One strong cause-aligned accent (often orange, warm red, or green). High contrast for accessibility (WCAG AAA target for this sector).

```css
/* Non-profit — warm, human, trustworthy */
--color-bg:       oklch(99% 0.004 65);    /* warm near-white */
--color-accent:   oklch(60% 0.20 48);    /* warm orange — action, energy */
--color-accent-2: oklch(55% 0.16 145);   /* charitable green — growth, hope */
--color-text:     oklch(18% 0.012 50);   /* warm near-black */
--color-muted:    oklch(52% 0.015 65);   /* secondary text */
--color-impact:   oklch(65% 0.22 48);    /* for impact numbers — prominent */
--color-border:   oklch(88% 0.010 65);   /* warm light border */
```

### Typography
- Impact numbers: very large, bold — `clamp(3rem, 6vw, 6rem)`. These are the most persuasive element.
- Mission statement: generous leading (1.7+), slightly larger than standard body.
- Testimonials / beneficiary quotes: italic, slightly larger, visually distinct.
- Legal / charity registration: standard small print, never below 12px.

### Spacing & Density
Generous section spacing — mission-driven organisations benefit from breathing room that conveys thoughtfulness, not haste. Photography should dominate — don't crowd it with text.

---

## Key Component Patterns

### Impact Counter Block
The most persuasive element for donor decision-making. Use animated count-up on scroll entry.

```html
<section class="impact-stats">
  <div class="stat">
    <span class="stat-number" data-count="14200">14,200</span>
    <span class="stat-label">meals served this year</span>
  </div>
  <div class="stat">
    <span class="stat-number" data-count="847">847</span>
    <span class="stat-label">families housed</span>
  </div>
  <div class="stat">
    <span class="stat-number" data-count="92">92%</span>
    <span class="stat-label">of donations reach programmes</span>
  </div>
</section>
```

### Donation Form — Monthly / One-time Toggle
```
[Monthly] [One-time]     ← toggle, monthly default

[£5] [£10] [£25] [Other] ← preset amounts + free entry

[Donate £10/month]       ← CTA shows exact commitment
```
Rules: show impact equivalent ("£25 feeds a family for a week"), offer recurring by default, never hide admin ratio.

### Campaign Progress Bar
```
[████████░░░░░░░] 64% of £50,000 goal
£32,140 raised · 847 donors · 18 days left
```
Displays urgency without manipulation — real numbers only.

### Story Card (Beneficiary)
```
[Photo]
"[Quote in first person — specific, named person]"
— Maria, mother of three, supported since 2023
[Read Maria's story →]
```
Never: stock photography, anonymous quotes, generic "happy client" format.

---

## Copy & Messaging Patterns

| Context | Pattern | Example |
|---|---|---|
| Headline | Specific impact + cause | "Every £10 feeds a family for a week" |
| CTA | Commitment-clear | "Donate £25/month" — not "Give now" |
| Trust | Admin ratio | "92p of every £1 reaches our programmes" |
| Urgency | Real deadlines | "Match funding ends Friday" — not "Act now" |
| Impact | Named, specific | "You helped house 847 families this year" |

**Never:** stock photos of generic poverty, guilt-tripping language, vague impact claims ("helping communities").

---

## Design References
- Charity: Water (charitywater.org) — impact storytelling, campaign progress
- UNICEF — trust hierarchy, accessibility, multi-language
- Wikipedia fundraising banners — minimal but high-conversion donation UI
