# Redesign Existing Page

> Protocol for improving an existing design without starting from scratch. Diagnose before prescribing. Preserve what works; replace only what fails.

**Load alongside:** relevant domain rule (`rules/14-landing-pages.md` / `rules/13-saas-products.md` / etc.) · `checklists/global-design-review.md`

---

## The Core Rule of Redesign

**Never redesign aesthetics without diagnosing function first.**

A page that "looks dated" but converts at 8% is not broken. A page that looks "clean and modern" but loses users on the form is.

Start with data. If data is unavailable, start with a structured audit. Never start with "what should it look like instead."

---

## Phase 1: Audit Before Touching Anything

### Data audit (do this first if any analytics exist)

Collect before forming any opinion:

```
Current metrics:
- Conversion rate: [%]
- Bounce rate: [%]
- Time on page: [seconds]
- Scroll depth: [% of users reaching below the fold]
- Exit rate by section: [which section loses most users]
- Top exit page (if multi-page flow): [page name]

Heatmap data (if available):
- Most clicked elements: [list]
- Rage clicks (frustration signal): [locations]
- Form abandonment rate + which field: [%]
- Dead click zones (users clicking non-interactive elements): [locations]
```

**Diagnosis protocol:**
- High bounce + low time → user doesn't understand what the page is within 5 seconds
- High scroll + low conversion → user understands but isn't convinced
- Low scroll → content or visual pattern is stopping them above the fold
- High form abandonment → friction in the form itself (too many fields, unclear labels, fear of commitment)
- Rage clicks → expected interactive element that isn't interactive

---

### Heuristic audit (if no data)

Use `agents/design-critic.md` for full review. Key questions for redesign context:

**Comprehension test:**
Cover all visual design. Read only the text. Answer:
- What is this product/service?
- Who is it for?
- What does it cost or require?
- What do I do next?

If any answer is unclear from text alone, that is a structural problem — not a visual one.

**5-second test (simulate):**
Look at the hero for 5 seconds. What is communicated?
If the primary value proposition is not communicated, the hero fails — regardless of how it looks.

**CTA audit:**
- Count CTAs on the page. Are there more than 1 primary per section?
- Is the primary CTA visible above the fold on mobile?
- Is the CTA label specific or generic?

**Trust audit:**
- Is social proof present? Is it near the primary CTA?
- Is the proof specific (names, roles, numbers) or generic?

---

## Phase 2: Diagnosis — Classify the Problem

Every problem falls into one category. Don't redesign the visual layer for a structural problem.

| Category | Symptoms | Solution type |
|---|---|---|
| **Structural** | Wrong sections, missing sections, wrong order | Rearrange or add content |
| **Hierarchy** | Multiple competing focal points, weak CTA | Resize, reweight, reposition |
| **Content** | Vague copy, banned language, generic CTAs | Rewrite without redesigning |
| **Visual** | Inconsistent tokens, banned patterns, dated aesthetics | Visual update |
| **State** | Missing loading/error/empty states | Add states |
| **Performance** | Slow LCP, layout shift, jank | Technical fix |
| **Accessibility** | Contrast failure, keyboard traps, missing ARIA | Accessibility fix |

**Match the intervention to the problem:**
- Structural problem → change the architecture
- Hierarchy problem → adjust visual weight (no aesthetic redesign needed)
- Content problem → rewrite copy (no design work needed)
- Visual problem → update tokens, patterns, and components
- State problem → design and implement missing states
- Performance problem → technical optimization
- Accessibility problem → accessibility fix

---

## Phase 3: Preserve vs. Replace

Before changing anything, classify every element:

```
PRESERVE:
- Sections that perform well (high engagement, high scroll-through)
- Navigation structure users have learned
- Core value proposition if it's already clear
- Brand elements with recognition equity

REPLACE:
- Sections that fail the comprehension test
- Banned patterns from SKILL.md Section 2
- Any section users demonstrably exit or ignore (scroll depth data)
- Visual patterns that are inconsistent or dated

ADD:
- Missing states (loading, empty, error)
- Missing trust signals near CTA
- Missing social proof or evidence
- Missing FAQ or objection handling
- Missing mobile-specific behavior

REMOVE:
- Sections that duplicate other sections
- Decoration added to compensate for weak hierarchy
- Features or content that serve no user or business goal
- Filler content: placeholder stats, stock imagery, generic copy
```

---

## Phase 4: Redesign Protocol

### If structural changes are needed

Apply the relevant blueprint for the page type:
- Landing page → `blueprints/landing-page-from-scratch.md` section order as reference
- SaaS screen → `blueprints/saas-app-from-scratch.md` core screens
- Marketing website → `blueprints/website-from-scratch.md` homepage architecture

Do not redesign visuals until structure is approved.

### If visual update only

**Token-first approach:**
1. Define new OKLCH color tokens (don't touch components yet)
2. Define new type scale with `clamp()` (don't touch copy yet)
3. Update spacing tokens if needed
4. Apply tokens to components — no component structure changes

This allows visual refresh without breaking working structure.

**Pattern replacement:**
For each banned pattern found, reference the replacement:

| Banned pattern | Replace with |
|---|---|
| Side-stripe border card accent | Full border, background tint, or number/icon |
| Gradient text (`background-clip: text`) | Single solid color, differentiated by weight |
| Hero metric template | Specific narrative with supporting evidence |
| Identical card grid | Bento grid with varied cell sizes |
| `ease-in-out` everywhere | Named bezier curves per interaction type |
| Glassmorphism as decoration | Solid surface, or glass only for spatial depth |
| Purple-indigo gradient hero | Committed single hue, `oklch` color strategy |

### If adding missing states

Follow Gate 4 checklist from `quality-gates.md`.
For each interactive component: idle → hover → active → focus → disabled → loading → empty → error → success.

---

## Phase 5: Before/After Specification

Document what changed and why. Required for any handoff:

```markdown
## Change: [Section or component name]

**Before:** [Description of old state]
**Problem:** [Specific issue this caused — data or diagnosis]
**After:** [Description of new state]
**Why this fix:** [Principle or gate it addresses]
**Success criterion:** [How we know it's better — metric or test]
```

---

## Phase 6: Regression Check

After any redesign, verify that changes didn't break things that were working.

```
Regression checklist:
- [ ] Navigation still works on mobile (hamburger, dropdown, links)
- [ ] Forms still submit correctly
- [ ] All previously-working links still work
- [ ] Load time same or better (compare Lighthouse before/after)
- [ ] Accessibility score same or better (axe-core scan before/after)
- [ ] All interactive states still exist and function
- [ ] Token references updated consistently (no orphaned raw values)
```

### Verify-before-tile (when rolling a new pattern across many pages)

A redesign often means applying one new pattern (a bento block, an icon system, a CTA) to N pages. **Build it on ONE page, prove it, then tile** — never apply to all N first and check at the end.

```
Per page, before moving to the next:
- [ ] Horizontal overflow check at 390 / 768 / 1280 / 1440 (document.scrollWidth vs viewport)
- [ ] axe-core scan at the same widths (0 new violations)
- [ ] Look at the actual render — a screenshot, not just "no errors"
Only after the pattern is clean on page 1 do you replicate to pages 2..N.
```

Trust **artifacts on disk**, not a summary's claim of verification. If a prior note says "screenshots in /redesign/", confirm the files exist before believing the result. (Real miss caught this way on sk-seo.ru 2026-05-31: a hand-off summary claimed an axe pass with screenshots that were never written.)

---

## Redesign Anti-Patterns

These actions create redesigns that fail:

**Aesthetic-first redesign:** "Let's make it look more modern" without diagnosing why it's underperforming. Result: new visuals, same structural problems, no conversion improvement.

**Complete replacement:** Throwing away everything because the design "feels dated." Results in loss of patterns users had learned, brand recognition damage, and reintroducing old solved problems.

**Solving by adding:** Adding more content, more features, more social proof, more sections to a page that's already not working. More content on a broken page is more broken page.

**Ignoring the mobile context:** Redesigning desktop, treating mobile as "and make it responsive." Mobile users are not smaller desktop users — they have different intent, different context, and different patience.

**Redesigning the wrong thing:** Page performance is driven by the offer, not the design. If the product doesn't match market need, no design improvement will fix conversion.

**Tile-before-verify:** Applying the new pattern to all pages, then checking once at the end. A break in the shared CSS now multiplies across every page, and you can't tell which page introduced it. Verify page-by-page (see Phase 6).

**Shipping deploy junk (no-build sites):** A `cp -r` / "upload the whole folder" deploy step on a raw-HTML site sweeps backup folders, `*.tmp`, and source assets onto production — on an SEO site, backup HTML at predictable URLs is crawlable duplicate content. Before deploy, move junk out of the deploy paths (move, never delete user files); after deploy, restore. Confirm the cache-buster (`?v=`) actually changed on the live page.

---

## Quality Gates for Redesign

All gates from `quality-gates.md` still apply. Additionally:

- [ ] Preserved elements are documented (what and why)
- [ ] Replaced elements are documented (what problem they had)
- [ ] Before/after comparison document exists
- [ ] Regression check passed
- [ ] Analytics baseline recorded (for post-launch comparison)

Run `agents/design-critic.md` on the redesigned version.
Run `agents/conversion-designer.md` if the page has conversion goals.
Run `agents/frontend-handoff-reviewer.md` before development.
