# Formation

## Understanding Formations

We have 5 agents: 1 GK (fixed) + 4 outfield. Formation notation: **DEF-MID-FWD**.
Any combination is valid — including 0 of any position type.
Changing formation means changing which positions get assigned AND rewriting prompts for affected players.

## Available Formations

### Defensive

| Formation | Shape | Strengths | Weaknesses |
|-----------|-------|-----------|------------|
| 3-0-1 | DEF DEF DEF — FWD | Near-impossible to score against. Counter-attack only. | Isolated forward, no midfield link. |
| 2-1-1 | DEF DEF — MID — FWD | Solid back line, MID links play. Balanced defense. | Only 1 attacking outlet. |
| 2-2-0 | DEF DEF — MID MID | Total midfield control. Suffocate possession. | No forward — who scores? |

### Balanced

| Formation | Shape | Strengths | Weaknesses |
|-----------|-------|-----------|------------|
| 2-1-1 | DEF DEF — MID — FWD | Strong defensively, MID distributes. | Can be outnumbered in attack. |
| 1-2-1 | DEF — MID MID — FWD | Midfield dominance. Control tempo. | Single DEF is exposed on counters. |
| 1-1-2 | DEF — MID — FWD FWD | Our current. Good attacking width. | Thin in defense and midfield. |

### Attacking

| Formation | Shape | Strengths | Weaknesses |
|-----------|-------|-----------|------------|
| 1-0-3 | DEF — FWD FWD FWD | Overwhelming attack. Constant pressure. | Huge gap between DEF and FWDs. No midfield. |
| 0-2-2 | MID MID — FWD FWD | All-out attack with midfield support. | No dedicated defender — GK is alone. |
| 0-1-3 | MID — FWD FWD FWD | Maximum firepower. | Suicidal defensively. |

### Exotic

| Formation | Shape | Strengths | Weaknesses |
|-----------|-------|-----------|------------|
| 2-0-2 | DEF DEF — FWD FWD | Direct play, skip the midfield. Long balls. | No link between lines. All-or-nothing transitions. |
| 0-4-0 | MID MID MID MID | Total control. Everyone can attack and defend. | No specialist finisher. Who scores? |
| 1-3-0 | DEF — MID MID MID | Possession stranglehold. | Need a MID who can finish. |

## Current Formation: 1-1-2 (GK - DEF - MID - FWD1 - FWD2)

```
        FWD1     FWD2
            MID
            DEF
            GK
```

### Why this formation (v1)
- Two forwards provide width and finishing options
- MID is the brain linking defense to attack
- DEF + GK provide enough cover for the back
- Simple to prompt — each agent has a clear, distinct role

### Known risks
- If DEF is beaten, GK is exposed 1v1
- MID is overloaded — must defend AND create
- If opponent parks the bus, we may lack midfield numbers to break them down

## Formations to Test in Practice

Priority experiments:

1. **2-1-1** — Add a second DEF, drop to 1 FWD. Test if defensive solidity wins more than extra forward.
2. **1-2-1** — Add a second MID, drop to 1 FWD. Test if midfield control compensates for fewer finishers.
3. **2-0-2** — No MID, direct play. Test if skipping midfield with long balls is effective.

## Positioning Philosophy (current 1-1-2)

Middle lane = the strip as wide as the box, goal to goal (v4).

- **GK** (v8): On the goal line whenever an opponent has the ball outside our box, long range included (their GKs scored from their own end in 006/007). INTERCEPTs only inside our box. With the ball: PASS to MID, else to DEF if free with no opponent close, else CLEAR toward the center.
- **DEF** (v8): Deep spot in front of our goal. PASSes by default to MID or a free teammate further upfield. CLEARs only deep in our box or under pressure. MARKs any attacker inside our box, and otherwise the attacker nearest our goal between the sides of our box. Never passes to GK, never moves while holding the ball.
- **MID** (v7): Heart of the swarm. Presses when he is the nearest swarm player, otherwise screens toward our goal or cuts the pass. SHOOTs only when near their goal with it in front of him and no better-placed free teammate.
- **FWD1** (v7): Part of the swarm: a short pass from MID and FWD2, never wider than the ball. SHOOTs with the goal in front and close unless a free teammate is better placed. Near a touchline or end line, PASSes back into the swarm at once.
- **FWD2 / Lovelace** (v8, Nova Lite 2): Plays as a second long-range shooter beside Tesla (level with him, never ahead, so Tesla's shooting rule keeps working). Marks their midfielder when they have the ball. Never carries the ball: shoots or passes at once. Stays away from touchlines and corners except when pressing or intercepting under the shared rule. His agent is erratic regardless of prompt (match 013), so the prompt is kept simple. On the platform, Hertz currently runs the FWD2 v7 text (013 swap).

## Shape Principles

1. **Compactness**: Keep distance between lines tight. Don't let gaps open between DEF and MID.
2. **Swarm in the middle** (v8): MID, FWD1 and FWD2 stay a short pass apart around the ball, never wider than it (farther from the goal-to-goal line than the ball is). Only the nearest of them goes to a wide ball. Previously **Attack and shoot through the middle**: the best shots come from straight in front of goal (coach, match 005). Forwards wait there and MID shoots there when free. A carry that drifts wide ends with a PASS back to the middle (matches 002/004/005 corner-running).
3. **Narrow on defense**: Everyone tucks in centrally. Protect the middle.
4. **Transition speed**: Whoever wins the ball hits it forward at once: a pass to a free forward, or a long clear toward them.
5. **Swarm pressing** (v8, word for word in every prompt): carrier in or at the edge of our box — DEF; anywhere else — the nearest of MID, FWD1 and FWD2 (ties: MID, then FWD1). The nearest of those three not pressing INTERCEPTs the pass to the opponent closest to the carrier.

## Formation Change Protocol

When switching formations:
1. Decide new position assignments for all 4 outfield players
2. Write or adapt prompts for each player's new role
3. Update coordination sections — different formations need different inter-agent communication
4. Run through the Writer -> Reviewer -> Evaluator pipeline for ALL affected prompts
5. Update this file with the new formation
6. Test in practice before competitive play

## Adjustments Log

- **Match 001 (1-1-2, v1)**: Won 1-0 but under siege (18% possession, 7 shots against, 0 on target). DEF+GK held. The two forwards produced the goal on the counter. Debrief suggested 1-2-1 for possession, but possession is not our game against faster agents (see `playbook.md`). **Decision**: keep 1-1-2 for the v3 test so the prompt change is the only variable. If v3 concedes, try 2-1-1 next.
- **Match 002 (1-1-2, v3)**: Drew 2-2. One goal conceded was a long shot from near halfway with the middle empty, because our players had followed the ball to the flanks. That's a behavior problem, not a numbers problem: a second DEF with the same 'press and force wide' rules would get pulled out too. **Decision**: v4 stays 1-1-2 with middle-lane rules. **Switch to 2-1-1** if v4 concedes through the middle again, concedes 2 or more, or DEF is still visibly overloaded.
- **Match 003 (1-1-2, v4)**: Won 2-1, 54% possession, conceded only at 1'. The middle lane held, so the switch rule did not trigger. The new problem was build-up: GK and DEF recycled the ball between themselves. → v5 (GK + DEF) keeps the shape and fixes the release. Watch the space behind DEF's new higher spot.
- **Match 004 (1-1-2, GK/DEF v5)**: Lost 0-3, all goals at 1'. The space behind DEF's higher spot, the risk the Evaluator flagged, was exploited. The switch rule (concede 2 or more) formally triggers, but the cause is one specific prompt change. **Decision**: v6 puts DEF back at v4's depth as one fixed spot at the edge of our box, and keeps v5's ball-release rules. If v6 concedes 2 or more, switch to 2-1-1.
