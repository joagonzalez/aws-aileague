# Match 034: vs The Benchmark FC

## Result
- Score: 2 - 1 (WIN)
- Date: 2026-10-07
- Type: practice
- Formation: 1-2-1
- Strategy: Swarm
- Deploy tag: deploy-v14-2026-10-07
- Prompt versions deployed: GK v13, DEF v13, MID v12, FWD1 v12, FWD2 v13
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

Coach watched; no live messages sent. Goals: 1': Jay Smooth (FWD) 0-1. 1': Tesla 1-1. 2': Hertz 2-1.

## Key Moments
1. Hertz winner. Benchmark had 59% possession, 2 shots. GK Dist 0.

## Coach Interventions
| When | Message | Observed effect |
|------|---------|-----------------|
| — | None (watched, no messages sent) | — |

## Raw Stats
- Possession: 41% vs 59%
- Shots: 6 vs 2
- Shots on target: 2 vs 1
- Our commands: 380 total, 983ms avg latency
- Their commands: 380 total, 614ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 135 | 36% |
| Press | 119 | 31% |
| Intercept | 63 | 17% |
| Mark | 1 | 0% |
| Pass | 15 | 4% |
| Shoot | 30 | 8% |
| Clear | 17 | 4% |
| GK Dist | 0 | 0% |

"Clear" is CLEAR_OVERRIDE.

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 755ms | | 100% |
| DEF (Turing) | 1072ms | | 100% |
| MID (Tesla) | 1100ms | | 100% |
| FWD1 (Hertz) | 775ms | | 100% |
| FWD2 (Lovelace) | 1109ms | | 100% |

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
