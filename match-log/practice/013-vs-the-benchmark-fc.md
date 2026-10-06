# Match 013: vs The Benchmark FC

## Result
- Score: 2 - 3 (LOSS)
- Date: 2026-10-06
- Type: practice
- Formation: 1-1-2
- Strategy: Swarm
- Deploy tag: deploy-v8-2026-10-05
- Prompt versions deployed: GK v8, DEF v8, MID v7, FWD1 v7, FWD2 v7
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Claude Sonnet

## Key Moments
1. **Swap test:** the forward prompts were swapped. Hertz ran the FWD2 (right) prompt, Lovelace the FWD1 (left) prompt. Models unchanged (Hertz Nova Lite 2, Lovelace Sonnet).
2. **Result of the swap (coach):** Hertz played "waaaay better", and Lovelace was still erratic and playing badly. The erratic behavior followed **Lovelace's agent**, not the prompt.
3. 1': Benchmark scored twice (MID Lee Steady, FWD Jay Smooth).
4. 1': Tesla scored twice to make it 2-2 (8 goals in his last 5 matches).
5. 3': Jay Smooth scored the winner.
6. Benchmark again had one slow FWD (1042ms, avg 348ms). That's four matches in a row.

## Coach Interventions
<!-- Not reported. Fill in, or write "None". -->
| When | Message | Observed effect |
|------|---------|-----------------|
| [minute] | [what you typed] | [what changed after it] |

## Raw Stats
- Possession: 57% vs 43%
- Shots: 6 vs 7
- Shots on target: 2 vs 3
- Our commands: 560 total, 900ms avg latency
- Their commands: 560 total, 348ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 227 | 41% |
| Press | 128 | 23% |
| Intercept | 98 | 18% |
| Mark | 1 | 0% |
| Pass | 29 | 5% |
| Shoot | 53 | 9% |
| Clear | 23 | 4% |
| GK Dist | 1 | 0% |

Opponent: Move 372 (66%), Press 114 (20%), Pass 41 (7%), Clear 23 (4%), Shoot 9 (2%), GK Dist 1 (0%).

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 647ms | | 100% |
| DEF (Turing) | 968ms | | 100% |
| MID (Tesla) | 1308ms | | 100% |
| FWD1 (Hertz) | 656ms | | 100% |
| FWD2 (Lovelace) | 1012ms | | 100% |

Opponent: GK 191ms, DEF 194ms, MID 194ms, FWD **1042ms**, FWD 207ms. MVP: their GK (Drew Midway).

## Per-Position Analysis

### GK
- Performance: weak
- What worked: 647ms.
- What failed: Conceded 3, two of them in minute 1.
- Root cause: The opening minute remains our weakest moment (opponent goals at 1' in most matches).

### DEF
- Performance: adequate
- What worked: 968ms.
- What failed: Their MID and FWD both scored at 1'.
- Root cause: Same opening-minute problem.

### MID
- Performance: strong
- What worked: Scored both our goals at 1'.
- What failed: 1308ms, his slowest ever.
- Root cause: MID rule 1 long-range shooting remains our best weapon.

### FWD1
- Performance: strong
- What worked: (coach) Hertz played "waaaay better" running the FWD2 prompt. 656ms.
- What failed: No goal.
- Root cause: Hertz's agent is sound. The FWD2 prompt (press only when strictly closer, otherwise cover) may suit him better than FWD1's.

### FWD2
- Performance: weak
- What worked: 100% success.
- What failed: (coach) Still erratic and "playing as crap", now on the FWD1 prompt.
- Root cause: **Agent-level issue with Lovelace.** Erratic across prompts (v3–v8, both forward roles), models (Haiku, Sonnet) and formations. Consistently ~300ms slower than Hertz. The swap test rules out his prompt.

## Team-Level Observations
- **The swap test points to Lovelace's agent:** the erratic behavior stayed with him on Hertz's prompt.
- Results with the forwards on Nova Lite 2 / Sonnet: 3-0 W, 2-1 W, 1-2 L (1-2-1 test), 2-3 L (swap). All against Benchmark, which had one slow FWD in all four. The setup is not yet validated against Fort Knox or Total Attack.
- Tesla: 8 goals in matches 009–013. He's our scoring engine.

## Action Items
- [ ] Lovelace: fix at the agent level. Delete and recreate the agent if the platform allows it, otherwise redeploy. Compare his "Advanced" settings with Hertz's. (priority: high)
- [ ] Hertz: keep the FWD2 prompt he played "way better" with. (priority: high)
- [ ] Validate the setup against Fort Knox / Total Attack before competitive play. (priority: high)
- [ ] Opening minute: we keep conceding in minute 1. Revisit kickoff shape and "Pre-match fitness". (priority: high)

## Opponent Scouting Notes
- Saved to `strategy/opponent-notes/the-benchmark-fc.md`.
