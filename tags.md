# Deployment Tags

Every commit that introduces a new prompt release gets an annotated tag, even if the release is never played. "Played in" shows which matches actually ran it.

| Tag | Date | Commit | Positions Changed | Played in | Summary |
|-----|------|--------|-------------------|-----------|---------|
| `deploy-v1-2026-10-05` | 2026-10-05 | `c1c5346` | all (initial) | 001 | Initial release, 1-1-2. MID on Sonnet, FWD2 on Nova Lite 2. |
| `deploy-v2-2026-10-05` | 2026-10-05 | `36edf53` | all | — (never played) | Possession and passing emphasis, all Haiku. Superseded by v3 before any match. |
| `deploy-v3-2026-10-05` | 2026-10-05 | `5c55dd0` | all | 002 | Counter-punch: coach's "aggressive, hit the ball" message built in, zone pressing, long GK distribution, tempo line for latency. |
| `deploy-v4-2026-10-05` | 2026-10-05 | `be3b9ca` | all | 003 | First release through the automated workflow (approved round 1 after the loop fix). Middle-lane defending, one presser per zone, wide exit for the forwards, shared shooting trigger, GK 'distribute' only. |
| `deploy-v5-2026-10-05` | 2026-10-05 | `0077329` | GK, DEF (MID/FWD1/FWD2 stay v4) | 004 (0-3 L) | Fixes the back-line loop. GK CLEARs long and never passes to DEF. DEF has one fixed higher spot, never passes to GK, never moves while holding the ball. Middle lane kept. |
| `deploy-v6-2026-10-05` | 2026-10-05 | `e5d0193` | GK v6, DEF v6, MID v5, FWD1 v5, FWD2 v5 | 005 (0-1 L) | DEF back to v4 depth as one fixed spot at the box edge, CLEARs any ball he has or can reach there. GK CLEARs into the middle of their half. Forwards stay central between the posts and release at once. First run of the improved loop (prepassed carry-forward). |
| `deploy-v7-2026-10-05` | 2026-10-05 | `4fca8bb` | MID v6, FWD1 v6, FWD2 v6 (GK v7, DEF v7: Coordination only) | 006 (2-3 L), 007 (0-2 L), 008 (0-1 L) | Attack rewrite with visible cues (ball, teammates, goal) instead of pitch areas. Shoot from the middle (MID too). Closer forward presses. Wide → pass back. First 3000-char budget test (MID 2999, FWD 2990/2988). |
| `deploy-v8-2026-10-05` | 2026-10-05 | `27c7a32` | all (GK v8, DEF v8, MID v7, FWD1 v7, FWD2 v7) | 009 (1-2 L) | Identity switch Counter → Swarm: compact group around the ball, never wider than it, PASS first. DEF passes by default, GK passes to MID, swarm pressing (nearest presses, next cuts the pass). |

## Format

Tag name: `deploy-vN-YYYY-MM-DD`, where N is the team prompt release number.

```bash
git tag -a deploy-v3-2026-10-05 -m "v3: <what changed and why>"
git push origin master --follow-tags
```

When a release plays a match, add the match number to "Played in" and reference the tag in the match log's `Deploy tag:` line.
