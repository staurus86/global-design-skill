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

## Ambiguity Resolution Protocol

When the request doesn't map cleanly to a level:

1. **State your interpretation** — "I'm reading this as a Level 3 targeted overhaul of the hero section. Is that right?"
2. **Offer the adjacent level** — "If you want a full page redesign, say the word and I'll go deeper."
3. **Never silently guess** — guessing level wrong wastes more time than a two-sentence clarification.

For requests that are genuinely vague ("make it better"), default to Level 2 and state what you're doing.

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
