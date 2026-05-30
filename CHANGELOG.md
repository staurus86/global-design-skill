# Changelog

All notable changes to global-design-skill are documented here.

Format: [version] — date — description

---

## [1.9.5] — 2026-05-30

### Reference sources distributed across the skill (curated, license-aware)

A large catalog of design sources was triaged and placed in its correct home — copyable code separated from inspiration-to-study, with explicit licensing throughout.

- **New `references/component-libraries.md`** — license-aware catalog of *usable code and assets*: component libraries (shadcn/ui, Magic UI, Aceternity, Origin UI, HyperUI, daisyUI, Preline, Flowbite, Meraki, Radix, Mantine, MUI, Chakra, Ant Design), free templates/cloneables (Figma, Framer, Webflow, Untitled UI), and free illustrations/SVG generators (unDraw, Open Doodles, Open Peeps, Haikei). Leads with a "copy code only where the license permits" table and an anti-slop "re-token before shipping" warning.
- **`references/inspiration-sites.md`** — expanded with Categories 9–12: Section & Component galleries (Component Gallery, Navbar Gallery, Footer Design, Bento Grids, CTA/Unsection), Motion & Interaction study (GSAP Showcase/Demos, Design Spells), Branding & Visual Identity (Typewolf, Fonts In Use, Brand New, Rebrand Gallery, Commerce Cream), and Anti-Slop Study (925Studios guide, Hallmark). Category 1 gained Siteinspire, Land-book, One Page Love, Refero, UI Patterns, ScreensDesign. "Take techniques, not brand assets" reinforced.
- **`references/sources.md`** — Design Systems extended with USWDS, Microsoft Fluent, IBM Carbon, Shopify Polaris, Atlassian (with licensing notes).
- **`rules/15-iconography.md`** — R5 now lists free, commercial-safe icon sources with licenses (Lucide ISC, Heroicons/Tabler/Phosphor MIT, SVG Repo verify-per-icon).
- **`references/typography.md`** — new "Where to Source Fonts" (Google Fonts, Fontshare, Fontsource) + discovery (Typewolf, Fonts In Use); self-host guidance.
- **`references/color-alchemy.md`** — new "Palette Tools" (Coolors, oklch.com) with explore-then-tokenize workflow.
- **`rules/00-escalation-protocol.md`** — new **Macrostructure-First** framework: choose page skeleton (editorial / dashboard-first / product-led / manifesto / split-screen / narrative-scroll / comparison-first / proof-first) before color or components — structural variety as the primary anti-slop defense.
- `README.md` references tree → 23; `SKILL.md` Full Package Reference notes the new catalogs.

---

## [1.9.4] — 2026-05-30

### Two component patterns added (harvested from sibling design skills)

- `patterns/navigation/header-patterns.md` — **Pattern C: Fluid Island** — a floating, detached glass-pill navbar that reads as a spatial object, not browser chrome. Sticky-offset + content-width + click-through gutters + blur-on-sticky guidance.
- `patterns/effects/hover-effects.md` — **Effect 8: Button-in-Button** — trailing arrow nested in its own circular wrapper that translates independently of the button on hover (mechanical depth, not a flat color swap). Added to the Hover Effect Selection Guide.

Both were genuinely absent (verified by gap-check); the rest of the surveyed design skills (high-end-visual-design, industrial-brutalist-ui, designer-skills, theme-factory) were already covered by existing rules, patterns, blueprints, agents, and the A–H aesthetic archetypes — no wholesale import.

---

## [1.9.3] — 2026-05-30

### Authoritative sources catalog (new)

- `references/sources.md` — primary-source bibliography behind the skill's standards, grouped by domain (accessibility/contrast, OKLCH color, typography, motion, Core Web Vitals, CSS Baseline, frameworks, UX laws, design systems). URLs verified current as of May 2026; dated facts noted (WCAG 2.2 Rec Oct 2023, INP replaced FID Mar 2024, Motion renamed from Framer Motion 2025).
- `README.md` — references tree corrected to 22 files: adds the previously unlisted `tech-standards.md` plus new `sources.md`.
- `skills/global-design/SKILL.md` — Full Package Reference notes the sources catalog.

### Frameworks harvested from the retired `hyperdesign` skill

- `rules/00-escalation-protocol.md` — three approach frameworks added:
  - **Design Dials** — DESIGN_VARIANCE / MOTION_INTENSITY / VISUAL_DENSITY, independent 1–10 sliders with defaults and raise/lower triggers
  - **Junior Pass** — show assumptions + gray-box placeholders before any Level 3+ build; skip only for Level 1–2 or explicit "just build it"
  - **Design Direction Fallback — 5 Schools** — for style-vague requests: propose 3 contrasting directions from Information Architecture / Motion Poetics / Minimalism / Experimental Avant-garde / Eastern Philosophy
- `checklists/global-design-review.md` — **AI Slop Test** added to Pre-Delivery Sanity Tests: first-order (category→look), second-order (category+avoided-cliché→look), third-order composition audit (balance / whitespace / rhythm / gestalt)
- `hyperdesign` skill retired — all unique content harvested; remaining material was already covered by `agents/`, `patterns/`, `blueprints/`, and `rules/`.

---

## [1.9.2] — 2026-05-30

### Typography Rule — 3 new rules (gap-closing vs. industry references)

- `rules/03-typography.md` — closes gaps surfaced by cross-referencing canonical UI guides (Adham Dannaway "16 UI Design Tips", Nordclan "UX for frontend"):
  - **R11** — Left-align body text; center only elements ≤ 2 lines; never justify web body text
  - **R12** — Pick body/UI fonts with a tall x-height (legible at 14–18px); reserve low x-height fonts (Gill Sans, Futura) for large display
  - **R13** — Vertical rhythm: derive text spacing from line-height (40–75%), gap above a heading > gap below it
  - Anti-patterns + Acceptance Criteria extended with the three new checks

### Info status color (new — 4th functional color)

- Adds the `info` status color (cyan, hue 230 — kept distinct from accent hue 258 so an informational message never reads as a primary action). Completes the standard error/success/warning/info set.
  - `tokens/tokens.css` — `--color-info-100/500/700` primitives + `--color-info` / `--color-info-bg` semantic tokens
  - `tokens/tokens-dark.css` — dark-mode info overrides (both `[data-theme="dark"]` and `prefers-color-scheme` blocks)
  - `tokens/design-tokens.json` — info primitive scale + semantic status entries
  - `tokens/README.md` — info documented in the semantic status list
  - `skills/global-design/SKILL.md` — inline `--color-info` token in the core palette
  - `rules/04-color.md` — R3 status exception + R7 color-is-never-the-only-signal table include info
  - `rules/06-components.md` — R8 adds `.badge-info`

---

## [1.9.1] — 2026-05-30

### Contrast Standards Rule (new)

- `rules/19-contrast-standards.md` — full contrast standard covering all three layers of the UI (page background → block/section → text). 13 rules:
  - **R1** — The contrast triangle: surface separation, text-on-block, adjacent sections — each with its own threshold and upper limit
  - **R2** — WCAG 2.2 AA/AAA tier table with large text definition and exemptions (disabled, decorative, logos)
  - **R3** — OKLCH quick-check heuristic (ΔL thresholds) + verified tool list (Polypane, ColorAndFonts, Firefox DevTools)
  - **R4** — Surface layer stacking: page bg → card → elevated panel, with token examples for light and dark mode
  - **R5** — Adjacent section separation: ΔL ≥ 4 OR 1px border rule
  - **R6** — Text on colored blocks: measure against the immediate block background, not page background
  - **R7** — Gradient backgrounds: worst-point sampling method + scrim overlay technique
  - **R8** — Dark mode upper bound: halation explanation, comfort range 10:1–15:1, off-white token formula, forbidden pure white
  - **R9** — Muted, placeholder, and disabled states: placeholder requires 4.5:1 (not exempt); disabled is WCAG-exempt but needs non-color indicator
  - **R10** — Focus ring contrast: WCAG 2.2 §2.4.11, 3:1 against both bg and element, double-ring technique
  - **R11** — APCA (WCAG 3.0 preview): Lc threshold table, relationship to WCAG 2.2 AA, tool link
  - **R12** — Fix workflow: 6-step priority order + L-delta matrices for light and dark mode
  - **R13** — Automated checking: axe-core CI command, Playwright integration
  - Eye comfort section: line-height, line-length, letter-spacing, anti-aliasing interaction with contrast

- `checklists/global-design-review.md` — Color section expanded from 9 to 16 checks:
  - 2.6: text contrast measured against immediate block background
  - 2.7: placeholder text ≥ 4.5:1
  - 2.8: focus ring ≥ 3:1 on both sides
  - 2.9: dark mode body text ≤ 15:1 upper bound
  - 2.10: gradient backgrounds sampled at worst-contrast point
  - 2.11: adjacent sections — ΔL ≥ 4 or visible border
  - 2.12: card/block on page bg — ≥ 1.5:1 or border defines boundary

- `CLAUDE.md` — added routing row: "Contrast audit / fix" → `rules/19-contrast-standards.md`
- `README.md` — rule 19 added to repository structure tree

### Maintainability Fixes (skill-insp audit)

- `skills/global-design/SKILL.md` — Full Package Reference: rules count corrected 19 → 20 (escalation protocol + contrast standards added to the enumeration); frontmatter version 1.9.0 → 1.9.1
- `skills/global-design/task-routing.md` — Rules-by-Domain table completed with rows 17 (motion/react), 18 (css-framework-selection), 19 (contrast-standards), 00 (escalation-protocol); routing footer v1.7.0 → v1.9.1
- `manifest.yaml` — version 1.9.0 → 1.9.1

### Progressive Disclosure & Eval Coverage (skill-insp audit)

- `references/tech-standards.md` (new) — full stack code reference (CSS, Tailwind v4, React 19, Next.js 15, motion/react, GSAP, TypeScript 5) extracted from SKILL.md
- `skills/global-design/SKILL.md` — Technology Standards replaced with a compact "use X / not Y" summary table + pointer; file slimmed 609 → 420 lines (standalone utility preserved)
- `evals/golden/o02-o05.expected.md` (new) — golden reference specs for the remaining output evals (coverage now 5/5)
- `scripts/check-eval-output.py` (new) — deterministic checker for `required_in_output` / `forbidden_in_output` terms against a captured response
- `evals/README.md` — documented the eval runner
- `skills/global-design/SKILL.md` — Task Routing: added `GlobalDesignSkill:get_sector_context` (MCP) row for industry/niche-specific rules

---

## [1.9.0] — 2026-05-29

### Behavioral Design Reference

- `references/behavioral-design.md` — 29 cognitive biases mapped to UI/UX design decisions. Sourced from full scan of keepsimple.io/uxcore (105 biases reviewed; 29 directly applicable to interface design selected). Organized by design task:
  - **Pricing pages:** Anchoring effect, Decoy effect, Contrast effect, Mental accounting, Hyperbolic discounting, Less-is-better effect
  - **CTAs & copy:** Framing effect, Loss aversion, Self-reference effect, Illusory truth effect, Curse of knowledge, Negativity bias
  - **Navigation & IA:** Magical Number 7±2, Serial-position effect, Ambiguity effect, Unit bias
  - **Trust & social proof:** Halo effect, Bandwagon effect, Authority bias, Confirmation bias, Mere-exposure effect
  - **Onboarding & retention:** Peak-end rule, IKEA effect, Endowment effect, Escalation of commitment, Reactance
  - **Visual hierarchy:** Von Restorff effect, Picture superiority effect, Processing difficulty effect
  - Each entry includes: definition, where to apply in UI, HTML/code example, "why it works" one-liner
  - Quick reference table: 15 design tasks → applicable biases

### Repository Maintenance

- `README.md` — references count updated 19 → 20; `behavioral-design.md` added to repository structure tree
- `skills/global-design/SKILL.md` — Full Package Reference section updated to mention behavioral design reference

---

## [1.8.0] — 2026-05-29

### HyperFrames Integration

- `integrations/hyperframes/guide.md` — HTML-to-MP4 video workflow: composition structure, `data-start`/`data-duration` attributes, OKLCH token compatibility, animation adapter matrix (CSS ✅ GSAP ✅ motion/react ❌ scroll-driven ❌), 10-point pre-render checklist
- `CLAUDE.md` — added routing row for HTML design → MP4 video tasks (product demo, social content, changelog animation)

### Skill Compliance — Anthropic Official Guide

- `skills/global-design/SKILL.md` — restructured frontmatter: `version`, `author`, `tags`, `requires`, `standalone` moved under `metadata:` per Anthropic skill spec Reference B
- `skills/global-design/SKILL.md` — `description` rewritten to include explicit "Use when..." trigger phrases per WHAT+WHEN requirement; ~530 chars, within 1024 limit
- `skills/global-design/SKILL.md` — Scope Boundaries updated: HyperFrames HTML-to-video noted as exception to "no video production" rule

### Industry Sector Depth (9 sectors expanded)

Each of the following files received: OKLCH Design System palette, Key Component Patterns with HTML examples, Copy & Messaging table, Design References.

- `industries/health.md` — provider card pattern, appointment booking flow, emergency notice, trust bar, clinical color system
- `industries/finance.md` — fee comparison table, interactive calculator, security/compliance trust bar, account comparison cards, tabular-nums typography rule
- `industries/non-profit.md` — impact counter with count-up animation, donation form (monthly/one-time toggle), campaign progress bar, beneficiary story card, warm OKLCH palette
- `industries/real-estate.md` — property card, full-screen gallery, map+neighbourhood panel, viewing booking widget, mortgage estimator, premium neutral palette
- `industries/travel.md` — date picker/availability calendar, price breakdown panel, review display with sub-scores, real-data scarcity notice, sticky mobile booking bar
- `industries/government.md` — GDS-pattern step form, service start page, eligibility checker, document checklist, status tracker, plain language copy rules, GOV.UK color system
- `industries/entertainment.md` — trailer hero with muted autoplay, ticket purchase widget, countdown timer, streaming content grid, dark + neon palette per sub-niche
- `industries/education.md` — course hero, curriculum accordion, outcome stats block, pricing + payment plans, aspirational color system
- `industries/services.md` — practitioner hero, service tier cards, process timeline, testimonial card with photo, booking calendar widget, personal brand palette

### Agent Examples (2 agents)

- `agents/design-director.md` — 3 full example reviews added: REJECT (B2B SaaS generic hero), PASS (health clinic trust-first design), REVISE (e-commerce premium brand without identity)
- `agents/ux-architect.md` — 3 full example reviews added: SaaS onboarding flow blocker (60% abandonment root cause), e-commerce checkout IA (78% cart abandonment fix), admin panel missing states audit

### Repository Maintenance

- `README.md` — integrations count corrected 14 → 16; `hyperframes/guide.md` added to repository structure tree
- `manifest.yaml` — hyperframes integration reference added

---

## [1.7.0] — 2026-05-26

### CSS Framework Support Layer

- `rules/18-css-framework-selection.md` — router rule: auto-detects CSS framework via `package.json` signals, asks when detection fails, routes to framework-specific profile; runs first on any design or build task
- `integrations/frameworks/bootstrap/profile.md` — Bootstrap 5.3 profile: utility overrides, OKLCH token mapping, component patterns
- `integrations/frameworks/bulma/profile.md` — Bulma 1.0 profile: OKLCH variable mapping, modifier class conventions
- `integrations/frameworks/open-props/profile.md` — Open Props profile: custom property integration, size/color scale alignment
- `integrations/frameworks/unocss/profile.md` — UnoCSS profile: preset selection, shortcuts, OKLCH theme config
- `integrations/frameworks/panda-css/profile.md` — Panda CSS profile: token config, recipes, slot patterns
- `CLAUDE.md` — added CSS framework detection row to task routing table (runs before all other rules)

### Bug Fixes

- Fixed skill frontmatter YAML parse error in standalone field (`fix/skill: fix YAML parse error`)
- Fixed broken file dependencies causing errors during standalone skill evaluation
- Resolved regressions introduced by cosmetic polish pass; score restored from 87 → 91+
- Applied full audit pass against bestskills.dev rubric; raised overall score to 91+

### Community

- `CODE_OF_CONDUCT.md` — added Contributor Covenant v2.1; satisfies GitHub Community Standards

---

## [1.6.0] — 2026-05-25

### Sprint 37 — Repository Infrastructure

- `.gitattributes` — LF normalization for all text files on commit
- `.editorconfig` — consistent indent/charset/newline per file type
- `.github/workflows/ci.yml` — CI pipeline: line-ending check, industry validation, MCP/learning/SEDI test suites, Python syntax check across all `.py` files

### Sprint 38 — Root Agent Files

- `AGENTS.md` — contribution rules for Codex, Copilot, Claude, Cursor, Gemini; key invariants (stdout in MCP, STORE_ROOT import pattern, CRLF, test requirements)
- `CLAUDE.md` — task routing, design constraints, MCP setup for Claude Code
- `.github/instructions/mcp-server.instructions.md` — path-specific Copilot rules for `mcp-server/**/*.py`
- `.github/instructions/industries.instructions.md` — path-specific rules for `industries/*.md`

### Sprint 39 — Security and Privacy

- `SECURITY.md` — scope, MCP HTTP behavior, local storage path, reporting policy, `GDS_MCP_SAFE_MODE` flag
- `PRIVACY.md` — what is stored locally, what makes outbound requests, deletion commands, safe mode instructions
- `mcp-server/server.py` — `GDS_MCP_SAFE_MODE` env var: when set, all learning + SEDI tools are replaced with discoverable stubs returning a clear JSON error; `logging.error()` replaces `print()` for STDIO transport safety; `mcp.run(transport="stdio")` explicit transport

### Sprint 40 — Eval Suite

- `evals/trigger-evals.json` — 15 prompts with `should_trigger: true/false` verdicts for skill routing verification
- `evals/output-evals.json` — 5 full-task scenarios with `required_in_output` and `forbidden_in_output` arrays
- `evals/golden/o01-hero-redesign.expected.md` — reference output defining the quality bar for hero redesign
- `evals/README.md` — how to run and extend evals

### Sprint 41 — MCP Resources and Prompts

- `mcp-server/server.py` — 11 dynamic resources via `gds://` URI scheme: `rules/{name}`, `industries/{sector}`, `blueprints/{name}`, `patterns/{category}/{name}`, `tokens/css`, `tokens/css-dark`, `templates/frontend-tz`, `templates/component-spec`, `checklists/global-design-review`, `checklists/landing-conversion-review`, `skills/global-design`
- `mcp-server/server.py` — 5 workflow prompts: `audit_landing_page`, `redesign_hero`, `create_frontend_handoff`, `improve_admin_table`, `sector_design_brief`
- `mcp-server/server.py` — `_read_repo_file()` helper with CRLF normalization
- `mcp-server/tests/test_resources.py` — 10 tests for resource reading and `GDS_MCP_SAFE_MODE` env parsing

### Sprint 42 — Installer and CLI

- `scripts/gds` — cross-platform Python CLI: `gds install [--tool=...] [path]`, `gds doctor [path]`, `gds version`; `doctor` runs 9-point health check (Python version, fastmcp, skills, agents, server syntax, tokens, industries, MCP config, line endings)
- `scripts/install.sh` — bash one-liner wrapper for Linux/Mac

### Sprint 43 — Compatibility and Discovery

- `ROADMAP.md` — v1.6, v1.7, v2.0 milestones
- `docs/packs.md` — full pack breakdown: Core, UI packs (Landing/SaaS/Admin/Effects), Audit packs (a11y/perf/design-system/conversion), MCP Intelligence
- `README.md` — "Start here" table, "How it learns (SEDI)" section, self-learning tagline, compatibility matrix (7 tools x 4 capabilities), MCP section with resources URI list and 5 prompts

### Sprint 44 — Demo Gallery Wave 3

- `demo/caniuse-table.html` — self-contained Before/After redesign for a Can I Use browser compatibility table, with skeleton state, change log, token legend, responsive browser cards, and keyboard-accessible toggle
- `demo/devto-card.html` — self-contained Before/After redesign for a Dev.to article card, with skeleton state, change log, token legend, responsive article layout, and keyboard-accessible toggle
- `demo/index.html` — Wave 3 cards activated with live links; all 8 gallery demos are now clickable

### Sprint 45 — Demo Gallery Ninth Example

- `demo/lighthouse-audit.html` — self-contained Before/After redesign for a Lighthouse performance audit result, with priority action framing, Core Web Vitals cards, sequenced fix list, skeleton state, change log, token legend, and keyboard-accessible toggle
- `demo/index.html` — Lighthouse audit card added to Wave 3; gallery count updated to 9 redesigns
- `demo/README.md` — demo inventory updated with the ninth example

### Sprint 46 — Lighthouse Demo Depth Pass

- `demo/lighthouse-audit.html` — enriched the After state with audit-specific tokens, category score breakdown, environment metadata, projected score panel, performance budget rails, verification command snippet, and stateful fix checklist
- `demo/lighthouse-audit.html` — fixed score-chip label architecture: category text and numeric score now render as separate elements, while score bar color selectors only target progress rails

### Sprint 47 — README Consistency Pass

- `README.md` — synchronized version references, install commands, MCP tool/resource counts, quality gate names, typography wording, and Gemini CLI compatibility notes
- `scripts/gds` and `manifest.yaml` — version synchronized to 1.6.0
- `.github/workflows/pages.yml` — added a manual GitHub Pages deploy trigger for README-only or workflow-only maintenance pushes
- `.github/workflows/*.yml` — opted workflows into GitHub Actions Node 24 execution to clear Node 20 deprecation warnings

---

## [1.5.0] — 2026-05-25

### Sprint 31 — Industry Content Layer (Phase 1)

- `industries/_index.md` — routing table for all 13 sectors with disambiguation rules
- `industries/b2b-products.md` — YAML frontmatter v1.0.0, 9 sections: sector profile, mobile rules, required elements, banned patterns, trust signals, conversion path, page structure, quick diagnosis, disambiguation
- `industries/b2c-products.md` — same structure; swipeable gallery, add-to-cart primary CTA, review aggregators
- `industries/services.md` — booking-first layout, social proof hierarchy, bottom sheet on mobile
- `industries/content-media.md` — reading experience, subscription conversion, editorial layout
- `industries/education.md` — course conversion, outcome-first messaging, cohort vs self-paced paths
- `industries/health.md` — trust-first design, regulatory constraint handling, appointment booking
- `industries/finance.md` — compliance design patterns, trust hierarchy, risk disclosure layout
- `industries/real-estate.md` — listing-first layout, map integration, lead capture patterns
- `industries/travel.md` — availability-first UX, price anchoring, destination photography rules
- `industries/tech-saas.md` — developer-first hierarchy, free trial conversion, API documentation patterns
- `industries/non-profit.md` — donation funnel, emotional proof patterns, volunteer conversion
- `industries/government.md` — accessibility-first, task-completion hierarchy, plain language rules
- `industries/entertainment.md` — sub-niche routing (casual-games / aaa-games / streaming / live-events)
- `scripts/validate-industries.py` — frontmatter validator: checks all 9 required sections across all 13 files

### Sprint 32 — Extended State System (Phase 1)

- `patterns/states/_decision-matrix.md` — when to use loading vs skeleton vs partial-error vs offline vs permission vs rate-limit; loading/skeleton mutual exclusion rule
- `patterns/states/skeleton-states.md` — shimmer/pulse/structure-preview variants, CSS implementation
- `patterns/states/partial-error-states.md` — inline error rows, degraded-mode banners, retry-per-row
- `patterns/states/offline-states.md` — sync queue UI, last-updated timestamp, reconnection flow
- `patterns/states/permission-states.md` — no-access / upgrade-required / role-locked / coming-soon variants
- `patterns/states/rate-limit-states.md` — countdown timer, retry-after display, quota progress bar

### Sprint 33 — Validators + Feedback Tracking (Phase 1)

- `validators/lighthouse-ci.md` — LCP < 2.5s / CLS < 0.1 / FID < 100ms budgets, CI config examples
- `validators/axe-core.md` — a11y thresholds, Jest/Playwright setup
- `validators/bundle-analyzer.md` — size limits per component, tree-shaking checklist
- `feedback/gate-8-tracker.md` — log template for developer questions after handoff
- `feedback/iteration-log.md` — template for recording revision count before acceptance

### Sprint 34 — MCP Static Server (Phase 2)

- `mcp-server/` — new directory; Python 3.11+, fastmcp + graceful ImportError fallback
- `mcp-server/pyproject.toml` — dependencies: mcp>=1.0, fastmcp>=0.1, markdown-it-py>=3.0, PyYAML>=6.0
- `mcp-server/server.py` — 10 registered MCP tools with graceful degradation if fastmcp unavailable
- `mcp-server/tools/sector_context.py` — `list_sectors()`, `classify_niche()`, `get_sector_context()`
- `mcp-server/tools/industry_rules.py` — `check_banned_patterns(sector, content)`
- `mcp-server/tools/design_audit.py` — `get_quick_diagnosis(who_pays, decision_type, risk_level, choice_type, user_value)`
- `mcp-server/tests/test_classify_niche.py` — parametrised accuracy test over 50 fixtures (100% accuracy achieved)
- `mcp-server/tests/test_sector_context.py` — validates all 13 industry files parse and contain required sections
- `mcp-server/tests/fixtures/sample_queries.json` — 50 ground-truth queries across 13 sectors
- `mcp-server/README.md` — setup for Claude Code, Cursor, Windsurf; privacy disclosure; tool reference

### Sprint 35 — Learning Engine (Phase 3)

- `learning/sector_classifier.py` — keyword-weighted sector detection; `sub_niche` for entertainment; confidence < 0.5 → `"unknown"` + clarification
- `learning/ethical_scraper.py` — robots.txt compliance, noindex respect, 10 req/min rate limit, User-Agent `GlobalDesignSkill-Bot/1.0`
- `learning/pattern_extractor.py` — BeautifulSoup-based layout/components/trust_signals/conversion_elements extraction
- `learning/gap_detector.py` — static vs learned comparison; `suspicion_flag` at >40% divergence
- `learning/knowledge_base.py` — JSON store at `~/.global-design-skill/knowledge/`; LRU eviction at 500 MB; MAX_REFERENCES_PER_NICHE=10; CACHE_TTL_DAYS=30
- `mcp-server/tools/learning_tools.py` — 5 MCP tools: `learn_from_reference()`, `get_or_learn_sector()`, `list_learned_niches()`, `forget_niche()`, `reset_weights()`

### Sprint 36 — SEDI Full Architecture (Phase 4)

- `sedi/local_store.py` — `~/.global-design-skill/` initializer; 5 subdirs (knowledge/weights/feedback/evolution_log/metrics); chmod 700 on Unix
- `sedi/perception.py` — `RequestAnalysis` dataclass: intent / sector / niche / sub_niche / context / emotions / constraints; confidence < 0.5 → sector="unknown"
- `sedi/cognition.py` — `ConflictPriority` enum (USER_OVERRIDE > LEARNED > STATIC > GENERIC); `select_blueprint()` with sector overrides; `resolve_knowledge()` with validated-learned gate
- `sedi/execution.py` — `DesignOutput` dataclass; source citations per applied rule; quality gate stubs
- `sedi/feedback_engine.py` — explicit rating 1–5; implicit score from revision_count; success_rate formula; pattern weights ±10%, capped [0.1, 2.0]; `reset_weights()` per-sector or global
- `sedi/evolution.py` — `capture_baseline()` / `update_current_accuracy()` / `improvement_rate.json`; `check_stale_niches()`; `log_evolution_event()`; `run_weekly_cycle()`
- `mcp-server/tools/learning_tools.py` — 2 additional SEDI tools: `resolve_suspicion()` (3 modes: accept_learned / keep_static / merge) + `reset_weights_tool()`
- `integrations/claude-code/CLAUDE.md` — updated: `industries/` directory reference, sector-aware routing instruction

---

## [1.0.0] — 2026-05-20

### Sprint 0 — Foundation

- `README.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `install.md`, `manifest.yaml`
- Full directory scaffold: skills/, agents/, rules/, patterns/, tokens/, templates/, checklists/, recipes/, examples/, integrations/
- `skills/global-design/SKILL.md` — main entry point: decision pipeline, 8 aesthetic archetypes, banned patterns list, technology standards
- `skills/global-design/task-routing.md` — routing table: build / review / improve / output tasks
- `skills/global-design/operating-principles.md` — 10 principles, cognitive laws (Hick, Fitts, Miller, Doherty)
- `skills/global-design/quality-gates.md` — 8 acceptance gates from problem definition to frontend readiness
- `skills/global-design/output-formats.md` — output templates per audience

### Sprint 1 — Agents (5 files)

- `agents/design-director.md` — visual maturity, brand alignment, aesthetic archetype check
- `agents/ux-architect.md` — problem definition, IA, user flows, edge cases
- `agents/conversion-designer.md` — CTAs, offer structure, friction inventory, pricing psychology
- `agents/design-critic.md` — adversarial review, banned pattern audit, REJECTED/CONDITIONAL/APPROVED verdicts
- `agents/frontend-handoff-reviewer.md` — Gate 8 validation: every state, token, ARIA attribute specified

### Sprint 2 — Blueprints (5 files)

- `blueprints/landing-page-from-scratch.md` — 9-section AIDA structure, hero to final CTA
- `blueprints/saas-app-from-scratch.md` — 3 shell options, 6 core screens, React 19 + Next.js 15 code
- `blueprints/admin-panel-from-scratch.md` — density-first, 6 screens, keyboard shortcuts
- `blueprints/website-from-scratch.md` — multi-page IA, CSS Anchor Positioning nav, schema markup
- `blueprints/redesign-existing-page.md` — 6-phase protocol: audit → classify → preserve/replace → redesign → regression

### Sprint 3 — Rules (7 files)

- `rules/01-visual-hierarchy.md` — 10 rules: focal point, size delta, contrast mapping, CTA dominance
- `rules/02-layout-and-grid.md` — 12 rules: mobile-first, grid break, safe areas, z-index system
- `rules/06-components.md` — 10 rules: component contracts, all states required, native dialog
- `rules/12-admin-panels.md` — 11 rules: density-first, label everything, destructive friction levels
- `rules/13-saas-products.md` — 10 rules: Day 1 vs Day 365, aha moment, useOptimistic
- `rules/14-landing-pages.md` — 11 rules: one CTA per section, headline formula, AIDA structure
- `rules/16-design-for-seo.md` — 10 rules: Core Web Vitals, schema markup, semantic HTML

### Sprint 4 — Marketing Patterns (5 files)

- `patterns/marketing-blocks/hero-sections.md` — 4 patterns: split, centered, full-bleed, asymmetric bento
- `patterns/marketing-blocks/pricing-sections.md` — 3 patterns + anchoring, decoy effect, annual default
- `patterns/marketing-blocks/social-proof.md` — 5 patterns: logos, metrics, testimonials, featured quote
- `patterns/marketing-blocks/cta-sections.md` — 4 patterns + full button CSS system
- `patterns/marketing-blocks/faq-sections.md` — 3 patterns + FAQPage schema JSON-LD

### Sprint 5 — Product UI Patterns (5 files)

- `patterns/product-ui/onboarding.md` — linear wizard, in-app checklist, product tour
- `patterns/product-ui/empty-states.md` — 5 types, copy formula, float animation
- `patterns/product-ui/error-states.md` — 9-type taxonomy, 5 patterns, copy formula
- `patterns/product-ui/loading-states.md` — decision matrix (<100ms / 100ms–1s / 1–10s / >10s), 6 patterns
- `patterns/product-ui/settings-pages.md` — IA, save-on-change vs submit, toggle, danger zone, API keys

### Sprint 6 — Navigation + Admin Patterns (6 files)

- `patterns/navigation/header-patterns.md` — marketing header (transparent→solid), app header, skip nav
- `patterns/navigation/sidebar-patterns.md` — full + collapsed, workspace switcher, expandable groups
- `patterns/navigation/mobile-navigation.md` — bottom tab bar, hamburger drawer with @starting-style
- `patterns/admin-ui/data-tables.md` — toolbar, bulk bar, sort, sticky headers, skeleton, pagination
- `patterns/admin-ui/filters.md` — filter bar, active chips, dropdown panel, date range, URL state
- `patterns/admin-ui/dashboard-layouts.md` — KPI cards, sparklines, 12-col grid, real-time pattern, accessible charts

### Sprint 7 — Templates + Checklists (6 files)

- `templates/specs/frontend-tz.md` — Gate 8 developer handoff: all states with exact values, tokens, ARIA, acceptance criteria
- `templates/specs/component-spec.md` — component API, anatomy, variants, states, ARIA, changelog
- `templates/briefs/project-brief.md` — problem, north star metric, scope, constraints, sign-off table
- `checklists/global-design-review.md` — 100+ checks across 11 sections, banned pattern audit
- `checklists/landing-conversion-review.md` — AIDA, CTA quality, social proof, friction, pricing, SEO
- `checklists/ui-review.md` — forms, tables, filters, modals, loading, errors, admin-specific, a11y

### Sprint 8 — Recipes (8 files)

- `recipes/make-page-more-premium.md` — 9 steps: typeface, OKLCH tint, grain texture, grid break, split hero, shadow system, bezel, spacing rhythm, signature detail
- `recipes/make-interface-cleaner.md` — 9 steps: 1 accent color, background depth, 3-level hierarchy, icon removal, dividers, button hierarchy, spacing grid, copy, z-axis
- `recipes/improve-hero-section.md` — 7 steps: layout choice, headline formula, eyebrow tag, product visual with perspective, CTA discipline, entry animation, LCP
- `recipes/improve-pricing-page.md` — 8 steps: annual default, recommended plan, price anchoring, feature table, social proof, CTA copy, enterprise, FAQ
- `recipes/improve-forms.md` — 7 steps: field audit, labels, error formula (validate on blur), loading/success, password reqs, never reset fields, keyboard nav
- `recipes/add-dark-mode.md` — 7 steps: OKLCH token architecture, shadow system, toggle without flash, localStorage, image/logo handling, component audit, transition
- `recipes/improve-mobile-version.md` — 10 steps: 100dvh, 44px targets, iOS zoom prevention, mobile nav, safe area insets, horizontal scroll, typography, hover-only, CTA above fold, performance
- `recipes/improve-empty-states.md` — 5 types (first-time/no-results/cleared/permission/error), copy tone rules, float animation, acceptance criteria

### Sprint 9 — Design Tokens (4 files)

- `tokens/design-tokens.json` — W3C DTCG format: OKLCH primitive palettes (10-step), semantic light/dark tokens, 20-value spacing grid, fluid type scale, tracking, line-height, radius, shadow, duration, cubic-bezier easings, z-index, breakpoints
- `tokens/tokens.css` — complete CSS custom properties: all token categories + component aliases (input/button/card/focus-ring) + global resets
- `tokens/tokens-dark.css` — dark mode via `[data-theme="dark"]` + `@media prefers-color-scheme`, shadow→border conversion, `.theme-transition` class
- `tokens/README.md` — two-layer color system, usage examples, Style Dictionary config, Tailwind v4 integration, stylelint rule

### Sprint 10 — Repository Finalization

- `README.md` — updated: complete file map (57 files), quick start, capabilities table, quality gates summary, banned patterns quick reference
- `CHANGELOG.md` — updated: complete sprint history

### Sprint 11 — Missing Rules (5 files)

- `rules/03-typography.md` — R1 fluid clamp scale, R2 16px minimum, R3 letter-spacing tracks size, R4 line-height by context, R5 75ch max line length, R6 font pairing (banned fonts list), R7 eyebrow tag CSS, R8 H1 ≤3 lines on mobile, R9 no gradient text, R10 variable font weight animation
- `rules/04-color.md` — R1 OKLCH mandatory (anatomy), R2 tinted neutrals, R3 one accent hue, R4 accent ≤15% surface area, R5 chroma at extremes, R6 WCAG contrast table, R7 color not only differentiator, R8 dark mode as separate system, R9 color-mix() for alpha, R10 color strategy selection
- `rules/05-animation.md` — R1 everything must enter, R2 no ease-in-out (easing guide), R3 no transition:all, R4 duration scale table, R5 @starting-style, R6 prefers-reduced-motion, R7 IntersectionObserver, R8 no multiple pulse (shimmer), R9 stagger, R10 motion/react not framer-motion
- `rules/07-accessibility.md` — R1 keyboard-operable, R2 focus-visible ring, R3 persistent labels, R4 alt text, R5 ARIA custom components, R6 aria-live dynamic content, R7 modal focus trap, R8 44px touch targets, R9 skip navigation, R10 semantic HTML first. Keyboard reference table.
- `rules/08-performance.md` — Core Web Vitals targets table, R1 LCP fetchpriority, R2 image dimensions (CLS), R3 WebP/AVIF (compression targets), R4 lazy/eager loading, R5 font-display:swap, R6 async/defer scripts, R7 no CLS from dynamic content, R8 Doherty Threshold 400ms, R9 virtualize >200 rows, R10 Next.js "use cache"

### Sprint 12 — Integrations (3 files)

- `integrations/claude-code/CLAUDE.md` — ready-to-paste CLAUDE.md snippet: all 8 rule categories, token usage guide, quality gates checklist, banned patterns quick reference, reference file table
- `integrations/cursor/cursor-rules.md` — .cursorrules content for Cursor IDE: complete rule set in cursor-native format, 3 setup options (file/settings/docs)
- `integrations/chatgpt/custom-gpt-instructions.md` — full system prompt for Custom GPT or OpenAI API: role definition, all rule categories, banned patterns, color strategy guide, tech stack defaults, response format instructions, Python API usage example

### Sprint 13 — Worked Examples (5 files)

- `examples/01-hero-redesign.md` — centered to editorial split: font, gradient, CTA hierarchy fixes
- `examples/02-color-token-migration.md` — 12 files of hardcoded hex → OKLCH semantic token layer
- `examples/03-form-accessibility.md` — 8 a11y fixes: labels, error formula, touch targets, autocomplete
- `examples/04-card-grid-cleanup.md` — 3-equal-column grid → asymmetric bento with hierarchy
- `examples/05-performance-audit.md` — fetchpriority, preload, image sizing, defer: LCP 4.2s → 1.8s

### Sprint 14 — Missing Rules (4 files)

- `rules/09-responsive.md` — 5 breakpoints, mobile-first, 100dvh, safe area insets, srcset/sizes, hover-only gating
- `rules/10-forms.md` — minimum fields, blur validation, error formula, no reset, autocomplete/inputmode, disabled states
- `rules/11-data-tables.md` — column alignment, density modes, aria-sort, row selection, sticky header, pagination vs infinite
- `rules/15-iconography.md` — stroke 1.5px, currentColor, single icon set, no emoji as icons, semantic labels

### Sprint 15 — Missing Patterns (4 files)

- `patterns/product-ui/forms.md` — sign-in, settings, multi-step, shared elements
- `patterns/product-ui/modals.md` — confirmation dialog, form modal, drawer, @starting-style entry, focus trap
- `patterns/product-ui/notifications.md` — 4-type decision tree, toast manager, banner, inline alert, aria-live
- `patterns/marketing-blocks/feature-sections.md` — alternating split, asymmetric bento grid, how-it-works steps

### Sprint 16 — New Agents (5 files)

- `agents/accessibility-auditor.md` — 4-phase WCAG audit (visual, keyboard, ARIA, content), severity matrix, WCAG 2.2 table
- `agents/performance-auditor.md` — CWV investigation, LCP/CLS/INP identification, budget table, regression detection
- `agents/copy-editor.md` — headline test, CTA formula, error formula, 20+ banned words, tone calibration table
- `agents/motion-designer.md` — easing audit by context, duration scale, prefers-reduced-motion, motion budget by page type
- `agents/design-systems-auditor.md` — token coverage grep commands, component state matrix, debt scoring 0–100, migration path

### Sprint 17 — Marketing Patterns + Recipes (3 files)

- `patterns/marketing-blocks/feature-sections.md` — alternating split, asymmetric bento, how-it-works with connectors
- `recipes/improve-navigation.md` — 6 steps: Hick's Law audit, rename to user goals, active state, mobile nav, breadcrumbs
- `recipes/improve-typography.md` — 7 steps: font replacement, fluid scale, line-height, letter-spacing, eyebrow, 65ch prose, gradient text

### Sprint 18 — Example + New Integrations (3 files)

- `examples/06-dark-mode-implementation.md` — primitive→semantic token layer, class-based toggle, localStorage, no-flash inline script, Next.js implementation
- `integrations/windsurf/rules.md` — .windsurfrules content: all 8 rule categories in Windsurf-native format
- `integrations/github-copilot/copilot-instructions.md` — .github/copilot-instructions.md: full design system rules for Copilot Chat

### Sprint 19 — Figma Integration (2 files)

- `integrations/figma/variables-export-guide.md` — variable architecture (primitives + semantic), Tokens Studio export, Style Dictionary transform, GitHub Actions auto-sync
- `integrations/figma/plugin-workflow.md` — plugin stack, Tokens Studio setup + GitHub sync, contrast checking workflow, handoff annotation, Gate checklist

### Sprint 20 — Navigation Patterns (3 files)

- `patterns/navigation/tabs-patterns.md` — horizontal tabs, pill tabs, vertical tabs, keyboard handler, ARIA roles
- `patterns/navigation/breadcrumbs.md` — standard, collapsed (ellipsis), dropdown variant, JSON-LD structured data
- `patterns/navigation/pagination.md` — standard, compact, rows-per-page, ellipsis algorithm, rel=prev/next SEO

### Sprint 21 — Product UI Patterns (3 files)

- `patterns/product-ui/search.md` — inline filter, live search with combobox ARIA + keyboard, empty state
- `patterns/product-ui/tooltips-popovers.md` — CSS-only tooltip, click popover, info tooltip, positioning rules
- `patterns/product-ui/command-palette.md` — full ⌘K palette: combobox, grouping, keyboard nav, search, command data schema

### Sprint 22 — Marketing + Admin Patterns (4 files)

- `patterns/marketing-blocks/comparison-sections.md` — pricing card grid, feature comparison table with highlighted column
- `patterns/marketing-blocks/stats-sections.md` — horizontal stats bar, stats with context + source, animated counter
- `patterns/admin-ui/charts.md` — chart type selection, Recharts line/bar/donut, sparklines, accessibility requirements
- `patterns/admin-ui/bulk-actions.md` — inline toolbar (slides in on selection), sticky bottom bar (mobile), confirmation modal

### Sprint 23 — Recipes (3 files)

- `recipes/add-animations.md` — 8 steps: motion budget, easing tokens, hover transitions, IntersectionObserver, hero entrance, skeleton shimmer, motion/react migration, @starting-style modals
- `recipes/improve-loading-states.md` — 5 patterns: skeleton loading, button spinner, optimistic UI, blur-up images, empty state
- `recipes/improve-onboarding.md` — 3 principles, multi-step wizard component, empty dashboard checklist, activation metrics

### Sprint 24 — Blueprints (3 files)

- `blueprints/pricing-page-from-scratch.md` — hero + annual toggle, 3-tier cards, comparison table, FAQ accordion, trust strip, final CTA, pricing psychology checklist
- `blueprints/portfolio-from-scratch.md` — hero with availability status, work grid (featured + 2-col), short about, contact CTA, portfolio anti-patterns
- `blueprints/onboarding-flow-from-scratch.md` — signup form (OAuth first), 3-step wizard, aha moment animation, getting-started checklist, activation metrics

### Sprint 25 — Example Directories (2 files)

- `examples/landing-pages/01-saas-hero-redesign.md` — banned centered hero → editorial left-aligned split with Fraunces + product screenshot
- `examples/apps/01-settings-page.md` — flat single-column form → vertical tab navigation with two-column rows + isolated danger zone

### Sprint 26 — References System + Reference Hunter Agent (13 files)

- `references/inspiration-sites.md` — 8-category curated gallery: general galleries, SaaS/product, marketing, portfolios, pricing, navigation, forms, dashboards
- `references/aesthetic-archetypes.md` — real production sites per archetype A–H, each with 8 examples + signature techniques + what to study
- `references/saas-ui-examples.md` — annotated SaaS UI: command palette, empty states, settings pages, onboarding, loading states, errors, modals, notifications, tables
- `references/marketing-sites.md` — hero sections, social proof, feature sections, pricing, CTAs, nav, animation — all annotated with "what to steal"
- `references/portfolios.md` — 8 top portfolio sites (paco.me, rauno.me, leerob.io, antfu.me, joshwcomeau.com, maggieappleton.com, brianlovin.it, tobiasahlin.com) with thesis analysis
- `references/pricing-pages.md` — Linear, Vercel, Stripe, Notion, GitHub, Intercom pricing analyzed — psychology, patterns, anti-patterns
- `references/navigation-examples.md` — sidebar (Linear, Vercel, Stripe, Notion), top nav (Webflow, Stripe, Arc), mobile (bottom tabs, hamburger), breadcrumbs
- `agents/reference-hunter.md` — 4 capabilities: (1) search by block category, (2) search by style/aesthetic, (3) competitive analysis, (4) URL audit with scoring rubric
- `templates/specs/design-review-report.md` — structured review output: gates, dimension scores, banned patterns, critical/major/minor issues, sign-off table
- `templates/briefs/redesign-brief.md` — redesign scope brief: what exists, what fails, constraints, acceptance criteria, sign-off
- `examples/audits/01-landing-page-audit.md` — full audit of generic B2B SaaS landing: 34/100 → all 8 gates, banned patterns found, prioritized fixes
- `examples/websites/01-multi-page-site.md` — multi-page site IA decisions, docs nav system, CSS Anchor Positioning, View Transitions, schema markup per page type

---

## Total: 121 files, ~44,000 lines

| Category | Files | Description |
|---|---|---|
| Core skill | 5 | Entry point, routing, principles, gates, formats |
| Agents | 11 | 11 specialized review roles (+ reference-hunter) |
| Blueprints | 8 | Build-from-scratch protocols |
| Rules | 16 | Domain rules with rationale and code |
| Patterns | 27 | Marketing, product UI, navigation, admin |
| References | 7 | Curated real-world examples per category and archetype |
| Tokens | 4 | JSON + CSS light + CSS dark + guide |
| Templates | 5 | Specs, briefs, review report, redesign brief |
| Checklists | 3 | Design review, conversion, UI ship |
| Recipes | 13 | Step-by-step improvement guides (+wow hero, +page transitions) |
| Integrations | 7 | Claude Code, Cursor, ChatGPT, Windsurf, Copilot, Figma (×2) |
| Examples | 10 | Before/after worked examples + audits + websites |
| Docs | 4 | README, CONTRIBUTING, CHANGELOG, install |

### Sprint 27 — Effects System + Wow Recipes (8 files)

**patterns/effects/ (new directory):**
- `patterns/effects/visual-effects.md` — grain texture, mesh gradient, spotlight cursor, glow/bloom, glassmorphism depth, double bezel, background patterns (dot/grid/diagonal), shadow depth system, aurora
- `patterns/effects/parallax-system.md` — 6 levels: CSS perspective (zero JS), JS scroll+RAF, multi-layer depth, mouse-tracking (lerp), GSAP ScrollTrigger scrub+pin, CSS scroll-driven `@scroll-timeline`
- `patterns/effects/text-animations.md` — split reveal (CSS + GSAP SplitText), blur-in sequence, character scramble hover, typewriter with cursor, variable font weight on scroll, gradient sweep, velocity marquee, count-up with IntersectionObserver
- `patterns/effects/scroll-experiences.md` — Lenis smooth scroll + GSAP integration, pinned stacking cards, horizontal scroll gallery, reading progress bar, section reveal system (IntersectionObserver), scroll-linked opacity fade, scroll snap
- `patterns/effects/hover-effects.md` — 3D card tilt + shine (mouse tracking), magnetic button, button fill slide/radial, image zoom/clip-path/overlay/caption, link underline draw, card lift, pill nav sliding indicator
- `patterns/effects/cursor-effects.md` — cursor glow tracking, custom dot cursor with lerp + hover/click states, mix-blend-mode invert, text-reveal cursor, cursor trail (`pointer: coarse` detection throughout)

**recipes/ (2 files):**
- `recipes/create-wow-hero.md` — 9-step wow hero: headline formula, 3 layout options, background atmosphere per archetype, display font setup, product visual with bezel+perspective, CTA hierarchy with magnetic, trust signal, entrance sequence, LCP optimization checklist
- `recipes/add-page-transitions.md` — first-load entrance (`[data-enter]` stagger system), View Transitions API (Baseline 2024), shared element transitions for portfolios, Next.js App Router integration, navigation progress bar

### Sprint 28 — Effects Completion + Wow Blueprint (4 new files + 3 updates)

**New files:**
- `patterns/effects/3d-effects.md` — CSS 3D fundamentals (perspective model), card flip, product tilt showcase with layered parallax, isometric layout, prism rotation, Three.js minimal setup, react-three-fiber integration, Spline embed, 3D text. Performance rules + when-to-use matrix
- `blueprints/interactive-landing-page.md` — full wow-stack blueprint: token foundation, global atmosphere (grain + spotlight), hero with entrance sequence, scroll reveals, GSAP pinned stack, marquee, CTA glow, View Transitions. 25-item assembly checklist, 4 archetype starter configs
- `checklists/wow-effects-checklist.md` — 9-category effects quality gate (65 items): reduced motion, GPU/compositing, bundle/load, mobile degradation, visual quality, entrance sequence, banned patterns, scroll integrity, accessibility. Scoring: ≥90% ship, 70–89% beta, <70% block
- `examples/websites/02-agency-portfolio.md` — full Cyberbrutalism (archetype C) studio site: brutal nav with offset-shadow buttons, kinetic marquee, Monument hero, asymmetric work grid, manifesto, case study layout, character scramble effect, view-transition title morph

**Updates:**
- `skills/global-design/task-routing.md` — rewritten: fixed broken paths, added Visual Effects Tasks section (all 7 effects files), references routing, reference-hunter agent
- `skills/global-design/SKILL.md` — added Effects Decision Block (4-step flow), fixed routing table, restored knowledge references + added example references
- `integrations/claude-code/CLAUDE.md` — added effects rules (will-change, devicePixelRatio, pointer:coarse, 100dvh), corrected rule file paths, added effects patterns table

**Also committed:** 12 knowledge references (`references/typography.md`, `color-alchemy.md`, `motion-systems.md`, `motion-dev.md`, `visual-effects.md`, `3d-animations.md`, `accessibility.md`, `performance.md`, `tokens.md`, `forms.md`, `responsive.md`, `data-viz.md`) and `patterns/marketing-blocks/bento-grid.md` — content that existed on disk but was never tracked (~5,700 lines).

### Sprint 29 — Link Rot Audit + Missing Files (4 new files + ~20 reference fixes)

Full-repository cross-reference audit. Fixed dangling links left by an earlier `rules/` renumbering and created files that were referenced but never authored.

**New files:**
- `checklists/frontend-handoff-review.md` — extended Gate 8 handoff checklist, 7 sections + final gate
- `checklists/admin-panel-review.md` — admin-panel review: density, data tables, destructive actions, bulk actions, states, keyboard efficiency, scored gate
- `templates/outputs/ux-audit-report.md` — UX audit deliverable template: exec summary, critical/medium issues, WCAG findings, priorities, estimates, scope
- `integrations/figma/figma-handoff-checklist.md` — Figma handoff: variable→token mapping, naming conventions, component structure, Dev Mode, token sync pipeline

**Reference fixes:**
- Renamed `examples/05-performance-lcp.md` → `05-performance-audit.md` in README + CHANGELOG
- Repointed ~17 stale rule references (old renumbering scheme: `01-spacing`, `02-cognitive-laws`, `04-color-systems`, `05-spacing-and-density`, `06-layout`, `07-responsive-design`, `08-accessibility`, `10-forms-and-inputs`, `11-tables-and-data-ui`) to canonical names across 14 files
- Fixed `patterns/product-ui/data-tables.md` → `patterns/admin-ui/data-tables.md` in `rules/11-data-tables.md`
- Fixed `skills/hyperdesign/references/color-alchemy.md` → `references/color-alchemy.md` in `tokens/README.md`

### Sprint 30 — Publication Readiness (1 new file + metadata fixes)

Prepared the repository for public GitHub release.

- `LICENSE` — added MIT license file (© 2026 Stanislav Kirichenko)
- Replaced placeholder GitHub URLs (`yourusername`, `your-org`) with the real repository path `github.com/staurus86/global-design-skill` in README, install.md, manifest.yaml, and the Claude Code integration
- `manifest.yaml` — fixed `author` field, corrected `tokens` list (was 5 non-existent files, now the 3 real token files), completed the `agents` list (5 → 11) and `integrations` list (+windsurf, +github_copilot)
- `install.md` — rewrote to remove references to a non-existent helper script; manual `cp` commands throughout; corrected token file names; added Windsurf and GitHub Copilot sections
- `CONTRIBUTING.md` — removed stale "rule gaps" list (all 16 rules now exist)
- `README.md` — added Author section (Stanislav Kirichenko / Staurus, sk-seo.ru), corrected the author name, linked the `LICENSE` file

---

## Total: 154 files, ~59,000 lines

| Category | Files | Description |
|---|---|---|
| Core skill | 5 | Entry point, routing, principles, gates, formats |
| Agents | 11 | Specialized review roles incl. reference-hunter |
| Blueprints | 9 | Build-from-scratch protocols incl. interactive landing |
| Rules | 16 | Domain rules with rationale and code |
| Patterns | 38 | Marketing, product UI, navigation, admin, effects |
| References | 19 | 12 knowledge references + 7 curated example galleries |
| Tokens | 4 | JSON + CSS light + CSS dark + guide |
| Templates | 6 | Specs, briefs, review report, redesign brief, audit report |
| Checklists | 6 | Design review, conversion, UI, handoff, admin, wow effects |
| Recipes | 15 | Step-by-step improvement guides incl. wow recipes |
| Integrations | 8 | Claude Code, Cursor, ChatGPT, Windsurf, Copilot, Figma (×3) |
| Examples | 11 | Before/after worked examples + audits + websites |
| Docs | 6 | README, CONTRIBUTING, CHANGELOG, install, manifest, LICENSE |
