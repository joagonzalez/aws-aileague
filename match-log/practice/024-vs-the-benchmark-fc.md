# Match 024: vs The Benchmark FC

## Result
- Score: 1 - 1 (DRAW)
- Date: 2026-10-07
- Type: practice
- Formation: 1-2-1
- Strategy: Swarm
- Deploy tag: deploy-v13-2026-10-06
- Prompt versions deployed: GK v12, DEF v12, MID v11, FWD1 v11, FWD2 v12
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

Coach watched; no live messages sent. Goals: 1-1; the platform report pasted without the goals section.

## Key Moments
1. Second match on v13; long match (133 commands per agent, overtime after 1-1).
2. First non-win against Benchmark since 013 (017: 1-0, 018: 2-1). MOVE 330 (50%): the highest share since C003. PASS 39, SHOOT 38, Clear 14, MARK 2.
3. Coach: Hertz in the corners again (rule 7 chasing their GK, 133 commands); Tesla and Lovelace shooting less than before.
4. Possession, shots and on-target were not in the pasted report.

## Coach Interventions
| When | Message | Observed effect |
|------|---------|-----------------|
| — | None (watched, no messages sent) | — |

## Raw Stats
- Possession: not in the pasted report
- Shots: not in the pasted report
- Shots on target: not in the pasted report
- Our commands: 664 total, 926ms avg latency
- Their commands: 665 total, 493ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 330 | 50% |
| Press | 139 | 21% |
| Intercept | 95 | 14% |
| Mark | 2 | 0% |
| Pass | 39 | 6% |
| Shoot | 38 | 6% |
| Clear | 14 | 2% |
| GK Dist | 7 | 1% |

"Clear" is CLEAR_OVERRIDE. Opponent: Move 317 (48%), Press 141 (21%), Follow 57 (9%), Pass 56 (8%), Intercept 45 (7%), Shoot 23 (3%), Clear 18 (3%), GK Dist 6 (1%), Mark 2 (0%).

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 702ms | | 100% |
| DEF (Turing) | 946ms | | 100% |
| MID (Tesla) | 1003ms | | 100% |
| FWD1 (Hertz) | 705ms | | 100% |
| FWD2 (Lovelace) | 1212ms | | 100% |

Opponent: GK 191ms (most tactical: Drew Midway, 133 commands), DEF 195ms, MID 190ms (MVP, fastest: Lee Steady), FWD 935ms, FWD 946ms.

## Per-Position Analysis

### GK
- Performance: adequate
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: see Key Moments and the v14 brief.

### DEF
- Performance: adequate
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: see Key Moments and the v14 brief.

### MID
- Performance: adequate
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: see Key Moments and the v14 brief.

### FWD1
- Performance: weak
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: see Key Moments and the v14 brief.

### FWD2
- Performance: adequate
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: see Key Moments and the v14 brief.

## Team-Level Observations
- See the v13 series summary in match 027's Team-Level Observations and the v14 brief.
- Opponent formation: GK, DEF, MID, FWD, FWD.

## Action Items
- [ ] v14 (through the workflow): (a) Hertz presses their GK only when the GK is outside his box, never their DEF, otherwise holds the central runner spot (023–027: corners); (b) kick-off is a lofted pass to Hertz or the shot, never a short ground pass into a press (020–026: minute-1 concessions unchanged by the pass variant); (c) "you have the ball" instead of "the ball is at your feet" (the stricter trigger bought nothing: SHOOT commands still unrelated to shots); (d) Tesla/Lovelace: one step sideways to open the line, then shoot, when nobody is within a few steps (what Total Attack's players do). (priority: high)
- [ ] Office hours: CLEAR_OVERRIDE persists with the word removed (what emits it?); SHOOT 0 → 8 shots and 79 → 2 (what rejects a SHOOT, what else produces shots?); PASS 0 under press; per-agent view. (priority: high)

## Opponent Scouting Notes
- `strategy/opponent-notes/the-benchmark-fc.md`.
