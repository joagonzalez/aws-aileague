# Match 022: vs Total Attack United

## Result
- Score: 3 - 5 (LOSS)
- Date: 2026-10-06
- Type: practice
- Formation: 1-2-1 (platform setting since the match 012 test; this log originally said 1-1-2 by habit — corrected 2026-10-07)
- Strategy: Swarm
- Deploy tag: deploy-v12-2026-10-06
- Prompt versions deployed: GK v11, DEF v11, MID v10, FWD1 v10, FWD2 v11
- Models: GK Claude Haiku, DEF Nova Micro, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

First match on v12, coach watching. Third straight loss to Total Attack United (3-7, 0-2, 3-5). The coach keeps v12 for now to test it against the other teams.

## Key Moments
1. Healthy signature: 560 commands, 832 ms average, every agent 672–1041 ms. 112 commands per agent (overtime-length, eight goals).
2. **Our "Clear" is CLEAR_OVERRIDE.** The platform's own match overview says "Panic's CLEAR_OVERRIDE spam (25 commands)", and our breakdown shows Clear 25. The official command list (`strategy/platform-reference.md`) has no CLEAR; CLEAR_OVERRIDE "returns the player to the default AI". Every CLEAR in our prompts (10 occurrences across the five current prompts; 26 of 27 match reports show Clear 5–35 for us) has been handing that player to the built-in AI for that decision. The fix for v13 is to remove the word everywhere and name a receiver instead (lofted PASS to FWD1 / MID, or SHOOT at full power).
3. **Nova Micro on DEF: 830 ms**, against 841–947 ms on Haiku. No speed gain. Latency on this platform is not set by the model; the harness is the floor. Recommendation: DEF back to Claude Haiku (smarter at the same speed).
4. Goals: Al Frenzy (their MID) 0-1, Vic Surge (FWD) 0-2, 0-3, all in minute 1; Tesla 1-3; Al Frenzy 1-4; Tesla 2-4; Vic Surge 2-5; Tesla 3-5. Tesla: 26 goals in 17 matches. **Their GK and DEF did not score** for the first time in three Total Attack matches (Hertz now presses their GK: v12 change 2).
5. **Coach observation (live): too many goals from midfield; not enough pressure on their MID there; Shannon does not stop those shots.** Under v12 the swarm presses "a carrier in our half or within a long pass of halfway"; a MID shooting from deeper in his own half is pressed by nobody (the v12 Evaluator's note 7 named exactly this). Shannon: every shot on target has been a goal for both teams in 27 matches; no GK on this platform saves. Defence is preventing the shot.
6. **Coach observation (live): Lovelace and Hertz should take long shots when the chance appears.** Their shot rules require "their goal in front of you", defined as the central third and away from the end line, before the long shot fires; Tesla's long shots use the same test but he lives in the middle. For the wide/runner positions the test is too strict.
7. **PASS 0, SHOOT 89 for 3 shots, MARK 0, GK Dist 3.** v12's lofted passes and through balls did not register as PASS at all; 89 SHOOT commands produced 3 shots. The command-name mapping is still not something we control from the text (019: PASS 53 / SHOOT 0 on near-identical wording).
8. Three conceded in minute 1 again (020: five). The kick-off change (pass instead of shot) did not stop the minute-1 blitz; with PASS 0 recorded, the kick-off pass may not have been executed as a pass at all.
9. Shots on target = goals, both teams (3 of 3, 5 of 5). 27 matches running.

## Coach Interventions
| When | Message | Observed effect |
|------|---------|-----------------|
| — | None (watched, no messages sent) | — |

## Raw Stats
- Possession: 61% vs 39%
- Shots: 3 vs 10
- Shots on target: 3 vs 5
- Our commands: 560 total, 832ms avg latency
- Their commands: 585 total, 600ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 228 | 41% |
| Press | 130 | 23% |
| Intercept | 85 | 15% |
| Mark | 0 | 0% |
| Pass | 0 | 0% |
| Shoot | 89 | 16% |
| Clear | 25 | 4% |
| GK Dist | 3 | 1% |

"Clear" is CLEAR_OVERRIDE (platform overview text). Opponent: Move 316 (54%), Pass 126 (22%), Press 50 (9%), Clear 30 (5%), Follow 27 (5%), Intercept 16 (3%), Mark 10 (2%), Shoot 7 (1%), GK Dist 3 (1%).

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 702ms | | 100% |
| DEF (Turing) | 830ms | | 100% |
| MID (Tesla) | 984ms | | 100% |
| FWD1 (Hertz) | 672ms | | 100% |
| FWD2 (Lovelace) | 1041ms | | 100% |

Opponent: GK 203ms (MVP, fastest, most tactical: Max Fury, 117 commands), DEF **670ms** (was ~186ms in 020–021: they changed something), MID 207ms, FWD 868ms, FWD 1088ms.

## Per-Position Analysis

### GK
- Performance: weak
- What worked: 702ms. Their GK did not score (Hertz's press).
- What failed: 5 conceded from 5 on target; 3 GK Dist, so most releases were not his own command.
- Root cause: Shots on target are goals on this engine. Not fixable in the GK prompt; the shots must be prevented upstream.

### DEF
- Performance: weak
- What worked: Nothing visible.
- What failed: 830ms on Nova Micro: no faster than Haiku. Vic Surge scored three; MARK 0 team-wide.
- Root cause: Model latency is harness-bound. His CLEARs (part of the 25) handed him to the default AI at the moments that mattered most (under pressure in our box).

### MID
- Performance: strong
- What worked: Three goals (26 in 17 matches).
- What failed: 89 SHOOT commands for 3 shots.
- Root cause: SHOOT issued without the ball or blocked; same as every match since C002.

### FWD1
- Performance: adequate
- What worked: 672ms. Their GK did not score.
- What failed: No goal; coach wants him shooting from range when open.
- Root cause: Rule 2's long shot needs "goal in front" (central third, away from the end line); as the runner he is often wide of that. v13: clear line to goal anywhere in their half.

### FWD2
- Performance: weak
- What worked: Nothing visible.
- What failed: No goal; 1041ms; MARK 0 (his "MARK tightly their midfielder" did not register).
- Root cause: Same shot-test restriction as Hertz; mapping of MARK unstable.

## Team-Level Observations
- Formation effectiveness: Lost 3-5. v12 is 0-1. Against Total Attack we are 1-3 (015 win on v9 with the live "be aggressive and shoot" message; 020, 021, 022 losses unattended).
- Should we change formation? No. The coach tests v12 against Benchmark and Fort Knox next for a general read; v13 brief below is ready.
- Coordination gaps: (1) their MID shoots from his own half unpressed; (2) CLEAR = default AI; (3) wide/runner long shots blocked by the "goal in front" test; (4) minute-1 blitz after kick-offs persists.
- Opponent patterns: Total Attack United now has a 670 ms DEF (model change on their side) and passes 22% of commands; 10 shots, 5 on target.
- Opponent formation: GK, DEF, MID, FWD, FWD.

## Action Items
- [ ] Docs now: schema rule 7 and CLAUDE.md say CLEAR is CLEAR_OVERRIDE; never write "clear" as an action. (priority: high)
- [ ] v13 brief (when the coach is ready): (a) remove every CLEAR: GK "kick it long to FWD1" only; DEF "lofted PASS to FWD1, else lofted PASS to MID"; MID/FWD fallbacks "lofted PASS to FWD1" or "SHOOT at full power". (b) Swarm press reach: the nearer of MID and FWD2 presses any carrier anywhere except their GK and deepest DEF (Hertz's), so their MID is pressed in his own half too; Lovelace MARKs their MID tightly whenever he is without the ball. (c) Hertz and Lovelace: in their half with a clear line to goal (no outfield opponent directly between you and the goal) → SHOOT at full power, wherever they stand; the central-third "goal in front" test goes. (d) DEF back to Claude Haiku. (e) From the official Practice page: Total Attack's GK is a sweeper-keeper at halfway, so their goal is empty; every player with the ball and a clear line SHOOTs at full power at the empty goal from wherever he stands when their GK is nearer the halfway line than his own goal (dormant against teams whose GK stays home). (f) SHOOT/PASS only with the ball at your feet (official: possession required; 022 wasted 86 ticks). (g) Second marker rule from the official coordination page: if a teammate already marks that attacker, mark the next nearest. (priority: high)
- [ ] Keep v12 for the Benchmark and Fort Knox tests; compare with 018 (2-1) and 019 (2-1) on v11. (priority: medium)
- [ ] Office hours: confirm that the "Clear" count is CLEAR_OVERRIDE and what it does mid-match (one tick, or until the next command?). (priority: high)

## Opponent Scouting Notes
- Updated `strategy/opponent-notes/total-attack-united.md`.
