---
id: src-comparison-of-6502-random-generators
type: source
title: 'Source Summary: Comparison of 6502 pseudo random generators'
aliases:
- Comparison of 6502 pseudo random generators
- comparison_of_6502_random_generators.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/comparison_of_6502_random_generators.md
  sha256: c37b8b9b169458e7b4ec5ebb31ebe9f72ce1660fa313120740ff8d927387ea91
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Comparison of 6502 pseudo random generators

**Raw Source File**: `data/docs/codebase_c64_org/base/comparison_of_6502_random_generators.md`
**SHA256**: `c37b8b9b169458e7b4ec5ebb31ebe9f72ce1660fa313120740ff8d927387ea91`

## Summary



# Comparison of 6502 pseudo random generators

# Comparison of 6502 pseudo random generators

This is an overview of the main properties of eight algorithms here on codebase.

Each algorithm was implemented as stated in the linked articles. Code size, execution time was measured. Execution times do not include the RTS command. Many PRNGs have a problem when the internal state becomes 0. Since this might be an important feature, it was stated which algorithms can also eventually output and hand...
