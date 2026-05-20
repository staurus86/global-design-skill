# Installation Guide

Clone the repository first:

```bash
git clone https://github.com/staurus86/global-design-skill.git
```

All paths below are relative to the cloned `global-design-skill/` directory.

---

## Claude Code

### Option A: Per-project install

Copy the skill and agents into your project's `.claude/` directory:

```bash
# From inside your project
mkdir -p .claude/skills .claude/agents
cp -r path/to/global-design-skill/skills/global-design .claude/skills/
cp path/to/global-design-skill/agents/*.md .claude/agents/

# Append the routing block to your project CLAUDE.md
cat path/to/global-design-skill/integrations/claude-code/CLAUDE.md >> CLAUDE.md
```

### Option B: Global install

Make the skill available in every project:

```bash
cp -r skills/global-design ~/.claude/skills/global-design
cp agents/*.md ~/.claude/agents/
cat integrations/claude-code/CLAUDE.md >> ~/.claude/CLAUDE.md
```

### Verify

Open Claude Code and run:

```
Use global-design-skill and describe what you can help with.
```

---

## Cursor

```bash
cp integrations/cursor/cursor-rules.md your-project/.cursorrules
```

Or append to an existing `.cursorrules`:

```bash
cat integrations/cursor/cursor-rules.md >> your-project/.cursorrules
```

---

## Windsurf

```bash
cp integrations/windsurf/rules.md your-project/.windsurfrules
```

---

## GitHub Copilot

```bash
mkdir -p your-project/.github
cp integrations/github-copilot/copilot-instructions.md your-project/.github/copilot-instructions.md
```

---

## ChatGPT Custom GPT

1. Go to [ChatGPT](https://chat.openai.com) → Explore GPTs → Create
2. Open `integrations/chatgpt/custom-gpt-instructions.md`
3. Paste the full content into the **Instructions** field
4. Upload key reference files as **Knowledge**:
   - `skills/global-design/SKILL.md`
   - `skills/global-design/task-routing.md`
   - `rules/` (any domain-specific rules)
   - `checklists/global-design-review.md`

---

## Figma integration

See `integrations/figma/figma-handoff-checklist.md` for component naming conventions and the handoff protocol. `integrations/figma/variables-export-guide.md` and `plugin-workflow.md` cover the token export pipeline.

---

## Using design tokens

The token system has three files in `tokens/`:

| File | Purpose |
|---|---|
| `tokens/design-tokens.json` | Source of truth — W3C DTCG format |
| `tokens/tokens.css` | CSS custom properties, light mode |
| `tokens/tokens-dark.css` | Dark mode overrides (`[data-theme="dark"]`) |

### CSS (copy-paste)

Copy the CSS files into your project and import them:

```css
@import "tailwindcss";
@import "./tokens/tokens.css";
@import "./tokens/tokens-dark.css";
```

### JSON (for Style Dictionary / Figma Tokens)

```bash
npm install -D style-dictionary
# Point Style Dictionary at tokens/design-tokens.json
# to generate CSS, JS, iOS, and Android outputs
```

See `tokens/README.md` for the full token reference and tooling setup.

---

## Updating

```bash
cd global-design-skill
git pull origin main
```

Then re-run the copy commands from the relevant section above to refresh the files in your project.

---

## Troubleshooting

**"Skill not found"** — Verify `skills/global-design/SKILL.md` exists and that the routing block from `integrations/claude-code/CLAUDE.md` is present in your `CLAUDE.md`.

**Agent not activating** — Check that agent files are directly in `.claude/agents/` (not a subdirectory).

**Tokens not applying** — Confirm `@import "tailwindcss"` comes before the token imports.
