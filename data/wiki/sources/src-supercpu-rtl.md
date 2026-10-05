---
id: src-supercpu-rtl
type: source
title: 'Source Summary: RTL'
aliases:
- RTL
- supercpu_rtl.md
tags:
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/supercpu_rtl.md
  sha256: bb612e7a970395c980b4e44736f62706c41d29295fafeeb8a606688dc4a8f133
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: RTL

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_rtl.md`
**SHA256**: `bb612e7a970395c980b4e44736f62706c41d29295fafeeb8a606688dc4a8f133`

## Summary



# RTL

base:supercpu_rtl

                # RTL

```
    /*-------------------------------------------------------------------------
    OP CODE: RTL (ReTurn from subroutine Long)
    ==========================================
    
    Addressing Modes:
        Stack                            ($6b - 1 byte, 6 cycles)
    Flags Affected:
        N/A
    Description:
        Pull the program counter (incrementing the stacked, sixteen-bit value
        by one before loading the program counter w...
