# 🛡️ Development Quality Assurance

This section documents the comprehensive quality assurance setup for velvet-chains corsair development.

## 🎯 Pre-Commit Quality Guards

The repository uses **pre-commit hooks** that automatically run before each commit to ensure code quality. These hooks will:

- **🐍 Format Python** with ruff to corsair standards
- **🔍 Lint Python** and auto-fix issues where possible
- **⚔️ Compile Rust** to catch syntax/type errors immediately
- **💎 Format Rust** with cargo fmt for consistent styling
- **🔨 Lint Rust** with clippy to enforce best practices
- **📝 Clean whitespace** and ensure proper file endings
- **🚫 Block large files** to keep repository lean
- **📚 Validate Markdown** documentation format

### Installation (One-Time Setup)

```bash
# Install pre-commit (macOS with Homebrew)
brew install pre-commit

# Install hooks in the repository
pre-commit install
```

### Manual Pre-Commit Execution

```bash
# Run on all files
pre-commit run --all-files

# Run on staged files only (default)
pre-commit run
```

## 🎪 Convenient Make Commands

Use the provided Makefile for common development tasks:

```bash
make help      # 🎭 Show all available commands
make test      # 🧪 Run complete test suite
make lint      # 🔍 Run all linting checks
make format    # 🎨 Format all code
make check     # 🔧 Verify compilation
make build     # 🏗️ Build release binary
make clean     # 🧹 Clean build artifacts
make all       # 🎯 Complete workflow (format→lint→test→build)
```

## 🧪 Complete Test Suite

The `test-all.sh` script runs comprehensive quality checks:

```bash
./test-all.sh
```

This includes:
- **Python formatting** and linting
- **Rust compilation**, formatting, and linting
- **Integration tests** of core functionality
- **Syntax validation** for both languages

## 🎭 Quality Standards

### Python Code Standards
- **Formatting**: Managed by `ruff format` (black-compatible)
- **Linting**: Enforced by `ruff check` with modern Python practices
- **Line Length**: 88 characters (ruff default)
- **Import Style**: Explicit imports, f-strings preferred

### Rust Code Standards
- **Edition**: 2021 (latest stable)
- **Formatting**: `cargo fmt` with project defaults
- **Linting**: `clippy` with warnings as errors (`-D warnings`)
- **Error Handling**: Modern patterns with `?` operator

### Commit Standards
- **Pre-commit**: All hooks must pass before commit
- **Messages**: Theatrical corsair style with emoji and clear scope
- **History**: Clean, atomic commits with descriptive messages

## 🚨 Error Prevention

The quality guards prevent common issues:

- **Compilation errors** before they reach CI/CD
- **Formatting inconsistencies** across different editors
- **Linting violations** that would fail automated checks
- **Large files** accidentally committed
- **Syntax errors** in Python or Rust
- **Trailing whitespace** and missing newlines

## 🎪 Troubleshooting

**Pre-commit hook failures:**
```bash
# See what failed and why
pre-commit run --all-files --verbose

# Skip hooks for emergency commits (use sparingly)
git commit --no-verify -m "emergency fix"

# Update hook versions
pre-commit autoupdate
```

**Environment issues:**
```bash
# Reinstall hooks after major changes
pre-commit clean
pre-commit install

# Test specific hook
pre-commit run rust-fmt --all-files
```

---

**⚓ Remember**: These quality guards ensure that every commit sparkles with theatrical excellence while maintaining professional technical standards! 🎭✨
