# Match 046: vs The Benchmark FC

## Result
- Score: 4 - 0 (WIN)
- Date: 2026-10-07
- Type: practice
- Formation: 1-2-1
- Strategy: Swarm
- Deploy tag: deploy-v14-2026-10-07
- Prompt versions deployed: GK v13, DEF v13, MID v12, FWD1 v12, FWD2 v13
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

Coach watched; no live messages sent. Goals: 1': Tesla 1-0, 2-0. 2': Hertz 3-0. 2': Tesla 4-0.

## Key Moments
1. Platform back to normal speed: 944 ms average, Turing 875, Tesla 963, Hertz 657, Lovelace 1115; 85 commands per agent. Four goals in two minutes, Benchmark 7 shots and none on target.
2. v14 since the rollback: 4-0 (2-0, 1-0, 2-1, 4-0). v14 overall 15-3 in practice; vs Benchmark 6-0.
3. PRESS 179 (42%), the highest share on record, with a clean sheet: against Benchmark the press concedes only when the platform is slow (029, 037 at ~920 ms were 6-3 and 4-3).
4. Shots on target = goals (4 of 4, 0 of 0). 38 matches running.

## Coach Interventions
| When | Message | Observed effect |
|------|---------|-----------------|
| — | None (watched, no messages sent) | — |

## Raw Stats
- Possession: 54% vs 46%
- Shots: 4 vs 7
- Shots on target: 4 vs 0
- Our commands: 425 total, 944ms avg latency
- Their commands: 425 total, 608ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 143 | 34% |
| Press | 179 | 42% |
| Intercept | 33 | 8% |
| Mark | 3 | 1% |
| Pass | 15 | 4% |
| Shoot | 38 | 9% |
| Clear | 12 | 3% |
| GK Dist | 2 | 0% |

"Clear" is CLEAR_OVERRIDE. Opponent: Move 232 (55%), Press 70 (16%), Pass 42 (10%), Follow 27 (6%), Intercept 19 (4%), Shoot 18 (4%), Clear 12 (3%), Mark 3 (1%), GK Dist 2 (0%).

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 675ms | | 100% |
| DEF (Turing) | 875ms | | 100% |
| MID (Tesla) | 963ms | | 100% |
| FWD1 (Hertz) | 657ms | | 100% |
| FWD2 (Lovelace) | 1115ms | | 100% |

Opponent: GK 209ms (most tactical: Drew Midway, 85 commands), DEF 205ms (MVP, fastest: Norm Easy), MID 207ms, FWD 1073ms, FWD 1155ms.

## Per-Position Analysis

### GK
- Performance: strong
- What worked: see Key Moments.
- What failed: nothing visible.
- Root cause: N/A.

### DEF
- Performance: strong
- What worked: see Key Moments.
- What failed: nothing visible.
- Root cause: N/A.

### MID
- Performance: strong
- What worked: see Key Moments.
- What failed: nothing visible.
- Root cause: N/A.

### FWD1
- Performance: strong
- What worked: see Key Moments.
- What failed: nothing visible.
- Root cause: N/A.

### FWD2
- Performance: strong
- What worked: see Key Moments.
- What failed: nothing visible.
- Root cause: N/A.

## Team-Level Observations
- v14 frozen for the competitive matches; this is its signature at normal speed.
- Opponent formation: GK, DEF, MID, FWD, FWD.

## Action Items
- [ ] Competitive: first-15-second latency check; "be more aggressive and shoot!" at kick-off. (priority: high)

## Opponent Scouting Notes
- `strategy/opponent-notes/the-benchmark-fc.md`.
