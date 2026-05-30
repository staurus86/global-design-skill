# Rule 00 — Design Escalation Protocol

> The single most common failure mode in AI-assisted design: applying cosmetic fixes when a structural redesign is required, or the reverse — burning the house down when the user just wanted a new coat of paint. This rule maps user intent signals to response depth before any design work begins.

---

## The Escalation Stack

Every design request maps to one of five levels. Identify the level first. Then act at exactly that level — not above, not below.

```
Level 5 — FULL REDESIGN      Structural change, new visual identity
Level 4 — SUBSTANTIAL REWORK Significant section or component overhaul
Level 3 — TARGETED OVERHAUL  Specific problem solved end-to-end
Level 2 — SELECTIVE CLEANUP  Remove 20-30% of clutter, fix worst issues
Level 1 — MICRO-ADJUSTMENT   Single property, copy, or color tweak
```

---

## Phrasing → Level Mapping

### Level 5 — Full Redesign

Trigger phrases:
- "Redesign this completely"
- "Make it look like [premium brand reference]" (Linear, Stripe, Vercel, Spitfire Audio)
- "This looks like a template, fix it"
- "Start from scratch but keep the content"
- "It looks AI-generated / generic"
- "Make it feel like a [$10k / $50k] site"

**Required response:**
- Audit current design and name 5+ structural problems
- Propose a new visual direction before implementing
- Change layout, visual identity, typography system, color strategy
- Do not preserve existing patterns unless explicitly asked

---

### Level 4 — Substantial Rework

Trigger phrases:
- "The hero section isn't working"
- "Make this more premium / high-end"
- "It feels dated / corporate / cheap"
- "The above-the-fold isn't converting"
- "Overhaul the [section name]"

**Required response:**
- Identify root cause of the problem (hierarchy? density? color? copy?)
- Rework that section completely — layout, spacing, type, visual assets
- Verify the fix solves the stated problem, not just looks different

---

### Level 3 — Targeted Overhaul

Trigger phrases:
- "Fix the navigation"
- "The pricing section looks broken on mobile"
- "The form is hard to use"
- "This component doesn't match the rest"
- "The CTA isn't visible enough"

**Required response:**
- Solve the specific problem end-to-end
- Check adjacent components for consistency
- Do not touch unrelated sections

---

### Level 2 — Selective Cleanup

Trigger phrases:
- "Clean this up"
- "Make it less cluttered"
- "Simplify"
- "Too much going on"
- "Tighten it up"

**Required response:**
- Remove 20–30% of decorative elements
- Increase whitespace
- Do not change layout structure or color palette
- One sentence summary of what was removed and why

---

### Level 1 — Micro-Adjustment

Trigger phrases:
- "Change the button color to..."
- "Make the font slightly larger"
- "Adjust the spacing here"
- "Just tweak the copy"
- "Small change: ..."

**Required response:**
- Change exactly what was asked
- Touch nothing else
- No redesign suggestions unless the user asks

---

## Brand Reference Anchors

When a brand is named explicitly, calibrate to that brand's visual weight:

| Brand | What it signals | Calibration |
|---|---|---|
| Linear / Vercel | Dark, minimal, developer-focused | High information density, monospace accents, subtle motion |
| Stripe | Light, trust-forward, enterprise | Conservative spacing, high contrast, no decoration |
| Spitfire Audio / Native Instruments | Dark, premium, image-led | Images 70%+ of cards, 112px+ section spacing, near-zero decoration |
| Apple | System-level refinement | Large type, full-bleed imagery, motion as product feature |
| Notion / Loom | Friendly SaaS | Soft radius, illustrated accents, conversational copy |

If a brand is named but you are not certain of its aesthetic, state that and ask before proceeding.

---

## Design Dials

Once the escalation level is set, calibrate the *loudness* of the output with three dials. State them explicitly at the start of a design response whenever they differ from the defaults — the user can then push any dial up or down in one word.

| Dial | 1 | 10 | Default | Raise when | Lower when |
|---|---|---|---|---|---|
| **DESIGN_VARIANCE** | safe / conventional | pioneering / unexpected | 5 | portfolio, agency, "wow", brand hero | B2B form-first, admin, trust-critical |
| **MOTION_INTENSITY** | static | full theatrical | 4 | landing, interactive showcase | dashboard, data table, productivity app |
| **VISUAL_DENSITY** | sparse / editorial | data-dense | 4 | marketing, editorial, portfolio | analytics, monitoring, back-office (raise to 7–9) |

**Rule:** Dials are independent. A monitoring dashboard can be high density (8) and low motion (2) and low variance (3) at once. Do not collapse all three to a single "boldness" slider.

---

## Macrostructure-First

The strongest defense against AI-slop is structural, not cosmetic. Before colors, fonts, or components, choose the page's **macrostructure** — the skeleton that organizes the whole narrative. Two briefs with the same palette but different macrostructures don't look like the same template recolored; two briefs with the same macrostructure and different palettes do.

| Macrostructure | Organizing logic | Fits |
|---|---|---|
| **Editorial** | Long-form narrative, strong type hierarchy, generous measure | Manifestos, brand stories, thought leadership |
| **Dashboard-first** | The product UI *is* the hero; show the real interface | Dev tools, analytics, data products |
| **Product-led** | Feature → benefit → proof, repeated in rhythm | SaaS, B2B apps |
| **Manifesto** | One belief stated boldly, evidence underneath | Category creators, rebrands, launches |
| **Split-screen** | Two persistent panels — one fixed, one scrolling | Portfolios, comparison, dual-audience |
| **Narrative scroll** | Scroll-driven sequence, one idea per viewport | Storytelling, product reveals, "wow" |
| **Comparison-first** | Us-vs-them / before-after as the spine | Switching markets, displacement plays |
| **Proof-first** | Logos, metrics, testimonials lead, pitch follows | Enterprise, trust-critical, late-stage |

**Rule:** Name the macrostructure before writing markup ("Macrostructure: dashboard-first — the product is the argument"). Do not default to centered-hero → 3-feature-grid → pricing → footer; that skeleton *is* the slop. Combine with the aesthetic from Design Direction Fallback and the loudness from Design Dials — three independent choices, not one template.

---

## Junior Pass

Before a full implementation on any Level 3+ task, show the cheap version first: stated assumptions + reasoning + gray-box placeholders with labels — then wait for confirmation. Understanding the request wrong early is ~100× cheaper to fix than after a full build.

```
JUNIOR PASS — before building [X]:
  Assumptions:   [type / user / goal / device / tone you inferred]
  Approach:      [archetype, layout skeleton, dials]
  Placeholders:  [ gray box: "hero image 16:9" ] [ gray box: "3 feature cards" ]
  Confirm before I build the real thing? (or correct any assumption)
```

**Skip the Junior Pass only when:** the task is Level 1–2, or the user explicitly said "just build it" / "don't ask, implement."

---

## Ambiguity Resolution Protocol

When the request doesn't map cleanly to a level:

1. **State your interpretation** — "I'm reading this as a Level 3 targeted overhaul of the hero section. Is that right?"
2. **Offer the adjacent level** — "If you want a full page redesign, say the word and I'll go deeper."
3. **Never silently guess** — guessing level wrong wastes more time than a two-sentence clarification.

For requests that are genuinely vague ("make it better"), default to Level 2 and state what you're doing.

---

## Design Direction Fallback — 5 Schools

When the request is vague about *style* ("make something nice", "I don't know what I want", "just design it"), do not reach for the same aesthetic reflex. Propose exactly **3 differentiated directions**, each drawn from a different design school — as visual descriptions, before any code.

| School | Visual character | Representative voices |
|---|---|---|
| **Information Architecture** | Rational, data-driven, restrained | Pentagram, Swiss International, Noto |
| **Motion Poetics** | Kinetic, immersive, technical beauty | Field.io, Refik Anadol, generative systems |
| **Minimalism** | Order, generous whitespace, precision | Kenya Hara, Naoto Fukasawa, Apple (pre-2020) |
| **Experimental Avant-garde** | Pioneering, generative, visual shock | Stefan Sagmeister, David Carson, Lubalin |
| **Eastern Philosophy** | Warmth, poetic restraint, contemplative | Kengo Kuma, wabi-sabi, Muji |

**Per direction, present:** a named philosopher/studio anchor ("Kenya Hara-style Eastern Minimalism", not "minimalism") · a 1-sentence reason it fits this context · 3–4 signature visual traits · 3–5 tone keywords.

**Rule:** No two directions from the same school — they must produce obvious visual contrast. After the user picks, return to the escalation level and Design Dials with the confirmed direction.

---

## Escalation Triggers During Work

Upgrade the level mid-task if you discover:

- The stated fix requires changing 3+ sections to look coherent
- The root cause is in the design system (tokens, type scale), not the component
- The content itself is broken (copy, hierarchy, missing states)

When upgrading: **stop, name what you found, propose the expanded scope, wait for confirmation.**

---

## Anti-Patterns

| What Claude does | Problem | Correct behavior |
|---|---|---|
| Applies full redesign when asked to "clean up" | Ignores user's scope signal | Level 2 only |
| Makes cosmetic tweaks when brand reference is named | Misreads escalation signal | Level 5 full redesign |
| Silently redesigns adjacent sections | Scope creep | Stay in stated scope |
| Asks 5 clarifying questions before acting | Over-caution on clear requests | Act at the obvious level |
| Adds features during a cleanup | Feature creep | Mention, don't implement |
