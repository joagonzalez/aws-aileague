# Bright Ballistas

Competitive opponent (human team). Players: Keeper (GK), Wall (DEF, MVP, 194ms), Piston (FWD).

## Matches
| # | Type | Score | Our versions |
|---|------|-------|--------------|
| C007 | competitive | 2-3 L | v14 pasted, but our team average was 412 ms with 0 SHOOT/MARK/INTERCEPT: the default-agent signature (C004) on some or all slots |

## Observed (C007)
- 49% possession, 6 shots, 3 on target, 3 goals: their DEF from distance, their FWD Piston, one unknown. MOVE 60%, SHOOT 44 (9%), PASS 32, PRESS 55 (12%): they shoot a lot and press little.
- Standard shape: back three ~195 ms, forwards not reported.

## If we meet them again
- A shooting team: prevent shots (press the carrier, mark the second attacker). With our prompts running, their 12% press should leave Tesla his long shots.
