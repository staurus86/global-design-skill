---
version: 1.0.0
last_updated: 2026-05-25
source: manual
stale_after_days: 90
---

# Finance & Fintech

## Sector Profile
- **Decision pattern:** Caution + trust, highly regulated
- **Risk level:** Very high — money and security
- **Key users:** Individual customer, investor, business owner
- **Overlaps with:** `b2b-products.md` for B2B financial services

## Mobile-First Rules
- Account opening / onboarding: single field per screen on mobile
- Fee tables: horizontally scrollable with sticky first column (product name)
- Calculator: full-width inputs, results immediately below, no modal

## Required Elements
- Security badges (SSL, bank-level encryption, regulatory compliance)
- Regulatory body membership or license number
- Fee transparency — all costs visible before sign-up
- Account types / product descriptions in plain language
- Interactive calculator or simulator (savings, loan, returns)
- Customer support access (phone, chat)
- Mobile app preview if app-first product
- Onboarding flow preview
- Fraud protection and insurance information

## Banned Patterns
- Hidden fees revealed after account opening
- Dense legal text presented as the primary product description
- Missing security or regulatory information
- "Guaranteed returns" without proper disclaimer
- Pressure tactics ("Offer expires today")
- Fake testimonials with stock photos

## Trust Signals
- FCA, SEC, FINRA, or local regulator authorisation
- Bank partnership or insured deposits badge
- Published fee schedule
- Customer count or AUM (assets under management)
- Security certification (SOC 2, ISO 27001)
- Awards from financial press

## Conversion Path
- **Awareness:** Search, word of mouth, comparison sites
- **Consideration:** Fee comparison, product review, security check
- **Decision:** Eligibility check, onboarding preview
- **Action:** Open account / start investing

## Typical Page Structure
Security + regulatory trust → Products → Calculator → Fees → Support → Onboarding preview → Open account CTA

## Quick Diagnosis
1. Who pays? → Individual or business
2. What do they decide? → Trust a company with their money
3. Risk level? → Very high
4. Decision type? → Cautious, evidence-heavy, regulatory
5. Primary value? → Security, returns, convenience

## Disambiguation
- Corporate treasury or enterprise finance tool → also apply `b2b-products.md`
- Crypto exchange → this file applies; add disclaimer requirements

---

## Design System for This Sector

### Color Strategy

Conservative, institutional. Primary: deep navy or teal. Accent: understated green (returns/positive) or gold (premium tier). Never playful, never pastel.

```css
/* Finance — institutional trust */
--color-bg:       oklch(99% 0.002 250);   /* near-white, neutral tint */
--color-accent:   oklch(38% 0.12 255);   /* deep institutional blue */
--color-accent-2: oklch(50% 0.14 160);   /* trust green — positive movement */
--color-text:     oklch(14% 0.005 250);  /* near-black, authoritative */
--color-positive: oklch(50% 0.18 145);   /* profit/positive */
--color-negative: oklch(50% 0.20 25);    /* loss/negative — never pure red */
--color-border:   oklch(88% 0.005 250);  /* structural, clean */
```

Dark mode for trading/dashboard: `oklch(14% 0.02 255)` base — reduces eye strain for long sessions.

### Typography
- Numbers: `font-variant-numeric: tabular-nums` — critical for price column alignment.
- Legal / small print: never below 12px, never below 3:1 contrast ratio.
- Account numbers: monospace, letter-spaced 0.08em.
- Rates and percentages: bold, prominent — never buried in body text.

### Spacing & Density
Comparison-heavy sector — support side-by-side layout at 1280px. Fee tables: sticky first column on mobile. Dashboard: tighter density than marketing pages, but never cramped on financial figures.

---

## Key Component Patterns

### Fee Comparison Table
```
| Feature       | Basic (Free) | Pro (£9/mo) | Business (£29/mo) |
|---------------|:---:|:---:|:---:|
| Accounts      | 1   | 5   | Unlimited |
| Transfer fee  | 1.5%| 0.8%| 0.3%      |
| Support       | Email | Chat | Dedicated |
```
Rules: highlight recommended tier, sticky first column on mobile horizontal scroll, all fees visible before sign-up.

### Interactive Calculator
- Inputs: large sliders or number inputs — not small text fields.
- Results: update in real-time without submit button.
- Assumptions section: clearly listed below result.
- Disclaimer: "This is an estimate, not financial advice" — readable, not hidden.

### Security & Compliance Trust Bar
```
[Bank-grade encryption] [FCA Regulated] [FSCS Protected £85k] [SOC 2 Type II] [2FA supported]
```
Position: hero section, between headline and primary CTA. Not footer-only.

### Account Comparison Cards
- Max 3 tiers visible without scrolling.
- Badge "Most popular" on middle tier.
- Difference callout: "+Unlimited transfers" between tiers.
- CTA: "Open [Tier] account" — specific, not generic "Sign up".

---

## Copy & Messaging Patterns

| Context | Pattern | Example |
|---|---|---|
| Headline | `[Outcome] with [Differentiator]` | "Invest smarter with 0.3% fees" |
| CTA | Account-action | "Open account" / "Start investing" — not "Join now" |
| Trust | AUM or customer count | "2.4 million customers trust us with £18bn" |
| Fees | Monthly-first | "£9/month — cancel anytime" |
| Regulatory | Always visible | "[Company] is authorised by [Body], reg. [Number]" |

**Never:** "Guaranteed returns", countdown timers, approximate rounding on fee schedules.

---

## Design References
- Monzo (monzo.com) — card-first UX, clean onboarding, progressive disclosure
- Wise (wise.com) — fee transparency table, real-time calculator
- Revolut — dark mode dashboard, multi-currency display pattern
