# Installation Guide

Clone the repository first:

```bash
git clone https://github.com/staurus86/global-design-skill.git
```

All paths below are relative to the cloned `global-design-skill/` directory.

---

## One-command install (recommended)

Use the `gds` CLI to install everything in one step:

```bash
# Install for all tools (Claude Code + Cursor + Copilot + Windsurf + MCP)
python scripts/gds install --tool=all /path/to/your-project

# Install for a specific tool only
python scripts/gds install --tool=claude-code /path/to/your-project
python scripts/gds install --tool=cursor /path/to/your-project
python scripts/gds install --tool=mcp /path/to/your-project

# Verify the install
python scripts/gds doctor /path/to/your-project
```

On Linux/Mac you can also use the bash wrapper:

```bash
bash scripts/install.sh /path/to/your-project
```

`gds doctor` runs a 9-point health check: Python version, fastmcp, skills, agents, MCP server syntax, tokens, industry files, MCP config, and line endings.

---

## Manual install

### Claude Code

#### Option A: Per-project install

```bash
# From inside your project
SRC=path/to/global-design-skill
mkdir -p .claude/skills/global-design .claude/agents
cp -r "$SRC/skills/global-design/." .claude/skills/global-design/

# Bundle the resource dirs SKILL.md links to (references/, rules/, patterns/, ...)
# so its relative paths resolve inside the installed skill folder.
for d in references blueprints patterns rules checklists templates agents industries tokens integrations recipes; do
  cp -r "$SRC/$d" .claude/skills/global-design/
done

cp "$SRC"/agents/*.md .claude/agents/

# Append the routing block to your project CLAUDE.md
cat "$SRC/integrations/claude-code/CLAUDE.md" >> CLAUDE.md
```

> The `gds install` command above does the resource bundling for you. Copy the dirs manually only if you are not using the CLI.

#### Option B: Global install

Make the skill available in every project:

```bash
mkdir -p ~/.claude/skills/global-design ~/.claude/agents
cp -r skills/global-design/. ~/.claude/skills/global-design/

# Bundle the resource dirs SKILL.md links to, so its relative paths resolve.
for d in references blueprints patterns rules checklists templates agents industries tokens integrations recipes; do
  cp -r "$d" ~/.claude/skills/global-design/
done

cp agents/*.md ~/.claude/agents/
cat integrations/claude-code/CLAUDE.md >> ~/.claude/CLAUDE.md
```

#### Verify

Open Claude Code and run:

```
Use global-design-skill and describe what you can help with.
```

---

### Cursor

```bash
cp integrations/cursor/cursor-rules.md your-project/.cursorrules
```

Or append to an existing `.cursorrules`:

```bash
cat integrations/cursor/cursor-rules.md >> your-project/.cursorrules
```

---

### Windsurf

```bash
cp integrations/windsurf/rules.md your-project/.windsurfrules
```

---

### GitHub Copilot

```bash
mkdir -p your-project/.github
cp integrations/github-copilot/copilot-instructions.md your-project/.github/copilot-instructions.md
```

---

### MCP Server (optional)

The MCP server gives Claude Code, Cursor, and Windsurf direct access to sector-specific design rules, learning tools, and SEDI intelligence.

**Requirements:** Python 3.11+

```bash
cd mcp-server
pip install -e ".[test]"
python server.py
```

Add to `.claude/mcp.json` in your project (or let `gds install --tool=mcp` do it automatically):

```json
{
  "mcpServers": {
    "GlobalDesignSkill": {
      "command": "python",
      "args": ["/path/to/global-design-skill/mcp-server/server.py"]
    }
  }
}
```

**Safe mode** (no outbound HTTP, static tools only):

```bash
GDS_MCP_SAFE_MODE=1 python mcp-server/server.py
```

See `PRIVACY.md` for what is stored locally and `SECURITY.md` for the full safe-mode reference.

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
git pull origin master
```

Then re-run the copy commands from the relevant section above to refresh the files in your project.

---

## Troubleshooting

**"Skill not found"** — Verify `skills/global-design/SKILL.md` exists and that the routing block from `integrations/claude-code/CLAUDE.md` is present in your `CLAUDE.md`.

**Anti-slop catalog / `references/`, `rules/`, `patterns/` links don't load** — The skill folder is missing its bundled resources. SKILL.md references them with relative paths, so they must sit beside `SKILL.md` inside `.claude/skills/global-design/`. Re-run `gds install --tool=claude-code <project>` (it copies them automatically), or run `gds doctor <project>` to confirm "Skill resources bundled" passes.

**Agent not activating** — Check that agent files are directly in `.claude/agents/` (not a subdirectory).

**Tokens not applying** — Confirm `@import "tailwindcss"` comes before the token imports.
