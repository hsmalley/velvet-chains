# 🏴‍☠️ Velvet Chains Examples

Welcome to our treasure trove of voidlight demonstrations, darling. These examples showcase the consensual chaos and theatrical git wizardry of our space-pirate toolchain.

## 🌟 **Quick Start Examples**

### **Preview Only (Safe Harbor)**
```bash
# Rainbow preview with 50 commits - no git history touched
python3.12 voidlight_choreographer.py -n 50 --preview-only

# Generate SVG heatmap for sharing the spectacle  
python3.12 voidlight_choreographer.py -n 100 --preview-only --svg-out demo_heatmap.svg

# Preview with specific date range
python3.12 voidlight_choreographer.py \
  -n 80 \
  --start-date 2024-01-01 \
  --end-date 2024-12-31 \
  --preview-only
```

### **Commit Generation (Sandbox Required)**
```bash
# Create demo branch first (safety protocol)
git checkout -b demo/voidlight-showcase

# Generate commits with weekly spread
python3.12 voidlight_choreographer.py \
  -n 120 \
  --spread-mode week \
  --weekdays-only \
  --start-date 2024-06-01 \
  --end-date 2024-11-30

# Clean up afterward (consensual aftercare)
git checkout main
git branch -D demo/voidlight-showcase
```

## 🎨 **Advanced Choreography**

### **Seasonal Patterns**
```bash
# Winter coding surge (Dec-Feb weighted)
python3.12 voidlight_choreographer.py \
  -n 200 \
  --month-weights 3,3,1,0.5,0.5,0.5,0.5,0.5,0.5,1,2,3 \
  --preview-only

# Summer lull pattern (Jun-Aug minimal)  
python3.12 voidlight_choreographer.py \
  -n 150 \
  --month-weights 2,2,2,1.5,1,0.3,0.3,0.3,1,1.5,2,2 \
  --preview-only
```

### **Corporate Fibonacci Spectacle**
```bash
# Fibonacci sequence for month weights (mathematical beauty)
python3.12 voidlight_choreographer.py \
  -n 300 \
  --month-weights 1,1,2,3,5,8,13,8,5,3,2,1 \
  --spread-mode week \
  --preview-only \
  --svg-out fibonacci_commits.svg
```

## 🛸 **Rust Engine Examples**

### **Direct Story Generation**
```bash
# Single pirate tale for commit messages
git-voidlight

# Deterministic story with seed
git-voidlight --seed 1337

# Stage, commit, and flourish in one command
git-voidlight --commit -a -m "Refactor plasma conduits" 
```

### **Hook Installation**
```bash
# Install prepare-commit-msg hook automatically
git-voidlight install-hook

# Force overwrite existing hook
git-voidlight install-hook --force

# Install to custom location
git-voidlight install-hook ~/.git-templates/hooks/
```

## 🌊 **Workflow Demonstrations**

### **Lightning Demo (Conference Ready)**
```bash
#!/bin/bash
# Perfect for livestreams and conference demos

echo "🏴‍☠️ Velvet Chains Lightning Demo"
echo "=================================="

# Quick preview burst
python3.12 voidlight_choreographer.py \
  -n 25 \
  --spread-mode day \
  --start-days-ago 30 \
  --weekdays-only \
  --preview-only \
  --color

echo ""
echo "✨ Demo complete - no git history harmed! ✨"
```

### **Corporate Chaos (Fiscal Quarter)**
```bash
#!/bin/bash
# Demonstrate a typical corporate development cycle

# Q1: Project kickoff surge
python3.12 voidlight_choreographer.py \
  -n 180 \
  --start-date 2024-01-01 \
  --end-date 2024-03-31 \
  --month-weights 3,8,5,0,0,0,0,0,0,0,0,0 \
  --weekdays-only \
  --preview-only \
  --svg-out q1_surge.svg

echo "Q1 surge pattern exported to q1_surge.svg"
```

### **Night Parade (Goth Aesthetic)**
```bash
#!/bin/bash
# Halloween to Valentine's Day romantic arc

python3.12 voidlight_choreographer.py \
  -n 88 \
  --seed 1986 \
  --start-date 2024-10-31 \
  --end-date 2025-02-14 \
  --weekdays-only \
  --color \
  --preview-only

echo "🌙 Romantic winter arc complete 💕"
```

## 📊 **Output Samples**

### **Terminal Heatmap (Rainbow Mode)**
```
🌈 RAINBOW HEATMAP (older → newer, 90 days) 🌈

Mon ░░██████████▓▓▓▓▓██████░░░░
Tue ██▓▓▓▓████████▓▓▓▓▓███████░
Wed ░▓▓███████████████▓▓▓▓▓▓░░░
Thu ░░████████▓▓▓▓▓▓▓███████░░░
Fri ░░░███▓▓▓███████▓▓▓██████░░
Sat ░░░░░░░░░░░░░░░░░░░░░░░░░░░
Sun ░░░░░░░░░░░░░░░░░░░░░░░░░░░

    ‾    ‾    ‾    ‾    ‾    ‾    ‾
```

### **Sample Generated Messages**
```
🏴‍☠️ Captain Velvet, corseted corsair caught me against the trembling 
bulkhead, breath hot with rum-drenched sin. Silk ropes braided the 
safe word around my pulse. I traded the treasure map inked beneath 
my ribs for another strike. Until the void shuddered and moaned 
like a satiated kraken. 🪢🔥

✨ Mistress Nebula, whip-smart navigator sealed me to the figurehead 
with starlit chains and a smile sharper than a cutlass. Chains sang 
hymns of desire against the bulkhead. We rewrote the Articles of 
Plunder line by sweating line. While the Jolly Roger fluttered 
like a lover's gasp. 🛸🍑
```

## 🔧 **Troubleshooting & Tips**

### **Common Issues**
```bash
# If commits seem too clustered
--spread-mode week  # Use week-based distribution

# If dates are outside expected range  
--start-date 2024-01-01 --end-date 2024-12-31  # Explicit bounds

# If you want reproducible results
--seed 42  # Same seed = same output

# If colors hurt your terminal
--no-color  # Disable rainbow output
```

### **Safety Reminders**
- Always start with `--preview-only`
- Use demo branches for real commit generation
- Clean up afterward with `git reset --hard` 
- Never run on main/master without team consent

## 📝 **Integration Examples**

### **CI/CD Demo Generation**
```yaml
# .github/workflows/demo-generation.yml
name: Generate Demo Commits
on: 
  workflow_dispatch:
    inputs:
      commit_count:
        default: 50
        
jobs:
  demo:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Generate Preview
        run: |
          python3.12 voidlight_choreographer.py \
            -n ${{ github.event.inputs.commit_count }} \
            --preview-only \
            --svg-out demo_output.svg
      - name: Upload SVG
        uses: actions/upload-artifact@v4
        with:
          name: demo-heatmap
          path: demo_output.svg
```

### **Pre-commit Hook Integration**
```bash
# Add to .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: voidlight-preview
        name: Voidlight Preview Check
        entry: python3.12 voidlight_choreographer.py
        args: [-n, "10", --preview-only]
        language: system
        pass_filenames: false
        always_run: true
```

---

*Remember: These examples are for demonstration, education, and consensual chaos. Always respect git history, announce your intentions, and clean up afterward. The safe word is "fiction"!* 

🏴‍☠️ **Happy sailing, corsair!** ⚓
