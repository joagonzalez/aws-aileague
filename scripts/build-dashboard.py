#!/usr/bin/env python3
"""Parse match logs and prompt metadata into a JSON file for the dashboard."""

import importlib.util
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
POSITIONS = ["gk", "def", "mid", "fwd1", "fwd2"]

# Reuse the paste-ready generator so "chars" means exactly what gets pasted into the platform.
_spec = importlib.util.spec_from_file_location("paste_ready", ROOT / "scripts" / "build-paste-ready.py")
paste_ready = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(paste_ready)


def prompt_stats(pos, version):
    """Size and complexity of prompts/<pos>/v<version>.md as it would be pasted."""
    f = PROMPTS_DIR / pos / f"v{version}.md"
    if not f.exists():
        return None
    prompt = paste_ready.parse_prompt(f.read_text())
    if any(s not in prompt["sections"] for s in paste_ready.REQUIRED_SECTIONS):
        return None
    text = paste_ready.build_paste_text(prompt["sections"])
    return {
        "version": str(version),
        "chars": len(text),
        "words": len(text.split()),
        "rules": len(re.findall(r"^\d+\.", prompt["sections"]["Decision Framework"], re.MULTILINE)),
        "constraints": len(re.findall(r"^- ", prompt["sections"]["Constraints"], re.MULTILINE)),
    }


def get_section(text, heading):
    """Return the body of a '## <heading>' section (heading matched as a prefix)."""
    m = re.search(rf"^## {re.escape(heading)}[^\n]*\n(.*?)(?=^## |\Z)", text, re.MULTILINE | re.DOTALL)
    return m.group(1) if m else ""


def parse_table(section):
    """Parse the first markdown table in a section into a list of {header_lower: cell} dicts."""
    rows = [line.strip() for line in section.splitlines() if line.strip().startswith("|")]
    if len(rows) < 2:
        return []
    split = lambda line: [c.strip() for c in line.strip("|").split("|")]
    headers = [h.lower() for h in split(rows[0])]
    return [dict(zip(headers, split(r))) for r in rows[2:]]


def to_number(cell):
    """'682ms' -> 682, '100%' -> 100, '' or placeholder -> None."""
    m = re.fullmatch(r"\s*(\d+(?:\.\d+)?)\s*(ms|%)?\s*", cell or "")
    if not m:
        return None
    value = float(m.group(1))
    return int(value) if value.is_integer() else value


def ratio(numerator, denominator, scale=100):
    if numerator is None or not denominator:
        return None
    return round(numerator / denominator * scale, 1)


def parse_metrics(text):
    """Parse Raw Stats, Command Breakdown and Agent Latency sections into numbers."""
    metrics = {}
    raw = get_section(text, "Raw Stats")
    pairs = {
        "possession": r"^- Possession:\s*(\d+)%\s*vs\s*(\d+)%",
        "shots": r"^- Shots:\s*(\d+)\s*vs\s*(\d+)",
        "on_target": r"^- Shots on target:\s*(\d+)\s*vs\s*(\d+)",
    }
    for key, pattern in pairs.items():
        m = re.search(pattern, raw, re.MULTILINE)
        if m:
            metrics[f"{key}_us"] = int(m.group(1))
            metrics[f"{key}_them"] = int(m.group(2))
    for side, label in (("us", "Our"), ("them", "Their")):
        m = re.search(rf"^- {label} commands:\s*(\d+) total(.*)$", raw, re.MULTILINE)
        if m:
            metrics[f"commands_{side}"] = int(m.group(1))
            avg = re.search(r"(\d+)ms avg", m.group(2))
            p95 = re.search(r"(\d+)ms p95", m.group(2))
            if avg:
                metrics[f"latency_avg_{side}"] = int(avg.group(1))
            if p95:
                metrics[f"latency_p95_{side}"] = int(p95.group(1))

    commands = {}
    for row in parse_table(get_section(text, "Command Breakdown")):
        count = to_number(row.get("count"))
        if row.get("command") and count is not None:
            commands[row["command"].lower().replace(" ", "_")] = count
    if commands:
        metrics["commands"] = commands

    agents = {}
    for row in parse_table(get_section(text, "Agent Latency")):
        pos = (row.get("position") or "").split(" ")[0].lower()
        if pos not in POSITIONS:
            continue
        agent = {}
        for header, cell in row.items():
            if "p95" in header:
                agent["latency_p95"] = to_number(cell)
            elif "latency" in header:
                agent["latency_avg"] = to_number(cell)
            elif "success" in header:
                agent["success"] = to_number(cell)
        agents[pos] = agent
    if agents:
        metrics["agents"] = agents
        successes = [a["success"] for a in agents.values() if a.get("success") is not None]
        if successes:
            metrics["success_avg"] = round(sum(successes) / len(successes), 1)

    # Derived metrics
    if "latency_avg_us" in metrics and "latency_avg_them" in metrics:
        metrics["latency_gap"] = metrics["latency_avg_us"] - metrics["latency_avg_them"]
    metrics["shot_accuracy"] = ratio(metrics.get("on_target_us"), metrics.get("shots_us"))
    metrics["shoot_cmd_to_shot"] = ratio(metrics.get("shots_us"), commands.get("shoot"))
    total = metrics.get("commands_us") or sum(commands.values())
    for cmd in ("press", "intercept", "mark", "pass", "shoot"):
        metrics[f"{cmd}_share"] = ratio(commands.get(cmd), total)
    return {k: v for k, v in metrics.items() if v is not None}


def parse_coach_interventions(text):
    interventions = []
    for row in parse_table(get_section(text, "Coach Interventions")):
        when = row.get("when", "")
        message = next((v for k, v in row.items() if k.startswith("message")), "")
        effect = next((v for k, v in row.items() if "effect" in k), "")
        if not message or when.startswith("[") or message.lower() == "none":
            continue
        interventions.append({"when": when, "message": message, "effect": effect})
    return interventions


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

    strategy_m = re.search(r"^- Strategy:\s*([^\[\n]+?)\s*$", text, re.MULTILINE)
    if strategy_m:
        match["strategy"] = strategy_m.group(1)

    tag_m = re.search(r"^- Deploy tag:\s*([^\[\s]\S*)", text, re.MULTILINE)
    if tag_m:
        match["deploy_tag"] = tag_m.group(1)

    metrics = parse_metrics(text)
    if metrics:
        match["metrics"] = metrics

    match["coach_interventions"] = parse_coach_interventions(text)

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

    # Prompt size/complexity of the versions deployed in this match
    if match.get("versions"):
        stats = {pos: prompt_stats(pos, v) for pos, v in match["versions"].items()}
        stats = {pos: s for pos, s in stats.items() if s}
        if stats:
            match["prompt_stats"] = stats
            chars = [s["chars"] for s in stats.values()]
            rules = [s["rules"] for s in stats.values()]
            match.setdefault("metrics", {})
            match["metrics"]["prompt_chars_avg"] = round(sum(chars) / len(chars))
            match["metrics"]["prompt_chars_max"] = max(chars)
            match["metrics"]["prompt_rules_avg"] = round(sum(rules) / len(rules), 1)

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
    """What each player runs on the platform (deploy/platform-state.json), with version + model."""
    info = {}
    state = paste_ready.platform_state()
    for pos in ["gk", "def", "mid", "fwd1", "fwd2"]:
        slot = state[pos]
        if slot["path"].exists():
            text = slot["path"].read_text()
            version_m = re.search(r"# .+ — v(\d+)", text)
            model_m = re.search(r"Model:\s*(.+)", text)
            info[pos] = {
                "version": version_m.group(1) if version_m else "?",
                "model": slot["model"] or (model_m.group(1).strip() if model_m else "?"),
                "source": slot["path"].relative_to(ROOT).as_posix(),
            }
    return info


def version_key(f):
    return int(re.sub(r"\D", "", f.stem) or 0)


def get_all_versions():
    """List all version files per position."""
    versions = {}
    for pos in ["gk", "def", "mid", "fwd1", "fwd2"]:
        pos_dir = PROMPTS_DIR / pos
        if pos_dir.exists():
            v_files = sorted(pos_dir.glob("v*.md"), key=version_key)
            versions[pos] = [f.stem for f in v_files]
    return versions


def get_version_stats():
    """Prompt size/complexity for every version file, per position."""
    out = {}
    for pos, stems in get_all_versions().items():
        out[pos] = {stem: prompt_stats(pos, stem[1:]) for stem in stems}
    return out


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
    data["version_stats"] = get_version_stats()

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
