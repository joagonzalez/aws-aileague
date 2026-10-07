# Match 029: vs The Benchmark FC

## Result
- Score: 6 - 3 (WIN)
- Date: 2026-10-07
- Type: practice
- Formation: 1-2-1
- Strategy: Swarm
- Deploy tag: deploy-v14-2026-10-07
- Prompt versions deployed: GK v13, DEF v13, MID v12, FWD1 v12, FWD2 v13
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

Coach watched; no live messages sent. Goals: 1': Unknown (Benchmark) 0-1. 1': Tesla 1-1. 1': Hertz 2-1, 3-1. 2': Hertz 4-1. 2': Jay Smooth (FWD) 4-2. 2': Tesla 5-2. 2': Jay Smooth 5-3. 2': Tesla 6-3.

## Key Moments
1. Second match on v14. Nine goals, six ours: Hertz hat-trick as the runner, Tesla three.
2. Most goals we have ever scored and the most conceded to Benchmark (3; previous worst 2 in 002 and 013). PRESS 234 (38%, the highest share since match 001): the extended press reach (v13 c) plus v14's swarm taking their deepest DEF. The platform's note: tighten positioning before the press. Shots on target = goals (6 of 6, 3 of 3).
3. SHOOT 72 for 9 shots: the best command-to-shot ratio since C002. GK Dist 1, Clear 27, MARK 0.
4. Latency: every agent 811-1116 ms, Tesla's slowest healthy run; overtime-length match (123 commands per agent).

## Coach Interventions
| When | Message | Observed effect |
|------|---------|-----------------|
| — | None (watched, no messages sent) | — |

## Raw Stats
- Possession: 66% vs 34%
- Shots: 9 vs 6
- Shots on target: 6 vs 3
- Our commands: 615 total, 942ms avg latency
- Their commands: 615 total, 528ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 225 | 37% |
| Press | 234 | 38% |
| Intercept | 39 | 6% |
| Mark | 0 | 0% |
| Pass | 17 | 3% |
| Shoot | 72 | 12% |
| Clear | 27 | 4% |
| GK Dist | 1 | 0% |

"Clear" is CLEAR_OVERRIDE. Opponent: Move 343 (56%), Press 90 (15%), Shoot 75 (12%), Clear 36 (6%), Intercept 28 (5%), Follow 23 (4%), Pass 17 (3%), Mark 2 (0%), GK Dist 1 (0%).

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 852ms | | 100% |
| DEF (Turing) | 895ms | | 100% |
| MID (Tesla) | 1116ms | | 100% |
| FWD1 (Hertz) | 811ms | | 100% |
| FWD2 (Lovelace) | 1046ms | | 100% |

Opponent: GK 175ms (MVP, fastest, most tactical: Drew Midway, 123 commands), DEF 181ms, MID 184ms, FWD 1011ms, FWD 1146ms.

## Per-Position Analysis

### GK
- Performance: adequate
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: see Key Moments.

### DEF
- Performance: adequate
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
- `strategy/opponent-notes/the-benchmark-fc.md`.
