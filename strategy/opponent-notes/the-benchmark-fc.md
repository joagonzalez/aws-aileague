# The Benchmark FC

## Matches
| # | Type | Score | Our versions |
|---|------|-------|--------------|
| 001 | practice | 1-0 W | all v1 |
| 002 | practice | 2-2 D | all v3 |
| 003 | practice | 2-1 W | all v4 |
| 004 | practice | 0-3 L | GK/DEF v5, rest v4 |
| 005 | practice | 0-1 L | GK/DEF v6, MID/FWD v5 |
| 006 | practice | 2-3 L | v7 |
| 009 | practice | 1-2 L | v8 |
| 010 | practice | 3-0 W | v8, forwards on Sonnet/Nova Lite 2 |
| 011 | practice | 2-1 W | same as 010 |
| 012 | practice | 1-2 L | 1-2-1 test: Hertz on Tesla's MID prompt |
| 013 | practice | 2-3 L | v8, forward prompts swapped |
| 014 | practice | 1-0 W | v9 (Lovelace FWD2 v8, Hertz on FWD2 v7 text), both on Nova Lite 2 |
| 017 | practice | 1-0 W | v9, health check after competitive 001 (Tesla 3') |
| 018 | practice | 2-1 W | v11 validation match (Tesla 1', unknown 2'); Benchmark's first shot on target against us in three matches |
| 024 | practice | 1-1 D | v13, coach watching; long match, MOVE 50% |
| 027 | practice | 3-0 W | v13, coach watching; three goals in minute 1, 0 on target against |
| 029 | practice | 6-3 W | v14, coach watching. Hertz hat-trick, Tesla x3; conceded 3 under a 38% press |
| 031 | practice | 2-1 W | v14 |
| 034 | practice | 2-1 W | v14 |
| 037 | practice | 4-3 W | v14, Tesla x4; conceded 3 under a 27% press |
| 039 | practice | 2-1 W | v14, their GK own goal |

## Official description
Balanced. Solid fundamentals: plays through the midfield, holds shape, finishes cleanly.

Practice page (official): "Balanced — Standard positioning — a good baseline to measure overall performance." This is the workshop's Balanced Team sample prompts. Our baseline opponent: 10 matches, use it to compare releases (017 v9 1-0, 018 v11 2-1).

## Profile
- **Speed**: 370ms average in 001, 199ms in 002 (every position 196–207ms). Ours: 813ms, then 863ms. They react 2–4x faster.
- **Style**: Heavy pressing (42% in 001, 40% in 002, 28% in 003). Possession 82% in 001 but only 46% in 003. Never intercepts or marks. Their DEF (Norm Easy, 195ms) was the platform MVP in 003.
- **Finishing**: Poor in 001 (7 shots, 0 on target). Scored 2 against v3 in 002. In 003: 5 shots, 1 on target, 1 goal (at 1'). In 004: 8 shots, 3 on target, 3 goals, all at 1'. Their FWD (Jay Smooth) scored twice, apparently into the space behind our higher DEF. Their DEF (Norm Easy) scored in 004 and was MVP in 003. In 005: 4 shots, 1 on target, 1 goal by Jay Smooth at 1' (his 3rd goal in two matches, all in minute 1). In 006: 12 shots, 3 on target, 3 goals (Jay Smooth twice, and their GK Drew Midway from his own end at 3'). Press rose to 45%. In 009: 65% possession, press 44%, their GK (Drew Midway) scored from his own end again at 2', winner at 3'. In 010: 78% possession but 0 shots on target. One of their FWDs ran at 853ms (normally ~200), so their average was 324ms. In 011: again one slow FWD (869ms, avg 336ms). Their DEF Norm Easy scored at 2'. In 014: two slow FWDs (955/993ms, avg 502ms), 6 shots, 0 on target; they passed far more (65, 17%) and used FOLLOW (36, 10%) for the first time.
- **Formation**: Unknown.

## Exploitable Weaknesses
- Their press leaves space behind it. Our goal came from intercepting during their press and attacking straight away.
- They cannot finish, so a compact block that MARKs and INTERCEPTs can absorb their possession.

## How to Play Them
- Do not try to out-pass them. Win the ball with interceptions, then hit it forward at once.
- No short build-up from GK or DEF while they are pressing near our box. Go long to the forwards.
- Shoot at every clear chance near their box. We will not get many possessions.
