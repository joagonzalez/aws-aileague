#!/usr/bin/env python3
"""Generate deploy/paste-ready.md from prompts/<position>/current.md and lint each prompt.

Only the behavioral text is pasted into the platform (no header, model line or changelog).
Exits non-zero if a prompt is missing a required section or exceeds the platform hard limit.

Usage:
  python3 scripts/build-paste-ready.py                         # regenerate from current.md
  python3 scripts/build-paste-ready.py --check <file.md> ...   # lint drafts only, write nothing
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMPTS_DIR = ROOT / "prompts"
OUTPUT_FILE = ROOT / "deploy" / "paste-ready.md"

PLAYERS = [
    ("gk", 1, "Shannon", "GK"),
    ("def", 2, "Turing", "DEF"),
    ("mid", 3, "Tesla", "MID"),
    ("fwd1", 4, "Hertz", "FWD1"),
    ("fwd2", 5, "Lovelace", "FWD2"),
]

REQUIRED_SECTIONS = [
    "Role",
    "Decision Framework",
    "Personality / Tendencies",
    "Coordination",
    "Constraints",
    "Changelog",
]

HARD_LIMIT = 6000
FAST_MODELS = {"Claude Haiku", "Nova Micro"}
FAST_BUDGET = 2000
SMART_BUDGET = 5000

# Phrases the agent cannot act on, or vague wording banned by specs/evaluation-criteria.md.
LINT_PATTERNS = {
    r"\btry to\b": "vague wording",
    r"\bconsider\b": "vague wording",
    r"\bif possible\b": "vague wording",
    r"\bwhen needed\b": "vague wording",
    r"\btell\b": "agents cannot talk to each other",
    r"\bcall for\b": "agents cannot talk to each other",
    r"\bsignal\b": "agents cannot talk to each other",
    r"\bcommunicat": "agents cannot talk to each other",
    r"\b(\d+(-\d+)?|few|couple of)\s+seconds?\b": "agents see game state, not a clock",
    r"\bshield\b": "no platform command for this",
    r"\bwait\b": "no platform command for this",
}


def parse_prompt(text):
    header = re.search(r"^# (.+?) — v(\d+)\s*$", text, re.MULTILINE)
    model = re.search(r"^Model:\s*(.+)$", text, re.MULTILINE)
    sections = {}
    for m in re.finditer(r"^## (.+?)\s*\n(.*?)(?=^## |\Z)", text, re.MULTILINE | re.DOTALL):
        sections[m.group(1).strip()] = m.group(2).strip()
    return {
        "version": header.group(2) if header else "?",
        "model": model.group(1).strip() if model else "?",
        "sections": sections,
    }


def build_paste_text(sections):
    return "\n\n".join([
        sections["Role"],
        "Check these rules in order and do the first one that matches:\n" + sections["Decision Framework"],
        "Style:\n" + sections["Personality / Tendencies"],
        "Teammates:\n" + sections["Coordination"],
        "Hard rules:\n" + sections["Constraints"],
    ])


def lint(pos, prompt, paste_text):
    errors, warnings = [], []
    missing = [s for s in REQUIRED_SECTIONS if s not in prompt["sections"]]
    if missing:
        errors.append(f"{pos}: missing sections {missing}")
        return errors, warnings

    length = len(paste_text)
    budget = FAST_BUDGET if prompt["model"] in FAST_MODELS else SMART_BUDGET
    if length > HARD_LIMIT:
        errors.append(f"{pos}: {length} chars exceeds platform limit {HARD_LIMIT}")
    elif length > budget:
        warnings.append(f"{pos}: {length} chars exceeds {budget} budget for {prompt['model']}")

    for pattern, reason in LINT_PATTERNS.items():
        for m in re.finditer(pattern, paste_text, re.IGNORECASE):
            line = paste_text[: m.start()].count("\n") + 1
            warnings.append(f"{pos}: '{m.group(0)}' ({reason}) — pasted line {line}")
    return errors, warnings


def check_files(paths):
    """Lint specific prompt files (e.g. drafts prompts/mid/v4.md) without writing paste-ready.md."""
    failed = False
    for path in paths:
        prompt = parse_prompt(Path(path).read_text())
        paste_text = build_paste_text(prompt["sections"]) if all(s in prompt["sections"] for s in REQUIRED_SECTIONS) else ""
        errors, warnings = lint(path, prompt, paste_text)
        print(f"{path}: v{prompt['version']} {prompt['model']} — {len(paste_text)}/{HARD_LIMIT} chars")
        for e in errors:
            print(f"ERROR   {e}")
        for w in warnings:
            print(f"WARNING {w}")
        failed = failed or bool(errors)
    sys.exit(1 if failed else 0)


def main():
    if len(sys.argv) > 2 and sys.argv[1] == "--check":
        check_files(sys.argv[2:])
    all_errors, all_warnings, blocks, summary = [], [], [], []

    for pos, number, name, label in PLAYERS:
        prompt = parse_prompt((PROMPTS_DIR / pos / "current.md").read_text())
        if any(s not in prompt["sections"] for s in REQUIRED_SECTIONS):
            errors, _ = lint(pos, prompt, "")
            all_errors += errors
            continue
        paste_text = build_paste_text(prompt["sections"])
        errors, warnings = lint(pos, prompt, paste_text)
        all_errors += errors
        all_warnings += warnings
        summary.append(f"{label} v{prompt['version']}")
        blocks.append(
            f"## Player {number} — {name} ({label}) — v{prompt['version']} — {prompt['model']} — "
            f"{len(paste_text)}/{HARD_LIMIT} chars\n\n```text\n{paste_text}\n```\n"
        )

    if all_errors:
        for e in all_errors:
            print(f"ERROR   {e}")
        sys.exit(1)

    OUTPUT_FILE.write_text(
        "# Paste-Ready Prompts for AWS Platform\n\n"
        "Generated by `scripts/build-paste-ready.py` from `prompts/<position>/current.md`. "
        "Do not edit by hand; edit `current.md` and re-run the script.\n\n"
        f"Versions: {', '.join(summary)}\n\n"
        "Paste each code block into that player's prompt field, set the model shown in the heading, "
        "then click \"Redeploy changes\".\n\n"
        + "\n".join(blocks)
    )
    print(f"Wrote {OUTPUT_FILE.relative_to(ROOT)}")
    for b in blocks:
        print("  " + b.splitlines()[0].removeprefix("## "))
    for w in all_warnings:
        print(f"WARNING {w}")


if __name__ == "__main__":
    main()
