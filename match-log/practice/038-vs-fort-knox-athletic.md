# Match 038: vs Fort Knox Athletic

## Result
- Score: 2 - 0 (WIN)
- Date: 2026-10-07
- Type: practice
- Formation: 1-2-1
- Strategy: Swarm
- Deploy tag: deploy-v14-2026-10-07
- Prompt versions deployed: GK v13, DEF v13, MID v12, FWD1 v12, FWD2 v13
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

Coach watched; no live messages sent. Goals: 2': Hertz 1-0, 2-0.

## Key Moments
1. **Platform slow: 229 commands (46 per agent, against 75-120 normally), 1451 ms average, Turing 1700 ms, Lovelace 2172 ms (above the 2 s tick: he missed ticks).** Still 2-0, Hertz twice, 0 on target against. MARK 81 (35%), SHOOT 0 commands for 4 shots.

## Coach Interventions
| When | Message | Observed effect |
|------|---------|-----------------|
| — | None (watched, no messages sent) | — |

## Raw Stats
- Possession: 50% vs 50%
- Shots: 4 vs 2
- Shots on target: 2 vs 0
- Our commands: 229 total, 1451ms avg latency
- Their commands: 230 total, 492ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 44 | 19% |
| Press | 33 | 14% |
| Intercept | 36 | 16% |
| Mark | 81 | 35% |
| Pass | 26 | 11% |
| Shoot | 0 | 0% |
| Clear | 5 | 2% |
| GK Dist | 4 | 2% |

"Clear" is CLEAR_OVERRIDE.

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 733ms | | 100% |
| DEF (Turing) | 1700ms | | 100% |
| MID (Tesla) | 948ms | | 100% |
| FWD1 (Hertz) | 707ms | | 100% |
| FWD2 (Lovelace) | 2172ms | | 100% |

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
