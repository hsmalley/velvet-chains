#!/usr/bin/env python3
"""
generate_commits.py — Absolutely gaudy, emoji-saturated, rainbow-vomiting snark-commit generator.

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
    python3 generate_commits.py -n 200 --preview-only --svg-out preview_heatmap.svg

  create commits (rainbow mode on by default):
    python3 generate_commits.py -n 120 --start-date 2024-01-01 --end-date 2024-12-31 --spread-mode week

Enjoy the chaos. 🐙🎉
"""
from __future__ import annotations
import argparse
import os
import random
import subprocess
import sys
import json
from datetime import datetime, timedelta, date
from collections import defaultdict, OrderedDict
from math import ceil

# -------------------------
# CONFIG: EXTREME SNARKY MESSAGES (space-pirate + BDSM-adjacent + silly)
# -------------------------
# A big pool of silly, snarky commits - space pirate & mild BDSM flavor (consensual, non-explicit).
SNARKY_CORE = [
    "Shaved the starboard deck; it still smells of cache. 🏴‍☠️✨",
    "Tied the feature down with polite rope (consensual). 🪢😉",
    "Executed a daring boarding action against flaky tests. ⚓️🐛",
    "Adjusted the whip of CI; it purred. 🐈‍⬛🔧",
    "Plundered logs for treasure; found only warnings. 💰📜",
    "Set sail on the seas of tech debt; lowered the sarcasm flag. ⛵️🧭",
    "Gave the bug a safe word and a stern talking-to. 🗣️🔒",
    "Installed a tiny anchor to stop the regression drift. ⚓️",
    "Reprimanded the function with a glittery paddle. 🎀🪵",
    "Space pirate handshake: 'it compiles'. 🖖🚀",
    "Added a velvet rope around the hotpath. 🧵🚫",
    "Swabbed the test deck; found smug lints. 🧹🧼",
    "Broke the moon with optimism then bandaged it. 🌝💥🩹",
    "Adjusted the throttle, yelled 'YO HO' at the compiler. 🎺🛠️",
    "Rewrote in pirate-speak; tests mutinied. ☠️📜",
    "Bound by consent: this is a temporary hack. 🤝🩶",
    "Applied charm: replaced panic with wink emojis. 😉🔥",
    "Raised the black flag of 'works on my machine'. 🏴‍☠️🖥️",
    "Gave the exception a spanking; it behaved. 🍑💥",
    "Smuggled unit tests into the brig; they told tales. 🧭📚",
    "Calibrated the cat-o'-nine-logs. 🐱‍👤📈",
    "Refitted the code hull with duct-tape couture. 🎩🩹",
    "Issued a parley with the linter; offered biscuits. 🍪🤝",
    "Hung a 'Do Not Touch' sign in a loving tone. 🪧❤️",
    "Swapped the captain's hat for a debugger. 🧢🔍",
    "Swapped curses for comments — slightly better. ✨💬",
    "Added a 'safe word' check before risky ops. 🔐🗝️",
    "Reprimanded the race condition with a stern log. 🏁🗣️",
    "Gifted the function a collar of tests. 🐾✅",
    "Pinned dependency, whispered promises to CI. 🤫🔁",
    "Moved the bomb to a quieter room (temporarily). 💣➡️🛌",
    "Applied consent-driven refactor: everyone agreed. 👍🛠️",
    "Added ceremonial trumpet before critical code. 🎺👑",
    "Renamed things for dramatic effect. 🎭📛",
    "Took the code on a romantic date; it responded with bugs. 💌🐞",
    "Hidden feature: space-parrot mode. 🦜🚀",
    "Optimized for swagger, not correctness. 😎⚙️",
    "Ate an edge-case for breakfast. 🥣🪓",
    "Sewn leather and README into a glorious patch. 🪡📘",
    "Made the tests slightly scandalous and more reliable. 😏✅",
    "Declared feature 'emotionally compatible'. 💞🔧",
    "Swapped the bug for a charming bug with manners. 🎩🐛",
    "Made a dramatic sacrifice to the test suite. 🕯️📉",
    "Pinned hopes to a single unit test. 🧷🎯",
    "Refactored with pirate grace. Arr! 🏴‍☠️🧭",
    "Tied loose ends together with glitter. ✨🔗",
    "Added a submissive fallback function called 'please'. 🙇‍♂️🔁",
    "Placed a tiny flag: 'here there be hacks'. 🚩🧰",
    "Rearranged deck chairs, discovered a race condition. 🪑🏃",
    "Temporarily disciplined the callback. 📏🔁",
    "Made the function blush and return politely. 😊↩️",
    "Gave the module a stern bedtime story. 📖🌙",
    "Added a private lounge for deprecated APIs. 🛋️🚪",
    "Smoothed rough edges with pirate polish. 🪞🏴",
    "Added playful chains of green tests. ⛓️✅",
    "Tightened the harness on the critical path. 🦺⚙️",
    "Blessed by space-coffee; compilation accepted. ☕️🛸",
    "Implemented a consensual handoff to staging. 🤝📦",
    "Added a 'no surprises' clause to the function. 📜✒️",
    "Bribed the scheduler with cookies. 🍪🕰️",
    "Raised the colors and suppressed the screaming. 🏳️‍🌈🔕",
    "Installed a portcullis around the API. 🏰🔐",
    "Made a new friend: an assert with manners. 🎩🧾",
    "Applied gentle coercion to flaky tests. 🫶🔁",
    "Built a hammock for background workers. 🏖️🧵",
    "Hooked the function into the brig for questioning. 🪝❓",
    "Patted the bug gently and sent it to QA. 🐞📤",
    "Ordered a treasure map for debugging steps. 🗺️🧭",
    "Swapped error smoke for festive confetti. 🎉💨",
    "Renamed secrets to 'mysterious variables'. 🕵️‍♀️🔐",
    "Made code sing sea shanties on build. 🎶🏗️",
    "Added dramatic monologue to the README. 🎭📘",
    "Gave the CI a beret; now it feels cultured. 🧢⚙️",
    "Bound by mutual consent: this is a feature. 🤝🌟",
]

# -------------------------
# TEMPLATING: filenames, funcs, blame tags, extra emoji pool
# -------------------------
FILE_EXTS = ['py', 'js', 'ts', 'go', 'java', 'rb', 'sh', 'md', 'yaml', 'yml', 'json', 'c', 'cpp']
FUNC_PREFIXES = ['get', 'set', 'calc', 'handle', 'do', 'fix', 'load', 'render', 'update', 'compute', 'validate', 'parse', 'summon', 'pirate']
BLAME_TAGS = ['@legacy', '@backend', '@frontend', '@ops', '@infra', '@ghost', '@intern', '@QA', '@deploy', '@unknown', '@gremlin', '@capn']

EXTRA_EMOJI = ["🧪","🛠️","🐛","🤡","🔥","🐹","🪠","🔧","🏴‍☠️","🍑","🪢","💫","🌈","✨","🎭","🎺","☕️","🍪","🕯️"]

def random_filename():
    """Return a random filename used in templated messages."""
    name = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(random.randint(4, 10)))
    ext = random.choice(FILE_EXTS)
    return f"{name}.{ext}"

def random_funcname():
    """Return a random function name used in templated messages."""
    return random.choice(FUNC_PREFIXES) + '_' + ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(random.randint(4, 10)))

def random_blametag():
    """Return a random blame tag (who to blame/playfully tag)."""
    return random.choice(BLAME_TAGS)

def make_commit_message(idx, total, author_dt):
    """Create a templated commit message with emoji, pirate/BDSM themes, and snark."""
    core = random.choice(SNARKY_CORE)
    file = random_filename()
    func = random_funcname()
    blame = random_blametag()
    emoji = random.choice(EXTRA_EMOJI)
    return f"{emoji} Test: {core} ({file}::{func}) {blame} — commit {idx}/{total} ({author_dt.date().isoformat()})"

# -------------------------
# GIT & FORMATTING HELPERS (small functions, brief comments)
# -------------------------
def run_git(cmd_args, repo_path, env=None, check=True):
    """Run a git command and optionally raise on failure."""
    proc = subprocess.run(["git"] + cmd_args, cwd=repo_path, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if check and proc.returncode != 0:
        raise subprocess.CalledProcessError(proc.returncode, proc.args, output=proc.stdout, stderr=proc.stderr)
    return proc

def iso_utc(dt: datetime) -> str:
    """Format datetime for GIT env variables (UTC)."""
    return dt.strftime("%Y-%m-%dT%H:%M:%S+0000")

def ensure_repo(path: str):
    """Exit if the provided path isn't a git repo (.git missing)."""
    if not os.path.isdir(path):
        raise SystemExit(f"Repo path {path!r} does not exist or is not a directory.")
    git_dir = os.path.join(path, ".git")
    if not os.path.isdir(git_dir):
        raise SystemExit(f"{path!r} does not look like a git repo (no .git folder).")

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
    "\x1b[48;5;45m",   # teal
    "\x1b[48;5;33m",   # blue
    "\x1b[48;5;99m",   # purple
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
    weekday_names = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    lines = []
    header = f"{BOLD}{FG_WHITE}🌈 RAINBOW HEATMAP (older → newer, {days} days) 🌈{RESET}"
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
        lines.append(f"{(i-29):3d} |{bar} ({c})")
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
    return "#8a2be2"     # purple/violet for high

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
        f'<rect width="100%" height="100%" fill="#0b0b0b"/>',
        f'<g transform="translate({padding},{padding})">'
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
            svg_parts.append(f'<rect x="{x}" y="{y}" width="{cell-1}" height="{cell-1}" fill="{color}" rx="2" ry="2"/>')
    # legend
    svg_parts.append('</g>')
    legend_x = padding
    legend_y = padding + 7 * cell + 6
    svg_parts.append(f'<g transform="translate({legend_x},{legend_y})">')
    svg_parts.append(f'<text x="0" y="12" fill="#ffffff" style="font-family:monospace;font-size:12px">🌈 Heatmap SVG — start: {start_date.isoformat()}</text>')
    svg_parts.append('</g>')
    svg_parts.append('</svg>')
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
    except Exception:
        raise argparse.ArgumentTypeError("Dates must be YYYY-MM-DD")

def daterange(start: date, end: date):
    """Yield each date from start..end inclusive."""
    for n in range((end - start).days + 1):
        yield start + timedelta(n)

# -------------------------
# MAIN: arg parsing, planning, preview, commit creation
# -------------------------
def main():
    """Main entry: plan commits, preview (JSON + optional SVG), and optionally create commits."""
    parser = argparse.ArgumentParser(description="Generate gaudy, emoji'd commits with rainbow output.")
    parser.add_argument("-n", "--num", type=int, required=True, help="Total number of commits to create")
    parser.add_argument("--repo", default=".", help="Path to existing git repo (default: current directory)")
    parser.add_argument("--file", default=".generated_commits.txt", help="File to append to for commits")
    parser.add_argument("--seed", type=int, default=None, help="Random seed (optional)")
    parser.add_argument("--start-days-ago", type=int, default=365, help="Fallback range if start/end not provided")
    parser.add_argument("--start-date", type=parse_ymd, help="Start date YYYY-MM-DD (inclusive)")
    parser.add_argument("--end-date", type=parse_ymd, help="End date YYYY-MM-DD (inclusive)")
    parser.add_argument("--weekdays-only", action="store_true", help="Only plan commits on weekdays (Mon-Fri)")
    parser.add_argument("--preview-only", action="store_true", help="Show preview and do NOT create commits (exports JSON and optional SVG)")
    parser.add_argument("--spread-mode", choices=["day", "week"], default="day", help="Spread by individual days or by week buckets")
    parser.add_argument("--month-weights", type=str, help="12 comma-separated month weights Jan..Dec (e.g. '1,2,1,...'). Defaults to equal weights.")
    parser.add_argument("--color/--no-color", dest="use_color", default=True, help="Enable/disable colored rainbow output")
    parser.add_argument("--svg-out", type=str, help="If provided during preview, save an SVG heatmap to this path")
    parser.add_argument("--max-attempts-offset", type=int, default=20, help="Attempts to get committer offset satisfying constraints")
    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    repo = os.path.abspath(args.repo)
    ensure_repo(repo)
    target_file_rel = args.file
    target_file = os.path.join(repo, target_file_rel)

    total = args.num
    if total <= 0:
        raise SystemExit("Number of commits must be positive.")

    # determine date window
    today = datetime.utcnow().date()
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

    # build candidate days
    all_candidate_days = [d for d in daterange(start_date, end_date)]
    if args.weekdays_only:
        all_candidate_days = [d for d in all_candidate_days if d.weekday() < 5]
    if not all_candidate_days:
        raise SystemExit("No candidate days available after applying filters (weekdays-only?)")

    # parse month weights
    if args.month_weights:
        parts = [p.strip() for p in args.month_weights.split(",")]
        if len(parts) != 12:
            raise SystemExit("month-weights must have 12 comma-separated numbers for Jan..Dec")
        try:
            month_weights = [float(p) for p in parts]
            if any(w < 0 for w in month_weights):
                raise SystemExit("month-weights must be non-negative numbers")
        except Exception:
            raise SystemExit("Could not parse month-weights numbers")
    else:
        month_weights = [1.0] * 12

    # Choose days according to spread mode
    planned_commits = []
    if args.spread_mode == "day":
        day_list = all_candidate_days[:]
        weights = [random.expovariate(1.0) for _ in day_list]
        def pick_day():
            r = random.random() * sum(weights)
            cum = 0.0
            for i, w in enumerate(weights):
                cum += w
                if r <= cum:
                    return day_list[i]
            return day_list[-1]
        chosen_days = [pick_day() for _ in range(total)]
    else:
        weeks = OrderedDict()
        for d in all_candidate_days:
            iso = d.isocalendar()
            key = (iso[0], iso[1])
            weeks.setdefault(key, []).append(d)
        week_keys = list(weeks.keys())
        if not week_keys:
            raise SystemExit("No weeks available in the date range")
        week_weights = []
        for key in week_keys:
            days_in_week = weeks[key]
            wk_start = min(days_in_week)
            month_idx = wk_start.month - 1
            base = month_weights[month_idx]
            w = base * random.expovariate(1.0)
            week_weights.append(w)
        def pick_week():
            r = random.random() * sum(week_weights)
            cum = 0.0
            for i, w in enumerate(week_weights):
                cum += w
                if r <= cum:
                    return week_keys[i]
            return week_keys[-1]
        chosen_weeks = [pick_week() for _ in range(total)]
        chosen_days = [random.choice(weeks[wk]) for wk in chosen_weeks]

    # For each chosen day pick author & committer datetimes within 16h
    for idx, chosen_day in enumerate(chosen_days, start=1):
        author_base = datetime(chosen_day.year, chosen_day.month, chosen_day.day, 6, 0, 0)
        seconds_window = 16 * 3600 - 1
        rand_sec = random.randint(0, seconds_window)
        author_dt = author_base + timedelta(seconds=rand_sec)

        attempts = 0
        committer_dt = author_dt
        while attempts < args.max_attempts_offset:
            offset_hours = random.uniform(-8, 8)
            candidate = author_dt + timedelta(seconds=int(offset_hours * 3600))
            if args.weekdays_only:
                if candidate.weekday() < 5 and author_dt.weekday() < 5:
                    committer_dt = candidate
                    break
            else:
                committer_dt = candidate
                break
            attempts += 1
        else:
            committer_dt = author_dt

        diff = abs((committer_dt - author_dt).total_seconds())
        if diff > 16 * 3600:
            sign = 1 if (committer_dt > author_dt) else -1
            committer_dt = author_dt + timedelta(seconds=sign * 8 * 3600)

        msg = make_commit_message(idx, total, author_dt)
        planned_commits.append((author_dt, committer_dt, msg, chosen_day))

    # Build preview heatmap array
    counts_by_offset = defaultdict(int)
    for a_dt, c_dt, msg, chosen_day in planned_commits:
        offset = (today - chosen_day).days
        counts_by_offset[offset] += 1
    heatmap_arr = make_heatmap_data(counts_by_offset, total_days)

    # Terminal rendering (rainbow vomit)
    heatmap_terminal = render_heatmap_terminal(heatmap_arr, use_color=args.use_color)
    hist_terminal = render_histogram_terminal(heatmap_arr, use_color=args.use_color)

    # Print a wildly colorful preview
    print("\n" + "=" * 80)
    print(f"{BOLD}{FG_WHITE}🧭 OVER-THE-TOP PLANNED COMMITS PREVIEW 🧭{RESET}")
    print("=" * 80 + "\n")
    print(f"{BOLD}📁 Repo:{RESET} {repo}")
    print(f"{BOLD}📝 Target file:{RESET} {target_file_rel}")
    print(f"{BOLD}🔢 Planned commits:{RESET} {total}")
    print(f"{BOLD}📅 Range:{RESET} {start_date.isoformat()} → {end_date.isoformat()} ({total_days} days)")
    print(f"{BOLD}🌈 Mode:{RESET} {args.spread_mode}    {BOLD}Weekdays-only:{RESET} {'ON' if args.weekdays_only else 'OFF'}")
    print(f"{BOLD}🎲 Seed:{RESET} {args.seed}")
    print("\n" + heatmap_terminal + "\n")
    print(hist_terminal)
    print("\nSample planned commits (first 20):\n")
    for i, (a_dt, c_dt, msg, chosen_day) in enumerate(planned_commits[:20], start=1):
        ad = a_dt.strftime("%Y-%m-%d %H:%M:%S UTC")
        cd = c_dt.strftime("%Y-%m-%d %H:%M:%S UTC")
        diff_hours = abs((c_dt - a_dt).total_seconds()) / 3600.0
        color_idx = i % len(PALETTE_BG)
        prefix = PALETTE_BG[color_idx] + FG_BLACK + " " + RESET
        print(f"{prefix} {BOLD}{i:3d}{RESET}. {chosen_day.isoformat()} | Author: {ad} | Committer: {cd} | Δ {diff_hours:.2f}h")
        print(f"     → {msg}")

    print("\nTotals by day-offset (days ago : commits):")
    for d in sorted(counts_by_offset.keys()):
        print(f"  {d:3d} days ago : {counts_by_offset[d]} commits")

    # If preview-only: export JSON and optionally SVG, then stop
    if args.preview_only:
        timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
        preview_filename = os.path.join(repo, f"planned_commits_preview_{timestamp}.json")
        json_list = []
        for a_dt, c_dt, msg, chosen_day in planned_commits:
            json_list.append({
                "author_date_iso": a_dt.strftime("%Y-%m-%dT%H:%M:%S+00:00"),
                "committer_date_iso": c_dt.strftime("%Y-%m-%dT%H:%M:%S+00:00"),
                "chosen_day": chosen_day.isoformat(),
                "message": msg
            })
        with open(preview_filename, "w", encoding="utf-8") as jf:
            json.dump({
                "repo": repo,
                "target_file": target_file_rel,
                "generated_at_utc": datetime.utcnow().isoformat() + "Z",
                "commits_count": len(json_list),
                "commits": json_list
            }, jf, indent=2, ensure_ascii=False)
        print(f"\n💾 Preview JSON exported to: {preview_filename} ✅")
        if args.svg_out:
            svg_path = os.path.join(repo, args.svg_out) if not os.path.isabs(args.svg_out) else args.svg_out
            try:
                export_svg_heatmap(heatmap_arr, svg_path, start_date)
                print(f"🖼️ SVG heatmap exported to: {svg_path} ✅")
            except Exception as e:
                print(f"❌ Failed to export SVG: {e}")
        print("\n--preview-only set: stopping before creating commits. 🚫")
        return

    # Ensure target file exists and then create commits
    if not os.path.exists(target_file):
        with open(target_file, "w", encoding="utf-8") as f:
            f.write("# generated commit log — rainbow edition 🌈\n")

    print("\n🔨 Creating commits now... (prepare to be dazzled) 🔨")
    sys.stdout.flush()

    for i, (author_dt, committer_dt, full_msg, chosen_day) in enumerate(planned_commits, start=1):
        author_iso = iso_utc(author_dt)
        committer_iso = iso_utc(committer_dt)

        line = f"{author_iso}  - {full_msg}\n"
        with open(target_file, "a", encoding="utf-8") as f:
            f.write(line)

        try:
            run_git(["add", target_file_rel], repo)
        except subprocess.CalledProcessError as e:
            print("git add failed:", e.stderr.decode().strip())
            raise SystemExit(1)

        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = author_iso
        env["GIT_COMMITTER_DATE"] = committer_iso

        try:
            run_git(["commit", "-m", full_msg], repo, env=env)
        except subprocess.CalledProcessError as e:
            stderr = e.stderr.decode().strip()
            if "nothing to commit" in stderr.lower():
                try:
                    run_git(["commit", "--allow-empty", "-m", full_msg], repo, env=env)
                except subprocess.CalledProcessError as e2:
                    print("Commit failed even with --allow-empty:", e2.stderr.decode().strip())
                    raise SystemExit(1)
            else:
                print("git commit failed:", stderr)
                raise SystemExit(1)

        if i % 25 == 0 or i == total:
            print(f"  -> created {i}/{total} commits (latest author date {author_iso})")
            sys.stdout.flush()

    print("\n✅ Done. If you want these upstream: git push origin <branch>")
    print("⚠️ Reminder: this creates historical commits — don't misrepresent real work. Use for demos/sandbox only. 🧪")
    print("🏴‍☠️ Party on, pirate coder. Stay consensual, stay silly. 🌈")

if __name__ == "__main__":
    main()