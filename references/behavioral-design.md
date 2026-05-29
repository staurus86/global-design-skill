# Behavioral Design Reference

> Cognitive biases mapped to UI/UX design decisions. For each bias: what it is, where to apply it in UI, and a concrete pattern.
>
> Source: [keepsimple.io/uxcore](https://keepsimple.io/uxcore) — 105 biases; this file covers the 29 most directly applicable to interface design.
>
> Use this file when designing: pricing pages, CTAs, navigation, trust signals, onboarding, error states, or any conversion-critical UI.

---

## 1. Pricing Pages

### Anchoring Effect
People rely too heavily on the first number they see. Subsequent numbers are judged relative to it.

**Apply:** Show original/MSRP price before discounted price. The crossed-out number sets the anchor.

```html
<!-- WITH bias: crossed-out price anchors perception -->
<div class="plan-price">
  <span class="price-was">was $99/mo</span>
  <span class="price-now">$25/mo</span>
  <span class="badge">Best Value</span>
</div>
```

**Why it works:** The first number seen dominates value judgment. $25 feels like a bargain against $99.

---

### Decoy Effect (Asymmetric Dominance)
Adding a third, clearly inferior option makes the target option look dramatically better.

**Apply:** In 3-tier pricing, the middle "decoy" option should be priced close to the premium but clearly worse in value — making premium feel obvious.

```html
<!-- Decoy: Plus at $22 has fewer features than Premium at $24 -->
<div class="pricing-tiers">
  <div class="tier">Basic — $8/mo — 3 projects</div>
  <div class="tier decoy">Plus — $22/mo — 10 projects, email only</div>  <!-- decoy -->
  <div class="tier featured">Premium — $24/mo — unlimited + priority support</div>
</div>
```

**Why it works:** Asymmetric dominance — Premium is strictly better than Plus for $2 more, making the choice obvious.

---

### Contrast Effect
People's perception of value is shaped by what surrounds it. The same product looks better or worse depending on its neighbors.

**Apply:** Flank your target product/tier between a clearly worse and clearly better option. The middle option benefits from both contrasts.

**Why it works:** Surrounding context reshapes value perception without changing the product itself.

---

### Mental Accounting
People treat money differently depending on how it's categorized or presented.

**Apply:** Break down subscription costs into per-day or per-feature amounts. "Less than a coffee/day" makes $30/month feel trivial.

```html
<!-- WITH bias: broken down to feel smaller -->
<p class="price-breakdown">
  $0.99/day · <strong>$29/month</strong> · billed annually
</p>
<p class="price-sub">That's less than a daily coffee</p>
```

**Why it works:** Each sub-charge is evaluated against its own mental budget category, not the total.

---

### Hyperbolic Discounting
People strongly prefer immediate rewards over larger delayed ones, even when the delayed reward is objectively better.

**Apply:** Lead with "free now" over "save X% annually." A 30-day free trial beats "get 2 months free with annual plan."

```html
<!-- WITH bias: immediate reward first -->
<div class="cta-block">
  <button class="btn-primary">Start free — 30 days, no card needed</button>
  <p class="sub">Then $29/month — cancel any time</p>
</div>

<!-- NOT: -->
<!-- <button>Save 20% with annual billing</button> -->
```

**Why it works:** "Free now" beats "save later" — immediacy is worth more than size.

---

### Less-Is-Better Effect
A smaller, specific offer can feel more valuable than a larger, diffuse one.

**Apply:** Offer one precise upgrade benefit, not a list of ten. "Get 50 GB extra storage" > "Get our full premium package."

**Why it works:** Quality-to-quantity ratio dominates. Specificity beats volume.

---

## 2. CTAs & Copy

### Framing Effect
The same information presented differently produces opposite emotional responses.

**Apply:** Frame CTAs and feature descriptions in positive terms. "Join 14,000 teams" > "Don't fall behind." Same for system messages: "Your data is saved" > "Error: unsaved changes."

```html
<!-- Positive frame — system update -->
<!-- WITHOUT: "Your layout will be changed" -->
<!-- WITH: "We've improved your workspace — same data, better performance" -->

<!-- Positive frame — error state -->
<!-- WITHOUT: "Error: connection lost" -->
<!-- WITH: "We lost your connection — your work is saved, reconnecting..." -->
```

**Why it works:** Identical information produces opposite emotional responses based on framing.

---

### Loss Aversion
The pain of losing something is approximately 2× more intense than the pleasure of gaining the same thing.

**Apply:** In trial expiry, cancellation, and upgrade flows — show what the user will *lose*, not what they'll *gain*.

```html
<!-- WITH bias: loss framing on trial expiry -->
<div class="trial-expiry">
  <p class="warning">⏰ Trial ends in 3 days. When it ends, you'll lose:</p>
  <ul class="loss-list">
    <li>✗ 12.4 GB of uploaded files</li>
    <li>✗ 6 saved custom dashboards</li>
    <li>✗ 84 saved automation workflows</li>
    <li>✗ All team member access (4 users)</li>
  </ul>
  <button class="btn-primary">Keep everything — $29/month</button>
  <a class="btn-ghost">Discard everything and downgrade</a>
</div>
```

**Why it works:** Pain of losing is 2× the pleasure of gaining. Loss framing creates stronger urgency than gain framing.

---

### Self-Reference Effect
People remember information better when it relates to them personally.

**Apply:** Use "you/your" language throughout. Tailor landing page headlines to a specific role or situation. Segment by persona where possible.

```html
<!-- WITHOUT: "Project management for teams" -->
<!-- WITH: "The tool solo founders use to ship without a PM" -->

<!-- Form placeholder — personal connection -->
<input placeholder="Where does your team currently track tasks?" />
<!-- not: "Describe your workflow" -->
```

**Why it works:** "This is about me" recognition encodes information more deeply.

---

### Illusory Truth Effect
The more often something is repeated, the more likely people are to believe it — even without proof.

**Apply:** Repeat your core value proposition in multiple places on the page: headline, feature section, CTA, footer. Consistent repetition builds perceived credibility.

**Why it works:** Repetition creates familiarity the brain interprets as truth. No proof needed — frequency is the signal.

---

### Curse of Knowledge
Designers and writers forget what it's like not to know the product. This creates jargon-heavy, confusing copy.

**Apply:** Replace technical terms with outcome-oriented plain language. Test your copy on someone unfamiliar with the product. In onboarding: replace configuration options with pre-made choices.

```html
<!-- WITHOUT (curse of knowledge): -->
<!-- "Configure your webhook integration endpoint for event-driven data sync" -->

<!-- WITH: -->
<!-- "Connect your tools — we'll send updates automatically when things change" -->
```

**Why it works:** Replacing jargon with guided choices prevents the team's expertise from becoming a barrier to new users.

---

### Negativity Bias
People focus more on negative experiences than positive ones, even when both are equally present.

**Apply:** Design error states, outage notifications, and downgrade confirmations with extra care. One badly-handled incident undoes months of goodwill. Be proactive: communicate problems before users discover them.

```html
<!-- WITH bias: proactive incident notification -->
<!-- WITHOUT: "Service disruption occurred." -->
<!-- WITH: -->
<div class="incident-notice" role="alert">
  <strong>We noticed an issue before you did.</strong>
  Your exports were delayed by ~12 minutes between 14:20–14:32 UTC.
  All jobs have completed. <a href="/status">Full incident report →</a>
</div>
```

**Why it works:** Proactive communication converts "this is broken" to "they're on top of it."

---

## 3. Navigation & Information Architecture

### The Magical Number 7±2 (Miller's Law)
Short-term human memory can hold 7±2 items at once. More than that, and recall drops significantly.

**Apply:** Cap top-level navigation at 7 items. For settings panels with many sections, group into chunks of 5–7. This is the cognitive basis for Hick's Law (`rules/01-visual-hierarchy.md`).

```html
<!-- Max 7 nav items — split overflow into groups -->
<nav>
  <a>Dashboard</a>
  <a>Projects</a>
  <a>Team</a>
  <a>Reports</a>
  <a>Integrations</a>
  <!-- Settings group: 3 sub-items, not 3 separate nav items -->
  <details><summary>Settings</summary>
    <a>Profile</a><a>Billing</a><a>Security</a>
  </details>
</nav>
```

**Why it works:** Working memory cap is real — exceeding it causes cognitive overload and navigation abandonment.

---

### Serial-Position Effect
People remember items at the beginning (primacy) and end (recency) of a list better than those in the middle.

**Apply:** Put the most important navigation item first or last. Bury neutral or less-important items in the middle. In changelogs and release notes: lead with the best news, end with a forward-looking statement, put deprecations in the middle.

**Why it works:** First and last positions are recalled best. Middle positions are forgotten.

---

### Ambiguity Effect
People strongly avoid options with unknown or unclear outcomes, preferring familiar, certain choices.

**Apply:** In pricing tables and feature lists, replace vague language with specific numbers. "Unlimited" is better than "plenty." "50 GB" is better than "large storage." "Responds in 4 hours" is better than "fast support."

```html
<!-- WITHOUT: "Advanced analytics" -->
<!-- WITH: "Analytics: 12-month history, hourly breakdown, CSV export" -->

<!-- WITHOUT: "Priority support" -->
<!-- WITH: "Dedicated Slack channel + 4-hour response SLA" -->
```

**Why it works:** Quantified benefits eliminate ambiguity — people choose what they can evaluate.

---

### Unit Bias
People want to complete the unit they're given. Short lists feel achievable; long lists feel insurmountable.

**Apply:** Paginate long task lists and content feeds into completable chunks. Show "6 tasks" not "36 tasks". Progress bars should show small, reachable milestones, not a single large goal.

**Why it works:** Completable units sustain engagement. 6 feels achievable, 36 feels overwhelming.

---

## 4. Trust & Social Proof

### Halo Effect
A positive impression in one area (design quality, brand aesthetics) transfers to unrelated areas (reliability, product quality).

**Apply:** Invest in visual design quality beyond what seems "necessary." A polished, intentional visual design makes users assume the underlying product is equally well-crafted.

**Why it works:** Beautiful design halos over to perceived reliability and performance. First visual impression shapes all subsequent evaluation.

---

### Bandwagon Effect
People follow the crowd — adopting beliefs or choices because they're popular.

**Apply:** Show specific social proof numbers on product cards and landing pages. "14,200 teams use this" > "Join our community." Specificity matters — round numbers feel fabricated.

```html
<div class="social-proof">
  <span>★★★★★ 4.8</span>
  <span>14,247 teams active this month</span>
  <span>Trusted by teams at Stripe, Linear, Vercel</span>
</div>
```

**Why it works:** If thousands chose it, it must be good — social proof reduces perceived risk.

---

### Authority Bias
People defer to authority figures and assume they're correct.

**Apply:** Attach credentials, titles, and institutional affiliations to recommendations, testimonials, and expert quotes. An unnamed quote is worth far less than one from "Dr. Sarah Mills, Head of Security at [Company]."

```html
<!-- WITHOUT: "This tool changed how we work." -->
<!-- WITH: -->
<blockquote>
  "This tool changed how we work."
  <footer>— Dr. Sarah Mills, CISO · Stripe · 18 years in security</footer>
</blockquote>
```

**Why it works:** Expert identity and credentials dramatically increase compliance and trust.

---

### Illusory Truth Effect (trust application)
Repeated exposure to a claim increases belief in it, regardless of evidence.

**Apply:** Repeat your security, privacy, and trust claims across the page — not just in the footer. "Your data never leaves your servers" should appear near the form, near the CTA, and in the FAQ.

---

### Confirmation Bias
People seek out information that confirms their existing beliefs.

**Apply:** Skeptical users will actively look for evidence that your product is unsafe or untrustworthy. Surface security signals, compliance badges, and transparency proactively — don't wait for users to ask.

```html
<!-- Security dashboard — continuous proof for skeptical users -->
<div class="security-panel">
  <div class="badge">SOC 2 Type II certified</div>
  <div class="badge">GDPR compliant</div>
  <div class="activity">Last login: 2 hours ago · San Francisco, CA</div>
  <div class="activity">0 failed login attempts in last 30 days</div>
</div>
```

**Why it works:** Intercepting skeptical users' search with confirming evidence converts "this is sketchy" into "this is legitimate."

---

### Mere-Exposure Effect
People develop preference for things they're familiar with, simply through repeated exposure.

**Apply:** Maintain consistent visual identity across all touchpoints (app, emails, social, ads). Users who see your brand repeatedly become more likely to convert — not because the product changed, but because familiarity feels like trust.

**Why it works:** Familiar cues trigger subconscious preference without the user recognizing why the page feels trustworthy.

---

## 5. Onboarding & Retention

### Peak-End Rule
People judge an experience almost entirely by how it felt at its most intense point (peak) and at its conclusion — not by the average.

**Apply:** Design checkout confirmation, onboarding completion, and upgrade success states as emotional high points. Add a personal note, an unexpected benefit, or a forward-looking element.

```html
<!-- WITH bias: confirmation page as peak moment -->
<div class="order-confirmed">
  <p class="celebration">🎉 You're all set, Alex!</p>
  <p class="delivery">Estimated delivery: Wednesday, March 26</p>
  <p class="personal">Hand-packed by our team in Portland. Hope you love it.</p>
  <div class="next-order">
    <code>THANKYOU10</code> — 10% off your next order
  </div>
</div>
```

**Why it works:** Memory weights the peak and ending disproportionately. A delightful final step improves recall of the entire experience.

---

### IKEA Effect
People place higher value on things they helped create, even if the result is objectively similar to a pre-made alternative.

**Apply:** Build investment steps into onboarding — let users name their workspace, choose a theme, or configure one setting before they see the full product. The act of creation creates ownership.

```html
<!-- Onboarding step 2 of 5: create first project -->
<div class="onboarding-step">
  <h2>Name your first project</h2>
  <input placeholder="e.g. Website Redesign, Q4 Campaign..." />
  <p class="hint">You can always rename it later</p>
  <button>Create project →</button>
</div>
```

**Why it works:** Users who invest effort in creating something value the result disproportionately — a generic template becomes "my workspace."

---

### Endowment Effect
People overvalue what they already own or possess.

**Apply:** Use "your" language for existing features and data. When introducing UI changes, frame them as enhancements to what users already have, not replacements.

```html
<!-- WITHOUT: "We've updated the dashboard layout" -->
<!-- WITH: "Your dashboard has a new layout — same data, easier to scan" -->

<!-- WITHOUT: "Upgrade to unlock reports" -->
<!-- WITH: "Your data is ready — upgrade to view your reports" -->
```

**Why it works:** Respecting ownership and using possessive language leads to higher adoption of changes.

---

### Escalation of Commitment (Sunk Cost)
People continue investing in something because they've already invested, even when quitting is objectively better.

**Apply:** On cancel or churn flows, show accumulated investment — progress, content created, data uploaded, days of use.

```html
<!-- Cancel flow — showing sunk cost -->
<div class="cancel-confirm">
  <p>Before you go — here's what you've built:</p>
  <ul>
    <li>📁 47 projects created</li>
    <li>📊 3 months of analytics data</li>
    <li>👥 6 team members connected</li>
    <li>⏱ 142 hours logged</li>
  </ul>
  <p>All of this will be permanently deleted.</p>
  <button class="btn-ghost btn-danger">Yes, delete everything</button>
  <button class="btn-primary">Keep my account</button>
</div>
```

**Why it works:** Showing accumulated investment makes abandonment feel wasteful — users continue to avoid "wasting" what they've already put in.

---

### Reactance
When people's freedom is restricted or threatened, they push back — even against choices that benefit them.

**Apply:** Avoid aggressive upsell language that feels coercive. Give users an out ("Maybe later" / "Remind me in 7 days") alongside the upgrade CTA. Acknowledge that upgrading is their choice.

```html
<!-- WITHOUT: "You MUST upgrade to continue" -->
<!-- WITH: -->
<div class="upgrade-prompt">
  <p>You've hit the free plan limit (3 projects).</p>
  <p>Upgrade to Pro to create unlimited projects.</p>
  <button class="btn-primary">Upgrade — $29/month</button>
  <button class="btn-ghost">Remind me in 7 days</button>
  <p class="choice-note">You're in control — cancel any time.</p>
</div>
```

**Why it works:** Restricted freedom triggers pushback. Acknowledging choice and offering autonomy increases conversion.

---

## 6. Visual Hierarchy & Attention

### Von Restorff Effect (Isolation Effect)
When multiple similar objects are present, the one that differs from the rest is most likely to be remembered.

**Apply:** Use visual differentiation to draw attention to the most important element: a colored CTA button in a grey nav, a "Most popular" badge on the mid-tier, a "New" pill on a feature.

```html
<!-- Nav: one visually distinct item draws attention -->
<nav>
  <a>Home</a><a>Features</a><a>Docs</a>
  <a class="nav-highlight">Pricing <span class="badge">New</span></a>
  <a>Blog</a><a>Sign In</a>
</nav>
```

**Why it works:** Visually distinct items capture attention and are remembered far better than conforming items.

---

### Picture Superiority Effect
People remember images approximately 6× better than text alone.

**Apply:** Replace bullet-point feature lists with icons + short labels, or product screenshots. For complex features: use a short animation or illustration over a text paragraph.

```html
<!-- WITHOUT: text feature list -->
<ul>
  <li>Advanced analytics dashboard</li>
  <li>Team collaboration tools</li>
  <li>API access</li>
</ul>

<!-- WITH: visual feature grid -->
<div class="feature-grid">
  <div class="feature">
    <img src="analytics-icon.svg" alt="" aria-hidden="true">
    <span>Analytics</span>
  </div>
  <!-- ... -->
</div>
```

**Why it works:** Images are encoded through dual channels (visual + verbal), achieving 6× better retention than text alone.

---

### Processing Difficulty Effect
Information that requires effort to process is remembered more deeply.

**Apply:** For destructive or irreversible actions (delete, cancel, overwrite), deliberately increase friction. Require users to type a confirmation phrase — the effort forces deep engagement with the consequences.

```html
<!-- Destructive action: type to confirm -->
<dialog class="delete-confirm">
  <h2>Delete workspace "Acme Corp"?</h2>
  <p>This will permanently delete 47 projects, 142 hours of data, and all team members.</p>
  <p>Type <strong>delete acme corp</strong> to confirm:</p>
  <input type="text" placeholder="delete acme corp" id="confirm-input">
  <button id="confirm-btn" disabled>Delete permanently</button>
</dialog>
```

**Why it works:** Cognitive effort creates a stronger memory trace. Typing the name forces deep engagement with consequences — reducing accidental deletions.

---

## Quick Reference Table

| Design task | Bias to apply |
|---|---|
| Pricing table | Anchoring, Decoy, Contrast, Mental accounting |
| Free trial CTA | Hyperbolic discounting, Loss aversion |
| Annual upgrade prompt | Hyperbolic discounting, Mental accounting |
| Trial expiry notice | Loss aversion |
| Navigation structure | Magical Number 7±2, Serial-position, Von Restorff |
| Feature list | Picture superiority, Ambiguity effect |
| Social proof section | Bandwagon, Authority bias, Illusory truth |
| Trust signals | Halo effect, Confirmation bias, Mere-exposure |
| Landing headline | Self-reference, Framing, Illusory truth |
| Onboarding steps | IKEA effect, Unit bias, Curse of knowledge |
| Checkout/success page | Peak-end rule |
| Cancel/churn flow | Escalation of commitment, Endowment effect, Loss aversion |
| Upgrade upsell | Reactance, Loss aversion, Hyperbolic discounting |
| Error states | Negativity bias, Framing |
| Destructive actions | Processing difficulty effect |
| Settings navigation | Magical Number 7±2, Unit bias |

---

## What this file does NOT cover

Biases in the UX Core library that are **not applicable to direct UI design decisions:**
- Statistical reasoning errors (Gambler's fallacy, Clustering illusion, Base rate fallacy)
- Social/group dynamics (Fundamental attribution error, Stereotype, In-group favoritism)
- HR and management biases (Planning fallacy, Dunning-Kruger, Hindsight bias)
- Offensive security applications (noted in UX Core's OffSec category)

For the complete library of 105 biases: [keepsimple.io/uxcore](https://keepsimple.io/uxcore)
