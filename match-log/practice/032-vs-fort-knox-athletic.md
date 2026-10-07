# Match 032: vs Fort Knox Athletic

## Result
- Score: 4 - 0 (WIN)
- Date: 2026-10-07
- Type: practice
- Formation: 1-2-1
- Strategy: Swarm
- Deploy tag: deploy-v14-2026-10-07
- Prompt versions deployed: GK v13, DEF v13, MID v12, FWD1 v12, FWD2 v13
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

Coach watched; no live messages sent. Goals: 1': Tesla 1-0, 2-0. 2': Tesla 3-0, 4-0.

## Key Moments
1. Tesla four goals; MARK 126, PASS 64, SHOOT 0 commands for 5 shots (the Fort Knox profile again). Clean sheet, 0 on target against.

## Coach Interventions
| When | Message | Observed effect |
|------|---------|-----------------|
| — | None (watched, no messages sent) | — |

## Raw Stats
- Possession: 54% vs 46%
- Shots: 5 vs 1
- Shots on target: 4 vs 0
- Our commands: 430 total, 893ms avg latency
- Their commands: 430 total, 478ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 86 | 20% |
| Press | 84 | 20% |
| Intercept | 46 | 11% |
| Mark | 126 | 29% |
| Pass | 64 | 15% |
| Shoot | 0 | 0% |
| Clear | 19 | 4% |
| GK Dist | 5 | 1% |

"Clear" is CLEAR_OVERRIDE.

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 698ms | | 100% |
| DEF (Turing) | 1058ms | | 100% |
| MID (Tesla) | 994ms | | 100% |
| FWD1 (Hertz) | 650ms | | 100% |
| FWD2 (Lovelace) | 970ms | | 100% |

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
- `strategy/opponent-notes/fort-knox-athletic.md`.
