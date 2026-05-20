# Figma Plugin Workflow

> Recommended plugins and workflows for maintaining design-code consistency. Covers token sync, design handoff, accessibility checking, and component annotation.

---

## Essential Plugin Stack

| Plugin | Purpose | When to use |
|---|---|---|
| **Tokens Studio** | Sync variables to JSON / CSS | Token management and export |
| **Contrast** | WCAG contrast checking | During component design |
| **Figma Measure** | Inspect spacing values | Handoff verification |
| **Iconify** | Consistent icon library | Adding icons without stroke drift |
| **Automator** | Batch token application | Migrating existing files to tokens |

---

## Workflow 1 — Setting Up Tokens Studio

### Initial setup

1. Install [Tokens Studio for Figma](https://www.figma.com/community/plugin/843461159747178978)
2. Open plugin → **Settings**
3. Enable: **W3C DTCG format** (critical for compatibility)
4. Set token source: **local** (JSON in plugin) or **GitHub/GitLab** (for auto-sync)

### Connecting to GitHub

```
Settings → Sync → GitHub
Repository: <your-org>/<your-project>   # the repo where your tokens live
Branch: main
File path: design-tokens.json
Token: [GitHub Personal Access Token with repo scope]
```

After connecting:
- **Push** sends Figma Variables → `design-tokens.json` in repo
- **Pull** fetches repo changes → updates Figma Variables
- Set up webhook or schedule for automatic sync

### Token set structure in plugin

```
Token Sets:
  ├── Primitives    [Always active — never assigned to a mode]
  ├── Semantic/Light [Assigned to Light mode]
  └── Semantic/Dark  [Assigned to Dark mode]
```

**Assign sets to modes:**
Plugin → Token Sets → right-click `Semantic/Light` → Assign to mode: Light  
Plugin → Token Sets → right-click `Semantic/Dark` → Assign to mode: Dark

---

## Workflow 2 — Designing with Tokens

### Applying tokens to components

In Figma:
1. Select a frame or component
2. Open Tokens Studio plugin
3. Click any token to apply it to the selected property

**Or use the native Variables panel (Figma 2024+):**

1. Select layer
2. Fill → click the variable icon (grid icon next to the color picker)
3. Browse → select from `Semantic` collection

### Design rules in Figma (mirror the code rules)

| Property | Allowed sources |
|---|---|
| Fill color | Semantic collection only |
| Stroke color | Semantic collection only |
| Text color | Semantic `color/text/*` |
| Spacing | Semantic `spacing/*` values |
| Corner radius | Semantic `radius/*` values |
| Font size | Typography styles (linked to type tokens) |

**Never:**
- Pick a color from the color picker without assigning a variable
- Use Primitives collection directly in components
- Hardcode spacing as a raw number without a variable

### Enabling dark mode preview in Figma

1. Select the frame → **right panel → Layer** section
2. Under the frame name: **Mode** dropdown → switch to `Dark`
3. All components using Semantic tokens update instantly

---

## Workflow 3 — Accessibility Checking During Design

### Contrast verification

Install [Contrast](https://www.figma.com/community/plugin/748533339900865323/contrast) plugin.

**Check every component before handoff:**

```
Run: Plugins → Contrast → Run check on selection

Targets:
  Text on background:   ≥ 4.5:1 (AA) | ≥ 7:1 (AAA)
  Large text (18px+):   ≥ 3:1 (AA)
  UI components:        ≥ 3:1 (focus indicators, icons, borders)

Check both modes:
  1. Select component → Mode: Light → run check
  2. Select component → Mode: Dark → run check
```

**Common failures:**

| Failure | Fix |
|---|---|
| `text/muted` on `surface` below 3:1 | Replace with `text/secondary` |
| `color/accent` on `surface-3` below 3:1 | Adjust accent L value higher in light mode |
| White text on `color/warning` (yellow) | Use dark text on yellow — yellow is light |
| Ghost button border below 3:1 | Strengthen `color/border-strong` token |

### Touch target checking

All interactive components must be ≥ 44×44px:

1. Select component
2. Check W and H in right panel
3. If smaller, add invisible padding or increase component size

Annotation shortcut: use a 44×44px rectangle with dashed stroke as an overlay to mark the tap target boundary in handoff specs.

---

## Workflow 4 — Handoff Annotation

Add these annotations before sharing with developers:

### Component states annotation

For each interactive component, include a frame showing all states:

```
States frame structure:
  [Default] [Hover] [Active] [Focus] [Disabled] [Loading/Error]

Label each state using the Text style: Annotation/Label
Use the annotation color: Semantic/color/info
```

### Spacing annotation

Use **Figma Measure** plugin to generate redline spacing annotations:

1. Select two elements
2. Plugins → Figma Measure → Show spacing
3. Values should match token names (8, 12, 16, 24, 32, 48...)

If a spacing value doesn't match a token, it's a design error — adjust before handoff.

### Component spec template

Create a spec frame for each new component:

```
Component Spec — [ComponentName]
─────────────────────────────────
States:
  [Frame with all states]

Tokens used:
  Background:  color/surface-2
  Text:        color/text-primary
  Border:      color/border
  Accent:      color/accent

Spacing:
  Padding: space-3 / space-4 (12px / 16px)
  Gap: space-2 (8px)

Accessibility:
  Min height: 44px
  Focus: visible ring (color/border-focus, 2px offset)
  ARIA: role="button", aria-label if icon-only

Notes:
  [Any non-obvious behavior or edge cases]
```

---

## Workflow 5 — Design Handoff Gate

Before marking a design as ready for development, run this checklist:

```
[ ] All colors from Semantic variables (no raw hex in fills/strokes)
[ ] All spacing from spacing/* variables (no arbitrary numbers)
[ ] All corner radii from radius/* variables
[ ] All interactive components have all required states
[ ] Contrast ≥ 4.5:1 for text, ≥ 3:1 for UI in both Light and Dark modes
[ ] All touch targets ≥ 44×44px
[ ] Icons: 1.5px stroke weight, currentColor (will be set in code)
[ ] No placeholder data (no "Lorem ipsum", "John Doe", fake stats)
[ ] Component spec frames completed for all new components
[ ] Figma Variables pushed to repo via Tokens Studio
```

---

## Workflow 6 — Keeping Figma and Code in Sync

### After code changes

If a developer needs to change a token value in CSS (e.g., accent color adjustment):

1. Developer updates `tokens.css` → opens PR
2. PR description notes token changes
3. Designer updates Figma Variables to match
4. Both merge together

### After design changes

If designer changes a token in Figma:

1. In Tokens Studio: Push → pushes `design-tokens.json` to branch
2. Developer runs transform script: `node scripts/tokens-to-css.js`
3. PR opened with CSS changes for review

### Divergence check

Run monthly: compare Figma primitive values to `tokens.css` primitives.

```bash
# Quick diff command
grep "primitive-accent-500" tokens/tokens.css
# vs Figma's Primitives/accent/500 value
```

If they diverge, always treat CSS as source of truth for production (Figma may have experimental changes that didn't ship).

---

*Integration version: global-design-skill v1.0 — `integrations/figma/plugin-workflow.md`*  
*Related: `integrations/figma/variables-export-guide.md`, `tokens/tokens.css`, `rules/04-color.md`, `rules/07-accessibility.md`*
