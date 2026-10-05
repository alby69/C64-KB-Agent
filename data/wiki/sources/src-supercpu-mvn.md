---
id: src-supercpu-mvn
type: source
title: 'Source Summary: MVN'
aliases:
- MVN
- supercpu_mvn.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/supercpu_mvn.md
  sha256: 56f9e340f0034bbf7456035d5d5124c1de14de928ebc9b78313fa7eb1393c13c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: MVN

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_mvn.md`
**SHA256**: `56f9e340f0034bbf7456035d5d5124c1de14de928ebc9b78313fa7eb1393c13c`

## Summary



# MVN

base:supercpu_mvn

                # MVN

```
    /*-------------------------------------------------------------------------
    OP CODE: MVN (block MoVe Next)
    ==============================
    
    Addressing Modes:
        Block Move                       ($54 - 3 bytes, * cycles)
        * 7 Cycles per byte moved.
    Flags Affected:
        N/A
    Description:
        Moves (copies) a block of memory to a new location. The source,
        destination and length operands of th...
