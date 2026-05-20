# Figma Variables Export Guide

> How to export Figma Variables to W3C DTCG-compatible `design-tokens.json` and sync them with `tokens/tokens.css` in your codebase.

---

## The Problem

Figma Variables live in the design file. Your CSS tokens live in code. When a designer changes `--color-accent` in Figma, developers must manually update `tokens.css`. This guide closes that gap.

---

## Token Architecture in Figma

Mirror the same two-layer structure from `tokens/tokens.css`:

### Layer 1 — Primitive collection

Name it `Primitives`. Mode: none (single set of values).

```
Primitives/
  neutral/
    0     → oklch(99% 0.003 258)
    50    → oklch(97% 0.005 258)
    100   → oklch(94% 0.006 258)
    ...
    950   → oklch(10% 0.008 258)
  accent/
    300   → oklch(75% 0.18 258)
    400   → oklch(68% 0.20 258)
    500   → oklch(60% 0.22 258)
    600   → oklch(53% 0.22 258)
    700   → oklch(45% 0.20 258)
  status/
    green-400  → oklch(72% 0.17 145)
    green-500  → oklch(62% 0.19 145)
    yellow-400 → oklch(80% 0.16 85)
    yellow-500 → oklch(72% 0.18 85)
    red-400    → oklch(65% 0.20 22)
    red-500    → oklch(56% 0.22 22)
    blue-400   → oklch(68% 0.18 235)
    blue-500   → oklch(59% 0.20 235)
```

### Layer 2 — Semantic collection

Name it `Semantic`. Modes: `Light` and `Dark`.

```
Semantic/
  color/
    surface      → (Light) Primitives/neutral/0    (Dark) Primitives/neutral/950
    surface-2    → (Light) Primitives/neutral/50   (Dark) Primitives/neutral/900
    surface-3    → (Light) Primitives/neutral/100  (Dark) Primitives/neutral/850
    text/
      primary    → (Light) Primitives/neutral/900  (Dark) Primitives/neutral/50
      secondary  → (Light) Primitives/neutral/600  (Dark) Primitives/neutral/400
      muted      → (Light) Primitives/neutral/400  (Dark) Primitives/neutral/600
      disabled   → (Light) Primitives/neutral/300  (Dark) Primitives/neutral/700
    border       → (Light) Primitives/neutral/200  (Dark) Primitives/neutral/800
    border-strong→ (Light) Primitives/neutral/300  (Dark) Primitives/neutral/700
    accent       → (Light) Primitives/accent/500   (Dark) Primitives/accent/400
    accent-hover → (Light) Primitives/accent/600   (Dark) Primitives/accent/300
    success      → (Light) Primitives/status/green-500  (Dark) Primitives/status/green-400
    warning      → (Light) Primitives/status/yellow-500 (Dark) Primitives/status/yellow-400
    danger       → (Light) Primitives/status/red-500    (Dark) Primitives/status/red-400
    info         → (Light) Primitives/status/blue-500   (Dark) Primitives/status/blue-400
  spacing/
    1  → 4
    2  → 8
    3  → 12
    4  → 16
    5  → 20
    6  → 24
    8  → 32
    10 → 40
    12 → 48
    16 → 64
    20 → 80
    24 → 96
  radius/
    sm   → 4
    md   → 8
    lg   → 12
    xl   → 16
    2xl  → 24
    full → 9999
```

---

## Exporting from Figma

### Option A — Figma Tokens Plugin (recommended for teams)

**Plugin:** [Tokens Studio for Figma](https://www.figma.com/community/plugin/843461159747178978/tokens-studio-for-figma)

1. Install the plugin
2. Open plugin → Settings → **W3C DTCG format** (enable)
3. Sync → Export to JSON
4. Save as `design-tokens.json` in repo root

**W3C DTCG output format:**

```json
{
  "Primitives": {
    "neutral": {
      "0": {
        "$value": "oklch(99% 0.003 258)",
        "$type": "color"
      },
      "950": {
        "$value": "oklch(10% 0.008 258)",
        "$type": "color"
      }
    },
    "accent": {
      "500": {
        "$value": "oklch(60% 0.22 258)",
        "$type": "color"
      }
    }
  },
  "Semantic": {
    "Light": {
      "color": {
        "surface": {
          "$value": "{Primitives.neutral.0}",
          "$type": "color"
        },
        "accent": {
          "$value": "{Primitives.accent.500}",
          "$type": "color"
        }
      }
    },
    "Dark": {
      "color": {
        "surface": {
          "$value": "{Primitives.neutral.950}",
          "$type": "color"
        },
        "accent": {
          "$value": "{Primitives.accent.400}",
          "$type": "color"
        }
      }
    }
  }
}
```

### Option B — Figma REST API (for CI/CD automation)

```bash
# Get variables from Figma REST API
curl -H "X-Figma-Token: $FIGMA_TOKEN" \
  "https://api.figma.com/v1/files/$FILE_ID/variables/local" \
  | jq '.' > figma-variables.json
```

---

## Transforming JSON to CSS

### Using Style Dictionary

```bash
npm install -D style-dictionary
```

```js
// sd.config.js
import StyleDictionary from 'style-dictionary'

export default {
  source: ['design-tokens.json'],
  platforms: {
    css: {
      transformGroup: 'css',
      prefix: 'color',
      buildPath: 'tokens/',
      files: [
        {
          destination: 'tokens-generated.css',
          format: 'css/variables',
          filter: token => token.filePath.includes('Semantic/Light')
        }
      ]
    }
  }
}
```

```bash
npx style-dictionary build --config sd.config.js
```

### Manual transform script (no dependencies)

```js
// scripts/tokens-to-css.js
import fs from 'fs'

const tokens = JSON.parse(fs.readFileSync('design-tokens.json', 'utf-8'))

function resolveName(path) {
  return '--' + path
    .replace(/\./g, '-')
    .replace(/([A-Z])/g, m => '-' + m.toLowerCase())
    .replace(/^-/, '')
    .toLowerCase()
}

function flatten(obj, prefix = '') {
  const result = {}
  for (const [key, value] of Object.entries(obj)) {
    const newKey = prefix ? `${prefix}-${key}` : key
    if (value.$value !== undefined) {
      result[newKey] = value.$value
    } else {
      Object.assign(result, flatten(value, newKey))
    }
  }
  return result
}

const light = flatten(tokens.Semantic.Light)
const dark  = flatten(tokens.Semantic.Dark)

const lightCSS = Object.entries(light)
  .map(([k, v]) => `  --${k.toLowerCase().replace(/_/g, '-')}: ${v};`)
  .join('\n')

const darkCSS = Object.entries(dark)
  .map(([k, v]) => `  --${k.toLowerCase().replace(/_/g, '-')}: ${v};`)
  .join('\n')

fs.writeFileSync('tokens/tokens-light.css', `/* Generated from Figma — do not edit manually */\n:root,\n[data-theme="light"] {\n${lightCSS}\n}\n`)
fs.writeFileSync('tokens/tokens-dark.css', `/* Generated from Figma — do not edit manually */\n[data-theme="dark"] {\n${darkCSS}\n}\n`)

console.log('tokens/tokens-light.css and tokens/tokens-dark.css updated')
```

---

## GitHub Actions — Auto-Sync on Design Change

```yaml
# .github/workflows/sync-tokens.yml
name: Sync Figma Tokens

on:
  workflow_dispatch:
  schedule:
    - cron: '0 9 * * 1'  # Every Monday at 9:00 UTC

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Fetch Figma variables
        env:
          FIGMA_TOKEN: ${{ secrets.FIGMA_TOKEN }}
          FIGMA_FILE_ID: ${{ secrets.FIGMA_FILE_ID }}
        run: |
          curl -s -H "X-Figma-Token: $FIGMA_TOKEN" \
            "https://api.figma.com/v1/files/$FIGMA_FILE_ID/variables/local" \
            > figma-variables.json

      - name: Transform to CSS
        run: node scripts/tokens-to-css.js

      - name: Open PR if changed
        uses: peter-evans/create-pull-request@v6
        with:
          commit-message: "chore: sync design tokens from Figma"
          title: "Design token update from Figma"
          body: "Automated sync from Figma Variables. Review changes before merging."
          branch: "chore/figma-token-sync"
```

---

## Naming Conventions

| Figma Variable name | CSS custom property |
|---|---|
| `Semantic/Light/color/surface` | `--color-surface` |
| `Semantic/Light/color/text/primary` | `--color-text-primary` |
| `Semantic/Light/color/accent` | `--color-accent` |
| `Semantic/Light/spacing/4` | `--space-4` |
| `Semantic/Light/radius/md` | `--radius-md` |

**Figma naming rules:**
- Use `/` as the group separator (becomes `-` in CSS)
- All lowercase, no camelCase in variable names
- Semantic names only in the Semantic collection — no primitive values
- Group by category: `color/`, `spacing/`, `radius/`, `typography/`

---

## Verification

```
[ ] Primitives collection: no modes, raw OKLCH values only
[ ] Semantic collection: Light + Dark modes, references to Primitives
[ ] All component frames use Semantic tokens (not Primitives directly)
[ ] design-tokens.json exports correctly via Tokens Studio
[ ] CSS generation script produces valid --color-* properties
[ ] [data-theme="dark"] toggles all surfaces, text, and accent colors
[ ] No hardcoded hex values anywhere in the Figma file
```

---

*Integration version: global-design-skill v1.0 — `integrations/figma/variables-export-guide.md`*  
*Related: `tokens/tokens.css`, `tokens/tokens-dark.css`, `examples/06-dark-mode-implementation.md`, `rules/04-color.md`*
