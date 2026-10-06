# Playbook

## Team Identity: Swarm + Runner (v11, current)

Strategy name for match logs: **Swarm**.

MID (Tesla) and FWD2 (Lovelace) move as a compact pair around the ball in the center; FWD1 (Hertz) is the runner, a long pass ahead between their deepest outfield player and their goal. Tesla SHOOTs from their half on any clear line, even with a teammate ahead, and PASSes long to Hertz when an opponent blocks the line; Lovelace passes long to Hertz when he is free, otherwise shoots from distance. GK and DEF PASS to MID first and otherwise SHOOT long toward their goal (deep shots score on this platform: Turing in 003/006, opposing DEFs 4 times, opposing GKs 4 times from their own end). Every shot on target has been a goal in all 18 matches, so defence means preventing shots. v8 (three-man swarm, pass first) went 4-0 in 014-017 but bunched all three in midfield and switched off Tesla's shot whenever Hertz stood free ahead (coach, 017).

Why we switched (matches 006–008, coach direction): after four rewrites the forwards still drifted to the corners and contributed nothing. Our v5–v7 long clears landed in the corners where they chased them, passing collapsed (0 PASS vs Total Attack), and we lost five straight.

Pressing (v11, identical in every prompt): a carrier in our half or within a long pass of halfway — the nearer of MID and FWD2 (ties: MID) PRESSes him, sprinting; the other MARKs tightly the opponent closest to him. A carrier in our half between the sides of our box with no outfield teammate other than DEF between him and our goal — DEF PRESSes him too, GK inside our box. FWD1 never presses; nobody else presses. Why (C002): under v10 the second presser's job was written as "INTERCEPT the pass to X", which the harness ran as FOLLOW (71 FOLLOW, 0 INTERCEPT; INTERCEPT takes no target, see `strategy/platform-reference.md`), DEF pressed only the carrier nearest our goal, and their MID scored three unpressed long shots from midfield. v11 also removes the one-step carry (C003: 89% MOVE, 1 SHOOT), adds one kick-off rule per outfield player, through balls to Hertz, full-power long shots, GK throw/kick, and Lovelace FOLLOWing Tesla a short pass away when we have the ball.

## Previous Identity: Counter-Punch (v3–v7, retired)

Strategy name for match logs: **Counter** (v1 was **Possession**).

Our agents react about 2x slower than fast opponents (813ms vs 370ms in match 001), so we will not win a passing game. We defend compactly, win the ball with interceptions, and **hit it forward and at goal immediately**. Match 001's only goal came this way, right after the coach's live message asking the team to "be more aggressive and hit the ball."

## Tactical Patterns

### Pattern 1: Quick Counter (DEFAULT)
- **Trigger**: We win the ball anywhere
- **Execution**: The player who wins it hits it forward at once: a pass to an unmarked forward, or a long clear toward FWD1/FWD2 if nobody is free. FWDs run at goal and SHOOT at the first clear chance near the box.
- **Key**: No backward passes in our half. No holding. One or two touches from winning the ball to a shot.
- **Who's involved**: GK/DEF/MID → FWD1/FWD2

### Pattern 2: Strike on Sight
- **Trigger**: Any player has the ball inside or near the opponent's box with a clear line to goal
- **Execution**: SHOOT. Do not look for a better pass.
- **Key**: We get few possessions (18% in match 001). Every one near goal must end in a shot.
- **Who's involved**: FWD1, FWD2, MID

### Pattern 3: Coordinated Press
- **Trigger**: Opponent has the ball
- **Execution** (v7): their half — the forward closer to the carrier (FWD1 if equal); middle lane of our half outside our box — MID; inside our box — DEF. Nobody presses a wide carrier in our half. Everyone else INTERCEPTs the nearest passing lane or MARKs their attacker. Middle lane = the strip as wide as the box, goal to goal.
- **Key**: Match 001 had 124 PRESS commands and the opponent still kept 82% possession. Mass chasing does not work against faster agents. Intercepts created our goal.
- **Who's involved**: All outfield agents

### Pattern 4: Defensive Block
- **Trigger**: Opponent attacks into our half with more players than DEF can cover
- **Execution**: MID drops beside DEF and MARKs the free attacker. FWDs stay near the halfway line as counter outlets.
- **Key**: Never commit both forwards back. Keep the counter available.
- **Who's involved**: DEF + MID (block), FWD1/FWD2 (outlets)

### Retired: Controlled Possession
The v1 default. Dropped after match 001: 18% possession makes patient build-up unrealistic against faster opponents. Revisit only if we face a slower opponent and keep more than 50% possession.

## Default Approach

Play **Pattern 1 + 2** whenever we have the ball and **Pattern 3** whenever we don't. Switch to **Pattern 4** under sustained pressure.

## In-Match Coaching

The platform accepts live messages during a match, and they change agent behavior. Treat them as a tactical lever and log every one in the match log's **Coach Interventions** section.

| Situation | Message | Status |
|-----------|---------|--------|
| No shots, team passive | "Be more aggressive and shoot!" (sent repeatedly from kickoff) | **Proven** — goal at 2' in match 001 (sent once); sent throughout 015 (3-2 W) and 016 (4-0 W). Send it in every competitive match |
| Opponent keeps passing around our press | "One presser per zone only. Everyone else cut the passing lanes." | Untested |
| Players drifting to the flanks, middle open | "Protect the middle. Do not follow the ball into the corners." | Untested |
| Protecting a late lead | "Defend deep. MARK every attacker. CLEAR the ball long, no risks." | Untested |
| Chasing a goal late | "Everyone attack. MID join the forwards. SHOOT on sight." | Untested |

Rules:
- If a message clearly helps, write that behavior into the base prompts for the next version. The prompts should not depend on someone typing it mid-match.
- Note the minute each message is sent. If its effect fades, re-send it and record that too.

## Adjustments Log

- **Match 002 (v3)**: Drew 2-2. Shots went up (SHOOT 14 → 37), but we conceded from an empty middle and the forwards ran into the corner. → v4 adds middle-lane defending, a wide exit for the forwards and one shared shooting trigger for MID/FWD1/FWD2.
- **Match 001 (v1)**: Won 1-0. Controlled possession never happened (18% possession). Counter-attacking plus the coach's aggression message produced the only goal. → v3 makes Quick Counter + Strike on Sight the default, coordinates pressing, and retires Controlled Possession.
