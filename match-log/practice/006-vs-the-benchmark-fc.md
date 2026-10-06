# Match 006: vs The Benchmark FC

## Result
- Score: 2 - 3 (LOSS)
- Date: 2026-10-05
- Type: practice
- Formation: 1-1-2
- Strategy: Counter
- Deploy tag: deploy-v7-2026-10-05
- Prompt versions deployed: GK v7, DEF v7, MID v6, FWD1 v6, FWD2 v6
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Claude Haiku, FWD2 Claude Haiku

## Key Moments
1. 1': Benchmark FWD (Jay Smooth) scored.
2. 1': Hertz (FWD1) equalized.
3. 2': Turing (DEF) scored, 2-1 to us.
4. 2': Jay Smooth equalized.
5. 3': Benchmark's GK (Drew Midway) scored the winner, an 'unlikely goal' from his own goal.
6. Recurring (coach): Hertz and Lovelace still in the corners. They can't pass and never get a clear angle. The team never consolidates in the center.

## Coach Interventions
<!-- Not reported. Fill in, or write "None". -->
| When | Message | Observed effect |
|------|---------|-----------------|
| [minute] | [what you typed] | [what changed after it] |

## Raw Stats
- Possession: 56% vs 44%
- Shots: 5 vs 12
- Shots on target: 2 vs 3
- Our commands: 550 total, 876ms avg latency
- Their commands: 550 total, 198ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 247 | 45% |
| Press | 154 | 28% |
| Intercept | 71 | 13% |
| Mark | 0 | 0% |
| Pass | 24 | 4% |
| Shoot | 21 | 4% |
| Clear | 25 | 5% |
| GK Dist | 8 | 1% |

Opponent: Press 249 (45%), Move 243 (44%), Pass 26 (5%), Clear 22 (4%), GK Dist 10 (2%).

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 655ms | | 100% |
| DEF (Turing) | 1007ms | | 100% |
| MID (Tesla) | 956ms | | 100% |
| FWD1 (Hertz) | 688ms | | 100% |
| FWD2 (Lovelace) | 967ms | | 100% |

Opponent: all 192–200ms. MVP and fastest player: their DEF (Norm Easy, 192ms).

## Per-Position Analysis
### GK
- Performance: weak
- What worked: 655ms.
- What failed: Conceded 3 from 3 shots on target, one scored by their own GK from deep.
- Root cause: Unknown. See the long-range pattern under Team-Level.

### DEF
- Performance: adequate
- What worked: Scored at 2'.
- What failed: 1007ms. Clears long from his spot instead of passing (v6/v7 design). Coach wants him to pass, and clear only when close to GK.
- Root cause: v6/v7 rule 1 always CLEARs at the box edge.

### MID
- Performance: adequate
- What worked: 956ms with a 2999-char prompt (941 at 2000 chars in 005).
- What failed: Few passes (24 team-wide).
- Root cause: The forwards are never near him to pass to.

### FWD1
- Performance: adequate
- What worked: Scored at 1'. 688ms.
- What failed: (coach) "null players": still drift to the corners, can't pass, never get an angle for a clear shot, contribute nothing.
- Root cause: See Team-Level: four rewrites of the forward rules have not changed the behavior.

### FWD2
- Performance: weak
- What worked: 100% success.
- What failed: (coach) "null players": still drift to the corners, can't pass, never get an angle for a clear shot, contribute nothing.
- Root cause: Same as FWD1.

## Team-Level Observations
- Formation effectiveness: Scored 2 (first goals since 003) but conceded 3 from 3 shots on target.
- Should we change formation? See the overall analysis in match 008.
- Coordination gaps: No compact unit. The forwards are far from MID and each other.
- Opponent patterns: Press 45%. Their GK scored from his own end.

## Action Items
- See match 008 for the combined v7 action items.

## Opponent Scouting Notes
- Saved to `strategy/opponent-notes/the-benchmark-fc.md`.
