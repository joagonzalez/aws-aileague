# Match 037: vs The Benchmark FC

## Result
- Score: 4 - 3 (WIN)
- Date: 2026-10-07
- Type: practice
- Formation: 1-2-1
- Strategy: Swarm
- Deploy tag: deploy-v14-2026-10-07
- Prompt versions deployed: GK v13, DEF v13, MID v12, FWD1 v12, FWD2 v13
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

Coach watched; no live messages sent. Goals: 1': Tesla 1-0, 2-0. 1': Unknown (Benchmark) 2-1. 2': Tesla 3-1. 2': Jay Smooth 3-2. 2': Unknown 3-3. 3': Tesla 4-3.

## Key Moments
1. Tesla four goals; conceded 3 to Benchmark for the second time on v14 (029: 3). PRESS 150 (27%): the press-heavy shape concedes behind it against balanced teams; still a win.

## Coach Interventions
| When | Message | Observed effect |
|------|---------|-----------------|
| — | None (watched, no messages sent) | — |

## Raw Stats
- Possession: 60% vs 40%
- Shots: 6 vs 9
- Shots on target: 4 vs 3
- Our commands: 549 total, 920ms avg latency
- Their commands: 550 total, 515ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 200 | 36% |
| Press | 150 | 27% |
| Intercept | 97 | 18% |
| Mark | 0 | 0% |
| Pass | 18 | 3% |
| Shoot | 53 | 10% |
| Clear | 26 | 5% |
| GK Dist | 5 | 1% |

"Clear" is CLEAR_OVERRIDE.

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 755ms | | 100% |
| DEF (Turing) | 1087ms | | 100% |
| MID (Tesla) | 1053ms | | 100% |
| FWD1 (Hertz) | 724ms | | 100% |
| FWD2 (Lovelace) | 1224ms | | 100% |

Opponent back three ~180-210 ms, forwards 840-1435 ms (their numbers also rose in the later matches).

## Per-Position Analysis

### GK
- Performance: strong
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: see the v14 series summary (match 041).

### DEF
- Performance: strong
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: see the v14 series summary (match 041).

### MID
- Performance: strong
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: see the v14 series summary (match 041).

### FWD1
- Performance: strong
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: see the v14 series summary (match 041).

### FWD2
- Performance: strong
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: see the v14 series summary (match 041).

## Team-Level Observations
- See the v14 series summary in match 041.
- Opponent formation: GK, DEF, MID, FWD, FWD.

## Action Items
- [ ] See match 041. (priority: high)

## Opponent Scouting Notes
- `strategy/opponent-notes/the-benchmark-fc.md`.
