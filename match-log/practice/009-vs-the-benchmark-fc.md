# Match 009: vs The Benchmark FC

## Result
- Score: 1 - 2 (LOSS)
- Date: 2026-10-05
- Type: practice
- Formation: 1-1-2
- Strategy: Swarm
- Deploy tag: deploy-v8-2026-10-05
- Prompt versions deployed: GK v8, DEF v8, MID v7, FWD1 v7, FWD2 v7
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Claude Haiku, FWD2 unconfirmed (Sonnet planned)

## Key Moments
1. 2': Benchmark's GK (Drew Midway) scored from his own end. Opposing GKs have now scored in 006, 007 and 009.
2. 2': Tesla (MID) equalized. MID's "shoot from the middle" rule produced a goal.
3. 3': Benchmark scored the winner (scorer unknown).
4. Recurring (coach): Hertz and Lovelace still "useless players", even with the v8 swarm rules. Coach's answers to the watch list: do the forwards stay with the group? **No.** Do they pass instead of running wide? **No.** The v8 swarm and pass-first rules did not reach the forwards' behavior.
5. Models: the coach was told to test Lovelace on Sonnet. Not confirmed which model he actually ran on. FWD2's 828ms is lower than any of his Haiku readings (893–999).

## Coach Interventions
<!-- Not reported. Fill in, or write "None". -->
| When | Message | Observed effect |
|------|---------|-----------------|
| [minute] | [what you typed] | [what changed after it] |

## Raw Stats
- Possession: 35% vs 65%
- Shots: 3 vs 4
- Shots on target: 1 vs 2
- Our commands: 434 total, 837ms avg latency
- Their commands: 435 total, 188ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 195 | 45% |
| Press | 122 | 28% |
| Intercept | 47 | 11% |
| Mark | 2 | 0% |
| Pass | 24 | 6% |
| Shoot | 16 | 4% |
| Clear | 23 | 5% |
| GK Dist | 5 | 1% |

Opponent: Move 197 (45%), Press 191 (44%), Pass 24 (6%), Clear 17 (4%), GK Dist 6 (1%).

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 644ms | | 100% |
| DEF (Turing) | 1148ms | | 100% |
| MID (Tesla) | 870ms | | 100% |
| FWD1 (Hertz) | 641ms | | 100% |
| FWD2 (Lovelace) | 828ms | | 100% |

Opponent: GK 212ms, DEF 207ms, MID 207ms, FWD 218ms, FWD 206ms. MVP and fastest player: their FWD (Kim Poise, 206ms).

## Per-Position Analysis

### GK
- Performance: weak
- What worked: 644ms.
- What failed: Their GK scored from his own end again (third time in four matches).
- Root cause: Unknown, and now the most repeatable leak we have. The coach needs to see what Shannon does when their GK kicks long.

### DEF
- Performance: adequate
- What worked: 100% success.
- What failed: 1148ms, slowest again. 24 passes team-wide despite v8's pass-by-default.
- Root cause: Low possession (35%) left little to pass.

### MID
- Performance: adequate
- What worked: Scored the equalizer at 2' from the middle (v7 MID rule 1). 870ms.
- What failed: 35% possession.
- Root cause: The swarm didn't hold the ball under Benchmark's 44% press.

### FWD1
- Performance: weak
- What worked: 641ms.
- What failed: (coach) still a "useless player".
- Root cause: Five versions of forward rules (v3–v8) have not changed what the coach sees. See Team-Level.

### FWD2
- Performance: weak
- What worked: 828ms.
- What failed: (coach) still a "useless player".
- Root cause: As FWD1. Model unconfirmed.

## Team-Level Observations
- **Getting worse, not better:** W 1-0 (v1), D 2-2 (v3), W 2-1 (v4), then L 0-3, 0-1, 2-3, 0-2, 0-1, 1-2. Six straight losses since v4. Prompts grew from ~1500 to ~2900 chars and from ~6 to ~9 rules over the same period. There's no evidence the added complexity helped, and it may have hurt.
- **Forward behavior is unchanged by wording.** Five forward rewrites (v3, v4, v5, v7, v8) ended in the same coach verdict. The remaining levers: the model (being tested), and what kind of command we ask for (see the next point).
- **Hypothesis: fixed positions go stale; tracking commands don't.** A MOVE_TO a spot is fixed when issued and stays wrong for the ~0.65–1.1 s until the next decision, so players overshoot to stale places (corners). PRESS (chase the ball), MARK and INTERCEPT keep tracking their target between decisions. Our prompts since v4 are full of "move to your spot". MOVE has been 36–45% of our commands.
- **Opposing goalkeepers scoring from their own end** (006, 007, 009) is our most repeatable leak.

## Action Items
- [ ] Models: next match tests the forwards on Sonnet and Nova Lite 2 with v8 prompts unchanged (coach). Record which forward ran which model. (priority: high)
- [ ] Control: if the model test doesn't help, replay v4 (our best result) against Benchmark to separate "our prompts got worse" from opponent/variance noise. (priority: high)
- [ ] GK: observe what Shannon does when the opponent GK kicks long. (priority: high)
- [ ] v9 direction (pending tests): fewer, simpler rules built on tracking commands (PRESS/MARK/INTERCEPT, PASS/SHOOT) instead of "move to a spot". (priority: medium)

## Opponent Scouting Notes
- Saved to `strategy/opponent-notes/the-benchmark-fc.md`.
