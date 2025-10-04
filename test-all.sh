#!/bin/bash
# 🏴‍☠️ Velvet Chains Test Ritual - Complete Quality Assurance Ceremony
# Runs all tests, lints, and quality checks with corsair precision

set -euo pipefail

echo "🎭 ==============================================="
echo "🏴‍☠️ VELVET CHAINS QUALITY ASSURANCE CEREMONY"
echo "🎭 ==============================================="
echo ""

# Change to script directory
cd "$(dirname "$0")"

echo "🐍 Testing Python Choreographer Magic..."
echo "----------------------------------------"

# Format Python code
echo "🎨 Formatting Python with velvet precision..."
ruff format voidlight_choreographer.py voidlight_whispers.py

# Lint Python code
echo "🔍 Submitting Python to linting dominatrix..."
ruff check voidlight_choreographer.py voidlight_whispers.py

# Test Python compilation
echo "🧪 Testing Python syntax integrity..."
python3 -m compileall voidlight_choreographer.py voidlight_whispers.py

echo ""
echo "⚔️ Testing Rust Engine Sanctification..."
echo "----------------------------------------"

# Check Rust compilation
echo "🔧 Forging Rust engine without flaws..."
cargo check --manifest-path voidlight_engine/Cargo.toml

# Format Rust code
echo "💎 Polishing Rust to mirror finish..."
cargo fmt --manifest-path voidlight_engine/Cargo.toml

# Lint Rust code
echo "🔨 Submitting engine to clippy dominatrix..."
cargo clippy --manifest-path voidlight_engine/Cargo.toml --all-targets -- -D warnings

# Test Rust compilation
echo "🏗️ Building complete voidlight engine..."
cargo build --manifest-path voidlight_engine/Cargo.toml

echo ""
echo "🎯 Running Integration Tests..."
echo "------------------------------"

# Test basic voidlight functionality
echo "🧪 Testing voidlight story generation..."
cd voidlight_engine && cargo run -- --seed 42 generate > /tmp/test_story.txt && cd ..
if [[ -s /tmp/test_story.txt ]]; then
    echo "✅ Story generation successful"
else
    echo "❌ Story generation failed"
    exit 1
fi

# Test choreographer functionality
echo "🧪 Testing choreographer preview mode..."
python3 voidlight_choreographer.py --preview-only -n 1 --seed 42 > /tmp/test_choreo.txt
if [[ -s /tmp/test_choreo.txt ]]; then
    echo "✅ Choreographer preview successful"
else
    echo "❌ Choreographer preview failed"
    exit 1
fi

echo ""
echo "🏆 =============================================="
echo "🎉 ALL QUALITY ASSURANCE CEREMONIES COMPLETE!"
echo "🏆 =============================================="
echo "✨ Your velvet chains sparkle with perfection ✨"
echo ""
