---
id: src-supercpu-mvp
type: source
title: 'Source Summary: MVP'
aliases:
- MVP
- supercpu_mvp.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/supercpu_mvp.md
  sha256: 0e7b406b413e6a839069ca66a63a3e65a834ff085f4922f87dcd603ac4dd1848
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: MVP

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_mvp.md`
**SHA256**: `0e7b406b413e6a839069ca66a63a3e65a834ff085f4922f87dcd603ac4dd1848`

## Summary



# MVP

base:supercpu_mvp

                # MVP

```
    /*-------------------------------------------------------------------------
    OP CODE: MVP (block MoVe Previous)
    ==============================
    
    Addressing Modes:
        Block Move                        ($44 - 3 bytes, * cycles)
        * 7 Cycles per byte moved.
    Flags Affected:
        N/A
    Description:
        Moves (copies) a block of memory to a new location. The source,
        destination and length operands ...
