# Case Study — bestseotools.ru (catalog redesign, до → после)

> A real, multi-session redesign of a 450-tool SEO/marketing catalog. Used as the proving ground for `references/catalog-and-directory-design.md`, the verification snippets in `references/live-audit-snippets.md`, and the semantic/accessible-layer rules. Independent reviewer score moved **65–70% → ~85%** on the anti-slop task across the rounds documented here.

Screenshots: `before/` (original), `dna/` (the Author's Arsenal build), `after/` (early fixes), `after/v2-*` (current state — badge system, shelves, grouped nav, radar legend, semantic cleanup).

---

## The arc

**Before** — a generic aggregator: centered hero, generic H1 ("Лучшие инструменты для SEO"), 393 identical icon+title+description cards, a single `$` glyph as the only status, a flat 45-item category row, no point of view. Passed naive "clean" checks but was forgettable. (`before/desktop-fullpage.jpeg`, `before/desktop-hero.jpeg`)

**After (DNA)** — generative anti-slop: author chip ("Куратор — Кириченко Станислав"), H1 reframed to *"инструменты, которые стоят в моём рабочем стеке"*, JTBD scenarios ("Что тебе нужно?"), the «Стек Станислава» tool-radar, selection methodology block. (`dna/01..05`)

**After (v2)** — product layer + semantic cleanup: explicit pricing badges, curated shelves, grouped category nav, radar legend + axis labels, favorites/export/share, and a pass over the accessible/text layer. (`after/v2-*`)

---

## Problems → fixes (each generalised into the skill)

| # | Before (problem) | After (fix) | Encoded in |
|---|---|---|---|
| 1 | Generic H1 = the category name | H1 carries the author's point of view; author chip up top | `rules/00` Memorability Gate, `catalog-and-directory-design.md` §5/§7 |
| 2 | 393 identical cards | Differentiating signals (status / region / ★ my-stack), colour only on the commercial signal | `catalog-and-directory-design.md` §4 |
| 3 | Single `$` = the only status, ambiguous (paid **and** freemium under it) | Distinct **Free / Freemium / Paid** badges + **★ Мой стек**; `$` retired (`display:none`, kept in DOM only as a JS data hook) | `catalog-and-directory-design.md` §4, `checklists/global-design-review.md` |
| 4 | Filters/search *looked* applied but cards stayed visible | `.card{display:flex}` overrode `[hidden]{display:none}` → added `.card[hidden]{display:none!important}`. **Verify rendered visibility (`offsetParent`), not the attribute.** | `references/live-audit-snippets.md` E |
| 5 | Active category "ran back and forth" while scrolling | Scroll-spy compared scroll vs **cached** offsets; lazy images grow page height → stale. Use **live `getBoundingClientRect()`** | `rules/17-motion-react.md` |
| 6 | Tall grouped nav collapsed the instant it pinned | Sticky can't pin a tall element. Expanded nav `position:relative` (scrolls away); only the **compact bar** sticks, after the expanded one has scrolled past | `rules/17-motion-react.md` |
| 7 | Decorative numbers duplicated `<ol>` numbering for screen readers ("1, 1 …"); lone `$` leaked into `innerText` | `aria-hidden` on decorative ranks / plot nodes / status glyphs; audit the **text/SR layer**, not just visual | `rules/07-accessibility.md`, `live-audit-snippets.md` F |
| 8 | Hero stat tiles showed `—` with no JS; live HTML served 396 while file had 450 | Static count **fallbacks must equal** the JS-computed values (no-JS/crawler layer); check **cache/version desync** (CDN, Cache-Control on HTML, Service Worker) | `live-audit-snippets.md` G, `blueprints/redesign-existing-page.md` Phase 6 |
| 9 | A firehose of 450 with only search | Curated **shelves** ("ready stacks") + JTBD + favorites/export/share | `catalog-and-directory-design.md` §3/§7/§8 |

---

## What this case proves

- **Clean ≠ memorable.** Removing slop tells got the site to ~70%; the jump to ~85% came from *generative* anti-slop (author voice, scenarios, curated shelves) — the second half of `catalog-and-directory-design.md`.
- **The accessible/text layer is a first-class deliverable.** Several "passing" states were broken only for screen-readers / Googlebot / `innerText` (lone `$`, duplicate list numbers). Audit what bots and SR read, not just the rendered pixels.
- **Measure the rendered result, exercise interactive state.** The worst bug (all filters + search visually dead) passed an attribute-level test and a default screenshot; it failed only a rendered-visibility check.

*Case version: global-design-skill — `redesigns/bestseotools/CASE-STUDY.md`*
