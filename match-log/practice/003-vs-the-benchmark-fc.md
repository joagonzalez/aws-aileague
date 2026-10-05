# Match 003: vs The Benchmark FC

## Result
- Score: 2 - 1 (WIN)
- Date: 2026-10-05
- Type: practice
- Formation: 1-1-2
- Strategy: Counter
- Deploy tag: deploy-v4-2026-10-05
- Prompt versions deployed: GK v4, DEF v4, MID v4, FWD1 v4, FWD2 v4
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Claude Haiku, FWD2 Claude Haiku

## Key Moments
1. 1': Benchmark scored first (scorer unknown) during a chaotic, high-tempo opening.
2. 2': Turing (DEF) scored from a turnover. The platform credits our INTERCEPT-led recovery against Benchmark's lack of intercepts.
3. 3': Hertz (FWD1) scored after the defense won the ball back.
4. Rest of the match: no more goals. Every goal in matches 001 and 003 came in the first 3 minutes.
5. Recurring (coach observation): Turing was unstable. He ran toward our own GK and did not pass.
6. Recurring (coach observation): GK and Turing passed the ball back and forth to each other and never connected with MID or the forwards. Both kept moving toward our own goal.
7. Platform Coach's Corner for us: increase SHOOT relative to MOVE. We created few clear chances despite 54% possession and won through "defensive recycling".

## Coach Interventions
<!-- Not reported yet: were the suggested messages to Turing/Shannon sent? Fill in, or write "None". -->
| When | Message | Observed effect |
|------|---------|-----------------|
| [minute] | [what you typed] | [what changed after it] |

## Raw Stats
- Possession: 54% vs 46%
- Shots: 3 vs 5
- Shots on target: 2 vs 1
- Our commands: 510 total, 829ms avg latency
- Their commands: 510 total, 196ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 200 | 39% |
| Press | 141 | 28% |
| Intercept | 79 | 15% |
| Mark | 1 | 0% |
| Pass | 37 | 7% |
| Shoot | 20 | 4% |
| Clear | 24 | 5% |
| GK Dist | 8 | 2% |

Opponent: Move 299 (59%), Press 143 (28%), Pass 38 (7%), Clear 21 (4%), GK Dist 9 (2%). Still no intercepts or marks.

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 640ms | | 100% |
| DEF (Turing) | 852ms | | 100% |
| MID (Tesla) | 968ms | | 100% |
| FWD1 (Hertz) | 678ms | | 100% |
| FWD2 (Lovelace) | 980ms | | 100% |

Opponent: GK 212ms, DEF 195ms, MID 219ms, FWD 206ms, FWD 209ms (all 100%). Platform MVP and fastest player: their DEF (Norm Easy, 195ms).

## Per-Position Analysis

### GK
- Performance: adequate
- What worked: Conceded only at 1'. Fastest agent (640ms). GK Dist went from 0 to 8, confirming the v4 hypothesis that the verb "distribute" maps to the GK Dist command.
- What failed: Distribution went short to Turing, starting the GK↔DEF back-and-forth. The ball rarely reached MID or the forwards.
- Root cause: v4 rule 2 "distribute it long to FWD1 or FWD2". The distribute command seems to go to the nearest or easiest teammate (Turing, who stands deep), not long. v3's "kick it long", which was read as CLEAR, actually moved the ball upfield. The v4 change optimized a command count (GK Dist) instead of the outcome. Lesson: command counts are clues, not goals.

### DEF
- Performance: adequate
- What worked: Scored at 2' from a turnover. The middle-lane shape held: one goal conceded (at 1') against 2 in match 002. 852ms, down from 1020ms.
- What failed: Unstable, drifting toward our own goal. Passed back to GK instead of forward. Moved with the ball instead of releasing it.
- Root cause: (1) Every v4 positioning target points deep: rule 6 (goal-side of the attacker closest to our goal), rule 8 (in front of our box on the ball-to-goal line) and rule 4 (stay between carrier and goal). The targets are recomputed every decision, hence the jitter, and they leave Turing next to the GK. (2) Rule 2 says "PASS forward to MID or a forward if unmarked, otherwise CLEAR", but nothing forbids passing to the GK or moving with the ball. Under the press, the GK is the only free teammate nearby. With ~0.85 s per decision, a MOVE issued just before he won the ball carries him backward with it.

### MID
- Performance: adequate
- What worked: Haiku this time: 968ms against 1050ms on Sonnet. Part of 79 intercepts.
- What failed: Rarely got the ball from the back (GK/DEF recycling). Only 1 MARK command team-wide even though v4 makes MARK MID's and DEF's default.
- Root cause: Build-up was stuck behind MID. The MARK rules lose to MOVE-type rules in practice (to be checked).

### FWD1
- Performance: strong
- What worked: Scored at 3'. 678ms. No corner-running reported.
- What failed: Few chances (3 team shots). SHOOT commands fell from 37 to 20.
- Root cause: The ball seldom reached the attacking third because of the back-line recycling.

### FWD2
- Performance: adequate
- What worked: 100% success.
- What failed: 980ms, still the slowest forward on the same model as FWD1. Few chances.
- Root cause: Same supply problem as FWD1.

## Team-Level Observations
- Formation effectiveness: 1-1-2 with v4's middle lane: first win since match 001 and first time above 50% possession. Opponent shots on target dropped to 1. The formation switch rule did not trigger (conceded 1, not through an open middle).
- Should we change formation? No. Fix the build-up first.
- Coordination gaps: GK↔DEF loop. Neither prompt forbids passing to the other, both stand deep, and MID/forwards are marked by the press. The 54% possession is partly this sterile recycling ("won via defensive recycling").
- Opponent patterns: Move-heavy (59%), press 28%, still zero intercepts. Their DEF was the platform MVP at 195ms.
- Opponent formation: Unknown.
- Latency: 829ms average (863 in 002, 813 in 001). Same-model (Haiku) comparisons from v3 to v4: GK 707→640, DEF 1020→852, FWD1 713→678, FWD2 999→980, even though DEF, FWD1 and FWD2 prompts got longer. No sign that prompt length drives latency. Platform variance dominates. MID on Haiku 968 vs Sonnet 1050.
- Timing: all goals in matches 001 and 003 came in the first 3 minutes. Record goal minutes in every match to see if this pattern holds.

## Action Items
- [ ] GK: CLEAR long upfield toward the forwards when holding the ball. Never distribute or pass to DEF. (priority: high)
- [ ] DEF: Never pass to GK. Never MOVE while holding the ball: PASS to a clearly free teammate further upfield, otherwise CLEAR long. (priority: high)
- [ ] DEF: One stable default spot, higher than the edge of our box, while keeping the middle-lane protection that held in this match. (priority: high)
- [ ] Specs: Reviewer lesson. A command count (e.g. GK Dist) is a clue, not a target. Judge prompt changes by the on-pitch outcome. (priority: medium)
- [ ] Shooting: SHOOT fell from 37 to 20 with 3 shots. Re-check after the build-up fix before changing the shooting trigger again. (priority: medium)
- [ ] Debrief: Record whether the suggested coach messages were sent. (priority: medium)

## Opponent Scouting Notes
- Saved to `strategy/opponent-notes/the-benchmark-fc.md`.
