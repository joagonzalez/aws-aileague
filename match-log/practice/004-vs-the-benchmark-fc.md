# Match 004: vs The Benchmark FC

## Result
- Score: 0 - 3 (LOSS)
- Date: 2026-10-05
- Type: practice
- Formation: 1-1-2
- Strategy: Counter
- Deploy tag: deploy-v5-2026-10-05
- Prompt versions deployed: GK v5, DEF v5, MID v4, FWD1 v4, FWD2 v4
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Claude Haiku, FWD2 Claude Haiku

## Key Moments
1. 1': Benchmark scored three times, all within the first minute: their FWD (Jay Smooth) twice and their DEF (Norm Easy) once. The match was decided before our agents had made more than a handful of decisions.
2. Recurring (coach observation): Hertz and Lovelace drifted toward the corners. Few clear shots, and chances went unused.
3. Recurring (coach observation): Turing held the ball in our own box without clearing, even when no one was near him, and that risked goals.
4. Platform Coach's Corner for us: increase PASS + GK Dist from 17 to 40+, to turn possession into threatening sequences instead of aimless movement (MOVE was 45%).

## Coach Interventions
<!-- Not reported yet: were the suggested live messages (forwards central / Turing clear) sent? Fill in, or write "None". -->
| When | Message | Observed effect |
|------|---------|-----------------|
| [minute] | [what you typed] | [what changed after it] |

## Raw Stats
- Possession: 60% vs 40%
- Shots: 3 vs 8
- Shots on target: 0 vs 3
- Our commands: 374 total, 952ms avg latency
- Their commands: 390 total, 203ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 167 | 45% |
| Press | 72 | 19% |
| Intercept | 35 | 9% |
| Mark | 34 | 9% |
| Pass | 15 | 4% |
| Shoot | 28 | 7% |
| Clear | 21 | 6% |
| GK Dist | 2 | 1% |

Opponent: Move 227 (58%), Press 132 (34%), Pass 16 (4%), Clear 12 (3%), GK Dist 3 (1%). Still no MARK or INTERCEPT.

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 620ms | | 100% |
| DEF (Turing) | 1313ms | | 100% |
| MID (Tesla) | 1024ms | | 100% |
| FWD1 (Hertz) | 654ms | | 100% |
| FWD2 (Lovelace) | 997ms | | 100% |

Opponent: GK 216ms, DEF 202ms, MID 201ms, FWD 209ms, FWD 198ms. Platform MVP and fastest player: their FWD (Kim Poise, 198ms).

## Per-Position Analysis

### GK
- Performance: weak
- What worked: 620ms (fastest again). GK Dist back to ~0 and clears used, as v5 intended.
- What failed: 3 conceded in the first minute, 3 of 8 shots on target.
- Root cause: Mostly the defensive line in front of him (see DEF). We don't know yet whether any goal was a GK positioning error.

### DEF
- Performance: weak
- What worked: MARK rose from 1 to 34 (v5 rule 6 now fires).
- What failed: Held the ball in our box without clearing (coach observation). 1313ms, his slowest yet. Their FWD scored twice in the first minute.
- Root cause: (1) v5 moved his default spot up to midway between our box and halfway. The v5 Evaluator flagged the space behind that spot as the main risk ("only MID contests a pass in behind; the opponent reacts 4x faster"), and their striker scored twice. We shipped a known risk without a guard. (2) Holding the ball in the box: rule 1 says CLEAR, but rule 3 ("ball loose in our box and you're closer than GK → INTERCEPT") probably catches a ball at his feet that the platform reports as loose, so he keeps intercepting instead of clearing. At ~1.3 s per decision, two wasted decisions are enough for an attacker to arrive.

### MID
- Performance: adequate
- What worked: Part of 34 MARKs and 35 intercepts.
- What failed: 1024ms. Possession (60%) did not turn into chances.
- Root cause: Unchanged v4 prompt. The problem was further up (forwards wide) and behind (DEF).

### FWD1
- Performance: weak
- What worked: 654ms.
- What failed: Drifted toward the corners. 3 team shots, 0 on target. SHOOT commands produced few real shots (28 commands, 3 shots).
- Root cause: v4 keeps the forwards central only when they have the ball (wide exit, no carrying to the corner). Off the ball, rule 6 "MOVE into open space toward their box" follows the open space, which is on the flanks against a compact defense. Rule 7 presses any carrier in their half, dragging FWD1 to the touchline. Rule 5 chases loose balls wherever our long clears land.

### FWD2
- Performance: weak
- What worked: 100% success.
- What failed: Same drift to the corners. 997ms.
- Root cause: Same rule 6 as FWD1.

## Team-Level Observations
- Formation effectiveness: The 1-1-2 switch rule ("concede 2 or more") formally triggers. But the only change from the 2-1 win in match 003 was the v5 GK/DEF prompts, and the failure matches the risk the Evaluator predicted for DEF's new spot. Fix that first. If the next version still concedes 2 or more, move to 2-1-1.
- Should we change formation? Not before testing whether DEF's v4 depth plus v5's ball release fixes it.
- Coordination gaps: Possession without penetration: 60% possession, MOVE 45%, 3 shots. Forwards wide, so no central options.
- Opponent patterns: Their DEF scored again (DEF goals in 003 and 004 were Norm Easy). Their FWDs are fast (198ms) and finish early.
- **Matches are short.** Commands per agent per match: ~67 (001), ~145 (002), ~102 (003), ~75 (004). Across 001, 003 and 004, five of the six goals with a recorded minute came in minute 1 or 2. The opening minute decides matches, and each of our agents gets only a handful of decisions in it.
- **For the first time, the command counts differ** (374 vs 390). Our slowest agents seem to miss decision slots when their latency is very high (DEF 1313ms).
- **Part of the latency belongs to the agent, not the prompt or model.** Hertz and Lovelace run the same model with prompts of nearly identical length (1967 vs 1983 chars). Yet Hertz is consistently ~300ms faster: 713 vs 999, 678 vs 980, 654 vs 997 (and 1060 vs 1380 in the readiness check). Turing is the slowest in every measurement. This points to how each agent is deployed on the platform or in the AWS account.
- **SHOOT commands rarely become shots**: 14→2 (001), 20→3 (003), 28→3 (004). The likely cause is latency: by the time the command arrives (~1 s), a 200ms opponent has closed the player down or taken the ball. Releasing earlier (first-time shots, no carrying) is the prompt-level lever.

## Action Items
- [ ] DEF: Go back to v4's depth: one fixed spot at the edge of our box in the middle lane, without v4's moving ball-to-goal line. Keep v5's release rules (never pass to GK, never move with the ball). (priority: high)
- [ ] DEF: Ball at his feet or loose within reach in our box → CLEAR long immediately, never wait. Merge rule 3 into rule 1. (priority: high)
- [ ] FWD1/FWD2: Stay inside the middle lane (between the posts) off the ball. Only one forward goes wide, and only for the ball. FWD1 presses only middle-lane carriers. (priority: high)
- [ ] FWD1/FWD2: Release faster. In the attacking third, shoot or pass straight away instead of carrying. (priority: high)
- [ ] GK: Clear toward the middle of their half, where the central forwards now wait. (priority: medium)
- [ ] Process: When the Evaluator names a main risk for a defensive change, add a guard for it, or test it in practice before counting on it. (priority: high)
- [ ] Platform: Compare Turing's and Lovelace's settings with Hertz's in "Advanced". Try redeploying the two slow agents. (priority: high)

## Opponent Scouting Notes
- Saved to `strategy/opponent-notes/the-benchmark-fc.md`.
