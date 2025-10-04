# voidlight

A BDSM space-pirate romance generator for git commit messages. Use it to:

- append four-sentence micro-novellas to every commit (`prepare-commit-msg`)
- print fresh stories for release notes or issue threads
- run `git voidlight --commit ...` to stage, commit, and flourish in one breath

## Installation

```bash
cargo install voidlight
```

## Usage

```bash
git voidlight --commit -m "Tightened the plasma rig"
```

Install the hook directly:

```bash
git voidlight install-hook
```

The hook simply invokes `git-voidlight --hook "$@"`.

## License

MIT
