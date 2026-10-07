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
7. **Name the commands**: use the platform's command words in actions — MOVE, PRESS, INTERCEPT, MARK, FOLLOW, PASS, SHOOT (and throw / kick for GK) — so each rule maps directly to one command (official list in `strategy/platform-reference.md`). **Never write "CLEAR" as an action**: there is no CLEAR command; the "Clear" count in match reports is CLEAR_OVERRIDE, which hands the player to the platform's default AI (match 022's overview text: "CLEAR_OVERRIDE spam (25 commands)" = our Clear 25). To get the ball away, name a receiver ("lofted PASS to FWD1", GK "kick it long to FWD1") or "SHOOT at full power". Pass and shot qualifiers that map to real parameters: "through ball", "lofted pass", "ground pass"; "far corner", "center of the goal"; "sprint". Avoid actions with no command behind them ("shield", "wait", "make yourself big"). **INTERCEPT takes no target**: it means "go win the ball" (loose or in flight near you); never write "INTERCEPT the pass to X" (the harness ran that as FOLLOW in competitive 002). To cut a passing lane or stop a shooter, write "MARK X tightly"; a loose mark or "FOLLOW X at a distance" is shadowing, not blocking. Never write "reset", "override", "default", "clear" or "tackle": the first four can hand the player to the platform's built-in AI, the last is the foul-prone SLIDE_TACKLE.
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
