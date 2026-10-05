# Evaluation Criteria

Used by the Reviewer and Evaluator agents to assess prompt quality.

## Reviewer Checks (per-prompt)

### Schema Compliance
- [ ] All 7 required sections present (Role, Decision Framework, Personality, Coordination, Constraints, Changelog)
- [ ] Header follows format: `# <Position> — v<N>`
- [ ] Decision Framework is priority-ordered (numbered)
- [ ] Constraints are phrased as prohibitions

### Clarity & Precision
- [ ] No vague language ("try to", "consider", "if possible", "when needed")
- [ ] Every situation in the Decision Framework is concrete and recognizable
- [ ] Every action is unambiguous — only one interpretation possible
- [ ] No contradictions between Decision Framework rules
- [ ] No contradictions between Decision Framework and Constraints

### Conciseness
- [ ] Total prompt under 300 words
- [ ] No redundant rules (same situation covered twice)
- [ ] No filler text or unnecessary elaboration

### Lessons Learned
- [ ] If match-log entries exist for this position, the prompt addresses identified weaknesses
- [ ] Changelog references the match/reason that motivated changes

## Evaluator Checks (team-wide)

### Team Coherence
- [ ] Coordination sections are bidirectionally consistent across all 5 prompts
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

## Scoring (for Reviewer)

Each check is binary (pass/fail). The prompt must pass ALL checks to advance to the Evaluator.

On failure: return the specific failed checks with actionable feedback to the Writer.
