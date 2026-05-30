# Worked Examples — how the skill routes across 5 site types

> Dry-run walkthroughs (not built artifacts): for five different site themes, this traces what the skill actually loads, what it asks, what the agent personas do, and what comes out. Grounded in the real routing — `skills/global-design/task-routing.md`, `rules/18-css-framework-selection.md`, `rules/00-escalation-protocol.md`, the MCP tools (`get_sector_context`, `learn_from_reference`), `blueprints/*`, `agents/*`, `skills/global-design/quality-gates.md`, `references/live-audit-snippets.md`.

**Shared pipeline (every task):**
`framework-detect (rule 18) → escalation level + dials (rule 00) → sector via MCP → blueprint / reference → domain rules → agent personas → 8 quality-gates → live-audit-snippets`

Honest note: the "agents" are markdown personas (`agents/*.md`) that frame the reasoning; the MCP server really does return sector rules from `industries/*.md` and cache learned niches. The skill directs the working agent — it does not spawn autonomous bots.

---

## 1. Fintech SaaS — analytics dashboard (build from scratch)

**Trigger:** "Build a fintech analytics dashboard, Next.js."

**Stack (load order):**
1. `rules/18` → reads `package.json` → finds `tailwindcss` → "Tailwind, no extra profile, rules apply as-is."
2. `rules/00` → Level 5 (from scratch). Dials: `DESIGN_VARIANCE 3` (trust-critical B2B), `MOTION_INTENSITY 2`, `VISUAL_DENSITY 8` (data-heavy).
3. MCP `get_sector_context("finance" + "tech-saas")` → from `industries/finance.md` + `tech-saas.md`: conservative palette, compliance/trust signals, data density, "no fake metrics", numeric precision, table-first.
4. `blueprints/saas-app-from-scratch.md` + `rules/13-saas-products.md` + `rules/11-data-tables.md` + `rules/01-visual-hierarchy.md` + `rules/04-color.md` (OKLCH) + `references/data-viz.md`.

**Questions (Junior Pass — mandatory at Level 5):**
- Who is the user — analyst / trader / risk manager? (drives density + default view)
- New product, or is there an existing design system / tokens?
- Dark theme as default or option? (fintech is often dark-first)
- Real metrics, or labelled gray-box placeholders?

Then a **Junior Pass**: ASCII skeleton (sidebar + KPI strip + bento chart grid + table), dials, gray-boxes — waits for confirmation before building.

**Agent actions:**
1. `agents/ux-architect.md` — screen map, IA, default views.
2. `agents/design-director.md` — macrostructure **dashboard-first** ("the product is the argument"), metaphor (cockpit), OKLCH tokens.
3. Build per blueprint (Tailwind, `motion/react` for entries/number counters — `rules/17`).
4. Data-viz patterns → charts (animate only transform/opacity — `rules/17 R10`).
5. `agents/accessibility-auditor.md` + `rules/07` + `rules/19-contrast-standards.md` — numeric contrast, focus rings, 44px targets.
6. `agents/performance-auditor.md` — LCP, no layout shift on charts.
7. **8 quality-gates** → `references/live-audit-snippets.md` (contrast in light+dark, table states empty/loading/error, **snippet E** — filters actually hide rows).
8. `agents/frontend-handoff-reviewer.md` + `templates/specs/frontend-tz.md` — dev handoff.

**Output:** dashboard-first macrostructure + OKLCH tokens + key screens (Tailwind/React) + component specs + handoff TZ + gates/live-audit report. Density 8, variance 3 — strict, no decoration.

---

## 2. Travel — boutique hotel landing page (from scratch, style undefined)

**Trigger:** "I need a beautiful landing for a boutique hotel, not sure what stack — make it wow."

**Stack:**
1. `rules/18` → no `package.json` → **Step 2 framework question** (vanilla / Bootstrap / Bulma / Tailwind…). "Wow landing, no heavy state" → recommend Tailwind or vanilla + tokens.
2. `rules/00` → Level 5; "not sure of style" + "wow" → triggers **Design Direction Fallback (5 schools)** → dials `DESIGN_VARIANCE 8`, `MOTION_INTENSITY 7`, `VISUAL_DENSITY 3` (editorial, image-led).
3. MCP `get_sector_context("travel")` → `industries/travel.md`: image-first, atmosphere/emotion, trust signals (reviews, ratings, photo proof), "book now" CTA.
4. `blueprints/landing-page-from-scratch.md` + `blueprints/interactive-landing-page.md` + `rules/14-landing-pages.md` + `references/marketing-sites.md` + `rules/03-typography.md`.

**Questions:**
- First, **3 directions from different schools** (rule 00): e.g. "Eastern Minimalism (Kenya Hara) — warm air + photography", "Editorial (Pentagram) — large type + grid", "Motion Poetics — cinematic scroll." Each: 3–4 visual traits + tone. Waits for the pick.
- Language/geo, seasonality, is there a pro photoshoot (image-led depends on it), goal — direct bookings or enquiries?

**Agent actions:**
1. `agents/design-director.md` — presents 3 directions (visual descriptions, no code), waits.
2. After the pick — macrostructure (**narrative-scroll** or **editorial**), never the default centered-hero (it's a Banned Pattern).
3. `agents/motion-designer.md` + `rules/17` — scroll scenes (`useScroll` / `whileInView`, reduced-motion).
4. `agents/conversion-designer.md` + `checklists/landing-conversion-review.md` — one primary CTA, trust next to CTA, booking form (`rules/10-forms.md`).
5. `agents/copy-editor.md` — copy without AI-slop.
6. Gates + `references/live-audit-snippets.md` (text contrast over a photo hero — snippet A, light/dark) + `checklists/wow-effects-checklist.md`.
7. Optional: `integrations/hyperframes/` — render a promo MP4 from the finished HTML.

**Output:** chosen direction → landing (Tailwind/vanilla) with narrative-scroll, cinematic motion, a single booking CTA, conversion + wow checks. Variance 8 — bold, but passed the contrast audit over photography.

---

## 3. E-commerce — category / catalog page redesign (existing)

**Trigger:** "Redo this shop category page — it looks like a template."

**Stack:**
1. `rules/18` → detect (often Bootstrap / Shopify-Liquid) → loads `integrations/frameworks/bootstrap/profile.md` if Bootstrap.
2. `rules/00` → "looks like a template" = a Level 5 signal; but it's a redesign → **diagnose before prescribing**.
3. `blueprints/redesign-existing-page.md` (Phase 1 audit → classify the problem → preserve/replace) — don't restyle until diagnosed.
4. MCP `get_sector_context("b2c-products")` → `industries/b2c-products.md`.
5. **`references/catalog-and-directory-design.md`** (catalog core: metaphor, JTBD scenarios, card-differentiation matrix, badge system, on-ramp shelves) + `rules/11-data-tables.md` + `references/behavioral-design.md`.

**Questions:**
- Is there analytics (CR, bounce, scroll-depth, exit by section)? If yes → diagnose by data; if no → heuristic audit.
- What to preserve (learned patterns, navigation) vs replace?
- Confirm: "I'm reading this as a Level 5 structural catalog redesign — right? or targeted?" (Ambiguity protocol).

**Agent actions:**
1. `agents/design-critic.md` — audit: 5+ structural problems (identical cards = Banned, symbol-as-status instead of badges, no selection scenarios, weak CTA).
2. Memorability Gate (`rules/00`) — metaphor + The One Memorable Thing + 10-second recall.
3. Token-first visual (OKLCH), bento grid instead of N identical cards, **Free/Paid/status badges instead of a single symbol** (anti-pattern added in v1.9.10), faceted filters.
4. `agents/conversion-designer.md` — product card: "best for", price, rating, quick CTA.
5. **Regression check (Phase 6)** + `references/live-audit-snippets.md`: **snippet E** (filters actually hide), **F** (text layer), matrix light/dark × grid/list × empty/filtered.
6. `templates/briefs/redesign-brief.md` + before/after spec (Phase 5).

**Output:** diagnosis (structural / hierarchy / content) → rebuilt category with differentiated cards, a badge system, selection scenarios; a before/after document; regression check passed. If the real problem was the offer, not the design, that's stated plainly (the "aesthetic-first redesign" anti-pattern).

---

## 4. Unknown niche — a Magic: The Gathering deck-builder community (from scratch)

**Trigger:** "A community site for MTG deck builders — tournaments, ratings."

**Stack:**
1. `rules/18` → framework question/detect.
2. `rules/00` → Level 5.
3. MCP `list_sectors` → none of the 14 cover "gaming / TCG community" → **`learn_from_reference`** (the "Unknown niche" path in CLAUDE.md) → learns from 2–3 niche references (mtggoldfish / archidekt-like): patterns, lexicon, trust signals, audience expectations. Result cached (`list_learned_niches`).
4. `blueprints/portfolio-from-scratch.md` / community patterns + `references/inspiration-sites.md` + `references/catalog-and-directory-design.md` (decks/ratings = catalog + community).

**Questions:**
- Give 2–3 niche references (for `learn_from_reference`), or trust the ones `agents/reference-hunter.md` finds?
- Audience: casual vs competitive (different density/jargon) → **mode-switch** (beginner/pro)?
- 3 directions (Design Direction Fallback), since "gaming" drifts to the default dark-neon slop.

**Agent actions:**
1. `agents/reference-hunter.md` → feeds `learn_from_reference` → returns a niche profile (visual language, terms, audience expectations).
2. `agents/design-director.md` → metaphor (e.g. "the play table / mana colors as navigation"), macrostructure (map / scenario-first for decks), not the default.
3. Build + `agents/motion-designer.md` (restrained), deck cards by the differentiation matrix.
4. Gates + live-audit (dark-theme contrast — a frequent failure) + Memorability Gate.

**Output:** a niche profile (cached for reuse) → a site with a metaphor drawn from the real niche, beginner/pro mode-switch, a deck catalog with ratings; proven not generic (the 10-second test names a hook, not "an MTG site").

---

## 5. Healthcare — pediatric clinic site (audit an existing, trust-critical)

**Trigger:** "Review and improve a pediatric clinic site — trust and accessibility matter."

**Stack:**
1. `rules/18` → detect.
2. `rules/00` → "review and improve" is ambiguous → **Ambiguity protocol**: "I'm reading this as Level 3–4: audit + targeted rebuild of the weak blocks — right?" Dials: `DESIGN_VARIANCE 2` (trust-critical), `MOTION_INTENSITY 2`, `VISUAL_DENSITY 4`.
3. MCP `get_sector_context("health")` → `industries/health.md`: trust / licensing / expert doctors (E-E-A-T), calm palette, accessibility as a priority, clear "book an appointment" CTA.
4. **`checklists/global-design-review.md`** (full audit) + **`agents/accessibility-auditor.md`** + `rules/07-accessibility.md` + `rules/19-contrast-standards.md` (medical = strict AA+ contrast).

**Questions:**
- Real data on doctors / licensing / reviews (can't fabricate — E-E-A-T)?
- Audience: parents on mobile, often stressed → mobile-first, large targets?
- Legal constraints on medical wording?

**Agent actions:**
1. `agents/design-critic.md` + full checklist — score by criteria, Banned Patterns, **text/SR-layer checks** (v1.9.10: decorative numbers aria-hidden, no single-symbol status).
2. `agents/accessibility-auditor.md` — WCAG 2.2 AA: contrast, focus, 44px, skip link, aria-live on the booking form; run `references/live-audit-snippets.md` (A contrast light/dark, F text layer) against the real render, not the default screenshot.
3. Macrostructure **proof-first** (doctors, licenses, reviews lead; booking nearby) — `rules/00`.
4. `agents/conversion-designer.md` — booking form (`rules/10-forms.md`), trust beside the CTA.
5. `agents/copy-editor.md` — no medical AI-slop, calibrated certainty.
6. Gates + `templates/outputs/ux-audit-report.md` / `design-review-report.md`.

**Output:** an audit report (scores + prioritized fixes), proof-first rebuild of the weak blocks, WCAG AA with evidence (axe/contrast before-after), a booking form with trust. Variance 2 — calm, dependable. Nothing about the doctors is invented (flagged "needs your content").

---

## What these 5 exercise

| Skill path | Fires in |
|---|---|
| Framework-detect (rule 18) first | all 5 |
| Escalation + Ambiguity protocol | #3, #5 |
| Design Direction Fallback (5 schools) | #2, #4 |
| MCP `get_sector_context` (14 sectors) | #1, #2, #3, #5 |
| MCP `learn_from_reference` (unknown niche) | #4 |
| Memorability Gate + Macrostructure-first | #2, #3, #4 |
| `catalog-and-directory-design.md` + v1.9.10 lessons | #3, #4 |
| Junior Pass before building | #1, #2, #4 |
| `live-audit-snippets` + 8 gates | all 5 |

*Examples version: global-design-skill v1.9.10 — `examples/skill-walkthroughs.md`. Real worked redesign: `redesigns/bestseotools/CASE-STUDY.md`.*
