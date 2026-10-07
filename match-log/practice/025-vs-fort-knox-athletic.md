# Match 025: vs Fort Knox Athletic

## Result
- Score: 3 - 1 (WIN)
- Date: 2026-10-07
- Type: practice
- Formation: 1-2-1
- Strategy: Swarm
- Deploy tag: deploy-v13-2026-10-06
- Prompt versions deployed: GK v12, DEF v12, MID v11, FWD1 v11, FWD2 v12
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

Coach watched; no live messages sent. Goals: 1': Tesla 1-0. 1': Hertz 2-0. 2': Tesla 3-0. 2': Unknown (Fort Knox) 3-1.

## Key Moments
1. Third match on v13. Three goals in two minutes; Hertz scored as the runner (coach: being alone up top created the chance).
2. **MARK 149 (35%)** against the low block, as in 019 (101): marking fires against a team that stands still. PASS 67, MOVE 63 (15%, lowest ever).
3. **SHOOT 0 commands, 8 shots, 3 on target, 3 goals.** Shots happen without SHOOT commands; with 21 Clears (CLEAR_OVERRIDE ticks hand the player to the default AI) one hypothesis is that the default AI takes them. Organizer question.
4. Coach: Hertz still drifts to the corners between runs.

## Coach Interventions
| When | Message | Observed effect |
|------|---------|-----------------|
| — | None (watched, no messages sent) | — |

## Raw Stats
- Possession: 52% vs 48%
- Shots: 8 vs 2
- Shots on target: 3 vs 1
- Our commands: 425 total, 893ms avg latency
- Their commands: 425 total, 477ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 63 | 15% |
| Press | 66 | 16% |
| Intercept | 52 | 12% |
| Mark | 149 | 35% |
| Pass | 67 | 16% |
| Shoot | 0 | 0% |
| Clear | 21 | 5% |
| GK Dist | 5 | 1% |

"Clear" is CLEAR_OVERRIDE. Opponent: Move 249 (59%), Pass 54 (13%), Press 34 (8%), Follow 33 (8%), Clear 19 (4%), Intercept 16 (4%), Shoot 14 (3%), GK Dist 5 (1%), Mark 1 (0%). Also logged for us: Follow 2.

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 657ms | | 100% |
| DEF (Turing) | 1043ms | | 100% |
| MID (Tesla) | 894ms | | 100% |
| FWD1 (Hertz) | 609ms | | 100% |
| FWD2 (Lovelace) | 1066ms | | 100% |

Opponent: GK 187ms (most tactical: Pat Bunker, 85 commands), DEF 182ms (MVP, fastest: Tim Shield), MID 183ms, FWD 820ms, FWD 955ms.

## Per-Position Analysis

### GK
- Performance: strong
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: see Key Moments and the v14 brief.

### DEF
- Performance: strong
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: see Key Moments and the v14 brief.

### MID
- Performance: strong
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: see Key Moments and the v14 brief.

### FWD1
- Performance: strong
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
- `strategy/opponent-notes/fort-knox-athletic.md`.
