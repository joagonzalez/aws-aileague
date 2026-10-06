# Match 011: vs The Benchmark FC

## Result
- Score: 2 - 1 (WIN)
- Date: 2026-10-05
- Type: practice
- Formation: 1-1-2
- Strategy: Swarm
- Deploy tag: deploy-v8-2026-10-05
- Prompt versions deployed: GK v8, DEF v8, MID v7, FWD1 v7, FWD2 v7
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Claude Sonnet

## Key Moments
1. Same setup as match 010 (assumed: v8, Hertz on Nova Lite 2, Lovelace on Sonnet).
2. 2': Benchmark's DEF (Norm Easy) scored.
3. 2': Tesla (MID) equalized.
4. The score was 1-1 when the scoreboard showed **OVERTIME** (coach screenshot), so regulation time is very short (~2 minutes).
5. 3': Tesla scored the winner.
6. Coach screenshot: Lovelace stood **frozen in the far corner** while play was on the other side of the pitch, on Sonnet. A stronger model did not fix the forwards' positioning.
7. Benchmark again had one slow FWD (869ms; 853ms in 010), average 336ms. Our last two wins came against a weakened Benchmark.

## Coach Interventions
<!-- Not reported. Fill in, or write "None". -->
| When | Message | Observed effect |
|------|---------|-----------------|
| [minute] | [what you typed] | [what changed after it] |

## Raw Stats
- Possession: 41% vs 59%
- Shots: 5 vs 8
- Shots on target: 2 vs 1
- Our commands: 420 total, 887ms avg latency
- Their commands: 420 total, 336ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 201 | 48% |
| Press | 118 | 28% |
| Intercept | 48 | 11% |
| Mark | 0 | 0% |
| Pass | 15 | 4% |
| Shoot | 18 | 4% |
| Clear | 17 | 4% |
| GK Dist | 3 | 1% |

Opponent: Move 227 (54%), Press 152 (36%), Pass 17 (4%), Clear 13 (3%), Shoot 8 (2%), GK Dist 3 (1%).

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 642ms | | 100% |
| DEF (Turing) | 892ms | | 100% |
| MID (Tesla) | 993ms | | 100% |
| FWD1 (Hertz) | 666ms | | 100% |
| FWD2 (Lovelace) | 918ms | | 100% |

Opponent: GK 200ms, DEF 202ms, MID 202ms, FWD **869ms**, FWD 207ms. MVP: their GK (Drew Midway).

## Per-Position Analysis

### GK
- Performance: strong
- What worked: Conceded 1 from 1 shot on target (8 shots against). 642ms.
- What failed: Their DEF scored at 2'.
- Root cause: Long-range goals from deep players remain the opponents' main route.

### DEF
- Performance: adequate
- What worked: 892ms.
- What failed: Their DEF (Norm Easy) scored, probably from distance.
- Root cause: See GK.

### MID
- Performance: strong
- What worked: Scored both goals (2', 3'). That's 6 goals in matches 009–011, mostly long shots.
- What failed: 993ms.
- Root cause: MID rule 1 (long-range reading) is our best weapon.

### FWD1
- Performance: weak
- What worked: 666ms (Nova Lite 2).
- What failed: No goals since match 006.
- Root cause: The forwards' positioning problem is model-independent (see FWD2).

### FWD2
- Performance: weak
- What worked: 100% success.
- What failed: Frozen in the far corner (coach screenshot). 918ms on Sonnet (809 in 010).
- Root cause: Hypothesis: his "move to a spot" targets (right of center, right post, in front of their goal) end up off the pitch, and the game pins him at the edge. A corner is two edges at once. This fits every version and both models. Forwards should only get actions aimed at something on the pitch (ball, teammates, opponents).

## Team-Level Observations
- **Three wins in a row** (010, 011 with forwards on Nova Lite 2/Sonnet). Both came against a Benchmark with one slow FWD, so test against Fort Knox / Total Attack.
- **Tesla is our scorer, the forwards aren't.** Our goals since 006: Hertz 1, Turing 1, Tesla 6.
- **Matches are ~2 minutes of regulation,** then overtime if tied. Every goal happens in minutes 1–3, so the first seconds matter most.
- **Sonnet costs no speed:** Lovelace 809 and 918ms on Sonnet vs 893–999 on Haiku.

## Action Items
- [ ] Formation: test 1-2-1 (coach decision). Lovelace becomes a second long-shooting MID, Hertz is the single FWD. (priority: high)
- [ ] FWD (v9): remove all "move to a spot" instructions. Use only actions aimed at the ball, teammates or opponents. (priority: high)
- [ ] Test against Fort Knox / Total Attack, since both recent wins came against a weakened Benchmark. (priority: high)

## Opponent Scouting Notes
- Saved to `strategy/opponent-notes/the-benchmark-fc.md`.
