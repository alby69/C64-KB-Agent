---
id: src-supercpu-sbc
type: source
title: 'Source Summary: SBC'
aliases:
- SBC
- supercpu_sbc.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/supercpu_sbc.md
  sha256: 977962623ae04d6552489ce573d1a2bd67baf5de6ee1bffef56176975bc55985
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: SBC

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_sbc.md`
**SHA256**: `977962623ae04d6552489ce573d1a2bd67baf5de6ee1bffef56176975bc55985`

## Summary



# SBC

base:supercpu_sbc

                # SBC

```
    /*-------------------------------------------------------------------------
    OP CODE: SBC (Subtract with Borrow from aCcumulator)
    ====================================================
    
    Addressing Modes:
        Immediate                        ($e9 - 2 bytes*, 2 cycles¹°)
        Absolute                         ($ed - 3 bytes, 4 cycles¹°)
        Absolute Long                    ($ef - 4 bytes, 5 cycles¹°)
        Direct P...
