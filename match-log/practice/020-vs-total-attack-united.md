# Match 020: vs Total Attack United

## Result
- Score: 3 - 7 (LOSS)
- Date: 2026-10-06
- Type: practice
- Formation: 1-2-1 (platform setting since the match 012 test; this log originally said 1-1-2 by habit — corrected 2026-10-07)
- Strategy: Swarm
- Deploy tag: deploy-v11-2026-10-06
- Prompt versions deployed: GK v10, DEF v10, MID v9, FWD1 v9, FWD2 v10
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

Third match on v11. The coach watched this one. Heaviest defeat since competitive 001.

## Key Moments
1. Healthy signature: 600 commands, 812 ms average, every agent 678–998 ms. This is v11 playing, not a platform failure.
2. **Five goals conceded in minute 1**: Max Fury (their GK) 0-1, Vic Surge (FWD) 0-2, Al Frenzy (MID) 0-3, Vic Surge 0-4 and 0-5. Then Tesla 1-5, Tesla 2-5 (2'), Max Fury (GK) 2-6, Ray Chase (DEF) 2-7, Tesla 3-7. Tesla: 23 goals in 15 matches.
3. **Their GK scored twice and their DEF once from their own end.** Opposing GKs have now scored 6 times against us, DEFs 5. Under v11 nobody presses a carrier deeper than a long pass from halfway (Evaluator note 3 at the v11 review), and Hertz never presses, so their GK has all the time he wants. Every shot on target is a goal, so the GK long shot is a free goal for them.
4. **Kick-off chain.** After each concession we kick off; MID rule 1 says through ball to Hertz if free, else SHOOT at full power from the center spot. Five goals in minute 1 means five kick-offs in a row; 87 SHOOT commands (14%, the most ever) produced 5 shots. The hypothesis: Tesla's kick-off shot from the center spot goes straight to their GK, who launches the next attack or shoots himself. To verify on the next replay.
5. **INTERCEPT 210 (35%) and MARK 0.** In match 019 the same prompts gave MARK 101 / INTERCEPT 42; in 018 MARK 1 / INTERCEPT 37. The harness does not translate our MARK wording consistently. PASS 5 (1%) against 53 in 019: with 66% possession and 11 shots against, the ball was rarely in a passing situation.
6. **Coach observations (live):** Hertz took several ticks to shoot when he was alone in front of their goal; Turing was slow to start marking an opponent who needed it.
7. Shots on target = goals, both teams (3 of 3, 7 of 7). 25 matches running.
8. 120 commands per agent: the longest match yet (ten goals, ten resets).

## Coach Interventions
| When | Message | Observed effect |
|------|---------|-----------------|
| — | None (watched, no messages sent) | — |

## Raw Stats
- Possession: 66% vs 34%
- Shots: 5 vs 11
- Shots on target: 3 vs 7
- Our commands: 600 total, 812ms avg latency
- Their commands: 600 total, 511ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 234 | 39% |
| Press | 33 | 6% |
| Intercept | 210 | 35% |
| Mark | 0 | 0% |
| Pass | 5 | 1% |
| Shoot | 87 | 14% |
| Clear | 28 | 5% |
| GK Dist | 3 | 1% |

Opponent: Move 349 (58%), Pass 86 (14%), Press 75 (13%), Clear 33 (6%), Follow 23 (4%), Intercept 18 (3%), Shoot 7 (1%), Mark 6 (1%), GK Dist 3 (1%).

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 696ms | | 100% |
| DEF (Turing) | 929ms | | 100% |
| MID (Tesla) | 998ms | | 100% |
| FWD1 (Hertz) | 678ms | | 100% |
| FWD2 (Lovelace) | 916ms | | 100% |

Opponent: GK 182ms (MVP, fastest, most tactical: Max Fury, 120 commands), DEF 186ms, MID 186ms, FWD **1087ms**, FWD **1115ms**.

## Per-Position Analysis

### GK
- Performance: weak
- What worked: 696ms. GK rule 1 (on the line, INTERCEPT shots) is the only guard against long shots.
- What failed: 7 conceded from 7 on target, two of them their GK's long shots from his own end.
- Root cause: Shots on target are goals on this engine; nothing a GK rule can fix. The long shot must be pressed at the source.

### DEF
- Performance: weak
- What worked: Nothing visible.
- What failed: Coach: slow to mark an attacker who needed it. Their FWD Vic Surge scored three times. MARK 0 team-wide.
- Root cause: Two candidates. (a) Rule order: rule 5 (press the clear-line carrier) sits above the MARK guards (7–8) and its trigger flips as the swarm presser moves (the v11 Evaluator's notes 1 and 6), so DEF starts a press, abandons it, and only then marks. (b) Translation: the report shows MARK 0 and INTERCEPT 210, so his "MARK tightly" may have run as INTERCEPT (go to the ball) instead of standing on the attacker. 929ms is also his slowest healthy run; against a 186 ms MID every decision lands ~0.75 s later than theirs.

### MID
- Performance: adequate
- What worked: Three goals.
- What failed: 87 SHOOT commands, 5 shots. Kick-off rule 1 may be feeding their GK (Key Moment 4).
- Root cause: Kick-off shot from the center spot; to verify.

### FWD1
- Performance: weak
- What worked: 678ms.
- What failed: Coach: alone in front of their goal with the ball and took several ticks to shoot.
- Root cause: **Rule order.** Rule 2 shoots only when "their goal is in front of you", defined as farther from their end line than from the goal-to-goal line. Alone in front of the goal he is near the end line, so rule 2 is false and rule 3 ("near a touchline or their end line — ground PASS to MID") fires: he passes back instead of shooting. Not a model-speed problem; he is our fastest agent.

### FWD2
- Performance: adequate
- What worked: 916ms.
- What failed: FOLLOW 0 again.
- Root cause: Command mapping.

## Team-Level Observations
- Formation effectiveness: Lost 3-7. v11 is 2-1 in practice (2-1, 2-1, 3-7). Against Total Attack, v9 won 3-2 (015) with the coach's "be aggressive and shoot" sent live; v11 unattended lost by four.
- Should we change formation? No. Three rule fixes and one open question (DEF's slowness), see Action Items.
- Coordination gaps: (1) nobody presses their GK or DEF with the ball at their own end, and they score from there; (2) the kick-off shot from the center may hand the ball to their GK; (3) Hertz passes back from the one place he should shoot.
- Opponent patterns: Total Attack is the same template at the back (182–186 ms, MOVE 58%) but their GK is the MVP: 120 commands, two goals, launches every attack. Their FWD Vic Surge scored three. Their 11 shots is the most against us in 25 matches.
- Opponent formation: GK, DEF, MID, FWD, FWD.
- Model question (coach): would smaller models make Hertz and Turing react faster? Our agents have never answered under ~600 ms on any model we tried (Haiku, Sonnet, Nova Lite 2); the opponents' 180–210 ms agents are a different thing (see `bug.md`). Hertz's problem is a rule (above). Turing's may be both; a Nova Micro test on DEF in one practice match would answer the speed half, the rule fix answers the other.

## Action Items
- [ ] v12 brief (through the workflow): FWD1 — "You have the ball inside their box — SHOOT at once at full power" above the end-line pass rule, and the end-line rule excludes the box. MID — kick-off: through ball to Hertz if free, else ground PASS to FWD2 (no shot from the center spot). FWD1 — PRESS their GK (and their DEF when he is the deepest carrier) when he has the ball, sprinting: the one exception to "never presses"; it stops the GK long shot at the source (6 GK goals against us, 5 DEF). DEF — put the MARK guards (7–8) above the clear-line press (5) when an attacker without the ball is already goal-side, so he marks first and presses second. (priority: high)
- [ ] Model test, one practice match: Turing (DEF) on Nova Micro with the v12 prompt. Record his latency and whether the marking improves. If he drops well under 600 ms with the same behaviour, try Hertz too. (priority: medium)
- [ ] Watch the next replay for the kick-off sequence: does Tesla's center-spot shot reach their GK? (priority: medium)
- [ ] Office hours: MARK translated as MARK (101) in 019 and as nothing/INTERCEPT (0 / 210) in 020 from identical prompts; SHOOT 0 in 019 with 2 goals. Ask how commands are derived from the prompt text. (priority: high)

## Opponent Scouting Notes
- Updated `strategy/opponent-notes/total-attack-united.md`.
