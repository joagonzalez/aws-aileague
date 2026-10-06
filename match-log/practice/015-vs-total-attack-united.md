# Match 015: vs Total Attack United

## Result
- Score: 3 - 2 (WIN)
- Date: 2026-10-06
- Type: practice
- Formation: 1-1-2
- Strategy: Swarm
- Deploy tag: deploy-v9-2026-10-06
- Prompt versions deployed: GK v8, DEF v8, MID v7, FWD1 v7, FWD2 v8
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

## Key Moments
1. Same setup as match 014, pasted from `deploy/paste-ready.md` (Hertz on the FWD2 v7 text, Lovelace on FWD2 v8, both Nova Lite 2). First match against Total Attack since the 0-2 loss in 007.
2. 1': Tesla (MID) scored during our possession and high press.
3. 2': Vic Surge (their FWD) equalized at once.
4. 2': Tesla scored again, then completed his hat-trick in the same minute (5 goals for Tesla across 015 and 016).
5. 2': Max Fury, their GK, scored from his own end. Fourth opposing-GK goal against us (006, 007, 009, 015).
6. Five goals in the first two minutes. Every goal this season still falls in minutes 1–3.
7. The coach typed "be more aggressive and shoot!" repeatedly throughout the match (see Coach Interventions). SHOOT commands: 58 (13%, our highest share ever), 4 shots, 3 on target, 3 goals.
8. Platform Coach's Corner for us: reduce PRESS (112), tighten MARK and SET_STANCE to lock defensive shape against faster counters.
9. Total Attack had two slow forwards (1093ms, 1301ms; avg 607ms). Every opponent since match 010 has had at least one forward near 1 s. This looks like a platform-side pattern for the AI teams, not a Benchmark quirk.

## Coach Interventions
| When | Message | Observed effect |
|------|---------|-----------------|
| Throughout, repeated | Be more aggressive and shoot! | Sent many times from kickoff. SHOOT commands reached 58 (13%), the season high, and 3 of 4 shots were on target. Cannot be separated from the prompts; the same message was sent in 016. |

## Raw Stats
- Possession: 58% vs 42%
- Shots: 4 vs 9
- Shots on target: 3 vs 2
- Our commands: 434 total, 842ms avg latency
- Their commands: 435 total, 607ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 178 | 41% |
| Press | 112 | 26% |
| Intercept | 68 | 16% |
| Mark | 0 | 0% |
| Pass | 0 | 0% |
| Shoot | 58 | 13% |
| Clear | 18 | 4% |
| GK Dist | 0 | 0% |

Opponent: Move 268 (62%), Press 87 (20%), Pass 46 (11%), Clear 23 (5%), Shoot 11 (3%). No intercepts or marks.

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 648ms | | 100% |
| DEF (Turing) | 865ms | | 100% |
| MID (Tesla) | 989ms | | 100% |
| FWD1 (Hertz) | 612ms | | 100% |
| FWD2 (Lovelace) | 919ms | | 100% |

Opponent: GK 194ms, DEF 188ms, MID 193ms, FWD **1093ms**, FWD **1301ms**. MVP and fastest: their DEF (Ray Chase, 188ms). Most tactical: their GK (Max Fury, 87 commands).

## Per-Position Analysis

### GK
- Performance: adequate
- What worked: 648ms. Held 7 of 9 shots off target (the press and shape did that).
- What failed: Conceded 2 from 2 on target, one from their GK's own end. Zero GK Dist and zero PASS logged for the whole team, so his releases were CLEARs.
- Root cause: Every shot on target is a goal on this platform (16 matches). The long ball from their GK is still undiagnosed (open since 008).

### DEF
- Performance: adequate
- What worked: 865ms. Part of 68 intercepts.
- What failed: 0 MARK. Their FWD scored at 2'.
- Root cause: v8 rule 7 marks only an attacker nearer our goal than the ball; against Total Attack's forward-running it should fire more. The 0 PASS count also means his rule 2 PASS-by-default never happened (or PASS is reported under another command).

### MID
- Performance: strong
- What worked: Hat-trick in two minutes, all from midfield. 989ms.
- What failed: Nothing.
- Root cause: MID rule 1 long shot, plus the live message. Tesla now has 13 goals in 009–016.

### FWD1
- Performance: adequate
- What worked: 612ms, his fastest.
- What failed: No goal; behavior not reported.
- Root cause: N/A.

### FWD2
- Performance: adequate
- What worked: 919ms. No corner report.
- What failed: Behavior not reported; no goal.
- Root cause: By design he gets few touches (v8).

## Team-Level Observations
- Formation effectiveness: 3-2 W, first ever against Total Attack. 58% possession.
- Should we change formation? No.
- Coordination gaps: **0 PASS and 0 MARK team-wide** in the platform breakdown, even though GK, DEF and MID prompts say PASS first and DEF/FWD2 have MARK rules. Either the platform collapsed those columns in this report, or the live "be aggressive and shoot" message overrode the pass-first rules. Compare with 016 (66 PASS, 175 MARK, same message): the difference is the opponent, so the rules do fire; against a high press there is nobody free to pass to.
- Opponent patterns: as advertised, early goals (2') and a GK who shoots from his own end. 62% MOVE, 2 of 9 on target.
- Opponent formation: Unknown.
- SHOOT commands to shots: 58 → 4, same ~7% conversion as always, but 3 of the 4 went in.

## Action Items
- [ ] Freeze this setup for competitive play (validated against all three AI teams: 1-0, 3-2, 4-0). (priority: high)
- [ ] Keep sending "be more aggressive and shoot!" from kickoff in competitive matches; it is a legal lever and was present in all three validation wins. (priority: high)
- [ ] GK: the opposing GK long ball has now scored four times. Watch Shannon on the next one; if he leaves the line, this is the first candidate for a post-competition fix. (priority: medium)
- [ ] Platform: check whether the report's command columns are complete (0 PASS here vs 66 in 016 with the same prompts). (priority: low)

## Opponent Scouting Notes
- Saved to `strategy/opponent-notes/total-attack-united.md`.
