# Rule — Rendered Verification

> A correct screenshot of the default state is not verification. The most expensive design bugs — invisible dark-mode headings, a filter that looks applied but hides nothing, a paid badge buried under a featured one, a counter that desyncs between JS and the no-JS HTML — all pass static review and a single hero screenshot. They fail only when you render the real DOM and exercise every mode. This rule makes that pass mandatory and routes the audits that catch each class. It is the operational half of Quality Gates 4–7: the Gates say *what* must hold; this rule says *prove it on the rendered page*.

This rule is the substance of Decision Pipeline step **12 VERIFY**. Do not declare a build done, a redesign shipped, or a Gate passed on inspection of the source alone.

---

## R1 — When rendered verification is mandatory vs optional.

| Situation | Rendered pass | Why |
|---|---|---|
| Escalation Level 3–5 (targeted overhaul → full redesign) | **Mandatory** | Structural change touches states and modes a default view never shows |
| Any build with dark mode, view toggles, filters/search, or JS-rendered counts | **Mandatory** | These are exactly the surfaces that pass attribute checks and fail rendered ones |
| Deploy / handoff of running code (PHP/React/static) | **Mandatory** before declaring done | A deploy is not verified until the live URL is exercised — never claim "deployed" without it |
| Level 1–2 (micro-adjustment, selective cleanup) on a non-interactive surface | Optional | A single property tweak with no state/mode surface rarely hides a rendered bug |
| Spec / handoff document with no running code | N/A | Nothing to render — verify against Quality Gates on paper |

**Rule:** when in doubt, render. The cost of a render pass is minutes; the cost of shipping an invisible heading is a re-deploy and lost trust.

---

## R2 — The render → audit → fix loop.

Run this loop, not a one-shot screenshot. Use the `webapp-testing` skill (Playwright) or paste the console scripts from `references/live-audit-snippets.md` into DevTools.

```
1. RENDER    → Load the real DOM (local dev server or live URL), not a mock
2. AUDIT     → Run the live-audit snippets + exercise the mode matrix (R3)
3. TRIAGE    → Each finding: is it source intent or rendered reality that's wrong?
4. FIX AT SOURCE → Patch the rule/token/component, not the one instance (R4)
5. RE-RENDER → Re-run the same audits in the same modes; confirm zero regressions
```

**Measure the rendered result, not the source intent.** A "correct" `color` can paint transparent (`-webkit-text-fill-color`, see `rules/19` R14); a filter with the right `[hidden]` attribute can stay visible if a `display` rule overrides it. Read what the browser actually paints and what a screen-reader / Googlebot actually receives (`innerText`, the a11y tree, `offsetParent !== null`), not what the markup intends.

---

## R3 — Exercise the full mode matrix, not the default view.

Bugs hide in the combinations the homepage hero never shows. Exercise every axis that applies:

| Axis | Values to exercise |
|---|---|
| **Theme** | light, dark (every transparent-fill and contrast check runs in *both* — a per-theme patch leaves the bug in the un-patched theme) |
| **Viewport** | 390px, 768px, 1280px (Gate 5 floor) — confirm no horizontal overflow at 390px |
| **View mode** | grid ↔ list, expanded ↔ collapsed, any toggle the UI offers |
| **State** | idle, loading, empty, no-results (distinct from empty), error, success, permission-denied, first-run |
| **Interaction** | apply a filter and confirm the rendered-visible count drops; submit a form; open a modal and trap focus |

The required combinatorial protocol and ready-to-paste scripts live in `references/live-audit-snippets.md` (D — theme × view-mode × state exercise). Do not hand-test one cell and assume the rest.

---

## R4 — Fix at the source, in every mode — never per-instance.

When the audit finds a bug, the fix is in the rule, token, or component — not the single rendered instance.

- A transparent-fill heading in dark mode → kill the legacy gradient-text at its source rule, then re-scan **both** themes. Patching the one heading leaves every other instance broken.
- A filter that doesn't hide → fix the CSS specificity collision (`.card{display:flex}` defeating `[hidden]{display:none}`) globally, not by adding one `!important`.
- A JS-only counter that desyncs from the no-JS HTML → ship a real static fallback in the markup, not a placeholder; check CDN/Cache-Control/Service Worker for stale snapshots.

This mirrors `blueprints/redesign-existing-page.md` **verify-before-tile**: prove a new pattern on one page (axe + overflow + render in every mode), *then* replicate. Tiling an unverified pattern multiplies the bug.

---

## R5 — The accessible/text layer is a first-class deliverable.

Rendered pixels can be perfect while the text layer is broken only for screen-readers, Googlebot, and `innerText`. Verify what bots and assistive tech receive, not just the painted result:

- No lone status glyphs (`$`, `→`) read aloud out of context
- No decorative numbers duplicating an `<ol>`'s own numbering ("1, 1 …" to a screen-reader)
- No category labels mangled by CSS abbreviation that screen-readers expand wrong
- The no-JS HTML and every CDN/cached snapshot agree with the live JS-rendered page (Gate per `rules/16-design-for-seo.md`)

Snippets F (text-layer audit) and G (count/version parity) in `references/live-audit-snippets.md`.

---

## Acceptance Criteria

```
[ ] Build rendered on the real DOM (dev server or live URL), not inspected as source only — for every Level 3+ task and every deploy
[ ] Mode matrix exercised: both themes × {390/768/1280} × every view toggle × {idle/loading/empty/no-results/error/success}
[ ] Contrast/visibility measured against the rendered fill and offsetParent, not color/attribute intent (ties rules/19 R14)
[ ] Filters/search verified to actually hide — rendered-visible count drops, not just an attribute flips
[ ] Every finding fixed at the source rule/token/component and re-scanned in ALL modes — no per-instance patches
[ ] Text layer verified: innerText / a11y tree clean (no lone glyphs, no duplicate list numbers, labels expand correctly)
[ ] no-JS HTML and CDN/cached snapshots match the live JS-rendered page (no count/version desync)
[ ] axe-core run on the rendered page passes (no new contrast/ARIA violations)
[ ] Deploy: live URL exercised (curl/Playwright/screenshot) before declaring "done" — never claimed on inspection alone
[ ] Re-render after fixes confirms zero regressions in the same matrix
```

---

*Rule version: global-design-skill v2.2.0 — `rules/20-rendered-verification.md`*
*Related: `references/live-audit-snippets.md` (console + Playwright audits), `checklists/global-design-review.md` (verify-in-every-mode matrix), `blueprints/redesign-existing-page.md` (verify-before-tile), `rules/19-contrast-standards.md` (R14 rendered fill), `rules/16-design-for-seo.md` (no-JS parity), `skills/global-design/quality-gates.md` (Gates 4–7)*
