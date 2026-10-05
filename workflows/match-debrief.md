# Workflow: Match Debrief

## Overview
Post-match analysis that feeds directly into prompt improvements. This is the learning engine — skip it and we fly blind.

## Trigger
After every match (practice or competitive).

## Step 1: Log the Match

Create a new file in `match-log/practice/` or `match-log/competitive/`:

**Filename**: `NNN-vs-<opponent>.md` (e.g., `001-vs-thunder-fc.md`)

Copy `match-log/TEMPLATE.md` and fill in every section. The dashboard parser (`scripts/build-dashboard.py`) relies on its `Score`, `Date`, `Formation`, `Strategy`, `Deploy tag`, `Models`, `Prompt versions deployed` and `- Performance:` lines, and on the Raw Stats, Command Breakdown, Agent Latency and Coach Interventions tables, so keep those formats exactly. Leave a cell empty if the platform does not show that number (e.g. p95). Don't type a guess.

Always fill in **Coach Interventions**: every live message you typed during the match, when you sent it, and what changed afterwards. In match 001 our only goal came right after a live "be aggressive, hit the ball" message, and that was nearly left out of the log.

## Step 2: Analyst Review

The Analyst agent reviews the match log and:
1. Confirms root causes are accurate (traces behavior back to specific prompt rules)
2. Separates symptoms from causes. Example: a low pass count with 18% possession is a possession problem, not a passing-instruction problem.
3. Checks whether a coach intervention changed behavior. If it did, the base prompts were missing that behavior, so add it to the next version.
4. Prioritizes action items by impact
5. Identifies patterns across multiple matches (if previous logs exist)
6. Checks: did changes from last debrief actually fix the issues?

## Step 3: Feed into Prompt Development

For each high-priority action item:
1. Trigger the Prompt Development workflow (`workflows/prompt-development.md`)
2. Pass the match log entry as input to the Writer agent
3. The Writer must reference the match in the prompt's changelog

## Step 4: Update Scouting

If opponent notes are worth saving:
1. Create or update `strategy/opponent-notes/<opponent>.md`
2. Note their formation, tendencies, and exploitable weaknesses

## Tracking Across Matches

After 3+ matches, look for:
- **Recurring failures**: Same position failing the same way → prompt rule is fundamentally wrong, not just needs tweaking
- **Successful patterns**: What's working → protect these rules during revisions
- **Meta-trends**: Are we better attacking or defending? Adjust strategy accordingly
