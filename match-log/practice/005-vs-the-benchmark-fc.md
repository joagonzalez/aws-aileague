# Match 005: vs The Benchmark FC

## Result
- Score: 0 - 1 (LOSS)
- Date: 2026-10-05
- Type: practice
- Formation: 1-1-2
- Strategy: Counter
- Deploy tag: deploy-v6-2026-10-05
- Prompt versions deployed: GK v6, DEF v6, MID v5, FWD1 v5, FWD2 v5
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Claude Haiku, FWD2 Claude Haiku

## Key Moments
1. 1': Benchmark's FWD (Jay Smooth) scored. Opponent goals at 1' in matches 003, 004 and 005 (5 of their 6 timed goals).
2. Recurring (coach observation): Hertz and Lovelace still ended up in the corners and kept running even with no pitch left, no shooting angle and no pass. They scattered far from their teammates.
3. Coach observation: the forwards have no clear "without the ball" behavior, such as coming back to the center and pressing to win the ball back.
4. Platform Coach's Corner for us: increase SHOOT and position the strikers closer to goal. 12 SHOOTs with nothing on target points to poor finishing, not a lack of chances.

## Coach Interventions
<!-- Not reported. Fill in, or write "None". -->
| When | Message | Observed effect |
|------|---------|-----------------|
| [minute] | [what you typed] | [what changed after it] |

## Raw Stats
- Possession: 39% vs 61%
- Shots: 3 vs 4
- Shots on target: 0 vs 1
- Our commands: 335 total, 814ms avg latency
- Their commands: 335 total, 197ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 128 | 38% |
| Press | 107 | 32% |
| Intercept | 45 | 13% |
| Mark | 0 | 0% |
| Pass | 28 | 8% |
| Shoot | 12 | 4% |
| Clear | 15 | 4% |
| GK Dist | 0 | 0% |

Opponent: Move 205 (61%), Press 91 (27%), Pass 28 (8%), Clear 10 (3%), GK Dist 1 (0%).

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 669ms | | 100% |
| DEF (Turing) | 890ms | | 100% |
| MID (Tesla) | 941ms | | 100% |
| FWD1 (Hertz) | 638ms | | 100% |
| FWD2 (Lovelace) | 893ms | | 100% |

Opponent: GK 214ms, DEF 212ms, MID 212ms, FWD 206ms, FWD 210ms.

## Per-Position Analysis

### GK
- Performance: adequate
- What worked: Conceded once, from their only shot on target. 669ms.
- What failed: The 1' goal, again.
- Root cause: Unknown without the goal sequence. See the minute-1 pattern under Team-Level.

### DEF
- Performance: adequate
- What worked: The defense held after minute 1 (4 shots against, 1 on target). 890ms, down from 1313.
- What failed: Zero MARK commands (34 in 004). v6 rule 6 marks only in specific cases and otherwise sends him to his spot.
- Root cause: v6 traded marking for a fixed spot at the box edge. The net result is better than v5: 1 goal conceded, not 3.

### MID
- Performance: adequate
- What worked: 941ms. Part of 107 presses and 45 intercepts.
- What failed: 39% possession and few links to the forwards (28 passes).
- Root cause: The forwards were scattered and far from him (see below).

### FWD1
- Performance: weak
- What worked: 638ms, fastest agent again.
- What failed: Corner-running continued. 3 team shots, 0 on target.
- Root cause: The v5 rules say the right things (stay in the middle lane, wide exit, no carrying toward a corner), but the behavior contradicts them. The agent probably can't place our pitch geometry ("middle lane", "edge of their box", "in line with the left post", "wide near their end line") in the state it receives, so those rules don't fire. MOVE also keeps running between decisions (~0.65 s here), so carries overshoot to the end line.

### FWD2
- Performance: weak
- What worked: 100% success.
- What failed: Same corner-running and scattering. "NEVER PRESS" leaves him passive when he loses the ball.
- Root cause: Same geometry problem as FWD1. The one-presser rule (only FWD1 presses in their half) stops him trying to win the ball back.

## Team-Level Observations
- Formation effectiveness: 1-1-2 conceded only once (the switch rule needs 2), but scored 0 for the second match in a row.
- Should we change formation? Not yet. The problem is in attack, not numbers at the back.
- Coordination gaps: The forwards scattered far from MID and each other. No passing triangle.
- Results by release: v1 W 1-0, v3 D 2-2, v4 W 2-1, v5 L 0-3, v6 L 0-1. Goals for: 1, 2, 2, 0, 0. With one match per version and Benchmark's own variance, single results are noisy.
- **Minute 1 is our weakest moment**: we conceded at 1' in 003, 004 and 005. Hypothesis: at kickoff our agents are slow to start (the readiness check showed 1.0–1.6 s per call, slower than in-match), so the opponent attacks a standing team. To confirm: does our team stand still for the first seconds?
- Platform Coach's Corner wants SHOOTs and strikers closer to goal. 12 SHOOTs, 0 on target.

## Action Items
- [ ] FWD1/FWD2: Off-ball behavior based on things the agent can see: teammates, the ball, their goal. Stay within a short pass of MID and of each other. When we lose the ball, the closer forward PRESSes to win it back and the other comes back toward the center. (priority: high)
- [ ] FWD1/FWD2: With the ball near their end line or a corner, PASS back to MID or the other forward at once. Never run on. (priority: high)
- [ ] Platform: Get the "What can my agents do?" details: command list and the state/coordinates the agents receive. The geometry-based rules depend on it. (priority: high)
- [ ] Kickoff: Watch the first 10 seconds of the next match. If our players stand still, investigate cold start (Advanced settings, redeploy, readiness check timing). (priority: high)
- [ ] Budget: Test 3000 chars for the forwards to make room for clear off-ball behavior (see the v7 proposal). (priority: medium)

## Opponent Scouting Notes
- Saved to `strategy/opponent-notes/the-benchmark-fc.md`.
