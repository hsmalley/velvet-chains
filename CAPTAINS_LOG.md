# 🏴‍☠️ Velvet Chains & Voidlight

Welcome to the brig, darling. This repository is a **BDSM space-pirate romance engine** disguised as a git toolchain. It fabricates historical commits, spins NSFW micro-novellas, and drenches your history in consensual decadence. Read the safe word (_“fiction”_) twice, then proceed at your own peril.

## 🌌 Sinful Feature Cabaret

- Conjures `N` backdated commits with timestamps that purr in harmony.
- Distributes them across days or weeks, respecting weekday-only fantasies and weighted months.
- Preview mode splashes rainbow heatmaps, histograms, and exports JSON/SVG alibis.
- Imports previous plans to replay the exact rope pattern.
- Shares a 3000-entry vault of NSFW space-pirate love letters and blame tags.
- Offers both Python scripts and a Rust heart beating beneath the leather.

## 🔧 Rituals & Requirements

- **Python 3.12+** for the decadent planner (`voidlight_choreographer.py`).
- **Rust (cargo 1.70+)** for the binary hook & `git voidlight` subcommand.
- Optional decadence: `pip install ruff` to make the linter blush.

Initial setup:

```bash
python3.12 -m pip install --upgrade ruff
chmod +x voidlight_choreographer.py
```

### ⛓️ Auto-Hook: Snark at Commit Time

Forge the Rust binary, then let Git whisper it into every commit message:

```bash
cargo install --path voidlight_engine --force
rm -f .git/hooks/prepare-commit-msg
ln -s "$(pwd)/voidlight_hooks/voidlight-commit-ritual" .git/hooks/prepare-commit-msg
```

> Already published to crates.io? Swap the first line for `cargo install voidlight`.

Corporate shackles hate symlinks? Copy instead:

```bash
cp voidlight_hooks/voidlight-commit-ritual .git/hooks/prepare-commit-msg
```

Prefer a version-controlled dungeon?

```bash
git config core.hooksPath voidlight_hooks
```

The hook rebuilds the Rust binary when needed and then laces a 4-sentence kink novella into every commit.

Shortcut: once `git-voidlight` is on your `$PATH`, simply run `git voidlight install-hook` (add `--force` to overwrite an existing hook).

### 🚀 `git voidlight` — Subcommand of Desire

Promote the binary into a first-class git command:

```bash
cargo install --path voidlight_engine --force
```

Then either call it directly or wrap an alias:

```bash
git config alias.voidlight '!git-voidlight'
```

Usage that stages, commits, and appends a flourish in one breath:

```bash
git voidlight --commit -a -m "Refactor the warp-drive leash" -- -- path/to/file
```

Skip `--commit` to simply print a fresh tale to stdout—perfect for `CAPTAINS_LOG` lore or issue comment theatrics.

### 🐍 Python Package (`voidlight-plan`)

Prefer the Python planner? Package it as a CLI:

```bash
pip install .
voidlight-plan --help
```

Or pull straight from the repo:

```bash
pip install git+https://github.com/velvet-chains/snark_tester.git
```

Use `voidlight-plan` exactly like `voidlight_choreographer.py`—all flags carry over, now globally available on your path.

## 🚀 Quick Start Fantasia

### Preview Without Touching Git History

```bash
python3.12 voidlight_choreographer.py -n 50 --preview-only --svg-out preview.svg
```

Expect rainbow vomit, heatmap couture, and a JSON dossier you can tuck into your captain’s coat.

### Commit For Real (Demo Branch Only)

```bash
python3.12 voidlight_choreographer.py \
  -n 120 \
  --repo . \
  --file .generated_commits.txt \
  --spread-mode week \
  --start-date 2024-01-01 \
  --end-date 2024-12-31
```

Every commit writes to `.generated_commits.txt`, stages it, and lands with historical timestamps that stay within 16 h of each other.

### Replaying a Previous Choreography

```bash
python3.12 voidlight_choreographer.py --import-json planned_commits_preview_20251004T123059Z.json
```

Override `--repo` or `--file` if you want to lash the flourish onto a new project.

## 🎛️ CLI Cheat Sheet (Velvet Edition)

| Flag | Default | Description |
|------|---------|-------------|
| `-n / --num` | required | Commit count to fabricate. |
| `--repo` | `.` | Parlor where the fantasy is staged. |
| `--file` | `.generated_commits.txt` | Where the captain scrawls each forged entry. |
| `--seed` | `None` | Random seed for reproducible chaos. |
| `--start-date` / `--end-date` | None | Explicit date window (inclusive). |
| `--start-days-ago` | `365` | Backfill window when no start/end is offered. |
| `--spread-mode` | `day` | `day` or `week` distribution. |
| `--month-weights` | `1,1,...` | Comma-separated 12-tuple of relative weights. |
| `--weekdays-only` | off | Only lash commits Monday–Friday. |
| `--color` / `--no-color` | on | Toggle the rainbow vomit in terminal output. |
| `--svg-out` | None | Write an SVG heatmap when previewing. |
| `--max-attempts-offset` | `20` | How often we try to align author/committer timestamps. |
| `--preview-only` | off | Produce previews/export JSON without committing. |
| `--import-json` | None | Load a preview JSON and replay its plan. |

## 🧪 Rituals & Aftercare

- Polish the code: `ruff format voidlight_choreographer.py`
- Sanity check bytecode: `PYTHONPYCACHEPREFIX=./.pycache python3.12 -m compileall voidlight_choreographer.py`
- Practice safe words: start every dance with `--preview-only`.
- Quarantine the spectacle on a demo branch until everyone consents.

## 🔥 Consent Clause (repeat after me)

- These commits are fiction. Don’t weaponize them.
- Announce before you unleash glitter on teammates.
- When the show ends: `git reset --hard`, delete demo branches, remove `.generated_commits.txt`.

Hydrate. Breathe. Then fire the rainbow cannon. 🏳️‍🌈
