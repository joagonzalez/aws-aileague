# Match 041: vs Total Attack United

## Result
- Score: 0 - 6 (LOSS)
- Date: 2026-10-07
- Type: practice
- Formation: 1-2-1
- Strategy: Swarm
- Deploy tag: deploy-v14-2026-10-07
- Prompt versions deployed: GK v13, DEF v13, MID v12, FWD1 v12, FWD2 v13
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

Coach watched; no live messages sent. Goals: 1': Max Fury (GK) 0-1. 1': Vic Surge 0-2, 0-3, 0-4. 2': Vic Surge 0-5. 2': Al Frenzy (MID) 0-6.

## Key Moments
1. Heaviest defeat since C001: four conceded in minute 1, 72% possession, 1 shot, 0 on target. Vic Surge four. Our latency 1074 ms average, Lovelace 1276. PASS 1, SHOOT 62 commands for 1 shot, GK Dist 0.
2. Coach: 'we started great winning everything and then the machines became better'. See the series summary: the losses coincide with our slowest matches, not with a change on their side.

## Coach Interventions
| When | Message | Observed effect |
|------|---------|-----------------|
| — | None (watched, no messages sent) | — |

## Raw Stats
- Possession: 72% vs 28%
- Shots: 1 vs 13
- Shots on target: 0 vs 6
- Our commands: 424 total, 1074ms avg latency
- Their commands: 425 total, 546ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 197 | 46% |
| Press | 82 | 19% |
| Intercept | 70 | 17% |
| Mark | 0 | 0% |
| Pass | 1 | 0% |
| Shoot | 62 | 15% |
| Clear | 12 | 3% |
| GK Dist | 0 | 0% |

"Clear" is CLEAR_OVERRIDE.

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 830ms | | 100% |
| DEF (Turing) | 1063ms | | 100% |
| MID (Tesla) | 1118ms | | 100% |
| FWD1 (Hertz) | 846ms | | 100% |
| FWD2 (Lovelace) | 1276ms | | 100% |

Opponent back three ~180-210 ms, forwards 840-1435 ms (their numbers also rose in the later matches).

## Per-Position Analysis

### GK
- Performance: weak
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: see the v14 series summary (match 041).

### DEF
- Performance: weak
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: see the v14 series summary (match 041).

### MID
- Performance: weak
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: see the v14 series summary (match 041).

### FWD1
- Performance: weak
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: see the v14 series summary (match 041).

### FWD2
- Performance: weak
- What worked: see Key Moments.
- What failed: see Key Moments.
- Root cause: see the v14 series summary (match 041).

## Team-Level Observations
- **v14 series, 14 matches (028-041): 11-3, 46 for, 23 against.** vs Benchmark 5-0 (2-1, 6-3, 2-1, 4-3, 2-1), vs Fort Knox 3-0 (4-2, 4-0, 2-0), vs Total Attack 3-3 (5-1, 3-1, 4-0 won; 4-5, 2-6, 0-6 lost). Since v9 vs balanced/defensive teams: 17-1-1.
- **The three losses are our three slowest Total Attack matches.** Wins vs TA: 948, 865, 976 ms average; losses: 1058, 1059, 1074 ms (Turing 1319-1391, Lovelace 1067-1276). Match 038 (1451 ms, Lovelace 2172 ms, only 46 commands per agent) shows the platform was under load in the evening: above the 2 s tick an agent misses decisions entirely. Total Attack's prompts did not change; ours answered later. Against a team whose back three answers in 190 ms and whose first-minute blitz is decided by who reacts first, 200 ms of extra lag per decision is the difference between 4-0 and 0-6.
- Total Attack's goals in the losses: their GK 1+4+1, their DEF 2+2+0, Vic Surge 2+0+4, their MID 0+0+1. The keeper's long shots are the open problem of v14 (Hertz presses him only outside his box; he shoots from inside or at its edge, and every shot on target is a goal: 36 matches running).
- PASS is 0-1 in every Total Attack match, win or lose; passing collapses under their press regardless of result.
- The 30-match practice cap was not enforced (41 played).
- Opponent formation: GK, DEF, MID, FWD, FWD.

## Action Items
- [ ] Competitive: v14 stays frozen (17-1-1 vs balanced/defensive since v9; the competitive field has been balanced-shaped in all five matches). Check the first-15-second latency; if the platform is slow (our agents above ~1050 ms), expect the minute-1 blitz and send "be more aggressive and shoot!" at kick-off. (priority: high)
- [ ] Post-competition v15 candidates, each one rule: (a) their GK's long shot: Hertz presses their GK whenever he has the ball AND is nearer the halfway line than his goal line (sweeper position), not only outside the box; (b) kick-off after a concession vs a sweeper-keeper: the empty-goal rule should fire from the center spot (their GK is nearer halfway than his goal) — check on a replay whether it does; (c) PASS 0 under press: a lofted pass to Hertz as the first on-ball option whenever an opponent is within a few steps in our half. (priority: medium)
- [ ] Office hours / organizers: evening latency (1058-1451 ms average, Lovelace 2172 ms) and the 46-command match 038; a per-agent timeout count would show missed ticks. (priority: medium)

## Opponent Scouting Notes
- `strategy/opponent-notes/total-attack-united.md`.
