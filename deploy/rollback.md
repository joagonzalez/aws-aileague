# Rollback

Every release is tagged `deploy-vN-YYYY-MM-DD` and the tag holds the exact paste text that was deployed. To put a previous release back on the platform:

```bash
git show deploy-v12-2026-10-06:deploy/paste-ready.md > /tmp/paste-v12.md
```

Paste each block from that file into the player's instructions, set the models it names, click Redeploy, then update `deploy/platform-state.json` (`prompt` per player pointing at `prompts/<pos>/vN.md` of that release) so the dashboard and `paste-ready.md` say what is really deployed. Say so in the next match log's `Deploy tag:` line.

`deploy/backups/` holds platform exports taken before a switch (the portal's own JSON, with model IDs); `deploy/agents-import.json` is the current release in that same format. Re-importing a backup is the fastest rollback if the portal accepts imports.

Known-good fallbacks:
- `deploy-v12-2026-10-06` — 2-1, 2-1 vs Benchmark/Fort Knox on v11 and the v12 fixes (in-box shot, GK press, kick-off pass, GK-to-Hertz kick); 3-5 vs Total Attack. Set DEF to Claude Haiku, not the Nova Micro the tag's file shows.
- `deploy-v10-2026-10-06` — the competitive 5-4 and 2-0 wins (C002, C003).
