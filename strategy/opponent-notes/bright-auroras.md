# Bright Auroras

Competitive opponent (human team).

## Matches
| # | Type | Score | Our versions |
|---|------|-------|--------------|
| C001 | competitive | 0-5 L | v9 pasted, but our prompts did not run (52 commands, 33ms avg); the result says nothing about the matchup |

## Observed (C001)
- 26% possession, 8 shots, 5 on target, 5 goals. 50 SHOOT commands (10%), MOVE 66%, PRESS 13%, PASS 4%.
- Goals: their FWD Trueno three times at 1', their MID Brujula at 1', their DEF Andes (MVP) at 2'.
- GK, DEF and MID at ~200ms; both forwards slow (879ms, 913ms), the platform-wide pattern.
- Coach impression: well distributed, passing between each other. The report's PASS count (18) says the structure came from positioning rather than passes.

## If we meet them again
- They win by shot volume and conversion. Our press and intercept layer must be running (check the command count in the first seconds).
- Their forwards are slow; their DEF and MID are the fast, dangerous ones (two of five goals).
