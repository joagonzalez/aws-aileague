# Match 004: vs Bright Artisans

## Result
- Score: 2 - 0 (WIN)
- Date: 2026-10-06
- Type: competitive
- Formation: 1-2-1 (platform setting since the match 012 test; this log originally said 1-1-2 by habit — corrected 2026-10-07)
- Strategy: Swarm
- Deploy tag: deploy-v10-2026-10-06
- Prompt versions deployed: GK v9, DEF v9, MID v8, FWD1 v8, FWD2 v9
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

We play as **Kernel Panic FC**. Unattended. Won, but see Key Moment 1: our prompts almost certainly did not run.

## Key Moments
1. **Every one of our agents answered in 201–209 ms.** Our healthy range is 600–1200 ms (C002: 658–940, C003: 968–1159, C005: 637–713). No LLM call on Haiku or Nova Lite 2 returns in 200 ms. Unlike C001 (33 ms, 52 commands), the command count was full (365) and the mix was MOVE 59% / PRESS 32% / PASS 5% / GK Dist 2% / CLEAR 2% with **0 SHOOT, 0 MARK, 0 INTERCEPT, 0 FOLLOW**. That mix is the same profile every opponent's ~200 ms back three shows (PRESS-heavy, no MARK). Conclusion: the platform's built-in default AI played this match for us, in a different failure mode from C001.
2. 1': Hertz (FWD) 1-0. 1': "Unknown" 2-0. Both inside the first minute, 6 shots, 2 on target, against a team that managed 1 shot.
3. Bright Artisans: PRESS 51%, INTERCEPT 16%, 0 MARK; back three at ~200 ms, forwards at 984 / 1008 ms. The standard template again.
4. Shots on target = goals, both teams (2 of 2 us, 0 of 0 them). 21 matches running.
5. 73 commands per agent: regulation length.

## Coach Interventions
| When | Message | Observed effect |
|------|---------|-----------------|
| — | None (the match ran unattended; no live messages were sent) | — |

## Raw Stats
- Possession: 75% vs 25%
- Shots: 6 vs 1
- Shots on target: 2 vs 0
- Our commands: 365 total, 199ms avg latency
- Their commands: 365 total, 510ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 217 | 59% |
| Press | 115 | 32% |
| Intercept | 0 | 0% |
| Mark | 0 | 0% |
| Pass | 19 | 5% |
| Shoot | 0 | 0% |
| Clear | 7 | 2% |
| GK Dist | 7 | 2% |

Opponent: Press 185 (51%), Intercept 59 (16%), Move 57 (16%), Pass 29 (8%), Clear 15 (4%), Shoot 13 (4%), GK Dist 7 (2%).

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 209ms | | 100% |
| DEF (Turing) | 205ms | | 100% |
| MID (Tesla) | 204ms | | 100% |
| FWD1 (Hertz) | 201ms | | 100% |
| FWD2 (Lovelace) | 209ms | | 100% |

Opponent: GK 205ms, DEF 203ms, MID 194ms, FWD **984ms**, FWD **1008ms**. MVP and fastest: their MID (Mercer, 194ms). Most tactical: Shannon (73 commands).

## Per-Position Analysis

### GK
- Performance: adequate
- What worked: Clean sheet (1 shot against).
- What failed: Nothing attributable to the prompt.
- Root cause: Prompt not running (Key Moment 1). No prompt conclusion from this match.

### DEF
- Performance: adequate
- What worked: Clean sheet.
- What failed: N/A.
- Root cause: Prompt not running.

### MID
- Performance: adequate
- What worked: N/A.
- What failed: 0 SHOOT commands for the team; Tesla had 17 goals in 11 matches on our prompts.
- Root cause: Prompt not running.

### FWD1
- Performance: strong
- What worked: Goal at 1'.
- What failed: N/A.
- Root cause: Prompt not running; the goal belongs to the default AI.

### FWD2
- Performance: adequate
- What worked: Possibly the "Unknown" goal.
- What failed: N/A.
- Root cause: Prompt not running.

## Team-Level Observations
- Formation effectiveness: Not measurable. The default AI won 2-0 with 75% possession against the weakest opponent so far (1 shot).
- Should we change formation? No. Change nothing because of this match.
- **Second deployment-failure signature.** C001: 33 ms, 52 commands (nothing ran). C004: ~200 ms, full command count, 0 SHOOT / MARK / INTERCEPT (default AI ran). Detection rule update: our agents under 300 ms means the prompts are not loaded, whatever the command count.
- **Scouting insight.** Every competitive opponent (Bright Auroras, Nankatsu, Speedy Gonzales, Bright Artisans, Pantera Onca) shows GK/DEF/MID at ~200 ms with a PRESS-heavy, no-MARK profile, and only the two forwards at ~1 s. The ~200 ms profile is what our own default-AI match looks like. Working hypothesis: most teams run real agents only on their forwards and the platform's default AI on the back three. Their back three cannot be out-thought, only out-shot; their forwards are LLM agents and slow.
- Candidate causes to check on the platform: whether v11 was pasted and "Redeploy" was mid-flight when the match started, whether the deployment showed as active, Bedrock throttling (five matches in a row for everyone at the same venue), or the readiness check.

## Action Items
- [ ] Platform: before every competitive match, open the agents page and confirm the deployment is active and shows our prompt text; run the readiness check. The first 15 seconds of the live stats tell the truth: under 300 ms per agent means the default AI is playing. (priority: high)
- [ ] Ask the organizers whether a full-count match with every agent at ~200 ms is a known fallback (model throttling, timeout fallback) and whether it is logged. (priority: high)
- [ ] Scouting: treat the ~200 ms back three of every opponent as the platform's default AI; plan to beat the default AI, not a human tactic. (priority: medium)

## Opponent Scouting Notes
- Saved to `strategy/opponent-notes/bright-artisans.md`.
