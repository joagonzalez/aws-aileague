# Match 007: vs Total Attack United

## Result
- Score: 0 - 2 (LOSS)
- Date: 2026-10-05
- Type: practice
- Formation: 1-1-2
- Strategy: Counter
- Deploy tag: deploy-v7-2026-10-05
- Prompt versions deployed: GK v7, DEF v7, MID v6, FWD1 v6, FWD2 v6
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Claude Haiku, FWD2 Claude Haiku

## Key Moments
1. 1': Total Attack FWD (Vic Surge) scored.
2. 2': Their GK (Max Fury) scored directly from his own end.
3. Recurring (coach): forwards in the corners, no passes, no angles.
4. Platform: we issued ZERO PASS commands all match.

## Coach Interventions
<!-- Not reported. Fill in, or write "None". -->
| When | Message | Observed effect |
|------|---------|-----------------|
| [minute] | [what you typed] | [what changed after it] |

## Raw Stats
- Possession: 57% vs 43%
- Shots: 3 vs 10
- Shots on target: 0 vs 2
- Our commands: 370 total, 867ms avg latency
- Their commands: 370 total, 194ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 133 | 36% |
| Press | 112 | 30% |
| Intercept | 68 | 18% |
| Mark | 0 | 0% |
| Pass | 0 | 0% |
| Shoot | 34 | 9% |
| Clear | 20 | 5% |
| GK Dist | 3 | 1% |

Opponent: Move 173 (47%), Press 163 (44%), Pass 21 (6%), Clear 10 (3%), GK Dist 3 (1%). No intercepts or marks.

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 638ms | | 100% |
| DEF (Turing) | 950ms | | 100% |
| MID (Tesla) | 884ms | | 100% |
| FWD1 (Hertz) | 634ms | | 100% |
| FWD2 (Lovelace) | 955ms | | 100% |

Opponent: all 198–203ms. MVP and fastest player: their MID (Al Frenzy, 198ms).

## Per-Position Analysis
### GK
- Performance: weak
- What worked: 638ms.
- What failed: Their GK scored directly from his own end, the second GK goal against us in two matches.
- Root cause: Unknown. The coach needs to see how the long balls beat him.

### DEF
- Performance: adequate
- What worked: 950ms.
- What failed: No passing from the back at all.
- Root cause: v6/v7 'always CLEAR at the box edge'.

### MID
- Performance: weak
- What worked: 884ms.
- What failed: 0 passes. SHOOT 34 but 3 shots, 0 on target.
- Root cause: v7 'shoot when central' fires, but the shots don't register or miss. With no forwards nearby, there's no one to pass to.

### FWD1
- Performance: weak
- What worked: 634ms.
- What failed: (coach) "null players": still drift to the corners, can't pass, never get an angle for a clear shot, contribute nothing.
- Root cause: See match 008.

### FWD2
- Performance: weak
- What worked: 100% success.
- What failed: (coach) "null players": still drift to the corners, can't pass, never get an angle for a clear shot, contribute nothing.
- Root cause: See match 008.

## Team-Level Observations
- Formation effectiveness: 57% possession, 3 shots, 0 on target, conceded at 1' and 2'.
- Coordination gaps: Zero passes. The team plays as 5 individuals.
- Opponent patterns: Press 44%, early goals as advertised. Their GK scored from distance.

## Action Items
- See match 008 for the combined v7 action items.

## Opponent Scouting Notes
- Saved to `strategy/opponent-notes/total-attack-united.md`.
