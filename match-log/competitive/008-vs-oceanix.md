# Match 008: vs Oceanix

## Result
- Score: 2 - 3 (LOSS)
- Date: 2026-10-08
- Type: competitive
- Formation: 1-2-1
- Strategy: Swarm
- Deploy tag: deploy-v14-2026-10-07
- Prompt versions deployed: GK v13, DEF v13, MID v12, FWD1 v12, FWD2 v13
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

We play as Kernel Panic FC. Coach watched; no live messages sent. Goals: 1': Agent 3 (FWD) 0-1. 1': Unknown (us) 1-1. 2': Agent 0 (their GK) 1-2. 2': Agent 2 (MID) 1-3. 2': Unknown (us) 2-3.

## Key Moments
1. Healthy signature: 903-1014 ms, all five ours, 92 commands per agent. A real loss with v14 running.
2. **73% possession, 6 shots, 2 on target; MOVE 309 (67%), INTERCEPT 0, MARK 0.** The MOVE share is the highest since C003's 89% (the v10 carry); v14's practice range is 34-55%. Oceanix pressed 250 times (54%). Under that press our possession turned into repositioning, not shots: Tesla's sidestep clause has no MOVE-with-ball constraint (the v14 Evaluator's note 2 warned it can repeat against a defender who tracks the step), and Lovelace's FOLLOW is MOVE too.
3. Their goals: FWD at 1' in transition, **their GK from his own end at 2'** (Agent 0), their MID at 2'. 4 shots, 3 on target. The sweeper-keeper long shot again, from a human team this time.
4. No Tesla goal (both ours 'Unknown'). PASS 24, GK Dist 7.
5. Shots on target = goals (2 of 2, 3 of 3). 40 matches running.

## Coach Interventions
| When | Message | Observed effect |
|------|---------|-----------------|
| — | None (watched, no messages sent) | — |

## Raw Stats
- Possession: 73% vs 27%
- Shots: 6 vs 4
- Shots on target: 2 vs 3
- Our commands: 460 total, 929ms avg latency
- Their commands: 460 total, 535ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 309 | 67% |
| Press | 88 | 19% |
| Intercept | 0 | 0% |
| Mark | 0 | 0% |
| Pass | 24 | 5% |
| Shoot | 17 | 4% |
| Clear | 15 | 3% |
| GK Dist | 7 | 2% |

"Clear" is CLEAR_OVERRIDE. Opponent: Press 250 (54%), Move 78 (17%), Pass 54 (12%), Intercept 28 (6%), Clear 20 (4%), Shoot 13 (3%), GK Dist 6 (1%), Follow 6 (1%), Mark 5 (1%).

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 948ms | | 100% |
| DEF (Turing) | 1014ms | | 100% |
| MID (Tesla) | 962ms | | 100% |
| FWD1 (Hertz) | 999ms | | 100% |
| FWD2 (Lovelace) | 903ms | | 100% |

Opponent: GK 205ms, DEF 199ms, MID 190ms (MVP, fastest: Agent 2), FWD 1058ms, FWD 1076ms. Agents named Agent 0-4. Most tactical: Shannon (92 commands).

## Per-Position Analysis

### GK
- Performance: adequate
- What worked: 948 ms, ours; 92 commands.
- What failed: Conceded 3 of 3 on target, one a GK long shot.
- Root cause: Shots on target are goals; prevention is upstream.

### DEF
- Performance: weak
- What worked: 1014 ms, ours.
- What failed: Transition goal at 1'; MARK 0.
- Root cause: Unknown from totals.

### MID
- Performance: weak
- What worked: 962 ms.
- What failed: No goal; team MOVE 67%, 17 SHOOT commands.
- Root cause: Sidestep clause without a MOVE-with-ball constraint; see v16 candidate.

### FWD1
- Performance: adequate
- What worked: 999 ms, slow for him.
- What failed: Possibly one of the two unknown goals.
- Root cause: Supply under a 54% press.

### FWD2
- Performance: adequate
- What worked: 903 ms.
- What failed: Possibly one of the two unknown goals.
- Root cause: —

## Team-Level Observations
- Formation effectiveness: lost 2-3 with everything running: v14's first competitive loss with a verified deployment. v14 vs human teams: 0-1 clean (C008), plus C006/C007 compromised.
- Competitive with prompts verified running since v10: C002 W 5-4, C003 W 2-0, C005 L 1-2, C008 L 2-3 (2-2, 10 for, 9 against). The human teams that beat us press at 50%+ (Pantera 50%, Oceanix 54%); the ones we beat press less (Nankatsu 54% but no GK threat; Speedy 51%).
- Candidate single fix (v16): add the MOVE-with-ball constraint Lovelace already has to Tesla ('NEVER MOVE with the ball, except the one sideways step of rule 4 — SHOOT or PASS it at once'), so possession under press turns into shots or lofts instead of a sideways carry. No rule changes.
- Opponent formation: GK, DEF, MID, FWD, FWD.

## Action Items
- [ ] v16 (one constraint line on MID), validated in one practice match vs Total Attack: MOVE share under 50%, shots at or above 4, Tesla scoring. Deploy for the last competitive matches only if it passes; v14 otherwise. (priority: high)
- [ ] Scouting saved: strategy/opponent-notes/oceanix.md. (priority: low)

## Opponent Scouting Notes
- Saved to `strategy/opponent-notes/oceanix.md`.
