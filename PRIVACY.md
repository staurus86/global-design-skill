# Privacy Policy

## Summary

Global Design Skill collects no telemetry. No data leaves your machine unless you explicitly ask it to fetch a URL.

## What is stored locally

When you use the learning tools or SEDI feedback, the following is written to `~/.global-design-skill/`:

| Directory | Contents | Example |
|---|---|---|
| `knowledge/` | Extracted patterns from reference sites you provided | `tech-saas__developer-tools.json` |
| `weights/` | Pattern weight adjustments based on your feedback | `tech-saas.json` |
| `feedback/` | Interaction ratings and revision counts | `tech-saas__developer-tools.json` |
| `evolution_log/` | Weekly accuracy snapshots | `20260525T120000_baseline.json` |
| `metrics/` | Aggregated accuracy metrics | `improvement_rate.json` |

**None of this is transmitted anywhere.** No analytics, no crash reporting, no usage metrics.

## What makes outbound HTTP requests

Only the `learn_from_reference_tool` MCP tool, and only when you call it with an explicit URL.

The tool:
1. Checks `robots.txt` on the target domain — if disallowed, refuses to fetch
2. Sends a single GET request with `User-Agent: GlobalDesignSkill-Bot/1.0 (Learning/Reference Collection)`
3. Extracts layout/component/trust patterns from HTML
4. Saves extracted patterns to your local `~/.global-design-skill/knowledge/`

No credentials, cookies, or authentication data are ever sent or stored.

## How to delete your data

```bash
# Delete all learned data
rm -rf ~/.global-design-skill/

# Delete a specific niche (via MCP)
GlobalDesignSkill:forget_niche sector=tech-saas niche=developer-tools

# Reset pattern weights (via MCP)
GlobalDesignSkill:reset_weights
```

## Disabling learning entirely

Set the environment variable before starting the server:

```bash
GDS_MCP_SAFE_MODE=1 python mcp-server/server.py
```

In safe mode, all learning tools (`learn_from_reference`, `get_or_learn_sector`) return an error. Only the 5 static tools remain active.
