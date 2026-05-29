---
version: 1.0.0
last_updated: 2026-05-25
source: manual
stale_after_days: 90
---

# Education & Training

## Sector Profile
- **Decision pattern:** Investment in self, long-term, considered
- **Risk level:** High — time, money, career trajectory
- **Key users:** Student, parent, HR/L&D buyer
- **Overlaps with:** `b2b-products.md` for corporate training sold to companies

## Mobile-First Rules
- Curriculum accordion: tap to expand each module, visible progress indicator
- Instructor photo: above the fold on mobile, full-width with credentials overlay
- Pricing: sticky bottom bar on mobile showing price + enroll CTA

## Required Elements
- Full curriculum / syllabus with module breakdown
- Instructor credentials, photo, and relevant achievements
- Student outcomes: job placement rate, salary uplift, testimonials with names
- Pricing with payment plan options
- Certification or accreditation information
- Free preview lesson or sample content
- FAQ covering refund policy, prerequisites, schedule, and time commitment
- Community or alumni network description
- Career support / job assistance section if applicable

## Banned Patterns
- "Get rich in 30 days" or outcome guarantees without evidence
- Hidden cost (upsells revealed after enrollment)
- No curriculum visible before purchase
- Unverifiable testimonials
- Countdown timers on evergreen courses ("Enrolment closes in 2 hours")

## Trust Signals
- Instructor LinkedIn profile or professional portfolio
- Student outcome data with methodology note
- Accreditation logos (university partnership, industry body)
- Student count ("14,000 enrolled")
- Press coverage or award recognition
- Money-back guarantee with clear terms

## Conversion Path
- **Awareness:** SEO, word of mouth, social proof
- **Consideration:** Curriculum review, instructor research, outcome data
- **Decision:** Free lesson, community preview, FAQ review
- **Action:** Enroll + first payment

## Typical Page Structure
Outcome headline → Who it's for → Curriculum → Instructor → Student stories → Pricing → FAQ → Enroll CTA

## Quick Diagnosis
1. Who pays? → Individual or corporate (HR/L&D)
2. What do they decide? → Invest time + money in learning
3. Risk level? → High
4. Decision type? → Considered — needs evidence of outcomes
5. Primary value? → Career advancement, skill acquisition, certification

## Disambiguation
- Corporate training sold to procurement → also apply `b2b-products.md` rules
- Editorial blog that also sells courses → this file applies to course pages only

---

## Design System for This Sector

### Color Strategy

Aspirational and trustworthy — blends professional credibility with approachable warmth. Primary: deep blue or teal (knowledge, authority). Accent: energetic but not aggressive — orange or warm green for progress/CTA.

```css
/* Education — aspirational, credible */
--color-bg:         oklch(99% 0.003 250); /* near-white */
--color-accent:     oklch(48% 0.18 255); /* deep learning blue */
--color-accent-2:   oklch(68% 0.20 55);  /* warm amber — progress, CTA */
--color-text:       oklch(16% 0.008 250);/* near-black */
--color-muted:      oklch(52% 0.010 250);/* secondary text */
--color-progress:   oklch(55% 0.18 145); /* green — completion, progress */
--color-cert:       oklch(72% 0.15 80);  /* gold — certificate, achievement */
--color-border:     oklch(88% 0.005 250);/* clean structural */
```

### Typography
- Course title: bold, generous — this is the product name.
- Instructor name: slightly styled — personal credibility is the trust anchor.
- Outcome stats (job placement, salary uplift): large, bold — these close the sale.
- Curriculum items: medium weight, scannable — learners preview before buying.

### Progress Indicators
Progress is core to the education experience — use consistently: course completion bars, module unlock states, certificate progress, lesson count "14/22 lessons complete".

---

## Key Component Patterns

### Course Hero
```html
<section class="course-hero">
  <div class="course-info">
    <span class="eyebrow">Full-stack Development · 12 weeks</span>
    <h1>React & Node.js Bootcamp</h1>
    <p class="outcome">87% of graduates hired within 3 months · avg salary £52,000</p>
    <div class="meta">
      <span>⭐ 4.8 (2,340 reviews)</span>
      <span>👥 14,200 enrolled</span>
      <span>🏆 Certificate included</span>
    </div>
    <div class="pricing">
      <span class="price">£1,490</span>
      <span class="installment">or 3 × £530</span>
    </div>
    <a href="/enroll" class="btn-enroll">Enroll now — starts Feb 3</a>
    <a href="/free-lesson" class="btn-preview">Watch free lesson first</a>
  </div>
  <div class="instructor-card">
    <img src="instructor.jpg" alt="Sarah Mills">
    <h3>Sarah Mills</h3>
    <p>Former Google engineer · 8 years teaching</p>
  </div>
</section>
```

### Curriculum Accordion
```html
<section class="curriculum">
  <h2>What you'll learn <span class="meta">22 modules · 48 hours of content</span></h2>
  <details class="module">
    <summary>
      <span class="module-num">Module 1</span>
      <span class="module-title">JavaScript Fundamentals</span>
      <span class="module-meta">4 lessons · 3h 20m</span>
    </summary>
    <ul>
      <li>Variables, types, and scope <span class="duration">45 min</span></li>
      <li>Functions and closures <span class="duration">55 min</span></li>
    </ul>
  </details>
</section>
```
Show first 3 modules open, rest collapsed. Preview lesson CTA inside accordion.

### Outcome Stats Block
The highest-converting element for considered purchases.
```
[87%]              [£52k]             [3 months]
graduates hired    avg starting       median time
within 3 months    salary             to first job

Based on survey of 847 graduates, 2024 cohort. [Methodology →]
```
Source must be cited. Never fabricate.

### Pricing + Payment Plans
```
Full payment:     £1,490  [Save £150]
3 instalments:    £530 × 3
Monthly plan:     £199/mo × 8

[Enroll now]   [Try free for 7 days]

✓ 30-day money-back guarantee
✓ Lifetime access to materials
✓ Certificate on completion
```

---

## Copy & Messaging Patterns

| Context | Pattern | Example |
|---|---|---|
| Headline | Outcome + timeframe | "Become a React developer in 12 weeks" |
| CTA | Low-risk entry | "Try free lesson" before "Enroll" |
| Outcomes | Specific data | "87% hired in 3 months (2024 cohort, n=847)" |
| Guarantee | Clear terms | "30-day full refund, no questions asked" |
| Instructor | Credentials first | "Former [Company] engineer, [N] years teaching" |

**Never:** countdown timers on evergreen courses, "only 3 spots left" on digital products, income guarantees without FTC/ASA compliant framing.

---

## Design References
- Coursera — course hero, curriculum accordion, outcome stats
- Lambda School / BloomTech — bootcamp conversion patterns, ISA framing
- Brilliant (brilliant.org) — interactive learning UI, progress gamification
