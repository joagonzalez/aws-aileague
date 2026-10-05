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
How this agent interacts with adjacent positions:
- Which position(s) it communicates with
- What information it shares or expects
- How it responds to calls from teammates

Rules:
- Must be bidirectionally consistent (if GK tells DEF to push up, DEF's prompt must mention listening to GK)
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

## Platform Note

## Platform Rules

The AWS platform auto-adds game commands and formatting. Key implications:

1. **Agents already know HOW** to move, pass, shoot, mark, press, intercept, throw, kick. We do NOT teach mechanics.
2. **We only define WHEN and WHERE** — tactical decisions, not physical actions.
3. **Plain English works best** — no code, no coordinates, no API calls.
4. **The pitch is directional** — our team attacks toward the opponent's goal.
5. **Priorities in order, be specific** — e.g., "if inside the box, shoot" (from AWS tip).
6. **6000 character limit** per player prompt on the platform.

## Quality Guidelines

- **Character budget**: Hard limit is 6000 chars. Only the behavioral text is pasted (no header/model/changelog metadata).
  - Fast models (Haiku, Nova Micro): keep lean, ~1500 chars. Simple if/then rules.
  - Smart models (Sonnet, Nova Pro): can go richer, up to ~4000-5000 chars. More situational depth.
- **Conciseness**: Each section should be as short as possible while being unambiguous.
- **Specificity**: Avoid wording like "try to", "consider", "if possible". Use imperative: "do X", "never Y".
- **Testability**: Every rule in the decision framework should be verifiable — you should be able to watch a match and say "yes, the agent followed rule #3" or "no, it violated rule #5".
