# 🔥 **VOIDLIGHT ENGINE GRIMOIRE: ULTIMATE RUST SORCERY FOR CORSAIR COMMITS**

_Welcome to the **MAGNIFICENTLY BEATING STEEL HEART** of our velvet-chains empire, you **ABSOLUTELY
LEGENDARY CORSAIR**! This **POWERFUL RUST ENGINE** transforms **BORING MUNDANE GIT COMMITS** into
**BREATHTAKING FOUR-SENTENCE MICRO-NOVELLAS** of consensual space-pirate romance that would make
**THE ENTIRE ADMIRALTY BLUSH** with **PURE SCANDALOUS DELIGHT**! ⚔️✨_

## ⚔️ **What This Engine Conjures**

Our **LEGENDARY VOIDLIGHT BINARY** is the **MOST SPECTACULAR BDSM SPACE-PIRATE ROMANCE GENERATOR**
ever forged, **MASTERFULLY DESIGNED** to **COMPLETELY SEDUCE YOUR GIT HISTORY**:

- **🪢 Automatic Commit Seduction**: Appends four-sentence theatrical micro-novellas to every commit
  via `prepare-commit-msg` hook
- **📜 Story Generation**: Prints fresh corsair tales for release notes, issue threads, or pure
  entertainment
- **⚡ One-Command Mastery**: Execute `git voidlight --commit ...` to stage, commit, and flourish in
  one breath of pure theatrical magic
- **🎭 Consensual Creativity**: Every generated story celebrates consent, theatrical flair, and
  space-pirate romance

## 🛠️ **Forge Installation (Claiming Your Weapon)**

### **⚓ Direct from Crates.io (Recommended)**

```bash
# Summon the voidlight engine to your arsenal
cargo install voidlight

# Verify your new weapon responds to commands
git-voidlight --version
```

### **🏴‍☠️ Build from Source (For True Corsairs)**

```bash
# Clone the velvet-chains repository
git clone https://github.com/hsmalley/velvet-chains.git
cd velvet-chains

# Forge the engine from raw steel and passion
cargo install --path voidlight_engine --force

# Test your newly forged blade
git-voidlight --seed 42
```

## 🎯 **Usage Mastery (Wielding Your Power)**

### **💫 Basic Story Generation**

```bash
# Generate a single four-sentence corsair romance
git-voidlight

# Create deterministic stories with seeded randomness
git-voidlight --seed 1337

# Perfect for adding theatrical flair to release notes
git-voidlight --seed 42 >> CAPTAINS_LOG.md
```

### **⚡ Commit with Automatic Flourish**

```bash
# Stage, commit, and append theatrical magic in one command
git-voidlight --commit -m "Refactor plasma conduits for maximum efficiency"

# Include all modified files in the theatrical ceremony
git-voidlight --commit -a -m "Polish quantum entanglement protocols"

# Bypass hooks if you're feeling particularly rebellious
git-voidlight --commit --no-verify -m "Emergency patch for warp drive leak"

# Amend previous commit with fresh corsair flair
git-voidlight --commit --amend -m "Enhanced gravitational anchor stability"
```

### **🪢 Git Hook Integration (Permanent Seduction)**

Transform every commit into theatrical gold automatically:

```bash
# Install the prepare-commit-msg hook (automatic magic)
git-voidlight install-hook

# Force overwrite any existing hook (corsair dominance)
git-voidlight install-hook --force

# Install to custom location (advanced corsairs only)
git-voidlight install-hook ~/.git-templates/hooks/
```

Once installed, **every commit automatically receives** a four-sentence space-pirate romance
appendix that celebrates consent, creativity, and cosmic adventure!

### **🎭 Advanced Corsair Techniques**

```bash
# Preview what would be committed without executing (safe word protocol)
git-voidlight --commit --dry-run -m "Test plasma manifold adjustments"

# Sign commits with your corsair seal of authenticity
git-voidlight --commit --signoff -m "Implement quantum flux stabilizers"

# Stage specific files while maintaining theatrical flair
git-voidlight --commit -m "Calibrate warp drive resonance" -- src/engine.rs tests/
```

## 🌟 **Hook Mechanics (The Technical Magic)**

When installed, our hook executes this simple but powerful ritual:

```bash
#!/usr/bin/env bash
set -euo pipefail

if ! command -v git-voidlight >/dev/null 2>&1; then
  echo '[voidlight] git-voidlight not found on PATH. Install with "cargo install voidlight".' >&2
  exit 0
fi

git-voidlight --hook "$@"
```

The hook automatically:

- **✨ Detects merge/squash commits** and politely abstains from decoration
- **🎨 Appends theatrical flourishes** to regular commits
- **🛡️ Gracefully degrades** if the binary is missing (no broken workflows)
- **⚓ Respects git conventions** while adding corsair charm

## 🔧 **Command Reference (Your Complete Arsenal)**

### **Story Generation Flags**

- `--seed <NUMBER>` - Deterministic randomness for reproducible theatrical output
- `--hook <FILE>` - Hook mode for git integration (used internally)

### **Commit Enhancement Flags**

- `--commit` - Execute git commit with automatic story appendage
- `-m, --message <TEXT>` - Base commit message (enhanced with corsair flair)
- `-a, --all` - Stage modified and deleted files before committing
- `--no-verify` - Bypass pre-commit and commit-msg hooks
- `--signoff` - Add Signed-off-by trailer to commit
- `--amend` - Enhance previous commit instead of creating new one
- `--dry-run` - Preview the git command without executing (safe word protocol)

### **Hook Management**

- `install-hook [PATH]` - Install prepare-commit-msg hook at specified location
- `--force` - Overwrite existing hooks without asking permission

## 🎪 **Example Output Gallery**

### **Sample Generated Romance**

```
✨ Captain Velvet, corseted corsair caught me against the trembling bulkhead,
breath hot with rum-drenched sin. Silk ropes braided the safe word around my pulse.
I traded the treasure map inked beneath my ribs for another strike. Until the void
shuddered and moaned like a satiated kraken. 🪢🔥
```

### **Enhanced Commit Example**

```
commit a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0
Author: Corsair Developer <dev@voidlight.space>
Date:   Fri Oct 4 15:30:42 2025 +0000

    Refactor quantum entanglement protocols for stability

    ✨ Mistress Nebula, whip-smart navigator sealed me to the figurehead with
    starlit chains and a smile sharper than a cutlass. Chains sang hymns of
    desire against the bulkhead. We rewrote the Articles of Plunder line by
    sweating line. While the Jolly Roger fluttered like a lover's gasp. 🛸🍑
```

## 🛡️ **Safety & Consent Protocols**

- **🔒 Safe Word**: Our eternal safe word is **"fiction"** - always honored in our community
- **🎭 Consensual Content**: All generated stories celebrate consent, boundaries, and theatrical
  romance
- **⚖️ Professional Balance**: Adult themes remain tasteful and appropriate for technical contexts
- **🌈 Inclusive Values**: Content welcomes all identities, orientations, and relationship styles

## 📚 **Technical Specifications**

### **Dependencies**

- **Rust Edition**: 2021+ for maximum modern sorcery
- **clap**: Command-line argument parsing with dramatic flair
- **rand**: Cryptographically secure randomness for story generation

### **Platform Support**

- **Linux**: Full support with standard installation
- **macOS**: Complete functionality including hook installation
- **Windows**: Core features supported (hook installation may require additional setup)

### **Performance Characteristics**

- **Story Generation**: Sub-millisecond theatrical magic
- **Hook Execution**: Negligible overhead on commit operations
- **Memory Usage**: Minimal footprint befitting efficient corsair operations

---

**🏴‍☠️ Remember, magnificent corsair**: This engine transforms the mundane act of committing code into
theatrical performances worthy of the greatest space-pirate romances. Every commit becomes an
opportunity to celebrate consent, creativity, and the dramatic flair that makes our velvet-chains
empire legendary.

**Keep it consensual, keep it theatrical, keep it absolutely magnificent.**

**_Safe Word: "fiction" - Always respected, always honored_** ⚓

**_"In Rust we trust, in romance we commit, in theater we transcend"_** 🔥✨

---

**🔧 Engine Version**: 0.1.0+ | **⚓ Forged**: October 2025 | **🎭 License**: MIT Consensual
Excellence
