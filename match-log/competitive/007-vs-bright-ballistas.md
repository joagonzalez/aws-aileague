# Match 007: vs Bright Ballistas

## Result
- Score: 2 - 3 (LOSS)
- Date: 2026-10-08
- Type: competitive
- Formation: 1-2-1
- Strategy: Swarm
- Deploy tag: deploy-v14-2026-10-07
- Prompt versions deployed: GK v13, DEF v13, MID v12, FWD1 v12, FWD2 v13
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

We play as Kernel Panic FC. Coach watched; no live messages sent. Goals: 1': Wall (their DEF) 0-1. 1': Hertz 1-1. 1': Piston (FWD) 1-2. 2': Hertz 2-2. 2': Unknown 2-3.

## Key Moments
1. **Our team average latency was 412 ms**, with the per-agent table missing from the report. Our healthy range is 850-1000 ms. **0 SHOOT, 0 INTERCEPT, 0 MARK commands**, PRESS 292 (61%), MOVE 152: the command mix of C004 (default AI, 0 SHOOT/MARK/INTERCEPT). Most likely some or all slots ran the platform's default agent, as in C004 and C006. Fourth compromised competitive match of eight.
2. Hertz scored twice (he also scored in C004 when the default AI played). Their DEF Wall opened from distance; Piston and an unknown scorer finished. 6 shots, 3 on target, 3 goals.
3. Shots on target = goals for both teams (2 of 2, 3 of 3). 39 matches running.

## Coach Interventions
| When | Message | Observed effect |
|------|---------|-----------------|
| — | None (watched, no messages sent) | — |

## Raw Stats
- Possession: 51% vs 49%
- Shots: 3 vs 6
- Shots on target: 2 vs 3
- Our commands: 475 total, 412ms avg latency
- Their commands: 475 total, 530ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 152 | 32% |
| Press | 292 | 61% |
| Intercept | 0 | 0% |
| Mark | 0 | 0% |
| Pass | 13 | 3% |
| Shoot | 0 | 0% |
| Clear | 15 | 3% |
| GK Dist | 3 | 1% |

"Clear" is CLEAR_OVERRIDE. Opponent: Move 284 (60%), Press 55 (12%), Shoot 44 (9%), Pass 32 (7%), Follow 21 (4%), Clear 18 (4%), Intercept 16 (3%), GK Dist 3 (1%), Mark 2 (0%).

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) |  | | 100% |
| DEF (Turing) |  | | 100% |
| MID (Tesla) |  | | 100% |
| FWD1 (Hertz) |  | | 100% |
| FWD2 (Lovelace) |  | | 100% |

Opponent: MVP and fastest: Wall (DEF, 194ms); most tactical: Keeper (GK, 95 commands). The per-agent table was empty in the report.

## Per-Position Analysis

### GK
- Performance: weak
- What worked: Nothing attributable.
- What failed: 3 conceded.
- Root cause: Prompt probably not running (412 ms team average).

### DEF
- Performance: weak
- What worked: Nothing attributable.
- What failed: Their DEF scored from distance at 1'.
- Root cause: Same.

### MID
- Performance: weak
- What worked: Nothing attributable.
- What failed: 0 SHOOT commands for the team; Tesla had scored in 18 straight matches.
- Root cause: Same.

### FWD1
- Performance: strong
- What worked: Two goals.
- What failed: —
- Root cause: Default AI scores with him too (C004).

### FWD2
- Performance: weak
- What worked: Nothing attributable.
- What failed: —
- Root cause: Same.

## Team-Level Observations
- Formation effectiveness: not readable; the 412 ms average and the 0/0/0 command profile say our prompts were not (fully) running.
- Competitive record 3-5 after C008 (C001, C004, C006, C007 compromised by deployment or the default agent).
- Opponent formation: GK, DEF, MID, FWD, FWD.

## Action Items
- [ ] Before each remaining competitive match: export the team JSON and compare it with deploy/paste-ready.md (v14), then watch the first 15 seconds: any agent near 200 ms = default agent; abort-level problem. (priority: high)
- [ ] Organizers (bug.md): fourth competitive match with the default-agent signature. (priority: high)

## Opponent Scouting Notes
- Saved to `strategy/opponent-notes/bright-ballistas.md`.
