# Match 030: vs Fort Knox Athletic

## Result
- Score: 4 - 2 (WIN)
- Date: 2026-10-07
- Type: practice
- Formation: 1-2-1
- Strategy: Swarm
- Deploy tag: deploy-v14-2026-10-07
- Prompt versions deployed: GK v13, DEF v13, MID v12, FWD1 v12, FWD2 v13
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

Coach watched; no live messages sent. Goals: 1': Tesla 1-0, 2-0. 1': Les Crawl (FWD) 2-1. 1': Pat Bunker (their GK) 2-2. 2': Tesla 3-2, 4-2.

## Key Moments
1. Third match on v14 and the last practice match of the allowance (30 of 30). Tesla four goals (40 in 23 matches on our prompts).
2. Their GK scored from his own end at 1' (Pat Bunker): with Hertz pressing only a keeper out of his box, a home-staying keeper's long shot is guarded only by GK rule 1. Second GK goal against us on v14 (Max Fury in 028), both single goals in wins.
3. **MARK 184 (36%) and SHOOT 0 commands for 3-4 shots and 4 goals**, exactly the 025 profile against the low block (MARK 149, SHOOT 0, 8 shots): the report's SHOOT counter does not count whatever produces our shots against Fort Knox. PASS 77 (the most ever), GK Dist 9.
4. Platform stats inconsistent: 3 shots, 4 on target. Shots on target = goals holds for them (2 of 2).

## Coach Interventions
| When | Message | Observed effect |
|------|---------|-----------------|
| — | None (watched, no messages sent) | — |

## Raw Stats
- Possession: 57% vs 43%
- Shots: 3 vs 2
- Shots on target: 4 vs 2
- Our commands: 510 total, 869ms avg latency
- Their commands: 510 total, 544ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 97 | 19% |
| Press | 83 | 16% |
| Intercept | 33 | 6% |
| Mark | 184 | 36% |
| Pass | 77 | 15% |
| Shoot | 0 | 0% |
| Clear | 27 | 5% |
| GK Dist | 9 | 2% |

"Clear" is CLEAR_OVERRIDE. Opponent: Move 306 (60%), Pass 71 (14%), Press 40 (8%), Follow 37 (7%), Clear 27 (5%), GK Dist 10 (2%), Intercept 9 (2%), Shoot 5 (1%), Mark 5 (1%).

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 672ms | | 100% |
| DEF (Turing) | 954ms | | 100% |
| MID (Tesla) | 948ms | | 100% |
| FWD1 (Hertz) | 661ms | | 100% |
| FWD2 (Lovelace) | 995ms | | 100% |

Opponent: GK 181ms (MVP, fastest, most tactical: Pat Bunker, 102 commands), DEF 184ms, MID 183ms, FWD 925ms, FWD 952ms.

## Per-Position Analysis

### GK
- Performance: adequate
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
- Performance: adequate
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
- `strategy/opponent-notes/fort-knox-athletic.md`.
