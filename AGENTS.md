# AWS Agentic Football Cup

This repo persists prompts, strategy, and match analysis for the AWS Agentic Football Cup competition.

## Team

| # | Position | Model | Prompt |
|---|----------|-------|--------|
| 1 | GK (Goalkeeper) | Claude Haiku | `prompts/gk/current.md` |
| 2 | DEF (Defender) | Claude Haiku | `prompts/def/current.md` |
| 3 | MID (Midfielder) | Claude Sonnet | `prompts/mid/current.md` |
| 4 | FWD1 (Forward 1) | Claude Haiku | `prompts/fwd1/current.md` |
| 5 | FWD2 (Forward 2) | Nova Lite 2 | `prompts/fwd2/current.md` |

## Repo Structure

- `prompts/` — Versioned player prompts (the core asset)
- `strategy/` — Formation, playbook, model selection, opponent scouting
- `match-log/` — Post-match analysis (the feedback loop)
- `workflows/` — SDD pipelines (Writer -> Reviewer -> Evaluator)
- `specs/` — Prompt schema and evaluation criteria

## Development Workflow (SDD)

Every prompt change goes through a gated pipeline:

```
Writer -> Reviewer (PASS/FAIL) -> Evaluator (APPROVE/REJECT) -> Deploy
```

See `workflows/prompt-development.md` for the full pipeline.

## Match Feedback Loop

After every match:
1. Log result using `match-log/TEMPLATE.md`
2. Analyze per-position performance (trace to specific prompt rules)
3. Feed findings into the Writer for the next prompt iteration

See `workflows/match-debrief.md` for details.

## Competition Rules

- Max 10 matches total (Tuesday-Thursday)
- 30-minute cooldown between matches
- No consecutive/repeated matches against same opponent
- Click “Deploy changes” / “Redeploy changes” for updates to take effect
- Every deployment gets a git tag for traceability

## Degrees of Freedom

1. **Prompt content** — the decision rules, personality, constraints for each agent
2. **Model selection** — speed vs intelligence trade-off per position (see `strategy/model-selection.md`)
3. **Formation/tactics** — how agents coordinate (see `strategy/formation.md`, `strategy/playbook.md`)