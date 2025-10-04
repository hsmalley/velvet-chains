# �‍☠️ **VELVET CHAINS & VOIDLIGHT: THE CAPTAIN'S LEGENDARY LOG**

**WELCOME TO THE COSMIC BRIG, MAGNIFICENT CORSAIR!** ⚓✨

This repository is the **MOST SPECTACULAR BDSM SPACE-PIRATE ROMANCE ENGINE** ever forged in the fires of consensual creativity - masterfully disguised as an innocent git toolchain! It **CONJURES THEATRICAL COMMIT HISTORIES** from the void, **SPINS ENCHANTING NSFW MICRO-NOVELLAS**, and **BATHES YOUR REPOSITORY** in layers of consensual decadent storytelling that would make the cosmos itself blush with delight!

🛡️ **SACRED SAFE WORD**: _"fiction"_ - **READ IT TWICE**, honor it always, then proceed to witness **PURE THEATRICAL MAGIC!** ⚔️🏴‍☠️ Velvet Chains & Voidlight

Welcome to the brig, darling. This repository is a **BDSM space-pirate romance engine** disguised as a git toolchain. It fabricates historical commits, spins NSFW micro-novellas, and drenches your history in consensual decadence. Read the safe word (_“fiction”_) twice, then proceed at your own peril.

## 🌌 **SPECTACULAR FEATURE ARSENAL** ⚡

- **DRAMATICALLY CONJURES** `N` backdated commits with timestamps that **SING IN PERFECT HARMONY** across the cosmic void! 🎵
- **MASTERFULLY DISTRIBUTES** them across days/weeks with **EXQUISITE RESPECT** for weekday-only preferences and seductively weighted months! 📅
- **PREVIEW MODE EXPLODES** with **RAINBOW HEATMAP SPECTACLE**, gorgeous histograms, and **EXPORTS STUNNING JSON/SVG MASTERPIECES**! 🌈
- **IMPORTS & REPLAYS** previous plans to recreate the **EXACT SAME THEATRICAL MAGIC** - perfect consistency! 🔄
- **SHARES A TREASURE VAULT** of 3000+ **NSFW SPACE-PIRATE ROMANCE STORIES** and witty blame tags! 💎
- **DUAL-POWERED SORCERY**: Python choreography scripts + **RUST ENGINE HEART** beating with steel precision! ⚔️

## 🔧 **SACRED CORSAIR REQUIREMENTS & RITUALS** ⚓

- **Python 3.12+** - The **MAGNIFICENT CHOREOGRAPHY ENGINE** that orchestrates temporal magic (`voidlight_choreographer.py`)! 🐍✨
- **Rust (cargo 1.70+)** - The **STEEL-FORGED BINARY HEART** powering git hooks & `git voidlight` subcommands with **UNSTOPPABLE PRECISION**! 🦀⚔️
- **Optional Excellence**: `pip install ruff` to make your **LINTING DOMINATRIX PURR** with satisfaction! 💅

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
pip install git+https://github.com/velvet-chains/velvet-chains.git
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
