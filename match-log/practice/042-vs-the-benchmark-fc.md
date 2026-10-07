# Match 042: vs The Benchmark FC

## Result
- Score: 0 - 4 (LOSS)
- Date: 2026-10-07
- Type: practice
- Formation: 1-2-1
- Strategy: Swarm
- Deploy tag: deploy-v15-2026-10-07
- Prompt versions deployed: GK v14, DEF v14, MID v13, FWD1 v13, FWD2 v14
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

v15 validation match (intended vs Total Attack; played vs Benchmark). Coach watched; no live messages sent. **Gate failed: v15 rolled back, v14 redeployed for the competitive matches.**

## Key Moments
1. **1 shot, 0 on target, no Tesla goal**, 63% possession. On v14 Benchmark was beaten 5 times out of 5 (2-1, 6-3, 2-1, 4-3, 2-1) and Tesla scored in every one. Latency was healthy (686-1010 ms, Lovelace 1280), Shannon ours (686 ms). v15 is the only variable.
2. Jay Smooth (their FWD) scored all four, three of them in minute 2. 11 shots, 4 on target. Our PRESS 138 (36%), MOVE 154, PASS 12, GK Dist 1, SHOOT 33 commands for 1 shot.
3. Which edit did it is not readable from team totals. Candidates: (a) edit 3 fires against Benchmark's press (21%): a pressed Turing/Tesla lofts to Hertz instead of the short pass, and the lofts were not registering as PASS (12) or reaching anyone (1 shot); (b) the MID trims that moved the open/blocked and 'free' definitions into rules 1 and 3 may have changed how Haiku reads rules 4-6 (Tesla's shot switched off); (c) variance. With four competitive matches left there is no budget to separate them.
4. Coach: "way worse with Benchmark, we were easily winning them generally".

## Coach Interventions
| When | Message | Observed effect |
|------|---------|-----------------|
| — | None (watched, no messages sent) | — |

## Raw Stats
- Possession: 63% vs 37%
- Shots: 1 vs 11
- Shots on target: 0 vs 4
- Our commands: 385 total, 918ms avg latency
- Their commands: 385 total, 529ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 154 | 40% |
| Press | 138 | 36% |
| Intercept | 36 | 9% |
| Mark | 0 | 0% |
| Pass | 12 | 3% |
| Shoot | 33 | 9% |
| Clear | 11 | 3% |
| GK Dist | 1 | 0% |

"Clear" is CLEAR_OVERRIDE. Opponent: Move 193 (50%), Press 81 (21%), Pass 40 (10%), Intercept 27 (7%), Follow 19 (5%), Clear 15 (4%), Shoot 9 (2%), GK Dist 1 (0%).

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 686ms | | 100% |
| DEF (Turing) | 1010ms | | 100% |
| MID (Tesla) | 985ms | | 100% |
| FWD1 (Hertz) | 669ms | | 100% |
| FWD2 (Lovelace) | 1280ms | | 100% |

Opponent: GK 221ms (most tactical: Drew Midway, 77 commands), DEF 204ms (MVP, fastest: Norm Easy), MID 216ms, FWD 875ms, FWD 1063ms.

## Per-Position Analysis

### GK
- Performance: weak
- What worked: Ours this time (686 ms).
- What failed: 4 conceded from 4 on target; GK Dist 1.
- Root cause: Shots on target are goals; the shots came from a collapsed midfield.

### DEF
- Performance: weak
- What worked: Nothing visible.
- What failed: Jay Smooth four times.
- Root cause: Unknown from totals; v15's loft-when-pressed is the suspect that fires against Benchmark.

### MID
- Performance: weak
- What worked: Nothing visible.
- What failed: No goal, 1 team shot.
- Root cause: v15 MID changes (reorder, loft branch, definition trims): the only prompt whose shooting rules were touched in wording.

### FWD1
- Performance: weak
- What worked: 669 ms, central (no corner report).
- What failed: No shot.
- Root cause: No supply.

### FWD2
- Performance: weak
- What worked: Nothing visible.
- What failed: 1280 ms.
- Root cause: Platform load on his slot.

## Team-Level Observations
- Formation effectiveness: v15 0-1; v14 vs Benchmark 5-0. The gate ("nothing worse than v14's signature vs a balanced team") fails on shots (1 vs 3-9), goals (0 vs 2-6) and Tesla (0).
- Should we change formation? No. **Decision: roll back to v14 for the four remaining competitive matches.** deploy/platform-state.json now points every player at the v14 release files; deploy/paste-ready.md is v14 text again (verified against the deploy-v14 tag). current.md stays v15 as the record of the last approved release; a future v16 starts from v14's text, not v15's.
- Lesson: three edits at once cannot be separated with one match. Post-competition, if v15's ideas are revisited, one edit per practice match, Total Attack and Benchmark both.
- Opponent formation: GK, DEF, MID, FWD, FWD.

## Action Items
- [ ] Deploy v14 from deploy/paste-ready.md (now regenerated from the v14 files), confirm all five agents show it, export a backup. (priority: high)
- [ ] Competitive: first-15-second latency check; "be more aggressive and shoot!" at kick-off. (priority: high)
- [ ] Post-competition: v16 starts from the v14 text; test the v15 ideas one at a time. (priority: low)

## Opponent Scouting Notes
- `strategy/opponent-notes/the-benchmark-fc.md`.
