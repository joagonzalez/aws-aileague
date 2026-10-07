# Match 028: vs Total Attack United

## Result
- Score: 5 - 1 (WIN)
- Date: 2026-10-07
- Type: practice
- Formation: 1-2-1
- Strategy: Swarm
- Deploy tag: deploy-v14-2026-10-07
- Prompt versions deployed: GK v13, DEF v13, MID v12, FWD1 v12, FWD2 v13
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

Coach watched; no live messages sent. Goals: 1': Tesla 1-0, 2-0. 2': Unknown 3-0, 4-0. 2': Hertz 5-0. 2': Max Fury (their GK) 5-1 (the platform's text calls it a consolation).

## Key Moments
1. **First match on v14 and the first win over Total Attack since 015 (and the first ever unattended).** 5-1; v13 lost 1-6 and 3-4 to the same team.
2. **No goal conceded in minute 1** (v13: 3 and 4 after our kick-offs). The kick-off loft to Hertz (v14 b) replaced the stolen short pass; four goals of ours in the first two minutes.
3. Hertz scored (5-0) and the coach's corner complaint of the last five matches (corners) is gone from the report's picture: INTERCEPT 165 (32%) is the swarm's second player and loose balls; PRESS 48 (v13 vs TA: 147, 65) because Hertz no longer chases their keeper.
4. Their GK scored once from his own end; their DEF (Ray Chase, 3 goals in 023/026) and MID did not. The swarm pressing their deepest DEF (v14 a) and Hertz on a keeper out of his box held.
5. PASS 6 (v13 vs TA: 0, 0), SHOOT 69 for 4 shots, Clear 18, MARK 0 as before. Shots on target = goals (5 of 5, 1 of 1): 33 matches.

## Coach Interventions
| When | Message | Observed effect |
|------|---------|-----------------|
| — | None (watched, no messages sent) | — |

## Raw Stats
- Possession: 65% vs 35%
- Shots: 4 vs 6
- Shots on target: 5 vs 1
- Our commands: 510 total, 948ms avg latency
- Their commands: 510 total, 513ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 199 | 39% |
| Press | 48 | 9% |
| Intercept | 165 | 32% |
| Mark | 0 | 0% |
| Pass | 6 | 1% |
| Shoot | 69 | 14% |
| Clear | 18 | 4% |
| GK Dist | 5 | 1% |

"Clear" is CLEAR_OVERRIDE. Opponent: Move 285 (56%), Press 69 (14%), Pass 63 (12%), Follow 29 (6%), Clear 24 (5%), Intercept 21 (4%), Shoot 11 (2%), GK Dist 5 (1%), Mark 3 (1%).

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 748ms | | 100% |
| DEF (Turing) | 1021ms | | 100% |
| MID (Tesla) | 1045ms | | 100% |
| FWD1 (Hertz) | 726ms | | 100% |
| FWD2 (Lovelace) | 987ms | | 100% |

Opponent: GK 202ms (most tactical: Max Fury, 102 commands), DEF 200ms, MID 199ms (MVP, fastest: Al Frenzy), FWD 974ms, FWD 953ms.

## Per-Position Analysis

### GK
- Performance: strong
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: see Key Moments.

### DEF
- Performance: strong
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: see Key Moments.

### MID
- Performance: strong
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: see Key Moments.

### FWD1
- Performance: strong
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: see Key Moments.

### FWD2
- Performance: adequate
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: see Key Moments.

## Team-Level Observations
- v14 validation series (028-030): 3-0, 15 for, 6 against; 5-1 vs Total Attack, 6-3 vs Benchmark, 4-2 vs Fort Knox. Gate passed: vs Total Attack conceded 1 (v13: 6 and 4); vs Benchmark scored 6 (027: 3) but conceded 3 (027: 0), the press-heavy shape (PRESS 234) leaves gaps behind it; net strongly positive.
- **Decision: freeze v14 for the competitive matches.** The practice allowance is used up (30 of 30), so any further prompt change would go into competitive play untested.
- Open items for after the competition, not before: their GK's long shot from his own end (one goal in each of 028 and 030); conceding 3 to Benchmark under a 38% press; the SHOOT counter not counting our shots against Fort Knox; Clear (CLEAR_OVERRIDE) still 18-27.
- Opponent formation: GK, DEF, MID, FWD, FWD.

## Action Items
- [ ] Deploy nothing new. v14 is the competitive version; export a platform backup of it into deploy/backups/. (priority: high)
- [ ] Competitive: be present, check the first 15 seconds for 600-1200 ms per agent, send "be more aggressive and shoot!" at kick-off. (priority: high)

## Opponent Scouting Notes
- `strategy/opponent-notes/total-attack-united.md`.
