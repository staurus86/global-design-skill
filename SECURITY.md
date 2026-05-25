# Security Policy

## Scope

This repository contains:
- Markdown design rule files (no secrets, no credentials)
- A Python MCP server that reads local files and makes outbound HTTP requests to reference URLs you provide
- A learning engine that stores data in `~/.global-design-skill/` on your machine

## Reporting a vulnerability

If you find a security issue (e.g. path traversal in MCP tools, unsafe deserialization, robots.txt bypass), please open a GitHub issue or email the maintainer directly before public disclosure.

## What the MCP server does

| Action | Scope |
|---|---|
| Reads files | Only within the `industries/`, `patterns/`, `tokens/`, `rules/` directories |
| HTTP requests | Only to URLs you explicitly pass to `learn_from_reference_tool` |
| Writes files | Only to `~/.global-design-skill/` on your local machine |
| Telemetry | None — no external reporting of any kind |

## Learning tools — HTTP requests

The `learn_from_reference_tool` makes outbound HTTP GET requests to URLs you provide. It:
- Sends `User-Agent: GlobalDesignSkill-Bot/1.0 (Learning/Reference Collection)`
- Reads and respects `robots.txt` before fetching
- Rate-limits to 10 requests/minute
- Never follows redirects to other domains
- Never stores cookies or session data

To run in **static-only mode** (no outbound HTTP):

```bash
GDS_MCP_SAFE_MODE=1 python mcp-server/server.py
```

In safe mode, `learn_from_reference_tool` returns an error instead of fetching.

## Local storage

All learned patterns, weights, and feedback are stored locally at `~/.global-design-skill/`. To delete everything:

```bash
rm -rf ~/.global-design-skill/
```

Or use the MCP tool:
```
GlobalDesignSkill:forget_niche sector=<sector> niche=<niche>
GlobalDesignSkill:reset_weights
```

## Supported Python version

Python 3.11+. Older versions are not tested and may have security issues in dependencies.
