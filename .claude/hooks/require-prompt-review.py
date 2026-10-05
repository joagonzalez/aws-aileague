#!/usr/bin/env python3
"""Commit gate: a change to prompts/<pos>/current.md needs an approved review record.

If current.md is at version vN, prompts/<pos>/reviews/vN.md must exist, be part of the commit
(staged or already tracked), and contain the lines 'Reviewer: PASS' and 'Evaluator: APPROVE'.
Those records are written by the prompt-development workflow (.claude/workflows/prompt-development.js).

Runs two ways:
  - Claude Code PreToolUse hook on Bash (default): reads the tool call from stdin and only acts on
    `git commit`. Exit 2 blocks the commit and shows the reason to Claude.
  - git pre-commit hook: `python3 .claude/hooks/require-prompt-review.py --git-hook`
"""

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CURRENT_RE = re.compile(r"prompts/[^/]+/current\.md")


def git_lines(*args):
    result = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    return [line for line in result.stdout.splitlines() if line]


def changed_current_files(include_worktree):
    files = set(git_lines("diff", "--cached", "--name-only"))
    if include_worktree:
        files |= set(git_lines("diff", "--name-only"))
        files |= set(git_lines("ls-files", "--others", "--exclude-standard"))
    return sorted(f for f in files if CURRENT_RE.fullmatch(f))


def problems_for(path, include_worktree):
    full = ROOT / path
    if not full.exists():
        return []  # deletion — nothing to approve
    header = re.search(r"^# .+ — v(\d+)\s*$", full.read_text(), re.MULTILINE)
    if not header:
        return [f"{path} has no '# <Position> — vN' header"]
    version = header.group(1)
    record = f"{Path(path).parent.as_posix()}/reviews/v{version}.md"
    record_file = ROOT / record
    if not record_file.exists():
        return [f"{path} is v{version} but {record} does not exist"]
    text = record_file.read_text()
    missing = [line for line in ("Reviewer: PASS", "Evaluator: APPROVE")
               if not re.search(rf"^{line}\s*$", text, re.MULTILINE)]
    if missing:
        return [f"{record} is not an approval (missing {' and '.join(repr(m) for m in missing)})"]
    in_index = bool(git_lines("ls-files", "--", record))
    if not in_index and not include_worktree:
        return [f"{record} exists but is not staged — git add it with the prompt change"]
    return []


def main():
    if "--git-hook" in sys.argv:
        include_worktree = False
    else:
        try:
            payload = json.load(sys.stdin)
        except (json.JSONDecodeError, ValueError):
            return 0
        command = (payload.get("tool_input") or {}).get("command", "")
        if not re.search(r"\bgit\b[^;&|\n]*\bcommit\b", command):
            return 0
        # `git add ... && git commit` or `git commit -a` will include worktree changes the index doesn't show yet.
        include_worktree = bool(re.search(r"\bgit\s+add\b|\bcommit\b[^;&|\n]*\s(-[a-zA-Z]*a[a-zA-Z]*|--all)\b", command))

    problems = [p for f in changed_current_files(include_worktree) for p in problems_for(f, include_worktree)]
    if not problems:
        return 0
    print(
        "Blocked: prompt changes need an approved review from the prompt-development workflow.\n"
        + "\n".join(f"- {p}" for p in problems)
        + "\nRun the saved workflow `prompt-development` (see CLAUDE.md → Prompt Development), "
          "then commit the drafts, the updated current.md and the review records together.",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    sys.exit(main())
