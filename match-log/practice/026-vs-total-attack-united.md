# Match 026: vs Total Attack United

## Result
- Score: 3 - 4 (LOSS)
- Date: 2026-10-07
- Type: practice
- Formation: 1-2-1
- Strategy: Swarm
- Deploy tag: deploy-v13-2026-10-06
- Prompt versions deployed: GK v12, DEF v12, MID v11, FWD1 v11, FWD2 v12
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

Coach watched; no live messages sent. Goals: 1': Ray Chase (DEF) 0-1. 1': Vic Surge (FWD) 0-2. 1': Tesla 1-2, 2-2. 1': Ray Chase 2-3. 1': Vic Surge 2-4. 2': Tesla 3-4.

## Key Moments
1. Fourth match on v13. Tesla hat-trick (31 goals in 20 matches); lost by one on 7 shots to 11.
2. **PASS 0 and GK Dist 1 again against Total Attack.** Their press (97) and camping forwards: our agents do not pass under it, so the long releases to Hertz never happen. MOVE 301 (55%).
3. Their DEF Ray Chase scored twice from distance and Vic Surge twice; MARK 0 for us: the second-marker rule did not show as MARK against moving forwards (vs 149 against Fort Knox's static block).
4. Turing 1272 ms, his slowest ever. Clear 23.
5. Coach: Total Attack's players stop and shoot from far, or step back/sideways to get free and then shoot; worth copying for Tesla and Lovelace (v14 item d).

## Coach Interventions
| When | Message | Observed effect |
|------|---------|-----------------|
| — | None (watched, no messages sent) | — |

## Raw Stats
- Possession: 61% vs 39%
- Shots: 7 vs 11
- Shots on target: 3 vs 4
- Our commands: 545 total, 939ms avg latency
- Their commands: 545 total, 468ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 301 | 55% |
| Press | 65 | 12% |
| Intercept | 80 | 15% |
| Mark | 0 | 0% |
| Pass | 0 | 0% |
| Shoot | 75 | 14% |
| Clear | 23 | 4% |
| GK Dist | 1 | 0% |

"Clear" is CLEAR_OVERRIDE. Opponent: Move 290 (53%), Press 97 (18%), Pass 59 (11%), Clear 26 (5%), Intercept 25 (5%), Follow 24 (4%), Shoot 16 (3%), Mark 7 (1%), GK Dist 1 (0%).

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 683ms | | 100% |
| DEF (Turing) | 1272ms | | 100% |
| MID (Tesla) | 935ms | | 100% |
| FWD1 (Hertz) | 659ms | | 100% |
| FWD2 (Lovelace) | 1101ms | | 100% |

Opponent: GK 196ms (most tactical: Max Fury, 109 commands), DEF 188ms, MID 184ms (MVP, fastest: Al Frenzy), FWD 821ms, FWD 895ms.

## Per-Position Analysis

### GK
- Performance: weak
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: see Key Moments and the v14 brief.

### DEF
- Performance: weak
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: see Key Moments and the v14 brief.

### MID
- Performance: strong
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: see Key Moments and the v14 brief.

### FWD1
- Performance: adequate
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
- `strategy/opponent-notes/total-attack-united.md`.
