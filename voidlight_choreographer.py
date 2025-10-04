#!/usr/bin/env python3
"""
voidlight_choreographer.py — Absolutely gaudy, emoji-saturated, rainbow-vomiting snark-commit generator.

What it does (short):
 - creates N commits in an existing git repo with historical timestamps
 - tons of emojis, space-pirate & BDSM-adjacent snark, and over-the-top silliness 🏴‍☠️🪩🧪
 - colorizes terminal output in blazing rainbow ANSI colors 🌈
 - preview mode exports JSON and optional SVG (--svg-out)
 - supports date-range, weekdays-only, day/week spread, and month weights
 - ensures AuthorDate and CommitDate are within 16 hours of each other
 - tiny svg generator (no external deps) to visualize the heatmap for sharing

Use responsibly (sandbox/demo). Don't use to impersonate real work. Consent & safety vibes: "safe word" applies here too. 🔒

Examples:
  preview + JSON + SVG:
    python3 voidlight_choreographer.py -n 200 --preview-only --svg-out preview_heatmap.svg

  create commits (rainbow mode on by default):
    python3 voidlight_choreographer.py -n 120 --start-date 2024-01-01 --end-date 2024-12-31 --spread-mode week

Enjoy the chaos. 🐙🎉
"""

from __future__ import annotations

import argparse
import json
import os
import random
import subprocess
import sys
from collections import OrderedDict, defaultdict
from collections.abc import Sequence
from dataclasses import dataclass
from datetime import UTC, date, datetime, time, timedelta
from math import ceil
from pathlib import Path

from voidlight_whispers import (
    pick_snarky_blame_tag,
    pick_snarky_extra_emoji,
    pick_snarky_message,
)

# -------------------------
# CONFIG: EXTREME SNARKY MESSAGES (space-pirate + BDSM-adjacent + silly)
# -------------------------
# A big pool of silly, snarky commits - space pirate & mild BDSM flavor (consensual, non-explicit).

# -------------------------
# TEMPLATING: filenames, funcs, blame tags, extra emoji pool
# -------------------------
FILE_EXTS = [
    "py",
    "js",
    "ts",
    "go",
    "java",
    "rb",
    "sh",
    "md",
    "yaml",
    "yml",
    "json",
    "c",
    "cpp",
]
FUNC_PREFIXES = [
    "get",
    "set",
    "calc",
    "handle",
    "do",
    "fix",
    "load",
    "render",
    "update",
    "compute",
    "validate",
    "parse",
    "summon",
    "pirate",
]
# Legacy arrays kept for compatibility with templating but now sourced externally

DEFAULT_TARGET_FILE = ".generated_commits.txt"


def random_filename():
    """Return a random filename used in templated messages."""
    name = "".join(
        random.choice("abcdefghijklmnopqrstuvwxyz")
        for _ in range(random.randint(4, 10))
    )
    ext = random.choice(FILE_EXTS)
    return f"{name}.{ext}"


def random_funcname():
    """Return a random function name used in templated messages."""
    return (
        random.choice(FUNC_PREFIXES)
        + "_"
        + "".join(
            random.choice("abcdefghijklmnopqrstuvwxyz")
            for _ in range(random.randint(4, 10))
        )
    )


def random_blametag():
    """Return a random blame tag (who to blame/playfully tag)."""
    return pick_snarky_blame_tag()


def make_commit_message(idx, total, author_dt):
    """Create a templated commit message with emoji, pirate/BDSM themes, and snark."""
    core = pick_snarky_message()
    file = random_filename()
    func = random_funcname()
    blame = random_blametag()
    emoji = pick_snarky_extra_emoji()
    return f"{emoji} Test: {core} ({file}::{func}) {blame} — commit {idx}/{total} ({author_dt.date().isoformat()})"


@dataclass(slots=True)
class PlannedCommit:
    """One carefully bound commit plan with matching timestamps and sass."""

    author_dt: datetime
    committer_dt: datetime
    message: str
    chosen_day: date


# -------------------------
# GIT & FORMATTING HELPERS (small functions, brief comments)
# -------------------------
def run_git(
    cmd_args: Sequence[str],
    repo_path: Path,
    env: dict[str, str] | None = None,
    check: bool = True,
) -> subprocess.CompletedProcess[bytes]:
    """Run a git command and optionally raise on failure."""

    proc = subprocess.run(
        ["git", *cmd_args],
        cwd=repo_path,
        env=env,
        capture_output=True,
        check=False,
    )
    if check and proc.returncode != 0:
        raise subprocess.CalledProcessError(
            proc.returncode, proc.args, output=proc.stdout, stderr=proc.stderr
        )
    return proc


def iso_utc(dt: datetime) -> str:
    """Format datetime for GIT env variables (UTC)."""
    return dt.strftime("%Y-%m-%dT%H:%M:%S+0000")


def now_utc() -> datetime:
    """Summon a glitter-approved timezone-aware UTC timestamp."""

    return datetime.now(UTC)


def ensure_repo(path: Path) -> None:
    """Exit if the provided path isn't a git repo (.git missing)."""

    if not path.is_dir():
        raise SystemExit(f"Repo path '{path}' does not exist or is not a directory.")
    if not (path / ".git").is_dir():
        raise SystemExit(f"'{path}' does not look like a git repo (no .git folder).")


# -------------------------
# COLORS: massive rainbow palette & helpers
# -------------------------
RESET = "\x1b[0m"
BOLD = "\x1b[1m"
# A palette of bright background colors (rainbow vomit)
PALETTE_BG = [
    "\x1b[48;5;196m",  # red
    "\x1b[48;5;202m",  # orange
    "\x1b[48;5;226m",  # yellow
    "\x1b[48;5;118m",  # green
    "\x1b[48;5;45m",  # teal
    "\x1b[48;5;33m",  # blue
    "\x1b[48;5;99m",  # purple
    "\x1b[48;5;201m",  # magenta
]
FG_BLACK = "\x1b[30m"
FG_WHITE = "\x1b[97m"


def rainbow_block(i, use_color=True):
    """Return a colored two-character block cycling through the palette (rainbow vomit)."""
    if not use_color:
        return "██"
    return PALETTE_BG[i % len(PALETTE_BG)] + "  " + RESET


def color_for_count_index(c):
    """Map intensity c to a palette index (higher c -> hotter color)."""
    if c == 0:
        return None
    if c == 1:
        return 0
    if c == 2:
        return 2
    if 3 <= c <= 4:
        return 4
    return 6  # high intensity


def block_for_count(c, use_color=True):
    """Return a two-char block (rainbow colored or ASCII) based on count intensity."""
    idx = color_for_count_index(c)
    if idx is None:
        return "  " if not use_color else "  "
    if not use_color:
        if c == 1:
            return "░░"
        elif c == 2:
            return "▒▒"
        elif 3 <= c <= 4:
            return "▓▓"
        else:
            return "██"
    return rainbow_block(idx, use_color=use_color)


# -------------------------
# HEATMAP & SVG RENDERING (small helpers)
# -------------------------
def make_heatmap_data(counts_by_offset, total_days):
    """Convert counts keyed by day-offset (0=today) to array oldest->newest."""
    arr = [0] * total_days
    for offset, c in counts_by_offset.items():
        if 0 <= offset < total_days:
            arr[total_days - 1 - offset] = c
    return arr


def render_heatmap_terminal(arr, use_color=True):
    """Render a terminal rainbow heatmap (weeks x days)."""
    days = len(arr)
    weeks = ceil(days / 7)
    pad = weeks * 7 - days
    padded = [0] * pad + arr[:]
    grid = [[] for _ in range(7)]
    for w in range(weeks):
        for r in range(7):
            idx = w * 7 + r
            grid[r].append(padded[idx])
    weekday_names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    lines = []
    header = (
        f"{BOLD}{FG_WHITE}🌈 RAINBOW HEATMAP (older → newer, {days} days) 🌈{RESET}"
    )
    lines.append(header)
    lines.append("")
    for r, name in enumerate(weekday_names):
        line = f"{BOLD}{name}{RESET} "
        for c in grid[r]:
            line += block_for_count(c, use_color=use_color)
        lines.append(line)
    tick_row = "    "
    for w in range(weeks):
        tick_row += "‾ " if (w % 4 == 0) else "  "
    lines.append("")
    lines.append(tick_row + "  (each column ≈ 1 week) 🗓️")
    return "\n".join(lines)


def render_histogram_terminal(arr, use_color=True):
    """Render a colorful histogram of the last 30 days (terminal)."""
    bucket = arr[-30:]
    maxc = max(bucket) if bucket else 0
    lines = [f"\n{BOLD}📊 Recent 30-day histogram (← older, → newer){RESET}"]
    if maxc == 0:
        lines.append(" (no commits in last 30 days) 🚫")
        return "\n".join(lines)
    for i, c in enumerate(bucket):
        length = int((c / maxc) * 20) if maxc else 0
        bar = ""
        for j in range(length):
            bar += rainbow_block(j, use_color=use_color)
        lines.append(f"{(i - 29):3d} |{bar} ({c})")
    return "\n".join(lines)


def svg_color_for_count(c):
    """Return an SVG hex color string for intensity c (rainbow scale)."""
    if c == 0:
        return "#eeeeee"
    if c == 1:
        return "#ff4d4d"  # red-ish
    if c == 2:
        return "#ffb84d"  # orange
    if 3 <= c <= 4:
        return "#ffd24d"  # yellow
    return "#8a2be2"  # purple/violet for high


def export_svg_heatmap(arr, filename, start_date):
    """Export a simple SVG heatmap to filename (no external deps)."""
    days = len(arr)
    weeks = ceil(days / 7)
    cell = 12  # cell size px
    padding = 4
    width = weeks * cell + padding * 2
    height = 7 * cell + padding * 2 + 30
    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#0b0b0b"/>',
        f'<g transform="translate({padding},{padding})">',
    ]
    # pad left so earliest maps correctly
    pad = weeks * 7 - days
    padded = [0] * pad + arr[:]
    for w in range(weeks):
        for r in range(7):
            idx = w * 7 + r
            c = padded[idx]
            x = w * cell
            y = r * cell
            color = svg_color_for_count(c)
            svg_parts.append(
                f'<rect x="{x}" y="{y}" width="{cell - 1}" height="{cell - 1}" fill="{color}" rx="2" ry="2"/>'
            )
    # legend
    svg_parts.append("</g>")
    legend_x = padding
    legend_y = padding + 7 * cell + 6
    svg_parts.append(f'<g transform="translate({legend_x},{legend_y})">')
    svg_parts.append(
        f'<text x="0" y="12" fill="#ffffff" style="font-family:monospace;font-size:12px">🌈 Heatmap SVG — start: {start_date.isoformat()}</text>'
    )
    svg_parts.append("</g>")
    svg_parts.append("</svg>")
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(svg_parts))
    return filename


# -------------------------
# DATE & PARSING HELPERS (very brief)
# -------------------------
def parse_ymd(s: str) -> date:
    """Parse YYYY-MM-DD to date."""
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except Exception as exc:
        raise argparse.ArgumentTypeError("Dates must be YYYY-MM-DD") from exc


def daterange(start: date, end: date):
    """Yield each date from start..end inclusive."""
    for n in range((end - start).days + 1):
        yield start + timedelta(n)


def parse_month_weights(raw: str | None) -> list[float]:
    """Decode month weights, defaulting to egalitarian glitter."""

    if raw is None:
        return [1.0] * 12

    parts = [p.strip() for p in raw.split(",")]
    if len(parts) != 12:
        raise SystemExit(
            "month-weights must flaunt 12 comma-separated numbers for Jan..Dec"
        )

    try:
        weights = [float(p) for p in parts]
    except ValueError as exc:
        raise SystemExit("Could not decode month-weights into luscious floats") from exc

    if any(w < 0 for w in weights):
        raise SystemExit("month-weights must be non-negative — no gloom allowed")

    return weights


def randomized_weight(base: float) -> float:
    """Amplify a base month weight with exponential glitter."""

    return 0.0 if base <= 0 else base * random.expovariate(1.0)


def ensure_weights_have_heat(weights: Sequence[float]) -> None:
    """Explode dramatically if every weight is zero and the party dies."""

    if not any(w > 0 for w in weights):
        raise SystemExit(
            "All weights are zero — nobody invited sparkle to the dance floor"
        )


def compute_day_weights(
    days: Sequence[date], month_weights: Sequence[float]
) -> list[float]:
    """Assign each day a weight respecting month swagger."""

    weights = [randomized_weight(month_weights[d.month - 1]) for d in days]
    ensure_weights_have_heat(weights)
    return weights


def compute_week_buckets(days: Sequence[date]) -> OrderedDict:
    """Group dates into ISO weeks for high-level glitter scheduling."""

    buckets: OrderedDict[tuple[int, int], list[date]] = OrderedDict()
    for d in days:
        iso = d.isocalendar()
        buckets.setdefault((iso[0], iso[1]), []).append(d)
    return buckets


def compute_week_weights(
    week_buckets: OrderedDict, month_weights: Sequence[float]
) -> list[float]:
    """Produce week-level weights keyed off the week's starting month."""

    weights = []
    for days in week_buckets.values():
        wk_start = min(days)
        weights.append(randomized_weight(month_weights[wk_start.month - 1]))
    ensure_weights_have_heat(weights)
    return weights


def choose_with_weights(
    population: Sequence, weights: Sequence[float], total: int
) -> list:
    """Sample with replacement using the provided flamboyant weights."""

    return random.choices(population, weights=weights, k=total)


def choose_commit_days(
    total: int,
    candidate_days: Sequence[date],
    spread_mode: str,
    month_weights: Sequence[float],
) -> list[date]:
    """Select commit days according to the chosen glitter pattern."""

    if spread_mode == "day":
        weights = compute_day_weights(candidate_days, month_weights)
        return choose_with_weights(candidate_days, weights, total)

    week_buckets = compute_week_buckets(candidate_days)
    if not week_buckets:
        raise SystemExit("No ISO weeks found — the calendar collapsed into a wormhole")

    week_weights = compute_week_weights(week_buckets, month_weights)
    week_keys = list(week_buckets.keys())
    chosen_weeks = choose_with_weights(week_keys, week_weights, total)
    return [random.choice(week_buckets[wk]) for wk in chosen_weeks]


def clamp_datetime(value: datetime, low: datetime, high: datetime) -> datetime:
    """Clamp timestamps into the consensual window."""

    if value < low:
        return low
    if value > high:
        return high
    return value


def random_author_datetime(chosen_day: date) -> datetime:
    """Return a sunrise-to-nightfall author timestamp."""

    start = datetime.combine(chosen_day, time(hour=6, minute=0, second=0))
    return start + timedelta(seconds=random.randint(0, 16 * 3600 - 1))


def random_committer_datetime(
    author_dt: datetime,
    clamp_low: datetime,
    clamp_high: datetime,
    *,
    weekdays_only: bool,
    max_attempts: int,
) -> datetime:
    """Jiggle the committer timestamp within ±8h, respecting boundaries."""

    author_low = clamp_datetime(author_dt - timedelta(hours=8), clamp_low, clamp_high)
    author_high = clamp_datetime(author_dt + timedelta(hours=8), clamp_low, clamp_high)

    for _ in range(max_attempts):
        offset_hours = random.uniform(-8, 8)
        candidate = author_dt + timedelta(seconds=int(offset_hours * 3600))
        candidate = clamp_datetime(candidate, clamp_low, clamp_high)
        candidate = clamp_datetime(candidate, author_low, author_high)
        if weekdays_only and candidate.weekday() >= 5:
            continue
        return candidate

    return clamp_datetime(author_dt, clamp_low, clamp_high)


def assemble_planned_commits(
    chosen_days: Sequence[date],
    *,
    weekdays_only: bool,
    max_attempts_offset: int,
    start_date: date,
    end_date: date,
) -> list[PlannedCommit]:
    """Transform chosen days into fully-dressed PlannedCommit entries."""

    total = len(chosen_days)
    global_low = datetime.combine(start_date, time.min)
    global_high = datetime.combine(end_date, time.max)
    planned: list[PlannedCommit] = []

    for idx, chosen_day in enumerate(chosen_days, start=1):
        author_dt = random_author_datetime(chosen_day)
        day_low = max(global_low, datetime.combine(chosen_day, time.min))
        day_high = min(global_high, datetime.combine(chosen_day, time.max))
        committer_dt = random_committer_datetime(
            author_dt,
            day_low,
            day_high,
            weekdays_only=weekdays_only,
            max_attempts=max_attempts_offset,
        )
        planned.append(
            PlannedCommit(
                author_dt=author_dt,
                committer_dt=committer_dt,
                message=make_commit_message(idx, total, author_dt),
                chosen_day=chosen_day,
            )
        )

    return planned


# -------------------------
# MAIN: arg parsing, planning, preview, commit creation
# -------------------------
def main() -> None:
    """Plan, preview, and optionally create a tidal wave of glitter commits."""

    parser = argparse.ArgumentParser(
        description="Generate gaudy, emoji'd commits with rainbow output."
    )
    parser.add_argument(
        "-n",
        "--num",
        type=int,
        required=True,
        help="Total number of commits to create",
    )
    parser.add_argument(
        "--repo",
        default=".",
        help="Path to existing git repo (default: current directory)",
    )
    parser.add_argument(
        "--file",
        default=DEFAULT_TARGET_FILE,
        help="File to append to for commits",
    )
    parser.add_argument("--seed", type=int, default=None, help="Random seed (optional)")
    parser.add_argument(
        "--start-days-ago",
        type=int,
        default=365,
        help="Fallback range if start/end not provided",
    )
    parser.add_argument(
        "--start-date", type=parse_ymd, help="Start date YYYY-MM-DD (inclusive)"
    )
    parser.add_argument(
        "--end-date", type=parse_ymd, help="End date YYYY-MM-DD (inclusive)"
    )
    parser.add_argument(
        "--weekdays-only",
        action="store_true",
        help="Only plan commits on weekdays (Mon-Fri)",
    )
    parser.add_argument(
        "--preview-only",
        action="store_true",
        help="Show preview and do NOT create commits (exports JSON and optional SVG)",
    )
    parser.add_argument(
        "--spread-mode",
        choices=["day", "week"],
        default="day",
        help="Spread by individual days or by week buckets",
    )
    parser.add_argument(
        "--month-weights",
        type=str,
        help="12 comma-separated month weights Jan..Dec (e.g. '1,2,1,...'). Defaults to equal weights.",
    )
    parser.add_argument(
        "--color",
        dest="use_color",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Toggle the retina-searing rainbow output",
    )
    parser.add_argument(
        "--svg-out",
        type=str,
        help="If provided during preview, save an SVG heatmap to this path",
    )
    parser.add_argument(
        "--max-attempts-offset",
        type=int,
        default=20,
        help="Attempts to get committer offset satisfying constraints",
    )
    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    repo = Path(args.repo).expanduser().resolve()
    ensure_repo(repo)
    target_file_rel = args.file
    target_file = repo / target_file_rel

    total = args.num
    if total <= 0:
        raise SystemExit("Number of commits must be positive.")

    today = now_utc().date()

    if args.start_date and args.end_date:
        start_date = args.start_date
        end_date = args.end_date
        if start_date > end_date:
            raise SystemExit("start-date must be <= end-date")
    elif args.start_date and not args.end_date:
        start_date = args.start_date
        end_date = today
        if start_date > end_date:
            raise SystemExit("start-date must be <= today")
    elif not args.start_date and args.end_date:
        end_date = args.end_date
        start_date = end_date - timedelta(days=args.start_days_ago)
    else:
        end_date = today
        start_date = today - timedelta(days=args.start_days_ago)

    total_days = (end_date - start_date).days + 1
    if total_days < 1:
        raise SystemExit("Date range must include at least one day.")

    all_candidate_days = list(daterange(start_date, end_date))
    if args.weekdays_only:
        all_candidate_days = [d for d in all_candidate_days if d.weekday() < 5]
    if not all_candidate_days:
        raise SystemExit(
            "No candidate days available after applying filters (weekdays-only?)"
        )

    month_weights = parse_month_weights(args.month_weights)
    chosen_days = choose_commit_days(
        total, all_candidate_days, args.spread_mode, month_weights
    )
    planned_commits = assemble_planned_commits(
        chosen_days,
        weekdays_only=args.weekdays_only,
        max_attempts_offset=args.max_attempts_offset,
        start_date=start_date,
        end_date=end_date,
    )

    counts_by_offset = defaultdict(int)
    for commit in planned_commits:
        offset = (today - commit.chosen_day).days
        counts_by_offset[offset] += 1
    heatmap_arr = make_heatmap_data(counts_by_offset, total_days)

    heatmap_terminal = render_heatmap_terminal(heatmap_arr, use_color=args.use_color)
    hist_terminal = render_histogram_terminal(heatmap_arr, use_color=args.use_color)

    print("\n" + "=" * 80)
    print(f"{BOLD}{FG_WHITE}🧭 OVER-THE-TOP PLANNED COMMITS PREVIEW 🧭{RESET}")
    print("=" * 80 + "\n")
    print(f"{BOLD}📁 Repo:{RESET} {repo}")
    print(f"{BOLD}📝 Target file:{RESET} {target_file_rel}")
    print(f"{BOLD}🔢 Planned commits:{RESET} {total}")
    print(
        f"{BOLD}📅 Range:{RESET} {start_date.isoformat()} → {end_date.isoformat()} ({total_days} days)"
    )
    weekday_flag = "ON" if args.weekdays_only else "OFF"
    print(
        f"{BOLD}🌈 Mode:{RESET} {args.spread_mode}    {BOLD}Weekdays-only:{RESET} {weekday_flag}"
    )
    print(f"{BOLD}🎲 Seed:{RESET} {args.seed}")
    print("\n" + heatmap_terminal + "\n")
    print(hist_terminal)
    print("\nSample planned commits (first 20):\n")
    for i, commit in enumerate(planned_commits[:20], start=1):
        ad = commit.author_dt.strftime("%Y-%m-%d %H:%M:%S UTC")
        cd = commit.committer_dt.strftime("%Y-%m-%d %H:%M:%S UTC")
        diff_hours = (
            abs((commit.committer_dt - commit.author_dt).total_seconds()) / 3600.0
        )
        color_idx = i % len(PALETTE_BG)
        prefix = PALETTE_BG[color_idx] + FG_BLACK + " " + RESET
        print(
            f"{prefix} {BOLD}{i:3d}{RESET}. {commit.chosen_day.isoformat()} | Author: {ad} | Committer: {cd} | Δ {diff_hours:.2f}h"
        )
        print(f"     → {commit.message}")

    print("\nTotals by day-offset (days ago : commits):")
    for offset in sorted(counts_by_offset.keys()):
        print(f"  {offset:3d} days ago : {counts_by_offset[offset]} commits")

    if args.preview_only:
        timestamp = now_utc().strftime("%Y%m%dT%H%M%SZ")
        preview_filename = repo / f"planned_commits_preview_{timestamp}.json"
        json_list = [
            {
                "author_date_iso": commit.author_dt.strftime("%Y-%m-%dT%H:%M:%S+00:00"),
                "committer_date_iso": commit.committer_dt.strftime(
                    "%Y-%m-%dT%H:%M:%S+00:00"
                ),
                "chosen_day": commit.chosen_day.isoformat(),
                "message": commit.message,
            }
            for commit in planned_commits
        ]
        with preview_filename.open("w", encoding="utf-8") as jf:
            json.dump(
                {
                    "repo": str(repo),
                    "target_file": target_file_rel,
                    "generated_at_utc": now_utc().isoformat().replace("+00:00", "Z"),
                    "commits_count": len(json_list),
                    "commits": json_list,
                },
                jf,
                indent=2,
                ensure_ascii=False,
            )
        print(f"\n💾 Preview JSON exported to: {preview_filename} ✅")
        if args.svg_out:
            svg_target = Path(args.svg_out).expanduser()
            svg_path = svg_target if svg_target.is_absolute() else repo / svg_target
            try:
                export_svg_heatmap(heatmap_arr, svg_path, start_date)
                print(f"🖼️ SVG heatmap exported to: {svg_path} ✅")
            except Exception as exc:
                print(f"❌ Failed to export SVG: {exc}")
        print("\n--preview-only set: stopping before creating commits. 🚫")
        return

    if not target_file.exists():
        with target_file.open("w", encoding="utf-8") as handle:
            handle.write("# generated commit log — rainbow edition 🌈\n")

    print("\n🔨 Creating commits now... (prepare to be dazzled) 🔨")
    sys.stdout.flush()

    for i, commit in enumerate(planned_commits, start=1):
        author_iso = iso_utc(commit.author_dt)
        committer_iso = iso_utc(commit.committer_dt)

        with target_file.open("a", encoding="utf-8") as handle:
            handle.write(f"{author_iso}  - {commit.message}\n")

        try:
            run_git(["add", target_file_rel], repo)
        except subprocess.CalledProcessError as exc:
            print("git add failed:", exc.stderr.decode().strip())
            raise SystemExit(1) from exc

        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = author_iso
        env["GIT_COMMITTER_DATE"] = committer_iso

        try:
            run_git(["commit", "-m", commit.message], repo, env=env)
        except subprocess.CalledProcessError as exc:
            stderr = exc.stderr.decode().strip()
            if "nothing to commit" in stderr.lower():
                try:
                    run_git(
                        ["commit", "--allow-empty", "-m", commit.message], repo, env=env
                    )
                except subprocess.CalledProcessError as secondary:
                    print(
                        "Commit failed even with --allow-empty:",
                        secondary.stderr.decode().strip(),
                    )
                    raise SystemExit(1) from exc
            else:
                print("git commit failed:", stderr)
                raise SystemExit(1) from exc

        if i % 25 == 0 or i == total:
            print(f"  -> created {i}/{total} commits (latest author date {author_iso})")
            sys.stdout.flush()

    print("\n✅ Done. If you want these upstream: git push origin <branch>")
    print(
        "⚠️ Reminder: this creates historical commits — don't misrepresent real work. Use for demos/sandbox only. 🧪"
    )
    print("🏴‍☠️ Party on, pirate coder. Stay consensual, stay silly. 🌈")


if __name__ == "__main__":
    main()
