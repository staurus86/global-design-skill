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

---

## Design System for This Sector

### Color Strategy

Official, accessible, high-contrast. Follow established government design systems where they exist (GOV.UK: crown blue; US Digital Service: navy). Avoid gradients, decorative color, or brand-style palettes — this sector prioritises clarity over aesthetics.

```css
/* Government — accessible, authoritative, clear */
--color-bg:         oklch(100% 0 0);       /* pure white — maximum contrast */
--color-accent:     oklch(38% 0.14 255);  /* official blue */
--color-focus:      oklch(80% 0.22 88);   /* yellow focus ring (GOV.UK pattern) */
--color-text:       oklch(14% 0 0);       /* near-black */
--color-success:    oklch(36% 0.15 145);  /* dark green — confirmation */
--color-error:      oklch(42% 0.22 25);   /* dark red — form errors */
--color-warning:    oklch(55% 0.18 75);   /* amber — important notices */
--color-border:     oklch(60% 0 0);       /* mid-gray — form field borders */
```

WCAG AA is mandatory; target AAA for text on backgrounds. Focus ring: minimum 3px solid `--color-focus`.

### Typography
- System fonts only (or government-mandated typeface): no web fonts that add download overhead for rural/slow connections.
- Body: minimum 19px (GOV.UK standard — larger than typical web default).
- `line-height: 1.5` minimum on all body text.
- Links: underline always visible — never remove underline from body links.
- Labels: bold, adjacent to input (never placeholder-only).

### Spacing & Density
One question or concept per page (GDS interaction design pattern). Forms: generous vertical spacing between fields (min `var(--space-6)`). Long content: side navigation with anchor links for page sections.

---

## Key Component Patterns

### Step-by-Step Form (GDS Pattern)
One question per page. Progress always visible.

```html
<div class="step-header">
  <span class="step-count">Step 3 of 7</span>
  <progress value="3" max="7" aria-label="Step 3 of 7"></progress>
</div>

<form>
  <fieldset>
    <legend><h1>What is your date of birth?</h1></legend>
    <div class="dob-inputs">
      <label for="day">Day</label><input id="day" name="day" type="text" inputmode="numeric" maxlength="2">
      <label for="month">Month</label><input id="month" name="month" type="text" inputmode="numeric" maxlength="2">
      <label for="year">Year</label><input id="year" name="year" type="text" inputmode="numeric" maxlength="4">
    </div>
  </fieldset>
  <button type="submit">Continue</button>
</form>
```

### Service Start Page
```
[Service title — plain language, H1]
[What you can do with this service — 2–3 bullet points]
[Who this service is for — eligibility in plain English]
[What you'll need — document checklist before starting]
[How long it takes — expected processing time]
[Start now →]
```

### Eligibility Checker (Before Main Form)
```
Before you start, check you're eligible:
☐ You must be 18 or over
☐ You must live in [Country/Region]
☐ You must have a [Document type]

[I am eligible — start application]
[I'm not sure — get help]
```

### Document Checklist
```html
<ul class="checklist" role="list">
  <li class="checklist-item">
    <span class="check-icon" aria-hidden="true">☐</span>
    <span>National Insurance number</span>
    <span class="hint">Found on payslips or HMRC letters</span>
  </li>
</ul>
```

### Status Tracker
```
Application submitted     ✓ Completed  — 3 Jan 2026
Under review             ◉ In progress — Est. 15 working days
Decision made            ○ Not started
```

---

## Copy & Messaging Patterns

| Context | Pattern | Example |
|---|---|---|
| Service title | Verb-first | "Apply for a parking permit" not "Parking Permit Application Portal" |
| Eligibility | Positive conditions | "You can use this if..." not "This service is not available to..." |
| Error | Specific fix | "Enter your date of birth in the format DD MM YYYY" not "Invalid date" |
| Confirmation | What happens next | "We'll send a decision within 15 working days to [email]" |
| Support | Multiple channels | "Call 0300 XXX XXXX · Mon–Fri 9am–5pm" always visible |

Plain language rule: use the word a 9-year-old would use. Replace "initiate" with "start", "utilise" with "use", "prior to" with "before".

---

## Design References
- GOV.UK Design System (design-system.service.gov.uk) — the global standard for government UI
- USDS Design System (designsystem.digital.gov) — US equivalent
- Ontario Design System (design.ontario.ca) — accessible bilingual pattern
