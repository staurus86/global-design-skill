# Reference — Pricing Page Examples

> Annotated breakdown of the best pricing pages in production. Study before building any pricing section. Focus on psychology, hierarchy, and copy — not just visual design.

---

## The Best Pricing Pages Analyzed

### Linear — linear.app/pricing

**Tier structure:** Free / Pro ($8/seat/mo) / Enterprise (custom)  
**Annual toggle:** Yes — default to monthly, annual shown as savings  
**What makes it exceptional:**

- **Radical honesty.** No features hidden in tooltips or asterisks. What you see is what you get.
- **Free tier signals:** "Unlimited members" on the free tier. Linear trusts that real value drives upgrades — they're not restricting seat count to force paid conversion.
- **Pro justification:** The upgrade reasons are specific: "Unlimited history", "Priority support", "SSO". Not "advanced features" — named capabilities.
- **Enterprise is contact-sales, not a feature tier.** Linear doesn't try to self-serve enterprises — they have a dedicated page and a clear hand-off. No fake "Enterprise" checkmarks.

**What to steal:**
- The comparison section under the pricing cards is a table, not a checklist. Tables allow scanning across tiers, checklists require reading each row.
- The FAQ below the pricing cards addresses the 3 most common objections: "What happens when I hit the limit?", "Can I change plans?", "What payment methods?"

---

### Vercel — vercel.com/pricing

**Tier structure:** Hobby (free) / Pro ($20/mo) / Enterprise (custom)  
**Annual discount:** Yes — shown upfront  
**What makes it exceptional:**

- **Usage-based clarity.** Instead of "up to X builds/month" in small print, Vercel shows a bill estimator. "Estimate your bill" interactive calculator. Removes billing anxiety before signup.
- **"What's included" is written in user terms.** Not "100GB bandwidth" but "~10,000 visitors per month". Translates technical limits into outcomes.
- **Hobby tier limitations are generous.** The free tier includes global CDN, serverless functions, analytics preview. This generosity is the growth engine — Hobby users become advocates.
- **The Pro card has a subtle "Most popular" tag.** Not a badge — just a slightly different card background. Low-pressure anchoring.

**What to steal:**
- The "Enterprise" column doesn't show fake prices like "$X,XXX/month". It shows "Custom" with a clear list of what Enterprise actually includes (SOC2, SAML SSO, 99.99% SLA). No price theater.

---

### Stripe — stripe.com/pricing

**Model:** Transaction percentage (2.9% + 30¢) + optional add-ons  
**What makes it exceptional:**

- **One number up front.** The complexity of Stripe's actual pricing (country fees, card types, currencies, disputes, payouts) is enormous. But the headline number — 2.9% + 30¢ — is the only thing a new user needs.
- **Progressive disclosure.** "See all features" expands. "Volume pricing" is a separate page. "Enterprise" is a different contact-us flow. Complexity is deferred until the user needs it.
- **The trust signals ARE the pricing page.** "PCI DSS Level 1 certified", "99.99% uptime SLA", "Fraud detection" — these aren't in a testimonial section, they're next to the price. Security sells.
- **Pricing calculator for complex models.** ACH, international cards, Connect platform fees — each has its own calculator. The calculator is the pricing page for advanced users.

**What to steal:**
- The "Integrated per-transaction fees" table below the main price. It shows all the "what ifs" (refunds, disputes, manual captures) in one clear reference table. Users don't need to email sales to know about fees.

---

### Notion — notion.so/pricing

**Tier structure:** Free / Plus ($10/seat/mo) / Business ($18/seat/mo) / Enterprise  
**Annual discount:** Yes — ~20% shown as default  
**What makes it exceptional:**

- **"Free forever" is the headline.** Not "free trial" — free forever for personal use. This communicates permanence that converts individual users to champions within organizations.
- **The upgrade path is a team narrative.** "Plus" is "For small teams". "Business" is "For growing teams". The tier names are ICPs, not capability tiers.
- **Seat-based pricing that feels fair.** The per-seat model is explained with a calculator: "5 people = $50/month". Not an estimation — an exact number.
- **Guest seats are free.** This is how Notion grows virally — every paid user can invite unlimited guests. Guests experience Notion, some convert.

**What to steal:**
- The FAQ section addresses billing confusion: "What counts as a member vs. a guest?" — this is the most-asked pricing question for seat-based SaaS and Notion addresses it in the FAQ.

---

### GitHub — github.com/pricing

**Tier structure:** Free / Team ($4/seat/mo) / Enterprise ($21/seat/mo)  
**What makes it exceptional:**

- **The free tier IS the product for 70% of users.** Unlimited public repositories, unlimited contributors, Actions minutes for public repos. GitHub doesn't restrict features that would hurt open-source adoption.
- **Public vs. private repo is the paywall.** One clear distinction. For commercial use (private repos + CI/CD), you pay. For OSS (everything public), you don't. The moat IS the free tier.
- **No manipulative anchoring.** Three tiers, none of which feel artificially restricted or inflated. The Enterprise tier is clearly for large organizations with compliance needs — not just for users who want more storage.

**What to steal:**
- "Compare all plans" link that goes to a full feature table. The comparison table is exhaustive (100+ rows) but organized into categories. Users who need to compare at that depth CAN.

---

### Intercom — intercom.com/pricing

**Model:** Value metric (resolved conversations) + seat add-ons  
**What makes it exceptional:**

- **Prices based on outcomes, not seats.** "Per resolved conversation" aligns Intercom's revenue with the customer's success. When the customer handles more volume, Intercom earns more. This is pricing as partnership.
- **The pricing estimate is upfront.** "Estimate what you'll pay" calculator on the pricing page. Enter your expected conversation volume → see your monthly bill. No sales call needed to understand cost.
- **Tiered overage handling.** Instead of "you'll get cut off at your limit", Intercom shows what happens when you exceed: additional cost per conversation. No surprises.

**What to steal:**
- The "What is a resolved conversation?" tooltip next to the pricing metric. Defining your value metric in the pricing page removes the #1 confusion point for value-metric pricing.

---

### Figma — figma.com/pricing

**Tier structure:** Starter (free) / Professional ($15/seat/mo) / Organization ($45/seat/mo) / Enterprise (custom)  
**What makes it exceptional:**

- **Free tier hooks the entire team.** Unlimited editors on free tier — but only 3 projects and no version history. The restriction forces teams to upgrade, but doesn't prevent adoption.
- **The professional tier removes restrictions, doesn't add features.** "Unlimited projects, unlimited version history, team libraries." The upgrade story is "remove limits" not "unlock features."
- **Organization vs. Professional is about admin, not design.** The step from Pro to Org is SSO, advanced permissions, centralized billing — enterprise needs, not designer needs. This separates design tooling decisions from IT/procurement decisions.

**What to steal:**
- The "Used by teams at" logo section directly above the pricing cards. Social proof closest to the decision point.

---

## Pricing Page Patterns

### Annual Toggle

**Best implementation:** Default to annual, show monthly as "per month if billed annually" so users see the best price first. Show savings as absolute value ("Save $48/year") not percentage ("Save 20%") — absolute saves feel more concrete.

**Bad implementation:** Default to monthly, hide the annual discount. Users who don't notice the toggle pay more and feel cheated when they discover it later.

---

### The "Most Popular" Tag

**What works:** Subtle background difference on the recommended tier. One-line caption: "Most popular for growing teams."

**What doesn't work:** Bright badge, star icon, animated highlight. Manipulation is visible — it increases distrust in sophisticated buyers.

**The real signal:** If a tier IS most popular, it will have social proof (customer quotes) right next to it. That's more convincing than a badge.

---

### Enterprise Tier

**What sophisticated buyers expect:**
- Custom pricing (say "Custom" — not a fake number)
- The specific features enterprise needs: SOC2/ISO certifications, SSO/SAML, SLA guarantees, audit logs, dedicated support
- A clear sales path: "Talk to our team" with a direct calendar link, not a generic "Contact us" form

**What repels enterprise buyers:**
- Feature gatekeeping (charging more for accessibility features or export options)
- Opaque pricing with no starting point
- Routing to a generic contact form instead of a dedicated enterprise sales process

---

### FAQ Section

Always include. These 5 questions are universal for SaaS pricing:

1. "What happens when my trial ends?" — removes commitment anxiety
2. "Can I change my plan?" — removes lock-in anxiety
3. "Do you offer refunds?" — removes risk anxiety
4. "What payment methods do you accept?" — removes payment friction
5. "Do you offer discounts for nonprofits / students / annual plans?" — captures price-sensitive segments

---

### Trust Strip Below Pricing Cards

Place immediately below the CTA buttons, before the FAQ:
- Payment security icons (Visa/MC/Stripe trust marks)
- "No credit card required" if true
- "Cancel anytime" if true
- Security certification (SOC2, HIPAA, GDPR) if relevant

---

## Common Pricing Page Failures

| Failure | Why it hurts | Fix |
|---|---|---|
| Hidden fees revealed at checkout | Destroys trust at the highest-friction moment | Show all fees on the pricing page, including taxes if applicable |
| Feature grid as the primary pricing table | Hard to scan, buries the key comparison | Lead with 3 cards + outcome summary; link to full comparison table |
| Monthly default when annual is better value | Users who don't notice pay more, feel cheated | Default to annual with clear monthly toggle |
| No clear CTA per tier | Users don't know what action to take | One clear button per tier, action-oriented copy |
| Enterprise tier looks like a worse deal | "Everything in Pro, plus..." framing makes Enterprise look like an upsell | Frame Enterprise as a different product for a different buyer |
| No social proof near pricing | Users hesitate without reassurance at the decision point | Add 1–2 quotes from customers of each tier adjacent to the relevant card |

---

*Reference version: global-design-skill v1.0 — `references/pricing-pages.md`*  
*Updated: 2026-05-20*  
*Related: `agents/reference-hunter.md`, `references/inspiration-sites.md`, `blueprints/pricing-page-from-scratch.md`, `patterns/marketing-blocks/pricing-sections.md`*
