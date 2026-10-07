# Match 044: vs The Benchmark FC

## Result
- Score: 1 - 0 (WIN)
- Date: 2026-10-07
- Type: practice
- Formation: 1-2-1
- Strategy: Swarm
- Deploy tag: deploy-v14-2026-10-07
- Prompt versions deployed: GK v13, DEF v13, MID v12, FWD1 v12, FWD2 v13
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

Coach watched; no live messages sent. v14 redeployed after the v15 rollback. Goals: 1': Tesla 1-0.

## Key Moments
1. Won 1-0, Tesla; Benchmark 2 shots, 0 on target.
2. **Slowest match on record: 158 commands (32 per agent), 1592 ms average, Turing 1988 ms, Lovelace 1865 ms, Shannon 1003 ms.** Only Hertz (657) was in his normal range. Benchmark's own forwards were slow too (1316 ms).
3. Coach: Tesla sometimes does not sprint in midfield and opponents reach him; Lovelace freezes. At 1064 ms Tesla's every decision lands a second late against 215 ms opponents; at 1865-2442 ms Lovelace misses about half his ticks. No prompt wording changes that.

## Coach Interventions
| When | Message | Observed effect |
|------|---------|-----------------|
| — | None (watched, no messages sent) | — |

## Raw Stats
- Possession: 44% vs 56%
- Shots: 5 vs 2
- Shots on target: 1 vs 0
- Our commands: 158 total, 1592ms avg latency
- Their commands: 160 total, 664ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 60 | 38% |
| Press | 60 | 38% |
| Intercept | 17 | 11% |
| Mark | 0 | 0% |
| Pass | 10 | 6% |
| Shoot | 7 | 4% |
| Clear | 4 | 3% |
| GK Dist | 0 | 0% |

"Clear" is CLEAR_OVERRIDE.

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 1003ms | | 100% |
| DEF (Turing) | 1988ms | | 100% |
| MID (Tesla) | 1064ms | | 100% |
| FWD1 (Hertz) | 657ms | | 100% |
| FWD2 (Lovelace) | 1865ms | | 100% |

## Per-Position Analysis

### GK
- Performance: adequate
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: platform latency (see Key Moments).

### DEF
- Performance: adequate
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: platform latency (see Key Moments).

### MID
- Performance: adequate
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: platform latency (see Key Moments).

### FWD1
- Performance: adequate
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: platform latency (see Key Moments).

### FWD2
- Performance: adequate
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: platform latency (see Key Moments).

## Team-Level Observations
- v14 after the rollback: 2-0, 1-0 with the platform at 1400-1600 ms average and half the normal command count. Both behaviours the coach saw (Lovelace freezing, Tesla reached before he moves) are latency: a decision above 2 s misses the tick and the player holds his last command.
- Decision: no prompt change before the competitive matches (v15's untested change cost a validation match). Play when the platform is fast; check the first-15-second latency.
- Opponent formation: GK, DEF, MID, FWD, FWD.

## Action Items
- [ ] Competitive: first-15-second latency check; if our agents are above ~1050 ms, expect missed ticks; "be more aggressive and shoot!" at kick-off. (priority: high)
- [ ] Post-competition v16 candidates (one per practice match): Tesla sprints on his support move (rule 9) and his on-ball "nobody within a few steps" shot relaxed to "no opponent within a step"; Lovelace's model (Haiku 893-999 ms, Nova Lite 2 840-1276, Sonnet 809: none fast). (priority: low)

## Opponent Scouting Notes
- `strategy/opponent-notes/the-benchmark-fc.md`.
