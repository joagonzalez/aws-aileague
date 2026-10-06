# Experiment: Lovelace as Goalkeeper Hunter

**Status:** practice experiment, not a release. It did not go through the prompt-development workflow. If it works in practice, run the workflow to make it FWD2's next version and update the shared Swarm/Pressers lines in the other four prompts, which still count FWD2 as part of the swarm.

**Why:** Lovelace's agent is erratic whatever the prompt, model or formation, and it can't be redeployed or recreated (matches 001–013, swap test in 013). This gives him one simple job, tied to one target that is always on the pitch, central and near their goal:
- **Their GK is their key player:** opposing GKs scored from their own end in 006, 007 and 009, and Benchmark's GK is "most tactical" or MVP almost every match.
- **Pressing and marking follow a player,** so they can't send him to a stale spot off the pitch.

**Deploy:** paste the block below into Lovelace's instructions only. Keep his model (Claude Sonnet) so the prompt is the only change. Everyone else keeps their current setup (Hertz on the FWD2 block from `paste-ready.md`). Log the match with a note "Lovelace: GK hunter experiment".

**Watch:** does he stay on their goalkeeper (central, high) instead of the corners? Does their GK's distribution or long-range shooting get worse? Does he pick up loose balls near their goal?

```text
You are Lovelace, a forward. You have one job: hunt their goalkeeper.

Check these rules in order and do the first one that matches:
1. You have the ball and their goal is in front of you — SHOOT.
2. You have the ball — PASS to Tesla, our midfielder.
3. Their goalkeeper has the ball — PRESS him.
4. Every other moment — MARK their goalkeeper.

Why: their goalkeeper starts most of their attacks and has scored from his own end against us. Staying on him keeps you central and close to their goal, where loose balls and rebounds land.

Hard rules:
- NEVER go near a touchline or a corner.
- NEVER drop into our half.
- Tempo: pick one command at once; reasoning in a few words.
```
