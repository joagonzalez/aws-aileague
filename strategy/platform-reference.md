# Platform Reference (official AWS workshop pages)

Source: https://catalog.workshops.aws/agentic-football/en-US/ — "How to play" (overview, Actions and Stats, Game Rules), "Phase 1: Build Your Team" and the Agent Prompts Library (Aggressive Team sample). Captured 2026-10-06 from pasted page text; the site is a JS app and cannot be scraped.

This is the ground truth for what the agents can do and see. Our own observations are marked *(ours)*.

## Match and invocation

| Fact | Value |
|------|-------|
| Format | 5v5, fully automated, documented as 5 minutes *(ours: regulation has ended around 2' in practice, then overtime; confirm the competition length)* |
| Invocation rate | ~1 invocation per agent every 2 seconds. Each agent is invoked independently per tick with the same game state |
| Decision timeout | 5 seconds. If the agent does not answer in time, **the player holds its last command** |
| Visibility | Only what a player on the pitch could see. Opponent prompts and code are never visible |
| Default AI | Each player has a built-in AI underneath. `CLEAR_OVERRIDE` returns a player to it; `RESET` clears all overrides for the team. *(ours: competitive 001, 33 ms / 52 commands, was the default AI playing, not our prompts)* |

Latency implication *(ours)*: both teams get the same number of decisions (400 vs 400 commands in match 017; 725 vs 725 in 001). Our 0.7–1.0 s average costs reaction lag inside the tick, not decisions. Only output length can reduce it; the timeout is far away.

## Game state the agent sees each tick

- `tick`, `gameTime` (seconds), `playMode` (`KICK_OFF`, `OPEN_PLAY`, `FREE_KICK`, ...), `score` (home/away)
- `ball`: position (x, y, z), velocity, `isFree`, `possessionAgentId`
- `players[]`: `agentId` (index 0 is always the GK), `teamCode`, position, velocity, orientation, `stamina` (0–100), speed, `isSprinting`, `currentAction`, `lastAction`
- `teamChat[]`: the latest coach instructions sent from the Player Portal, read on the next tick
- `teamId`, `myPlayers` (the single index being invoked)

So the agent **does** see the score, the clock and every player's stamina and movement direction. It does not see fouls or cards directly (they show up as `FREE_KICK` play mode and a missing player).

Pitch: x ≈ −55 to +55, y ≈ −35 to +35. HOME (team 0) attacks toward +x, AWAY toward −x. Our prompts stay side-agnostic ("their goal"), which is correct because we can be either.

## Commands

The agent returns a JSON array with one command for its player: `commandType`, `playerId`, `parameters`, `duration` (0 for one-shot, ticks for maintained). On the Harness path the platform builds this from our plain-English tactics.

| Command | Kind | Parameters | Notes |
|---------|------|------------|-------|
| `MOVE_TO` | one-shot | `target_x`, `target_y`, `sprint` (bool) | Sprint is faster but drains stamina |
| `PASS` | one-shot | `target_player_id`, `type` = `GROUND` / `AERIAL` / `THROUGH` | **Player must have possession.** THROUGH "plays the ball into space ahead of the target". "Through ball" and "lofted/aerial pass" are the plain-English hooks |
| `SHOOT` | one-shot | `aim_location` = `TL` / `TR` / `BL` / `BR` / `CENTER`, `power` 0–1 | **Player must have possession**; a SHOOT without the ball is dropped. *(ours: 89 SHOOT commands → 3 shots in match 022, 36 → 0 in 021: agents issue it without the ball and waste the tick.)* Corners are real aim points |
| `SLIDE_TACKLE` | one-shot | `target_player_id`, `sprint`, `distance` | "Risky aggressive tackle": the foul source. We never ask for it |
| `GK_DISTRIBUTE` | one-shot | `target_player_id`, `method` = `THROW` / `KICK` | GK only, **to a named teammate**. Logged as "GK Dist" in match reports |
| `PRESS_BALL` | maintained | `intensity` 0–1 | "Chase and pressure the ball carrier. Above 0.5 the player sprints; above 0.3 they attempt tackles." So pressing is the tackle (foul) source; "press hard" = sprint + tackles |
| `MARK` | maintained | `target_player_id`, `tightness` = `LOOSE` / `TIGHT` | "Man-mark a specific opponent" |
| `INTERCEPT` | maintained | `aggressive` (bool) | "**Position to cut out a pass.** aggressive: true commits more forcefully." No target: the engine picks the lane. A legitimate second-presser job; "INTERCEPT the pass to X" is still inexpressible |
| `FOLLOW_PLAYER` | maintained | `target_player_id`, `target_team` = `HOME` / `AWAY`, `distance` | **Works on teammates too**: shadow a player at a set distance. Loose marking or tracking a run |
| `SET_STANCE` | tactical | `stance` 0 = Balanced, 1 = Attacking, 2 = Defensive | Tactical commands "stay active until explicitly cleared" |
| `CLEAR_OVERRIDE` | tactical | none | "Remove active manual command — player returns to default AI behavior." **Never want this**; it is what our "CLEAR" produced |
| `RESET` | tactical | none | Clear all overrides for the team. **Never want this** |

*(ours)* Match reports count a "Clear" command (5–35 per match for us). **It is `CLEAR_OVERRIDE`**: match 022's platform overview says "Panic's CLEAR_OVERRIDE spam (25 commands)" where our breakdown shows Clear 25. There is no CLEAR command; every "CLEAR" in our prompts handed that player to the default AI for the decision. Never write "clear", "reset", "override" or "default" as an action; name a receiver or shoot instead. Also *(ours, match 022)*: Nova Micro on DEF answered in 830 ms against 841–947 ms on Haiku, so latency is set by the harness, not the model.

Maintained commands persist for their duration and a timed-out player holds its last command, so a positional job expressed as MARK / FOLLOW / PRESS keeps running between our slow ticks, while a one-shot MOVE_TO is re-decided ~1 s late every tick.

## Rules

- A goal counts when the ball fully crosses the line between the posts. After a goal play restarts with a kick-off from the center, all players reset to starting positions, the team that conceded kicks off. The docs call the seconds after a goal "a window to set up your formation".
- **The ball never goes out of play.** No throw-ins, corners or goal kicks; no penalties. Possession changes only by tackles, interceptions and goals. *(ours: this is why chasing the ball into a corner is a trap: it never leaves, so a corner scramble can last.)*
- Fouls and cards exist ("pressing too hard risks fouls and cards"); a card can reduce the player count. Free kicks are the restart.
- Stamina is real and sprinting drains it over a continuous match with no stoppages.

## Workshop sample prompts (Aggressive Team) — what they tell us

- Structure: identity ("controlling ONLY player N"), role bullets, a numbered priority list, the full command list with parameters, field coordinates, strict JSON response format. On the competition platform the command list and response format are added by the harness; we only supply the tactics.
- Thresholds the authors consider normal: SHOOT within ~35 units (MID) to ~40 units (forwards) of goal, DEF from ~30; `power` 1.0 for every shot; PRESS intensity 0.9–1.0; INTERCEPT `aggressive: true`.
- Their own advice: "Keep prompts concise — your agent has a 5-second response window. Every unnecessary token is time wasted."
- The aggressive GK is told to come to the halfway line and shoot from ~35 units. Opposing GKs have scored on us from their own end four times, which is consistent with long shots being strong on this engine.
