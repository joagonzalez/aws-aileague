# Platform issue: two competitive matches did not run our agents

Team: **Kernel Panic FC**. Date of the matches: 2026-10-06. Prepared for office hours on 2026-10-07.

Of our five competitive matches, two were not played by our deployed agents (Claude Haiku on GK/DEF/MID, Nova Lite 2 on FWD1/FWD2, Harness path). Both show the platform's "Success 100%" for every agent. We did not change models or prompts between the healthy matches and the failed ones.

## 1. What a healthy match looks like for us

Every match where our prompts ran has the same signature:

| Match | Result | Our avg latency | Per agent | Our commands | SHOOT | MARK / INTERCEPT |
|---|---|---|---|---|---|---|
| Practice 017 vs Benchmark | 1-0 W | 856 ms | 671–980 ms | 400 | 19 | 0 / 20 |
| C002 vs Nankatsu SC | 5-4 W | 730 ms | 658–940 ms | 615 | 73 | 3 / 0 |
| C003 vs Speedy Gonzales | 2-0 W | 1078 ms | 968–1159 ms | 350 | 1 | 0 / 0 |
| C005 vs Pantera Onca | 1-2 L | 679 ms | 637–713 ms | 400 | 33 | 58 / 0 |
| Practice 018 vs Benchmark | 2-1 W | 877 ms | 691–1028 ms | 400 | 30 | 1 / 37 |

Claude Haiku and Nova Lite 2 answer in **600–1200 ms**. That is the cost of one LLM call with our prompts.

## 2. C001 vs Bright Auroras (0-5): nothing ran

- **33 ms average latency, every agent 85–96 ms.** No LLM call returns in 90 ms.
- **52 commands for the whole match**, against 480 for the opponent and 335–725 in every practice match. About one command per agent every 12 seconds instead of every 2.
- **0 PRESS** (our most frequent command in practice, ~40%), **1 SHOOT** (our MID had scored 13 goals in the previous 8 matches), and **13 FOLLOW**, a command none of our prompts used at the time.
- Platform showed Success 100% for all five agents.
- Five shots on target against, five goals.

## 3. C004 vs Bright Artisans (2-0): something else ran, with a full command count

- **199 ms average latency, every agent 201–209 ms.** Our configured models never answer that fast; the previous and following matches with the same deployment were 637–1159 ms per agent.
- Command count was normal (365), so this is a different failure mode from C001.
- **0 SHOOT, 0 MARK, 0 INTERCEPT, 0 FOLLOW**; MOVE 59%, PRESS 32%. Our prompts produce SHOOT on 5–12% of ticks in every healthy match.
- Platform showed Success 100% for all five agents.
- We won, so this one did not cost us, but it shows the failure can recur silently.

Observation: the ~200 ms, press-heavy, no-MARK, no-SHOOT profile of our agents in C004 is identical to the GK/DEF/MID profile of **every** opponent we have faced, including the AWS reference team The Benchmark FC (206 / 208 / 206 ms, forwards 927 / 1014 ms). Whatever produces that profile (a built-in agent, a fallback, or a very small model with a minimal prompt), it played our five slots in C004 without our prompts.

## 4. Questions for the organizers

1. What does the platform do when an agent **errors or times out**: fall back to a built-in agent for that tick, or for the whole match? Is a fallback counted as "Success 100%"? Both failed matches show 100%.
2. Is there an **invocation / error log per match** (Bedrock throttling, model access, cold-start timeouts) for Kernel Panic FC on 2026-10-06, for C001 (vs Bright Auroras) and C004 (vs Bright Artisans)?
3. Does a competitive match use the **last "Redeploy"** state? How can we confirm the deployment was active at kick-off, and is there a readiness check we should run before each competitive match?
4. What are the **~200 ms agents**: ours in C004, and the GK/DEF/MID of every opponent and of The Benchmark FC? If that is a built-in or default agent, it changes how the stats should be read.
5. Can a match in which the platform demonstrably did not run the team's agents (C001: 52 commands at 33 ms) be **replayed or annulled**, since the cause is on the platform side?

## 4b. Command-count questions (practice 023–027 on v13, 2026-10-07)

6. **CLEAR_OVERRIDE persists with the word removed.** v13 has no "clear" anywhere in any prompt; the "Clear" count is still 9–23 per match (v12: 25). What emits CLEAR_OVERRIDE: the agent choosing it, or the harness on a timeout / unparseable response? Does it reset the player to the default AI for one tick or until the next command?
7. **SHOOT commands are unrelated to shots.** 0 SHOOT commands → 8 shots (025 vs Fort Knox); 79 → 2 (023), 75 → 7 (026). What makes a SHOOT command fail (possession test? range?), and what produced 8 shots with no SHOOT command (the default AI during CLEAR_OVERRIDE ticks?).
8. **PASS 0** in both matches against Total Attack United (023, 026) with 61–69% possession; 39–67 against the other teams. Is a PASS rejected when the target is marked or the carrier is pressed?
9. Is there a **per-agent command breakdown** anywhere? Team totals cannot tell which player's rule produced a command.

## 5. What we do on our side now

- Before each competitive match: open the agents page, confirm the deployment is active and shows our prompt text, run the readiness check.
- In the first 15 seconds of a live match: check per-agent latency. Under 300 ms means our prompts are not running.
- Full logs: `match-log/competitive/001-vs-bright-auroras.md` and `004-vs-bright-artisans.md`; detection rule in `CLAUDE.md` (Platform Notes).
