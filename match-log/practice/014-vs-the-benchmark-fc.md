# Match 014: vs The Benchmark FC

## Result
- Score: 1 - 0 (WIN)
- Date: 2026-10-06
- Type: practice
- Formation: 1-1-2
- Strategy: Swarm
- Deploy tag: deploy-v9-2026-10-06
- Prompt versions deployed: GK v8, DEF v8, MID v7, FWD1 v7, FWD2 v8
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

## Key Moments
1. First match of release v9: Lovelace on the FWD2 v8 text (second shooter level with Tesla, MARKs their midfielder), Hertz still on the FWD2 v7 text (013 swap), models and texts exactly as in `deploy/paste-ready.md` (coach confirmed: pasted from that file).
2. 3': Hertz (FWD) scored the only goal. The platform credits our PRESS intensity (150 commands, 40%) for disrupting Benchmark's build-up. First forward goal since match 006, and the first goal this season not scored by Tesla since 009.
3. The goal came at 3', so the match went through regulation at 0-0 and was decided in overtime. For the first time since 010/011 we did not concede in minute 1.
4. Tesla did not score. Team SHOOT commands fell to 15 (53 in 013); to check whether Lovelace standing level with Tesla changed Tesla's long-shot count (v9 watch item).
5. Benchmark had **two** slow forwards this time (955ms, 993ms; one slow FWD in 010–013), average 502ms. Fifth match in a row against a weakened Benchmark.
6. Benchmark played differently: PASS 65 (17%, their highest) and 36 FOLLOW commands (10%), never seen from them before. They had 6 shots, 0 on target.
7. Platform Coach's Corner for us: keep the press, raise SHOOT (15) in the final third; "one goal from one on-target shot is vulnerable".
8. GK Dist 9 while GK v8 rule 2 says PASS. Either the GK's PASS is reported as GK Dist, or the platform only allows distribute from the hands (the v8 GK review predicted this check).

## Coach Interventions
<!-- Not reported. Fill in, or write "None". -->
| When | Message | Observed effect |
|------|---------|-----------------|
| [minute] | [what you typed] | [what changed after it] |

## Raw Stats
- Possession: 54% vs 46%
- Shots: 4 vs 6
- Shots on target: 1 vs 0
- Our commands: 375 total, 804ms avg latency
- Their commands: 375 total, 502ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 127 | 34% |
| Press | 150 | 40% |
| Intercept | 39 | 10% |
| Mark | 2 | 1% |
| Pass | 21 | 6% |
| Shoot | 15 | 4% |
| Clear | 12 | 3% |
| GK Dist | 9 | 2% |

Opponent: Move 163 (43%), Press 74 (20%), Pass 65 (17%), Follow 36 (10%), Clear 14 (4%), Shoot 14 (4%), GK Dist 9 (2%).

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 625ms | | 100% |
| DEF (Turing) | 778ms | | 100% |
| MID (Tesla) | 980ms | | 100% |
| FWD1 (Hertz) | 647ms | | 100% |
| FWD2 (Lovelace) | 852ms | | 100% |

Opponent: GK 203ms, DEF 203ms, MID 202ms, FWD **955ms**, FWD **993ms**. MVP and fastest: their MID (Lee Steady, 202ms). Most tactical: their GK (Drew Midway, 75 commands).

## Per-Position Analysis

### GK
- Performance: strong
- What worked: Clean sheet; Benchmark 0 on target from 6 shots. 625ms, his fastest. 9 GK Dist, no CLEAR-into-the-corner pattern reported.
- What failed: Nothing observed.
- Root cause: Season-wide, every shot on target has been a goal for both sides (14 matches), so the clean sheet belongs to the press and the shape, not to saves. Note the GK Dist vs PASS question (Key Moments 8).

### DEF
- Performance: strong
- What worked: Clean sheet. 778ms, his second-fastest match. MARK only 2 (no passive marking).
- What failed: Nothing observed.
- Root cause: v8 fixed spot plus the swarm press kept Benchmark to 0 on target.

### MID
- Performance: adequate
- What worked: 980ms. Part of the 40% press.
- What failed: No goal for the first time since 009. Team SHOOT 15.
- Root cause: Unknown. Candidates: Lovelace level with him changes nothing by design, but Hertz (FWD2 v7 text, "point striker beyond FWD1") standing free ahead of him switches off MID rule 1's shot (the "no free teammate nearer their goal" clause). Check where Tesla's SHOOTs came from, if the coach saw any.

### FWD1
- Performance: strong
- What worked: Scored at 3' on his second match with the FWD2 v7 text. 647ms.
- What failed: Nothing reported.
- Root cause: The FWD2 v7 text suits his agent (013 and 014). Keep it; release it as FWD1's own version with the labels switched (v8 FWD2 changelog recommendation).

### FWD2
- Performance: adequate
- What worked: 852ms on Nova Lite 2 (893–1012 on Haiku/Sonnet). No corner parking reported.
- What failed: Behavior not reported; no goal.
- Root cause: v8 is designed for few touches (he gets the ball only when Tesla is pressed or wide), so a low count is expected. Needs the coach's screenshot of where he stood.

## Team-Level Observations
- Formation effectiveness: 1-1-2 Swarm, 54% possession, 4 shots, 1 on target, 1 goal; 0 on target against. Fifth win of the season, all five with the opponent held to 0 or 1 shot on target.
- Should we change formation? No. Don't change anything until this setup has played Fort Knox and Total Attack.
- Coordination gaps: SHOOT 15 and PASS 21 are low. 150 PRESS commands won the match. Press share in our wins: 37% (001), 28% (003), 39% (010), 28% (011), 40% (014); in our last four losses 28%, 25%, 23%, 20%.
- Opponent patterns: Benchmark now passes (17%) and uses FOLLOW (10%), and keeps shooting off target (6 shots, 0 on target). Two slow forwards.
- Opponent formation: Unknown (GK, DEF, MID, FWD, FWD).
- **Validation gap:** this is the fifth consecutive result against a weakened Benchmark (one slow FWD in 010–013, two in 014). Results with Hertz on the FWD2 v7 text: 2-3 L (013, Lovelace on FWD1 text), 1-0 W (014, Lovelace on FWD2 v8).
- **Every shot on target is a goal**, both teams, matches 001–014 (12 with stats). Defending means preventing shots; attacking means landing one.

## Action Items
- [ ] Validate: play this exact setup (no prompt or model change) against Fort Knox Athletic, then Total Attack United. Log both. (priority: high)
- [ ] Tesla: ask the coach where his SHOOT commands came from and whether Hertz stood ahead of him when he had the ball. If MID rule 1 is being switched off by a free Hertz, exempt MID's shot from the teammate clause in the next release. (priority: high)
- [ ] Platform: GK Dist 9 vs PASS in GK rule 2. Check in "What can my agents do?" whether the GK can PASS at all, and what state fields the agents receive. (priority: high)
- [ ] FWD1 release: make Hertz's FWD2 v7 text the official FWD1 v8 with labels switched, so both forwards stop calling themselves FWD2 in the shared Pressers tie-break. (priority: medium)
- [ ] Coach Interventions: fill in or write "None". (priority: medium)

## Opponent Scouting Notes
- Saved to `strategy/opponent-notes/the-benchmark-fc.md`.
