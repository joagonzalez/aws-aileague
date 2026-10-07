# Prompt Schema Specification

Every player prompt MUST follow this structure. The Reviewer agent validates against this schema.

## Required Sections

### 1. Header
```
# <Position Name> — v<N>
Model: <model name>
```
Position must be one of: Goalkeeper, Defender, Midfielder, Forward 1, Forward 2.
Model must be one of: Nova Micro, Nova Lite, Nova Lite 2, Nova Pro, Claude Haiku, Claude Sonnet.
See `strategy/model-selection.md` for rationale on model choice per position.

### 2. Role (1-2 sentences)
Core identity. What this agent IS and its primary mission.
- Must be specific to position
- Must establish the agent's mindset

### 3. Decision Framework (priority-ordered)
The heart of the prompt. A ranked list of situation → action mappings:
```
1. [Highest priority situation] → [Action]
2. [Next situation] → [Action]
...
```
Rules:
- Situations must be concrete and recognizable (not vague like "when needed")
- Actions must be unambiguous (not "consider doing X")
- Priority order matters — higher items override lower items in conflict
- Aim for 5-10 rules. Fewer is better if they cover the scenarios

### 4. Personality / Tendencies
Behavioral biases that guide edge cases not covered by the decision framework:
- Aggression level (conservative / balanced / aggressive)
- Risk tolerance (low / medium / high)
- Positioning preference (deep / standard / high)
- Any other relevant bias

### 5. Coordination
How this agent's positioning fits with adjacent positions. Agents cannot talk to each other. Each one only sees the game state, so coordination means **positional expectations**, not messages:
- Where this agent should be relative to teammates (e.g., "FWD2 stays on the opposite side to FWD1")
- Who this agent passes to, and who it expects the ball from
- Who presses and who covers in each zone

Rules:
- Must be bidirectionally consistent (if DEF clears long toward the forwards, the forwards' prompts must say to stay high for it)
- No "tell", "call for", "signal" or "communicate". Match 001's command list has no talk command, so these instructions do nothing
- Keep coordination simple — complex multi-agent protocols break down

### 5b. Situational Rules (optional, from the official template's layer 3)
Context overrides from the game state the agent can see (score, clock, stamina). At most 2–3 one-line items, each backed by a logged situation or the official guidance:
- Stamina: "when your stamina is low, do not sprint" (official: below 30%).
- Score: only if a match log shows it would have changed a result. Matches are decided in minute 1 (C002: nine goals in two minutes), so "when WINNING play conservatively" has not paid; "when LOSING take more shots" is already the identity.
Omit the section when there is nothing to say; never add it to fill the template.

### 6. Constraints
Hard rules — things to NEVER do:
- Must be phrased as prohibitions
- Should prevent catastrophic errors specific to the position
- Keep to 3-5 constraints max

### 7. Changelog
Version history:
```
- v1: Initial draft — [brief description]
- v2: [What changed and why, referencing match if applicable]
```

## Platform Rules

The AWS platform auto-adds game commands and formatting. Key implications:

1. **Agents already know HOW** to move, pass, shoot, mark, press, intercept, throw, kick. We do NOT teach mechanics.
2. **We only define WHEN and WHERE** — tactical decisions, not physical actions.
3. **Plain English works best** — no code, no coordinates, no API calls.
4. **The pitch is directional** — our team attacks toward the opponent's goal.
5. **Priorities in order, be specific** — e.g., "if inside the box, shoot" (from AWS tip).
6. **6000 character limit** per player prompt on the platform.
7. **Name the commands**: use the platform's command words in actions — MOVE, PRESS, INTERCEPT, MARK, FOLLOW, PASS, SHOOT (and throw / kick for GK) — so each rule maps directly to one command (official list in `strategy/platform-reference.md`). **Never write "CLEAR" as an action**: there is no CLEAR command; the "Clear" count in match reports is CLEAR_OVERRIDE, which hands the player to the platform's default AI (match 022's overview text: "CLEAR_OVERRIDE spam (25 commands)" = our Clear 25). To get the ball away, name a receiver ("lofted PASS to FWD1", GK "kick it long to FWD1") or "SHOOT at full power". Pass and shot qualifiers that map to real parameters: "through ball", "lofted pass", "ground pass"; "far corner", "center of the goal"; "sprint". Avoid actions with no command behind them ("shield", "wait", "make yourself big"). **INTERCEPT takes no target**: officially "position to cut out a pass" (the engine picks the lane), also the right word for a loose or in-flight ball near you; never write "INTERCEPT the pass to X" (the harness ran that as FOLLOW in competitive 002). To stop a specific receiver or shooter, write "MARK X tightly"; a loose mark or "FOLLOW X at a distance" is shadowing, not blocking. **SHOOT and PASS need possession**: the engine drops them otherwise and the tick is wasted (match 022: 89 SHOOT commands, 3 shots), so on-ball rules must say "the ball is at your feet" and off-ball rules must not say SHOOT or PASS. PRESS above low intensity attempts tackles, so "press hard" is where fouls come from. Never write "reset", "override", "default", "clear" or "tackle": the first four can hand the player to the platform's built-in AI, the last is the foul-prone SLIDE_TACKLE.
8. **State, not durations**: agents see the game state each tick, including the score and the clock, so conditions about the score and the time are allowed ("we lead and under a minute remains"). Decisions are one command per tick, so write conditions about positions ("if the ball passes you"), never durations ("press for 3 seconds").
9. **Live coach messages**: the coach can type instructions during a match. A message that works should be written into the base prompt for the next version (see `strategy/playbook.md` → In-Match Coaching).

## Quality Guidelines

- **Character budget**: Hard limit is 6000 chars of pasted text (see `deploy/paste-ready.md`, which reports the count per player). Header, model and changelog are not pasted.
  - Fast models (Haiku, Nova Micro): ≤ 3000 chars pasted (raised from 2000 for v7). Use the extra room for clarity (plain definitions, observable cues, a short 'why' on critical rules), not more rules. Keep about 8 decision rules. Prompt length showed no link to latency in matches 001–005.
  - Smart models (Sonnet, Nova Pro): up to ~4000-5000 chars. More situational depth.
- **Priority shadowing**: a higher rule whose situation overlaps a lower one blocks the lower one. Put the more dangerous or more specific situation first (e.g., "attacker with the ball near our goal" above "attacker without the ball near you").
- **Conciseness**: Each section should be as short as possible while being unambiguous.
- **Specificity**: Avoid wording like "try to", "consider", "if possible". Use imperative: "do X", "never Y".
- **Testability**: Every rule in the decision framework should be verifiable — you should be able to watch a match and say "yes, the agent followed rule #3" or "no, it violated rule #5".

## Official Prompt Guidance — check on every iteration

From the workshop's "System Prompt Engineering", "Multi-Agent Coordination" and "Actions and Stats" pages (full text in `strategy/platform-reference.md`). The Writer applies these; the Reviewer checks them.

1. **Four layers, in this order**: identity and role; decision hierarchy (priority order that resolves trade-offs every tick, the last item is the default action); situational rules (optional, see 5b); constraints ("you must NEVER"). Our Coordination section sits between the hierarchy and the constraints.
2. **Every sentence must influence a decision.** No narrative, no "play well", no reassurance. The official anti-patterns are the Vague Prompt and the Novel; the official response-window advice is "be concise".
3. **Encode strategy as behaviours per phase**, never as a style word: what to do when the opponent has the ball, when we win it, when we have it in the attacking third. "Counter-attacking", "possession", "aggressive" are not instructions.
4. **Roles with boundaries** (coordination page): each prompt states the player's zone, primary action, trigger to leave the zone, and handoff (when he defers to a teammate). Handoffs are the shared Swarm and Pressers lines and must be identical in all five prompts.
5. **Teammate-aware rules** use what the agent sees: a teammate making a forward run gets a through ball into space; don't move into a zone a teammate already covers; move toward a pressed ball carrier to offer a pass; if a teammate already marks that attacker, mark the next nearest threat. The official "before shooting, check for a better-placed teammate" is **not** applied here: it switched Tesla's shot off (017) and shots on target are goals.
6. **Command realities** (Actions page): SHOOT and PASS need possession, so on-ball rules say "the ball is at your feet" and off-ball rules never say SHOOT or PASS; INTERCEPT positions to cut out a pass (no target); MARK takes a player and LOOSE/TIGHT; PRESS tackles above low intensity; GK_DISTRIBUTE and PASS take a named receiver, so every release names one; sprinting drains stamina; "CLEAR" is CLEAR_OVERRIDE and must never appear.
7. **Different positions, different prompts**: the GK's hierarchy should look nothing like the striker's. A rule copied across positions needs a reason in the changelog.
8. **Coordination failure patterns to check against** (coordination page): the Ball Magnet (all chase the ball), the Ghost Town (spread out, never pass), the Confusion (two press the same opponent), the Statue Garden (formation, no reaction). Name in the changelog which pattern the last match showed and which rule answers it.

