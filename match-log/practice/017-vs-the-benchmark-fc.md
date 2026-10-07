# Match 017: vs The Benchmark FC

## Result
- Score: 1 - 0 (WIN)
- Date: 2026-10-06
- Type: practice
- Formation: 1-2-1 (platform setting since the match 012 test; this log originally said 1-1-2 by habit — corrected 2026-10-07)
- Strategy: Swarm
- Deploy tag: deploy-v9-2026-10-06
- Prompt versions deployed: GK v8, DEF v8, MID v7, FWD1 v7, FWD2 v8
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

## Key Moments
1. **Health check after competitive 001.** Our agents are running our prompts again: 400 commands, 856ms average, every agent 671–980ms, PRESS 158 (40%). Competitive 001 (52 commands, 33ms) was a deployment failure, confirmed.
2. 3': Tesla (MID) scored, in overtime again (regulation ends 0-0 at about 2 minutes). Tesla: 14 goals in 009–017.
3. Benchmark: 6 shots, 0 on target, 63% MOVE. Two slow forwards (913ms, 962ms), as in every match since 010.
4. Platform Coach's Corner for us: only 19 SHOOT commands; more finishing in transition.
5. Coach observations (feedback after this match): Turing and Shannon seem to run toward our own goal instead of defending; the forwards are bunched together with Tesla and the midfield is a mess; the coach wants one forward to find an open position and the other to pass to him. Note: the clearest "Turing runs to the GK" sighting was competitive 001, when the default agent was playing. Treat the DEF/GK observation as unconfirmed under our prompts until seen again.

## Coach Interventions
<!-- Was "be more aggressive and shoot!" sent? Fill in, or write "None". -->
| When | Message | Observed effect |
|------|---------|-----------------|
| [minute] | [what you typed] | [what changed after it] |

## Raw Stats
- Possession: 50% vs 50%
- Shots: 3 vs 6
- Shots on target: 1 vs 0
- Our commands: 400 total, 856ms avg latency
- Their commands: 400 total, 503ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 172 | 43% |
| Press | 158 | 40% |
| Intercept | 20 | 5% |
| Mark | 0 | 0% |
| Pass | 24 | 6% |
| Shoot | 19 | 5% |
| Clear | 5 | 1% |
| GK Dist | 2 | 1% |

Opponent: Move 252 (63%), Press 96 (24%), Pass 32 (8%), Shoot 12 (3%), Clear 6 (2%), GK Dist 2 (1%).

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 671ms | | 100% |
| DEF (Turing) | 929ms | | 100% |
| MID (Tesla) | 980ms | | 100% |
| FWD1 (Hertz) | 684ms | | 100% |
| FWD2 (Lovelace) | 915ms | | 100% |

Opponent: GK 212ms, DEF 215ms, MID 211ms, FWD **913ms**, FWD **962ms**. MVP and fastest: their MID (Lee Steady, 211ms). Most tactical: their GK (Drew Midway, 80 commands).

## Per-Position Analysis

### GK
- Performance: strong
- What worked: Clean sheet, 0 on target against. 671ms. Only 2 GK Dist and 5 team CLEARs: the ball left the back by PASS.
- What failed: Coach impression of running toward our goal (unconfirmed under our prompts; GK rule 5 does send him to the goal line whenever the opponent has the ball, which is by design).
- Root cause: N/A.

### DEF
- Performance: adequate
- What worked: Clean sheet. 929ms.
- What failed: 0 MARK. Coach impression of running toward our goal / GK. Under DEF v8 the only rules that move him toward our goal are the loose-ball-in-box MOVE (rule 3) and the MARK rules (6–7), which are defensive; and he never passes to GK.
- Root cause: To be confirmed by watching him in a healthy match. Not a rule contradiction in v8.

### MID
- Performance: strong
- What worked: Winner at 3'. 980ms.
- What failed: 19 team SHOOT commands, 3 shots.
- Root cause: Rule 1 switches off when a free teammate is nearer their goal with the goal in front, and Hertz's role stands exactly there. Candidate fix for v10.

### FWD1
- Performance: adequate
- What worked: 684ms.
- What failed: Bunched with Tesla and Lovelace (coach). No goal.
- Root cause: The FWD2 v7 text puts him "a short pass beyond the ball or FWD1" and the Swarm line keeps all three a short pass apart, so the three stack in midfield.

### FWD2
- Performance: adequate
- What worked: 915ms. Not reported in a corner.
- What failed: Part of the midfield bunch (coach).
- Root cause: v8 rule 6 holds him level with Tesla a short pass away; with Hertz also a short pass away the three occupy one spot.

## Team-Level Observations
- Formation effectiveness: 1-0, fourth straight practice win for the v9 setup (1-0, 3-2, 4-0, 1-0), all with 0 or 2 shots on target against.
- Should we change formation? No. Roles change inside 1-1-2 (see Action Items).
- Coordination gaps: the Swarm line works for pressing (40% press, 0 on target against) but bunches three players in midfield, so Tesla's long shot is often switched off by a free teammate ahead and there is no runner to pass to.
- Opponent patterns: Benchmark unchanged; still cannot finish (0 of 6).
- Opponent formation: Unknown.
- Shots on target = goals, 18 matches running (1/1 us, 0/6 them).

## Action Items
- [ ] v10 release through the workflow (coach brief): keep the press and the deep spots; DEF and GK close down a carrier near their zone and shoot long when free; FWD1 (Hertz) becomes the runner who seeks open space ahead and central, Lovelace stays beside Tesla as passer and second shooter; Tesla shoots when he has a clear line regardless of teammates and otherwise passes long to the free runner. One practice match with the healthy-signature check before it plays a competitive match. (priority: high)
- [ ] Make Hertz's text an official FWD1 version so the platform-state override can go. (priority: high)
- [ ] Coach: in the next match, note whether Turing or Shannon moves toward our goal while the opponent does NOT have the ball. (priority: medium)

## Opponent Scouting Notes
- Saved to `strategy/opponent-notes/the-benchmark-fc.md`.
