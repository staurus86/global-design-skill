# Reference — Portfolio Sites

> Annotated examples of the best developer, designer, and designer-developer portfolio sites. Study these before building any portfolio. Each entry explains the decision that makes the site distinctive.

---

## Designer-Developer Crossover Portfolios

Sites that demonstrate both visual design skill and technical implementation quality.

### paco.me — Paco Coursey
**URL:** paco.me  
**Archetype:** A — Ethereal Black  
**What to study:**

- **Interaction design as portfolio proof.** The site's own micro-interactions ARE the portfolio. Every hover state, every transition demonstrates the skill being claimed.
- **Keyboard shortcut panel.** Press `?` — a command palette of site shortcuts appears. This is the entire portfolio thesis in one interaction: "I think about keyboard-first UX."
- **Dark mode executed correctly.** Not inverted light mode — designed dark-first with separate shadow system (glow on dark vs. drop-shadow on light).
- **Content hierarchy without decoration.** No icons, no gradient accents. Just typographic weight and scale creating hierarchy.

**Signature techniques:**
- `framer-motion` (pre-deprecation) spring transitions on every card hover
- Custom cursor — subtly enlarged, no trail
- Consistent 8px spacing grid throughout

---

### rauno.me — Rauno Freiberg
**URL:** rauno.me  
**Archetype:** B — Editorial Luxury  
**What to study:**

- **Typography as the entire visual identity.** The site is built around how type relates to space. No background decoration, no imagery beyond project screenshots.
- **Editorial whitespace.** Section padding that seems "too much" is what makes the type breathe. Study the relationship between line length and surrounding space.
- **Image layout.** Project screenshots displayed as editorial photos — perspective, shadow, slight rotation. Not screenshots in a card, but photographs of screens.
- **The scroll.** Slow, deliberate. The scroll speed itself communicates editorial quality.

**Signature techniques:**
- Full-bleed project screens with CSS `perspective()` and subtle `rotate()`
- Line-height: 1.65 throughout body copy (higher than most sites)
- Minimal color: single off-white background, one near-black, no accent

---

### leerob.io — Lee Robinson
**URL:** leerob.io  
**Archetype:** A — Ethereal Black  
**What to study:**

- **Writing as primary content.** Portfolio organized around articles, not projects. The thesis: "my blog is my portfolio." Study for: how developer thought leadership converts better than project screenshots for senior roles.
- **Next.js as portfolio proof.** The site itself demonstrates Next.js expertise through its implementation (MDX, ISR, server components). The technology choice IS part of the portfolio.
- **Minimal navigation.** Home / Writing / About. Three items. Nothing else. Study how ruthless IA makes a portfolio feel confident, not sparse.
- **GitHub activity as credibility.** Recent commits visible on the homepage. Not screenshots — live data.

**Signature techniques:**
- MDX for all content — code blocks with syntax highlighting are first-class content
- `use server` components for all data fetching
- Minimal color: one electric blue accent for links only

---

### antfu.me — Anthony Fu
**URL:** antfu.me  
**Archetype:** D — Organic Softness (unusual for a developer)  
**What to study:**

- **Open source as portfolio.** Homepage is essentially a GitHub contributions graph + project list. No "About me" prominence — the work speaks. Study for: OSS contributor portfolios where contribution history is more convincing than a bio.
- **Monochrome warmth.** Almost no color, but warm black-on-cream creates softness without being pale or washed out.
- **Animation as signature.** The Japanese character animation on hover — a single distinctive interaction that makes the site memorable. Study: one signature interaction beats 10 generic ones.
- **Transition between projects.** Click a project — the site transitions not just the content but the color temperature. Each project has its own ambient color.

**Signature techniques:**
- CSS `@starting-style` for page transitions
- Monochrome with hue rotation per project
- Typography: single variable font, minimal weight variation

---

### joshwcomeau.com — Josh Comeau
**URL:** joshwcomeau.com  
**Archetype:** D — Organic Softness with interactive elements  
**What to study:**

- **Interactive explainers as portfolio proof.** The articles ARE interactive demos. Sliders, animations, visual explanations — the blog demonstrates front-end skill better than any project grid.
- **Educational tone as brand.** Not "here are my projects" but "here's how this works." Portfolio positioned as a teaching resource rather than a resumé. Study for: education-forward developer portfolio positioning.
- **Color as personality.** Pink/purple palette that reads as warm and approachable, not corporate. The color choice communicates "I care about design" without claiming to be a designer.
- **Component polish.** Every interactive demo is a finished, accessible component. Detail at this level signals senior skill.

**Signature techniques:**
- Inline interactive demos with CSS sliders + JavaScript updates
- Houdini `@property` for animated custom properties
- Persistent dark mode via `prefers-color-scheme` + manual override

---

### brianlovin.it — Brian Lovin
**URL:** brianlovin.it  
**Archetype:** A — Ethereal Black  
**What to study:**

- **Design annotations as portfolio content.** The "Design Details" section documents UI patterns across the industry with deep analysis. Study for: demonstrating taste and analytical skill without claiming authorship of other people's work.
- **Writing about design as proof of design thinking.** The portfolio thesis: "I can see what makes design good or bad." This is more convincing for senior design roles than a Dribbble grid.
- **Community and presence.** GitHub contributions, writing frequency, public work. The portfolio is a live activity feed, not a static showcase.
- **Dark mode default.** Dark-first design with system-aware toggle.

**Signature techniques:**
- Custom annotation system for screenshots (notes on hover/click)
- MDX blog with GitHub-style code blocks
- Extensive use of `data-theme` attribute for per-component dark mode testing

---

### tobiasahlin.com — Tobias Ahlin
**URL:** tobiasahlin.com  
**Archetype:** B — Editorial Luxury  
**What to study:**

- **Typography-first portfolio.** The site's visual identity is entirely in typeface choice and spacing. No decorative elements. Study for: how editorial typography alone can create a premium positioning.
- **SpinKit (open source animation library).** The portfolio is inseparable from the creator's best-known open source work. Study for: when your OSS contribution IS your portfolio.
- **Long-form case studies.** Projects explained through decisions, not outcomes. "Why we chose this" beats "what we built."

---

### maggieappleton.com — Maggie Appleton
**URL:** maggieappleton.com  
**Archetype:** D — Organic Softness  
**What to study:**

- **Digital garden as portfolio.** Notes, essays, and projects interconnected like a wiki. Study for: knowledge worker portfolios where the connections between ideas matter as much as the ideas themselves.
- **Illustration integrated with typography.** Custom illustrations that feel native to the content — not decorative, but explanatory. Each illustration reduces the text needed.
- **Garden-first IA.** "Notes" and "Essays" and "Projects" are separate categories with different maturity signals. Work labeled as "in progress" openly.
- **Bidirectional linking.** Each article shows what links to it. Wiki-style graph visible from every page.

---

## What Distinguishes Excellent Portfolio Sites

**Common to all top portfolios:**

1. **The site IS the proof.** Every portfolio above uses its own design/technology as the first and best demonstration of skill. The medium is the message.

2. **A clear thesis.** Each portfolio has one reason to remember it:
   - paco.me: keyboard-first interaction design
   - leerob.io: Next.js + developer writing
   - joshwcomeau.com: interactive frontend education
   - maggieappleton.com: digital garden + illustration
   
3. **Quality over quantity.** 3–5 deeply documented projects beat 20 shallow ones. None of these sites have more than 10 featured projects.

4. **Writing as signal.** Every high-quality portfolio has substantial writing. Articles and case studies signal thinking quality, not just execution quality.

5. **No Lorem ipsum, no John Doe.** Placeholder content signals work in progress. These sites launch only with real, specific content.

---

## Portfolio Anti-Patterns

- **Carousel of mockups without context.** Showing a Dribbble-style screen without explaining the problem, constraints, or decisions.
- **"I'm a passionate designer who loves creating beautiful experiences."** Bio copy that any designer could claim.
- **Figma-embed portfolio.** Embedding a Figma file is not a portfolio — it's a file share.
- **Copy-pasted testimonials from LinkedIn.** LinkedIn endorsements aren't testimonials — they're social proof inflation.
- **Animated cursor as the only interesting interaction.** Custom cursors that serve no UX purpose signal that you ran out of ideas.
- **Three-equal-column project grid.** Symmetric grids hide hierarchy. Feature your best work bigger.
- **"Available for work" without specificity.** "Available for senior product design roles at early-stage B2B SaaS" converts better.

---

## Portfolio by Career Stage

**Junior developer/designer:**
- 3 projects, deeply documented
- Process > deliverable (show decisions, not just outputs)
- One very polished component or demo that demonstrates technical skill
- Focus: "I can execute and explain my reasoning"

**Mid-level:**
- 5–8 projects, mix of case studies and quick shots
- Writing section — 3–5 articles about craft
- GitHub activity as supporting signal
- Focus: "I have taste and I can grow"

**Senior / principal:**
- 3–5 high-impact projects with business outcomes
- Conference talks, writing, OSS contributions as peer signals
- Less "what I made" — more "what I influenced"
- Focus: "I improve teams, not just outputs"

---

*Reference version: global-design-skill v1.0 — `references/portfolios.md`*  
*Updated: 2026-05-20*  
*Related: `agents/reference-hunter.md`, `references/inspiration-sites.md`, `blueprints/portfolio-from-scratch.md`*
