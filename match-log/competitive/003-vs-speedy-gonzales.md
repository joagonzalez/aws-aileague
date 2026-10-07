# Match 003: vs Speedy Gonzales

## Result
- Score: 2 - 0 (WIN)
- Date: 2026-10-06
- Type: competitive
- Formation: 1-2-1 (platform setting since the match 012 test; this log originally said 1-1-2 by habit — corrected 2026-10-07)
- Strategy: Swarm
- Deploy tag: deploy-v10-2026-10-06
- Prompt versions deployed: GK v9, DEF v9, MID v8, FWD1 v8, FWD2 v9
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

We play as **Kernel Panic FC**. Second match for the v10 release. Clean sheet, 0 shots on target against.

## Key Moments
1. 1': Tesla (MID) 1-0, "capitalized on Speedy's high press intensity (177 PRESS_BALL commands) leaving defensive gaps" (platform AI overview). Tesla: 17 goals in 11 matches.
2. 2': "Unknown" 2-0 for us (position not attributed; coach to confirm who).
3. Speedy Gonzales: 3 shots, 0 on target. 29% possession. Their forwards at 1024ms and 983ms never got a clean shot.
4. 350 commands per team, 70 per agent: regulation length, no overtime (C002 had 123 per agent with overtime).
5. **Command mix anomaly.** 310 of our 350 commands (89%) were MOVE, SHOOT 1, PRESS 2, no INTERCEPT, no FOLLOW, no MARK. The same prompts produced SHOOT 73 / PRESS 30 / FOLLOW 71 in C002 an hour or so earlier, and the platform still counted 6 shots and 2 goals for us against a single SHOOT command. Latency was the slowest healthy run on record (968–1159ms, team 1078ms; their forwards were ~1000ms too), which points to platform load. Either the harness fell back to MOVE_TO on slow or unparsed answers, or 71% possession with Speedy pressing at 51% meant our on-ball rules resolved to the one-step carry most ticks. Not resolvable from the report; see Action Items.
6. Platform Coach's Corner for us: "Increase PASS beyond 20; over-reliance on MOVE_TO (310) created static positioning".
7. Shots on target = goals for both teams again (us 2 of 2, them 0 of 0). 20 matches running.

## Coach Interventions
| When | Message | Observed effect |
|------|---------|-----------------|
| — | None (the match ran unattended; no live messages were sent) | — |

## Raw Stats
- Possession: 71% vs 29%
- Shots: 6 vs 3
- Shots on target: 2 vs 0
- Our commands: 350 total, 1078ms avg latency
- Their commands: 350 total, 525ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 310 | 89% |
| Press | 2 | 1% |
| Intercept | 0 | 0% |
| Mark | 0 | 0% |
| Pass | 20 | 6% |
| Shoot | 1 | 0% |
| Clear | 13 | 4% |
| GK Dist | 4 | 1% |

Opponent: Press 177 (51%), Intercept 68 (19%), Move 33 (9%), Pass 31 (9%), Shoot 18 (5%), Clear 18 (5%), GK Dist 5 (1%).

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 1157ms | | 100% |
| DEF (Turing) | 1082ms | | 100% |
| MID (Tesla) | 1159ms | | 100% |
| FWD1 (Hertz) | 968ms | | 100% |
| FWD2 (Lovelace) | 1037ms | | 100% |

Opponent: GK 209ms, DEF 212ms, MID 207ms, FWD **1024ms**, FWD **983ms**. MVP and fastest: their MID (Valdivia, 207ms). Most tactical: Shannon (70 commands).

## Per-Position Analysis

### GK
- Performance: strong
- What worked: Clean sheet, 0 on target against. 4 GK Dist.
- What failed: 1157ms, his slowest ever (range 620–707 before this match).
- Root cause: Platform-wide slowness this match (every agent of ours and both opposing forwards near 1s).

### DEF
- Performance: strong
- What worked: Clean sheet, 13 team CLEARs, 3 shots against.
- What failed: Nothing visible.
- Root cause: N/A.

### MID
- Performance: strong
- What worked: Opening goal at 1' from a gap behind their press.
- What failed: 1 SHOOT command for the team.
- Root cause: See Key Moment 5. Unknown whether he was shooting via another command type or the harness fell back to MOVE.

### FWD1
- Performance: adequate
- What worked: 968ms, fastest on the team. 71% possession means the swarm kept the ball in their half.
- What failed: No goal attributed.
- Root cause: N/A.

### FWD2
- Performance: adequate
- What worked: Possibly the "Unknown" goal.
- What failed: No FOLLOW or MARK logged this match, unlike C002's 71 FOLLOWs; off-ball rules barely fired at 71% possession.
- Root cause: N/A.

## Team-Level Observations
- Formation effectiveness: 2-0, clean sheet, 71% possession. v10 is 2-0 in competitive play (7 scored, 4 conceded).
- Should we change formation? No.
- Coordination gaps: none visible in the result; the command mix says the agents mostly MOVEd, which worked against a team that only pressed. Do not read the 89% MOVE as a tactic to keep.
- Opponent patterns: Speedy Gonzales is the same template as Nankatsu and Bright Auroras: PRESS 51%, INTERCEPT 19%, fast back three at ~210ms, forwards at ~1000ms. 0 shots on target. Weakest competitive opponent so far.
- Opponent formation: GK, DEF, MID, FWD, FWD.
- Competitive matches used: 3 of 10 (C001 was the deployment failure).

## Action Items
- [ ] Before the next competitive match, play one practice match and compare the command mix with C002 (SHOOT ~12%, PRESS ~5%, FOLLOW ~12%). If MOVE is above 80% again with normal latency, the v10 on-ball rules are collapsing into the one-step carry (MID rule 5, FWD1 rule 3) and v11 must remove the carry. If it only happens with ~1.1s latency, it is platform load. (priority: high)
- [ ] Scouting saved: `strategy/opponent-notes/speedy-gonzales.md`. (priority: low)

## Opponent Scouting Notes
- Saved to `strategy/opponent-notes/speedy-gonzales.md`.
