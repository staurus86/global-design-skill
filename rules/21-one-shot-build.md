# Rule 21 — One-Shot Autonomous Build

> Protocol for "build me a site" delivered in a single prompt with no follow-up dialogue expected. The interactive default (clarifying question → Junior Pass → confirm → build) collapses into one pass: **assume → declare → build → verify → deliver**. The quality bar does not relax — only the conversation does. Every gate from `quality-gates.md` still applies; the user is simply no longer the QA loop.

---

## When This Rule Applies

| Signal | Mode |
|---|---|
| Single prompt asking for a complete site/page ("сделай сайт", "build me a landing page for X") | One-shot |
| Explicit autonomy: "just build it", "don't ask, implement", "не задавай вопросов", "за один промпт" | One-shot |
| Agent / CI / headless context where no dialogue is possible | One-shot |
| User is present and the request is ambiguous on *scope* (level unclear per `rules/00`) | Interactive — ask the one targeted question |
| Audit, review, or question — no build requested | Not this rule |

**Precedence:** this rule overrides the Junior Pass requirement in `rules/00-escalation-protocol.md` — the Junior Pass content (assumptions, approach) is still produced, but *inside the deliverable* instead of as a blocking question.

---

## The One-Shot Pipeline

Chains existing protocols — nothing here replaces them, this is the autonomous wiring:

```
1. ESCALATION → treat as Level 5 full build (rules/00)
2. ASSUME     → fill the Assumption Ledger below — zero questions
3. MASTER     → lock a mini-MASTER inline: tokens, type scale, spacing,
                voice, visual metaphor, the One Memorable Thing
                (templates/specs/design-system-master.md)
4. STRUCTURE  → name the macrostructure + map the IA before any markup
                (rules/00 Macrostructure-First; blueprints/website-from-scratch.md)
5. BUILD      → blueprint order: nav → homepage → inner pages → states
                (matching blueprints/*-from-scratch.md for the site type)
6. VERIFY     → rendered verification loop (rules/20) + Gates 1–8 self-check
                + Banned Patterns scan + contrast pass (rules/19)
7. DELIVER    → working code + Assumption Ledger + verification evidence
                + max 3 open questions
```

Steps 3 and 4 are where one-shot builds die when skipped: without a locked MASTER the pages drift; without a named macrostructure the output defaults to centered-hero → 3-feature-grid → footer, which *is* the slop.

---

## Assumption Ledger

Every dimension the prompt leaves silent gets a stated default — never a silent guess, never a question. The ledger ships with the deliverable.

| Dimension | Default when prompt is silent | Override signal |
|---|---|---|
| Site type | Marketing site, 5–7 pages (`blueprints/website-from-scratch.md` minimal IA) | "landing" → single page; "app/dashboard" → SaaS blueprint |
| Audience | Buyer evaluating the product category; mid-trust, mobile-likely | Named role, B2B/B2C signal, sector |
| Conversion goal | Contact / lead capture | "sell", "signup", "subscribe", "download" |
| Macrostructure | Pick from the `rules/00` table by business type — never default to centered-hero skeleton | Content of the prompt (product demo → dashboard-first; founder story → editorial) |
| Aesthetic school | Pick **one** of the 5 schools (`rules/00`) by sector and name it — do not present 3 options, there is no one to choose | Named brand reference → calibrate to it (Brand Anchors table) |
| Design Dials | Variance 6 · Motion 4 · Density 4 — one notch bolder than interactive default: with no feedback loop, distinctive beats safe | Sector (finance/government → variance 4); "wow" → motion 6+ |
| Color | Derive accent hue from sector semantics; full OKLCH ramp per SKILL.md tokens | Brand color in prompt, existing logo/site |
| Typography | Fluid scale from SKILL.md; one display + one text face max | Brand font named |
| Copy | Write real copy per `rules/14` — never lorem ipsum, never fake names/metrics | Provided content |
| Imagery | CSS/gradient placeholder with labeled aspect ratio ("hero visual 16:9") | Provided assets, "use stock" |
| Industry rules | Call `GlobalDesignSkill:get_sector_context` if MCP available; else `industries/*.md` | — |

---

## Stack Defaults

Run `rules/18-css-framework-selection.md` detection first if a repo exists. Otherwise:

| Signal in prompt | Stack |
|---|---|
| Nothing specified, marketing/portfolio/local-business site | Static HTML + CSS custom properties (`tokens/tokens.css` shape) — zero build step, deployable anywhere |
| "React", "Next", app-like behavior, auth, dashboard | Next.js 16 + Tailwind v4 + motion/react |
| Existing codebase present | Match the repo — framework, conventions, token system |

A one-shot static site must be openable from `file://` — no dev server required to see the result.

---

## Self-Verification — Mandatory, Not Optional

In one-shot mode nobody reviews intermediate output, so step 6 carries the full QA weight:

- [ ] Render the real DOM at 390 / 768 / 1280 — `rules/20-rendered-verification.md` loop (axe, overflow, contrast), not a single default-state screenshot
- [ ] Gates 1–8 self-checked as a pass/fail table in the deliverable
- [ ] Banned Patterns scan (SKILL.md) run against your own output
- [ ] **Memorability Gate** (`rules/00`): name the One Memorable Thing in the deliverable — if you cannot name it, iterate before delivering, not after
- [ ] `prefers-reduced-motion`, focus-visible, keyboard nav verified — not assumed

"Should work" is not a deliverable state. If rendering is impossible in the environment, say so explicitly and list exactly what remains unverified.

---

## Deliverable Format

```
1. THE SITE        → working files, organized, ready to open/deploy
2. ASSUMPTION LEDGER → each silent dimension: chosen default + one-line reason
3. VERIFIED        → gates table + rendered-check evidence (viewports, axe, contrast)
4. OPEN QUESTIONS  → max 3 items genuinely worth the user's confirmation
                     (brand assets, real copy, imagery) — not design decisions
```

---

## Anti-Patterns

| Wrong | Right |
|---|---|
| Asking a clarifying question in one-shot mode | State the assumption in the ledger, build, flag for review |
| Delivering unverified code ("this should work") | Run the rule-20 loop before claiming done |
| Safe generic design "because there's no feedback" | One-shot *raises* variance — distinctive defaults, named metaphor |
| Skipping the MASTER "because it's one prompt" | Mini-MASTER inline — token drift kills multi-page one-shots |
| Lorem ipsum, "John Doe", invented metrics | Real copy per `rules/14`; omit testimonials if none exist |
| Presenting 3 design directions and waiting | Pick one school, name it, justify in one line, build |
| Burying assumptions in prose | Ledger table — scannable, correctable in one reply |
