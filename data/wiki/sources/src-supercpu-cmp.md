---
id: src-supercpu-cmp
type: source
title: 'Source Summary: CMP'
aliases:
- CMP
- supercpu_cmp.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/supercpu_cmp.md
  sha256: 13919f6cf36be2f53ef7f17823ee6e826cd7098f73bee1f6f15cb48bea63e27e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: CMP

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_cmp.md`
**SHA256**: `13919f6cf36be2f53ef7f17823ee6e826cd7098f73bee1f6f15cb48bea63e27e`

## Summary



# CMP

base:supercpu_cmp

                # CMP

```
    //---------------------------------------------------------------------------------------------
    // PseudoCommand-OPC: CMP16 (CoMPare accumulator with memory)
    //
    // Addressing Modes:
    //   Immediate                               ($c9 - 2 bytes*, 2 cycles¹)
    //   Absolute                                ($cd - 3 bytes, 4 cycles¹)
    //   Absolute Long                           ($cf - 4 bytes, 5 cycles¹)
    //   Direct Pa...
