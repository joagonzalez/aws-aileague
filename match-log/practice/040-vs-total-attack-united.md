# Match 040: vs Total Attack United

## Result
- Score: 2 - 6 (LOSS)
- Date: 2026-10-07
- Type: practice
- Formation: 1-2-1
- Strategy: Swarm
- Deploy tag: deploy-v14-2026-10-07
- Prompt versions deployed: GK v13, DEF v13, MID v12, FWD1 v12, FWD2 v13
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

Coach watched; no live messages sent. Goals: 1': Max Fury (GK) 0-1. 1': Tesla 1-1. 2': Max Fury 1-2. 2': Ray Chase (DEF) 1-3. 2': Max Fury 1-4. 2': Ray Chase 1-5. 2': Tesla 2-5. 2': Max Fury 2-6.

## Key Moments
1. **Their GK scored four, their DEF two: six long shots from their own end.** 13 shots, 6 on target. Our latency 1059 ms average (Turing 1319). PASS 0. The AI overview did not generate.
2. Hertz's press is limited to a keeper outside his box (v14 a); Max Fury shoots from inside or at the edge of it, and every shot on target is a goal.

## Coach Interventions
| When | Message | Observed effect |
|------|---------|-----------------|
| — | None (watched, no messages sent) | — |

## Raw Stats
- Possession: 55% vs 45%
- Shots: 3 vs 13
- Shots on target: 2 vs 6
- Our commands: 543 total, 1059ms avg latency
- Their commands: 545 total, 513ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 191 | 35% |
| Press | 121 | 22% |
| Intercept | 130 | 24% |
| Mark | 0 | 0% |
| Pass | 0 | 0% |
| Shoot | 72 | 13% |
| Clear | 26 | 5% |
| GK Dist | 3 | 1% |

"Clear" is CLEAR_OVERRIDE.

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 833ms | | 100% |
| DEF (Turing) | 1319ms | | 100% |
| MID (Tesla) | 1058ms | | 100% |
| FWD1 (Hertz) | 698ms | | 100% |
| FWD2 (Lovelace) | 1067ms | | 100% |

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
