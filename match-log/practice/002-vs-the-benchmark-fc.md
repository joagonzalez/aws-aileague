# Match 002: vs The Benchmark FC

## Result
- Score: 2 - 2 (DRAW)
- Date: 2026-10-05
- Type: practice
- Formation: 1-1-2
- Strategy: Counter
- Deploy tag: deploy-v3-2026-10-05
- Prompt versions deployed: GK v3, DEF v3, MID v3, FWD1 v3, FWD2 v3
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Sonnet, FWD1 Claude Haiku, FWD2 Claude Haiku

## Key Moments
1. Conceded goal 1: a long shot from almost the halfway line. Our players were spread out toward the corners and flanks, so the shooter was completely free in the middle of the pitch. The other three goals were not described.
1b. Deployment slip: MID was still on Claude Sonnet (v1 setting) instead of Haiku as v3 specifies. Only MID was missed. MID's 1050ms is a Sonnet number.
2. Recurring (coach observation): forwards carried the ball straight toward the corner flag and did not change direction to pass or shoot.
3. Recurring (coach observation): MID had several direct shooting chances and passed every time.
4. Platform "Coach's Corner" for us: increase SHOOT beyond 37 commands. Pressing generated chances, but finishing was underused relative to ball recovery.

## Coach Interventions
<!-- Not reported yet. Fill in, or write "None". -->
| When | Message | Observed effect |
|------|---------|-----------------|
| [minute] | [what you typed] | [what changed after it] |

## Raw Stats
<!-- The platform report for this match did not include possession or shots. -->
- Possession: [us]% vs [them]%
- Shots: [us] vs [them]
- Shots on target: [us] vs [them]
- Our commands: 725 total, 863ms avg latency
- Their commands: 725 total, 199ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 286 | 39% |
| Press | 218 | 30% |
| Intercept | 106 | 15% |
| Mark | 10 | 1% |
| Pass | 40 | 6% |
| Shoot | 37 | 5% |
| Clear | 28 | 4% |
| GK Dist | 0 | 0% |

Opponent: Move 374 (52%), Press 289 (40%), Pass 42 (6%), Clear 20 (3%). No intercepts or marks.

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 707ms | | 100% |
| DEF (Turing) | 1020ms | | 100% |
| MID (Tesla) | 1050ms | | 100% |
| FWD1 (Hertz) | 713ms | | 100% |
| FWD2 (Lovelace) | 999ms | | 100% |

Opponent: GK 196ms, DEF 206ms, MID 200ms, FWD 207ms, FWD 200ms (all 100%).

## Per-Position Analysis

### GK
- Performance: adequate
- What worked: 100% success, 707ms (among our fastest).
- What failed: 2 goals conceded. One was a long shot from near the halfway line, which a goalkeeper on the line should usually stop. Zero GK Dist commands. The 725-command total adds up without them, so the GK never distributed through that command.
- Root cause: Long shot: v3 rule 6 puts GK 'a few steps off the goal line' when the ball is in their half, and the next decision lands ~0.7 s late. GK must recover to the line as soon as an opponent can shoot. v3 rule 2 (rush out at a 1v1) contradicts the constraint "NEVER leave the box" (flagged by the v3 audit).

### DEF
- Performance: weak
- What worked: 100% success, some clears (28 team total).
- What failed: 1020ms, the slowest Haiku agent. Conceded 2. On the first one our players were spread out toward the corners and nobody guarded the middle, so a shooter near the halfway line was unmarked. Only 10 MARK commands team-wide.
- Root cause: Rule 2 sends DEF to PRESS any ball carrier near our box and 'force them wide', so DEF follows the ball into the channels. MID presses or pushes up and the forwards stay high, so nobody is told to hold the central lane. The constraint 'never leave the center in front of goal empty' loses to rule 2, and the v3 audit flagged that contradiction. Latency: DEF acts on a picture of the pitch about 1 s old against attackers at 200ms.

### MID
- Performance: weak
- What worked: Part of 106 intercepts and 40 passes (double match 001's share).
- What failed: Passed instead of shooting on direct chances (coach observation). Slowest agent at 1050ms, but it ran on Sonnet by mistake, not Haiku.
- Root cause: v3 rule 1 only shoots "near the opponent's box", which is too narrow for a midfielder who usually arrives at the edge of the attacking third. Rule 2 ("FWD unmarked ahead → PASS") almost always matches first.

### FWD1
- Performance: adequate
- What worked: 713ms. Team scored 2 (scorers unknown). Team SHOOT commands rose from 14 to 37.
- What failed: Ran straight toward the corner with the ball and did not turn to pass or shoot (coach observation).
- Root cause: v3 rule 4 "Run at goal with it until you are in shooting range" has no exit when the carry drifts wide toward the end line. Each decision also takes 0.7–1 s, so a carry keeps going a long way before the next command.

### FWD2
- Performance: adequate
- What worked: 100% success.
- What failed: Same corner-running pattern as FWD1. 999ms, much slower than FWD1 on the same model.
- Root cause: v3 rule 4 (run at goal until a defender commits) has the same missing exit for wide positions.

## Team-Level Observations
- Formation effectiveness: 1-1-2 scored twice (up from 1) but conceded twice (up from 0). The opponent was much faster this time: 199ms vs 370ms in match 001.
- Should we change formation? Not yet. The first goal conceded is a shape problem (players spread to the flanks and the middle left open), which prompt rules can fix. If v4 still concedes through the middle, test 2-1-1.
- Coordination gaps: v3 audit found two pressers in the opponent's half (FWD1 always presses; FWD2 also presses when closer).
- Opponent patterns: Even more press-heavy (289, 40%), no intercepts or marks, 6% passes. Platform advice to them: add INTERCEPT to cover transition gaps. Their transitions are where we can hurt them.
- Opponent formation: Unknown.
- Latency: Both teams issued exactly 725 commands (334 vs 335 in match 001), so the platform polls both teams at the same rate. Our slower agents don't get fewer decisions; each decision acts on an older picture of the pitch (~0.86 s vs ~0.2 s). That fits the forwards over-running to the corner.
- Tempo line ("keep any reasoning to a few words"): no measurable effect. Our average went 813 → 863ms while the opponent went 370 → 199ms, so platform-side variance exists too. It isn't the coach's internet connection: agents run server-side on AWS, and the opponent was measured at ~200ms in the same match.
- Same model, very different speeds: Haiku agents ran 707–713ms (GK, FWD1) and 999–1020ms (DEF, FWD2). MID's 1050ms was Sonnet. FWD2 on Haiku (999ms) was slower than on Nova Lite 2 in match 001 (840ms). The slower ones handle more complex situations, so most likely they write more per decision.
- Command mix vs match 001: SHOOT 14 → 37, PRESS share 37% → 30%, PASS 3% → 6%, INTERCEPT 14% → 15%, MARK 1% → 1%.

## Action Items
- [ ] FWD1/FWD2: Add an exit for wide carries. Near the end line or corner, SHOOT if there is an angle, otherwise PASS to the middle. Carry toward the middle of the goal, never along the touchline. (priority: high)
- [ ] MID: Widen the shooting trigger to the whole attacking third with no defender directly between ball and goal, and put it before the pass rule. (priority: high)
- [ ] ALL attackers: Raise SHOOT frequency (platform Coach's Corner). (priority: high)
- [ ] FWD1/FWD2: Fix the double press in the opponent's half (v3 audit). (priority: high)
- [ ] GK: Resolve the rush-out vs never-leave-the-box contradiction (v3 audit). Check why there were zero GK Dist commands. (priority: medium)
- [ ] Models: Latency is now the biggest gap (863 vs 199ms) and prompt wording didn't move it. Test Nova Micro on one of the slow Haiku positions (DEF 1020, MID 1050, FWD2 999) in practice. (priority: high)
- [ ] ALL: Central protection. One player always holds the middle in front of our goal when the opponent has the ball; nobody follows the ball into the corners except the single presser for that zone. (priority: high)
- [ ] GK: Get back to the goal line as soon as an opponent has the ball in a position to shoot, including long range. (priority: high)
- [ ] Deploy: Check every model dropdown against the prompt headers before Redeploy (MID was left on Sonnet). (priority: high)
- [ ] Debrief: Record how the other 3 goals happened and any coach messages. (priority: medium)

## Opponent Scouting Notes
- Saved to `strategy/opponent-notes/the-benchmark-fc.md`.
