# Match 002: vs Nankatsu SC

## Result
- Score: 5 - 4 (WIN)
- Date: 2026-10-06
- Type: competitive
- Formation: 1-2-1 (platform setting since the match 012 test; this log originally said 1-1-2 by habit — corrected 2026-10-07)
- Strategy: Swarm
- Deploy tag: deploy-v10-2026-10-06
- Prompt versions deployed: GK v9, DEF v9, MID v8, FWD1 v8, FWD2 v9
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

We play as **Kernel Panic FC**. First match for the v10 release and the first competitive match in which our prompts demonstrably ran (615 commands, 730ms average, every agent 658–940ms: the healthy signature).

## Key Moments
1. 1': Tesla (MID) 1-0, "from midfield, exploiting Nankatsu's heavy PRESS_BALL commitment (332 commands) leaving gaps" (platform AI overview).
2. 1': Tsubasa Ozora (their MID) 1-1 and 2-1, both from midfield.
3. 1': Tesla 2-2. 1': Tsubasa 3-2, his third.
4. 2': Hertz (FWD1) 3-3. **The runner plan scored.** v10 made Hertz the runner a long pass ahead and told Tesla and Lovelace to feed him.
5. 2': "Unknown" 4-3 for us (platform could not attribute the position; candidates: Lovelace, Turing's long shot or Shannon's long kick. Coach to confirm).
6. 2': Hertz 5-3, "capitalizing on Nankatsu's defensive fatigue from constant pressing". 2': Taro Misaki (their FWD) 5-4.
7. 123 commands per agent (Shannon, "most tactical", 123) against 70 per agent in C003: this match went long (overtime after the 3-3), so regulation is about 70 ticks (~2.5 minutes), not the 5 minutes the workshop docs state.
8. Shots on target = goals for both teams again (us 5 of 5, them 4 of 4). 19 matches running.

## Coach Interventions
| When | Message | Observed effect |
|------|---------|-----------------|
| — | None (the match ran unattended; no live messages were sent) | — |

## Raw Stats
- Possession: 47% vs 53%
- Shots: 8 vs 8
- Shots on target: 5 vs 4
- Our commands: 615 total, 730ms avg latency
- Their commands: 615 total, 514ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 330 | 54% |
| Press | 30 | 5% |
| Intercept | 0 | 0% |
| Mark | 3 | 0% |
| Pass | 67 | 11% |
| Shoot | 73 | 12% |
| Clear | 35 | 6% |
| GK Dist | 6 | 1% |

Also logged for us: Follow 71 (12%). No prompt of ours names FOLLOW; the likeliest sources are Lovelace's v9 rule 6 (MARK their midfielder, logged as only 3 MARKs) and the shared "INTERCEPT the pass to the opponent closest to the carrier" rule (0 INTERCEPTs), both of which the harness may translate into FOLLOW_PLAYER on that opponent.

Opponent: Press 332 (54%), Intercept 99 (16%), Shoot 78 (13%), Move 56 (9%), Clear 34 (6%), Pass 11 (2%), GK Dist 5 (1%).

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 658ms | | 100% |
| DEF (Turing) | 667ms | | 100% |
| MID (Tesla) | 940ms | | 100% |
| FWD1 (Hertz) | 683ms | | 100% |
| FWD2 (Lovelace) | 689ms | | 100% |

Opponent: GK 205ms, DEF 187ms, MID 188ms, FWD **930ms**, FWD **979ms**. MVP and fastest: their DEF (Kazuo Tachibana, 187ms). Most tactical: Shannon (123 commands).

## Per-Position Analysis

### GK
- Performance: adequate
- What worked: Released quickly (6 GK Dist, PASS 67 team-wide, the highest ever). 658ms.
- What failed: Conceded 4, three of them long shots from midfield by a 188ms MID.
- Root cause: Rule 1 (INTERCEPT shots inside our box, stay on the line) is the right rule against long shots, but every shot on target is a goal on this engine; the only defence is a presser on their MID before he shoots. With PRESS at 30 for the whole team, he was rarely pressed.

### DEF
- Performance: adequate
- What worked: 667ms. Team CLEAR 35, no goal attributed to a mistake of his.
- What failed: Their MID scored three times from midfield. DEF v9 rule 8 presses the central carrier in our half only when he is the opponent nearest our goal; a MID shooting from around the halfway line with a forward ahead of him is never that carrier, so DEF holds his spot and nobody closes the shooter.
- Root cause: Prompt rule gap (the "nearest our goal" guard), plus the swarm's press not triggering (see MID).

### MID
- Performance: strong
- What worked: Two goals at 1', both long shots from midfield (16 in 10 matches). Team SHOOT 73 (12%), up from 19 in match 017: the v8 shooting rule without the teammate clause works. PASS 67 team-wide, so the long ball to Hertz was being played.
- What failed: PRESS 30 and INTERCEPT 0 for the team. Rule 6 makes him the first presser when nearest; he was nearest rarely, or the harness mapped the press to MOVE (330 MOVEs).
- Root cause: Unknown without per-agent counts. Watch his off-ball behaviour in the next match.

### FWD1
- Performance: strong
- What worked: **Two goals at 2'**, both after the runner plan put him ahead of the ball. First Hertz goals since 016.
- What failed: Nothing visible.
- Root cause: N/A.

### FWD2
- Performance: adequate
- What worked: 689ms, the fastest Lovelace has ever been. Possibly the "Unknown" goal.
- What failed: MARK their midfielder (rule 6) shows as 3 MARKs; 71 FOLLOWs suggest the harness ran it as FOLLOW_PLAYER, which shadows at a distance rather than tight-marking. Their MID scored three times.
- Root cause: Command mapping of "MARK" on this harness; to confirm with the per-agent view if the platform has one.

## Team-Level Observations
- Formation effectiveness: Won 5-4. Attack is the best it has been: 5 goals from 8 shots, 73 SHOOT commands, 67 PASSes, goals from MID and the runner.
- Should we change formation? No. The v10 attacking roles are validated (Tesla 2, Hertz 2, one unattributed).
- Coordination gaps: the defensive layer thinned out under v10. PRESS fell from 158 (017) to 30, INTERCEPT from 20 to 0, and we conceded 4 after conceding 2 in the previous four practice matches combined. Only one swarm player presses at a time by design, Hertz is now too far ahead to ever be the nearest, and DEF presses only the carrier nearest our goal. A MID shooting from midfield with a forward beyond him is pressed by nobody.
- Platform Coach's Corner for us: "Increase INTERCEPT from 0 to 40+ and add MARK (currently 3)".
- Opponent patterns: Nankatsu is press-and-shoot (PRESS 54%, INTERCEPT 16%, PASS 2%); fast back three at ~190ms, slow forwards at ~950ms. Same signature as Benchmark FC and Bright Auroras: the human teams appear to run the workshop sample prompts (PRESS_BALL at maximum intensity, INTERCEPT always on). Their gaps behind the press are where our goals came from.
- Opponent formation: GK, DEF, MID, FWD, FWD.
- Health check passed: 615 commands, 658–940ms. The C001 failure did not recur.

## Action Items
- [ ] v11 brief: close the long-shot gap. DEF presses any carrier in our half between the sides of our box whose line to our goal is clear, not only the one nearest our goal; the swarm presser rule needs a trigger that fires (their MID with the ball in or near our half → nearest of MID/FWD2 presses, no exceptions). Keep every attacking rule as is. (priority: high)
- [ ] v11 brief: write the intercept job as "INTERCEPT" with a clear trigger (a pass is being played across you) rather than "the pass to the opponent closest to him", which the harness seems to run as FOLLOW. See `strategy/platform-reference.md`. (priority: high)
- [ ] Check whether the platform shows a per-agent command breakdown; it would settle where the 71 FOLLOWs and 330 MOVEs come from. (priority: medium)
- [ ] Scouting saved: `strategy/opponent-notes/nankatsu-sc.md`. (priority: low)

## Opponent Scouting Notes
- Saved to `strategy/opponent-notes/nankatsu-sc.md`.
