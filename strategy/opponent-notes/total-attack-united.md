# Total Attack United

## Matches
| # | Type | Score | Our versions |
|---|------|-------|--------------|
| 007 | practice | 0-2 L | v7 |
| 015 | practice | 3-2 W | v9 (Lovelace FWD2 v8, Hertz on FWD2 v7 text, both Nova Lite 2); coach repeated "be more aggressive and shoot!" |
| 020 | practice | 3-7 L | v11, unattended. Five conceded in minute 1; their GK scored twice and DEF once from their own end; 11 shots, 7 on target. Nobody presses their GK under v11 |
| 021 | practice | 0-2 L | v11, coach watching. 69% possession, 0 shots: GK's untargeted long kick went to DEF and the ball circulated in our box; their MID 1', GK 2' |
| 022 | practice | 3-5 L | v12 (DEF on Nova Micro, 830 ms: no gain), coach watching. Their MID x2 from his own half unpressed, FWD x3; their GK/DEF did not score for the first time (Hertz presses their GK). Our 'Clear 25' = CLEAR_OVERRIDE |
| 023 | practice | 1-6 L | v13, coach watching. Their GK x2, DEF, FWD x2 + unknown; PASS 0, 2 shots |
| 026 | practice | 3-4 L | v13, coach watching. Tesla hat-trick; their DEF x2, FWD x2; PASS 0, GK Dist 1 |
| 028 | practice | **5-1 W** | v14, coach watching. First win over them unattended: Tesla x2, Hertz, two unknown; no minute-1 concession; their GK scored once |
| 033 | practice | 3-1 W | v14 |
| 035 | practice | 4-5 L | v14, our avg 1058 ms; their DEF x2, GK, Vic Surge x2 |
| 036 | practice | 4-0 W | v14, 0 on target against |
| 040 | practice | 2-6 L | v14, our avg 1059 ms; **their GK x4**, DEF x2 |
| 041 | practice | 0-6 L | v14, our avg 1074 ms; Vic Surge x4, GK, MID; four conceded in minute 1 |
| 045 | practice | 2-1 W | v14 redeployed; Tesla x2, their GK long shot; 1094 ms avg, Turing 1890 ms |

## Official description
Aggressive. Presses high, commits numbers forward, takes risks for early goals.

Practice page (official): "Extremely Aggressive — GK plays sweeper-keeper, DEF joins every attack, FWDs camp near goal — exposes weak counter-attacking." This is the workshop's **Aggressive Team sample prompts** (Appendix): the GK "MOVE_TO the halfway line or beyond", shoots within ~35 units and presses in his half; the DEF carries forward and shoots from ~30; the MID is a second striker shooting from anywhere within ~35; both FWDs camp in the box, shoot from ~40 at power 1.0, never track back past halfway.

What that explains (020–022): their GK scored twice (020) and once (021), their DEF once, their MID four times, all long shots from their own half, because their prompts tell them to. Max Fury is MVP with 117–120 commands because the sweeper-keeper is involved in every phase.

**How to beat them (v13 candidate): their goal is empty whenever their GK is up at halfway.** Every shot on target is a goal on this engine, so any of our players with the ball and a clear line should SHOOT at full power at the empty goal from wherever they stand, the moment their GK is nearer the halfway line than his own goal. Their DEF joins every attack, so the space behind him is where Hertz's through balls go (the page says this team "exposes weak counter-attacking": our GK kick / DEF loft to Hertz is the counter). Their MID must be pressed in his own half (swarm reach), not only near halfway.

## Observed (007)
- As advertised: goals at 1' (FWD Vic Surge) and 2' (their GK Max Fury, directly from his own end). Press 44%, 10 shots (2 on target). Never intercepts or marks.
- We had 57% possession but 0 passes and 0 shots on target. Our counter never got going, because the forwards were wide and isolated.

## Observed (015)
- Still early goals (their FWD Vic Surge and their GK Max Fury, both at 2'), 62% MOVE, 9 shots but 2 on target. Two slow forwards (1093/1301ms, avg 607ms).
- We won 3-2 with Tesla's hat-trick in minutes 1-2 and 58 SHOOT commands (13%). Our PASS and MARK counts were 0: against their press nobody is free, so the pass-first rules fall through to shots and clears.
- Their GK scoring from his own end is their most repeatable threat against us (007, 015).

## What we expected before playing them
- **Danger:** the opening minutes. Every goal in our matches so far came in the first 3 minutes, and this team goes for early goals. Our shape must be set from kickoff.
- **Danger:** several attackers at once against one DEF. Watch whether MID's middle-lane screen and DEF's MARK rule cover two attackers in our half.
- **Opportunity:** they commit numbers forward, so there should be space behind them. This is what our counter is built for: GK and DEF clear long to forwards waiting near halfway.
- **Check:** does their high press force more long clears (good) or panic passes (bad)?
