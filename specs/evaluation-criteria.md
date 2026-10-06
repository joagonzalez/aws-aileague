# Evaluation Criteria

Used by the Reviewer and Evaluator agents to assess prompt quality.

## Reviewer Checks (per-prompt)

### Schema Compliance
- [ ] All 7 required sections present (Header, Role, Decision Framework, Personality, Coordination, Constraints, Changelog)
- [ ] Header follows format: `# <Position> — v<N>`
- [ ] Decision Framework is priority-ordered (numbered)
- [ ] Constraints are phrased as prohibitions

### Clarity & Precision
- [ ] No vague language ("try to", "consider", "if possible", "when needed")
- [ ] Every situation in the Decision Framework is concrete and recognizable
- [ ] Every action is unambiguous — only one interpretation possible
- [ ] No contradictions between Decision Framework rules
- [ ] No contradictions between Decision Framework and Constraints
- [ ] No priority shadowing — no higher rule's situation swallows a lower rule so that the lower one can never fire
- [ ] Actions use platform command words (MOVE, PRESS, INTERCEPT, MARK, PASS, SHOOT, CLEAR, distribute)
- [ ] No instructions the agent cannot execute: talking to teammates ("tell", "call for", "signal"), time durations ("for 3 seconds"), or actions with no command ("shield", "wait")

### Conciseness
- [ ] Pasted text within the character budget for its model (`specs/prompt-schema.md` → Quality Guidelines; `scripts/build-paste-ready.py` reports the counts)
- [ ] No redundant rules (same situation covered twice)
- [ ] No filler text or unnecessary elaboration

### Lessons Learned
- [ ] If match-log entries exist for this position, the prompt addresses identified weaknesses
- [ ] Changelog references the match/reason that motivated changes
- [ ] Any coach intervention that clearly helped in a logged match is now part of the base prompt

## Evaluator Checks (team-wide)

### Team Coherence
- [ ] Coordination sections are bidirectionally consistent across all 5 prompts
- [ ] Any risk that could directly cost a goal (space behind the last defender, an unmarked attacker in our half, the ball held in our box) has a guard in the prompts. If not, REJECT (match 004)
- [ ] Exactly one position is responsible for pressing the ball in each zone (their half / midfield / near our box); the others cover
- [ ] No positional gaps — every area of the pitch has coverage
- [ ] No positional overlap — agents don't fight over the same responsibilities
- [ ] Formation described in `strategy/formation.md` is reflected in prompts

### Strategic Alignment
- [ ] Prompts align with the current playbook (`strategy/playbook.md`)
- [ ] Risk profiles are compatible (e.g., aggressive FWDs paired with solid DEF)
- [ ] The team can handle both attacking and defending scenarios

### Regression Prevention
- [ ] Changes don't undo fixes that worked in previous matches
- [ ] If a previous version's decision rule was effective (per match-log), it's preserved or improved, not removed
- [ ] Fixes target causes, not symptoms (e.g., don't add passing rules to fix a low pass count caused by low possession)
- [ ] Command counts are clues, not goals. A change aimed at moving a count (e.g. more GK Dist) must also state the on-pitch outcome it expects. Match 003: the 'distribute' wording lifted GK Dist from 0 to 8 but sent the ball short to DEF instead of upfield

## Scoring (for Reviewer)

Each check is binary (pass/fail). The prompt must pass ALL checks to advance to the Evaluator.

On failure: return the specific failed checks with actionable feedback to the Writer.
