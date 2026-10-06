# Match 012: vs The Benchmark FC

## Result
- Score: 1 - 2 (LOSS)
- Date: 2026-10-05
- Type: practice
- Formation: 1-2-1
- Strategy: Swarm
- Deploy tag: deploy-v8-2026-10-05
- Prompt versions deployed: GK v8, DEF v8, MID v7, FWD1 v7, FWD2 v7
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 unconfirmed, FWD2 unconfirmed

## Key Moments
1. **Quick 1-2-1 test:** formation set to 1-2-1, and Hertz ran **Tesla's MID v7 prompt** as a second midfielder. Lovelace was the single forward (FWD v7). The prompts were not adapted to 1-2-1 (coach). The "FWD1 v7" above is wrong for Hertz: he ran mid/v7.
2. The platform report still listed our players as GK, DEF, MID, FWD, FWD. The formation setting may not change player roles, only the starting layout.
3. 1': Kernel Panic scored (scorer unknown).
4. 2': Benchmark's FWD (Jay Smooth) equalized, then scored the winner in the same minute, "exploiting gaps left by Kernel Panic's ball-focused commands".
5. SHOOT jumped to 42 commands (10%, our highest share) but produced 4 shots and 1 on target.
6. Benchmark again had one slow FWD (846ms, avg 321ms) and still won.

## Coach Interventions
<!-- Not reported. Fill in, or write "None". -->
| When | Message | Observed effect |
|------|---------|-----------------|
| [minute] | [what you typed] | [what changed after it] |

## Raw Stats
- Possession: 55% vs 45%
- Shots: 4 vs 5
- Shots on target: 1 vs 2
- Our commands: 410 total, 833ms avg latency
- Their commands: 410 total, 321ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 201 | 49% |
| Press | 102 | 25% |
| Intercept | 32 | 8% |
| Mark | 2 | 0% |
| Pass | 17 | 4% |
| Shoot | 42 | 10% |
| Clear | 13 | 3% |
| GK Dist | 1 | 0% |

Opponent: Move 275 (67%), Press 80 (20%), Pass 33 (8%), Clear 17 (4%), Shoot 4 (1%), GK Dist 1 (0%).

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 650ms | | 100% |
| DEF (Turing) | 781ms | | 100% |
| MID (Tesla) | 919ms | | 100% |
| FWD1 (Hertz) | 625ms | | 100% |
| FWD2 (Lovelace) | 970ms | | 100% |

Opponent: GK 185ms, DEF 192ms, MID 190ms, FWD **846ms**, FWD 200ms. MVP: their GK (Drew Midway).

## Per-Position Analysis

### GK
- Performance: adequate
- What worked: 650ms.
- What failed: Conceded 2 at 2' to their FWD.
- Root cause: Gaps behind a ball-focused team (see Team-Level).

### DEF
- Performance: weak
- What worked: 781ms, his fastest so far.
- What failed: Their FWD scored twice in one minute.
- Root cause: Two midfielders running the same "go to the ball" prompt leave one DEF covering the space behind. That's the known 1-2-1 weakness ("single DEF exposed on counters").

### MID
- Performance: adequate
- What worked: Part of 42 SHOOT commands.
- What failed: Shared his role with an identical copy (Hertz). Only 1 shot on target.
- Root cause: Both midfielders call themselves "MID" in the shared pressing and swarm lines, so they compete for the same actions.

### FWD1
- Performance: adequate
- What worked: Ran the MID prompt as a second midfielder. 625ms.
- What failed: No clear gain. Identical rules to Tesla.
- Root cause: Copy-paste test, no 1-2-1 coordination.

### FWD2
- Performance: weak
- What worked: 100% success.
- What failed: Single forward. No goals.
- Root cause: Lovelace's agent issue (corner parking, consistently slower) is unresolved.

## Team-Level Observations
- **The quick 1-2-1 (two copies of Tesla) lost 1-2.** It's one match, against a Benchmark with a slow FWD, and with unadapted prompts, so it's inconclusive. It did not show a clear improvement over the 1-1-2 setup that won 3-0 and 2-1.
- **More SHOOT commands didn't mean more shots:** 42 SHOOT commands gave 4 shots. Two shooters issuing SHOOT gives worse chances, not more goals.
- **Formation vs roles:** the platform still labels the players GK/DEF/MID/FWD/FWD after selecting 1-2-1. To be clarified whether roles follow the formation after redeploying.

## Action Items
- [ ] Decide: go back to the winning 1-1-2 setup (v8, Hertz Nova Lite 2, Lovelace Sonnet) and validate it against Fort Knox / Total Attack, or build proper 1-2-1 prompts (v9) with distinct midfield roles. (priority: high)
- [ ] Lovelace: check his deployed instructions and redeploy his agent. (priority: high)
- [ ] Confirm the forwards' models in this match. (priority: low)

## Opponent Scouting Notes
- Saved to `strategy/opponent-notes/the-benchmark-fc.md`.
