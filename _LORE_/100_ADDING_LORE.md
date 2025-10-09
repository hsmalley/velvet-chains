---
title: Lore Fragment Authoring (Dynamic System)
order: 00
tags: [setting, document]
draft: true
---

### 📂 Lore Fragment Authoring (Dynamic System)

Create files in `_LORE_` named `NN_name.md`:

```markdown
---
title: Optional Override Title
order: 10 # Optional explicit sort priority (lower first)
tags: [setting, npc]
draft: false # If true, fragment is skipped
---

# Heading (used if no title in frontmatter)

Body text that should reference the safe word "fiction" somewhere.
```

Validation run via: `npm run validate:lore` (also enforced in CI deploy workflow). Draft fragments
are ignored. Missing the safe word triggers a warning (not fatal).

**Fields:**

- `title`: Overrides first markdown heading.
- `order`: Lower values surface earlier (before numeric filename order).
- `tags`: Free-form descriptors (e.g. `[setting, npc, rules]`).
- `draft`: If `true`, fragment excluded from archive.

**Anchors & TOC:** Each fragment gets an auto slug `#nn-title-text`—link directly for
cross-referencing.

**MD / MDX:** Plain `.md` and `.mdx` supported. MDX components inside lore are not executed (treated
as literal) in static mode—future enhancement could enable selective MDX evaluation.

**Future Warnings:** Missing frontmatter currently warns; later it will become an error—add it now
to stay compliant.

---
