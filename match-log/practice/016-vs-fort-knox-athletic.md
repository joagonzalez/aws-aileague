# Match 016: vs Fort Knox Athletic

## Result
- Score: 4 - 0 (WIN)
- Date: 2026-10-06
- Type: practice
- Formation: 1-2-1 (platform setting since the match 012 test; this log originally said 1-1-2 by habit — corrected 2026-10-07)
- Strategy: Swarm
- Deploy tag: deploy-v9-2026-10-06
- Prompt versions deployed: GK v8, DEF v8, MID v7, FWD1 v7, FWD2 v8
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

## Key Moments
1. Same setup as 014 and 015, pasted from `deploy/paste-ready.md`. First match against Fort Knox since the 0-1 loss in 008.
2. 1': Hertz (FWD) scored. Our first minute-1 goal since 013, and the first match this season in which we scored first in minute 1 without conceding.
3. 2': Tesla (MID), then Hertz again, then Tesla: 4-0 after two minutes. Hertz now has 3 goals in 3 matches on the FWD2 v7 text.
4. **Zero SHOOT commands, 5 shots, 4 on target, 4 goals.** Same as 008 (0 SHOOT, 4 shots): the platform counts something other than SHOOT as shots, probably passes or clears toward goal. Platform Coach's Corner asks us to add deliberate finishing instructions.
5. MARK 175 (40%), the same share as the 0-1 loss in 008 against the same opponent, but this time with 66 PASS and 4 goals. Against a possession side the MARK rules (DEF rule 7, FWD2 rule 5) fire constantly; in 008 that was read as passive, here it won.
6. Fort Knox: 310 MOVE (70%), zero MARK, zero INTERCEPT, 2 shots, 0 on target. Two slow forwards (870ms, 927ms; avg 459ms).
7. The coach typed "be more aggressive and shoot!" repeatedly throughout, as in 015.

## Coach Interventions
| When | Message | Observed effect |
|------|---------|-----------------|
| Throughout, repeated | Be more aggressive and shoot! | Sent many times from kickoff. 0 SHOOT commands were logged, yet 4 of 5 shots went in, so the message did not act through SHOOT here. Same message as in 015. |

## Raw Stats
- Possession: 48% vs 52%
- Shots: 5 vs 2
- Shots on target: 4 vs 0
- Our commands: 440 total, 809ms avg latency
- Their commands: 440 total, 459ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 75 | 17% |
| Press | 59 | 13% |
| Intercept | 30 | 7% |
| Mark | 175 | 40% |
| Pass | 66 | 15% |
| Shoot | 0 | 0% |
| Clear | 25 | 6% |
| GK Dist | 10 | 2% |

Opponent: Move 310 (70%), Pass 39 (9%), Press 30 (7%), Shoot 29 (7%), Clear 22 (5%), GK Dist 10 (2%). No marks or intercepts.

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 634ms | | 100% |
| DEF (Turing) | 851ms | | 100% |
| MID (Tesla) | 972ms | | 100% |
| FWD1 (Hertz) | 590ms | | 100% |
| FWD2 (Lovelace) | 879ms | | 100% |

Opponent: GK 193ms, DEF 198ms, MID 196ms, FWD **870ms**, FWD **927ms**. MVP, fastest and most tactical: their GK (Pat Bunker, 193ms, 88 commands).

## Per-Position Analysis

### GK
- Performance: strong
- What worked: Clean sheet, 0 on target against. 10 GK Dist (so GK releases are reported as GK Dist whether the prompt says PASS or not).
- What failed: Nothing.
- Root cause: Fort Knox never got a shot on target; the shape in front of him did the work.

### DEF
- Performance: strong
- What worked: Clean sheet. 851ms. A large share of the 175 MARKs and 66 PASSes: pass-by-default worked against a team that does not press.
- What failed: Nothing.
- Root cause: v8 rules 2 and 7 as designed.

### MID
- Performance: strong
- What worked: Two goals at 2'. 972ms.
- What failed: Nothing.
- Root cause: Long shots again. Tesla: 13 goals in 009–016.

### FWD1
- Performance: strong
- What worked: Two goals (1', 2'). 590ms, the fastest reading any of our agents has had.
- What failed: Nothing.
- Root cause: The FWD2 v7 text fits his agent. Three matches, three goals.

### FWD2
- Performance: adequate
- What worked: 879ms. Part of the MARK count (rule 5 marks their midfielder when they have the ball).
- What failed: No goal; behavior not reported.
- Root cause: By design.

## Team-Level Observations
- Formation effectiveness: 4-0, the biggest win of the season, with 48% possession.
- Should we change formation? No. **The v9 setup is now validated against all three AI teams: 1-0 Benchmark, 3-2 Total Attack, 4-0 Fort Knox.** Season record 7W 1D 8L; this setup 3W 0L, 8 goals for, 2 against.
- Coordination gaps: none visible in the result. Note the command mix swings completely with the opponent (015: 0 PASS, 0 MARK, 58 SHOOT; 016: 66 PASS, 175 MARK, 0 SHOOT) with identical prompts and the same live message. Command counts describe the opponent as much as our prompts.
- Opponent patterns: Fort Knox plays MOVE-only (70%) with no marking or intercepting; their GK is their best player. Two slow forwards.
- Opponent formation: Unknown.
- Shots on target = goals in every match for both sides, 16 matches running (us 4/4, them 0/0 here).

## Action Items
- [ ] Freeze the setup and commit/tag the state before competitive play. (priority: high)
- [ ] Competitive routine: paste from `deploy/paste-ready.md`, check the five model dropdowns, redeploy, and send "be more aggressive and shoot!" from kickoff. (priority: high)
- [ ] Record the scorers, minutes and the coach's message in every competitive log. (priority: high)
- [ ] After the first two competitive matches, revisit: the opposing-GK long ball (4 goals against), and a FWD1 v8 release that is Hertz's FWD2 v7 text with the labels switched. No prompt changes before then. (priority: medium)

## Opponent Scouting Notes
- Saved to `strategy/opponent-notes/fort-knox-athletic.md`.
