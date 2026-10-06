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

- **GK** (v9): On the goal line whenever an opponent has the ball, long range included. INTERCEPTs inside our box only; PRESSes a carrier inside our box when no teammate is goal-side. With the ball: PASS to MID if free, else SHOOT long toward the center of their goal, else CLEAR the same way. Never passes to DEF.
- **DEF** (v9): One fixed spot at the edge of our box. PASSes to MID first; if MID is covered and he is free with a clear line, SHOOTs long; CLEARs only deep in the box or under pressure. MARKs any attacker inside our box and any attacker goal-side of the ball between the sides of our box; PRESSes the carrier in our half between the sides of our box only when that carrier is the opponent nearest our goal. Never passes to GK, never moves with the ball, never past halfway or wider than the box.
- **MID** (v8, Tesla): Our scorer. SHOOTs from their half whenever the goal is in front of him, even with a teammate ahead; when an outfield opponent blocks the line and Hertz is free ahead, PASSes long to Hertz. Presses as the nearest swarm player, otherwise screens toward our goal or cuts the pass.
- **FWD1** (v8, Hertz, Nova Lite 2): The runner. Off the ball he holds open central space ahead of the ball, between their deepest outfield player and their goal, at least a long pass from MID and FWD2. With the ball and the goal in front: SHOOT at once. Near a touchline: PASS back to MID.
- **FWD2 / Lovelace** (v9, Nova Lite 2): Level beside Tesla, never ahead of him. With the ball: PASS long to Hertz if he is free ahead, else SHOOT from distance, else PASS to MID. MARKs their midfielder when they have the ball. Never carries. His agent is erratic regardless of prompt (013), so the prompt stays plain.

## Shape Principles

1. **Compactness**: Keep distance between lines tight. Don't let gaps open between DEF and MID.
2. **Swarm + runner** (v10): MID and FWD2 stay a short pass apart around the ball in the center, never wider than it (farther from the goal-to-goal line than the ball is); FWD1 is the runner ahead, a long pass from them, between their deepest outfield player and their goal. Previously (v8) all three stayed a short pass apart, which bunched them in midfield and switched off Tesla's shot (coach, 017).
3. **Narrow on defense**: Everyone tucks in centrally. Protect the middle.
4. **Transition speed**: Whoever wins the ball hits it forward at once: a pass to a free forward, or a long clear toward them.
5. **Swarm pressing** (v10, word for word in every prompt): carrier in our half between the sides of our box who is the opponent nearest our goal — DEF (plus GK inside our box); any other carrier — the nearest of MID, FWD2 and FWD1 (ties: MID, then FWD2); the next nearest INTERCEPTs the pass to the opponent closest to the carrier. Nobody else presses.

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
- **Matches 014–017 (1-1-2, v9)**: 1-0, 3-2, 4-0, 1-0 with Hertz on the FWD2 v7 text and Lovelace on FWD2 v8. Coach: forwards bunch with Tesla, DEF/GK seem to drift toward our goal. **Decision**: v10 keeps 1-1-2 and changes roles: Hertz becomes the runner, DEF and GK get long shots, Tesla shoots regardless of teammates. One practice match with the healthy-signature check before competitive use.
- **Match 004 (1-1-2, GK/DEF v5)**: Lost 0-3, all goals at 1'. The space behind DEF's higher spot, the risk the Evaluator flagged, was exploited. The switch rule (concede 2 or more) formally triggers, but the cause is one specific prompt change. **Decision**: v6 puts DEF back at v4's depth as one fixed spot at the edge of our box, and keeps v5's ball-release rules. If v6 concedes 2 or more, switch to 2-1-1.
