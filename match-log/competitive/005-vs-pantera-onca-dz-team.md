# Match 005: vs Pantera Onca DZ Team

## Result
- Score: 1 - 2 (LOSS)
- Date: 2026-10-06
- Type: competitive
- Formation: 1-2-1 (platform setting since the match 012 test; this log originally said 1-1-2 by habit — corrected 2026-10-07)
- Strategy: Swarm
- Deploy tag: deploy-v10-2026-10-06
- Prompt versions deployed: GK v9, DEF v9, MID v8, FWD1 v8, FWD2 v9
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

We play as **Kernel Panic FC**. Unattended. First competitive loss with our prompts running (healthy signature: 400 commands, 637–713 ms). Version to confirm with the coach: logged as v10 because v11 was released the same day and reported as not yet tried.

## Key Moments
1. 1': Ronaldo (their FWD) 0-1, "capitalized on Pantera's relentless PRESS_BALL setup (201 commands), forcing immediate turnovers in Kernel's build-up" (platform AI overview). A turnover in our build-up ended in a shot on target, which is a goal on this engine.
2. 2': "Unknown" 1-1 for us.
3. 3': Modrić (their MID) 1-2, in overtime territory (80 commands per agent against 70–73 in a regulation-length match). Their MID again: the fast ~200 ms MID has scored against us in C002 (three times) and now C005.
4. **33 SHOOT commands produced 2 shots.** In C002, 73 SHOOT commands produced 8 shots; in C003, 1 SHOOT command produced 6 shots. The SHOOT count and the shot count are unrelated, so SHOOT commands are often issued when the player cannot shoot (no ball, or blocked), and shots get counted from something else. Our conversion to actual shots is the real problem: 56% possession, 246 MOVE (62%), 2 shots.
5. MARK 58 (14%), the first time MARK has appeared in volume for us (C002: 3). PRESS 13, INTERCEPT 0, FOLLOW 0.
6. Shots on target = goals, both teams (1 of 1 us, 2 of 2 them). 22 matches running. 4 shots to 2 decided it.

## Coach Interventions
| When | Message | Observed effect |
|------|---------|-----------------|
| — | None (the match ran unattended; no live messages were sent) | — |

## Raw Stats
- Possession: 56% vs 44%
- Shots: 2 vs 4
- Shots on target: 1 vs 2
- Our commands: 400 total, 679ms avg latency
- Their commands: 400 total, 504ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 246 | 62% |
| Press | 13 | 3% |
| Intercept | 0 | 0% |
| Mark | 58 | 14% |
| Pass | 26 | 7% |
| Shoot | 33 | 8% |
| Clear | 22 | 6% |
| GK Dist | 2 | 1% |

Opponent: Press 201 (50%), Move 88 (22%), Pass 56 (14%), Intercept 33 (8%), Clear 15 (4%), Shoot 4 (1%), GK Dist 3 (1%).

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 637ms | | 100% |
| DEF (Turing) | 649ms | | 100% |
| MID (Tesla) | 713ms | | 100% |
| FWD1 (Hertz) | 661ms | | 100% |
| FWD2 (Lovelace) | 675ms | | 100% |

Opponent: GK 205ms (MVP, fastest: Courtois), DEF 210ms, MID 208ms, FWD **939ms**, FWD **1009ms**. Most tactical: Shannon (80 commands).

## Per-Position Analysis

### GK
- Performance: adequate
- What worked: 637ms, his fastest. 2 GK Dist only: the ball left the back by PASS/CLEAR.
- What failed: Conceded 2 from 2 on target. GK rule 1 holds the line against long shots; it cannot stop a shot on target on this engine.
- Root cause: Shots conceded, not saves missed. Prevention is upstream (DEF/MID press).

### DEF
- Performance: weak
- What worked: 22 team CLEARs.
- What failed: Goal 1 came from a turnover in our build-up at 1' (their press at 50%). DEF v9 rule 2 passes to MID first; against a press of 201 commands the short pass into the swarm is the turnover.
- Root cause: v9 build-up passes short into pressure. v11 keeps "PASS to MID first" too: watch this. If the next match shows the same, the fix is "under pressure in our half, CLEAR long toward Hertz before passing short".

### MID
- Performance: weak
- What worked: 713ms.
- What failed: No Tesla goal for the first time since 013 on our prompts. 2 team shots from 56% possession. Their MID scored again from midfield (3').
- Root cause: Pressed at 50%, his clear-line trigger rarely held; and under v10 nobody pressed their MID (C002 lesson, fixed in v11 by DEF rule 5 and the swarm press).

### FWD1
- Performance: adequate
- What worked: 661ms.
- What failed: No goal attributed.
- Root cause: 26 PASSes team-wide; the long ball to the runner was rare against a press that forced turnovers early.

### FWD2
- Performance: adequate
- What worked: 58 MARKs team-wide suggest his "MARK their midfielder" ran as MARK this time. Possibly the "Unknown" goal.
- What failed: Their MID still scored.
- Root cause: A loose mark (v10 does not say "tightly"); v11 does.

## Team-Level Observations
- Formation effectiveness: Lost 1-2 on 2 shots against 4. v10 competitive record with prompts running: 2-1 (C002 W, C003 W, C005 L). Competitive used: 5 of 10 (3-2).
- Should we change formation? No.
- Coordination gaps: the two concessions are the two v10 defects already addressed by v11: (a) nobody presses their MID in or near our half (C002, C005 3'); (b) build-up pass into a 50% press (C005 1'; v11 does not yet change this, see DEF).
- Opponent patterns: Pantera is the same template (PRESS 50%, back three at ~205 ms, forwards at ~1 s) but passes more than the others (PASS 14%) and shoots little (4 SHOOT commands, 4 shots, 2 on target: everything they hit was a real chance).
- Opponent formation: GK, DEF, MID, FWD, FWD.
- MOVE share since v10: 54%, 89%, (59% default AI), 62%. Our agents spend most ticks repositioning. v11 removes the one-step carry; check whether MOVE drops below 50%.

## Action Items
- [ ] Deploy v11 and play one practice match: confirm the healthy signature (600–1200 ms), MOVE under 50%, MARK and PRESS both present, FOLLOW only when we have the ball, DEF PRESS count. Then the next competitive match. (priority: high)
- [ ] v12 candidate if the practice match repeats the C005 1' turnover: DEF and GK under pressure in our half CLEAR long toward Hertz (the runner) before passing short to MID. (priority: medium)
- [ ] Investigate the SHOOT-command vs shot gap (33 commands, 2 shots): are agents issuing SHOOT without the ball? The platform may have a per-agent view. (priority: medium)
- [ ] Scouting saved: `strategy/opponent-notes/pantera-onca-dz-team.md`. (priority: low)

## Opponent Scouting Notes
- Saved to `strategy/opponent-notes/pantera-onca-dz-team.md`.
