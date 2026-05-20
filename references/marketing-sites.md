# Reference — Marketing & Landing Page Examples

> Annotated examples of the best marketing site sections in production. Study these before building any landing page, hero section, or campaign page.

---

## Hero Sections

The hero is the single highest-ROI section of any landing page. The best heroes answer "what is this, for whom, and why should I care" in under 3 seconds.

| Site | Hero pattern | Annotation |
|---|---|---|
| **Arc Browser** (arc.net) | Full-screen, personality-led, minimal CTA | The headline is a question ("A browser that thinks like you"). No feature list. No screenshot. Trust that the personality itself converts. Study for: emotional copywriting driving a technically undifferentiated product. |
| **Vercel** (vercel.com) | Left-aligned text + dark code block right | "Ship globally, instantly." — 3 words. Code block demonstrates value without explanation. Study for: developer product hero where the code IS the proof. |
| **Framer** (framer.com) | Animated product demo as hero | Hero section IS a working demo of the product's output — a Framer-built Framer page. Meta, self-referential, and undeniable as proof. Study for: when your product's best ad is your product. |
| **Loom** (loom.com) | Product screenshot + social proof inline | Screenshot of the recording interface + "Join 25 million users" immediately below the headline. Specificity in social proof ("25 million" not "millions of"). Study for: consumer-friendly SaaS that needs both product clarity and social validation. |
| **Railway** (railway.app) | Terminal animation as hero | Minimal dark, animated terminal showing deploy command. Value prop communicated through motion, not text. Study for: zero-to-deploy storytelling without a single marketing word. |
| **Craft** (craft.do) | Warm editorial, product screenshot with perspective | Serif display font, paper-warm background, tilted iPad screenshot. No gradient, no glow. Study for: premium positioning without saying "premium". |
| **Resend** (resend.com) | Code snippet as primary hero element | The value prop IS the API code. A single `resend.emails.send({})` call. Study for: developer tools where the DX quality is the value proposition. |
| **Webflow** (webflow.com) | Split hero with CMS diagram | Left: headline + CTA. Right: animated visual of a page being built. Study for: visual product demonstration that doesn't require a video. |

**Hero anti-patterns to avoid (all from real sites):**
- Centered headline + subtitle + two equal buttons (the banned default)
- Background video with no pause control
- Headline > 3 lines on mobile
- "Get Started" or "Learn More" as the only CTA copy
- Logo grid as the first element below the hero

---

## Social Proof Sections

The best social proof is specific, contextual, and placed immediately after the claim it's proving.

| Site | Social proof approach | Annotation |
|---|---|---|
| **Stripe** (stripe.com) | Logo grid → metric → testimonial | Three-layer approach: credibility logos (Fortune 500) → revenue processed metric ("hundreds of billions") → specific quote. Each layer proves the previous. |
| **Linear** (linear.app) | Testimonials from known builders | Quotes from founders and CTOs of recognizable startups. Named + photo + company. "We use Linear" from a company your prospect knows converts better than a generic review. |
| **Intercom** (intercom.com) | Case study highlights | Not quotes but outcomes: "[Company] reduced support volume 40%". Metric + company name + context. The quote is secondary to the result. |
| **Loom** | Community-type social proof | User-generated content embedded: real recordings from real teams. The proof is in use, not in a quote about use. |
| **Webflow** | Agency showcase | Partner ecosystem as proof. 1000+ agencies built on Webflow proves ecosystem health — not just that individual users like it. |
| **Framer** | Community templates gallery | Gallery of sites built by the community. Visual proof that scales — 100 screenshots beat one testimonial. |

**Social proof by product maturity:**
- Early stage (< 1000 customers): Named founders + specific use cases from 3–5 companies
- Growth stage (1K–100K): Metric outcomes + category-name customers + aggregate stats
- Mature (100K+): Market dominance stats + analyst recognition + ecosystem size

---

## Feature Sections

Feature sections fail when they list features instead of demonstrating value.

| Site | Feature section approach | Annotation |
|---|---|---|
| **Arc Browser** | Each feature as a story | No feature grid. Each feature gets its own illustrated story scroll section. "Spaces for every context in your life." The feature name is last, not first. |
| **Linear** | Issue tracking demo | Animated issue creation flow embedded as the feature explanation. Not a screenshot — an in-page demo. |
| **Notion** | Use case switching | Tabbed interface where clicking a use case (Personal / Team / Enterprise) changes the entire content panel. Features are secondary to use cases. |
| **Webflow** | CMS in motion | Animated GIF (looping video) showing a content editor updating a page. The feature demo is the content. |
| **Stripe** | Two-column code + explanation | Left: human explanation. Right: working code snippet that corresponds. "Payments in 3 lines" backed by the 3-line example. |
| **Vercel** | Deployment timeline animation | Visual timeline showing: push to GitHub → CI → global CDN. Animated, specific, and technical. Speaks directly to the developer audience. |
| **Supabase** | Split SQL/JavaScript demo | "Write a query, get an API" literally shown side-by-side. The feature is the code, not a description of the code. |

**Feature section hierarchy:**
1. User outcome (what they accomplish)
2. How the product enables it (mechanism)
3. Feature name (label)

Most sites invert this: they lead with the feature name and hope users infer the outcome.

---

## Pricing Sections

Great pricing pages make the "right" choice obvious while respecting the user's intelligence.

| Site | Pricing approach | Annotation |
|---|---|---|
| **Linear** (linear.app/pricing) | Free / Pro / Enterprise — no tricks | Price is clear. Features aren't hidden in a tooltip. Free tier is generous and honest about limits. No urgency manipulation. |
| **Vercel** (vercel.com/pricing) | Usage-based with simulation | The pricing calculator is the pricing page. "See what your bill would be" instead of per-seat confusion. Study for: metered billing UX. |
| **Stripe** (stripe.com/pricing) | Transaction percentage only | The most complex pricing in fintech explained in one number: 2.9% + 30¢. Complexity is deferred until needed. Study for: pricing transparency. |
| **Intercom** (intercom.com/pricing) | Value metric based | Priced per "resolved conversation" not per seat. The pricing metric aligns with what users value. Study for: value-metric pricing UX. |
| **GitHub** (github.com/pricing) | Free for public / paid for private | GitHub's free tier IS their product for open-source. The paywall is for enterprises. This drives massive adoption. Study for: freemium moat strategy. |
| **Notion** (notion.so/pricing) | Per seat, free for personal | Free forever for individuals. Per-seat billing only for teams. Study for: bottom-up SaaS pricing that converts individuals to teams. |

**Pricing page anatomy (what every row should have):**
- Plan name (1–2 words, role-based not tier-based: "Starter" not "Basic")
- Price (monthly and annual, annual default)
- What's included (3–5 bullets max — link to comparison table for the rest)
- Primary CTA (action-oriented: "Start free" not "Choose plan")
- Who this is for (1-line ICP description: "For solo developers")

---

## CTA Sections (End of Page)

The final CTA section is where all previous conversion work either pays off or wastes.

| Site | CTA approach | Annotation |
|---|---|---|
| **Vercel** | "Deploy now" with GitHub sign-in | One button, OAuth login, 30-second time-to-value. The CTA has the lowest possible friction. Study for: product-led growth CTAs. |
| **Arc** | "Download for Mac" — nothing else | One action. No email capture. No "learn more". The product IS the CTA. Study for: when the signup IS the product. |
| **Linear** | "Get started — free for your team" | Specificity in the CTA: "your team", not "you". Signals collaborative value. Free explicitly stated. |
| **Stripe** | "Start now" + "Contact sales" split | Two clearly delineated paths: self-serve vs. enterprise. Neither is "primary" — they serve different buyers. |
| **Webflow** | "Start building for free — no credit card" | Removes the primary objection (payment) in the CTA itself. "No credit card" is a conversion mechanic, not a legal requirement. |
| **Loom** | "Record a video" | Not "Sign up". Not "Get started". The CTA is the first action that delivers value. Study for: when you can name the first meaningful action. |

**CTA formula:** `Verb + Object + Context`
- "Record a video" = Verb (Record) + Object (video) — minimal, action-forward
- "Deploy your first app free" = Verb (Deploy) + Object (app) + Context (first / free)
- "Start building for free" = Verb (Start) + Object (building) + Context (free)

---

## Navigation — Marketing Site

| Site | Navigation pattern | Annotation |
|---|---|---|
| **Webflow** | Mega-menu with categories | Product → Use Cases → Enterprise → Blog → Pricing. Each category has a mega-menu with 3–4 sub-items + featured link. Study for: complex SaaS with multiple ICPs. |
| **Stripe** | Simple top nav + mobile-first | Products / Solutions / Developers / Resources / Pricing. No mega-menu needed — the top-level navigation IS the IA. Study for: content-rich developer products. |
| **Linear** | Minimal 5-item nav | Features / Pricing / Blog / Changelog / Sign in. No dropdown, no mega-menu. Study for: product-led growth where the product page IS the homepage. |
| **Arc Browser** | Progressive disclosure nav | Top nav with 3 items. Scroll down → sticky nav transforms to show more context. Study for: narrative landing pages where the nav changes as the story develops. |
| **Framer** | Transparent → solid scroll | Nav starts transparent over the hero (matches hero background), becomes solid white on scroll. Study for: cinematic marketing landing pages. |
| **Vercel** | Code-context adaptive | Navigation changes based on whether you're on marketing (simple) or dashboard (complex sidebar). Two different nav systems, one product. |

---

## Animation and Motion on Marketing Pages

| Site | Animation technique | Annotation |
|---|---|---|
| **Framer** | Scroll-linked component reveals | Each feature appears with a spring reveal as its section enters the viewport. Consistent system — every reveal uses the same timing. |
| **Vercel** | Deployment animation | A simplified deployment pipeline animates on the hero — dots travel from "Push" to "Edge" to "Visitors". Communicates product value without a word. |
| **Arc Browser** | Feature storytelling via animation | Each feature section has a dedicated animation that plays when the section enters viewport. Not decorative — each animation IS the feature demonstration. |
| **Webflow** | Marquee strips | Scrolling logo strips and testimonial carousels. Not scroll-linked — constant motion that communicates abundance of social proof. |
| **Raycast** | Blur reveal entrance | Page loads with elements slightly blurred, then sharpens. Feels like focus adjustment — communicates clarity as a brand value. |
| **Linear** | Subtle hover micro-interactions | Every interactive element has a 120ms transition. Nothing dramatic. The accumulation of small perfect interactions creates the "polished" feeling. |

**Marketing animation budget:**
- Hero: 1 signature animation (scroll-linked or entrance)
- Feature sections: 1 reveal animation per section (scroll-triggered)
- Social proof: 0 or 1 continuous motion (logo marquee)
- CTA: 0 animations — focus should be undistracted

---

*Reference version: global-design-skill v1.0 — `references/marketing-sites.md`*  
*Updated: 2026-05-20*  
*Related: `agents/reference-hunter.md`, `references/inspiration-sites.md`, `blueprints/landing-page-from-scratch.md`*
