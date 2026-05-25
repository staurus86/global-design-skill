#!/usr/bin/env bash
# install.sh — Quick installer for Global Design Skill
#
# Usage:
#   bash scripts/install.sh [OPTIONS] [PROJECT_PATH]
#
# One-liner (after cloning):
#   bash path/to/global-design-skill/scripts/install.sh ~/myproject
#
# Options:
#   --claude-code    Install for Claude Code (skills + agents + CLAUDE.md)
#   --cursor         Install .cursorrules
#   --copilot        Install .github/copilot-instructions.md
#   --windsurf       Install .windsurfrules
#   --mcp            Install MCP server dependencies + .claude/mcp.json
#   --all            Install everything (default when no --* flags given)
#
# Requires: Python 3.11+

set -euo pipefail

GDS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET="${1:-$(pwd)}"
TOOL_ARGS=()

for arg in "$@"; do
    case "$arg" in
        --claude-code) TOOL_ARGS+=(--tool=claude-code) ;;
        --cursor)      TOOL_ARGS+=(--tool=cursor) ;;
        --copilot)     TOOL_ARGS+=(--tool=copilot) ;;
        --windsurf)    TOOL_ARGS+=(--tool=windsurf) ;;
        --mcp)         TOOL_ARGS+=(--tool=mcp) ;;
        --all)         TOOL_ARGS+=(--tool=all) ;;
        --*)           echo "Unknown option: $arg" >&2; exit 1 ;;
        *)             TARGET="$arg" ;;
    esac
done

echo "Global Design Skill — installer"
echo "Repository: $GDS_DIR"
echo "Target:     $TARGET"
echo ""

if ! command -v python3 &>/dev/null; then
    echo "Error: python3 not found. Install Python 3.11+ first." >&2
    exit 1
fi

PYTHON_VERSION=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
PYTHON_MAJOR=$(echo "$PYTHON_VERSION" | cut -d. -f1)
PYTHON_MINOR=$(echo "$PYTHON_VERSION" | cut -d. -f2)

if [ "$PYTHON_MAJOR" -lt 3 ] || { [ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 11 ]; }; then
    echo "Error: Python 3.11+ required (found $PYTHON_VERSION)" >&2
    exit 1
fi

# Delegate to the Python CLI
python3 "$GDS_DIR/scripts/gds" install "${TOOL_ARGS[@]}" "$TARGET"

echo ""
echo "Verify with: python3 $GDS_DIR/scripts/gds doctor $TARGET"
