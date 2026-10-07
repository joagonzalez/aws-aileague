# Match 045: vs Total Attack United

## Result
- Score: 2 - 1 (WIN)
- Date: 2026-10-07
- Type: practice
- Formation: 1-2-1
- Strategy: Swarm
- Deploy tag: deploy-v14-2026-10-07
- Prompt versions deployed: GK v13, DEF v13, MID v12, FWD1 v12, FWD2 v13
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

Coach watched; no live messages sent. Goals: 1': Tesla 1-0. 2': Tesla 2-0. 2': Max Fury (their GK) 2-1.

## Key Moments
1. Fourth win over Total Attack on v14 (5-1, 3-1, 4-0, 2-1 against 4-5, 2-6, 0-6). Won it slow: 1094 ms average, Turing 1890 ms, Lovelace 1644 ms, 51 commands per agent. Hertz 673, Tesla 960, Shannon 664 in range.
2. Tesla both goals (first and second minute); 9 shots against, 1 on target, their GK's long shot. No minute-1 concession.
3. PASS 1, INTERCEPT 71 (28%), SHOOT 33 for 4 shots; the Total Attack profile as before.

## Coach Interventions
| When | Message | Observed effect |
|------|---------|-----------------|
| — | None (watched, no messages sent) | — |

## Raw Stats
- Possession: 65% vs 35%
- Shots: 4 vs 9
- Shots on target: 2 vs 1
- Our commands: 255 total, 1094ms avg latency
- Their commands: 255 total, 547ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 87 | 34% |
| Press | 53 | 21% |
| Intercept | 71 | 28% |
| Mark | 0 | 0% |
| Pass | 1 | 0% |
| Shoot | 33 | 13% |
| Clear | 6 | 2% |
| GK Dist | 4 | 2% |

"Clear" is CLEAR_OVERRIDE. Opponent: Move 131 (51%), Press 42 (16%), Pass 24 (9%), Follow 20 (8%), Intercept 13 (5%), Clear 11 (4%), Shoot 9 (4%), GK Dist 4 (2%), Mark 1 (0%).

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 664ms | | 100% |
| DEF (Turing) | 1890ms | | 100% |
| MID (Tesla) | 960ms | | 100% |
| FWD1 (Hertz) | 673ms | | 100% |
| FWD2 (Lovelace) | 1644ms | | 100% |

Opponent: GK 198ms (MVP, fastest, most tactical: Max Fury, 51 commands), DEF 210ms, MID 218ms, FWD 875ms, FWD 1016ms.

## Per-Position Analysis

### GK
- Performance: adequate
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: platform latency (see Key Moments).

### DEF
- Performance: adequate
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: platform latency (see Key Moments).

### MID
- Performance: adequate
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: platform latency (see Key Moments).

### FWD1
- Performance: adequate
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: platform latency (see Key Moments).

### FWD2
- Performance: adequate
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: platform latency (see Key Moments).

## Team-Level Observations
- v14 since the rollback: 3-0 (2-0, 1-0, 2-1), all at 1094-1592 ms with the platform under load. v14 overall: 14-3 in practice; vs Total Attack 4-3.
- Decision unchanged: v14 frozen for the competitive matches.
- Opponent formation: GK, DEF, MID, FWD, FWD.

## Action Items
- [ ] Competitive: first-15-second latency check; "be more aggressive and shoot!" at kick-off. (priority: high)

## Opponent Scouting Notes
- `strategy/opponent-notes/total-attack-united.md`.
