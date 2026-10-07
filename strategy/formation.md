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
| 1-2-1 | DEF — MID MID — FWD | **Our current platform setting since match 012.** Midfield dominance. Control tempo. | Single DEF is exposed on counters. |
| 1-1-2 | DEF — MID — FWD FWD | Matches 001–011. Good attacking width. | Thin in defense and midfield. |

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

## Current Formation: 1-2-1 (platform setting; prompt roles GK - DEF - MID - FWD1 - FWD2)

**Correction, 2026-10-07.** The platform's formation selector has been on **1-2-1** since the match 012 test and was never switched back; match logs 013–022 and C001–C005 said 1-1-2 by habit and have been corrected. Every result since 012 (7-1 vs balanced/defensive teams, the competitive 5-4 and 2-0) was obtained with 1-2-1 on the platform and prompts written for the GK/DEF/MID/FWD1/FWD2 roles, which the platform keeps labelling the same way (012 log). What the selector changes is the starting/reset positions after each goal; the roles come from our prompts. **Decision: keep 1-2-1.** It is what works; switching to 1-1-2 now would be an untested change. Open question for the coach: under 1-2-1, which of slots 3 (Hertz) and 4 (Lovelace) starts in the second midfield spot and which as the lone forward?

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

## Positioning Philosophy (prompt roles; platform formation 1-2-1)

Middle lane = the strip as wide as the box, goal to goal (v4).

- **GK** (v13, v14 release; v14 changed wording only): Shoots at the empty goal when their GK is up near halfway with an open line (Total Attack's sweeper-keeper); otherwise as v11. On the goal line whenever an opponent has the ball, long range included, kick-offs included. INTERCEPTs shots and loose balls inside our box only; PRESSes a carrier inside our box when no teammate is goal-side. With the ball: throws it to MID if free, else kicks it long to FWD1 by name (021: an untargeted kick went to DEF and the ball circulated in our box). Never throws or kicks to DEF, never holds the ball.
- **DEF** (v13, Claude Haiku; v14 changed wording only): Empty-goal shot first; lofted pass to FWD1 else to MID, never an untargeted clear (CLEAR is CLEAR_OVERRIDE); INTERCEPTs a loose ball within reach. Otherwise as v11. One fixed spot at the edge of our box; holds it at kick-offs. Under pressure or deep in the box: lofted pass to FWD1 if he is ahead of the ball, else CLEAR to the center of their half (021). Otherwise PASSes to MID first; if MID is covered and he is free with a clear line, SHOOTs long at full power. PRESSes, sprinting, any carrier in or at the edge of our box; MARKs tightly any attacker inside our box or goal-side of the ball in the strip; only when no such attacker exists does he press a clear-line carrier in our half (020: he pressed instead of marking, their FWD scored three). Never passes to GK, never moves with the ball, never past halfway or wider than the box.
- **MID** (v12, Tesla): Our scorer. Kick-off: lofted pass to Hertz far ahead, free or not (v14). In their half with nobody close and the line blocked: one step sideways, then shoot (v14, copied from Total Attack). Empty-goal shot when their GK is up with an open line; SHOOT/PASS only with the ball at his feet; presses any opponent anywhere except their GK/deepest DEF; as the second swarm player marks the goal-side forward DEF is not marking, else INTERCEPTs; no sprint below 30 stamina. SHOOTs at once inside their box; SHOOTs at full power from their half whenever his line is clear, even with a teammate ahead; when an outfield opponent blocks the line (or from our half) and Hertz is free ahead, plays a through ball into his run. Nobody close and no clear line: shoot or pass, never carry (C003). Kick-off: through ball to Hertz if free, else ground pass to Lovelace, never a shot from the center spot (020); presses the taker when they kick off. Presses as the nearer swarm player, sprinting; otherwise MARKs tightly the opponent closest to the carrier, or screens toward our goal.
- **FWD1** (v12, Hertz, Nova Lite 2): The runner. Presses only their GK outside his box (v14; v13's press on any keeper/deepest DEF put him in the corners). Empty-goal shot; long shot from anywhere in their half on an open line or with nobody close; no sprint below 30 stamina. Off the ball he holds open central space ahead of the ball, between their deepest outfield player and their goal, at least a long pass from MID and FWD2; sprints ahead at kick-offs and onto through balls; receives the GK's long kick and DEF's loft. With the ball inside their box: SHOOT at once (020: he passed back from in front of goal); in their half with the goal in front: SHOOT at full power. Near a touchline or near their end line outside the box: PASS back to MID. Presses only their GK, or their deepest DEF in their half, with the ball (7 opposing-GK goals, 5 DEF goals against us); INTERCEPTs only a loose ball or a pass in flight within a short pass of him.
- **FWD2 / Lovelace** (v13, Nova Lite 2): Sidestep-then-shoot in their half when blocked and nobody close (v14). Empty-goal shot; long shot on an open line anywhere in their half; marks the goal-side forward DEF is not marking before anything else off the ball, else INTERCEPTs, marks their MID only when their GK/deepest DEF has the ball. FOLLOWs Tesla a short pass away when we have the ball (one maintained command instead of a re-decided spot); takes Tesla's kick-off pass when Hertz is not free. With the ball: through ball to Hertz if he is free ahead, else SHOOT at once inside their box or at full power from distance, else PASS to MID. When they have it: presses as the nearer swarm player, else MARKs tightly the opponent closest to the carrier, else MARKs tightly their midfielder; at their kick-off MARKs the receiver nearest the taker. Never carries. His agent is erratic regardless of prompt (013), so the prompt stays plain.

## Shape Principles

1. **Compactness**: Keep distance between lines tight. Don't let gaps open between DEF and MID.
2. **Swarm + runner** (v11): MID and FWD2 stay a short pass apart around the ball in the center, never wider than it; FWD1 is the runner a long pass ahead of them, between their deepest outfield player and their goal. v11 implements the pair with a FOLLOW (Lovelace shadows Tesla) and feeds the runner with through balls (official pass types, `strategy/platform-reference.md`). Previously (v8) all three stayed a short pass apart, which bunched them in midfield and switched off Tesla's shot (coach, 017).
3. **Narrow on defense**: Everyone tucks in centrally. Protect the middle.
4. **Transition speed**: Whoever wins the ball hits it forward at once: a pass to a free forward, or a long clear toward them.
5. **Swarm pressing** (v14, word for word in every prompt): any carrier except their GK — the nearer of MID and FWD2 (ties: MID) PRESSes him, sprinting; the other MARKs tightly the goal-side attacker DEF is not marking (goal-side: no ball, nearer our goal than the ball, in our box or in our half between its sides), else INTERCEPTs to cut out his pass. A central carrier in our half with nobody but DEF between him and our goal — DEF PRESSes him too, GK inside our box. FWD1 presses only their GK outside his box; nobody else presses him. (v13 sent Hertz at their GK and deepest DEF anywhere; he lived in the corners chasing keepers who hold the ball 80–133 commands a match, 023–027. Now the swarm takes their deepest DEF, and Hertz presses only a keeper out of his box.)

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
- **Competitive 002–003 (1-1-2, v10)**: 5-4 vs Nankatsu SC, 2-0 vs Speedy Gonzales, unattended. Attack validated (Tesla 2, Hertz 2 as the runner). Conceded 4 in C002, three of them unpressed long shots from midfield: the second-presser job was written as INTERCEPT-with-target, which the harness ran as FOLLOW. **Decision**: v11 keeps 1-1-2 and every attacking rule; rewrites pressing on the official command model, adds kick-off rules, removes the one-step carry. One practice match checking the command mix (INTERCEPT and MARK present, SHOOT ≥ 10%, FOLLOW only when we have the ball) before competitive use.
- **Practice 018–021 (1-1-2, v11)**: 2-1, 2-1, 3-7 and 0-2 (both losses to Total Attack United). Their GK and DEF scored from their own end unpressed; our kick-off shot fed their GK; the GK's untargeted long kick went to DEF and the ball circulated in our box (0 shots from 69% possession); Hertz passed back from inside their box. **Decision**: v12 keeps 1-1-2: in-box shot for every attacker, Hertz presses their GK/deepest DEF, kick-off pass instead of shot, mark before press for DEF, GK kicks to Hertz by name, DEF lofts to Hertz. DEF on Nova Micro for one practice match as a speed test.
- **Practice 022 (1-1-2, v12)**: 3-5 vs Total Attack. Their MID twice from his own half unpressed, their forwards camping at our box (Vic Surge 3), our 25 'Clears' were CLEAR_OVERRIDE (default AI), 89 SHOOT commands without the ball. **Decision**: v13 keeps 1-1-2 and every attacking rule; removes CLEAR, requires possession for SHOOT/PASS, extends the press to any opponent, adds the second marker on camping forwards, the empty-goal shot (sweeper-keeper), open-line long shots for the forwards, a stamina line. Every new rule is conditional on the opponent's behaviour so the prompts play as v12 against Benchmark/Fort Knox (7-1). Gate: validate vs Total Attack and Benchmark before competitive use; rollback in `deploy/rollback.md`.
- **Practice 023–027 (1-2-1 on the platform, v13)**: 3-1 Fort Knox, 1-1 and 3-0 Benchmark, 1-6 and 3-4 Total Attack. Coach: Hertz in the corners (chasing keepers), Tesla slow at kick-off and the short pass stolen, Tesla/Lovelace shooting less. **Decision**: v14 = v13 plus four edits (Hertz presses only a keeper out of his box; kick-off loft to Hertz; 'you have the ball'; sidestep-then-shoot for Tesla and Lovelace). Validate in one practice match before competitive use (2–3 practice matches left).
- **Practice 028–030 (v14)**: 5-1 Total Attack, 6-3 Benchmark, 4-2 Fort Knox. The four edits held (no minute-1 concession vs Total Attack, Hertz central and scoring 4 in three matches). **Decision: v14 frozen for the competitive matches; practice allowance exhausted (30/30).**
- **Match 004 (1-1-2, GK/DEF v5)**: Lost 0-3, all goals at 1'. The space behind DEF's higher spot, the risk the Evaluator flagged, was exploited. The switch rule (concede 2 or more) formally triggers, but the cause is one specific prompt change. **Decision**: v6 puts DEF back at v4's depth as one fixed spot at the edge of our box, and keeps v5's ball-release rules. If v6 concedes 2 or more, switch to 2-1-1.
