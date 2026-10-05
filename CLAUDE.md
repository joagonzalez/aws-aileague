# AWS AI League — Agentic Football Cup

## Project Overview
This repo manages prompts, strategy, and match analysis for a 5-agent football team competing in the AWS Agentic Football Cup. Every change is versioned and tagged so we can trace what worked and what didn't.

## Repo Structure

```
prompts/<position>/vN.md   — Versioned prompts (v1, v2, ...)
prompts/<position>/current.md — The active deployed prompt
strategy/                  — Formation, playbook, model selection, opponent scouting
match-log/                 — Post-match analysis (THE feedback loop)
workflows/                 — SDD workflow definitions
specs/                     — Prompt schema and evaluation criteria
dashboard/                 — GitHub Pages experiment tracker (auto-deployed)
scripts/                   — Build scripts (dashboard data generator)
```

## Positions
- `gk` — Goalkeeper
- `def` — Defender
- `mid` — Midfielder
- `fwd1` — Forward 1
- `fwd2` — Forward 2

## Core Workflow: Prompt Development (SDD)

Every prompt change follows the Writer → Reviewer → Evaluator pipeline:

1. **Writer** drafts/revises a prompt following `specs/prompt-schema.md`
2. **Reviewer** validates against schema + `specs/evaluation-criteria.md` → PASS or FAIL (with feedback back to Writer, max 3 iterations)
3. **Evaluator** checks team coherence across all 5 prompts → APPROVE or REJECT (with feedback back to Writer)
4. On APPROVE: update `current.md`, commit, tag, deploy

See `workflows/prompt-development.md` for the full pipeline.

## Match Feedback Loop (Critical)

After every match:
1. Log the result in `match-log/practice/` or `match-log/competitive/`
2. Use `workflows/match-debrief.md` to analyze what happened
3. Feed findings into the Writer agent for the next prompt iteration
4. The match log IS the data — never skip this step

## Git Conventions

- **Tags**: Every deployment gets a tag: `deploy-vN-YYYY-MM-DD` with a message describing what changed
- **Commits**: Descriptive messages linking to match context when applicable
- **Branches**: Use feature branches for experimental prompt strategies, merge to master for deployment
- Log all tags in `tags.md` for quick reference

## Dashboard

A static dashboard is deployed to GitHub Pages on every push to master. It visualizes:
- Match results (W/L/D, scores, timeline)
- Current deployment config (prompt versions + models per position)
- Per-position performance trends
- Action items from debriefs

To rebuild locally: `python3 scripts/build-dashboard.py` then open `dashboard/index.html`.

## Platform Notes

- Agents already know HOW to play (move, pass, shoot, mark, press, intercept, throw, kick)
- Prompts only define WHEN and WHERE to do things — pure tactical instructions
- Plain English works best, no code or coordinates
- Model is configurable per player — see `strategy/model-selection.md`

## Rules to Follow

- Always read `specs/prompt-schema.md` before writing or reviewing a prompt
- Always check `match-log/` for recent lessons before revising a prompt
- Never deploy without running through `workflows/deploy-checklist.md`
- Keep prompts concise — LLM performance degrades with bloat
- Each prompt must follow the schema in `specs/prompt-schema.md` exactly
- When comparing prompt versions, check the changelog section in each version

## Competition Constraints (from AWS)

- Max 10 matches total (Tuesday–Thursday)
- 30-minute cooldown between matches
- No consecutive/repeated matches against same opponent
- Must click "Deploy changes" / "Redeploy changes" for updates to take effect
