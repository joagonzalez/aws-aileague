# Match 010: vs The Benchmark FC

## Result
- Score: 3 - 0 (WIN)
- Date: 2026-10-05
- Type: practice
- Formation: 1-1-2
- Strategy: Swarm
- Deploy tag: deploy-v8-2026-10-05
- Prompt versions deployed: GK v8, DEF v8, MID v7, FWD1 v7, FWD2 v7
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Claude Sonnet

## Key Moments
1. Model test (coach): Hertz (FWD1) on Nova Lite 2, Lovelace (FWD2) on Claude Sonnet, everyone else on Haiku. v8 prompts unchanged.
2. 2': Tesla (MID) scored from long range (coach: the report's 'Unknown' was Tesla).
3. 2': Tesla scored again from long range.
4. 2': Tesla completed a hat-trick from long range. All three goals came in minute 2, from 3 shots, all on target.
5. Benchmark had 78% possession and 0 shots on target.
6. **Confounder:** one Benchmark FWD ran at 853ms (normally ~200ms), lifting their average to 324ms. Their attack was effectively weakened this match.
7. Platform advice mentions a command we've never used: **SET_STANCE** ("lock shape between transitions").

## Coach Interventions
<!-- Not reported. Fill in, or write "None". -->
| When | Message | Observed effect |
|------|---------|-----------------|
| [minute] | [what you typed] | [what changed after it] |

## Raw Stats
- Possession: 22% vs 78%
- Shots: 3 vs 2
- Shots on target: 3 vs 0
- Our commands: 405 total, 852ms avg latency
- Their commands: 405 total, 324ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 143 | 35% |
| Press | 158 | 39% |
| Intercept | 44 | 11% |
| Mark | 1 | 0% |
| Pass | 23 | 6% |
| Shoot | 14 | 3% |
| Clear | 21 | 5% |
| GK Dist | 1 | 0% |

Opponent: Move 235 (58%), Press 109 (27%), Pass 28 (7%), Shoot 19 (5%), Clear 13 (3%), GK Dist 1 (0%).

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 654ms | | 100% |
| DEF (Turing) | 862ms | | 100% |
| MID (Tesla) | 985ms | | 100% |
| FWD1 (Hertz) | 653ms | | 100% |
| FWD2 (Lovelace) | 809ms | | 100% |

Opponent: GK 215ms, DEF 211ms, MID 198ms, FWD **853ms**, FWD 205ms. MVP and fastest player: their MID (Lee Steady, 198ms).

## Per-Position Analysis

### GK
- Performance: strong
- What worked: Clean sheet. Opponent 0 shots on target. 654ms.
- What failed: Nothing observed.
- Root cause: The press kept Benchmark from shooting. Their slow FWD helped.

### DEF
- Performance: strong
- What worked: Clean sheet. 862ms, better than his usual ~1000.
- What failed: Nothing observed.
- Root cause: v8 shape plus a high press.

### MID
- Performance: strong
- What worked: Scored all three at 2', all long-range shots (coach: "took advantage of long shots, that was awesome"). On Haiku. v7 MID rule 1 reads "nearer their goal than the halfway line". The v8 Reviewer flagged that as ambiguous (it allows long shots) and filed it as minor. That ambiguity produced the hat-trick.
- What failed: 985ms.
- Root cause: v7 MID rule 1 converts central chances.

### FWD1
- Performance: adequate
- What worked: 653ms. Part of the highest press share since match 001 (39%).
- What failed: Did not score (unless he was the unknown scorer). Behavior not yet reported.
- Root cause: Nova Lite 2. Latency unchanged from his Haiku range (634–713), so for Hertz the model barely affects speed.

### FWD2
- Performance: adequate
- What worked: 809ms, lower than all his Haiku readings (893–999).
- What failed: Did not score (unless he was the unknown scorer). Behavior not yet reported.
- Root cause: Claude Sonnet. 809ms is *faster* than all his Haiku readings (893–999). Sonnet costs no speed here.

## Team-Level Observations
- **First win in seven matches**, after the only change: the forwards' models (v8 prompts unchanged). The press share rose to 39% (28% in 009) and 3 of 3 shots were on target.
- **The win came from Tesla's long shots, not mainly from the forwards' models.** Tesla (Haiku) scored all three. The model change may have helped the press (39%), but the forwards did not score. Benchmark's slow FWD (853ms) also weakened them, and it's one match. A replication against a different opponent is needed before we lock the setup.
- **Possession isn't required to win:** 22% possession, 3-0. Pressing and fast finishing beat possession, the same as match 001 (18% possession, 1-0).
- **New command seen: SET_STANCE.**
- **Long shots work on this platform.** Across matches 001–010, 6 of our 11 goals came from deep players (Turing twice, Tesla four times). Against us: three goals by opposing GKs from their own end (006, 007, 009), a DEF goal (004) and a long shot from near halfway (002). v7's decision to cut MID's long-range shooting (because of match 007: 34 SHOOT commands, 0 on target) was based on one match and is contradicted here.

## Action Items
- [ ] Replicate: same setup (v8, forwards on Sonnet / Nova Lite 2, rest Haiku) against Fort Knox or Total Attack. (priority: high)
- [ ] Confirm which forward ran which model, and how each behaved (group, passing, shooting). (priority: high)
- [ ] Long shots: make long-range shooting from central positions an explicit weapon for MID (and test DEF), instead of an accidental ambiguity. (priority: high, after replication)
- [ ] Formation idea: our MID scores and our forwards don't. Test 1-2-1 (a second long-shooting MID instead of a forward) after the replication. (priority: medium)
- [ ] Platform: what does SET_STANCE do? (priority: medium)

## Opponent Scouting Notes
- Saved to `strategy/opponent-notes/the-benchmark-fc.md`.
