# Landing Page Conversion Review Checklist

> Run before any landing page goes live. Each item is pass/fail. A page with CRITICAL failures must not launch. Track conversion metrics against baseline after every change.

**Legend:** ✅ Pass · ❌ Fail (blocks launch) · ⚠️ Needs review · N/A Not applicable

---

## 1. Above-the-Fold Audit

*Everything visible without scrolling on a 768px viewport.*

| # | Check | Priority | Status |
|---|---|---|---|
| 1.1 | Value proposition is clear within 5 seconds — can a stranger describe what this is? | CRITICAL | |
| 1.2 | Primary CTA is visible above fold without scrolling | CRITICAL | |
| 1.3 | Headline ≤ 3 lines on the smallest target viewport | CRITICAL | |
| 1.4 | Headline follows formula: [Outcome] for [Audience] without [Pain] | CRITICAL | |
| 1.5 | Subheadline adds specificity (not a repeat of headline in different words) | IMPORTANT | |
| 1.6 | No more than 1 primary CTA above fold | CRITICAL | |
| 1.7 | Hero image/visual relates to the offer — not decorative stock | IMPORTANT | |
| 1.8 | LCP element identified and has `fetchpriority="high"` | CRITICAL | |

---

## 2. CTA Quality

| # | Check | Priority | Status |
|---|---|---|---|
| 2.1 | CTA label describes the action: Verb + Object + Context | CRITICAL | |
| 2.2 | Banned generic CTAs absent: "Get Started", "Learn More", "Submit", "Click Here" | CRITICAL | |
| 2.3 | CTA communicates what happens next (not just what user should do) | IMPORTANT | |
| 2.4 | Primary CTA repeats at each section transition (not only in hero) | IMPORTANT | |
| 2.5 | Secondary CTA is visually subordinate (ghost/text only — never two filled buttons) | CRITICAL | |
| 2.6 | CTA buttons ≥ 44px height, sufficient padding on sides | CRITICAL | |
| 2.7 | Risk reduction near CTA: "No credit card required", "Cancel anytime", etc. | IMPORTANT | |
| 2.8 | CTA in final section of page before footer | IMPORTANT | |

---

## 3. AIDA Structure

| # | Check | Priority | Status |
|---|---|---|---|
| 3.1 | Attention: hero creates a sharp, specific hook (not generic headline) | CRITICAL | |
| 3.2 | Interest: section 2-3 provides evidence, specifics, demos — not more claims | CRITICAL | |
| 3.3 | Desire: social proof, benefits, outcomes — close to the CTA | CRITICAL | |
| 3.4 | Action: one clear final CTA — not multiple competing options | CRITICAL | |
| 3.5 | All four phases present — no phase missing or merged into one section | IMPORTANT | |
| 3.6 | No information dump in hero (hero = Attention only, not Interest + Desire too) | IMPORTANT | |

---

## 4. Social Proof

| # | Check | Priority | Status |
|---|---|---|---|
| 4.1 | Social proof placed near CTA, not buried at bottom | IMPORTANT | |
| 4.2 | Testimonials have: full name + title + company + photo + specific claim | CRITICAL | |
| 4.3 | No fabricated metrics: "99.9% uptime", "50% faster", "10× ROI" without source | CRITICAL | |
| 4.4 | Logo bar uses recognizable company logos (not unknown brands) | IMPORTANT | |
| 4.5 | Review score shows total count: "4.8/5 (2,847 reviews)" not "4.8/5" | IMPORTANT | |
| 4.6 | Testimonials are specific — mention the problem solved, not generic praise | IMPORTANT | |
| 4.7 | Social proof recency visible (dated testimonials, "used by 12,000 teams in 2026") | NICE | |

---

## 5. Friction Inventory

*Friction is anything that makes the user hesitate, slow down, or leave.*

| # | Check | Priority | Status |
|---|---|---|---|
| 5.1 | Sign-up form: only fields that are actually necessary | CRITICAL | |
| 5.2 | Password requirements shown before user types (not after error) | IMPORTANT | |
| 5.3 | Email field is type="email" (gets native validation + mobile keyboard) | IMPORTANT | |
| 5.4 | No CAPTCHA on initial conversion (move to post-signup if needed) | IMPORTANT | |
| 5.5 | Social login available alongside email form (reduces friction) | NICE | |
| 5.6 | Form submit button says what happens: "Create free account" not "Submit" | CRITICAL | |
| 5.7 | Privacy micro-copy near email field: "No spam. Unsubscribe anytime." | IMPORTANT | |
| 5.8 | After form submit: explicit next step communicated ("Check your email") | CRITICAL | |

---

## 6. Objection Handling

| # | Check | Priority | Status |
|---|---|---|---|
| 6.1 | FAQ section addresses real user objections (not company FAQs) | IMPORTANT | |
| 6.2 | Pricing objection handled: free tier / trial / money-back guarantee visible | CRITICAL | |
| 6.3 | "Is this for me?" objection addressed via specific audience targeting | IMPORTANT | |
| 6.4 | Implementation objection handled: setup time, complexity, required skills | IMPORTANT | |
| 6.5 | FAQ uses FAQPage schema markup (JSON-LD) | IMPORTANT | |

---

## 7. Pricing Clarity (if pricing page)

| # | Check | Priority | Status |
|---|---|---|---|
| 7.1 | Price shown in USD or local currency (never "Contact for pricing" for self-serve) | CRITICAL | |
| 7.2 | Annual vs. monthly toggle with savings shown ("Save 20%") | IMPORTANT | |
| 7.3 | Recommended tier visually distinct (scaled, badge, different border) | IMPORTANT | |
| 7.4 | Feature comparison table shows what each tier includes AND excludes | CRITICAL | |
| 7.5 | Decoy pricing present: middle tier provides better value-per-dollar | NICE | |
| 7.6 | Price anchoring: most expensive tier shown first (left to right) | NICE | |
| 7.7 | Free trial or money-back guarantee labeled directly on CTA | IMPORTANT | |

---

## 8. Mobile Experience

| # | Check | Priority | Status |
|---|---|---|---|
| 8.1 | Tested on 390px width (iPhone 14 Pro) | CRITICAL | |
| 8.2 | CTA button full-width or prominent on mobile | CRITICAL | |
| 8.3 | Text readable without pinching (≥ 16px body) | CRITICAL | |
| 8.4 | Hero image doesn't push CTA below fold on mobile | CRITICAL | |
| 8.5 | Navigation collapses correctly (hamburger or bottom tab) | CRITICAL | |
| 8.6 | Form inputs ≥ 44px height (thumb-friendly) | CRITICAL | |
| 8.7 | No horizontal scroll on mobile | CRITICAL | |
| 8.8 | Click-to-call phone links where phone numbers appear | NICE | |

---

## 9. Performance (Conversion Killers)

| # | Check | Priority | Status |
|---|---|---|---|
| 9.1 | LCP ≤ 2.5s on mobile (4G) | CRITICAL | |
| 9.2 | Page renders visible content in < 1s (FCP) | IMPORTANT | |
| 9.3 | No layout shift during page load (CLS ≤ 0.1) | CRITICAL | |
| 9.4 | No render-blocking scripts in `<head>` | IMPORTANT | |
| 9.5 | Hero image WebP/AVIF, compressed | IMPORTANT | |
| 9.6 | Analytics / tracking scripts load async | IMPORTANT | |

---

## 10. Copy Quality

| # | Check | Priority | Status |
|---|---|---|---|
| 10.1 | No banned words: Seamless, Elevate, Unleash, Next-Gen, Empower, Revolutionize | CRITICAL | |
| 10.2 | No em dashes (— or --) | IMPORTANT | |
| 10.3 | No "Scroll to explore" or bouncing arrows | IMPORTANT | |
| 10.4 | No meta-labels: "SECTION 01", "OUR STORY", "FEATURES" as eyebrows | IMPORTANT | |
| 10.5 | Headline is specific: names the outcome, audience, or differentiator | CRITICAL | |
| 10.6 | Copy uses "you" more than "we" (reader-centric) | IMPORTANT | |
| 10.7 | Numbers are specific: "2,847 teams" not "thousands of teams" | IMPORTANT | |
| 10.8 | Sentences under 25 words average (scannable) | NICE | |

---

## 11. SEO Basics

| # | Check | Priority | Status |
|---|---|---|---|
| 11.1 | One `<h1>` on page | CRITICAL | |
| 11.2 | Title tag ≤ 60 characters, includes primary keyword | CRITICAL | |
| 11.3 | Meta description 120–160 characters with CTA | IMPORTANT | |
| 11.4 | OG tags: og:title, og:description, og:image (1200×630px) | IMPORTANT | |
| 11.5 | Canonical URL set | IMPORTANT | |
| 11.6 | Schema markup: Organization, Product, or FAQPage where applicable | IMPORTANT | |

---

## Pre-Launch Checklist

```
[ ] All CRITICAL items pass
[ ] Google Analytics / tracking verified in staging
[ ] Conversion event (form submit / sign-up) firing correctly
[ ] Thank-you page / post-conversion flow designed and tested
[ ] Mobile tested on real device (not just browser resize)
[ ] Page speed tested: PageSpeed Insights score ≥ 90 mobile
[ ] Spell check complete
[ ] All links work (no 404s)
[ ] Form submit tested end-to-end (email received)
[ ] A/B test variant set up (if applicable)
```

---

## Review Summary

**Date:** [YYYY-MM-DD]

**Reviewer:** [Name]

**Page URL:** [URL or staging link]

**Primary metric:** [conversion rate / sign-ups / leads]

**Current baseline:** [value or "pre-launch — no baseline"]

**Critical fails:** [N]

**Verdict:**
```
[ ] APPROVED — ready to launch
[ ] CONDITIONAL — fix before launch: [list]
[ ] REJECTED — critical failures: [list]
```

---

*Checklist version: global-design-skill v1.0 — `checklists/landing-conversion-review.md`*
*Related: `rules/14-landing-pages.md`, `blueprints/landing-page-from-scratch.md`, `agents/conversion-designer.md`*
