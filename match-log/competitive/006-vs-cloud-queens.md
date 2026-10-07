# Match 006: vs Cloud Queens

## Result
- Score: 0 - 4 (LOSS)
- Date: 2026-10-07
- Type: competitive
- Formation: 1-2-1
- Strategy: Swarm
- Deploy tag: deploy-v14-2026-10-07
- Prompt versions deployed: GK v13, DEF v13, MID v12, FWD1 v12, FWD2 v13
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

We play as Kernel Panic FC. Coach watched; no live messages sent.

## Key Moments
1. **Shannon answered in 220 ms; the other four in 1010–1226 ms.** Our GK on Claude Haiku has never been under 620 ms. One slot ran the platform's default agent (the ~200 ms profile every opponent's back three shows): a third deployment-failure mode after C001 (all five at 33 ms, 52 commands) and C004 (all five at ~200 ms). The goalkeeper's prompt was not running. GK Dist 9 is consistent with the default agent distributing.
2. **Platform slow for us again**: 994 ms average, Hertz 1123 ms (his normal range is 640–790), Lovelace 1226 ms. The losing signature from practice 035/040/041.
3. 2': four goals in the same minute: Unknown, casemiro (MID), maradona (FWD) twice. 6 shots, 4 on target, 4 goals. We had 3 shots, 0 on target.
4. Cloud Queens: the standard shape (back three at 204–209 ms, forwards at ~1200 ms), MOVE 57%, PASS 49 (12%, more than most), SHOOT 11, FOLLOW 36.
5. Our mix: PRESS 154 (37%), MARK 54 (the first MARK volume outside Fort Knox matches), INTERCEPT 67, MOVE 55 (13%, lowest ever), SHOOT 39 for 3 shots, PASS 22.
6. Shots on target = goals, both teams (0 of 0, 4 of 4). 37 matches running.

## Coach Interventions
| When | Message | Observed effect |
|------|---------|-----------------|
| — | None (watched, no messages sent) | — |

## Raw Stats
- Possession: 50% vs 50%
- Shots: 3 vs 6
- Shots on target: 0 vs 4
- Our commands: 420 total, 994ms avg latency
- Their commands: 420 total, 572ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 55 | 13% |
| Press | 154 | 37% |
| Intercept | 67 | 16% |
| Mark | 54 | 13% |
| Pass | 22 | 5% |
| Shoot | 39 | 9% |
| Clear | 20 | 5% |
| GK Dist | 9 | 2% |

"Clear" is CLEAR_OVERRIDE. Opponent: Move 239 (57%), Pass 49 (12%), Press 44 (10%), Follow 36 (9%), Clear 20 (5%), Shoot 11 (3%), GK Dist 9 (2%), Intercept 8 (2%), Mark 4 (1%).

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 220ms | | 100% |
| DEF (Turing) | 1010ms | | 100% |
| MID (Tesla) | 1089ms | | 100% |
| FWD1 (Hertz) | 1123ms | | 100% |
| FWD2 (Lovelace) | 1226ms | | 100% |

Opponent: GK 209ms (most tactical: kanh, 84 commands), DEF 207ms, MID 204ms (MVP, fastest: casemiro), FWD 1200ms, FWD 1193ms.

## Per-Position Analysis

### GK
- Performance: weak
- What worked: Nothing attributable to the prompt.
- What failed: 220 ms: the prompt was not running. 4 conceded from 4 on target.
- Root cause: Deployment: the GK slot ran the default agent. Check the agents page for Shannon's prompt text and model before the next match; redeploy.

### DEF
- Performance: weak
- What worked: MARK 54 team-wide.
- What failed: Four conceded in one minute.
- Root cause: Slow platform (1010 ms) and no goalkeeper of ours behind him.

### MID
- Performance: weak
- What worked: Nothing visible.
- What failed: No goal for the first time since 021; 39 SHOOT commands, 3 shots, 0 on target.
- Root cause: 1089 ms; four kick-offs in a minute after the concessions.

### FWD1
- Performance: weak
- What worked: Nothing visible.
- What failed: 1123 ms, far above his range; no shot.
- Root cause: Platform load.

### FWD2
- Performance: weak
- What worked: Nothing visible.
- What failed: 1226 ms.
- Root cause: Platform load.

## Team-Level Observations
- Formation effectiveness: Not a clean read: one slot on the default agent and the slow-platform signature on the other four. v14's record with everything running is 11-3 in practice.
- Should we change formation? No.
- Competitive record: 3-3 (C001 L deployment failure, C002 W, C003 W, C004 W default AI, C005 L, C006 L this). Four competitive matches left.
- **Detection rule, updated:** any single agent of ours at ~200 ms means that slot is on the default agent, even when the others look healthy.
- Opponent patterns: Cloud Queens is the standard template with more passing (12%) and accurate finishing (4 of 6).
- Opponent formation: GK, DEF, MID, FWD, FWD.

## Action Items
- [ ] Before the next competitive match: open each of the five agents on the platform and confirm the prompt text matches deploy/paste-ready.md and the model is set; redeploy all five (or import deploy/agents-import.json); export a backup and diff it against the paste file. (priority: high)
- [ ] Watch the first 15 seconds: any agent at ~200 ms, or all of ours above ~1050 ms, and the match is compromised; send "be more aggressive and shoot!" at kick-off regardless. (priority: high)
- [ ] Organizers (bug.md): a single slot reverting to the default agent on a deployed team. (priority: high)
- [ ] Scouting saved: strategy/opponent-notes/cloud-queens.md. (priority: low)

## Opponent Scouting Notes
- Saved to `strategy/opponent-notes/cloud-queens.md`.
