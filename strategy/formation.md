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

- **GK** (v5): On the goal line whenever an opponent has the ball outside our box, long range included. Leaves the line only inside our box. With the ball: CLEARs long upfield past DEF toward the forwards. Never passes or distributes to DEF (match 003: v4's 'distribute' went short to DEF and started a back-line loop).
- **DEF** (v5): One fixed spot in the middle lane, midway between the edge of our box and the halfway line. Leaves it only to MARK the lane attacker closest to our goal (opponent ball in our half) or to win the ball in our box. Never leaves the middle lane, never passes to GK, never moves while holding the ball: PASS to a free teammate further upfield, else CLEAR long.
- **MID**: Screens the middle lane in our half and PRESSes carriers there (outside our box). In their half it stays just behind the ball and SHOOTs anywhere in the attacking third with a clear line.
- **FWD1**: Primary finisher and the only presser in their half. Takes short carries toward the middle. Near the corner, PASSes to the middle instead of running on.
- **FWD2**: Second finisher. Never presses; cuts passing lanes. Counter outlet beside the center circle, not out wide.

## Shape Principles

1. **Compactness**: Keep distance between lines tight. Don't let gaps open between DEF and MID.
2. **Attack through the middle**: forwards attack the box, not the flanks. A carry that drifts wide ends with a PASS to the middle (match 002 corner-running).
3. **Narrow on defense**: Everyone tucks in centrally. Protect the middle.
4. **Transition speed**: Whoever wins the ball hits it forward at once: a pass to a free forward, or a long clear toward them.
5. **One presser per zone** (v4, word for word in every prompt): their half — FWD1; middle lane of our half outside our box — MID; inside our box — DEF. Nobody presses a wide carrier in our half. The rest MARK or INTERCEPT.

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
