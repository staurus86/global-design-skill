# Case Study — chexter.ru (homepage redesign, до → после)

> A Level-5 full redesign of the homepage of chexter.ru — a Russian B2B SaaS suite of website-audit tools (SEO + GEO). Pilot-first: one page taken to a proven, verified standard before tiling. Verified on a **live PHP render** (HTTP 200, axe 0 violations, 0 horizontal overflow at 390/768/1280), not on claims.

Screenshots: `before/` (light prod homepage), `after/` (the Living Diagnostics redesign, real PHP-rendered).

---

## The arc

**Before** — a competent but forgettable light SaaS landing: generic H1 *«Проверка сайта онлайн — SEO-аудит за 30 секунд»* (a speed promise, no point of view), a sparse mid-page (JS-dependent cards leaving large empty bands on a full-page capture), and a tool catalog presented as a filter + uniform grid — the classic catalog slop risk. Passed naive "clean" checks; named no metaphor.

**After (Living Diagnostics)** — a dark, narrative-scroll *"x-ray of your site"*. The chosen direction (school: Motion Poetics; dials VARIANCE 7 / MOTION 7 / DENSITY 4). The One Memorable Thing is a live **scan panel** that sweeps the entered URL and builds SEO / GEO / Speed metrics. The catalog became "16 instruments of the scanner" grouped by SEO / Technical / AI, fronted by JTBD scenarios («Что нужно проверить?»). The differentiator of the niche — **GEO / AI-visibility** (does ChatGPT/Perplexity/Gemini see and cite you) — drives the whole narrative.

---

## Problems → fixes (each generalised into the skill)

| # | Before (problem) | After (fix) | Encoded in |
|---|---|---|---|
| 1 | Generic H1 = a speed promise; no metaphor | H1 carries a point of view («глазами AI и Google»); scan-panel as the One Memorable Thing | `rules/00` Memorability Gate |
| 2 | Catalog as filter + identical grid | JTBD scenarios + curated SEO/Technical/AI groups, AI group signalled in teal | `references/catalog-and-directory-design.md` §3/§4 |
| 3 | Primary button white-on-accent contrast **3.54:1** | Darker `--c-accent-deep` (oklch 51%) → ≥4.5:1; caught by axe, not by eye | `checklists/global-design-review.md` 2.3 |
| 4 | No focus-visible ring, no skip-link, faint placeholder | `:focus-visible` on all interactives, skip-link, placeholder → muted | `rules/07-accessibility.md`, checklist 2.7/7.1/7.2 |
| 5 | Hyphenated `id` used as JS global → `g_seo is not defined` → **whole mid-page blank** (cards + reveals dead) | `getElementById`; one JS throw blanks all later effects | `references/live-audit-snippets.md` §H |
| 6 | Mobile overflow 451 > 390 | `min-width:0` on Grid/Flex track children; trust `scrollWidth`, not bounding rects | `references/live-audit-snippets.md` §I |
| 7 | Below-fold reveals stayed `opacity:0` in `fullPage` shots | Scroll through before capturing | `references/live-audit-snippets.md` §J |
| 8 | `php -S` 500 locally — entry hardcodes a prod base path | Local-only router shim overriding the constant; never edit the deploy entry | `references/live-audit-snippets.md` §J |
| 9 | Assumed font was Inter (skill bans it) — it was Onest/Manrope | Read the layout/CSS before claiming theme or fonts | this case study |

---

## What this case proves

- **Verify on the real artifact, locally, before claiming done.** Installing PHP + a router shim turned "PHP doesn't run here" into a true before/after with axe 0 and overflow 0 — the redesign was proven on the actual PHP render, not the static prototype alone.
- **One JS throw is a layout bug.** The worst-looking failure (a blank middle) was a single `ReferenceError`; the fix is trivial once you capture `pageerror` instead of trusting the screenshot.
- **Isolation makes a Level-5 pilot safe.** Dark theme scoped to `body.home-v2` + `hv-` prefixed classes + a standalone-layout flag → zero regression on `/pricing/`, `/tools/`, `/blog/` (all still 200) while the homepage changed completely.
- **Clean ≠ memorable, again.** The jump from the old light page wasn't "darker and nicer" — it was a metaphor (x-ray scan) + the niche's real differentiator (GEO/AI), which is what a visitor recalls.

*Case version: global-design-skill — `redesigns/chexter/CASE-STUDY.md`. Pilot verified 2026-05-31. Mass roll-out (other pages) tracked separately.*
