---
id: src-supercpu-sta
type: source
title: 'Source Summary: STA'
aliases:
- STA
- supercpu_sta.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/supercpu_sta.md
  sha256: a3f5823dd77cf320846a0c6c5279af2bc196607ecb8299cbd8d8cb536fcb8f40
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: STA

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_sta.md`
**SHA256**: `a3f5823dd77cf320846a0c6c5279af2bc196607ecb8299cbd8d8cb536fcb8f40`

## Summary



# STA

base:supercpu_sta

                # STA

```
    /*-------------------------------------------------------------------------
    OP CODE: STA (STore Accumulator to memory)
    ==========================================
    
    Addressing Modes:
        Absolute                         ($8d - 3 bytes, 4 cycles¹)
        Absolute Long                    ($8f - 4 bytes, 5 cycles¹)
        Direct Page (also DP)            ($85 - 2 bytes, 3 cycles¹²)
        DP Indirect                    ...
