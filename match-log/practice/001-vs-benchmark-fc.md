# Match 001: vs The Benchmark FC

## Result
- Score: 1 - 0 (WIN)
- Date: 2026-10-05
- Type: practice
- Formation: 1-1-2
- Strategy: Possession
- Deploy tag: deploy-v1-2026-10-05
- Prompt versions deployed: GK v1, DEF v1, MID v1, FWD1 v1, FWD2 v1
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Sonnet, FWD1 Claude Haiku, FWD2 Nova Lite 2

## Key Moments
1. Before 2': Coach sent a live message telling the team to be more aggressive and hit the ball (see Coach Interventions). Sent once only.
2. 2': Goal — scored from quick transition after intercepting opponent's aggressive press. Clinical finish. This came right after the coach message and was our only goal.

## Coach Interventions
| When | Message (paraphrased) | Observed effect |
|------|-----------------------|-----------------|
| Before 2' | Be more aggressive and hit the ball | Goal at 2', our only goal. The base prompts had produced nothing until then. Sent only once and never repeated. No further goals for the rest of the match, so the effect may have faded or the opponent adjusted. |

Takeaway: the v1 prompts were too passive on the ball. That aggression must be in the base prompts, not depend on someone typing it mid-match.

## Raw Stats
- Possession: 18% vs 82%
- Shots: 2 vs 7
- Shots on target: 1 vs 0
- Our commands: 334 total, 813ms avg latency
- Their commands: 335 total, 370ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 125 | 37% |
| Press | 124 | 37% |
| Intercept | 48 | 14% |
| Shoot | 14 | 4% |
| Pass | 11 | 3% |
| Clear | 7 | 2% |
| GK Dist | 3 | 1% |
| Mark | 2 | 1% |

## Agent Latency
| Position | Latency | Success |
|----------|---------|---------|
| GK (Shannon) | 682ms | 100% |
| DEF (Turing) | 802ms | 100% |
| MID (Tesla) | 948ms | 100% |
| FWD1 (Hertz) | 678ms | 100% |
| FWD2 (Lovelace) | 840ms | 100% |

## Per-Position Analysis

### GK
- Performance: strong
- What worked: 100% success, held the clean sheet. Distributed 3 times.
- What failed: Nothing critical.
- Root cause: N/A — GK prompt worked well.

### DEF
- Performance: adequate
- What worked: 100% success, 7 clears helped protect the goal.
- What failed: Only 2 marks in the entire match. Opponent had 7 shots.
- Root cause: Prompt has no explicit "MARK the nearest attacker" rule. Decision framework focuses on closing down and clearing, not marking.

### MID
- Performance: weak
- What worked: Intercepts (contributes to 48 team total).
- What failed: Only 11 total team passes — MID is supposed to be the link but barely passed. 948ms latency is the slowest on the team.
- Root cause: Prompt says "play the through-ball immediately" and "hold possession" but doesn't generate enough PASS commands. Also Claude Sonnet at 948ms is too slow for the tempo.

### FWD1
- Performance: strong
- What worked: Scored the winning goal at 2'. Fast (678ms). Part of 14 shoot commands.
- What failed: Only 18% possession means FWDs barely had the ball to work with.
- Root cause: The goal only came after the coach's live "be aggressive, hit the ball" message. The base prompt was not aggressive enough on its own. Also upstream: MID was not feeding the forwards.

### FWD2
- Performance: adequate
- What worked: 100% success rate.
- What failed: 840ms latency is slow for Nova Lite 2. Not clear how many passes/assists were contributed.
- Root cause: May need to test a faster model. Prompt seems OK but wasn't tested much due to low possession.

## Team-Level Observations
- Formation effectiveness: 1-1-2 survived but we were under siege. 82% possession for opponent is dangerous.
- Should we change formation? Consider 2-1-1 (add second DEF) or 1-2-1 (add second MID for possession) to address the imbalance.
- Coordination gaps: MID is not connecting to FWDs — only 11 passes total. The link between defense and attack is broken.
- Opponent patterns: Benchmark FC pressed aggressively (140 press commands, 42%) but couldn't shoot on target. They lacked finishing despite domination.
- Opponent formation: Unknown — but they had fast agents (370ms avg vs our 813ms).
- Re-analysis (post-v2 review): The low pass count is a symptom of 18% possession, not the cause. We cannot out-pass agents that react about 2x faster. Our only goal came from aggression plus a direct strike, right after the coach asked for it.
- Re-analysis: 124 PRESS commands (37%) did not stop 82% opposition possession. Everyone chased the ball instead of one player pressing while the others cut passing lanes. INTERCEPT (48) is what created the goal.
- Re-analysis: 14 SHOOT commands produced only 2 recorded shots. Check whether SHOOT was issued without the ball (wasted commands).
- Re-analysis: Every model was 680–950ms, Haiku included, against the opponent's 370ms. Switching models alone will not close that gap.

## Action Items
- [x] MID: Add explicit PASS and MARK instructions. MID should pass way more. (priority: high) — done in v2
- [x] DEF: Add MARK as a primary action — only 2 marks is dangerous. (priority: high) — done in v2
- [x] MID model: Consider switching from Sonnet to Haiku — 948ms is too slow, costing us tempo. (priority: high) — done in v2
- [x] FWD2 model: Consider switching from Nova Lite 2 to Haiku — 840ms vs 678ms for FWD1. (priority: medium) — done in v2
- [x] ALL: Address passing — 11 passes total is critically low. Every outfield prompt needs more emphasis on passing. (priority: high) — done in v2, partly reversed in v3 (passing must be forward and direct, not possession)
- [ ] ALL: Make the coach's "be aggressive, hit the ball" message the default: shoot on sight near goal, attack loose balls, hit it forward when you win it. (priority: high) — v3
- [ ] ALL: Coordinate pressing: one player presses the ball, the others INTERCEPT lanes or MARK. (priority: high) — v3
- [ ] ALL: Remove instructions agents cannot execute (talking to teammates, "for N seconds", shielding/waiting). (priority: medium) — v3
- [ ] Strategy: Our counter-attack identity works (scored from transition). Make it the default playbook pattern instead of controlled possession. (priority: high) — v3
- [ ] Formation: Keep 1-1-2 for the v3 test so the prompt change is the only variable. Revisit 2-1-1 if we concede. (priority: medium)
- [ ] Coaching: Log every live message with its time and effect in the Coach Interventions section. (priority: medium)

## Opponent Scouting Notes
- The Benchmark FC: aggressive pressing (140 cmds), high possession (82%), but zero shots on target from 7 attempts. Poor finishing. Vulnerable to counter-attacks on turnovers. Fast agents (370ms avg).
- Saved to `strategy/opponent-notes/the-benchmark-fc.md`.
