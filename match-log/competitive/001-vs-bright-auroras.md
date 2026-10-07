# Match 001: vs Bright Auroras

## Result
- Score: 0 - 5 (LOSS)
- Date: 2026-10-06
- Type: competitive
- Formation: 1-2-1 (platform setting since the match 012 test; this log originally said 1-1-2 by habit — corrected 2026-10-07)
- Strategy: Swarm
- Deploy tag: deploy-v9-2026-10-06
- Prompt versions deployed: GK v8, DEF v8, MID v7, FWD1 v7, FWD2 v8
- Models: GK Claude Haiku, DEF Claude Haiku, MID Claude Haiku, FWD1 Nova Lite 2, FWD2 Nova Lite 2

## Key Moments
1. **Our agents did not run our prompts.** 52 commands all match (practice matches: 335–725) against 480 for the opponent, 33ms average latency, every agent 85–96ms (practice: 590–1300ms). No LLM answers in 90ms. 13 FOLLOW commands were logged and no prompt of ours has ever used FOLLOW_PLAYER. PRESS, our most common command in practice, was 0. What played was the platform's default or fallback behaviour, roughly one command per agent every 12 seconds.
2. 1': Trueno (their FWD) scored three times and Brujula (MID) once, all in minute 1. 2': Andes (DEF) made it 5-0.
3. Coach observation: Turing ran toward our own goalkeeper instead of defending. DEF v8 forbids passing to GK and fixes his spot at the box edge; this is the default behaviour, not his prompt.
4. Coach observation: Bright Auroras were well distributed and passed between each other. Their report shows PASS 18 (4%) and MOVE 66%, so the "passing" was mostly positioning; the platform told them their pass count was low.
5. Bright Auroras: 50 SHOOT commands, 8 shots, 5 on target, 5 goals. Shots on target = goals, 17 matches running.
6. Their two forwards ran at 879ms and 913ms, like every opponent since match 010. The slow-forward pattern is platform-wide, not specific to the AI teams.
7. Setup as pasted from `deploy/paste-ready.md` before the match (to confirm: did the platform show the agents as deployed and the models as set when the match started?).

## Coach Interventions
<!-- Was "be more aggressive and shoot!" sent? Fill in, or write "None". -->
| When | Message | Observed effect |
|------|---------|-----------------|
| [minute] | [what you typed] | [what changed after it] |

## Raw Stats
- Possession: 74% vs 26%
- Shots: 8 vs 8
- Shots on target: 0 vs 5
- Our commands: 52 total, 33ms avg latency
- Their commands: 480 total, 492ms avg latency

## Command Breakdown (Our Team)
| Command | Count | % |
|---------|-------|---|
| Move | 14 | 27% |
| Press | 0 | 0% |
| Intercept | 1 | 2% |
| Mark | 6 | 12% |
| Pass | 5 | 10% |
| Shoot | 1 | 2% |
| Clear | 12 | 23% |
| GK Dist | 0 | 0% |

Also logged for us: Follow 13 (25%), a command none of our prompts use.

Opponent: Move 319 (66%), Press 63 (13%), Shoot 50 (10%), Clear 23 (5%), Pass 18 (4%), GK Dist 7 (1%).

## Agent Latency
| Position | Avg latency | p95 latency | Success |
|----------|-------------|-------------|---------|
| GK (Shannon) | 96ms | | 100% |
| DEF (Turing) | 88ms | | 100% |
| MID (Tesla) | 85ms | | 100% |
| FWD1 (Hertz) | 88ms | | 100% |
| FWD2 (Lovelace) | 94ms | | 100% |

Opponent: GK 208ms, DEF 200ms, MID 203ms, FWD **879ms**, FWD **913ms**. MVP: their DEF (Andes). Fastest: Tesla (85ms, which is the symptom, not an achievement). Most tactical: their GK (Cóndor, 96 commands).

## Per-Position Analysis

### GK
- Performance: weak
- What worked: Nothing attributable to the prompt.
- What failed: Conceded 5 from 5 on target.
- Root cause: Prompt not running (see Key Moments 1). No prompt conclusion can be drawn from this match.

### DEF
- Performance: weak
- What worked: Nothing attributable to the prompt.
- What failed: Ran toward our GK (coach). 12 CLEARs team-wide, 0 PRESS.
- Root cause: Default platform behaviour. DEF v8 never passes to GK and holds the box edge.

### MID
- Performance: weak
- What worked: Nothing attributable to the prompt.
- What failed: 1 SHOOT command for the whole team; Tesla had scored 13 in the previous 8 matches.
- Root cause: Prompt not running.

### FWD1
- Performance: weak
- What worked: Nothing attributable to the prompt.
- What failed: No shots on target.
- Root cause: Prompt not running.

### FWD2
- Performance: weak
- What worked: Nothing attributable to the prompt.
- What failed: As above.
- Root cause: Prompt not running.

## Team-Level Observations
- Formation effectiveness: Not measurable. The team that played was not ours.
- Should we change formation? **No. Change nothing in the prompts or models because of this match.** The v9 setup is 3-0 in the practice matches where it demonstrably ran (400+ commands, 600–1000ms per agent).
- Coordination gaps: N/A.
- Opponent patterns: Bright Auroras shoot a lot (50 SHOOT, 10%) and convert (5 of 8 on target). Their outfield agents are 200ms except two slow forwards. Possession 26% and they won 5-0: possession is irrelevant on this platform, as in our own 3-0 at 22%.
- Opponent formation: GK, DEF, MID, FWD, FWD.
- **Detection rule for next time:** before kickoff and in the first seconds, check the live command count and latency. Our healthy signature is ~600–1000ms per agent. Anything under 200ms for our agents means the prompts are not loaded.
- Candidate causes to check on the platform, in order: (1) the deployment was not active for the competitive match (a redeploy was needed, or competitive uses a separate deploy step); (2) model access or quota errors for Haiku / Nova Lite 2 at match time, with the platform silently substituting a default (the 100% "success" column would then be misleading); (3) a cold start in which the first LLM calls timed out and the platform fell back for the whole match; (4) the "Pre-match fitness" or readiness check was not run.

## Action Items
- [ ] Platform: open the agents page and confirm each agent shows our prompt text and the right model, and that the deployment status is active. Redeploy regardless, and run the readiness check. (priority: high)
- [ ] Platform: look for an error or invocation log for the match (Bedrock throttling, model access, timeouts). Ask the organizers whether a 33ms / 52-command match is a known failure mode. (priority: high)
- [ ] Before the next competitive match, play one practice match and confirm the healthy signature (400+ commands, agents at 600–1000ms, PRESS the top command) before spending a competitive slot. (priority: high)
- [ ] During the next competitive match, check the live stats in the first 15 seconds. If our agents are under 200ms, note it and treat the match as a deployment failure. (priority: high)
- [ ] Coach Interventions: record whether the live message was sent. (priority: medium)
- [ ] Scouting: Bright Auroras shoot 50 times a match; the only defence is preventing shots. Note for a possible rematch. (priority: low)

## Opponent Scouting Notes
- Saved to `strategy/opponent-notes/bright-auroras.md`.
