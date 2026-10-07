# Match 019: vs Fort Knox Athletic

## Result
- Score: 2 - 1 (WIN)
- Date: 2026-10-06
- Type: practice
- Formation: 1-1-2
- Strategy: Swarm
- Deploy tag: deploy-v11-2026-10-06
- Prompt versions deployed: GK v10, DEF v10, MID v9, FWD1 v9, FWD2 v10
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

Second match on v11. Unattended.

## Key Moments
1. Healthy signature: 380 commands, 887 ms average, every agent 641–1066 ms.
2. 1': Tesla (MID) 1-0. 1': "Unknown" (Fort Knox) 1-1, their only shot on target. 3': Tesla 2-1. Tesla: 20 goals in 14 matches.
3. **MARK 101 (27%)**, the first match where the v11 "MARK tightly" jobs ran as MARK (018: 1). INTERCEPT 42, PRESS 63, PASS 53 (14%, the highest share ever: through balls are being played). MOVE 100 (26%), the lowest ever.
4. **SHOOT 0 commands**, yet 2 shots, 2 on target, 2 goals. In 018 the same prompts gave 30 SHOOT commands for 3 shots. The command names in the report do not track our wording from match to match.
5. Fort Knox: 0 shots recorded but 1 on target and 1 goal (the platform's own stats disagree). 54% MOVE, FOLLOW 41, SHOOT 6.
6. Shots on target = goals, both teams (2 of 2, 1 of 1). 24 matches running.
7. 76 commands per agent: regulation length.

## Coach Interventions
| When | Message | Observed effect |
|------|---------|-----------------|
| — | None | — |

## Raw Stats
- Possession: 56% vs 44%
- Shots: 2 vs 0
- Shots on target: 2 vs 1
- Our commands: 380 total, 887ms avg latency
- Their commands: 380 total, 597ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 100 | 26% |
| Press | 63 | 17% |
| Intercept | 42 | 11% |
| Mark | 101 | 27% |
| Pass | 53 | 14% |
| Shoot | 0 | 0% |
| Clear | 13 | 3% |
| GK Dist | 8 | 2% |

Opponent: Move 205 (54%), Pass 47 (12%), Press 45 (12%), Follow 41 (11%), Clear 13 (3%), Intercept 11 (3%), GK Dist 8 (2%), Shoot 6 (2%), Mark 4 (1%).

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 668ms | | 100% |
| DEF (Turing) | 841ms | | 100% |
| MID (Tesla) | 1026ms | | 100% |
| FWD1 (Hertz) | 641ms | | 100% |
| FWD2 (Lovelace) | 1066ms | | 100% |

Opponent: GK 203ms (most tactical: Pat Bunker, 76 commands), DEF 203ms, MID 197ms (MVP, fastest: Ken Vault), FWD **1033ms**, FWD **1163ms**.

## Per-Position Analysis

### GK
- Performance: strong
- What worked: 8 GK Dist (018: 0): the throw/kick wording mapped this time. One goal from one shot on target.
- What failed: Nothing visible.
- Root cause: N/A.

### DEF
- Performance: strong
- What worked: One shot on target against all match; MARK 101 team-wide includes his tight marks.
- What failed: Nothing visible in the report.
- Root cause: N/A.

### MID
- Performance: strong
- What worked: Both goals. PASS 53: the through ball is being played.
- What failed: 1026ms.
- Root cause: N/A.

### FWD1
- Performance: adequate
- What worked: 641ms, fastest on the team.
- What failed: No goal despite 53 passes; see match 020 for the coach's observation (slow to shoot when alone in front of goal).
- Root cause: Rule order, see 020.

### FWD2
- Performance: adequate
- What worked: Possibly the marking volume (rule 7: MARK tightly their midfielder).
- What failed: 1066ms, his slowest. FOLLOW 0 again: "FOLLOW Tesla" does not map.
- Root cause: Command mapping.

## Team-Level Observations
- Formation effectiveness: Won 2-1; v11 is 2-0 in practice. The defensive layer v11 was built for showed up (MARK 101, INTERCEPT 42, PRESS 63, one shot on target against).
- Should we change formation? No.
- Coordination gaps: none visible.
- Opponent patterns: Fort Knox unchanged: compact, MOVE-heavy, few shots; back three at ~200 ms, forwards at ~1.1 s.
- Opponent formation: GK, DEF, MID, FWD, FWD.

## Action Items
- [ ] See match 020's action items (v12 brief). (priority: high)

## Opponent Scouting Notes
- Updated `strategy/opponent-notes/fort-knox-athletic.md`.
