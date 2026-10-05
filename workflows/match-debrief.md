# Workflow: Match Debrief

## Overview
Post-match analysis that feeds directly into prompt improvements. This is the learning engine — skip it and we fly blind.

## Trigger
After every match (practice or competitive).

## Step 1: Log the Match

Create a new file in `match-log/practice/` or `match-log/competitive/`:

**Filename**: `NNN-vs-<opponent>.md` (e.g., `001-vs-thunder-fc.md`)

**Template**:
```markdown
# Match NNN: vs <Opponent>

## Result
- Score: [us] - [them]
- Date: YYYY-MM-DD
- Type: practice | competitive
- Prompt versions deployed: GK v_, DEF v_, MID v_, FWD1 v_, FWD2 v_

## Key Moments
1. [Minute/event]: [What happened]
2. ...

## Per-Position Analysis

### GK
- Performance: [strong / adequate / weak]
- What worked: [specific behavior observed]
- What failed: [specific behavior observed]
- Root cause: [which prompt rule caused the good/bad behavior, or what was missing]

### DEF
- Performance: [strong / adequate / weak]
- What worked:
- What failed:
- Root cause:

### MID
- Performance: [strong / adequate / weak]
- What worked:
- What failed:
- Root cause:

### FWD1
- Performance: [strong / adequate / weak]
- What worked:
- What failed:
- Root cause:

### FWD2
- Performance: [strong / adequate / weak]
- What worked:
- What failed:
- Root cause:

## Team-Level Observations
- Formation effectiveness: [did agents maintain shape?]
- Coordination gaps: [where did communication/handoffs break?]
- Opponent patterns: [what did the other team do well? any exploitable weaknesses?]

## Action Items
- [ ] Position: [specific change to make] (priority: high/medium/low)
- [ ] Position: [specific change to make]
- [ ] Strategy: [any formation/playbook changes needed]

## Opponent Scouting Notes
[Save to strategy/opponent-notes/<opponent>.md for future reference]
```

## Step 2: Analyst Review

The Analyst agent reviews the match log and:
1. Confirms root causes are accurate (traces behavior back to specific prompt rules)
2. Prioritizes action items by impact
3. Identifies patterns across multiple matches (if previous logs exist)
4. Checks: did changes from last debrief actually fix the issues?

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
