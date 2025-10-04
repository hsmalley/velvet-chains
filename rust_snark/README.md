# snarkgit

A BDSM space-pirate romance generator for git commit messages. Use it to:

- append four-sentence micro-novellas to every commit (`prepare-commit-msg`)
- print fresh stories for release notes
- run `git snark --commit ...` to stage, commit, and flourish in one breath

## Installation

```bash
cargo install snarkgit
```

## Usage

```bash
git snark --commit -m "Tightened the plasma rig"
```

Install the hook directly:

```bash
git snark install-hook
```

The hook simply invokes `git-snark --hook "$@"`.

## License

MIT
