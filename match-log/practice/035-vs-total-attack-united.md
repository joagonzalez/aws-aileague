# Match 035: vs Total Attack United

## Result
- Score: 4 - 5 (LOSS)
- Date: 2026-10-07
- Type: practice
- Formation: 1-2-1
- Strategy: Swarm
- Deploy tag: deploy-v14-2026-10-07
- Prompt versions deployed: GK v13, DEF v13, MID v12, FWD1 v12, FWD2 v13
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

Coach watched; no live messages sent. Goals: 1': Ray Chase (DEF) 0-1. 1': Tesla 1-1. 2': Vic Surge 1-2, 1-3. 2': Tesla 2-3. 2': Max Fury (GK) 2-4. 2': Tesla 3-4, 4-4. 3': Ray Chase 4-5.

## Key Moments
1. First v14 loss. Tesla four goals, lost 4-5 on 4 shots to 11. **Our latency 1058 ms average, Turing 1391, Tesla 1229, Lovelace 1194**: the slowest healthy match so far at that point. PASS 0, MOVE 49%.
2. Their DEF twice and GK once from their own end; Vic Surge twice.

## Coach Interventions
| When | Message | Observed effect |
|------|---------|-----------------|
| — | None (watched, no messages sent) | — |

## Raw Stats
- Possession: 66% vs 34%
- Shots: 4 vs 11
- Shots on target: 4 vs 5
- Our commands: 579 total, 1058ms avg latency
- Their commands: 580 total, 592ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 286 | 49% |
| Press | 92 | 16% |
| Intercept | 86 | 15% |
| Mark | 0 | 0% |
| Pass | 0 | 0% |
| Shoot | 86 | 15% |
| Clear | 28 | 5% |
| GK Dist | 1 | 0% |

"Clear" is CLEAR_OVERRIDE.

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 807ms | | 100% |
| DEF (Turing) | 1391ms | | 100% |
| MID (Tesla) | 1229ms | | 100% |
| FWD1 (Hertz) | 771ms | | 100% |
| FWD2 (Lovelace) | 1194ms | | 100% |

Opponent back three ~180-210 ms, forwards 840-1435 ms (their numbers also rose in the later matches).

## Per-Position Analysis

### GK
- Performance: weak
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: see the v14 series summary (match 041).

### DEF
- Performance: weak
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: see the v14 series summary (match 041).

### MID
- Performance: weak
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: see the v14 series summary (match 041).

### FWD1
- Performance: weak
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: see the v14 series summary (match 041).

### FWD2
- Performance: weak
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: see the v14 series summary (match 041).

## Team-Level Observations
- See the v14 series summary in match 041.
- Opponent formation: GK, DEF, MID, FWD, FWD.

## Action Items
- [ ] See match 041. (priority: high)

## Opponent Scouting Notes
- `strategy/opponent-notes/total-attack-united.md`.
