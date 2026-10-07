# Match 018: vs The Benchmark FC

## Result
- Score: 2 - 1 (WIN)
- Date: 2026-10-06
- Type: practice
- Formation: 1-2-1 (platform setting since the match 012 test; this log originally said 1-1-2 by habit — corrected 2026-10-07)
- Strategy: Swarm
- Deploy tag: deploy-v11-2026-10-06
- Prompt versions deployed: GK v10, DEF v10, MID v9, FWD1 v9, FWD2 v10
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

First match on v11 (pressing rewritten on the official command model, kick-off rules, no one-step carry). Validation match before competitive use.

## Key Moments
1. **Healthy signature: 400 commands, 877 ms average, every agent 691–1028 ms.** v11 is loaded and running.
2. 1': Tesla (MID) 1-0. 18 goals in 12 matches on our prompts.
3. 2': Jay Smooth (their FWD) 1-1, "exploiting a momentary Kernel Panic defensive lapse". Benchmark's first shot on target against us in three matches (017: 0 of 6).
4. 2': "Unknown" 2-1 for us, right after the equalizer (kick-off rule territory: the conceding team kicks off, Tesla plays the through ball or shoots).
5. **v11 checklist against C002/C005 (v10):** MOVE 38% (was 54–62%: the carry removal worked); PRESS 151 (38%, was 13–30: the swarm press fires); INTERCEPT 37 (was 0: loose-ball intercepts exist now); SHOOT 30 (8%). **MARK 1 and FOLLOW 0**: the "MARK tightly" jobs and Lovelace's "FOLLOW Tesla" did not show up as those commands. See Team-Level Observations.
6. 30 SHOOT commands, 3 shots, 2 on target, 2 goals. The command-to-shot gap persists (C002 73→8, C005 33→2).
7. PASS 18 (5%): the through ball to Hertz was rare. Platform's Coach's Corner for us: fewer PRESS, more PASS.
8. Shots on target = goals, both teams (2 of 2, 1 of 1). 23 matches running.
9. 80 commands per agent: overtime after the 1-1.

## Coach Interventions
| When | Message | Observed effect |
|------|---------|-----------------|
| — | None | — |

## Raw Stats
- Possession: 50% vs 50%
- Shots: 3 vs 5
- Shots on target: 2 vs 1
- Our commands: 400 total, 877ms avg latency
- Their commands: 400 total, 506ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 152 | 38% |
| Press | 151 | 38% |
| Intercept | 37 | 9% |
| Mark | 1 | 0% |
| Pass | 18 | 5% |
| Shoot | 30 | 8% |
| Clear | 11 | 3% |
| GK Dist | 0 | 0% |

Opponent: Move 209 (52%), Press 68 (17%), Pass 44 (11%), Follow 32 (8%), Intercept 20 (5%), Shoot 13 (3%), Clear 12 (3%), Mark 2 (1%).

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 714ms | | 100% |
| DEF (Turing) | 903ms | | 100% |
| MID (Tesla) | 1028ms | | 100% |
| FWD1 (Hertz) | 691ms | | 100% |
| FWD2 (Lovelace) | 867ms | | 100% |

Opponent: GK 206ms (MVP, fastest, most tactical: Drew Midway, 80 commands), DEF 208ms, MID 206ms, FWD **927ms**, FWD **1014ms**.

## Per-Position Analysis

### GK
- Performance: adequate
- What worked: 714ms. Conceded 1 from 1 on target; 5 shots against, 4 off target.
- What failed: **0 GK Dist.** v10's "throw it to MID / kick it long" was meant to map to the GK's own distribution command; the report shows none, so his releases were logged as PASS or CLEAR (or the harness ignored the verbs).
- Root cause: Command mapping, to be confirmed. Not harmful on the pitch (the ball left the back; 11 CLEARs team-wide).

### DEF
- Performance: adequate
- What worked: 903ms. Team PRESS 151 and INTERCEPT 37 include his clear-line press (rule 5) and loose-ball intercepts; 5 shots against but 1 on target.
- What failed: One goal conceded at 2' from a "defensive lapse"; whether it came behind him while he pressed (the Evaluator's watch item) is unknown without a replay.
- Root cause: Unknown. Watch the next match.

### MID
- Performance: strong
- What worked: Goal at 1'. The clear-line shot still works under v9 wording.
- What failed: 1028ms, his slowest healthy run; PASS 18 team-wide, so the through ball to Hertz was rare.
- Root cause: Benchmark presses at 17% only, so Tesla's line was usually clear and he shot rather than passed; consistent with rules 2–3 ordering.

### FWD1
- Performance: adequate
- What worked: 691ms, out of the press as designed (PRESS 151 is MID/FWD2/DEF).
- What failed: No goal attributed; few through balls reached him (PASS 18).
- Root cause: See MID.

### FWD2
- Performance: adequate
- What worked: 867ms. Possibly the "Unknown" goal.
- What failed: **FOLLOW 0.** "FOLLOW Tesla, a short pass away" (rule 8) produced no FOLLOW command; MARK 1 means "MARK tightly their midfielder" (rule 7) and the shared "MARK tightly the opponent closest to him" did not run as MARK either.
- Root cause: The harness did not map our FOLLOW/MARK wording this match. In C002 (v10) the opposite happened: 71 FOLLOWs appeared from wording that never said FOLLOW; in C005 (v10) 58 MARKs appeared. The mapping of MARK/FOLLOW is unstable across matches and we cannot steer it from the prompt text alone.

## Team-Level Observations
- Formation effectiveness: Won 2-1, v11 validated for competitive use on the signature and the three measurable fixes (MOVE down to 38%, PRESS up to 38%, INTERCEPT back at 9%).
- Should we change formation? No.
- **MARK/FOLLOW mapping is the open problem.** Across four healthy matches, the same kind of wording produced MARK 3 / FOLLOW 71 (C002), MARK 0 / FOLLOW 0 (C003), MARK 58 / FOLLOW 0 (C005), MARK 1 / FOLLOW 0 (018). Possession explains part of it (defensive jobs fire less at 71%), but C005 (56%) and 018 (50%) differ by 57 MARKs. Either the harness translation varies, or those jobs are being executed as PRESS (151 this match, two pressers on the carrier). Ask at office hours whether a per-agent command view exists.
- **GK Dist 0** for the first time since logging (2–7 in every healthy match). v10's throw/kick verbs did not produce GK_DISTRIBUTE. Harmless so far.
- SHOOT commands vs shots: 30 → 3. Agents issue SHOOT without a shot resulting. Possibly SHOOT when not in possession, or blocked. Same question for office hours.
- Benchmark FC shows the same latency profile as every human opponent (back three ~206 ms, forwards ~1 s), and 32 FOLLOWs. The reference team's back three is the same thing the human teams run.
- Opponent patterns: Benchmark got 5 shots this time (017: 6, 0 on target; 014: ?). Pressing at 17% only; passes 11%.
- Opponent formation: GK, DEF, MID, FWD, FWD.

## Action Items
- [ ] Office hours: per-agent command breakdown? How are MARK / FOLLOW / GK_DISTRIBUTE chosen from the prompt text (why 58 MARKs in C005 and 1 in 018 from similar wording)? Why do SHOOT commands outnumber shots 10:1? (priority: high)
- [ ] Play the next competitive match on v11. Check the live latency in the first 15 seconds (under 300 ms = prompts not running). (priority: high)
- [ ] v12 candidates, one rule each, only if the next match shows the problem: (a) pressed in our half → long ball to Hertz before the short pass to MID (C005 1'); (b) if Lovelace keeps drifting, replace "FOLLOW Tesla" with the v9 MOVE-to-a-spot rule since FOLLOW does not map; (c) if a goal comes behind DEF while he presses, add "and no attacker without the ball is inside our box" to DEF rule 5. (priority: medium)
- [ ] Through balls are rare (PASS 18). Check in the next match whether Hertz receives any long pass; if not, the MID rule 2 trigger (blocker + Hertz free) is too narrow against low-press teams. (priority: medium)

## Opponent Scouting Notes
- Updated `strategy/opponent-notes/the-benchmark-fc.md`.
