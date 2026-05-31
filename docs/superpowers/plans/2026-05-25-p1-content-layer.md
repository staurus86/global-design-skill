# Phase 1 — Content Layer Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add 27 markdown files (13 industry sector files, 6 state files, 3 validator files, 2 feedback templates, 1 validation script) and update CLAUDE.md integration so AI tools automatically load the relevant sector context on business-related requests.

**Architecture:** All files are static markdown with YAML frontmatter. A Python validation script (`scripts/validate-industries.py`) is written first and used as the acceptance gate for every industry file. No code beyond the validator; no database; no server.

**Tech Stack:** Markdown, YAML frontmatter, Python 3.11 (validator only)

---

## File Map

**Create:**
```
industries/
  _index.md
  b2b-products.md, b2c-products.md, services.md, content-media.md
  education.md, health.md, finance.md, real-estate.md, travel.md
  tech-saas.md, non-profit.md, government.md, entertainment.md

patterns/states/
  _decision-matrix.md
  skeleton-states.md, partial-error-states.md, offline-states.md
  permission-states.md, rate-limit-states.md

validators/
  lighthouse-ci.md, axe-core.md, bundle-analyzer.md

feedback/
  gate-8-tracker.md, iteration-log.md

scripts/
  validate-industries.py
```

**Modify:**
```
integrations/claude-code/CLAUDE.md   — add industries/ reference
```

---

## Task 1: Validation Script

**Files:**
- Create: `scripts/validate-industries.py`

- [ ] **Step 1: Write the validator**

```python
#!/usr/bin/env python3
"""Validates industries/*.md files for required frontmatter and sections."""
import sys
from pathlib import Path
import re

REQUIRED_FRONTMATTER = {"version", "last_updated", "source", "stale_after_days"}
REQUIRED_SECTIONS = [
    "## Sector Profile",
    "## Mobile-First Rules",
    "## Required Elements",
    "## Banned Patterns",
    "## Trust Signals",
    "## Conversion Path",
    "## Typical Page Structure",
    "## Quick Diagnosis",
    "## Disambiguation",
]

def validate_file(path: Path) -> list[str]:
    errors = []
    text = path.read_text(encoding="utf-8")

    # Check frontmatter
    fm_match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not fm_match:
        errors.append(f"{path.name}: missing YAML frontmatter")
        return errors

    fm_text = fm_match.group(1)
    for key in REQUIRED_FRONTMATTER:
        if f"{key}:" not in fm_text:
            errors.append(f"{path.name}: frontmatter missing '{key}'")

    # Check sections
    for section in REQUIRED_SECTIONS:
        if section not in text:
            errors.append(f"{path.name}: missing section '{section}'")

    # No placeholder content
    for placeholder in ["TBD", "TODO", "PLACEHOLDER", "fill in"]:
        if placeholder in text:
            errors.append(f"{path.name}: contains placeholder '{placeholder}'")

    return errors

def main():
    root = Path(__file__).parent.parent
    industry_files = sorted((root / "industries").glob("*.md"))
    industry_files = [f for f in industry_files if f.name != "_index.md"]

    if not industry_files:
        print("No industry files found — create industries/*.md files first.")
        sys.exit(0)

    all_errors = []
    for f in industry_files:
        all_errors.extend(validate_file(f))

    if all_errors:
        print(f"VALIDATION FAILED — {len(all_errors)} error(s):")
        for e in all_errors:
            print(f"  ✗ {e}")
        sys.exit(1)
    else:
        print(f"VALIDATION PASSED — {len(industry_files)} file(s) valid.")

if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run on empty — confirm no files yet**

```bash
python scripts/validate-industries.py
```
Expected: `No industry files found — create industries/*.md first.`

- [ ] **Step 3: Commit**

```bash
git add scripts/validate-industries.py
git commit -m "feat(p1): add industries validation script"
```

---

## Task 2: industries/_index.md

**Files:**
- Create: `industries/_index.md`

- [ ] **Step 1: Write the file**

```markdown
# Industries Index

This directory maps 13 business sectors to design rules. AI tools read this
index first, then load the relevant sector file for the current request.

## Routing Logic

When a user request mentions a business context, determine the sector:

1. B2B product or service (equipment, SaaS, consulting, logistics) → `b2b-products.md`
2. Physical consumer product (bicycles, electronics, furniture) → `b2c-products.md`
3. Consumer service (therapy, cleaning, fitness, tarot) → `services.md`
4. Content or media publication → `content-media.md`
5. Course, training, or school → `education.md`
6. Medical, clinic, or wellness → `health.md`
7. Banking, insurance, fintech → `finance.md`
8. Property, rental, construction → `real-estate.md`
9. Hotel, tour, restaurant, travel → `travel.md`
10. Software product, SaaS, AI tool, developer tool → `tech-saas.md`
11. NGO, charity, foundation → `non-profit.md`
12. Government portal, civic service → `government.md`
13. Game, streaming, event, sports → `entertainment.md`

## Disambiguation

- SaaS sold to businesses → `b2b-products.md` if buyer is procurement/engineering;
  `tech-saas.md` if buyer is developer or power user
- Medical service → `health.md` not `services.md`
- No match → use generic rules from `rules/` and `blueprints/`

## Integration

This file is referenced from `integrations/claude-code/CLAUDE.md`.
Load the matching sector file before generating any design output.
```

- [ ] **Step 2: Commit**

```bash
git add industries/_index.md
git commit -m "feat(p1): add industries index with routing logic"
```

---

## Task 3: Industry Files — Batch A (b2b-products, b2c-products, services)

**Files:**
- Create: `industries/b2b-products.md`
- Create: `industries/b2c-products.md`
- Create: `industries/services.md`

- [ ] **Step 1: Write `industries/b2b-products.md`**

```markdown
---
version: 1.0.0
last_updated: 2026-05-25
source: manual
stale_after_days: 90
---

# B2B Products & Services

## Sector Profile
- **Decision pattern:** Rational, multi-stakeholder, long cycle (weeks–months)
- **Risk level:** High — money, reputation, career on the line
- **Key users:** Procurement officer, engineer, C-level buyer
- **Overlaps with:** `tech-saas.md` for software products with developer buyers

## Mobile-First Rules
- Technical specs tables must be readable without horizontal scroll at 390px
- RFQ forms: single-column layout on mobile, file upload button full-width
- Case study cards: stack vertically, show ROI metric above the fold on mobile

## Required Elements
- Technical specs / Data sheets (downloadable PDF)
- Case studies with quantified results (ROI %, cost saved, time saved)
- Certifications and compliance badges (ISO, CE, industry-specific)
- Team credentials and company history
- Comparison table vs competitors
- ROI calculator or savings estimator
- Demo / free trial CTA (not "Buy Now")
- Contact specialist form (not generic contact page)
- CAD / technical file downloads where applicable

## Banned Patterns
- "Buy Now" button for high-ticket or custom-quote products
- Hidden pricing with no indication of range
- Missing technical specifications
- Anonymous testimonials without company name and role
- Small font in spec tables (minimum 14px)
- Generic stock photos of offices or handshakes
- Single-page site with no navigation for complex product lines

## Trust Signals
- ISO 9001, AS9100, CE, API Q1, or industry-relevant certification badges
- Named case studies: "Company X reduced downtime by 34%"
- Client logo grid (recognisable brands in the buyer's industry)
- Years in operation and units sold/installed
- Factory or process photos (real, not stock)
- Named engineers or technical contacts with photos

## Conversion Path
- **Awareness:** Technical blog, white papers, trade show presence
- **Consideration:** Spec sheet download, technical webinar, CAD file access
- **Decision:** Demo request, RFQ submission, reference call
- **Action:** Quote → PO → onboarding

## Typical Page Structure
Problem → Solution overview → Technical specs → Case studies → Certifications → Process/team → Pricing range or RFQ → FAQ → Contact specialist

## Quick Diagnosis
1. Who pays? → Business (procurement / engineering)
2. What do they decide? → Buy / specify / recommend
3. Risk level? → High (affects production, compliance, budget)
4. Decision type? → Rational — requires evidence and specs
5. Primary value? → Reduce operational risk, improve efficiency

If answers match above → use B2B Products pattern.

## Disambiguation
- If the product is software and the buyer is a developer or SaaS admin → use `tech-saas.md`
- If the service is professional consulting with no physical product → still use this file
- If the product is sold direct-to-consumer (e.g. tools on Amazon) → use `b2c-products.md`
```

- [ ] **Step 2: Write `industries/b2c-products.md`**

```markdown
---
version: 1.0.0
last_updated: 2026-05-25
source: manual
stale_after_days: 90
---

# B2C Physical Products

## Sector Profile
- **Decision pattern:** Emotional + rational, comparison-heavy
- **Risk level:** Medium — money, disappointment, return hassle
- **Key users:** End consumer, sometimes gift buyer
- **Overlaps with:** `tech-saas.md` for consumer electronics with subscription

## Mobile-First Rules
- Product gallery: swipeable, minimum 3 images, pinch-to-zoom enabled
- "Add to Cart" button: sticky at bottom of screen on mobile product page
- Size/fit guide: accordion, loads inline (no new tab)
- Reviews: show star rating + count above the fold, load full list on scroll

## Required Elements
- High-quality photography: multiple angles, lifestyle, detail shots
- Technical specifications / attributes (size, weight, material, compatibility)
- Reviews with star rating, verified buyer badge, photo reviews
- Size guide or fit calculator where applicable
- Real-time stock status ("In stock", "Only 3 left", "Pre-order")
- Shipping cost and estimated delivery date
- Return and refund policy (visible, not buried)
- Related products / cross-sell block
- Wishlist / save for later

## Banned Patterns
- Single product photo
- Hidden shipping cost (revealed only at checkout)
- "Only 1 left!" when stock is actually unlimited
- Missing return policy link on product page
- Auto-play video with sound
- Forced account creation before checkout

## Trust Signals
- Star rating and review count in page title area
- User-generated photo reviews
- "Verified purchase" badge on reviews
- Secure checkout badge (SSL, payment logos)
- Returns / money-back guarantee callout
- Press mentions or award badges for premium products

## Conversion Path
- **Awareness:** Social media, influencer, search
- **Consideration:** Product page, review reading, comparison
- **Decision:** Size/fit confirmation, reviews validation
- **Action:** Add to cart → checkout

## Typical Page Structure
Product gallery → Name + price + rating → Variant selector → Add to Cart (sticky) → Description → Specs → Size guide → Reviews → Related products

## Quick Diagnosis
1. Who pays? → Consumer (individual)
2. What do they decide? → Buy a physical item
3. Risk level? → Medium (money, expectation mismatch)
4. Decision type? → Comparison + social validation
5. Primary value? → Desire fulfilment, status, utility

## Disambiguation
- Software, apps, or subscriptions → use `tech-saas.md`
- Service (not a physical item) → use `services.md`
```

- [ ] **Step 3: Write `industries/services.md`**

```markdown
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
```

- [ ] **Step 4: Run validator**

```bash
python scripts/validate-industries.py
```
Expected: `VALIDATION PASSED — 3 file(s) valid.`

- [ ] **Step 5: Commit**

```bash
git add industries/b2b-products.md industries/b2c-products.md industries/services.md
git commit -m "feat(p1): add industry files — b2b-products, b2c-products, services"
```

---

## Task 4: Industry Files — Batch B (content-media, education, health)

**Files:**
- Create: `industries/content-media.md`
- Create: `industries/education.md`
- Create: `industries/health.md`

- [ ] **Step 1: Write `industries/content-media.md`**

```markdown
---
version: 1.0.0
last_updated: 2026-05-25
source: manual
stale_after_days: 90
---

# Content & Media

## Sector Profile
- **Decision pattern:** Interest + habit, low commitment entry
- **Risk level:** Low — time and attention only
- **Key users:** Reader, listener, viewer, subscriber
- **Overlaps with:** `education.md` for editorial sites that sell courses

## Mobile-First Rules
- Article body: 16px minimum, 65–75ch line length, generous line-height (1.6–1.8)
- Reading progress indicator at top of long-form articles
- Subscribe CTA: bottom-of-article placement, not intrusive modal on entry

## Required Elements
- Clear content hierarchy (featured, recent, categories)
- Search and filter by topic, date, or content type
- Category and tag taxonomy
- Related content block at end of each piece
- Subscribe / follow CTA
- Author bio with photo and credentials
- Estimated read time or content length
- Social share buttons (after consuming, not before)

## Banned Patterns
- Paywall with no preview (show at least 2 paragraphs)
- Autoplay video with sound on page load
- Entry pop-up that blocks content before reading
- Infinite scroll with no way to reach the footer or navigate back
- Font smaller than 16px for body text
- More ads than content visible above the fold

## Trust Signals
- Author photo, name, and publication date
- Source citations and external links
- Editorial standards or "About" page
- Subscriber or follower count
- Awards or press recognition

## Conversion Path
- **Awareness:** Search, social share, referral
- **Consideration:** Headline + preview scan
- **Decision:** Read full article
- **Action:** Subscribe, share, return visit

## Typical Page Structure
Featured article → Recent posts grid → Categories → Newsletter CTA → Archive / search

## Quick Diagnosis
1. Who pays? → Reader (with attention) or advertiser
2. What do they decide? → Read, watch, listen, or subscribe
3. Risk level? → Low
4. Decision type? → Interest-driven, habitual
5. Primary value? → Information, entertainment, inspiration

## Disambiguation
- Site sells courses alongside editorial content → add `education.md` rules for course pages
- Podcast site with merch → add `entertainment.md` rules for the store section
```

- [ ] **Step 2: Write `industries/education.md`**

```markdown
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
```

- [ ] **Step 3: Write `industries/health.md`**

```markdown
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
```

- [ ] **Step 4: Run validator**

```bash
python scripts/validate-industries.py
```
Expected: `VALIDATION PASSED — 6 file(s) valid.`

- [ ] **Step 5: Commit**

```bash
git add industries/content-media.md industries/education.md industries/health.md
git commit -m "feat(p1): add industry files — content-media, education, health"
```

---

## Task 5: Industry Files — Batch C (finance, real-estate, travel)

**Files:**
- Create: `industries/finance.md`
- Create: `industries/real-estate.md`
- Create: `industries/travel.md`

- [ ] **Step 1: Write `industries/finance.md`**

```markdown
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
```

- [ ] **Step 2: Write `industries/real-estate.md`**

```markdown
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
```

- [ ] **Step 3: Write `industries/travel.md`**

```markdown
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
```

- [ ] **Step 4: Run validator**

```bash
python scripts/validate-industries.py
```
Expected: `VALIDATION PASSED — 9 file(s) valid.`

- [ ] **Step 5: Commit**

```bash
git add industries/finance.md industries/real-estate.md industries/travel.md
git commit -m "feat(p1): add industry files — finance, real-estate, travel"
```

---

## Task 6: Industry Files — Batch D (tech-saas, non-profit, government, entertainment)

**Files:**
- Create: `industries/tech-saas.md`
- Create: `industries/non-profit.md`
- Create: `industries/government.md`
- Create: `industries/entertainment.md`

- [ ] **Step 1: Write `industries/tech-saas.md`**

```markdown
---
version: 1.0.0
last_updated: 2026-05-25
source: manual
stale_after_days: 90
---

# Tech & SaaS

## Sector Profile
- **Decision pattern:** Innovation + proof, early-adopter or enterprise
- **Risk level:** Medium to high — integration risk, data migration, team adoption
- **Key users:** Developer, product manager, technical buyer, SaaS admin
- **Overlaps with:** `b2b-products.md` for enterprise software sold to procurement

## Mobile-First Rules
- Demo / product preview: responsive iframe or screenshot, not Flash/video-only
- Pricing table: horizontally scrollable on mobile, most popular plan centre-visible
- Documentation link: in primary navigation, accessible without scrolling

## Required Elements
- Clear value proposition in plain language (no buzzwords without explanation)
- Interactive demo or product tour
- Documentation or API reference link
- Pricing plans with feature comparison table
- Use case examples with named company stories
- Integration list (compatible tools, platforms, APIs)
- Security and compliance information (SOC 2, GDPR, HIPAA if relevant)
- Community or developer Discord / forum
- Changelog or "What's new" section

## Banned Patterns
- Buzzword-only descriptions ("AI-powered synergistic platform")
- Pricing hidden behind "contact sales" for self-serve plans
- No documentation accessible before sign-up
- Fake social proof (stock photos, fabricated company names)
- Missing integration list for a product that requires integrations

## Trust Signals
- Named customers with logos (recognisable companies)
- G2 / Capterra / Product Hunt badge with score
- GitHub stars for developer tools
- SOC 2 Type II or equivalent security certification
- Uptime SLA and status page link
- Founder or team LinkedIn with technical background

## Conversion Path
- **Awareness:** Developer community, ProductHunt, search, HN
- **Consideration:** Demo, documentation, pricing review
- **Decision:** Free trial, sandbox environment, integration test
- **Action:** Sign up → connect first integration → aha moment

## Typical Page Structure
Value proposition → Demo / interactive preview → Use cases → Pricing → Integrations → Security → Community → Sign up CTA

## Quick Diagnosis
1. Who pays? → Developer, SaaS admin, or enterprise buyer
2. What do they decide? → Adopt a software tool or platform
3. Risk level? → Medium–high (integration, data, team change)
4. Decision type? → Technical validation + proof of value
5. Primary value? → Save time, automate workflow, scale

## Disambiguation
- Physical tech product (hardware, IoT device) → use `b2b-products.md`
- Consumer app (social, games) → use `entertainment.md` or `b2c-products.md`
- Sold to enterprise procurement (not developers) → also apply `b2b-products.md` trust signals
```

- [ ] **Step 2: Write `industries/non-profit.md`**

```markdown
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
```

- [ ] **Step 3: Write `industries/government.md`**

```markdown
---
version: 1.0.0
last_updated: 2026-05-25
source: manual
stale_after_days: 90
---

# Government & Civic Services

## Sector Profile
- **Decision pattern:** Task completion, not persuasion — citizen needs to do a thing
- **Risk level:** Low–high depending on service (renew passport = high, find library = low)
- **Key users:** Citizen, resident, business operator seeking public services
- **Overlaps with:** `non-profit.md` for mission-driven civic organisations

## Mobile-First Rules
- Service finder / search: full-width, prominent, above the fold on mobile
- Forms: one question per page (GDS pattern), progress indicator, save and return
- Emergency / urgent services: top of every page, persistent, high contrast

## Required Elements
- Clear service description in plain language (reading age ≤ 9)
- Step-by-step process explanation before the form
- Eligibility criteria clearly stated upfront
- Expected processing time and what happens next
- Contact or support channel (phone, in-person, chat)
- Accessibility statement (WCAG AA mandatory, AAA target)
- Multi-language support for the primary community languages served
- Privacy notice specific to the service

## Banned Patterns
- Jargon or bureaucratic language without plain-language explanation
- Forcing account creation for simple information requests
- Hiding contact information
- Political bias in service description
- Outdated information without date stamp and review date

## Trust Signals
- Government logo and official domain (.gov, .gc.ca, etc.)
- Last reviewed / updated date
- Official contact information and address
- Privacy and data protection statement

## Conversion Path
- **Awareness:** Search, referral from another service
- **Consideration:** Eligibility check, process understanding
- **Decision:** Documents / prerequisites confirmed
- **Action:** Complete service (form, payment, appointment)

## Typical Page Structure
Service title → What this service does (plain language) → Who it's for (eligibility) → What you'll need → Step-by-step process → Apply / book → Contact for help

## Quick Diagnosis
1. Who pays? → Citizen (with taxes or service fee)
2. What do they decide? → Complete a civic task or access a public service
3. Risk level? → Varies (passport = high, library hours = low)
4. Decision type? → Task-completion, not persuasion
5. Primary value? → Efficiency, clarity, accessibility

## Disambiguation
- NGO delivering social services → use `non-profit.md`
- Government technology product sold commercially → use `tech-saas.md`
```

- [ ] **Step 4: Write `industries/entertainment.md`**

```markdown
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
```

- [ ] **Step 5: Run validator**

```bash
python scripts/validate-industries.py
```
Expected: `VALIDATION PASSED — 13 file(s) valid.`

- [ ] **Step 6: Commit**

```bash
git add industries/tech-saas.md industries/non-profit.md industries/government.md industries/entertainment.md
git commit -m "feat(p1): add industry files — tech-saas, non-profit, government, entertainment"
```

---

## Task 7: patterns/states/ Files

**Files:**
- Create: `patterns/states/_decision-matrix.md`
- Create: `patterns/states/skeleton-states.md`
- Create: `patterns/states/partial-error-states.md`
- Create: `patterns/states/offline-states.md`
- Create: `patterns/states/permission-states.md`
- Create: `patterns/states/rate-limit-states.md`

- [ ] **Step 1: Write `patterns/states/_decision-matrix.md`**

```markdown
# State Decision Matrix

This file extends the existing 9-state system (idle / hover / active / focus /
disabled / loading / empty / error / success) with 5 additional states.

No existing states are replaced. The matrix below determines which state to use
when multiple options are applicable.

## When to Use Each State

| State | Trigger condition | Typical duration | Example |
|-------|------------------|-----------------|---------|
| `loading` (spinner) | Wait < 1s, data volume unknown, no structure predictable | Short | Form submit, auth check |
| `skeleton` | Wait > 1s AND content structure is known before data arrives | Medium (1–10s) | Product list, article feed, user profile |
| `partial-error` | Main content loaded successfully; a subset of data failed | Persistent until retry | Table with 2/10 rows errored, dashboard widget unavailable |
| `offline` | Network connection lost, PWA or offline-capable app | Until reconnect | Dashboard with stale cached data |
| `permission` | User authenticated but lacks access to this resource | Persistent | Locked plan feature, role-restricted section |
| `rate-limit` | Too many requests sent; server returned 429 | Timed (until cooldown expires) | API quota exhausted, search throttled |

## Decision Rules

**loading vs skeleton:**
- Use `skeleton` when you know the layout before the data (e.g. a list of cards will have a title, subtitle, and image).
- Use `loading` when the result shape is unknown (e.g. an AI-generated response, a form validation result).
- Never show both for the same element simultaneously.

**error vs partial-error:**
- Use `error` when the entire component or page failed to load.
- Use `partial-error` when some data loaded and some did not — the user can still use part of the UI.

**offline vs error:**
- Use `offline` when `navigator.onLine === false` or the app detects a network-level failure.
- Use `error` for server errors (5xx) or application errors when the network is available.

**permission vs disabled:**
- Use `disabled` for UI controls that are not available in the current context or state (e.g. submit button before form is valid).
- Use `permission` for entire features or pages the user cannot access due to role or plan.
```

- [ ] **Step 2: Write `patterns/states/skeleton-states.md`**

```markdown
# Skeleton States

Use when: wait > 1s AND content structure is known before data arrives.

## Variants

### Shimmer (recommended default)
A gradient animation moves left-to-right across the placeholder shape.
Conveys that loading is active and progressive.

```css
@keyframes shimmer {
  0%   { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}

.skeleton {
  background: linear-gradient(
    90deg,
    var(--color-surface-2) 25%,
    var(--color-surface-3) 50%,
    var(--color-surface-2) 75%
  );
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
  border-radius: var(--radius-sm);
}
```

### Pulse
The entire placeholder fades in and out. Use when shimmer is too distracting
(e.g. dense data tables).

```css
@keyframes pulse {
  0%, 100% { opacity: 1; }
  50%       { opacity: 0.4; }
}

.skeleton--pulse {
  background: var(--color-surface-2);
  animation: pulse 1.5s ease-in-out infinite;
}
```

## Skeleton Structure Rules
- Match the skeleton shape to the real content dimensions (height, width, line count).
- Use `border-radius` to match card or avatar radius.
- Show at least 3 placeholder items in a list to convey list structure.
- Do not show a spinner AND skeleton simultaneously for the same element.
- Respect `prefers-reduced-motion`: remove animation, keep static placeholder shape.

```css
@media (prefers-reduced-motion: reduce) {
  .skeleton, .skeleton--pulse {
    animation: none;
  }
}
```

## Accessibility
- Wrap skeleton region in `aria-busy="true"` and `aria-label="Loading content"`.
- Remove `aria-busy` once content loads.
- Do not use `role="status"` on the skeleton itself — use it on a visually-hidden live region that announces completion.
```

- [ ] **Step 3: Write remaining state files**

`patterns/states/partial-error-states.md`:

```markdown
# Partial Error States

Use when: main content loaded; a subset of data failed.

## Pattern: Inline Error Row

For tables or lists where some rows failed to load:

```html
<tr class="row--error" aria-label="Row failed to load">
  <td colspan="4">
    <span class="error-icon" aria-hidden="true">⚠</span>
    Failed to load data for this item.
    <button type="button" onclick="retryRow(id)">Retry</button>
  </td>
</tr>
```

```css
.row--error { background: var(--color-error-surface); }
```

## Pattern: Degraded-Mode Banner

For dashboard widgets or sections that loaded partially:

```html
<div role="alert" class="banner banner--warning">
  Some data could not be loaded. Showing cached results from
  <time datetime="2026-05-25T10:00:00Z">10:00 AM</time>.
  <button type="button">Retry</button>
</div>
```

## Rules
- Always show what DID load — do not blank the whole component.
- Provide a retry action per failed unit, not just a global page refresh.
- Show the timestamp of the last successful data if displaying cached content.
- Never use red for a partial error that does not require user action.
```

`patterns/states/offline-states.md`:

```markdown
# Offline States

Use when: `navigator.onLine === false` or network-level failure detected.

## Pattern: Offline Banner

Persistent, dismissible banner at top of page:

```html
<div role="status" aria-live="polite" class="banner banner--offline">
  <span aria-hidden="true">📶</span>
  You are offline. Some features may not be available.
  Last synced: <time datetime="2026-05-25T09:45:00Z">9:45 AM</time>
</div>
```

## Pattern: Sync Queue Indicator

Show pending actions queued for when connection returns:

```html
<div class="sync-queue" aria-label="3 changes pending sync">
  <span class="sync-queue__count">3</span> unsaved changes
  will sync when you're back online.
</div>
```

## Rules
- Show offline state within 2 seconds of connection loss.
- Always show the last sync time so users know how stale cached data is.
- Disable (not hide) actions that require network — show tooltip explaining why.
- Automatically dismiss banner and trigger sync on reconnect.
- Announce reconnection to screen readers via `aria-live="polite"`.
```

`patterns/states/permission-states.md`:

```markdown
# Permission States

Use when: user is authenticated but cannot access a feature due to plan or role.

## Pattern: Locked Feature (upgrade path)

```html
<div class="feature--locked" aria-label="Feature requires Pro plan">
  <div class="feature__preview" aria-hidden="true">
    <!-- blurred or greyed preview of the feature -->
  </div>
  <div class="feature__gate">
    <h3>Available on Pro</h3>
    <p>Unlock advanced analytics and custom exports.</p>
    <a href="/upgrade" class="btn btn--primary">Upgrade to Pro</a>
    <a href="/compare-plans">Compare plans</a>
  </div>
</div>
```

## Pattern: Role-Restricted Section

```html
<div role="alert" class="permission-notice">
  <p>You don't have permission to view this section.</p>
  <p>Contact your workspace admin to request access.</p>
</div>
```

## Rules
- Never hide locked features — always show them with a clear unlock path.
- Distinguish between "upgrade required" (commercial) and "admin approval required" (role).
- Do not use `disabled` attribute on entire sections — use `aria-disabled` and the permission pattern.
- Show a preview (blurred or reduced) to communicate the value before the gate.
```

`patterns/states/rate-limit-states.md`:

```markdown
# Rate Limit States

Use when: server returns 429 or the app enforces a client-side quota.

## Pattern: Cooldown Timer

```html
<div role="alert" aria-live="assertive" class="rate-limit-notice">
  <p>Too many requests. Try again in
    <strong><time id="cooldown-timer">0:45</time></strong>.
  </p>
</div>
```

```js
function startCooldown(seconds) {
  const el = document.getElementById('cooldown-timer');
  const end = Date.now() + seconds * 1000;

  const tick = () => {
    const remaining = Math.ceil((end - Date.now()) / 1000);
    if (remaining <= 0) {
      el.closest('[role="alert"]').hidden = true;
      return;
    }
    const m = Math.floor(remaining / 60);
    const s = remaining % 60;
    el.textContent = `${m}:${s.toString().padStart(2, '0')}`;
    setTimeout(tick, 1000);
  };
  tick();
}
```

## Pattern: Quota Progress Bar

For API plans with monthly limits:

```html
<div class="quota-meter" role="meter" aria-valuenow="850"
     aria-valuemin="0" aria-valuemax="1000"
     aria-label="API calls this month: 850 of 1000">
  <div class="quota-meter__fill" style="width: 85%"></div>
  <span>850 / 1000 API calls used</span>
</div>
```

## Rules
- Always show the exact remaining wait time, not "please wait".
- Disable the triggering action for the duration of the cooldown.
- Provide an upgrade path when rate limit is a plan constraint.
- Never silently drop requests — always inform the user.
```

- [ ] **Step 4: Commit**

```bash
git add patterns/states/
git commit -m "feat(p1): add state decision matrix and 5 extended state files"
```

---

## Task 8: validators/ and feedback/ Files

**Files:**
- Create: `validators/lighthouse-ci.md`
- Create: `validators/axe-core.md`
- Create: `validators/bundle-analyzer.md`
- Create: `feedback/gate-8-tracker.md`
- Create: `feedback/iteration-log.md`

- [ ] **Step 1: Write validators files**

`validators/lighthouse-ci.md`:

```markdown
# Lighthouse CI Integration

## Performance Budgets

| Metric | Target | Fail threshold |
|--------|--------|---------------|
| LCP (Largest Contentful Paint) | < 2.5s | > 4s |
| CLS (Cumulative Layout Shift) | < 0.1 | > 0.25 |
| FID / INP | < 100ms | > 300ms |
| Performance score | ≥ 90 | < 75 |
| Accessibility score | ≥ 90 | < 80 |
| Best Practices score | ≥ 90 | < 80 |

## CI Configuration (GitHub Actions)

```yaml
# .github/workflows/lighthouse.yml
name: Lighthouse CI
on: [push, pull_request]
jobs:
  lighthouse:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '20' }
      - run: npm ci
      - run: npm run build
      - uses: treosh/lighthouse-ci-action@v11
        with:
          urls: |
            http://localhost:3000
            http://localhost:3000/pricing
          budgetPath: ./lighthouse-budget.json
          uploadArtifacts: true
```

`lighthouse-budget.json`:

```json
[
  {
    "path": "/*",
    "timings": [
      { "metric": "largest-contentful-paint", "budget": 2500 },
      { "metric": "cumulative-layout-shift",  "budget": 0.1 },
      { "metric": "interactive",              "budget": 5000 }
    ],
    "audits": [
      { "id": "uses-optimized-images",     "warn": 0 },
      { "id": "render-blocking-resources", "warn": 0 }
    ]
  }
]
```

## Running Locally

```bash
npm install -g @lhci/cli
lhci autorun --collect.url=http://localhost:3000
```
```

`validators/axe-core.md`:

```markdown
# axe-core Accessibility Testing

## Thresholds

| Violation severity | Threshold | Action |
|-------------------|-----------|--------|
| critical | 0 | Block merge |
| serious  | 0 | Block merge |
| moderate | ≤ 3 | Warning, review required |
| minor    | any | Info only |

## Playwright Integration

```ts
// tests/a11y.spec.ts
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test('homepage passes axe accessibility check', async ({ page }) => {
  await page.goto('/');
  const results = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa', 'wcag21aa'])
    .analyze();

  const critical = results.violations.filter(v => v.impact === 'critical');
  const serious  = results.violations.filter(v => v.impact === 'serious');

  expect(critical, `Critical violations: ${JSON.stringify(critical, null, 2)}`).toHaveLength(0);
  expect(serious,  `Serious violations: ${JSON.stringify(serious, null, 2)}`).toHaveLength(0);
});
```

## Jest Integration

```ts
// jest.setup.ts
import 'jest-axe/extend-expect';

// component.test.tsx
import { render } from '@testing-library/react';
import { axe } from 'jest-axe';
import { MyComponent } from './MyComponent';

it('has no accessibility violations', async () => {
  const { container } = render(<MyComponent />);
  expect(await axe(container)).toHaveNoViolations();
});
```
```

`validators/bundle-analyzer.md`:

```markdown
# Bundle Size Limits

## Size Targets Per Component Type

| Component type | Max JS (gzipped) | Notes |
|---------------|-----------------|-------|
| Leaf component (Button, Input) | 2 KB | No external deps |
| Composite component (Form, Modal) | 8 KB | Shared chunks excluded |
| Page component | 30 KB | First load JS |
| Full application shell | 80 KB | Initial bundle |
| Third-party library (single) | 20 KB | Prefer tree-shakeable |

## Next.js Bundle Analysis

```bash
ANALYZE=true npm run build
```

`next.config.ts`:

```ts
import BundleAnalyzer from '@next/bundle-analyzer';

const withBundleAnalyzer = BundleAnalyzer({
  enabled: process.env.ANALYZE === 'true',
});

export default withBundleAnalyzer({ /* your config */ });
```

## Tree-Shaking Checklist

- [ ] Import named exports only: `import { Button } from './ui'` not `import * as UI`
- [ ] No `export default` on libraries — use named exports
- [ ] `sideEffects: false` in `package.json` for component libraries
- [ ] Check with: `npx webpack-bundle-analyzer stats.json`
```

- [ ] **Step 2: Write feedback files**

`feedback/gate-8-tracker.md`:

```markdown
# Gate 8 Tracker

Gate 8 = "Developer can implement without asking a follow-up question."

Log every instance where a developer asked a question after receiving a
handoff spec. Each entry is a Gate 8 failure that improves future specs.

## Log Entry Template

```
Date: YYYY-MM-DD
Component: [component name]
Question asked: [exact question]
Root cause: [ ] Missing state  [ ] Ambiguous token  [ ] Missing ARIA
            [ ] No error spec  [ ] Missing interaction  [ ] Other: ___
Fix applied: [what was added to the spec]
Prevented by: [which spec section should have covered this]
```

## Aggregate Metrics (update weekly)

| Metric | Value |
|--------|-------|
| Gate 8 failures this sprint | |
| Most common root cause | |
| Average questions per handoff | |
| Target: questions per handoff | 0 |
```

`feedback/iteration-log.md`:

```markdown
# Design Iteration Log

Track how many rounds of revision each design output required before acceptance.
Low iteration count = skill is producing correct output. High count = a rule or
pattern needs updating.

## Log Entry Template

```
Date: YYYY-MM-DD
Task type: [ ] Landing page  [ ] Component  [ ] Admin panel  [ ] Other: ___
Iterations to acceptance: [number]
Round 1 rejection reason: [what was wrong]
Round 2+ rejection reasons: [what was still wrong]
Pattern implicated: [which file should be updated to prevent this]
```

## Aggregate Metrics (update weekly)

| Metric | Value |
|--------|-------|
| Average iterations this sprint | |
| Median iterations | |
| Tasks accepted in 1 iteration | |
| Target: accepted in ≤ 2 iterations | 80% |
```

- [ ] **Step 3: Commit**

```bash
git add validators/ feedback/
git commit -m "feat(p1): add validators and feedback templates"
```

---

## Task 9: Update CLAUDE.md Integration

**Files:**
- Modify: `integrations/claude-code/CLAUDE.md`

- [ ] **Step 1: Read current file**

Open `integrations/claude-code/CLAUDE.md` and locate the reference files table or the section where file categories are listed.

- [ ] **Step 2: Add industries reference**

Add the following block to the file, in the reference table or after the rules section:

```markdown
## Industry Context (new in v1.5.0)

When the user request mentions a business, product, or service:
1. Open `industries/_index.md` to identify the correct sector
2. Load the matching `industries/<sector>.md` file
3. Apply sector-specific Required Elements, Banned Patterns, Trust Signals,
   and Conversion Path rules before generating any design output

If no sector matches, proceed with generic rules from `rules/` and `blueprints/`.

## Extended States (new in v1.5.0)

The 9-state system is extended to 14 states. Read `patterns/states/_decision-matrix.md`
when designing loading, error, or access-control interactions.
```

- [ ] **Step 3: Run validator one final time**

```bash
python scripts/validate-industries.py
```
Expected: `VALIDATION PASSED — 13 file(s) valid.`

- [ ] **Step 4: Commit**

```bash
git add integrations/claude-code/CLAUDE.md
git commit -m "feat(p1): update CLAUDE.md with industries and extended states references"
```

---

## Self-Review Checklist

- [x] All 13 industry files have required frontmatter and 9 sections
- [x] `government.md` is a separate file (not merged into non-profit)
- [x] `entertainment.md` has sub-niche section with `sub_niche` values listed
- [x] `patterns/states/_decision-matrix.md` covers loading vs skeleton rule explicitly
- [x] Validation script rejects files missing any required section
- [x] No TBD, TODO, or placeholder text in any file
- [x] CLAUDE.md updated to reference both `industries/` and `patterns/states/`
