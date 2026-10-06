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

Every prompt change runs the saved Claude workflow **`prompt-development`** (`.claude/workflows/prompt-development.js`). Never hand-edit `prompts/*/vN.md` or `current.md` outside it.

- **Change prompts:** `Workflow({scriptPath: "/home/delfox/dev/aws-aileague/.claude/workflows/prompt-development.js", args: {mode: "develop", brief: "<what to change and why, citing the match>", positions: ["mid"], date: "YYYY-MM-DD"}})`. Use `scriptPath`, not `name`: calling it by name runs the version loaded when the session started and silently ignores edits made since (this happened on 2026-10-05). `positions` is optional; without it the Writer decides from the brief and the match logs.
- **Audit the deployed prompts:** `args: {mode: "review", date: "YYYY-MM-DD"}`.
- **Stages:** `prompt-writer` drafts `vN.md` → `prompt-reviewer` (PASS/FAIL, up to 3 rounds with the Writer) → `prompt-evaluator` (APPROVE/REJECT) → a review record per position in `prompts/<pos>/reviews/vN.md`. On APPROVE the draft is copied to `current.md` and the paste file and dashboard are regenerated. Role definitions live in `.claude/agents/`; Reviewer and Evaluator are read-only and never see the Writer's reasoning.
- **After it returns:** show the coach the summary and verdicts. Then commit the drafts, `current.md` and the review records together, and tag `deploy-vN-YYYY-MM-DD`. If not approved after 3 rounds, escalate to the coach.
- **Commit gate:** a PreToolUse hook (`.claude/hooks/require-prompt-review.py`) blocks any `git commit` that changes a `current.md` unless that version has a review record with `Reviewer: PASS` and `Evaluator: APPROVE`.
- If you are an agent running inside the workflow, do only your own stage. **Workflow agents never run git** (no add, commit, tag or push). Committing, tagging and pushing belong to the main session, after it has checked the result (on 2026-10-05 the release clerk committed and pushed v8 on its own).

See `workflows/prompt-development.md` for the full pipeline.

## Match Feedback Loop (Critical)

After every match:
1. Log the result in `match-log/practice/` or `match-log/competitive/` (including live coach messages)
2. Use `workflows/match-debrief.md` to analyze what happened
3. Feed findings into the Writer agent for the next prompt iteration
4. The match log IS the data — never skip this step

## Git Conventions

- **Tags**: Every commit that introduces a new prompt release gets an annotated tag `deploy-vN-YYYY-MM-DD` (N = team prompt release), even if it is never played. The message says what changed. Push with `--follow-tags`
- **Commits**: Descriptive messages linking to match context when applicable
- **Branches**: Use feature branches for experimental prompt strategies, merge to master for deployment
- Log all tags in `tags.md` for quick reference, including which matches each release played in

## Dashboard

A static dashboard is deployed to GitHub Pages on every push to master. It visualizes:
- Match results (W/L/D, scores, timeline)
- Current deployment config (prompt versions + models per position)
- Per-match metric trends: goals, possession, shots, shots on target, latency (avg/p95 vs opponent), command success, ball-winning and on-ball command counts. Hovering a match shows models, prompt versions, strategy, formation, deploy tag and coach messages
- Agent latency heatmap (agent × match) and a table view of every metric
- Per-position performance trends
- Action items from debriefs

To rebuild locally: `python3 scripts/build-dashboard.py` then open `dashboard/index.html`.

## Platform Notes

- Agents already know HOW to play (move, pass, shoot, mark, press, intercept, throw, kick)
- Official platform text ("What can my agents do?"): "You just describe the tactics — your agents already know how to move, pass, shoot, mark opponents, press the ball, intercept, and (for the goalkeeper) throw or kick the ball out. Tell them WHEN and WHERE to do these things. They play on a pitch where your team attacks toward the opponent's goal. You don't need to write any code or coordinates — plain instructions work best."
- Per-agent issues are real: Lovelace (FWD2 slot) was erratic regardless of prompt or model (swap test, match 013). If a player misbehaves with a prompt that works for another agent, suspect the agent, not the prompt.
- Command names seen in match reports: MOVE_TO, PRESS_BALL, INTERCEPT, MARK, FOLLOW_PLAYER, PASS, SHOOT, CLEAR, GK_DISTRIBUTE, SET_STANCE (platform advice: 'lock shape between transitions'; semantics unknown). FOLLOW_PLAYER is probably how "mark opponents" works, not a way to follow a teammate. Unconfirmed.
- Prompts only define WHEN and WHERE to do things — pure tactical instructions
- Plain English works best, no code or coordinates
- Model is configurable per player — see `strategy/model-selection.md`
- Agents cannot talk to each other. Coordination is positional only (no "tell", "call for", "signal")
- The coach can type live messages during a match, and they change behavior. Log every one in the match log's Coach Interventions section. If one works, write it into the next prompt version

## Rules to Follow

- Always read `specs/prompt-schema.md` before writing or reviewing a prompt
- Always check `match-log/` for recent lessons before revising a prompt
- Never deploy without running through `workflows/deploy-checklist.md`
- Keep prompts concise — LLM performance degrades with bloat
- Each prompt must follow the schema in `specs/prompt-schema.md` exactly
- When comparing prompt versions, check the changelog section in each version

## Competition Constraints (from AWS)

- Max 10 competitive matches total (Tuesday–Thursday)
- 30 practice matches against 3 AI teams: The Benchmark FC (balanced), Total Attack United (high press, numbers forward), Fort Knox Athletic (compact, counter-attacking). Scouting notes in `strategy/opponent-notes/`
- 30-minute cooldown between matches
- No consecutive/repeated matches against same opponent
- Must click "Deploy changes" / "Redeploy changes" for updates to take effect
