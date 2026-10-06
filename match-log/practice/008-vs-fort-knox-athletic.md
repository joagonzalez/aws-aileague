# Match 008: vs Fort Knox Athletic

## Result
- Score: 0 - 1 (LOSS)
- Date: 2026-10-05
- Type: practice
- Formation: 1-1-2
- Strategy: Counter
- Deploy tag: deploy-v7-2026-10-05
- Prompt versions deployed: GK v7, DEF v7, MID v6, FWD1 v6, FWD2 v6
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Claude Haiku, FWD2 Claude Haiku

## Key Moments
1. 3': Fort Knox scored (scorer unknown) from their only shot on target.
2. We had 4 shots (0 on target) without a single SHOOT command. Clears/passes toward goal seem to count as shots.
3. MARK was 41% of our commands (184): a passive team marking a possession side.
4. Recurring (coach): forwards in the corners, no passes, no angles.

## Coach Interventions
<!-- Not reported. Fill in, or write "None". -->
| When | Message | Observed effect |
|------|---------|-----------------|
| [minute] | [what you typed] | [what changed after it] |

## Raw Stats
- Possession: 43% vs 57%
- Shots: 4 vs 1
- Shots on target: 0 vs 1
- Our commands: 445 total, 884ms avg latency
- Their commands: 445 total, 193ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 87 | 20% |
| Press | 21 | 5% |
| Intercept | 75 | 17% |
| Mark | 184 | 41% |
| Pass | 52 | 12% |
| Shoot | 0 | 0% |
| Clear | 13 | 3% |
| GK Dist | 13 | 3% |

Opponent: Move 272 (61%), Press 120 (27%), Pass 36 (8%), GK Dist 13 (3%), Clear 4 (1%).

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 644ms | | 100% |
| DEF (Turing) | 1067ms | | 100% |
| MID (Tesla) | 965ms | | 100% |
| FWD1 (Hertz) | 671ms | | 100% |
| FWD2 (Lovelace) | 985ms | | 100% |

Opponent: all 193–203ms. MVP and fastest player: their FWD (Sam Hedge, 197ms).

## Per-Position Analysis
### GK
- Performance: adequate
- What worked: Conceded 1 from 1 shot on target. 644ms.
- What failed: The goal (sequence unknown).
- Root cause: Unknown.

### DEF
- Performance: adequate
- What worked: Defense restricted Fort Knox to 1 shot.
- What failed: 1067ms, slowest again. A big share of the 184 MARKs.
- Root cause: v7 rule 6 MARKs whenever the opponent has the ball in our half, and Fort Knox keeps it there.

### MID
- Performance: adequate
- What worked: 52 passes, the most in any match.
- What failed: No shots.
- Root cause: The marking rules dominate when the opponent has possession. The forwards are too far away to combine with.

### FWD1
- Performance: weak
- What worked: 671ms.
- What failed: (coach) "null players": still drift to the corners, can't pass, never get an angle for a clear shot, contribute nothing.
- Root cause: See Team-Level.

### FWD2
- Performance: weak
- What worked: 100% success.
- What failed: (coach) "null players": still drift to the corners, can't pass, never get an angle for a clear shot, contribute nothing.
- Root cause: See Team-Level.

## Team-Level Observations
- **v7 lost all three: 2-3, 0-2, 0-1.** Since v4's 2-1 win: five straight losses (0-3, 0-1, 2-3, 0-2, 0-1). Since v5 we have not improved.
- **The forwards haven't changed in four rewrites** (v3, v4, v5, v7 forward rules). Rule wording is not the lever. The remaining suspects:
  1. The agents can't turn our spatial instructions into good MOVE_TO targets (state format unknown).
  2. Haiku's spatial reasoning.
  3. Our own long clears (v5–v7 GK/DEF), which land in the corners where the forwards chase them.
- **The command set is bigger than we thought.** The platform's advice to Benchmark lists INTERCEPT, FOLLOW_PLAYER, MARK and SHOOT, and the reports say MOVE_TO and PRESS_BALL. FOLLOW_PLAYER exists and we have never used it. It could be the natural tool for a "swarm" (stay with a teammate) if it can target teammates. To confirm in "What can my agents do?".
- **Passing collapsed:** 37 (v4) → 15, 28, 24, **0**, 52. v5–v7 pushed CLEAR/SHOOT over PASS. In 3 of 3 matches the platform Coach's Corner asked for more PASS and less MOVE_TO.
- **Long-range goals against us:** Benchmark's GK (006) and Total Attack's GK (007) both scored from their own end, and Benchmark's DEF scored in 003/004. Need to see how these beat Shannon.
- **The 3000-char prompts did not slow anyone down:** MID 956/884/965 (941 at 2000 chars), FWD1 688/634/671 (638), FWD2 967/955/985 (893). Length is still not the latency lever.
- **Shots without SHOOT:** 4 shots and 0 SHOOT commands in 008, so the platform counts some clears/passes toward goal as shots.

## Action Items
- [ ] ALL outfield: play as a compact swarm in the center. Short distances to teammates and the ball, never near the touchlines. (priority: high, coach)
- [ ] FWD1/FWD2: no wide play. Short passes inside the swarm. Pass back instead of running wide. (priority: high, coach)
- [ ] DEF: PASS to a free teammate by default. CLEAR only when close to GK/our goal or under pressure. (priority: high, coach)
- [ ] MID/DEF: Cut passive MARKing (184 vs Fort Knox). MARK only the attacker nearest our goal. (priority: high)
- [ ] Platform: confirm FOLLOW_PLAYER semantics and the full command list ("What can my agents do?"). (priority: high)
- [ ] Model: forward behavior unchanged after four rewrites → test Sonnet on the forwards. (priority: high)
- [ ] GK: find out how long balls from their GK/DEF are beating Shannon. (priority: medium)

## Opponent Scouting Notes
- Saved to `strategy/opponent-notes/fort-knox-athletic.md`.
