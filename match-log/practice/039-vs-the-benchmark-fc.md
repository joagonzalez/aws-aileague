# Match 039: vs The Benchmark FC

## Result
- Score: 2 - 1 (WIN)
- Date: 2026-10-07
- Type: practice
- Formation: 1-2-1
- Strategy: Swarm
- Deploy tag: deploy-v14-2026-10-07
- Prompt versions deployed: GK v13, DEF v13, MID v12, FWD1 v12, FWD2 v13
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

Coach watched; no live messages sent. Goals: 1': Drew Midway (their GK, own goal) 1-0. 1': Tesla 2-0. 3': Tesla 3-0 — the report lists three for us; the score is 2-1, so one line is the own goal counted once and the 3' goal is the second.

## Key Moments
1. Benchmark 10 shots, 1 on target. Tesla scored; an own goal by their keeper. Their forward at 1435 ms: the platform was slow for them too.

## Coach Interventions
| When | Message | Observed effect |
|------|---------|-----------------|
| — | None (watched, no messages sent) | — |

## Raw Stats
- Possession: 49% vs 51%
- Shots: 6 vs 10
- Shots on target: 2 vs 1
- Our commands: 410 total, 952ms avg latency
- Their commands: 410 total, 527ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 170 | 41% |
| Press | 113 | 28% |
| Intercept | 65 | 16% |
| Mark | 1 | 0% |
| Pass | 18 | 4% |
| Shoot | 23 | 6% |
| Clear | 14 | 3% |
| GK Dist | 6 | 1% |

"Clear" is CLEAR_OVERRIDE.

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 821ms | | 100% |
| DEF (Turing) | 1003ms | | 100% |
| MID (Tesla) | 1054ms | | 100% |
| FWD1 (Hertz) | 792ms | | 100% |
| FWD2 (Lovelace) | 1119ms | | 100% |

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
