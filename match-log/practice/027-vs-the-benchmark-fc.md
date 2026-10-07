# Match 027: vs The Benchmark FC

## Result
- Score: 3 - 0 (WIN)
- Date: 2026-10-07
- Type: practice
- Formation: 1-2-1
- Strategy: Swarm
- Deploy tag: deploy-v13-2026-10-06
- Prompt versions deployed: GK v12, DEF v12, MID v11, FWD1 v11, FWD2 v12
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

Coach watched; no live messages sent. Goals: 1': Unknown 1-0. 1': Tesla 2-0. 1': Tesla 3-0.

## Key Moments
1. Fifth match on v13 (the coach's 'match 6'; no report exists for a 'match 5'). Three goals in the first minute, three shots, all on target; Benchmark 8 shots, none on target.
2. Clean sheet: Shannon 0 on target against; PRESS 125 (31%). PASS 11, Clear 9 (lowest ever), GK Dist 0.
3. Shots on target = goals, both teams (3 of 3, 0 of 0). 32 matches running.

## Coach Interventions
| When | Message | Observed effect |
|------|---------|-----------------|
| — | None (watched, no messages sent) | — |

## Raw Stats
- Possession: 49% vs 51%
- Shots: 3 vs 8
- Shots on target: 3 vs 0
- Our commands: 405 total, 899ms avg latency
- Their commands: 405 total, 504ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 166 | 41% |
| Press | 125 | 31% |
| Intercept | 58 | 14% |
| Mark | 0 | 0% |
| Pass | 11 | 3% |
| Shoot | 36 | 9% |
| Clear | 9 | 2% |
| GK Dist | 0 | 0% |

"Clear" is CLEAR_OVERRIDE. Opponent: Move 190 (47%), Press 93 (23%), Pass 37 (9%), Intercept 34 (8%), Follow 22 (5%), Shoot 13 (3%), Clear 12 (3%), Mark 4 (1%).

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 677ms | | 100% |
| DEF (Turing) | 954ms | | 100% |
| MID (Tesla) | 932ms | | 100% |
| FWD1 (Hertz) | 642ms | | 100% |
| FWD2 (Lovelace) | 1008ms | | 100% |

Opponent: GK 190ms (most tactical: Drew Midway, 81 commands), DEF 193ms, MID 189ms (MVP, fastest: Lee Steady), FWD 891ms, FWD 932ms.

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
- **v13 series (023–027): 2 W, 1 D, 2 L.** vs Benchmark/Fort Knox: 3-1, 1-1, 3-0 (7 for, 2 against); vs Total Attack: 1-6, 3-4 (4 for, 10 against). Since v9 vs non-aggressive teams: 9-1-1. The aggressive template remains the only thing that beats us: PASS 0 under its press, their DEF/GK long shots (Ray Chase 3, Max Fury 2), camping forwards (Vic Surge 4).
- Three surprises: Clear (CLEAR_OVERRIDE) did not drop after every CLEAR word was removed; SHOOT commands are unrelated to shots (0 → 8, 79 → 2); PASS is 0 in both Total Attack matches.
- Coach, all five matches: Hertz in the corners (rule 7 chases their GK, who holds the ball 80–133 commands a match); Tesla slow at kick-off and the short pass stolen; Tesla and Lovelace shooting less. Shannon solid (0 and 1 on target against in the wins).
- Gate: v13 holds vs balanced/defensive (ship for competitive), fails vs Total Attack. v14 is four targeted edits, validated in one of the 3 remaining practice matches.
- Opponent formation: GK, DEF, MID, FWD, FWD.

## Action Items
- [ ] v14 (through the workflow): (a) Hertz presses their GK only when the GK is outside his box, never their DEF, otherwise holds the central runner spot (023–027: corners); (b) kick-off is a lofted pass to Hertz or the shot, never a short ground pass into a press (020–026: minute-1 concessions unchanged by the pass variant); (c) "you have the ball" instead of "the ball is at your feet" (the stricter trigger bought nothing: SHOOT commands still unrelated to shots); (d) Tesla/Lovelace: one step sideways to open the line, then shoot, when nobody is within a few steps (what Total Attack's players do). (priority: high)
- [ ] Office hours: CLEAR_OVERRIDE persists with the word removed (what emits it?); SHOOT 0 → 8 shots and 79 → 2 (what rejects a SHOOT, what else produces shots?); PASS 0 under press; per-agent view. (priority: high)

## Opponent Scouting Notes
- `strategy/opponent-notes/the-benchmark-fc.md`.
