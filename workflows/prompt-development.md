# Workflow: Prompt Development Pipeline

## Overview
Structured Development Design (SDD) pipeline for creating and revising player prompts. Three agents, gated progression, max 3 revision loops.

## How it runs (automated)
This pipeline is a saved Claude workflow: `.claude/workflows/prompt-development.js`. The roles are subagents in `.claude/agents/` (`prompt-writer`, `prompt-reviewer`, `prompt-evaluator`).

| Mode | Args | What happens |
|------|------|--------------|
| develop | `{mode: "develop", brief, positions?, date}` | Writer drafts `prompts/<pos>/vN.md` → Reviewer → Evaluator (up to 3 rounds) → review records → on APPROVE, promote to `current.md` and regenerate `deploy/paste-ready.md` and the dashboard |
| review | `{mode: "review", positions?, date}` | Audits the deployed `current.md` files and writes review records. Changes no prompts |

Every run writes `prompts/<pos>/reviews/vN.md` with `Reviewer: PASS|FAIL`, `Evaluator: APPROVE|REJECT`, the findings and the iteration history. A Claude Code hook (`.claude/hooks/require-prompt-review.py`) refuses commits that change a `current.md` without an approving record. For manual commits outside Claude, install it as a git pre-commit hook too:

```bash
printf '#!/bin/sh\nexec python3 "$(git rev-parse --show-toplevel)/.claude/hooks/require-prompt-review.py" --git-hook\n' > .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
```

The stages below describe what each agent does.

## Trigger
- New position needs a prompt (first draft)
- Match debrief identifies a position that needs improvement
- Strategic pivot requires prompt changes

## Inputs Required
- **Position**: Which agent (gk, def, mid, fwd1, fwd2)
- **Strategy docs**: `strategy/formation.md` + `strategy/playbook.md`
- **Match feedback** (if revising): Relevant entries from `match-log/`
- **Previous version** (if revising): `prompts/<position>/current.md`
- **Specs**: `specs/prompt-schema.md` + `specs/evaluation-criteria.md`

## Pipeline

### Stage 1: Writer Agent

**Role**: Draft or revise the prompt.

**Instructions**:
1. Read `specs/prompt-schema.md` — follow the schema exactly
2. Read `strategy/formation.md` and `strategy/playbook.md` — align with team strategy
3. If revising: read `prompts/<position>/current.md` and relevant `match-log/` entries
4. If revising: identify specific weaknesses from match feedback
5. Write the new prompt version following the schema
6. Increment version number, update changelog with reason for changes

**Output**: A complete prompt draft as `prompts/<position>/vN.md`

---

### Stage 2: Reviewer Agent

**Role**: Validate the draft against specs. Gatekeeper for quality.

**Instructions**:
1. Read `specs/prompt-schema.md` and `specs/evaluation-criteria.md`
2. Read the Writer's draft
3. Run `python3 scripts/build-paste-ready.py` for the automated checks (sections, character budget, untestable phrases), then go through every remaining Reviewer check in `specs/evaluation-criteria.md` by hand, including priority shadowing
4. If revising: read relevant `match-log/` entries — verify the draft addresses identified issues

**Output**: PASS or FAIL

- **On PASS**: Forward to Evaluator (Stage 3)
- **On FAIL**: Return to Writer with:
  - List of specific failed checks
  - Concrete suggestions for fixing each failure
  - Quote the problematic text from the draft

**Max iterations**: 3 (Writer → Reviewer loops). If still failing after 3, escalate to human for manual review.

---

### Stage 3: Evaluator Agent

**Role**: Assess team-wide coherence. Strategic gatekeeper.

**Instructions**:
1. Read the passed draft
2. Read ALL 5 `prompts/<position>/current.md` files (substituting the new draft for its position)
3. Read `strategy/formation.md` and `strategy/playbook.md`
4. Read recent `match-log/` entries
5. Run through every Evaluator check in `specs/evaluation-criteria.md`

**Output**: APPROVE or REJECT

- **On APPROVE**:
  1. Copy draft to `prompts/<position>/current.md`
  2. Git commit with message: `prompt(<position>): v<N> — <one-line summary>`
  3. Proceed to deploy checklist
- **On REJECT**: Return to Writer with:
  - Which team coherence or strategic checks failed
  - How the draft conflicts with other positions' prompts
  - Suggested fixes

## Flow Diagram

```
             Writer
               |
               v
     +----> Draft vN
     |         |
     |         v
     |      Reviewer
     |      /     \
     |   FAIL    PASS
     |    |        |
     +----+        v
   (max 3)     Evaluator
               /      \
            REJECT   APPROVE
              |        |
              +---->   Deploy
              |
              v
           Writer (with Evaluator feedback)
```
