# Deployment Tags

Every commit that introduces a new prompt release gets an annotated tag, even if the release is never played. "Played in" shows which matches actually ran it.

| Tag | Date | Commit | Positions Changed | Played in | Summary |
|-----|------|--------|-------------------|-----------|---------|
| `deploy-v1-2026-10-05` | 2026-10-05 | `c1c5346` | all (initial) | 001 | Initial release, 1-1-2. MID on Sonnet, FWD2 on Nova Lite 2. |
| `deploy-v2-2026-10-05` | 2026-10-05 | `36edf53` | all | — (never played) | Possession and passing emphasis, all Haiku. Superseded by v3 before any match. |
| `deploy-v3-2026-10-05` | 2026-10-05 | see tag | all | — (pending) | Counter-punch: coach's "aggressive, hit the ball" message built in, zone pressing, long GK distribution, tempo line for latency. |

## Format

Tag name: `deploy-vN-YYYY-MM-DD`, where N is the team prompt release number.

```bash
git tag -a deploy-v3-2026-10-05 -m "v3: <what changed and why>"
git push origin master --follow-tags
```

When a release plays a match, add the match number to "Played in" and reference the tag in the match log's `Deploy tag:` line.
