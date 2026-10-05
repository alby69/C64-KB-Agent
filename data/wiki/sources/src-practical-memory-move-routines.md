---
id: src-practical-memory-move-routines
type: source
title: 'Source Summary: Practical Memory Move Routines'
aliases:
- Practical Memory Move Routines
- practical_memory_move_routines.md
tags:
- assembly
- memory management
sources:
- path: data/docs/codebase_c64_org/base/practical_memory_move_routines.md
  sha256: 1c6c18ecec48d039b9a58e175337ceb1d2b55e3ffce9b03991f724add4b3ac86
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Practical Memory Move Routines

**Raw Source File**: `data/docs/codebase_c64_org/base/practical_memory_move_routines.md`
**SHA256**: `1c6c18ecec48d039b9a58e175337ceb1d2b55e3ffce9b03991f724add4b3ac86`

## Summary



# Practical Memory Move Routines

# Practical Memory Move Routines

by Bruce Clark

(Info file taken from [www.6502.org](http://www.6502.org))

Here are some reasonably fast general-purpose routines for moving blocks of memory. You simply specify the address to move from, the address to move to, and the size of the block. When SIZE is zero, no bytes are moved. SIZEL and SIZEH do not need to be consecutive memory locations, or even on the zero page for that matter. These routines only take one ...
