# 🏴‍☠️ generate_snark.py — Neon-Slick Snark Cannon

Welcome aboard the **Absolutely gaudy, NSFW, emoji-saturated, rainbow-vomiting snark-commit generator**. This script fabricates ridiculous historical commits drenched in pirate sass, consensual rope-play metaphors, and retina-melting ANSI colors. It’s **only** for demos, art projects, and consenting glitter goblins — never for impersonating real work.

> ⚠️ Safe word reminder: _"fiction"_. Don’t weaponize fabricated history without consent.

## 🌈 Feature Striptease

- Generates `N` commits with randomized messages, timestamps, and blame tags.
- Supports day-by-day or week-wise spreading, weekday-only planning, and weighted months.
- Preview mode prints a rainbow heatmap + histogram, exports JSON, and optional SVG.
- Import the preview JSON later to replay the exact choreographed commit queue.
- Fully colorized output with `--no-color` grayscale aftercare available.
- Slots-powered dataclasses and other Python 3.12+ delights for maximum sheen.

## 🛠️ Requirements & Setup

- **Python 3.12+** (the script mainlines `datetime.UTC`, `argparse.BooleanOptionalAction`, and other modern toys).
- An existing git repository with a branch you’re comfortable desecrating.
- Optional but spicy: `ruff` for formatting (`pip install ruff`).

Clone or copy the script into your repo, then:

```bash
python3.12 -m pip install --upgrade ruff
chmod +x generate_snark.py
```

## 🚀 Quick Start Fantasia

### Preview Without Touching Git History

```bash
python3.12 generate_snark.py -n 50 --preview-only --svg-out preview.svg
```

This splashes the terminal with:

- summary stats
- rainbow heatmap + histogram
- top 20 planned commits
- a JSON file in the repo root (`planned_commits_preview_<timestamp>.json`)
- optional SVG heatmap if you supplied `--svg-out`

### Commit For Real (Still: Demo Branch Only)

```bash
python3.12 generate_snark.py \
  -n 120 \
  --repo . \
  --file .generated_commits.txt \
  --spread-mode week \
  --start-date 2024-01-01 \
  --end-date 2024-12-31
```

The script appends log entries to `.generated_commits.txt`, stages them, and creates commits with historical timestamps spaced inside ±8 hours.

## 🔄 Importing A Previously Exported Plan

Preview JSONs are reusable choreographies. To replay one exactly:

```bash
python3.12 generate_snark.py \
  --import-json planned_commits_preview_20251004T123059Z.json
```

You can still override `--repo` or `--file` if you want to aim the glitter cannon elsewhere.

## 🎛️ CLI Cheat Sheet

| Flag | Default | Description |
|------|---------|-------------|
| `-n / --num` | required | Commit count to fabricate. |
| `--repo` | `.` | Path to an existing git repo. |
| `--file` | `.generated_commits.txt` | File to append commit log entries. |
| `--seed` | `None` | Random seed for reproducible chaos. |
| `--start-date` / `--end-date` | None | Explicit date window (inclusive). |
| `--start-days-ago` | `365` | If no explicit start, backfill this many days. |
| `--spread-mode` | `day` | `day` or `week` distribution. |
| `--month-weights` | `1,1,...` | Comma-separated 12-tuple of relative weights. |
| `--weekdays-only` | off | Skip weekends entirely. |
| `--color` / `--no-color` | on | Toggle the rainbow vomit in terminal output. |
| `--svg-out` | None | Write an SVG heatmap when previewing. |
| `--max-attempts-offset` | `20` | Retry budget for finding committer timestamps. |
| `--preview-only` | off | Produce previews/export JSON without committing. |
| `--import-json` | None | Load a preview JSON and replay its plan. |

## 🧪 Development / Safety Rituals

- Format: `ruff format generate_snark.py`
- Byte-compile sanity: `PYTHONPYCACHEPREFIX=./.pycache python3.12 -m compileall generate_snark.py`
- Dry runs: always start with `--preview-only` before touching history.
- Keep commits quarantined (e.g., on a `demo/snark` branch). Never merge into production without consent.

## 🔥 Consent Clause

- These commits are fictional. Don’t use them to falsify work, harass teams, or otherwise break trust.
- Always inform collaborators before pushing the glitter avalanche upstream.
- Clean up when you’re done (`git reset --hard`, delete branches, remove `.generated_commits.txt`).

Now grab your shiniest eyepatch, hydrate, and let the rainbow cannon roar.🏳️‍🌈
