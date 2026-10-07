# Match 021: vs Total Attack United

## Result
- Score: 0 - 2 (LOSS)
- Date: 2026-10-06
- Type: practice
- Formation: 1-2-1 (platform setting since the match 012 test; this log originally said 1-1-2 by habit — corrected 2026-10-07)
- Strategy: Swarm
- Deploy tag: deploy-v11-2026-10-06
- Prompt versions deployed: GK v10, DEF v10, MID v9, FWD1 v9, FWD2 v10
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

Fourth match on v11, coach watching. Second straight loss to Total Attack (020: 3-7).

## Key Moments
1. Healthy signature: 360 commands, 932 ms average, every agent 637–968 ms.
2. **69% possession, 0 shots.** First match in 26 with no shot at all. PASS 2, GK Dist 14 (most ever), CLEAR 18, SHOOT 36 commands with no shot resulting.
3. **Coach observation (live): GK and DEF passed the ball between themselves in our area for long stretches instead of releasing it long to MID or the forwards.** Both prompts forbid passing to each other; what happened is the GK's "kick it long toward the center of their goal" has no named receiver, the harness picks one for GK_DISTRIBUTE and takes the nearest, DEF, who then clears or passes short under Total Attack's press and the ball comes back. The v11 Evaluator flagged exactly this (note 5: "GK kick names no target; the harness will pick one; leave unless kicks land short") and the kicks landed short.
4. 1': Al Frenzy (their MID) 0-1, "amid relentless PRESS_BALL commands (111) that left midfield exposed". 2': Max Fury (their GK) 0-2. Opposing GKs have scored 7 times against us; nobody presses him under v11.
5. Shots on target = goals, both teams (0 of 0, 2 of 2). 26 matches running.
6. 72 commands per agent: regulation length.

## Coach Interventions
| When | Message | Observed effect |
|------|---------|-----------------|
| — | None (watched, no messages sent) | — |

## Raw Stats
- Possession: 69% vs 31%
- Shots: 0 vs 8
- Shots on target: 0 vs 2
- Our commands: 360 total, 932ms avg latency
- Their commands: 360 total, 517ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 115 | 32% |
| Press | 111 | 31% |
| Intercept | 64 | 18% |
| Mark | 0 | 0% |
| Pass | 2 | 1% |
| Shoot | 36 | 10% |
| Clear | 18 | 5% |
| GK Dist | 14 | 4% |

Opponent: Move 183 (51%), Press 59 (16%), Pass 37 (10%), Follow 32 (9%), Clear 23 (6%), GK Dist 16 (4%), Intercept 7 (2%), Mark 2 (1%), Shoot 1 (0%).

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 637ms | | 100% |
| DEF (Turing) | 947ms | | 100% |
| MID (Tesla) | 968ms | | 100% |
| FWD1 (Hertz) | 686ms | | 100% |
| FWD2 (Lovelace) | 966ms | | 100% |

Opponent: GK 192ms (most tactical: Max Fury, 72 commands), DEF 187ms (MVP, fastest: Ray Chase), MID 190ms, FWD 646ms, FWD **1054ms**.

## Per-Position Analysis

### GK
- Performance: weak
- What worked: 637ms. Only 2 shots on target against from 8.
- What failed: 14 distributions, most of them to DEF (coach), so the ball never left our half by his foot.
- Root cause: Rule 2's kick names no receiver; the harness chooses DEF. Fix in v12: "kick it long to FWD1", and "NEVER throw or kick to DEF".

### DEF
- Performance: weak
- What worked: 2 on target against from 8 shots.
- What failed: Received the GK's kicks and could not release forward under pressure; CLEAR 18 with the ball coming back.
- Root cause: CLEAR has no receiver either. v12: lofted pass to FWD1 before an untargeted CLEAR.

### MID
- Performance: weak
- What worked: Nothing visible.
- What failed: No goal for the first time since 013; 36 SHOOT commands and no shot.
- Root cause: The ball never reached him in their half; PASS 2 for the team.

### FWD1
- Performance: weak
- What worked: 686ms.
- What failed: No shot.
- Root cause: No supply (see GK/DEF). v12 also makes him press their GK.

### FWD2
- Performance: weak
- What worked: Nothing visible.
- What failed: No shot. MARK 0 again.
- Root cause: No supply; command mapping.

## Team-Level Observations
- Formation effectiveness: Lost 0-2. v11 is 2-2 in practice; both losses to Total Attack (3-7, 0-2), whose press at the front and GK long balls exploit v11's two open gaps: nobody presses their GK, and our back line's releases name no receiver.
- Should we change formation? No. v12 (in the workflow now) adds the GK-kick target, the DEF lofted pass, Hertz pressing their GK, the kick-off pass instead of the center-spot shot, the inside-the-box shot and the mark-before-press order.
- Possession is meaningless on this platform when it sits in our own box: 69% and 0 shots.
- Opponent patterns: Total Attack United, same as 020: GK Max Fury runs the team (72 commands, a goal), back three at ~190 ms, one forward at 646 ms this time.
- Opponent formation: GK, DEF, MID, FWD, FWD.

## Action Items
- [ ] v12 brief item 5 (sent to the Writer): GK kicks long to FWD1 by name, never to DEF; DEF lofted pass to FWD1 before an untargeted CLEAR. (priority: high)
- [ ] After v12 is deployed: one practice match, preferably against Total Attack United, checking GK Dist count and where the kicks land, PASS count, shots. (priority: high)

## Opponent Scouting Notes
- Updated `strategy/opponent-notes/total-attack-united.md`.
