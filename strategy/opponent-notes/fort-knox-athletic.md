# Fort Knox Athletic

## Matches
| # | Type | Score | Our versions |
|---|------|-------|--------------|
| 008 | practice | 0-1 L | v7 |
| 016 | practice | 4-0 W | v9 (Lovelace FWD2 v8, Hertz on FWD2 v7 text, both Nova Lite 2); coach repeated "be more aggressive and shoot!" |
| 019 | practice | 2-1 W | v11, unattended (Tesla 1', 3'); one shot on target against; MARK 101, PASS 53 |
| 025 | practice | 3-1 W | v13, coach watching; Tesla x2, Hertz; MARK 149, PASS 67, 0 SHOOT commands for 8 shots |
| 030 | practice | 4-2 W | v14, coach watching. Tesla x4; their GK scored from his own end; MARK 184, PASS 77, SHOOT 0 commands |
| 032 | practice | 4-0 W | v14, Tesla x4, MARK 126 |
| 038 | practice | 2-0 W | v14, Hertz x2; platform slow (1451 ms avg, 229 commands) |
| 043 | practice | 2-0 W | v14 redeployed; platform slow (1402 ms, Lovelace 2442 ms) |

## Official description
Defensive. Compact, disciplined, and lethal on the counter-attack.

Practice page (official): "Extremely Defensive — All players stay deep, MID acts as extra defender, minimal shooting — tests whether your attack can break a low block." The workshop's Defensive Team sample prompts. Our answer so far is the long shot (016 4-0, 019 2-1: Tesla from distance); a low block cannot be passed through, it is shot over. Their minimal shooting is why 019 had one shot on target against.

## Observed (008)
- Compact and patient: 57% possession, only 1 shot (on target, the goal at 3'). Move 61%, Press 27%.
- They pulled us into passive marking: our MARK was 41% (184), press 5%, 0 SHOOT commands. As predicted, they gave our counter little space.

## Observed (016)
- 70% MOVE, zero MARK, zero INTERCEPT, 2 shots, 0 on target. Two slow forwards (870/927ms, avg 459ms). Their GK was MVP, fastest and most tactical.
- We won 4-0 in two minutes (Hertz 2, Tesla 2) with MARK at 40% again (175, same share as the 008 loss), 66 PASS and 0 SHOOT commands. The MARK-heavy pattern against them is not passive when the ball also gets to Tesla and Hertz.

## What we expected before playing them
- **Danger:** probably our worst match-up. They won't push forward, so our counter has little space to attack. Their own counter targets the space behind DEF's v5 spot (midway between our box and halfway), which the v5 Evaluator flagged as the main risk.
- **Danger:** losing the ball in their half while MID and both forwards are forward. Check how fast DEF and MID get back into the middle lane.
- **Opportunity:** long-range shots. Our shared trigger (attacking third, no outfield player between ball and goal) may fire often against a deep block that leaves the edge of the box open.
- **Check:** do we keep possession without a way through (sterile), and do we then lose the ball and concede on the break?
