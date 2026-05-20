# Installation Guide

## Claude Code

### Option A: Copy to project (recommended)

```bash
git clone https://github.com/yourusername/global-design-skill.git
cd your-project
bash path/to/global-design-skill/scripts/copy-skill-to-project.sh
```

This copies `skills/global-design/` into `.claude/skills/` and appends the routing block to your `CLAUDE.md`.

### Option B: Global install

```bash
# Copy skill to Claude global skills directory
cp -r skills/global-design ~/.claude/skills/global-design

# Copy agents
cp agents/*.md ~/.claude/agents/

# Add to global CLAUDE.md
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

Or append to existing `.cursorrules`:

```bash
cat integrations/cursor/cursor-rules.md >> your-project/.cursorrules
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

See `integrations/figma/figma-handoff-checklist.md` for the component naming conventions and handoff protocol that pairs with this skill.

---

## Using design tokens

### CSS (copy-paste)

Copy any file from `tokens/*.css` into your project's `globals.css`:

```css
@import "tailwindcss";
@import "./tokens/saas-dark.css";
```

### JSON (for Style Dictionary / Figma Tokens / Token Pipeline)

```bash
# Install Style Dictionary
npm install -D style-dictionary

# Point to token file
# tokens/default-tokens.json → generates CSS, JS, iOS, Android outputs
```

---

## Updating

```bash
git pull origin main

# Re-copy skill files if using Option A
bash scripts/copy-skill-to-project.sh --update
```

---

## Troubleshooting

**"Skill not found"** — Verify `skills/global-design/SKILL.md` exists and is referenced in `CLAUDE.md`.

**Agent not activating** — Check that agent files are in `.claude/agents/` (not a subdirectory).

**Tokens not applying** — Confirm `@import "tailwindcss"` comes before token imports.
