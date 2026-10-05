# Model Selection Strategy

## Available Models

| Model | Speed | Intelligence | Notes |
|-------|-------|-------------|-------|
| Nova Micro | fastest | lowest | Minimal latency, simple rule-following |
| Nova Lite | balanced | medium | Middle ground |
| Nova Lite 2 | balanced | medium | Newer version of Lite |
| Nova Pro | slowest | highest (Nova) | Complex reasoning, slower response |
| Claude Haiku | fast | high | Fast AND sharp — best speed/intelligence ratio |
| Claude Sonnet | moderate | highest | Strongest reasoning, moderate speed |

## Position-Model Mapping

### Design Principle
Football is real-time. Latency = slow reactions = goals conceded. But some positions need more intelligence than speed. The key trade-off:

```
Speed-critical positions  →  faster models
Decision-critical positions  →  smarter models
```

### Current Assignment (v1 — adjust after match data)

| Position | Model | Rationale |
|----------|-------|-----------|
| GK | Claude Haiku | Needs instant reactions (save, rush, hold). Simple decision tree but must be FAST. Haiku is fast AND sharp. |
| DEF | Claude Haiku | Quick marking/clearing decisions. Speed matters more than creativity. |
| MID | Claude Haiku | v1 used Sonnet (948ms — too slow). Haiku is fast AND sharp enough for passing/marking decisions. Speed > deep reasoning here. |
| FWD1 | Claude Haiku | Finishing is about timing and instinct. Fast model, sharp prompts. Scored at 2' in match 001. |
| FWD2 | Claude Haiku | v1 used Nova Lite 2 (840ms — slower than FWD1's 678ms). Unified to Haiku for consistent team speed. |

### Latency Findings (match 001)

| Model | Position | Latency |
|-------|----------|---------|
| Claude Haiku | FWD1 / GK / DEF | 678 / 682 / 802ms |
| Nova Lite 2 | FWD2 | 840ms |
| Claude Sonnet | MID | 948ms |
| *Opponent average* | — | *370ms* |

- Every model we used was 680–950ms. Switching models alone cannot reach the opponent's 370ms.
- The same model (Haiku) varied by 120ms across positions. Prompt complexity and how much the agent writes before acting probably matter as much as the model.
- Why output length matters: latency is roughly a fixed startup cost plus time per output token. The model reads input much faster than it writes output, so a longer prompt costs little, but every word of reasoning the agent writes before its command adds delay.
- v3 adds a tempo line to every prompt: "Choose one command immediately and keep any reasoning to a few words — no explanations." Compare per-agent latency in the next match against these numbers. If Haiku drops well below 680ms, output length is the lever.
- Caveats: the platform adds its own formatting, and if that asks for a reasoning field our line can only shorten it. Less reasoning can also mean worse decisions, so check decision quality in the debrief alongside latency.

### Next Model Experiments (one at a time, after v3 has a baseline)
1. **GK on Nova Micro**: the GK has the simplest decision tree. If latency drops a lot with no extra goals conceded, try DEF next.
2. **FWD1 on Nova Micro**: finishing depends on timing. Only try this if experiment 1 shows Nova Micro is much faster.

### Alternative Configurations to Test

**Config A: All Claude (speed gradient)**
- GK: Haiku, DEF: Haiku, MID: Sonnet, FWD1: Haiku, FWD2: Haiku
- Rationale: Claude models may follow prompts more precisely

**Config B: Smart core, fast edges**
- GK: Nova Micro, DEF: Nova Lite 2, MID: Claude Sonnet, FWD1: Claude Haiku, FWD2: Claude Haiku
- Rationale: GK barely needs reasoning, invest intelligence in attack

**Config C: All-in on intelligence**
- GK: Claude Haiku, DEF: Claude Sonnet, MID: Claude Sonnet, FWD1: Claude Sonnet, FWD2: Claude Haiku
- Rationale: Smarter agents everywhere, accept the speed cost

## How to Evaluate

After each match, note in the match log:
1. Did any agent seem slow to react? (model too heavy)
2. Did any agent make dumb decisions? (model too light)
3. Were there moments where speed mattered more than the choice made?
4. Were there moments where a smarter choice would have compensated for slower speed?

## Model Interaction with Prompt Complexity

Important: model choice and prompt complexity are coupled.
- **Fast/simple models** (Nova Micro) need VERY explicit, short prompts. They can't handle nuance.
- **Smart models** (Sonnet, Pro) can handle longer prompts with more conditional logic.
- If you use a fast model, keep the prompt under 150 words and use simple if/then rules.
- If you use a smart model, you can afford more sophisticated decision frameworks.

Adjust prompt length and complexity to match the assigned model.
