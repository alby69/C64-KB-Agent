---
id: src-supercpu-txy
type: source
title: 'Source Summary: TXY'
aliases:
- TXY
- supercpu_txy.md
tags:
- general
sources:
- path: data/docs/codebase_c64_org/base/supercpu_txy.md
  sha256: 4c36a2eb532d7de94d7ac8f799f192036fe964f8abe7a9772da48df2957b10ba
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: TXY

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_txy.md`
**SHA256**: `4c36a2eb532d7de94d7ac8f799f192036fe964f8abe7a9772da48df2957b10ba`

## Summary



# TXY

base:supercpu_txy

                # TXY

```
    /*-------------------------------------------------------------------------
    OP CODE: TXY (Transfer index register X to Y)
    =============================================
    
    Addressing Modes:
        Implied                            ($9b - 1 byte, 2 cycles)
    Flags Affected:
        n - Set if most significant bit of transferred value is set; else
            cleared.
        z - Set if value transferred is zero; else clea...
