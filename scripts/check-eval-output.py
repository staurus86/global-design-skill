#!/usr/bin/env python3
"""Check a captured eval response against evals/output-evals.json term lists.

Usage:
    python scripts/check-eval-output.py <eval_id> <response_file>
    python scripts/check-eval-output.py o02 response.md

Deterministic, case-insensitive substring check for `required_in_output`
(all must appear) and `forbidden_in_output` (none may appear). Semantic
`gate_checks` are NOT verified here -- see evals/golden/ for the qualitative
reference per scenario.

Exit code: 0 = pass, 1 = fail, 2 = usage / lookup error.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EVALS = ROOT / "evals" / "output-evals.json"


def main(argv):
    if len(argv) != 3:
        print(__doc__)
        return 2

    eval_id, response_path = argv[1], argv[2]
    scenarios = json.loads(EVALS.read_text(encoding="utf-8"))
    scenario = next((s for s in scenarios if s["id"] == eval_id), None)
    if scenario is None:
        ids = ", ".join(s["id"] for s in scenarios)
        print(f"Unknown eval id '{eval_id}'. Available: {ids}")
        return 2

    text = Path(response_path).read_text(encoding="utf-8").lower()
    required = scenario.get("required_in_output", [])
    forbidden = scenario.get("forbidden_in_output", [])
    missing = [t for t in required if t.lower() not in text]
    present = [t for t in forbidden if t.lower() in text]

    print(f"Eval {eval_id}: {scenario['task']}")
    for t in required:
        print(f"  required  [{'MISSING' if t in missing else 'ok':>7}] {t}")
    for t in forbidden:
        print(f"  forbidden [{'PRESENT' if t in present else 'ok':>7}] {t}")
    gates = scenario.get("gate_checks", [])
    if gates:
        print(f"  gate_checks (verify manually): {gates}")

    passed = not missing and not present
    print("RESULT:", "PASS" if passed else "FAIL")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
