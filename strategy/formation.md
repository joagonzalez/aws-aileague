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

- **GK**: Stays on goal line by default. Only advances for 1v1 situations.
- **DEF**: Sits in front of GK. Marks the most dangerous attacker. Clears the ball upfield.
- **MID**: The pivot. Links defense to attack. Covers for DEF when drawn out. Distributes to FWDs.
- **FWD1**: Left-biased forward. Primary finisher. Runs behind defense.
- **FWD2**: Right-biased forward. Support striker. Holds up play.

## Shape Principles

1. **Compactness**: Keep distance between lines tight. Don't let gaps open between DEF and MID.
2. **Width on attack**: FWDs spread wide to stretch the opponent. MID fills the center.
3. **Narrow on defense**: Everyone tucks in centrally. Protect the middle.
4. **Transition speed**: When we win the ball, MID's first instinct is to look forward to FWDs.

## Formation Change Protocol

When switching formations:
1. Decide new position assignments for all 4 outfield players
2. Write or adapt prompts for each player's new role
3. Update coordination sections — different formations need different inter-agent communication
4. Run through the Writer -> Reviewer -> Evaluator pipeline for ALL affected prompts
5. Update this file with the new formation
6. Test in practice before competitive play

## Adjustments Log

_Update after matches:_
- _No data yet — awaiting first match._
