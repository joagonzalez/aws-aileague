# Match 043: vs Fort Knox Athletic

## Result
- Score: 2 - 0 (WIN)
- Date: 2026-10-07
- Type: practice
- Formation: 1-2-1
- Strategy: Swarm
- Deploy tag: deploy-v14-2026-10-07
- Prompt versions deployed: GK v13, DEF v13, MID v12, FWD1 v12, FWD2 v13
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

Coach watched; no live messages sent. v14 redeployed after the v15 rollback. Goals: 1': Tesla 1-0. 2': Tesla 2-0.

## Key Moments
1. v14 redeployed after the v15 rollback (platform export verified). Won 2-0, Tesla twice, 0 on target against.
2. **Platform very slow: 219 commands (44 per agent, normal 75-120), 1402 ms average, Lovelace 2442 ms, Turing 1303 ms.** Above the 2 s tick an agent misses decisions and holds its last command: this is the 'Lovelace freezes in midfield' the coach saw. Hertz 625 ms, Tesla 954.
3. MARK 95 (43%), PASS 33, SHOOT 0 commands for 3 shots (the Fort Knox profile).

## Coach Interventions
| When | Message | Observed effect |
|------|---------|-----------------|
| — | None (watched, no messages sent) | — |

## Raw Stats
- Possession: 53% vs 47%
- Shots: 3 vs 2
- Shots on target: 2 vs 0
- Our commands: 219 total, 1402ms avg latency
- Their commands: 220 total, 533ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 34 | 16% |
| Press | 24 | 11% |
| Intercept | 17 | 8% |
| Mark | 95 | 43% |
| Pass | 33 | 15% |
| Shoot | 0 | 0% |
| Clear | 11 | 5% |
| GK Dist | 5 | 2% |

"Clear" is CLEAR_OVERRIDE.

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 655ms | | 100% |
| DEF (Turing) | 1303ms | | 100% |
| MID (Tesla) | 954ms | | 100% |
| FWD1 (Hertz) | 625ms | | 100% |
| FWD2 (Lovelace) | 2442ms | | 100% |

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
- `strategy/opponent-notes/fort-knox-athletic.md`.
