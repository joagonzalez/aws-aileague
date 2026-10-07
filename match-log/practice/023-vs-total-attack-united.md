# Match 023: vs Total Attack United

## Result
- Score: 1 - 6 (LOSS)
- Date: 2026-10-07
- Type: practice
- Formation: 1-2-1
- Strategy: Swarm
- Deploy tag: deploy-v13-2026-10-06
- Prompt versions deployed: GK v12, DEF v12, MID v11, FWD1 v11, FWD2 v12
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

Coach watched; no live messages sent. Goals: 1': Max Fury (their GK) 0-1. 1': Unknown 0-2. 2': Max Fury 0-3. 2': Ray Chase (DEF) 0-4. 2': Tesla 1-4. 2': Vic Surge (FWD) 1-5, 1-6.

## Key Moments
1. First match on v13. Heaviest defeat since C001. Their GK scored twice and their DEF once from their own end: Hertz's press on their GK (v12/v13 rule 7) did not stop the sweeper-keeper's long shots.
2. **Clear 21 with every CLEAR word removed from the prompts.** The CLEAR_OVERRIDE count did not move (v12: 25), so our wording was never its cause; the agent or harness emits it by itself. Organizer question.
3. **PASS 0.** Under Total Attack's press (147 PRESS of ours too) our agents issued no pass at all: no through ball to Hertz, no GK/DEF long release (GK Dist 7). 69% possession, 2 shots.
4. **79 SHOOT commands, 2 shots.** The possession wording ('the ball is at your feet') did not close the gap.
5. Coach: Hertz spends the match near the corners instead of central ahead of the ball; Tesla slow at kick-off and the first short pass is stolen. Hertz's corners trace to rule 7: their GK has the ball constantly (109 commands), Hertz sprints at him in his box and is left wide when the ball leaves.

## Coach Interventions
| When | Message | Observed effect |
|------|---------|-----------------|
| — | None (watched, no messages sent) | — |

## Raw Stats
- Possession: 69% vs 31%
- Shots: 2 vs 13
- Shots on target: 1 vs 6
- Our commands: 545 total, 842ms avg latency
- Their commands: 545 total, 448ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 184 | 34% |
| Press | 147 | 27% |
| Intercept | 107 | 20% |
| Mark | 0 | 0% |
| Pass | 0 | 0% |
| Shoot | 79 | 14% |
| Clear | 21 | 4% |
| GK Dist | 7 | 1% |

"Clear" is CLEAR_OVERRIDE. Opponent: Move 311 (57%), Pass 68 (12%), Press 67 (12%), Follow 31 (6%), Clear 29 (5%), Intercept 18 (3%), Shoot 10 (2%), GK Dist 7 (1%), Mark 4 (1%).

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 681ms | | 100% |
| DEF (Turing) | 961ms | | 100% |
| MID (Tesla) | 985ms | | 100% |
| FWD1 (Hertz) | 649ms | | 100% |
| FWD2 (Lovelace) | 1063ms | | 100% |

Opponent: GK 195ms, DEF 193ms, MID 183ms (MVP, fastest: Al Frenzy), FWD 840ms, FWD 905ms. Most tactical: Max Fury (GK, 109 commands).

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
- Performance: weak
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
