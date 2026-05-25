# Evals

Structured test scenarios that verify the skill produces better output than an unaided AI assistant.

## Why evals

Every `trigger-evals.json` scenario shows that the skill activates for the right tasks and stays silent for the wrong ones. Every `output-evals.json` scenario documents what a correct output contains and what it must never contain — making it possible to verify the skill actually changes behavior.

## Files

| File | Purpose |
|---|---|
| `trigger-evals.json` | 15 prompts with `should_trigger: true/false` — tests skill routing |
| `output-evals.json` | 5 full-task scenarios with `required_in_output` and `forbidden_in_output` |
| `golden/` | Reference outputs — what a high-quality response looks like for key tasks |

## How to use trigger evals

Run each prompt through your AI tool with and without `"Use global-design-skill"`. The tool should activate for all `should_trigger: true` cases and stay in base mode for `false` cases.

Acceptable trigger signal: the response cites quality gates, mentions sector-specific rules, or references skill files.

## How to use output evals

For each scenario in `output-evals.json`:
1. Run the prompt with `"Use global-design-skill"` prepended
2. Check that all `required_in_output` terms appear in the response
3. Check that none of `forbidden_in_output` terms appear
4. Verify the listed `gate_checks` are addressed

## Golden outputs

`golden/*.expected.md` files contain reference responses that represent the quality bar. They are not exhaustive — a response that differs from the golden file is not necessarily wrong, but a response that misses `required_in_output` terms is.

## Adding a new eval

1. Add entry to `trigger-evals.json` or `output-evals.json`
2. Optionally add `golden/<scenario-id>.expected.md`
3. Document your expected signal in `notes`
