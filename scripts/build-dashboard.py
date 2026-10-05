#!/usr/bin/env python3
"""Parse match logs and prompt metadata into a JSON file for the dashboard."""

import json
import os
import re
import glob
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MATCH_LOG_DIR = ROOT / "match-log"
PROMPTS_DIR = ROOT / "prompts"
STRATEGY_DIR = ROOT / "strategy"
OUTPUT_DIR = ROOT / "dashboard"


def parse_match_file(filepath):
    """Parse a single match log markdown file into structured data."""
    text = filepath.read_text()
    match = {}
    match["file"] = str(filepath.relative_to(ROOT))
    match["type"] = "practice" if "practice" in str(filepath) else "competitive"

    # Parse header
    title_m = re.search(r"^# Match (\d+): vs (.+)$", text, re.MULTILINE)
    if title_m:
        match["number"] = int(title_m.group(1))
        match["opponent"] = title_m.group(2).strip()

    # Parse result section
    score_m = re.search(r"Score:\s*(\d+)\s*-\s*(\d+)", text)
    if score_m:
        match["score_us"] = int(score_m.group(1))
        match["score_them"] = int(score_m.group(2))
        if match["score_us"] > match["score_them"]:
            match["result"] = "W"
        elif match["score_us"] < match["score_them"]:
            match["result"] = "L"
        else:
            match["result"] = "D"

    date_m = re.search(r"Date:\s*(\d{4}-\d{2}-\d{2})", text)
    if date_m:
        match["date"] = date_m.group(1)

    # Parse formation
    formation_m = re.search(r"Formation:\s*(\S+)", text)
    if formation_m:
        match["formation"] = formation_m.group(1)

    # Parse models
    models_m = re.search(
        r"Models:\s*GK\s+(.+?),\s*DEF\s+(.+?),\s*MID\s+(.+?),\s*FWD1\s+(.+?),\s*FWD2\s+(.+?)$",
        text,
        re.MULTILINE,
    )
    if models_m:
        match["models"] = {
            "gk": models_m.group(1).strip(),
            "def": models_m.group(2).strip(),
            "mid": models_m.group(3).strip(),
            "fwd1": models_m.group(4).strip(),
            "fwd2": models_m.group(5).strip(),
        }

    # Parse prompt versions
    versions_m = re.search(
        r"Prompt versions deployed:\s*GK v(\S+),\s*DEF v(\S+),\s*MID v(\S+),\s*FWD1 v(\S+),\s*FWD2 v(\S+)",
        text,
    )
    if versions_m:
        match["versions"] = {
            "gk": versions_m.group(1),
            "def": versions_m.group(2),
            "mid": versions_m.group(3),
            "fwd1": versions_m.group(4),
            "fwd2": versions_m.group(5),
        }

    # Parse per-position performance
    positions = {}
    for pos in ["GK", "DEF", "MID", "FWD1", "FWD2"]:
        perf_m = re.search(
            rf"### {pos}\s*\n- Performance:\s*(strong|adequate|weak)",
            text,
            re.IGNORECASE,
        )
        if perf_m:
            positions[pos.lower()] = perf_m.group(1).lower()
    if positions:
        match["performance"] = positions

    # Parse action items
    actions = re.findall(r"- \[[ x]\] (.+?)(?:\n|$)", text)
    if actions:
        match["action_items"] = actions

    # Parse team-level observations
    obs_section = re.search(
        r"## Team-Level Observations\s*\n(.*?)(?=\n## |\Z)", text, re.DOTALL
    )
    if obs_section:
        obs_text = obs_section.group(1).strip()
        obs_lines = [
            line.strip("- ").strip()
            for line in obs_text.split("\n")
            if line.strip() and line.strip() != "-"
        ]
        if obs_lines:
            match["observations"] = obs_lines

    return match


def get_current_prompt_info():
    """Read current.md for each position and extract version + model."""
    info = {}
    for pos in ["gk", "def", "mid", "fwd1", "fwd2"]:
        current_file = PROMPTS_DIR / pos / "current.md"
        if current_file.exists():
            text = current_file.read_text()
            version_m = re.search(r"# .+ — v(\d+)", text)
            model_m = re.search(r"Model:\s*(.+)", text)
            info[pos] = {
                "version": version_m.group(1) if version_m else "?",
                "model": model_m.group(1).strip() if model_m else "?",
            }
    return info


def get_all_versions():
    """List all version files per position."""
    versions = {}
    for pos in ["gk", "def", "mid", "fwd1", "fwd2"]:
        pos_dir = PROMPTS_DIR / pos
        if pos_dir.exists():
            v_files = sorted(pos_dir.glob("v*.md"))
            versions[pos] = [f.stem for f in v_files]
    return versions


def build_dashboard_data():
    """Build the complete dashboard JSON."""
    data = {}

    # Parse all match logs
    matches = []
    for match_type in ["practice", "competitive"]:
        match_dir = MATCH_LOG_DIR / match_type
        if match_dir.exists():
            for f in sorted(match_dir.glob("*.md")):
                if f.name == ".gitkeep":
                    continue
                parsed = parse_match_file(f)
                if parsed.get("number"):
                    matches.append(parsed)

    data["matches"] = sorted(matches, key=lambda m: m.get("number", 0))

    # Current formation from strategy/formation.md
    formation_file = STRATEGY_DIR / "formation.md"
    if formation_file.exists():
        ft = formation_file.read_text()
        fm = re.search(r"## Current Formation:\s*(\S+)", ft)
        data["current_formation"] = fm.group(1) if fm else "unknown"

    # Current deployment info
    data["current_config"] = get_current_prompt_info()

    # Version history
    data["versions"] = get_all_versions()

    # Stats
    competitive = [m for m in matches if m.get("type") == "competitive"]
    practice = [m for m in matches if m.get("type") == "practice"]
    data["stats"] = {
        "total_matches": len(matches),
        "competitive": {
            "played": len(competitive),
            "remaining": 10 - len(competitive),
            "wins": sum(1 for m in competitive if m.get("result") == "W"),
            "draws": sum(1 for m in competitive if m.get("result") == "D"),
            "losses": sum(1 for m in competitive if m.get("result") == "L"),
            "goals_for": sum(m.get("score_us", 0) for m in competitive),
            "goals_against": sum(m.get("score_them", 0) for m in competitive),
        },
        "practice": {
            "played": len(practice),
            "wins": sum(1 for m in practice if m.get("result") == "W"),
            "draws": sum(1 for m in practice if m.get("result") == "D"),
            "losses": sum(1 for m in practice if m.get("result") == "L"),
        },
    }

    # Aggregate performance per position across all matches
    perf_map = {"strong": 3, "adequate": 2, "weak": 1}
    perf_totals = {}
    for pos in ["gk", "def", "mid", "fwd1", "fwd2"]:
        ratings = [
            perf_map.get(m["performance"].get(pos, ""), 0)
            for m in matches
            if m.get("performance")
        ]
        ratings = [r for r in ratings if r > 0]
        if ratings:
            perf_totals[pos] = {
                "avg": round(sum(ratings) / len(ratings), 2),
                "matches_rated": len(ratings),
            }
    data["performance_trends"] = perf_totals

    return data


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    data = build_dashboard_data()
    output_file = OUTPUT_DIR / "data.json"
    output_file.write_text(json.dumps(data, indent=2))
    print(f"Dashboard data written to {output_file}")
    print(f"  Matches parsed: {data['stats']['total_matches']}")
    print(f"  Current config: {json.dumps(data['current_config'], indent=4)}")


if __name__ == "__main__":
    main()
