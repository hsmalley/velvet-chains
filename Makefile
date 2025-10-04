# 🏴‍☠️ Velvet Chains Corsair Makefile - Command your fleet with theatrical precision
# Provides convenient targets for development, testing, and deployment rituals

.PHONY: help install test lint format check build clean pre-commit all
.DEFAULT_GOAL := help

# 🎭 Color codes for theatrical output
BOLD := \033[1m
RED := \033[31m
GREEN := \033[32m
YELLOW := \033[33m
BLUE := \033[34m
PURPLE := \033[35m
CYAN := \033[36m
RESET := \033[0m

## 🎪 Display this magnificent help menu
help:
	@echo "$(BOLD)$(PURPLE)🏴‍☠️ VELVET CHAINS CORSAIR COMMAND CENTER$(RESET)"
	@echo "$(CYAN)═══════════════════════════════════════════$(RESET)"
	@echo ""
	@echo "$(BOLD)Available theatrical commands:$(RESET)"
	@echo ""
	@awk 'BEGIN {FS = ":.*##"} /^[a-zA-Z_-]+:.*?##/ { printf "$(YELLOW)%-15s$(RESET) %s\n", $$1, $$2 }' $(MAKEFILE_LIST)
	@echo ""
	@echo "$(CYAN)Usage: make <command>$(RESET)"
	@echo "$(CYAN)Example: make test$(RESET)"

## 🔧 Install all dependencies and setup development environment
install:
	@echo "$(BOLD)$(BLUE)🔧 Installing corsair development dependencies...$(RESET)"
	brew install pre-commit rust python@3.13 || true
	pre-commit install
	@echo "$(GREEN)✅ Development environment ready for theatrical coding!$(RESET)"

## 🧪 Run all tests and quality checks
test:
	@echo "$(BOLD)$(BLUE)🧪 Running complete test ritual...$(RESET)"
	./test-all.sh
	@echo "$(GREEN)✅ All tests pass with corsair excellence!$(RESET)"

## 🔍 Run linting and code quality checks
lint:
	@echo "$(BOLD)$(BLUE)🔍 Submitting code to quality dominatrix...$(RESET)"
	ruff check voidlight_choreographer.py voidlight_whispers.py
	cargo clippy --manifest-path voidlight_engine/Cargo.toml --all-targets -- -D warnings
	@echo "$(GREEN)✅ Code meets corsair standards!$(RESET)"

## 🎨 Format all code with velvet precision
format:
	@echo "$(BOLD)$(BLUE)🎨 Formatting code with theatrical precision...$(RESET)"
	ruff format voidlight_choreographer.py voidlight_whispers.py
	cargo fmt --manifest-path voidlight_engine/Cargo.toml
	@echo "$(GREEN)✅ Code formatted to corsair perfection!$(RESET)"

## 🔧 Check compilation without building artifacts
check:
	@echo "$(BOLD)$(BLUE)🔧 Verifying compilation integrity...$(RESET)"
	python3 -m compileall voidlight_choreographer.py voidlight_whispers.py
	cargo check --manifest-path voidlight_engine/Cargo.toml
	@echo "$(GREEN)✅ All code compiles cleanly!$(RESET)"

## 🏗️ Build the complete voidlight engine
build:
	@echo "$(BOLD)$(BLUE)🏗️ Forging voidlight engine with steel precision...$(RESET)"
	cargo build --manifest-path voidlight_engine/Cargo.toml --release
	@echo "$(GREEN)✅ Voidlight engine forged and ready for deployment!$(RESET)"

## 🧹 Clean build artifacts and temporary files
clean:
	@echo "$(BOLD)$(BLUE)🧹 Cleaning corsair workspace...$(RESET)"
	cargo clean --manifest-path voidlight_engine/Cargo.toml
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
	rm -f /tmp/test_*.txt
	@echo "$(GREEN)✅ Workspace cleaned to corsair standards!$(RESET)"

## 🛡️ Run pre-commit hooks on all files
pre-commit:
	@echo "$(BOLD)$(BLUE)🛡️ Running pre-commit quality guard...$(RESET)"
	pre-commit run --all-files
	@echo "$(GREEN)✅ All pre-commit hooks pass!$(RESET)"

## 🎯 Run complete development workflow (format, lint, test, build)
all: format lint check test build
	@echo "$(BOLD)$(GREEN)🎉 Complete corsair development workflow successful!$(RESET)"
	@echo "$(CYAN)Your velvet chains sparkle with theatrical excellence! ✨$(RESET)"

## 📦 Create release artifacts
release: clean all
	@echo "$(BOLD)$(BLUE)📦 Preparing corsair release artifacts...$(RESET)"
	cargo build --manifest-path voidlight_engine/Cargo.toml --release
	@echo "$(GREEN)✅ Release artifacts ready for deployment!$(RESET)"
	@echo "$(YELLOW)Release binary: $(RESET)voidlight_engine/target/release/git-voidlight"
