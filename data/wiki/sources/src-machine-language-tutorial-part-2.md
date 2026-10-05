---
id: src-machine-language-tutorial-part-2
type: source
title: 'Source Summary: Machine Language Tutorial Part 2 - Memory Manipulation'
aliases:
- Machine Language Tutorial Part 2 - Memory Manipulation
- machine_language_tutorial_part_2.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/machine_language_tutorial_part_2.md
  sha256: 345213dc15332dbd6a6a4297fa7b0444d0ce4614aef237077205910201280e94
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Machine Language Tutorial Part 2 - Memory Manipulation

**Raw Source File**: `data/docs/codebase_c64_org/base/machine_language_tutorial_part_2.md`
**SHA256**: `345213dc15332dbd6a6a4297fa7b0444d0ce4614aef237077205910201280e94`

## Summary



# Machine Language Tutorial Part 2 - Memory Manipulation

### Table of Contents

# Machine Language Tutorial Part 2 - Memory Manipulation

The 6510 has three registers that can all hold 8 bits of data (this is why the C64 is called an 8-bit computer): A, X, and Y. The proper name for the A register is the accumulator because of its ability to do math, and X & Y are called index registers. You cannot transfer data directly between two memory addresses, so these must pass through the registers.
...
